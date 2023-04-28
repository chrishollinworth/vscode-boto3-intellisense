"""
Type annotations for lex-models service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_lex_models import LexModelBuildingServiceClient
    from mypy_boto3_lex_models.paginator import (
        GetBotAliasesPaginator,
        GetBotChannelAssociationsPaginator,
        GetBotVersionsPaginator,
        GetBotsPaginator,
        GetBuiltinIntentsPaginator,
        GetBuiltinSlotTypesPaginator,
        GetIntentVersionsPaginator,
        GetIntentsPaginator,
        GetSlotTypeVersionsPaginator,
        GetSlotTypesPaginator,
    )

    client: LexModelBuildingServiceClient = boto3.client("lex-models")

    get_bot_aliases_paginator: GetBotAliasesPaginator = client.get_paginator("get_bot_aliases")
    get_bot_channel_associations_paginator: GetBotChannelAssociationsPaginator = client.get_paginator("get_bot_channel_associations")
    get_bot_versions_paginator: GetBotVersionsPaginator = client.get_paginator("get_bot_versions")
    get_bots_paginator: GetBotsPaginator = client.get_paginator("get_bots")
    get_builtin_intents_paginator: GetBuiltinIntentsPaginator = client.get_paginator("get_builtin_intents")
    get_builtin_slot_types_paginator: GetBuiltinSlotTypesPaginator = client.get_paginator("get_builtin_slot_types")
    get_intent_versions_paginator: GetIntentVersionsPaginator = client.get_paginator("get_intent_versions")
    get_intents_paginator: GetIntentsPaginator = client.get_paginator("get_intents")
    get_slot_type_versions_paginator: GetSlotTypeVersionsPaginator = client.get_paginator("get_slot_type_versions")
    get_slot_types_paginator: GetSlotTypesPaginator = client.get_paginator("get_slot_types")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import LocaleType
from .type_defs import (
    GetBotAliasesResponseTypeDef,
    GetBotChannelAssociationsResponseTypeDef,
    GetBotsResponseTypeDef,
    GetBotVersionsResponseTypeDef,
    GetBuiltinIntentsResponseTypeDef,
    GetBuiltinSlotTypesResponseTypeDef,
    GetIntentsResponseTypeDef,
    GetIntentVersionsResponseTypeDef,
    GetSlotTypesResponseTypeDef,
    GetSlotTypeVersionsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "GetBotAliasesPaginator",
    "GetBotChannelAssociationsPaginator",
    "GetBotVersionsPaginator",
    "GetBotsPaginator",
    "GetBuiltinIntentsPaginator",
    "GetBuiltinSlotTypesPaginator",
    "GetIntentVersionsPaginator",
    "GetIntentsPaginator",
    "GetSlotTypeVersionsPaginator",
    "GetSlotTypesPaginator",
)

class GetBotAliasesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotAliases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbotaliasespaginator)
    """

    def paginate(
        self,
        *,
        botName: str,
        nameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetBotAliasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotAliases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbotaliasespaginator)
        """

class GetBotChannelAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotChannelAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbotchannelassociationspaginator)
    """

    def paginate(
        self,
        *,
        botName: str,
        botAlias: str,
        nameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetBotChannelAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotChannelAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbotchannelassociationspaginator)
        """

class GetBotVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbotversionspaginator)
    """

    def paginate(
        self, *, name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetBotVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbotversionspaginator)
        """

class GetBotsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBots)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbotspaginator)
    """

    def paginate(
        self, *, nameContains: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetBotsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBots.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbotspaginator)
        """

class GetBuiltinIntentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinIntents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbuiltinintentspaginator)
    """

    def paginate(
        self,
        *,
        locale: LocaleType = None,
        signatureContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetBuiltinIntentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinIntents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbuiltinintentspaginator)
        """

class GetBuiltinSlotTypesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinSlotTypes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbuiltinslottypespaginator)
    """

    def paginate(
        self,
        *,
        locale: LocaleType = None,
        signatureContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetBuiltinSlotTypesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinSlotTypes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbuiltinslottypespaginator)
        """

class GetIntentVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntentVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getintentversionspaginator)
    """

    def paginate(
        self, *, name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetIntentVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntentVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getintentversionspaginator)
        """

class GetIntentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getintentspaginator)
    """

    def paginate(
        self, *, nameContains: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetIntentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getintentspaginator)
        """

class GetSlotTypeVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypeVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getslottypeversionspaginator)
    """

    def paginate(
        self, *, name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetSlotTypeVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypeVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getslottypeversionspaginator)
        """

class GetSlotTypesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getslottypespaginator)
    """

    def paginate(
        self, *, nameContains: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetSlotTypesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getslottypespaginator)
        """
