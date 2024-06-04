"""
Main interface for cloudfront-keyvaluestore service.

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudfront_keyvaluestore import (
        Client,
        CloudFrontKeyValueStoreClient,
        ListKeysPaginator,
    )

    session = boto3.Session()

    client: CloudFrontKeyValueStoreClient = boto3.client("cloudfront-keyvaluestore")
    session_client: CloudFrontKeyValueStoreClient = session.client("cloudfront-keyvaluestore")

    list_keys_paginator: ListKeysPaginator = client.get_paginator("list_keys")
    ```
"""

from .client import CloudFrontKeyValueStoreClient
from .paginator import ListKeysPaginator

Client = CloudFrontKeyValueStoreClient

__all__ = ("Client", "CloudFrontKeyValueStoreClient", "ListKeysPaginator")
