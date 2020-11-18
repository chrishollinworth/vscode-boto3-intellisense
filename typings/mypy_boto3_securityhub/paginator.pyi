# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for securityhub service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_securityhub import SecurityHubClient
    from mypy_boto3_securityhub.paginator import (
        GetEnabledStandardsPaginator,
        GetFindingsPaginator,
        GetInsightsPaginator,
        ListEnabledProductsForImportPaginator,
        ListInvitationsPaginator,
        ListMembersPaginator,
    )

    client: SecurityHubClient = boto3.client("securityhub")

    get_enabled_standards_paginator: GetEnabledStandardsPaginator = client.get_paginator("get_enabled_standards")
    get_findings_paginator: GetFindingsPaginator = client.get_paginator("get_findings")
    get_insights_paginator: GetInsightsPaginator = client.get_paginator("get_insights")
    list_enabled_products_for_import_paginator: ListEnabledProductsForImportPaginator = client.get_paginator("list_enabled_products_for_import")
    list_invitations_paginator: ListInvitationsPaginator = client.get_paginator("list_invitations")
    list_members_paginator: ListMembersPaginator = client.get_paginator("list_members")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_securityhub.type_defs import (
    AwsSecurityFindingFiltersTypeDef,
    GetEnabledStandardsResponseTypeDef,
    GetFindingsResponseTypeDef,
    GetInsightsResponseTypeDef,
    ListEnabledProductsForImportResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListMembersResponseTypeDef,
    PaginatorConfigTypeDef,
    SortCriterionTypeDef,
)

__all__ = (
    "GetEnabledStandardsPaginator",
    "GetFindingsPaginator",
    "GetInsightsPaginator",
    "ListEnabledProductsForImportPaginator",
    "ListInvitationsPaginator",
    "ListMembersPaginator",
)


class GetEnabledStandardsPaginator(Boto3Paginator):
    """
    [Paginator.GetEnabledStandards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Paginator.GetEnabledStandards)
    """

    def paginate(
        self,
        StandardsSubscriptionArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetEnabledStandardsResponseTypeDef]:
        """
        [GetEnabledStandards.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Paginator.GetEnabledStandards.paginate)
        """


class GetFindingsPaginator(Boto3Paginator):
    """
    [Paginator.GetFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Paginator.GetFindings)
    """

    def paginate(
        self,
        Filters: "AwsSecurityFindingFiltersTypeDef" = None,
        SortCriteria: List[SortCriterionTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetFindingsResponseTypeDef]:
        """
        [GetFindings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Paginator.GetFindings.paginate)
        """


class GetInsightsPaginator(Boto3Paginator):
    """
    [Paginator.GetInsights documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Paginator.GetInsights)
    """

    def paginate(
        self, InsightArns: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetInsightsResponseTypeDef]:
        """
        [GetInsights.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Paginator.GetInsights.paginate)
        """


class ListEnabledProductsForImportPaginator(Boto3Paginator):
    """
    [Paginator.ListEnabledProductsForImport documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Paginator.ListEnabledProductsForImport)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnabledProductsForImportResponseTypeDef]:
        """
        [ListEnabledProductsForImport.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Paginator.ListEnabledProductsForImport.paginate)
        """


class ListInvitationsPaginator(Boto3Paginator):
    """
    [Paginator.ListInvitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Paginator.ListInvitations)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInvitationsResponseTypeDef]:
        """
        [ListInvitations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Paginator.ListInvitations.paginate)
        """


class ListMembersPaginator(Boto3Paginator):
    """
    [Paginator.ListMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Paginator.ListMembers)
    """

    def paginate(
        self, OnlyAssociated: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMembersResponseTypeDef]:
        """
        [ListMembers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/securityhub.html#SecurityHub.Paginator.ListMembers.paginate)
        """
