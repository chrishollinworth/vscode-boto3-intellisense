"""
Main interface for partnercentral-selling service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_partnercentral_selling import (
        Client,
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
        PartnerCentralSellingAPIClient,
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

from .client import PartnerCentralSellingAPIClient
from .paginator import (
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

Client = PartnerCentralSellingAPIClient

__all__ = (
    "Client",
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
    "PartnerCentralSellingAPIClient",
)
