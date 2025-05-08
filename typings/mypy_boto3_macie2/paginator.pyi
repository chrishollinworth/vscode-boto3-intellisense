"""
Type annotations for macie2 service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_macie2.client import Macie2Client
    from mypy_boto3_macie2.paginator import (
        DescribeBucketsPaginator,
        GetUsageStatisticsPaginator,
        ListAllowListsPaginator,
        ListAutomatedDiscoveryAccountsPaginator,
        ListClassificationJobsPaginator,
        ListClassificationScopesPaginator,
        ListCustomDataIdentifiersPaginator,
        ListFindingsFiltersPaginator,
        ListFindingsPaginator,
        ListInvitationsPaginator,
        ListManagedDataIdentifiersPaginator,
        ListMembersPaginator,
        ListOrganizationAdminAccountsPaginator,
        ListResourceProfileArtifactsPaginator,
        ListResourceProfileDetectionsPaginator,
        ListSensitivityInspectionTemplatesPaginator,
        SearchResourcesPaginator,
    )

    session = Session()
    client: Macie2Client = session.client("macie2")

    describe_buckets_paginator: DescribeBucketsPaginator = client.get_paginator("describe_buckets")
    get_usage_statistics_paginator: GetUsageStatisticsPaginator = client.get_paginator("get_usage_statistics")
    list_allow_lists_paginator: ListAllowListsPaginator = client.get_paginator("list_allow_lists")
    list_automated_discovery_accounts_paginator: ListAutomatedDiscoveryAccountsPaginator = client.get_paginator("list_automated_discovery_accounts")
    list_classification_jobs_paginator: ListClassificationJobsPaginator = client.get_paginator("list_classification_jobs")
    list_classification_scopes_paginator: ListClassificationScopesPaginator = client.get_paginator("list_classification_scopes")
    list_custom_data_identifiers_paginator: ListCustomDataIdentifiersPaginator = client.get_paginator("list_custom_data_identifiers")
    list_findings_filters_paginator: ListFindingsFiltersPaginator = client.get_paginator("list_findings_filters")
    list_findings_paginator: ListFindingsPaginator = client.get_paginator("list_findings")
    list_invitations_paginator: ListInvitationsPaginator = client.get_paginator("list_invitations")
    list_managed_data_identifiers_paginator: ListManagedDataIdentifiersPaginator = client.get_paginator("list_managed_data_identifiers")
    list_members_paginator: ListMembersPaginator = client.get_paginator("list_members")
    list_organization_admin_accounts_paginator: ListOrganizationAdminAccountsPaginator = client.get_paginator("list_organization_admin_accounts")
    list_resource_profile_artifacts_paginator: ListResourceProfileArtifactsPaginator = client.get_paginator("list_resource_profile_artifacts")
    list_resource_profile_detections_paginator: ListResourceProfileDetectionsPaginator = client.get_paginator("list_resource_profile_detections")
    list_sensitivity_inspection_templates_paginator: ListSensitivityInspectionTemplatesPaginator = client.get_paginator("list_sensitivity_inspection_templates")
    search_resources_paginator: SearchResourcesPaginator = client.get_paginator("search_resources")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeBucketsRequestPaginateTypeDef,
    DescribeBucketsResponseTypeDef,
    GetUsageStatisticsRequestPaginateTypeDef,
    GetUsageStatisticsResponseTypeDef,
    ListAllowListsRequestPaginateTypeDef,
    ListAllowListsResponseTypeDef,
    ListAutomatedDiscoveryAccountsRequestPaginateTypeDef,
    ListAutomatedDiscoveryAccountsResponseTypeDef,
    ListClassificationJobsRequestPaginateTypeDef,
    ListClassificationJobsResponseTypeDef,
    ListClassificationScopesRequestPaginateTypeDef,
    ListClassificationScopesResponseTypeDef,
    ListCustomDataIdentifiersRequestPaginateTypeDef,
    ListCustomDataIdentifiersResponseTypeDef,
    ListFindingsFiltersRequestPaginateTypeDef,
    ListFindingsFiltersResponseTypeDef,
    ListFindingsRequestPaginateTypeDef,
    ListFindingsResponseTypeDef,
    ListInvitationsRequestPaginateTypeDef,
    ListInvitationsResponseTypeDef,
    ListManagedDataIdentifiersRequestPaginateTypeDef,
    ListManagedDataIdentifiersResponseTypeDef,
    ListMembersRequestPaginateTypeDef,
    ListMembersResponseTypeDef,
    ListOrganizationAdminAccountsRequestPaginateTypeDef,
    ListOrganizationAdminAccountsResponseTypeDef,
    ListResourceProfileArtifactsRequestPaginateTypeDef,
    ListResourceProfileArtifactsResponseTypeDef,
    ListResourceProfileDetectionsRequestPaginateTypeDef,
    ListResourceProfileDetectionsResponseTypeDef,
    ListSensitivityInspectionTemplatesRequestPaginateTypeDef,
    ListSensitivityInspectionTemplatesResponseTypeDef,
    SearchResourcesRequestPaginateTypeDef,
    SearchResourcesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeBucketsPaginator",
    "GetUsageStatisticsPaginator",
    "ListAllowListsPaginator",
    "ListAutomatedDiscoveryAccountsPaginator",
    "ListClassificationJobsPaginator",
    "ListClassificationScopesPaginator",
    "ListCustomDataIdentifiersPaginator",
    "ListFindingsFiltersPaginator",
    "ListFindingsPaginator",
    "ListInvitationsPaginator",
    "ListManagedDataIdentifiersPaginator",
    "ListMembersPaginator",
    "ListOrganizationAdminAccountsPaginator",
    "ListResourceProfileArtifactsPaginator",
    "ListResourceProfileDetectionsPaginator",
    "ListSensitivityInspectionTemplatesPaginator",
    "SearchResourcesPaginator",
)

if TYPE_CHECKING:
    _DescribeBucketsPaginatorBase = Paginator[DescribeBucketsResponseTypeDef]
else:
    _DescribeBucketsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeBucketsPaginator(_DescribeBucketsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/DescribeBuckets.html#Macie2.Paginator.DescribeBuckets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#describebucketspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeBucketsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeBucketsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/DescribeBuckets.html#Macie2.Paginator.DescribeBuckets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#describebucketspaginator)
        """

