# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from cocotb.triggers import ClockCycles
from forastero.driver import BaseDriver

from .transaction import SignalState


class SignalDriver(BaseDriver):
    async def drive(self, transaction: SignalState):
        self.io.signal.value = transaction.value
        await ClockCycles(self.clk, transaction.cycles)
