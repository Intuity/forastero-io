# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from cocotb.handle import HierarchyObject
from forastero.io import BaseIO, IORole


class SignalIO(BaseIO):
    def __init__(self, signal: HierarchyObject, role: IORole):
        self.signal = signal
        self._role = role

    def initialise(self, _role: IORole):
        if self._role == IORole.INITIATOR:
            self.signal.value = 0
