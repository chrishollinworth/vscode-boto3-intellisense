"""
Main interface for athena service.

Usage::

    ```python
    import boto3
    from mypy_boto3_athena import (
        AthenaClient,
        Client,
        GetQueryResultsPaginator,
        ListDataCatalogsPaginator,
        ListDatabasesPaginator,
        ListNamedQueriesPaginator,
        ListQueryExecutionsPaginator,
        ListTableMetadataPaginator,
        ListTagsForResourcePaginator,
    )

    session = boto3.Session()

    client: AthenaClient = boto3.client("athena")
    session_client: AthenaClient = session.client("athena")

    get_query_results_paginator: GetQueryResultsPaginator = client.get_paginator("get_query_results")
    list_data_catalogs_paginator: ListDataCatalogsPaginator = client.get_paginator("list_data_catalogs")
    list_databases_paginator: ListDatabasesPaginator = client.get_paginator("list_databases")
    list_named_queries_paginator: ListNamedQueriesPaginator = client.get_paginator("list_named_queries")
    list_query_executions_paginator: ListQueryExecutionsPaginator = client.get_paginator("list_query_executions")
    list_table_metadata_paginator: ListTableMetadataPaginator = client.get_paginator("list_table_metadata")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""
from .client import AthenaClient
from .paginator import (
    GetQueryResultsPaginator,
    ListDatabasesPaginator,
    ListDataCatalogsPaginator,
    ListNamedQueriesPaginator,
    ListQueryExecutionsPaginator,
    ListTableMetadataPaginator,
    ListTagsForResourcePaginator,
)

Client = AthenaClient

__all__ = (
    "AthenaClient",
    "Client",
    "GetQueryResultsPaginator",
    "ListDataCatalogsPaginator",
    "ListDatabasesPaginator",
    "ListNamedQueriesPaginator",
    "ListQueryExecutionsPaginator",
    "ListTableMetadataPaginator",
    "ListTagsForResourcePaginator",
)
