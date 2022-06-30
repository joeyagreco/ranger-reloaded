from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Device:
    ipAddress: str
    openPorts: list[str] = field(default_factory=lambda: list())
