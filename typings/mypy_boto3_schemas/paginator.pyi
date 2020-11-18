# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for schemas service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_schemas import SchemasClient
    from mypy_boto3_schemas.paginator import (
        ListDiscoverersPaginator,
        ListRegistriesPaginator,
        ListSchemaVersionsPaginator,
        ListSchemasPaginator,
        SearchSchemasPaginator,
    )

    client: SchemasClient = boto3.client("schemas")

    list_discoverers_paginator: ListDiscoverersPaginator = client.get_paginator("list_discoverers")
    list_registries_paginator: ListRegistriesPaginator = client.get_paginator("list_registries")
    list_schema_versions_paginator: ListSchemaVersionsPaginator = client.get_paginator("list_schema_versions")
    list_schemas_paginator: ListSchemasPaginator = client.get_paginator("list_schemas")
    search_schemas_paginator: SearchSchemasPaginator = client.get_paginator("search_schemas")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_schemas.type_defs import (
    ListDiscoverersResponseTypeDef,
    ListRegistriesResponseTypeDef,
    ListSchemasResponseTypeDef,
    ListSchemaVersionsResponseTypeDef,
    PaginatorConfigTypeDef,
    SearchSchemasResponseTypeDef,
)

__all__ = (
    "ListDiscoverersPaginator",
    "ListRegistriesPaginator",
    "ListSchemaVersionsPaginator",
    "ListSchemasPaginator",
    "SearchSchemasPaginator",
)


class ListDiscoverersPaginator(Boto3Paginator):
    """
    [Paginator.ListDiscoverers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Paginator.ListDiscoverers)
    """

    def paginate(
        self,
        DiscovererIdPrefix: str = None,
        SourceArnPrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDiscoverersResponseTypeDef]:
        """
        [ListDiscoverers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Paginator.ListDiscoverers.paginate)
        """


class ListRegistriesPaginator(Boto3Paginator):
    """
    [Paginator.ListRegistries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Paginator.ListRegistries)
    """

    def paginate(
        self,
        RegistryNamePrefix: str = None,
        Scope: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListRegistriesResponseTypeDef]:
        """
        [ListRegistries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Paginator.ListRegistries.paginate)
        """


class ListSchemaVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListSchemaVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Paginator.ListSchemaVersions)
    """

    def paginate(
        self, RegistryName: str, SchemaName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSchemaVersionsResponseTypeDef]:
        """
        [ListSchemaVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Paginator.ListSchemaVersions.paginate)
        """


class ListSchemasPaginator(Boto3Paginator):
    """
    [Paginator.ListSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Paginator.ListSchemas)
    """

    def paginate(
        self,
        RegistryName: str,
        SchemaNamePrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListSchemasResponseTypeDef]:
        """
        [ListSchemas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Paginator.ListSchemas.paginate)
        """


class SearchSchemasPaginator(Boto3Paginator):
    """
    [Paginator.SearchSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Paginator.SearchSchemas)
    """

    def paginate(
        self, Keywords: str, RegistryName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchSchemasResponseTypeDef]:
        """
        [SearchSchemas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Paginator.SearchSchemas.paginate)
        """
