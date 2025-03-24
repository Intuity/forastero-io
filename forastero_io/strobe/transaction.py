# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from dataclasses import dataclass

from forastero import BaseTransaction


@dataclass(kw_only=True)
class StrobeEvent(BaseTransaction):
    data: int = 0
    strobe: bool = True
