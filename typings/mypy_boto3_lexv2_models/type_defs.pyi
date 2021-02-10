"""
Main interface for lexv2-models service type definitions.

Usage::

    ```python
    from mypy_boto3_lexv2_models.type_defs import AudioLogDestinationTypeDef

    data: AudioLogDestinationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AudioLogDestinationTypeDef",
    "AudioLogSettingTypeDef",
    "BotAliasHistoryEventTypeDef",
    "BotAliasLocaleSettingsTypeDef",
    "BotAliasSummaryTypeDef",
    "BotLocaleHistoryEventTypeDef",
    "BotLocaleSummaryTypeDef",
    "BotSummaryTypeDef",
    "BotVersionLocaleDetailsTypeDef",
    "BotVersionSummaryTypeDef",
    "BuiltInIntentSummaryTypeDef",
    "BuiltInSlotTypeSummaryTypeDef",
    "ButtonTypeDef",
    "CloudWatchLogGroupLogDestinationTypeDef",
    "CodeHookSpecificationTypeDef",
    "ConversationLogSettingsTypeDef",
    "CustomPayloadTypeDef",
    "DataPrivacyTypeDef",
    "DialogCodeHookSettingsTypeDef",
    "FulfillmentCodeHookSettingsTypeDef",
    "ImageResponseCardTypeDef",
    "InputContextTypeDef",
    "IntentClosingSettingTypeDef",
    "IntentConfirmationSettingTypeDef",
    "IntentSummaryTypeDef",
    "KendraConfigurationTypeDef",
    "LambdaCodeHookTypeDef",
    "MessageGroupTypeDef",
    "MessageTypeDef",
    "ObfuscationSettingTypeDef",
    "OutputContextTypeDef",
    "PlainTextMessageTypeDef",
    "PromptSpecificationTypeDef",
    "ResponseSpecificationTypeDef",
    "S3BucketLogDestinationTypeDef",
    "SSMLMessageTypeDef",
    "SampleUtteranceTypeDef",
    "SampleValueTypeDef",
    "SentimentAnalysisSettingsTypeDef",
    "SlotDefaultValueSpecificationTypeDef",
    "SlotDefaultValueTypeDef",
    "SlotPriorityTypeDef",
    "SlotSummaryTypeDef",
    "SlotTypeSummaryTypeDef",
    "SlotTypeValueTypeDef",
    "SlotValueElicitationSettingTypeDef",
    "SlotValueRegexFilterTypeDef",
    "SlotValueSelectionSettingTypeDef",
    "StillWaitingResponseSpecificationTypeDef",
    "TextLogDestinationTypeDef",
    "TextLogSettingTypeDef",
    "VoiceSettingsTypeDef",
    "WaitAndContinueSpecificationTypeDef",
    "BotFilterTypeDef",
    "BotLocaleFilterTypeDef",
    "BotLocaleSortByTypeDef",
    "BotSortByTypeDef",
    "BotVersionSortByTypeDef",
    "BuildBotLocaleResponseTypeDef",
    "BuiltInIntentSortByTypeDef",
    "BuiltInSlotTypeSortByTypeDef",
    "CreateBotAliasResponseTypeDef",
    "CreateBotLocaleResponseTypeDef",
    "CreateBotResponseTypeDef",
    "CreateBotVersionResponseTypeDef",
    "CreateIntentResponseTypeDef",
    "CreateSlotResponseTypeDef",
    "CreateSlotTypeResponseTypeDef",
    "DeleteBotAliasResponseTypeDef",
    "DeleteBotLocaleResponseTypeDef",
    "DeleteBotResponseTypeDef",
    "DeleteBotVersionResponseTypeDef",
    "DescribeBotAliasResponseTypeDef",
    "DescribeBotLocaleResponseTypeDef",
    "DescribeBotResponseTypeDef",
    "DescribeBotVersionResponseTypeDef",
    "DescribeIntentResponseTypeDef",
    "DescribeSlotResponseTypeDef",
    "DescribeSlotTypeResponseTypeDef",
    "IntentFilterTypeDef",
    "IntentSortByTypeDef",
    "ListBotAliasesResponseTypeDef",
    "ListBotLocalesResponseTypeDef",
    "ListBotVersionsResponseTypeDef",
    "ListBotsResponseTypeDef",
    "ListBuiltInIntentsResponseTypeDef",
    "ListBuiltInSlotTypesResponseTypeDef",
    "ListIntentsResponseTypeDef",
    "ListSlotTypesResponseTypeDef",
    "ListSlotsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "SlotFilterTypeDef",
    "SlotSortByTypeDef",
    "SlotTypeFilterTypeDef",
    "SlotTypeSortByTypeDef",
    "UpdateBotAliasResponseTypeDef",
    "UpdateBotLocaleResponseTypeDef",
    "UpdateBotResponseTypeDef",
    "UpdateIntentResponseTypeDef",
    "UpdateSlotResponseTypeDef",
    "UpdateSlotTypeResponseTypeDef",
)

AudioLogDestinationTypeDef = TypedDict(
    "AudioLogDestinationTypeDef", {"s3Bucket": "S3BucketLogDestinationTypeDef"}
)

AudioLogSettingTypeDef = TypedDict(
    "AudioLogSettingTypeDef", {"enabled": bool, "destination": "AudioLogDestinationTypeDef"}
)

BotAliasHistoryEventTypeDef = TypedDict(
    "BotAliasHistoryEventTypeDef",
    {"botVersion": str, "startDate": datetime, "endDate": datetime},
    total=False,
)

_RequiredBotAliasLocaleSettingsTypeDef = TypedDict(
    "_RequiredBotAliasLocaleSettingsTypeDef", {"enabled": bool}
)
_OptionalBotAliasLocaleSettingsTypeDef = TypedDict(
    "_OptionalBotAliasLocaleSettingsTypeDef",
    {"codeHookSpecification": "CodeHookSpecificationTypeDef"},
    total=False,
)


class BotAliasLocaleSettingsTypeDef(
    _RequiredBotAliasLocaleSettingsTypeDef, _OptionalBotAliasLocaleSettingsTypeDef
):
    pass


BotAliasSummaryTypeDef = TypedDict(
    "BotAliasSummaryTypeDef",
    {
        "botAliasId": str,
        "botAliasName": str,
        "description": str,
        "botVersion": str,
        "botAliasStatus": Literal["Creating", "Available", "Deleting", "Failed"],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

BotLocaleHistoryEventTypeDef = TypedDict(
    "BotLocaleHistoryEventTypeDef", {"event": str, "eventDate": datetime}
)

BotLocaleSummaryTypeDef = TypedDict(
    "BotLocaleSummaryTypeDef",
    {
        "localeId": str,
        "localeName": str,
        "description": str,
        "botLocaleStatus": Literal[
            "Creating", "Building", "Built", "ReadyExpressTesting", "Failed", "Deleting", "NotBuilt"
        ],
        "lastUpdatedDateTime": datetime,
        "lastBuildSubmittedDateTime": datetime,
    },
    total=False,
)

BotSummaryTypeDef = TypedDict(
    "BotSummaryTypeDef",
    {
        "botId": str,
        "botName": str,
        "description": str,
        "botStatus": Literal[
            "Creating", "Available", "Inactive", "Deleting", "Failed", "Versioning"
        ],
        "latestBotVersion": str,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

BotVersionLocaleDetailsTypeDef = TypedDict(
    "BotVersionLocaleDetailsTypeDef", {"sourceBotVersion": str}
)

BotVersionSummaryTypeDef = TypedDict(
    "BotVersionSummaryTypeDef",
    {
        "botName": str,
        "botVersion": str,
        "description": str,
        "botStatus": Literal[
            "Creating", "Available", "Inactive", "Deleting", "Failed", "Versioning"
        ],
        "creationDateTime": datetime,
    },
    total=False,
)

BuiltInIntentSummaryTypeDef = TypedDict(
    "BuiltInIntentSummaryTypeDef", {"intentSignature": str, "description": str}, total=False
)

BuiltInSlotTypeSummaryTypeDef = TypedDict(
    "BuiltInSlotTypeSummaryTypeDef", {"slotTypeSignature": str, "description": str}, total=False
)

ButtonTypeDef = TypedDict("ButtonTypeDef", {"text": str, "value": str})

CloudWatchLogGroupLogDestinationTypeDef = TypedDict(
    "CloudWatchLogGroupLogDestinationTypeDef", {"cloudWatchLogGroupArn": str, "logPrefix": str}
)

CodeHookSpecificationTypeDef = TypedDict(
    "CodeHookSpecificationTypeDef", {"lambdaCodeHook": "LambdaCodeHookTypeDef"}
)

ConversationLogSettingsTypeDef = TypedDict(
    "ConversationLogSettingsTypeDef",
    {
        "textLogSettings": List["TextLogSettingTypeDef"],
        "audioLogSettings": List["AudioLogSettingTypeDef"],
    },
    total=False,
)

CustomPayloadTypeDef = TypedDict("CustomPayloadTypeDef", {"value": str})

DataPrivacyTypeDef = TypedDict("DataPrivacyTypeDef", {"childDirected": bool})

DialogCodeHookSettingsTypeDef = TypedDict("DialogCodeHookSettingsTypeDef", {"enabled": bool})

FulfillmentCodeHookSettingsTypeDef = TypedDict(
    "FulfillmentCodeHookSettingsTypeDef", {"enabled": bool}
)

_RequiredImageResponseCardTypeDef = TypedDict("_RequiredImageResponseCardTypeDef", {"title": str})
_OptionalImageResponseCardTypeDef = TypedDict(
    "_OptionalImageResponseCardTypeDef",
    {"subtitle": str, "imageUrl": str, "buttons": List["ButtonTypeDef"]},
    total=False,
)


class ImageResponseCardTypeDef(
    _RequiredImageResponseCardTypeDef, _OptionalImageResponseCardTypeDef
):
    pass


InputContextTypeDef = TypedDict("InputContextTypeDef", {"name": str})

IntentClosingSettingTypeDef = TypedDict(
    "IntentClosingSettingTypeDef", {"closingResponse": "ResponseSpecificationTypeDef"}
)

IntentConfirmationSettingTypeDef = TypedDict(
    "IntentConfirmationSettingTypeDef",
    {
        "promptSpecification": "PromptSpecificationTypeDef",
        "declinationResponse": "ResponseSpecificationTypeDef",
    },
)

IntentSummaryTypeDef = TypedDict(
    "IntentSummaryTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "description": str,
        "parentIntentSignature": str,
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

_RequiredKendraConfigurationTypeDef = TypedDict(
    "_RequiredKendraConfigurationTypeDef", {"kendraIndex": str}
)
_OptionalKendraConfigurationTypeDef = TypedDict(
    "_OptionalKendraConfigurationTypeDef",
    {"queryFilterStringEnabled": bool, "queryFilterString": str},
    total=False,
)


class KendraConfigurationTypeDef(
    _RequiredKendraConfigurationTypeDef, _OptionalKendraConfigurationTypeDef
):
    pass


LambdaCodeHookTypeDef = TypedDict(
    "LambdaCodeHookTypeDef", {"lambdaARN": str, "codeHookInterfaceVersion": str}
)

_RequiredMessageGroupTypeDef = TypedDict(
    "_RequiredMessageGroupTypeDef", {"message": "MessageTypeDef"}
)
_OptionalMessageGroupTypeDef = TypedDict(
    "_OptionalMessageGroupTypeDef", {"variations": List["MessageTypeDef"]}, total=False
)


class MessageGroupTypeDef(_RequiredMessageGroupTypeDef, _OptionalMessageGroupTypeDef):
    pass


MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "plainTextMessage": "PlainTextMessageTypeDef",
        "customPayload": "CustomPayloadTypeDef",
        "ssmlMessage": "SSMLMessageTypeDef",
        "imageResponseCard": "ImageResponseCardTypeDef",
    },
    total=False,
)

ObfuscationSettingTypeDef = TypedDict(
    "ObfuscationSettingTypeDef", {"obfuscationSettingType": Literal["None", "DefaultObfuscation"]}
)

OutputContextTypeDef = TypedDict(
    "OutputContextTypeDef", {"name": str, "timeToLiveInSeconds": int, "turnsToLive": int}
)

PlainTextMessageTypeDef = TypedDict("PlainTextMessageTypeDef", {"value": str})

_RequiredPromptSpecificationTypeDef = TypedDict(
    "_RequiredPromptSpecificationTypeDef",
    {"messageGroups": List["MessageGroupTypeDef"], "maxRetries": int},
)
_OptionalPromptSpecificationTypeDef = TypedDict(
    "_OptionalPromptSpecificationTypeDef", {"allowInterrupt": bool}, total=False
)


class PromptSpecificationTypeDef(
    _RequiredPromptSpecificationTypeDef, _OptionalPromptSpecificationTypeDef
):
    pass


_RequiredResponseSpecificationTypeDef = TypedDict(
    "_RequiredResponseSpecificationTypeDef", {"messageGroups": List["MessageGroupTypeDef"]}
)
_OptionalResponseSpecificationTypeDef = TypedDict(
    "_OptionalResponseSpecificationTypeDef", {"allowInterrupt": bool}, total=False
)


class ResponseSpecificationTypeDef(
    _RequiredResponseSpecificationTypeDef, _OptionalResponseSpecificationTypeDef
):
    pass


_RequiredS3BucketLogDestinationTypeDef = TypedDict(
    "_RequiredS3BucketLogDestinationTypeDef", {"s3BucketArn": str, "logPrefix": str}
)
_OptionalS3BucketLogDestinationTypeDef = TypedDict(
    "_OptionalS3BucketLogDestinationTypeDef", {"kmsKeyArn": str}, total=False
)


class S3BucketLogDestinationTypeDef(
    _RequiredS3BucketLogDestinationTypeDef, _OptionalS3BucketLogDestinationTypeDef
):
    pass


SSMLMessageTypeDef = TypedDict("SSMLMessageTypeDef", {"value": str})

SampleUtteranceTypeDef = TypedDict("SampleUtteranceTypeDef", {"utterance": str})

SampleValueTypeDef = TypedDict("SampleValueTypeDef", {"value": str})

SentimentAnalysisSettingsTypeDef = TypedDict(
    "SentimentAnalysisSettingsTypeDef", {"detectSentiment": bool}
)

SlotDefaultValueSpecificationTypeDef = TypedDict(
    "SlotDefaultValueSpecificationTypeDef", {"defaultValueList": List["SlotDefaultValueTypeDef"]}
)

SlotDefaultValueTypeDef = TypedDict("SlotDefaultValueTypeDef", {"defaultValue": str})

SlotPriorityTypeDef = TypedDict("SlotPriorityTypeDef", {"priority": int, "slotId": str})

SlotSummaryTypeDef = TypedDict(
    "SlotSummaryTypeDef",
    {
        "slotId": str,
        "slotName": str,
        "description": str,
        "slotConstraint": Literal["Required", "Optional"],
        "slotTypeId": str,
        "valueElicitationPromptSpecification": "PromptSpecificationTypeDef",
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

SlotTypeSummaryTypeDef = TypedDict(
    "SlotTypeSummaryTypeDef",
    {
        "slotTypeId": str,
        "slotTypeName": str,
        "description": str,
        "parentSlotTypeSignature": str,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

SlotTypeValueTypeDef = TypedDict(
    "SlotTypeValueTypeDef",
    {"sampleValue": "SampleValueTypeDef", "synonyms": List["SampleValueTypeDef"]},
    total=False,
)

_RequiredSlotValueElicitationSettingTypeDef = TypedDict(
    "_RequiredSlotValueElicitationSettingTypeDef",
    {"slotConstraint": Literal["Required", "Optional"]},
)
_OptionalSlotValueElicitationSettingTypeDef = TypedDict(
    "_OptionalSlotValueElicitationSettingTypeDef",
    {
        "defaultValueSpecification": "SlotDefaultValueSpecificationTypeDef",
        "promptSpecification": "PromptSpecificationTypeDef",
        "sampleUtterances": List["SampleUtteranceTypeDef"],
        "waitAndContinueSpecification": "WaitAndContinueSpecificationTypeDef",
    },
    total=False,
)


class SlotValueElicitationSettingTypeDef(
    _RequiredSlotValueElicitationSettingTypeDef, _OptionalSlotValueElicitationSettingTypeDef
):
    pass


SlotValueRegexFilterTypeDef = TypedDict("SlotValueRegexFilterTypeDef", {"pattern": str})

_RequiredSlotValueSelectionSettingTypeDef = TypedDict(
    "_RequiredSlotValueSelectionSettingTypeDef",
    {"resolutionStrategy": Literal["OriginalValue", "TopResolution"]},
)
_OptionalSlotValueSelectionSettingTypeDef = TypedDict(
    "_OptionalSlotValueSelectionSettingTypeDef",
    {"regexFilter": "SlotValueRegexFilterTypeDef"},
    total=False,
)


class SlotValueSelectionSettingTypeDef(
    _RequiredSlotValueSelectionSettingTypeDef, _OptionalSlotValueSelectionSettingTypeDef
):
    pass


_RequiredStillWaitingResponseSpecificationTypeDef = TypedDict(
    "_RequiredStillWaitingResponseSpecificationTypeDef",
    {
        "messageGroups": List["MessageGroupTypeDef"],
        "frequencyInSeconds": int,
        "timeoutInSeconds": int,
    },
)
_OptionalStillWaitingResponseSpecificationTypeDef = TypedDict(
    "_OptionalStillWaitingResponseSpecificationTypeDef", {"allowInterrupt": bool}, total=False
)


class StillWaitingResponseSpecificationTypeDef(
    _RequiredStillWaitingResponseSpecificationTypeDef,
    _OptionalStillWaitingResponseSpecificationTypeDef,
):
    pass


TextLogDestinationTypeDef = TypedDict(
    "TextLogDestinationTypeDef", {"cloudWatch": "CloudWatchLogGroupLogDestinationTypeDef"}
)

TextLogSettingTypeDef = TypedDict(
    "TextLogSettingTypeDef", {"enabled": bool, "destination": "TextLogDestinationTypeDef"}
)

VoiceSettingsTypeDef = TypedDict("VoiceSettingsTypeDef", {"voiceId": str})

_RequiredWaitAndContinueSpecificationTypeDef = TypedDict(
    "_RequiredWaitAndContinueSpecificationTypeDef",
    {
        "waitingResponse": "ResponseSpecificationTypeDef",
        "continueResponse": "ResponseSpecificationTypeDef",
    },
)
_OptionalWaitAndContinueSpecificationTypeDef = TypedDict(
    "_OptionalWaitAndContinueSpecificationTypeDef",
    {"stillWaitingResponse": "StillWaitingResponseSpecificationTypeDef"},
    total=False,
)


class WaitAndContinueSpecificationTypeDef(
    _RequiredWaitAndContinueSpecificationTypeDef, _OptionalWaitAndContinueSpecificationTypeDef
):
    pass


BotFilterTypeDef = TypedDict(
    "BotFilterTypeDef",
    {"name": Literal["BotName"], "values": List[str], "operator": Literal["CO", "EQ"]},
)

BotLocaleFilterTypeDef = TypedDict(
    "BotLocaleFilterTypeDef",
    {"name": Literal["BotLocaleName"], "values": List[str], "operator": Literal["CO", "EQ"]},
)

BotLocaleSortByTypeDef = TypedDict(
    "BotLocaleSortByTypeDef",
    {"attribute": Literal["BotLocaleName"], "order": Literal["Ascending", "Descending"]},
)

BotSortByTypeDef = TypedDict(
    "BotSortByTypeDef",
    {"attribute": Literal["BotName"], "order": Literal["Ascending", "Descending"]},
)

BotVersionSortByTypeDef = TypedDict(
    "BotVersionSortByTypeDef",
    {"attribute": Literal["BotVersion"], "order": Literal["Ascending", "Descending"]},
)

BuildBotLocaleResponseTypeDef = TypedDict(
    "BuildBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botLocaleStatus": Literal[
            "Creating", "Building", "Built", "ReadyExpressTesting", "Failed", "Deleting", "NotBuilt"
        ],
        "lastBuildSubmittedDateTime": datetime,
    },
    total=False,
)

BuiltInIntentSortByTypeDef = TypedDict(
    "BuiltInIntentSortByTypeDef",
    {"attribute": Literal["IntentSignature"], "order": Literal["Ascending", "Descending"]},
)

BuiltInSlotTypeSortByTypeDef = TypedDict(
    "BuiltInSlotTypeSortByTypeDef",
    {"attribute": Literal["SlotTypeSignature"], "order": Literal["Ascending", "Descending"]},
)

CreateBotAliasResponseTypeDef = TypedDict(
    "CreateBotAliasResponseTypeDef",
    {
        "botAliasId": str,
        "botAliasName": str,
        "description": str,
        "botVersion": str,
        "botAliasLocaleSettings": Dict[str, "BotAliasLocaleSettingsTypeDef"],
        "conversationLogSettings": "ConversationLogSettingsTypeDef",
        "sentimentAnalysisSettings": "SentimentAnalysisSettingsTypeDef",
        "botAliasStatus": Literal["Creating", "Available", "Deleting", "Failed"],
        "botId": str,
        "creationDateTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateBotLocaleResponseTypeDef = TypedDict(
    "CreateBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeName": str,
        "localeId": str,
        "description": str,
        "nluIntentConfidenceThreshold": float,
        "voiceSettings": "VoiceSettingsTypeDef",
        "botLocaleStatus": Literal[
            "Creating", "Building", "Built", "ReadyExpressTesting", "Failed", "Deleting", "NotBuilt"
        ],
        "creationDateTime": datetime,
    },
    total=False,
)

CreateBotResponseTypeDef = TypedDict(
    "CreateBotResponseTypeDef",
    {
        "botId": str,
        "botName": str,
        "description": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": int,
        "botStatus": Literal[
            "Creating", "Available", "Inactive", "Deleting", "Failed", "Versioning"
        ],
        "creationDateTime": datetime,
        "botTags": Dict[str, str],
        "testBotAliasTags": Dict[str, str],
    },
    total=False,
)

CreateBotVersionResponseTypeDef = TypedDict(
    "CreateBotVersionResponseTypeDef",
    {
        "botId": str,
        "description": str,
        "botVersion": str,
        "botVersionLocaleSpecification": Dict[str, "BotVersionLocaleDetailsTypeDef"],
        "botStatus": Literal[
            "Creating", "Available", "Inactive", "Deleting", "Failed", "Versioning"
        ],
        "creationDateTime": datetime,
    },
    total=False,
)

CreateIntentResponseTypeDef = TypedDict(
    "CreateIntentResponseTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "description": str,
        "parentIntentSignature": str,
        "sampleUtterances": List["SampleUtteranceTypeDef"],
        "dialogCodeHook": "DialogCodeHookSettingsTypeDef",
        "fulfillmentCodeHook": "FulfillmentCodeHookSettingsTypeDef",
        "intentConfirmationSetting": "IntentConfirmationSettingTypeDef",
        "intentClosingSetting": "IntentClosingSettingTypeDef",
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
        "kendraConfiguration": "KendraConfigurationTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
    },
    total=False,
)

CreateSlotResponseTypeDef = TypedDict(
    "CreateSlotResponseTypeDef",
    {
        "slotId": str,
        "slotName": str,
        "description": str,
        "slotTypeId": str,
        "valueElicitationSetting": "SlotValueElicitationSettingTypeDef",
        "obfuscationSetting": "ObfuscationSettingTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "creationDateTime": datetime,
    },
    total=False,
)

CreateSlotTypeResponseTypeDef = TypedDict(
    "CreateSlotTypeResponseTypeDef",
    {
        "slotTypeId": str,
        "slotTypeName": str,
        "description": str,
        "slotTypeValues": List["SlotTypeValueTypeDef"],
        "valueSelectionSetting": "SlotValueSelectionSettingTypeDef",
        "parentSlotTypeSignature": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
    },
    total=False,
)

DeleteBotAliasResponseTypeDef = TypedDict(
    "DeleteBotAliasResponseTypeDef",
    {
        "botAliasId": str,
        "botId": str,
        "botAliasStatus": Literal["Creating", "Available", "Deleting", "Failed"],
    },
    total=False,
)

DeleteBotLocaleResponseTypeDef = TypedDict(
    "DeleteBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botLocaleStatus": Literal[
            "Creating", "Building", "Built", "ReadyExpressTesting", "Failed", "Deleting", "NotBuilt"
        ],
    },
    total=False,
)

DeleteBotResponseTypeDef = TypedDict(
    "DeleteBotResponseTypeDef",
    {
        "botId": str,
        "botStatus": Literal[
            "Creating", "Available", "Inactive", "Deleting", "Failed", "Versioning"
        ],
    },
    total=False,
)

DeleteBotVersionResponseTypeDef = TypedDict(
    "DeleteBotVersionResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "botStatus": Literal[
            "Creating", "Available", "Inactive", "Deleting", "Failed", "Versioning"
        ],
    },
    total=False,
)

DescribeBotAliasResponseTypeDef = TypedDict(
    "DescribeBotAliasResponseTypeDef",
    {
        "botAliasId": str,
        "botAliasName": str,
        "description": str,
        "botVersion": str,
        "botAliasLocaleSettings": Dict[str, "BotAliasLocaleSettingsTypeDef"],
        "conversationLogSettings": "ConversationLogSettingsTypeDef",
        "sentimentAnalysisSettings": "SentimentAnalysisSettingsTypeDef",
        "botAliasHistoryEvents": List["BotAliasHistoryEventTypeDef"],
        "botAliasStatus": Literal["Creating", "Available", "Deleting", "Failed"],
        "botId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

DescribeBotLocaleResponseTypeDef = TypedDict(
    "DescribeBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "localeName": str,
        "description": str,
        "nluIntentConfidenceThreshold": float,
        "voiceSettings": "VoiceSettingsTypeDef",
        "intentsCount": int,
        "slotTypesCount": int,
        "botLocaleStatus": Literal[
            "Creating", "Building", "Built", "ReadyExpressTesting", "Failed", "Deleting", "NotBuilt"
        ],
        "failureReasons": List[str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "lastBuildSubmittedDateTime": datetime,
        "botLocaleHistoryEvents": List["BotLocaleHistoryEventTypeDef"],
    },
    total=False,
)

DescribeBotResponseTypeDef = TypedDict(
    "DescribeBotResponseTypeDef",
    {
        "botId": str,
        "botName": str,
        "description": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": int,
        "botStatus": Literal[
            "Creating", "Available", "Inactive", "Deleting", "Failed", "Versioning"
        ],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

DescribeBotVersionResponseTypeDef = TypedDict(
    "DescribeBotVersionResponseTypeDef",
    {
        "botId": str,
        "botName": str,
        "botVersion": str,
        "description": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": int,
        "botStatus": Literal[
            "Creating", "Available", "Inactive", "Deleting", "Failed", "Versioning"
        ],
        "failureReasons": List[str],
        "creationDateTime": datetime,
    },
    total=False,
)

DescribeIntentResponseTypeDef = TypedDict(
    "DescribeIntentResponseTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "description": str,
        "parentIntentSignature": str,
        "sampleUtterances": List["SampleUtteranceTypeDef"],
        "dialogCodeHook": "DialogCodeHookSettingsTypeDef",
        "fulfillmentCodeHook": "FulfillmentCodeHookSettingsTypeDef",
        "slotPriorities": List["SlotPriorityTypeDef"],
        "intentConfirmationSetting": "IntentConfirmationSettingTypeDef",
        "intentClosingSetting": "IntentClosingSettingTypeDef",
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
        "kendraConfiguration": "KendraConfigurationTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

DescribeSlotResponseTypeDef = TypedDict(
    "DescribeSlotResponseTypeDef",
    {
        "slotId": str,
        "slotName": str,
        "description": str,
        "slotTypeId": str,
        "valueElicitationSetting": "SlotValueElicitationSettingTypeDef",
        "obfuscationSetting": "ObfuscationSettingTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

DescribeSlotTypeResponseTypeDef = TypedDict(
    "DescribeSlotTypeResponseTypeDef",
    {
        "slotTypeId": str,
        "slotTypeName": str,
        "description": str,
        "slotTypeValues": List["SlotTypeValueTypeDef"],
        "valueSelectionSetting": "SlotValueSelectionSettingTypeDef",
        "parentSlotTypeSignature": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

IntentFilterTypeDef = TypedDict(
    "IntentFilterTypeDef",
    {"name": Literal["IntentName"], "values": List[str], "operator": Literal["CO", "EQ"]},
)

IntentSortByTypeDef = TypedDict(
    "IntentSortByTypeDef",
    {
        "attribute": Literal["IntentName", "LastUpdatedDateTime"],
        "order": Literal["Ascending", "Descending"],
    },
)

ListBotAliasesResponseTypeDef = TypedDict(
    "ListBotAliasesResponseTypeDef",
    {"botAliasSummaries": List["BotAliasSummaryTypeDef"], "nextToken": str, "botId": str},
    total=False,
)

ListBotLocalesResponseTypeDef = TypedDict(
    "ListBotLocalesResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "nextToken": str,
        "botLocaleSummaries": List["BotLocaleSummaryTypeDef"],
    },
    total=False,
)

ListBotVersionsResponseTypeDef = TypedDict(
    "ListBotVersionsResponseTypeDef",
    {"botId": str, "botVersionSummaries": List["BotVersionSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListBotsResponseTypeDef = TypedDict(
    "ListBotsResponseTypeDef",
    {"botSummaries": List["BotSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListBuiltInIntentsResponseTypeDef = TypedDict(
    "ListBuiltInIntentsResponseTypeDef",
    {
        "builtInIntentSummaries": List["BuiltInIntentSummaryTypeDef"],
        "nextToken": str,
        "localeId": str,
    },
    total=False,
)

ListBuiltInSlotTypesResponseTypeDef = TypedDict(
    "ListBuiltInSlotTypesResponseTypeDef",
    {
        "builtInSlotTypeSummaries": List["BuiltInSlotTypeSummaryTypeDef"],
        "nextToken": str,
        "localeId": str,
    },
    total=False,
)

ListIntentsResponseTypeDef = TypedDict(
    "ListIntentsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentSummaries": List["IntentSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListSlotTypesResponseTypeDef = TypedDict(
    "ListSlotTypesResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "slotTypeSummaries": List["SlotTypeSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListSlotsResponseTypeDef = TypedDict(
    "ListSlotsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "slotSummaries": List["SlotSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

SlotFilterTypeDef = TypedDict(
    "SlotFilterTypeDef",
    {"name": Literal["SlotName"], "values": List[str], "operator": Literal["CO", "EQ"]},
)

SlotSortByTypeDef = TypedDict(
    "SlotSortByTypeDef",
    {
        "attribute": Literal["SlotName", "LastUpdatedDateTime"],
        "order": Literal["Ascending", "Descending"],
    },
)

SlotTypeFilterTypeDef = TypedDict(
    "SlotTypeFilterTypeDef",
    {"name": Literal["SlotTypeName"], "values": List[str], "operator": Literal["CO", "EQ"]},
)

SlotTypeSortByTypeDef = TypedDict(
    "SlotTypeSortByTypeDef",
    {
        "attribute": Literal["SlotTypeName", "LastUpdatedDateTime"],
        "order": Literal["Ascending", "Descending"],
    },
)

UpdateBotAliasResponseTypeDef = TypedDict(
    "UpdateBotAliasResponseTypeDef",
    {
        "botAliasId": str,
        "botAliasName": str,
        "description": str,
        "botVersion": str,
        "botAliasLocaleSettings": Dict[str, "BotAliasLocaleSettingsTypeDef"],
        "conversationLogSettings": "ConversationLogSettingsTypeDef",
        "sentimentAnalysisSettings": "SentimentAnalysisSettingsTypeDef",
        "botAliasStatus": Literal["Creating", "Available", "Deleting", "Failed"],
        "botId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

UpdateBotLocaleResponseTypeDef = TypedDict(
    "UpdateBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "localeName": str,
        "description": str,
        "nluIntentConfidenceThreshold": float,
        "voiceSettings": "VoiceSettingsTypeDef",
        "botLocaleStatus": Literal[
            "Creating", "Building", "Built", "ReadyExpressTesting", "Failed", "Deleting", "NotBuilt"
        ],
        "failureReasons": List[str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

UpdateBotResponseTypeDef = TypedDict(
    "UpdateBotResponseTypeDef",
    {
        "botId": str,
        "botName": str,
        "description": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": int,
        "botStatus": Literal[
            "Creating", "Available", "Inactive", "Deleting", "Failed", "Versioning"
        ],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

UpdateIntentResponseTypeDef = TypedDict(
    "UpdateIntentResponseTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "description": str,
        "parentIntentSignature": str,
        "sampleUtterances": List["SampleUtteranceTypeDef"],
        "dialogCodeHook": "DialogCodeHookSettingsTypeDef",
        "fulfillmentCodeHook": "FulfillmentCodeHookSettingsTypeDef",
        "slotPriorities": List["SlotPriorityTypeDef"],
        "intentConfirmationSetting": "IntentConfirmationSettingTypeDef",
        "intentClosingSetting": "IntentClosingSettingTypeDef",
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
        "kendraConfiguration": "KendraConfigurationTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

UpdateSlotResponseTypeDef = TypedDict(
    "UpdateSlotResponseTypeDef",
    {
        "slotId": str,
        "slotName": str,
        "description": str,
        "slotTypeId": str,
        "valueElicitationSetting": "SlotValueElicitationSettingTypeDef",
        "obfuscationSetting": "ObfuscationSettingTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

UpdateSlotTypeResponseTypeDef = TypedDict(
    "UpdateSlotTypeResponseTypeDef",
    {
        "slotTypeId": str,
        "slotTypeName": str,
        "description": str,
        "slotTypeValues": List["SlotTypeValueTypeDef"],
        "valueSelectionSetting": "SlotValueSelectionSettingTypeDef",
        "parentSlotTypeSignature": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)
