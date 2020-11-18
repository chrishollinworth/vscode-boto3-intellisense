# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for lex-models service client

Usage::

    ```python
    import boto3
    from mypy_boto3_lex_models import LexModelBuildingServiceClient

    client: LexModelBuildingServiceClient = boto3.client("lex-models")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import ClientMeta

from mypy_boto3_lex_models.paginator import (
    GetBotAliasesPaginator,
    GetBotChannelAssociationsPaginator,
    GetBotsPaginator,
    GetBotVersionsPaginator,
    GetBuiltinIntentsPaginator,
    GetBuiltinSlotTypesPaginator,
    GetIntentsPaginator,
    GetIntentVersionsPaginator,
    GetSlotTypesPaginator,
    GetSlotTypeVersionsPaginator,
)
from mypy_boto3_lex_models.type_defs import (
    CodeHookTypeDef,
    ConversationLogsRequestTypeDef,
    CreateBotVersionResponseTypeDef,
    CreateIntentVersionResponseTypeDef,
    CreateSlotTypeVersionResponseTypeDef,
    EnumerationValueTypeDef,
    FollowUpPromptTypeDef,
    FulfillmentActivityTypeDef,
    GetBotAliasesResponseTypeDef,
    GetBotAliasResponseTypeDef,
    GetBotChannelAssociationResponseTypeDef,
    GetBotChannelAssociationsResponseTypeDef,
    GetBotResponseTypeDef,
    GetBotsResponseTypeDef,
    GetBotVersionsResponseTypeDef,
    GetBuiltinIntentResponseTypeDef,
    GetBuiltinIntentsResponseTypeDef,
    GetBuiltinSlotTypesResponseTypeDef,
    GetExportResponseTypeDef,
    GetImportResponseTypeDef,
    GetIntentResponseTypeDef,
    GetIntentsResponseTypeDef,
    GetIntentVersionsResponseTypeDef,
    GetSlotTypeResponseTypeDef,
    GetSlotTypesResponseTypeDef,
    GetSlotTypeVersionsResponseTypeDef,
    GetUtterancesViewResponseTypeDef,
    IntentTypeDef,
    KendraConfigurationTypeDef,
    ListTagsForResourceResponseTypeDef,
    PromptTypeDef,
    PutBotAliasResponseTypeDef,
    PutBotResponseTypeDef,
    PutIntentResponseTypeDef,
    PutSlotTypeResponseTypeDef,
    SlotTypeConfigurationTypeDef,
    SlotTypeDef,
    StartImportResponseTypeDef,
    StatementTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("LexModelBuildingServiceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    PreconditionFailedException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]


class LexModelBuildingServiceClient:
    """
    [LexModelBuildingService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.can_paginate)
        """

    def create_bot_version(
        self, name: str, checksum: str = None
    ) -> CreateBotVersionResponseTypeDef:
        """
        [Client.create_bot_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.create_bot_version)
        """

    def create_intent_version(
        self, name: str, checksum: str = None
    ) -> CreateIntentVersionResponseTypeDef:
        """
        [Client.create_intent_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.create_intent_version)
        """

    def create_slot_type_version(
        self, name: str, checksum: str = None
    ) -> CreateSlotTypeVersionResponseTypeDef:
        """
        [Client.create_slot_type_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.create_slot_type_version)
        """

    def delete_bot(self, name: str) -> None:
        """
        [Client.delete_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot)
        """

    def delete_bot_alias(self, name: str, botName: str) -> None:
        """
        [Client.delete_bot_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot_alias)
        """

    def delete_bot_channel_association(self, name: str, botName: str, botAlias: str) -> None:
        """
        [Client.delete_bot_channel_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot_channel_association)
        """

    def delete_bot_version(self, name: str, version: str) -> None:
        """
        [Client.delete_bot_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot_version)
        """

    def delete_intent(self, name: str) -> None:
        """
        [Client.delete_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.delete_intent)
        """

    def delete_intent_version(self, name: str, version: str) -> None:
        """
        [Client.delete_intent_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.delete_intent_version)
        """

    def delete_slot_type(self, name: str) -> None:
        """
        [Client.delete_slot_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.delete_slot_type)
        """

    def delete_slot_type_version(self, name: str, version: str) -> None:
        """
        [Client.delete_slot_type_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.delete_slot_type_version)
        """

    def delete_utterances(self, botName: str, userId: str) -> None:
        """
        [Client.delete_utterances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.delete_utterances)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.generate_presigned_url)
        """

    def get_bot(self, name: str, versionOrAlias: str) -> GetBotResponseTypeDef:
        """
        [Client.get_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot)
        """

    def get_bot_alias(self, name: str, botName: str) -> GetBotAliasResponseTypeDef:
        """
        [Client.get_bot_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_alias)
        """

    def get_bot_aliases(
        self, botName: str, nextToken: str = None, maxResults: int = None, nameContains: str = None
    ) -> GetBotAliasesResponseTypeDef:
        """
        [Client.get_bot_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_aliases)
        """

    def get_bot_channel_association(
        self, name: str, botName: str, botAlias: str
    ) -> GetBotChannelAssociationResponseTypeDef:
        """
        [Client.get_bot_channel_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_channel_association)
        """

    def get_bot_channel_associations(
        self,
        botName: str,
        botAlias: str,
        nextToken: str = None,
        maxResults: int = None,
        nameContains: str = None,
    ) -> GetBotChannelAssociationsResponseTypeDef:
        """
        [Client.get_bot_channel_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_channel_associations)
        """

    def get_bot_versions(
        self, name: str, nextToken: str = None, maxResults: int = None
    ) -> GetBotVersionsResponseTypeDef:
        """
        [Client.get_bot_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_versions)
        """

    def get_bots(
        self, nextToken: str = None, maxResults: int = None, nameContains: str = None
    ) -> GetBotsResponseTypeDef:
        """
        [Client.get_bots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.get_bots)
        """

    def get_builtin_intent(self, signature: str) -> GetBuiltinIntentResponseTypeDef:
        """
        [Client.get_builtin_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.get_builtin_intent)
        """

    def get_builtin_intents(
        self,
        locale: Literal[
            "de-DE", "en-AU", "en-GB", "en-US", "es-ES", "es-US", "fr-FR", "fr-CA", "it-IT"
        ] = None,
        signatureContains: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> GetBuiltinIntentsResponseTypeDef:
        """
        [Client.get_builtin_intents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.get_builtin_intents)
        """

    def get_builtin_slot_types(
        self,
        locale: Literal[
            "de-DE", "en-AU", "en-GB", "en-US", "es-ES", "es-US", "fr-FR", "fr-CA", "it-IT"
        ] = None,
        signatureContains: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> GetBuiltinSlotTypesResponseTypeDef:
        """
        [Client.get_builtin_slot_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.get_builtin_slot_types)
        """

    def get_export(
        self,
        name: str,
        version: str,
        resourceType: Literal["BOT", "INTENT", "SLOT_TYPE"],
        exportType: Literal["ALEXA_SKILLS_KIT", "LEX"],
    ) -> GetExportResponseTypeDef:
        """
        [Client.get_export documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.get_export)
        """

    def get_import(self, importId: str) -> GetImportResponseTypeDef:
        """
        [Client.get_import documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.get_import)
        """

    def get_intent(self, name: str, version: str) -> GetIntentResponseTypeDef:
        """
        [Client.get_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.get_intent)
        """

    def get_intent_versions(
        self, name: str, nextToken: str = None, maxResults: int = None
    ) -> GetIntentVersionsResponseTypeDef:
        """
        [Client.get_intent_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.get_intent_versions)
        """

    def get_intents(
        self, nextToken: str = None, maxResults: int = None, nameContains: str = None
    ) -> GetIntentsResponseTypeDef:
        """
        [Client.get_intents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.get_intents)
        """

    def get_slot_type(self, name: str, version: str) -> GetSlotTypeResponseTypeDef:
        """
        [Client.get_slot_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.get_slot_type)
        """

    def get_slot_type_versions(
        self, name: str, nextToken: str = None, maxResults: int = None
    ) -> GetSlotTypeVersionsResponseTypeDef:
        """
        [Client.get_slot_type_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.get_slot_type_versions)
        """

    def get_slot_types(
        self, nextToken: str = None, maxResults: int = None, nameContains: str = None
    ) -> GetSlotTypesResponseTypeDef:
        """
        [Client.get_slot_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.get_slot_types)
        """

    def get_utterances_view(
        self, botName: str, botVersions: List[str], statusType: Literal["Detected", "Missed"]
    ) -> GetUtterancesViewResponseTypeDef:
        """
        [Client.get_utterances_view documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.get_utterances_view)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.list_tags_for_resource)
        """

    def put_bot(
        self,
        name: str,
        locale: Literal[
            "de-DE", "en-AU", "en-GB", "en-US", "es-ES", "es-US", "fr-FR", "fr-CA", "it-IT"
        ],
        childDirected: bool,
        description: str = None,
        intents: List["IntentTypeDef"] = None,
        enableModelImprovements: bool = None,
        nluIntentConfidenceThreshold: float = None,
        clarificationPrompt: "PromptTypeDef" = None,
        abortStatement: "StatementTypeDef" = None,
        idleSessionTTLInSeconds: int = None,
        voiceId: str = None,
        checksum: str = None,
        processBehavior: Literal["SAVE", "BUILD"] = None,
        detectSentiment: bool = None,
        createVersion: bool = None,
        tags: List["TagTypeDef"] = None,
    ) -> PutBotResponseTypeDef:
        """
        [Client.put_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.put_bot)
        """

    def put_bot_alias(
        self,
        name: str,
        botVersion: str,
        botName: str,
        description: str = None,
        checksum: str = None,
        conversationLogs: ConversationLogsRequestTypeDef = None,
        tags: List["TagTypeDef"] = None,
    ) -> PutBotAliasResponseTypeDef:
        """
        [Client.put_bot_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.put_bot_alias)
        """

    def put_intent(
        self,
        name: str,
        description: str = None,
        slots: List["SlotTypeDef"] = None,
        sampleUtterances: List[str] = None,
        confirmationPrompt: "PromptTypeDef" = None,
        rejectionStatement: "StatementTypeDef" = None,
        followUpPrompt: "FollowUpPromptTypeDef" = None,
        conclusionStatement: "StatementTypeDef" = None,
        dialogCodeHook: "CodeHookTypeDef" = None,
        fulfillmentActivity: "FulfillmentActivityTypeDef" = None,
        parentIntentSignature: str = None,
        checksum: str = None,
        createVersion: bool = None,
        kendraConfiguration: "KendraConfigurationTypeDef" = None,
    ) -> PutIntentResponseTypeDef:
        """
        [Client.put_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.put_intent)
        """

    def put_slot_type(
        self,
        name: str,
        description: str = None,
        enumerationValues: List["EnumerationValueTypeDef"] = None,
        checksum: str = None,
        valueSelectionStrategy: Literal["ORIGINAL_VALUE", "TOP_RESOLUTION"] = None,
        createVersion: bool = None,
        parentSlotTypeSignature: str = None,
        slotTypeConfigurations: List["SlotTypeConfigurationTypeDef"] = None,
    ) -> PutSlotTypeResponseTypeDef:
        """
        [Client.put_slot_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.put_slot_type)
        """

    def start_import(
        self,
        payload: Union[bytes, IO[bytes]],
        resourceType: Literal["BOT", "INTENT", "SLOT_TYPE"],
        mergeStrategy: Literal["OVERWRITE_LATEST", "FAIL_ON_CONFLICT"],
        tags: List["TagTypeDef"] = None,
    ) -> StartImportResponseTypeDef:
        """
        [Client.start_import documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.start_import)
        """

    def tag_resource(self, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Client.untag_resource)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_bot_aliases"]) -> GetBotAliasesPaginator:
        """
        [Paginator.GetBotAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotAliases)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_bot_channel_associations"]
    ) -> GetBotChannelAssociationsPaginator:
        """
        [Paginator.GetBotChannelAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotChannelAssociations)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_bot_versions"]) -> GetBotVersionsPaginator:
        """
        [Paginator.GetBotVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotVersions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_bots"]) -> GetBotsPaginator:
        """
        [Paginator.GetBots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_builtin_intents"]
    ) -> GetBuiltinIntentsPaginator:
        """
        [Paginator.GetBuiltinIntents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinIntents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_builtin_slot_types"]
    ) -> GetBuiltinSlotTypesPaginator:
        """
        [Paginator.GetBuiltinSlotTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinSlotTypes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_intent_versions"]
    ) -> GetIntentVersionsPaginator:
        """
        [Paginator.GetIntentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntentVersions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_intents"]) -> GetIntentsPaginator:
        """
        [Paginator.GetIntents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_slot_type_versions"]
    ) -> GetSlotTypeVersionsPaginator:
        """
        [Paginator.GetSlotTypeVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypeVersions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_slot_types"]) -> GetSlotTypesPaginator:
        """
        [Paginator.GetSlotTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypes)
        """
