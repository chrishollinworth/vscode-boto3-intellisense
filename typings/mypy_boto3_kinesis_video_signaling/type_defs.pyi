"""
Type annotations for kinesis-video-signaling service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_signaling/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_kinesis_video_signaling.type_defs import GetIceServerConfigRequestTypeDef

    data: GetIceServerConfigRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
else:
    from typing import Dict, List
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "GetIceServerConfigRequestTypeDef",
    "GetIceServerConfigResponseTypeDef",
    "IceServerTypeDef",
    "ResponseMetadataTypeDef",
    "SendAlexaOfferToMasterRequestTypeDef",
    "SendAlexaOfferToMasterResponseTypeDef",
)

class GetIceServerConfigRequestTypeDef(TypedDict):
    ChannelARN: str
    ClientId: NotRequired[str]
    Service: NotRequired[Literal["TURN"]]
    Username: NotRequired[str]

class IceServerTypeDef(TypedDict):
    Uris: NotRequired[List[str]]
    Username: NotRequired[str]
    Password: NotRequired[str]
    Ttl: NotRequired[int]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class SendAlexaOfferToMasterRequestTypeDef(TypedDict):
    ChannelARN: str
    SenderClientId: str
    MessagePayload: str

class GetIceServerConfigResponseTypeDef(TypedDict):
    IceServerList: List[IceServerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendAlexaOfferToMasterResponseTypeDef(TypedDict):
    Answer: str
    ResponseMetadata: ResponseMetadataTypeDef
