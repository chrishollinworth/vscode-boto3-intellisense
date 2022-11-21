"""
Type annotations for ivschat service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ivschat.type_defs import CloudWatchLogsDestinationConfigurationTypeDef

    data: CloudWatchLogsDestinationConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import ChatTokenCapabilityType, FallbackResultType, LoggingConfigurationStateType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CloudWatchLogsDestinationConfigurationTypeDef",
    "CreateChatTokenRequestRequestTypeDef",
    "CreateChatTokenResponseTypeDef",
    "CreateLoggingConfigurationRequestRequestTypeDef",
    "CreateLoggingConfigurationResponseTypeDef",
    "CreateRoomRequestRequestTypeDef",
    "CreateRoomResponseTypeDef",
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    "DeleteMessageRequestRequestTypeDef",
    "DeleteMessageResponseTypeDef",
    "DeleteRoomRequestRequestTypeDef",
    "DestinationConfigurationTypeDef",
    "DisconnectUserRequestRequestTypeDef",
    "FirehoseDestinationConfigurationTypeDef",
    "GetLoggingConfigurationRequestRequestTypeDef",
    "GetLoggingConfigurationResponseTypeDef",
    "GetRoomRequestRequestTypeDef",
    "GetRoomResponseTypeDef",
    "ListLoggingConfigurationsRequestRequestTypeDef",
    "ListLoggingConfigurationsResponseTypeDef",
    "ListRoomsRequestRequestTypeDef",
    "ListRoomsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoggingConfigurationSummaryTypeDef",
    "MessageReviewHandlerTypeDef",
    "ResponseMetadataTypeDef",
    "RoomSummaryTypeDef",
    "S3DestinationConfigurationTypeDef",
    "SendEventRequestRequestTypeDef",
    "SendEventResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateLoggingConfigurationRequestRequestTypeDef",
    "UpdateLoggingConfigurationResponseTypeDef",
    "UpdateRoomRequestRequestTypeDef",
    "UpdateRoomResponseTypeDef",
)

CloudWatchLogsDestinationConfigurationTypeDef = TypedDict(
    "CloudWatchLogsDestinationConfigurationTypeDef",
    {
        "logGroupName": str,
    },
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

_RequiredCreateLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLoggingConfigurationRequestRequestTypeDef",
    {
        "destinationConfiguration": "DestinationConfigurationTypeDef",
    },
)
_OptionalCreateLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLoggingConfigurationRequestRequestTypeDef",
    {
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateLoggingConfigurationRequestRequestTypeDef(
    _RequiredCreateLoggingConfigurationRequestRequestTypeDef,
    _OptionalCreateLoggingConfigurationRequestRequestTypeDef,
):
    pass

CreateLoggingConfigurationResponseTypeDef = TypedDict(
    "CreateLoggingConfigurationResponseTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "destinationConfiguration": "DestinationConfigurationTypeDef",
        "id": str,
        "name": str,
        "state": Literal["ACTIVE"],
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRoomRequestRequestTypeDef = TypedDict(
    "CreateRoomRequestRequestTypeDef",
    {
        "loggingConfigurationIdentifiers": List[str],
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
        "loggingConfigurationIdentifiers": List[str],
        "maximumMessageLength": int,
        "maximumMessageRatePerSecond": int,
        "messageReviewHandler": "MessageReviewHandlerTypeDef",
        "name": str,
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    {
        "identifier": str,
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

DestinationConfigurationTypeDef = TypedDict(
    "DestinationConfigurationTypeDef",
    {
        "cloudWatchLogs": "CloudWatchLogsDestinationConfigurationTypeDef",
        "firehose": "FirehoseDestinationConfigurationTypeDef",
        "s3": "S3DestinationConfigurationTypeDef",
    },
    total=False,
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

FirehoseDestinationConfigurationTypeDef = TypedDict(
    "FirehoseDestinationConfigurationTypeDef",
    {
        "deliveryStreamName": str,
    },
)

GetLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "GetLoggingConfigurationRequestRequestTypeDef",
    {
        "identifier": str,
    },
)

GetLoggingConfigurationResponseTypeDef = TypedDict(
    "GetLoggingConfigurationResponseTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "destinationConfiguration": "DestinationConfigurationTypeDef",
        "id": str,
        "name": str,
        "state": LoggingConfigurationStateType,
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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
        "loggingConfigurationIdentifiers": List[str],
        "maximumMessageLength": int,
        "maximumMessageRatePerSecond": int,
        "messageReviewHandler": "MessageReviewHandlerTypeDef",
        "name": str,
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLoggingConfigurationsRequestRequestTypeDef = TypedDict(
    "ListLoggingConfigurationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListLoggingConfigurationsResponseTypeDef = TypedDict(
    "ListLoggingConfigurationsResponseTypeDef",
    {
        "loggingConfigurations": List["LoggingConfigurationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRoomsRequestRequestTypeDef = TypedDict(
    "ListRoomsRequestRequestTypeDef",
    {
        "loggingConfigurationIdentifier": str,
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

LoggingConfigurationSummaryTypeDef = TypedDict(
    "LoggingConfigurationSummaryTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "destinationConfiguration": "DestinationConfigurationTypeDef",
        "id": str,
        "name": str,
        "state": LoggingConfigurationStateType,
        "tags": Dict[str, str],
        "updateTime": datetime,
    },
    total=False,
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
        "loggingConfigurationIdentifiers": List[str],
        "messageReviewHandler": "MessageReviewHandlerTypeDef",
        "name": str,
        "tags": Dict[str, str],
        "updateTime": datetime,
    },
    total=False,
)

S3DestinationConfigurationTypeDef = TypedDict(
    "S3DestinationConfigurationTypeDef",
    {
        "bucketName": str,
    },
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

_RequiredUpdateLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLoggingConfigurationRequestRequestTypeDef",
    {
        "identifier": str,
    },
)
_OptionalUpdateLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLoggingConfigurationRequestRequestTypeDef",
    {
        "destinationConfiguration": "DestinationConfigurationTypeDef",
        "name": str,
    },
    total=False,
)

class UpdateLoggingConfigurationRequestRequestTypeDef(
    _RequiredUpdateLoggingConfigurationRequestRequestTypeDef,
    _OptionalUpdateLoggingConfigurationRequestRequestTypeDef,
):
    pass

UpdateLoggingConfigurationResponseTypeDef = TypedDict(
    "UpdateLoggingConfigurationResponseTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "destinationConfiguration": "DestinationConfigurationTypeDef",
        "id": str,
        "name": str,
        "state": Literal["ACTIVE"],
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "loggingConfigurationIdentifiers": List[str],
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
        "loggingConfigurationIdentifiers": List[str],
        "maximumMessageLength": int,
        "maximumMessageRatePerSecond": int,
        "messageReviewHandler": "MessageReviewHandlerTypeDef",
        "name": str,
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
