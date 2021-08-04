"""
Main interface for mobile service.

Usage::

    ```python
    import boto3
    from mypy_boto3_mobile import (
        Client,
        ListBundlesPaginator,
        ListProjectsPaginator,
        MobileClient,
    )

    session = boto3.Session()

    client: MobileClient = boto3.client("mobile")
    session_client: MobileClient = session.client("mobile")

    list_bundles_paginator: ListBundlesPaginator = client.get_paginator("list_bundles")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    ```
"""
from .client import MobileClient
from .paginator import ListBundlesPaginator, ListProjectsPaginator

Client = MobileClient

__all__ = ("Client", "ListBundlesPaginator", "ListProjectsPaginator", "MobileClient")
