"""
Type annotations for wellarchitected service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/type_defs.html)

Usage::

    ```python
    from mypy_boto3_wellarchitected.type_defs import AdditionalResourcesTypeDef

    data: AdditionalResourcesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AdditionalResourceTypeType,
    AnswerReasonType,
    CheckFailureReasonType,
    CheckStatusType,
    ChoiceReasonType,
    ChoiceStatusType,
    DifferenceStatusType,
    ImportLensStatusType,
    LensStatusType,
    LensStatusTypeType,
    LensTypeType,
    NotificationTypeType,
    OrganizationSharingStatusType,
    PermissionTypeType,
    ReportFormatType,
    RiskType,
    ShareInvitationActionType,
    ShareResourceTypeType,
    ShareStatusType,
    TrustedAdvisorIntegrationStatusType,
    WorkloadEnvironmentType,
    WorkloadImprovementStatusType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AdditionalResourcesTypeDef",
    "AnswerSummaryTypeDef",
    "AnswerTypeDef",
    "AssociateLensesInputRequestTypeDef",
    "BestPracticeTypeDef",
    "CheckDetailTypeDef",
    "CheckSummaryTypeDef",
    "ChoiceAnswerSummaryTypeDef",
    "ChoiceAnswerTypeDef",
    "ChoiceContentTypeDef",
    "ChoiceImprovementPlanTypeDef",
    "ChoiceTypeDef",
    "ChoiceUpdateTypeDef",
    "ConsolidatedReportMetricTypeDef",
    "CreateLensShareInputRequestTypeDef",
    "CreateLensShareOutputTypeDef",
    "CreateLensVersionInputRequestTypeDef",
    "CreateLensVersionOutputTypeDef",
    "CreateMilestoneInputRequestTypeDef",
    "CreateMilestoneOutputTypeDef",
    "CreateWorkloadInputRequestTypeDef",
    "CreateWorkloadOutputTypeDef",
    "CreateWorkloadShareInputRequestTypeDef",
    "CreateWorkloadShareOutputTypeDef",
    "DeleteLensInputRequestTypeDef",
    "DeleteLensShareInputRequestTypeDef",
    "DeleteWorkloadInputRequestTypeDef",
    "DeleteWorkloadShareInputRequestTypeDef",
    "DisassociateLensesInputRequestTypeDef",
    "ExportLensInputRequestTypeDef",
    "ExportLensOutputTypeDef",
    "GetAnswerInputRequestTypeDef",
    "GetAnswerOutputTypeDef",
    "GetConsolidatedReportInputRequestTypeDef",
    "GetConsolidatedReportOutputTypeDef",
    "GetLensInputRequestTypeDef",
    "GetLensOutputTypeDef",
    "GetLensReviewInputRequestTypeDef",
    "GetLensReviewOutputTypeDef",
    "GetLensReviewReportInputRequestTypeDef",
    "GetLensReviewReportOutputTypeDef",
    "GetLensVersionDifferenceInputRequestTypeDef",
    "GetLensVersionDifferenceOutputTypeDef",
    "GetMilestoneInputRequestTypeDef",
    "GetMilestoneOutputTypeDef",
    "GetWorkloadInputRequestTypeDef",
    "GetWorkloadOutputTypeDef",
    "ImportLensInputRequestTypeDef",
    "ImportLensOutputTypeDef",
    "ImprovementSummaryTypeDef",
    "LensMetricTypeDef",
    "LensReviewReportTypeDef",
    "LensReviewSummaryTypeDef",
    "LensReviewTypeDef",
    "LensShareSummaryTypeDef",
    "LensSummaryTypeDef",
    "LensTypeDef",
    "LensUpgradeSummaryTypeDef",
    "ListAnswersInputRequestTypeDef",
    "ListAnswersOutputTypeDef",
    "ListCheckDetailsInputRequestTypeDef",
    "ListCheckDetailsOutputTypeDef",
    "ListCheckSummariesInputRequestTypeDef",
    "ListCheckSummariesOutputTypeDef",
    "ListLensReviewImprovementsInputRequestTypeDef",
    "ListLensReviewImprovementsOutputTypeDef",
    "ListLensReviewsInputRequestTypeDef",
    "ListLensReviewsOutputTypeDef",
    "ListLensSharesInputRequestTypeDef",
    "ListLensSharesOutputTypeDef",
    "ListLensesInputRequestTypeDef",
    "ListLensesOutputTypeDef",
    "ListMilestonesInputRequestTypeDef",
    "ListMilestonesOutputTypeDef",
    "ListNotificationsInputRequestTypeDef",
    "ListNotificationsOutputTypeDef",
    "ListShareInvitationsInputRequestTypeDef",
    "ListShareInvitationsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListWorkloadSharesInputRequestTypeDef",
    "ListWorkloadSharesOutputTypeDef",
    "ListWorkloadsInputRequestTypeDef",
    "ListWorkloadsOutputTypeDef",
    "MilestoneSummaryTypeDef",
    "MilestoneTypeDef",
    "NotificationSummaryTypeDef",
    "PillarDifferenceTypeDef",
    "PillarMetricTypeDef",
    "PillarReviewSummaryTypeDef",
    "QuestionDifferenceTypeDef",
    "QuestionMetricTypeDef",
    "ResponseMetadataTypeDef",
    "ShareInvitationSummaryTypeDef",
    "ShareInvitationTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateAnswerInputRequestTypeDef",
    "UpdateAnswerOutputTypeDef",
    "UpdateGlobalSettingsInputRequestTypeDef",
    "UpdateLensReviewInputRequestTypeDef",
    "UpdateLensReviewOutputTypeDef",
    "UpdateShareInvitationInputRequestTypeDef",
    "UpdateShareInvitationOutputTypeDef",
    "UpdateWorkloadInputRequestTypeDef",
    "UpdateWorkloadOutputTypeDef",
    "UpdateWorkloadShareInputRequestTypeDef",
    "UpdateWorkloadShareOutputTypeDef",
    "UpgradeLensReviewInputRequestTypeDef",
    "VersionDifferencesTypeDef",
    "WorkloadDiscoveryConfigTypeDef",
    "WorkloadShareSummaryTypeDef",
    "WorkloadShareTypeDef",
    "WorkloadSummaryTypeDef",
    "WorkloadTypeDef",
)

AdditionalResourcesTypeDef = TypedDict(
    "AdditionalResourcesTypeDef",
    {
        "Type": AdditionalResourceTypeType,
        "Content": List["ChoiceContentTypeDef"],
    },
    total=False,
)

AnswerSummaryTypeDef = TypedDict(
    "AnswerSummaryTypeDef",
    {
        "QuestionId": str,
        "PillarId": str,
        "QuestionTitle": str,
        "Choices": List["ChoiceTypeDef"],
        "SelectedChoices": List[str],
        "ChoiceAnswerSummaries": List["ChoiceAnswerSummaryTypeDef"],
        "IsApplicable": bool,
        "Risk": RiskType,
        "Reason": AnswerReasonType,
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
        "HelpfulResourceDisplayText": str,
        "Choices": List["ChoiceTypeDef"],
        "SelectedChoices": List[str],
        "ChoiceAnswers": List["ChoiceAnswerTypeDef"],
        "IsApplicable": bool,
        "Risk": RiskType,
        "Notes": str,
        "Reason": AnswerReasonType,
    },
    total=False,
)

AssociateLensesInputRequestTypeDef = TypedDict(
    "AssociateLensesInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAliases": List[str],
    },
)

BestPracticeTypeDef = TypedDict(
    "BestPracticeTypeDef",
    {
        "ChoiceId": str,
        "ChoiceTitle": str,
    },
    total=False,
)

CheckDetailTypeDef = TypedDict(
    "CheckDetailTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Provider": Literal["TRUSTED_ADVISOR"],
        "LensArn": str,
        "PillarId": str,
        "QuestionId": str,
        "ChoiceId": str,
        "Status": CheckStatusType,
        "AccountId": str,
        "FlaggedResources": int,
        "Reason": CheckFailureReasonType,
        "UpdatedAt": datetime,
    },
    total=False,
)

CheckSummaryTypeDef = TypedDict(
    "CheckSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Provider": Literal["TRUSTED_ADVISOR"],
        "Description": str,
        "UpdatedAt": datetime,
        "LensArn": str,
        "PillarId": str,
        "QuestionId": str,
        "ChoiceId": str,
        "Status": CheckStatusType,
        "AccountSummary": Dict[CheckStatusType, int],
    },
    total=False,
)

ChoiceAnswerSummaryTypeDef = TypedDict(
    "ChoiceAnswerSummaryTypeDef",
    {
        "ChoiceId": str,
        "Status": ChoiceStatusType,
        "Reason": ChoiceReasonType,
    },
    total=False,
)

ChoiceAnswerTypeDef = TypedDict(
    "ChoiceAnswerTypeDef",
    {
        "ChoiceId": str,
        "Status": ChoiceStatusType,
        "Reason": ChoiceReasonType,
        "Notes": str,
    },
    total=False,
)

ChoiceContentTypeDef = TypedDict(
    "ChoiceContentTypeDef",
    {
        "DisplayText": str,
        "Url": str,
    },
    total=False,
)

ChoiceImprovementPlanTypeDef = TypedDict(
    "ChoiceImprovementPlanTypeDef",
    {
        "ChoiceId": str,
        "DisplayText": str,
        "ImprovementPlanUrl": str,
    },
    total=False,
)

ChoiceTypeDef = TypedDict(
    "ChoiceTypeDef",
    {
        "ChoiceId": str,
        "Title": str,
        "Description": str,
        "HelpfulResource": "ChoiceContentTypeDef",
        "ImprovementPlan": "ChoiceContentTypeDef",
        "AdditionalResources": List["AdditionalResourcesTypeDef"],
    },
    total=False,
)

_RequiredChoiceUpdateTypeDef = TypedDict(
    "_RequiredChoiceUpdateTypeDef",
    {
        "Status": ChoiceStatusType,
    },
)
_OptionalChoiceUpdateTypeDef = TypedDict(
    "_OptionalChoiceUpdateTypeDef",
    {
        "Reason": ChoiceReasonType,
        "Notes": str,
    },
    total=False,
)

class ChoiceUpdateTypeDef(_RequiredChoiceUpdateTypeDef, _OptionalChoiceUpdateTypeDef):
    pass

ConsolidatedReportMetricTypeDef = TypedDict(
    "ConsolidatedReportMetricTypeDef",
    {
        "MetricType": Literal["WORKLOAD"],
        "RiskCounts": Dict[RiskType, int],
        "WorkloadId": str,
        "WorkloadName": str,
        "WorkloadArn": str,
        "UpdatedAt": datetime,
        "Lenses": List["LensMetricTypeDef"],
        "LensesAppliedCount": int,
    },
    total=False,
)

CreateLensShareInputRequestTypeDef = TypedDict(
    "CreateLensShareInputRequestTypeDef",
    {
        "LensAlias": str,
        "SharedWith": str,
        "ClientRequestToken": str,
    },
)

CreateLensShareOutputTypeDef = TypedDict(
    "CreateLensShareOutputTypeDef",
    {
        "ShareId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLensVersionInputRequestTypeDef = TypedDict(
    "_RequiredCreateLensVersionInputRequestTypeDef",
    {
        "LensAlias": str,
        "LensVersion": str,
        "ClientRequestToken": str,
    },
)
_OptionalCreateLensVersionInputRequestTypeDef = TypedDict(
    "_OptionalCreateLensVersionInputRequestTypeDef",
    {
        "IsMajorVersion": bool,
    },
    total=False,
)

class CreateLensVersionInputRequestTypeDef(
    _RequiredCreateLensVersionInputRequestTypeDef, _OptionalCreateLensVersionInputRequestTypeDef
):
    pass

CreateLensVersionOutputTypeDef = TypedDict(
    "CreateLensVersionOutputTypeDef",
    {
        "LensArn": str,
        "LensVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMilestoneInputRequestTypeDef = TypedDict(
    "CreateMilestoneInputRequestTypeDef",
    {
        "WorkloadId": str,
        "MilestoneName": str,
        "ClientRequestToken": str,
    },
)

CreateMilestoneOutputTypeDef = TypedDict(
    "CreateMilestoneOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorkloadInputRequestTypeDef = TypedDict(
    "_RequiredCreateWorkloadInputRequestTypeDef",
    {
        "WorkloadName": str,
        "Description": str,
        "Environment": WorkloadEnvironmentType,
        "Lenses": List[str],
        "ClientRequestToken": str,
    },
)
_OptionalCreateWorkloadInputRequestTypeDef = TypedDict(
    "_OptionalCreateWorkloadInputRequestTypeDef",
    {
        "AccountIds": List[str],
        "AwsRegions": List[str],
        "NonAwsRegions": List[str],
        "PillarPriorities": List[str],
        "ArchitecturalDesign": str,
        "ReviewOwner": str,
        "IndustryType": str,
        "Industry": str,
        "Notes": str,
        "Tags": Dict[str, str],
        "DiscoveryConfig": "WorkloadDiscoveryConfigTypeDef",
        "Applications": List[str],
    },
    total=False,
)

class CreateWorkloadInputRequestTypeDef(
    _RequiredCreateWorkloadInputRequestTypeDef, _OptionalCreateWorkloadInputRequestTypeDef
):
    pass

CreateWorkloadOutputTypeDef = TypedDict(
    "CreateWorkloadOutputTypeDef",
    {
        "WorkloadId": str,
        "WorkloadArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorkloadShareInputRequestTypeDef = TypedDict(
    "CreateWorkloadShareInputRequestTypeDef",
    {
        "WorkloadId": str,
        "SharedWith": str,
        "PermissionType": PermissionTypeType,
        "ClientRequestToken": str,
    },
)

CreateWorkloadShareOutputTypeDef = TypedDict(
    "CreateWorkloadShareOutputTypeDef",
    {
        "WorkloadId": str,
        "ShareId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLensInputRequestTypeDef = TypedDict(
    "DeleteLensInputRequestTypeDef",
    {
        "LensAlias": str,
        "ClientRequestToken": str,
        "LensStatus": LensStatusTypeType,
    },
)

DeleteLensShareInputRequestTypeDef = TypedDict(
    "DeleteLensShareInputRequestTypeDef",
    {
        "ShareId": str,
        "LensAlias": str,
        "ClientRequestToken": str,
    },
)

DeleteWorkloadInputRequestTypeDef = TypedDict(
    "DeleteWorkloadInputRequestTypeDef",
    {
        "WorkloadId": str,
        "ClientRequestToken": str,
    },
)

DeleteWorkloadShareInputRequestTypeDef = TypedDict(
    "DeleteWorkloadShareInputRequestTypeDef",
    {
        "ShareId": str,
        "WorkloadId": str,
        "ClientRequestToken": str,
    },
)

DisassociateLensesInputRequestTypeDef = TypedDict(
    "DisassociateLensesInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAliases": List[str],
    },
)

_RequiredExportLensInputRequestTypeDef = TypedDict(
    "_RequiredExportLensInputRequestTypeDef",
    {
        "LensAlias": str,
    },
)
_OptionalExportLensInputRequestTypeDef = TypedDict(
    "_OptionalExportLensInputRequestTypeDef",
    {
        "LensVersion": str,
    },
    total=False,
)

class ExportLensInputRequestTypeDef(
    _RequiredExportLensInputRequestTypeDef, _OptionalExportLensInputRequestTypeDef
):
    pass

ExportLensOutputTypeDef = TypedDict(
    "ExportLensOutputTypeDef",
    {
        "LensJSON": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetAnswerInputRequestTypeDef = TypedDict(
    "_RequiredGetAnswerInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "QuestionId": str,
    },
)
_OptionalGetAnswerInputRequestTypeDef = TypedDict(
    "_OptionalGetAnswerInputRequestTypeDef",
    {
        "MilestoneNumber": int,
    },
    total=False,
)

class GetAnswerInputRequestTypeDef(
    _RequiredGetAnswerInputRequestTypeDef, _OptionalGetAnswerInputRequestTypeDef
):
    pass

GetAnswerOutputTypeDef = TypedDict(
    "GetAnswerOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensAlias": str,
        "LensArn": str,
        "Answer": "AnswerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetConsolidatedReportInputRequestTypeDef = TypedDict(
    "_RequiredGetConsolidatedReportInputRequestTypeDef",
    {
        "Format": ReportFormatType,
    },
)
_OptionalGetConsolidatedReportInputRequestTypeDef = TypedDict(
    "_OptionalGetConsolidatedReportInputRequestTypeDef",
    {
        "IncludeSharedResources": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetConsolidatedReportInputRequestTypeDef(
    _RequiredGetConsolidatedReportInputRequestTypeDef,
    _OptionalGetConsolidatedReportInputRequestTypeDef,
):
    pass

GetConsolidatedReportOutputTypeDef = TypedDict(
    "GetConsolidatedReportOutputTypeDef",
    {
        "Metrics": List["ConsolidatedReportMetricTypeDef"],
        "NextToken": str,
        "Base64String": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLensInputRequestTypeDef = TypedDict(
    "_RequiredGetLensInputRequestTypeDef",
    {
        "LensAlias": str,
    },
)
_OptionalGetLensInputRequestTypeDef = TypedDict(
    "_OptionalGetLensInputRequestTypeDef",
    {
        "LensVersion": str,
    },
    total=False,
)

class GetLensInputRequestTypeDef(
    _RequiredGetLensInputRequestTypeDef, _OptionalGetLensInputRequestTypeDef
):
    pass

GetLensOutputTypeDef = TypedDict(
    "GetLensOutputTypeDef",
    {
        "Lens": "LensTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLensReviewInputRequestTypeDef = TypedDict(
    "_RequiredGetLensReviewInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
    },
)
_OptionalGetLensReviewInputRequestTypeDef = TypedDict(
    "_OptionalGetLensReviewInputRequestTypeDef",
    {
        "MilestoneNumber": int,
    },
    total=False,
)

class GetLensReviewInputRequestTypeDef(
    _RequiredGetLensReviewInputRequestTypeDef, _OptionalGetLensReviewInputRequestTypeDef
):
    pass

GetLensReviewOutputTypeDef = TypedDict(
    "GetLensReviewOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensReview": "LensReviewTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLensReviewReportInputRequestTypeDef = TypedDict(
    "_RequiredGetLensReviewReportInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
    },
)
_OptionalGetLensReviewReportInputRequestTypeDef = TypedDict(
    "_OptionalGetLensReviewReportInputRequestTypeDef",
    {
        "MilestoneNumber": int,
    },
    total=False,
)

class GetLensReviewReportInputRequestTypeDef(
    _RequiredGetLensReviewReportInputRequestTypeDef, _OptionalGetLensReviewReportInputRequestTypeDef
):
    pass

GetLensReviewReportOutputTypeDef = TypedDict(
    "GetLensReviewReportOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensReviewReport": "LensReviewReportTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLensVersionDifferenceInputRequestTypeDef = TypedDict(
    "_RequiredGetLensVersionDifferenceInputRequestTypeDef",
    {
        "LensAlias": str,
    },
)
_OptionalGetLensVersionDifferenceInputRequestTypeDef = TypedDict(
    "_OptionalGetLensVersionDifferenceInputRequestTypeDef",
    {
        "BaseLensVersion": str,
        "TargetLensVersion": str,
    },
    total=False,
)

class GetLensVersionDifferenceInputRequestTypeDef(
    _RequiredGetLensVersionDifferenceInputRequestTypeDef,
    _OptionalGetLensVersionDifferenceInputRequestTypeDef,
):
    pass

GetLensVersionDifferenceOutputTypeDef = TypedDict(
    "GetLensVersionDifferenceOutputTypeDef",
    {
        "LensAlias": str,
        "LensArn": str,
        "BaseLensVersion": str,
        "TargetLensVersion": str,
        "LatestLensVersion": str,
        "VersionDifferences": "VersionDifferencesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMilestoneInputRequestTypeDef = TypedDict(
    "GetMilestoneInputRequestTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
    },
)

GetMilestoneOutputTypeDef = TypedDict(
    "GetMilestoneOutputTypeDef",
    {
        "WorkloadId": str,
        "Milestone": "MilestoneTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkloadInputRequestTypeDef = TypedDict(
    "GetWorkloadInputRequestTypeDef",
    {
        "WorkloadId": str,
    },
)

GetWorkloadOutputTypeDef = TypedDict(
    "GetWorkloadOutputTypeDef",
    {
        "Workload": "WorkloadTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImportLensInputRequestTypeDef = TypedDict(
    "_RequiredImportLensInputRequestTypeDef",
    {
        "JSONString": str,
        "ClientRequestToken": str,
    },
)
_OptionalImportLensInputRequestTypeDef = TypedDict(
    "_OptionalImportLensInputRequestTypeDef",
    {
        "LensAlias": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class ImportLensInputRequestTypeDef(
    _RequiredImportLensInputRequestTypeDef, _OptionalImportLensInputRequestTypeDef
):
    pass

ImportLensOutputTypeDef = TypedDict(
    "ImportLensOutputTypeDef",
    {
        "LensArn": str,
        "Status": ImportLensStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImprovementSummaryTypeDef = TypedDict(
    "ImprovementSummaryTypeDef",
    {
        "QuestionId": str,
        "PillarId": str,
        "QuestionTitle": str,
        "Risk": RiskType,
        "ImprovementPlanUrl": str,
        "ImprovementPlans": List["ChoiceImprovementPlanTypeDef"],
    },
    total=False,
)

LensMetricTypeDef = TypedDict(
    "LensMetricTypeDef",
    {
        "LensArn": str,
        "Pillars": List["PillarMetricTypeDef"],
        "RiskCounts": Dict[RiskType, int],
    },
    total=False,
)

LensReviewReportTypeDef = TypedDict(
    "LensReviewReportTypeDef",
    {
        "LensAlias": str,
        "LensArn": str,
        "Base64String": str,
    },
    total=False,
)

LensReviewSummaryTypeDef = TypedDict(
    "LensReviewSummaryTypeDef",
    {
        "LensAlias": str,
        "LensArn": str,
        "LensVersion": str,
        "LensName": str,
        "LensStatus": LensStatusType,
        "UpdatedAt": datetime,
        "RiskCounts": Dict[RiskType, int],
    },
    total=False,
)

LensReviewTypeDef = TypedDict(
    "LensReviewTypeDef",
    {
        "LensAlias": str,
        "LensArn": str,
        "LensVersion": str,
        "LensName": str,
        "LensStatus": LensStatusType,
        "PillarReviewSummaries": List["PillarReviewSummaryTypeDef"],
        "UpdatedAt": datetime,
        "Notes": str,
        "RiskCounts": Dict[RiskType, int],
        "NextToken": str,
    },
    total=False,
)

LensShareSummaryTypeDef = TypedDict(
    "LensShareSummaryTypeDef",
    {
        "ShareId": str,
        "SharedWith": str,
        "Status": ShareStatusType,
        "StatusMessage": str,
    },
    total=False,
)

LensSummaryTypeDef = TypedDict(
    "LensSummaryTypeDef",
    {
        "LensArn": str,
        "LensAlias": str,
        "LensName": str,
        "LensType": LensTypeType,
        "Description": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "LensVersion": str,
        "Owner": str,
        "LensStatus": LensStatusType,
    },
    total=False,
)

LensTypeDef = TypedDict(
    "LensTypeDef",
    {
        "LensArn": str,
        "LensVersion": str,
        "Name": str,
        "Description": str,
        "Owner": str,
        "ShareInvitationId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

LensUpgradeSummaryTypeDef = TypedDict(
    "LensUpgradeSummaryTypeDef",
    {
        "WorkloadId": str,
        "WorkloadName": str,
        "LensAlias": str,
        "LensArn": str,
        "CurrentLensVersion": str,
        "LatestLensVersion": str,
    },
    total=False,
)

_RequiredListAnswersInputRequestTypeDef = TypedDict(
    "_RequiredListAnswersInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
    },
)
_OptionalListAnswersInputRequestTypeDef = TypedDict(
    "_OptionalListAnswersInputRequestTypeDef",
    {
        "PillarId": str,
        "MilestoneNumber": int,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListAnswersInputRequestTypeDef(
    _RequiredListAnswersInputRequestTypeDef, _OptionalListAnswersInputRequestTypeDef
):
    pass

ListAnswersOutputTypeDef = TypedDict(
    "ListAnswersOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensAlias": str,
        "LensArn": str,
        "AnswerSummaries": List["AnswerSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCheckDetailsInputRequestTypeDef = TypedDict(
    "_RequiredListCheckDetailsInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensArn": str,
        "PillarId": str,
        "QuestionId": str,
        "ChoiceId": str,
    },
)
_OptionalListCheckDetailsInputRequestTypeDef = TypedDict(
    "_OptionalListCheckDetailsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListCheckDetailsInputRequestTypeDef(
    _RequiredListCheckDetailsInputRequestTypeDef, _OptionalListCheckDetailsInputRequestTypeDef
):
    pass

ListCheckDetailsOutputTypeDef = TypedDict(
    "ListCheckDetailsOutputTypeDef",
    {
        "CheckDetails": List["CheckDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCheckSummariesInputRequestTypeDef = TypedDict(
    "_RequiredListCheckSummariesInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensArn": str,
        "PillarId": str,
        "QuestionId": str,
        "ChoiceId": str,
    },
)
_OptionalListCheckSummariesInputRequestTypeDef = TypedDict(
    "_OptionalListCheckSummariesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListCheckSummariesInputRequestTypeDef(
    _RequiredListCheckSummariesInputRequestTypeDef, _OptionalListCheckSummariesInputRequestTypeDef
):
    pass

ListCheckSummariesOutputTypeDef = TypedDict(
    "ListCheckSummariesOutputTypeDef",
    {
        "CheckSummaries": List["CheckSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLensReviewImprovementsInputRequestTypeDef = TypedDict(
    "_RequiredListLensReviewImprovementsInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
    },
)
_OptionalListLensReviewImprovementsInputRequestTypeDef = TypedDict(
    "_OptionalListLensReviewImprovementsInputRequestTypeDef",
    {
        "PillarId": str,
        "MilestoneNumber": int,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListLensReviewImprovementsInputRequestTypeDef(
    _RequiredListLensReviewImprovementsInputRequestTypeDef,
    _OptionalListLensReviewImprovementsInputRequestTypeDef,
):
    pass

ListLensReviewImprovementsOutputTypeDef = TypedDict(
    "ListLensReviewImprovementsOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensAlias": str,
        "LensArn": str,
        "ImprovementSummaries": List["ImprovementSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLensReviewsInputRequestTypeDef = TypedDict(
    "_RequiredListLensReviewsInputRequestTypeDef",
    {
        "WorkloadId": str,
    },
)
_OptionalListLensReviewsInputRequestTypeDef = TypedDict(
    "_OptionalListLensReviewsInputRequestTypeDef",
    {
        "MilestoneNumber": int,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListLensReviewsInputRequestTypeDef(
    _RequiredListLensReviewsInputRequestTypeDef, _OptionalListLensReviewsInputRequestTypeDef
):
    pass

ListLensReviewsOutputTypeDef = TypedDict(
    "ListLensReviewsOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensReviewSummaries": List["LensReviewSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLensSharesInputRequestTypeDef = TypedDict(
    "_RequiredListLensSharesInputRequestTypeDef",
    {
        "LensAlias": str,
    },
)
_OptionalListLensSharesInputRequestTypeDef = TypedDict(
    "_OptionalListLensSharesInputRequestTypeDef",
    {
        "SharedWithPrefix": str,
        "NextToken": str,
        "MaxResults": int,
        "Status": ShareStatusType,
    },
    total=False,
)

class ListLensSharesInputRequestTypeDef(
    _RequiredListLensSharesInputRequestTypeDef, _OptionalListLensSharesInputRequestTypeDef
):
    pass

ListLensSharesOutputTypeDef = TypedDict(
    "ListLensSharesOutputTypeDef",
    {
        "LensShareSummaries": List["LensShareSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLensesInputRequestTypeDef = TypedDict(
    "ListLensesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "LensType": LensTypeType,
        "LensStatus": LensStatusTypeType,
        "LensName": str,
    },
    total=False,
)

ListLensesOutputTypeDef = TypedDict(
    "ListLensesOutputTypeDef",
    {
        "LensSummaries": List["LensSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMilestonesInputRequestTypeDef = TypedDict(
    "_RequiredListMilestonesInputRequestTypeDef",
    {
        "WorkloadId": str,
    },
)
_OptionalListMilestonesInputRequestTypeDef = TypedDict(
    "_OptionalListMilestonesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListMilestonesInputRequestTypeDef(
    _RequiredListMilestonesInputRequestTypeDef, _OptionalListMilestonesInputRequestTypeDef
):
    pass

ListMilestonesOutputTypeDef = TypedDict(
    "ListMilestonesOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneSummaries": List["MilestoneSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNotificationsInputRequestTypeDef = TypedDict(
    "ListNotificationsInputRequestTypeDef",
    {
        "WorkloadId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListNotificationsOutputTypeDef = TypedDict(
    "ListNotificationsOutputTypeDef",
    {
        "NotificationSummaries": List["NotificationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListShareInvitationsInputRequestTypeDef = TypedDict(
    "ListShareInvitationsInputRequestTypeDef",
    {
        "WorkloadNamePrefix": str,
        "LensNamePrefix": str,
        "ShareResourceType": ShareResourceTypeType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListShareInvitationsOutputTypeDef = TypedDict(
    "ListShareInvitationsOutputTypeDef",
    {
        "ShareInvitationSummaries": List["ShareInvitationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "WorkloadArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWorkloadSharesInputRequestTypeDef = TypedDict(
    "_RequiredListWorkloadSharesInputRequestTypeDef",
    {
        "WorkloadId": str,
    },
)
_OptionalListWorkloadSharesInputRequestTypeDef = TypedDict(
    "_OptionalListWorkloadSharesInputRequestTypeDef",
    {
        "SharedWithPrefix": str,
        "NextToken": str,
        "MaxResults": int,
        "Status": ShareStatusType,
    },
    total=False,
)

class ListWorkloadSharesInputRequestTypeDef(
    _RequiredListWorkloadSharesInputRequestTypeDef, _OptionalListWorkloadSharesInputRequestTypeDef
):
    pass

ListWorkloadSharesOutputTypeDef = TypedDict(
    "ListWorkloadSharesOutputTypeDef",
    {
        "WorkloadId": str,
        "WorkloadShareSummaries": List["WorkloadShareSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkloadsInputRequestTypeDef = TypedDict(
    "ListWorkloadsInputRequestTypeDef",
    {
        "WorkloadNamePrefix": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListWorkloadsOutputTypeDef = TypedDict(
    "ListWorkloadsOutputTypeDef",
    {
        "WorkloadSummaries": List["WorkloadSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "Type": NotificationTypeType,
        "LensUpgradeSummary": "LensUpgradeSummaryTypeDef",
    },
    total=False,
)

PillarDifferenceTypeDef = TypedDict(
    "PillarDifferenceTypeDef",
    {
        "PillarId": str,
        "PillarName": str,
        "DifferenceStatus": DifferenceStatusType,
        "QuestionDifferences": List["QuestionDifferenceTypeDef"],
    },
    total=False,
)

PillarMetricTypeDef = TypedDict(
    "PillarMetricTypeDef",
    {
        "PillarId": str,
        "RiskCounts": Dict[RiskType, int],
        "Questions": List["QuestionMetricTypeDef"],
    },
    total=False,
)

PillarReviewSummaryTypeDef = TypedDict(
    "PillarReviewSummaryTypeDef",
    {
        "PillarId": str,
        "PillarName": str,
        "Notes": str,
        "RiskCounts": Dict[RiskType, int],
    },
    total=False,
)

QuestionDifferenceTypeDef = TypedDict(
    "QuestionDifferenceTypeDef",
    {
        "QuestionId": str,
        "QuestionTitle": str,
        "DifferenceStatus": DifferenceStatusType,
    },
    total=False,
)

QuestionMetricTypeDef = TypedDict(
    "QuestionMetricTypeDef",
    {
        "QuestionId": str,
        "Risk": RiskType,
        "BestPractices": List["BestPracticeTypeDef"],
    },
    total=False,
)

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

ShareInvitationSummaryTypeDef = TypedDict(
    "ShareInvitationSummaryTypeDef",
    {
        "ShareInvitationId": str,
        "SharedBy": str,
        "SharedWith": str,
        "PermissionType": PermissionTypeType,
        "ShareResourceType": ShareResourceTypeType,
        "WorkloadName": str,
        "WorkloadId": str,
        "LensName": str,
        "LensArn": str,
    },
    total=False,
)

ShareInvitationTypeDef = TypedDict(
    "ShareInvitationTypeDef",
    {
        "ShareInvitationId": str,
        "ShareResourceType": ShareResourceTypeType,
        "WorkloadId": str,
        "LensAlias": str,
        "LensArn": str,
    },
    total=False,
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "WorkloadArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "WorkloadArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAnswerInputRequestTypeDef = TypedDict(
    "_RequiredUpdateAnswerInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "QuestionId": str,
    },
)
_OptionalUpdateAnswerInputRequestTypeDef = TypedDict(
    "_OptionalUpdateAnswerInputRequestTypeDef",
    {
        "SelectedChoices": List[str],
        "ChoiceUpdates": Dict[str, "ChoiceUpdateTypeDef"],
        "Notes": str,
        "IsApplicable": bool,
        "Reason": AnswerReasonType,
    },
    total=False,
)

class UpdateAnswerInputRequestTypeDef(
    _RequiredUpdateAnswerInputRequestTypeDef, _OptionalUpdateAnswerInputRequestTypeDef
):
    pass

UpdateAnswerOutputTypeDef = TypedDict(
    "UpdateAnswerOutputTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "LensArn": str,
        "Answer": "AnswerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGlobalSettingsInputRequestTypeDef = TypedDict(
    "UpdateGlobalSettingsInputRequestTypeDef",
    {
        "OrganizationSharingStatus": OrganizationSharingStatusType,
    },
    total=False,
)

_RequiredUpdateLensReviewInputRequestTypeDef = TypedDict(
    "_RequiredUpdateLensReviewInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
    },
)
_OptionalUpdateLensReviewInputRequestTypeDef = TypedDict(
    "_OptionalUpdateLensReviewInputRequestTypeDef",
    {
        "LensNotes": str,
        "PillarNotes": Dict[str, str],
    },
    total=False,
)

class UpdateLensReviewInputRequestTypeDef(
    _RequiredUpdateLensReviewInputRequestTypeDef, _OptionalUpdateLensReviewInputRequestTypeDef
):
    pass

UpdateLensReviewOutputTypeDef = TypedDict(
    "UpdateLensReviewOutputTypeDef",
    {
        "WorkloadId": str,
        "LensReview": "LensReviewTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateShareInvitationInputRequestTypeDef = TypedDict(
    "UpdateShareInvitationInputRequestTypeDef",
    {
        "ShareInvitationId": str,
        "ShareInvitationAction": ShareInvitationActionType,
    },
)

UpdateShareInvitationOutputTypeDef = TypedDict(
    "UpdateShareInvitationOutputTypeDef",
    {
        "ShareInvitation": "ShareInvitationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWorkloadInputRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkloadInputRequestTypeDef",
    {
        "WorkloadId": str,
    },
)
_OptionalUpdateWorkloadInputRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkloadInputRequestTypeDef",
    {
        "WorkloadName": str,
        "Description": str,
        "Environment": WorkloadEnvironmentType,
        "AccountIds": List[str],
        "AwsRegions": List[str],
        "NonAwsRegions": List[str],
        "PillarPriorities": List[str],
        "ArchitecturalDesign": str,
        "ReviewOwner": str,
        "IsReviewOwnerUpdateAcknowledged": bool,
        "IndustryType": str,
        "Industry": str,
        "Notes": str,
        "ImprovementStatus": WorkloadImprovementStatusType,
        "DiscoveryConfig": "WorkloadDiscoveryConfigTypeDef",
        "Applications": List[str],
    },
    total=False,
)

class UpdateWorkloadInputRequestTypeDef(
    _RequiredUpdateWorkloadInputRequestTypeDef, _OptionalUpdateWorkloadInputRequestTypeDef
):
    pass

UpdateWorkloadOutputTypeDef = TypedDict(
    "UpdateWorkloadOutputTypeDef",
    {
        "Workload": "WorkloadTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateWorkloadShareInputRequestTypeDef = TypedDict(
    "UpdateWorkloadShareInputRequestTypeDef",
    {
        "ShareId": str,
        "WorkloadId": str,
        "PermissionType": PermissionTypeType,
    },
)

UpdateWorkloadShareOutputTypeDef = TypedDict(
    "UpdateWorkloadShareOutputTypeDef",
    {
        "WorkloadId": str,
        "WorkloadShare": "WorkloadShareTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpgradeLensReviewInputRequestTypeDef = TypedDict(
    "_RequiredUpgradeLensReviewInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "MilestoneName": str,
    },
)
_OptionalUpgradeLensReviewInputRequestTypeDef = TypedDict(
    "_OptionalUpgradeLensReviewInputRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class UpgradeLensReviewInputRequestTypeDef(
    _RequiredUpgradeLensReviewInputRequestTypeDef, _OptionalUpgradeLensReviewInputRequestTypeDef
):
    pass

VersionDifferencesTypeDef = TypedDict(
    "VersionDifferencesTypeDef",
    {
        "PillarDifferences": List["PillarDifferenceTypeDef"],
    },
    total=False,
)

WorkloadDiscoveryConfigTypeDef = TypedDict(
    "WorkloadDiscoveryConfigTypeDef",
    {
        "TrustedAdvisorIntegrationStatus": TrustedAdvisorIntegrationStatusType,
    },
    total=False,
)

WorkloadShareSummaryTypeDef = TypedDict(
    "WorkloadShareSummaryTypeDef",
    {
        "ShareId": str,
        "SharedWith": str,
        "PermissionType": PermissionTypeType,
        "Status": ShareStatusType,
        "StatusMessage": str,
    },
    total=False,
)

WorkloadShareTypeDef = TypedDict(
    "WorkloadShareTypeDef",
    {
        "ShareId": str,
        "SharedBy": str,
        "SharedWith": str,
        "PermissionType": PermissionTypeType,
        "Status": ShareStatusType,
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
        "RiskCounts": Dict[RiskType, int],
        "ImprovementStatus": WorkloadImprovementStatusType,
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
        "Environment": WorkloadEnvironmentType,
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
        "ImprovementStatus": WorkloadImprovementStatusType,
        "RiskCounts": Dict[RiskType, int],
        "PillarPriorities": List[str],
        "Lenses": List[str],
        "Owner": str,
        "ShareInvitationId": str,
        "Tags": Dict[str, str],
        "DiscoveryConfig": "WorkloadDiscoveryConfigTypeDef",
        "Applications": List[str],
    },
    total=False,
)
