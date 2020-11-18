"""
Main interface for s3outposts service.

Usage::

    ```python
    import boto3
    from mypy_boto3_s3outposts import (
        Client,
        ListEndpointsPaginator,
        S3OutpostsClient,
    )

    session = boto3.Session()

    client: S3OutpostsClient = boto3.client("s3outposts")
    session_client: S3OutpostsClient = session.client("s3outposts")

    list_endpoints_paginator: ListEndpointsPaginator = client.get_paginator("list_endpoints")
    ```
"""
from mypy_boto3_s3outposts.client import S3OutpostsClient
from mypy_boto3_s3outposts.paginator import ListEndpointsPaginator

Client = S3OutpostsClient


__all__ = ("Client", "ListEndpointsPaginator", "S3OutpostsClient")
