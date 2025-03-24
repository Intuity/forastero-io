# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from .initiator import (
    AXI4LiteReadAddressInitiator,
    AXI4LiteReadResponseInitiator,
    AXI4LiteWriteAddressInitiator,
    AXI4LiteWriteDataInitiator,
    AXI4LiteWriteResponseInitiator,
)
from .io import (
    AXI4LiteReadAddressIO,
    AXI4LiteReadResponseIO,
    AXI4LiteWriteAddressIO,
    AXI4LiteWriteDataIO,
    AXI4LiteWriteResponseIO,
)
from .memory import AXI4LiteMemoryModel
from .monitor import (
    AXI4LiteReadAddressMonitor,
    AXI4LiteReadResponseMonitor,
    AXI4LiteWriteAddressMonitor,
    AXI4LiteWriteDataMonitor,
    AXI4LiteWriteResponseMonitor,
)
from .sequences import (
    axi4lite_ar_backpressure,
    axi4lite_aw_backpressure,
    axi4lite_b_backpressure,
    axi4lite_r_backpressure,
    axi4lite_read_seq,
    axi4lite_w_backpressure,
    axi4lite_write_seq,
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

# Guard
assert all(
    (
        AXI4LiteBackpressure,
        AXI4LiteMemoryModel,
        AXI4LiteReadAddress,
        AXI4LiteReadAddressInitiator,
        AXI4LiteReadAddressIO,
        AXI4LiteReadAddressMonitor,
        AXI4LiteReadAddressTarget,
        AXI4LiteReadResponse,
        AXI4LiteReadResponseInitiator,
        AXI4LiteReadResponseIO,
        AXI4LiteReadResponseMonitor,
        AXI4LiteReadResponseTarget,
        AXI4LiteWriteAddress,
        AXI4LiteWriteAddressInitiator,
        AXI4LiteWriteAddressIO,
        AXI4LiteWriteAddressMonitor,
        AXI4LiteWriteAddressTarget,
        AXI4LiteWriteData,
        AXI4LiteWriteDataInitiator,
        AXI4LiteWriteDataIO,
        AXI4LiteWriteDataMonitor,
        AXI4LiteWriteDataTarget,
        AXI4LiteWriteResponse,
        AXI4LiteWriteResponseInitiator,
        AXI4LiteWriteResponseIO,
        AXI4LiteWriteResponseMonitor,
        AXI4LiteWriteResponseTarget,
        axi4lite_aw_backpressure,
        axi4lite_w_backpressure,
        axi4lite_ar_backpressure,
        axi4lite_b_backpressure,
        axi4lite_r_backpressure,
        axi4lite_write_seq,
        axi4lite_read_seq,
    )
)
