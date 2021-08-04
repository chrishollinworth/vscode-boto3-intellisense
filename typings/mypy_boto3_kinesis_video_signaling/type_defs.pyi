"""
Type annotations for kinesis-video-signaling service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_signaling/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesis_video_signaling.type_defs import GetIceServerConfigRequestRequestTypeDef

    data: GetIceServerConfigRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "GetIceServerConfigRequestRequestTypeDef",
    "GetIceServerConfigResponseTypeDef",
    "IceServerTypeDef",
    "ResponseMetadataTypeDef",
    "SendAlexaOfferToMasterRequestRequestTypeDef",
    "SendAlexaOfferToMasterResponseTypeDef",
)

_RequiredGetIceServerConfigRequestRequestTypeDef = TypedDict(
    "_RequiredGetIceServerConfigRequestRequestTypeDef",
    {
        "ChannelARN": str,
    },
)
_OptionalGetIceServerConfigRequestRequestTypeDef = TypedDict(
    "_OptionalGetIceServerConfigRequestRequestTypeDef",
    {
        "ClientId": str,
        "Service": Literal["TURN"],
        "Username": str,
    },
    total=False,
)

class GetIceServerConfigRequestRequestTypeDef(
    _RequiredGetIceServerConfigRequestRequestTypeDef,
    _OptionalGetIceServerConfigRequestRequestTypeDef,
):
    pass

GetIceServerConfigResponseTypeDef = TypedDict(
    "GetIceServerConfigResponseTypeDef",
    {
        "IceServerList": List["IceServerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IceServerTypeDef = TypedDict(
    "IceServerTypeDef",
    {
        "Uris": List[str],
        "Username": str,
        "Password": str,
        "Ttl": int,
    },
    total=False,
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

SendAlexaOfferToMasterRequestRequestTypeDef = TypedDict(
    "SendAlexaOfferToMasterRequestRequestTypeDef",
    {
        "ChannelARN": str,
        "SenderClientId": str,
        "MessagePayload": str,
    },
)

SendAlexaOfferToMasterResponseTypeDef = TypedDict(
    "SendAlexaOfferToMasterResponseTypeDef",
    {
        "Answer": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
