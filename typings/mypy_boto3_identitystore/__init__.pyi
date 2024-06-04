"""
Main interface for identitystore service.

Usage::

    ```python
    import boto3
    from mypy_boto3_identitystore import (
        Client,
        IdentityStoreClient,
        ListGroupMembershipsForMemberPaginator,
        ListGroupMembershipsPaginator,
        ListGroupsPaginator,
        ListUsersPaginator,
    )

    session = boto3.Session()

    client: IdentityStoreClient = boto3.client("identitystore")
    session_client: IdentityStoreClient = session.client("identitystore")

    list_group_memberships_paginator: ListGroupMembershipsPaginator = client.get_paginator("list_group_memberships")
    list_group_memberships_for_member_paginator: ListGroupMembershipsForMemberPaginator = client.get_paginator("list_group_memberships_for_member")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    ```
"""

from .client import IdentityStoreClient
from .paginator import (
    ListGroupMembershipsForMemberPaginator,
    ListGroupMembershipsPaginator,
    ListGroupsPaginator,
    ListUsersPaginator,
)

Client = IdentityStoreClient

__all__ = (
    "Client",
    "IdentityStoreClient",
    "ListGroupMembershipsForMemberPaginator",
    "ListGroupMembershipsPaginator",
    "ListGroupsPaginator",
    "ListUsersPaginator",
)