if TYPE_CHECKING:
    _GetUsageStatisticsPaginatorBase = Paginator[GetUsageStatisticsResponseTypeDef]
else:
    _GetUsageStatisticsPaginatorBase = Paginator  # type: ignore[assignment]

class GetUsageStatisticsPaginator(_GetUsageStatisticsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/GetUsageStatistics.html#Macie2.Paginator.GetUsageStatistics)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#getusagestatisticspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetUsageStatisticsRequestPaginateTypeDef]
    ) -> PageIterator[GetUsageStatisticsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/GetUsageStatistics.html#Macie2.Paginator.GetUsageStatistics.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#getusagestatisticspaginator)
        """

if TYPE_CHECKING:
    _ListAllowListsPaginatorBase = Paginator[ListAllowListsResponseTypeDef]
else:
    _ListAllowListsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAllowListsPaginator(_ListAllowListsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListAllowLists.html#Macie2.Paginator.ListAllowLists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listallowlistspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAllowListsRequestPaginateTypeDef]
    ) -> PageIterator[ListAllowListsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListAllowLists.html#Macie2.Paginator.ListAllowLists.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listallowlistspaginator)
        """

if TYPE_CHECKING:
    _ListAutomatedDiscoveryAccountsPaginatorBase = Paginator[
        ListAutomatedDiscoveryAccountsResponseTypeDef
    ]
else:
    _ListAutomatedDiscoveryAccountsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAutomatedDiscoveryAccountsPaginator(_ListAutomatedDiscoveryAccountsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListAutomatedDiscoveryAccounts.html#Macie2.Paginator.ListAutomatedDiscoveryAccounts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listautomateddiscoveryaccountspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAutomatedDiscoveryAccountsRequestPaginateTypeDef]
    ) -> PageIterator[ListAutomatedDiscoveryAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListAutomatedDiscoveryAccounts.html#Macie2.Paginator.ListAutomatedDiscoveryAccounts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listautomateddiscoveryaccountspaginator)
        """

if TYPE_CHECKING:
    _ListClassificationJobsPaginatorBase = Paginator[ListClassificationJobsResponseTypeDef]
else:
    _ListClassificationJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListClassificationJobsPaginator(_ListClassificationJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListClassificationJobs.html#Macie2.Paginator.ListClassificationJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listclassificationjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListClassificationJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListClassificationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListClassificationJobs.html#Macie2.Paginator.ListClassificationJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listclassificationjobspaginator)
        """

if TYPE_CHECKING:
    _ListClassificationScopesPaginatorBase = Paginator[ListClassificationScopesResponseTypeDef]
else:
    _ListClassificationScopesPaginatorBase = Paginator  # type: ignore[assignment]

class ListClassificationScopesPaginator(_ListClassificationScopesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListClassificationScopes.html#Macie2.Paginator.ListClassificationScopes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listclassificationscopespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListClassificationScopesRequestPaginateTypeDef]
    ) -> PageIterator[ListClassificationScopesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListClassificationScopes.html#Macie2.Paginator.ListClassificationScopes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listclassificationscopespaginator)
        """

if TYPE_CHECKING:
    _ListCustomDataIdentifiersPaginatorBase = Paginator[ListCustomDataIdentifiersResponseTypeDef]
else:
    _ListCustomDataIdentifiersPaginatorBase = Paginator  # type: ignore[assignment]

class ListCustomDataIdentifiersPaginator(_ListCustomDataIdentifiersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListCustomDataIdentifiers.html#Macie2.Paginator.ListCustomDataIdentifiers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listcustomdataidentifierspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCustomDataIdentifiersRequestPaginateTypeDef]
    ) -> PageIterator[ListCustomDataIdentifiersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListCustomDataIdentifiers.html#Macie2.Paginator.ListCustomDataIdentifiers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listcustomdataidentifierspaginator)
        """

if TYPE_CHECKING:
    _ListFindingsFiltersPaginatorBase = Paginator[ListFindingsFiltersResponseTypeDef]
else:
    _ListFindingsFiltersPaginatorBase = Paginator  # type: ignore[assignment]

class ListFindingsFiltersPaginator(_ListFindingsFiltersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListFindingsFilters.html#Macie2.Paginator.ListFindingsFilters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listfindingsfilterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFindingsFiltersRequestPaginateTypeDef]
    ) -> PageIterator[ListFindingsFiltersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListFindingsFilters.html#Macie2.Paginator.ListFindingsFilters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listfindingsfilterspaginator)
        """

if TYPE_CHECKING:
    _ListFindingsPaginatorBase = Paginator[ListFindingsResponseTypeDef]
else:
    _ListFindingsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFindingsPaginator(_ListFindingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListFindings.html#Macie2.Paginator.ListFindings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listfindingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFindingsRequestPaginateTypeDef]
    ) -> PageIterator[ListFindingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListFindings.html#Macie2.Paginator.ListFindings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listfindingspaginator)
        """

if TYPE_CHECKING:
    _ListInvitationsPaginatorBase = Paginator[ListInvitationsResponseTypeDef]
else:
    _ListInvitationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListInvitationsPaginator(_ListInvitationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListInvitations.html#Macie2.Paginator.ListInvitations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listinvitationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInvitationsRequestPaginateTypeDef]
    ) -> PageIterator[ListInvitationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListInvitations.html#Macie2.Paginator.ListInvitations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listinvitationspaginator)
        """

if TYPE_CHECKING:
    _ListManagedDataIdentifiersPaginatorBase = Paginator[ListManagedDataIdentifiersResponseTypeDef]
else:
    _ListManagedDataIdentifiersPaginatorBase = Paginator  # type: ignore[assignment]

class ListManagedDataIdentifiersPaginator(_ListManagedDataIdentifiersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListManagedDataIdentifiers.html#Macie2.Paginator.ListManagedDataIdentifiers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listmanageddataidentifierspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListManagedDataIdentifiersRequestPaginateTypeDef]
    ) -> PageIterator[ListManagedDataIdentifiersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListManagedDataIdentifiers.html#Macie2.Paginator.ListManagedDataIdentifiers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listmanageddataidentifierspaginator)
        """

if TYPE_CHECKING:
    _ListMembersPaginatorBase = Paginator[ListMembersResponseTypeDef]
else:
    _ListMembersPaginatorBase = Paginator  # type: ignore[assignment]

class ListMembersPaginator(_ListMembersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListMembers.html#Macie2.Paginator.ListMembers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listmemberspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMembersRequestPaginateTypeDef]
    ) -> PageIterator[ListMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListMembers.html#Macie2.Paginator.ListMembers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listmemberspaginator)
        """

if TYPE_CHECKING:
    _ListOrganizationAdminAccountsPaginatorBase = Paginator[
        ListOrganizationAdminAccountsResponseTypeDef
    ]
else:
    _ListOrganizationAdminAccountsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOrganizationAdminAccountsPaginator(_ListOrganizationAdminAccountsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListOrganizationAdminAccounts.html#Macie2.Paginator.ListOrganizationAdminAccounts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listorganizationadminaccountspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOrganizationAdminAccountsRequestPaginateTypeDef]
    ) -> PageIterator[ListOrganizationAdminAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListOrganizationAdminAccounts.html#Macie2.Paginator.ListOrganizationAdminAccounts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listorganizationadminaccountspaginator)
        """

if TYPE_CHECKING:
    _ListResourceProfileArtifactsPaginatorBase = Paginator[
        ListResourceProfileArtifactsResponseTypeDef
    ]
else:
    _ListResourceProfileArtifactsPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceProfileArtifactsPaginator(_ListResourceProfileArtifactsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListResourceProfileArtifacts.html#Macie2.Paginator.ListResourceProfileArtifacts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listresourceprofileartifactspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceProfileArtifactsRequestPaginateTypeDef]
    ) -> PageIterator[ListResourceProfileArtifactsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListResourceProfileArtifacts.html#Macie2.Paginator.ListResourceProfileArtifacts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listresourceprofileartifactspaginator)
        """

if TYPE_CHECKING:
    _ListResourceProfileDetectionsPaginatorBase = Paginator[
        ListResourceProfileDetectionsResponseTypeDef
    ]
else:
    _ListResourceProfileDetectionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceProfileDetectionsPaginator(_ListResourceProfileDetectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListResourceProfileDetections.html#Macie2.Paginator.ListResourceProfileDetections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listresourceprofiledetectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceProfileDetectionsRequestPaginateTypeDef]
    ) -> PageIterator[ListResourceProfileDetectionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListResourceProfileDetections.html#Macie2.Paginator.ListResourceProfileDetections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listresourceprofiledetectionspaginator)
        """

if TYPE_CHECKING:
    _ListSensitivityInspectionTemplatesPaginatorBase = Paginator[
        ListSensitivityInspectionTemplatesResponseTypeDef
    ]
else:
    _ListSensitivityInspectionTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSensitivityInspectionTemplatesPaginator(_ListSensitivityInspectionTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListSensitivityInspectionTemplates.html#Macie2.Paginator.ListSensitivityInspectionTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listsensitivityinspectiontemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSensitivityInspectionTemplatesRequestPaginateTypeDef]
    ) -> PageIterator[ListSensitivityInspectionTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/ListSensitivityInspectionTemplates.html#Macie2.Paginator.ListSensitivityInspectionTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#listsensitivityinspectiontemplatespaginator)
        """

if TYPE_CHECKING:
    _SearchResourcesPaginatorBase = Paginator[SearchResourcesResponseTypeDef]
else:
    _SearchResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchResourcesPaginator(_SearchResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/SearchResources.html#Macie2.Paginator.SearchResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#searchresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchResourcesRequestPaginateTypeDef]
    ) -> PageIterator[SearchResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2/paginator/SearchResources.html#Macie2.Paginator.SearchResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators/#searchresourcespaginator)
        """
