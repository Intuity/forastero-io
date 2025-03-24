# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from cocotb.triggers import ClockCycles, RisingEdge
from forastero.driver import BaseDriver
from forastero.monitor import BaseMonitor

from .transaction import StreamBackpressure, StreamDataValid


class StreamResponderDriver(BaseDriver):
    async def drive(self, transaction: StreamBackpressure):
        # Setup the transaction
        self.io.set("ready", transaction.ready)
        # Wait for the required number of cycles
        await ClockCycles(self.clk, transaction.cycles)


class StreamResponderMonitor(BaseMonitor):
    async def monitor(self, capture):
        while True:
            await RisingEdge(self.clk)
            if self.rst.value == 1:
                continue
            if self.io.get("valid") and self.io.get("ready"):
                capture(
                    StreamDataValid(
                        id=self.io.get("id", None),
                        data=self.io.get("data"),
                        valid=1,
                    )
                )
