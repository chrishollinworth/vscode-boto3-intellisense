"""
Main interface for s3control service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_s3control import (
        Client,
        ListAccessPointsForDirectoryBucketsPaginator,
        ListAccessPointsForObjectLambdaPaginator,
        ListCallerAccessGrantsPaginator,
        S3ControlClient,
    )

    session = Session()
    client: S3ControlClient = session.client("s3control")

    list_access_points_for_directory_buckets_paginator: ListAccessPointsForDirectoryBucketsPaginator = client.get_paginator("list_access_points_for_directory_buckets")
    list_access_points_for_object_lambda_paginator: ListAccessPointsForObjectLambdaPaginator = client.get_paginator("list_access_points_for_object_lambda")
    list_caller_access_grants_paginator: ListCallerAccessGrantsPaginator = client.get_paginator("list_caller_access_grants")
    ```
"""

from .client import S3ControlClient
from .paginator import (
    ListAccessPointsForDirectoryBucketsPaginator,
    ListAccessPointsForObjectLambdaPaginator,
    ListCallerAccessGrantsPaginator,
)

Client = S3ControlClient

__all__ = (
    "Client",
    "ListAccessPointsForDirectoryBucketsPaginator",
    "ListAccessPointsForObjectLambdaPaginator",
    "ListCallerAccessGrantsPaginator",
    "S3ControlClient",
)
