"""
Main interface for inspector2 service.

Usage::

    ```python
    import boto3
    from mypy_boto3_inspector2 import (
        Client,
        Inspector2Client,
        ListAccountPermissionsPaginator,
        ListCoveragePaginator,
        ListCoverageStatisticsPaginator,
        ListDelegatedAdminAccountsPaginator,
        ListFiltersPaginator,
        ListFindingAggregationsPaginator,
        ListFindingsPaginator,
        ListMembersPaginator,
        ListUsageTotalsPaginator,
    )

    session = boto3.Session()

    client: Inspector2Client = boto3.client("inspector2")
    session_client: Inspector2Client = session.client("inspector2")

    list_account_permissions_paginator: ListAccountPermissionsPaginator = client.get_paginator("list_account_permissions")
    list_coverage_paginator: ListCoveragePaginator = client.get_paginator("list_coverage")
    list_coverage_statistics_paginator: ListCoverageStatisticsPaginator = client.get_paginator("list_coverage_statistics")
    list_delegated_admin_accounts_paginator: ListDelegatedAdminAccountsPaginator = client.get_paginator("list_delegated_admin_accounts")
    list_filters_paginator: ListFiltersPaginator = client.get_paginator("list_filters")
    list_finding_aggregations_paginator: ListFindingAggregationsPaginator = client.get_paginator("list_finding_aggregations")
    list_findings_paginator: ListFindingsPaginator = client.get_paginator("list_findings")
    list_members_paginator: ListMembersPaginator = client.get_paginator("list_members")
    list_usage_totals_paginator: ListUsageTotalsPaginator = client.get_paginator("list_usage_totals")
    ```
"""
from .client import Inspector2Client
from .paginator import (
    ListAccountPermissionsPaginator,
    ListCoveragePaginator,
    ListCoverageStatisticsPaginator,
    ListDelegatedAdminAccountsPaginator,
    ListFiltersPaginator,
    ListFindingAggregationsPaginator,
    ListFindingsPaginator,
    ListMembersPaginator,
    ListUsageTotalsPaginator,
)

Client = Inspector2Client

__all__ = (
    "Client",
    "Inspector2Client",
    "ListAccountPermissionsPaginator",
    "ListCoveragePaginator",
    "ListCoverageStatisticsPaginator",
    "ListDelegatedAdminAccountsPaginator",
    "ListFiltersPaginator",
    "ListFindingAggregationsPaginator",
    "ListFindingsPaginator",
    "ListMembersPaginator",
    "ListUsageTotalsPaginator",
)
