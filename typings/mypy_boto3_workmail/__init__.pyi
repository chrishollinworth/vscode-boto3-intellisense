"""
Main interface for workmail service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_workmail import (
        Client,
        ListAliasesPaginator,
        ListAvailabilityConfigurationsPaginator,
        ListGroupMembersPaginator,
        ListGroupsPaginator,
        ListMailboxPermissionsPaginator,
        ListOrganizationsPaginator,
        ListPersonalAccessTokensPaginator,
        ListResourceDelegatesPaginator,
        ListResourcesPaginator,
        ListUsersPaginator,
        WorkMailClient,
    )

    session = Session()
    client: WorkMailClient = session.client("workmail")

    list_aliases_paginator: ListAliasesPaginator = client.get_paginator("list_aliases")
    list_availability_configurations_paginator: ListAvailabilityConfigurationsPaginator = client.get_paginator("list_availability_configurations")
    list_group_members_paginator: ListGroupMembersPaginator = client.get_paginator("list_group_members")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    list_mailbox_permissions_paginator: ListMailboxPermissionsPaginator = client.get_paginator("list_mailbox_permissions")
    list_organizations_paginator: ListOrganizationsPaginator = client.get_paginator("list_organizations")
    list_personal_access_tokens_paginator: ListPersonalAccessTokensPaginator = client.get_paginator("list_personal_access_tokens")
    list_resource_delegates_paginator: ListResourceDelegatesPaginator = client.get_paginator("list_resource_delegates")
    list_resources_paginator: ListResourcesPaginator = client.get_paginator("list_resources")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    ```
"""

from .client import WorkMailClient
from .paginator import (
    ListAliasesPaginator,
    ListAvailabilityConfigurationsPaginator,
    ListGroupMembersPaginator,
    ListGroupsPaginator,
    ListMailboxPermissionsPaginator,
    ListOrganizationsPaginator,
    ListPersonalAccessTokensPaginator,
    ListResourceDelegatesPaginator,
    ListResourcesPaginator,
    ListUsersPaginator,
)

Client = WorkMailClient

__all__ = (
    "Client",
    "ListAliasesPaginator",
    "ListAvailabilityConfigurationsPaginator",
    "ListGroupMembersPaginator",
    "ListGroupsPaginator",
    "ListMailboxPermissionsPaginator",
    "ListOrganizationsPaginator",
    "ListPersonalAccessTokensPaginator",
    "ListResourceDelegatesPaginator",
    "ListResourcesPaginator",
    "ListUsersPaginator",
    "WorkMailClient",
)
