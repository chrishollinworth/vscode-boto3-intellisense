"""
Type annotations for lex-models service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_lex_models import LexModelBuildingServiceClient

    client: LexModelBuildingServiceClient = boto3.client("lex-models")
    ```
"""

import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import (
    ExportTypeType,
    LocaleType,
    MergeStrategyType,
    MigrationSortAttributeType,
    MigrationStatusType,
    MigrationStrategyType,
    ProcessBehaviorType,
    ResourceTypeType,
    SlotValueSelectionStrategyType,
    SortOrderType,
    StatusTypeType,
)
from .paginator import (
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
from .type_defs import (
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
    GetMigrationResponseTypeDef,
    GetMigrationsResponseTypeDef,
    GetSlotTypeResponseTypeDef,
    GetSlotTypesResponseTypeDef,
    GetSlotTypeVersionsResponseTypeDef,
    GetUtterancesViewResponseTypeDef,
    InputContextTypeDef,
    IntentTypeDef,
    KendraConfigurationTypeDef,
    ListTagsForResourceResponseTypeDef,
    OutputContextTypeDef,
    PromptTypeDef,
    PutBotAliasResponseTypeDef,
    PutBotResponseTypeDef,
    PutIntentResponseTypeDef,
    PutSlotTypeResponseTypeDef,
    SlotTypeConfigurationTypeDef,
    SlotTypeDef,
    StartImportResponseTypeDef,
    StartMigrationResponseTypeDef,
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
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    PreconditionFailedException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]

class LexModelBuildingServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LexModelBuildingServiceClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#close)
        """

    def create_bot_version(
        self, *, name: str, checksum: str = None
    ) -> CreateBotVersionResponseTypeDef:
        """
        Creates a new version of the bot based on the `$LATEST` version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.create_bot_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#create_bot_version)
        """

    def create_intent_version(
        self, *, name: str, checksum: str = None
    ) -> CreateIntentVersionResponseTypeDef:
        """
        Creates a new version of an intent based on the `$LATEST` version of the intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.create_intent_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#create_intent_version)
        """

    def create_slot_type_version(
        self, *, name: str, checksum: str = None
    ) -> CreateSlotTypeVersionResponseTypeDef:
        """
        Creates a new version of a slot type based on the `$LATEST` version of the
        specified slot type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.create_slot_type_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#create_slot_type_version)
        """

    def delete_bot(self, *, name: str) -> None:
        """
        Deletes all versions of the bot, including the `$LATEST` version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#delete_bot)
        """

    def delete_bot_alias(self, *, name: str, botName: str) -> None:
        """
        Deletes an alias for the specified bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#delete_bot_alias)
        """

    def delete_bot_channel_association(self, *, name: str, botName: str, botAlias: str) -> None:
        """
        Deletes the association between an Amazon Lex bot and a messaging platform.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot_channel_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#delete_bot_channel_association)
        """

    def delete_bot_version(self, *, name: str, version: str) -> None:
        """
        Deletes a specific version of a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#delete_bot_version)
        """

    def delete_intent(self, *, name: str) -> None:
        """
        Deletes all versions of the intent, including the `$LATEST` version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.delete_intent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#delete_intent)
        """

    def delete_intent_version(self, *, name: str, version: str) -> None:
        """
        Deletes a specific version of an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.delete_intent_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#delete_intent_version)
        """

    def delete_slot_type(self, *, name: str) -> None:
        """
        Deletes all versions of the slot type, including the `$LATEST` version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.delete_slot_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#delete_slot_type)
        """

    def delete_slot_type_version(self, *, name: str, version: str) -> None:
        """
        Deletes a specific version of a slot type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.delete_slot_type_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#delete_slot_type_version)
        """

    def delete_utterances(self, *, botName: str, userId: str) -> None:
        """
        Deletes stored utterances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.delete_utterances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#delete_utterances)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#generate_presigned_url)
        """

    def get_bot(self, *, name: str, versionOrAlias: str) -> GetBotResponseTypeDef:
        """
        Returns metadata information for a specific bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_bot)
        """

    def get_bot_alias(self, *, name: str, botName: str) -> GetBotAliasResponseTypeDef:
        """
        Returns information about an Amazon Lex bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_bot_alias)
        """

    def get_bot_aliases(
        self,
        *,
        botName: str,
        nextToken: str = None,
        maxResults: int = None,
        nameContains: str = None
    ) -> GetBotAliasesResponseTypeDef:
        """
        Returns a list of aliases for a specified Amazon Lex bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_bot_aliases)
        """

    def get_bot_channel_association(
        self, *, name: str, botName: str, botAlias: str
    ) -> GetBotChannelAssociationResponseTypeDef:
        """
        Returns information about the association between an Amazon Lex bot and a
        messaging platform.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_channel_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_bot_channel_association)
        """

    def get_bot_channel_associations(
        self,
        *,
        botName: str,
        botAlias: str,
        nextToken: str = None,
        maxResults: int = None,
        nameContains: str = None
    ) -> GetBotChannelAssociationsResponseTypeDef:
        """
        Returns a list of all of the channels associated with the specified bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_channel_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_bot_channel_associations)
        """

    def get_bot_versions(
        self, *, name: str, nextToken: str = None, maxResults: int = None
    ) -> GetBotVersionsResponseTypeDef:
        """
        Gets information about all of the versions of a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_bot_versions)
        """

    def get_bots(
        self, *, nextToken: str = None, maxResults: int = None, nameContains: str = None
    ) -> GetBotsResponseTypeDef:
        """
        Returns bot information as follows * If you provide the `nameContains` field,
        the response includes information for the `$LATEST` version of all bots whose
        name contains the specified string.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_bots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_bots)
        """

    def get_builtin_intent(self, *, signature: str) -> GetBuiltinIntentResponseTypeDef:
        """
        Returns information about a built-in intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_builtin_intent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_builtin_intent)
        """

    def get_builtin_intents(
        self,
        *,
        locale: LocaleType = None,
        signatureContains: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetBuiltinIntentsResponseTypeDef:
        """
        Gets a list of built-in intents that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_builtin_intents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_builtin_intents)
        """

    def get_builtin_slot_types(
        self,
        *,
        locale: LocaleType = None,
        signatureContains: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetBuiltinSlotTypesResponseTypeDef:
        """
        Gets a list of built-in slot types that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_builtin_slot_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_builtin_slot_types)
        """

    def get_export(
        self, *, name: str, version: str, resourceType: ResourceTypeType, exportType: ExportTypeType
    ) -> GetExportResponseTypeDef:
        """
        Exports the contents of a Amazon Lex resource in a specified format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_export)
        """

    def get_import(self, *, importId: str) -> GetImportResponseTypeDef:
        """
        Gets information about an import job started with the `StartImport` operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_import)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_import)
        """

    def get_intent(self, *, name: str, version: str) -> GetIntentResponseTypeDef:
        """
        Returns information about an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_intent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_intent)
        """

    def get_intent_versions(
        self, *, name: str, nextToken: str = None, maxResults: int = None
    ) -> GetIntentVersionsResponseTypeDef:
        """
        Gets information about all of the versions of an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_intent_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_intent_versions)
        """

    def get_intents(
        self, *, nextToken: str = None, maxResults: int = None, nameContains: str = None
    ) -> GetIntentsResponseTypeDef:
        """
        Returns intent information as follows * If you specify the `nameContains` field,
        returns the `$LATEST` version of all intents that contain the specified string.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_intents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_intents)
        """

    def get_migration(self, *, migrationId: str) -> GetMigrationResponseTypeDef:
        """
        Provides details about an ongoing or complete migration from an Amazon Lex V1
        bot to an Amazon Lex V2 bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_migration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_migration)
        """

    def get_migrations(
        self,
        *,
        sortByAttribute: MigrationSortAttributeType = None,
        sortByOrder: SortOrderType = None,
        v1BotNameContains: str = None,
        migrationStatusEquals: MigrationStatusType = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> GetMigrationsResponseTypeDef:
        """
        Gets a list of migrations between Amazon Lex V1 and Amazon Lex V2.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_migrations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_migrations)
        """

    def get_slot_type(self, *, name: str, version: str) -> GetSlotTypeResponseTypeDef:
        """
        Returns information about a specific version of a slot type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_slot_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_slot_type)
        """

    def get_slot_type_versions(
        self, *, name: str, nextToken: str = None, maxResults: int = None
    ) -> GetSlotTypeVersionsResponseTypeDef:
        """
        Gets information about all versions of a slot type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_slot_type_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_slot_type_versions)
        """

    def get_slot_types(
        self, *, nextToken: str = None, maxResults: int = None, nameContains: str = None
    ) -> GetSlotTypesResponseTypeDef:
        """
        Returns slot type information as follows * If you specify the `nameContains`
        field, returns the `$LATEST` version of all slot types that contain the
        specified string.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_slot_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_slot_types)
        """

    def get_utterances_view(
        self, *, botName: str, botVersions: List[str], statusType: StatusTypeType
    ) -> GetUtterancesViewResponseTypeDef:
        """
        Use the `GetUtterancesView` operation to get information about the utterances
        that your users have made to your bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.get_utterances_view)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_utterances_view)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Gets a list of tags associated with the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#list_tags_for_resource)
        """

    def put_bot(
        self,
        *,
        name: str,
        locale: LocaleType,
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
        processBehavior: ProcessBehaviorType = None,
        detectSentiment: bool = None,
        createVersion: bool = None,
        tags: List["TagTypeDef"] = None
    ) -> PutBotResponseTypeDef:
        """
        Creates an Amazon Lex conversational bot or replaces an existing bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.put_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#put_bot)
        """

    def put_bot_alias(
        self,
        *,
        name: str,
        botVersion: str,
        botName: str,
        description: str = None,
        checksum: str = None,
        conversationLogs: "ConversationLogsRequestTypeDef" = None,
        tags: List["TagTypeDef"] = None
    ) -> PutBotAliasResponseTypeDef:
        """
        Creates an alias for the specified version of the bot or replaces an alias for
        the specified bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.put_bot_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#put_bot_alias)
        """

    def put_intent(
        self,
        *,
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
        inputContexts: List["InputContextTypeDef"] = None,
        outputContexts: List["OutputContextTypeDef"] = None
    ) -> PutIntentResponseTypeDef:
        """
        Creates an intent or replaces an existing intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.put_intent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#put_intent)
        """

    def put_slot_type(
        self,
        *,
        name: str,
        description: str = None,
        enumerationValues: List["EnumerationValueTypeDef"] = None,
        checksum: str = None,
        valueSelectionStrategy: SlotValueSelectionStrategyType = None,
        createVersion: bool = None,
        parentSlotTypeSignature: str = None,
        slotTypeConfigurations: List["SlotTypeConfigurationTypeDef"] = None
    ) -> PutSlotTypeResponseTypeDef:
        """
        Creates a custom slot type or replaces an existing custom slot type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.put_slot_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#put_slot_type)
        """

    def start_import(
        self,
        *,
        payload: Union[bytes, IO[bytes], StreamingBody],
        resourceType: ResourceTypeType,
        mergeStrategy: MergeStrategyType,
        tags: List["TagTypeDef"] = None
    ) -> StartImportResponseTypeDef:
        """
        Starts a job to import a resource to Amazon Lex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.start_import)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#start_import)
        """

    def start_migration(
        self,
        *,
        v1BotName: str,
        v1BotVersion: str,
        v2BotName: str,
        v2BotRole: str,
        migrationStrategy: MigrationStrategyType
    ) -> StartMigrationResponseTypeDef:
        """
        Starts migrating a bot from Amazon Lex V1 to Amazon Lex V2.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.start_migration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#start_migration)
        """

    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from a bot, bot alias or bot channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#untag_resource)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_bot_aliases"]) -> GetBotAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotAliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbotaliasespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_bot_channel_associations"]
    ) -> GetBotChannelAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotChannelAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbotchannelassociationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_bot_versions"]) -> GetBotVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbotversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_bots"]) -> GetBotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbotspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_builtin_intents"]
    ) -> GetBuiltinIntentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinIntents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbuiltinintentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_builtin_slot_types"]
    ) -> GetBuiltinSlotTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinSlotTypes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbuiltinslottypespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_intent_versions"]
    ) -> GetIntentVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntentVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getintentversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_intents"]) -> GetIntentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getintentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_slot_type_versions"]
    ) -> GetSlotTypeVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypeVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getslottypeversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_slot_types"]) -> GetSlotTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getslottypespaginator)
        """
