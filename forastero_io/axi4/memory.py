# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

import functools
from random import Random

from cocotb.utils import get_sim_time
from forastero.bench import BaseBench
from forastero.monitor import MonitorEvent

from .common import Burst
from .initiator import (
    AXI4ReadResponseInitiator,
    AXI4WriteResponseInitiator,
)
from .monitor import (
    AXI4ReadAddressMonitor,
    AXI4WriteAddressMonitor,
    AXI4WriteDataMonitor,
)
from .transaction import (
    AXI4ReadAddress,
    AXI4ReadResponse,
    AXI4WriteAddress,
    AXI4WriteData,
    AXI4WriteResponse,
)


class AXI4MemoryModel:
    def __init__(
        self,
        tb: BaseBench,
        awreq: AXI4WriteAddressMonitor,
        wreq: AXI4WriteDataMonitor,
        arreq: AXI4ReadAddressMonitor,
        brsp: AXI4WriteResponseInitiator,
        rrsp: AXI4ReadResponseInitiator,
        error_noninit: True,
        rand_noninit: True,
        response_delay: tuple[int, int] = (0, 0),
    ) -> None:
        # Hold references
        self.awreq = awreq
        self.wreq = wreq
        self.arreq = arreq
        self.brsp = brsp
        self.rrsp = rrsp
        self.error_noninit = error_noninit
        self.rand_noninit = rand_noninit
        self.response_delay = response_delay
        # Fork logging and random from testbench
        self.log = tb.fork_log("axi4lmem")
        self.random = Random(tb.random.random())
        # Calculate widths and masks
        self.bit_width = self.wreq.io.width("wdata")
        self.byte_width = (self.bit_width + 7) // 8
        self.mask = (1 << self.bit_width) - 1
        # Create memory
        self.memory = {}
        # Queues
        self.q_awreq: list[AXI4WriteAddress] = []
        self.q_wreq: list[AXI4WriteData] = []
        # Counter for how many wlasts are due for processing
        self.wlast_count = 0
        # Subscribe to events
        self.awreq.subscribe(MonitorEvent.CAPTURE, self._handle)
        self.wreq.subscribe(MonitorEvent.CAPTURE, self._handle)
        self.arreq.subscribe(MonitorEvent.CAPTURE, self._handle)

    @functools.lru_cache  # noqa: B019
    def _bit_strobe(self, byte_strobe: int) -> int:
        return sum(
            ((0xFF << (i * 8)) if ((byte_strobe >> i) & 0x1) else 0)
            for i in range(int(self.byte_width))
        )

    def read(self, address: int, check: bool = True) -> int:
        if address not in self.memory:
            if check and self.error_noninit:
                raise Exception(f"Read from uninitialised address: 0x{address:016X}")
            elif self.rand_noninit:
                self.memory[address] = self.random.getrandbits(self.bit_width)
            else:
                self.memory[address] = 0
        return self.memory[address]

    def write(self, address: int, data: int, strobe: int) -> None:
        current = self.read(address, check=False)
        bit_strobe = self._bit_strobe(strobe)
        if bit_strobe == self.mask:
            self.memory[address] = data
        else:
            value = (data & bit_strobe) | (current & (self.mask ^ bit_strobe))
            self.memory[address] = value

    def _handle(self, component, event, obj) -> None:
        # Queue AW/W requests, immediately respond to AR requests
        match obj:
            case AXI4WriteAddress():
                self.q_awreq.append(obj)
            case AXI4WriteData():
                self.q_wreq.append(obj)
                if obj.last:
                    self.wlast_count += 1
            case AXI4ReadAddress():
                # TODO: Implement wrapping logic
                if obj.burst != Burst.INCR:
                    raise NotImplementedError
                for i in range(obj.length + 1):
                    self.rrsp.enqueue(
                        AXI4ReadResponse(
                            axid=obj.axid,
                            data=self.read(obj.address + i),
                            last=True if (i == (obj.length - 1)) else False,
                            deliver_at_ns=get_sim_time(units="ns")
                            + self.random.randint(*self.response_delay),
                        )
                    )
        # Once a matching AW and W request are available, respond
        if self.q_awreq and (self.wlast_count > 0):
            awreq = self.q_awreq.pop(0)
            wreq = self.q_wreq.pop(0)
            self.wlast_count -= 1
            write_addr = awreq.address
            while True:
                # Commit write to the memory
                self.write(write_addr, wreq.data, wreq.strobe)
                # Calculate next address in the burst
                if awreq.burst == Burst.INCR:
                    write_addr += 8
                elif awreq.burst == Burst.WRAP:
                    # TODO: Implement wrapping logic
                    raise Exception("Model does not support wrapping bursts")
                elif awreq.burst == Burst.FIXED:
                    pass
                else:
                    raise Exception(f"Unsupported burst type {awreq.burst}")
                # Stop iterating once LAST is seen
                if wreq.last:
                    break
                # Otherwise, pop the next request
                wreq = self.q_wreq.pop(0)
            self.brsp.enqueue(
                AXI4WriteResponse(
                    deliver_at_ns=get_sim_time(units="ns")
                    + self.random.randint(*self.response_delay),
                )
            )
