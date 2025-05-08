"""
Type annotations for lex-models service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_lex_models.client import LexModelBuildingServiceClient

    session = Session()
    client: LexModelBuildingServiceClient = session.client("lex-models")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

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
    CreateBotVersionRequestTypeDef,
    CreateBotVersionResponseTypeDef,
    CreateIntentVersionRequestTypeDef,
    CreateIntentVersionResponseTypeDef,
    CreateSlotTypeVersionRequestTypeDef,
    CreateSlotTypeVersionResponseTypeDef,
    DeleteBotAliasRequestTypeDef,
    DeleteBotChannelAssociationRequestTypeDef,
    DeleteBotRequestTypeDef,
    DeleteBotVersionRequestTypeDef,
    DeleteIntentRequestTypeDef,
    DeleteIntentVersionRequestTypeDef,
    DeleteSlotTypeRequestTypeDef,
    DeleteSlotTypeVersionRequestTypeDef,
    DeleteUtterancesRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetBotAliasesRequestTypeDef,
    GetBotAliasesResponseTypeDef,
    GetBotAliasRequestTypeDef,
    GetBotAliasResponseTypeDef,
    GetBotChannelAssociationRequestTypeDef,
    GetBotChannelAssociationResponseTypeDef,
    GetBotChannelAssociationsRequestTypeDef,
    GetBotChannelAssociationsResponseTypeDef,
    GetBotRequestTypeDef,
    GetBotResponseTypeDef,
    GetBotsRequestTypeDef,
    GetBotsResponseTypeDef,
    GetBotVersionsRequestTypeDef,
    GetBotVersionsResponseTypeDef,
    GetBuiltinIntentRequestTypeDef,
    GetBuiltinIntentResponseTypeDef,
    GetBuiltinIntentsRequestTypeDef,
    GetBuiltinIntentsResponseTypeDef,
    GetBuiltinSlotTypesRequestTypeDef,
    GetBuiltinSlotTypesResponseTypeDef,
    GetExportRequestTypeDef,
    GetExportResponseTypeDef,
    GetImportRequestTypeDef,
    GetImportResponseTypeDef,
    GetIntentRequestTypeDef,
    GetIntentResponseTypeDef,
    GetIntentsRequestTypeDef,
    GetIntentsResponseTypeDef,
    GetIntentVersionsRequestTypeDef,
    GetIntentVersionsResponseTypeDef,
    GetMigrationRequestTypeDef,
    GetMigrationResponseTypeDef,
    GetMigrationsRequestTypeDef,
    GetMigrationsResponseTypeDef,
    GetSlotTypeRequestTypeDef,
    GetSlotTypeResponseTypeDef,
    GetSlotTypesRequestTypeDef,
    GetSlotTypesResponseTypeDef,
    GetSlotTypeVersionsRequestTypeDef,
    GetSlotTypeVersionsResponseTypeDef,
    GetUtterancesViewRequestTypeDef,
    GetUtterancesViewResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutBotAliasRequestTypeDef,
    PutBotAliasResponseTypeDef,
    PutBotRequestTypeDef,
    PutBotResponseTypeDef,
    PutIntentRequestTypeDef,
    PutIntentResponseTypeDef,
    PutSlotTypeRequestTypeDef,
    PutSlotTypeResponseTypeDef,
    StartImportRequestTypeDef,
    StartImportResponseTypeDef,
    StartMigrationRequestTypeDef,
    StartMigrationResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("LexModelBuildingServiceClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LexModelBuildingServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#generate_presigned_url)
        """

    def create_bot_version(
        self, **kwargs: Unpack[CreateBotVersionRequestTypeDef]
    ) -> CreateBotVersionResponseTypeDef:
        """
        Creates a new version of the bot based on the <code>$LATEST</code> version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/create_bot_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#create_bot_version)
        """

    def create_intent_version(
        self, **kwargs: Unpack[CreateIntentVersionRequestTypeDef]
    ) -> CreateIntentVersionResponseTypeDef:
        """
        Creates a new version of an intent based on the <code>$LATEST</code> version of
        the intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/create_intent_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#create_intent_version)
        """

    def create_slot_type_version(
        self, **kwargs: Unpack[CreateSlotTypeVersionRequestTypeDef]
    ) -> CreateSlotTypeVersionResponseTypeDef:
        """
        Creates a new version of a slot type based on the <code>$LATEST</code> version
        of the specified slot type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/create_slot_type_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#create_slot_type_version)
        """

    def delete_bot(self, **kwargs: Unpack[DeleteBotRequestTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Deletes all versions of the bot, including the <code>$LATEST</code> version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/delete_bot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#delete_bot)
        """

    def delete_bot_alias(
        self, **kwargs: Unpack[DeleteBotAliasRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an alias for the specified bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/delete_bot_alias.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#delete_bot_alias)
        """

    def delete_bot_channel_association(
        self, **kwargs: Unpack[DeleteBotChannelAssociationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the association between an Amazon Lex bot and a messaging platform.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/delete_bot_channel_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#delete_bot_channel_association)
        """

    def delete_bot_version(
        self, **kwargs: Unpack[DeleteBotVersionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a specific version of a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/delete_bot_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#delete_bot_version)
        """

    def delete_intent(
        self, **kwargs: Unpack[DeleteIntentRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes all versions of the intent, including the <code>$LATEST</code> version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/delete_intent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#delete_intent)
        """

    def delete_intent_version(
        self, **kwargs: Unpack[DeleteIntentVersionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a specific version of an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/delete_intent_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#delete_intent_version)
        """

    def delete_slot_type(
        self, **kwargs: Unpack[DeleteSlotTypeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes all versions of the slot type, including the <code>$LATEST</code>
        version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/delete_slot_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#delete_slot_type)
        """

    def delete_slot_type_version(
        self, **kwargs: Unpack[DeleteSlotTypeVersionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a specific version of a slot type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/delete_slot_type_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#delete_slot_type_version)
        """

    def delete_utterances(
        self, **kwargs: Unpack[DeleteUtterancesRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes stored utterances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/delete_utterances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#delete_utterances)
        """

    def get_bot(self, **kwargs: Unpack[GetBotRequestTypeDef]) -> GetBotResponseTypeDef:
        """
        Returns metadata information for a specific bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_bot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_bot)
        """

    def get_bot_alias(
        self, **kwargs: Unpack[GetBotAliasRequestTypeDef]
    ) -> GetBotAliasResponseTypeDef:
        """
        Returns information about an Amazon Lex bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_bot_alias.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_bot_alias)
        """

    def get_bot_aliases(
        self, **kwargs: Unpack[GetBotAliasesRequestTypeDef]
    ) -> GetBotAliasesResponseTypeDef:
        """
        Returns a list of aliases for a specified Amazon Lex bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_bot_aliases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_bot_aliases)
        """

    def get_bot_channel_association(
        self, **kwargs: Unpack[GetBotChannelAssociationRequestTypeDef]
    ) -> GetBotChannelAssociationResponseTypeDef:
        """
        Returns information about the association between an Amazon Lex bot and a
        messaging platform.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_bot_channel_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_bot_channel_association)
        """

    def get_bot_channel_associations(
        self, **kwargs: Unpack[GetBotChannelAssociationsRequestTypeDef]
    ) -> GetBotChannelAssociationsResponseTypeDef:
        """
        Returns a list of all of the channels associated with the specified bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_bot_channel_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_bot_channel_associations)
        """

    def get_bot_versions(
        self, **kwargs: Unpack[GetBotVersionsRequestTypeDef]
    ) -> GetBotVersionsResponseTypeDef:
        """
        Gets information about all of the versions of a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_bot_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_bot_versions)
        """

    def get_bots(self, **kwargs: Unpack[GetBotsRequestTypeDef]) -> GetBotsResponseTypeDef:
        """
        Returns bot information as follows:.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_bots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_bots)
        """

    def get_builtin_intent(
        self, **kwargs: Unpack[GetBuiltinIntentRequestTypeDef]
    ) -> GetBuiltinIntentResponseTypeDef:
        """
        Returns information about a built-in intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_builtin_intent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_builtin_intent)
        """

    def get_builtin_intents(
        self, **kwargs: Unpack[GetBuiltinIntentsRequestTypeDef]
    ) -> GetBuiltinIntentsResponseTypeDef:
        """
        Gets a list of built-in intents that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_builtin_intents.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_builtin_intents)
        """

    def get_builtin_slot_types(
        self, **kwargs: Unpack[GetBuiltinSlotTypesRequestTypeDef]
    ) -> GetBuiltinSlotTypesResponseTypeDef:
        """
        Gets a list of built-in slot types that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_builtin_slot_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_builtin_slot_types)
        """

    def get_export(self, **kwargs: Unpack[GetExportRequestTypeDef]) -> GetExportResponseTypeDef:
        """
        Exports the contents of a Amazon Lex resource in a specified format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_export.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_export)
        """

    def get_import(self, **kwargs: Unpack[GetImportRequestTypeDef]) -> GetImportResponseTypeDef:
        """
        Gets information about an import job started with the <code>StartImport</code>
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_import.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_import)
        """

    def get_intent(self, **kwargs: Unpack[GetIntentRequestTypeDef]) -> GetIntentResponseTypeDef:
        """
        Returns information about an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_intent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_intent)
        """

    def get_intent_versions(
        self, **kwargs: Unpack[GetIntentVersionsRequestTypeDef]
    ) -> GetIntentVersionsResponseTypeDef:
        """
        Gets information about all of the versions of an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_intent_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_intent_versions)
        """

    def get_intents(self, **kwargs: Unpack[GetIntentsRequestTypeDef]) -> GetIntentsResponseTypeDef:
        """
        Returns intent information as follows:.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_intents.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_intents)
        """

    def get_migration(
        self, **kwargs: Unpack[GetMigrationRequestTypeDef]
    ) -> GetMigrationResponseTypeDef:
        """
        Provides details about an ongoing or complete migration from an Amazon Lex V1
        bot to an Amazon Lex V2 bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_migration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_migration)
        """

    def get_migrations(
        self, **kwargs: Unpack[GetMigrationsRequestTypeDef]
    ) -> GetMigrationsResponseTypeDef:
        """
        Gets a list of migrations between Amazon Lex V1 and Amazon Lex V2.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_migrations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_migrations)
        """

    def get_slot_type(
        self, **kwargs: Unpack[GetSlotTypeRequestTypeDef]
    ) -> GetSlotTypeResponseTypeDef:
        """
        Returns information about a specific version of a slot type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_slot_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_slot_type)
        """

    def get_slot_type_versions(
        self, **kwargs: Unpack[GetSlotTypeVersionsRequestTypeDef]
    ) -> GetSlotTypeVersionsResponseTypeDef:
        """
        Gets information about all versions of a slot type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_slot_type_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_slot_type_versions)
        """

    def get_slot_types(
        self, **kwargs: Unpack[GetSlotTypesRequestTypeDef]
    ) -> GetSlotTypesResponseTypeDef:
        """
        Returns slot type information as follows:.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_slot_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_slot_types)
        """

    def get_utterances_view(
        self, **kwargs: Unpack[GetUtterancesViewRequestTypeDef]
    ) -> GetUtterancesViewResponseTypeDef:
        """
        Use the <code>GetUtterancesView</code> operation to get information about the
        utterances that your users have made to your bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_utterances_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_utterances_view)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Gets a list of tags associated with the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#list_tags_for_resource)
        """

    def put_bot(self, **kwargs: Unpack[PutBotRequestTypeDef]) -> PutBotResponseTypeDef:
        """
        Creates an Amazon Lex conversational bot or replaces an existing bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/put_bot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#put_bot)
        """

    def put_bot_alias(
        self, **kwargs: Unpack[PutBotAliasRequestTypeDef]
    ) -> PutBotAliasResponseTypeDef:
        """
        Creates an alias for the specified version of the bot or replaces an alias for
        the specified bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/put_bot_alias.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#put_bot_alias)
        """

    def put_intent(self, **kwargs: Unpack[PutIntentRequestTypeDef]) -> PutIntentResponseTypeDef:
        """
        Creates an intent or replaces an existing intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/put_intent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#put_intent)
        """

    def put_slot_type(
        self, **kwargs: Unpack[PutSlotTypeRequestTypeDef]
    ) -> PutSlotTypeResponseTypeDef:
        """
        Creates a custom slot type or replaces an existing custom slot type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/put_slot_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#put_slot_type)
        """

    def start_import(
        self, **kwargs: Unpack[StartImportRequestTypeDef]
    ) -> StartImportResponseTypeDef:
        """
        Starts a job to import a resource to Amazon Lex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/start_import.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#start_import)
        """

    def start_migration(
        self, **kwargs: Unpack[StartMigrationRequestTypeDef]
    ) -> StartMigrationResponseTypeDef:
        """
        Starts migrating a bot from Amazon Lex V1 to Amazon Lex V2.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/start_migration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#start_migration)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from a bot, bot alias or bot channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#untag_resource)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_bot_aliases"]
    ) -> GetBotAliasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_bot_channel_associations"]
    ) -> GetBotChannelAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_bot_versions"]
    ) -> GetBotVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_bots"]
    ) -> GetBotsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_builtin_intents"]
    ) -> GetBuiltinIntentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_builtin_slot_types"]
    ) -> GetBuiltinSlotTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_intent_versions"]
    ) -> GetIntentVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_intents"]
    ) -> GetIntentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_slot_type_versions"]
    ) -> GetSlotTypeVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_slot_types"]
    ) -> GetSlotTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client/#get_paginator)
        """
