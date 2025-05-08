"""
Type annotations for partnercentral-selling service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_partnercentral_selling.client import PartnerCentralSellingAPIClient

    session = Session()
    client: PartnerCentralSellingAPIClient = session.client("partnercentral-selling")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

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
from .type_defs import (
    AcceptEngagementInvitationRequestTypeDef,
    AssignOpportunityRequestTypeDef,
    AssociateOpportunityRequestTypeDef,
    CreateEngagementInvitationRequestTypeDef,
    CreateEngagementInvitationResponseTypeDef,
    CreateEngagementRequestTypeDef,
    CreateEngagementResponseTypeDef,
    CreateOpportunityRequestTypeDef,
    CreateOpportunityResponseTypeDef,
    CreateResourceSnapshotJobRequestTypeDef,
    CreateResourceSnapshotJobResponseTypeDef,
    CreateResourceSnapshotRequestTypeDef,
    CreateResourceSnapshotResponseTypeDef,
    DeleteResourceSnapshotJobRequestTypeDef,
    DisassociateOpportunityRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAwsOpportunitySummaryRequestTypeDef,
    GetAwsOpportunitySummaryResponseTypeDef,
    GetEngagementInvitationRequestTypeDef,
    GetEngagementInvitationResponseTypeDef,
    GetEngagementRequestTypeDef,
    GetEngagementResponseTypeDef,
    GetOpportunityRequestTypeDef,
    GetOpportunityResponseTypeDef,
    GetResourceSnapshotJobRequestTypeDef,
    GetResourceSnapshotJobResponseTypeDef,
    GetResourceSnapshotRequestTypeDef,
    GetResourceSnapshotResponseTypeDef,
    GetSellingSystemSettingsRequestTypeDef,
    GetSellingSystemSettingsResponseTypeDef,
    ListEngagementByAcceptingInvitationTasksRequestTypeDef,
    ListEngagementByAcceptingInvitationTasksResponseTypeDef,
    ListEngagementFromOpportunityTasksRequestTypeDef,
    ListEngagementFromOpportunityTasksResponseTypeDef,
    ListEngagementInvitationsRequestTypeDef,
    ListEngagementInvitationsResponseTypeDef,
    ListEngagementMembersRequestTypeDef,
    ListEngagementMembersResponseTypeDef,
    ListEngagementResourceAssociationsRequestTypeDef,
    ListEngagementResourceAssociationsResponseTypeDef,
    ListEngagementsRequestTypeDef,
    ListEngagementsResponseTypeDef,
    ListOpportunitiesRequestTypeDef,
    ListOpportunitiesResponseTypeDef,
    ListResourceSnapshotJobsRequestTypeDef,
    ListResourceSnapshotJobsResponseTypeDef,
    ListResourceSnapshotsRequestTypeDef,
    ListResourceSnapshotsResponseTypeDef,
    ListSolutionsRequestTypeDef,
    ListSolutionsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutSellingSystemSettingsRequestTypeDef,
    PutSellingSystemSettingsResponseTypeDef,
    RejectEngagementInvitationRequestTypeDef,
    StartEngagementByAcceptingInvitationTaskRequestTypeDef,
    StartEngagementByAcceptingInvitationTaskResponseTypeDef,
    StartEngagementFromOpportunityTaskRequestTypeDef,
    StartEngagementFromOpportunityTaskResponseTypeDef,
    StartResourceSnapshotJobRequestTypeDef,
    StopResourceSnapshotJobRequestTypeDef,
    SubmitOpportunityRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateOpportunityRequestTypeDef,
    UpdateOpportunityResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("PartnerCentralSellingAPIClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class PartnerCentralSellingAPIClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling.html#PartnerCentralSellingAPI.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PartnerCentralSellingAPIClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling.html#PartnerCentralSellingAPI.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#generate_presigned_url)
        """

    def accept_engagement_invitation(
        self, **kwargs: Unpack[AcceptEngagementInvitationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Use the <code>AcceptEngagementInvitation</code> action to accept an engagement
        invitation shared by AWS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/accept_engagement_invitation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#accept_engagement_invitation)
        """

    def assign_opportunity(
        self, **kwargs: Unpack[AssignOpportunityRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Enables you to reassign an existing <code>Opportunity</code> to another user
        within your Partner Central account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/assign_opportunity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#assign_opportunity)
        """

    def associate_opportunity(
        self, **kwargs: Unpack[AssociateOpportunityRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Enables you to create a formal association between an <code>Opportunity</code>
        and various related entities, enriching the context and details of the
        opportunity for better collaboration and decision making.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/associate_opportunity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#associate_opportunity)
        """

    def create_engagement(
        self, **kwargs: Unpack[CreateEngagementRequestTypeDef]
    ) -> CreateEngagementResponseTypeDef:
        """
        The <code>CreateEngagement</code> action allows you to create an
        <code>Engagement</code>, which serves as a collaborative space between
        different parties such as AWS Partners and AWS Sellers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/create_engagement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#create_engagement)
        """

    def create_engagement_invitation(
        self, **kwargs: Unpack[CreateEngagementInvitationRequestTypeDef]
    ) -> CreateEngagementInvitationResponseTypeDef:
        """
        This action creates an invitation from a sender to a single receiver to join an
        engagement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/create_engagement_invitation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#create_engagement_invitation)
        """

    def create_opportunity(
        self, **kwargs: Unpack[CreateOpportunityRequestTypeDef]
    ) -> CreateOpportunityResponseTypeDef:
        """
        Creates an <code>Opportunity</code> record in Partner Central.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/create_opportunity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#create_opportunity)
        """

    def create_resource_snapshot(
        self, **kwargs: Unpack[CreateResourceSnapshotRequestTypeDef]
    ) -> CreateResourceSnapshotResponseTypeDef:
        """
        This action allows you to create an immutable snapshot of a specific resource,
        such as an opportunity, within the context of an engagement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/create_resource_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#create_resource_snapshot)
        """

    def create_resource_snapshot_job(
        self, **kwargs: Unpack[CreateResourceSnapshotJobRequestTypeDef]
    ) -> CreateResourceSnapshotJobResponseTypeDef:
        """
        Use this action to create a job to generate a snapshot of the specified
        resource within an engagement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/create_resource_snapshot_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#create_resource_snapshot_job)
        """

    def delete_resource_snapshot_job(
        self, **kwargs: Unpack[DeleteResourceSnapshotJobRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Use this action to deletes a previously created resource snapshot job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/delete_resource_snapshot_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#delete_resource_snapshot_job)
        """

    def disassociate_opportunity(
        self, **kwargs: Unpack[DisassociateOpportunityRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Allows you to remove an existing association between an
        <code>Opportunity</code> and related entities, such as a Partner Solution,
        Amazon Web Services product, or an Amazon Web Services Marketplace offer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/disassociate_opportunity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#disassociate_opportunity)
        """

    def get_aws_opportunity_summary(
        self, **kwargs: Unpack[GetAwsOpportunitySummaryRequestTypeDef]
    ) -> GetAwsOpportunitySummaryResponseTypeDef:
        """
        Retrieves a summary of an AWS Opportunity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/get_aws_opportunity_summary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#get_aws_opportunity_summary)
        """

    def get_engagement(
        self, **kwargs: Unpack[GetEngagementRequestTypeDef]
    ) -> GetEngagementResponseTypeDef:
        """
        Use this action to retrieve the engagement record for a given
        <code>EngagementIdentifier</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/get_engagement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#get_engagement)
        """

    def get_engagement_invitation(
        self, **kwargs: Unpack[GetEngagementInvitationRequestTypeDef]
    ) -> GetEngagementInvitationResponseTypeDef:
        """
        Retrieves the details of an engagement invitation shared by AWS with a partner.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/get_engagement_invitation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#get_engagement_invitation)
        """

    def get_opportunity(
        self, **kwargs: Unpack[GetOpportunityRequestTypeDef]
    ) -> GetOpportunityResponseTypeDef:
        """
        Fetches the <code>Opportunity</code> record from Partner Central by a given
        <code>Identifier</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/get_opportunity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#get_opportunity)
        """

    def get_resource_snapshot(
        self, **kwargs: Unpack[GetResourceSnapshotRequestTypeDef]
    ) -> GetResourceSnapshotResponseTypeDef:
        """
        Use this action to retrieve a specific snapshot record.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/get_resource_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#get_resource_snapshot)
        """

    def get_resource_snapshot_job(
        self, **kwargs: Unpack[GetResourceSnapshotJobRequestTypeDef]
    ) -> GetResourceSnapshotJobResponseTypeDef:
        """
        Use this action to retrieves information about a specific resource snapshot job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/get_resource_snapshot_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#get_resource_snapshot_job)
        """

    def get_selling_system_settings(
        self, **kwargs: Unpack[GetSellingSystemSettingsRequestTypeDef]
    ) -> GetSellingSystemSettingsResponseTypeDef:
        """
        Retrieves the currently set system settings, which include the IAM Role used
        for resource snapshot jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/get_selling_system_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#get_selling_system_settings)
        """

    def list_engagement_by_accepting_invitation_tasks(
        self, **kwargs: Unpack[ListEngagementByAcceptingInvitationTasksRequestTypeDef]
    ) -> ListEngagementByAcceptingInvitationTasksResponseTypeDef:
        """
        Lists all in-progress, completed, or failed
        StartEngagementByAcceptingInvitationTask tasks that were initiated by the
        caller's account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/list_engagement_by_accepting_invitation_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#list_engagement_by_accepting_invitation_tasks)
        """

    def list_engagement_from_opportunity_tasks(
        self, **kwargs: Unpack[ListEngagementFromOpportunityTasksRequestTypeDef]
    ) -> ListEngagementFromOpportunityTasksResponseTypeDef:
        """
        Lists all in-progress, completed, or failed
        <code>EngagementFromOpportunity</code> tasks that were initiated by the
        caller's account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/list_engagement_from_opportunity_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#list_engagement_from_opportunity_tasks)
        """

    def list_engagement_invitations(
        self, **kwargs: Unpack[ListEngagementInvitationsRequestTypeDef]
    ) -> ListEngagementInvitationsResponseTypeDef:
        """
        Retrieves a list of engagement invitations sent to the partner.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/list_engagement_invitations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#list_engagement_invitations)
        """

    def list_engagement_members(
        self, **kwargs: Unpack[ListEngagementMembersRequestTypeDef]
    ) -> ListEngagementMembersResponseTypeDef:
        """
        Retrieves the details of member partners in an Engagement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/list_engagement_members.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#list_engagement_members)
        """

    def list_engagement_resource_associations(
        self, **kwargs: Unpack[ListEngagementResourceAssociationsRequestTypeDef]
    ) -> ListEngagementResourceAssociationsResponseTypeDef:
        """
        Lists the associations between resources and engagements where the caller is a
        member and has at least one snapshot in the engagement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/list_engagement_resource_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#list_engagement_resource_associations)
        """

    def list_engagements(
        self, **kwargs: Unpack[ListEngagementsRequestTypeDef]
    ) -> ListEngagementsResponseTypeDef:
        """
        This action allows users to retrieve a list of Engagement records from Partner
        Central.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/list_engagements.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#list_engagements)
        """

    def list_opportunities(
        self, **kwargs: Unpack[ListOpportunitiesRequestTypeDef]
    ) -> ListOpportunitiesResponseTypeDef:
        """
        This request accepts a list of filters that retrieve opportunity subsets as
        well as sort options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/list_opportunities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#list_opportunities)
        """

    def list_resource_snapshot_jobs(
        self, **kwargs: Unpack[ListResourceSnapshotJobsRequestTypeDef]
    ) -> ListResourceSnapshotJobsResponseTypeDef:
        """
        Lists resource snapshot jobs owned by the customer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/list_resource_snapshot_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#list_resource_snapshot_jobs)
        """

    def list_resource_snapshots(
        self, **kwargs: Unpack[ListResourceSnapshotsRequestTypeDef]
    ) -> ListResourceSnapshotsResponseTypeDef:
        """
        Retrieves a list of resource view snapshots based on specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/list_resource_snapshots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#list_resource_snapshots)
        """

    def list_solutions(
        self, **kwargs: Unpack[ListSolutionsRequestTypeDef]
    ) -> ListSolutionsResponseTypeDef:
        """
        Retrieves a list of Partner Solutions that the partner registered on Partner
        Central.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/list_solutions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#list_solutions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#list_tags_for_resource)
        """

    def put_selling_system_settings(
        self, **kwargs: Unpack[PutSellingSystemSettingsRequestTypeDef]
    ) -> PutSellingSystemSettingsResponseTypeDef:
        """
        Updates the currently set system settings, which include the IAM Role used for
        resource snapshot jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/put_selling_system_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#put_selling_system_settings)
        """

    def reject_engagement_invitation(
        self, **kwargs: Unpack[RejectEngagementInvitationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This action rejects an <code>EngagementInvitation</code> that AWS shared.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/reject_engagement_invitation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#reject_engagement_invitation)
        """

    def start_engagement_by_accepting_invitation_task(
        self, **kwargs: Unpack[StartEngagementByAcceptingInvitationTaskRequestTypeDef]
    ) -> StartEngagementByAcceptingInvitationTaskResponseTypeDef:
        """
        This action starts the engagement by accepting an
        <code>EngagementInvitation</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/start_engagement_by_accepting_invitation_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#start_engagement_by_accepting_invitation_task)
        """

    def start_engagement_from_opportunity_task(
        self, **kwargs: Unpack[StartEngagementFromOpportunityTaskRequestTypeDef]
    ) -> StartEngagementFromOpportunityTaskResponseTypeDef:
        """
        This action initiates the engagement process from an existing opportunity by
        accepting the engagement invitation and creating a corresponding opportunity in
        the partner's system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/start_engagement_from_opportunity_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#start_engagement_from_opportunity_task)
        """

    def start_resource_snapshot_job(
        self, **kwargs: Unpack[StartResourceSnapshotJobRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Starts a resource snapshot job that has been previously created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/start_resource_snapshot_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#start_resource_snapshot_job)
        """

    def stop_resource_snapshot_job(
        self, **kwargs: Unpack[StopResourceSnapshotJobRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops a resource snapshot job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/stop_resource_snapshot_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#stop_resource_snapshot_job)
        """

    def submit_opportunity(
        self, **kwargs: Unpack[SubmitOpportunityRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Use this action to submit an Opportunity that was previously created by partner
        for AWS review.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/submit_opportunity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#submit_opportunity)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a tag or tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#untag_resource)
        """

    def update_opportunity(
        self, **kwargs: Unpack[UpdateOpportunityRequestTypeDef]
    ) -> UpdateOpportunityResponseTypeDef:
        """
        Updates the <code>Opportunity</code> record identified by a given
        <code>Identifier</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/update_opportunity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#update_opportunity)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_engagement_by_accepting_invitation_tasks"]
    ) -> ListEngagementByAcceptingInvitationTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_engagement_from_opportunity_tasks"]
    ) -> ListEngagementFromOpportunityTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_engagement_invitations"]
    ) -> ListEngagementInvitationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_engagement_members"]
    ) -> ListEngagementMembersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_engagement_resource_associations"]
    ) -> ListEngagementResourceAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_engagements"]
    ) -> ListEngagementsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_opportunities"]
    ) -> ListOpportunitiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_snapshot_jobs"]
    ) -> ListResourceSnapshotJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_snapshots"]
    ) -> ListResourceSnapshotsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_solutions"]
    ) -> ListSolutionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-selling/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/client/#get_paginator)
        """
