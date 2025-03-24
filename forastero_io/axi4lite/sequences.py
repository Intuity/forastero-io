# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

import forastero
from forastero.driver import BaseDriver, DriverEvent, MonitorEvent
from forastero.sequence import SeqContext, SeqProxy

from .initiator import (
    AXI4LiteReadAddressInitiator,
    AXI4LiteWriteAddressInitiator,
    AXI4LiteWriteDataInitiator,
)
from .monitor import (
    AXI4LiteReadResponseMonitor,
    AXI4LiteWriteResponseMonitor,
)
from .target import (
    AXI4LiteReadAddressTarget,
    AXI4LiteReadResponseTarget,
    AXI4LiteWriteAddressTarget,
    AXI4LiteWriteDataTarget,
    AXI4LiteWriteResponseTarget,
)
from .transaction import (
    AXI4LiteBackpressure,
    AXI4LiteReadAddress,
    AXI4LiteReadResponse,
    AXI4LiteWriteAddress,
    AXI4LiteWriteData,
    AXI4LiteWriteResponse,
)


async def axi4lite_backpressure(
    ctx: SeqContext,
    driver: SeqProxy[BaseDriver],
    min_interval: int = 1,
    max_interval: int = 10,
    backpressure: float = 0.5,
):
    """
    Generate random backpressure using the READY signal of an AXI4 interface,
    with options to tune how often backpressure is applied.

    :param min_interval: Shortest time to hold ready constant
    :param max_interval: Longest time to hold ready constant
    :param backpressure: Weighting proportion for how often ready should be low,
                         i.e. values approaching 1 mean always backpressure,
                         while values approaching 0 mean never backpressure
    """
    while True:
        driver.enqueue(
            AXI4LiteBackpressure(
                ready=ctx.random.choices(
                    (True, False), weights=(1.0 - backpressure, backpressure), k=1
                )[0],
                cycles=ctx.random.randint(min_interval, max_interval),
            )
        )
        await driver.wait_for(DriverEvent.PRE_DRIVE)


@forastero.sequence(auto_lock=True)
@forastero.requires("driver", AXI4LiteWriteAddressTarget)
async def axi4lite_aw_backpressure(
    ctx: SeqContext,
    driver: SeqProxy[AXI4LiteWriteAddressTarget],
    min_interval: int = 1,
    max_interval: int = 10,
    backpressure: float = 0.5,
):
    """
    Generate random backpressure using the READY signal of an AXI4 interface,
    with options to tune how often backpressure is applied.

    :param min_interval: Shortest time to hold ready constant
    :param max_interval: Longest time to hold ready constant
    :param backpressure: Weighting proportion for how often ready should be low,
                         i.e. values approaching 1 mean always backpressure,
                         while values approaching 0 mean never backpressure
    """
    await axi4lite_backpressure(ctx, driver, min_interval, max_interval, backpressure)


@forastero.sequence(auto_lock=True)
@forastero.requires("driver", AXI4LiteWriteDataTarget)
async def axi4lite_w_backpressure(
    ctx: SeqContext,
    driver: SeqProxy[AXI4LiteWriteDataTarget],
    min_interval: int = 1,
    max_interval: int = 10,
    backpressure: float = 0.5,
):
    """
    Generate random backpressure using the READY signal of an AXI4 interface,
    with options to tune how often backpressure is applied.

    :param min_interval: Shortest time to hold ready constant
    :param max_interval: Longest time to hold ready constant
    :param backpressure: Weighting proportion for how often ready should be low,
                         i.e. values approaching 1 mean always backpressure,
                         while values approaching 0 mean never backpressure
    """
    await axi4lite_backpressure(ctx, driver, min_interval, max_interval, backpressure)


@forastero.sequence(auto_lock=True)
@forastero.requires("driver", AXI4LiteReadAddressTarget)
async def axi4lite_ar_backpressure(
    ctx: SeqContext,
    driver: SeqProxy[AXI4LiteReadAddressTarget],
    min_interval: int = 1,
    max_interval: int = 10,
    backpressure: float = 0.5,
):
    """
    Generate random backpressure using the READY signal of an AXI4 interface,
    with options to tune how often backpressure is applied.

    :param min_interval: Shortest time to hold ready constant
    :param max_interval: Longest time to hold ready constant
    :param backpressure: Weighting proportion for how often ready should be low,
                         i.e. values approaching 1 mean always backpressure,
                         while values approaching 0 mean never backpressure
    """
    await axi4lite_backpressure(ctx, driver, min_interval, max_interval, backpressure)


