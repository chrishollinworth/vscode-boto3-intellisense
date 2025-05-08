"""
Main interface for s3tables service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3tables/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_s3tables import (
        Client,
        ListNamespacesPaginator,
        ListTableBucketsPaginator,
        ListTablesPaginator,
        S3TablesClient,
    )

    session = Session()
    client: S3TablesClient = session.client("s3tables")

    list_namespaces_paginator: ListNamespacesPaginator = client.get_paginator("list_namespaces")
    list_table_buckets_paginator: ListTableBucketsPaginator = client.get_paginator("list_table_buckets")
    list_tables_paginator: ListTablesPaginator = client.get_paginator("list_tables")
    ```
"""

from .client import S3TablesClient
from .paginator import ListNamespacesPaginator, ListTableBucketsPaginator, ListTablesPaginator

Client = S3TablesClient

__all__ = (
    "Client",
    "ListNamespacesPaginator",
    "ListTableBucketsPaginator",
    "ListTablesPaginator",
    "S3TablesClient",
)
