"""
Main interface for apigatewaymanagementapi service type definitions.

Usage::

    ```python
    from mypy_boto3_apigatewaymanagementapi.type_defs import IdentityTypeDef

    data: IdentityTypeDef = {...}
    ```
"""
import sys
from datetime import datetime

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("IdentityTypeDef", "GetConnectionResponseTypeDef")

IdentityTypeDef = TypedDict("IdentityTypeDef", {"SourceIp": str, "UserAgent": str})

GetConnectionResponseTypeDef = TypedDict(
    "GetConnectionResponseTypeDef",
    {"ConnectedAt": datetime, "Identity": "IdentityTypeDef", "LastActiveAt": datetime},
    total=False,
)
