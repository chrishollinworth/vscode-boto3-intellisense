"""
Main interface for appsync service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_appsync import (
        AppSyncClient,
        Client,
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

from .client import AppSyncClient
from .paginator import (
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

Client = AppSyncClient

__all__ = (
    "AppSyncClient",
    "Client",
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
