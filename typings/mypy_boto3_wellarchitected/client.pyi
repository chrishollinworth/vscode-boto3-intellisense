"""
Main interface for wellarchitected service client

Usage::

    ```python
    import boto3
    from mypy_boto3_wellarchitected import WellArchitectedClient

    client: WellArchitectedClient = boto3.client("wellarchitected")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_wellarchitected.type_defs import (
    CreateMilestoneOutputTypeDef,
    CreateWorkloadOutputTypeDef,
    CreateWorkloadShareOutputTypeDef,
    GetAnswerOutputTypeDef,
    GetLensReviewOutputTypeDef,
    GetLensReviewReportOutputTypeDef,
    GetLensVersionDifferenceOutputTypeDef,
    GetMilestoneOutputTypeDef,
    GetWorkloadOutputTypeDef,
    ListAnswersOutputTypeDef,
    ListLensesOutputTypeDef,
    ListLensReviewImprovementsOutputTypeDef,
    ListLensReviewsOutputTypeDef,
    ListMilestonesOutputTypeDef,
    ListNotificationsOutputTypeDef,
    ListShareInvitationsOutputTypeDef,
    ListWorkloadSharesOutputTypeDef,
    ListWorkloadsOutputTypeDef,
    UpdateAnswerOutputTypeDef,
    UpdateLensReviewOutputTypeDef,
    UpdateShareInvitationOutputTypeDef,
    UpdateWorkloadOutputTypeDef,
    UpdateWorkloadShareOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("WellArchitectedClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class WellArchitectedClient:
    """
    [WellArchitected.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_lenses(self, WorkloadId: str, LensAliases: List[str]) -> None:
        """
        [Client.associate_lenses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.associate_lenses)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.can_paginate)
        """

    def create_milestone(
        self, WorkloadId: str, MilestoneName: str, ClientRequestToken: str
    ) -> CreateMilestoneOutputTypeDef:
        """
        [Client.create_milestone documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.create_milestone)
        """

    def create_workload(
        self,
        WorkloadName: str,
        Description: str,
        Environment: Literal["PRODUCTION", "PREPRODUCTION"],
        ReviewOwner: str,
        Lenses: List[str],
        ClientRequestToken: str,
        AccountIds: List[str] = None,
        AwsRegions: List[str] = None,
        NonAwsRegions: List[str] = None,
        PillarPriorities: List[str] = None,
        ArchitecturalDesign: str = None,
        IndustryType: str = None,
        Industry: str = None,
        Notes: str = None,
    ) -> CreateWorkloadOutputTypeDef:
        """
        [Client.create_workload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.create_workload)
        """

    def create_workload_share(
        self,
        WorkloadId: str,
        SharedWith: str,
        PermissionType: Literal["READONLY", "CONTRIBUTOR"],
        ClientRequestToken: str,
    ) -> CreateWorkloadShareOutputTypeDef:
        """
        [Client.create_workload_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.create_workload_share)
        """

    def delete_workload(self, WorkloadId: str, ClientRequestToken: str) -> None:
        """
        [Client.delete_workload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.delete_workload)
        """

    def delete_workload_share(self, ShareId: str, WorkloadId: str, ClientRequestToken: str) -> None:
        """
        [Client.delete_workload_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.delete_workload_share)
        """

    def disassociate_lenses(self, WorkloadId: str, LensAliases: List[str]) -> None:
        """
        [Client.disassociate_lenses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.disassociate_lenses)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.generate_presigned_url)
        """

    def get_answer(
        self, WorkloadId: str, LensAlias: str, QuestionId: str, MilestoneNumber: int = None
    ) -> GetAnswerOutputTypeDef:
        """
        [Client.get_answer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.get_answer)
        """

    def get_lens_review(
        self, WorkloadId: str, LensAlias: str, MilestoneNumber: int = None
    ) -> GetLensReviewOutputTypeDef:
        """
        [Client.get_lens_review documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.get_lens_review)
        """

    def get_lens_review_report(
        self, WorkloadId: str, LensAlias: str, MilestoneNumber: int = None
    ) -> GetLensReviewReportOutputTypeDef:
        """
        [Client.get_lens_review_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.get_lens_review_report)
        """

    def get_lens_version_difference(
        self, LensAlias: str, BaseLensVersion: str
    ) -> GetLensVersionDifferenceOutputTypeDef:
        """
        [Client.get_lens_version_difference documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.get_lens_version_difference)
        """

    def get_milestone(self, WorkloadId: str, MilestoneNumber: int) -> GetMilestoneOutputTypeDef:
        """
        [Client.get_milestone documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.get_milestone)
        """

    def get_workload(self, WorkloadId: str) -> GetWorkloadOutputTypeDef:
        """
        [Client.get_workload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.get_workload)
        """

    def list_answers(
        self,
        WorkloadId: str,
        LensAlias: str,
        PillarId: str = None,
        MilestoneNumber: int = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListAnswersOutputTypeDef:
        """
        [Client.list_answers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.list_answers)
        """

    def list_lens_review_improvements(
        self,
        WorkloadId: str,
        LensAlias: str,
        PillarId: str = None,
        MilestoneNumber: int = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListLensReviewImprovementsOutputTypeDef:
        """
        [Client.list_lens_review_improvements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.list_lens_review_improvements)
        """

    def list_lens_reviews(
        self,
        WorkloadId: str,
        MilestoneNumber: int = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListLensReviewsOutputTypeDef:
        """
        [Client.list_lens_reviews documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.list_lens_reviews)
        """

    def list_lenses(self, NextToken: str = None, MaxResults: int = None) -> ListLensesOutputTypeDef:
        """
        [Client.list_lenses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.list_lenses)
        """

    def list_milestones(
        self, WorkloadId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListMilestonesOutputTypeDef:
        """
        [Client.list_milestones documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.list_milestones)
        """

    def list_notifications(
        self, WorkloadId: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListNotificationsOutputTypeDef:
        """
        [Client.list_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.list_notifications)
        """

    def list_share_invitations(
        self, WorkloadNamePrefix: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListShareInvitationsOutputTypeDef:
        """
        [Client.list_share_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.list_share_invitations)
        """

    def list_workload_shares(
        self,
        WorkloadId: str,
        SharedWithPrefix: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListWorkloadSharesOutputTypeDef:
        """
        [Client.list_workload_shares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.list_workload_shares)
        """

    def list_workloads(
        self, WorkloadNamePrefix: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListWorkloadsOutputTypeDef:
        """
        [Client.list_workloads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.list_workloads)
        """

    def update_answer(
        self,
        WorkloadId: str,
        LensAlias: str,
        QuestionId: str,
        SelectedChoices: List[str] = None,
        Notes: str = None,
        IsApplicable: bool = None,
    ) -> UpdateAnswerOutputTypeDef:
        """
        [Client.update_answer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.update_answer)
        """

    def update_lens_review(
        self,
        WorkloadId: str,
        LensAlias: str,
        LensNotes: str = None,
        PillarNotes: Dict[str, str] = None,
    ) -> UpdateLensReviewOutputTypeDef:
        """
        [Client.update_lens_review documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.update_lens_review)
        """

    def update_share_invitation(
        self, ShareInvitationId: str, ShareInvitationAction: Literal["ACCEPT", "REJECT"]
    ) -> UpdateShareInvitationOutputTypeDef:
        """
        [Client.update_share_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.update_share_invitation)
        """

    def update_workload(
        self,
        WorkloadId: str,
        WorkloadName: str = None,
        Description: str = None,
        Environment: Literal["PRODUCTION", "PREPRODUCTION"] = None,
        AccountIds: List[str] = None,
        AwsRegions: List[str] = None,
        NonAwsRegions: List[str] = None,
        PillarPriorities: List[str] = None,
        ArchitecturalDesign: str = None,
        ReviewOwner: str = None,
        IsReviewOwnerUpdateAcknowledged: bool = None,
        IndustryType: str = None,
        Industry: str = None,
        Notes: str = None,
        ImprovementStatus: Literal[
            "NOT_APPLICABLE", "NOT_STARTED", "IN_PROGRESS", "COMPLETE", "RISK_ACKNOWLEDGED"
        ] = None,
    ) -> UpdateWorkloadOutputTypeDef:
        """
        [Client.update_workload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.update_workload)
        """

    def update_workload_share(
        self, ShareId: str, WorkloadId: str, PermissionType: Literal["READONLY", "CONTRIBUTOR"]
    ) -> UpdateWorkloadShareOutputTypeDef:
        """
        [Client.update_workload_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.update_workload_share)
        """

    def upgrade_lens_review(
        self, WorkloadId: str, LensAlias: str, MilestoneName: str, ClientRequestToken: str = None
    ) -> None:
        """
        [Client.upgrade_lens_review documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/wellarchitected.html#WellArchitected.Client.upgrade_lens_review)
        """
