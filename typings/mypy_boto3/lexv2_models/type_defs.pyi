"""
Type annotations for lexv2-models service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lexv2_models.type_defs import ActiveContextTypeDef

    data: ActiveContextTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AggregatedUtterancesFilterOperatorType,
    AggregatedUtterancesSortAttributeType,
    AnalyticsBinByNameType,
    AnalyticsCommonFilterNameType,
    AnalyticsFilterOperatorType,
    AnalyticsIntentFieldType,
    AnalyticsIntentFilterNameType,
    AnalyticsIntentMetricNameType,
    AnalyticsIntentStageFieldType,
    AnalyticsIntentStageFilterNameType,
    AnalyticsIntentStageMetricNameType,
    AnalyticsIntervalType,
    AnalyticsMetricStatisticType,
    AnalyticsModalityType,
    AnalyticsNodeTypeType,
    AnalyticsSessionFieldType,
    AnalyticsSessionFilterNameType,
    AnalyticsSessionMetricNameType,
    AnalyticsSessionSortByNameType,
    AnalyticsSortOrderType,
    AnalyticsUtteranceFieldType,
    AnalyticsUtteranceFilterNameType,
    AnalyticsUtteranceMetricNameType,
    AssociatedTranscriptFilterNameType,
    BotAliasStatusType,
    BotFilterNameType,
    BotFilterOperatorType,
    BotLocaleFilterOperatorType,
    BotLocaleStatusType,
    BotRecommendationStatusType,
    BotStatusType,
    BotTypeType,
    ConversationEndStateType,
    ConversationLogsInputModeFilterType,
    CustomVocabularyStatusType,
    DialogActionTypeType,
    EffectType,
    ErrorCodeType,
    ExportFilterOperatorType,
    ExportStatusType,
    ImportExportFileFormatType,
    ImportFilterOperatorType,
    ImportResourceTypeType,
    ImportStatusType,
    IntentFilterOperatorType,
    IntentSortAttributeType,
    IntentStateType,
    MergeStrategyType,
    MessageSelectionStrategyType,
    ObfuscationSettingTypeType,
    PromptAttemptType,
    SearchOrderType,
    SlotConstraintType,
    SlotFilterOperatorType,
    SlotShapeType,
    SlotSortAttributeType,
    SlotTypeCategoryType,
    SlotTypeFilterNameType,
    SlotTypeFilterOperatorType,
    SlotTypeSortAttributeType,
    SlotValueResolutionStrategyType,
    SortOrderType,
    TestExecutionApiModeType,
    TestExecutionModalityType,
    TestExecutionSortAttributeType,
    TestExecutionStatusType,
    TestResultMatchStatusType,
    TestResultTypeFilterType,
    TestSetDiscrepancyReportStatusType,
    TestSetGenerationStatusType,
    TestSetModalityType,
    TestSetSortAttributeType,
    TestSetStatusType,
    TimeDimensionType,
    UtteranceContentTypeType,
    VoiceEngineType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ActiveContextTypeDef",
    "AdvancedRecognitionSettingTypeDef",
    "AgentTurnResultTypeDef",
    "AgentTurnSpecificationTypeDef",
    "AggregatedUtterancesFilterTypeDef",
    "AggregatedUtterancesSortByTypeDef",
    "AggregatedUtterancesSummaryTypeDef",
    "AllowedInputTypesTypeDef",
    "AnalyticsBinBySpecificationTypeDef",
    "AnalyticsBinKeyTypeDef",
    "AnalyticsIntentFilterTypeDef",
    "AnalyticsIntentGroupByKeyTypeDef",
    "AnalyticsIntentGroupBySpecificationTypeDef",
    "AnalyticsIntentMetricResultTypeDef",
    "AnalyticsIntentMetricTypeDef",
    "AnalyticsIntentNodeSummaryTypeDef",
    "AnalyticsIntentResultTypeDef",
    "AnalyticsIntentStageFilterTypeDef",
    "AnalyticsIntentStageGroupByKeyTypeDef",
    "AnalyticsIntentStageGroupBySpecificationTypeDef",
    "AnalyticsIntentStageMetricResultTypeDef",
    "AnalyticsIntentStageMetricTypeDef",
    "AnalyticsIntentStageResultTypeDef",
    "AnalyticsPathFilterTypeDef",
    "AnalyticsSessionFilterTypeDef",
    "AnalyticsSessionGroupByKeyTypeDef",
    "AnalyticsSessionGroupBySpecificationTypeDef",
    "AnalyticsSessionMetricResultTypeDef",
    "AnalyticsSessionMetricTypeDef",
    "AnalyticsSessionResultTypeDef",
    "AnalyticsUtteranceAttributeResultTypeDef",
    "AnalyticsUtteranceAttributeTypeDef",
    "AnalyticsUtteranceFilterTypeDef",
    "AnalyticsUtteranceGroupByKeyTypeDef",
    "AnalyticsUtteranceGroupBySpecificationTypeDef",
    "AnalyticsUtteranceMetricResultTypeDef",
    "AnalyticsUtteranceMetricTypeDef",
    "AnalyticsUtteranceResultTypeDef",
    "AssociatedTranscriptFilterTypeDef",
    "AssociatedTranscriptTypeDef",
    "AudioAndDTMFInputSpecificationTypeDef",
    "AudioLogDestinationTypeDef",
    "AudioLogSettingTypeDef",
    "AudioSpecificationTypeDef",
    "BatchCreateCustomVocabularyItemRequestRequestTypeDef",
    "BatchCreateCustomVocabularyItemResponseTypeDef",
    "BatchDeleteCustomVocabularyItemRequestRequestTypeDef",
    "BatchDeleteCustomVocabularyItemResponseTypeDef",
    "BatchUpdateCustomVocabularyItemRequestRequestTypeDef",
    "BatchUpdateCustomVocabularyItemResponseTypeDef",
    "BotAliasHistoryEventTypeDef",
    "BotAliasLocaleSettingsTypeDef",
    "BotAliasSummaryTypeDef",
    "BotAliasTestExecutionTargetTypeDef",
    "BotExportSpecificationTypeDef",
    "BotFilterTypeDef",
    "BotImportSpecificationTypeDef",
    "BotLocaleExportSpecificationTypeDef",
    "BotLocaleFilterTypeDef",
    "BotLocaleHistoryEventTypeDef",
    "BotLocaleImportSpecificationTypeDef",
    "BotLocaleSortByTypeDef",
    "BotLocaleSummaryTypeDef",
    "BotMemberTypeDef",
    "BotRecommendationResultStatisticsTypeDef",
    "BotRecommendationResultsTypeDef",
    "BotRecommendationSummaryTypeDef",
    "BotSortByTypeDef",
    "BotSummaryTypeDef",
    "BotVersionLocaleDetailsTypeDef",
    "BotVersionSortByTypeDef",
    "BotVersionSummaryTypeDef",
    "BuildBotLocaleRequestRequestTypeDef",
    "BuildBotLocaleResponseTypeDef",
    "BuiltInIntentSortByTypeDef",
    "BuiltInIntentSummaryTypeDef",
    "BuiltInSlotTypeSortByTypeDef",
    "BuiltInSlotTypeSummaryTypeDef",
    "ButtonTypeDef",
    "CloudWatchLogGroupLogDestinationTypeDef",
    "CodeHookSpecificationTypeDef",
    "CompositeSlotTypeSettingTypeDef",
    "ConditionTypeDef",
    "ConditionalBranchTypeDef",
    "ConditionalSpecificationTypeDef",
    "ConversationLevelIntentClassificationResultItemTypeDef",
    "ConversationLevelResultDetailTypeDef",
    "ConversationLevelSlotResolutionResultItemTypeDef",
    "ConversationLevelTestResultItemTypeDef",
    "ConversationLevelTestResultsFilterByTypeDef",
    "ConversationLevelTestResultsTypeDef",
    "ConversationLogSettingsTypeDef",
    "ConversationLogsDataSourceFilterByTypeDef",
    "ConversationLogsDataSourceTypeDef",
    "CreateBotAliasRequestRequestTypeDef",
    "CreateBotAliasResponseTypeDef",
    "CreateBotLocaleRequestRequestTypeDef",
    "CreateBotLocaleResponseTypeDef",
    "CreateBotRequestRequestTypeDef",
    "CreateBotResponseTypeDef",
    "CreateBotVersionRequestRequestTypeDef",
    "CreateBotVersionResponseTypeDef",
    "CreateExportRequestRequestTypeDef",
    "CreateExportResponseTypeDef",
    "CreateIntentRequestRequestTypeDef",
    "CreateIntentResponseTypeDef",
    "CreateResourcePolicyRequestRequestTypeDef",
    "CreateResourcePolicyResponseTypeDef",
    "CreateResourcePolicyStatementRequestRequestTypeDef",
    "CreateResourcePolicyStatementResponseTypeDef",
    "CreateSlotRequestRequestTypeDef",
    "CreateSlotResponseTypeDef",
    "CreateSlotTypeRequestRequestTypeDef",
    "CreateSlotTypeResponseTypeDef",
    "CreateTestSetDiscrepancyReportRequestRequestTypeDef",
    "CreateTestSetDiscrepancyReportResponseTypeDef",
    "CreateUploadUrlResponseTypeDef",
    "CustomPayloadTypeDef",
    "CustomVocabularyEntryIdTypeDef",
    "CustomVocabularyExportSpecificationTypeDef",
    "CustomVocabularyImportSpecificationTypeDef",
    "CustomVocabularyItemTypeDef",
    "DTMFSpecificationTypeDef",
    "DataPrivacyTypeDef",
    "DateRangeFilterTypeDef",
    "DefaultConditionalBranchTypeDef",
    "DeleteBotAliasRequestRequestTypeDef",
    "DeleteBotAliasResponseTypeDef",
    "DeleteBotLocaleRequestRequestTypeDef",
    "DeleteBotLocaleResponseTypeDef",
    "DeleteBotRequestRequestTypeDef",
    "DeleteBotResponseTypeDef",
    "DeleteBotVersionRequestRequestTypeDef",
    "DeleteBotVersionResponseTypeDef",
    "DeleteCustomVocabularyRequestRequestTypeDef",
    "DeleteCustomVocabularyResponseTypeDef",
    "DeleteExportRequestRequestTypeDef",
    "DeleteExportResponseTypeDef",
    "DeleteImportRequestRequestTypeDef",
    "DeleteImportResponseTypeDef",
    "DeleteIntentRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteResourcePolicyResponseTypeDef",
    "DeleteResourcePolicyStatementRequestRequestTypeDef",
    "DeleteResourcePolicyStatementResponseTypeDef",
    "DeleteSlotRequestRequestTypeDef",
    "DeleteSlotTypeRequestRequestTypeDef",
    "DeleteTestSetRequestRequestTypeDef",
    "DeleteUtterancesRequestRequestTypeDef",
    "DescribeBotAliasRequestRequestTypeDef",
    "DescribeBotAliasResponseTypeDef",
    "DescribeBotLocaleRequestRequestTypeDef",
    "DescribeBotLocaleResponseTypeDef",
    "DescribeBotRecommendationRequestRequestTypeDef",
    "DescribeBotRecommendationResponseTypeDef",
    "DescribeBotRequestRequestTypeDef",
    "DescribeBotResponseTypeDef",
    "DescribeBotVersionRequestRequestTypeDef",
    "DescribeBotVersionResponseTypeDef",
    "DescribeCustomVocabularyMetadataRequestRequestTypeDef",
    "DescribeCustomVocabularyMetadataResponseTypeDef",
    "DescribeExportRequestRequestTypeDef",
    "DescribeExportResponseTypeDef",
    "DescribeImportRequestRequestTypeDef",
    "DescribeImportResponseTypeDef",
    "DescribeIntentRequestRequestTypeDef",
    "DescribeIntentResponseTypeDef",
    "DescribeResourcePolicyRequestRequestTypeDef",
    "DescribeResourcePolicyResponseTypeDef",
    "DescribeSlotRequestRequestTypeDef",
    "DescribeSlotResponseTypeDef",
    "DescribeSlotTypeRequestRequestTypeDef",
    "DescribeSlotTypeResponseTypeDef",
    "DescribeTestExecutionRequestRequestTypeDef",
    "DescribeTestExecutionResponseTypeDef",
    "DescribeTestSetDiscrepancyReportRequestRequestTypeDef",
    "DescribeTestSetDiscrepancyReportResponseTypeDef",
    "DescribeTestSetGenerationRequestRequestTypeDef",
    "DescribeTestSetGenerationResponseTypeDef",
    "DescribeTestSetRequestRequestTypeDef",
    "DescribeTestSetResponseTypeDef",
    "DialogActionTypeDef",
    "DialogCodeHookInvocationSettingTypeDef",
    "DialogCodeHookSettingsTypeDef",
    "DialogStateTypeDef",
    "ElicitationCodeHookInvocationSettingTypeDef",
    "EncryptionSettingTypeDef",
    "ExecutionErrorDetailsTypeDef",
    "ExportFilterTypeDef",
    "ExportResourceSpecificationTypeDef",
    "ExportSortByTypeDef",
    "ExportSummaryTypeDef",
    "ExternalSourceSettingTypeDef",
    "FailedCustomVocabularyItemTypeDef",
    "FulfillmentCodeHookSettingsTypeDef",
    "FulfillmentStartResponseSpecificationTypeDef",
    "FulfillmentUpdateResponseSpecificationTypeDef",
    "FulfillmentUpdatesSpecificationTypeDef",
    "GetTestExecutionArtifactsUrlRequestRequestTypeDef",
    "GetTestExecutionArtifactsUrlResponseTypeDef",
    "GrammarSlotTypeSettingTypeDef",
    "GrammarSlotTypeSourceTypeDef",
    "ImageResponseCardTypeDef",
    "ImportFilterTypeDef",
    "ImportResourceSpecificationTypeDef",
    "ImportSortByTypeDef",
    "ImportSummaryTypeDef",
    "InitialResponseSettingTypeDef",
    "InputContextTypeDef",
    "InputSessionStateSpecificationTypeDef",
    "IntentClassificationTestResultItemCountsTypeDef",
    "IntentClassificationTestResultItemTypeDef",
    "IntentClassificationTestResultsTypeDef",
    "IntentClosingSettingTypeDef",
    "IntentConfirmationSettingTypeDef",
    "IntentFilterTypeDef",
    "IntentLevelSlotResolutionTestResultItemTypeDef",
    "IntentLevelSlotResolutionTestResultsTypeDef",
    "IntentOverrideTypeDef",
    "IntentSortByTypeDef",
    "IntentStatisticsTypeDef",
    "IntentSummaryTypeDef",
    "InvokedIntentSampleTypeDef",
    "KendraConfigurationTypeDef",
    "LambdaCodeHookTypeDef",
    "LexTranscriptFilterTypeDef",
    "ListAggregatedUtterancesRequestRequestTypeDef",
    "ListAggregatedUtterancesResponseTypeDef",
    "ListBotAliasesRequestRequestTypeDef",
    "ListBotAliasesResponseTypeDef",
    "ListBotLocalesRequestRequestTypeDef",
    "ListBotLocalesResponseTypeDef",
    "ListBotRecommendationsRequestRequestTypeDef",
    "ListBotRecommendationsResponseTypeDef",
    "ListBotVersionsRequestRequestTypeDef",
    "ListBotVersionsResponseTypeDef",
    "ListBotsRequestRequestTypeDef",
    "ListBotsResponseTypeDef",
    "ListBuiltInIntentsRequestRequestTypeDef",
    "ListBuiltInIntentsResponseTypeDef",
    "ListBuiltInSlotTypesRequestRequestTypeDef",
    "ListBuiltInSlotTypesResponseTypeDef",
    "ListCustomVocabularyItemsRequestRequestTypeDef",
    "ListCustomVocabularyItemsResponseTypeDef",
    "ListExportsRequestRequestTypeDef",
    "ListExportsResponseTypeDef",
    "ListImportsRequestRequestTypeDef",
    "ListImportsResponseTypeDef",
    "ListIntentMetricsRequestRequestTypeDef",
    "ListIntentMetricsResponseTypeDef",
    "ListIntentPathsRequestRequestTypeDef",
    "ListIntentPathsResponseTypeDef",
    "ListIntentStageMetricsRequestRequestTypeDef",
    "ListIntentStageMetricsResponseTypeDef",
    "ListIntentsRequestRequestTypeDef",
    "ListIntentsResponseTypeDef",
    "ListRecommendedIntentsRequestRequestTypeDef",
    "ListRecommendedIntentsResponseTypeDef",
    "ListSessionAnalyticsDataRequestRequestTypeDef",
    "ListSessionAnalyticsDataResponseTypeDef",
    "ListSessionMetricsRequestRequestTypeDef",
    "ListSessionMetricsResponseTypeDef",
    "ListSlotTypesRequestRequestTypeDef",
    "ListSlotTypesResponseTypeDef",
    "ListSlotsRequestRequestTypeDef",
    "ListSlotsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTestExecutionResultItemsRequestRequestTypeDef",
    "ListTestExecutionResultItemsResponseTypeDef",
    "ListTestExecutionsRequestRequestTypeDef",
    "ListTestExecutionsResponseTypeDef",
    "ListTestSetRecordsRequestRequestTypeDef",
    "ListTestSetRecordsResponseTypeDef",
    "ListTestSetsRequestRequestTypeDef",
    "ListTestSetsResponseTypeDef",
    "ListUtteranceAnalyticsDataRequestRequestTypeDef",
    "ListUtteranceAnalyticsDataResponseTypeDef",
    "ListUtteranceMetricsRequestRequestTypeDef",
    "ListUtteranceMetricsResponseTypeDef",
    "MessageGroupTypeDef",
    "MessageTypeDef",
    "MultipleValuesSettingTypeDef",
    "NewCustomVocabularyItemTypeDef",
    "ObfuscationSettingTypeDef",
    "OutputContextTypeDef",
    "OverallTestResultItemTypeDef",
    "OverallTestResultsTypeDef",
    "ParentBotNetworkTypeDef",
    "PathFormatTypeDef",
    "PlainTextMessageTypeDef",
    "PostDialogCodeHookInvocationSpecificationTypeDef",
    "PostFulfillmentStatusSpecificationTypeDef",
    "PrincipalTypeDef",
    "PromptAttemptSpecificationTypeDef",
    "PromptSpecificationTypeDef",
    "RecommendedIntentSummaryTypeDef",
    "RelativeAggregationDurationTypeDef",
    "ResponseMetadataTypeDef",
    "ResponseSpecificationTypeDef",
    "RuntimeHintDetailsTypeDef",
    "RuntimeHintValueTypeDef",
    "RuntimeHintsTypeDef",
    "S3BucketLogDestinationTypeDef",
    "S3BucketTranscriptSourceTypeDef",
    "SSMLMessageTypeDef",
    "SampleUtteranceTypeDef",
    "SampleValueTypeDef",
    "SearchAssociatedTranscriptsRequestRequestTypeDef",
    "SearchAssociatedTranscriptsResponseTypeDef",
    "SentimentAnalysisSettingsTypeDef",
    "SessionDataSortByTypeDef",
    "SessionSpecificationTypeDef",
    "SlotCaptureSettingTypeDef",
    "SlotDefaultValueSpecificationTypeDef",
    "SlotDefaultValueTypeDef",
    "SlotFilterTypeDef",
    "SlotPriorityTypeDef",
    "SlotResolutionTestResultItemCountsTypeDef",
    "SlotResolutionTestResultItemTypeDef",
    "SlotSortByTypeDef",
    "SlotSummaryTypeDef",
    "SlotTypeFilterTypeDef",
    "SlotTypeSortByTypeDef",
    "SlotTypeStatisticsTypeDef",
    "SlotTypeSummaryTypeDef",
    "SlotTypeValueTypeDef",
    "SlotValueElicitationSettingTypeDef",
    "SlotValueOverrideTypeDef",
    "SlotValueRegexFilterTypeDef",
    "SlotValueSelectionSettingTypeDef",
    "SlotValueTypeDef",
    "SpecificationsTypeDef",
    "StartBotRecommendationRequestRequestTypeDef",
    "StartBotRecommendationResponseTypeDef",
    "StartImportRequestRequestTypeDef",
    "StartImportResponseTypeDef",
    "StartTestExecutionRequestRequestTypeDef",
    "StartTestExecutionResponseTypeDef",
    "StartTestSetGenerationRequestRequestTypeDef",
    "StartTestSetGenerationResponseTypeDef",
    "StillWaitingResponseSpecificationTypeDef",
    "StopBotRecommendationRequestRequestTypeDef",
    "StopBotRecommendationResponseTypeDef",
    "SubSlotSettingTypeDef",
    "SubSlotTypeCompositionTypeDef",
    "SubSlotValueElicitationSettingTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TestExecutionResultFilterByTypeDef",
    "TestExecutionResultItemsTypeDef",
    "TestExecutionSortByTypeDef",
    "TestExecutionSummaryTypeDef",
    "TestExecutionTargetTypeDef",
    "TestSetDiscrepancyErrorsTypeDef",
    "TestSetDiscrepancyReportBotAliasTargetTypeDef",
    "TestSetDiscrepancyReportResourceTargetTypeDef",
    "TestSetExportSpecificationTypeDef",
    "TestSetGenerationDataSourceTypeDef",
    "TestSetImportInputLocationTypeDef",
    "TestSetImportResourceSpecificationTypeDef",
    "TestSetIntentDiscrepancyItemTypeDef",
    "TestSetSlotDiscrepancyItemTypeDef",
    "TestSetSortByTypeDef",
    "TestSetStorageLocationTypeDef",
    "TestSetSummaryTypeDef",
    "TestSetTurnRecordTypeDef",
    "TestSetTurnResultTypeDef",
    "TextInputSpecificationTypeDef",
    "TextLogDestinationTypeDef",
    "TextLogSettingTypeDef",
    "TranscriptFilterTypeDef",
    "TranscriptSourceSettingTypeDef",
    "TurnSpecificationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBotAliasRequestRequestTypeDef",
    "UpdateBotAliasResponseTypeDef",
    "UpdateBotLocaleRequestRequestTypeDef",
    "UpdateBotLocaleResponseTypeDef",
    "UpdateBotRecommendationRequestRequestTypeDef",
    "UpdateBotRecommendationResponseTypeDef",
    "UpdateBotRequestRequestTypeDef",
    "UpdateBotResponseTypeDef",
    "UpdateExportRequestRequestTypeDef",
    "UpdateExportResponseTypeDef",
    "UpdateIntentRequestRequestTypeDef",
    "UpdateIntentResponseTypeDef",
    "UpdateResourcePolicyRequestRequestTypeDef",
    "UpdateResourcePolicyResponseTypeDef",
    "UpdateSlotRequestRequestTypeDef",
    "UpdateSlotResponseTypeDef",
    "UpdateSlotTypeRequestRequestTypeDef",
    "UpdateSlotTypeResponseTypeDef",
    "UpdateTestSetRequestRequestTypeDef",
    "UpdateTestSetResponseTypeDef",
    "UserTurnInputSpecificationTypeDef",
    "UserTurnIntentOutputTypeDef",
    "UserTurnOutputSpecificationTypeDef",
    "UserTurnResultTypeDef",
    "UserTurnSlotOutputTypeDef",
    "UserTurnSpecificationTypeDef",
    "UtteranceAggregationDurationTypeDef",
    "UtteranceAudioInputSpecificationTypeDef",
    "UtteranceBotResponseTypeDef",
    "UtteranceDataSortByTypeDef",
    "UtteranceInputSpecificationTypeDef",
    "UtteranceLevelTestResultItemTypeDef",
    "UtteranceLevelTestResultsTypeDef",
    "UtteranceSpecificationTypeDef",
    "VoiceSettingsTypeDef",
    "WaitAndContinueSpecificationTypeDef",
    "WaiterConfigTypeDef",
)

ActiveContextTypeDef = TypedDict(
    "ActiveContextTypeDef",
    {
        "name": str,
    },
)

AdvancedRecognitionSettingTypeDef = TypedDict(
    "AdvancedRecognitionSettingTypeDef",
    {
        "audioRecognitionStrategy": Literal["UseSlotValuesAsCustomVocabulary"],
    },
    total=False,
)

_RequiredAgentTurnResultTypeDef = TypedDict(
    "_RequiredAgentTurnResultTypeDef",
    {
        "expectedAgentPrompt": str,
    },
)
_OptionalAgentTurnResultTypeDef = TypedDict(
    "_OptionalAgentTurnResultTypeDef",
    {
        "actualAgentPrompt": str,
        "errorDetails": "ExecutionErrorDetailsTypeDef",
        "actualElicitedSlot": str,
        "actualIntent": str,
    },
    total=False,
)

class AgentTurnResultTypeDef(_RequiredAgentTurnResultTypeDef, _OptionalAgentTurnResultTypeDef):
    pass

AgentTurnSpecificationTypeDef = TypedDict(
    "AgentTurnSpecificationTypeDef",
    {
        "agentPrompt": str,
    },
)

AggregatedUtterancesFilterTypeDef = TypedDict(
    "AggregatedUtterancesFilterTypeDef",
    {
        "name": Literal["Utterance"],
        "values": List[str],
        "operator": AggregatedUtterancesFilterOperatorType,
    },
)

AggregatedUtterancesSortByTypeDef = TypedDict(
    "AggregatedUtterancesSortByTypeDef",
    {
        "attribute": AggregatedUtterancesSortAttributeType,
        "order": SortOrderType,
    },
)

AggregatedUtterancesSummaryTypeDef = TypedDict(
    "AggregatedUtterancesSummaryTypeDef",
    {
        "utterance": str,
        "hitCount": int,
        "missedCount": int,
        "utteranceFirstRecordedInAggregationDuration": datetime,
        "utteranceLastRecordedInAggregationDuration": datetime,
        "containsDataFromDeletedResources": bool,
    },
    total=False,
)

AllowedInputTypesTypeDef = TypedDict(
    "AllowedInputTypesTypeDef",
    {
        "allowAudioInput": bool,
        "allowDTMFInput": bool,
    },
)

_RequiredAnalyticsBinBySpecificationTypeDef = TypedDict(
    "_RequiredAnalyticsBinBySpecificationTypeDef",
    {
        "name": AnalyticsBinByNameType,
        "interval": AnalyticsIntervalType,
    },
)
_OptionalAnalyticsBinBySpecificationTypeDef = TypedDict(
    "_OptionalAnalyticsBinBySpecificationTypeDef",
    {
        "order": AnalyticsSortOrderType,
    },
    total=False,
)

class AnalyticsBinBySpecificationTypeDef(
    _RequiredAnalyticsBinBySpecificationTypeDef, _OptionalAnalyticsBinBySpecificationTypeDef
):
    pass

AnalyticsBinKeyTypeDef = TypedDict(
    "AnalyticsBinKeyTypeDef",
    {
        "name": AnalyticsBinByNameType,
        "value": int,
    },
    total=False,
)

AnalyticsIntentFilterTypeDef = TypedDict(
    "AnalyticsIntentFilterTypeDef",
    {
        "name": AnalyticsIntentFilterNameType,
        "operator": AnalyticsFilterOperatorType,
        "values": List[str],
    },
)

AnalyticsIntentGroupByKeyTypeDef = TypedDict(
    "AnalyticsIntentGroupByKeyTypeDef",
    {
        "name": AnalyticsIntentFieldType,
        "value": str,
    },
    total=False,
)

AnalyticsIntentGroupBySpecificationTypeDef = TypedDict(
    "AnalyticsIntentGroupBySpecificationTypeDef",
    {
        "name": AnalyticsIntentFieldType,
    },
)

AnalyticsIntentMetricResultTypeDef = TypedDict(
    "AnalyticsIntentMetricResultTypeDef",
    {
        "name": AnalyticsIntentMetricNameType,
        "statistic": AnalyticsMetricStatisticType,
        "value": float,
    },
    total=False,
)

_RequiredAnalyticsIntentMetricTypeDef = TypedDict(
    "_RequiredAnalyticsIntentMetricTypeDef",
    {
        "name": AnalyticsIntentMetricNameType,
        "statistic": AnalyticsMetricStatisticType,
    },
)
_OptionalAnalyticsIntentMetricTypeDef = TypedDict(
    "_OptionalAnalyticsIntentMetricTypeDef",
    {
        "order": AnalyticsSortOrderType,
    },
    total=False,
)

class AnalyticsIntentMetricTypeDef(
    _RequiredAnalyticsIntentMetricTypeDef, _OptionalAnalyticsIntentMetricTypeDef
):
    pass

AnalyticsIntentNodeSummaryTypeDef = TypedDict(
    "AnalyticsIntentNodeSummaryTypeDef",
    {
        "intentName": str,
        "intentPath": str,
        "intentCount": int,
        "intentLevel": int,
        "nodeType": AnalyticsNodeTypeType,
    },
    total=False,
)

AnalyticsIntentResultTypeDef = TypedDict(
    "AnalyticsIntentResultTypeDef",
    {
        "binKeys": List["AnalyticsBinKeyTypeDef"],
        "groupByKeys": List["AnalyticsIntentGroupByKeyTypeDef"],
        "metricsResults": List["AnalyticsIntentMetricResultTypeDef"],
    },
    total=False,
)

AnalyticsIntentStageFilterTypeDef = TypedDict(
    "AnalyticsIntentStageFilterTypeDef",
    {
        "name": AnalyticsIntentStageFilterNameType,
        "operator": AnalyticsFilterOperatorType,
        "values": List[str],
    },
)

AnalyticsIntentStageGroupByKeyTypeDef = TypedDict(
    "AnalyticsIntentStageGroupByKeyTypeDef",
    {
        "name": AnalyticsIntentStageFieldType,
        "value": str,
    },
    total=False,
)

AnalyticsIntentStageGroupBySpecificationTypeDef = TypedDict(
    "AnalyticsIntentStageGroupBySpecificationTypeDef",
    {
        "name": AnalyticsIntentStageFieldType,
    },
)

AnalyticsIntentStageMetricResultTypeDef = TypedDict(
    "AnalyticsIntentStageMetricResultTypeDef",
    {
        "name": AnalyticsIntentStageMetricNameType,
        "statistic": AnalyticsMetricStatisticType,
        "value": float,
    },
    total=False,
)

_RequiredAnalyticsIntentStageMetricTypeDef = TypedDict(
    "_RequiredAnalyticsIntentStageMetricTypeDef",
    {
        "name": AnalyticsIntentStageMetricNameType,
        "statistic": AnalyticsMetricStatisticType,
    },
)
_OptionalAnalyticsIntentStageMetricTypeDef = TypedDict(
    "_OptionalAnalyticsIntentStageMetricTypeDef",
    {
        "order": AnalyticsSortOrderType,
    },
    total=False,
)

class AnalyticsIntentStageMetricTypeDef(
    _RequiredAnalyticsIntentStageMetricTypeDef, _OptionalAnalyticsIntentStageMetricTypeDef
):
    pass

AnalyticsIntentStageResultTypeDef = TypedDict(
    "AnalyticsIntentStageResultTypeDef",
    {
        "binKeys": List["AnalyticsBinKeyTypeDef"],
        "groupByKeys": List["AnalyticsIntentStageGroupByKeyTypeDef"],
        "metricsResults": List["AnalyticsIntentStageMetricResultTypeDef"],
    },
    total=False,
)

AnalyticsPathFilterTypeDef = TypedDict(
    "AnalyticsPathFilterTypeDef",
    {
        "name": AnalyticsCommonFilterNameType,
        "operator": AnalyticsFilterOperatorType,
        "values": List[str],
    },
)

AnalyticsSessionFilterTypeDef = TypedDict(
    "AnalyticsSessionFilterTypeDef",
    {
        "name": AnalyticsSessionFilterNameType,
        "operator": AnalyticsFilterOperatorType,
        "values": List[str],
    },
)

AnalyticsSessionGroupByKeyTypeDef = TypedDict(
    "AnalyticsSessionGroupByKeyTypeDef",
    {
        "name": AnalyticsSessionFieldType,
        "value": str,
    },
    total=False,
)

AnalyticsSessionGroupBySpecificationTypeDef = TypedDict(
    "AnalyticsSessionGroupBySpecificationTypeDef",
    {
        "name": AnalyticsSessionFieldType,
    },
)

AnalyticsSessionMetricResultTypeDef = TypedDict(
    "AnalyticsSessionMetricResultTypeDef",
    {
        "name": AnalyticsSessionMetricNameType,
        "statistic": AnalyticsMetricStatisticType,
        "value": float,
    },
    total=False,
)

_RequiredAnalyticsSessionMetricTypeDef = TypedDict(
    "_RequiredAnalyticsSessionMetricTypeDef",
    {
        "name": AnalyticsSessionMetricNameType,
        "statistic": AnalyticsMetricStatisticType,
    },
)
_OptionalAnalyticsSessionMetricTypeDef = TypedDict(
    "_OptionalAnalyticsSessionMetricTypeDef",
    {
        "order": AnalyticsSortOrderType,
    },
    total=False,
)

class AnalyticsSessionMetricTypeDef(
    _RequiredAnalyticsSessionMetricTypeDef, _OptionalAnalyticsSessionMetricTypeDef
):
    pass

AnalyticsSessionResultTypeDef = TypedDict(
    "AnalyticsSessionResultTypeDef",
    {
        "binKeys": List["AnalyticsBinKeyTypeDef"],
        "groupByKeys": List["AnalyticsSessionGroupByKeyTypeDef"],
        "metricsResults": List["AnalyticsSessionMetricResultTypeDef"],
    },
    total=False,
)

AnalyticsUtteranceAttributeResultTypeDef = TypedDict(
    "AnalyticsUtteranceAttributeResultTypeDef",
    {
        "lastUsedIntent": str,
    },
    total=False,
)

AnalyticsUtteranceAttributeTypeDef = TypedDict(
    "AnalyticsUtteranceAttributeTypeDef",
    {
        "name": Literal["LastUsedIntent"],
    },
)

AnalyticsUtteranceFilterTypeDef = TypedDict(
    "AnalyticsUtteranceFilterTypeDef",
    {
        "name": AnalyticsUtteranceFilterNameType,
        "operator": AnalyticsFilterOperatorType,
        "values": List[str],
    },
)

AnalyticsUtteranceGroupByKeyTypeDef = TypedDict(
    "AnalyticsUtteranceGroupByKeyTypeDef",
    {
        "name": AnalyticsUtteranceFieldType,
        "value": str,
    },
    total=False,
)

AnalyticsUtteranceGroupBySpecificationTypeDef = TypedDict(
    "AnalyticsUtteranceGroupBySpecificationTypeDef",
    {
        "name": AnalyticsUtteranceFieldType,
    },
)

AnalyticsUtteranceMetricResultTypeDef = TypedDict(
    "AnalyticsUtteranceMetricResultTypeDef",
    {
        "name": AnalyticsUtteranceMetricNameType,
        "statistic": AnalyticsMetricStatisticType,
        "value": float,
    },
    total=False,
)

_RequiredAnalyticsUtteranceMetricTypeDef = TypedDict(
    "_RequiredAnalyticsUtteranceMetricTypeDef",
    {
        "name": AnalyticsUtteranceMetricNameType,
        "statistic": AnalyticsMetricStatisticType,
    },
)
_OptionalAnalyticsUtteranceMetricTypeDef = TypedDict(
    "_OptionalAnalyticsUtteranceMetricTypeDef",
    {
        "order": AnalyticsSortOrderType,
    },
    total=False,
)

class AnalyticsUtteranceMetricTypeDef(
    _RequiredAnalyticsUtteranceMetricTypeDef, _OptionalAnalyticsUtteranceMetricTypeDef
):
    pass

AnalyticsUtteranceResultTypeDef = TypedDict(
    "AnalyticsUtteranceResultTypeDef",
    {
        "binKeys": List["AnalyticsBinKeyTypeDef"],
        "groupByKeys": List["AnalyticsUtteranceGroupByKeyTypeDef"],
        "metricsResults": List["AnalyticsUtteranceMetricResultTypeDef"],
        "attributeResults": List["AnalyticsUtteranceAttributeResultTypeDef"],
    },
    total=False,
)

AssociatedTranscriptFilterTypeDef = TypedDict(
    "AssociatedTranscriptFilterTypeDef",
    {
        "name": AssociatedTranscriptFilterNameType,
        "values": List[str],
    },
)

AssociatedTranscriptTypeDef = TypedDict(
    "AssociatedTranscriptTypeDef",
    {
        "transcript": str,
    },
    total=False,
)

_RequiredAudioAndDTMFInputSpecificationTypeDef = TypedDict(
    "_RequiredAudioAndDTMFInputSpecificationTypeDef",
    {
        "startTimeoutMs": int,
    },
)
_OptionalAudioAndDTMFInputSpecificationTypeDef = TypedDict(
    "_OptionalAudioAndDTMFInputSpecificationTypeDef",
    {
        "audioSpecification": "AudioSpecificationTypeDef",
        "dtmfSpecification": "DTMFSpecificationTypeDef",
    },
    total=False,
)

class AudioAndDTMFInputSpecificationTypeDef(
    _RequiredAudioAndDTMFInputSpecificationTypeDef, _OptionalAudioAndDTMFInputSpecificationTypeDef
):
    pass

AudioLogDestinationTypeDef = TypedDict(
    "AudioLogDestinationTypeDef",
    {
        "s3Bucket": "S3BucketLogDestinationTypeDef",
    },
)

_RequiredAudioLogSettingTypeDef = TypedDict(
    "_RequiredAudioLogSettingTypeDef",
    {
        "enabled": bool,
        "destination": "AudioLogDestinationTypeDef",
    },
)
_OptionalAudioLogSettingTypeDef = TypedDict(
    "_OptionalAudioLogSettingTypeDef",
    {
        "selectiveLoggingEnabled": bool,
    },
    total=False,
)

class AudioLogSettingTypeDef(_RequiredAudioLogSettingTypeDef, _OptionalAudioLogSettingTypeDef):
    pass

AudioSpecificationTypeDef = TypedDict(
    "AudioSpecificationTypeDef",
    {
        "maxLengthMs": int,
        "endTimeoutMs": int,
    },
)

BatchCreateCustomVocabularyItemRequestRequestTypeDef = TypedDict(
    "BatchCreateCustomVocabularyItemRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "customVocabularyItemList": List["NewCustomVocabularyItemTypeDef"],
    },
)

BatchCreateCustomVocabularyItemResponseTypeDef = TypedDict(
    "BatchCreateCustomVocabularyItemResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "errors": List["FailedCustomVocabularyItemTypeDef"],
        "resources": List["CustomVocabularyItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteCustomVocabularyItemRequestRequestTypeDef = TypedDict(
    "BatchDeleteCustomVocabularyItemRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "customVocabularyItemList": List["CustomVocabularyEntryIdTypeDef"],
    },
)

BatchDeleteCustomVocabularyItemResponseTypeDef = TypedDict(
    "BatchDeleteCustomVocabularyItemResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "errors": List["FailedCustomVocabularyItemTypeDef"],
        "resources": List["CustomVocabularyItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdateCustomVocabularyItemRequestRequestTypeDef = TypedDict(
    "BatchUpdateCustomVocabularyItemRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "customVocabularyItemList": List["CustomVocabularyItemTypeDef"],
    },
)

BatchUpdateCustomVocabularyItemResponseTypeDef = TypedDict(
    "BatchUpdateCustomVocabularyItemResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "errors": List["FailedCustomVocabularyItemTypeDef"],
        "resources": List["CustomVocabularyItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BotAliasHistoryEventTypeDef = TypedDict(
    "BotAliasHistoryEventTypeDef",
    {
        "botVersion": str,
        "startDate": datetime,
        "endDate": datetime,
    },
    total=False,
)

_RequiredBotAliasLocaleSettingsTypeDef = TypedDict(
    "_RequiredBotAliasLocaleSettingsTypeDef",
    {
        "enabled": bool,
    },
)
_OptionalBotAliasLocaleSettingsTypeDef = TypedDict(
    "_OptionalBotAliasLocaleSettingsTypeDef",
    {
        "codeHookSpecification": "CodeHookSpecificationTypeDef",
    },
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
        "botAliasStatus": BotAliasStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

BotAliasTestExecutionTargetTypeDef = TypedDict(
    "BotAliasTestExecutionTargetTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
    },
)

BotExportSpecificationTypeDef = TypedDict(
    "BotExportSpecificationTypeDef",
    {
        "botId": str,
        "botVersion": str,
    },
)

BotFilterTypeDef = TypedDict(
    "BotFilterTypeDef",
    {
        "name": BotFilterNameType,
        "values": List[str],
        "operator": BotFilterOperatorType,
    },
)

_RequiredBotImportSpecificationTypeDef = TypedDict(
    "_RequiredBotImportSpecificationTypeDef",
    {
        "botName": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
    },
)
_OptionalBotImportSpecificationTypeDef = TypedDict(
    "_OptionalBotImportSpecificationTypeDef",
    {
        "idleSessionTTLInSeconds": int,
        "botTags": Dict[str, str],
        "testBotAliasTags": Dict[str, str],
    },
    total=False,
)

class BotImportSpecificationTypeDef(
    _RequiredBotImportSpecificationTypeDef, _OptionalBotImportSpecificationTypeDef
):
    pass

BotLocaleExportSpecificationTypeDef = TypedDict(
    "BotLocaleExportSpecificationTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

BotLocaleFilterTypeDef = TypedDict(
    "BotLocaleFilterTypeDef",
    {
        "name": Literal["BotLocaleName"],
        "values": List[str],
        "operator": BotLocaleFilterOperatorType,
    },
)

BotLocaleHistoryEventTypeDef = TypedDict(
    "BotLocaleHistoryEventTypeDef",
    {
        "event": str,
        "eventDate": datetime,
    },
)

_RequiredBotLocaleImportSpecificationTypeDef = TypedDict(
    "_RequiredBotLocaleImportSpecificationTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalBotLocaleImportSpecificationTypeDef = TypedDict(
    "_OptionalBotLocaleImportSpecificationTypeDef",
    {
        "nluIntentConfidenceThreshold": float,
        "voiceSettings": "VoiceSettingsTypeDef",
    },
    total=False,
)

class BotLocaleImportSpecificationTypeDef(
    _RequiredBotLocaleImportSpecificationTypeDef, _OptionalBotLocaleImportSpecificationTypeDef
):
    pass

BotLocaleSortByTypeDef = TypedDict(
    "BotLocaleSortByTypeDef",
    {
        "attribute": Literal["BotLocaleName"],
        "order": SortOrderType,
    },
)

BotLocaleSummaryTypeDef = TypedDict(
    "BotLocaleSummaryTypeDef",
    {
        "localeId": str,
        "localeName": str,
        "description": str,
        "botLocaleStatus": BotLocaleStatusType,
        "lastUpdatedDateTime": datetime,
        "lastBuildSubmittedDateTime": datetime,
    },
    total=False,
)

BotMemberTypeDef = TypedDict(
    "BotMemberTypeDef",
    {
        "botMemberId": str,
        "botMemberName": str,
        "botMemberAliasId": str,
        "botMemberAliasName": str,
        "botMemberVersion": str,
    },
)

BotRecommendationResultStatisticsTypeDef = TypedDict(
    "BotRecommendationResultStatisticsTypeDef",
    {
        "intents": "IntentStatisticsTypeDef",
        "slotTypes": "SlotTypeStatisticsTypeDef",
    },
    total=False,
)

BotRecommendationResultsTypeDef = TypedDict(
    "BotRecommendationResultsTypeDef",
    {
        "botLocaleExportUrl": str,
        "associatedTranscriptsUrl": str,
        "statistics": "BotRecommendationResultStatisticsTypeDef",
    },
    total=False,
)

_RequiredBotRecommendationSummaryTypeDef = TypedDict(
    "_RequiredBotRecommendationSummaryTypeDef",
    {
        "botRecommendationStatus": BotRecommendationStatusType,
        "botRecommendationId": str,
    },
)
_OptionalBotRecommendationSummaryTypeDef = TypedDict(
    "_OptionalBotRecommendationSummaryTypeDef",
    {
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

class BotRecommendationSummaryTypeDef(
    _RequiredBotRecommendationSummaryTypeDef, _OptionalBotRecommendationSummaryTypeDef
):
    pass

BotSortByTypeDef = TypedDict(
    "BotSortByTypeDef",
    {
        "attribute": Literal["BotName"],
        "order": SortOrderType,
    },
)

BotSummaryTypeDef = TypedDict(
    "BotSummaryTypeDef",
    {
        "botId": str,
        "botName": str,
        "description": str,
        "botStatus": BotStatusType,
        "latestBotVersion": str,
        "lastUpdatedDateTime": datetime,
        "botType": BotTypeType,
    },
    total=False,
)

BotVersionLocaleDetailsTypeDef = TypedDict(
    "BotVersionLocaleDetailsTypeDef",
    {
        "sourceBotVersion": str,
    },
)

BotVersionSortByTypeDef = TypedDict(
    "BotVersionSortByTypeDef",
    {
        "attribute": Literal["BotVersion"],
        "order": SortOrderType,
    },
)

BotVersionSummaryTypeDef = TypedDict(
    "BotVersionSummaryTypeDef",
    {
        "botName": str,
        "botVersion": str,
        "description": str,
        "botStatus": BotStatusType,
        "creationDateTime": datetime,
    },
    total=False,
)

BuildBotLocaleRequestRequestTypeDef = TypedDict(
    "BuildBotLocaleRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

BuildBotLocaleResponseTypeDef = TypedDict(
    "BuildBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botLocaleStatus": BotLocaleStatusType,
        "lastBuildSubmittedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BuiltInIntentSortByTypeDef = TypedDict(
    "BuiltInIntentSortByTypeDef",
    {
        "attribute": Literal["IntentSignature"],
        "order": SortOrderType,
    },
)

BuiltInIntentSummaryTypeDef = TypedDict(
    "BuiltInIntentSummaryTypeDef",
    {
        "intentSignature": str,
        "description": str,
    },
    total=False,
)

BuiltInSlotTypeSortByTypeDef = TypedDict(
    "BuiltInSlotTypeSortByTypeDef",
    {
        "attribute": Literal["SlotTypeSignature"],
        "order": SortOrderType,
    },
)

BuiltInSlotTypeSummaryTypeDef = TypedDict(
    "BuiltInSlotTypeSummaryTypeDef",
    {
        "slotTypeSignature": str,
        "description": str,
    },
    total=False,
)

ButtonTypeDef = TypedDict(
    "ButtonTypeDef",
    {
        "text": str,
        "value": str,
    },
)

CloudWatchLogGroupLogDestinationTypeDef = TypedDict(
    "CloudWatchLogGroupLogDestinationTypeDef",
    {
        "cloudWatchLogGroupArn": str,
        "logPrefix": str,
    },
)

CodeHookSpecificationTypeDef = TypedDict(
    "CodeHookSpecificationTypeDef",
    {
        "lambdaCodeHook": "LambdaCodeHookTypeDef",
    },
)

CompositeSlotTypeSettingTypeDef = TypedDict(
    "CompositeSlotTypeSettingTypeDef",
    {
        "subSlots": List["SubSlotTypeCompositionTypeDef"],
    },
    total=False,
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "expressionString": str,
    },
)

_RequiredConditionalBranchTypeDef = TypedDict(
    "_RequiredConditionalBranchTypeDef",
    {
        "name": str,
        "condition": "ConditionTypeDef",
        "nextStep": "DialogStateTypeDef",
    },
)
_OptionalConditionalBranchTypeDef = TypedDict(
    "_OptionalConditionalBranchTypeDef",
    {
        "response": "ResponseSpecificationTypeDef",
    },
    total=False,
)

class ConditionalBranchTypeDef(
    _RequiredConditionalBranchTypeDef, _OptionalConditionalBranchTypeDef
):
    pass

ConditionalSpecificationTypeDef = TypedDict(
    "ConditionalSpecificationTypeDef",
    {
        "active": bool,
        "conditionalBranches": List["ConditionalBranchTypeDef"],
        "defaultBranch": "DefaultConditionalBranchTypeDef",
    },
)

ConversationLevelIntentClassificationResultItemTypeDef = TypedDict(
    "ConversationLevelIntentClassificationResultItemTypeDef",
    {
        "intentName": str,
        "matchResult": TestResultMatchStatusType,
    },
)

_RequiredConversationLevelResultDetailTypeDef = TypedDict(
    "_RequiredConversationLevelResultDetailTypeDef",
    {
        "endToEndResult": TestResultMatchStatusType,
    },
)
_OptionalConversationLevelResultDetailTypeDef = TypedDict(
    "_OptionalConversationLevelResultDetailTypeDef",
    {
        "speechTranscriptionResult": TestResultMatchStatusType,
    },
    total=False,
)

class ConversationLevelResultDetailTypeDef(
    _RequiredConversationLevelResultDetailTypeDef, _OptionalConversationLevelResultDetailTypeDef
):
    pass

ConversationLevelSlotResolutionResultItemTypeDef = TypedDict(
    "ConversationLevelSlotResolutionResultItemTypeDef",
    {
        "intentName": str,
        "slotName": str,
        "matchResult": TestResultMatchStatusType,
    },
)

_RequiredConversationLevelTestResultItemTypeDef = TypedDict(
    "_RequiredConversationLevelTestResultItemTypeDef",
    {
        "conversationId": str,
        "endToEndResult": TestResultMatchStatusType,
        "intentClassificationResults": List[
            "ConversationLevelIntentClassificationResultItemTypeDef"
        ],
        "slotResolutionResults": List["ConversationLevelSlotResolutionResultItemTypeDef"],
    },
)
_OptionalConversationLevelTestResultItemTypeDef = TypedDict(
    "_OptionalConversationLevelTestResultItemTypeDef",
    {
        "speechTranscriptionResult": TestResultMatchStatusType,
    },
    total=False,
)

class ConversationLevelTestResultItemTypeDef(
    _RequiredConversationLevelTestResultItemTypeDef, _OptionalConversationLevelTestResultItemTypeDef
):
    pass

ConversationLevelTestResultsFilterByTypeDef = TypedDict(
    "ConversationLevelTestResultsFilterByTypeDef",
    {
        "endToEndResult": TestResultMatchStatusType,
    },
    total=False,
)

ConversationLevelTestResultsTypeDef = TypedDict(
    "ConversationLevelTestResultsTypeDef",
    {
        "items": List["ConversationLevelTestResultItemTypeDef"],
    },
)

ConversationLogSettingsTypeDef = TypedDict(
    "ConversationLogSettingsTypeDef",
    {
        "textLogSettings": List["TextLogSettingTypeDef"],
        "audioLogSettings": List["AudioLogSettingTypeDef"],
    },
    total=False,
)

ConversationLogsDataSourceFilterByTypeDef = TypedDict(
    "ConversationLogsDataSourceFilterByTypeDef",
    {
        "startTime": datetime,
        "endTime": datetime,
        "inputMode": ConversationLogsInputModeFilterType,
    },
)

ConversationLogsDataSourceTypeDef = TypedDict(
    "ConversationLogsDataSourceTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "filter": "ConversationLogsDataSourceFilterByTypeDef",
    },
)

_RequiredCreateBotAliasRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBotAliasRequestRequestTypeDef",
    {
        "botAliasName": str,
        "botId": str,
    },
)
_OptionalCreateBotAliasRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBotAliasRequestRequestTypeDef",
    {
        "description": str,
        "botVersion": str,
        "botAliasLocaleSettings": Dict[str, "BotAliasLocaleSettingsTypeDef"],
        "conversationLogSettings": "ConversationLogSettingsTypeDef",
        "sentimentAnalysisSettings": "SentimentAnalysisSettingsTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateBotAliasRequestRequestTypeDef(
    _RequiredCreateBotAliasRequestRequestTypeDef, _OptionalCreateBotAliasRequestRequestTypeDef
):
    pass

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
        "botAliasStatus": BotAliasStatusType,
        "botId": str,
        "creationDateTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBotLocaleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBotLocaleRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "nluIntentConfidenceThreshold": float,
    },
)
_OptionalCreateBotLocaleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBotLocaleRequestRequestTypeDef",
    {
        "description": str,
        "voiceSettings": "VoiceSettingsTypeDef",
    },
    total=False,
)

class CreateBotLocaleRequestRequestTypeDef(
    _RequiredCreateBotLocaleRequestRequestTypeDef, _OptionalCreateBotLocaleRequestRequestTypeDef
):
    pass

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
        "botLocaleStatus": BotLocaleStatusType,
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBotRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBotRequestRequestTypeDef",
    {
        "botName": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": int,
    },
)
_OptionalCreateBotRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBotRequestRequestTypeDef",
    {
        "description": str,
        "botTags": Dict[str, str],
        "testBotAliasTags": Dict[str, str],
        "botType": BotTypeType,
        "botMembers": List["BotMemberTypeDef"],
    },
    total=False,
)

class CreateBotRequestRequestTypeDef(
    _RequiredCreateBotRequestRequestTypeDef, _OptionalCreateBotRequestRequestTypeDef
):
    pass

CreateBotResponseTypeDef = TypedDict(
    "CreateBotResponseTypeDef",
    {
        "botId": str,
        "botName": str,
        "description": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": int,
        "botStatus": BotStatusType,
        "creationDateTime": datetime,
        "botTags": Dict[str, str],
        "testBotAliasTags": Dict[str, str],
        "botType": BotTypeType,
        "botMembers": List["BotMemberTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBotVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBotVersionRequestRequestTypeDef",
    {
        "botId": str,
        "botVersionLocaleSpecification": Dict[str, "BotVersionLocaleDetailsTypeDef"],
    },
)
_OptionalCreateBotVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBotVersionRequestRequestTypeDef",
    {
        "description": str,
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
        "botId": str,
        "description": str,
        "botVersion": str,
        "botVersionLocaleSpecification": Dict[str, "BotVersionLocaleDetailsTypeDef"],
        "botStatus": BotStatusType,
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateExportRequestRequestTypeDef = TypedDict(
    "_RequiredCreateExportRequestRequestTypeDef",
    {
        "resourceSpecification": "ExportResourceSpecificationTypeDef",
        "fileFormat": ImportExportFileFormatType,
    },
)
_OptionalCreateExportRequestRequestTypeDef = TypedDict(
    "_OptionalCreateExportRequestRequestTypeDef",
    {
        "filePassword": str,
    },
    total=False,
)

class CreateExportRequestRequestTypeDef(
    _RequiredCreateExportRequestRequestTypeDef, _OptionalCreateExportRequestRequestTypeDef
):
    pass

CreateExportResponseTypeDef = TypedDict(
    "CreateExportResponseTypeDef",
    {
        "exportId": str,
        "resourceSpecification": "ExportResourceSpecificationTypeDef",
        "fileFormat": ImportExportFileFormatType,
        "exportStatus": ExportStatusType,
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIntentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIntentRequestRequestTypeDef",
    {
        "intentName": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalCreateIntentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIntentRequestRequestTypeDef",
    {
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
        "initialResponseSetting": "InitialResponseSettingTypeDef",
    },
    total=False,
)

class CreateIntentRequestRequestTypeDef(
    _RequiredCreateIntentRequestRequestTypeDef, _OptionalCreateIntentRequestRequestTypeDef
):
    pass

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
        "initialResponseSetting": "InitialResponseSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResourcePolicyRequestRequestTypeDef = TypedDict(
    "CreateResourcePolicyRequestRequestTypeDef",
    {
        "resourceArn": str,
        "policy": str,
    },
)

CreateResourcePolicyResponseTypeDef = TypedDict(
    "CreateResourcePolicyResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateResourcePolicyStatementRequestRequestTypeDef = TypedDict(
    "_RequiredCreateResourcePolicyStatementRequestRequestTypeDef",
    {
        "resourceArn": str,
        "statementId": str,
        "effect": EffectType,
        "principal": List["PrincipalTypeDef"],
        "action": List[str],
    },
)
_OptionalCreateResourcePolicyStatementRequestRequestTypeDef = TypedDict(
    "_OptionalCreateResourcePolicyStatementRequestRequestTypeDef",
    {
        "condition": Dict[str, Dict[str, str]],
        "expectedRevisionId": str,
    },
    total=False,
)

class CreateResourcePolicyStatementRequestRequestTypeDef(
    _RequiredCreateResourcePolicyStatementRequestRequestTypeDef,
    _OptionalCreateResourcePolicyStatementRequestRequestTypeDef,
):
    pass

CreateResourcePolicyStatementResponseTypeDef = TypedDict(
    "CreateResourcePolicyStatementResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSlotRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSlotRequestRequestTypeDef",
    {
        "slotName": str,
        "valueElicitationSetting": "SlotValueElicitationSettingTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
    },
)
_OptionalCreateSlotRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSlotRequestRequestTypeDef",
    {
        "description": str,
        "slotTypeId": str,
        "obfuscationSetting": "ObfuscationSettingTypeDef",
        "multipleValuesSetting": "MultipleValuesSettingTypeDef",
        "subSlotSetting": "SubSlotSettingTypeDef",
    },
    total=False,
)

class CreateSlotRequestRequestTypeDef(
    _RequiredCreateSlotRequestRequestTypeDef, _OptionalCreateSlotRequestRequestTypeDef
):
    pass

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
        "multipleValuesSetting": "MultipleValuesSettingTypeDef",
        "subSlotSetting": "SubSlotSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSlotTypeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSlotTypeRequestRequestTypeDef",
    {
        "slotTypeName": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalCreateSlotTypeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSlotTypeRequestRequestTypeDef",
    {
        "description": str,
        "slotTypeValues": List["SlotTypeValueTypeDef"],
        "valueSelectionSetting": "SlotValueSelectionSettingTypeDef",
        "parentSlotTypeSignature": str,
        "externalSourceSetting": "ExternalSourceSettingTypeDef",
        "compositeSlotTypeSetting": "CompositeSlotTypeSettingTypeDef",
    },
    total=False,
)

class CreateSlotTypeRequestRequestTypeDef(
    _RequiredCreateSlotTypeRequestRequestTypeDef, _OptionalCreateSlotTypeRequestRequestTypeDef
):
    pass

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
        "externalSourceSetting": "ExternalSourceSettingTypeDef",
        "compositeSlotTypeSetting": "CompositeSlotTypeSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTestSetDiscrepancyReportRequestRequestTypeDef = TypedDict(
    "CreateTestSetDiscrepancyReportRequestRequestTypeDef",
    {
        "testSetId": str,
        "target": "TestSetDiscrepancyReportResourceTargetTypeDef",
    },
)

CreateTestSetDiscrepancyReportResponseTypeDef = TypedDict(
    "CreateTestSetDiscrepancyReportResponseTypeDef",
    {
        "testSetDiscrepancyReportId": str,
        "creationDateTime": datetime,
        "testSetId": str,
        "target": "TestSetDiscrepancyReportResourceTargetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUploadUrlResponseTypeDef = TypedDict(
    "CreateUploadUrlResponseTypeDef",
    {
        "importId": str,
        "uploadUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomPayloadTypeDef = TypedDict(
    "CustomPayloadTypeDef",
    {
        "value": str,
    },
)

CustomVocabularyEntryIdTypeDef = TypedDict(
    "CustomVocabularyEntryIdTypeDef",
    {
        "itemId": str,
    },
)

CustomVocabularyExportSpecificationTypeDef = TypedDict(
    "CustomVocabularyExportSpecificationTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

CustomVocabularyImportSpecificationTypeDef = TypedDict(
    "CustomVocabularyImportSpecificationTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

_RequiredCustomVocabularyItemTypeDef = TypedDict(
    "_RequiredCustomVocabularyItemTypeDef",
    {
        "itemId": str,
        "phrase": str,
    },
)
_OptionalCustomVocabularyItemTypeDef = TypedDict(
    "_OptionalCustomVocabularyItemTypeDef",
    {
        "weight": int,
        "displayAs": str,
    },
    total=False,
)

class CustomVocabularyItemTypeDef(
    _RequiredCustomVocabularyItemTypeDef, _OptionalCustomVocabularyItemTypeDef
):
    pass

DTMFSpecificationTypeDef = TypedDict(
    "DTMFSpecificationTypeDef",
    {
        "maxLength": int,
        "endTimeoutMs": int,
        "deletionCharacter": str,
        "endCharacter": str,
    },
)

DataPrivacyTypeDef = TypedDict(
    "DataPrivacyTypeDef",
    {
        "childDirected": bool,
    },
)

DateRangeFilterTypeDef = TypedDict(
    "DateRangeFilterTypeDef",
    {
        "startDateTime": datetime,
        "endDateTime": datetime,
    },
)

DefaultConditionalBranchTypeDef = TypedDict(
    "DefaultConditionalBranchTypeDef",
    {
        "nextStep": "DialogStateTypeDef",
        "response": "ResponseSpecificationTypeDef",
    },
    total=False,
)

_RequiredDeleteBotAliasRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBotAliasRequestRequestTypeDef",
    {
        "botAliasId": str,
        "botId": str,
    },
)
_OptionalDeleteBotAliasRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBotAliasRequestRequestTypeDef",
    {
        "skipResourceInUseCheck": bool,
    },
    total=False,
)

class DeleteBotAliasRequestRequestTypeDef(
    _RequiredDeleteBotAliasRequestRequestTypeDef, _OptionalDeleteBotAliasRequestRequestTypeDef
):
    pass

DeleteBotAliasResponseTypeDef = TypedDict(
    "DeleteBotAliasResponseTypeDef",
    {
        "botAliasId": str,
        "botId": str,
        "botAliasStatus": BotAliasStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBotLocaleRequestRequestTypeDef = TypedDict(
    "DeleteBotLocaleRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DeleteBotLocaleResponseTypeDef = TypedDict(
    "DeleteBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botLocaleStatus": BotLocaleStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteBotRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBotRequestRequestTypeDef",
    {
        "botId": str,
    },
)
_OptionalDeleteBotRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBotRequestRequestTypeDef",
    {
        "skipResourceInUseCheck": bool,
    },
    total=False,
)

class DeleteBotRequestRequestTypeDef(
    _RequiredDeleteBotRequestRequestTypeDef, _OptionalDeleteBotRequestRequestTypeDef
):
    pass

DeleteBotResponseTypeDef = TypedDict(
    "DeleteBotResponseTypeDef",
    {
        "botId": str,
        "botStatus": BotStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteBotVersionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBotVersionRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
    },
)
_OptionalDeleteBotVersionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBotVersionRequestRequestTypeDef",
    {
        "skipResourceInUseCheck": bool,
    },
    total=False,
)

class DeleteBotVersionRequestRequestTypeDef(
    _RequiredDeleteBotVersionRequestRequestTypeDef, _OptionalDeleteBotVersionRequestRequestTypeDef
):
    pass

DeleteBotVersionResponseTypeDef = TypedDict(
    "DeleteBotVersionResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "botStatus": BotStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCustomVocabularyRequestRequestTypeDef = TypedDict(
    "DeleteCustomVocabularyRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DeleteCustomVocabularyResponseTypeDef = TypedDict(
    "DeleteCustomVocabularyResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "customVocabularyStatus": CustomVocabularyStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteExportRequestRequestTypeDef = TypedDict(
    "DeleteExportRequestRequestTypeDef",
    {
        "exportId": str,
    },
)

DeleteExportResponseTypeDef = TypedDict(
    "DeleteExportResponseTypeDef",
    {
        "exportId": str,
        "exportStatus": ExportStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteImportRequestRequestTypeDef = TypedDict(
    "DeleteImportRequestRequestTypeDef",
    {
        "importId": str,
    },
)

DeleteImportResponseTypeDef = TypedDict(
    "DeleteImportResponseTypeDef",
    {
        "importId": str,
        "importStatus": ImportStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIntentRequestRequestTypeDef = TypedDict(
    "DeleteIntentRequestRequestTypeDef",
    {
        "intentId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

_RequiredDeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteResourcePolicyRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalDeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteResourcePolicyRequestRequestTypeDef",
    {
        "expectedRevisionId": str,
    },
    total=False,
)

class DeleteResourcePolicyRequestRequestTypeDef(
    _RequiredDeleteResourcePolicyRequestRequestTypeDef,
    _OptionalDeleteResourcePolicyRequestRequestTypeDef,
):
    pass

DeleteResourcePolicyResponseTypeDef = TypedDict(
    "DeleteResourcePolicyResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteResourcePolicyStatementRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteResourcePolicyStatementRequestRequestTypeDef",
    {
        "resourceArn": str,
        "statementId": str,
    },
)
_OptionalDeleteResourcePolicyStatementRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteResourcePolicyStatementRequestRequestTypeDef",
    {
        "expectedRevisionId": str,
    },
    total=False,
)

class DeleteResourcePolicyStatementRequestRequestTypeDef(
    _RequiredDeleteResourcePolicyStatementRequestRequestTypeDef,
    _OptionalDeleteResourcePolicyStatementRequestRequestTypeDef,
):
    pass

DeleteResourcePolicyStatementResponseTypeDef = TypedDict(
    "DeleteResourcePolicyStatementResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSlotRequestRequestTypeDef = TypedDict(
    "DeleteSlotRequestRequestTypeDef",
    {
        "slotId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
    },
)

_RequiredDeleteSlotTypeRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteSlotTypeRequestRequestTypeDef",
    {
        "slotTypeId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalDeleteSlotTypeRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteSlotTypeRequestRequestTypeDef",
    {
        "skipResourceInUseCheck": bool,
    },
    total=False,
)

class DeleteSlotTypeRequestRequestTypeDef(
    _RequiredDeleteSlotTypeRequestRequestTypeDef, _OptionalDeleteSlotTypeRequestRequestTypeDef
):
    pass

DeleteTestSetRequestRequestTypeDef = TypedDict(
    "DeleteTestSetRequestRequestTypeDef",
    {
        "testSetId": str,
    },
)

_RequiredDeleteUtterancesRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteUtterancesRequestRequestTypeDef",
    {
        "botId": str,
    },
)
_OptionalDeleteUtterancesRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteUtterancesRequestRequestTypeDef",
    {
        "localeId": str,
        "sessionId": str,
    },
    total=False,
)

class DeleteUtterancesRequestRequestTypeDef(
    _RequiredDeleteUtterancesRequestRequestTypeDef, _OptionalDeleteUtterancesRequestRequestTypeDef
):
    pass

DescribeBotAliasRequestRequestTypeDef = TypedDict(
    "DescribeBotAliasRequestRequestTypeDef",
    {
        "botAliasId": str,
        "botId": str,
    },
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
        "botAliasStatus": BotAliasStatusType,
        "botId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "parentBotNetworks": List["ParentBotNetworkTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBotLocaleRequestRequestTypeDef = TypedDict(
    "DescribeBotLocaleRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
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
        "botLocaleStatus": BotLocaleStatusType,
        "failureReasons": List[str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "lastBuildSubmittedDateTime": datetime,
        "botLocaleHistoryEvents": List["BotLocaleHistoryEventTypeDef"],
        "recommendedActions": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBotRecommendationRequestRequestTypeDef = TypedDict(
    "DescribeBotRecommendationRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationId": str,
    },
)

DescribeBotRecommendationResponseTypeDef = TypedDict(
    "DescribeBotRecommendationResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationStatus": BotRecommendationStatusType,
        "botRecommendationId": str,
        "failureReasons": List[str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "transcriptSourceSetting": "TranscriptSourceSettingTypeDef",
        "encryptionSetting": "EncryptionSettingTypeDef",
        "botRecommendationResults": "BotRecommendationResultsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBotRequestRequestTypeDef = TypedDict(
    "DescribeBotRequestRequestTypeDef",
    {
        "botId": str,
    },
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
        "botStatus": BotStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "botType": BotTypeType,
        "botMembers": List["BotMemberTypeDef"],
        "failureReasons": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBotVersionRequestRequestTypeDef = TypedDict(
    "DescribeBotVersionRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
    },
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
        "botStatus": BotStatusType,
        "failureReasons": List[str],
        "creationDateTime": datetime,
        "parentBotNetworks": List["ParentBotNetworkTypeDef"],
        "botType": BotTypeType,
        "botMembers": List["BotMemberTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomVocabularyMetadataRequestRequestTypeDef = TypedDict(
    "DescribeCustomVocabularyMetadataRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DescribeCustomVocabularyMetadataResponseTypeDef = TypedDict(
    "DescribeCustomVocabularyMetadataResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "customVocabularyStatus": CustomVocabularyStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportRequestRequestTypeDef = TypedDict(
    "DescribeExportRequestRequestTypeDef",
    {
        "exportId": str,
    },
)

DescribeExportResponseTypeDef = TypedDict(
    "DescribeExportResponseTypeDef",
    {
        "exportId": str,
        "resourceSpecification": "ExportResourceSpecificationTypeDef",
        "fileFormat": ImportExportFileFormatType,
        "exportStatus": ExportStatusType,
        "failureReasons": List[str],
        "downloadUrl": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImportRequestRequestTypeDef = TypedDict(
    "DescribeImportRequestRequestTypeDef",
    {
        "importId": str,
    },
)

DescribeImportResponseTypeDef = TypedDict(
    "DescribeImportResponseTypeDef",
    {
        "importId": str,
        "resourceSpecification": "ImportResourceSpecificationTypeDef",
        "importedResourceId": str,
        "importedResourceName": str,
        "mergeStrategy": MergeStrategyType,
        "importStatus": ImportStatusType,
        "failureReasons": List[str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIntentRequestRequestTypeDef = TypedDict(
    "DescribeIntentRequestRequestTypeDef",
    {
        "intentId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
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
        "initialResponseSetting": "InitialResponseSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourcePolicyRequestRequestTypeDef = TypedDict(
    "DescribeResourcePolicyRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

DescribeResourcePolicyResponseTypeDef = TypedDict(
    "DescribeResourcePolicyResponseTypeDef",
    {
        "resourceArn": str,
        "policy": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSlotRequestRequestTypeDef = TypedDict(
    "DescribeSlotRequestRequestTypeDef",
    {
        "slotId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
    },
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
        "multipleValuesSetting": "MultipleValuesSettingTypeDef",
        "subSlotSetting": "SubSlotSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSlotTypeRequestRequestTypeDef = TypedDict(
    "DescribeSlotTypeRequestRequestTypeDef",
    {
        "slotTypeId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
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
        "externalSourceSetting": "ExternalSourceSettingTypeDef",
        "compositeSlotTypeSetting": "CompositeSlotTypeSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTestExecutionRequestRequestTypeDef = TypedDict(
    "DescribeTestExecutionRequestRequestTypeDef",
    {
        "testExecutionId": str,
    },
)

DescribeTestExecutionResponseTypeDef = TypedDict(
    "DescribeTestExecutionResponseTypeDef",
    {
        "testExecutionId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "testExecutionStatus": TestExecutionStatusType,
        "testSetId": str,
        "testSetName": str,
        "target": "TestExecutionTargetTypeDef",
        "apiMode": TestExecutionApiModeType,
        "testExecutionModality": TestExecutionModalityType,
        "failureReasons": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTestSetDiscrepancyReportRequestRequestTypeDef = TypedDict(
    "DescribeTestSetDiscrepancyReportRequestRequestTypeDef",
    {
        "testSetDiscrepancyReportId": str,
    },
)

DescribeTestSetDiscrepancyReportResponseTypeDef = TypedDict(
    "DescribeTestSetDiscrepancyReportResponseTypeDef",
    {
        "testSetDiscrepancyReportId": str,
        "testSetId": str,
        "creationDateTime": datetime,
        "target": "TestSetDiscrepancyReportResourceTargetTypeDef",
        "testSetDiscrepancyReportStatus": TestSetDiscrepancyReportStatusType,
        "lastUpdatedDataTime": datetime,
        "testSetDiscrepancyTopErrors": "TestSetDiscrepancyErrorsTypeDef",
        "testSetDiscrepancyRawOutputUrl": str,
        "failureReasons": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTestSetGenerationRequestRequestTypeDef = TypedDict(
    "DescribeTestSetGenerationRequestRequestTypeDef",
    {
        "testSetGenerationId": str,
    },
)

DescribeTestSetGenerationResponseTypeDef = TypedDict(
    "DescribeTestSetGenerationResponseTypeDef",
    {
        "testSetGenerationId": str,
        "testSetGenerationStatus": TestSetGenerationStatusType,
        "failureReasons": List[str],
        "testSetId": str,
        "testSetName": str,
        "description": str,
        "storageLocation": "TestSetStorageLocationTypeDef",
        "generationDataSource": "TestSetGenerationDataSourceTypeDef",
        "roleArn": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTestSetRequestRequestTypeDef = TypedDict(
    "DescribeTestSetRequestRequestTypeDef",
    {
        "testSetId": str,
    },
)

DescribeTestSetResponseTypeDef = TypedDict(
    "DescribeTestSetResponseTypeDef",
    {
        "testSetId": str,
        "testSetName": str,
        "description": str,
        "modality": TestSetModalityType,
        "status": TestSetStatusType,
        "roleArn": str,
        "numTurns": int,
        "storageLocation": "TestSetStorageLocationTypeDef",
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDialogActionTypeDef = TypedDict(
    "_RequiredDialogActionTypeDef",
    {
        "type": DialogActionTypeType,
    },
)
_OptionalDialogActionTypeDef = TypedDict(
    "_OptionalDialogActionTypeDef",
    {
        "slotToElicit": str,
        "suppressNextMessage": bool,
    },
    total=False,
)

class DialogActionTypeDef(_RequiredDialogActionTypeDef, _OptionalDialogActionTypeDef):
    pass

_RequiredDialogCodeHookInvocationSettingTypeDef = TypedDict(
    "_RequiredDialogCodeHookInvocationSettingTypeDef",
    {
        "enableCodeHookInvocation": bool,
        "active": bool,
        "postCodeHookSpecification": "PostDialogCodeHookInvocationSpecificationTypeDef",
    },
)
_OptionalDialogCodeHookInvocationSettingTypeDef = TypedDict(
    "_OptionalDialogCodeHookInvocationSettingTypeDef",
    {
        "invocationLabel": str,
    },
    total=False,
)

class DialogCodeHookInvocationSettingTypeDef(
    _RequiredDialogCodeHookInvocationSettingTypeDef, _OptionalDialogCodeHookInvocationSettingTypeDef
):
    pass

DialogCodeHookSettingsTypeDef = TypedDict(
    "DialogCodeHookSettingsTypeDef",
    {
        "enabled": bool,
    },
)

DialogStateTypeDef = TypedDict(
    "DialogStateTypeDef",
    {
        "dialogAction": "DialogActionTypeDef",
        "intent": "IntentOverrideTypeDef",
        "sessionAttributes": Dict[str, str],
    },
    total=False,
)

_RequiredElicitationCodeHookInvocationSettingTypeDef = TypedDict(
    "_RequiredElicitationCodeHookInvocationSettingTypeDef",
    {
        "enableCodeHookInvocation": bool,
    },
)
_OptionalElicitationCodeHookInvocationSettingTypeDef = TypedDict(
    "_OptionalElicitationCodeHookInvocationSettingTypeDef",
    {
        "invocationLabel": str,
    },
    total=False,
)

class ElicitationCodeHookInvocationSettingTypeDef(
    _RequiredElicitationCodeHookInvocationSettingTypeDef,
    _OptionalElicitationCodeHookInvocationSettingTypeDef,
):
    pass

EncryptionSettingTypeDef = TypedDict(
    "EncryptionSettingTypeDef",
    {
        "kmsKeyArn": str,
        "botLocaleExportPassword": str,
        "associatedTranscriptsPassword": str,
    },
    total=False,
)

ExecutionErrorDetailsTypeDef = TypedDict(
    "ExecutionErrorDetailsTypeDef",
    {
        "errorCode": str,
        "errorMessage": str,
    },
)

ExportFilterTypeDef = TypedDict(
    "ExportFilterTypeDef",
    {
        "name": Literal["ExportResourceType"],
        "values": List[str],
        "operator": ExportFilterOperatorType,
    },
)

ExportResourceSpecificationTypeDef = TypedDict(
    "ExportResourceSpecificationTypeDef",
    {
        "botExportSpecification": "BotExportSpecificationTypeDef",
        "botLocaleExportSpecification": "BotLocaleExportSpecificationTypeDef",
        "customVocabularyExportSpecification": "CustomVocabularyExportSpecificationTypeDef",
        "testSetExportSpecification": "TestSetExportSpecificationTypeDef",
    },
    total=False,
)

ExportSortByTypeDef = TypedDict(
    "ExportSortByTypeDef",
    {
        "attribute": Literal["LastUpdatedDateTime"],
        "order": SortOrderType,
    },
)

ExportSummaryTypeDef = TypedDict(
    "ExportSummaryTypeDef",
    {
        "exportId": str,
        "resourceSpecification": "ExportResourceSpecificationTypeDef",
        "fileFormat": ImportExportFileFormatType,
        "exportStatus": ExportStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

ExternalSourceSettingTypeDef = TypedDict(
    "ExternalSourceSettingTypeDef",
    {
        "grammarSlotTypeSetting": "GrammarSlotTypeSettingTypeDef",
    },
    total=False,
)

FailedCustomVocabularyItemTypeDef = TypedDict(
    "FailedCustomVocabularyItemTypeDef",
    {
        "itemId": str,
        "errorMessage": str,
        "errorCode": ErrorCodeType,
    },
    total=False,
)

_RequiredFulfillmentCodeHookSettingsTypeDef = TypedDict(
    "_RequiredFulfillmentCodeHookSettingsTypeDef",
    {
        "enabled": bool,
    },
)
_OptionalFulfillmentCodeHookSettingsTypeDef = TypedDict(
    "_OptionalFulfillmentCodeHookSettingsTypeDef",
    {
        "postFulfillmentStatusSpecification": "PostFulfillmentStatusSpecificationTypeDef",
        "fulfillmentUpdatesSpecification": "FulfillmentUpdatesSpecificationTypeDef",
        "active": bool,
    },
    total=False,
)

class FulfillmentCodeHookSettingsTypeDef(
    _RequiredFulfillmentCodeHookSettingsTypeDef, _OptionalFulfillmentCodeHookSettingsTypeDef
):
    pass

_RequiredFulfillmentStartResponseSpecificationTypeDef = TypedDict(
    "_RequiredFulfillmentStartResponseSpecificationTypeDef",
    {
        "delayInSeconds": int,
        "messageGroups": List["MessageGroupTypeDef"],
    },
)
_OptionalFulfillmentStartResponseSpecificationTypeDef = TypedDict(
    "_OptionalFulfillmentStartResponseSpecificationTypeDef",
    {
        "allowInterrupt": bool,
    },
    total=False,
)

class FulfillmentStartResponseSpecificationTypeDef(
    _RequiredFulfillmentStartResponseSpecificationTypeDef,
    _OptionalFulfillmentStartResponseSpecificationTypeDef,
):
    pass

_RequiredFulfillmentUpdateResponseSpecificationTypeDef = TypedDict(
    "_RequiredFulfillmentUpdateResponseSpecificationTypeDef",
    {
        "frequencyInSeconds": int,
        "messageGroups": List["MessageGroupTypeDef"],
    },
)
_OptionalFulfillmentUpdateResponseSpecificationTypeDef = TypedDict(
    "_OptionalFulfillmentUpdateResponseSpecificationTypeDef",
    {
        "allowInterrupt": bool,
    },
    total=False,
)

class FulfillmentUpdateResponseSpecificationTypeDef(
    _RequiredFulfillmentUpdateResponseSpecificationTypeDef,
    _OptionalFulfillmentUpdateResponseSpecificationTypeDef,
):
    pass

_RequiredFulfillmentUpdatesSpecificationTypeDef = TypedDict(
    "_RequiredFulfillmentUpdatesSpecificationTypeDef",
    {
        "active": bool,
    },
)
_OptionalFulfillmentUpdatesSpecificationTypeDef = TypedDict(
    "_OptionalFulfillmentUpdatesSpecificationTypeDef",
    {
        "startResponse": "FulfillmentStartResponseSpecificationTypeDef",
        "updateResponse": "FulfillmentUpdateResponseSpecificationTypeDef",
        "timeoutInSeconds": int,
    },
    total=False,
)

class FulfillmentUpdatesSpecificationTypeDef(
    _RequiredFulfillmentUpdatesSpecificationTypeDef, _OptionalFulfillmentUpdatesSpecificationTypeDef
):
    pass

GetTestExecutionArtifactsUrlRequestRequestTypeDef = TypedDict(
    "GetTestExecutionArtifactsUrlRequestRequestTypeDef",
    {
        "testExecutionId": str,
    },
)

GetTestExecutionArtifactsUrlResponseTypeDef = TypedDict(
    "GetTestExecutionArtifactsUrlResponseTypeDef",
    {
        "testExecutionId": str,
        "downloadArtifactsUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GrammarSlotTypeSettingTypeDef = TypedDict(
    "GrammarSlotTypeSettingTypeDef",
    {
        "source": "GrammarSlotTypeSourceTypeDef",
    },
    total=False,
)

_RequiredGrammarSlotTypeSourceTypeDef = TypedDict(
    "_RequiredGrammarSlotTypeSourceTypeDef",
    {
        "s3BucketName": str,
        "s3ObjectKey": str,
    },
)
_OptionalGrammarSlotTypeSourceTypeDef = TypedDict(
    "_OptionalGrammarSlotTypeSourceTypeDef",
    {
        "kmsKeyArn": str,
    },
    total=False,
)

class GrammarSlotTypeSourceTypeDef(
    _RequiredGrammarSlotTypeSourceTypeDef, _OptionalGrammarSlotTypeSourceTypeDef
):
    pass

_RequiredImageResponseCardTypeDef = TypedDict(
    "_RequiredImageResponseCardTypeDef",
    {
        "title": str,
    },
)
_OptionalImageResponseCardTypeDef = TypedDict(
    "_OptionalImageResponseCardTypeDef",
    {
        "subtitle": str,
        "imageUrl": str,
        "buttons": List["ButtonTypeDef"],
    },
    total=False,
)

class ImageResponseCardTypeDef(
    _RequiredImageResponseCardTypeDef, _OptionalImageResponseCardTypeDef
):
    pass

ImportFilterTypeDef = TypedDict(
    "ImportFilterTypeDef",
    {
        "name": Literal["ImportResourceType"],
        "values": List[str],
        "operator": ImportFilterOperatorType,
    },
)

ImportResourceSpecificationTypeDef = TypedDict(
    "ImportResourceSpecificationTypeDef",
    {
        "botImportSpecification": "BotImportSpecificationTypeDef",
        "botLocaleImportSpecification": "BotLocaleImportSpecificationTypeDef",
        "customVocabularyImportSpecification": "CustomVocabularyImportSpecificationTypeDef",
        "testSetImportResourceSpecification": "TestSetImportResourceSpecificationTypeDef",
    },
    total=False,
)

ImportSortByTypeDef = TypedDict(
    "ImportSortByTypeDef",
    {
        "attribute": Literal["LastUpdatedDateTime"],
        "order": SortOrderType,
    },
)

ImportSummaryTypeDef = TypedDict(
    "ImportSummaryTypeDef",
    {
        "importId": str,
        "importedResourceId": str,
        "importedResourceName": str,
        "importStatus": ImportStatusType,
        "mergeStrategy": MergeStrategyType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "importedResourceType": ImportResourceTypeType,
    },
    total=False,
)

InitialResponseSettingTypeDef = TypedDict(
    "InitialResponseSettingTypeDef",
    {
        "initialResponse": "ResponseSpecificationTypeDef",
        "nextStep": "DialogStateTypeDef",
        "conditional": "ConditionalSpecificationTypeDef",
        "codeHook": "DialogCodeHookInvocationSettingTypeDef",
    },
    total=False,
)

InputContextTypeDef = TypedDict(
    "InputContextTypeDef",
    {
        "name": str,
    },
)

InputSessionStateSpecificationTypeDef = TypedDict(
    "InputSessionStateSpecificationTypeDef",
    {
        "sessionAttributes": Dict[str, str],
        "activeContexts": List["ActiveContextTypeDef"],
        "runtimeHints": "RuntimeHintsTypeDef",
    },
    total=False,
)

_RequiredIntentClassificationTestResultItemCountsTypeDef = TypedDict(
    "_RequiredIntentClassificationTestResultItemCountsTypeDef",
    {
        "totalResultCount": int,
        "intentMatchResultCounts": Dict[TestResultMatchStatusType, int],
    },
)
_OptionalIntentClassificationTestResultItemCountsTypeDef = TypedDict(
    "_OptionalIntentClassificationTestResultItemCountsTypeDef",
    {
        "speechTranscriptionResultCounts": Dict[TestResultMatchStatusType, int],
    },
    total=False,
)

class IntentClassificationTestResultItemCountsTypeDef(
    _RequiredIntentClassificationTestResultItemCountsTypeDef,
    _OptionalIntentClassificationTestResultItemCountsTypeDef,
):
    pass

IntentClassificationTestResultItemTypeDef = TypedDict(
    "IntentClassificationTestResultItemTypeDef",
    {
        "intentName": str,
        "multiTurnConversation": bool,
        "resultCounts": "IntentClassificationTestResultItemCountsTypeDef",
    },
)

IntentClassificationTestResultsTypeDef = TypedDict(
    "IntentClassificationTestResultsTypeDef",
    {
        "items": List["IntentClassificationTestResultItemTypeDef"],
    },
)

IntentClosingSettingTypeDef = TypedDict(
    "IntentClosingSettingTypeDef",
    {
        "closingResponse": "ResponseSpecificationTypeDef",
        "active": bool,
        "nextStep": "DialogStateTypeDef",
        "conditional": "ConditionalSpecificationTypeDef",
    },
    total=False,
)

_RequiredIntentConfirmationSettingTypeDef = TypedDict(
    "_RequiredIntentConfirmationSettingTypeDef",
    {
        "promptSpecification": "PromptSpecificationTypeDef",
    },
)
_OptionalIntentConfirmationSettingTypeDef = TypedDict(
    "_OptionalIntentConfirmationSettingTypeDef",
    {
        "declinationResponse": "ResponseSpecificationTypeDef",
        "active": bool,
        "confirmationResponse": "ResponseSpecificationTypeDef",
        "confirmationNextStep": "DialogStateTypeDef",
        "confirmationConditional": "ConditionalSpecificationTypeDef",
        "declinationNextStep": "DialogStateTypeDef",
        "declinationConditional": "ConditionalSpecificationTypeDef",
        "failureResponse": "ResponseSpecificationTypeDef",
        "failureNextStep": "DialogStateTypeDef",
        "failureConditional": "ConditionalSpecificationTypeDef",
        "codeHook": "DialogCodeHookInvocationSettingTypeDef",
        "elicitationCodeHook": "ElicitationCodeHookInvocationSettingTypeDef",
    },
    total=False,
)

class IntentConfirmationSettingTypeDef(
    _RequiredIntentConfirmationSettingTypeDef, _OptionalIntentConfirmationSettingTypeDef
):
    pass

IntentFilterTypeDef = TypedDict(
    "IntentFilterTypeDef",
    {
        "name": Literal["IntentName"],
        "values": List[str],
        "operator": IntentFilterOperatorType,
    },
)

IntentLevelSlotResolutionTestResultItemTypeDef = TypedDict(
    "IntentLevelSlotResolutionTestResultItemTypeDef",
    {
        "intentName": str,
        "multiTurnConversation": bool,
        "slotResolutionResults": List["SlotResolutionTestResultItemTypeDef"],
    },
)

IntentLevelSlotResolutionTestResultsTypeDef = TypedDict(
    "IntentLevelSlotResolutionTestResultsTypeDef",
    {
        "items": List["IntentLevelSlotResolutionTestResultItemTypeDef"],
    },
)

IntentOverrideTypeDef = TypedDict(
    "IntentOverrideTypeDef",
    {
        "name": str,
        "slots": Dict[str, "SlotValueOverrideTypeDef"],
    },
    total=False,
)

IntentSortByTypeDef = TypedDict(
    "IntentSortByTypeDef",
    {
        "attribute": IntentSortAttributeType,
        "order": SortOrderType,
    },
)

IntentStatisticsTypeDef = TypedDict(
    "IntentStatisticsTypeDef",
    {
        "discoveredIntentCount": int,
    },
    total=False,
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

InvokedIntentSampleTypeDef = TypedDict(
    "InvokedIntentSampleTypeDef",
    {
        "intentName": str,
    },
    total=False,
)

_RequiredKendraConfigurationTypeDef = TypedDict(
    "_RequiredKendraConfigurationTypeDef",
    {
        "kendraIndex": str,
    },
)
_OptionalKendraConfigurationTypeDef = TypedDict(
    "_OptionalKendraConfigurationTypeDef",
    {
        "queryFilterStringEnabled": bool,
        "queryFilterString": str,
    },
    total=False,
)

class KendraConfigurationTypeDef(
    _RequiredKendraConfigurationTypeDef, _OptionalKendraConfigurationTypeDef
):
    pass

LambdaCodeHookTypeDef = TypedDict(
    "LambdaCodeHookTypeDef",
    {
        "lambdaARN": str,
        "codeHookInterfaceVersion": str,
    },
)

LexTranscriptFilterTypeDef = TypedDict(
    "LexTranscriptFilterTypeDef",
    {
        "dateRangeFilter": "DateRangeFilterTypeDef",
    },
    total=False,
)

_RequiredListAggregatedUtterancesRequestRequestTypeDef = TypedDict(
    "_RequiredListAggregatedUtterancesRequestRequestTypeDef",
    {
        "botId": str,
        "localeId": str,
        "aggregationDuration": "UtteranceAggregationDurationTypeDef",
    },
)
_OptionalListAggregatedUtterancesRequestRequestTypeDef = TypedDict(
    "_OptionalListAggregatedUtterancesRequestRequestTypeDef",
    {
        "botAliasId": str,
        "botVersion": str,
        "sortBy": "AggregatedUtterancesSortByTypeDef",
        "filters": List["AggregatedUtterancesFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAggregatedUtterancesRequestRequestTypeDef(
    _RequiredListAggregatedUtterancesRequestRequestTypeDef,
    _OptionalListAggregatedUtterancesRequestRequestTypeDef,
):
    pass

ListAggregatedUtterancesResponseTypeDef = TypedDict(
    "ListAggregatedUtterancesResponseTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "botVersion": str,
        "localeId": str,
        "aggregationDuration": "UtteranceAggregationDurationTypeDef",
        "aggregationWindowStartTime": datetime,
        "aggregationWindowEndTime": datetime,
        "aggregationLastRefreshedDateTime": datetime,
        "aggregatedUtterancesSummaries": List["AggregatedUtterancesSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBotAliasesRequestRequestTypeDef = TypedDict(
    "_RequiredListBotAliasesRequestRequestTypeDef",
    {
        "botId": str,
    },
)
_OptionalListBotAliasesRequestRequestTypeDef = TypedDict(
    "_OptionalListBotAliasesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListBotAliasesRequestRequestTypeDef(
    _RequiredListBotAliasesRequestRequestTypeDef, _OptionalListBotAliasesRequestRequestTypeDef
):
    pass

ListBotAliasesResponseTypeDef = TypedDict(
    "ListBotAliasesResponseTypeDef",
    {
        "botAliasSummaries": List["BotAliasSummaryTypeDef"],
        "nextToken": str,
        "botId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBotLocalesRequestRequestTypeDef = TypedDict(
    "_RequiredListBotLocalesRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
    },
)
_OptionalListBotLocalesRequestRequestTypeDef = TypedDict(
    "_OptionalListBotLocalesRequestRequestTypeDef",
    {
        "sortBy": "BotLocaleSortByTypeDef",
        "filters": List["BotLocaleFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListBotLocalesRequestRequestTypeDef(
    _RequiredListBotLocalesRequestRequestTypeDef, _OptionalListBotLocalesRequestRequestTypeDef
):
    pass

ListBotLocalesResponseTypeDef = TypedDict(
    "ListBotLocalesResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "nextToken": str,
        "botLocaleSummaries": List["BotLocaleSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBotRecommendationsRequestRequestTypeDef = TypedDict(
    "_RequiredListBotRecommendationsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalListBotRecommendationsRequestRequestTypeDef = TypedDict(
    "_OptionalListBotRecommendationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListBotRecommendationsRequestRequestTypeDef(
    _RequiredListBotRecommendationsRequestRequestTypeDef,
    _OptionalListBotRecommendationsRequestRequestTypeDef,
):
    pass

ListBotRecommendationsResponseTypeDef = TypedDict(
    "ListBotRecommendationsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationSummaries": List["BotRecommendationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBotVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListBotVersionsRequestRequestTypeDef",
    {
        "botId": str,
    },
)
_OptionalListBotVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListBotVersionsRequestRequestTypeDef",
    {
        "sortBy": "BotVersionSortByTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListBotVersionsRequestRequestTypeDef(
    _RequiredListBotVersionsRequestRequestTypeDef, _OptionalListBotVersionsRequestRequestTypeDef
):
    pass

ListBotVersionsResponseTypeDef = TypedDict(
    "ListBotVersionsResponseTypeDef",
    {
        "botId": str,
        "botVersionSummaries": List["BotVersionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBotsRequestRequestTypeDef = TypedDict(
    "ListBotsRequestRequestTypeDef",
    {
        "sortBy": "BotSortByTypeDef",
        "filters": List["BotFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListBotsResponseTypeDef = TypedDict(
    "ListBotsResponseTypeDef",
    {
        "botSummaries": List["BotSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBuiltInIntentsRequestRequestTypeDef = TypedDict(
    "_RequiredListBuiltInIntentsRequestRequestTypeDef",
    {
        "localeId": str,
    },
)
_OptionalListBuiltInIntentsRequestRequestTypeDef = TypedDict(
    "_OptionalListBuiltInIntentsRequestRequestTypeDef",
    {
        "sortBy": "BuiltInIntentSortByTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListBuiltInIntentsRequestRequestTypeDef(
    _RequiredListBuiltInIntentsRequestRequestTypeDef,
    _OptionalListBuiltInIntentsRequestRequestTypeDef,
):
    pass

ListBuiltInIntentsResponseTypeDef = TypedDict(
    "ListBuiltInIntentsResponseTypeDef",
    {
        "builtInIntentSummaries": List["BuiltInIntentSummaryTypeDef"],
        "nextToken": str,
        "localeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBuiltInSlotTypesRequestRequestTypeDef = TypedDict(
    "_RequiredListBuiltInSlotTypesRequestRequestTypeDef",
    {
        "localeId": str,
    },
)
_OptionalListBuiltInSlotTypesRequestRequestTypeDef = TypedDict(
    "_OptionalListBuiltInSlotTypesRequestRequestTypeDef",
    {
        "sortBy": "BuiltInSlotTypeSortByTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListBuiltInSlotTypesRequestRequestTypeDef(
    _RequiredListBuiltInSlotTypesRequestRequestTypeDef,
    _OptionalListBuiltInSlotTypesRequestRequestTypeDef,
):
    pass

ListBuiltInSlotTypesResponseTypeDef = TypedDict(
    "ListBuiltInSlotTypesResponseTypeDef",
    {
        "builtInSlotTypeSummaries": List["BuiltInSlotTypeSummaryTypeDef"],
        "nextToken": str,
        "localeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCustomVocabularyItemsRequestRequestTypeDef = TypedDict(
    "_RequiredListCustomVocabularyItemsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalListCustomVocabularyItemsRequestRequestTypeDef = TypedDict(
    "_OptionalListCustomVocabularyItemsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListCustomVocabularyItemsRequestRequestTypeDef(
    _RequiredListCustomVocabularyItemsRequestRequestTypeDef,
    _OptionalListCustomVocabularyItemsRequestRequestTypeDef,
):
    pass

ListCustomVocabularyItemsResponseTypeDef = TypedDict(
    "ListCustomVocabularyItemsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "customVocabularyItems": List["CustomVocabularyItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExportsRequestRequestTypeDef = TypedDict(
    "ListExportsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "sortBy": "ExportSortByTypeDef",
        "filters": List["ExportFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
        "localeId": str,
    },
    total=False,
)

ListExportsResponseTypeDef = TypedDict(
    "ListExportsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "exportSummaries": List["ExportSummaryTypeDef"],
        "nextToken": str,
        "localeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImportsRequestRequestTypeDef = TypedDict(
    "ListImportsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "sortBy": "ImportSortByTypeDef",
        "filters": List["ImportFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
        "localeId": str,
    },
    total=False,
)

ListImportsResponseTypeDef = TypedDict(
    "ListImportsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "importSummaries": List["ImportSummaryTypeDef"],
        "nextToken": str,
        "localeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIntentMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredListIntentMetricsRequestRequestTypeDef",
    {
        "botId": str,
        "startDateTime": Union[datetime, str],
        "endDateTime": Union[datetime, str],
        "metrics": List["AnalyticsIntentMetricTypeDef"],
    },
)
_OptionalListIntentMetricsRequestRequestTypeDef = TypedDict(
    "_OptionalListIntentMetricsRequestRequestTypeDef",
    {
        "binBy": List["AnalyticsBinBySpecificationTypeDef"],
        "groupBy": List["AnalyticsIntentGroupBySpecificationTypeDef"],
        "filters": List["AnalyticsIntentFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListIntentMetricsRequestRequestTypeDef(
    _RequiredListIntentMetricsRequestRequestTypeDef, _OptionalListIntentMetricsRequestRequestTypeDef
):
    pass

ListIntentMetricsResponseTypeDef = TypedDict(
    "ListIntentMetricsResponseTypeDef",
    {
        "botId": str,
        "results": List["AnalyticsIntentResultTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIntentPathsRequestRequestTypeDef = TypedDict(
    "_RequiredListIntentPathsRequestRequestTypeDef",
    {
        "botId": str,
        "startDateTime": Union[datetime, str],
        "endDateTime": Union[datetime, str],
        "intentPath": str,
    },
)
_OptionalListIntentPathsRequestRequestTypeDef = TypedDict(
    "_OptionalListIntentPathsRequestRequestTypeDef",
    {
        "filters": List["AnalyticsPathFilterTypeDef"],
    },
    total=False,
)

class ListIntentPathsRequestRequestTypeDef(
    _RequiredListIntentPathsRequestRequestTypeDef, _OptionalListIntentPathsRequestRequestTypeDef
):
    pass

ListIntentPathsResponseTypeDef = TypedDict(
    "ListIntentPathsResponseTypeDef",
    {
        "nodeSummaries": List["AnalyticsIntentNodeSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIntentStageMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredListIntentStageMetricsRequestRequestTypeDef",
    {
        "botId": str,
        "startDateTime": Union[datetime, str],
        "endDateTime": Union[datetime, str],
        "metrics": List["AnalyticsIntentStageMetricTypeDef"],
    },
)
_OptionalListIntentStageMetricsRequestRequestTypeDef = TypedDict(
    "_OptionalListIntentStageMetricsRequestRequestTypeDef",
    {
        "binBy": List["AnalyticsBinBySpecificationTypeDef"],
        "groupBy": List["AnalyticsIntentStageGroupBySpecificationTypeDef"],
        "filters": List["AnalyticsIntentStageFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListIntentStageMetricsRequestRequestTypeDef(
    _RequiredListIntentStageMetricsRequestRequestTypeDef,
    _OptionalListIntentStageMetricsRequestRequestTypeDef,
):
    pass

ListIntentStageMetricsResponseTypeDef = TypedDict(
    "ListIntentStageMetricsResponseTypeDef",
    {
        "botId": str,
        "results": List["AnalyticsIntentStageResultTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIntentsRequestRequestTypeDef = TypedDict(
    "_RequiredListIntentsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalListIntentsRequestRequestTypeDef = TypedDict(
    "_OptionalListIntentsRequestRequestTypeDef",
    {
        "sortBy": "IntentSortByTypeDef",
        "filters": List["IntentFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListIntentsRequestRequestTypeDef(
    _RequiredListIntentsRequestRequestTypeDef, _OptionalListIntentsRequestRequestTypeDef
):
    pass

ListIntentsResponseTypeDef = TypedDict(
    "ListIntentsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentSummaries": List["IntentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRecommendedIntentsRequestRequestTypeDef = TypedDict(
    "_RequiredListRecommendedIntentsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationId": str,
    },
)
_OptionalListRecommendedIntentsRequestRequestTypeDef = TypedDict(
    "_OptionalListRecommendedIntentsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListRecommendedIntentsRequestRequestTypeDef(
    _RequiredListRecommendedIntentsRequestRequestTypeDef,
    _OptionalListRecommendedIntentsRequestRequestTypeDef,
):
    pass

ListRecommendedIntentsResponseTypeDef = TypedDict(
    "ListRecommendedIntentsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationId": str,
        "summaryList": List["RecommendedIntentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSessionAnalyticsDataRequestRequestTypeDef = TypedDict(
    "_RequiredListSessionAnalyticsDataRequestRequestTypeDef",
    {
        "botId": str,
        "startDateTime": Union[datetime, str],
        "endDateTime": Union[datetime, str],
    },
)
_OptionalListSessionAnalyticsDataRequestRequestTypeDef = TypedDict(
    "_OptionalListSessionAnalyticsDataRequestRequestTypeDef",
    {
        "sortBy": "SessionDataSortByTypeDef",
        "filters": List["AnalyticsSessionFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListSessionAnalyticsDataRequestRequestTypeDef(
    _RequiredListSessionAnalyticsDataRequestRequestTypeDef,
    _OptionalListSessionAnalyticsDataRequestRequestTypeDef,
):
    pass

ListSessionAnalyticsDataResponseTypeDef = TypedDict(
    "ListSessionAnalyticsDataResponseTypeDef",
    {
        "botId": str,
        "nextToken": str,
        "sessions": List["SessionSpecificationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSessionMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredListSessionMetricsRequestRequestTypeDef",
    {
        "botId": str,
        "startDateTime": Union[datetime, str],
        "endDateTime": Union[datetime, str],
        "metrics": List["AnalyticsSessionMetricTypeDef"],
    },
)
_OptionalListSessionMetricsRequestRequestTypeDef = TypedDict(
    "_OptionalListSessionMetricsRequestRequestTypeDef",
    {
        "binBy": List["AnalyticsBinBySpecificationTypeDef"],
        "groupBy": List["AnalyticsSessionGroupBySpecificationTypeDef"],
        "filters": List["AnalyticsSessionFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListSessionMetricsRequestRequestTypeDef(
    _RequiredListSessionMetricsRequestRequestTypeDef,
    _OptionalListSessionMetricsRequestRequestTypeDef,
):
    pass

ListSessionMetricsResponseTypeDef = TypedDict(
    "ListSessionMetricsResponseTypeDef",
    {
        "botId": str,
        "results": List["AnalyticsSessionResultTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSlotTypesRequestRequestTypeDef = TypedDict(
    "_RequiredListSlotTypesRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalListSlotTypesRequestRequestTypeDef = TypedDict(
    "_OptionalListSlotTypesRequestRequestTypeDef",
    {
        "sortBy": "SlotTypeSortByTypeDef",
        "filters": List["SlotTypeFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListSlotTypesRequestRequestTypeDef(
    _RequiredListSlotTypesRequestRequestTypeDef, _OptionalListSlotTypesRequestRequestTypeDef
):
    pass

ListSlotTypesResponseTypeDef = TypedDict(
    "ListSlotTypesResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "slotTypeSummaries": List["SlotTypeSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSlotsRequestRequestTypeDef = TypedDict(
    "_RequiredListSlotsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
    },
)
_OptionalListSlotsRequestRequestTypeDef = TypedDict(
    "_OptionalListSlotsRequestRequestTypeDef",
    {
        "sortBy": "SlotSortByTypeDef",
        "filters": List["SlotFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListSlotsRequestRequestTypeDef(
    _RequiredListSlotsRequestRequestTypeDef, _OptionalListSlotsRequestRequestTypeDef
):
    pass

ListSlotsResponseTypeDef = TypedDict(
    "ListSlotsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "slotSummaries": List["SlotSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTestExecutionResultItemsRequestRequestTypeDef = TypedDict(
    "_RequiredListTestExecutionResultItemsRequestRequestTypeDef",
    {
        "testExecutionId": str,
        "resultFilterBy": "TestExecutionResultFilterByTypeDef",
    },
)
_OptionalListTestExecutionResultItemsRequestRequestTypeDef = TypedDict(
    "_OptionalListTestExecutionResultItemsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListTestExecutionResultItemsRequestRequestTypeDef(
    _RequiredListTestExecutionResultItemsRequestRequestTypeDef,
    _OptionalListTestExecutionResultItemsRequestRequestTypeDef,
):
    pass

ListTestExecutionResultItemsResponseTypeDef = TypedDict(
    "ListTestExecutionResultItemsResponseTypeDef",
    {
        "testExecutionResults": "TestExecutionResultItemsTypeDef",
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTestExecutionsRequestRequestTypeDef = TypedDict(
    "ListTestExecutionsRequestRequestTypeDef",
    {
        "sortBy": "TestExecutionSortByTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListTestExecutionsResponseTypeDef = TypedDict(
    "ListTestExecutionsResponseTypeDef",
    {
        "testExecutions": List["TestExecutionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTestSetRecordsRequestRequestTypeDef = TypedDict(
    "_RequiredListTestSetRecordsRequestRequestTypeDef",
    {
        "testSetId": str,
    },
)
_OptionalListTestSetRecordsRequestRequestTypeDef = TypedDict(
    "_OptionalListTestSetRecordsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListTestSetRecordsRequestRequestTypeDef(
    _RequiredListTestSetRecordsRequestRequestTypeDef,
    _OptionalListTestSetRecordsRequestRequestTypeDef,
):
    pass

ListTestSetRecordsResponseTypeDef = TypedDict(
    "ListTestSetRecordsResponseTypeDef",
    {
        "testSetRecords": List["TestSetTurnRecordTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTestSetsRequestRequestTypeDef = TypedDict(
    "ListTestSetsRequestRequestTypeDef",
    {
        "sortBy": "TestSetSortByTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListTestSetsResponseTypeDef = TypedDict(
    "ListTestSetsResponseTypeDef",
    {
        "testSets": List["TestSetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUtteranceAnalyticsDataRequestRequestTypeDef = TypedDict(
    "_RequiredListUtteranceAnalyticsDataRequestRequestTypeDef",
    {
        "botId": str,
        "startDateTime": Union[datetime, str],
        "endDateTime": Union[datetime, str],
    },
)
_OptionalListUtteranceAnalyticsDataRequestRequestTypeDef = TypedDict(
    "_OptionalListUtteranceAnalyticsDataRequestRequestTypeDef",
    {
        "sortBy": "UtteranceDataSortByTypeDef",
        "filters": List["AnalyticsUtteranceFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListUtteranceAnalyticsDataRequestRequestTypeDef(
    _RequiredListUtteranceAnalyticsDataRequestRequestTypeDef,
    _OptionalListUtteranceAnalyticsDataRequestRequestTypeDef,
):
    pass

ListUtteranceAnalyticsDataResponseTypeDef = TypedDict(
    "ListUtteranceAnalyticsDataResponseTypeDef",
    {
        "botId": str,
        "nextToken": str,
        "utterances": List["UtteranceSpecificationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUtteranceMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredListUtteranceMetricsRequestRequestTypeDef",
    {
        "botId": str,
        "startDateTime": Union[datetime, str],
        "endDateTime": Union[datetime, str],
        "metrics": List["AnalyticsUtteranceMetricTypeDef"],
    },
)
_OptionalListUtteranceMetricsRequestRequestTypeDef = TypedDict(
    "_OptionalListUtteranceMetricsRequestRequestTypeDef",
    {
        "binBy": List["AnalyticsBinBySpecificationTypeDef"],
        "groupBy": List["AnalyticsUtteranceGroupBySpecificationTypeDef"],
        "attributes": List["AnalyticsUtteranceAttributeTypeDef"],
        "filters": List["AnalyticsUtteranceFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListUtteranceMetricsRequestRequestTypeDef(
    _RequiredListUtteranceMetricsRequestRequestTypeDef,
    _OptionalListUtteranceMetricsRequestRequestTypeDef,
):
    pass

ListUtteranceMetricsResponseTypeDef = TypedDict(
    "ListUtteranceMetricsResponseTypeDef",
    {
        "botId": str,
        "results": List["AnalyticsUtteranceResultTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMessageGroupTypeDef = TypedDict(
    "_RequiredMessageGroupTypeDef",
    {
        "message": "MessageTypeDef",
    },
)
_OptionalMessageGroupTypeDef = TypedDict(
    "_OptionalMessageGroupTypeDef",
    {
        "variations": List["MessageTypeDef"],
    },
    total=False,
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

MultipleValuesSettingTypeDef = TypedDict(
    "MultipleValuesSettingTypeDef",
    {
        "allowMultipleValues": bool,
    },
    total=False,
)

_RequiredNewCustomVocabularyItemTypeDef = TypedDict(
    "_RequiredNewCustomVocabularyItemTypeDef",
    {
        "phrase": str,
    },
)
_OptionalNewCustomVocabularyItemTypeDef = TypedDict(
    "_OptionalNewCustomVocabularyItemTypeDef",
    {
        "weight": int,
        "displayAs": str,
    },
    total=False,
)

class NewCustomVocabularyItemTypeDef(
    _RequiredNewCustomVocabularyItemTypeDef, _OptionalNewCustomVocabularyItemTypeDef
):
    pass

ObfuscationSettingTypeDef = TypedDict(
    "ObfuscationSettingTypeDef",
    {
        "obfuscationSettingType": ObfuscationSettingTypeType,
    },
)

OutputContextTypeDef = TypedDict(
    "OutputContextTypeDef",
    {
        "name": str,
        "timeToLiveInSeconds": int,
        "turnsToLive": int,
    },
)

_RequiredOverallTestResultItemTypeDef = TypedDict(
    "_RequiredOverallTestResultItemTypeDef",
    {
        "multiTurnConversation": bool,
        "totalResultCount": int,
        "endToEndResultCounts": Dict[TestResultMatchStatusType, int],
    },
)
_OptionalOverallTestResultItemTypeDef = TypedDict(
    "_OptionalOverallTestResultItemTypeDef",
    {
        "speechTranscriptionResultCounts": Dict[TestResultMatchStatusType, int],
    },
    total=False,
)

class OverallTestResultItemTypeDef(
    _RequiredOverallTestResultItemTypeDef, _OptionalOverallTestResultItemTypeDef
):
    pass

OverallTestResultsTypeDef = TypedDict(
    "OverallTestResultsTypeDef",
    {
        "items": List["OverallTestResultItemTypeDef"],
    },
)

ParentBotNetworkTypeDef = TypedDict(
    "ParentBotNetworkTypeDef",
    {
        "botId": str,
        "botVersion": str,
    },
)

PathFormatTypeDef = TypedDict(
    "PathFormatTypeDef",
    {
        "objectPrefixes": List[str],
    },
    total=False,
)

PlainTextMessageTypeDef = TypedDict(
    "PlainTextMessageTypeDef",
    {
        "value": str,
    },
)

PostDialogCodeHookInvocationSpecificationTypeDef = TypedDict(
    "PostDialogCodeHookInvocationSpecificationTypeDef",
    {
        "successResponse": "ResponseSpecificationTypeDef",
        "successNextStep": "DialogStateTypeDef",
        "successConditional": "ConditionalSpecificationTypeDef",
        "failureResponse": "ResponseSpecificationTypeDef",
        "failureNextStep": "DialogStateTypeDef",
        "failureConditional": "ConditionalSpecificationTypeDef",
        "timeoutResponse": "ResponseSpecificationTypeDef",
        "timeoutNextStep": "DialogStateTypeDef",
        "timeoutConditional": "ConditionalSpecificationTypeDef",
    },
    total=False,
)

PostFulfillmentStatusSpecificationTypeDef = TypedDict(
    "PostFulfillmentStatusSpecificationTypeDef",
    {
        "successResponse": "ResponseSpecificationTypeDef",
        "failureResponse": "ResponseSpecificationTypeDef",
        "timeoutResponse": "ResponseSpecificationTypeDef",
        "successNextStep": "DialogStateTypeDef",
        "successConditional": "ConditionalSpecificationTypeDef",
        "failureNextStep": "DialogStateTypeDef",
        "failureConditional": "ConditionalSpecificationTypeDef",
        "timeoutNextStep": "DialogStateTypeDef",
        "timeoutConditional": "ConditionalSpecificationTypeDef",
    },
    total=False,
)

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "service": str,
        "arn": str,
    },
    total=False,
)

_RequiredPromptAttemptSpecificationTypeDef = TypedDict(
    "_RequiredPromptAttemptSpecificationTypeDef",
    {
        "allowedInputTypes": "AllowedInputTypesTypeDef",
    },
)
_OptionalPromptAttemptSpecificationTypeDef = TypedDict(
    "_OptionalPromptAttemptSpecificationTypeDef",
    {
        "allowInterrupt": bool,
        "audioAndDTMFInputSpecification": "AudioAndDTMFInputSpecificationTypeDef",
        "textInputSpecification": "TextInputSpecificationTypeDef",
    },
    total=False,
)

class PromptAttemptSpecificationTypeDef(
    _RequiredPromptAttemptSpecificationTypeDef, _OptionalPromptAttemptSpecificationTypeDef
):
    pass

_RequiredPromptSpecificationTypeDef = TypedDict(
    "_RequiredPromptSpecificationTypeDef",
    {
        "messageGroups": List["MessageGroupTypeDef"],
        "maxRetries": int,
    },
)
_OptionalPromptSpecificationTypeDef = TypedDict(
    "_OptionalPromptSpecificationTypeDef",
    {
        "allowInterrupt": bool,
        "messageSelectionStrategy": MessageSelectionStrategyType,
        "promptAttemptsSpecification": Dict[PromptAttemptType, "PromptAttemptSpecificationTypeDef"],
    },
    total=False,
)

class PromptSpecificationTypeDef(
    _RequiredPromptSpecificationTypeDef, _OptionalPromptSpecificationTypeDef
):
    pass

RecommendedIntentSummaryTypeDef = TypedDict(
    "RecommendedIntentSummaryTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "sampleUtterancesCount": int,
    },
    total=False,
)

RelativeAggregationDurationTypeDef = TypedDict(
    "RelativeAggregationDurationTypeDef",
    {
        "timeDimension": TimeDimensionType,
        "timeValue": int,
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

_RequiredResponseSpecificationTypeDef = TypedDict(
    "_RequiredResponseSpecificationTypeDef",
    {
        "messageGroups": List["MessageGroupTypeDef"],
    },
)
_OptionalResponseSpecificationTypeDef = TypedDict(
    "_OptionalResponseSpecificationTypeDef",
    {
        "allowInterrupt": bool,
    },
    total=False,
)

class ResponseSpecificationTypeDef(
    _RequiredResponseSpecificationTypeDef, _OptionalResponseSpecificationTypeDef
):
    pass

RuntimeHintDetailsTypeDef = TypedDict(
    "RuntimeHintDetailsTypeDef",
    {
        "runtimeHintValues": List["RuntimeHintValueTypeDef"],
        "subSlotHints": Dict[str, Dict[str, Any]],
    },
    total=False,
)

RuntimeHintValueTypeDef = TypedDict(
    "RuntimeHintValueTypeDef",
    {
        "phrase": str,
    },
)

RuntimeHintsTypeDef = TypedDict(
    "RuntimeHintsTypeDef",
    {
        "slotHints": Dict[str, Dict[str, "RuntimeHintDetailsTypeDef"]],
    },
    total=False,
)

_RequiredS3BucketLogDestinationTypeDef = TypedDict(
    "_RequiredS3BucketLogDestinationTypeDef",
    {
        "s3BucketArn": str,
        "logPrefix": str,
    },
)
_OptionalS3BucketLogDestinationTypeDef = TypedDict(
    "_OptionalS3BucketLogDestinationTypeDef",
    {
        "kmsKeyArn": str,
    },
    total=False,
)

class S3BucketLogDestinationTypeDef(
    _RequiredS3BucketLogDestinationTypeDef, _OptionalS3BucketLogDestinationTypeDef
):
    pass

_RequiredS3BucketTranscriptSourceTypeDef = TypedDict(
    "_RequiredS3BucketTranscriptSourceTypeDef",
    {
        "s3BucketName": str,
        "transcriptFormat": Literal["Lex"],
    },
)
_OptionalS3BucketTranscriptSourceTypeDef = TypedDict(
    "_OptionalS3BucketTranscriptSourceTypeDef",
    {
        "pathFormat": "PathFormatTypeDef",
        "transcriptFilter": "TranscriptFilterTypeDef",
        "kmsKeyArn": str,
    },
    total=False,
)

class S3BucketTranscriptSourceTypeDef(
    _RequiredS3BucketTranscriptSourceTypeDef, _OptionalS3BucketTranscriptSourceTypeDef
):
    pass

SSMLMessageTypeDef = TypedDict(
    "SSMLMessageTypeDef",
    {
        "value": str,
    },
)

SampleUtteranceTypeDef = TypedDict(
    "SampleUtteranceTypeDef",
    {
        "utterance": str,
    },
)

SampleValueTypeDef = TypedDict(
    "SampleValueTypeDef",
    {
        "value": str,
    },
)

_RequiredSearchAssociatedTranscriptsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchAssociatedTranscriptsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationId": str,
        "filters": List["AssociatedTranscriptFilterTypeDef"],
    },
)
_OptionalSearchAssociatedTranscriptsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchAssociatedTranscriptsRequestRequestTypeDef",
    {
        "searchOrder": SearchOrderType,
        "maxResults": int,
        "nextIndex": int,
    },
    total=False,
)

class SearchAssociatedTranscriptsRequestRequestTypeDef(
    _RequiredSearchAssociatedTranscriptsRequestRequestTypeDef,
    _OptionalSearchAssociatedTranscriptsRequestRequestTypeDef,
):
    pass

SearchAssociatedTranscriptsResponseTypeDef = TypedDict(
    "SearchAssociatedTranscriptsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationId": str,
        "nextIndex": int,
        "associatedTranscripts": List["AssociatedTranscriptTypeDef"],
        "totalResults": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SentimentAnalysisSettingsTypeDef = TypedDict(
    "SentimentAnalysisSettingsTypeDef",
    {
        "detectSentiment": bool,
    },
)

SessionDataSortByTypeDef = TypedDict(
    "SessionDataSortByTypeDef",
    {
        "name": AnalyticsSessionSortByNameType,
        "order": AnalyticsSortOrderType,
    },
)

SessionSpecificationTypeDef = TypedDict(
    "SessionSpecificationTypeDef",
    {
        "botAliasId": str,
        "botVersion": str,
        "localeId": str,
        "channel": str,
        "sessionId": str,
        "conversationStartTime": datetime,
        "conversationEndTime": datetime,
        "conversationDurationSeconds": int,
        "conversationEndState": ConversationEndStateType,
        "mode": AnalyticsModalityType,
        "numberOfTurns": int,
        "invokedIntentSamples": List["InvokedIntentSampleTypeDef"],
        "originatingRequestId": str,
    },
    total=False,
)

SlotCaptureSettingTypeDef = TypedDict(
    "SlotCaptureSettingTypeDef",
    {
        "captureResponse": "ResponseSpecificationTypeDef",
        "captureNextStep": "DialogStateTypeDef",
        "captureConditional": "ConditionalSpecificationTypeDef",
        "failureResponse": "ResponseSpecificationTypeDef",
        "failureNextStep": "DialogStateTypeDef",
        "failureConditional": "ConditionalSpecificationTypeDef",
        "codeHook": "DialogCodeHookInvocationSettingTypeDef",
        "elicitationCodeHook": "ElicitationCodeHookInvocationSettingTypeDef",
    },
    total=False,
)

SlotDefaultValueSpecificationTypeDef = TypedDict(
    "SlotDefaultValueSpecificationTypeDef",
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

SlotFilterTypeDef = TypedDict(
    "SlotFilterTypeDef",
    {
        "name": Literal["SlotName"],
        "values": List[str],
        "operator": SlotFilterOperatorType,
    },
)

SlotPriorityTypeDef = TypedDict(
    "SlotPriorityTypeDef",
    {
        "priority": int,
        "slotId": str,
    },
)

_RequiredSlotResolutionTestResultItemCountsTypeDef = TypedDict(
    "_RequiredSlotResolutionTestResultItemCountsTypeDef",
    {
        "totalResultCount": int,
        "slotMatchResultCounts": Dict[TestResultMatchStatusType, int],
    },
)
_OptionalSlotResolutionTestResultItemCountsTypeDef = TypedDict(
    "_OptionalSlotResolutionTestResultItemCountsTypeDef",
    {
        "speechTranscriptionResultCounts": Dict[TestResultMatchStatusType, int],
    },
    total=False,
)

class SlotResolutionTestResultItemCountsTypeDef(
    _RequiredSlotResolutionTestResultItemCountsTypeDef,
    _OptionalSlotResolutionTestResultItemCountsTypeDef,
):
    pass

SlotResolutionTestResultItemTypeDef = TypedDict(
    "SlotResolutionTestResultItemTypeDef",
    {
        "slotName": str,
        "resultCounts": "SlotResolutionTestResultItemCountsTypeDef",
    },
)

SlotSortByTypeDef = TypedDict(
    "SlotSortByTypeDef",
    {
        "attribute": SlotSortAttributeType,
        "order": SortOrderType,
    },
)

SlotSummaryTypeDef = TypedDict(
    "SlotSummaryTypeDef",
    {
        "slotId": str,
        "slotName": str,
        "description": str,
        "slotConstraint": SlotConstraintType,
        "slotTypeId": str,
        "valueElicitationPromptSpecification": "PromptSpecificationTypeDef",
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

SlotTypeFilterTypeDef = TypedDict(
    "SlotTypeFilterTypeDef",
    {
        "name": SlotTypeFilterNameType,
        "values": List[str],
        "operator": SlotTypeFilterOperatorType,
    },
)

SlotTypeSortByTypeDef = TypedDict(
    "SlotTypeSortByTypeDef",
    {
        "attribute": SlotTypeSortAttributeType,
        "order": SortOrderType,
    },
)

SlotTypeStatisticsTypeDef = TypedDict(
    "SlotTypeStatisticsTypeDef",
    {
        "discoveredSlotTypeCount": int,
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
        "slotTypeCategory": SlotTypeCategoryType,
    },
    total=False,
)

SlotTypeValueTypeDef = TypedDict(
    "SlotTypeValueTypeDef",
    {
        "sampleValue": "SampleValueTypeDef",
        "synonyms": List["SampleValueTypeDef"],
    },
    total=False,
)

_RequiredSlotValueElicitationSettingTypeDef = TypedDict(
    "_RequiredSlotValueElicitationSettingTypeDef",
    {
        "slotConstraint": SlotConstraintType,
    },
)
_OptionalSlotValueElicitationSettingTypeDef = TypedDict(
    "_OptionalSlotValueElicitationSettingTypeDef",
    {
        "defaultValueSpecification": "SlotDefaultValueSpecificationTypeDef",
        "promptSpecification": "PromptSpecificationTypeDef",
        "sampleUtterances": List["SampleUtteranceTypeDef"],
        "waitAndContinueSpecification": "WaitAndContinueSpecificationTypeDef",
        "slotCaptureSetting": "SlotCaptureSettingTypeDef",
    },
    total=False,
)

class SlotValueElicitationSettingTypeDef(
    _RequiredSlotValueElicitationSettingTypeDef, _OptionalSlotValueElicitationSettingTypeDef
):
    pass

SlotValueOverrideTypeDef = TypedDict(
    "SlotValueOverrideTypeDef",
    {
        "shape": SlotShapeType,
        "value": "SlotValueTypeDef",
        "values": List[Dict[str, Any]],
    },
    total=False,
)

SlotValueRegexFilterTypeDef = TypedDict(
    "SlotValueRegexFilterTypeDef",
    {
        "pattern": str,
    },
)

_RequiredSlotValueSelectionSettingTypeDef = TypedDict(
    "_RequiredSlotValueSelectionSettingTypeDef",
    {
        "resolutionStrategy": SlotValueResolutionStrategyType,
    },
)
_OptionalSlotValueSelectionSettingTypeDef = TypedDict(
    "_OptionalSlotValueSelectionSettingTypeDef",
    {
        "regexFilter": "SlotValueRegexFilterTypeDef",
        "advancedRecognitionSetting": "AdvancedRecognitionSettingTypeDef",
    },
    total=False,
)

class SlotValueSelectionSettingTypeDef(
    _RequiredSlotValueSelectionSettingTypeDef, _OptionalSlotValueSelectionSettingTypeDef
):
    pass

SlotValueTypeDef = TypedDict(
    "SlotValueTypeDef",
    {
        "interpretedValue": str,
    },
    total=False,
)

SpecificationsTypeDef = TypedDict(
    "SpecificationsTypeDef",
    {
        "slotTypeId": str,
        "valueElicitationSetting": "SubSlotValueElicitationSettingTypeDef",
    },
)

_RequiredStartBotRecommendationRequestRequestTypeDef = TypedDict(
    "_RequiredStartBotRecommendationRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "transcriptSourceSetting": "TranscriptSourceSettingTypeDef",
    },
)
_OptionalStartBotRecommendationRequestRequestTypeDef = TypedDict(
    "_OptionalStartBotRecommendationRequestRequestTypeDef",
    {
        "encryptionSetting": "EncryptionSettingTypeDef",
    },
    total=False,
)

class StartBotRecommendationRequestRequestTypeDef(
    _RequiredStartBotRecommendationRequestRequestTypeDef,
    _OptionalStartBotRecommendationRequestRequestTypeDef,
):
    pass

StartBotRecommendationResponseTypeDef = TypedDict(
    "StartBotRecommendationResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationStatus": BotRecommendationStatusType,
        "botRecommendationId": str,
        "creationDateTime": datetime,
        "transcriptSourceSetting": "TranscriptSourceSettingTypeDef",
        "encryptionSetting": "EncryptionSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartImportRequestRequestTypeDef = TypedDict(
    "_RequiredStartImportRequestRequestTypeDef",
    {
        "importId": str,
        "resourceSpecification": "ImportResourceSpecificationTypeDef",
        "mergeStrategy": MergeStrategyType,
    },
)
_OptionalStartImportRequestRequestTypeDef = TypedDict(
    "_OptionalStartImportRequestRequestTypeDef",
    {
        "filePassword": str,
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
        "importId": str,
        "resourceSpecification": "ImportResourceSpecificationTypeDef",
        "mergeStrategy": MergeStrategyType,
        "importStatus": ImportStatusType,
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartTestExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredStartTestExecutionRequestRequestTypeDef",
    {
        "testSetId": str,
        "target": "TestExecutionTargetTypeDef",
        "apiMode": TestExecutionApiModeType,
    },
)
_OptionalStartTestExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalStartTestExecutionRequestRequestTypeDef",
    {
        "testExecutionModality": TestExecutionModalityType,
    },
    total=False,
)

class StartTestExecutionRequestRequestTypeDef(
    _RequiredStartTestExecutionRequestRequestTypeDef,
    _OptionalStartTestExecutionRequestRequestTypeDef,
):
    pass

StartTestExecutionResponseTypeDef = TypedDict(
    "StartTestExecutionResponseTypeDef",
    {
        "testExecutionId": str,
        "creationDateTime": datetime,
        "testSetId": str,
        "target": "TestExecutionTargetTypeDef",
        "apiMode": TestExecutionApiModeType,
        "testExecutionModality": TestExecutionModalityType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartTestSetGenerationRequestRequestTypeDef = TypedDict(
    "_RequiredStartTestSetGenerationRequestRequestTypeDef",
    {
        "testSetName": str,
        "storageLocation": "TestSetStorageLocationTypeDef",
        "generationDataSource": "TestSetGenerationDataSourceTypeDef",
        "roleArn": str,
    },
)
_OptionalStartTestSetGenerationRequestRequestTypeDef = TypedDict(
    "_OptionalStartTestSetGenerationRequestRequestTypeDef",
    {
        "description": str,
        "testSetTags": Dict[str, str],
    },
    total=False,
)

class StartTestSetGenerationRequestRequestTypeDef(
    _RequiredStartTestSetGenerationRequestRequestTypeDef,
    _OptionalStartTestSetGenerationRequestRequestTypeDef,
):
    pass

StartTestSetGenerationResponseTypeDef = TypedDict(
    "StartTestSetGenerationResponseTypeDef",
    {
        "testSetGenerationId": str,
        "creationDateTime": datetime,
        "testSetGenerationStatus": TestSetGenerationStatusType,
        "testSetName": str,
        "description": str,
        "storageLocation": "TestSetStorageLocationTypeDef",
        "generationDataSource": "TestSetGenerationDataSourceTypeDef",
        "roleArn": str,
        "testSetTags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStillWaitingResponseSpecificationTypeDef = TypedDict(
    "_RequiredStillWaitingResponseSpecificationTypeDef",
    {
        "messageGroups": List["MessageGroupTypeDef"],
        "frequencyInSeconds": int,
        "timeoutInSeconds": int,
    },
)
_OptionalStillWaitingResponseSpecificationTypeDef = TypedDict(
    "_OptionalStillWaitingResponseSpecificationTypeDef",
    {
        "allowInterrupt": bool,
    },
    total=False,
)

class StillWaitingResponseSpecificationTypeDef(
    _RequiredStillWaitingResponseSpecificationTypeDef,
    _OptionalStillWaitingResponseSpecificationTypeDef,
):
    pass

StopBotRecommendationRequestRequestTypeDef = TypedDict(
    "StopBotRecommendationRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationId": str,
    },
)

StopBotRecommendationResponseTypeDef = TypedDict(
    "StopBotRecommendationResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationStatus": BotRecommendationStatusType,
        "botRecommendationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubSlotSettingTypeDef = TypedDict(
    "SubSlotSettingTypeDef",
    {
        "expression": str,
        "slotSpecifications": Dict[str, "SpecificationsTypeDef"],
    },
    total=False,
)

SubSlotTypeCompositionTypeDef = TypedDict(
    "SubSlotTypeCompositionTypeDef",
    {
        "name": str,
        "slotTypeId": str,
    },
)

_RequiredSubSlotValueElicitationSettingTypeDef = TypedDict(
    "_RequiredSubSlotValueElicitationSettingTypeDef",
    {
        "promptSpecification": "PromptSpecificationTypeDef",
    },
)
_OptionalSubSlotValueElicitationSettingTypeDef = TypedDict(
    "_OptionalSubSlotValueElicitationSettingTypeDef",
    {
        "defaultValueSpecification": "SlotDefaultValueSpecificationTypeDef",
        "sampleUtterances": List["SampleUtteranceTypeDef"],
        "waitAndContinueSpecification": "WaitAndContinueSpecificationTypeDef",
    },
    total=False,
)

class SubSlotValueElicitationSettingTypeDef(
    _RequiredSubSlotValueElicitationSettingTypeDef, _OptionalSubSlotValueElicitationSettingTypeDef
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tags": Dict[str, str],
    },
)

_RequiredTestExecutionResultFilterByTypeDef = TypedDict(
    "_RequiredTestExecutionResultFilterByTypeDef",
    {
        "resultTypeFilter": TestResultTypeFilterType,
    },
)
_OptionalTestExecutionResultFilterByTypeDef = TypedDict(
    "_OptionalTestExecutionResultFilterByTypeDef",
    {
        "conversationLevelTestResultsFilterBy": "ConversationLevelTestResultsFilterByTypeDef",
    },
    total=False,
)

class TestExecutionResultFilterByTypeDef(
    _RequiredTestExecutionResultFilterByTypeDef, _OptionalTestExecutionResultFilterByTypeDef
):
    pass

TestExecutionResultItemsTypeDef = TypedDict(
    "TestExecutionResultItemsTypeDef",
    {
        "overallTestResults": "OverallTestResultsTypeDef",
        "conversationLevelTestResults": "ConversationLevelTestResultsTypeDef",
        "intentClassificationTestResults": "IntentClassificationTestResultsTypeDef",
        "intentLevelSlotResolutionTestResults": "IntentLevelSlotResolutionTestResultsTypeDef",
        "utteranceLevelTestResults": "UtteranceLevelTestResultsTypeDef",
    },
    total=False,
)

TestExecutionSortByTypeDef = TypedDict(
    "TestExecutionSortByTypeDef",
    {
        "attribute": TestExecutionSortAttributeType,
        "order": SortOrderType,
    },
)

TestExecutionSummaryTypeDef = TypedDict(
    "TestExecutionSummaryTypeDef",
    {
        "testExecutionId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "testExecutionStatus": TestExecutionStatusType,
        "testSetId": str,
        "testSetName": str,
        "target": "TestExecutionTargetTypeDef",
        "apiMode": TestExecutionApiModeType,
        "testExecutionModality": TestExecutionModalityType,
    },
    total=False,
)

TestExecutionTargetTypeDef = TypedDict(
    "TestExecutionTargetTypeDef",
    {
        "botAliasTarget": "BotAliasTestExecutionTargetTypeDef",
    },
    total=False,
)

TestSetDiscrepancyErrorsTypeDef = TypedDict(
    "TestSetDiscrepancyErrorsTypeDef",
    {
        "intentDiscrepancies": List["TestSetIntentDiscrepancyItemTypeDef"],
        "slotDiscrepancies": List["TestSetSlotDiscrepancyItemTypeDef"],
    },
)

TestSetDiscrepancyReportBotAliasTargetTypeDef = TypedDict(
    "TestSetDiscrepancyReportBotAliasTargetTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
    },
)

TestSetDiscrepancyReportResourceTargetTypeDef = TypedDict(
    "TestSetDiscrepancyReportResourceTargetTypeDef",
    {
        "botAliasTarget": "TestSetDiscrepancyReportBotAliasTargetTypeDef",
    },
    total=False,
)

TestSetExportSpecificationTypeDef = TypedDict(
    "TestSetExportSpecificationTypeDef",
    {
        "testSetId": str,
    },
)

TestSetGenerationDataSourceTypeDef = TypedDict(
    "TestSetGenerationDataSourceTypeDef",
    {
        "conversationLogsDataSource": "ConversationLogsDataSourceTypeDef",
    },
    total=False,
)

TestSetImportInputLocationTypeDef = TypedDict(
    "TestSetImportInputLocationTypeDef",
    {
        "s3BucketName": str,
        "s3Path": str,
    },
)

_RequiredTestSetImportResourceSpecificationTypeDef = TypedDict(
    "_RequiredTestSetImportResourceSpecificationTypeDef",
    {
        "testSetName": str,
        "roleArn": str,
        "storageLocation": "TestSetStorageLocationTypeDef",
        "importInputLocation": "TestSetImportInputLocationTypeDef",
        "modality": TestSetModalityType,
    },
)
_OptionalTestSetImportResourceSpecificationTypeDef = TypedDict(
    "_OptionalTestSetImportResourceSpecificationTypeDef",
    {
        "description": str,
        "testSetTags": Dict[str, str],
    },
    total=False,
)

class TestSetImportResourceSpecificationTypeDef(
    _RequiredTestSetImportResourceSpecificationTypeDef,
    _OptionalTestSetImportResourceSpecificationTypeDef,
):
    pass

TestSetIntentDiscrepancyItemTypeDef = TypedDict(
    "TestSetIntentDiscrepancyItemTypeDef",
    {
        "intentName": str,
        "errorMessage": str,
    },
)

TestSetSlotDiscrepancyItemTypeDef = TypedDict(
    "TestSetSlotDiscrepancyItemTypeDef",
    {
        "intentName": str,
        "slotName": str,
        "errorMessage": str,
    },
)

TestSetSortByTypeDef = TypedDict(
    "TestSetSortByTypeDef",
    {
        "attribute": TestSetSortAttributeType,
        "order": SortOrderType,
    },
)

_RequiredTestSetStorageLocationTypeDef = TypedDict(
    "_RequiredTestSetStorageLocationTypeDef",
    {
        "s3BucketName": str,
        "s3Path": str,
    },
)
_OptionalTestSetStorageLocationTypeDef = TypedDict(
    "_OptionalTestSetStorageLocationTypeDef",
    {
        "kmsKeyArn": str,
    },
    total=False,
)

class TestSetStorageLocationTypeDef(
    _RequiredTestSetStorageLocationTypeDef, _OptionalTestSetStorageLocationTypeDef
):
    pass

TestSetSummaryTypeDef = TypedDict(
    "TestSetSummaryTypeDef",
    {
        "testSetId": str,
        "testSetName": str,
        "description": str,
        "modality": TestSetModalityType,
        "status": TestSetStatusType,
        "roleArn": str,
        "numTurns": int,
        "storageLocation": "TestSetStorageLocationTypeDef",
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

_RequiredTestSetTurnRecordTypeDef = TypedDict(
    "_RequiredTestSetTurnRecordTypeDef",
    {
        "recordNumber": int,
        "turnSpecification": "TurnSpecificationTypeDef",
    },
)
_OptionalTestSetTurnRecordTypeDef = TypedDict(
    "_OptionalTestSetTurnRecordTypeDef",
    {
        "conversationId": str,
        "turnNumber": int,
    },
    total=False,
)

class TestSetTurnRecordTypeDef(
    _RequiredTestSetTurnRecordTypeDef, _OptionalTestSetTurnRecordTypeDef
):
    pass

TestSetTurnResultTypeDef = TypedDict(
    "TestSetTurnResultTypeDef",
    {
        "agent": "AgentTurnResultTypeDef",
        "user": "UserTurnResultTypeDef",
    },
    total=False,
)

TextInputSpecificationTypeDef = TypedDict(
    "TextInputSpecificationTypeDef",
    {
        "startTimeoutMs": int,
    },
)

TextLogDestinationTypeDef = TypedDict(
    "TextLogDestinationTypeDef",
    {
        "cloudWatch": "CloudWatchLogGroupLogDestinationTypeDef",
    },
)

_RequiredTextLogSettingTypeDef = TypedDict(
    "_RequiredTextLogSettingTypeDef",
    {
        "enabled": bool,
        "destination": "TextLogDestinationTypeDef",
    },
)
_OptionalTextLogSettingTypeDef = TypedDict(
    "_OptionalTextLogSettingTypeDef",
    {
        "selectiveLoggingEnabled": bool,
    },
    total=False,
)

class TextLogSettingTypeDef(_RequiredTextLogSettingTypeDef, _OptionalTextLogSettingTypeDef):
    pass

TranscriptFilterTypeDef = TypedDict(
    "TranscriptFilterTypeDef",
    {
        "lexTranscriptFilter": "LexTranscriptFilterTypeDef",
    },
    total=False,
)

TranscriptSourceSettingTypeDef = TypedDict(
    "TranscriptSourceSettingTypeDef",
    {
        "s3BucketTranscriptSource": "S3BucketTranscriptSourceTypeDef",
    },
    total=False,
)

TurnSpecificationTypeDef = TypedDict(
    "TurnSpecificationTypeDef",
    {
        "agentTurn": "AgentTurnSpecificationTypeDef",
        "userTurn": "UserTurnSpecificationTypeDef",
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateBotAliasRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBotAliasRequestRequestTypeDef",
    {
        "botAliasId": str,
        "botAliasName": str,
        "botId": str,
    },
)
_OptionalUpdateBotAliasRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBotAliasRequestRequestTypeDef",
    {
        "description": str,
        "botVersion": str,
        "botAliasLocaleSettings": Dict[str, "BotAliasLocaleSettingsTypeDef"],
        "conversationLogSettings": "ConversationLogSettingsTypeDef",
        "sentimentAnalysisSettings": "SentimentAnalysisSettingsTypeDef",
    },
    total=False,
)

class UpdateBotAliasRequestRequestTypeDef(
    _RequiredUpdateBotAliasRequestRequestTypeDef, _OptionalUpdateBotAliasRequestRequestTypeDef
):
    pass

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
        "botAliasStatus": BotAliasStatusType,
        "botId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateBotLocaleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBotLocaleRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "nluIntentConfidenceThreshold": float,
    },
)
_OptionalUpdateBotLocaleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBotLocaleRequestRequestTypeDef",
    {
        "description": str,
        "voiceSettings": "VoiceSettingsTypeDef",
    },
    total=False,
)

class UpdateBotLocaleRequestRequestTypeDef(
    _RequiredUpdateBotLocaleRequestRequestTypeDef, _OptionalUpdateBotLocaleRequestRequestTypeDef
):
    pass

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
        "botLocaleStatus": BotLocaleStatusType,
        "failureReasons": List[str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "recommendedActions": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBotRecommendationRequestRequestTypeDef = TypedDict(
    "UpdateBotRecommendationRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationId": str,
        "encryptionSetting": "EncryptionSettingTypeDef",
    },
)

UpdateBotRecommendationResponseTypeDef = TypedDict(
    "UpdateBotRecommendationResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationStatus": BotRecommendationStatusType,
        "botRecommendationId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "transcriptSourceSetting": "TranscriptSourceSettingTypeDef",
        "encryptionSetting": "EncryptionSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateBotRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBotRequestRequestTypeDef",
    {
        "botId": str,
        "botName": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": int,
    },
)
_OptionalUpdateBotRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBotRequestRequestTypeDef",
    {
        "description": str,
        "botType": BotTypeType,
        "botMembers": List["BotMemberTypeDef"],
    },
    total=False,
)

class UpdateBotRequestRequestTypeDef(
    _RequiredUpdateBotRequestRequestTypeDef, _OptionalUpdateBotRequestRequestTypeDef
):
    pass

UpdateBotResponseTypeDef = TypedDict(
    "UpdateBotResponseTypeDef",
    {
        "botId": str,
        "botName": str,
        "description": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": int,
        "botStatus": BotStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "botType": BotTypeType,
        "botMembers": List["BotMemberTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateExportRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateExportRequestRequestTypeDef",
    {
        "exportId": str,
    },
)
_OptionalUpdateExportRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateExportRequestRequestTypeDef",
    {
        "filePassword": str,
    },
    total=False,
)

class UpdateExportRequestRequestTypeDef(
    _RequiredUpdateExportRequestRequestTypeDef, _OptionalUpdateExportRequestRequestTypeDef
):
    pass

UpdateExportResponseTypeDef = TypedDict(
    "UpdateExportResponseTypeDef",
    {
        "exportId": str,
        "resourceSpecification": "ExportResourceSpecificationTypeDef",
        "fileFormat": ImportExportFileFormatType,
        "exportStatus": ExportStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateIntentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIntentRequestRequestTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalUpdateIntentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIntentRequestRequestTypeDef",
    {
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
        "initialResponseSetting": "InitialResponseSettingTypeDef",
    },
    total=False,
)

class UpdateIntentRequestRequestTypeDef(
    _RequiredUpdateIntentRequestRequestTypeDef, _OptionalUpdateIntentRequestRequestTypeDef
):
    pass

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
        "initialResponseSetting": "InitialResponseSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateResourcePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateResourcePolicyRequestRequestTypeDef",
    {
        "resourceArn": str,
        "policy": str,
    },
)
_OptionalUpdateResourcePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateResourcePolicyRequestRequestTypeDef",
    {
        "expectedRevisionId": str,
    },
    total=False,
)

class UpdateResourcePolicyRequestRequestTypeDef(
    _RequiredUpdateResourcePolicyRequestRequestTypeDef,
    _OptionalUpdateResourcePolicyRequestRequestTypeDef,
):
    pass

UpdateResourcePolicyResponseTypeDef = TypedDict(
    "UpdateResourcePolicyResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSlotRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSlotRequestRequestTypeDef",
    {
        "slotId": str,
        "slotName": str,
        "valueElicitationSetting": "SlotValueElicitationSettingTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
    },
)
_OptionalUpdateSlotRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSlotRequestRequestTypeDef",
    {
        "description": str,
        "slotTypeId": str,
        "obfuscationSetting": "ObfuscationSettingTypeDef",
        "multipleValuesSetting": "MultipleValuesSettingTypeDef",
        "subSlotSetting": "SubSlotSettingTypeDef",
    },
    total=False,
)

class UpdateSlotRequestRequestTypeDef(
    _RequiredUpdateSlotRequestRequestTypeDef, _OptionalUpdateSlotRequestRequestTypeDef
):
    pass

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
        "multipleValuesSetting": "MultipleValuesSettingTypeDef",
        "subSlotSetting": "SubSlotSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSlotTypeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSlotTypeRequestRequestTypeDef",
    {
        "slotTypeId": str,
        "slotTypeName": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalUpdateSlotTypeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSlotTypeRequestRequestTypeDef",
    {
        "description": str,
        "slotTypeValues": List["SlotTypeValueTypeDef"],
        "valueSelectionSetting": "SlotValueSelectionSettingTypeDef",
        "parentSlotTypeSignature": str,
        "externalSourceSetting": "ExternalSourceSettingTypeDef",
        "compositeSlotTypeSetting": "CompositeSlotTypeSettingTypeDef",
    },
    total=False,
)

class UpdateSlotTypeRequestRequestTypeDef(
    _RequiredUpdateSlotTypeRequestRequestTypeDef, _OptionalUpdateSlotTypeRequestRequestTypeDef
):
    pass

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
        "externalSourceSetting": "ExternalSourceSettingTypeDef",
        "compositeSlotTypeSetting": "CompositeSlotTypeSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTestSetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTestSetRequestRequestTypeDef",
    {
        "testSetId": str,
        "testSetName": str,
    },
)
_OptionalUpdateTestSetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTestSetRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateTestSetRequestRequestTypeDef(
    _RequiredUpdateTestSetRequestRequestTypeDef, _OptionalUpdateTestSetRequestRequestTypeDef
):
    pass

UpdateTestSetResponseTypeDef = TypedDict(
    "UpdateTestSetResponseTypeDef",
    {
        "testSetId": str,
        "testSetName": str,
        "description": str,
        "modality": TestSetModalityType,
        "status": TestSetStatusType,
        "roleArn": str,
        "numTurns": int,
        "storageLocation": "TestSetStorageLocationTypeDef",
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUserTurnInputSpecificationTypeDef = TypedDict(
    "_RequiredUserTurnInputSpecificationTypeDef",
    {
        "utteranceInput": "UtteranceInputSpecificationTypeDef",
    },
)
_OptionalUserTurnInputSpecificationTypeDef = TypedDict(
    "_OptionalUserTurnInputSpecificationTypeDef",
    {
        "requestAttributes": Dict[str, str],
        "sessionState": "InputSessionStateSpecificationTypeDef",
    },
    total=False,
)

class UserTurnInputSpecificationTypeDef(
    _RequiredUserTurnInputSpecificationTypeDef, _OptionalUserTurnInputSpecificationTypeDef
):
    pass

_RequiredUserTurnIntentOutputTypeDef = TypedDict(
    "_RequiredUserTurnIntentOutputTypeDef",
    {
        "name": str,
    },
)
_OptionalUserTurnIntentOutputTypeDef = TypedDict(
    "_OptionalUserTurnIntentOutputTypeDef",
    {
        "slots": Dict[str, "UserTurnSlotOutputTypeDef"],
    },
    total=False,
)

class UserTurnIntentOutputTypeDef(
    _RequiredUserTurnIntentOutputTypeDef, _OptionalUserTurnIntentOutputTypeDef
):
    pass

_RequiredUserTurnOutputSpecificationTypeDef = TypedDict(
    "_RequiredUserTurnOutputSpecificationTypeDef",
    {
        "intent": "UserTurnIntentOutputTypeDef",
    },
)
_OptionalUserTurnOutputSpecificationTypeDef = TypedDict(
    "_OptionalUserTurnOutputSpecificationTypeDef",
    {
        "activeContexts": List["ActiveContextTypeDef"],
        "transcript": str,
    },
    total=False,
)

class UserTurnOutputSpecificationTypeDef(
    _RequiredUserTurnOutputSpecificationTypeDef, _OptionalUserTurnOutputSpecificationTypeDef
):
    pass

_RequiredUserTurnResultTypeDef = TypedDict(
    "_RequiredUserTurnResultTypeDef",
    {
        "input": "UserTurnInputSpecificationTypeDef",
        "expectedOutput": "UserTurnOutputSpecificationTypeDef",
    },
)
_OptionalUserTurnResultTypeDef = TypedDict(
    "_OptionalUserTurnResultTypeDef",
    {
        "actualOutput": "UserTurnOutputSpecificationTypeDef",
        "errorDetails": "ExecutionErrorDetailsTypeDef",
        "endToEndResult": TestResultMatchStatusType,
        "intentMatchResult": TestResultMatchStatusType,
        "slotMatchResult": TestResultMatchStatusType,
        "speechTranscriptionResult": TestResultMatchStatusType,
        "conversationLevelResult": "ConversationLevelResultDetailTypeDef",
    },
    total=False,
)

class UserTurnResultTypeDef(_RequiredUserTurnResultTypeDef, _OptionalUserTurnResultTypeDef):
    pass

UserTurnSlotOutputTypeDef = TypedDict(
    "UserTurnSlotOutputTypeDef",
    {
        "value": str,
        "values": List[Dict[str, Any]],
        "subSlots": Dict[str, Dict[str, Any]],
    },
    total=False,
)

UserTurnSpecificationTypeDef = TypedDict(
    "UserTurnSpecificationTypeDef",
    {
        "input": "UserTurnInputSpecificationTypeDef",
        "expected": "UserTurnOutputSpecificationTypeDef",
    },
)

UtteranceAggregationDurationTypeDef = TypedDict(
    "UtteranceAggregationDurationTypeDef",
    {
        "relativeAggregationDuration": "RelativeAggregationDurationTypeDef",
    },
)

UtteranceAudioInputSpecificationTypeDef = TypedDict(
    "UtteranceAudioInputSpecificationTypeDef",
    {
        "audioFileS3Location": str,
    },
)

UtteranceBotResponseTypeDef = TypedDict(
    "UtteranceBotResponseTypeDef",
    {
        "content": str,
        "contentType": UtteranceContentTypeType,
        "imageResponseCard": "ImageResponseCardTypeDef",
    },
    total=False,
)

UtteranceDataSortByTypeDef = TypedDict(
    "UtteranceDataSortByTypeDef",
    {
        "name": Literal["UtteranceTimestamp"],
        "order": AnalyticsSortOrderType,
    },
)

UtteranceInputSpecificationTypeDef = TypedDict(
    "UtteranceInputSpecificationTypeDef",
    {
        "textInput": str,
        "audioInput": "UtteranceAudioInputSpecificationTypeDef",
    },
    total=False,
)

_RequiredUtteranceLevelTestResultItemTypeDef = TypedDict(
    "_RequiredUtteranceLevelTestResultItemTypeDef",
    {
        "recordNumber": int,
        "turnResult": "TestSetTurnResultTypeDef",
    },
)
_OptionalUtteranceLevelTestResultItemTypeDef = TypedDict(
    "_OptionalUtteranceLevelTestResultItemTypeDef",
    {
        "conversationId": str,
    },
    total=False,
)

class UtteranceLevelTestResultItemTypeDef(
    _RequiredUtteranceLevelTestResultItemTypeDef, _OptionalUtteranceLevelTestResultItemTypeDef
):
    pass

UtteranceLevelTestResultsTypeDef = TypedDict(
    "UtteranceLevelTestResultsTypeDef",
    {
        "items": List["UtteranceLevelTestResultItemTypeDef"],
    },
)

UtteranceSpecificationTypeDef = TypedDict(
    "UtteranceSpecificationTypeDef",
    {
        "botAliasId": str,
        "botVersion": str,
        "localeId": str,
        "sessionId": str,
        "channel": str,
        "mode": AnalyticsModalityType,
        "conversationStartTime": datetime,
        "conversationEndTime": datetime,
        "utterance": str,
        "utteranceTimestamp": datetime,
        "audioVoiceDurationMillis": int,
        "utteranceUnderstood": bool,
        "inputType": str,
        "outputType": str,
        "associatedIntentName": str,
        "associatedSlotName": str,
        "intentState": IntentStateType,
        "dialogActionType": str,
        "botResponseAudioVoiceId": str,
        "slotsFilledInSession": str,
        "utteranceRequestId": str,
        "botResponses": List["UtteranceBotResponseTypeDef"],
    },
    total=False,
)

_RequiredVoiceSettingsTypeDef = TypedDict(
    "_RequiredVoiceSettingsTypeDef",
    {
        "voiceId": str,
    },
)
_OptionalVoiceSettingsTypeDef = TypedDict(
    "_OptionalVoiceSettingsTypeDef",
    {
        "engine": VoiceEngineType,
    },
    total=False,
)

class VoiceSettingsTypeDef(_RequiredVoiceSettingsTypeDef, _OptionalVoiceSettingsTypeDef):
    pass

_RequiredWaitAndContinueSpecificationTypeDef = TypedDict(
    "_RequiredWaitAndContinueSpecificationTypeDef",
    {
        "waitingResponse": "ResponseSpecificationTypeDef",
        "continueResponse": "ResponseSpecificationTypeDef",
    },
)
_OptionalWaitAndContinueSpecificationTypeDef = TypedDict(
    "_OptionalWaitAndContinueSpecificationTypeDef",
    {
        "stillWaitingResponse": "StillWaitingResponseSpecificationTypeDef",
        "active": bool,
    },
    total=False,
)

class WaitAndContinueSpecificationTypeDef(
    _RequiredWaitAndContinueSpecificationTypeDef, _OptionalWaitAndContinueSpecificationTypeDef
):
    pass

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
