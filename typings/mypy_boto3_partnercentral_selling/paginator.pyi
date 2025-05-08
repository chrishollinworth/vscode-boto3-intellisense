"""
Type annotations for partnercentral-selling service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_partnercentral_selling.client import PartnerCentralSellingAPIClient
    from mypy_boto3_partnercentral_selling.paginator import (
        ListEngagementByAcceptingInvitationTasksPaginator,
        ListEngagementFromOpportunityTasksPaginator,
        ListEngagementInvitationsPaginator,
        ListEngagementMembersPaginator,
        ListEngagementResourceAssociationsPaginator,
        ListEngagementsPaginator,
        ListOpportunitiesPaginator,
        ListResourceSnapshotJobsPaginator,
        ListResourceSnapshotsPaginator,
        ListSolutionsPaginator,
    )

    session = Session()
    client: PartnerCentralSellingAPIClient = session.client("partnercentral-selling")

    list_engagement_by_accepting_invitation_tasks_paginator: ListEngagementByAcceptingInvitationTasksPaginator = client.get_paginator("list_engagement_by_accepting_invitation_tasks")
    list_engagement_from_opportunity_tasks_paginator: ListEngagementFromOpportunityTasksPaginator = client.get_paginator("list_engagement_from_opportunity_tasks")
    list_engagement_invitations_paginator: ListEngagementInvitationsPaginator = client.get_paginator("list_engagement_invitations")
    list_engagement_members_paginator: ListEngagementMembersPaginator = client.get_paginator("list_engagement_members")
    list_engagement_resource_associations_paginator: ListEngagementResourceAssociationsPaginator = client.get_paginator("list_engagement_resource_associations")
    list_engagements_paginator: ListEngagementsPaginator = client.get_paginator("list_engagements")
    list_opportunities_paginator: ListOpportunitiesPaginator = client.get_paginator("list_opportunities")
    list_resource_snapshot_jobs_paginator: ListResourceSnapshotJobsPaginator = client.get_paginator("list_resource_snapshot_jobs")
    list_resource_snapshots_paginator: ListResourceSnapshotsPaginator = client.get_paginator("list_resource_snapshots")
    list_solutions_paginator: ListSolutionsPaginator = client.get_paginator("list_solutions")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListEngagementByAcceptingInvitationTasksRequestPaginateTypeDef,
    ListEngagementByAcceptingInvitationTasksResponseTypeDef,
    ListEngagementFromOpportunityTasksRequestPaginateTypeDef,
    ListEngagementFromOpportunityTasksResponseTypeDef,
    ListEngagementInvitationsRequestPaginateTypeDef,
    ListEngagementInvitationsResponseTypeDef,
    ListEngagementMembersRequestPaginateTypeDef,
    ListEngagementMembersResponseTypeDef,
    ListEngagementResourceAssociationsRequestPaginateTypeDef,
    ListEngagementResourceAssociationsResponseTypeDef,
    ListEngagementsRequestPaginateTypeDef,
    ListEngagementsResponseTypeDef,
    ListOpportunitiesRequestPaginateTypeDef,
    ListOpportunitiesResponseTypeDef,
    ListResourceSnapshotJobsRequestPaginateTypeDef,
    ListResourceSnapshotJobsResponseTypeDef,
    ListResourceSnapshotsRequestPaginateTypeDef,
    ListResourceSnapshotsResponseTypeDef,
    ListSolutionsRequestPaginateTypeDef,
    ListSolutionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListEngagementByAcceptingInvitationTasksPaginator",
    "ListEngagementFromOpportunityTasksPaginator",
    "ListEngagementInvitationsPaginator",
    "ListEngagementMembersPaginator",
    "ListEngagementResourceAssociationsPaginator",
    "ListEngagementsPaginator",
    "ListOpportunitiesPaginator",
    "ListResourceSnapshotJobsPaginator",
    "ListResourceSnapshotsPaginator",
    "ListSolutionsPaginator",
)

if TYPE_CHECKING:
    _ListEngagementByAcceptingInvitationTasksPaginatorBase = Paginator[
        ListEngagementByAcceptingInvitationTasksResponseTypeDef
    ]
else:
    _ListEngagementByAcceptingInvitationTasksPaginatorBase = Paginator  # type: ignore[assignment]

class ListEngagementByAcceptingInvitationTasksPaginator(
    _ListEngagementByAcceptingInvitationTasksPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/paginator/ListEngagementByAcceptingInvitationTasks.html#PartnerCentralSellingAPI.Paginator.ListEngagementByAcceptingInvitationTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/#listengagementbyacceptinginvitationtaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEngagementByAcceptingInvitationTasksRequestPaginateTypeDef]
    ) -> PageIterator[ListEngagementByAcceptingInvitationTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/paginator/ListEngagementByAcceptingInvitationTasks.html#PartnerCentralSellingAPI.Paginator.ListEngagementByAcceptingInvitationTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/#listengagementbyacceptinginvitationtaskspaginator)
        """

if TYPE_CHECKING:
    _ListEngagementFromOpportunityTasksPaginatorBase = Paginator[
        ListEngagementFromOpportunityTasksResponseTypeDef
    ]
else:
    _ListEngagementFromOpportunityTasksPaginatorBase = Paginator  # type: ignore[assignment]

