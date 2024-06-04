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
    "AnalyticsBinByNameType",
    "AnalyticsCommonFilterNameType",
    "AnalyticsFilterOperatorType",
    "AnalyticsIntentFieldType",
    "AnalyticsIntentFilterNameType",
    "AnalyticsIntentMetricNameType",
    "AnalyticsIntentStageFieldType",
    "AnalyticsIntentStageFilterNameType",
    "AnalyticsIntentStageMetricNameType",
    "AnalyticsIntervalType",
    "AnalyticsMetricStatisticType",
    "AnalyticsModalityType",
    "AnalyticsNodeTypeType",
    "AnalyticsSessionFieldType",
    "AnalyticsSessionFilterNameType",
    "AnalyticsSessionMetricNameType",
    "AnalyticsSessionSortByNameType",
    "AnalyticsSortOrderType",
    "AnalyticsUtteranceAttributeNameType",
    "AnalyticsUtteranceFieldType",
    "AnalyticsUtteranceFilterNameType",
    "AnalyticsUtteranceMetricNameType",
    "AnalyticsUtteranceSortByNameType",
    "AssociatedTranscriptFilterNameType",
    "AudioRecognitionStrategyType",
    "BotAliasAvailableWaiterName",
    "BotAliasReplicationStatusType",
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
    "BotReplicaStatusType",
    "BotSortAttributeType",
    "BotStatusType",
    "BotTypeType",
    "BotVersionAvailableWaiterName",
    "BotVersionReplicaSortAttributeType",
    "BotVersionReplicationStatusType",
    "BotVersionSortAttributeType",
    "BuiltInIntentSortAttributeType",
    "BuiltInSlotTypeSortAttributeType",
    "ConversationEndStateType",
    "ConversationLogsInputModeFilterType",
    "CustomVocabularyStatusType",
    "DialogActionTypeType",
    "EffectType",
    "ErrorCodeType",
    "ExportFilterNameType",
    "ExportFilterOperatorType",
    "ExportSortAttributeType",
    "ExportStatusType",
    "GenerationSortByAttributeType",
    "GenerationStatusType",
    "ImportExportFileFormatType",
    "ImportFilterNameType",
    "ImportFilterOperatorType",
    "ImportResourceTypeType",
    "ImportSortAttributeType",
    "ImportStatusType",
    "IntentFilterNameType",
    "IntentFilterOperatorType",
    "IntentSortAttributeType",
    "IntentStateType",
    "MergeStrategyType",
    "MessageSelectionStrategyType",
    "ObfuscationSettingTypeType",
    "PromptAttemptType",
    "SearchOrderType",
    "SlotConstraintType",
    "SlotFilterNameType",
    "SlotFilterOperatorType",
    "SlotResolutionStrategyType",
    "SlotShapeType",
    "SlotSortAttributeType",
    "SlotTypeCategoryType",
    "SlotTypeFilterNameType",
    "SlotTypeFilterOperatorType",
    "SlotTypeSortAttributeType",
    "SlotValueResolutionStrategyType",
    "SortOrderType",
    "TestExecutionApiModeType",
    "TestExecutionModalityType",
    "TestExecutionSortAttributeType",
    "TestExecutionStatusType",
    "TestResultMatchStatusType",
    "TestResultTypeFilterType",
    "TestSetDiscrepancyReportStatusType",
    "TestSetGenerationStatusType",
    "TestSetModalityType",
    "TestSetSortAttributeType",
    "TestSetStatusType",
    "TimeDimensionType",
    "TranscriptFormatType",
    "UtteranceContentTypeType",
    "VoiceEngineType",
)

