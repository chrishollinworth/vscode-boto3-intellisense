"""
Type annotations for inspector2 service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_inspector2.client import Inspector2Client
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

    session = Session()
    client: Inspector2Client = session.client("inspector2")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetCisScanResultDetailsRequestPaginateTypeDef,
    GetCisScanResultDetailsResponseTypeDef,
    ListAccountPermissionsRequestPaginateTypeDef,
    ListAccountPermissionsResponseTypeDef,
    ListCisScanConfigurationsRequestPaginateTypeDef,
    ListCisScanConfigurationsResponseTypeDef,
    ListCisScanResultsAggregatedByChecksRequestPaginateTypeDef,
    ListCisScanResultsAggregatedByChecksResponseTypeDef,
    ListCisScanResultsAggregatedByTargetResourceRequestPaginateTypeDef,
    ListCisScanResultsAggregatedByTargetResourceResponseTypeDef,
    ListCisScansRequestPaginateTypeDef,
    ListCisScansResponseTypeDef,
    ListCoverageRequestPaginateTypeDef,
    ListCoverageResponseTypeDef,
    ListCoverageStatisticsRequestPaginateTypeDef,
    ListCoverageStatisticsResponseTypeDef,
    ListDelegatedAdminAccountsRequestPaginateTypeDef,
    ListDelegatedAdminAccountsResponseTypeDef,
    ListFiltersRequestPaginateTypeDef,
    ListFiltersResponseTypeDef,
    ListFindingAggregationsRequestPaginateTypeDef,
    ListFindingAggregationsResponseTypeDef,
    ListFindingsRequestPaginateTypeDef,
    ListFindingsResponseTypeDef,
    ListMembersRequestPaginateTypeDef,
    ListMembersResponseTypeDef,
    ListUsageTotalsRequestPaginateTypeDef,
    ListUsageTotalsResponseTypeDef,
    SearchVulnerabilitiesRequestPaginateTypeDef,
    SearchVulnerabilitiesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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

if TYPE_CHECKING:
    _GetCisScanResultDetailsPaginatorBase = Paginator[GetCisScanResultDetailsResponseTypeDef]
else:
    _GetCisScanResultDetailsPaginatorBase = Paginator  # type: ignore[assignment]

class GetCisScanResultDetailsPaginator(_GetCisScanResultDetailsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/GetCisScanResultDetails.html#Inspector2.Paginator.GetCisScanResultDetails)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#getcisscanresultdetailspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetCisScanResultDetailsRequestPaginateTypeDef]
    ) -> PageIterator[GetCisScanResultDetailsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/GetCisScanResultDetails.html#Inspector2.Paginator.GetCisScanResultDetails.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#getcisscanresultdetailspaginator)
        """

if TYPE_CHECKING:
    _ListAccountPermissionsPaginatorBase = Paginator[ListAccountPermissionsResponseTypeDef]
