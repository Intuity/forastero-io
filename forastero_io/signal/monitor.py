# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from cocotb.triggers import RisingEdge
from forastero.monitor import BaseMonitor

from .transaction import SignalState


class SignalMonitor(BaseMonitor):
    """
    Simple signal monitor

    :param cap_non_zero: When cap_non_zero = True, the monitor will to capture
                         for every rising edge of the clock where the signal is
                         not zero. When cap_non_zero = False, the monitor will
                         capture whenever the signal changes.
    """

    def __init__(self, *args, cap_non_zero=False, **kwds):
        super().__init__(*args, **kwds)
        self.cap_non_zero = cap_non_zero

    async def monitor(self, capture):
        last_state = int(self.io.signal.value)
        while True:
            await RisingEdge(self.clk)
            if self.rst.value == 1:
                await RisingEdge(self.clk)
                last_state = int(self.io.signal.value)
                continue
            curr_state = int(self.io.signal.value)
            if (self.cap_non_zero and curr_state != 0) or (
                not self.cap_non_zero and curr_state != last_state
            ):
                capture(SignalState(value=curr_state))
