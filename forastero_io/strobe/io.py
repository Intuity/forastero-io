# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from collections.abc import Callable

from cocotb.handle import HierarchyObject
from forastero.io import BaseIO, IORole


class StrobeIO(BaseIO):
    def __init__(
        self,
        dut: HierarchyObject,
        name: str,
        role: IORole,
        io_style: Callable[[str | None, str, IORole, IORole], str] | None = None,
    ):
        super().__init__(dut, name, role, ["data", "strobe"], [], io_style=io_style)
