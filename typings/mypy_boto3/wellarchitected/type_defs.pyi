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
    DefinitionTypeType,
    DifferenceStatusType,
    DiscoveryIntegrationStatusType,
    ImportLensStatusType,
    LensStatusType,
    LensStatusTypeType,
    LensTypeType,
    NotificationTypeType,
    OrganizationSharingStatusType,
    PermissionTypeType,
    ProfileNotificationTypeType,
    ProfileOwnerTypeType,
    QuestionPriorityType,
    QuestionType,
    QuestionTypeType,
    ReportFormatType,
    ReviewTemplateAnswerStatusType,
    ReviewTemplateUpdateStatusType,
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
    "AssociateProfilesInputRequestTypeDef",
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
    "CreateProfileInputRequestTypeDef",
    "CreateProfileOutputTypeDef",
    "CreateProfileShareInputRequestTypeDef",
    "CreateProfileShareOutputTypeDef",
    "CreateReviewTemplateInputRequestTypeDef",
    "CreateReviewTemplateOutputTypeDef",
    "CreateTemplateShareInputRequestTypeDef",
    "CreateTemplateShareOutputTypeDef",
    "CreateWorkloadInputRequestTypeDef",
    "CreateWorkloadOutputTypeDef",
    "CreateWorkloadShareInputRequestTypeDef",
    "CreateWorkloadShareOutputTypeDef",
    "DeleteLensInputRequestTypeDef",
    "DeleteLensShareInputRequestTypeDef",
    "DeleteProfileInputRequestTypeDef",
    "DeleteProfileShareInputRequestTypeDef",
    "DeleteReviewTemplateInputRequestTypeDef",
    "DeleteTemplateShareInputRequestTypeDef",
    "DeleteWorkloadInputRequestTypeDef",
    "DeleteWorkloadShareInputRequestTypeDef",
    "DisassociateLensesInputRequestTypeDef",
    "DisassociateProfilesInputRequestTypeDef",
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
    "GetProfileInputRequestTypeDef",
    "GetProfileOutputTypeDef",
    "GetProfileTemplateOutputTypeDef",
    "GetReviewTemplateAnswerInputRequestTypeDef",
    "GetReviewTemplateAnswerOutputTypeDef",
    "GetReviewTemplateInputRequestTypeDef",
    "GetReviewTemplateLensReviewInputRequestTypeDef",
    "GetReviewTemplateLensReviewOutputTypeDef",
    "GetReviewTemplateOutputTypeDef",
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
    "ListProfileNotificationsInputRequestTypeDef",
    "ListProfileNotificationsOutputTypeDef",
    "ListProfileSharesInputRequestTypeDef",
    "ListProfileSharesOutputTypeDef",
    "ListProfilesInputRequestTypeDef",
    "ListProfilesOutputTypeDef",
    "ListReviewTemplateAnswersInputRequestTypeDef",
    "ListReviewTemplateAnswersOutputTypeDef",
    "ListReviewTemplatesInputRequestTypeDef",
    "ListReviewTemplatesOutputTypeDef",
    "ListShareInvitationsInputRequestTypeDef",
    "ListShareInvitationsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListTemplateSharesInputRequestTypeDef",
    "ListTemplateSharesOutputTypeDef",
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
    "ProfileChoiceTypeDef",
    "ProfileNotificationSummaryTypeDef",
    "ProfileQuestionTypeDef",
    "ProfileQuestionUpdateTypeDef",
    "ProfileShareSummaryTypeDef",
    "ProfileSummaryTypeDef",
    "ProfileTemplateChoiceTypeDef",
    "ProfileTemplateQuestionTypeDef",
    "ProfileTemplateTypeDef",
    "ProfileTypeDef",
    "QuestionDifferenceTypeDef",
    "QuestionMetricTypeDef",
    "ResponseMetadataTypeDef",
    "ReviewTemplateAnswerSummaryTypeDef",
    "ReviewTemplateAnswerTypeDef",
    "ReviewTemplateLensReviewTypeDef",
    "ReviewTemplatePillarReviewSummaryTypeDef",
    "ReviewTemplateSummaryTypeDef",
    "ReviewTemplateTypeDef",
    "ShareInvitationSummaryTypeDef",
    "ShareInvitationTypeDef",
    "TagResourceInputRequestTypeDef",
    "TemplateShareSummaryTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateAnswerInputRequestTypeDef",
    "UpdateAnswerOutputTypeDef",
    "UpdateGlobalSettingsInputRequestTypeDef",
    "UpdateLensReviewInputRequestTypeDef",
    "UpdateLensReviewOutputTypeDef",
    "UpdateProfileInputRequestTypeDef",
    "UpdateProfileOutputTypeDef",
    "UpdateReviewTemplateAnswerInputRequestTypeDef",
    "UpdateReviewTemplateAnswerOutputTypeDef",
    "UpdateReviewTemplateInputRequestTypeDef",
    "UpdateReviewTemplateLensReviewInputRequestTypeDef",
    "UpdateReviewTemplateLensReviewOutputTypeDef",
    "UpdateReviewTemplateOutputTypeDef",
    "UpdateShareInvitationInputRequestTypeDef",
    "UpdateShareInvitationOutputTypeDef",
    "UpdateWorkloadInputRequestTypeDef",
    "UpdateWorkloadOutputTypeDef",
    "UpdateWorkloadShareInputRequestTypeDef",
    "UpdateWorkloadShareOutputTypeDef",
    "UpgradeLensReviewInputRequestTypeDef",
    "UpgradeProfileVersionInputRequestTypeDef",
    "UpgradeReviewTemplateLensReviewInputRequestTypeDef",
    "VersionDifferencesTypeDef",
    "WorkloadDiscoveryConfigTypeDef",
    "WorkloadProfileTypeDef",
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
        "QuestionType": QuestionTypeType,
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

