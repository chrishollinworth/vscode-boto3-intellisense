"""
Main interface for finspace-data service.

Usage::

    ```python
    import boto3
    from mypy_boto3_finspace_data import (
        Client,
        FinSpaceDataClient,
        ListChangesetsPaginator,
        ListDataViewsPaginator,
        ListDatasetsPaginator,
        ListPermissionGroupsPaginator,
        ListUsersPaginator,
    )

    session = boto3.Session()

    client: FinSpaceDataClient = boto3.client("finspace-data")
    session_client: FinSpaceDataClient = session.client("finspace-data")

    list_changesets_paginator: ListChangesetsPaginator = client.get_paginator("list_changesets")
    list_data_views_paginator: ListDataViewsPaginator = client.get_paginator("list_data_views")
    list_datasets_paginator: ListDatasetsPaginator = client.get_paginator("list_datasets")
    list_permission_groups_paginator: ListPermissionGroupsPaginator = client.get_paginator("list_permission_groups")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    ```
"""

from .client import FinSpaceDataClient
from .paginator import (
    ListChangesetsPaginator,
    ListDatasetsPaginator,
    ListDataViewsPaginator,
    ListPermissionGroupsPaginator,
    ListUsersPaginator,
)

Client = FinSpaceDataClient

__all__ = (
    "Client",
    "FinSpaceDataClient",
    "ListChangesetsPaginator",
    "ListDataViewsPaginator",
    "ListDatasetsPaginator",
    "ListPermissionGroupsPaginator",
    "ListUsersPaginator",
)
