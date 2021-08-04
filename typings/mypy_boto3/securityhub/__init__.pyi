"""
Main interface for securityhub service.

Usage::

    ```python
    import boto3
    from mypy_boto3_securityhub import (
        Client,
        GetEnabledStandardsPaginator,
        GetFindingsPaginator,
        GetInsightsPaginator,
        ListEnabledProductsForImportPaginator,
        ListInvitationsPaginator,
        ListMembersPaginator,
        SecurityHubClient,
    )

    session = boto3.Session()

    client: SecurityHubClient = boto3.client("securityhub")
    session_client: SecurityHubClient = session.client("securityhub")

    get_enabled_standards_paginator: GetEnabledStandardsPaginator = client.get_paginator("get_enabled_standards")
    get_findings_paginator: GetFindingsPaginator = client.get_paginator("get_findings")
    get_insights_paginator: GetInsightsPaginator = client.get_paginator("get_insights")
    list_enabled_products_for_import_paginator: ListEnabledProductsForImportPaginator = client.get_paginator("list_enabled_products_for_import")
    list_invitations_paginator: ListInvitationsPaginator = client.get_paginator("list_invitations")
    list_members_paginator: ListMembersPaginator = client.get_paginator("list_members")
    ```
"""
from .client import SecurityHubClient
from .paginator import (
    GetEnabledStandardsPaginator,
    GetFindingsPaginator,
    GetInsightsPaginator,
    ListEnabledProductsForImportPaginator,
    ListInvitationsPaginator,
    ListMembersPaginator,
)

Client = SecurityHubClient

__all__ = (
    "Client",
    "GetEnabledStandardsPaginator",
    "GetFindingsPaginator",
    "GetInsightsPaginator",
    "ListEnabledProductsForImportPaginator",
    "ListInvitationsPaginator",
    "ListMembersPaginator",
    "SecurityHubClient",
)
