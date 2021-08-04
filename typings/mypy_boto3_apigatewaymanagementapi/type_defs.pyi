"""
Type annotations for apigatewaymanagementapi service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/type_defs.html)

Usage::

    ```python
    from mypy_boto3_apigatewaymanagementapi.type_defs import DeleteConnectionRequestRequestTypeDef

    data: DeleteConnectionRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, Union

from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "DeleteConnectionRequestRequestTypeDef",
    "GetConnectionRequestRequestTypeDef",
    "GetConnectionResponseTypeDef",
    "IdentityTypeDef",
    "PostToConnectionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
)

DeleteConnectionRequestRequestTypeDef = TypedDict(
    "DeleteConnectionRequestRequestTypeDef",
    {
        "ConnectionId": str,
    },
)

GetConnectionRequestRequestTypeDef = TypedDict(
    "GetConnectionRequestRequestTypeDef",
    {
        "ConnectionId": str,
    },
)

GetConnectionResponseTypeDef = TypedDict(
    "GetConnectionResponseTypeDef",
    {
        "ConnectedAt": datetime,
        "Identity": "IdentityTypeDef",
        "LastActiveAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "SourceIp": str,
        "UserAgent": str,
    },
)

PostToConnectionRequestRequestTypeDef = TypedDict(
    "PostToConnectionRequestRequestTypeDef",
    {
        "Data": Union[bytes, IO[bytes], StreamingBody],
        "ConnectionId": str,
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)