else:
    _ListAccountPermissionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccountPermissionsPaginator(_ListAccountPermissionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListAccountPermissions.html#Inspector2.Paginator.ListAccountPermissions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listaccountpermissionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccountPermissionsRequestPaginateTypeDef]
    ) -> PageIterator[ListAccountPermissionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListAccountPermissions.html#Inspector2.Paginator.ListAccountPermissions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listaccountpermissionspaginator)
        """

if TYPE_CHECKING:
    _ListCisScanConfigurationsPaginatorBase = Paginator[ListCisScanConfigurationsResponseTypeDef]
else:
    _ListCisScanConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCisScanConfigurationsPaginator(_ListCisScanConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListCisScanConfigurations.html#Inspector2.Paginator.ListCisScanConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listcisscanconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCisScanConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListCisScanConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListCisScanConfigurations.html#Inspector2.Paginator.ListCisScanConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listcisscanconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListCisScanResultsAggregatedByChecksPaginatorBase = Paginator[
        ListCisScanResultsAggregatedByChecksResponseTypeDef
    ]
else:
    _ListCisScanResultsAggregatedByChecksPaginatorBase = Paginator  # type: ignore[assignment]

class ListCisScanResultsAggregatedByChecksPaginator(
    _ListCisScanResultsAggregatedByChecksPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListCisScanResultsAggregatedByChecks.html#Inspector2.Paginator.ListCisScanResultsAggregatedByChecks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listcisscanresultsaggregatedbycheckspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCisScanResultsAggregatedByChecksRequestPaginateTypeDef]
    ) -> PageIterator[ListCisScanResultsAggregatedByChecksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListCisScanResultsAggregatedByChecks.html#Inspector2.Paginator.ListCisScanResultsAggregatedByChecks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listcisscanresultsaggregatedbycheckspaginator)
        """

if TYPE_CHECKING:
    _ListCisScanResultsAggregatedByTargetResourcePaginatorBase = Paginator[
        ListCisScanResultsAggregatedByTargetResourceResponseTypeDef
    ]
else:
    _ListCisScanResultsAggregatedByTargetResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListCisScanResultsAggregatedByTargetResourcePaginator(
    _ListCisScanResultsAggregatedByTargetResourcePaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListCisScanResultsAggregatedByTargetResource.html#Inspector2.Paginator.ListCisScanResultsAggregatedByTargetResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listcisscanresultsaggregatedbytargetresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCisScanResultsAggregatedByTargetResourceRequestPaginateTypeDef]
    ) -> PageIterator[ListCisScanResultsAggregatedByTargetResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListCisScanResultsAggregatedByTargetResource.html#Inspector2.Paginator.ListCisScanResultsAggregatedByTargetResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listcisscanresultsaggregatedbytargetresourcepaginator)
        """

if TYPE_CHECKING:
    _ListCisScansPaginatorBase = Paginator[ListCisScansResponseTypeDef]
else:
    _ListCisScansPaginatorBase = Paginator  # type: ignore[assignment]

class ListCisScansPaginator(_ListCisScansPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListCisScans.html#Inspector2.Paginator.ListCisScans)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listcisscanspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCisScansRequestPaginateTypeDef]
    ) -> PageIterator[ListCisScansResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListCisScans.html#Inspector2.Paginator.ListCisScans.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listcisscanspaginator)
        """

if TYPE_CHECKING:
    _ListCoveragePaginatorBase = Paginator[ListCoverageResponseTypeDef]
else:
    _ListCoveragePaginatorBase = Paginator  # type: ignore[assignment]

class ListCoveragePaginator(_ListCoveragePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListCoverage.html#Inspector2.Paginator.ListCoverage)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listcoveragepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCoverageRequestPaginateTypeDef]
    ) -> PageIterator[ListCoverageResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListCoverage.html#Inspector2.Paginator.ListCoverage.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listcoveragepaginator)
        """

if TYPE_CHECKING:
    _ListCoverageStatisticsPaginatorBase = Paginator[ListCoverageStatisticsResponseTypeDef]
else:
    _ListCoverageStatisticsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCoverageStatisticsPaginator(_ListCoverageStatisticsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListCoverageStatistics.html#Inspector2.Paginator.ListCoverageStatistics)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listcoveragestatisticspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCoverageStatisticsRequestPaginateTypeDef]
    ) -> PageIterator[ListCoverageStatisticsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListCoverageStatistics.html#Inspector2.Paginator.ListCoverageStatistics.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listcoveragestatisticspaginator)
        """

if TYPE_CHECKING:
    _ListDelegatedAdminAccountsPaginatorBase = Paginator[ListDelegatedAdminAccountsResponseTypeDef]
else:
    _ListDelegatedAdminAccountsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDelegatedAdminAccountsPaginator(_ListDelegatedAdminAccountsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListDelegatedAdminAccounts.html#Inspector2.Paginator.ListDelegatedAdminAccounts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listdelegatedadminaccountspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDelegatedAdminAccountsRequestPaginateTypeDef]
    ) -> PageIterator[ListDelegatedAdminAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListDelegatedAdminAccounts.html#Inspector2.Paginator.ListDelegatedAdminAccounts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listdelegatedadminaccountspaginator)
        """

if TYPE_CHECKING:
    _ListFiltersPaginatorBase = Paginator[ListFiltersResponseTypeDef]
else:
    _ListFiltersPaginatorBase = Paginator  # type: ignore[assignment]

class ListFiltersPaginator(_ListFiltersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListFilters.html#Inspector2.Paginator.ListFilters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listfilterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFiltersRequestPaginateTypeDef]
    ) -> PageIterator[ListFiltersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListFilters.html#Inspector2.Paginator.ListFilters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listfilterspaginator)
        """

if TYPE_CHECKING:
    _ListFindingAggregationsPaginatorBase = Paginator[ListFindingAggregationsResponseTypeDef]
else:
    _ListFindingAggregationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFindingAggregationsPaginator(_ListFindingAggregationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListFindingAggregations.html#Inspector2.Paginator.ListFindingAggregations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listfindingaggregationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFindingAggregationsRequestPaginateTypeDef]
    ) -> PageIterator[ListFindingAggregationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListFindingAggregations.html#Inspector2.Paginator.ListFindingAggregations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listfindingaggregationspaginator)
        """

if TYPE_CHECKING:
    _ListFindingsPaginatorBase = Paginator[ListFindingsResponseTypeDef]
else:
    _ListFindingsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFindingsPaginator(_ListFindingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListFindings.html#Inspector2.Paginator.ListFindings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listfindingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFindingsRequestPaginateTypeDef]
    ) -> PageIterator[ListFindingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListFindings.html#Inspector2.Paginator.ListFindings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listfindingspaginator)
        """

if TYPE_CHECKING:
    _ListMembersPaginatorBase = Paginator[ListMembersResponseTypeDef]
else:
    _ListMembersPaginatorBase = Paginator  # type: ignore[assignment]

class ListMembersPaginator(_ListMembersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListMembers.html#Inspector2.Paginator.ListMembers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listmemberspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMembersRequestPaginateTypeDef]
    ) -> PageIterator[ListMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListMembers.html#Inspector2.Paginator.ListMembers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listmemberspaginator)
        """

if TYPE_CHECKING:
    _ListUsageTotalsPaginatorBase = Paginator[ListUsageTotalsResponseTypeDef]
else:
    _ListUsageTotalsPaginatorBase = Paginator  # type: ignore[assignment]

class ListUsageTotalsPaginator(_ListUsageTotalsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListUsageTotals.html#Inspector2.Paginator.ListUsageTotals)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listusagetotalspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUsageTotalsRequestPaginateTypeDef]
    ) -> PageIterator[ListUsageTotalsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/ListUsageTotals.html#Inspector2.Paginator.ListUsageTotals.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#listusagetotalspaginator)
        """

if TYPE_CHECKING:
    _SearchVulnerabilitiesPaginatorBase = Paginator[SearchVulnerabilitiesResponseTypeDef]
else:
    _SearchVulnerabilitiesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchVulnerabilitiesPaginator(_SearchVulnerabilitiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/SearchVulnerabilities.html#Inspector2.Paginator.SearchVulnerabilities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#searchvulnerabilitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchVulnerabilitiesRequestPaginateTypeDef]
    ) -> PageIterator[SearchVulnerabilitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/paginator/SearchVulnerabilities.html#Inspector2.Paginator.SearchVulnerabilities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/paginators/#searchvulnerabilitiespaginator)
        """
