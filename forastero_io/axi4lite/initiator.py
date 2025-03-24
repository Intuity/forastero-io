# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from cocotb.triggers import ClockCycles, RisingEdge
from cocotb.utils import get_sim_time
from forastero.driver import BaseDriver

from .transaction import (
    AXI4LiteReadAddress,
    AXI4LiteReadResponse,
    AXI4LiteWriteAddress,
    AXI4LiteWriteData,
    AXI4LiteWriteResponse,
)


class AXI4LiteWriteAddressInitiator(BaseDriver):
    async def drive(self, transaction: AXI4LiteWriteAddress):
        self.io.set("awaddr", transaction.address)
        self.io.set("awprot", int(transaction.protection))
        self.io.set("awvalid", int(transaction.valid))
        if transaction.valid:
            while True:
                await RisingEdge(self.clk)
                if self.io.get("awready"):
                    break
            self.io.set("awvalid", 0)
        else:
            await RisingEdge(self.clk)


class AXI4LiteWriteDataInitiator(BaseDriver):
    async def drive(self, transaction: AXI4LiteWriteData):
        self.io.set("wdata", transaction.data)
        self.io.set("wstrb", transaction.strobe)
        self.io.set("wvalid", transaction.valid)
        if transaction.valid:
            while True:
                await RisingEdge(self.clk)
                if self.io.get("wready"):
                    break
            self.io.set("wvalid", 0)
        else:
            await RisingEdge(self.clk)


class AXI4LiteReadAddressInitiator(BaseDriver):
    async def drive(self, transaction: AXI4LiteReadAddress):
        self.io.set("araddr", transaction.address)
        self.io.set("arprot", int(transaction.protection))
        self.io.set("arvalid", int(transaction.valid))
        if transaction.valid:
            while True:
                await RisingEdge(self.clk)
                if self.io.get("arready"):
                    break
            self.io.set("arvalid", 0)
        else:
            await RisingEdge(self.clk)


class AXI4LiteWriteResponseInitiator(BaseDriver):
    async def drive(self, transaction: AXI4LiteWriteResponse):
        if transaction.delay > 0:
            await ClockCycles(self.clk, transaction.delay)
        if transaction.deliver_at_ns is not None:
            while get_sim_time(units="ns") < transaction.deliver_at_ns:
                await RisingEdge(self.clk)
        self.io.set("bresp", int(transaction.response))
        self.io.set("bvalid", transaction.valid)
        if transaction.valid:
            while True:
                await RisingEdge(self.clk)
                if self.io.get("bready"):
                    break
            self.io.set("bvalid", 0)
        else:
            await RisingEdge(self.clk)


class AXI4LiteReadResponseInitiator(BaseDriver):
    async def drive(self, transaction: AXI4LiteReadResponse):
        if transaction.delay > 0:
            await ClockCycles(self.clk, transaction.delay)
        if transaction.deliver_at_ns is not None:
            while get_sim_time(units="ns") < transaction.deliver_at_ns:
                await RisingEdge(self.clk)
        self.io.set("rdata", transaction.data)
        self.io.set("rresp", int(transaction.response))
        self.io.set("rvalid", transaction.valid)
        if transaction.valid:
            while True:
                await RisingEdge(self.clk)
                if self.io.get("rready"):
                    break
            self.io.set("rvalid", 0)
        else:
            await RisingEdge(self.clk)
