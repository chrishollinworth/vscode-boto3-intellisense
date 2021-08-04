"""
Type annotations for lex-models service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/literals.html)

Usage::

    ```python
    from mypy_boto3_lex_models.literals import ChannelStatusType

    data: ChannelStatusType = "CREATED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ChannelStatusType",
    "ChannelTypeType",
    "ContentTypeType",
    "DestinationType",
    "ExportStatusType",
    "ExportTypeType",
    "FulfillmentActivityTypeType",
    "GetBotAliasesPaginatorName",
    "GetBotChannelAssociationsPaginatorName",
    "GetBotVersionsPaginatorName",
    "GetBotsPaginatorName",
    "GetBuiltinIntentsPaginatorName",
    "GetBuiltinSlotTypesPaginatorName",
    "GetIntentVersionsPaginatorName",
    "GetIntentsPaginatorName",
    "GetSlotTypeVersionsPaginatorName",
    "GetSlotTypesPaginatorName",
    "ImportStatusType",
    "LocaleType",
    "LogTypeType",
    "MergeStrategyType",
    "MigrationAlertTypeType",
    "MigrationSortAttributeType",
    "MigrationStatusType",
    "MigrationStrategyType",
    "ObfuscationSettingType",
    "ProcessBehaviorType",
    "ResourceTypeType",
    "SlotConstraintType",
    "SlotValueSelectionStrategyType",
    "SortOrderType",
    "StatusType",
    "StatusTypeType",
)

ChannelStatusType = Literal["CREATED", "FAILED", "IN_PROGRESS"]
ChannelTypeType = Literal["Facebook", "Kik", "Slack", "Twilio-Sms"]
ContentTypeType = Literal["CustomPayload", "PlainText", "SSML"]
DestinationType = Literal["CLOUDWATCH_LOGS", "S3"]
ExportStatusType = Literal["FAILED", "IN_PROGRESS", "READY"]
ExportTypeType = Literal["ALEXA_SKILLS_KIT", "LEX"]
FulfillmentActivityTypeType = Literal["CodeHook", "ReturnIntent"]
GetBotAliasesPaginatorName = Literal["get_bot_aliases"]
GetBotChannelAssociationsPaginatorName = Literal["get_bot_channel_associations"]
GetBotVersionsPaginatorName = Literal["get_bot_versions"]
GetBotsPaginatorName = Literal["get_bots"]
GetBuiltinIntentsPaginatorName = Literal["get_builtin_intents"]
GetBuiltinSlotTypesPaginatorName = Literal["get_builtin_slot_types"]
GetIntentVersionsPaginatorName = Literal["get_intent_versions"]
GetIntentsPaginatorName = Literal["get_intents"]
GetSlotTypeVersionsPaginatorName = Literal["get_slot_type_versions"]
GetSlotTypesPaginatorName = Literal["get_slot_types"]
ImportStatusType = Literal["COMPLETE", "FAILED", "IN_PROGRESS"]
LocaleType = Literal[
    "de-DE",
    "en-AU",
    "en-GB",
    "en-IN",
    "en-US",
    "es-419",
    "es-ES",
    "es-US",
    "fr-CA",
    "fr-FR",
    "it-IT",
    "ja-JP",
]
LogTypeType = Literal["AUDIO", "TEXT"]
MergeStrategyType = Literal["FAIL_ON_CONFLICT", "OVERWRITE_LATEST"]
MigrationAlertTypeType = Literal["ERROR", "WARN"]
MigrationSortAttributeType = Literal["MIGRATION_DATE_TIME", "V1_BOT_NAME"]
MigrationStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS"]
MigrationStrategyType = Literal["CREATE_NEW", "UPDATE_EXISTING"]
ObfuscationSettingType = Literal["DEFAULT_OBFUSCATION", "NONE"]
ProcessBehaviorType = Literal["BUILD", "SAVE"]
ResourceTypeType = Literal["BOT", "INTENT", "SLOT_TYPE"]
SlotConstraintType = Literal["Optional", "Required"]
SlotValueSelectionStrategyType = Literal["ORIGINAL_VALUE", "TOP_RESOLUTION"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
StatusType = Literal["BUILDING", "FAILED", "NOT_BUILT", "READY", "READY_BASIC_TESTING"]
StatusTypeType = Literal["Detected", "Missed"]
