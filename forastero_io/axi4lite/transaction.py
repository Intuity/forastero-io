# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from dataclasses import dataclass

from forastero import BaseTransaction

from ..axi4.common import Prot, Resp


@dataclass(kw_only=True)
class AXI4LiteWriteAddress(BaseTransaction):
    address: int = 0
    protection: Prot = Prot.DEFAULT
    valid: int = 1


@dataclass(kw_only=True)
class AXI4LiteWriteData(BaseTransaction):
    data: int = 0
    strobe: int = 0
    valid: int = 1


@dataclass(kw_only=True)
class AXI4LiteWriteResponse(BaseTransaction):
    response: Resp = Resp.OKAY
    valid: int = 1
    delay: int = 0
    deliver_at_ns: float | None = None


@dataclass(kw_only=True)
class AXI4LiteReadAddress(BaseTransaction):
    address: int = 0
    protection: Prot = Prot.DEFAULT
    valid: int = 1


@dataclass(kw_only=True)
class AXI4LiteReadResponse(BaseTransaction):
    data: int = 0
    response: Resp = Resp.OKAY
    valid: int = 1
    delay: int = 0
    deliver_at_ns: float | None = None


@dataclass(kw_only=True)
class AXI4LiteBackpressure(BaseTransaction):
    ready: bool = True
    cycles: int = 1
