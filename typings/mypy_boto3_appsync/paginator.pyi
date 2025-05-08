"""
Type annotations for appsync service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_appsync.client import AppSyncClient
    from mypy_boto3_appsync.paginator import (
        ListApiKeysPaginator,
        ListApisPaginator,
        ListChannelNamespacesPaginator,
        ListDataSourcesPaginator,
        ListDomainNamesPaginator,
        ListFunctionsPaginator,
        ListGraphqlApisPaginator,
        ListResolversByFunctionPaginator,
        ListResolversPaginator,
        ListSourceApiAssociationsPaginator,
        ListTypesByAssociationPaginator,
        ListTypesPaginator,
    )

    session = Session()
    client: AppSyncClient = session.client("appsync")

    list_api_keys_paginator: ListApiKeysPaginator = client.get_paginator("list_api_keys")
    list_apis_paginator: ListApisPaginator = client.get_paginator("list_apis")
    list_channel_namespaces_paginator: ListChannelNamespacesPaginator = client.get_paginator("list_channel_namespaces")
    list_data_sources_paginator: ListDataSourcesPaginator = client.get_paginator("list_data_sources")
    list_domain_names_paginator: ListDomainNamesPaginator = client.get_paginator("list_domain_names")
    list_functions_paginator: ListFunctionsPaginator = client.get_paginator("list_functions")
    list_graphql_apis_paginator: ListGraphqlApisPaginator = client.get_paginator("list_graphql_apis")
    list_resolvers_by_function_paginator: ListResolversByFunctionPaginator = client.get_paginator("list_resolvers_by_function")
    list_resolvers_paginator: ListResolversPaginator = client.get_paginator("list_resolvers")
    list_source_api_associations_paginator: ListSourceApiAssociationsPaginator = client.get_paginator("list_source_api_associations")
    list_types_by_association_paginator: ListTypesByAssociationPaginator = client.get_paginator("list_types_by_association")
    list_types_paginator: ListTypesPaginator = client.get_paginator("list_types")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListApiKeysRequestPaginateTypeDef,
    ListApiKeysResponseTypeDef,
    ListApisRequestPaginateTypeDef,
    ListApisResponseTypeDef,
    ListChannelNamespacesRequestPaginateTypeDef,
    ListChannelNamespacesResponseTypeDef,
    ListDataSourcesRequestPaginateTypeDef,
    ListDataSourcesResponseTypeDef,
    ListDomainNamesRequestPaginateTypeDef,
    ListDomainNamesResponseTypeDef,
    ListFunctionsRequestPaginateTypeDef,
    ListFunctionsResponseTypeDef,
    ListGraphqlApisRequestPaginateTypeDef,
    ListGraphqlApisResponseTypeDef,
    ListResolversByFunctionRequestPaginateTypeDef,
    ListResolversByFunctionResponseTypeDef,
    ListResolversRequestPaginateTypeDef,
    ListResolversResponseTypeDef,
    ListSourceApiAssociationsRequestPaginateTypeDef,
    ListSourceApiAssociationsResponseTypeDef,
    ListTypesByAssociationRequestPaginateTypeDef,
    ListTypesByAssociationResponseTypeDef,
    ListTypesRequestPaginateTypeDef,
    ListTypesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListApiKeysPaginator",
    "ListApisPaginator",
    "ListChannelNamespacesPaginator",
    "ListDataSourcesPaginator",
    "ListDomainNamesPaginator",
    "ListFunctionsPaginator",
    "ListGraphqlApisPaginator",
    "ListResolversByFunctionPaginator",
    "ListResolversPaginator",
    "ListSourceApiAssociationsPaginator",
    "ListTypesByAssociationPaginator",
    "ListTypesPaginator",
)

if TYPE_CHECKING:
    _ListApiKeysPaginatorBase = Paginator[ListApiKeysResponseTypeDef]
else:
    _ListApiKeysPaginatorBase = Paginator  # type: ignore[assignment]

class ListApiKeysPaginator(_ListApiKeysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListApiKeys.html#AppSync.Paginator.ListApiKeys)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listapikeyspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApiKeysRequestPaginateTypeDef]
    ) -> PageIterator[ListApiKeysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListApiKeys.html#AppSync.Paginator.ListApiKeys.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listapikeyspaginator)
        """

if TYPE_CHECKING:
    _ListApisPaginatorBase = Paginator[ListApisResponseTypeDef]
else:
    _ListApisPaginatorBase = Paginator  # type: ignore[assignment]

