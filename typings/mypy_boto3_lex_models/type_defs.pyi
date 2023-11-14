"""
Type annotations for lex-models service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lex_models.type_defs import BotAliasMetadataTypeDef

    data: BotAliasMetadataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ChannelStatusType,
    ChannelTypeType,
    ContentTypeType,
    DestinationType,
    ExportStatusType,
    ExportTypeType,
    FulfillmentActivityTypeType,
    ImportStatusType,
    LocaleType,
    LogTypeType,
    MergeStrategyType,
    MigrationAlertTypeType,
    MigrationSortAttributeType,
    MigrationStatusType,
    MigrationStrategyType,
    ObfuscationSettingType,
    ProcessBehaviorType,
    ResourceTypeType,
    SlotConstraintType,
    SlotValueSelectionStrategyType,
    SortOrderType,
    StatusType,
    StatusTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BotAliasMetadataTypeDef",
    "BotChannelAssociationTypeDef",
    "BotMetadataTypeDef",
    "BuiltinIntentMetadataTypeDef",
    "BuiltinIntentSlotTypeDef",
    "BuiltinSlotTypeMetadataTypeDef",
    "CodeHookTypeDef",
    "ConversationLogsRequestTypeDef",
    "ConversationLogsResponseTypeDef",
    "CreateBotVersionRequestRequestTypeDef",
    "CreateBotVersionResponseTypeDef",
    "CreateIntentVersionRequestRequestTypeDef",
    "CreateIntentVersionResponseTypeDef",
    "CreateSlotTypeVersionRequestRequestTypeDef",
    "CreateSlotTypeVersionResponseTypeDef",
    "DeleteBotAliasRequestRequestTypeDef",
    "DeleteBotChannelAssociationRequestRequestTypeDef",
    "DeleteBotRequestRequestTypeDef",
    "DeleteBotVersionRequestRequestTypeDef",
    "DeleteIntentRequestRequestTypeDef",
    "DeleteIntentVersionRequestRequestTypeDef",
    "DeleteSlotTypeRequestRequestTypeDef",
    "DeleteSlotTypeVersionRequestRequestTypeDef",
    "DeleteUtterancesRequestRequestTypeDef",
    "EnumerationValueTypeDef",
    "FollowUpPromptTypeDef",
    "FulfillmentActivityTypeDef",
    "GetBotAliasRequestRequestTypeDef",
    "GetBotAliasResponseTypeDef",
    "GetBotAliasesRequestRequestTypeDef",
    "GetBotAliasesResponseTypeDef",
    "GetBotChannelAssociationRequestRequestTypeDef",
    "GetBotChannelAssociationResponseTypeDef",
    "GetBotChannelAssociationsRequestRequestTypeDef",
    "GetBotChannelAssociationsResponseTypeDef",
    "GetBotRequestRequestTypeDef",
    "GetBotResponseTypeDef",
    "GetBotVersionsRequestRequestTypeDef",
    "GetBotVersionsResponseTypeDef",
    "GetBotsRequestRequestTypeDef",
    "GetBotsResponseTypeDef",
    "GetBuiltinIntentRequestRequestTypeDef",
    "GetBuiltinIntentResponseTypeDef",
    "GetBuiltinIntentsRequestRequestTypeDef",
    "GetBuiltinIntentsResponseTypeDef",
    "GetBuiltinSlotTypesRequestRequestTypeDef",
    "GetBuiltinSlotTypesResponseTypeDef",
    "GetExportRequestRequestTypeDef",
    "GetExportResponseTypeDef",
    "GetImportRequestRequestTypeDef",
    "GetImportResponseTypeDef",
    "GetIntentRequestRequestTypeDef",
    "GetIntentResponseTypeDef",
    "GetIntentVersionsRequestRequestTypeDef",
    "GetIntentVersionsResponseTypeDef",
    "GetIntentsRequestRequestTypeDef",
    "GetIntentsResponseTypeDef",
    "GetMigrationRequestRequestTypeDef",
    "GetMigrationResponseTypeDef",
    "GetMigrationsRequestRequestTypeDef",
    "GetMigrationsResponseTypeDef",
    "GetSlotTypeRequestRequestTypeDef",
    "GetSlotTypeResponseTypeDef",
    "GetSlotTypeVersionsRequestRequestTypeDef",
    "GetSlotTypeVersionsResponseTypeDef",
    "GetSlotTypesRequestRequestTypeDef",
    "GetSlotTypesResponseTypeDef",
    "GetUtterancesViewRequestRequestTypeDef",
    "GetUtterancesViewResponseTypeDef",
    "InputContextTypeDef",
    "IntentMetadataTypeDef",
    "IntentTypeDef",
    "KendraConfigurationTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogSettingsRequestTypeDef",
    "LogSettingsResponseTypeDef",
    "MessageTypeDef",
    "MigrationAlertTypeDef",
    "MigrationSummaryTypeDef",
    "OutputContextTypeDef",
    "PaginatorConfigTypeDef",
    "PromptTypeDef",
    "PutBotAliasRequestRequestTypeDef",
    "PutBotAliasResponseTypeDef",
    "PutBotRequestRequestTypeDef",
    "PutBotResponseTypeDef",
    "PutIntentRequestRequestTypeDef",
    "PutIntentResponseTypeDef",
    "PutSlotTypeRequestRequestTypeDef",
    "PutSlotTypeResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SlotDefaultValueSpecTypeDef",
    "SlotDefaultValueTypeDef",
    "SlotTypeConfigurationTypeDef",
    "SlotTypeDef",
    "SlotTypeMetadataTypeDef",
    "SlotTypeRegexConfigurationTypeDef",
    "StartImportRequestRequestTypeDef",
    "StartImportResponseTypeDef",
    "StartMigrationRequestRequestTypeDef",
    "StartMigrationResponseTypeDef",
    "StatementTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UtteranceDataTypeDef",
    "UtteranceListTypeDef",
)

BotAliasMetadataTypeDef = TypedDict(
    "BotAliasMetadataTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
        "conversationLogs": "ConversationLogsResponseTypeDef",
    },
    total=False,
)

BotChannelAssociationTypeDef = TypedDict(
    "BotChannelAssociationTypeDef",
    {
        "name": str,
        "description": str,
        "botAlias": str,
        "botName": str,
        "createdDate": datetime,
        "type": ChannelTypeType,
        "botConfiguration": Dict[str, str],
        "status": ChannelStatusType,
        "failureReason": str,
    },
    total=False,
)

BotMetadataTypeDef = TypedDict(
    "BotMetadataTypeDef",
    {
        "name": str,
        "description": str,
        "status": StatusType,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)

BuiltinIntentMetadataTypeDef = TypedDict(
    "BuiltinIntentMetadataTypeDef",
    {
        "signature": str,
        "supportedLocales": List[LocaleType],
    },
    total=False,
)

BuiltinIntentSlotTypeDef = TypedDict(
    "BuiltinIntentSlotTypeDef",
    {
        "name": str,
    },
    total=False,
)

BuiltinSlotTypeMetadataTypeDef = TypedDict(
    "BuiltinSlotTypeMetadataTypeDef",
    {
        "signature": str,
        "supportedLocales": List[LocaleType],
    },
    total=False,
)

CodeHookTypeDef = TypedDict(
    "CodeHookTypeDef",
    {
        "uri": str,
        "messageVersion": str,
    },
)

ConversationLogsRequestTypeDef = TypedDict(
    "ConversationLogsRequestTypeDef",
    {
        "logSettings": List["LogSettingsRequestTypeDef"],
        "iamRoleArn": str,
    },
)

ConversationLogsResponseTypeDef = TypedDict(
    "ConversationLogsResponseTypeDef",
    {
        "logSettings": List["LogSettingsResponseTypeDef"],
        "iamRoleArn": str,
    },
    total=False,
)

_RequiredCreateBotVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBotVersionRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateBotVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBotVersionRequestRequestTypeDef",
    {
        "checksum": str,
    },
    total=False,
)

class CreateBotVersionRequestRequestTypeDef(
    _RequiredCreateBotVersionRequestRequestTypeDef, _OptionalCreateBotVersionRequestRequestTypeDef
):
    pass

CreateBotVersionResponseTypeDef = TypedDict(
    "CreateBotVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List["IntentTypeDef"],
        "clarificationPrompt": "PromptTypeDef",
        "abortStatement": "StatementTypeDef",
        "status": StatusType,
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": LocaleType,
        "childDirected": bool,
        "enableModelImprovements": bool,
        "detectSentiment": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIntentVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIntentVersionRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateIntentVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIntentVersionRequestRequestTypeDef",
    {
        "checksum": str,
    },
    total=False,
)

class CreateIntentVersionRequestRequestTypeDef(
    _RequiredCreateIntentVersionRequestRequestTypeDef,
    _OptionalCreateIntentVersionRequestRequestTypeDef,
):
    pass

CreateIntentVersionResponseTypeDef = TypedDict(
    "CreateIntentVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List["SlotTypeDef"],
        "sampleUtterances": List[str],
        "confirmationPrompt": "PromptTypeDef",
        "rejectionStatement": "StatementTypeDef",
        "followUpPrompt": "FollowUpPromptTypeDef",
        "conclusionStatement": "StatementTypeDef",
        "dialogCodeHook": "CodeHookTypeDef",
        "fulfillmentActivity": "FulfillmentActivityTypeDef",
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "kendraConfiguration": "KendraConfigurationTypeDef",
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSlotTypeVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSlotTypeVersionRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateSlotTypeVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSlotTypeVersionRequestRequestTypeDef",
    {
        "checksum": str,
    },
    total=False,
)

class CreateSlotTypeVersionRequestRequestTypeDef(
    _RequiredCreateSlotTypeVersionRequestRequestTypeDef,
    _OptionalCreateSlotTypeVersionRequestRequestTypeDef,
):
    pass

CreateSlotTypeVersionResponseTypeDef = TypedDict(
    "CreateSlotTypeVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List["EnumerationValueTypeDef"],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": SlotValueSelectionStrategyType,
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": List["SlotTypeConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBotAliasRequestRequestTypeDef = TypedDict(
    "DeleteBotAliasRequestRequestTypeDef",
    {
        "name": str,
        "botName": str,
    },
)

DeleteBotChannelAssociationRequestRequestTypeDef = TypedDict(
    "DeleteBotChannelAssociationRequestRequestTypeDef",
    {
        "name": str,
        "botName": str,
        "botAlias": str,
    },
)

DeleteBotRequestRequestTypeDef = TypedDict(
    "DeleteBotRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteBotVersionRequestRequestTypeDef = TypedDict(
    "DeleteBotVersionRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)

DeleteIntentRequestRequestTypeDef = TypedDict(
    "DeleteIntentRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteIntentVersionRequestRequestTypeDef = TypedDict(
    "DeleteIntentVersionRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)

DeleteSlotTypeRequestRequestTypeDef = TypedDict(
    "DeleteSlotTypeRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteSlotTypeVersionRequestRequestTypeDef = TypedDict(
    "DeleteSlotTypeVersionRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)

DeleteUtterancesRequestRequestTypeDef = TypedDict(
    "DeleteUtterancesRequestRequestTypeDef",
    {
        "botName": str,
        "userId": str,
    },
)

_RequiredEnumerationValueTypeDef = TypedDict(
    "_RequiredEnumerationValueTypeDef",
    {
        "value": str,
    },
)
_OptionalEnumerationValueTypeDef = TypedDict(
    "_OptionalEnumerationValueTypeDef",
    {
        "synonyms": List[str],
    },
    total=False,
)

class EnumerationValueTypeDef(_RequiredEnumerationValueTypeDef, _OptionalEnumerationValueTypeDef):
    pass

FollowUpPromptTypeDef = TypedDict(
    "FollowUpPromptTypeDef",
    {
        "prompt": "PromptTypeDef",
        "rejectionStatement": "StatementTypeDef",
    },
)

_RequiredFulfillmentActivityTypeDef = TypedDict(
    "_RequiredFulfillmentActivityTypeDef",
    {
        "type": FulfillmentActivityTypeType,
    },
)
_OptionalFulfillmentActivityTypeDef = TypedDict(
    "_OptionalFulfillmentActivityTypeDef",
    {
        "codeHook": "CodeHookTypeDef",
    },
    total=False,
)

class FulfillmentActivityTypeDef(
    _RequiredFulfillmentActivityTypeDef, _OptionalFulfillmentActivityTypeDef
):
    pass

GetBotAliasRequestRequestTypeDef = TypedDict(
    "GetBotAliasRequestRequestTypeDef",
    {
        "name": str,
        "botName": str,
    },
)

GetBotAliasResponseTypeDef = TypedDict(
    "GetBotAliasResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
        "conversationLogs": "ConversationLogsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBotAliasesRequestRequestTypeDef = TypedDict(
    "_RequiredGetBotAliasesRequestRequestTypeDef",
    {
        "botName": str,
    },
)
_OptionalGetBotAliasesRequestRequestTypeDef = TypedDict(
    "_OptionalGetBotAliasesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "nameContains": str,
    },
    total=False,
)

class GetBotAliasesRequestRequestTypeDef(
    _RequiredGetBotAliasesRequestRequestTypeDef, _OptionalGetBotAliasesRequestRequestTypeDef
):
    pass

GetBotAliasesResponseTypeDef = TypedDict(
    "GetBotAliasesResponseTypeDef",
    {
        "BotAliases": List["BotAliasMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBotChannelAssociationRequestRequestTypeDef = TypedDict(
    "GetBotChannelAssociationRequestRequestTypeDef",
    {
        "name": str,
        "botName": str,
        "botAlias": str,
    },
)

GetBotChannelAssociationResponseTypeDef = TypedDict(
    "GetBotChannelAssociationResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botAlias": str,
        "botName": str,
        "createdDate": datetime,
        "type": ChannelTypeType,
        "botConfiguration": Dict[str, str],
        "status": ChannelStatusType,
        "failureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBotChannelAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetBotChannelAssociationsRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
    },
)
_OptionalGetBotChannelAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetBotChannelAssociationsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "nameContains": str,
    },
    total=False,
)

class GetBotChannelAssociationsRequestRequestTypeDef(
    _RequiredGetBotChannelAssociationsRequestRequestTypeDef,
    _OptionalGetBotChannelAssociationsRequestRequestTypeDef,
):
    pass

GetBotChannelAssociationsResponseTypeDef = TypedDict(
    "GetBotChannelAssociationsResponseTypeDef",
    {
        "botChannelAssociations": List["BotChannelAssociationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBotRequestRequestTypeDef = TypedDict(
    "GetBotRequestRequestTypeDef",
    {
        "name": str,
        "versionOrAlias": str,
    },
)

GetBotResponseTypeDef = TypedDict(
    "GetBotResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List["IntentTypeDef"],
        "enableModelImprovements": bool,
        "nluIntentConfidenceThreshold": float,
        "clarificationPrompt": "PromptTypeDef",
        "abortStatement": "StatementTypeDef",
        "status": StatusType,
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": LocaleType,
        "childDirected": bool,
        "detectSentiment": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBotVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredGetBotVersionsRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalGetBotVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalGetBotVersionsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetBotVersionsRequestRequestTypeDef(
    _RequiredGetBotVersionsRequestRequestTypeDef, _OptionalGetBotVersionsRequestRequestTypeDef
):
    pass

GetBotVersionsResponseTypeDef = TypedDict(
    "GetBotVersionsResponseTypeDef",
    {
        "bots": List["BotMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBotsRequestRequestTypeDef = TypedDict(
    "GetBotsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "nameContains": str,
    },
    total=False,
)

GetBotsResponseTypeDef = TypedDict(
    "GetBotsResponseTypeDef",
    {
        "bots": List["BotMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBuiltinIntentRequestRequestTypeDef = TypedDict(
    "GetBuiltinIntentRequestRequestTypeDef",
    {
        "signature": str,
    },
)

GetBuiltinIntentResponseTypeDef = TypedDict(
    "GetBuiltinIntentResponseTypeDef",
    {
        "signature": str,
        "supportedLocales": List[LocaleType],
        "slots": List["BuiltinIntentSlotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBuiltinIntentsRequestRequestTypeDef = TypedDict(
    "GetBuiltinIntentsRequestRequestTypeDef",
    {
        "locale": LocaleType,
        "signatureContains": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetBuiltinIntentsResponseTypeDef = TypedDict(
    "GetBuiltinIntentsResponseTypeDef",
    {
        "intents": List["BuiltinIntentMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBuiltinSlotTypesRequestRequestTypeDef = TypedDict(
    "GetBuiltinSlotTypesRequestRequestTypeDef",
    {
        "locale": LocaleType,
        "signatureContains": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetBuiltinSlotTypesResponseTypeDef = TypedDict(
    "GetBuiltinSlotTypesResponseTypeDef",
    {
        "slotTypes": List["BuiltinSlotTypeMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExportRequestRequestTypeDef = TypedDict(
    "GetExportRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
        "resourceType": ResourceTypeType,
        "exportType": ExportTypeType,
    },
)

GetExportResponseTypeDef = TypedDict(
    "GetExportResponseTypeDef",
    {
        "name": str,
        "version": str,
        "resourceType": ResourceTypeType,
        "exportType": ExportTypeType,
        "exportStatus": ExportStatusType,
        "failureReason": str,
        "url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImportRequestRequestTypeDef = TypedDict(
    "GetImportRequestRequestTypeDef",
    {
        "importId": str,
    },
)

GetImportResponseTypeDef = TypedDict(
    "GetImportResponseTypeDef",
    {
        "name": str,
        "resourceType": ResourceTypeType,
        "mergeStrategy": MergeStrategyType,
        "importId": str,
        "importStatus": ImportStatusType,
        "failureReason": List[str],
        "createdDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIntentRequestRequestTypeDef = TypedDict(
    "GetIntentRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)

GetIntentResponseTypeDef = TypedDict(
    "GetIntentResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List["SlotTypeDef"],
        "sampleUtterances": List[str],
        "confirmationPrompt": "PromptTypeDef",
        "rejectionStatement": "StatementTypeDef",
        "followUpPrompt": "FollowUpPromptTypeDef",
        "conclusionStatement": "StatementTypeDef",
        "dialogCodeHook": "CodeHookTypeDef",
        "fulfillmentActivity": "FulfillmentActivityTypeDef",
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "kendraConfiguration": "KendraConfigurationTypeDef",
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetIntentVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredGetIntentVersionsRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalGetIntentVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalGetIntentVersionsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetIntentVersionsRequestRequestTypeDef(
    _RequiredGetIntentVersionsRequestRequestTypeDef, _OptionalGetIntentVersionsRequestRequestTypeDef
):
    pass

GetIntentVersionsResponseTypeDef = TypedDict(
    "GetIntentVersionsResponseTypeDef",
    {
        "intents": List["IntentMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIntentsRequestRequestTypeDef = TypedDict(
    "GetIntentsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "nameContains": str,
    },
    total=False,
)

GetIntentsResponseTypeDef = TypedDict(
    "GetIntentsResponseTypeDef",
    {
        "intents": List["IntentMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMigrationRequestRequestTypeDef = TypedDict(
    "GetMigrationRequestRequestTypeDef",
    {
        "migrationId": str,
    },
)

GetMigrationResponseTypeDef = TypedDict(
    "GetMigrationResponseTypeDef",
    {
        "migrationId": str,
        "v1BotName": str,
        "v1BotVersion": str,
        "v1BotLocale": LocaleType,
        "v2BotId": str,
        "v2BotRole": str,
        "migrationStatus": MigrationStatusType,
        "migrationStrategy": MigrationStrategyType,
        "migrationTimestamp": datetime,
        "alerts": List["MigrationAlertTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMigrationsRequestRequestTypeDef = TypedDict(
    "GetMigrationsRequestRequestTypeDef",
    {
        "sortByAttribute": MigrationSortAttributeType,
        "sortByOrder": SortOrderType,
        "v1BotNameContains": str,
        "migrationStatusEquals": MigrationStatusType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

GetMigrationsResponseTypeDef = TypedDict(
    "GetMigrationsResponseTypeDef",
    {
        "migrationSummaries": List["MigrationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSlotTypeRequestRequestTypeDef = TypedDict(
    "GetSlotTypeRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)

GetSlotTypeResponseTypeDef = TypedDict(
    "GetSlotTypeResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List["EnumerationValueTypeDef"],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": SlotValueSelectionStrategyType,
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": List["SlotTypeConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSlotTypeVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredGetSlotTypeVersionsRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalGetSlotTypeVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalGetSlotTypeVersionsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetSlotTypeVersionsRequestRequestTypeDef(
    _RequiredGetSlotTypeVersionsRequestRequestTypeDef,
    _OptionalGetSlotTypeVersionsRequestRequestTypeDef,
):
    pass

GetSlotTypeVersionsResponseTypeDef = TypedDict(
    "GetSlotTypeVersionsResponseTypeDef",
    {
        "slotTypes": List["SlotTypeMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSlotTypesRequestRequestTypeDef = TypedDict(
    "GetSlotTypesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "nameContains": str,
    },
    total=False,
)

GetSlotTypesResponseTypeDef = TypedDict(
    "GetSlotTypesResponseTypeDef",
    {
        "slotTypes": List["SlotTypeMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUtterancesViewRequestRequestTypeDef = TypedDict(
    "GetUtterancesViewRequestRequestTypeDef",
    {
        "botName": str,
        "botVersions": List[str],
        "statusType": StatusTypeType,
    },
)

GetUtterancesViewResponseTypeDef = TypedDict(
    "GetUtterancesViewResponseTypeDef",
    {
        "botName": str,
        "utterances": List["UtteranceListTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputContextTypeDef = TypedDict(
    "InputContextTypeDef",
    {
        "name": str,
    },
)

IntentMetadataTypeDef = TypedDict(
    "IntentMetadataTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)

IntentTypeDef = TypedDict(
    "IntentTypeDef",
    {
        "intentName": str,
        "intentVersion": str,
    },
)

_RequiredKendraConfigurationTypeDef = TypedDict(
    "_RequiredKendraConfigurationTypeDef",
    {
        "kendraIndex": str,
        "role": str,
    },
)
_OptionalKendraConfigurationTypeDef = TypedDict(
    "_OptionalKendraConfigurationTypeDef",
    {
        "queryFilterString": str,
    },
    total=False,
)

class KendraConfigurationTypeDef(
    _RequiredKendraConfigurationTypeDef, _OptionalKendraConfigurationTypeDef
):
    pass

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLogSettingsRequestTypeDef = TypedDict(
    "_RequiredLogSettingsRequestTypeDef",
    {
        "logType": LogTypeType,
        "destination": DestinationType,
        "resourceArn": str,
    },
)
_OptionalLogSettingsRequestTypeDef = TypedDict(
    "_OptionalLogSettingsRequestTypeDef",
    {
        "kmsKeyArn": str,
    },
    total=False,
)

class LogSettingsRequestTypeDef(
    _RequiredLogSettingsRequestTypeDef, _OptionalLogSettingsRequestTypeDef
):
    pass

LogSettingsResponseTypeDef = TypedDict(
    "LogSettingsResponseTypeDef",
    {
        "logType": LogTypeType,
        "destination": DestinationType,
        "kmsKeyArn": str,
        "resourceArn": str,
        "resourcePrefix": str,
    },
    total=False,
)

_RequiredMessageTypeDef = TypedDict(
    "_RequiredMessageTypeDef",
    {
        "contentType": ContentTypeType,
        "content": str,
    },
)
_OptionalMessageTypeDef = TypedDict(
    "_OptionalMessageTypeDef",
    {
        "groupNumber": int,
    },
    total=False,
)

class MessageTypeDef(_RequiredMessageTypeDef, _OptionalMessageTypeDef):
    pass

MigrationAlertTypeDef = TypedDict(
    "MigrationAlertTypeDef",
    {
        "type": MigrationAlertTypeType,
        "message": str,
        "details": List[str],
        "referenceURLs": List[str],
    },
    total=False,
)

MigrationSummaryTypeDef = TypedDict(
    "MigrationSummaryTypeDef",
    {
        "migrationId": str,
        "v1BotName": str,
        "v1BotVersion": str,
        "v1BotLocale": LocaleType,
        "v2BotId": str,
        "v2BotRole": str,
        "migrationStatus": MigrationStatusType,
        "migrationStrategy": MigrationStrategyType,
        "migrationTimestamp": datetime,
    },
    total=False,
)

OutputContextTypeDef = TypedDict(
    "OutputContextTypeDef",
    {
        "name": str,
        "timeToLiveInSeconds": int,
        "turnsToLive": int,
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredPromptTypeDef = TypedDict(
    "_RequiredPromptTypeDef",
    {
        "messages": List["MessageTypeDef"],
        "maxAttempts": int,
    },
)
_OptionalPromptTypeDef = TypedDict(
    "_OptionalPromptTypeDef",
    {
        "responseCard": str,
    },
    total=False,
)

class PromptTypeDef(_RequiredPromptTypeDef, _OptionalPromptTypeDef):
    pass

_RequiredPutBotAliasRequestRequestTypeDef = TypedDict(
    "_RequiredPutBotAliasRequestRequestTypeDef",
    {
        "name": str,
        "botVersion": str,
        "botName": str,
    },
)
_OptionalPutBotAliasRequestRequestTypeDef = TypedDict(
    "_OptionalPutBotAliasRequestRequestTypeDef",
    {
        "description": str,
        "checksum": str,
        "conversationLogs": "ConversationLogsRequestTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class PutBotAliasRequestRequestTypeDef(
    _RequiredPutBotAliasRequestRequestTypeDef, _OptionalPutBotAliasRequestRequestTypeDef
):
    pass

PutBotAliasResponseTypeDef = TypedDict(
    "PutBotAliasResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
        "conversationLogs": "ConversationLogsResponseTypeDef",
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutBotRequestRequestTypeDef = TypedDict(
    "_RequiredPutBotRequestRequestTypeDef",
    {
        "name": str,
        "locale": LocaleType,
        "childDirected": bool,
    },
)
_OptionalPutBotRequestRequestTypeDef = TypedDict(
    "_OptionalPutBotRequestRequestTypeDef",
    {
        "description": str,
        "intents": List["IntentTypeDef"],
        "enableModelImprovements": bool,
        "nluIntentConfidenceThreshold": float,
        "clarificationPrompt": "PromptTypeDef",
        "abortStatement": "StatementTypeDef",
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "processBehavior": ProcessBehaviorType,
        "detectSentiment": bool,
        "createVersion": bool,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class PutBotRequestRequestTypeDef(
    _RequiredPutBotRequestRequestTypeDef, _OptionalPutBotRequestRequestTypeDef
):
    pass

PutBotResponseTypeDef = TypedDict(
    "PutBotResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List["IntentTypeDef"],
        "enableModelImprovements": bool,
        "nluIntentConfidenceThreshold": float,
        "clarificationPrompt": "PromptTypeDef",
        "abortStatement": "StatementTypeDef",
        "status": StatusType,
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": LocaleType,
        "childDirected": bool,
        "createVersion": bool,
        "detectSentiment": bool,
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutIntentRequestRequestTypeDef = TypedDict(
    "_RequiredPutIntentRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalPutIntentRequestRequestTypeDef = TypedDict(
    "_OptionalPutIntentRequestRequestTypeDef",
    {
        "description": str,
        "slots": List["SlotTypeDef"],
        "sampleUtterances": List[str],
        "confirmationPrompt": "PromptTypeDef",
        "rejectionStatement": "StatementTypeDef",
        "followUpPrompt": "FollowUpPromptTypeDef",
        "conclusionStatement": "StatementTypeDef",
        "dialogCodeHook": "CodeHookTypeDef",
        "fulfillmentActivity": "FulfillmentActivityTypeDef",
        "parentIntentSignature": str,
        "checksum": str,
        "createVersion": bool,
        "kendraConfiguration": "KendraConfigurationTypeDef",
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
    },
    total=False,
)

class PutIntentRequestRequestTypeDef(
    _RequiredPutIntentRequestRequestTypeDef, _OptionalPutIntentRequestRequestTypeDef
):
    pass

PutIntentResponseTypeDef = TypedDict(
    "PutIntentResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List["SlotTypeDef"],
        "sampleUtterances": List[str],
        "confirmationPrompt": "PromptTypeDef",
        "rejectionStatement": "StatementTypeDef",
        "followUpPrompt": "FollowUpPromptTypeDef",
        "conclusionStatement": "StatementTypeDef",
        "dialogCodeHook": "CodeHookTypeDef",
        "fulfillmentActivity": "FulfillmentActivityTypeDef",
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "createVersion": bool,
        "kendraConfiguration": "KendraConfigurationTypeDef",
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutSlotTypeRequestRequestTypeDef = TypedDict(
    "_RequiredPutSlotTypeRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalPutSlotTypeRequestRequestTypeDef = TypedDict(
    "_OptionalPutSlotTypeRequestRequestTypeDef",
    {
        "description": str,
        "enumerationValues": List["EnumerationValueTypeDef"],
        "checksum": str,
        "valueSelectionStrategy": SlotValueSelectionStrategyType,
        "createVersion": bool,
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": List["SlotTypeConfigurationTypeDef"],
    },
    total=False,
)

class PutSlotTypeRequestRequestTypeDef(
    _RequiredPutSlotTypeRequestRequestTypeDef, _OptionalPutSlotTypeRequestRequestTypeDef
):
    pass

PutSlotTypeResponseTypeDef = TypedDict(
    "PutSlotTypeResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List["EnumerationValueTypeDef"],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": SlotValueSelectionStrategyType,
        "createVersion": bool,
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": List["SlotTypeConfigurationTypeDef"],
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

SlotDefaultValueSpecTypeDef = TypedDict(
    "SlotDefaultValueSpecTypeDef",
    {
        "defaultValueList": List["SlotDefaultValueTypeDef"],
    },
)

SlotDefaultValueTypeDef = TypedDict(
    "SlotDefaultValueTypeDef",
    {
        "defaultValue": str,
    },
)

SlotTypeConfigurationTypeDef = TypedDict(
    "SlotTypeConfigurationTypeDef",
    {
        "regexConfiguration": "SlotTypeRegexConfigurationTypeDef",
    },
    total=False,
)

_RequiredSlotTypeDef = TypedDict(
    "_RequiredSlotTypeDef",
    {
        "name": str,
        "slotConstraint": SlotConstraintType,
    },
)
_OptionalSlotTypeDef = TypedDict(
    "_OptionalSlotTypeDef",
    {
        "description": str,
        "slotType": str,
        "slotTypeVersion": str,
        "valueElicitationPrompt": "PromptTypeDef",
        "priority": int,
        "sampleUtterances": List[str],
        "responseCard": str,
        "obfuscationSetting": ObfuscationSettingType,
        "defaultValueSpec": "SlotDefaultValueSpecTypeDef",
    },
    total=False,
)

class SlotTypeDef(_RequiredSlotTypeDef, _OptionalSlotTypeDef):
    pass

SlotTypeMetadataTypeDef = TypedDict(
    "SlotTypeMetadataTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)

SlotTypeRegexConfigurationTypeDef = TypedDict(
    "SlotTypeRegexConfigurationTypeDef",
    {
        "pattern": str,
    },
)

_RequiredStartImportRequestRequestTypeDef = TypedDict(
    "_RequiredStartImportRequestRequestTypeDef",
    {
        "payload": Union[bytes, IO[bytes], StreamingBody],
        "resourceType": ResourceTypeType,
        "mergeStrategy": MergeStrategyType,
    },
)
_OptionalStartImportRequestRequestTypeDef = TypedDict(
    "_OptionalStartImportRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class StartImportRequestRequestTypeDef(
    _RequiredStartImportRequestRequestTypeDef, _OptionalStartImportRequestRequestTypeDef
):
    pass

StartImportResponseTypeDef = TypedDict(
    "StartImportResponseTypeDef",
    {
        "name": str,
        "resourceType": ResourceTypeType,
        "mergeStrategy": MergeStrategyType,
        "importId": str,
        "importStatus": ImportStatusType,
        "tags": List["TagTypeDef"],
        "createdDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartMigrationRequestRequestTypeDef = TypedDict(
    "StartMigrationRequestRequestTypeDef",
    {
        "v1BotName": str,
        "v1BotVersion": str,
        "v2BotName": str,
        "v2BotRole": str,
        "migrationStrategy": MigrationStrategyType,
    },
)

StartMigrationResponseTypeDef = TypedDict(
    "StartMigrationResponseTypeDef",
    {
        "v1BotName": str,
        "v1BotVersion": str,
        "v1BotLocale": LocaleType,
        "v2BotId": str,
        "v2BotRole": str,
        "migrationId": str,
        "migrationStrategy": MigrationStrategyType,
        "migrationTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStatementTypeDef = TypedDict(
    "_RequiredStatementTypeDef",
    {
        "messages": List["MessageTypeDef"],
    },
)
_OptionalStatementTypeDef = TypedDict(
    "_OptionalStatementTypeDef",
    {
        "responseCard": str,
    },
    total=False,
)

class StatementTypeDef(_RequiredStatementTypeDef, _OptionalStatementTypeDef):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UtteranceDataTypeDef = TypedDict(
    "UtteranceDataTypeDef",
    {
        "utteranceString": str,
        "count": int,
        "distinctUsers": int,
        "firstUtteredDate": datetime,
        "lastUtteredDate": datetime,
    },
    total=False,
)

UtteranceListTypeDef = TypedDict(
    "UtteranceListTypeDef",
    {
        "botVersion": str,
        "utterances": List["UtteranceDataTypeDef"],
    },
    total=False,
)
