"""
Main interface for wellarchitected service type definitions.

Usage::

    ```python
    from mypy_boto3_wellarchitected.type_defs import AnswerSummaryTypeDef

    data: AnswerSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AnswerSummaryTypeDef",
    "AnswerTypeDef",
    "ChoiceTypeDef",
    "ImprovementSummaryTypeDef",
    "LensReviewReportTypeDef",
    "LensReviewSummaryTypeDef",
    "LensReviewTypeDef",
    "LensSummaryTypeDef",
    "LensUpgradeSummaryTypeDef",
    "MilestoneSummaryTypeDef",
    "MilestoneTypeDef",
    "NotificationSummaryTypeDef",
    "PillarDifferenceTypeDef",
    "PillarReviewSummaryTypeDef",
    "QuestionDifferenceTypeDef",
    "ResponseMetadata",
    "ShareInvitationSummaryTypeDef",
    "ShareInvitationTypeDef",
    "VersionDifferencesTypeDef",
    "WorkloadShareSummaryTypeDef",
    "WorkloadShareTypeDef",
    "WorkloadSummaryTypeDef",
    "WorkloadTypeDef",
    "CreateMilestoneOutputTypeDef",
    "CreateWorkloadOutputTypeDef",
    "CreateWorkloadShareOutputTypeDef",
    "GetAnswerOutputTypeDef",
    "GetLensReviewOutputTypeDef",
    "GetLensReviewReportOutputTypeDef",
    "GetLensVersionDifferenceOutputTypeDef",
    "GetMilestoneOutputTypeDef",
    "GetWorkloadOutputTypeDef",
    "ListAnswersOutputTypeDef",
    "ListLensReviewImprovementsOutputTypeDef",
    "ListLensReviewsOutputTypeDef",
    "ListLensesOutputTypeDef",
    "ListMilestonesOutputTypeDef",
    "ListNotificationsOutputTypeDef",
    "ListShareInvitationsOutputTypeDef",
    "ListWorkloadSharesOutputTypeDef",
    "ListWorkloadsOutputTypeDef",
    "UpdateAnswerOutputTypeDef",
    "UpdateLensReviewOutputTypeDef",
    "UpdateShareInvitationOutputTypeDef",
    "UpdateWorkloadOutputTypeDef",
    "UpdateWorkloadShareOutputTypeDef",
)

AnswerSummaryTypeDef = TypedDict(
    "AnswerSummaryTypeDef",
    {
        "QuestionId": str,
        "PillarId": str,
        "QuestionTitle": str,
        "Choices": List["ChoiceTypeDef"],
        "SelectedChoices": List[str],
        "IsApplicable": bool,
        "Risk": Literal["UNANSWERED", "HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE"],
    },
    total=False,
)

AnswerTypeDef = TypedDict(
    "AnswerTypeDef",
    {
        "QuestionId": str,
        "PillarId": str,
        "QuestionTitle": str,
        "QuestionDescription": str,
        "ImprovementPlanUrl": str,
        "HelpfulResourceUrl": str,
        "Choices": List["ChoiceTypeDef"],
        "SelectedChoices": List[str],
        "IsApplicable": bool,
        "Risk": Literal["UNANSWERED", "HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE"],
        "Notes": str,
    },
    total=False,
)

ChoiceTypeDef = TypedDict(
    "ChoiceTypeDef", {"ChoiceId": str, "Title": str, "Description": str}, total=False
)

ImprovementSummaryTypeDef = TypedDict(
    "ImprovementSummaryTypeDef",
    {
        "QuestionId": str,
        "PillarId": str,
        "QuestionTitle": str,
        "Risk": Literal["UNANSWERED", "HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE"],
        "ImprovementPlanUrl": str,
    },
    total=False,
)

LensReviewReportTypeDef = TypedDict(
    "LensReviewReportTypeDef", {"LensAlias": str, "Base64String": str}, total=False
)

LensReviewSummaryTypeDef = TypedDict(
    "LensReviewSummaryTypeDef",
    {
        "LensAlias": str,
        "LensVersion": str,
        "LensName": str,
        "LensStatus": Literal["CURRENT", "NOT_CURRENT", "DEPRECATED"],
        "UpdatedAt": datetime,
        "RiskCounts": Dict[Literal["UNANSWERED", "HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE"], int],
    },
    total=False,
)

LensReviewTypeDef = TypedDict(
    "LensReviewTypeDef",
    {
        "LensAlias": str,
        "LensVersion": str,
        "LensName": str,
        "LensStatus": Literal["CURRENT", "NOT_CURRENT", "DEPRECATED"],
        "PillarReviewSummaries": List["PillarReviewSummaryTypeDef"],
        "UpdatedAt": datetime,
        "Notes": str,
        "RiskCounts": Dict[Literal["UNANSWERED", "HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE"], int],
        "NextToken": str,
    },
    total=False,
)

LensSummaryTypeDef = TypedDict(
    "LensSummaryTypeDef",
    {"LensAlias": str, "LensVersion": str, "LensName": str, "Description": str},
    total=False,
)

LensUpgradeSummaryTypeDef = TypedDict(
    "LensUpgradeSummaryTypeDef",
    {
        "WorkloadId": str,
        "WorkloadName": str,
        "LensAlias": str,
        "CurrentLensVersion": str,
        "LatestLensVersion": str,
    },
    total=False,
)

MilestoneSummaryTypeDef = TypedDict(
    "MilestoneSummaryTypeDef",
    {
        "MilestoneNumber": int,
        "MilestoneName": str,
        "RecordedAt": datetime,
        "WorkloadSummary": "WorkloadSummaryTypeDef",
    },
    total=False,
)

MilestoneTypeDef = TypedDict(
    "MilestoneTypeDef",
    {
        "MilestoneNumber": int,
        "MilestoneName": str,
        "RecordedAt": datetime,
        "Workload": "WorkloadTypeDef",
    },
    total=False,
)

NotificationSummaryTypeDef = TypedDict(
    "NotificationSummaryTypeDef",
    {
        "Type": Literal["LENS_VERSION_UPGRADED", "LENS_VERSION_DEPRECATED"],
        "LensUpgradeSummary": "LensUpgradeSummaryTypeDef",
    },
    total=False,
)

PillarDifferenceTypeDef = TypedDict(
    "PillarDifferenceTypeDef",
    {
        "PillarId": str,
        "DifferenceStatus": Literal["UPDATED", "NEW", "DELETED"],
        "QuestionDifferences": List["QuestionDifferenceTypeDef"],
    },
    total=False,
)

PillarReviewSummaryTypeDef = TypedDict(
    "PillarReviewSummaryTypeDef",
    {
        "PillarId": str,
        "PillarName": str,
        "Notes": str,
        "RiskCounts": Dict[Literal["UNANSWERED", "HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE"], int],
    },
    total=False,
)

QuestionDifferenceTypeDef = TypedDict(
    "QuestionDifferenceTypeDef",
    {
        "QuestionId": str,
        "QuestionTitle": str,
        "DifferenceStatus": Literal["UPDATED", "NEW", "DELETED"],
    },
    total=False,
)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

ShareInvitationSummaryTypeDef = TypedDict(
    "ShareInvitationSummaryTypeDef",
    {
        "ShareInvitationId": str,
        "SharedBy": str,
        "SharedWith": str,
        "PermissionType": Literal["READONLY", "CONTRIBUTOR"],
        "WorkloadName": str,
        "WorkloadId": str,
    },
    total=False,
)

ShareInvitationTypeDef = TypedDict(
    "ShareInvitationTypeDef", {"ShareInvitationId": str, "WorkloadId": str}, total=False
)

VersionDifferencesTypeDef = TypedDict(
    "VersionDifferencesTypeDef", {"PillarDifferences": List["PillarDifferenceTypeDef"]}, total=False
)

WorkloadShareSummaryTypeDef = TypedDict(
    "WorkloadShareSummaryTypeDef",
    {
        "ShareId": str,
        "SharedWith": str,
        "PermissionType": Literal["READONLY", "CONTRIBUTOR"],
        "Status": Literal["ACCEPTED", "REJECTED", "PENDING", "REVOKED", "EXPIRED"],
    },
    total=False,
)

WorkloadShareTypeDef = TypedDict(
    "WorkloadShareTypeDef",
    {
        "ShareId": str,
        "SharedBy": str,
        "SharedWith": str,
        "PermissionType": Literal["READONLY", "CONTRIBUTOR"],
        "Status": Literal["ACCEPTED", "REJECTED", "PENDING", "REVOKED", "EXPIRED"],
        "WorkloadName": str,
        "WorkloadId": str,
    },
    total=False,
)

WorkloadSummaryTypeDef = TypedDict(
    "WorkloadSummaryTypeDef",
    {
        "WorkloadId": str,
        "WorkloadArn": str,
        "WorkloadName": str,
        "Owner": str,
        "UpdatedAt": datetime,
        "Lenses": List[str],
        "RiskCounts": Dict[Literal["UNANSWERED", "HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE"], int],
        "ImprovementStatus": Literal[
            "NOT_APPLICABLE", "NOT_STARTED", "IN_PROGRESS", "COMPLETE", "RISK_ACKNOWLEDGED"
        ],
    },
    total=False,
)

WorkloadTypeDef = TypedDict(
    "WorkloadTypeDef",
    {
        "WorkloadId": str,
        "WorkloadArn": str,
        "WorkloadName": str,
        "Description": str,
        "Environment": Literal["PRODUCTION", "PREPRODUCTION"],
        "UpdatedAt": datetime,
        "AccountIds": List[str],
        "AwsRegions": List[str],
        "NonAwsRegions": List[str],
        "ArchitecturalDesign": str,
        "ReviewOwner": str,
        "ReviewRestrictionDate": datetime,
        "IsReviewOwnerUpdateAcknowledged": bool,
        "IndustryType": str,
        "Industry": str,
        "Notes": str,
        "ImprovementStatus": Literal[
            "NOT_APPLICABLE", "NOT_STARTED", "IN_PROGRESS", "COMPLETE", "RISK_ACKNOWLEDGED"
        ],
        "RiskCounts": Dict[Literal["UNANSWERED", "HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE"], int],
        "PillarPriorities": List[str],
        "Lenses": List[str],
        "Owner": str,
        "ShareInvitationId": str,
    },
    total=False,
)

CreateMilestoneOutputTypeDef = TypedDict(
    "CreateMilestoneOutputTypeDef",
    {"WorkloadId": str, "MilestoneNumber": int, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateWorkloadOutputTypeDef = TypedDict(
    "CreateWorkloadOutputTypeDef",
    {"WorkloadId": str, "WorkloadArn": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateWorkloadShareOutputTypeDef = TypedDict(
    "CreateWorkloadShareOutputTypeDef",
    {"WorkloadId": str, "ShareId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetAnswerOutputTypeDef = TypedDict(
    "GetAnswerOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensAlias": str,
        "Answer": "AnswerTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetLensReviewOutputTypeDef = TypedDict(
    "GetLensReviewOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensReview": "LensReviewTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetLensReviewReportOutputTypeDef = TypedDict(
    "GetLensReviewReportOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensReviewReport": "LensReviewReportTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetLensVersionDifferenceOutputTypeDef = TypedDict(
    "GetLensVersionDifferenceOutputTypeDef",
    {
        "LensAlias": str,
        "BaseLensVersion": str,
        "LatestLensVersion": str,
        "VersionDifferences": "VersionDifferencesTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetMilestoneOutputTypeDef = TypedDict(
    "GetMilestoneOutputTypeDef",
    {"WorkloadId": str, "Milestone": "MilestoneTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetWorkloadOutputTypeDef = TypedDict(
    "GetWorkloadOutputTypeDef",
    {"Workload": "WorkloadTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListAnswersOutputTypeDef = TypedDict(
    "ListAnswersOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensAlias": str,
        "AnswerSummaries": List["AnswerSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListLensReviewImprovementsOutputTypeDef = TypedDict(
    "ListLensReviewImprovementsOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensAlias": str,
        "ImprovementSummaries": List["ImprovementSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListLensReviewsOutputTypeDef = TypedDict(
    "ListLensReviewsOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensReviewSummaries": List["LensReviewSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListLensesOutputTypeDef = TypedDict(
    "ListLensesOutputTypeDef",
    {
        "LensSummaries": List["LensSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListMilestonesOutputTypeDef = TypedDict(
    "ListMilestonesOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneSummaries": List["MilestoneSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListNotificationsOutputTypeDef = TypedDict(
    "ListNotificationsOutputTypeDef",
    {
        "NotificationSummaries": List["NotificationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListShareInvitationsOutputTypeDef = TypedDict(
    "ListShareInvitationsOutputTypeDef",
    {
        "ShareInvitationSummaries": List["ShareInvitationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListWorkloadSharesOutputTypeDef = TypedDict(
    "ListWorkloadSharesOutputTypeDef",
    {
        "WorkloadId": str,
        "WorkloadShareSummaries": List["WorkloadShareSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListWorkloadsOutputTypeDef = TypedDict(
    "ListWorkloadsOutputTypeDef",
    {
        "WorkloadSummaries": List["WorkloadSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

UpdateAnswerOutputTypeDef = TypedDict(
    "UpdateAnswerOutputTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "Answer": "AnswerTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

UpdateLensReviewOutputTypeDef = TypedDict(
    "UpdateLensReviewOutputTypeDef",
    {"WorkloadId": str, "LensReview": "LensReviewTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateShareInvitationOutputTypeDef = TypedDict(
    "UpdateShareInvitationOutputTypeDef",
    {"ShareInvitation": "ShareInvitationTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateWorkloadOutputTypeDef = TypedDict(
    "UpdateWorkloadOutputTypeDef",
    {"Workload": "WorkloadTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateWorkloadShareOutputTypeDef = TypedDict(
    "UpdateWorkloadShareOutputTypeDef",
    {
        "WorkloadId": str,
        "WorkloadShare": "WorkloadShareTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)
