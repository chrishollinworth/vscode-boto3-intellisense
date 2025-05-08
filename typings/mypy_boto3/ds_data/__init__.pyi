"""
Main interface for ds-data service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ds_data import (
        Client,
        DirectoryServiceDataClient,
        ListGroupMembersPaginator,
        ListGroupsForMemberPaginator,
        ListGroupsPaginator,
        ListUsersPaginator,
        SearchGroupsPaginator,
        SearchUsersPaginator,
    )

    session = Session()
    client: DirectoryServiceDataClient = session.client("ds-data")

    list_group_members_paginator: ListGroupMembersPaginator = client.get_paginator("list_group_members")
    list_groups_for_member_paginator: ListGroupsForMemberPaginator = client.get_paginator("list_groups_for_member")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    search_groups_paginator: SearchGroupsPaginator = client.get_paginator("search_groups")
    search_users_paginator: SearchUsersPaginator = client.get_paginator("search_users")
    ```
"""

from .client import DirectoryServiceDataClient
from .paginator import (
    ListGroupMembersPaginator,
    ListGroupsForMemberPaginator,
    ListGroupsPaginator,
    ListUsersPaginator,
    SearchGroupsPaginator,
    SearchUsersPaginator,
)

Client = DirectoryServiceDataClient

__all__ = (
    "Client",
    "DirectoryServiceDataClient",
    "ListGroupMembersPaginator",
    "ListGroupsForMemberPaginator",
    "ListGroupsPaginator",
    "ListUsersPaginator",
    "SearchGroupsPaginator",
    "SearchUsersPaginator",
)
