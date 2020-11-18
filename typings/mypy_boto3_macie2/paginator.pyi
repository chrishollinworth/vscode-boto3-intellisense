# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for macie2 service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_macie2 import Macie2Client
    from mypy_boto3_macie2.paginator import (
        DescribeBucketsPaginator,
        GetUsageStatisticsPaginator,
        ListClassificationJobsPaginator,
        ListCustomDataIdentifiersPaginator,
        ListFindingsPaginator,
        ListFindingsFiltersPaginator,
        ListInvitationsPaginator,
        ListMembersPaginator,
        ListOrganizationAdminAccountsPaginator,
    )

    client: Macie2Client = boto3.client("macie2")

    describe_buckets_paginator: DescribeBucketsPaginator = client.get_paginator("describe_buckets")
    get_usage_statistics_paginator: GetUsageStatisticsPaginator = client.get_paginator("get_usage_statistics")
    list_classification_jobs_paginator: ListClassificationJobsPaginator = client.get_paginator("list_classification_jobs")
    list_custom_data_identifiers_paginator: ListCustomDataIdentifiersPaginator = client.get_paginator("list_custom_data_identifiers")
    list_findings_paginator: ListFindingsPaginator = client.get_paginator("list_findings")
    list_findings_filters_paginator: ListFindingsFiltersPaginator = client.get_paginator("list_findings_filters")
    list_invitations_paginator: ListInvitationsPaginator = client.get_paginator("list_invitations")
    list_members_paginator: ListMembersPaginator = client.get_paginator("list_members")
    list_organization_admin_accounts_paginator: ListOrganizationAdminAccountsPaginator = client.get_paginator("list_organization_admin_accounts")
    ```
"""
from typing import Dict, Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_macie2.type_defs import (
    BucketCriteriaAdditionalPropertiesTypeDef,
    BucketSortCriteriaTypeDef,
    DescribeBucketsResponseTypeDef,
    FindingCriteriaTypeDef,
    GetUsageStatisticsResponseTypeDef,
    ListClassificationJobsResponseTypeDef,
    ListCustomDataIdentifiersResponseTypeDef,
    ListFindingsFiltersResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListJobsFilterCriteriaTypeDef,
    ListJobsSortCriteriaTypeDef,
    ListMembersResponseTypeDef,
    ListOrganizationAdminAccountsResponseTypeDef,
    PaginatorConfigTypeDef,
    SortCriteriaTypeDef,
    UsageStatisticsFilterTypeDef,
    UsageStatisticsSortByTypeDef,
)

__all__ = (
    "DescribeBucketsPaginator",
    "GetUsageStatisticsPaginator",
    "ListClassificationJobsPaginator",
    "ListCustomDataIdentifiersPaginator",
    "ListFindingsPaginator",
    "ListFindingsFiltersPaginator",
    "ListInvitationsPaginator",
    "ListMembersPaginator",
    "ListOrganizationAdminAccountsPaginator",
)


class DescribeBucketsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeBuckets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie2.html#Macie2.Paginator.DescribeBuckets)
    """

    def paginate(
        self,
        criteria: Dict[str, BucketCriteriaAdditionalPropertiesTypeDef] = None,
        sortCriteria: BucketSortCriteriaTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeBucketsResponseTypeDef]:
        """
        [DescribeBuckets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie2.html#Macie2.Paginator.DescribeBuckets.paginate)
        """


class GetUsageStatisticsPaginator(Boto3Paginator):
    """
    [Paginator.GetUsageStatistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie2.html#Macie2.Paginator.GetUsageStatistics)
    """

    def paginate(
        self,
        filterBy: List[UsageStatisticsFilterTypeDef] = None,
        sortBy: UsageStatisticsSortByTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetUsageStatisticsResponseTypeDef]:
        """
        [GetUsageStatistics.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie2.html#Macie2.Paginator.GetUsageStatistics.paginate)
        """


class ListClassificationJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListClassificationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie2.html#Macie2.Paginator.ListClassificationJobs)
    """

    def paginate(
        self,
        filterCriteria: ListJobsFilterCriteriaTypeDef = None,
        sortCriteria: ListJobsSortCriteriaTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListClassificationJobsResponseTypeDef]:
        """
        [ListClassificationJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie2.html#Macie2.Paginator.ListClassificationJobs.paginate)
        """


class ListCustomDataIdentifiersPaginator(Boto3Paginator):
    """
    [Paginator.ListCustomDataIdentifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie2.html#Macie2.Paginator.ListCustomDataIdentifiers)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCustomDataIdentifiersResponseTypeDef]:
        """
        [ListCustomDataIdentifiers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie2.html#Macie2.Paginator.ListCustomDataIdentifiers.paginate)
        """


class ListFindingsPaginator(Boto3Paginator):
    """
    [Paginator.ListFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie2.html#Macie2.Paginator.ListFindings)
    """

    def paginate(
        self,
        findingCriteria: "FindingCriteriaTypeDef" = None,
        sortCriteria: SortCriteriaTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListFindingsResponseTypeDef]:
        """
        [ListFindings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie2.html#Macie2.Paginator.ListFindings.paginate)
        """


class ListFindingsFiltersPaginator(Boto3Paginator):
    """
    [Paginator.ListFindingsFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie2.html#Macie2.Paginator.ListFindingsFilters)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFindingsFiltersResponseTypeDef]:
        """
        [ListFindingsFilters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie2.html#Macie2.Paginator.ListFindingsFilters.paginate)
        """


class ListInvitationsPaginator(Boto3Paginator):
    """
    [Paginator.ListInvitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie2.html#Macie2.Paginator.ListInvitations)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInvitationsResponseTypeDef]:
        """
        [ListInvitations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie2.html#Macie2.Paginator.ListInvitations.paginate)
        """


class ListMembersPaginator(Boto3Paginator):
    """
    [Paginator.ListMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie2.html#Macie2.Paginator.ListMembers)
    """

    def paginate(
        self, onlyAssociated: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMembersResponseTypeDef]:
        """
        [ListMembers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie2.html#Macie2.Paginator.ListMembers.paginate)
        """


class ListOrganizationAdminAccountsPaginator(Boto3Paginator):
    """
    [Paginator.ListOrganizationAdminAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie2.html#Macie2.Paginator.ListOrganizationAdminAccounts)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOrganizationAdminAccountsResponseTypeDef]:
        """
        [ListOrganizationAdminAccounts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie2.html#Macie2.Paginator.ListOrganizationAdminAccounts.paginate)
        """
