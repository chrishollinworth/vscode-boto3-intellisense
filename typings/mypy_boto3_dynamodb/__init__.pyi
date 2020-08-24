"""
Main interface for dynamodb service.

Usage::

    ```python
    import boto3
    from mypy_boto3_dynamodb import (
        Client,
        DynamoDBClient,
        DynamoDBServiceResource,
        ListBackupsPaginator,
        ListTablesPaginator,
        ListTagsOfResourcePaginator,
        QueryPaginator,
        ScanPaginator,
        ServiceResource,
        TableExistsWaiter,
        TableNotExistsWaiter,
    )

    session = boto3.Session()

    client: DynamoDBClient = boto3.client("dynamodb")
    session_client: DynamoDBClient = session.client("dynamodb")

    resource: DynamoDBServiceResource = boto3.resource("dynamodb")
    session_resource: DynamoDBServiceResource = session.resource("dynamodb")

    table_exists_waiter: TableExistsWaiter = client.get_waiter("table_exists")
    table_not_exists_waiter: TableNotExistsWaiter = client.get_waiter("table_not_exists")

    list_backups_paginator: ListBackupsPaginator = client.get_paginator("list_backups")
    list_tables_paginator: ListTablesPaginator = client.get_paginator("list_tables")
    list_tags_of_resource_paginator: ListTagsOfResourcePaginator = client.get_paginator("list_tags_of_resource")
    query_paginator: QueryPaginator = client.get_paginator("query")
    scan_paginator: ScanPaginator = client.get_paginator("scan")
    ```
"""
from mypy_boto3_dynamodb.client import DynamoDBClient
from mypy_boto3_dynamodb.paginator import (
    ListBackupsPaginator,
    ListTablesPaginator,
    ListTagsOfResourcePaginator,
    QueryPaginator,
    ScanPaginator,
)
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource
from mypy_boto3_dynamodb.waiter import TableExistsWaiter, TableNotExistsWaiter

Client = DynamoDBClient


ServiceResource = DynamoDBServiceResource


__all__ = (
    "Client",
    "DynamoDBClient",
    "DynamoDBServiceResource",
    "ListBackupsPaginator",
    "ListTablesPaginator",
    "ListTagsOfResourcePaginator",
    "QueryPaginator",
    "ScanPaginator",
    "ServiceResource",
    "TableExistsWaiter",
    "TableNotExistsWaiter",
)
