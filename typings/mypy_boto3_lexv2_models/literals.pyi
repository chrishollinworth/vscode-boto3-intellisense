"""
Type annotations for lexv2-models service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/literals.html)

Usage::

    ```python
    from mypy_boto3_lexv2_models.literals import AggregatedUtterancesFilterNameType

    data: AggregatedUtterancesFilterNameType = "Utterance"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AggregatedUtterancesFilterNameType",
    "AggregatedUtterancesFilterOperatorType",
    "AggregatedUtterancesSortAttributeType",
    "AssociatedTranscriptFilterNameType",
    "AudioRecognitionStrategyType",
    "BotAliasAvailableWaiterName",
    "BotAliasStatusType",
    "BotAvailableWaiterName",
    "BotExportCompletedWaiterName",
    "BotFilterNameType",
    "BotFilterOperatorType",
    "BotImportCompletedWaiterName",
    "BotLocaleBuiltWaiterName",
    "BotLocaleCreatedWaiterName",
    "BotLocaleExpressTestingAvailableWaiterName",
    "BotLocaleFilterNameType",
    "BotLocaleFilterOperatorType",
    "BotLocaleSortAttributeType",
    "BotLocaleStatusType",
    "BotRecommendationStatusType",
    "BotSortAttributeType",
    "BotStatusType",
    "BotTypeType",
    "BotVersionAvailableWaiterName",
    "BotVersionSortAttributeType",
    "BuiltInIntentSortAttributeType",
    "BuiltInSlotTypeSortAttributeType",
    "CustomVocabularyStatusType",
    "DialogActionTypeType",
    "EffectType",
    "ErrorCodeType",
    "ExportFilterNameType",
    "ExportFilterOperatorType",
    "ExportSortAttributeType",
    "ExportStatusType",
    "ImportExportFileFormatType",
    "ImportFilterNameType",
    "ImportFilterOperatorType",
    "ImportResourceTypeType",
    "ImportSortAttributeType",
    "ImportStatusType",
    "IntentFilterNameType",
    "IntentFilterOperatorType",
    "IntentSortAttributeType",
    "MergeStrategyType",
    "MessageSelectionStrategyType",
    "ObfuscationSettingTypeType",
    "PromptAttemptType",
    "SearchOrderType",
    "SlotConstraintType",
    "SlotFilterNameType",
    "SlotFilterOperatorType",
    "SlotShapeType",
    "SlotSortAttributeType",
    "SlotTypeCategoryType",
    "SlotTypeFilterNameType",
    "SlotTypeFilterOperatorType",
    "SlotTypeSortAttributeType",
    "SlotValueResolutionStrategyType",
    "SortOrderType",
    "TimeDimensionType",
    "TranscriptFormatType",
    "VoiceEngineType",
)

AggregatedUtterancesFilterNameType = Literal["Utterance"]
AggregatedUtterancesFilterOperatorType = Literal["CO", "EQ"]
AggregatedUtterancesSortAttributeType = Literal["HitCount", "MissedCount"]
AssociatedTranscriptFilterNameType = Literal["IntentId", "SlotTypeId"]
AudioRecognitionStrategyType = Literal["UseSlotValuesAsCustomVocabulary"]
BotAliasAvailableWaiterName = Literal["bot_alias_available"]
BotAliasStatusType = Literal["Available", "Creating", "Deleting", "Failed"]
BotAvailableWaiterName = Literal["bot_available"]
BotExportCompletedWaiterName = Literal["bot_export_completed"]
BotFilterNameType = Literal["BotName", "BotType"]
BotFilterOperatorType = Literal["CO", "EQ", "NE"]
BotImportCompletedWaiterName = Literal["bot_import_completed"]
BotLocaleBuiltWaiterName = Literal["bot_locale_built"]
BotLocaleCreatedWaiterName = Literal["bot_locale_created"]
BotLocaleExpressTestingAvailableWaiterName = Literal["bot_locale_express_testing_available"]
BotLocaleFilterNameType = Literal["BotLocaleName"]
BotLocaleFilterOperatorType = Literal["CO", "EQ"]
BotLocaleSortAttributeType = Literal["BotLocaleName"]
BotLocaleStatusType = Literal[
    "Building",
    "Built",
    "Creating",
    "Deleting",
    "Failed",
    "Importing",
    "NotBuilt",
    "Processing",
    "ReadyExpressTesting",
]
BotRecommendationStatusType = Literal[
    "Available",
    "Deleted",
    "Deleting",
    "Downloading",
    "Failed",
    "Processing",
    "Stopped",
    "Stopping",
    "Updating",
]
BotSortAttributeType = Literal["BotName"]
BotStatusType = Literal[
    "Available", "Creating", "Deleting", "Failed", "Importing", "Inactive", "Updating", "Versioning"
]
BotTypeType = Literal["Bot", "BotNetwork"]
BotVersionAvailableWaiterName = Literal["bot_version_available"]
BotVersionSortAttributeType = Literal["BotVersion"]
BuiltInIntentSortAttributeType = Literal["IntentSignature"]
BuiltInSlotTypeSortAttributeType = Literal["SlotTypeSignature"]
CustomVocabularyStatusType = Literal["Creating", "Deleting", "Exporting", "Importing", "Ready"]
DialogActionTypeType = Literal[
    "CloseIntent",
    "ConfirmIntent",
    "ElicitIntent",
    "ElicitSlot",
    "EndConversation",
    "EvaluateConditional",
    "FulfillIntent",
    "InvokeDialogCodeHook",
    "StartIntent",
]
EffectType = Literal["Allow", "Deny"]
ErrorCodeType = Literal[
    "DUPLICATE_INPUT",
    "INTERNAL_SERVER_FAILURE",
    "RESOURCE_ALREADY_EXISTS",
    "RESOURCE_DOES_NOT_EXIST",
]
ExportFilterNameType = Literal["ExportResourceType"]
ExportFilterOperatorType = Literal["CO", "EQ"]
ExportSortAttributeType = Literal["LastUpdatedDateTime"]
ExportStatusType = Literal["Completed", "Deleting", "Failed", "InProgress"]
ImportExportFileFormatType = Literal["LexJson", "TSV"]
ImportFilterNameType = Literal["ImportResourceType"]
ImportFilterOperatorType = Literal["CO", "EQ"]
ImportResourceTypeType = Literal["Bot", "BotLocale", "CustomVocabulary"]
ImportSortAttributeType = Literal["LastUpdatedDateTime"]
ImportStatusType = Literal["Completed", "Deleting", "Failed", "InProgress"]
IntentFilterNameType = Literal["IntentName"]
IntentFilterOperatorType = Literal["CO", "EQ"]
IntentSortAttributeType = Literal["IntentName", "LastUpdatedDateTime"]
MergeStrategyType = Literal["Append", "FailOnConflict", "Overwrite"]
MessageSelectionStrategyType = Literal["Ordered", "Random"]
ObfuscationSettingTypeType = Literal["DefaultObfuscation", "None"]
PromptAttemptType = Literal["Initial", "Retry1", "Retry2", "Retry3", "Retry4", "Retry5"]
SearchOrderType = Literal["Ascending", "Descending"]
SlotConstraintType = Literal["Optional", "Required"]
SlotFilterNameType = Literal["SlotName"]
SlotFilterOperatorType = Literal["CO", "EQ"]
SlotShapeType = Literal["List", "Scalar"]
SlotSortAttributeType = Literal["LastUpdatedDateTime", "SlotName"]
SlotTypeCategoryType = Literal["Composite", "Custom", "Extended", "ExternalGrammar"]
SlotTypeFilterNameType = Literal["ExternalSourceType", "SlotTypeName"]
SlotTypeFilterOperatorType = Literal["CO", "EQ"]
SlotTypeSortAttributeType = Literal["LastUpdatedDateTime", "SlotTypeName"]
SlotValueResolutionStrategyType = Literal["Concatenation", "OriginalValue", "TopResolution"]
SortOrderType = Literal["Ascending", "Descending"]
TimeDimensionType = Literal["Days", "Hours", "Weeks"]
TranscriptFormatType = Literal["Lex"]
VoiceEngineType = Literal["neural", "standard"]
