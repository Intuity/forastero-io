# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from dataclasses import dataclass

from forastero import BaseTransaction

from .common import Arcache, Awcache, Burst, Prot, Resp, Size


@dataclass(kw_only=True)
class AXI4WriteAddress(BaseTransaction):
    axid: int = 0
    address: int = 0
    length: int = 0
    size: Size = Size.B1
    burst: Burst = Burst.FIXED
    cache: Awcache = Awcache.DEV_NON_BUF
    protection: Prot = Prot.DEFAULT
    qos: int = 0
    region: int = 0
    user: int = 0
    valid: int = 1


@dataclass(kw_only=True)
class AXI4WriteData(BaseTransaction):
    index: int = 0
    data: int = 0
    strobe: int = 0
    last: bool = False
    user: int = 0
    valid: int = 1


@dataclass(kw_only=True)
class AXI4WriteResponse(BaseTransaction):
    axid: int = 0
    response: Resp = Resp.OKAY
    user: int = 0
    valid: int = 1
    deliver_at_ns: float | None = None


@dataclass(kw_only=True)
class AXI4ReadAddress(BaseTransaction):
    axid: int = 0
    address: int = 0
    length: int = 0
    size: Size = Size.B1
    burst: Burst = Burst.FIXED
    cache: Arcache = Arcache.DEV_NON_BUF
    protection: Prot = Prot.DEFAULT
    qos: int = 0
    region: int = 0
    user: int = 0
    valid: int = 1


@dataclass(kw_only=True)
class AXI4ReadResponse(BaseTransaction):
    axid: int = 0
    index: int = 0
    data: int = 0
    response: Resp = Resp.OKAY
    last: bool = False
    user: int = 0
    valid: int = 1
    deliver_at_ns: float | None = None


@dataclass(kw_only=True)
class AXI4Backpressure(BaseTransaction):
    ready: bool = True
    cycles: int = 1