class ListApisPaginator(_ListApisPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListApis.html#AppSync.Paginator.ListApis)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listapispaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApisRequestPaginateTypeDef]
    ) -> PageIterator[ListApisResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListApis.html#AppSync.Paginator.ListApis.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listapispaginator)
        """

if TYPE_CHECKING:
    _ListChannelNamespacesPaginatorBase = Paginator[ListChannelNamespacesResponseTypeDef]
else:
    _ListChannelNamespacesPaginatorBase = Paginator  # type: ignore[assignment]

class ListChannelNamespacesPaginator(_ListChannelNamespacesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListChannelNamespaces.html#AppSync.Paginator.ListChannelNamespaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listchannelnamespacespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListChannelNamespacesRequestPaginateTypeDef]
    ) -> PageIterator[ListChannelNamespacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListChannelNamespaces.html#AppSync.Paginator.ListChannelNamespaces.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listchannelnamespacespaginator)
        """

if TYPE_CHECKING:
    _ListDataSourcesPaginatorBase = Paginator[ListDataSourcesResponseTypeDef]
else:
    _ListDataSourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataSourcesPaginator(_ListDataSourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListDataSources.html#AppSync.Paginator.ListDataSources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listdatasourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataSourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListDataSourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListDataSources.html#AppSync.Paginator.ListDataSources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listdatasourcespaginator)
        """

if TYPE_CHECKING:
    _ListDomainNamesPaginatorBase = Paginator[ListDomainNamesResponseTypeDef]
else:
    _ListDomainNamesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDomainNamesPaginator(_ListDomainNamesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListDomainNames.html#AppSync.Paginator.ListDomainNames)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listdomainnamespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDomainNamesRequestPaginateTypeDef]
    ) -> PageIterator[ListDomainNamesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListDomainNames.html#AppSync.Paginator.ListDomainNames.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listdomainnamespaginator)
        """

if TYPE_CHECKING:
    _ListFunctionsPaginatorBase = Paginator[ListFunctionsResponseTypeDef]
else:
    _ListFunctionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFunctionsPaginator(_ListFunctionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListFunctions.html#AppSync.Paginator.ListFunctions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listfunctionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFunctionsRequestPaginateTypeDef]
    ) -> PageIterator[ListFunctionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListFunctions.html#AppSync.Paginator.ListFunctions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listfunctionspaginator)
        """

if TYPE_CHECKING:
    _ListGraphqlApisPaginatorBase = Paginator[ListGraphqlApisResponseTypeDef]
else:
    _ListGraphqlApisPaginatorBase = Paginator  # type: ignore[assignment]

class ListGraphqlApisPaginator(_ListGraphqlApisPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListGraphqlApis.html#AppSync.Paginator.ListGraphqlApis)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listgraphqlapispaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGraphqlApisRequestPaginateTypeDef]
    ) -> PageIterator[ListGraphqlApisResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListGraphqlApis.html#AppSync.Paginator.ListGraphqlApis.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listgraphqlapispaginator)
        """

if TYPE_CHECKING:
    _ListResolversByFunctionPaginatorBase = Paginator[ListResolversByFunctionResponseTypeDef]
else:
    _ListResolversByFunctionPaginatorBase = Paginator  # type: ignore[assignment]

class ListResolversByFunctionPaginator(_ListResolversByFunctionPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListResolversByFunction.html#AppSync.Paginator.ListResolversByFunction)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listresolversbyfunctionpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResolversByFunctionRequestPaginateTypeDef]
    ) -> PageIterator[ListResolversByFunctionResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListResolversByFunction.html#AppSync.Paginator.ListResolversByFunction.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listresolversbyfunctionpaginator)
        """

if TYPE_CHECKING:
    _ListResolversPaginatorBase = Paginator[ListResolversResponseTypeDef]
else:
    _ListResolversPaginatorBase = Paginator  # type: ignore[assignment]

class ListResolversPaginator(_ListResolversPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListResolvers.html#AppSync.Paginator.ListResolvers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listresolverspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResolversRequestPaginateTypeDef]
    ) -> PageIterator[ListResolversResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListResolvers.html#AppSync.Paginator.ListResolvers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listresolverspaginator)
        """

if TYPE_CHECKING:
    _ListSourceApiAssociationsPaginatorBase = Paginator[ListSourceApiAssociationsResponseTypeDef]
else:
    _ListSourceApiAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSourceApiAssociationsPaginator(_ListSourceApiAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListSourceApiAssociations.html#AppSync.Paginator.ListSourceApiAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listsourceapiassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSourceApiAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListSourceApiAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListSourceApiAssociations.html#AppSync.Paginator.ListSourceApiAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listsourceapiassociationspaginator)
        """

if TYPE_CHECKING:
    _ListTypesByAssociationPaginatorBase = Paginator[ListTypesByAssociationResponseTypeDef]
else:
    _ListTypesByAssociationPaginatorBase = Paginator  # type: ignore[assignment]

class ListTypesByAssociationPaginator(_ListTypesByAssociationPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListTypesByAssociation.html#AppSync.Paginator.ListTypesByAssociation)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listtypesbyassociationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTypesByAssociationRequestPaginateTypeDef]
    ) -> PageIterator[ListTypesByAssociationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListTypesByAssociation.html#AppSync.Paginator.ListTypesByAssociation.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listtypesbyassociationpaginator)
        """

if TYPE_CHECKING:
    _ListTypesPaginatorBase = Paginator[ListTypesResponseTypeDef]
else:
    _ListTypesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTypesPaginator(_ListTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListTypes.html#AppSync.Paginator.ListTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listtypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTypesRequestPaginateTypeDef]
    ) -> PageIterator[ListTypesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/paginator/ListTypes.html#AppSync.Paginator.ListTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators/#listtypespaginator)
        """
