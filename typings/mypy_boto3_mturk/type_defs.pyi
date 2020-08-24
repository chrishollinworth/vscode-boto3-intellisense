"""
Main interface for mturk service type definitions.

Usage::

    ```python
    from mypy_boto3_mturk.type_defs import AssignmentTypeDef

    data: AssignmentTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssignmentTypeDef",
    "BonusPaymentTypeDef",
    "HITTypeDef",
    "LocaleTypeDef",
    "NotifyWorkersFailureStatusTypeDef",
    "ParameterMapEntryTypeDef",
    "PolicyParameterTypeDef",
    "QualificationRequestTypeDef",
    "QualificationRequirementTypeDef",
    "QualificationTypeDef",
    "QualificationTypeTypeDef",
    "ReviewActionDetailTypeDef",
    "ReviewPolicyTypeDef",
    "ReviewReportTypeDef",
    "ReviewResultDetailTypeDef",
    "WorkerBlockTypeDef",
    "CreateHITResponseTypeDef",
    "CreateHITTypeResponseTypeDef",
    "CreateHITWithHITTypeResponseTypeDef",
    "CreateQualificationTypeResponseTypeDef",
    "GetAccountBalanceResponseTypeDef",
    "GetAssignmentResponseTypeDef",
    "GetFileUploadURLResponseTypeDef",
    "GetHITResponseTypeDef",
    "GetQualificationScoreResponseTypeDef",
    "GetQualificationTypeResponseTypeDef",
    "HITLayoutParameterTypeDef",
    "ListAssignmentsForHITResponseTypeDef",
    "ListBonusPaymentsResponseTypeDef",
    "ListHITsForQualificationTypeResponseTypeDef",
    "ListHITsResponseTypeDef",
    "ListQualificationRequestsResponseTypeDef",
    "ListQualificationTypesResponseTypeDef",
    "ListReviewPolicyResultsForHITResponseTypeDef",
    "ListReviewableHITsResponseTypeDef",
    "ListWorkerBlocksResponseTypeDef",
    "ListWorkersWithQualificationTypeResponseTypeDef",
    "NotificationSpecificationTypeDef",
    "NotifyWorkersResponseTypeDef",
    "PaginatorConfigTypeDef",
    "UpdateQualificationTypeResponseTypeDef",
)

AssignmentTypeDef = TypedDict(
    "AssignmentTypeDef",
    {
        "AssignmentId": str,
        "WorkerId": str,
        "HITId": str,
        "AssignmentStatus": Literal["Submitted", "Approved", "Rejected"],
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
        "HITStatus": Literal["Assignable", "Unassignable", "Reviewable", "Reviewing", "Disposed"],
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List["QualificationRequirementTypeDef"],
        "HITReviewStatus": Literal[
            "NotReviewed", "MarkedForReview", "ReviewedAppropriate", "ReviewedInappropriate"
        ],
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)

_RequiredLocaleTypeDef = TypedDict("_RequiredLocaleTypeDef", {"Country": str})
_OptionalLocaleTypeDef = TypedDict("_OptionalLocaleTypeDef", {"Subdivision": str}, total=False)


class LocaleTypeDef(_RequiredLocaleTypeDef, _OptionalLocaleTypeDef):
    pass


NotifyWorkersFailureStatusTypeDef = TypedDict(
    "NotifyWorkersFailureStatusTypeDef",
    {
        "NotifyWorkersFailureCode": Literal["SoftFailure", "HardFailure"],
        "NotifyWorkersFailureMessage": str,
        "WorkerId": str,
    },
    total=False,
)

ParameterMapEntryTypeDef = TypedDict(
    "ParameterMapEntryTypeDef", {"Key": str, "Values": List[str]}, total=False
)

PolicyParameterTypeDef = TypedDict(
    "PolicyParameterTypeDef",
    {"Key": str, "Values": List[str], "MapEntries": List["ParameterMapEntryTypeDef"]},
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
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
    },
)
_OptionalQualificationRequirementTypeDef = TypedDict(
    "_OptionalQualificationRequirementTypeDef",
    {
        "IntegerValues": List[int],
        "LocaleValues": List["LocaleTypeDef"],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
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
        "Status": Literal["Granted", "Revoked"],
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
        "QualificationTypeStatus": Literal["Active", "Inactive"],
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

ReviewActionDetailTypeDef = TypedDict(
    "ReviewActionDetailTypeDef",
    {
        "ActionId": str,
        "ActionName": str,
        "TargetId": str,
        "TargetType": str,
        "Status": Literal["Intended", "Succeeded", "Failed", "Cancelled"],
        "CompleteTime": datetime,
        "Result": str,
        "ErrorCode": str,
    },
    total=False,
)

_RequiredReviewPolicyTypeDef = TypedDict("_RequiredReviewPolicyTypeDef", {"PolicyName": str})
_OptionalReviewPolicyTypeDef = TypedDict(
    "_OptionalReviewPolicyTypeDef", {"Parameters": List["PolicyParameterTypeDef"]}, total=False
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

WorkerBlockTypeDef = TypedDict("WorkerBlockTypeDef", {"WorkerId": str, "Reason": str}, total=False)

CreateHITResponseTypeDef = TypedDict("CreateHITResponseTypeDef", {"HIT": "HITTypeDef"}, total=False)

CreateHITTypeResponseTypeDef = TypedDict(
    "CreateHITTypeResponseTypeDef", {"HITTypeId": str}, total=False
)

CreateHITWithHITTypeResponseTypeDef = TypedDict(
    "CreateHITWithHITTypeResponseTypeDef", {"HIT": "HITTypeDef"}, total=False
)

CreateQualificationTypeResponseTypeDef = TypedDict(
    "CreateQualificationTypeResponseTypeDef",
    {"QualificationType": "QualificationTypeTypeDef"},
    total=False,
)

GetAccountBalanceResponseTypeDef = TypedDict(
    "GetAccountBalanceResponseTypeDef", {"AvailableBalance": str, "OnHoldBalance": str}, total=False
)

GetAssignmentResponseTypeDef = TypedDict(
    "GetAssignmentResponseTypeDef",
    {"Assignment": "AssignmentTypeDef", "HIT": "HITTypeDef"},
    total=False,
)

GetFileUploadURLResponseTypeDef = TypedDict(
    "GetFileUploadURLResponseTypeDef", {"FileUploadURL": str}, total=False
)

GetHITResponseTypeDef = TypedDict("GetHITResponseTypeDef", {"HIT": "HITTypeDef"}, total=False)

GetQualificationScoreResponseTypeDef = TypedDict(
    "GetQualificationScoreResponseTypeDef", {"Qualification": "QualificationTypeDef"}, total=False
)

GetQualificationTypeResponseTypeDef = TypedDict(
    "GetQualificationTypeResponseTypeDef",
    {"QualificationType": "QualificationTypeTypeDef"},
    total=False,
)

HITLayoutParameterTypeDef = TypedDict("HITLayoutParameterTypeDef", {"Name": str, "Value": str})

ListAssignmentsForHITResponseTypeDef = TypedDict(
    "ListAssignmentsForHITResponseTypeDef",
    {"NextToken": str, "NumResults": int, "Assignments": List["AssignmentTypeDef"]},
    total=False,
)

ListBonusPaymentsResponseTypeDef = TypedDict(
    "ListBonusPaymentsResponseTypeDef",
    {"NumResults": int, "NextToken": str, "BonusPayments": List["BonusPaymentTypeDef"]},
    total=False,
)

ListHITsForQualificationTypeResponseTypeDef = TypedDict(
    "ListHITsForQualificationTypeResponseTypeDef",
    {"NextToken": str, "NumResults": int, "HITs": List["HITTypeDef"]},
    total=False,
)

ListHITsResponseTypeDef = TypedDict(
    "ListHITsResponseTypeDef",
    {"NextToken": str, "NumResults": int, "HITs": List["HITTypeDef"]},
    total=False,
)

ListQualificationRequestsResponseTypeDef = TypedDict(
    "ListQualificationRequestsResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "QualificationRequests": List["QualificationRequestTypeDef"],
    },
    total=False,
)

ListQualificationTypesResponseTypeDef = TypedDict(
    "ListQualificationTypesResponseTypeDef",
    {"NumResults": int, "NextToken": str, "QualificationTypes": List["QualificationTypeTypeDef"]},
    total=False,
)

ListReviewPolicyResultsForHITResponseTypeDef = TypedDict(
    "ListReviewPolicyResultsForHITResponseTypeDef",
    {
        "HITId": str,
        "AssignmentReviewPolicy": "ReviewPolicyTypeDef",
        "HITReviewPolicy": "ReviewPolicyTypeDef",
        "AssignmentReviewReport": "ReviewReportTypeDef",
        "HITReviewReport": "ReviewReportTypeDef",
        "NextToken": str,
    },
    total=False,
)

ListReviewableHITsResponseTypeDef = TypedDict(
    "ListReviewableHITsResponseTypeDef",
    {"NextToken": str, "NumResults": int, "HITs": List["HITTypeDef"]},
    total=False,
)

ListWorkerBlocksResponseTypeDef = TypedDict(
    "ListWorkerBlocksResponseTypeDef",
    {"NextToken": str, "NumResults": int, "WorkerBlocks": List["WorkerBlockTypeDef"]},
    total=False,
)

ListWorkersWithQualificationTypeResponseTypeDef = TypedDict(
    "ListWorkersWithQualificationTypeResponseTypeDef",
    {"NextToken": str, "NumResults": int, "Qualifications": List["QualificationTypeDef"]},
    total=False,
)

NotificationSpecificationTypeDef = TypedDict(
    "NotificationSpecificationTypeDef",
    {
        "Destination": str,
        "Transport": Literal["Email", "SQS", "SNS"],
        "Version": str,
        "EventTypes": List[
            Literal[
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
            ]
        ],
    },
)

NotifyWorkersResponseTypeDef = TypedDict(
    "NotifyWorkersResponseTypeDef",
    {"NotifyWorkersFailureStatuses": List["NotifyWorkersFailureStatusTypeDef"]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UpdateQualificationTypeResponseTypeDef = TypedDict(
    "UpdateQualificationTypeResponseTypeDef",
    {"QualificationType": "QualificationTypeTypeDef"},
    total=False,
)