AggregatedUtterancesFilterNameType = Literal["Utterance"]
AggregatedUtterancesFilterOperatorType = Literal["CO", "EQ"]
AggregatedUtterancesSortAttributeType = Literal["HitCount", "MissedCount"]
AnalyticsBinByNameType = Literal["ConversationStartTime", "UtteranceTimestamp"]
AnalyticsCommonFilterNameType = Literal[
    "BotAliasId", "BotVersion", "Channel", "LocaleId", "Modality"
]
AnalyticsFilterOperatorType = Literal["EQ", "GT", "LT"]
AnalyticsIntentFieldType = Literal["IntentEndState", "IntentLevel", "IntentName"]
AnalyticsIntentFilterNameType = Literal[
    "BotAliasId",
    "BotVersion",
    "Channel",
    "IntentEndState",
    "IntentName",
    "LocaleId",
    "Modality",
    "OriginatingRequestId",
    "SessionId",
]
AnalyticsIntentMetricNameType = Literal["Count", "Dropped", "Failure", "Success", "Switched"]
AnalyticsIntentStageFieldType = Literal["IntentStageName", "SwitchedToIntent"]
AnalyticsIntentStageFilterNameType = Literal[
    "BotAliasId",
    "BotVersion",
    "Channel",
    "IntentName",
    "IntentStageName",
    "LocaleId",
    "Modality",
    "OriginatingRequestId",
    "SessionId",
]
AnalyticsIntentStageMetricNameType = Literal["Count", "Dropped", "Failed", "Retry", "Success"]
AnalyticsIntervalType = Literal["OneDay", "OneHour"]
AnalyticsMetricStatisticType = Literal["Avg", "Max", "Sum"]
AnalyticsModalityType = Literal["DTMF", "MultiMode", "Speech", "Text"]
AnalyticsNodeTypeType = Literal["Exit", "Inner"]
AnalyticsSessionFieldType = Literal["ConversationEndState", "LocaleId"]
AnalyticsSessionFilterNameType = Literal[
    "BotAliasId",
    "BotVersion",
    "Channel",
    "ConversationEndState",
    "Duration",
    "IntentPath",
    "LocaleId",
    "Modality",
    "OriginatingRequestId",
    "SessionId",
]
AnalyticsSessionMetricNameType = Literal[
    "Concurrency", "Count", "Dropped", "Duration", "Failure", "Success", "TurnsPerConversation"
]
AnalyticsSessionSortByNameType = Literal["ConversationStartTime", "Duration", "NumberOfTurns"]
AnalyticsSortOrderType = Literal["Ascending", "Descending"]
AnalyticsUtteranceAttributeNameType = Literal["LastUsedIntent"]
AnalyticsUtteranceFieldType = Literal["UtteranceState", "UtteranceText"]
AnalyticsUtteranceFilterNameType = Literal[
    "BotAliasId",
    "BotVersion",
    "Channel",
    "LocaleId",
    "Modality",
    "OriginatingRequestId",
    "SessionId",
    "UtteranceState",
    "UtteranceText",
]
AnalyticsUtteranceMetricNameType = Literal["Count", "Detected", "Missed", "UtteranceTimestamp"]
AnalyticsUtteranceSortByNameType = Literal["UtteranceTimestamp"]
AssociatedTranscriptFilterNameType = Literal["IntentId", "SlotTypeId"]
AudioRecognitionStrategyType = Literal["UseSlotValuesAsCustomVocabulary"]
BotAliasAvailableWaiterName = Literal["bot_alias_available"]
BotAliasReplicationStatusType = Literal["Available", "Creating", "Deleting", "Failed", "Updating"]
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
BotReplicaStatusType = Literal["Deleting", "Enabled", "Enabling", "Failed"]
BotSortAttributeType = Literal["BotName"]
BotStatusType = Literal[
    "Available", "Creating", "Deleting", "Failed", "Importing", "Inactive", "Updating", "Versioning"
]
BotTypeType = Literal["Bot", "BotNetwork"]
BotVersionAvailableWaiterName = Literal["bot_version_available"]
BotVersionReplicaSortAttributeType = Literal["BotVersion"]
BotVersionReplicationStatusType = Literal["Available", "Creating", "Deleting", "Failed"]
BotVersionSortAttributeType = Literal["BotVersion"]
BuiltInIntentSortAttributeType = Literal["IntentSignature"]
BuiltInSlotTypeSortAttributeType = Literal["SlotTypeSignature"]
ConversationEndStateType = Literal["Dropped", "Failure", "Success"]
ConversationLogsInputModeFilterType = Literal["Speech", "Text"]
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
GenerationSortByAttributeType = Literal["creationStartTime", "lastUpdatedTime"]
GenerationStatusType = Literal["Complete", "Failed", "InProgress"]
ImportExportFileFormatType = Literal["CSV", "LexJson", "TSV"]
ImportFilterNameType = Literal["ImportResourceType"]
ImportFilterOperatorType = Literal["CO", "EQ"]
ImportResourceTypeType = Literal["Bot", "BotLocale", "CustomVocabulary", "TestSet"]
ImportSortAttributeType = Literal["LastUpdatedDateTime"]
ImportStatusType = Literal["Completed", "Deleting", "Failed", "InProgress"]
IntentFilterNameType = Literal["IntentName"]
IntentFilterOperatorType = Literal["CO", "EQ"]
IntentSortAttributeType = Literal["IntentName", "LastUpdatedDateTime"]
IntentStateType = Literal[
    "Failed", "Fulfilled", "FulfillmentInProgress", "InProgress", "ReadyForFulfillment", "Waiting"
]
MergeStrategyType = Literal["Append", "FailOnConflict", "Overwrite"]
MessageSelectionStrategyType = Literal["Ordered", "Random"]
ObfuscationSettingTypeType = Literal["DefaultObfuscation", "None"]
PromptAttemptType = Literal["Initial", "Retry1", "Retry2", "Retry3", "Retry4", "Retry5"]
SearchOrderType = Literal["Ascending", "Descending"]
SlotConstraintType = Literal["Optional", "Required"]
SlotFilterNameType = Literal["SlotName"]
SlotFilterOperatorType = Literal["CO", "EQ"]
SlotResolutionStrategyType = Literal["Default", "EnhancedFallback"]
SlotShapeType = Literal["List", "Scalar"]
SlotSortAttributeType = Literal["LastUpdatedDateTime", "SlotName"]
SlotTypeCategoryType = Literal["Composite", "Custom", "Extended", "ExternalGrammar"]
SlotTypeFilterNameType = Literal["ExternalSourceType", "SlotTypeName"]
SlotTypeFilterOperatorType = Literal["CO", "EQ"]
SlotTypeSortAttributeType = Literal["LastUpdatedDateTime", "SlotTypeName"]
SlotValueResolutionStrategyType = Literal["Concatenation", "OriginalValue", "TopResolution"]
SortOrderType = Literal["Ascending", "Descending"]
TestExecutionApiModeType = Literal["NonStreaming", "Streaming"]
TestExecutionModalityType = Literal["Audio", "Text"]
TestExecutionSortAttributeType = Literal["CreationDateTime", "TestSetName"]
TestExecutionStatusType = Literal[
    "Completed", "Failed", "InProgress", "Pending", "Stopped", "Stopping", "Waiting"
]
TestResultMatchStatusType = Literal["ExecutionError", "Matched", "Mismatched"]
TestResultTypeFilterType = Literal[
    "ConversationLevelTestResults",
    "IntentClassificationTestResults",
    "OverallTestResults",
    "SlotResolutionTestResults",
    "UtteranceLevelResults",
]
TestSetDiscrepancyReportStatusType = Literal["Completed", "Failed", "InProgress"]
TestSetGenerationStatusType = Literal["Failed", "Generating", "Pending", "Ready"]
TestSetModalityType = Literal["Audio", "Text"]
TestSetSortAttributeType = Literal["LastUpdatedDateTime", "TestSetName"]
TestSetStatusType = Literal[
    "Deleting", "Importing", "PendingAnnotation", "Ready", "ValidationError"
]
TimeDimensionType = Literal["Days", "Hours", "Weeks"]
TranscriptFormatType = Literal["Lex"]
UtteranceContentTypeType = Literal["CustomPayload", "ImageResponseCard", "PlainText", "SSML"]
VoiceEngineType = Literal["neural", "standard"]