@forastero.sequence(auto_lock=True)
@forastero.requires("driver", AXI4LiteWriteResponseTarget)
async def axi4lite_b_backpressure(
    ctx: SeqContext,
    driver: SeqProxy[AXI4LiteWriteResponseTarget],
    min_interval: int = 1,
    max_interval: int = 10,
    backpressure: float = 0.5,
):
    """
    Generate random backpressure using the READY signal of an AXI4 interface,
    with options to tune how often backpressure is applied.

    :param min_interval: Shortest time to hold ready constant
    :param max_interval: Longest time to hold ready constant
    :param backpressure: Weighting proportion for how often ready should be low,
                         i.e. values approaching 1 mean always backpressure,
                         while values approaching 0 mean never backpressure
    """
    await axi4lite_backpressure(ctx, driver, min_interval, max_interval, backpressure)


@forastero.sequence(auto_lock=True)
@forastero.requires("driver", AXI4LiteReadResponseTarget)
async def axi4lite_r_backpressure(
    ctx: SeqContext,
    driver: SeqProxy[AXI4LiteReadResponseTarget],
    min_interval: int = 1,
    max_interval: int = 10,
    backpressure: float = 0.5,
):
    """
    Generate random backpressure using the READY signal of an AXI4 interface,
    with options to tune how often backpressure is applied.

    :param min_interval: Shortest time to hold ready constant
    :param max_interval: Longest time to hold ready constant
    :param backpressure: Weighting proportion for how often ready should be low,
                         i.e. values approaching 1 mean always backpressure,
                         while values approaching 0 mean never backpressure
    """
    await axi4lite_backpressure(ctx, driver, min_interval, max_interval, backpressure)


@forastero.sequence(auto_lock=True)
@forastero.requires("aw_drv", AXI4LiteWriteAddressInitiator)
@forastero.requires("w_drv", AXI4LiteWriteDataInitiator)
@forastero.requires("b_mon", AXI4LiteWriteResponseMonitor)
async def axi4lite_write_seq(
    ctx: SeqContext,
    aw_drv: SeqProxy[AXI4LiteWriteAddressInitiator],
    w_drv: SeqProxy[AXI4LiteWriteDataInitiator],
    b_mon: SeqProxy[AXI4LiteWriteResponseMonitor],
    address: int,
    data: int,
    strobe: int,
    buffer: list[AXI4LiteWriteResponse] | None = None,
) -> AXI4LiteWriteResponse:
    """
    Perform a write to an AXI4-Lite endpoint, sequencing both address and data
    requests and returning the captured response.

    :param address: Address to write
    :param data:    Data to write
    """
    evt_aw = aw_drv.enqueue(
        AXI4LiteWriteAddress(address=address), wait_for=DriverEvent.POST_DRIVE
    )
    evt_w = w_drv.enqueue(
        AXI4LiteWriteData(data=data, strobe=strobe), wait_for=DriverEvent.POST_DRIVE
    )
    await evt_aw.wait()
    await evt_w.wait()
    rsp = await b_mon.wait_for(MonitorEvent.CAPTURE)
    if isinstance(buffer, list):
        buffer.append(rsp)
    return rsp


@forastero.sequence(auto_lock=True)
@forastero.requires("ar_drv", AXI4LiteReadAddressInitiator)
@forastero.requires("r_mon", AXI4LiteReadResponseMonitor)
async def axi4lite_read_seq(
    ctx: SeqContext,
    ar_drv: SeqProxy[AXI4LiteReadAddressInitiator],
    r_mon: SeqProxy[AXI4LiteReadResponseMonitor],
    address: int,
    buffer: list[AXI4LiteReadResponse],
) -> AXI4LiteReadResponse:
    """
    Perform a read to an AXI4-Lite endpoint, sequencing the address request and
    returning the captured response.

    :param address: Address to read
    :param buffer:  Buffer to read into
    """
    await ar_drv.enqueue(
        AXI4LiteReadAddress(address=address), wait_for=DriverEvent.POST_DRIVE
    ).wait()
    buffer.append(await r_mon.wait_for(MonitorEvent.CAPTURE))
