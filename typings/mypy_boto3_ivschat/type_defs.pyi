"""
Type annotations for ivschat service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ivschat.type_defs import CreateChatTokenRequestRequestTypeDef

    data: CreateChatTokenRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import ChatTokenCapabilityType, FallbackResultType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateChatTokenRequestRequestTypeDef",
    "CreateChatTokenResponseTypeDef",
    "CreateRoomRequestRequestTypeDef",
    "CreateRoomResponseTypeDef",
    "DeleteMessageRequestRequestTypeDef",
    "DeleteMessageResponseTypeDef",
    "DeleteRoomRequestRequestTypeDef",
    "DisconnectUserRequestRequestTypeDef",
    "GetRoomRequestRequestTypeDef",
    "GetRoomResponseTypeDef",
    "ListRoomsRequestRequestTypeDef",
    "ListRoomsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MessageReviewHandlerTypeDef",
    "ResponseMetadataTypeDef",
    "RoomSummaryTypeDef",
    "SendEventRequestRequestTypeDef",
    "SendEventResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateRoomRequestRequestTypeDef",
    "UpdateRoomResponseTypeDef",
)

_RequiredCreateChatTokenRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChatTokenRequestRequestTypeDef",
    {
        "roomIdentifier": str,
        "userId": str,
    },
)
_OptionalCreateChatTokenRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChatTokenRequestRequestTypeDef",
    {
        "attributes": Dict[str, str],
        "capabilities": List[ChatTokenCapabilityType],
        "sessionDurationInMinutes": int,
    },
    total=False,
)

class CreateChatTokenRequestRequestTypeDef(
    _RequiredCreateChatTokenRequestRequestTypeDef, _OptionalCreateChatTokenRequestRequestTypeDef
):
    pass

CreateChatTokenResponseTypeDef = TypedDict(
    "CreateChatTokenResponseTypeDef",
    {
        "sessionExpirationTime": datetime,
        "token": str,
        "tokenExpirationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRoomRequestRequestTypeDef = TypedDict(
    "CreateRoomRequestRequestTypeDef",
    {
        "maximumMessageLength": int,
        "maximumMessageRatePerSecond": int,
        "messageReviewHandler": "MessageReviewHandlerTypeDef",
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateRoomResponseTypeDef = TypedDict(
    "CreateRoomResponseTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "maximumMessageLength": int,
        "maximumMessageRatePerSecond": int,
        "messageReviewHandler": "MessageReviewHandlerTypeDef",
        "name": str,
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteMessageRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteMessageRequestRequestTypeDef",
    {
        "id": str,
        "roomIdentifier": str,
    },
)
_OptionalDeleteMessageRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteMessageRequestRequestTypeDef",
    {
        "reason": str,
    },
    total=False,
)

class DeleteMessageRequestRequestTypeDef(
    _RequiredDeleteMessageRequestRequestTypeDef, _OptionalDeleteMessageRequestRequestTypeDef
):
    pass

DeleteMessageResponseTypeDef = TypedDict(
    "DeleteMessageResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRoomRequestRequestTypeDef = TypedDict(
    "DeleteRoomRequestRequestTypeDef",
    {
        "identifier": str,
    },
)

_RequiredDisconnectUserRequestRequestTypeDef = TypedDict(
    "_RequiredDisconnectUserRequestRequestTypeDef",
    {
        "roomIdentifier": str,
        "userId": str,
    },
)
_OptionalDisconnectUserRequestRequestTypeDef = TypedDict(
    "_OptionalDisconnectUserRequestRequestTypeDef",
    {
        "reason": str,
    },
    total=False,
)

class DisconnectUserRequestRequestTypeDef(
    _RequiredDisconnectUserRequestRequestTypeDef, _OptionalDisconnectUserRequestRequestTypeDef
):
    pass

GetRoomRequestRequestTypeDef = TypedDict(
    "GetRoomRequestRequestTypeDef",
    {
        "identifier": str,
    },
)

GetRoomResponseTypeDef = TypedDict(
    "GetRoomResponseTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "maximumMessageLength": int,
        "maximumMessageRatePerSecond": int,
        "messageReviewHandler": "MessageReviewHandlerTypeDef",
        "name": str,
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRoomsRequestRequestTypeDef = TypedDict(
    "ListRoomsRequestRequestTypeDef",
    {
        "maxResults": int,
        "messageReviewHandlerUri": str,
        "name": str,
        "nextToken": str,
    },
    total=False,
)

ListRoomsResponseTypeDef = TypedDict(
    "ListRoomsResponseTypeDef",
    {
        "nextToken": str,
        "rooms": List["RoomSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MessageReviewHandlerTypeDef = TypedDict(
    "MessageReviewHandlerTypeDef",
    {
        "fallbackResult": FallbackResultType,
        "uri": str,
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

RoomSummaryTypeDef = TypedDict(
    "RoomSummaryTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "messageReviewHandler": "MessageReviewHandlerTypeDef",
        "name": str,
        "tags": Dict[str, str],
        "updateTime": datetime,
    },
    total=False,
)

_RequiredSendEventRequestRequestTypeDef = TypedDict(
    "_RequiredSendEventRequestRequestTypeDef",
    {
        "eventName": str,
        "roomIdentifier": str,
    },
)
_OptionalSendEventRequestRequestTypeDef = TypedDict(
    "_OptionalSendEventRequestRequestTypeDef",
    {
        "attributes": Dict[str, str],
    },
    total=False,
)

class SendEventRequestRequestTypeDef(
    _RequiredSendEventRequestRequestTypeDef, _OptionalSendEventRequestRequestTypeDef
):
    pass

SendEventResponseTypeDef = TypedDict(
    "SendEventResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateRoomRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRoomRequestRequestTypeDef",
    {
        "identifier": str,
    },
)
_OptionalUpdateRoomRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRoomRequestRequestTypeDef",
    {
        "maximumMessageLength": int,
        "maximumMessageRatePerSecond": int,
        "messageReviewHandler": "MessageReviewHandlerTypeDef",
        "name": str,
    },
    total=False,
)

class UpdateRoomRequestRequestTypeDef(
    _RequiredUpdateRoomRequestRequestTypeDef, _OptionalUpdateRoomRequestRequestTypeDef
):
    pass

UpdateRoomResponseTypeDef = TypedDict(
    "UpdateRoomResponseTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "maximumMessageLength": int,
        "maximumMessageRatePerSecond": int,
        "messageReviewHandler": "MessageReviewHandlerTypeDef",
        "name": str,
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
