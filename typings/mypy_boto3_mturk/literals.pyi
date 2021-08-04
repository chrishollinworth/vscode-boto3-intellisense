"""
Type annotations for mturk service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/literals.html)

Usage::

    ```python
    from mypy_boto3_mturk.literals import AssignmentStatusType

    data: AssignmentStatusType = "Approved"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AssignmentStatusType",
    "ComparatorType",
    "EventTypeType",
    "HITAccessActionsType",
    "HITReviewStatusType",
    "HITStatusType",
    "ListAssignmentsForHITPaginatorName",
    "ListBonusPaymentsPaginatorName",
    "ListHITsForQualificationTypePaginatorName",
    "ListHITsPaginatorName",
    "ListQualificationRequestsPaginatorName",
    "ListQualificationTypesPaginatorName",
    "ListReviewableHITsPaginatorName",
    "ListWorkerBlocksPaginatorName",
    "ListWorkersWithQualificationTypePaginatorName",
    "NotificationTransportType",
    "NotifyWorkersFailureCodeType",
    "QualificationStatusType",
    "QualificationTypeStatusType",
    "ReviewActionStatusType",
    "ReviewPolicyLevelType",
    "ReviewableHITStatusType",
)

AssignmentStatusType = Literal["Approved", "Rejected", "Submitted"]
ComparatorType = Literal[
    "DoesNotExist",
    "EqualTo",
    "Exists",
    "GreaterThan",
    "GreaterThanOrEqualTo",
    "In",
    "LessThan",
    "LessThanOrEqualTo",
    "NotEqualTo",
    "NotIn",
]
EventTypeType = Literal[
    "AssignmentAbandoned",
    "AssignmentAccepted",
    "AssignmentApproved",
    "AssignmentRejected",
    "AssignmentReturned",
    "AssignmentSubmitted",
    "HITCreated",
    "HITDisposed",
    "HITExpired",
    "HITExtended",
    "HITReviewable",
    "Ping",
]
HITAccessActionsType = Literal["Accept", "DiscoverPreviewAndAccept", "PreviewAndAccept"]
HITReviewStatusType = Literal[
    "MarkedForReview", "NotReviewed", "ReviewedAppropriate", "ReviewedInappropriate"
]
HITStatusType = Literal["Assignable", "Disposed", "Reviewable", "Reviewing", "Unassignable"]
ListAssignmentsForHITPaginatorName = Literal["list_assignments_for_hit"]
ListBonusPaymentsPaginatorName = Literal["list_bonus_payments"]
ListHITsForQualificationTypePaginatorName = Literal["list_hits_for_qualification_type"]
ListHITsPaginatorName = Literal["list_hits"]
ListQualificationRequestsPaginatorName = Literal["list_qualification_requests"]
ListQualificationTypesPaginatorName = Literal["list_qualification_types"]
ListReviewableHITsPaginatorName = Literal["list_reviewable_hits"]
ListWorkerBlocksPaginatorName = Literal["list_worker_blocks"]
ListWorkersWithQualificationTypePaginatorName = Literal["list_workers_with_qualification_type"]
NotificationTransportType = Literal["Email", "SNS", "SQS"]
NotifyWorkersFailureCodeType = Literal["HardFailure", "SoftFailure"]
QualificationStatusType = Literal["Granted", "Revoked"]
QualificationTypeStatusType = Literal["Active", "Inactive"]
ReviewActionStatusType = Literal["Cancelled", "Failed", "Intended", "Succeeded"]
ReviewPolicyLevelType = Literal["Assignment", "HIT"]
ReviewableHITStatusType = Literal["Reviewable", "Reviewing"]
