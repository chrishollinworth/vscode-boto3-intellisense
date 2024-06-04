"""
Type annotations for networkmonitor service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/literals.html)

Usage::

    ```python
    from mypy_boto3_networkmonitor.literals import AddressFamilyType

    data: AddressFamilyType = "IPV4"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AddressFamilyType",
    "ListMonitorsPaginatorName",
    "MonitorStateType",
    "ProbeStateType",
    "ProtocolType",
)

AddressFamilyType = Literal["IPV4", "IPV6"]
ListMonitorsPaginatorName = Literal["list_monitors"]
MonitorStateType = Literal["ACTIVE", "DELETING", "ERROR", "INACTIVE", "PENDING"]
ProbeStateType = Literal["ACTIVE", "DELETED", "DELETING", "ERROR", "INACTIVE", "PENDING"]
ProtocolType = Literal["ICMP", "TCP"]
