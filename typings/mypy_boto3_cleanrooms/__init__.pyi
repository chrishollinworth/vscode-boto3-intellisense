"""
Main interface for cleanrooms service.

Usage::

    ```python
    import boto3
    from mypy_boto3_cleanrooms import (
        CleanRoomsServiceClient,
        Client,
        ListCollaborationsPaginator,
        ListConfiguredTableAssociationsPaginator,
        ListConfiguredTablesPaginator,
        ListMembersPaginator,
        ListMembershipsPaginator,
        ListProtectedQueriesPaginator,
        ListSchemasPaginator,
    )

    session = boto3.Session()

    client: CleanRoomsServiceClient = boto3.client("cleanrooms")
    session_client: CleanRoomsServiceClient = session.client("cleanrooms")

    list_collaborations_paginator: ListCollaborationsPaginator = client.get_paginator("list_collaborations")
    list_configured_table_associations_paginator: ListConfiguredTableAssociationsPaginator = client.get_paginator("list_configured_table_associations")
    list_configured_tables_paginator: ListConfiguredTablesPaginator = client.get_paginator("list_configured_tables")
    list_members_paginator: ListMembersPaginator = client.get_paginator("list_members")
    list_memberships_paginator: ListMembershipsPaginator = client.get_paginator("list_memberships")
    list_protected_queries_paginator: ListProtectedQueriesPaginator = client.get_paginator("list_protected_queries")
    list_schemas_paginator: ListSchemasPaginator = client.get_paginator("list_schemas")
    ```
"""
from .client import CleanRoomsServiceClient
from .paginator import (
    ListCollaborationsPaginator,
    ListConfiguredTableAssociationsPaginator,
    ListConfiguredTablesPaginator,
    ListMembershipsPaginator,
    ListMembersPaginator,
    ListProtectedQueriesPaginator,
    ListSchemasPaginator,
)

Client = CleanRoomsServiceClient

__all__ = (
    "CleanRoomsServiceClient",
    "Client",
    "ListCollaborationsPaginator",
    "ListConfiguredTableAssociationsPaginator",
    "ListConfiguredTablesPaginator",
    "ListMembersPaginator",
    "ListMembershipsPaginator",
    "ListProtectedQueriesPaginator",
    "ListSchemasPaginator",
)
