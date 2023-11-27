"""
Type annotations for lexv2-models service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_lexv2_models import LexModelsV2Client

    client: LexModelsV2Client = boto3.client("lexv2-models")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    BotTypeType,
    EffectType,
    ImportExportFileFormatType,
    MergeStrategyType,
    SearchOrderType,
    TestExecutionApiModeType,
    TestExecutionModalityType,
)
from .type_defs import (
    AggregatedUtterancesFilterTypeDef,
    AggregatedUtterancesSortByTypeDef,
    AnalyticsBinBySpecificationTypeDef,
    AnalyticsIntentFilterTypeDef,
    AnalyticsIntentGroupBySpecificationTypeDef,
    AnalyticsIntentMetricTypeDef,
    AnalyticsIntentStageFilterTypeDef,
    AnalyticsIntentStageGroupBySpecificationTypeDef,
    AnalyticsIntentStageMetricTypeDef,
    AnalyticsPathFilterTypeDef,
    AnalyticsSessionFilterTypeDef,
    AnalyticsSessionGroupBySpecificationTypeDef,
    AnalyticsSessionMetricTypeDef,
    AnalyticsUtteranceAttributeTypeDef,
    AnalyticsUtteranceFilterTypeDef,
    AnalyticsUtteranceGroupBySpecificationTypeDef,
    AnalyticsUtteranceMetricTypeDef,
    AssociatedTranscriptFilterTypeDef,
    BatchCreateCustomVocabularyItemResponseTypeDef,
    BatchDeleteCustomVocabularyItemResponseTypeDef,
    BatchUpdateCustomVocabularyItemResponseTypeDef,
    BotAliasLocaleSettingsTypeDef,
    BotFilterTypeDef,
    BotLocaleFilterTypeDef,
    BotLocaleSortByTypeDef,
    BotMemberTypeDef,
    BotSortByTypeDef,
    BotVersionLocaleDetailsTypeDef,
    BotVersionSortByTypeDef,
    BuildBotLocaleResponseTypeDef,
    BuiltInIntentSortByTypeDef,
    BuiltInSlotTypeSortByTypeDef,
    CompositeSlotTypeSettingTypeDef,
    ConversationLogSettingsTypeDef,
    CreateBotAliasResponseTypeDef,
    CreateBotLocaleResponseTypeDef,
    CreateBotResponseTypeDef,
    CreateBotVersionResponseTypeDef,
    CreateExportResponseTypeDef,
    CreateIntentResponseTypeDef,
    CreateResourcePolicyResponseTypeDef,
    CreateResourcePolicyStatementResponseTypeDef,
    CreateSlotResponseTypeDef,
    CreateSlotTypeResponseTypeDef,
    CreateTestSetDiscrepancyReportResponseTypeDef,
    CreateUploadUrlResponseTypeDef,
    CustomVocabularyEntryIdTypeDef,
    CustomVocabularyItemTypeDef,
    DataPrivacyTypeDef,
    DeleteBotAliasResponseTypeDef,
    DeleteBotLocaleResponseTypeDef,
    DeleteBotResponseTypeDef,
    DeleteBotVersionResponseTypeDef,
    DeleteCustomVocabularyResponseTypeDef,
    DeleteExportResponseTypeDef,
    DeleteImportResponseTypeDef,
    DeleteResourcePolicyResponseTypeDef,
    DeleteResourcePolicyStatementResponseTypeDef,
    DescribeBotAliasResponseTypeDef,
    DescribeBotLocaleResponseTypeDef,
    DescribeBotRecommendationResponseTypeDef,
    DescribeBotResourceGenerationResponseTypeDef,
    DescribeBotResponseTypeDef,
    DescribeBotVersionResponseTypeDef,
    DescribeCustomVocabularyMetadataResponseTypeDef,
    DescribeExportResponseTypeDef,
    DescribeImportResponseTypeDef,
    DescribeIntentResponseTypeDef,
    DescribeResourcePolicyResponseTypeDef,
    DescribeSlotResponseTypeDef,
    DescribeSlotTypeResponseTypeDef,
    DescribeTestExecutionResponseTypeDef,
    DescribeTestSetDiscrepancyReportResponseTypeDef,
    DescribeTestSetGenerationResponseTypeDef,
    DescribeTestSetResponseTypeDef,
    DialogCodeHookSettingsTypeDef,
    EncryptionSettingTypeDef,
    ExportFilterTypeDef,
    ExportResourceSpecificationTypeDef,
    ExportSortByTypeDef,
    ExternalSourceSettingTypeDef,
    FulfillmentCodeHookSettingsTypeDef,
    GenerateBotElementResponseTypeDef,
    GenerationSortByTypeDef,
    GenerativeAISettingsTypeDef,
    GetTestExecutionArtifactsUrlResponseTypeDef,
    ImportFilterTypeDef,
    ImportResourceSpecificationTypeDef,
    ImportSortByTypeDef,
    InitialResponseSettingTypeDef,
    InputContextTypeDef,
    IntentClosingSettingTypeDef,
    IntentConfirmationSettingTypeDef,
    IntentFilterTypeDef,
    IntentSortByTypeDef,
    KendraConfigurationTypeDef,
    ListAggregatedUtterancesResponseTypeDef,
    ListBotAliasesResponseTypeDef,
    ListBotLocalesResponseTypeDef,
    ListBotRecommendationsResponseTypeDef,
    ListBotResourceGenerationsResponseTypeDef,
    ListBotsResponseTypeDef,
    ListBotVersionsResponseTypeDef,
    ListBuiltInIntentsResponseTypeDef,
    ListBuiltInSlotTypesResponseTypeDef,
    ListCustomVocabularyItemsResponseTypeDef,
    ListExportsResponseTypeDef,
    ListImportsResponseTypeDef,
    ListIntentMetricsResponseTypeDef,
    ListIntentPathsResponseTypeDef,
    ListIntentsResponseTypeDef,
    ListIntentStageMetricsResponseTypeDef,
    ListRecommendedIntentsResponseTypeDef,
    ListSessionAnalyticsDataResponseTypeDef,
    ListSessionMetricsResponseTypeDef,
    ListSlotsResponseTypeDef,
    ListSlotTypesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTestExecutionResultItemsResponseTypeDef,
    ListTestExecutionsResponseTypeDef,
    ListTestSetRecordsResponseTypeDef,
    ListTestSetsResponseTypeDef,
    ListUtteranceAnalyticsDataResponseTypeDef,
    ListUtteranceMetricsResponseTypeDef,
    MultipleValuesSettingTypeDef,
    NewCustomVocabularyItemTypeDef,
    ObfuscationSettingTypeDef,
    OutputContextTypeDef,
    PrincipalTypeDef,
    SampleUtteranceTypeDef,
    SearchAssociatedTranscriptsResponseTypeDef,
    SentimentAnalysisSettingsTypeDef,
    SessionDataSortByTypeDef,
    SlotFilterTypeDef,
    SlotPriorityTypeDef,
    SlotSortByTypeDef,
    SlotTypeFilterTypeDef,
    SlotTypeSortByTypeDef,
    SlotTypeValueTypeDef,
    SlotValueElicitationSettingTypeDef,
    SlotValueSelectionSettingTypeDef,
    StartBotRecommendationResponseTypeDef,
    StartBotResourceGenerationResponseTypeDef,
    StartImportResponseTypeDef,
    StartTestExecutionResponseTypeDef,
    StartTestSetGenerationResponseTypeDef,
    StopBotRecommendationResponseTypeDef,
    SubSlotSettingTypeDef,
    TestExecutionResultFilterByTypeDef,
    TestExecutionSortByTypeDef,
    TestExecutionTargetTypeDef,
    TestSetDiscrepancyReportResourceTargetTypeDef,
    TestSetGenerationDataSourceTypeDef,
    TestSetSortByTypeDef,
    TestSetStorageLocationTypeDef,
    TranscriptSourceSettingTypeDef,
    UpdateBotAliasResponseTypeDef,
    UpdateBotLocaleResponseTypeDef,
    UpdateBotRecommendationResponseTypeDef,
    UpdateBotResponseTypeDef,
    UpdateExportResponseTypeDef,
    UpdateIntentResponseTypeDef,
    UpdateResourcePolicyResponseTypeDef,
    UpdateSlotResponseTypeDef,
    UpdateSlotTypeResponseTypeDef,
    UpdateTestSetResponseTypeDef,
    UtteranceAggregationDurationTypeDef,
    UtteranceDataSortByTypeDef,
    VoiceSettingsTypeDef,
)
from .waiter import (
    BotAliasAvailableWaiter,
    BotAvailableWaiter,
    BotExportCompletedWaiter,
    BotImportCompletedWaiter,
    BotLocaleBuiltWaiter,
    BotLocaleCreatedWaiter,
    BotLocaleExpressTestingAvailableWaiter,
    BotVersionAvailableWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("LexModelsV2Client",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    PreconditionFailedException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class LexModelsV2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LexModelsV2Client exceptions.
        """
    def batch_create_custom_vocabulary_item(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        customVocabularyItemList: List["NewCustomVocabularyItemTypeDef"]
    ) -> BatchCreateCustomVocabularyItemResponseTypeDef:
        """
        Create a batch of custom vocabulary items for a given bot locale's custom
        vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.batch_create_custom_vocabulary_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#batch_create_custom_vocabulary_item)
        """
    def batch_delete_custom_vocabulary_item(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        customVocabularyItemList: List["CustomVocabularyEntryIdTypeDef"]
    ) -> BatchDeleteCustomVocabularyItemResponseTypeDef:
        """
        Delete a batch of custom vocabulary items for a given bot locale's custom
        vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.batch_delete_custom_vocabulary_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#batch_delete_custom_vocabulary_item)
        """
    def batch_update_custom_vocabulary_item(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        customVocabularyItemList: List["CustomVocabularyItemTypeDef"]
    ) -> BatchUpdateCustomVocabularyItemResponseTypeDef:
        """
        Update a batch of custom vocabulary items for a given bot locale's custom
        vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.batch_update_custom_vocabulary_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#batch_update_custom_vocabulary_item)
        """
    def build_bot_locale(
        self, *, botId: str, botVersion: str, localeId: str
    ) -> BuildBotLocaleResponseTypeDef:
        """
        Builds a bot, its intents, and its slot types into a specific locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.build_bot_locale)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#build_bot_locale)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#close)
        """
    def create_bot(
        self,
        *,
        botName: str,
        roleArn: str,
        dataPrivacy: "DataPrivacyTypeDef",
        idleSessionTTLInSeconds: int,
        description: str = None,
        botTags: Dict[str, str] = None,
        testBotAliasTags: Dict[str, str] = None,
        botType: BotTypeType = None,
        botMembers: List["BotMemberTypeDef"] = None
    ) -> CreateBotResponseTypeDef:
        """
        Creates an Amazon Lex conversational bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_bot)
        """
    def create_bot_alias(
        self,
        *,
        botAliasName: str,
        botId: str,
        description: str = None,
        botVersion: str = None,
        botAliasLocaleSettings: Dict[str, "BotAliasLocaleSettingsTypeDef"] = None,
        conversationLogSettings: "ConversationLogSettingsTypeDef" = None,
        sentimentAnalysisSettings: "SentimentAnalysisSettingsTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateBotAliasResponseTypeDef:
        """
        Creates an alias for the specified version of a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_bot_alias)
        """
    def create_bot_locale(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        nluIntentConfidenceThreshold: float,
        description: str = None,
        voiceSettings: "VoiceSettingsTypeDef" = None,
        generativeAISettings: "GenerativeAISettingsTypeDef" = None
    ) -> CreateBotLocaleResponseTypeDef:
        """
        Creates a locale in the bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_locale)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_bot_locale)
        """
    def create_bot_version(
        self,
        *,
        botId: str,
        botVersionLocaleSpecification: Dict[str, "BotVersionLocaleDetailsTypeDef"],
        description: str = None
    ) -> CreateBotVersionResponseTypeDef:
        """
        Creates an immutable version of the bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_bot_version)
        """
    def create_export(
        self,
        *,
        resourceSpecification: "ExportResourceSpecificationTypeDef",
        fileFormat: ImportExportFileFormatType,
        filePassword: str = None
    ) -> CreateExportResponseTypeDef:
        """
        Creates a zip archive containing the contents of a bot or a bot locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.create_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_export)
        """
    def create_intent(
        self,
        *,
        intentName: str,
        botId: str,
        botVersion: str,
        localeId: str,
        description: str = None,
        parentIntentSignature: str = None,
        sampleUtterances: List["SampleUtteranceTypeDef"] = None,
        dialogCodeHook: "DialogCodeHookSettingsTypeDef" = None,
        fulfillmentCodeHook: "FulfillmentCodeHookSettingsTypeDef" = None,
        intentConfirmationSetting: "IntentConfirmationSettingTypeDef" = None,
        intentClosingSetting: "IntentClosingSettingTypeDef" = None,
        inputContexts: List["InputContextTypeDef"] = None,
        outputContexts: List["OutputContextTypeDef"] = None,
        kendraConfiguration: "KendraConfigurationTypeDef" = None,
        initialResponseSetting: "InitialResponseSettingTypeDef" = None
    ) -> CreateIntentResponseTypeDef:
        """
        Creates an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.create_intent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_intent)
        """
    def create_resource_policy(
        self, *, resourceArn: str, policy: str
    ) -> CreateResourcePolicyResponseTypeDef:
        """
        Creates a new resource policy with the specified policy statements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.create_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_resource_policy)
        """
    def create_resource_policy_statement(
        self,
        *,
        resourceArn: str,
        statementId: str,
        effect: EffectType,
        principal: List["PrincipalTypeDef"],
        action: List[str],
        condition: Dict[str, Dict[str, str]] = None,
        expectedRevisionId: str = None
    ) -> CreateResourcePolicyStatementResponseTypeDef:
        """
        Adds a new resource policy statement to a bot or bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.create_resource_policy_statement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_resource_policy_statement)
        """
    def create_slot(
        self,
        *,
        slotName: str,
        valueElicitationSetting: "SlotValueElicitationSettingTypeDef",
        botId: str,
        botVersion: str,
        localeId: str,
        intentId: str,
        description: str = None,
        slotTypeId: str = None,
        obfuscationSetting: "ObfuscationSettingTypeDef" = None,
        multipleValuesSetting: "MultipleValuesSettingTypeDef" = None,
        subSlotSetting: "SubSlotSettingTypeDef" = None
    ) -> CreateSlotResponseTypeDef:
        """
        Creates a slot in an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.create_slot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_slot)
        """
    def create_slot_type(
        self,
        *,
        slotTypeName: str,
        botId: str,
        botVersion: str,
        localeId: str,
        description: str = None,
        slotTypeValues: List["SlotTypeValueTypeDef"] = None,
        valueSelectionSetting: "SlotValueSelectionSettingTypeDef" = None,
        parentSlotTypeSignature: str = None,
        externalSourceSetting: "ExternalSourceSettingTypeDef" = None,
        compositeSlotTypeSetting: "CompositeSlotTypeSettingTypeDef" = None
    ) -> CreateSlotTypeResponseTypeDef:
        """
        Creates a custom slot type To create a custom slot type, specify a name for the
        slot type and a set of enumeration values, the values that a slot of this type
        can assume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.create_slot_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_slot_type)
        """
    def create_test_set_discrepancy_report(
        self, *, testSetId: str, target: "TestSetDiscrepancyReportResourceTargetTypeDef"
    ) -> CreateTestSetDiscrepancyReportResponseTypeDef:
        """
        Create a report that describes the differences between the bot and the test set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.create_test_set_discrepancy_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_test_set_discrepancy_report)
        """
    def create_upload_url(self) -> CreateUploadUrlResponseTypeDef:
        """
        Gets a pre-signed S3 write URL that you use to upload the zip archive when
        importing a bot or a bot locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.create_upload_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_upload_url)
        """
    def delete_bot(
        self, *, botId: str, skipResourceInUseCheck: bool = None
    ) -> DeleteBotResponseTypeDef:
        """
        Deletes all versions of a bot, including the `Draft` version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_bot)
        """
    def delete_bot_alias(
        self, *, botAliasId: str, botId: str, skipResourceInUseCheck: bool = None
    ) -> DeleteBotAliasResponseTypeDef:
        """
        Deletes the specified bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_bot_alias)
        """
    def delete_bot_locale(
        self, *, botId: str, botVersion: str, localeId: str
    ) -> DeleteBotLocaleResponseTypeDef:
        """
        Removes a locale from a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_locale)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_bot_locale)
        """
    def delete_bot_version(
        self, *, botId: str, botVersion: str, skipResourceInUseCheck: bool = None
    ) -> DeleteBotVersionResponseTypeDef:
        """
        Deletes a specific version of a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_bot_version)
        """
    def delete_custom_vocabulary(
        self, *, botId: str, botVersion: str, localeId: str
    ) -> DeleteCustomVocabularyResponseTypeDef:
        """
        Removes a custom vocabulary from the specified locale in the specified bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.delete_custom_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_custom_vocabulary)
        """
    def delete_export(self, *, exportId: str) -> DeleteExportResponseTypeDef:
        """
        Removes a previous export and the associated files stored in an S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.delete_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_export)
        """
    def delete_import(self, *, importId: str) -> DeleteImportResponseTypeDef:
        """
        Removes a previous import and the associated file stored in an S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.delete_import)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_import)
        """
    def delete_intent(self, *, intentId: str, botId: str, botVersion: str, localeId: str) -> None:
        """
        Removes the specified intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.delete_intent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_intent)
        """
    def delete_resource_policy(
        self, *, resourceArn: str, expectedRevisionId: str = None
    ) -> DeleteResourcePolicyResponseTypeDef:
        """
        Removes an existing policy from a bot or bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_resource_policy)
        """
    def delete_resource_policy_statement(
        self, *, resourceArn: str, statementId: str, expectedRevisionId: str = None
    ) -> DeleteResourcePolicyStatementResponseTypeDef:
        """
        Deletes a policy statement from a resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.delete_resource_policy_statement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_resource_policy_statement)
        """
    def delete_slot(
        self, *, slotId: str, botId: str, botVersion: str, localeId: str, intentId: str
    ) -> None:
        """
        Deletes the specified slot from an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.delete_slot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_slot)
        """
    def delete_slot_type(
        self,
        *,
        slotTypeId: str,
        botId: str,
        botVersion: str,
        localeId: str,
        skipResourceInUseCheck: bool = None
    ) -> None:
        """
        Deletes a slot type from a bot locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.delete_slot_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_slot_type)
        """
    def delete_test_set(self, *, testSetId: str) -> None:
        """
        The action to delete the selected test set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.delete_test_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_test_set)
        """
    def delete_utterances(
        self, *, botId: str, localeId: str = None, sessionId: str = None
    ) -> Dict[str, Any]:
        """
        Deletes stored utterances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.delete_utterances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_utterances)
        """
    def describe_bot(self, *, botId: str) -> DescribeBotResponseTypeDef:
        """
        Provides metadata information about a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_bot)
        """
    def describe_bot_alias(self, *, botAliasId: str, botId: str) -> DescribeBotAliasResponseTypeDef:
        """
        Get information about a specific bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_bot_alias)
        """
    def describe_bot_locale(
        self, *, botId: str, botVersion: str, localeId: str
    ) -> DescribeBotLocaleResponseTypeDef:
        """
        Describes the settings that a bot has for a specific locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_locale)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_bot_locale)
        """
    def describe_bot_recommendation(
        self, *, botId: str, botVersion: str, localeId: str, botRecommendationId: str
    ) -> DescribeBotRecommendationResponseTypeDef:
        """
        Provides metadata information about a bot recommendation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_recommendation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_bot_recommendation)
        """
    def describe_bot_resource_generation(
        self, *, botId: str, botVersion: str, localeId: str, generationId: str
    ) -> DescribeBotResourceGenerationResponseTypeDef:
        """
        Returns information about a request to generate a bot through natural language
        description, made through the `StartBotResource` API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_resource_generation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_bot_resource_generation)
        """
    def describe_bot_version(
        self, *, botId: str, botVersion: str
    ) -> DescribeBotVersionResponseTypeDef:
        """
        Provides metadata about a version of a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_bot_version)
        """
    def describe_custom_vocabulary_metadata(
        self, *, botId: str, botVersion: str, localeId: str
    ) -> DescribeCustomVocabularyMetadataResponseTypeDef:
        """
        Provides metadata information about a custom vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.describe_custom_vocabulary_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_custom_vocabulary_metadata)
        """
    def describe_export(self, *, exportId: str) -> DescribeExportResponseTypeDef:
        """
        Gets information about a specific export.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.describe_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_export)
        """
    def describe_import(self, *, importId: str) -> DescribeImportResponseTypeDef:
        """
        Gets information about a specific import.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.describe_import)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_import)
        """
    def describe_intent(
        self, *, intentId: str, botId: str, botVersion: str, localeId: str
    ) -> DescribeIntentResponseTypeDef:
        """
        Returns metadata about an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.describe_intent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_intent)
        """
    def describe_resource_policy(
        self, *, resourceArn: str
    ) -> DescribeResourcePolicyResponseTypeDef:
        """
        Gets the resource policy and policy revision for a bot or bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.describe_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_resource_policy)
        """
    def describe_slot(
        self, *, slotId: str, botId: str, botVersion: str, localeId: str, intentId: str
    ) -> DescribeSlotResponseTypeDef:
        """
        Gets metadata information about a slot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.describe_slot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_slot)
        """
    def describe_slot_type(
        self, *, slotTypeId: str, botId: str, botVersion: str, localeId: str
    ) -> DescribeSlotTypeResponseTypeDef:
        """
        Gets metadata information about a slot type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.describe_slot_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_slot_type)
        """
    def describe_test_execution(
        self, *, testExecutionId: str
    ) -> DescribeTestExecutionResponseTypeDef:
        """
        Gets metadata information about the test execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.describe_test_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_test_execution)
        """
    def describe_test_set(self, *, testSetId: str) -> DescribeTestSetResponseTypeDef:
        """
        Gets metadata information about the test set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.describe_test_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_test_set)
        """
    def describe_test_set_discrepancy_report(
        self, *, testSetDiscrepancyReportId: str
    ) -> DescribeTestSetDiscrepancyReportResponseTypeDef:
        """
        Gets metadata information about the test set discrepancy report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.describe_test_set_discrepancy_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_test_set_discrepancy_report)
        """
    def describe_test_set_generation(
        self, *, testSetGenerationId: str
    ) -> DescribeTestSetGenerationResponseTypeDef:
        """
        Gets metadata information about the test set generation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.describe_test_set_generation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_test_set_generation)
        """
    def generate_bot_element(
        self, *, intentId: str, botId: str, botVersion: str, localeId: str
    ) -> GenerateBotElementResponseTypeDef:
        """
        Generates sample utterances for an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.generate_bot_element)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#generate_bot_element)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#generate_presigned_url)
        """
    def get_test_execution_artifacts_url(
        self, *, testExecutionId: str
    ) -> GetTestExecutionArtifactsUrlResponseTypeDef:
        """
        The pre-signed Amazon S3 URL to download the test execution result artifacts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.get_test_execution_artifacts_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#get_test_execution_artifacts_url)
        """
    def list_aggregated_utterances(
        self,
        *,
        botId: str,
        localeId: str,
        aggregationDuration: "UtteranceAggregationDurationTypeDef",
        botAliasId: str = None,
        botVersion: str = None,
        sortBy: "AggregatedUtterancesSortByTypeDef" = None,
        filters: List["AggregatedUtterancesFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListAggregatedUtterancesResponseTypeDef:
        """
        Provides a list of utterances that users have sent to the bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_aggregated_utterances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_aggregated_utterances)
        """
    def list_bot_aliases(
        self, *, botId: str, maxResults: int = None, nextToken: str = None
    ) -> ListBotAliasesResponseTypeDef:
        """
        Gets a list of aliases for the specified bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_bot_aliases)
        """
    def list_bot_locales(
        self,
        *,
        botId: str,
        botVersion: str,
        sortBy: "BotLocaleSortByTypeDef" = None,
        filters: List["BotLocaleFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListBotLocalesResponseTypeDef:
        """
        Gets a list of locales for the specified bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_locales)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_bot_locales)
        """
    def list_bot_recommendations(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListBotRecommendationsResponseTypeDef:
        """
        Get a list of bot recommendations that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_bot_recommendations)
        """
    def list_bot_resource_generations(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        sortBy: "GenerationSortByTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListBotResourceGenerationsResponseTypeDef:
        """
        Lists the generation requests made for a bot locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_resource_generations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_bot_resource_generations)
        """
    def list_bot_versions(
        self,
        *,
        botId: str,
        sortBy: "BotVersionSortByTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListBotVersionsResponseTypeDef:
        """
        Gets information about all of the versions of a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_bot_versions)
        """
    def list_bots(
        self,
        *,
        sortBy: "BotSortByTypeDef" = None,
        filters: List["BotFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListBotsResponseTypeDef:
        """
        Gets a list of available bots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_bots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_bots)
        """
    def list_built_in_intents(
        self,
        *,
        localeId: str,
        sortBy: "BuiltInIntentSortByTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListBuiltInIntentsResponseTypeDef:
        """
        Gets a list of built-in intents provided by Amazon Lex that you can use in your
        bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_built_in_intents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_built_in_intents)
        """
    def list_built_in_slot_types(
        self,
        *,
        localeId: str,
        sortBy: "BuiltInSlotTypeSortByTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListBuiltInSlotTypesResponseTypeDef:
        """
        Gets a list of built-in slot types that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_built_in_slot_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_built_in_slot_types)
        """
    def list_custom_vocabulary_items(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListCustomVocabularyItemsResponseTypeDef:
        """
        Paginated list of custom vocabulary items for a given bot locale's custom
        vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_custom_vocabulary_items)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_custom_vocabulary_items)
        """
    def list_exports(
        self,
        *,
        botId: str = None,
        botVersion: str = None,
        sortBy: "ExportSortByTypeDef" = None,
        filters: List["ExportFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None,
        localeId: str = None
    ) -> ListExportsResponseTypeDef:
        """
        Lists the exports for a bot, bot locale, or custom vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_exports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_exports)
        """
    def list_imports(
        self,
        *,
        botId: str = None,
        botVersion: str = None,
        sortBy: "ImportSortByTypeDef" = None,
        filters: List["ImportFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None,
        localeId: str = None
    ) -> ListImportsResponseTypeDef:
        """
        Lists the imports for a bot, bot locale, or custom vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_imports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_imports)
        """
    def list_intent_metrics(
        self,
        *,
        botId: str,
        startDateTime: Union[datetime, str],
        endDateTime: Union[datetime, str],
        metrics: List["AnalyticsIntentMetricTypeDef"],
        binBy: List["AnalyticsBinBySpecificationTypeDef"] = None,
        groupBy: List["AnalyticsIntentGroupBySpecificationTypeDef"] = None,
        filters: List["AnalyticsIntentFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListIntentMetricsResponseTypeDef:
        """
        Retrieves summary metrics for the intents in your bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_intent_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_intent_metrics)
        """
    def list_intent_paths(
        self,
        *,
        botId: str,
        startDateTime: Union[datetime, str],
        endDateTime: Union[datetime, str],
        intentPath: str,
        filters: List["AnalyticsPathFilterTypeDef"] = None
    ) -> ListIntentPathsResponseTypeDef:
        """
        Retrieves summary statistics for a path of intents that users take over sessions
        with your bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_intent_paths)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_intent_paths)
        """
    def list_intent_stage_metrics(
        self,
        *,
        botId: str,
        startDateTime: Union[datetime, str],
        endDateTime: Union[datetime, str],
        metrics: List["AnalyticsIntentStageMetricTypeDef"],
        binBy: List["AnalyticsBinBySpecificationTypeDef"] = None,
        groupBy: List["AnalyticsIntentStageGroupBySpecificationTypeDef"] = None,
        filters: List["AnalyticsIntentStageFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListIntentStageMetricsResponseTypeDef:
        """
        Retrieves summary metrics for the stages within intents in your bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_intent_stage_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_intent_stage_metrics)
        """
    def list_intents(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        sortBy: "IntentSortByTypeDef" = None,
        filters: List["IntentFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListIntentsResponseTypeDef:
        """
        Get a list of intents that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_intents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_intents)
        """
    def list_recommended_intents(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        botRecommendationId: str,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListRecommendedIntentsResponseTypeDef:
        """
        Gets a list of recommended intents provided by the bot recommendation that you
        can use in your bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_recommended_intents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_recommended_intents)
        """
    def list_session_analytics_data(
        self,
        *,
        botId: str,
        startDateTime: Union[datetime, str],
        endDateTime: Union[datetime, str],
        sortBy: "SessionDataSortByTypeDef" = None,
        filters: List["AnalyticsSessionFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListSessionAnalyticsDataResponseTypeDef:
        """
        Retrieves a list of metadata for individual user sessions with your bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_session_analytics_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_session_analytics_data)
        """
    def list_session_metrics(
        self,
        *,
        botId: str,
        startDateTime: Union[datetime, str],
        endDateTime: Union[datetime, str],
        metrics: List["AnalyticsSessionMetricTypeDef"],
        binBy: List["AnalyticsBinBySpecificationTypeDef"] = None,
        groupBy: List["AnalyticsSessionGroupBySpecificationTypeDef"] = None,
        filters: List["AnalyticsSessionFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListSessionMetricsResponseTypeDef:
        """
        Retrieves summary metrics for the user sessions with your bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_session_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_session_metrics)
        """
    def list_slot_types(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        sortBy: "SlotTypeSortByTypeDef" = None,
        filters: List["SlotTypeFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListSlotTypesResponseTypeDef:
        """
        Gets a list of slot types that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_slot_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_slot_types)
        """
    def list_slots(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        intentId: str,
        sortBy: "SlotSortByTypeDef" = None,
        filters: List["SlotFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListSlotsResponseTypeDef:
        """
        Gets a list of slots that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_slots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_slots)
        """
    def list_tags_for_resource(self, *, resourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        Gets a list of tags associated with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_tags_for_resource)
        """
    def list_test_execution_result_items(
        self,
        *,
        testExecutionId: str,
        resultFilterBy: "TestExecutionResultFilterByTypeDef",
        maxResults: int = None,
        nextToken: str = None
    ) -> ListTestExecutionResultItemsResponseTypeDef:
        """
        Gets a list of test execution result items.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_test_execution_result_items)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_test_execution_result_items)
        """
    def list_test_executions(
        self,
        *,
        sortBy: "TestExecutionSortByTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListTestExecutionsResponseTypeDef:
        """
        The list of test set executions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_test_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_test_executions)
        """
    def list_test_set_records(
        self, *, testSetId: str, maxResults: int = None, nextToken: str = None
    ) -> ListTestSetRecordsResponseTypeDef:
        """
        The list of test set records.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_test_set_records)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_test_set_records)
        """
    def list_test_sets(
        self,
        *,
        sortBy: "TestSetSortByTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListTestSetsResponseTypeDef:
        """
        The list of the test sets See also: `AWS API Documentation <https://docs.aws.ama
        zon.com/goto/WebAPI/models.lex.v2-2020-08-07/ListTestSets>`_ **Request Syntax**
        response = client.list_test_sets( sortBy={ 'attribute':
        'TestSetName'|'LastUpdatedDateTime', 'order'...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_test_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_test_sets)
        """
    def list_utterance_analytics_data(
        self,
        *,
        botId: str,
        startDateTime: Union[datetime, str],
        endDateTime: Union[datetime, str],
        sortBy: "UtteranceDataSortByTypeDef" = None,
        filters: List["AnalyticsUtteranceFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListUtteranceAnalyticsDataResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_utterance_analytics_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_utterance_analytics_data)
        """
    def list_utterance_metrics(
        self,
        *,
        botId: str,
        startDateTime: Union[datetime, str],
        endDateTime: Union[datetime, str],
        metrics: List["AnalyticsUtteranceMetricTypeDef"],
        binBy: List["AnalyticsBinBySpecificationTypeDef"] = None,
        groupBy: List["AnalyticsUtteranceGroupBySpecificationTypeDef"] = None,
        attributes: List["AnalyticsUtteranceAttributeTypeDef"] = None,
        filters: List["AnalyticsUtteranceFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListUtteranceMetricsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.list_utterance_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_utterance_metrics)
        """
    def search_associated_transcripts(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        botRecommendationId: str,
        filters: List["AssociatedTranscriptFilterTypeDef"],
        searchOrder: SearchOrderType = None,
        maxResults: int = None,
        nextIndex: int = None
    ) -> SearchAssociatedTranscriptsResponseTypeDef:
        """
        Search for associated transcripts that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.search_associated_transcripts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#search_associated_transcripts)
        """
    def start_bot_recommendation(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        transcriptSourceSetting: "TranscriptSourceSettingTypeDef",
        encryptionSetting: "EncryptionSettingTypeDef" = None
    ) -> StartBotRecommendationResponseTypeDef:
        """
        Use this to provide your transcript data, and to start the bot recommendation
        process.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.start_bot_recommendation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#start_bot_recommendation)
        """
    def start_bot_resource_generation(
        self, *, generationInputPrompt: str, botId: str, botVersion: str, localeId: str
    ) -> StartBotResourceGenerationResponseTypeDef:
        """
        Starts a request for the descriptive bot builder to generate a bot locale
        configuration based on the prompt you provide it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.start_bot_resource_generation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#start_bot_resource_generation)
        """
    def start_import(
        self,
        *,
        importId: str,
        resourceSpecification: "ImportResourceSpecificationTypeDef",
        mergeStrategy: MergeStrategyType,
        filePassword: str = None
    ) -> StartImportResponseTypeDef:
        """
        Starts importing a bot, bot locale, or custom vocabulary from a zip archive that
        you uploaded to an S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.start_import)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#start_import)
        """
    def start_test_execution(
        self,
        *,
        testSetId: str,
        target: "TestExecutionTargetTypeDef",
        apiMode: TestExecutionApiModeType,
        testExecutionModality: TestExecutionModalityType = None
    ) -> StartTestExecutionResponseTypeDef:
        """
        The action to start test set execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.start_test_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#start_test_execution)
        """
    def start_test_set_generation(
        self,
        *,
        testSetName: str,
        storageLocation: "TestSetStorageLocationTypeDef",
        generationDataSource: "TestSetGenerationDataSourceTypeDef",
        roleArn: str,
        description: str = None,
        testSetTags: Dict[str, str] = None
    ) -> StartTestSetGenerationResponseTypeDef:
        """
        The action to start the generation of test set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.start_test_set_generation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#start_test_set_generation)
        """
    def stop_bot_recommendation(
        self, *, botId: str, botVersion: str, localeId: str, botRecommendationId: str
    ) -> StopBotRecommendationResponseTypeDef:
        """
        Stop an already running Bot Recommendation request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.stop_bot_recommendation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#stop_bot_recommendation)
        """
    def tag_resource(self, *, resourceARN: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceARN: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from a bot, bot alias, or bot channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#untag_resource)
        """
    def update_bot(
        self,
        *,
        botId: str,
        botName: str,
        roleArn: str,
        dataPrivacy: "DataPrivacyTypeDef",
        idleSessionTTLInSeconds: int,
        description: str = None,
        botType: BotTypeType = None,
        botMembers: List["BotMemberTypeDef"] = None
    ) -> UpdateBotResponseTypeDef:
        """
        Updates the configuration of an existing bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update_bot)
        """
    def update_bot_alias(
        self,
        *,
        botAliasId: str,
        botAliasName: str,
        botId: str,
        description: str = None,
        botVersion: str = None,
        botAliasLocaleSettings: Dict[str, "BotAliasLocaleSettingsTypeDef"] = None,
        conversationLogSettings: "ConversationLogSettingsTypeDef" = None,
        sentimentAnalysisSettings: "SentimentAnalysisSettingsTypeDef" = None
    ) -> UpdateBotAliasResponseTypeDef:
        """
        Updates the configuration of an existing bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update_bot_alias)
        """
    def update_bot_locale(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        nluIntentConfidenceThreshold: float,
        description: str = None,
        voiceSettings: "VoiceSettingsTypeDef" = None,
        generativeAISettings: "GenerativeAISettingsTypeDef" = None
    ) -> UpdateBotLocaleResponseTypeDef:
        """
        Updates the settings that a bot has for a specific locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot_locale)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update_bot_locale)
        """
    def update_bot_recommendation(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        botRecommendationId: str,
        encryptionSetting: "EncryptionSettingTypeDef"
    ) -> UpdateBotRecommendationResponseTypeDef:
        """
        Updates an existing bot recommendation request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot_recommendation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update_bot_recommendation)
        """
    def update_export(
        self, *, exportId: str, filePassword: str = None
    ) -> UpdateExportResponseTypeDef:
        """
        Updates the password used to protect an export zip archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.update_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update_export)
        """
    def update_intent(
        self,
        *,
        intentId: str,
        intentName: str,
        botId: str,
        botVersion: str,
        localeId: str,
        description: str = None,
        parentIntentSignature: str = None,
        sampleUtterances: List["SampleUtteranceTypeDef"] = None,
        dialogCodeHook: "DialogCodeHookSettingsTypeDef" = None,
        fulfillmentCodeHook: "FulfillmentCodeHookSettingsTypeDef" = None,
        slotPriorities: List["SlotPriorityTypeDef"] = None,
        intentConfirmationSetting: "IntentConfirmationSettingTypeDef" = None,
        intentClosingSetting: "IntentClosingSettingTypeDef" = None,
        inputContexts: List["InputContextTypeDef"] = None,
        outputContexts: List["OutputContextTypeDef"] = None,
        kendraConfiguration: "KendraConfigurationTypeDef" = None,
        initialResponseSetting: "InitialResponseSettingTypeDef" = None
    ) -> UpdateIntentResponseTypeDef:
        """
        Updates the settings for an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.update_intent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update_intent)
        """
    def update_resource_policy(
        self, *, resourceArn: str, policy: str, expectedRevisionId: str = None
    ) -> UpdateResourcePolicyResponseTypeDef:
        """
        Replaces the existing resource policy for a bot or bot alias with a new one.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.update_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update_resource_policy)
        """
    def update_slot(
        self,
        *,
        slotId: str,
        slotName: str,
        valueElicitationSetting: "SlotValueElicitationSettingTypeDef",
        botId: str,
        botVersion: str,
        localeId: str,
        intentId: str,
        description: str = None,
        slotTypeId: str = None,
        obfuscationSetting: "ObfuscationSettingTypeDef" = None,
        multipleValuesSetting: "MultipleValuesSettingTypeDef" = None,
        subSlotSetting: "SubSlotSettingTypeDef" = None
    ) -> UpdateSlotResponseTypeDef:
        """
        Updates the settings for a slot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.update_slot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update_slot)
        """
    def update_slot_type(
        self,
        *,
        slotTypeId: str,
        slotTypeName: str,
        botId: str,
        botVersion: str,
        localeId: str,
        description: str = None,
        slotTypeValues: List["SlotTypeValueTypeDef"] = None,
        valueSelectionSetting: "SlotValueSelectionSettingTypeDef" = None,
        parentSlotTypeSignature: str = None,
        externalSourceSetting: "ExternalSourceSettingTypeDef" = None,
        compositeSlotTypeSetting: "CompositeSlotTypeSettingTypeDef" = None
    ) -> UpdateSlotTypeResponseTypeDef:
        """
        Updates the configuration of an existing slot type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.update_slot_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update_slot_type)
        """
    def update_test_set(
        self, *, testSetId: str, testSetName: str, description: str = None
    ) -> UpdateTestSetResponseTypeDef:
        """
        The action to update the test set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Client.update_test_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update_test_set)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["bot_alias_available"]) -> BotAliasAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotAliasAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botaliasavailablewaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["bot_available"]) -> BotAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botavailablewaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["bot_export_completed"]) -> BotExportCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotExportCompleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botexportcompletedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["bot_import_completed"]) -> BotImportCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotImportCompleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botimportcompletedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["bot_locale_built"]) -> BotLocaleBuiltWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotLocaleBuilt)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botlocalebuiltwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["bot_locale_created"]) -> BotLocaleCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotLocaleCreated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botlocalecreatedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["bot_locale_express_testing_available"]
    ) -> BotLocaleExpressTestingAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotLocaleExpressTestingAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botlocaleexpresstestingavailablewaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["bot_version_available"]
    ) -> BotVersionAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/lexv2-models.html#LexModelsV2.Waiter.BotVersionAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/waiters.html#botversionavailablewaiter)
        """
