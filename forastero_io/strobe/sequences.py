# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

import forastero
from forastero.driver import DriverEvent
from forastero.sequence import SeqContext, SeqProxy

from .requestor import StrobeDriver
from .transaction import StrobeEvent


@forastero.sequence(auto_lock=True)
@forastero.requires("req_drv", StrobeDriver)
async def strobe_seq(
    ctx: SeqContext,
    req_drv: SeqProxy[StrobeDriver],
    data,
    delay_range: tuple[int, int] = (1, 1),
) -> None:
    min_delay, max_delay = min(delay_range), max(delay_range)
    while True:
        await req_drv.enqueue(
            StrobeEvent(data=data, delay=ctx.random.randint(min_delay, max_delay)),
            wait_for=DriverEvent.POST_DRIVE,
        ).wait()
