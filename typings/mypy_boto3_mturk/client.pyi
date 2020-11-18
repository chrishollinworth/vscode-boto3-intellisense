# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for mturk service client

Usage::

    ```python
    import boto3
    from mypy_boto3_mturk import MTurkClient

    client: MTurkClient = boto3.client("mturk")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_mturk.paginator import (
    ListAssignmentsForHITPaginator,
    ListBonusPaymentsPaginator,
    ListHITsForQualificationTypePaginator,
    ListHITsPaginator,
    ListQualificationRequestsPaginator,
    ListQualificationTypesPaginator,
    ListReviewableHITsPaginator,
    ListWorkerBlocksPaginator,
    ListWorkersWithQualificationTypePaginator,
)
from mypy_boto3_mturk.type_defs import (
    CreateHITResponseTypeDef,
    CreateHITTypeResponseTypeDef,
    CreateHITWithHITTypeResponseTypeDef,
    CreateQualificationTypeResponseTypeDef,
    GetAccountBalanceResponseTypeDef,
    GetAssignmentResponseTypeDef,
    GetFileUploadURLResponseTypeDef,
    GetHITResponseTypeDef,
    GetQualificationScoreResponseTypeDef,
    GetQualificationTypeResponseTypeDef,
    HITLayoutParameterTypeDef,
    ListAssignmentsForHITResponseTypeDef,
    ListBonusPaymentsResponseTypeDef,
    ListHITsForQualificationTypeResponseTypeDef,
    ListHITsResponseTypeDef,
    ListQualificationRequestsResponseTypeDef,
    ListQualificationTypesResponseTypeDef,
    ListReviewableHITsResponseTypeDef,
    ListReviewPolicyResultsForHITResponseTypeDef,
    ListWorkerBlocksResponseTypeDef,
    ListWorkersWithQualificationTypeResponseTypeDef,
    NotificationSpecificationTypeDef,
    NotifyWorkersResponseTypeDef,
    QualificationRequirementTypeDef,
    ReviewPolicyTypeDef,
    UpdateQualificationTypeResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MTurkClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    RequestError: Type[BotocoreClientError]
    ServiceFault: Type[BotocoreClientError]


class MTurkClient:
    """
    [MTurk.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_qualification_request(
        self, QualificationRequestId: str, IntegerValue: int = None
    ) -> Dict[str, Any]:
        """
        [Client.accept_qualification_request documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.accept_qualification_request)
        """

    def approve_assignment(
        self, AssignmentId: str, RequesterFeedback: str = None, OverrideRejection: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.approve_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.approve_assignment)
        """

    def associate_qualification_with_worker(
        self,
        QualificationTypeId: str,
        WorkerId: str,
        IntegerValue: int = None,
        SendNotification: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.associate_qualification_with_worker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.associate_qualification_with_worker)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.can_paginate)
        """

    def create_additional_assignments_for_hit(
        self, HITId: str, NumberOfAdditionalAssignments: int, UniqueRequestToken: str = None
    ) -> Dict[str, Any]:
        """
        [Client.create_additional_assignments_for_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.create_additional_assignments_for_hit)
        """

    def create_hit(
        self,
        LifetimeInSeconds: int,
        AssignmentDurationInSeconds: int,
        Reward: str,
        Title: str,
        Description: str,
        MaxAssignments: int = None,
        AutoApprovalDelayInSeconds: int = None,
        Keywords: str = None,
        Question: str = None,
        RequesterAnnotation: str = None,
        QualificationRequirements: List["QualificationRequirementTypeDef"] = None,
        UniqueRequestToken: str = None,
        AssignmentReviewPolicy: "ReviewPolicyTypeDef" = None,
        HITReviewPolicy: "ReviewPolicyTypeDef" = None,
        HITLayoutId: str = None,
        HITLayoutParameters: List[HITLayoutParameterTypeDef] = None,
    ) -> CreateHITResponseTypeDef:
        """
        [Client.create_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.create_hit)
        """

    def create_hit_type(
        self,
        AssignmentDurationInSeconds: int,
        Reward: str,
        Title: str,
        Description: str,
        AutoApprovalDelayInSeconds: int = None,
        Keywords: str = None,
        QualificationRequirements: List["QualificationRequirementTypeDef"] = None,
    ) -> CreateHITTypeResponseTypeDef:
        """
        [Client.create_hit_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.create_hit_type)
        """

    def create_hit_with_hit_type(
        self,
        HITTypeId: str,
        LifetimeInSeconds: int,
        MaxAssignments: int = None,
        Question: str = None,
        RequesterAnnotation: str = None,
        UniqueRequestToken: str = None,
        AssignmentReviewPolicy: "ReviewPolicyTypeDef" = None,
        HITReviewPolicy: "ReviewPolicyTypeDef" = None,
        HITLayoutId: str = None,
        HITLayoutParameters: List[HITLayoutParameterTypeDef] = None,
    ) -> CreateHITWithHITTypeResponseTypeDef:
        """
        [Client.create_hit_with_hit_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.create_hit_with_hit_type)
        """

    def create_qualification_type(
        self,
        Name: str,
        Description: str,
        QualificationTypeStatus: Literal["Active", "Inactive"],
        Keywords: str = None,
        RetryDelayInSeconds: int = None,
        Test: str = None,
        AnswerKey: str = None,
        TestDurationInSeconds: int = None,
        AutoGranted: bool = None,
        AutoGrantedValue: int = None,
    ) -> CreateQualificationTypeResponseTypeDef:
        """
        [Client.create_qualification_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.create_qualification_type)
        """

    def create_worker_block(self, WorkerId: str, Reason: str) -> Dict[str, Any]:
        """
        [Client.create_worker_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.create_worker_block)
        """

    def delete_hit(self, HITId: str) -> Dict[str, Any]:
        """
        [Client.delete_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.delete_hit)
        """

    def delete_qualification_type(self, QualificationTypeId: str) -> Dict[str, Any]:
        """
        [Client.delete_qualification_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.delete_qualification_type)
        """

    def delete_worker_block(self, WorkerId: str, Reason: str = None) -> Dict[str, Any]:
        """
        [Client.delete_worker_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.delete_worker_block)
        """

    def disassociate_qualification_from_worker(
        self, WorkerId: str, QualificationTypeId: str, Reason: str = None
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_qualification_from_worker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.disassociate_qualification_from_worker)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.generate_presigned_url)
        """

    def get_account_balance(self) -> GetAccountBalanceResponseTypeDef:
        """
        [Client.get_account_balance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.get_account_balance)
        """

    def get_assignment(self, AssignmentId: str) -> GetAssignmentResponseTypeDef:
        """
        [Client.get_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.get_assignment)
        """

    def get_file_upload_url(
        self, AssignmentId: str, QuestionIdentifier: str
    ) -> GetFileUploadURLResponseTypeDef:
        """
        [Client.get_file_upload_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.get_file_upload_url)
        """

    def get_hit(self, HITId: str) -> GetHITResponseTypeDef:
        """
        [Client.get_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.get_hit)
        """

    def get_qualification_score(
        self, QualificationTypeId: str, WorkerId: str
    ) -> GetQualificationScoreResponseTypeDef:
        """
        [Client.get_qualification_score documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.get_qualification_score)
        """

    def get_qualification_type(
        self, QualificationTypeId: str
    ) -> GetQualificationTypeResponseTypeDef:
        """
        [Client.get_qualification_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.get_qualification_type)
        """

    def list_assignments_for_hit(
        self,
        HITId: str,
        NextToken: str = None,
        MaxResults: int = None,
        AssignmentStatuses: List[Literal["Submitted", "Approved", "Rejected"]] = None,
    ) -> ListAssignmentsForHITResponseTypeDef:
        """
        [Client.list_assignments_for_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.list_assignments_for_hit)
        """

    def list_bonus_payments(
        self,
        HITId: str = None,
        AssignmentId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListBonusPaymentsResponseTypeDef:
        """
        [Client.list_bonus_payments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.list_bonus_payments)
        """

    def list_hits(self, NextToken: str = None, MaxResults: int = None) -> ListHITsResponseTypeDef:
        """
        [Client.list_hits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.list_hits)
        """

    def list_hits_for_qualification_type(
        self, QualificationTypeId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListHITsForQualificationTypeResponseTypeDef:
        """
        [Client.list_hits_for_qualification_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.list_hits_for_qualification_type)
        """

    def list_qualification_requests(
        self, QualificationTypeId: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListQualificationRequestsResponseTypeDef:
        """
        [Client.list_qualification_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.list_qualification_requests)
        """

    def list_qualification_types(
        self,
        MustBeRequestable: bool,
        Query: str = None,
        MustBeOwnedByCaller: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListQualificationTypesResponseTypeDef:
        """
        [Client.list_qualification_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.list_qualification_types)
        """

    def list_review_policy_results_for_hit(
        self,
        HITId: str,
        PolicyLevels: List[Literal["Assignment", "HIT"]] = None,
        RetrieveActions: bool = None,
        RetrieveResults: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListReviewPolicyResultsForHITResponseTypeDef:
        """
        [Client.list_review_policy_results_for_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.list_review_policy_results_for_hit)
        """

    def list_reviewable_hits(
        self,
        HITTypeId: str = None,
        Status: Literal["Reviewable", "Reviewing"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListReviewableHITsResponseTypeDef:
        """
        [Client.list_reviewable_hits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.list_reviewable_hits)
        """

    def list_worker_blocks(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListWorkerBlocksResponseTypeDef:
        """
        [Client.list_worker_blocks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.list_worker_blocks)
        """

    def list_workers_with_qualification_type(
        self,
        QualificationTypeId: str,
        Status: Literal["Granted", "Revoked"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListWorkersWithQualificationTypeResponseTypeDef:
        """
        [Client.list_workers_with_qualification_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.list_workers_with_qualification_type)
        """

    def notify_workers(
        self, Subject: str, MessageText: str, WorkerIds: List[str]
    ) -> NotifyWorkersResponseTypeDef:
        """
        [Client.notify_workers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.notify_workers)
        """

    def reject_assignment(self, AssignmentId: str, RequesterFeedback: str) -> Dict[str, Any]:
        """
        [Client.reject_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.reject_assignment)
        """

    def reject_qualification_request(
        self, QualificationRequestId: str, Reason: str = None
    ) -> Dict[str, Any]:
        """
        [Client.reject_qualification_request documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.reject_qualification_request)
        """

    def send_bonus(
        self,
        WorkerId: str,
        BonusAmount: str,
        AssignmentId: str,
        Reason: str,
        UniqueRequestToken: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.send_bonus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.send_bonus)
        """

    def send_test_event_notification(
        self,
        Notification: NotificationSpecificationTypeDef,
        TestEventType: Literal[
            "AssignmentAccepted",
            "AssignmentAbandoned",
            "AssignmentReturned",
            "AssignmentSubmitted",
            "AssignmentRejected",
            "AssignmentApproved",
            "HITCreated",
            "HITExpired",
            "HITReviewable",
            "HITExtended",
            "HITDisposed",
            "Ping",
        ],
    ) -> Dict[str, Any]:
        """
        [Client.send_test_event_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.send_test_event_notification)
        """

    def update_expiration_for_hit(self, HITId: str, ExpireAt: datetime) -> Dict[str, Any]:
        """
        [Client.update_expiration_for_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.update_expiration_for_hit)
        """

    def update_hit_review_status(self, HITId: str, Revert: bool = None) -> Dict[str, Any]:
        """
        [Client.update_hit_review_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.update_hit_review_status)
        """

    def update_hit_type_of_hit(self, HITId: str, HITTypeId: str) -> Dict[str, Any]:
        """
        [Client.update_hit_type_of_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.update_hit_type_of_hit)
        """

    def update_notification_settings(
        self,
        HITTypeId: str,
        Notification: NotificationSpecificationTypeDef = None,
        Active: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_notification_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.update_notification_settings)
        """

    def update_qualification_type(
        self,
        QualificationTypeId: str,
        Description: str = None,
        QualificationTypeStatus: Literal["Active", "Inactive"] = None,
        Test: str = None,
        AnswerKey: str = None,
        TestDurationInSeconds: int = None,
        RetryDelayInSeconds: int = None,
        AutoGranted: bool = None,
        AutoGrantedValue: int = None,
    ) -> UpdateQualificationTypeResponseTypeDef:
        """
        [Client.update_qualification_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Client.update_qualification_type)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_assignments_for_hit"]
    ) -> ListAssignmentsForHITPaginator:
        """
        [Paginator.ListAssignmentsForHIT documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Paginator.ListAssignmentsForHIT)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_bonus_payments"]
    ) -> ListBonusPaymentsPaginator:
        """
        [Paginator.ListBonusPayments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Paginator.ListBonusPayments)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_hits"]) -> ListHITsPaginator:
        """
        [Paginator.ListHITs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Paginator.ListHITs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_hits_for_qualification_type"]
    ) -> ListHITsForQualificationTypePaginator:
        """
        [Paginator.ListHITsForQualificationType documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Paginator.ListHITsForQualificationType)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_qualification_requests"]
    ) -> ListQualificationRequestsPaginator:
        """
        [Paginator.ListQualificationRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Paginator.ListQualificationRequests)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_qualification_types"]
    ) -> ListQualificationTypesPaginator:
        """
        [Paginator.ListQualificationTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Paginator.ListQualificationTypes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_reviewable_hits"]
    ) -> ListReviewableHITsPaginator:
        """
        [Paginator.ListReviewableHITs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Paginator.ListReviewableHITs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_worker_blocks"]
    ) -> ListWorkerBlocksPaginator:
        """
        [Paginator.ListWorkerBlocks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Paginator.ListWorkerBlocks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_workers_with_qualification_type"]
    ) -> ListWorkersWithQualificationTypePaginator:
        """
        [Paginator.ListWorkersWithQualificationType documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mturk.html#MTurk.Paginator.ListWorkersWithQualificationType)
        """
