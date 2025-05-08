"""
Main interface for qapps service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_qapps import (
        Client,
        ListLibraryItemsPaginator,
        ListQAppsPaginator,
        QAppsClient,
    )

    session = Session()
    client: QAppsClient = session.client("qapps")

    list_library_items_paginator: ListLibraryItemsPaginator = client.get_paginator("list_library_items")
    list_q_apps_paginator: ListQAppsPaginator = client.get_paginator("list_q_apps")
    ```
"""

from .client import QAppsClient
from .paginator import ListLibraryItemsPaginator, ListQAppsPaginator

Client = QAppsClient

__all__ = ("Client", "ListLibraryItemsPaginator", "ListQAppsPaginator", "QAppsClient")
