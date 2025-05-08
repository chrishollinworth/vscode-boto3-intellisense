"""
Type annotations for kinesis-video-media service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_media/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_kinesis_video_media.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from botocore.response import StreamingBody

from .literals import StartSelectorTypeType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
else:
    from typing import Dict
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "GetMediaInputTypeDef",
    "GetMediaOutputTypeDef",
    "ResponseMetadataTypeDef",
    "StartSelectorTypeDef",
    "TimestampTypeDef",
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class GetMediaOutputTypeDef(TypedDict):
    ContentType: str
    Payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class StartSelectorTypeDef(TypedDict):
    StartSelectorType: StartSelectorTypeType
    AfterFragmentNumber: NotRequired[str]
    StartTimestamp: NotRequired[TimestampTypeDef]
    ContinuationToken: NotRequired[str]

class GetMediaInputTypeDef(TypedDict):
    StartSelector: StartSelectorTypeDef
    StreamName: NotRequired[str]
    StreamARN: NotRequired[str]
