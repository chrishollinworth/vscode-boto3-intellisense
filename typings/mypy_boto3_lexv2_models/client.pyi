"""
Main interface for lexv2-models service client

Usage::

    ```python
    import boto3
    from mypy_boto3_lexv2_models import LexModelsV2Client

    client: LexModelsV2Client = boto3.client("lexv2-models")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_lexv2_models.type_defs import (
    BotAliasLocaleSettingsTypeDef,
    BotFilterTypeDef,
    BotLocaleFilterTypeDef,
    BotLocaleSortByTypeDef,
    BotSortByTypeDef,
    BotVersionLocaleDetailsTypeDef,
    BotVersionSortByTypeDef,
    BuildBotLocaleResponseTypeDef,
    BuiltInIntentSortByTypeDef,
    BuiltInSlotTypeSortByTypeDef,
    ConversationLogSettingsTypeDef,
    CreateBotAliasResponseTypeDef,
    CreateBotLocaleResponseTypeDef,
    CreateBotResponseTypeDef,
    CreateBotVersionResponseTypeDef,
    CreateIntentResponseTypeDef,
    CreateSlotResponseTypeDef,
    CreateSlotTypeResponseTypeDef,
    DataPrivacyTypeDef,
    DeleteBotAliasResponseTypeDef,
    DeleteBotLocaleResponseTypeDef,
    DeleteBotResponseTypeDef,
    DeleteBotVersionResponseTypeDef,
    DescribeBotAliasResponseTypeDef,
    DescribeBotLocaleResponseTypeDef,
    DescribeBotResponseTypeDef,
    DescribeBotVersionResponseTypeDef,
    DescribeIntentResponseTypeDef,
    DescribeSlotResponseTypeDef,
    DescribeSlotTypeResponseTypeDef,
    DialogCodeHookSettingsTypeDef,
    FulfillmentCodeHookSettingsTypeDef,
    InputContextTypeDef,
    IntentClosingSettingTypeDef,
    IntentConfirmationSettingTypeDef,
    IntentFilterTypeDef,
    IntentSortByTypeDef,
    KendraConfigurationTypeDef,
    ListBotAliasesResponseTypeDef,
    ListBotLocalesResponseTypeDef,
    ListBotsResponseTypeDef,
    ListBotVersionsResponseTypeDef,
    ListBuiltInIntentsResponseTypeDef,
    ListBuiltInSlotTypesResponseTypeDef,
    ListIntentsResponseTypeDef,
    ListSlotsResponseTypeDef,
    ListSlotTypesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ObfuscationSettingTypeDef,
    OutputContextTypeDef,
    SampleUtteranceTypeDef,
    SentimentAnalysisSettingsTypeDef,
    SlotFilterTypeDef,
    SlotPriorityTypeDef,
    SlotSortByTypeDef,
    SlotTypeFilterTypeDef,
    SlotTypeSortByTypeDef,
    SlotTypeValueTypeDef,
    SlotValueElicitationSettingTypeDef,
    SlotValueSelectionSettingTypeDef,
    UpdateBotAliasResponseTypeDef,
    UpdateBotLocaleResponseTypeDef,
    UpdateBotResponseTypeDef,
    UpdateIntentResponseTypeDef,
    UpdateSlotResponseTypeDef,
    UpdateSlotTypeResponseTypeDef,
    VoiceSettingsTypeDef,
)

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


class LexModelsV2Client:
    """
    [LexModelsV2.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def build_bot_locale(
        self, botId: str, botVersion: str, localeId: str
    ) -> BuildBotLocaleResponseTypeDef:
        """
        [Client.build_bot_locale documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.build_bot_locale)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.can_paginate)
        """

    def create_bot(
        self,
        botName: str,
        roleArn: str,
        dataPrivacy: "DataPrivacyTypeDef",
        idleSessionTTLInSeconds: int,
        description: str = None,
        botTags: Dict[str, str] = None,
        testBotAliasTags: Dict[str, str] = None,
    ) -> CreateBotResponseTypeDef:
        """
        [Client.create_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot)
        """

    def create_bot_alias(
        self,
        botAliasName: str,
        botId: str,
        description: str = None,
        botVersion: str = None,
        botAliasLocaleSettings: Dict[str, "BotAliasLocaleSettingsTypeDef"] = None,
        conversationLogSettings: "ConversationLogSettingsTypeDef" = None,
        sentimentAnalysisSettings: "SentimentAnalysisSettingsTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> CreateBotAliasResponseTypeDef:
        """
        [Client.create_bot_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_alias)
        """

    def create_bot_locale(
        self,
        botId: str,
        botVersion: str,
        localeId: str,
        nluIntentConfidenceThreshold: float,
        description: str = None,
        voiceSettings: "VoiceSettingsTypeDef" = None,
    ) -> CreateBotLocaleResponseTypeDef:
        """
        [Client.create_bot_locale documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_locale)
        """

    def create_bot_version(
        self,
        botId: str,
        botVersionLocaleSpecification: Dict[str, "BotVersionLocaleDetailsTypeDef"],
        description: str = None,
    ) -> CreateBotVersionResponseTypeDef:
        """
        [Client.create_bot_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_version)
        """

    def create_intent(
        self,
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
    ) -> CreateIntentResponseTypeDef:
        """
        [Client.create_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.create_intent)
        """

    def create_slot(
        self,
        slotName: str,
        slotTypeId: str,
        valueElicitationSetting: "SlotValueElicitationSettingTypeDef",
        botId: str,
        botVersion: str,
        localeId: str,
        intentId: str,
        description: str = None,
        obfuscationSetting: "ObfuscationSettingTypeDef" = None,
    ) -> CreateSlotResponseTypeDef:
        """
        [Client.create_slot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.create_slot)
        """

    def create_slot_type(
        self,
        slotTypeName: str,
        valueSelectionSetting: "SlotValueSelectionSettingTypeDef",
        botId: str,
        botVersion: str,
        localeId: str,
        description: str = None,
        slotTypeValues: List["SlotTypeValueTypeDef"] = None,
        parentSlotTypeSignature: str = None,
    ) -> CreateSlotTypeResponseTypeDef:
        """
        [Client.create_slot_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.create_slot_type)
        """

    def delete_bot(
        self, botId: str, skipResourceInUseCheck: bool = None
    ) -> DeleteBotResponseTypeDef:
        """
        [Client.delete_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot)
        """

    def delete_bot_alias(
        self, botAliasId: str, botId: str, skipResourceInUseCheck: bool = None
    ) -> DeleteBotAliasResponseTypeDef:
        """
        [Client.delete_bot_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_alias)
        """

    def delete_bot_locale(
        self, botId: str, botVersion: str, localeId: str
    ) -> DeleteBotLocaleResponseTypeDef:
        """
        [Client.delete_bot_locale documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_locale)
        """

    def delete_bot_version(
        self, botId: str, botVersion: str, skipResourceInUseCheck: bool = None
    ) -> DeleteBotVersionResponseTypeDef:
        """
        [Client.delete_bot_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_version)
        """

    def delete_intent(self, intentId: str, botId: str, botVersion: str, localeId: str) -> None:
        """
        [Client.delete_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.delete_intent)
        """

    def delete_slot(
        self, slotId: str, botId: str, botVersion: str, localeId: str, intentId: str
    ) -> None:
        """
        [Client.delete_slot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.delete_slot)
        """

    def delete_slot_type(
        self,
        slotTypeId: str,
        botId: str,
        botVersion: str,
        localeId: str,
        skipResourceInUseCheck: bool = None,
    ) -> None:
        """
        [Client.delete_slot_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.delete_slot_type)
        """

    def describe_bot(self, botId: str) -> DescribeBotResponseTypeDef:
        """
        [Client.describe_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot)
        """

    def describe_bot_alias(self, botAliasId: str, botId: str) -> DescribeBotAliasResponseTypeDef:
        """
        [Client.describe_bot_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_alias)
        """

    def describe_bot_locale(
        self, botId: str, botVersion: str, localeId: str
    ) -> DescribeBotLocaleResponseTypeDef:
        """
        [Client.describe_bot_locale documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_locale)
        """

    def describe_bot_version(
        self, botId: str, botVersion: str
    ) -> DescribeBotVersionResponseTypeDef:
        """
        [Client.describe_bot_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_version)
        """

    def describe_intent(
        self, intentId: str, botId: str, botVersion: str, localeId: str
    ) -> DescribeIntentResponseTypeDef:
        """
        [Client.describe_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.describe_intent)
        """

    def describe_slot(
        self, slotId: str, botId: str, botVersion: str, localeId: str, intentId: str
    ) -> DescribeSlotResponseTypeDef:
        """
        [Client.describe_slot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.describe_slot)
        """

    def describe_slot_type(
        self, slotTypeId: str, botId: str, botVersion: str, localeId: str
    ) -> DescribeSlotTypeResponseTypeDef:
        """
        [Client.describe_slot_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.describe_slot_type)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.generate_presigned_url)
        """

    def list_bot_aliases(
        self, botId: str, maxResults: int = None, nextToken: str = None
    ) -> ListBotAliasesResponseTypeDef:
        """
        [Client.list_bot_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_aliases)
        """

    def list_bot_locales(
        self,
        botId: str,
        botVersion: str,
        sortBy: BotLocaleSortByTypeDef = None,
        filters: List[BotLocaleFilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListBotLocalesResponseTypeDef:
        """
        [Client.list_bot_locales documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_locales)
        """

    def list_bot_versions(
        self,
        botId: str,
        sortBy: BotVersionSortByTypeDef = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListBotVersionsResponseTypeDef:
        """
        [Client.list_bot_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_versions)
        """

    def list_bots(
        self,
        sortBy: BotSortByTypeDef = None,
        filters: List[BotFilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListBotsResponseTypeDef:
        """
        [Client.list_bots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.list_bots)
        """

    def list_built_in_intents(
        self,
        localeId: str,
        sortBy: BuiltInIntentSortByTypeDef = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListBuiltInIntentsResponseTypeDef:
        """
        [Client.list_built_in_intents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.list_built_in_intents)
        """

    def list_built_in_slot_types(
        self,
        localeId: str,
        sortBy: BuiltInSlotTypeSortByTypeDef = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListBuiltInSlotTypesResponseTypeDef:
        """
        [Client.list_built_in_slot_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.list_built_in_slot_types)
        """

    def list_intents(
        self,
        botId: str,
        botVersion: str,
        localeId: str,
        sortBy: IntentSortByTypeDef = None,
        filters: List[IntentFilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListIntentsResponseTypeDef:
        """
        [Client.list_intents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.list_intents)
        """

    def list_slot_types(
        self,
        botId: str,
        botVersion: str,
        localeId: str,
        sortBy: SlotTypeSortByTypeDef = None,
        filters: List[SlotTypeFilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListSlotTypesResponseTypeDef:
        """
        [Client.list_slot_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.list_slot_types)
        """

    def list_slots(
        self,
        botId: str,
        botVersion: str,
        localeId: str,
        intentId: str,
        sortBy: SlotSortByTypeDef = None,
        filters: List[SlotFilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListSlotsResponseTypeDef:
        """
        [Client.list_slots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.list_slots)
        """

    def list_tags_for_resource(self, resourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.list_tags_for_resource)
        """

    def tag_resource(self, resourceARN: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.tag_resource)
        """

    def untag_resource(self, resourceARN: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.untag_resource)
        """

    def update_bot(
        self,
        botId: str,
        botName: str,
        roleArn: str,
        dataPrivacy: "DataPrivacyTypeDef",
        idleSessionTTLInSeconds: int,
        description: str = None,
    ) -> UpdateBotResponseTypeDef:
        """
        [Client.update_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot)
        """

    def update_bot_alias(
        self,
        botAliasId: str,
        botAliasName: str,
        botId: str,
        description: str = None,
        botVersion: str = None,
        botAliasLocaleSettings: Dict[str, "BotAliasLocaleSettingsTypeDef"] = None,
        conversationLogSettings: "ConversationLogSettingsTypeDef" = None,
        sentimentAnalysisSettings: "SentimentAnalysisSettingsTypeDef" = None,
    ) -> UpdateBotAliasResponseTypeDef:
        """
        [Client.update_bot_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot_alias)
        """

    def update_bot_locale(
        self,
        botId: str,
        botVersion: str,
        localeId: str,
        nluIntentConfidenceThreshold: float,
        description: str = None,
        voiceSettings: "VoiceSettingsTypeDef" = None,
    ) -> UpdateBotLocaleResponseTypeDef:
        """
        [Client.update_bot_locale documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot_locale)
        """

    def update_intent(
        self,
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
    ) -> UpdateIntentResponseTypeDef:
        """
        [Client.update_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.update_intent)
        """

    def update_slot(
        self,
        slotId: str,
        slotName: str,
        slotTypeId: str,
        valueElicitationSetting: "SlotValueElicitationSettingTypeDef",
        botId: str,
        botVersion: str,
        localeId: str,
        intentId: str,
        description: str = None,
        obfuscationSetting: "ObfuscationSettingTypeDef" = None,
    ) -> UpdateSlotResponseTypeDef:
        """
        [Client.update_slot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.update_slot)
        """

    def update_slot_type(
        self,
        slotTypeId: str,
        slotTypeName: str,
        valueSelectionSetting: "SlotValueSelectionSettingTypeDef",
        botId: str,
        botVersion: str,
        localeId: str,
        description: str = None,
        slotTypeValues: List["SlotTypeValueTypeDef"] = None,
        parentSlotTypeSignature: str = None,
    ) -> UpdateSlotTypeResponseTypeDef:
        """
        [Client.update_slot_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-models.html#LexModelsV2.Client.update_slot_type)
        """
