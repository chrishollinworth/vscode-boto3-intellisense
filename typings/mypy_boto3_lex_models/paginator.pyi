"""
Type annotations for lex-models service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_lex_models.client import LexModelBuildingServiceClient
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

    session = Session()
    client: LexModelBuildingServiceClient = session.client("lex-models")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetBotAliasesRequestPaginateTypeDef,
    GetBotAliasesResponseTypeDef,
    GetBotChannelAssociationsRequestPaginateTypeDef,
    GetBotChannelAssociationsResponseTypeDef,
    GetBotsRequestPaginateTypeDef,
    GetBotsResponseTypeDef,
    GetBotVersionsRequestPaginateTypeDef,
    GetBotVersionsResponseTypeDef,
    GetBuiltinIntentsRequestPaginateTypeDef,
    GetBuiltinIntentsResponseTypeDef,
    GetBuiltinSlotTypesRequestPaginateTypeDef,
    GetBuiltinSlotTypesResponseTypeDef,
    GetIntentsRequestPaginateTypeDef,
    GetIntentsResponseTypeDef,
    GetIntentVersionsRequestPaginateTypeDef,
    GetIntentVersionsResponseTypeDef,
    GetSlotTypesRequestPaginateTypeDef,
    GetSlotTypesResponseTypeDef,
    GetSlotTypeVersionsRequestPaginateTypeDef,
    GetSlotTypeVersionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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

if TYPE_CHECKING:
    _GetBotAliasesPaginatorBase = Paginator[GetBotAliasesResponseTypeDef]
else:
    _GetBotAliasesPaginatorBase = Paginator  # type: ignore[assignment]

class GetBotAliasesPaginator(_GetBotAliasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/paginator/GetBotAliases.html#LexModelBuildingService.Paginator.GetBotAliases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/#getbotaliasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetBotAliasesRequestPaginateTypeDef]
    ) -> PageIterator[GetBotAliasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/paginator/GetBotAliases.html#LexModelBuildingService.Paginator.GetBotAliases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/#getbotaliasespaginator)
        """

if TYPE_CHECKING:
    _GetBotChannelAssociationsPaginatorBase = Paginator[GetBotChannelAssociationsResponseTypeDef]
