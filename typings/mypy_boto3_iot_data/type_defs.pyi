"""
Type annotations for iot-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iot_data.type_defs import DeleteThingShadowRequestRequestTypeDef

    data: DeleteThingShadowRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "DeleteThingShadowRequestRequestTypeDef",
    "DeleteThingShadowResponseTypeDef",
    "GetThingShadowRequestRequestTypeDef",
    "GetThingShadowResponseTypeDef",
    "ListNamedShadowsForThingRequestRequestTypeDef",
    "ListNamedShadowsForThingResponseTypeDef",
    "PublishRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "UpdateThingShadowRequestRequestTypeDef",
    "UpdateThingShadowResponseTypeDef",
)

_RequiredDeleteThingShadowRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteThingShadowRequestRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalDeleteThingShadowRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteThingShadowRequestRequestTypeDef",
    {
        "shadowName": str,
    },
    total=False,
)

class DeleteThingShadowRequestRequestTypeDef(
    _RequiredDeleteThingShadowRequestRequestTypeDef, _OptionalDeleteThingShadowRequestRequestTypeDef
):
    pass

DeleteThingShadowResponseTypeDef = TypedDict(
    "DeleteThingShadowResponseTypeDef",
    {
        "payload": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetThingShadowRequestRequestTypeDef = TypedDict(
    "_RequiredGetThingShadowRequestRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalGetThingShadowRequestRequestTypeDef = TypedDict(
    "_OptionalGetThingShadowRequestRequestTypeDef",
    {
        "shadowName": str,
    },
    total=False,
)

class GetThingShadowRequestRequestTypeDef(
    _RequiredGetThingShadowRequestRequestTypeDef, _OptionalGetThingShadowRequestRequestTypeDef
):
    pass

GetThingShadowResponseTypeDef = TypedDict(
    "GetThingShadowResponseTypeDef",
    {
        "payload": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListNamedShadowsForThingRequestRequestTypeDef = TypedDict(
    "_RequiredListNamedShadowsForThingRequestRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalListNamedShadowsForThingRequestRequestTypeDef = TypedDict(
    "_OptionalListNamedShadowsForThingRequestRequestTypeDef",
    {
        "nextToken": str,
        "pageSize": int,
    },
    total=False,
)

class ListNamedShadowsForThingRequestRequestTypeDef(
    _RequiredListNamedShadowsForThingRequestRequestTypeDef,
    _OptionalListNamedShadowsForThingRequestRequestTypeDef,
):
    pass

ListNamedShadowsForThingResponseTypeDef = TypedDict(
    "ListNamedShadowsForThingResponseTypeDef",
    {
        "results": List[str],
        "nextToken": str,
        "timestamp": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPublishRequestRequestTypeDef = TypedDict(
    "_RequiredPublishRequestRequestTypeDef",
    {
        "topic": str,
    },
)
_OptionalPublishRequestRequestTypeDef = TypedDict(
    "_OptionalPublishRequestRequestTypeDef",
    {
        "qos": int,
        "payload": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

class PublishRequestRequestTypeDef(
    _RequiredPublishRequestRequestTypeDef, _OptionalPublishRequestRequestTypeDef
):
    pass

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

_RequiredUpdateThingShadowRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateThingShadowRequestRequestTypeDef",
    {
        "thingName": str,
        "payload": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalUpdateThingShadowRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateThingShadowRequestRequestTypeDef",
    {
        "shadowName": str,
    },
    total=False,
)

class UpdateThingShadowRequestRequestTypeDef(
    _RequiredUpdateThingShadowRequestRequestTypeDef, _OptionalUpdateThingShadowRequestRequestTypeDef
):
    pass

UpdateThingShadowResponseTypeDef = TypedDict(
    "UpdateThingShadowResponseTypeDef",
    {
        "payload": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
