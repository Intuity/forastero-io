# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from cocotb.triggers import RisingEdge
from forastero.driver import BaseDriver
from forastero.monitor import BaseMonitor

from .transaction import StrobeEvent


class StrobeDriver(BaseDriver):
    async def drive(self, transaction: StrobeEvent):
        # Setup the transaction
        self.io.set("data", transaction.data)
        self.io.set("strobe", transaction.strobe)
        # Wait one cycle for setup
        await RisingEdge(self.clk)
        # Clear the request
        self.io.set("strobe", 0)


class StrobeMonitor(BaseMonitor):
    async def monitor(self, capture):
        while True:
            await RisingEdge(self.clk)
            if self.rst.value == 1:
                continue
            if self.io.get("strobe"):
                capture(StrobeEvent(data=self.io.get("data"), strobe=True))
