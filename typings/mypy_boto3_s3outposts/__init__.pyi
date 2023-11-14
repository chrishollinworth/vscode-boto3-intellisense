"""
Main interface for s3outposts service.

Usage::

    ```python
    import boto3
    from mypy_boto3_s3outposts import (
        Client,
        ListEndpointsPaginator,
        ListOutpostsWithS3Paginator,
        ListSharedEndpointsPaginator,
        S3OutpostsClient,
    )

    session = boto3.Session()

    client: S3OutpostsClient = boto3.client("s3outposts")
    session_client: S3OutpostsClient = session.client("s3outposts")

    list_endpoints_paginator: ListEndpointsPaginator = client.get_paginator("list_endpoints")
    list_outposts_with_s3_paginator: ListOutpostsWithS3Paginator = client.get_paginator("list_outposts_with_s3")
    list_shared_endpoints_paginator: ListSharedEndpointsPaginator = client.get_paginator("list_shared_endpoints")
    ```
"""
from .client import S3OutpostsClient
from .paginator import (
    ListEndpointsPaginator,
    ListOutpostsWithS3Paginator,
    ListSharedEndpointsPaginator,
)

Client = S3OutpostsClient

__all__ = (
    "Client",
    "ListEndpointsPaginator",
    "ListOutpostsWithS3Paginator",
    "ListSharedEndpointsPaginator",
    "S3OutpostsClient",
)
