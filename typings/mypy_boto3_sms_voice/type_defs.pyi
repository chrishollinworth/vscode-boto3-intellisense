"""
Main interface for sms-voice service type definitions.

Usage::

    ```python
    from mypy_boto3_sms_voice.type_defs import CallInstructionsMessageTypeTypeDef

    data: CallInstructionsMessageTypeTypeDef = {...}
    ```
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CallInstructionsMessageTypeTypeDef",
    "CloudWatchLogsDestinationTypeDef",
    "EventDestinationTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "PlainTextMessageTypeTypeDef",
    "SSMLMessageTypeTypeDef",
    "SnsDestinationTypeDef",
    "EventDestinationDefinitionTypeDef",
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "SendVoiceMessageResponseTypeDef",
    "VoiceMessageContentTypeDef",
)

CallInstructionsMessageTypeTypeDef = TypedDict(
    "CallInstructionsMessageTypeTypeDef", {"Text": str}, total=False
)

CloudWatchLogsDestinationTypeDef = TypedDict(
    "CloudWatchLogsDestinationTypeDef", {"IamRoleArn": str, "LogGroupArn": str}, total=False
)

EventDestinationTypeDef = TypedDict(
    "EventDestinationTypeDef",
    {
        "CloudWatchLogsDestination": "CloudWatchLogsDestinationTypeDef",
        "Enabled": bool,
        "KinesisFirehoseDestination": "KinesisFirehoseDestinationTypeDef",
        "MatchingEventTypes": List[
            Literal[
                "INITIATED_CALL",
                "RINGING",
                "ANSWERED",
                "COMPLETED_CALL",
                "BUSY",
                "FAILED",
                "NO_ANSWER",
            ]
        ],
        "Name": str,
        "SnsDestination": "SnsDestinationTypeDef",
    },
    total=False,
)

KinesisFirehoseDestinationTypeDef = TypedDict(
    "KinesisFirehoseDestinationTypeDef", {"DeliveryStreamArn": str, "IamRoleArn": str}, total=False
)

PlainTextMessageTypeTypeDef = TypedDict(
    "PlainTextMessageTypeTypeDef", {"LanguageCode": str, "Text": str, "VoiceId": str}, total=False
)

SSMLMessageTypeTypeDef = TypedDict(
    "SSMLMessageTypeTypeDef", {"LanguageCode": str, "Text": str, "VoiceId": str}, total=False
)

SnsDestinationTypeDef = TypedDict("SnsDestinationTypeDef", {"TopicArn": str}, total=False)

EventDestinationDefinitionTypeDef = TypedDict(
    "EventDestinationDefinitionTypeDef",
    {
        "CloudWatchLogsDestination": "CloudWatchLogsDestinationTypeDef",
        "Enabled": bool,
        "KinesisFirehoseDestination": "KinesisFirehoseDestinationTypeDef",
        "MatchingEventTypes": List[
            Literal[
                "INITIATED_CALL",
                "RINGING",
                "ANSWERED",
                "COMPLETED_CALL",
                "BUSY",
                "FAILED",
                "NO_ANSWER",
            ]
        ],
        "SnsDestination": "SnsDestinationTypeDef",
    },
    total=False,
)

GetConfigurationSetEventDestinationsResponseTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    {"EventDestinations": List["EventDestinationTypeDef"]},
    total=False,
)

ListConfigurationSetsResponseTypeDef = TypedDict(
    "ListConfigurationSetsResponseTypeDef",
    {"ConfigurationSets": List[str], "NextToken": str},
    total=False,
)

SendVoiceMessageResponseTypeDef = TypedDict(
    "SendVoiceMessageResponseTypeDef", {"MessageId": str}, total=False
)

VoiceMessageContentTypeDef = TypedDict(
    "VoiceMessageContentTypeDef",
    {
        "CallInstructionsMessage": "CallInstructionsMessageTypeTypeDef",
        "PlainTextMessage": "PlainTextMessageTypeTypeDef",
        "SSMLMessage": "SSMLMessageTypeTypeDef",
    },
    total=False,
)
