# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from cocotb.triggers import RisingEdge
from forastero.driver import BaseDriver

from .transaction import StreamDataValid


class StreamInitiatorDriver(BaseDriver):
    async def drive(self, transaction: StreamDataValid):
        # Setup the transaction
        self.io.set("id", transaction.id)
        self.io.set("data", transaction.data)
        self.io.set("valid", transaction.valid)
        if transaction.cycles == 0 and transaction.valid == 1:
            # Wait for transaction to be accepted
            while True:
                await RisingEdge(self.clk)
                if self.io.get("ready"):
                    break
        else:
            # Wait for the required number of cycles
            # If valid is set, then also check is ready signal is high
            for _ in range(transaction.cycles):
                await RisingEdge(self.clk)
        # Clear the valid
        self.io.set("valid", 0)
