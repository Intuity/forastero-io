# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from cocotb.triggers import ClockCycles, RisingEdge
from cocotb.utils import get_sim_time
from forastero.driver import BaseDriver

from .transaction import (
    AXI4ReadAddress,
    AXI4ReadResponse,
    AXI4WriteAddress,
    AXI4WriteData,
    AXI4WriteResponse,
)


class AXI4WriteAddressInitiator(BaseDriver):
    async def drive(self, transaction: AXI4WriteAddress):
        self.io.set("awid", transaction.axid)
        self.io.set("awaddr", transaction.address)
        self.io.set("awlen", transaction.length)
        self.io.set("awsize", int(transaction.size))
        self.io.set("awburst", int(transaction.burst))
        self.io.set("awcache", int(transaction.cache))
        self.io.set("awprot", int(transaction.protection))
        self.io.set("awqos", int(transaction.qos))
        self.io.set("awregion", int(transaction.region))
        self.io.set("awuser", int(transaction.user))
        self.io.set("awvalid", int(transaction.valid))
        if transaction.valid:
            while True:
                await RisingEdge(self.clk)
                if self.io.get("awready"):
                    break
            self.io.set("awvalid", 0)
        else:
            await RisingEdge(self.clk)


class AXI4WriteDataInitiator(BaseDriver):
    async def drive(self, transaction: AXI4WriteData):
        self.io.set("wdata", transaction.data)
        self.io.set("wstrb", transaction.strobe)
        self.io.set("wlast", transaction.last)
        self.io.set("wuser", transaction.user)
        self.io.set("wvalid", transaction.valid)
        if transaction.valid:
            while True:
                await RisingEdge(self.clk)
                if self.io.get("wready"):
                    break
            self.io.set("wvalid", 0)
        else:
            await RisingEdge(self.clk)


class AXI4ReadAddressInitiator(BaseDriver):
    async def drive(self, transaction: AXI4ReadAddress):
        self.io.set("arid", transaction.axid)
        self.io.set("araddr", transaction.address)
        self.io.set("arlen", transaction.length)
        self.io.set("arsize", int(transaction.size))
        self.io.set("arburst", int(transaction.burst))
        self.io.set("arcache", int(transaction.cache))
        self.io.set("arprot", int(transaction.protection))
        self.io.set("arqos", int(transaction.qos))
        self.io.set("arregion", int(transaction.region))
        self.io.set("aruser", int(transaction.user))
        self.io.set("arvalid", int(transaction.valid))
        if transaction.valid:
            while True:
                await RisingEdge(self.clk)
                if self.io.get("arready"):
                    break
            self.io.set("arvalid", 0)
        else:
            await RisingEdge(self.clk)


class AXI4WriteResponseInitiator(BaseDriver):
    async def drive(self, transaction: AXI4WriteResponse):
        self.io.set("bid", transaction.axid)
        self.io.set("bresp", int(transaction.response))
        self.io.set("buser", transaction.user)
        self.io.set("bvalid", transaction.valid)
        if transaction.valid:
            while True:
                await RisingEdge(self.clk)
                if self.io.get("bready"):
                    break
            self.io.set("bvalid", 0)
        else:
            await RisingEdge(self.clk)


class AXI4ReadResponseInitiator(BaseDriver):
    async def drive(self, transaction: AXI4ReadResponse):
        if transaction.delay > 0:
            await ClockCycles(self.clk, transaction.delay)
        if transaction.deliver_at_ns is not None:
            while get_sim_time(units="ns") < transaction.deliver_at_ns:
                await RisingEdge(self.clk)
        self.io.set("rid", transaction.axid)
        self.io.set("rdata", transaction.data)
        self.io.set("rresp", int(transaction.response))
        self.io.set("rlast", transaction.last)
        self.io.set("ruser", transaction.user)
        self.io.set("rvalid", transaction.valid)
        if transaction.valid:
            while True:
                await RisingEdge(self.clk)
                if self.io.get("rready"):
                    break
            self.io.set("rlast", 0)
            self.io.set("rvalid", 0)
        else:
            await RisingEdge(self.clk)
