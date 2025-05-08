"""
Type annotations for schemas service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_schemas.client import SchemasClient
    from mypy_boto3_schemas.paginator import (
        ListDiscoverersPaginator,
        ListRegistriesPaginator,
        ListSchemaVersionsPaginator,
        ListSchemasPaginator,
        SearchSchemasPaginator,
    )

    session = Session()
    client: SchemasClient = session.client("schemas")

    list_discoverers_paginator: ListDiscoverersPaginator = client.get_paginator("list_discoverers")
    list_registries_paginator: ListRegistriesPaginator = client.get_paginator("list_registries")
    list_schema_versions_paginator: ListSchemaVersionsPaginator = client.get_paginator("list_schema_versions")
    list_schemas_paginator: ListSchemasPaginator = client.get_paginator("list_schemas")
    search_schemas_paginator: SearchSchemasPaginator = client.get_paginator("search_schemas")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListDiscoverersRequestPaginateTypeDef,
    ListDiscoverersResponseTypeDef,
    ListRegistriesRequestPaginateTypeDef,
    ListRegistriesResponseTypeDef,
    ListSchemasRequestPaginateTypeDef,
    ListSchemasResponseTypeDef,
    ListSchemaVersionsRequestPaginateTypeDef,
    ListSchemaVersionsResponseTypeDef,
    SearchSchemasRequestPaginateTypeDef,
    SearchSchemasResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListDiscoverersPaginator",
    "ListRegistriesPaginator",
    "ListSchemaVersionsPaginator",
    "ListSchemasPaginator",
    "SearchSchemasPaginator",
)

if TYPE_CHECKING:
    _ListDiscoverersPaginatorBase = Paginator[ListDiscoverersResponseTypeDef]
else:
    _ListDiscoverersPaginatorBase = Paginator  # type: ignore[assignment]

class ListDiscoverersPaginator(_ListDiscoverersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas/paginator/ListDiscoverers.html#Schemas.Paginator.ListDiscoverers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators/#listdiscovererspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDiscoverersRequestPaginateTypeDef]
    ) -> PageIterator[ListDiscoverersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas/paginator/ListDiscoverers.html#Schemas.Paginator.ListDiscoverers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators/#listdiscovererspaginator)
        """

if TYPE_CHECKING:
    _ListRegistriesPaginatorBase = Paginator[ListRegistriesResponseTypeDef]
else:
    _ListRegistriesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRegistriesPaginator(_ListRegistriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas/paginator/ListRegistries.html#Schemas.Paginator.ListRegistries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators/#listregistriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRegistriesRequestPaginateTypeDef]
    ) -> PageIterator[ListRegistriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas/paginator/ListRegistries.html#Schemas.Paginator.ListRegistries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators/#listregistriespaginator)
        """

if TYPE_CHECKING:
    _ListSchemaVersionsPaginatorBase = Paginator[ListSchemaVersionsResponseTypeDef]
else:
    _ListSchemaVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSchemaVersionsPaginator(_ListSchemaVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas/paginator/ListSchemaVersions.html#Schemas.Paginator.ListSchemaVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators/#listschemaversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSchemaVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListSchemaVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas/paginator/ListSchemaVersions.html#Schemas.Paginator.ListSchemaVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators/#listschemaversionspaginator)
        """

if TYPE_CHECKING:
    _ListSchemasPaginatorBase = Paginator[ListSchemasResponseTypeDef]
else:
    _ListSchemasPaginatorBase = Paginator  # type: ignore[assignment]

class ListSchemasPaginator(_ListSchemasPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas/paginator/ListSchemas.html#Schemas.Paginator.ListSchemas)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators/#listschemaspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSchemasRequestPaginateTypeDef]
    ) -> PageIterator[ListSchemasResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas/paginator/ListSchemas.html#Schemas.Paginator.ListSchemas.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators/#listschemaspaginator)
        """

if TYPE_CHECKING:
    _SearchSchemasPaginatorBase = Paginator[SearchSchemasResponseTypeDef]
else:
    _SearchSchemasPaginatorBase = Paginator  # type: ignore[assignment]

class SearchSchemasPaginator(_SearchSchemasPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas/paginator/SearchSchemas.html#Schemas.Paginator.SearchSchemas)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators/#searchschemaspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchSchemasRequestPaginateTypeDef]
    ) -> PageIterator[SearchSchemasResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas/paginator/SearchSchemas.html#Schemas.Paginator.SearchSchemas.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators/#searchschemaspaginator)
        """
