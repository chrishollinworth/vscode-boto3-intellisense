"""
Main interface for identitystore service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_identitystore/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_identitystore import (
        Client,
        IdentityStoreClient,
        ListGroupMembershipsForMemberPaginator,
        ListGroupMembershipsPaginator,
        ListGroupsPaginator,
        ListUsersPaginator,
    )

    session = Session()
    client: IdentityStoreClient = session.client("identitystore")

    list_group_memberships_for_member_paginator: ListGroupMembershipsForMemberPaginator = client.get_paginator("list_group_memberships_for_member")
    list_group_memberships_paginator: ListGroupMembershipsPaginator = client.get_paginator("list_group_memberships")
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
