"""
Type annotations for sms-voice service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms_voice/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sms_voice.type_defs import CallInstructionsMessageTypeTypeDef

    data: CallInstructionsMessageTypeTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import EventTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CallInstructionsMessageTypeTypeDef",
    "CloudWatchLogsDestinationTypeDef",
    "CreateConfigurationSetEventDestinationRequestRequestTypeDef",
    "CreateConfigurationSetRequestRequestTypeDef",
    "DeleteConfigurationSetEventDestinationRequestRequestTypeDef",
    "DeleteConfigurationSetRequestRequestTypeDef",
    "EventDestinationDefinitionTypeDef",
    "EventDestinationTypeDef",
    "GetConfigurationSetEventDestinationsRequestRequestTypeDef",
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "ListConfigurationSetsRequestRequestTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "PlainTextMessageTypeTypeDef",
    "ResponseMetadataTypeDef",
    "SSMLMessageTypeTypeDef",
    "SendVoiceMessageRequestRequestTypeDef",
    "SendVoiceMessageResponseTypeDef",
    "SnsDestinationTypeDef",
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    "VoiceMessageContentTypeDef",
)

CallInstructionsMessageTypeTypeDef = TypedDict(
    "CallInstructionsMessageTypeTypeDef",
    {
        "Text": str,
    },
    total=False,
)

CloudWatchLogsDestinationTypeDef = TypedDict(
    "CloudWatchLogsDestinationTypeDef",
    {
        "IamRoleArn": str,
        "LogGroupArn": str,
    },
    total=False,
)

_RequiredCreateConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalCreateConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "EventDestination": "EventDestinationDefinitionTypeDef",
        "EventDestinationName": str,
    },
    total=False,
)

class CreateConfigurationSetEventDestinationRequestRequestTypeDef(
    _RequiredCreateConfigurationSetEventDestinationRequestRequestTypeDef,
    _OptionalCreateConfigurationSetEventDestinationRequestRequestTypeDef,
):
    pass

CreateConfigurationSetRequestRequestTypeDef = TypedDict(
    "CreateConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
    total=False,
)

DeleteConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
    },
)

DeleteConfigurationSetRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

EventDestinationDefinitionTypeDef = TypedDict(
    "EventDestinationDefinitionTypeDef",
    {
        "CloudWatchLogsDestination": "CloudWatchLogsDestinationTypeDef",
        "Enabled": bool,
        "KinesisFirehoseDestination": "KinesisFirehoseDestinationTypeDef",
        "MatchingEventTypes": List[EventTypeType],
        "SnsDestination": "SnsDestinationTypeDef",
    },
    total=False,
)

EventDestinationTypeDef = TypedDict(
    "EventDestinationTypeDef",
    {
        "CloudWatchLogsDestination": "CloudWatchLogsDestinationTypeDef",
        "Enabled": bool,
        "KinesisFirehoseDestination": "KinesisFirehoseDestinationTypeDef",
        "MatchingEventTypes": List[EventTypeType],
        "Name": str,
        "SnsDestination": "SnsDestinationTypeDef",
    },
    total=False,
)

GetConfigurationSetEventDestinationsRequestRequestTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

GetConfigurationSetEventDestinationsResponseTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    {
        "EventDestinations": List["EventDestinationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KinesisFirehoseDestinationTypeDef = TypedDict(
    "KinesisFirehoseDestinationTypeDef",
    {
        "DeliveryStreamArn": str,
        "IamRoleArn": str,
    },
    total=False,
)

ListConfigurationSetsRequestRequestTypeDef = TypedDict(
    "ListConfigurationSetsRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": str,
    },
    total=False,
)

ListConfigurationSetsResponseTypeDef = TypedDict(
    "ListConfigurationSetsResponseTypeDef",
    {
        "ConfigurationSets": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PlainTextMessageTypeTypeDef = TypedDict(
    "PlainTextMessageTypeTypeDef",
    {
        "LanguageCode": str,
        "Text": str,
        "VoiceId": str,
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

SSMLMessageTypeTypeDef = TypedDict(
    "SSMLMessageTypeTypeDef",
    {
        "LanguageCode": str,
        "Text": str,
        "VoiceId": str,
    },
    total=False,
)

SendVoiceMessageRequestRequestTypeDef = TypedDict(
    "SendVoiceMessageRequestRequestTypeDef",
    {
        "CallerId": str,
        "ConfigurationSetName": str,
        "Content": "VoiceMessageContentTypeDef",
        "DestinationPhoneNumber": str,
        "OriginationPhoneNumber": str,
    },
    total=False,
)

SendVoiceMessageResponseTypeDef = TypedDict(
    "SendVoiceMessageResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SnsDestinationTypeDef = TypedDict(
    "SnsDestinationTypeDef",
    {
        "TopicArn": str,
    },
    total=False,
)

_RequiredUpdateConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
    },
)
_OptionalUpdateConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "EventDestination": "EventDestinationDefinitionTypeDef",
    },
    total=False,
)

class UpdateConfigurationSetEventDestinationRequestRequestTypeDef(
    _RequiredUpdateConfigurationSetEventDestinationRequestRequestTypeDef,
    _OptionalUpdateConfigurationSetEventDestinationRequestRequestTypeDef,
):
    pass

VoiceMessageContentTypeDef = TypedDict(
    "VoiceMessageContentTypeDef",
    {
        "CallInstructionsMessage": "CallInstructionsMessageTypeTypeDef",
        "PlainTextMessage": "PlainTextMessageTypeTypeDef",
        "SSMLMessage": "SSMLMessageTypeTypeDef",
    },
    total=False,
)