AssociateProfilesInputRequestTypeDef = TypedDict(
    "AssociateProfilesInputRequestTypeDef",
    {
        "WorkloadId": str,
        "ProfileArns": List[str],
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

_RequiredCreateProfileInputRequestTypeDef = TypedDict(
    "_RequiredCreateProfileInputRequestTypeDef",
    {
        "ProfileName": str,
        "ProfileDescription": str,
        "ProfileQuestions": List["ProfileQuestionUpdateTypeDef"],
        "ClientRequestToken": str,
    },
)
_OptionalCreateProfileInputRequestTypeDef = TypedDict(
    "_OptionalCreateProfileInputRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateProfileInputRequestTypeDef(
    _RequiredCreateProfileInputRequestTypeDef, _OptionalCreateProfileInputRequestTypeDef
):
    pass

CreateProfileOutputTypeDef = TypedDict(
    "CreateProfileOutputTypeDef",
    {
        "ProfileArn": str,
        "ProfileVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProfileShareInputRequestTypeDef = TypedDict(
    "CreateProfileShareInputRequestTypeDef",
    {
        "ProfileArn": str,
        "SharedWith": str,
        "ClientRequestToken": str,
    },
)

CreateProfileShareOutputTypeDef = TypedDict(
    "CreateProfileShareOutputTypeDef",
    {
        "ShareId": str,
        "ProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReviewTemplateInputRequestTypeDef = TypedDict(
    "_RequiredCreateReviewTemplateInputRequestTypeDef",
    {
        "TemplateName": str,
        "Description": str,
        "Lenses": List[str],
        "ClientRequestToken": str,
    },
)
_OptionalCreateReviewTemplateInputRequestTypeDef = TypedDict(
    "_OptionalCreateReviewTemplateInputRequestTypeDef",
    {
        "Notes": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateReviewTemplateInputRequestTypeDef(
    _RequiredCreateReviewTemplateInputRequestTypeDef,
    _OptionalCreateReviewTemplateInputRequestTypeDef,
):
    pass

CreateReviewTemplateOutputTypeDef = TypedDict(
    "CreateReviewTemplateOutputTypeDef",
    {
        "TemplateArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTemplateShareInputRequestTypeDef = TypedDict(
    "CreateTemplateShareInputRequestTypeDef",
    {
        "TemplateArn": str,
        "SharedWith": str,
        "ClientRequestToken": str,
    },
)

CreateTemplateShareOutputTypeDef = TypedDict(
    "CreateTemplateShareOutputTypeDef",
    {
        "TemplateArn": str,
        "ShareId": str,
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
        "ProfileArns": List[str],
        "ReviewTemplateArns": List[str],
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

DeleteProfileInputRequestTypeDef = TypedDict(
    "DeleteProfileInputRequestTypeDef",
    {
        "ProfileArn": str,
        "ClientRequestToken": str,
    },
)

DeleteProfileShareInputRequestTypeDef = TypedDict(
    "DeleteProfileShareInputRequestTypeDef",
    {
        "ShareId": str,
        "ProfileArn": str,
        "ClientRequestToken": str,
    },
)

DeleteReviewTemplateInputRequestTypeDef = TypedDict(
    "DeleteReviewTemplateInputRequestTypeDef",
    {
        "TemplateArn": str,
        "ClientRequestToken": str,
    },
)

DeleteTemplateShareInputRequestTypeDef = TypedDict(
    "DeleteTemplateShareInputRequestTypeDef",
    {
        "ShareId": str,
        "TemplateArn": str,
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

DisassociateProfilesInputRequestTypeDef = TypedDict(
    "DisassociateProfilesInputRequestTypeDef",
    {
        "WorkloadId": str,
        "ProfileArns": List[str],
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

_RequiredGetProfileInputRequestTypeDef = TypedDict(
    "_RequiredGetProfileInputRequestTypeDef",
    {
        "ProfileArn": str,
    },
)
_OptionalGetProfileInputRequestTypeDef = TypedDict(
    "_OptionalGetProfileInputRequestTypeDef",
    {
        "ProfileVersion": str,
    },
    total=False,
)

class GetProfileInputRequestTypeDef(
    _RequiredGetProfileInputRequestTypeDef, _OptionalGetProfileInputRequestTypeDef
):
    pass

GetProfileOutputTypeDef = TypedDict(
    "GetProfileOutputTypeDef",
    {
        "Profile": "ProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProfileTemplateOutputTypeDef = TypedDict(
    "GetProfileTemplateOutputTypeDef",
    {
        "ProfileTemplate": "ProfileTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReviewTemplateAnswerInputRequestTypeDef = TypedDict(
    "GetReviewTemplateAnswerInputRequestTypeDef",
    {
        "TemplateArn": str,
        "LensAlias": str,
        "QuestionId": str,
    },
)

GetReviewTemplateAnswerOutputTypeDef = TypedDict(
    "GetReviewTemplateAnswerOutputTypeDef",
    {
        "TemplateArn": str,
        "LensAlias": str,
        "Answer": "ReviewTemplateAnswerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReviewTemplateInputRequestTypeDef = TypedDict(
    "GetReviewTemplateInputRequestTypeDef",
    {
        "TemplateArn": str,
    },
)

GetReviewTemplateLensReviewInputRequestTypeDef = TypedDict(
    "GetReviewTemplateLensReviewInputRequestTypeDef",
    {
        "TemplateArn": str,
        "LensAlias": str,
    },
)

GetReviewTemplateLensReviewOutputTypeDef = TypedDict(
    "GetReviewTemplateLensReviewOutputTypeDef",
    {
        "TemplateArn": str,
        "LensReview": "ReviewTemplateLensReviewTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReviewTemplateOutputTypeDef = TypedDict(
    "GetReviewTemplateOutputTypeDef",
    {
        "ReviewTemplate": "ReviewTemplateTypeDef",
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
        "Profiles": List["WorkloadProfileTypeDef"],
        "PrioritizedRiskCounts": Dict[RiskType, int],
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
        "Profiles": List["WorkloadProfileTypeDef"],
        "PrioritizedRiskCounts": Dict[RiskType, int],
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
        "ResourceArn": str,
        "ResourceName": str,
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
        "QuestionPriority": QuestionPriorityType,
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
        "QuestionPriority": QuestionPriorityType,
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
        "ResourceArn": str,
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

ListProfileNotificationsInputRequestTypeDef = TypedDict(
    "ListProfileNotificationsInputRequestTypeDef",
    {
        "WorkloadId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListProfileNotificationsOutputTypeDef = TypedDict(
    "ListProfileNotificationsOutputTypeDef",
    {
        "NotificationSummaries": List["ProfileNotificationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProfileSharesInputRequestTypeDef = TypedDict(
    "_RequiredListProfileSharesInputRequestTypeDef",
    {
        "ProfileArn": str,
    },
)
_OptionalListProfileSharesInputRequestTypeDef = TypedDict(
    "_OptionalListProfileSharesInputRequestTypeDef",
    {
        "SharedWithPrefix": str,
        "NextToken": str,
        "MaxResults": int,
        "Status": ShareStatusType,
    },
    total=False,
)

class ListProfileSharesInputRequestTypeDef(
    _RequiredListProfileSharesInputRequestTypeDef, _OptionalListProfileSharesInputRequestTypeDef
):
    pass

ListProfileSharesOutputTypeDef = TypedDict(
    "ListProfileSharesOutputTypeDef",
    {
        "ProfileShareSummaries": List["ProfileShareSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProfilesInputRequestTypeDef = TypedDict(
    "ListProfilesInputRequestTypeDef",
    {
        "ProfileNamePrefix": str,
        "ProfileOwnerType": ProfileOwnerTypeType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListProfilesOutputTypeDef = TypedDict(
    "ListProfilesOutputTypeDef",
    {
        "ProfileSummaries": List["ProfileSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListReviewTemplateAnswersInputRequestTypeDef = TypedDict(
    "_RequiredListReviewTemplateAnswersInputRequestTypeDef",
    {
        "TemplateArn": str,
        "LensAlias": str,
    },
)
_OptionalListReviewTemplateAnswersInputRequestTypeDef = TypedDict(
    "_OptionalListReviewTemplateAnswersInputRequestTypeDef",
    {
        "PillarId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListReviewTemplateAnswersInputRequestTypeDef(
    _RequiredListReviewTemplateAnswersInputRequestTypeDef,
    _OptionalListReviewTemplateAnswersInputRequestTypeDef,
):
    pass

ListReviewTemplateAnswersOutputTypeDef = TypedDict(
    "ListReviewTemplateAnswersOutputTypeDef",
    {
        "TemplateArn": str,
        "LensAlias": str,
        "AnswerSummaries": List["ReviewTemplateAnswerSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReviewTemplatesInputRequestTypeDef = TypedDict(
    "ListReviewTemplatesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListReviewTemplatesOutputTypeDef = TypedDict(
    "ListReviewTemplatesOutputTypeDef",
    {
        "ReviewTemplates": List["ReviewTemplateSummaryTypeDef"],
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
        "ProfileNamePrefix": str,
        "TemplateNamePrefix": str,
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

_RequiredListTemplateSharesInputRequestTypeDef = TypedDict(
    "_RequiredListTemplateSharesInputRequestTypeDef",
    {
        "TemplateArn": str,
    },
)
_OptionalListTemplateSharesInputRequestTypeDef = TypedDict(
    "_OptionalListTemplateSharesInputRequestTypeDef",
    {
        "SharedWithPrefix": str,
        "NextToken": str,
        "MaxResults": int,
        "Status": ShareStatusType,
    },
    total=False,
)

class ListTemplateSharesInputRequestTypeDef(
    _RequiredListTemplateSharesInputRequestTypeDef, _OptionalListTemplateSharesInputRequestTypeDef
):
    pass

ListTemplateSharesOutputTypeDef = TypedDict(
    "ListTemplateSharesOutputTypeDef",
    {
        "TemplateArn": str,
        "TemplateShareSummaries": List["TemplateShareSummaryTypeDef"],
        "NextToken": str,
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
        "PrioritizedRiskCounts": Dict[RiskType, int],
    },
    total=False,
)

ProfileChoiceTypeDef = TypedDict(
    "ProfileChoiceTypeDef",
    {
        "ChoiceId": str,
        "ChoiceTitle": str,
        "ChoiceDescription": str,
    },
    total=False,
)

ProfileNotificationSummaryTypeDef = TypedDict(
    "ProfileNotificationSummaryTypeDef",
    {
        "CurrentProfileVersion": str,
        "LatestProfileVersion": str,
        "Type": ProfileNotificationTypeType,
        "ProfileArn": str,
        "ProfileName": str,
        "WorkloadId": str,
        "WorkloadName": str,
    },
    total=False,
)

ProfileQuestionTypeDef = TypedDict(
    "ProfileQuestionTypeDef",
    {
        "QuestionId": str,
        "QuestionTitle": str,
        "QuestionDescription": str,
        "QuestionChoices": List["ProfileChoiceTypeDef"],
        "SelectedChoiceIds": List[str],
        "MinSelectedChoices": int,
        "MaxSelectedChoices": int,
    },
    total=False,
)

ProfileQuestionUpdateTypeDef = TypedDict(
    "ProfileQuestionUpdateTypeDef",
    {
        "QuestionId": str,
        "SelectedChoiceIds": List[str],
    },
    total=False,
)

ProfileShareSummaryTypeDef = TypedDict(
    "ProfileShareSummaryTypeDef",
    {
        "ShareId": str,
        "SharedWith": str,
        "Status": ShareStatusType,
        "StatusMessage": str,
    },
    total=False,
)

ProfileSummaryTypeDef = TypedDict(
    "ProfileSummaryTypeDef",
    {
        "ProfileArn": str,
        "ProfileVersion": str,
        "ProfileName": str,
        "ProfileDescription": str,
        "Owner": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

ProfileTemplateChoiceTypeDef = TypedDict(
    "ProfileTemplateChoiceTypeDef",
    {
        "ChoiceId": str,
        "ChoiceTitle": str,
        "ChoiceDescription": str,
    },
    total=False,
)

ProfileTemplateQuestionTypeDef = TypedDict(
    "ProfileTemplateQuestionTypeDef",
    {
        "QuestionId": str,
        "QuestionTitle": str,
        "QuestionDescription": str,
        "QuestionChoices": List["ProfileTemplateChoiceTypeDef"],
        "MinSelectedChoices": int,
        "MaxSelectedChoices": int,
    },
    total=False,
)

ProfileTemplateTypeDef = TypedDict(
    "ProfileTemplateTypeDef",
    {
        "TemplateName": str,
        "TemplateQuestions": List["ProfileTemplateQuestionTypeDef"],
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

ProfileTypeDef = TypedDict(
    "ProfileTypeDef",
    {
        "ProfileArn": str,
        "ProfileVersion": str,
        "ProfileName": str,
        "ProfileDescription": str,
        "ProfileQuestions": List["ProfileQuestionTypeDef"],
        "Owner": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "ShareInvitationId": str,
        "Tags": Dict[str, str],
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

ReviewTemplateAnswerSummaryTypeDef = TypedDict(
    "ReviewTemplateAnswerSummaryTypeDef",
    {
        "QuestionId": str,
        "PillarId": str,
        "QuestionTitle": str,
        "Choices": List["ChoiceTypeDef"],
        "SelectedChoices": List[str],
        "ChoiceAnswerSummaries": List["ChoiceAnswerSummaryTypeDef"],
        "IsApplicable": bool,
        "AnswerStatus": ReviewTemplateAnswerStatusType,
        "Reason": AnswerReasonType,
        "QuestionType": QuestionTypeType,
    },
    total=False,
)

ReviewTemplateAnswerTypeDef = TypedDict(
    "ReviewTemplateAnswerTypeDef",
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
        "AnswerStatus": ReviewTemplateAnswerStatusType,
        "Notes": str,
        "Reason": AnswerReasonType,
    },
    total=False,
)

ReviewTemplateLensReviewTypeDef = TypedDict(
    "ReviewTemplateLensReviewTypeDef",
    {
        "LensAlias": str,
        "LensArn": str,
        "LensVersion": str,
        "LensName": str,
        "LensStatus": LensStatusType,
        "PillarReviewSummaries": List["ReviewTemplatePillarReviewSummaryTypeDef"],
        "UpdatedAt": datetime,
        "Notes": str,
        "QuestionCounts": Dict[QuestionType, int],
        "NextToken": str,
    },
    total=False,
)

ReviewTemplatePillarReviewSummaryTypeDef = TypedDict(
    "ReviewTemplatePillarReviewSummaryTypeDef",
    {
        "PillarId": str,
        "PillarName": str,
        "Notes": str,
        "QuestionCounts": Dict[QuestionType, int],
    },
    total=False,
)

ReviewTemplateSummaryTypeDef = TypedDict(
    "ReviewTemplateSummaryTypeDef",
    {
        "Description": str,
        "Lenses": List[str],
        "Owner": str,
        "UpdatedAt": datetime,
        "TemplateArn": str,
        "TemplateName": str,
        "UpdateStatus": ReviewTemplateUpdateStatusType,
    },
    total=False,
)

ReviewTemplateTypeDef = TypedDict(
    "ReviewTemplateTypeDef",
    {
        "Description": str,
        "Lenses": List[str],
        "Notes": str,
        "QuestionCounts": Dict[QuestionType, int],
        "Owner": str,
        "UpdatedAt": datetime,
        "TemplateArn": str,
        "TemplateName": str,
        "Tags": Dict[str, str],
        "UpdateStatus": ReviewTemplateUpdateStatusType,
        "ShareInvitationId": str,
    },
    total=False,
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
        "ProfileName": str,
        "ProfileArn": str,
        "TemplateName": str,
        "TemplateArn": str,
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
        "ProfileArn": str,
        "TemplateArn": str,
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

TemplateShareSummaryTypeDef = TypedDict(
    "TemplateShareSummaryTypeDef",
    {
        "ShareId": str,
        "SharedWith": str,
        "Status": ShareStatusType,
        "StatusMessage": str,
    },
    total=False,
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
        "DiscoveryIntegrationStatus": DiscoveryIntegrationStatusType,
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

_RequiredUpdateProfileInputRequestTypeDef = TypedDict(
    "_RequiredUpdateProfileInputRequestTypeDef",
    {
        "ProfileArn": str,
    },
)
_OptionalUpdateProfileInputRequestTypeDef = TypedDict(
    "_OptionalUpdateProfileInputRequestTypeDef",
    {
        "ProfileDescription": str,
        "ProfileQuestions": List["ProfileQuestionUpdateTypeDef"],
    },
    total=False,
)

class UpdateProfileInputRequestTypeDef(
    _RequiredUpdateProfileInputRequestTypeDef, _OptionalUpdateProfileInputRequestTypeDef
):
    pass

UpdateProfileOutputTypeDef = TypedDict(
    "UpdateProfileOutputTypeDef",
    {
        "Profile": "ProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateReviewTemplateAnswerInputRequestTypeDef = TypedDict(
    "_RequiredUpdateReviewTemplateAnswerInputRequestTypeDef",
    {
        "TemplateArn": str,
        "LensAlias": str,
        "QuestionId": str,
    },
)
_OptionalUpdateReviewTemplateAnswerInputRequestTypeDef = TypedDict(
    "_OptionalUpdateReviewTemplateAnswerInputRequestTypeDef",
    {
        "SelectedChoices": List[str],
        "ChoiceUpdates": Dict[str, "ChoiceUpdateTypeDef"],
        "Notes": str,
        "IsApplicable": bool,
        "Reason": AnswerReasonType,
    },
    total=False,
)

class UpdateReviewTemplateAnswerInputRequestTypeDef(
    _RequiredUpdateReviewTemplateAnswerInputRequestTypeDef,
    _OptionalUpdateReviewTemplateAnswerInputRequestTypeDef,
):
    pass

UpdateReviewTemplateAnswerOutputTypeDef = TypedDict(
    "UpdateReviewTemplateAnswerOutputTypeDef",
    {
        "TemplateArn": str,
        "LensAlias": str,
        "Answer": "ReviewTemplateAnswerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateReviewTemplateInputRequestTypeDef = TypedDict(
    "_RequiredUpdateReviewTemplateInputRequestTypeDef",
    {
        "TemplateArn": str,
    },
)
_OptionalUpdateReviewTemplateInputRequestTypeDef = TypedDict(
    "_OptionalUpdateReviewTemplateInputRequestTypeDef",
    {
        "TemplateName": str,
        "Description": str,
        "Notes": str,
        "LensesToAssociate": List[str],
        "LensesToDisassociate": List[str],
    },
    total=False,
)

class UpdateReviewTemplateInputRequestTypeDef(
    _RequiredUpdateReviewTemplateInputRequestTypeDef,
    _OptionalUpdateReviewTemplateInputRequestTypeDef,
):
    pass

_RequiredUpdateReviewTemplateLensReviewInputRequestTypeDef = TypedDict(
    "_RequiredUpdateReviewTemplateLensReviewInputRequestTypeDef",
    {
        "TemplateArn": str,
        "LensAlias": str,
    },
)
_OptionalUpdateReviewTemplateLensReviewInputRequestTypeDef = TypedDict(
    "_OptionalUpdateReviewTemplateLensReviewInputRequestTypeDef",
    {
        "LensNotes": str,
        "PillarNotes": Dict[str, str],
    },
    total=False,
)

class UpdateReviewTemplateLensReviewInputRequestTypeDef(
    _RequiredUpdateReviewTemplateLensReviewInputRequestTypeDef,
    _OptionalUpdateReviewTemplateLensReviewInputRequestTypeDef,
):
    pass

UpdateReviewTemplateLensReviewOutputTypeDef = TypedDict(
    "UpdateReviewTemplateLensReviewOutputTypeDef",
    {
        "TemplateArn": str,
        "LensReview": "ReviewTemplateLensReviewTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateReviewTemplateOutputTypeDef = TypedDict(
    "UpdateReviewTemplateOutputTypeDef",
    {
        "ReviewTemplate": "ReviewTemplateTypeDef",
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

_RequiredUpgradeProfileVersionInputRequestTypeDef = TypedDict(
    "_RequiredUpgradeProfileVersionInputRequestTypeDef",
    {
        "WorkloadId": str,
        "ProfileArn": str,
    },
)
_OptionalUpgradeProfileVersionInputRequestTypeDef = TypedDict(
    "_OptionalUpgradeProfileVersionInputRequestTypeDef",
    {
        "MilestoneName": str,
        "ClientRequestToken": str,
    },
    total=False,
)

class UpgradeProfileVersionInputRequestTypeDef(
    _RequiredUpgradeProfileVersionInputRequestTypeDef,
    _OptionalUpgradeProfileVersionInputRequestTypeDef,
):
    pass

_RequiredUpgradeReviewTemplateLensReviewInputRequestTypeDef = TypedDict(
    "_RequiredUpgradeReviewTemplateLensReviewInputRequestTypeDef",
    {
        "TemplateArn": str,
        "LensAlias": str,
    },
)
_OptionalUpgradeReviewTemplateLensReviewInputRequestTypeDef = TypedDict(
    "_OptionalUpgradeReviewTemplateLensReviewInputRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class UpgradeReviewTemplateLensReviewInputRequestTypeDef(
    _RequiredUpgradeReviewTemplateLensReviewInputRequestTypeDef,
    _OptionalUpgradeReviewTemplateLensReviewInputRequestTypeDef,
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
        "WorkloadResourceDefinition": List[DefinitionTypeType],
    },
    total=False,
)

WorkloadProfileTypeDef = TypedDict(
    "WorkloadProfileTypeDef",
    {
        "ProfileArn": str,
        "ProfileVersion": str,
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
        "Profiles": List["WorkloadProfileTypeDef"],
        "PrioritizedRiskCounts": Dict[RiskType, int],
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
        "Profiles": List["WorkloadProfileTypeDef"],
        "PrioritizedRiskCounts": Dict[RiskType, int],
    },
    total=False,
)
