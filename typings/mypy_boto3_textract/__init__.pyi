"""
Main interface for textract service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_textract/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_textract import (
        Client,
        ListAdapterVersionsPaginator,
        ListAdaptersPaginator,
        TextractClient,
    )

    session = Session()
    client: TextractClient = session.client("textract")

    list_adapter_versions_paginator: ListAdapterVersionsPaginator = client.get_paginator("list_adapter_versions")
    list_adapters_paginator: ListAdaptersPaginator = client.get_paginator("list_adapters")
    ```
"""

from .client import TextractClient
from .paginator import ListAdaptersPaginator, ListAdapterVersionsPaginator

Client = TextractClient

__all__ = ("Client", "ListAdapterVersionsPaginator", "ListAdaptersPaginator", "TextractClient")
