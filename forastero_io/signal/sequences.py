# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

import forastero
from forastero.driver import DriverEvent
from forastero.sequence import SeqContext, SeqProxy

from .driver import SignalDriver
from .transaction import SignalState


@forastero.sequence(auto_lock=True)
@forastero.requires("driver", SignalDriver)
async def random_signal_seq(
    ctx: SeqContext,
    driver: SeqProxy[SignalDriver],
    min_interval: int = 1,
    max_interval: int = 10,
    probability: float = 0.5,
):
    while True:
        driver.enqueue(
            SignalState(
                value=ctx.random.choices(
                    (True, False), weights=(probability, 1.0 - probability), k=1
                )[0],
                cycles=ctx.random.randint(min_interval, max_interval),
            )
        )
        await driver.wait_for(DriverEvent.PRE_DRIVE)
