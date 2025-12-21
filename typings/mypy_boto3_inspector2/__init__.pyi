"""
Main interface for inspector2 service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_inspector2 import (
        Client,
        GetCisScanResultDetailsPaginator,
        GetClustersForImagePaginator,
        Inspector2Client,
        ListAccountPermissionsPaginator,
        ListCisScanConfigurationsPaginator,
        ListCisScanResultsAggregatedByChecksPaginator,
        ListCisScanResultsAggregatedByTargetResourcePaginator,
        ListCisScansPaginator,
        ListCoveragePaginator,
        ListCoverageStatisticsPaginator,
        ListDelegatedAdminAccountsPaginator,
        ListFiltersPaginator,
        ListFindingAggregationsPaginator,
        ListFindingsPaginator,
        ListMembersPaginator,
        ListUsageTotalsPaginator,
        SearchVulnerabilitiesPaginator,
    )

    session = Session()
    client: Inspector2Client = session.client("inspector2")

    get_cis_scan_result_details_paginator: GetCisScanResultDetailsPaginator = client.get_paginator("get_cis_scan_result_details")
    get_clusters_for_image_paginator: GetClustersForImagePaginator = client.get_paginator("get_clusters_for_image")
    list_account_permissions_paginator: ListAccountPermissionsPaginator = client.get_paginator("list_account_permissions")
    list_cis_scan_configurations_paginator: ListCisScanConfigurationsPaginator = client.get_paginator("list_cis_scan_configurations")
    list_cis_scan_results_aggregated_by_checks_paginator: ListCisScanResultsAggregatedByChecksPaginator = client.get_paginator("list_cis_scan_results_aggregated_by_checks")
    list_cis_scan_results_aggregated_by_target_resource_paginator: ListCisScanResultsAggregatedByTargetResourcePaginator = client.get_paginator("list_cis_scan_results_aggregated_by_target_resource")
    list_cis_scans_paginator: ListCisScansPaginator = client.get_paginator("list_cis_scans")
    list_coverage_paginator: ListCoveragePaginator = client.get_paginator("list_coverage")
    list_coverage_statistics_paginator: ListCoverageStatisticsPaginator = client.get_paginator("list_coverage_statistics")
    list_delegated_admin_accounts_paginator: ListDelegatedAdminAccountsPaginator = client.get_paginator("list_delegated_admin_accounts")
    list_filters_paginator: ListFiltersPaginator = client.get_paginator("list_filters")
    list_finding_aggregations_paginator: ListFindingAggregationsPaginator = client.get_paginator("list_finding_aggregations")
    list_findings_paginator: ListFindingsPaginator = client.get_paginator("list_findings")
    list_members_paginator: ListMembersPaginator = client.get_paginator("list_members")
    list_usage_totals_paginator: ListUsageTotalsPaginator = client.get_paginator("list_usage_totals")
    search_vulnerabilities_paginator: SearchVulnerabilitiesPaginator = client.get_paginator("search_vulnerabilities")
    ```
"""

from .client import Inspector2Client
from .paginator import (
    GetCisScanResultDetailsPaginator,
    GetClustersForImagePaginator,
    ListAccountPermissionsPaginator,
    ListCisScanConfigurationsPaginator,
    ListCisScanResultsAggregatedByChecksPaginator,
    ListCisScanResultsAggregatedByTargetResourcePaginator,
    ListCisScansPaginator,
    ListCoveragePaginator,
    ListCoverageStatisticsPaginator,
    ListDelegatedAdminAccountsPaginator,
    ListFiltersPaginator,
    ListFindingAggregationsPaginator,
    ListFindingsPaginator,
    ListMembersPaginator,
    ListUsageTotalsPaginator,
    SearchVulnerabilitiesPaginator,
)

Client = Inspector2Client

__all__ = (
    "Client",
    "GetCisScanResultDetailsPaginator",
    "GetClustersForImagePaginator",
    "Inspector2Client",
    "ListAccountPermissionsPaginator",
    "ListCisScanConfigurationsPaginator",
    "ListCisScanResultsAggregatedByChecksPaginator",
    "ListCisScanResultsAggregatedByTargetResourcePaginator",
    "ListCisScansPaginator",
    "ListCoveragePaginator",
    "ListCoverageStatisticsPaginator",
    "ListDelegatedAdminAccountsPaginator",
    "ListFiltersPaginator",
    "ListFindingAggregationsPaginator",
    "ListFindingsPaginator",
    "ListMembersPaginator",
    "ListUsageTotalsPaginator",
    "SearchVulnerabilitiesPaginator",
)
