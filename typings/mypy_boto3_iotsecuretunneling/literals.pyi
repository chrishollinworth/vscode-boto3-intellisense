"""
Type annotations for iotsecuretunneling service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/literals.html)

Usage::

    ```python
    from mypy_boto3_iotsecuretunneling.literals import ConnectionStatusType

    data: ConnectionStatusType = "CONNECTED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ConnectionStatusType", "TunnelStatusType")

ConnectionStatusType = Literal["CONNECTED", "DISCONNECTED"]
TunnelStatusType = Literal["CLOSED", "OPEN"]