class ListEngagementFromOpportunityTasksPaginator(_ListEngagementFromOpportunityTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/paginator/ListEngagementFromOpportunityTasks.html#PartnerCentralSellingAPI.Paginator.ListEngagementFromOpportunityTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/#listengagementfromopportunitytaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEngagementFromOpportunityTasksRequestPaginateTypeDef]
    ) -> PageIterator[ListEngagementFromOpportunityTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/paginator/ListEngagementFromOpportunityTasks.html#PartnerCentralSellingAPI.Paginator.ListEngagementFromOpportunityTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/#listengagementfromopportunitytaskspaginator)
        """

if TYPE_CHECKING:
    _ListEngagementInvitationsPaginatorBase = Paginator[ListEngagementInvitationsResponseTypeDef]
else:
    _ListEngagementInvitationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEngagementInvitationsPaginator(_ListEngagementInvitationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/paginator/ListEngagementInvitations.html#PartnerCentralSellingAPI.Paginator.ListEngagementInvitations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/#listengagementinvitationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEngagementInvitationsRequestPaginateTypeDef]
    ) -> PageIterator[ListEngagementInvitationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/paginator/ListEngagementInvitations.html#PartnerCentralSellingAPI.Paginator.ListEngagementInvitations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/#listengagementinvitationspaginator)
        """

if TYPE_CHECKING:
    _ListEngagementMembersPaginatorBase = Paginator[ListEngagementMembersResponseTypeDef]
else:
    _ListEngagementMembersPaginatorBase = Paginator  # type: ignore[assignment]

class ListEngagementMembersPaginator(_ListEngagementMembersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/paginator/ListEngagementMembers.html#PartnerCentralSellingAPI.Paginator.ListEngagementMembers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/#listengagementmemberspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEngagementMembersRequestPaginateTypeDef]
    ) -> PageIterator[ListEngagementMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/paginator/ListEngagementMembers.html#PartnerCentralSellingAPI.Paginator.ListEngagementMembers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/#listengagementmemberspaginator)
        """

if TYPE_CHECKING:
    _ListEngagementResourceAssociationsPaginatorBase = Paginator[
        ListEngagementResourceAssociationsResponseTypeDef
    ]
else:
    _ListEngagementResourceAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEngagementResourceAssociationsPaginator(_ListEngagementResourceAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/paginator/ListEngagementResourceAssociations.html#PartnerCentralSellingAPI.Paginator.ListEngagementResourceAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/#listengagementresourceassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEngagementResourceAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListEngagementResourceAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/paginator/ListEngagementResourceAssociations.html#PartnerCentralSellingAPI.Paginator.ListEngagementResourceAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/#listengagementresourceassociationspaginator)
        """

if TYPE_CHECKING:
    _ListEngagementsPaginatorBase = Paginator[ListEngagementsResponseTypeDef]
else:
    _ListEngagementsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEngagementsPaginator(_ListEngagementsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/paginator/ListEngagements.html#PartnerCentralSellingAPI.Paginator.ListEngagements)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/#listengagementspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEngagementsRequestPaginateTypeDef]
    ) -> PageIterator[ListEngagementsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/paginator/ListEngagements.html#PartnerCentralSellingAPI.Paginator.ListEngagements.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/#listengagementspaginator)
        """

if TYPE_CHECKING:
    _ListOpportunitiesPaginatorBase = Paginator[ListOpportunitiesResponseTypeDef]
else:
    _ListOpportunitiesPaginatorBase = Paginator  # type: ignore[assignment]

class ListOpportunitiesPaginator(_ListOpportunitiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/paginator/ListOpportunities.html#PartnerCentralSellingAPI.Paginator.ListOpportunities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/#listopportunitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOpportunitiesRequestPaginateTypeDef]
    ) -> PageIterator[ListOpportunitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/paginator/ListOpportunities.html#PartnerCentralSellingAPI.Paginator.ListOpportunities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/#listopportunitiespaginator)
        """

if TYPE_CHECKING:
    _ListResourceSnapshotJobsPaginatorBase = Paginator[ListResourceSnapshotJobsResponseTypeDef]
else:
    _ListResourceSnapshotJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceSnapshotJobsPaginator(_ListResourceSnapshotJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/paginator/ListResourceSnapshotJobs.html#PartnerCentralSellingAPI.Paginator.ListResourceSnapshotJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/#listresourcesnapshotjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceSnapshotJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListResourceSnapshotJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/paginator/ListResourceSnapshotJobs.html#PartnerCentralSellingAPI.Paginator.ListResourceSnapshotJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/#listresourcesnapshotjobspaginator)
        """

if TYPE_CHECKING:
    _ListResourceSnapshotsPaginatorBase = Paginator[ListResourceSnapshotsResponseTypeDef]
else:
    _ListResourceSnapshotsPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceSnapshotsPaginator(_ListResourceSnapshotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/paginator/ListResourceSnapshots.html#PartnerCentralSellingAPI.Paginator.ListResourceSnapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/#listresourcesnapshotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceSnapshotsRequestPaginateTypeDef]
    ) -> PageIterator[ListResourceSnapshotsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/paginator/ListResourceSnapshots.html#PartnerCentralSellingAPI.Paginator.ListResourceSnapshots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/#listresourcesnapshotspaginator)
        """

if TYPE_CHECKING:
    _ListSolutionsPaginatorBase = Paginator[ListSolutionsResponseTypeDef]
else:
    _ListSolutionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSolutionsPaginator(_ListSolutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/paginator/ListSolutions.html#PartnerCentralSellingAPI.Paginator.ListSolutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/#listsolutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSolutionsRequestPaginateTypeDef]
    ) -> PageIterator[ListSolutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/paginator/ListSolutions.html#PartnerCentralSellingAPI.Paginator.ListSolutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/paginators/#listsolutionspaginator)
        """
