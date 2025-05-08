"""
Type annotations for kinesis-video-webrtc-storage service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_webrtc_storage/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_kinesis_video_webrtc_storage.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
else:
    from typing import Dict
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "EmptyResponseMetadataTypeDef",
    "JoinStorageSessionAsViewerInputTypeDef",
    "JoinStorageSessionInputTypeDef",
    "ResponseMetadataTypeDef",
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class JoinStorageSessionAsViewerInputTypeDef(TypedDict):
    channelArn: str
    clientId: str

class JoinStorageSessionInputTypeDef(TypedDict):
    channelArn: str

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef
