"""
Main interface for cloudfront-keyvaluestore service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cloudfront_keyvaluestore import (
        Client,
        CloudFrontKeyValueStoreClient,
        ListKeysPaginator,
    )

    session = Session()
    client: CloudFrontKeyValueStoreClient = session.client("cloudfront-keyvaluestore")

    list_keys_paginator: ListKeysPaginator = client.get_paginator("list_keys")
    ```
"""

from .client import CloudFrontKeyValueStoreClient
from .paginator import ListKeysPaginator

Client = CloudFrontKeyValueStoreClient

__all__ = ("Client", "CloudFrontKeyValueStoreClient", "ListKeysPaginator")
