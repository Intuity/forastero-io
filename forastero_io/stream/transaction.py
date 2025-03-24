# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from dataclasses import dataclass

from forastero import BaseTransaction


@dataclass(kw_only=True)
class StreamBackpressure(BaseTransaction):
    ready: bool = True
    cycles: int = 1


@dataclass(kw_only=True)
class StreamDataValid(BaseTransaction):
    id: int | None = None
    data: int = 0xDEADBEEF
    valid: bool = True
    cycles: int = 0
