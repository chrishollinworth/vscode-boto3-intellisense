"""
Type annotations for inspector2 service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_inspector2 import Inspector2Client
    from mypy_boto3_inspector2.paginator import (
        GetCisScanResultDetailsPaginator,
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

    client: Inspector2Client = boto3.client("inspector2")

    get_cis_scan_result_details_paginator: GetCisScanResultDetailsPaginator = client.get_paginator("get_cis_scan_result_details")
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

from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    AggregationTypeType,
    CisScanConfigurationsSortByType,
    CisScanResultDetailsSortByType,
    CisScanResultsAggregatedByChecksSortByType,
    CisScanResultsAggregatedByTargetResourceSortByType,
    CisSortOrderType,
    FilterActionType,
    GroupKeyType,
    ListCisScansDetailLevelType,
    ListCisScansSortByType,
    ServiceType,
)
from .type_defs import (
    AggregationRequestTypeDef,
    CisScanResultDetailsFilterCriteriaTypeDef,
    CisScanResultsAggregatedByChecksFilterCriteriaTypeDef,
    CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef,
    CoverageFilterCriteriaTypeDef,
    FilterCriteriaTypeDef,
    GetCisScanResultDetailsResponseTypeDef,
    ListAccountPermissionsResponseTypeDef,
    ListCisScanConfigurationsFilterCriteriaTypeDef,
    ListCisScanConfigurationsResponseTypeDef,
    ListCisScanResultsAggregatedByChecksResponseTypeDef,
    ListCisScanResultsAggregatedByTargetResourceResponseTypeDef,
    ListCisScansFilterCriteriaTypeDef,
    ListCisScansResponseTypeDef,
    ListCoverageResponseTypeDef,
    ListCoverageStatisticsResponseTypeDef,
    ListDelegatedAdminAccountsResponseTypeDef,
    ListFiltersResponseTypeDef,
    ListFindingAggregationsResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListMembersResponseTypeDef,
    ListUsageTotalsResponseTypeDef,
    PaginatorConfigTypeDef,
    SearchVulnerabilitiesFilterCriteriaTypeDef,
    SearchVulnerabilitiesResponseTypeDef,
    SortCriteriaTypeDef,
    StringFilterTypeDef,
)

__all__ = (
    "GetCisScanResultDetailsPaginator",
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

class GetCisScanResultDetailsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.GetCisScanResultDetails)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#getcisscanresultdetailspaginator)
    """

    def paginate(
        self,
        *,
        accountId: str,
        scanArn: str,
        targetResourceId: str,
        filterCriteria: "CisScanResultDetailsFilterCriteriaTypeDef" = None,
        sortBy: CisScanResultDetailsSortByType = None,
        sortOrder: CisSortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetCisScanResultDetailsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.GetCisScanResultDetails.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#getcisscanresultdetailspaginator)
        """

class ListAccountPermissionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListAccountPermissions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listaccountpermissionspaginator)
    """

    def paginate(
        self, *, service: ServiceType = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountPermissionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListAccountPermissions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listaccountpermissionspaginator)
        """

class ListCisScanConfigurationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListCisScanConfigurations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listcisscanconfigurationspaginator)
    """

    def paginate(
        self,
        *,
        filterCriteria: "ListCisScanConfigurationsFilterCriteriaTypeDef" = None,
        sortBy: CisScanConfigurationsSortByType = None,
        sortOrder: CisSortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCisScanConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListCisScanConfigurations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listcisscanconfigurationspaginator)
        """

class ListCisScanResultsAggregatedByChecksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListCisScanResultsAggregatedByChecks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listcisscanresultsaggregatedbycheckspaginator)
    """

    def paginate(
        self,
        *,
        scanArn: str,
        filterCriteria: "CisScanResultsAggregatedByChecksFilterCriteriaTypeDef" = None,
        sortBy: CisScanResultsAggregatedByChecksSortByType = None,
        sortOrder: CisSortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCisScanResultsAggregatedByChecksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListCisScanResultsAggregatedByChecks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listcisscanresultsaggregatedbycheckspaginator)
        """

class ListCisScanResultsAggregatedByTargetResourcePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListCisScanResultsAggregatedByTargetResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listcisscanresultsaggregatedbytargetresourcepaginator)
    """

    def paginate(
        self,
        *,
        scanArn: str,
        filterCriteria: "CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef" = None,
        sortBy: CisScanResultsAggregatedByTargetResourceSortByType = None,
        sortOrder: CisSortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCisScanResultsAggregatedByTargetResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListCisScanResultsAggregatedByTargetResource.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listcisscanresultsaggregatedbytargetresourcepaginator)
        """

class ListCisScansPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListCisScans)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listcisscanspaginator)
    """

    def paginate(
        self,
        *,
        detailLevel: ListCisScansDetailLevelType = None,
        filterCriteria: "ListCisScansFilterCriteriaTypeDef" = None,
        sortBy: ListCisScansSortByType = None,
        sortOrder: CisSortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCisScansResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListCisScans.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listcisscanspaginator)
        """

class ListCoveragePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListCoverage)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listcoveragepaginator)
    """

    def paginate(
        self,
        *,
        filterCriteria: "CoverageFilterCriteriaTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCoverageResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListCoverage.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listcoveragepaginator)
        """

class ListCoverageStatisticsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListCoverageStatistics)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listcoveragestatisticspaginator)
    """

    def paginate(
        self,
        *,
        filterCriteria: "CoverageFilterCriteriaTypeDef" = None,
        groupBy: GroupKeyType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCoverageStatisticsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListCoverageStatistics.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listcoveragestatisticspaginator)
        """

class ListDelegatedAdminAccountsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListDelegatedAdminAccounts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listdelegatedadminaccountspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDelegatedAdminAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListDelegatedAdminAccounts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listdelegatedadminaccountspaginator)
        """

class ListFiltersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListFilters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listfilterspaginator)
    """

    def paginate(
        self,
        *,
        action: FilterActionType = None,
        arns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFiltersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListFilters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listfilterspaginator)
        """

class ListFindingAggregationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListFindingAggregations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listfindingaggregationspaginator)
    """

    def paginate(
        self,
        *,
        aggregationType: AggregationTypeType,
        accountIds: List["StringFilterTypeDef"] = None,
        aggregationRequest: "AggregationRequestTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFindingAggregationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListFindingAggregations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listfindingaggregationspaginator)
        """

class ListFindingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListFindings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listfindingspaginator)
    """

    def paginate(
        self,
        *,
        filterCriteria: "FilterCriteriaTypeDef" = None,
        sortCriteria: "SortCriteriaTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFindingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListFindings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listfindingspaginator)
        """

class ListMembersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListMembers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listmemberspaginator)
    """

    def paginate(
        self, *, onlyAssociated: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListMembers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listmemberspaginator)
        """

class ListUsageTotalsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListUsageTotals)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listusagetotalspaginator)
    """

    def paginate(
        self, *, accountIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUsageTotalsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.ListUsageTotals.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#listusagetotalspaginator)
        """

class SearchVulnerabilitiesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.SearchVulnerabilities)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#searchvulnerabilitiespaginator)
    """

    def paginate(
        self,
        *,
        filterCriteria: "SearchVulnerabilitiesFilterCriteriaTypeDef",
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchVulnerabilitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/inspector2.html#Inspector2.Paginator.SearchVulnerabilities.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators.html#searchvulnerabilitiespaginator)
        """
