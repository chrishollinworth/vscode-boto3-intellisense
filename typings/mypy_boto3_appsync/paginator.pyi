# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for appsync service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_appsync import AppSyncClient
    from mypy_boto3_appsync.paginator import (
        ListApiKeysPaginator,
        ListDataSourcesPaginator,
        ListFunctionsPaginator,
        ListGraphqlApisPaginator,
        ListResolversPaginator,
        ListResolversByFunctionPaginator,
        ListTypesPaginator,
    )

    client: AppSyncClient = boto3.client("appsync")

    list_api_keys_paginator: ListApiKeysPaginator = client.get_paginator("list_api_keys")
    list_data_sources_paginator: ListDataSourcesPaginator = client.get_paginator("list_data_sources")
    list_functions_paginator: ListFunctionsPaginator = client.get_paginator("list_functions")
    list_graphql_apis_paginator: ListGraphqlApisPaginator = client.get_paginator("list_graphql_apis")
    list_resolvers_paginator: ListResolversPaginator = client.get_paginator("list_resolvers")
    list_resolvers_by_function_paginator: ListResolversByFunctionPaginator = client.get_paginator("list_resolvers_by_function")
    list_types_paginator: ListTypesPaginator = client.get_paginator("list_types")
    ```
"""
import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_appsync.type_defs import (
    ListApiKeysResponseTypeDef,
    ListDataSourcesResponseTypeDef,
    ListFunctionsResponseTypeDef,
    ListGraphqlApisResponseTypeDef,
    ListResolversByFunctionResponseTypeDef,
    ListResolversResponseTypeDef,
    ListTypesResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListApiKeysPaginator",
    "ListDataSourcesPaginator",
    "ListFunctionsPaginator",
    "ListGraphqlApisPaginator",
    "ListResolversPaginator",
    "ListResolversByFunctionPaginator",
    "ListTypesPaginator",
)


class ListApiKeysPaginator(Boto3Paginator):
    """
    [Paginator.ListApiKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appsync.html#AppSync.Paginator.ListApiKeys)
    """

    def paginate(
        self, apiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApiKeysResponseTypeDef]:
        """
        [ListApiKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appsync.html#AppSync.Paginator.ListApiKeys.paginate)
        """


class ListDataSourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListDataSources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appsync.html#AppSync.Paginator.ListDataSources)
    """

    def paginate(
        self, apiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataSourcesResponseTypeDef]:
        """
        [ListDataSources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appsync.html#AppSync.Paginator.ListDataSources.paginate)
        """


class ListFunctionsPaginator(Boto3Paginator):
    """
    [Paginator.ListFunctions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appsync.html#AppSync.Paginator.ListFunctions)
    """

    def paginate(
        self, apiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFunctionsResponseTypeDef]:
        """
        [ListFunctions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appsync.html#AppSync.Paginator.ListFunctions.paginate)
        """


class ListGraphqlApisPaginator(Boto3Paginator):
    """
    [Paginator.ListGraphqlApis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appsync.html#AppSync.Paginator.ListGraphqlApis)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGraphqlApisResponseTypeDef]:
        """
        [ListGraphqlApis.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appsync.html#AppSync.Paginator.ListGraphqlApis.paginate)
        """


class ListResolversPaginator(Boto3Paginator):
    """
    [Paginator.ListResolvers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appsync.html#AppSync.Paginator.ListResolvers)
    """

    def paginate(
        self, apiId: str, typeName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResolversResponseTypeDef]:
        """
        [ListResolvers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appsync.html#AppSync.Paginator.ListResolvers.paginate)
        """


class ListResolversByFunctionPaginator(Boto3Paginator):
    """
    [Paginator.ListResolversByFunction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appsync.html#AppSync.Paginator.ListResolversByFunction)
    """

    def paginate(
        self, apiId: str, functionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResolversByFunctionResponseTypeDef]:
        """
        [ListResolversByFunction.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appsync.html#AppSync.Paginator.ListResolversByFunction.paginate)
        """


class ListTypesPaginator(Boto3Paginator):
    """
    [Paginator.ListTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appsync.html#AppSync.Paginator.ListTypes)
    """

    def paginate(
        self,
        apiId: str,
        format: Literal["SDL", "JSON"],
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTypesResponseTypeDef]:
        """
        [ListTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/appsync.html#AppSync.Paginator.ListTypes.paginate)
        """
