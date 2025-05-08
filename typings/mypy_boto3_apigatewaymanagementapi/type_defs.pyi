"""
Type annotations for apigatewaymanagementapi service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_apigatewaymanagementapi.type_defs import BlobTypeDef

    data: BlobTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
else:
    from typing import Dict
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "BlobTypeDef",
    "DeleteConnectionRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetConnectionRequestTypeDef",
    "GetConnectionResponseTypeDef",
    "IdentityTypeDef",
    "PostToConnectionRequestTypeDef",
    "ResponseMetadataTypeDef",
)

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class DeleteConnectionRequestTypeDef(TypedDict):
    ConnectionId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GetConnectionRequestTypeDef(TypedDict):
    ConnectionId: str

class IdentityTypeDef(TypedDict):
    SourceIp: str
    UserAgent: str

class PostToConnectionRequestTypeDef(TypedDict):
    Data: BlobTypeDef
    ConnectionId: str

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectionResponseTypeDef(TypedDict):
    ConnectedAt: datetime
    Identity: IdentityTypeDef
    LastActiveAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef
