"""
Type annotations for mturk service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mturk.type_defs import AcceptQualificationRequestRequestRequestTypeDef

    data: AcceptQualificationRequestRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

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

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AcceptQualificationRequestRequestRequestTypeDef",
    "ApproveAssignmentRequestRequestTypeDef",
    "AssignmentTypeDef",
    "AssociateQualificationWithWorkerRequestRequestTypeDef",
    "BonusPaymentTypeDef",
    "CreateAdditionalAssignmentsForHITRequestRequestTypeDef",
    "CreateHITRequestRequestTypeDef",
    "CreateHITResponseTypeDef",
    "CreateHITTypeRequestRequestTypeDef",
    "CreateHITTypeResponseTypeDef",
    "CreateHITWithHITTypeRequestRequestTypeDef",
    "CreateHITWithHITTypeResponseTypeDef",
    "CreateQualificationTypeRequestRequestTypeDef",
    "CreateQualificationTypeResponseTypeDef",
    "CreateWorkerBlockRequestRequestTypeDef",
    "DeleteHITRequestRequestTypeDef",
    "DeleteQualificationTypeRequestRequestTypeDef",
    "DeleteWorkerBlockRequestRequestTypeDef",
    "DisassociateQualificationFromWorkerRequestRequestTypeDef",
    "GetAccountBalanceResponseTypeDef",
    "GetAssignmentRequestRequestTypeDef",
    "GetAssignmentResponseTypeDef",
    "GetFileUploadURLRequestRequestTypeDef",
    "GetFileUploadURLResponseTypeDef",
    "GetHITRequestRequestTypeDef",
    "GetHITResponseTypeDef",
    "GetQualificationScoreRequestRequestTypeDef",
    "GetQualificationScoreResponseTypeDef",
    "GetQualificationTypeRequestRequestTypeDef",
    "GetQualificationTypeResponseTypeDef",
    "HITLayoutParameterTypeDef",
    "HITTypeDef",
    "ListAssignmentsForHITRequestRequestTypeDef",
    "ListAssignmentsForHITResponseTypeDef",
    "ListBonusPaymentsRequestRequestTypeDef",
    "ListBonusPaymentsResponseTypeDef",
    "ListHITsForQualificationTypeRequestRequestTypeDef",
    "ListHITsForQualificationTypeResponseTypeDef",
    "ListHITsRequestRequestTypeDef",
    "ListHITsResponseTypeDef",
    "ListQualificationRequestsRequestRequestTypeDef",
    "ListQualificationRequestsResponseTypeDef",
    "ListQualificationTypesRequestRequestTypeDef",
    "ListQualificationTypesResponseTypeDef",
    "ListReviewPolicyResultsForHITRequestRequestTypeDef",
    "ListReviewPolicyResultsForHITResponseTypeDef",
    "ListReviewableHITsRequestRequestTypeDef",
    "ListReviewableHITsResponseTypeDef",
    "ListWorkerBlocksRequestRequestTypeDef",
    "ListWorkerBlocksResponseTypeDef",
    "ListWorkersWithQualificationTypeRequestRequestTypeDef",
    "ListWorkersWithQualificationTypeResponseTypeDef",
    "LocaleTypeDef",
    "NotificationSpecificationTypeDef",
    "NotifyWorkersFailureStatusTypeDef",
    "NotifyWorkersRequestRequestTypeDef",
    "NotifyWorkersResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterMapEntryTypeDef",
    "PolicyParameterTypeDef",
    "QualificationRequestTypeDef",
    "QualificationRequirementTypeDef",
    "QualificationTypeDef",
    "QualificationTypeTypeDef",
    "RejectAssignmentRequestRequestTypeDef",
    "RejectQualificationRequestRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ReviewActionDetailTypeDef",
    "ReviewPolicyTypeDef",
    "ReviewReportTypeDef",
    "ReviewResultDetailTypeDef",
    "SendBonusRequestRequestTypeDef",
    "SendTestEventNotificationRequestRequestTypeDef",
    "UpdateExpirationForHITRequestRequestTypeDef",
    "UpdateHITReviewStatusRequestRequestTypeDef",
    "UpdateHITTypeOfHITRequestRequestTypeDef",
    "UpdateNotificationSettingsRequestRequestTypeDef",
    "UpdateQualificationTypeRequestRequestTypeDef",
    "UpdateQualificationTypeResponseTypeDef",
    "WorkerBlockTypeDef",
)

_RequiredAcceptQualificationRequestRequestRequestTypeDef = TypedDict(
    "_RequiredAcceptQualificationRequestRequestRequestTypeDef",
    {
        "QualificationRequestId": str,
    },
)
_OptionalAcceptQualificationRequestRequestRequestTypeDef = TypedDict(
    "_OptionalAcceptQualificationRequestRequestRequestTypeDef",
    {
        "IntegerValue": int,
    },
    total=False,
)

class AcceptQualificationRequestRequestRequestTypeDef(
    _RequiredAcceptQualificationRequestRequestRequestTypeDef,
    _OptionalAcceptQualificationRequestRequestRequestTypeDef,
):
    pass

_RequiredApproveAssignmentRequestRequestTypeDef = TypedDict(
    "_RequiredApproveAssignmentRequestRequestTypeDef",
    {
        "AssignmentId": str,
    },
)
_OptionalApproveAssignmentRequestRequestTypeDef = TypedDict(
    "_OptionalApproveAssignmentRequestRequestTypeDef",
    {
        "RequesterFeedback": str,
        "OverrideRejection": bool,
    },
    total=False,
)

class ApproveAssignmentRequestRequestTypeDef(
    _RequiredApproveAssignmentRequestRequestTypeDef, _OptionalApproveAssignmentRequestRequestTypeDef
):
    pass

AssignmentTypeDef = TypedDict(
    "AssignmentTypeDef",
    {
        "AssignmentId": str,
        "WorkerId": str,
        "HITId": str,
        "AssignmentStatus": AssignmentStatusType,
        "AutoApprovalTime": datetime,
        "AcceptTime": datetime,
        "SubmitTime": datetime,
        "ApprovalTime": datetime,
        "RejectionTime": datetime,
        "Deadline": datetime,
        "Answer": str,
        "RequesterFeedback": str,
    },
    total=False,
)

_RequiredAssociateQualificationWithWorkerRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateQualificationWithWorkerRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
    },
)
_OptionalAssociateQualificationWithWorkerRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateQualificationWithWorkerRequestRequestTypeDef",
    {
        "IntegerValue": int,
        "SendNotification": bool,
    },
    total=False,
)

class AssociateQualificationWithWorkerRequestRequestTypeDef(
    _RequiredAssociateQualificationWithWorkerRequestRequestTypeDef,
    _OptionalAssociateQualificationWithWorkerRequestRequestTypeDef,
):
    pass

BonusPaymentTypeDef = TypedDict(
    "BonusPaymentTypeDef",
    {
        "WorkerId": str,
        "BonusAmount": str,
        "AssignmentId": str,
        "Reason": str,
        "GrantTime": datetime,
    },
    total=False,
)

_RequiredCreateAdditionalAssignmentsForHITRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAdditionalAssignmentsForHITRequestRequestTypeDef",
    {
        "HITId": str,
        "NumberOfAdditionalAssignments": int,
    },
)
_OptionalCreateAdditionalAssignmentsForHITRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAdditionalAssignmentsForHITRequestRequestTypeDef",
    {
        "UniqueRequestToken": str,
    },
    total=False,
)

class CreateAdditionalAssignmentsForHITRequestRequestTypeDef(
    _RequiredCreateAdditionalAssignmentsForHITRequestRequestTypeDef,
    _OptionalCreateAdditionalAssignmentsForHITRequestRequestTypeDef,
):
    pass

_RequiredCreateHITRequestRequestTypeDef = TypedDict(
    "_RequiredCreateHITRequestRequestTypeDef",
    {
        "LifetimeInSeconds": int,
        "AssignmentDurationInSeconds": int,
        "Reward": str,
        "Title": str,
        "Description": str,
    },
)
_OptionalCreateHITRequestRequestTypeDef = TypedDict(
    "_OptionalCreateHITRequestRequestTypeDef",
    {
        "MaxAssignments": int,
        "AutoApprovalDelayInSeconds": int,
        "Keywords": str,
        "Question": str,
        "RequesterAnnotation": str,
        "QualificationRequirements": List["QualificationRequirementTypeDef"],
        "UniqueRequestToken": str,
        "AssignmentReviewPolicy": "ReviewPolicyTypeDef",
        "HITReviewPolicy": "ReviewPolicyTypeDef",
        "HITLayoutId": str,
        "HITLayoutParameters": List["HITLayoutParameterTypeDef"],
    },
    total=False,
)

class CreateHITRequestRequestTypeDef(
    _RequiredCreateHITRequestRequestTypeDef, _OptionalCreateHITRequestRequestTypeDef
):
    pass

CreateHITResponseTypeDef = TypedDict(
    "CreateHITResponseTypeDef",
    {
        "HIT": "HITTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHITTypeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateHITTypeRequestRequestTypeDef",
    {
        "AssignmentDurationInSeconds": int,
        "Reward": str,
        "Title": str,
        "Description": str,
    },
)
_OptionalCreateHITTypeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateHITTypeRequestRequestTypeDef",
    {
        "AutoApprovalDelayInSeconds": int,
        "Keywords": str,
        "QualificationRequirements": List["QualificationRequirementTypeDef"],
    },
    total=False,
)

class CreateHITTypeRequestRequestTypeDef(
    _RequiredCreateHITTypeRequestRequestTypeDef, _OptionalCreateHITTypeRequestRequestTypeDef
):
    pass

CreateHITTypeResponseTypeDef = TypedDict(
    "CreateHITTypeResponseTypeDef",
    {
        "HITTypeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHITWithHITTypeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateHITWithHITTypeRequestRequestTypeDef",
    {
        "HITTypeId": str,
        "LifetimeInSeconds": int,
    },
)
_OptionalCreateHITWithHITTypeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateHITWithHITTypeRequestRequestTypeDef",
    {
        "MaxAssignments": int,
        "Question": str,
        "RequesterAnnotation": str,
        "UniqueRequestToken": str,
        "AssignmentReviewPolicy": "ReviewPolicyTypeDef",
        "HITReviewPolicy": "ReviewPolicyTypeDef",
        "HITLayoutId": str,
        "HITLayoutParameters": List["HITLayoutParameterTypeDef"],
    },
    total=False,
)

class CreateHITWithHITTypeRequestRequestTypeDef(
    _RequiredCreateHITWithHITTypeRequestRequestTypeDef,
    _OptionalCreateHITWithHITTypeRequestRequestTypeDef,
):
    pass

CreateHITWithHITTypeResponseTypeDef = TypedDict(
    "CreateHITWithHITTypeResponseTypeDef",
    {
        "HIT": "HITTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateQualificationTypeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateQualificationTypeRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "QualificationTypeStatus": QualificationTypeStatusType,
    },
)
_OptionalCreateQualificationTypeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateQualificationTypeRequestRequestTypeDef",
    {
        "Keywords": str,
        "RetryDelayInSeconds": int,
        "Test": str,
        "AnswerKey": str,
        "TestDurationInSeconds": int,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)

class CreateQualificationTypeRequestRequestTypeDef(
    _RequiredCreateQualificationTypeRequestRequestTypeDef,
    _OptionalCreateQualificationTypeRequestRequestTypeDef,
):
    pass

CreateQualificationTypeResponseTypeDef = TypedDict(
    "CreateQualificationTypeResponseTypeDef",
    {
        "QualificationType": "QualificationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorkerBlockRequestRequestTypeDef = TypedDict(
    "CreateWorkerBlockRequestRequestTypeDef",
    {
        "WorkerId": str,
        "Reason": str,
    },
)

DeleteHITRequestRequestTypeDef = TypedDict(
    "DeleteHITRequestRequestTypeDef",
    {
        "HITId": str,
    },
)

DeleteQualificationTypeRequestRequestTypeDef = TypedDict(
    "DeleteQualificationTypeRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
    },
)

_RequiredDeleteWorkerBlockRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteWorkerBlockRequestRequestTypeDef",
    {
        "WorkerId": str,
    },
)
_OptionalDeleteWorkerBlockRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteWorkerBlockRequestRequestTypeDef",
    {
        "Reason": str,
    },
    total=False,
)

class DeleteWorkerBlockRequestRequestTypeDef(
    _RequiredDeleteWorkerBlockRequestRequestTypeDef, _OptionalDeleteWorkerBlockRequestRequestTypeDef
):
    pass

_RequiredDisassociateQualificationFromWorkerRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateQualificationFromWorkerRequestRequestTypeDef",
    {
        "WorkerId": str,
        "QualificationTypeId": str,
    },
)
_OptionalDisassociateQualificationFromWorkerRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateQualificationFromWorkerRequestRequestTypeDef",
    {
        "Reason": str,
    },
    total=False,
)

class DisassociateQualificationFromWorkerRequestRequestTypeDef(
    _RequiredDisassociateQualificationFromWorkerRequestRequestTypeDef,
    _OptionalDisassociateQualificationFromWorkerRequestRequestTypeDef,
):
    pass

GetAccountBalanceResponseTypeDef = TypedDict(
    "GetAccountBalanceResponseTypeDef",
    {
        "AvailableBalance": str,
        "OnHoldBalance": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssignmentRequestRequestTypeDef = TypedDict(
    "GetAssignmentRequestRequestTypeDef",
    {
        "AssignmentId": str,
    },
)

GetAssignmentResponseTypeDef = TypedDict(
    "GetAssignmentResponseTypeDef",
    {
        "Assignment": "AssignmentTypeDef",
        "HIT": "HITTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFileUploadURLRequestRequestTypeDef = TypedDict(
    "GetFileUploadURLRequestRequestTypeDef",
    {
        "AssignmentId": str,
        "QuestionIdentifier": str,
    },
)

GetFileUploadURLResponseTypeDef = TypedDict(
    "GetFileUploadURLResponseTypeDef",
    {
        "FileUploadURL": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHITRequestRequestTypeDef = TypedDict(
    "GetHITRequestRequestTypeDef",
    {
        "HITId": str,
    },
)

GetHITResponseTypeDef = TypedDict(
    "GetHITResponseTypeDef",
    {
        "HIT": "HITTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQualificationScoreRequestRequestTypeDef = TypedDict(
    "GetQualificationScoreRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
    },
)

GetQualificationScoreResponseTypeDef = TypedDict(
    "GetQualificationScoreResponseTypeDef",
    {
        "Qualification": "QualificationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQualificationTypeRequestRequestTypeDef = TypedDict(
    "GetQualificationTypeRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
    },
)

GetQualificationTypeResponseTypeDef = TypedDict(
    "GetQualificationTypeResponseTypeDef",
    {
        "QualificationType": "QualificationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HITLayoutParameterTypeDef = TypedDict(
    "HITLayoutParameterTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

HITTypeDef = TypedDict(
    "HITTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": HITStatusType,
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List["QualificationRequirementTypeDef"],
        "HITReviewStatus": HITReviewStatusType,
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)

_RequiredListAssignmentsForHITRequestRequestTypeDef = TypedDict(
    "_RequiredListAssignmentsForHITRequestRequestTypeDef",
    {
        "HITId": str,
    },
)
_OptionalListAssignmentsForHITRequestRequestTypeDef = TypedDict(
    "_OptionalListAssignmentsForHITRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "AssignmentStatuses": List[AssignmentStatusType],
    },
    total=False,
)

class ListAssignmentsForHITRequestRequestTypeDef(
    _RequiredListAssignmentsForHITRequestRequestTypeDef,
    _OptionalListAssignmentsForHITRequestRequestTypeDef,
):
    pass

ListAssignmentsForHITResponseTypeDef = TypedDict(
    "ListAssignmentsForHITResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "Assignments": List["AssignmentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBonusPaymentsRequestRequestTypeDef = TypedDict(
    "ListBonusPaymentsRequestRequestTypeDef",
    {
        "HITId": str,
        "AssignmentId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListBonusPaymentsResponseTypeDef = TypedDict(
    "ListBonusPaymentsResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "BonusPayments": List["BonusPaymentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListHITsForQualificationTypeRequestRequestTypeDef = TypedDict(
    "_RequiredListHITsForQualificationTypeRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
    },
)
_OptionalListHITsForQualificationTypeRequestRequestTypeDef = TypedDict(
    "_OptionalListHITsForQualificationTypeRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListHITsForQualificationTypeRequestRequestTypeDef(
    _RequiredListHITsForQualificationTypeRequestRequestTypeDef,
    _OptionalListHITsForQualificationTypeRequestRequestTypeDef,
):
    pass

ListHITsForQualificationTypeResponseTypeDef = TypedDict(
    "ListHITsForQualificationTypeResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List["HITTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHITsRequestRequestTypeDef = TypedDict(
    "ListHITsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListHITsResponseTypeDef = TypedDict(
    "ListHITsResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List["HITTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQualificationRequestsRequestRequestTypeDef = TypedDict(
    "ListQualificationRequestsRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListQualificationRequestsResponseTypeDef = TypedDict(
    "ListQualificationRequestsResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "QualificationRequests": List["QualificationRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQualificationTypesRequestRequestTypeDef = TypedDict(
    "_RequiredListQualificationTypesRequestRequestTypeDef",
    {
        "MustBeRequestable": bool,
    },
)
_OptionalListQualificationTypesRequestRequestTypeDef = TypedDict(
    "_OptionalListQualificationTypesRequestRequestTypeDef",
    {
        "Query": str,
        "MustBeOwnedByCaller": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListQualificationTypesRequestRequestTypeDef(
    _RequiredListQualificationTypesRequestRequestTypeDef,
    _OptionalListQualificationTypesRequestRequestTypeDef,
):
    pass

ListQualificationTypesResponseTypeDef = TypedDict(
    "ListQualificationTypesResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "QualificationTypes": List["QualificationTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListReviewPolicyResultsForHITRequestRequestTypeDef = TypedDict(
    "_RequiredListReviewPolicyResultsForHITRequestRequestTypeDef",
    {
        "HITId": str,
    },
)
_OptionalListReviewPolicyResultsForHITRequestRequestTypeDef = TypedDict(
    "_OptionalListReviewPolicyResultsForHITRequestRequestTypeDef",
    {
        "PolicyLevels": List[ReviewPolicyLevelType],
        "RetrieveActions": bool,
        "RetrieveResults": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListReviewPolicyResultsForHITRequestRequestTypeDef(
    _RequiredListReviewPolicyResultsForHITRequestRequestTypeDef,
    _OptionalListReviewPolicyResultsForHITRequestRequestTypeDef,
):
    pass

ListReviewPolicyResultsForHITResponseTypeDef = TypedDict(
    "ListReviewPolicyResultsForHITResponseTypeDef",
    {
        "HITId": str,
        "AssignmentReviewPolicy": "ReviewPolicyTypeDef",
        "HITReviewPolicy": "ReviewPolicyTypeDef",
        "AssignmentReviewReport": "ReviewReportTypeDef",
        "HITReviewReport": "ReviewReportTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReviewableHITsRequestRequestTypeDef = TypedDict(
    "ListReviewableHITsRequestRequestTypeDef",
    {
        "HITTypeId": str,
        "Status": ReviewableHITStatusType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListReviewableHITsResponseTypeDef = TypedDict(
    "ListReviewableHITsResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List["HITTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkerBlocksRequestRequestTypeDef = TypedDict(
    "ListWorkerBlocksRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListWorkerBlocksResponseTypeDef = TypedDict(
    "ListWorkerBlocksResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "WorkerBlocks": List["WorkerBlockTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWorkersWithQualificationTypeRequestRequestTypeDef = TypedDict(
    "_RequiredListWorkersWithQualificationTypeRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
    },
)
_OptionalListWorkersWithQualificationTypeRequestRequestTypeDef = TypedDict(
    "_OptionalListWorkersWithQualificationTypeRequestRequestTypeDef",
    {
        "Status": QualificationStatusType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListWorkersWithQualificationTypeRequestRequestTypeDef(
    _RequiredListWorkersWithQualificationTypeRequestRequestTypeDef,
    _OptionalListWorkersWithQualificationTypeRequestRequestTypeDef,
):
    pass

ListWorkersWithQualificationTypeResponseTypeDef = TypedDict(
    "ListWorkersWithQualificationTypeResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "Qualifications": List["QualificationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLocaleTypeDef = TypedDict(
    "_RequiredLocaleTypeDef",
    {
        "Country": str,
    },
)
_OptionalLocaleTypeDef = TypedDict(
    "_OptionalLocaleTypeDef",
    {
        "Subdivision": str,
    },
    total=False,
)

class LocaleTypeDef(_RequiredLocaleTypeDef, _OptionalLocaleTypeDef):
    pass

NotificationSpecificationTypeDef = TypedDict(
    "NotificationSpecificationTypeDef",
    {
        "Destination": str,
        "Transport": NotificationTransportType,
        "Version": str,
        "EventTypes": List[EventTypeType],
    },
)

NotifyWorkersFailureStatusTypeDef = TypedDict(
    "NotifyWorkersFailureStatusTypeDef",
    {
        "NotifyWorkersFailureCode": NotifyWorkersFailureCodeType,
        "NotifyWorkersFailureMessage": str,
        "WorkerId": str,
    },
    total=False,
)

NotifyWorkersRequestRequestTypeDef = TypedDict(
    "NotifyWorkersRequestRequestTypeDef",
    {
        "Subject": str,
        "MessageText": str,
        "WorkerIds": List[str],
    },
)

NotifyWorkersResponseTypeDef = TypedDict(
    "NotifyWorkersResponseTypeDef",
    {
        "NotifyWorkersFailureStatuses": List["NotifyWorkersFailureStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ParameterMapEntryTypeDef = TypedDict(
    "ParameterMapEntryTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
    total=False,
)

PolicyParameterTypeDef = TypedDict(
    "PolicyParameterTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MapEntries": List["ParameterMapEntryTypeDef"],
    },
    total=False,
)

QualificationRequestTypeDef = TypedDict(
    "QualificationRequestTypeDef",
    {
        "QualificationRequestId": str,
        "QualificationTypeId": str,
        "WorkerId": str,
        "Test": str,
        "Answer": str,
        "SubmitTime": datetime,
    },
    total=False,
)

_RequiredQualificationRequirementTypeDef = TypedDict(
    "_RequiredQualificationRequirementTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": ComparatorType,
    },
)
_OptionalQualificationRequirementTypeDef = TypedDict(
    "_OptionalQualificationRequirementTypeDef",
    {
        "IntegerValues": List[int],
        "LocaleValues": List["LocaleTypeDef"],
        "RequiredToPreview": bool,
        "ActionsGuarded": HITAccessActionsType,
    },
    total=False,
)

class QualificationRequirementTypeDef(
    _RequiredQualificationRequirementTypeDef, _OptionalQualificationRequirementTypeDef
):
    pass

QualificationTypeDef = TypedDict(
    "QualificationTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
        "GrantTime": datetime,
        "IntegerValue": int,
        "LocaleValue": "LocaleTypeDef",
        "Status": QualificationStatusType,
    },
    total=False,
)

QualificationTypeTypeDef = TypedDict(
    "QualificationTypeTypeDef",
    {
        "QualificationTypeId": str,
        "CreationTime": datetime,
        "Name": str,
        "Description": str,
        "Keywords": str,
        "QualificationTypeStatus": QualificationTypeStatusType,
        "Test": str,
        "TestDurationInSeconds": int,
        "AnswerKey": str,
        "RetryDelayInSeconds": int,
        "IsRequestable": bool,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)

RejectAssignmentRequestRequestTypeDef = TypedDict(
    "RejectAssignmentRequestRequestTypeDef",
    {
        "AssignmentId": str,
        "RequesterFeedback": str,
    },
)

_RequiredRejectQualificationRequestRequestRequestTypeDef = TypedDict(
    "_RequiredRejectQualificationRequestRequestRequestTypeDef",
    {
        "QualificationRequestId": str,
    },
)
_OptionalRejectQualificationRequestRequestRequestTypeDef = TypedDict(
    "_OptionalRejectQualificationRequestRequestRequestTypeDef",
    {
        "Reason": str,
    },
    total=False,
)

class RejectQualificationRequestRequestRequestTypeDef(
    _RequiredRejectQualificationRequestRequestRequestTypeDef,
    _OptionalRejectQualificationRequestRequestRequestTypeDef,
):
    pass

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

ReviewActionDetailTypeDef = TypedDict(
    "ReviewActionDetailTypeDef",
    {
        "ActionId": str,
        "ActionName": str,
        "TargetId": str,
        "TargetType": str,
        "Status": ReviewActionStatusType,
        "CompleteTime": datetime,
        "Result": str,
        "ErrorCode": str,
    },
    total=False,
)

_RequiredReviewPolicyTypeDef = TypedDict(
    "_RequiredReviewPolicyTypeDef",
    {
        "PolicyName": str,
    },
)
_OptionalReviewPolicyTypeDef = TypedDict(
    "_OptionalReviewPolicyTypeDef",
    {
        "Parameters": List["PolicyParameterTypeDef"],
    },
    total=False,
)

class ReviewPolicyTypeDef(_RequiredReviewPolicyTypeDef, _OptionalReviewPolicyTypeDef):
    pass

ReviewReportTypeDef = TypedDict(
    "ReviewReportTypeDef",
    {
        "ReviewResults": List["ReviewResultDetailTypeDef"],
        "ReviewActions": List["ReviewActionDetailTypeDef"],
    },
    total=False,
)

ReviewResultDetailTypeDef = TypedDict(
    "ReviewResultDetailTypeDef",
    {
        "ActionId": str,
        "SubjectId": str,
        "SubjectType": str,
        "QuestionId": str,
        "Key": str,
        "Value": str,
    },
    total=False,
)

_RequiredSendBonusRequestRequestTypeDef = TypedDict(
    "_RequiredSendBonusRequestRequestTypeDef",
    {
        "WorkerId": str,
        "BonusAmount": str,
        "AssignmentId": str,
        "Reason": str,
    },
)
_OptionalSendBonusRequestRequestTypeDef = TypedDict(
    "_OptionalSendBonusRequestRequestTypeDef",
    {
        "UniqueRequestToken": str,
    },
    total=False,
)

class SendBonusRequestRequestTypeDef(
    _RequiredSendBonusRequestRequestTypeDef, _OptionalSendBonusRequestRequestTypeDef
):
    pass

SendTestEventNotificationRequestRequestTypeDef = TypedDict(
    "SendTestEventNotificationRequestRequestTypeDef",
    {
        "Notification": "NotificationSpecificationTypeDef",
        "TestEventType": EventTypeType,
    },
)

UpdateExpirationForHITRequestRequestTypeDef = TypedDict(
    "UpdateExpirationForHITRequestRequestTypeDef",
    {
        "HITId": str,
        "ExpireAt": Union[datetime, str],
    },
)

_RequiredUpdateHITReviewStatusRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateHITReviewStatusRequestRequestTypeDef",
    {
        "HITId": str,
    },
)
_OptionalUpdateHITReviewStatusRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateHITReviewStatusRequestRequestTypeDef",
    {
        "Revert": bool,
    },
    total=False,
)

class UpdateHITReviewStatusRequestRequestTypeDef(
    _RequiredUpdateHITReviewStatusRequestRequestTypeDef,
    _OptionalUpdateHITReviewStatusRequestRequestTypeDef,
):
    pass

UpdateHITTypeOfHITRequestRequestTypeDef = TypedDict(
    "UpdateHITTypeOfHITRequestRequestTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
    },
)

_RequiredUpdateNotificationSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateNotificationSettingsRequestRequestTypeDef",
    {
        "HITTypeId": str,
    },
)
_OptionalUpdateNotificationSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateNotificationSettingsRequestRequestTypeDef",
    {
        "Notification": "NotificationSpecificationTypeDef",
        "Active": bool,
    },
    total=False,
)

class UpdateNotificationSettingsRequestRequestTypeDef(
    _RequiredUpdateNotificationSettingsRequestRequestTypeDef,
    _OptionalUpdateNotificationSettingsRequestRequestTypeDef,
):
    pass

_RequiredUpdateQualificationTypeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateQualificationTypeRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
    },
)
_OptionalUpdateQualificationTypeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateQualificationTypeRequestRequestTypeDef",
    {
        "Description": str,
        "QualificationTypeStatus": QualificationTypeStatusType,
        "Test": str,
        "AnswerKey": str,
        "TestDurationInSeconds": int,
        "RetryDelayInSeconds": int,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)

class UpdateQualificationTypeRequestRequestTypeDef(
    _RequiredUpdateQualificationTypeRequestRequestTypeDef,
    _OptionalUpdateQualificationTypeRequestRequestTypeDef,
):
    pass

UpdateQualificationTypeResponseTypeDef = TypedDict(
    "UpdateQualificationTypeResponseTypeDef",
    {
        "QualificationType": "QualificationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WorkerBlockTypeDef = TypedDict(
    "WorkerBlockTypeDef",
    {
        "WorkerId": str,
        "Reason": str,
    },
    total=False,
)
