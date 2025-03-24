# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

import forastero
from cocotb.triggers import ClockCycles
from forastero.driver import DriverEvent
from forastero.sequence import SeqContext, SeqProxy

from .initiator import StreamInitiatorDriver
from .responder import StreamResponderDriver
from .transaction import StreamBackpressure, StreamDataValid


@forastero.sequence()
@forastero.requires("driver", StreamInitiatorDriver)
async def stream_data_seq(
    ctx: SeqContext,
    driver: SeqProxy[StreamInitiatorDriver],
    data: list[int],
    min_delay: int = 1,
    max_delay: int = 10,
    delay_chance: float = 0.5,
):
    for entry in data:
        if ctx.random.choices(
            (True, False), weights=(1.0 - delay_chance, delay_chance), k=1
        )[0]:
            await ClockCycles(ctx.clk, ctx.random.randint(min_delay, max_delay))
        async with ctx.lock(driver):
            await driver.enqueue(
                StreamDataValid(data=entry), wait_for=DriverEvent.PRE_DRIVE
            ).wait()


@forastero.sequence()
@forastero.requires("driver", StreamResponderDriver)
async def stream_backpressure_seq(
    ctx: SeqContext,
    driver: SeqProxy[StreamResponderDriver],
    min_interval: int = 1,
    max_interval: int = 10,
    weights: list[int] | None = None,
    backpressure: float = 0.5,
):
    weights = weights or [1 for _ in range(min_interval, max_interval + 1)]
    while True:
        async with ctx.lock(driver):
            driver.enqueue(
                StreamBackpressure(
                    ready=ctx.random.choices(
                        (True, False), weights=(1.0 - backpressure, backpressure), k=1
                    )[0],
                    cycles=ctx.random.choices(
                        range(min_interval, max_interval + 1),
                        weights=weights,
                        k=1,
                    )[0],
                )
            )
        await driver.wait_for(DriverEvent.PRE_DRIVE)