else:
    _GetBotChannelAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class GetBotChannelAssociationsPaginator(_GetBotChannelAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/paginator/GetBotChannelAssociations.html#LexModelBuildingService.Paginator.GetBotChannelAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/#getbotchannelassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetBotChannelAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[GetBotChannelAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/paginator/GetBotChannelAssociations.html#LexModelBuildingService.Paginator.GetBotChannelAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/#getbotchannelassociationspaginator)
        """

if TYPE_CHECKING:
    _GetBotVersionsPaginatorBase = Paginator[GetBotVersionsResponseTypeDef]
else:
    _GetBotVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class GetBotVersionsPaginator(_GetBotVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/paginator/GetBotVersions.html#LexModelBuildingService.Paginator.GetBotVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/#getbotversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetBotVersionsRequestPaginateTypeDef]
    ) -> PageIterator[GetBotVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/paginator/GetBotVersions.html#LexModelBuildingService.Paginator.GetBotVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/#getbotversionspaginator)
        """

if TYPE_CHECKING:
    _GetBotsPaginatorBase = Paginator[GetBotsResponseTypeDef]
else:
    _GetBotsPaginatorBase = Paginator  # type: ignore[assignment]

class GetBotsPaginator(_GetBotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/paginator/GetBots.html#LexModelBuildingService.Paginator.GetBots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/#getbotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetBotsRequestPaginateTypeDef]
    ) -> PageIterator[GetBotsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/paginator/GetBots.html#LexModelBuildingService.Paginator.GetBots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/#getbotspaginator)
        """

if TYPE_CHECKING:
    _GetBuiltinIntentsPaginatorBase = Paginator[GetBuiltinIntentsResponseTypeDef]
else:
    _GetBuiltinIntentsPaginatorBase = Paginator  # type: ignore[assignment]

class GetBuiltinIntentsPaginator(_GetBuiltinIntentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/paginator/GetBuiltinIntents.html#LexModelBuildingService.Paginator.GetBuiltinIntents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/#getbuiltinintentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetBuiltinIntentsRequestPaginateTypeDef]
    ) -> PageIterator[GetBuiltinIntentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/paginator/GetBuiltinIntents.html#LexModelBuildingService.Paginator.GetBuiltinIntents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/#getbuiltinintentspaginator)
        """

if TYPE_CHECKING:
    _GetBuiltinSlotTypesPaginatorBase = Paginator[GetBuiltinSlotTypesResponseTypeDef]
else:
    _GetBuiltinSlotTypesPaginatorBase = Paginator  # type: ignore[assignment]

class GetBuiltinSlotTypesPaginator(_GetBuiltinSlotTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/paginator/GetBuiltinSlotTypes.html#LexModelBuildingService.Paginator.GetBuiltinSlotTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/#getbuiltinslottypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetBuiltinSlotTypesRequestPaginateTypeDef]
    ) -> PageIterator[GetBuiltinSlotTypesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/paginator/GetBuiltinSlotTypes.html#LexModelBuildingService.Paginator.GetBuiltinSlotTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/#getbuiltinslottypespaginator)
        """

if TYPE_CHECKING:
    _GetIntentVersionsPaginatorBase = Paginator[GetIntentVersionsResponseTypeDef]
else:
    _GetIntentVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class GetIntentVersionsPaginator(_GetIntentVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/paginator/GetIntentVersions.html#LexModelBuildingService.Paginator.GetIntentVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/#getintentversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetIntentVersionsRequestPaginateTypeDef]
    ) -> PageIterator[GetIntentVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/paginator/GetIntentVersions.html#LexModelBuildingService.Paginator.GetIntentVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/#getintentversionspaginator)
        """

if TYPE_CHECKING:
    _GetIntentsPaginatorBase = Paginator[GetIntentsResponseTypeDef]
else:
    _GetIntentsPaginatorBase = Paginator  # type: ignore[assignment]

class GetIntentsPaginator(_GetIntentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/paginator/GetIntents.html#LexModelBuildingService.Paginator.GetIntents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/#getintentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetIntentsRequestPaginateTypeDef]
    ) -> PageIterator[GetIntentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/paginator/GetIntents.html#LexModelBuildingService.Paginator.GetIntents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/#getintentspaginator)
        """

if TYPE_CHECKING:
    _GetSlotTypeVersionsPaginatorBase = Paginator[GetSlotTypeVersionsResponseTypeDef]
else:
    _GetSlotTypeVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class GetSlotTypeVersionsPaginator(_GetSlotTypeVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/paginator/GetSlotTypeVersions.html#LexModelBuildingService.Paginator.GetSlotTypeVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/#getslottypeversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetSlotTypeVersionsRequestPaginateTypeDef]
    ) -> PageIterator[GetSlotTypeVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/paginator/GetSlotTypeVersions.html#LexModelBuildingService.Paginator.GetSlotTypeVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/#getslottypeversionspaginator)
        """

if TYPE_CHECKING:
    _GetSlotTypesPaginatorBase = Paginator[GetSlotTypesResponseTypeDef]
else:
    _GetSlotTypesPaginatorBase = Paginator  # type: ignore[assignment]

class GetSlotTypesPaginator(_GetSlotTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/paginator/GetSlotTypes.html#LexModelBuildingService.Paginator.GetSlotTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/#getslottypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetSlotTypesRequestPaginateTypeDef]
    ) -> PageIterator[GetSlotTypesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models/paginator/GetSlotTypes.html#LexModelBuildingService.Paginator.GetSlotTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators/#getslottypespaginator)
        """
