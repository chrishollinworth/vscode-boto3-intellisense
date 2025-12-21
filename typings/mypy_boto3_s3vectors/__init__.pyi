"""
Main interface for s3vectors service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3vectors/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_s3vectors import (
        Client,
        ListIndexesPaginator,
        ListVectorBucketsPaginator,
        ListVectorsPaginator,
        S3VectorsClient,
    )

    session = Session()
    client: S3VectorsClient = session.client("s3vectors")

    list_indexes_paginator: ListIndexesPaginator = client.get_paginator("list_indexes")
    list_vector_buckets_paginator: ListVectorBucketsPaginator = client.get_paginator("list_vector_buckets")
    list_vectors_paginator: ListVectorsPaginator = client.get_paginator("list_vectors")
    ```
"""

from .client import S3VectorsClient
from .paginator import ListIndexesPaginator, ListVectorBucketsPaginator, ListVectorsPaginator

Client = S3VectorsClient

__all__ = (
    "Client",
    "ListIndexesPaginator",
    "ListVectorBucketsPaginator",
    "ListVectorsPaginator",
    "S3VectorsClient",
)
