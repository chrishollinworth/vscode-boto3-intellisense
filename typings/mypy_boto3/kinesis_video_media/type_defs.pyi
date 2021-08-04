"""
Type annotations for kinesis-video-media service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_media/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesis_video_media.type_defs import GetMediaInputRequestTypeDef

    data: GetMediaInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, Union

from botocore.response import StreamingBody

from .literals import StartSelectorTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "GetMediaInputRequestTypeDef",
    "GetMediaOutputTypeDef",
    "ResponseMetadataTypeDef",
    "StartSelectorTypeDef",
)

_RequiredGetMediaInputRequestTypeDef = TypedDict(
    "_RequiredGetMediaInputRequestTypeDef",
    {
        "StartSelector": "StartSelectorTypeDef",
    },
)
_OptionalGetMediaInputRequestTypeDef = TypedDict(
    "_OptionalGetMediaInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class GetMediaInputRequestTypeDef(
    _RequiredGetMediaInputRequestTypeDef, _OptionalGetMediaInputRequestTypeDef
):
    pass

GetMediaOutputTypeDef = TypedDict(
    "GetMediaOutputTypeDef",
    {
        "ContentType": str,
        "Payload": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

_RequiredStartSelectorTypeDef = TypedDict(
    "_RequiredStartSelectorTypeDef",
    {
        "StartSelectorType": StartSelectorTypeType,
    },
)
_OptionalStartSelectorTypeDef = TypedDict(
    "_OptionalStartSelectorTypeDef",
    {
        "AfterFragmentNumber": str,
        "StartTimestamp": Union[datetime, str],
        "ContinuationToken": str,
    },
    total=False,
)

class StartSelectorTypeDef(_RequiredStartSelectorTypeDef, _OptionalStartSelectorTypeDef):
    pass
