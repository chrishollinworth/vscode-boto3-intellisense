"""
Type annotations for mturk service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_mturk.type_defs import AcceptQualificationRequestRequestTypeDef

    data: AcceptQualificationRequestRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AssignmentStatusType,
    ComparatorType,
    EventTypeType,
    HITAccessActionsType,
    HITReviewStatusType,
    HITStatusType,
    NotificationTransportType,
    NotifyWorkersFailureCodeType,
    QualificationStatusType,
    QualificationTypeStatusType,
    ReviewableHITStatusType,
    ReviewActionStatusType,
    ReviewPolicyLevelType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AcceptQualificationRequestRequestTypeDef",
    "ApproveAssignmentRequestTypeDef",
    "AssignmentTypeDef",
    "AssociateQualificationWithWorkerRequestTypeDef",
    "BonusPaymentTypeDef",
    "CreateAdditionalAssignmentsForHITRequestTypeDef",
    "CreateHITRequestTypeDef",
    "CreateHITResponseTypeDef",
    "CreateHITTypeRequestTypeDef",
    "CreateHITTypeResponseTypeDef",
    "CreateHITWithHITTypeRequestTypeDef",
    "CreateHITWithHITTypeResponseTypeDef",
    "CreateQualificationTypeRequestTypeDef",
    "CreateQualificationTypeResponseTypeDef",
    "CreateWorkerBlockRequestTypeDef",
    "DeleteHITRequestTypeDef",
    "DeleteQualificationTypeRequestTypeDef",
    "DeleteWorkerBlockRequestTypeDef",
    "DisassociateQualificationFromWorkerRequestTypeDef",
    "GetAccountBalanceResponseTypeDef",
    "GetAssignmentRequestTypeDef",
    "GetAssignmentResponseTypeDef",
    "GetFileUploadURLRequestTypeDef",
    "GetFileUploadURLResponseTypeDef",
    "GetHITRequestTypeDef",
    "GetHITResponseTypeDef",
    "GetQualificationScoreRequestTypeDef",
    "GetQualificationScoreResponseTypeDef",
    "GetQualificationTypeRequestTypeDef",
    "GetQualificationTypeResponseTypeDef",
    "HITLayoutParameterTypeDef",
    "HITTypeDef",
    "ListAssignmentsForHITRequestPaginateTypeDef",
    "ListAssignmentsForHITRequestTypeDef",
    "ListAssignmentsForHITResponseTypeDef",
    "ListBonusPaymentsRequestPaginateTypeDef",
    "ListBonusPaymentsRequestTypeDef",
    "ListBonusPaymentsResponseTypeDef",
    "ListHITsForQualificationTypeRequestPaginateTypeDef",
    "ListHITsForQualificationTypeRequestTypeDef",
    "ListHITsForQualificationTypeResponseTypeDef",
    "ListHITsRequestPaginateTypeDef",
    "ListHITsRequestTypeDef",
    "ListHITsResponseTypeDef",
    "ListQualificationRequestsRequestPaginateTypeDef",
    "ListQualificationRequestsRequestTypeDef",
    "ListQualificationRequestsResponseTypeDef",
    "ListQualificationTypesRequestPaginateTypeDef",
    "ListQualificationTypesRequestTypeDef",
    "ListQualificationTypesResponseTypeDef",
    "ListReviewPolicyResultsForHITRequestTypeDef",
    "ListReviewPolicyResultsForHITResponseTypeDef",
    "ListReviewableHITsRequestPaginateTypeDef",
    "ListReviewableHITsRequestTypeDef",
    "ListReviewableHITsResponseTypeDef",
    "ListWorkerBlocksRequestPaginateTypeDef",
    "ListWorkerBlocksRequestTypeDef",
    "ListWorkerBlocksResponseTypeDef",
    "ListWorkersWithQualificationTypeRequestPaginateTypeDef",
    "ListWorkersWithQualificationTypeRequestTypeDef",
    "ListWorkersWithQualificationTypeResponseTypeDef",
    "LocaleTypeDef",
    "NotificationSpecificationTypeDef",
    "NotifyWorkersFailureStatusTypeDef",
    "NotifyWorkersRequestTypeDef",
    "NotifyWorkersResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterMapEntryOutputTypeDef",
    "ParameterMapEntryTypeDef",
    "PolicyParameterOutputTypeDef",
    "PolicyParameterTypeDef",
    "QualificationRequestTypeDef",
    "QualificationRequirementOutputTypeDef",
    "QualificationRequirementTypeDef",
    "QualificationRequirementUnionTypeDef",
    "QualificationTypeDef",
    "QualificationTypeTypeDef",
    "RejectAssignmentRequestTypeDef",
    "RejectQualificationRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ReviewActionDetailTypeDef",
    "ReviewPolicyOutputTypeDef",
    "ReviewPolicyTypeDef",
    "ReviewPolicyUnionTypeDef",
    "ReviewReportTypeDef",
    "ReviewResultDetailTypeDef",
    "SendBonusRequestTypeDef",
    "SendTestEventNotificationRequestTypeDef",
    "TimestampTypeDef",
    "UpdateExpirationForHITRequestTypeDef",
    "UpdateHITReviewStatusRequestTypeDef",
    "UpdateHITTypeOfHITRequestTypeDef",
    "UpdateNotificationSettingsRequestTypeDef",
    "UpdateQualificationTypeRequestTypeDef",
    "UpdateQualificationTypeResponseTypeDef",
    "WorkerBlockTypeDef",
)

class AcceptQualificationRequestRequestTypeDef(TypedDict):
    QualificationRequestId: str
    IntegerValue: NotRequired[int]

class ApproveAssignmentRequestTypeDef(TypedDict):
    AssignmentId: str
    RequesterFeedback: NotRequired[str]
    OverrideRejection: NotRequired[bool]

class AssignmentTypeDef(TypedDict):
    AssignmentId: NotRequired[str]
    WorkerId: NotRequired[str]
    HITId: NotRequired[str]
    AssignmentStatus: NotRequired[AssignmentStatusType]
    AutoApprovalTime: NotRequired[datetime]
    AcceptTime: NotRequired[datetime]
    SubmitTime: NotRequired[datetime]
    ApprovalTime: NotRequired[datetime]
    RejectionTime: NotRequired[datetime]
    Deadline: NotRequired[datetime]
    Answer: NotRequired[str]
    RequesterFeedback: NotRequired[str]

class AssociateQualificationWithWorkerRequestTypeDef(TypedDict):
    QualificationTypeId: str
    WorkerId: str
    IntegerValue: NotRequired[int]
    SendNotification: NotRequired[bool]

class BonusPaymentTypeDef(TypedDict):
    WorkerId: NotRequired[str]
    BonusAmount: NotRequired[str]
    AssignmentId: NotRequired[str]
    Reason: NotRequired[str]
    GrantTime: NotRequired[datetime]

class CreateAdditionalAssignmentsForHITRequestTypeDef(TypedDict):
    HITId: str
    NumberOfAdditionalAssignments: int
    UniqueRequestToken: NotRequired[str]

class HITLayoutParameterTypeDef(TypedDict):
    Name: str
    Value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateQualificationTypeRequestTypeDef(TypedDict):
    Name: str
    Description: str
    QualificationTypeStatus: QualificationTypeStatusType
    Keywords: NotRequired[str]
    RetryDelayInSeconds: NotRequired[int]
    Test: NotRequired[str]
    AnswerKey: NotRequired[str]
    TestDurationInSeconds: NotRequired[int]
    AutoGranted: NotRequired[bool]
    AutoGrantedValue: NotRequired[int]

class QualificationTypeTypeDef(TypedDict):
    QualificationTypeId: NotRequired[str]
    CreationTime: NotRequired[datetime]
    Name: NotRequired[str]
    Description: NotRequired[str]
    Keywords: NotRequired[str]
    QualificationTypeStatus: NotRequired[QualificationTypeStatusType]
    Test: NotRequired[str]
    TestDurationInSeconds: NotRequired[int]
    AnswerKey: NotRequired[str]
    RetryDelayInSeconds: NotRequired[int]
    IsRequestable: NotRequired[bool]
    AutoGranted: NotRequired[bool]
    AutoGrantedValue: NotRequired[int]

class CreateWorkerBlockRequestTypeDef(TypedDict):
    WorkerId: str
    Reason: str

class DeleteHITRequestTypeDef(TypedDict):
    HITId: str

class DeleteQualificationTypeRequestTypeDef(TypedDict):
    QualificationTypeId: str

class DeleteWorkerBlockRequestTypeDef(TypedDict):
    WorkerId: str
    Reason: NotRequired[str]

class DisassociateQualificationFromWorkerRequestTypeDef(TypedDict):
    WorkerId: str
    QualificationTypeId: str
    Reason: NotRequired[str]

class GetAssignmentRequestTypeDef(TypedDict):
    AssignmentId: str

class GetFileUploadURLRequestTypeDef(TypedDict):
    AssignmentId: str
    QuestionIdentifier: str

class GetHITRequestTypeDef(TypedDict):
    HITId: str

class GetQualificationScoreRequestTypeDef(TypedDict):
    QualificationTypeId: str
    WorkerId: str

class GetQualificationTypeRequestTypeDef(TypedDict):
    QualificationTypeId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAssignmentsForHITRequestTypeDef(TypedDict):
    HITId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    AssignmentStatuses: NotRequired[Sequence[AssignmentStatusType]]

class ListBonusPaymentsRequestTypeDef(TypedDict):
    HITId: NotRequired[str]
    AssignmentId: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListHITsForQualificationTypeRequestTypeDef(TypedDict):
    QualificationTypeId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListHITsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListQualificationRequestsRequestTypeDef(TypedDict):
    QualificationTypeId: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class QualificationRequestTypeDef(TypedDict):
    QualificationRequestId: NotRequired[str]
    QualificationTypeId: NotRequired[str]
    WorkerId: NotRequired[str]
    Test: NotRequired[str]
    Answer: NotRequired[str]
    SubmitTime: NotRequired[datetime]

class ListQualificationTypesRequestTypeDef(TypedDict):
    MustBeRequestable: bool
    Query: NotRequired[str]
    MustBeOwnedByCaller: NotRequired[bool]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListReviewPolicyResultsForHITRequestTypeDef(TypedDict):
    HITId: str
    PolicyLevels: NotRequired[Sequence[ReviewPolicyLevelType]]
    RetrieveActions: NotRequired[bool]
    RetrieveResults: NotRequired[bool]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListReviewableHITsRequestTypeDef(TypedDict):
    HITTypeId: NotRequired[str]
    Status: NotRequired[ReviewableHITStatusType]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListWorkerBlocksRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class WorkerBlockTypeDef(TypedDict):
    WorkerId: NotRequired[str]
    Reason: NotRequired[str]

class ListWorkersWithQualificationTypeRequestTypeDef(TypedDict):
    QualificationTypeId: str
    Status: NotRequired[QualificationStatusType]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class LocaleTypeDef(TypedDict):
    Country: str
    Subdivision: NotRequired[str]

class NotificationSpecificationTypeDef(TypedDict):
    Destination: str
    Transport: NotificationTransportType
    Version: str
    EventTypes: Sequence[EventTypeType]

class NotifyWorkersFailureStatusTypeDef(TypedDict):
    NotifyWorkersFailureCode: NotRequired[NotifyWorkersFailureCodeType]
    NotifyWorkersFailureMessage: NotRequired[str]
    WorkerId: NotRequired[str]

class NotifyWorkersRequestTypeDef(TypedDict):
    Subject: str
    MessageText: str
    WorkerIds: Sequence[str]

class ParameterMapEntryOutputTypeDef(TypedDict):
    Key: NotRequired[str]
    Values: NotRequired[List[str]]

class ParameterMapEntryTypeDef(TypedDict):
    Key: NotRequired[str]
    Values: NotRequired[Sequence[str]]

class RejectAssignmentRequestTypeDef(TypedDict):
    AssignmentId: str
    RequesterFeedback: str

class RejectQualificationRequestRequestTypeDef(TypedDict):
    QualificationRequestId: str
    Reason: NotRequired[str]

class ReviewActionDetailTypeDef(TypedDict):
    ActionId: NotRequired[str]
    ActionName: NotRequired[str]
    TargetId: NotRequired[str]
    TargetType: NotRequired[str]
    Status: NotRequired[ReviewActionStatusType]
    CompleteTime: NotRequired[datetime]
    Result: NotRequired[str]
    ErrorCode: NotRequired[str]

class ReviewResultDetailTypeDef(TypedDict):
    ActionId: NotRequired[str]
    SubjectId: NotRequired[str]
    SubjectType: NotRequired[str]
    QuestionId: NotRequired[str]
    Key: NotRequired[str]
    Value: NotRequired[str]

class SendBonusRequestTypeDef(TypedDict):
    WorkerId: str
    BonusAmount: str
    AssignmentId: str
    Reason: str
    UniqueRequestToken: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class UpdateHITReviewStatusRequestTypeDef(TypedDict):
    HITId: str
    Revert: NotRequired[bool]

class UpdateHITTypeOfHITRequestTypeDef(TypedDict):
    HITId: str
    HITTypeId: str

class UpdateQualificationTypeRequestTypeDef(TypedDict):
    QualificationTypeId: str
    Description: NotRequired[str]
    QualificationTypeStatus: NotRequired[QualificationTypeStatusType]
    Test: NotRequired[str]
    AnswerKey: NotRequired[str]
    TestDurationInSeconds: NotRequired[int]
    RetryDelayInSeconds: NotRequired[int]
    AutoGranted: NotRequired[bool]
    AutoGrantedValue: NotRequired[int]

class CreateHITTypeResponseTypeDef(TypedDict):
    HITTypeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountBalanceResponseTypeDef(TypedDict):
    AvailableBalance: str
    OnHoldBalance: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFileUploadURLResponseTypeDef(TypedDict):
    FileUploadURL: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssignmentsForHITResponseTypeDef(TypedDict):
    NumResults: int
    Assignments: List[AssignmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListBonusPaymentsResponseTypeDef(TypedDict):
    NumResults: int
    BonusPayments: List[BonusPaymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateQualificationTypeResponseTypeDef(TypedDict):
    QualificationType: QualificationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetQualificationTypeResponseTypeDef(TypedDict):
    QualificationType: QualificationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListQualificationTypesResponseTypeDef(TypedDict):
    NumResults: int
    QualificationTypes: List[QualificationTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateQualificationTypeResponseTypeDef(TypedDict):
    QualificationType: QualificationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssignmentsForHITRequestPaginateTypeDef(TypedDict):
    HITId: str
    AssignmentStatuses: NotRequired[Sequence[AssignmentStatusType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBonusPaymentsRequestPaginateTypeDef(TypedDict):
    HITId: NotRequired[str]
    AssignmentId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListHITsForQualificationTypeRequestPaginateTypeDef(TypedDict):
    QualificationTypeId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListHITsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListQualificationRequestsRequestPaginateTypeDef(TypedDict):
    QualificationTypeId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListQualificationTypesRequestPaginateTypeDef(TypedDict):
    MustBeRequestable: bool
    Query: NotRequired[str]
    MustBeOwnedByCaller: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListReviewableHITsRequestPaginateTypeDef(TypedDict):
    HITTypeId: NotRequired[str]
    Status: NotRequired[ReviewableHITStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkerBlocksRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkersWithQualificationTypeRequestPaginateTypeDef(TypedDict):
    QualificationTypeId: str
    Status: NotRequired[QualificationStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListQualificationRequestsResponseTypeDef(TypedDict):
    NumResults: int
    QualificationRequests: List[QualificationRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListWorkerBlocksResponseTypeDef(TypedDict):
    NumResults: int
    WorkerBlocks: List[WorkerBlockTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class QualificationRequirementOutputTypeDef(TypedDict):
    QualificationTypeId: str
    Comparator: ComparatorType
    IntegerValues: NotRequired[List[int]]
    LocaleValues: NotRequired[List[LocaleTypeDef]]
    RequiredToPreview: NotRequired[bool]
    ActionsGuarded: NotRequired[HITAccessActionsType]

class QualificationRequirementTypeDef(TypedDict):
    QualificationTypeId: str
    Comparator: ComparatorType
    IntegerValues: NotRequired[Sequence[int]]
    LocaleValues: NotRequired[Sequence[LocaleTypeDef]]
    RequiredToPreview: NotRequired[bool]
    ActionsGuarded: NotRequired[HITAccessActionsType]

class QualificationTypeDef(TypedDict):
    QualificationTypeId: NotRequired[str]
    WorkerId: NotRequired[str]
    GrantTime: NotRequired[datetime]
    IntegerValue: NotRequired[int]
    LocaleValue: NotRequired[LocaleTypeDef]
    Status: NotRequired[QualificationStatusType]

class SendTestEventNotificationRequestTypeDef(TypedDict):
    Notification: NotificationSpecificationTypeDef
    TestEventType: EventTypeType

class UpdateNotificationSettingsRequestTypeDef(TypedDict):
    HITTypeId: str
    Notification: NotRequired[NotificationSpecificationTypeDef]
    Active: NotRequired[bool]

class NotifyWorkersResponseTypeDef(TypedDict):
    NotifyWorkersFailureStatuses: List[NotifyWorkersFailureStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PolicyParameterOutputTypeDef(TypedDict):
    Key: NotRequired[str]
    Values: NotRequired[List[str]]
    MapEntries: NotRequired[List[ParameterMapEntryOutputTypeDef]]

class PolicyParameterTypeDef(TypedDict):
    Key: NotRequired[str]
    Values: NotRequired[Sequence[str]]
    MapEntries: NotRequired[Sequence[ParameterMapEntryTypeDef]]

class ReviewReportTypeDef(TypedDict):
    ReviewResults: NotRequired[List[ReviewResultDetailTypeDef]]
    ReviewActions: NotRequired[List[ReviewActionDetailTypeDef]]

class UpdateExpirationForHITRequestTypeDef(TypedDict):
    HITId: str
    ExpireAt: TimestampTypeDef

class HITTypeDef(TypedDict):
    HITId: NotRequired[str]
    HITTypeId: NotRequired[str]
    HITGroupId: NotRequired[str]
    HITLayoutId: NotRequired[str]
    CreationTime: NotRequired[datetime]
    Title: NotRequired[str]
    Description: NotRequired[str]
    Question: NotRequired[str]
    Keywords: NotRequired[str]
    HITStatus: NotRequired[HITStatusType]
    MaxAssignments: NotRequired[int]
    Reward: NotRequired[str]
    AutoApprovalDelayInSeconds: NotRequired[int]
    Expiration: NotRequired[datetime]
    AssignmentDurationInSeconds: NotRequired[int]
    RequesterAnnotation: NotRequired[str]
    QualificationRequirements: NotRequired[List[QualificationRequirementOutputTypeDef]]
    HITReviewStatus: NotRequired[HITReviewStatusType]
    NumberOfAssignmentsPending: NotRequired[int]
    NumberOfAssignmentsAvailable: NotRequired[int]
    NumberOfAssignmentsCompleted: NotRequired[int]

QualificationRequirementUnionTypeDef = Union[
    QualificationRequirementTypeDef, QualificationRequirementOutputTypeDef
]

class GetQualificationScoreResponseTypeDef(TypedDict):
    Qualification: QualificationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkersWithQualificationTypeResponseTypeDef(TypedDict):
    NumResults: int
    Qualifications: List[QualificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ReviewPolicyOutputTypeDef(TypedDict):
    PolicyName: str
    Parameters: NotRequired[List[PolicyParameterOutputTypeDef]]

class ReviewPolicyTypeDef(TypedDict):
    PolicyName: str
    Parameters: NotRequired[Sequence[PolicyParameterTypeDef]]

class CreateHITResponseTypeDef(TypedDict):
    HIT: HITTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHITWithHITTypeResponseTypeDef(TypedDict):
    HIT: HITTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssignmentResponseTypeDef(TypedDict):
    Assignment: AssignmentTypeDef
    HIT: HITTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetHITResponseTypeDef(TypedDict):
    HIT: HITTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListHITsForQualificationTypeResponseTypeDef(TypedDict):
    NumResults: int
    HITs: List[HITTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListHITsResponseTypeDef(TypedDict):
    NumResults: int
    HITs: List[HITTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListReviewableHITsResponseTypeDef(TypedDict):
    NumResults: int
    HITs: List[HITTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateHITTypeRequestTypeDef(TypedDict):
    AssignmentDurationInSeconds: int
    Reward: str
    Title: str
    Description: str
    AutoApprovalDelayInSeconds: NotRequired[int]
    Keywords: NotRequired[str]
    QualificationRequirements: NotRequired[Sequence[QualificationRequirementUnionTypeDef]]

class ListReviewPolicyResultsForHITResponseTypeDef(TypedDict):
    HITId: str
    AssignmentReviewPolicy: ReviewPolicyOutputTypeDef
    HITReviewPolicy: ReviewPolicyOutputTypeDef
    AssignmentReviewReport: ReviewReportTypeDef
    HITReviewReport: ReviewReportTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

ReviewPolicyUnionTypeDef = Union[ReviewPolicyTypeDef, ReviewPolicyOutputTypeDef]

class CreateHITRequestTypeDef(TypedDict):
    LifetimeInSeconds: int
    AssignmentDurationInSeconds: int
    Reward: str
    Title: str
    Description: str
    MaxAssignments: NotRequired[int]
    AutoApprovalDelayInSeconds: NotRequired[int]
    Keywords: NotRequired[str]
    Question: NotRequired[str]
    RequesterAnnotation: NotRequired[str]
    QualificationRequirements: NotRequired[Sequence[QualificationRequirementUnionTypeDef]]
    UniqueRequestToken: NotRequired[str]
    AssignmentReviewPolicy: NotRequired[ReviewPolicyUnionTypeDef]
    HITReviewPolicy: NotRequired[ReviewPolicyUnionTypeDef]
    HITLayoutId: NotRequired[str]
    HITLayoutParameters: NotRequired[Sequence[HITLayoutParameterTypeDef]]

class CreateHITWithHITTypeRequestTypeDef(TypedDict):
    HITTypeId: str
    LifetimeInSeconds: int
    MaxAssignments: NotRequired[int]
    Question: NotRequired[str]
    RequesterAnnotation: NotRequired[str]
    UniqueRequestToken: NotRequired[str]
    AssignmentReviewPolicy: NotRequired[ReviewPolicyUnionTypeDef]
    HITReviewPolicy: NotRequired[ReviewPolicyUnionTypeDef]
    HITLayoutId: NotRequired[str]
    HITLayoutParameters: NotRequired[Sequence[HITLayoutParameterTypeDef]]
