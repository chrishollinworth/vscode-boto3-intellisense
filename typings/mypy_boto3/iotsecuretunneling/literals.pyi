"""
Type annotations for iotsecuretunneling service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/literals.html)

Usage::

    ```python
    from mypy_boto3_iotsecuretunneling.literals import ClientModeType

    data: ClientModeType = "ALL"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ClientModeType", "ConnectionStatusType", "TunnelStatusType")

ClientModeType = Literal["ALL", "DESTINATION", "SOURCE"]
ConnectionStatusType = Literal["CONNECTED", "DISCONNECTED"]
TunnelStatusType = Literal["CLOSED", "OPEN"]
