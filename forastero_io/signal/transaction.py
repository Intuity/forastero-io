# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from dataclasses import dataclass

from forastero import BaseTransaction


@dataclass(kw_only=True)
class SignalState(BaseTransaction):
    value: int = 0
    cycles: int = 1
