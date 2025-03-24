# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from .initiator import (
    AXI4ReadAddressInitiator,
    AXI4ReadResponseInitiator,
    AXI4WriteAddressInitiator,
    AXI4WriteDataInitiator,
    AXI4WriteResponseInitiator,
)
from .io import (
    AXI4ReadAddressIO,
    AXI4ReadResponseIO,
    AXI4WriteAddressIO,
    AXI4WriteDataIO,
    AXI4WriteResponseIO,
)
from .memory import AXI4MemoryModel
from .monitor import (
    AXI4ReadAddressMonitor,
    AXI4ReadResponseMonitor,
    AXI4WriteAddressMonitor,
    AXI4WriteDataMonitor,
    AXI4WriteResponseMonitor,
)
from .sequences import (
    axi4_ar_backpressure,
    axi4_aw_backpressure,
    axi4_b_backpressure,
    axi4_r_backpressure,
    axi4_w_backpressure,
)
from .target import (
    AXI4ReadAddressTarget,
    AXI4ReadResponseTarget,
    AXI4WriteAddressTarget,
    AXI4WriteDataTarget,
    AXI4WriteResponseTarget,
)
from .transaction import (
    AXI4Backpressure,
    AXI4ReadAddress,
    AXI4ReadResponse,
    AXI4WriteAddress,
    AXI4WriteData,
    AXI4WriteResponse,
)

# Guard
assert all(
    (
        AXI4WriteAddressInitiator,
        AXI4WriteDataInitiator,
        AXI4ReadAddressInitiator,
        AXI4WriteResponseInitiator,
        AXI4ReadResponseInitiator,
        AXI4WriteAddressIO,
        AXI4WriteDataIO,
        AXI4WriteResponseIO,
        AXI4ReadAddressIO,
        AXI4ReadResponseIO,
        AXI4WriteAddressMonitor,
        AXI4WriteDataMonitor,
        AXI4WriteResponseMonitor,
        AXI4ReadAddressMonitor,
        AXI4ReadResponseMonitor,
        AXI4WriteAddressTarget,
        AXI4WriteDataTarget,
        AXI4WriteResponseTarget,
        AXI4ReadAddressTarget,
        AXI4ReadResponseTarget,
        AXI4WriteAddress,
        AXI4WriteData,
        AXI4WriteResponse,
        AXI4ReadAddress,
        AXI4ReadResponse,
        AXI4Backpressure,
        AXI4MemoryModel,
        axi4_aw_backpressure,
        axi4_w_backpressure,
        axi4_ar_backpressure,
        axi4_b_backpressure,
        axi4_r_backpressure,
    )
)
