"""
Main interface for textract service.

Usage::

    ```python
    import boto3
    from mypy_boto3_textract import (
        Client,
        ListAdapterVersionsPaginator,
        ListAdaptersPaginator,
        TextractClient,
    )

    session = boto3.Session()

    client: TextractClient = boto3.client("textract")
    session_client: TextractClient = session.client("textract")

    list_adapter_versions_paginator: ListAdapterVersionsPaginator = client.get_paginator("list_adapter_versions")
    list_adapters_paginator: ListAdaptersPaginator = client.get_paginator("list_adapters")
    ```
"""
from .client import TextractClient
from .paginator import ListAdaptersPaginator, ListAdapterVersionsPaginator

Client = TextractClient

__all__ = ("Client", "ListAdapterVersionsPaginator", "ListAdaptersPaginator", "TextractClient")
