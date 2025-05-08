"""
Main interface for opensearch service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearch/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_opensearch import (
        Client,
        ListApplicationsPaginator,
        OpenSearchServiceClient,
    )

    session = Session()
    client: OpenSearchServiceClient = session.client("opensearch")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    ```
"""

from .client import OpenSearchServiceClient
from .paginator import ListApplicationsPaginator

Client = OpenSearchServiceClient

__all__ = ("Client", "ListApplicationsPaginator", "OpenSearchServiceClient")
