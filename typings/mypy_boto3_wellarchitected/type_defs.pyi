"""
Type annotations for wellarchitected service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_wellarchitected.type_defs import AccountJiraConfigurationInputTypeDef

    data: AccountJiraConfigurationInputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AccountJiraIssueManagementStatusType,
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
    IntegrationStatusType,
    IssueManagementTypeType,
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
    WorkloadIssueManagementStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccountJiraConfigurationInputTypeDef",
    "AccountJiraConfigurationOutputTypeDef",
    "AdditionalResourcesTypeDef",
    "AnswerSummaryTypeDef",
    "AnswerTypeDef",
    "AssociateLensesInputTypeDef",
    "AssociateProfilesInputTypeDef",
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
    "CreateLensShareInputTypeDef",
    "CreateLensShareOutputTypeDef",
    "CreateLensVersionInputTypeDef",
    "CreateLensVersionOutputTypeDef",
    "CreateMilestoneInputTypeDef",
    "CreateMilestoneOutputTypeDef",
    "CreateProfileInputTypeDef",
    "CreateProfileOutputTypeDef",
    "CreateProfileShareInputTypeDef",
    "CreateProfileShareOutputTypeDef",
    "CreateReviewTemplateInputTypeDef",
    "CreateReviewTemplateOutputTypeDef",
    "CreateTemplateShareInputTypeDef",
    "CreateTemplateShareOutputTypeDef",
    "CreateWorkloadInputTypeDef",
    "CreateWorkloadOutputTypeDef",
    "CreateWorkloadShareInputTypeDef",
    "CreateWorkloadShareOutputTypeDef",
    "DeleteLensInputTypeDef",
    "DeleteLensShareInputTypeDef",
    "DeleteProfileInputTypeDef",
    "DeleteProfileShareInputTypeDef",
    "DeleteReviewTemplateInputTypeDef",
    "DeleteTemplateShareInputTypeDef",
    "DeleteWorkloadInputTypeDef",
    "DeleteWorkloadShareInputTypeDef",
    "DisassociateLensesInputTypeDef",
    "DisassociateProfilesInputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExportLensInputTypeDef",
    "ExportLensOutputTypeDef",
    "GetAnswerInputTypeDef",
    "GetAnswerOutputTypeDef",
    "GetConsolidatedReportInputTypeDef",
    "GetConsolidatedReportOutputTypeDef",
    "GetGlobalSettingsOutputTypeDef",
    "GetLensInputTypeDef",
    "GetLensOutputTypeDef",
    "GetLensReviewInputTypeDef",
    "GetLensReviewOutputTypeDef",
    "GetLensReviewReportInputTypeDef",
    "GetLensReviewReportOutputTypeDef",
    "GetLensVersionDifferenceInputTypeDef",
    "GetLensVersionDifferenceOutputTypeDef",
    "GetMilestoneInputTypeDef",
    "GetMilestoneOutputTypeDef",
    "GetProfileInputTypeDef",
    "GetProfileOutputTypeDef",
    "GetProfileTemplateOutputTypeDef",
    "GetReviewTemplateAnswerInputTypeDef",
    "GetReviewTemplateAnswerOutputTypeDef",
    "GetReviewTemplateInputTypeDef",
    "GetReviewTemplateLensReviewInputTypeDef",
    "GetReviewTemplateLensReviewOutputTypeDef",
    "GetReviewTemplateOutputTypeDef",
    "GetWorkloadInputTypeDef",
    "GetWorkloadOutputTypeDef",
    "ImportLensInputTypeDef",
    "ImportLensOutputTypeDef",
    "ImprovementSummaryTypeDef",
    "JiraConfigurationTypeDef",
    "JiraSelectedQuestionConfigurationOutputTypeDef",
    "JiraSelectedQuestionConfigurationTypeDef",
    "JiraSelectedQuestionConfigurationUnionTypeDef",
    "LensMetricTypeDef",
    "LensReviewReportTypeDef",
    "LensReviewSummaryTypeDef",
    "LensReviewTypeDef",
    "LensShareSummaryTypeDef",
    "LensSummaryTypeDef",
    "LensTypeDef",
    "LensUpgradeSummaryTypeDef",
    "ListAnswersInputTypeDef",
    "ListAnswersOutputTypeDef",
    "ListCheckDetailsInputTypeDef",
    "ListCheckDetailsOutputTypeDef",
    "ListCheckSummariesInputTypeDef",
    "ListCheckSummariesOutputTypeDef",
    "ListLensReviewImprovementsInputTypeDef",
    "ListLensReviewImprovementsOutputTypeDef",
    "ListLensReviewsInputTypeDef",
    "ListLensReviewsOutputTypeDef",
    "ListLensSharesInputTypeDef",
    "ListLensSharesOutputTypeDef",
    "ListLensesInputTypeDef",
    "ListLensesOutputTypeDef",
    "ListMilestonesInputTypeDef",
    "ListMilestonesOutputTypeDef",
    "ListNotificationsInputTypeDef",
    "ListNotificationsOutputTypeDef",
    "ListProfileNotificationsInputTypeDef",
    "ListProfileNotificationsOutputTypeDef",
    "ListProfileSharesInputTypeDef",
    "ListProfileSharesOutputTypeDef",
    "ListProfilesInputTypeDef",
    "ListProfilesOutputTypeDef",
    "ListReviewTemplateAnswersInputTypeDef",
    "ListReviewTemplateAnswersOutputTypeDef",
    "ListReviewTemplatesInputTypeDef",
    "ListReviewTemplatesOutputTypeDef",
    "ListShareInvitationsInputTypeDef",
    "ListShareInvitationsOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListTemplateSharesInputTypeDef",
    "ListTemplateSharesOutputTypeDef",
    "ListWorkloadSharesInputTypeDef",
    "ListWorkloadSharesOutputTypeDef",
    "ListWorkloadsInputTypeDef",
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
    "SelectedPillarOutputTypeDef",
    "SelectedPillarTypeDef",
    "ShareInvitationSummaryTypeDef",
    "ShareInvitationTypeDef",
    "TagResourceInputTypeDef",
    "TemplateShareSummaryTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateAnswerInputTypeDef",
    "UpdateAnswerOutputTypeDef",
    "UpdateGlobalSettingsInputTypeDef",
    "UpdateIntegrationInputTypeDef",
    "UpdateLensReviewInputTypeDef",
    "UpdateLensReviewOutputTypeDef",
    "UpdateProfileInputTypeDef",
    "UpdateProfileOutputTypeDef",
    "UpdateReviewTemplateAnswerInputTypeDef",
    "UpdateReviewTemplateAnswerOutputTypeDef",
    "UpdateReviewTemplateInputTypeDef",
    "UpdateReviewTemplateLensReviewInputTypeDef",
    "UpdateReviewTemplateLensReviewOutputTypeDef",
    "UpdateReviewTemplateOutputTypeDef",
    "UpdateShareInvitationInputTypeDef",
    "UpdateShareInvitationOutputTypeDef",
    "UpdateWorkloadInputTypeDef",
    "UpdateWorkloadOutputTypeDef",
    "UpdateWorkloadShareInputTypeDef",
    "UpdateWorkloadShareOutputTypeDef",
    "UpgradeLensReviewInputTypeDef",
    "UpgradeProfileVersionInputTypeDef",
    "UpgradeReviewTemplateLensReviewInputTypeDef",
    "VersionDifferencesTypeDef",
    "WorkloadDiscoveryConfigOutputTypeDef",
    "WorkloadDiscoveryConfigTypeDef",
    "WorkloadDiscoveryConfigUnionTypeDef",
    "WorkloadJiraConfigurationInputTypeDef",
    "WorkloadJiraConfigurationOutputTypeDef",
    "WorkloadProfileTypeDef",
    "WorkloadShareSummaryTypeDef",
    "WorkloadShareTypeDef",
    "WorkloadSummaryTypeDef",
    "WorkloadTypeDef",
)

class AccountJiraConfigurationInputTypeDef(TypedDict):
    IssueManagementStatus: NotRequired[AccountJiraIssueManagementStatusType]
    IssueManagementType: NotRequired[IssueManagementTypeType]
    JiraProjectKey: NotRequired[str]
    IntegrationStatus: NotRequired[Literal["NOT_CONFIGURED"]]

class AccountJiraConfigurationOutputTypeDef(TypedDict):
    IntegrationStatus: NotRequired[IntegrationStatusType]
    IssueManagementStatus: NotRequired[AccountJiraIssueManagementStatusType]
    IssueManagementType: NotRequired[IssueManagementTypeType]
    Subdomain: NotRequired[str]
    JiraProjectKey: NotRequired[str]
    StatusMessage: NotRequired[str]

class ChoiceContentTypeDef(TypedDict):
    DisplayText: NotRequired[str]
    Url: NotRequired[str]

class ChoiceAnswerSummaryTypeDef(TypedDict):
    ChoiceId: NotRequired[str]
    Status: NotRequired[ChoiceStatusType]
    Reason: NotRequired[ChoiceReasonType]

class JiraConfigurationTypeDef(TypedDict):
    JiraIssueUrl: NotRequired[str]
    LastSyncedTime: NotRequired[datetime]

class ChoiceAnswerTypeDef(TypedDict):
    ChoiceId: NotRequired[str]
    Status: NotRequired[ChoiceStatusType]
    Reason: NotRequired[ChoiceReasonType]
    Notes: NotRequired[str]

class AssociateLensesInputTypeDef(TypedDict):
    WorkloadId: str
    LensAliases: Sequence[str]

class AssociateProfilesInputTypeDef(TypedDict):
    WorkloadId: str
    ProfileArns: Sequence[str]

class BestPracticeTypeDef(TypedDict):
    ChoiceId: NotRequired[str]
    ChoiceTitle: NotRequired[str]

class CheckDetailTypeDef(TypedDict):
    Id: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    Provider: NotRequired[Literal["TRUSTED_ADVISOR"]]
    LensArn: NotRequired[str]
    PillarId: NotRequired[str]
    QuestionId: NotRequired[str]
    ChoiceId: NotRequired[str]
    Status: NotRequired[CheckStatusType]
    AccountId: NotRequired[str]
    FlaggedResources: NotRequired[int]
    Reason: NotRequired[CheckFailureReasonType]
    UpdatedAt: NotRequired[datetime]

class CheckSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Name: NotRequired[str]
    Provider: NotRequired[Literal["TRUSTED_ADVISOR"]]
    Description: NotRequired[str]
    UpdatedAt: NotRequired[datetime]
    LensArn: NotRequired[str]
    PillarId: NotRequired[str]
    QuestionId: NotRequired[str]
    ChoiceId: NotRequired[str]
    Status: NotRequired[CheckStatusType]
    AccountSummary: NotRequired[Dict[CheckStatusType, int]]

class ChoiceImprovementPlanTypeDef(TypedDict):
    ChoiceId: NotRequired[str]
    DisplayText: NotRequired[str]
    ImprovementPlanUrl: NotRequired[str]

class ChoiceUpdateTypeDef(TypedDict):
    Status: ChoiceStatusType
    Reason: NotRequired[ChoiceReasonType]
    Notes: NotRequired[str]

class CreateLensShareInputTypeDef(TypedDict):
    LensAlias: str
    SharedWith: str
    ClientRequestToken: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateLensVersionInputTypeDef(TypedDict):
    LensAlias: str
    LensVersion: str
    ClientRequestToken: str
    IsMajorVersion: NotRequired[bool]

class CreateMilestoneInputTypeDef(TypedDict):
    WorkloadId: str
    MilestoneName: str
    ClientRequestToken: str

class ProfileQuestionUpdateTypeDef(TypedDict):
    QuestionId: NotRequired[str]
    SelectedChoiceIds: NotRequired[Sequence[str]]

class CreateProfileShareInputTypeDef(TypedDict):
    ProfileArn: str
    SharedWith: str
    ClientRequestToken: str

class CreateReviewTemplateInputTypeDef(TypedDict):
    TemplateName: str
    Description: str
    Lenses: Sequence[str]
    ClientRequestToken: str
    Notes: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class CreateTemplateShareInputTypeDef(TypedDict):
    TemplateArn: str
    SharedWith: str
    ClientRequestToken: str

class WorkloadJiraConfigurationInputTypeDef(TypedDict):
    IssueManagementStatus: NotRequired[WorkloadIssueManagementStatusType]
    IssueManagementType: NotRequired[IssueManagementTypeType]
    JiraProjectKey: NotRequired[str]

class CreateWorkloadShareInputTypeDef(TypedDict):
    WorkloadId: str
    SharedWith: str
    PermissionType: PermissionTypeType
    ClientRequestToken: str

class DeleteLensInputTypeDef(TypedDict):
    LensAlias: str
    ClientRequestToken: str
    LensStatus: LensStatusTypeType

class DeleteLensShareInputTypeDef(TypedDict):
    ShareId: str
    LensAlias: str
    ClientRequestToken: str

class DeleteProfileInputTypeDef(TypedDict):
    ProfileArn: str
    ClientRequestToken: str

class DeleteProfileShareInputTypeDef(TypedDict):
    ShareId: str
    ProfileArn: str
    ClientRequestToken: str

class DeleteReviewTemplateInputTypeDef(TypedDict):
    TemplateArn: str
    ClientRequestToken: str

class DeleteTemplateShareInputTypeDef(TypedDict):
    ShareId: str
    TemplateArn: str
    ClientRequestToken: str

class DeleteWorkloadInputTypeDef(TypedDict):
    WorkloadId: str
    ClientRequestToken: str

class DeleteWorkloadShareInputTypeDef(TypedDict):
    ShareId: str
    WorkloadId: str
    ClientRequestToken: str

class DisassociateLensesInputTypeDef(TypedDict):
    WorkloadId: str
    LensAliases: Sequence[str]

class DisassociateProfilesInputTypeDef(TypedDict):
    WorkloadId: str
    ProfileArns: Sequence[str]

class ExportLensInputTypeDef(TypedDict):
    LensAlias: str
    LensVersion: NotRequired[str]

class GetAnswerInputTypeDef(TypedDict):
    WorkloadId: str
    LensAlias: str
    QuestionId: str
    MilestoneNumber: NotRequired[int]

class GetConsolidatedReportInputTypeDef(TypedDict):
    Format: ReportFormatType
    IncludeSharedResources: NotRequired[bool]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class GetLensInputTypeDef(TypedDict):
    LensAlias: str
    LensVersion: NotRequired[str]

class LensTypeDef(TypedDict):
    LensArn: NotRequired[str]
    LensVersion: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    Owner: NotRequired[str]
    ShareInvitationId: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]

class GetLensReviewInputTypeDef(TypedDict):
    WorkloadId: str
    LensAlias: str
    MilestoneNumber: NotRequired[int]

class GetLensReviewReportInputTypeDef(TypedDict):
    WorkloadId: str
    LensAlias: str
    MilestoneNumber: NotRequired[int]

class LensReviewReportTypeDef(TypedDict):
    LensAlias: NotRequired[str]
    LensArn: NotRequired[str]
    Base64String: NotRequired[str]

class GetLensVersionDifferenceInputTypeDef(TypedDict):
    LensAlias: str
    BaseLensVersion: NotRequired[str]
    TargetLensVersion: NotRequired[str]

class GetMilestoneInputTypeDef(TypedDict):
    WorkloadId: str
    MilestoneNumber: int

class GetProfileInputTypeDef(TypedDict):
    ProfileArn: str
    ProfileVersion: NotRequired[str]

class GetReviewTemplateAnswerInputTypeDef(TypedDict):
    TemplateArn: str
    LensAlias: str
    QuestionId: str

class GetReviewTemplateInputTypeDef(TypedDict):
    TemplateArn: str

class GetReviewTemplateLensReviewInputTypeDef(TypedDict):
    TemplateArn: str
    LensAlias: str

class ReviewTemplateTypeDef(TypedDict):
    Description: NotRequired[str]
    Lenses: NotRequired[List[str]]
    Notes: NotRequired[str]
    QuestionCounts: NotRequired[Dict[QuestionType, int]]
    Owner: NotRequired[str]
    UpdatedAt: NotRequired[datetime]
    TemplateArn: NotRequired[str]
    TemplateName: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]
    UpdateStatus: NotRequired[ReviewTemplateUpdateStatusType]
    ShareInvitationId: NotRequired[str]

class GetWorkloadInputTypeDef(TypedDict):
    WorkloadId: str

class ImportLensInputTypeDef(TypedDict):
    JSONString: str
    ClientRequestToken: str
    LensAlias: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class SelectedPillarOutputTypeDef(TypedDict):
    PillarId: NotRequired[str]
    SelectedQuestionIds: NotRequired[List[str]]

class SelectedPillarTypeDef(TypedDict):
    PillarId: NotRequired[str]
    SelectedQuestionIds: NotRequired[Sequence[str]]

class WorkloadProfileTypeDef(TypedDict):
    ProfileArn: NotRequired[str]
    ProfileVersion: NotRequired[str]

class PillarReviewSummaryTypeDef(TypedDict):
    PillarId: NotRequired[str]
    PillarName: NotRequired[str]
    Notes: NotRequired[str]
    RiskCounts: NotRequired[Dict[RiskType, int]]
    PrioritizedRiskCounts: NotRequired[Dict[RiskType, int]]

class LensShareSummaryTypeDef(TypedDict):
    ShareId: NotRequired[str]
    SharedWith: NotRequired[str]
    Status: NotRequired[ShareStatusType]
    StatusMessage: NotRequired[str]

class LensSummaryTypeDef(TypedDict):
    LensArn: NotRequired[str]
    LensAlias: NotRequired[str]
    LensName: NotRequired[str]
    LensType: NotRequired[LensTypeType]
    Description: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    UpdatedAt: NotRequired[datetime]
    LensVersion: NotRequired[str]
    Owner: NotRequired[str]
    LensStatus: NotRequired[LensStatusType]

class LensUpgradeSummaryTypeDef(TypedDict):
    WorkloadId: NotRequired[str]
    WorkloadName: NotRequired[str]
    LensAlias: NotRequired[str]
    LensArn: NotRequired[str]
    CurrentLensVersion: NotRequired[str]
    LatestLensVersion: NotRequired[str]
    ResourceArn: NotRequired[str]
    ResourceName: NotRequired[str]

class ListAnswersInputTypeDef(TypedDict):
    WorkloadId: str
    LensAlias: str
    PillarId: NotRequired[str]
    MilestoneNumber: NotRequired[int]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    QuestionPriority: NotRequired[QuestionPriorityType]

class ListCheckDetailsInputTypeDef(TypedDict):
    WorkloadId: str
    LensArn: str
    PillarId: str
    QuestionId: str
    ChoiceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListCheckSummariesInputTypeDef(TypedDict):
    WorkloadId: str
    LensArn: str
    PillarId: str
    QuestionId: str
    ChoiceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListLensReviewImprovementsInputTypeDef(TypedDict):
    WorkloadId: str
    LensAlias: str
    PillarId: NotRequired[str]
    MilestoneNumber: NotRequired[int]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    QuestionPriority: NotRequired[QuestionPriorityType]

class ListLensReviewsInputTypeDef(TypedDict):
    WorkloadId: str
    MilestoneNumber: NotRequired[int]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListLensSharesInputTypeDef(TypedDict):
    LensAlias: str
    SharedWithPrefix: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Status: NotRequired[ShareStatusType]

class ListLensesInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    LensType: NotRequired[LensTypeType]
    LensStatus: NotRequired[LensStatusTypeType]
    LensName: NotRequired[str]

class ListMilestonesInputTypeDef(TypedDict):
    WorkloadId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListNotificationsInputTypeDef(TypedDict):
    WorkloadId: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ResourceArn: NotRequired[str]

class ListProfileNotificationsInputTypeDef(TypedDict):
    WorkloadId: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

ProfileNotificationSummaryTypeDef = TypedDict(
    "ProfileNotificationSummaryTypeDef",
    {
        "CurrentProfileVersion": NotRequired[str],
        "LatestProfileVersion": NotRequired[str],
        "Type": NotRequired[ProfileNotificationTypeType],
        "ProfileArn": NotRequired[str],
        "ProfileName": NotRequired[str],
        "WorkloadId": NotRequired[str],
        "WorkloadName": NotRequired[str],
    },
)

class ListProfileSharesInputTypeDef(TypedDict):
    ProfileArn: str
    SharedWithPrefix: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Status: NotRequired[ShareStatusType]

class ProfileShareSummaryTypeDef(TypedDict):
    ShareId: NotRequired[str]
    SharedWith: NotRequired[str]
    Status: NotRequired[ShareStatusType]
    StatusMessage: NotRequired[str]

class ListProfilesInputTypeDef(TypedDict):
    ProfileNamePrefix: NotRequired[str]
    ProfileOwnerType: NotRequired[ProfileOwnerTypeType]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ProfileSummaryTypeDef(TypedDict):
    ProfileArn: NotRequired[str]
    ProfileVersion: NotRequired[str]
    ProfileName: NotRequired[str]
    ProfileDescription: NotRequired[str]
    Owner: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    UpdatedAt: NotRequired[datetime]

class ListReviewTemplateAnswersInputTypeDef(TypedDict):
    TemplateArn: str
    LensAlias: str
    PillarId: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListReviewTemplatesInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ReviewTemplateSummaryTypeDef(TypedDict):
    Description: NotRequired[str]
    Lenses: NotRequired[List[str]]
    Owner: NotRequired[str]
    UpdatedAt: NotRequired[datetime]
    TemplateArn: NotRequired[str]
    TemplateName: NotRequired[str]
    UpdateStatus: NotRequired[ReviewTemplateUpdateStatusType]

class ListShareInvitationsInputTypeDef(TypedDict):
    WorkloadNamePrefix: NotRequired[str]
    LensNamePrefix: NotRequired[str]
    ShareResourceType: NotRequired[ShareResourceTypeType]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ProfileNamePrefix: NotRequired[str]
    TemplateNamePrefix: NotRequired[str]

class ShareInvitationSummaryTypeDef(TypedDict):
    ShareInvitationId: NotRequired[str]
    SharedBy: NotRequired[str]
    SharedWith: NotRequired[str]
    PermissionType: NotRequired[PermissionTypeType]
    ShareResourceType: NotRequired[ShareResourceTypeType]
    WorkloadName: NotRequired[str]
    WorkloadId: NotRequired[str]
    LensName: NotRequired[str]
    LensArn: NotRequired[str]
    ProfileName: NotRequired[str]
    ProfileArn: NotRequired[str]
    TemplateName: NotRequired[str]
    TemplateArn: NotRequired[str]

class ListTagsForResourceInputTypeDef(TypedDict):
    WorkloadArn: str

class ListTemplateSharesInputTypeDef(TypedDict):
    TemplateArn: str
    SharedWithPrefix: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Status: NotRequired[ShareStatusType]

class TemplateShareSummaryTypeDef(TypedDict):
    ShareId: NotRequired[str]
    SharedWith: NotRequired[str]
    Status: NotRequired[ShareStatusType]
    StatusMessage: NotRequired[str]

class ListWorkloadSharesInputTypeDef(TypedDict):
    WorkloadId: str
    SharedWithPrefix: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Status: NotRequired[ShareStatusType]

class WorkloadShareSummaryTypeDef(TypedDict):
    ShareId: NotRequired[str]
    SharedWith: NotRequired[str]
    PermissionType: NotRequired[PermissionTypeType]
    Status: NotRequired[ShareStatusType]
    StatusMessage: NotRequired[str]

class ListWorkloadsInputTypeDef(TypedDict):
    WorkloadNamePrefix: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class QuestionDifferenceTypeDef(TypedDict):
    QuestionId: NotRequired[str]
    QuestionTitle: NotRequired[str]
    DifferenceStatus: NotRequired[DifferenceStatusType]

class ProfileChoiceTypeDef(TypedDict):
    ChoiceId: NotRequired[str]
    ChoiceTitle: NotRequired[str]
    ChoiceDescription: NotRequired[str]

class ProfileTemplateChoiceTypeDef(TypedDict):
    ChoiceId: NotRequired[str]
    ChoiceTitle: NotRequired[str]
    ChoiceDescription: NotRequired[str]

class ReviewTemplatePillarReviewSummaryTypeDef(TypedDict):
    PillarId: NotRequired[str]
    PillarName: NotRequired[str]
    Notes: NotRequired[str]
    QuestionCounts: NotRequired[Dict[QuestionType, int]]

class ShareInvitationTypeDef(TypedDict):
    ShareInvitationId: NotRequired[str]
    ShareResourceType: NotRequired[ShareResourceTypeType]
    WorkloadId: NotRequired[str]
    LensAlias: NotRequired[str]
    LensArn: NotRequired[str]
    ProfileArn: NotRequired[str]
    TemplateArn: NotRequired[str]

class TagResourceInputTypeDef(TypedDict):
    WorkloadArn: str
    Tags: Mapping[str, str]

class UntagResourceInputTypeDef(TypedDict):
    WorkloadArn: str
    TagKeys: Sequence[str]

class UpdateIntegrationInputTypeDef(TypedDict):
    WorkloadId: str
    ClientRequestToken: str
    IntegratingService: Literal["JIRA"]

class UpdateReviewTemplateInputTypeDef(TypedDict):
    TemplateArn: str
    TemplateName: NotRequired[str]
    Description: NotRequired[str]
    Notes: NotRequired[str]
    LensesToAssociate: NotRequired[Sequence[str]]
    LensesToDisassociate: NotRequired[Sequence[str]]

class UpdateReviewTemplateLensReviewInputTypeDef(TypedDict):
    TemplateArn: str
    LensAlias: str
    LensNotes: NotRequired[str]
    PillarNotes: NotRequired[Mapping[str, str]]

class UpdateShareInvitationInputTypeDef(TypedDict):
    ShareInvitationId: str
    ShareInvitationAction: ShareInvitationActionType

class UpdateWorkloadShareInputTypeDef(TypedDict):
    ShareId: str
    WorkloadId: str
    PermissionType: PermissionTypeType

class WorkloadShareTypeDef(TypedDict):
    ShareId: NotRequired[str]
    SharedBy: NotRequired[str]
    SharedWith: NotRequired[str]
    PermissionType: NotRequired[PermissionTypeType]
    Status: NotRequired[ShareStatusType]
    WorkloadName: NotRequired[str]
    WorkloadId: NotRequired[str]

class UpgradeLensReviewInputTypeDef(TypedDict):
    WorkloadId: str
    LensAlias: str
    MilestoneName: str
    ClientRequestToken: NotRequired[str]

class UpgradeProfileVersionInputTypeDef(TypedDict):
    WorkloadId: str
    ProfileArn: str
    MilestoneName: NotRequired[str]
    ClientRequestToken: NotRequired[str]

class UpgradeReviewTemplateLensReviewInputTypeDef(TypedDict):
    TemplateArn: str
    LensAlias: str
    ClientRequestToken: NotRequired[str]

class WorkloadDiscoveryConfigOutputTypeDef(TypedDict):
    TrustedAdvisorIntegrationStatus: NotRequired[TrustedAdvisorIntegrationStatusType]
    WorkloadResourceDefinition: NotRequired[List[DefinitionTypeType]]

class WorkloadDiscoveryConfigTypeDef(TypedDict):
    TrustedAdvisorIntegrationStatus: NotRequired[TrustedAdvisorIntegrationStatusType]
    WorkloadResourceDefinition: NotRequired[Sequence[DefinitionTypeType]]

class WorkloadJiraConfigurationOutputTypeDef(TypedDict):
    IssueManagementStatus: NotRequired[WorkloadIssueManagementStatusType]
    IssueManagementType: NotRequired[IssueManagementTypeType]
    JiraProjectKey: NotRequired[str]
    StatusMessage: NotRequired[str]

class UpdateGlobalSettingsInputTypeDef(TypedDict):
    OrganizationSharingStatus: NotRequired[OrganizationSharingStatusType]
    DiscoveryIntegrationStatus: NotRequired[DiscoveryIntegrationStatusType]
    JiraConfiguration: NotRequired[AccountJiraConfigurationInputTypeDef]

AdditionalResourcesTypeDef = TypedDict(
    "AdditionalResourcesTypeDef",
    {
        "Type": NotRequired[AdditionalResourceTypeType],
        "Content": NotRequired[List[ChoiceContentTypeDef]],
    },
)

class QuestionMetricTypeDef(TypedDict):
    QuestionId: NotRequired[str]
    Risk: NotRequired[RiskType]
    BestPractices: NotRequired[List[BestPracticeTypeDef]]

class ImprovementSummaryTypeDef(TypedDict):
    QuestionId: NotRequired[str]
    PillarId: NotRequired[str]
    QuestionTitle: NotRequired[str]
    Risk: NotRequired[RiskType]
    ImprovementPlanUrl: NotRequired[str]
    ImprovementPlans: NotRequired[List[ChoiceImprovementPlanTypeDef]]
    JiraConfiguration: NotRequired[JiraConfigurationTypeDef]

class UpdateAnswerInputTypeDef(TypedDict):
    WorkloadId: str
    LensAlias: str
    QuestionId: str
    SelectedChoices: NotRequired[Sequence[str]]
    ChoiceUpdates: NotRequired[Mapping[str, ChoiceUpdateTypeDef]]
    Notes: NotRequired[str]
    IsApplicable: NotRequired[bool]
    Reason: NotRequired[AnswerReasonType]

class UpdateReviewTemplateAnswerInputTypeDef(TypedDict):
    TemplateArn: str
    LensAlias: str
    QuestionId: str
    SelectedChoices: NotRequired[Sequence[str]]
    ChoiceUpdates: NotRequired[Mapping[str, ChoiceUpdateTypeDef]]
    Notes: NotRequired[str]
    IsApplicable: NotRequired[bool]
    Reason: NotRequired[AnswerReasonType]

class CreateLensShareOutputTypeDef(TypedDict):
    ShareId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLensVersionOutputTypeDef(TypedDict):
    LensArn: str
    LensVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMilestoneOutputTypeDef(TypedDict):
    WorkloadId: str
    MilestoneNumber: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfileOutputTypeDef(TypedDict):
    ProfileArn: str
    ProfileVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfileShareOutputTypeDef(TypedDict):
    ShareId: str
    ProfileArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReviewTemplateOutputTypeDef(TypedDict):
    TemplateArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTemplateShareOutputTypeDef(TypedDict):
    TemplateArn: str
    ShareId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkloadOutputTypeDef(TypedDict):
    WorkloadId: str
    WorkloadArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkloadShareOutputTypeDef(TypedDict):
    WorkloadId: str
    ShareId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ExportLensOutputTypeDef(TypedDict):
    LensJSON: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGlobalSettingsOutputTypeDef(TypedDict):
    OrganizationSharingStatus: OrganizationSharingStatusType
    DiscoveryIntegrationStatus: DiscoveryIntegrationStatusType
    JiraConfiguration: AccountJiraConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportLensOutputTypeDef(TypedDict):
    LensArn: str
    Status: ImportLensStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListCheckDetailsOutputTypeDef(TypedDict):
    CheckDetails: List[CheckDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListCheckSummariesOutputTypeDef(TypedDict):
    CheckSummaries: List[CheckSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceOutputTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfileInputTypeDef(TypedDict):
    ProfileName: str
    ProfileDescription: str
    ProfileQuestions: Sequence[ProfileQuestionUpdateTypeDef]
    ClientRequestToken: str
    Tags: NotRequired[Mapping[str, str]]

class UpdateProfileInputTypeDef(TypedDict):
    ProfileArn: str
    ProfileDescription: NotRequired[str]
    ProfileQuestions: NotRequired[Sequence[ProfileQuestionUpdateTypeDef]]

class GetLensOutputTypeDef(TypedDict):
    Lens: LensTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLensReviewReportOutputTypeDef(TypedDict):
    WorkloadId: str
    MilestoneNumber: int
    LensReviewReport: LensReviewReportTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetReviewTemplateOutputTypeDef(TypedDict):
    ReviewTemplate: ReviewTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReviewTemplateOutputTypeDef(TypedDict):
    ReviewTemplate: ReviewTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JiraSelectedQuestionConfigurationOutputTypeDef(TypedDict):
    SelectedPillars: NotRequired[List[SelectedPillarOutputTypeDef]]

class JiraSelectedQuestionConfigurationTypeDef(TypedDict):
    SelectedPillars: NotRequired[Sequence[SelectedPillarTypeDef]]

class LensReviewSummaryTypeDef(TypedDict):
    LensAlias: NotRequired[str]
    LensArn: NotRequired[str]
    LensVersion: NotRequired[str]
    LensName: NotRequired[str]
    LensStatus: NotRequired[LensStatusType]
    UpdatedAt: NotRequired[datetime]
    RiskCounts: NotRequired[Dict[RiskType, int]]
    Profiles: NotRequired[List[WorkloadProfileTypeDef]]
    PrioritizedRiskCounts: NotRequired[Dict[RiskType, int]]

class WorkloadSummaryTypeDef(TypedDict):
    WorkloadId: NotRequired[str]
    WorkloadArn: NotRequired[str]
    WorkloadName: NotRequired[str]
    Owner: NotRequired[str]
    UpdatedAt: NotRequired[datetime]
    Lenses: NotRequired[List[str]]
    RiskCounts: NotRequired[Dict[RiskType, int]]
    ImprovementStatus: NotRequired[WorkloadImprovementStatusType]
    Profiles: NotRequired[List[WorkloadProfileTypeDef]]
    PrioritizedRiskCounts: NotRequired[Dict[RiskType, int]]

class ListLensSharesOutputTypeDef(TypedDict):
    LensShareSummaries: List[LensShareSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListLensesOutputTypeDef(TypedDict):
    LensSummaries: List[LensSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

NotificationSummaryTypeDef = TypedDict(
    "NotificationSummaryTypeDef",
    {
        "Type": NotRequired[NotificationTypeType],
        "LensUpgradeSummary": NotRequired[LensUpgradeSummaryTypeDef],
    },
)

class ListProfileNotificationsOutputTypeDef(TypedDict):
    NotificationSummaries: List[ProfileNotificationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListProfileSharesOutputTypeDef(TypedDict):
    ProfileShareSummaries: List[ProfileShareSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListProfilesOutputTypeDef(TypedDict):
    ProfileSummaries: List[ProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListReviewTemplatesOutputTypeDef(TypedDict):
    ReviewTemplates: List[ReviewTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListShareInvitationsOutputTypeDef(TypedDict):
    ShareInvitationSummaries: List[ShareInvitationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTemplateSharesOutputTypeDef(TypedDict):
    TemplateArn: str
    TemplateShareSummaries: List[TemplateShareSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListWorkloadSharesOutputTypeDef(TypedDict):
    WorkloadId: str
    WorkloadShareSummaries: List[WorkloadShareSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PillarDifferenceTypeDef(TypedDict):
    PillarId: NotRequired[str]
    PillarName: NotRequired[str]
    DifferenceStatus: NotRequired[DifferenceStatusType]
    QuestionDifferences: NotRequired[List[QuestionDifferenceTypeDef]]

class ProfileQuestionTypeDef(TypedDict):
    QuestionId: NotRequired[str]
    QuestionTitle: NotRequired[str]
    QuestionDescription: NotRequired[str]
    QuestionChoices: NotRequired[List[ProfileChoiceTypeDef]]
    SelectedChoiceIds: NotRequired[List[str]]
    MinSelectedChoices: NotRequired[int]
    MaxSelectedChoices: NotRequired[int]

class ProfileTemplateQuestionTypeDef(TypedDict):
    QuestionId: NotRequired[str]
    QuestionTitle: NotRequired[str]
    QuestionDescription: NotRequired[str]
    QuestionChoices: NotRequired[List[ProfileTemplateChoiceTypeDef]]
    MinSelectedChoices: NotRequired[int]
    MaxSelectedChoices: NotRequired[int]

class ReviewTemplateLensReviewTypeDef(TypedDict):
    LensAlias: NotRequired[str]
    LensArn: NotRequired[str]
    LensVersion: NotRequired[str]
    LensName: NotRequired[str]
    LensStatus: NotRequired[LensStatusType]
    PillarReviewSummaries: NotRequired[List[ReviewTemplatePillarReviewSummaryTypeDef]]
    UpdatedAt: NotRequired[datetime]
    Notes: NotRequired[str]
    QuestionCounts: NotRequired[Dict[QuestionType, int]]
    NextToken: NotRequired[str]

class UpdateShareInvitationOutputTypeDef(TypedDict):
    ShareInvitation: ShareInvitationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkloadShareOutputTypeDef(TypedDict):
    WorkloadId: str
    WorkloadShare: WorkloadShareTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

WorkloadDiscoveryConfigUnionTypeDef = Union[
    WorkloadDiscoveryConfigTypeDef, WorkloadDiscoveryConfigOutputTypeDef
]

class WorkloadTypeDef(TypedDict):
    WorkloadId: NotRequired[str]
    WorkloadArn: NotRequired[str]
    WorkloadName: NotRequired[str]
    Description: NotRequired[str]
    Environment: NotRequired[WorkloadEnvironmentType]
    UpdatedAt: NotRequired[datetime]
    AccountIds: NotRequired[List[str]]
    AwsRegions: NotRequired[List[str]]
    NonAwsRegions: NotRequired[List[str]]
    ArchitecturalDesign: NotRequired[str]
    ReviewOwner: NotRequired[str]
    ReviewRestrictionDate: NotRequired[datetime]
    IsReviewOwnerUpdateAcknowledged: NotRequired[bool]
    IndustryType: NotRequired[str]
    Industry: NotRequired[str]
    Notes: NotRequired[str]
    ImprovementStatus: NotRequired[WorkloadImprovementStatusType]
    RiskCounts: NotRequired[Dict[RiskType, int]]
    PillarPriorities: NotRequired[List[str]]
    Lenses: NotRequired[List[str]]
    Owner: NotRequired[str]
    ShareInvitationId: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]
    DiscoveryConfig: NotRequired[WorkloadDiscoveryConfigOutputTypeDef]
    Applications: NotRequired[List[str]]
    Profiles: NotRequired[List[WorkloadProfileTypeDef]]
    PrioritizedRiskCounts: NotRequired[Dict[RiskType, int]]
    JiraConfiguration: NotRequired[WorkloadJiraConfigurationOutputTypeDef]

class ChoiceTypeDef(TypedDict):
    ChoiceId: NotRequired[str]
    Title: NotRequired[str]
    Description: NotRequired[str]
    HelpfulResource: NotRequired[ChoiceContentTypeDef]
    ImprovementPlan: NotRequired[ChoiceContentTypeDef]
    AdditionalResources: NotRequired[List[AdditionalResourcesTypeDef]]

class PillarMetricTypeDef(TypedDict):
    PillarId: NotRequired[str]
    RiskCounts: NotRequired[Dict[RiskType, int]]
    Questions: NotRequired[List[QuestionMetricTypeDef]]

class ListLensReviewImprovementsOutputTypeDef(TypedDict):
    WorkloadId: str
    MilestoneNumber: int
    LensAlias: str
    LensArn: str
    ImprovementSummaries: List[ImprovementSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class LensReviewTypeDef(TypedDict):
    LensAlias: NotRequired[str]
    LensArn: NotRequired[str]
    LensVersion: NotRequired[str]
    LensName: NotRequired[str]
    LensStatus: NotRequired[LensStatusType]
    PillarReviewSummaries: NotRequired[List[PillarReviewSummaryTypeDef]]
    JiraConfiguration: NotRequired[JiraSelectedQuestionConfigurationOutputTypeDef]
    UpdatedAt: NotRequired[datetime]
    Notes: NotRequired[str]
    RiskCounts: NotRequired[Dict[RiskType, int]]
    NextToken: NotRequired[str]
    Profiles: NotRequired[List[WorkloadProfileTypeDef]]
    PrioritizedRiskCounts: NotRequired[Dict[RiskType, int]]

JiraSelectedQuestionConfigurationUnionTypeDef = Union[
    JiraSelectedQuestionConfigurationTypeDef, JiraSelectedQuestionConfigurationOutputTypeDef
]

class ListLensReviewsOutputTypeDef(TypedDict):
    WorkloadId: str
    MilestoneNumber: int
    LensReviewSummaries: List[LensReviewSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListWorkloadsOutputTypeDef(TypedDict):
    WorkloadSummaries: List[WorkloadSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class MilestoneSummaryTypeDef(TypedDict):
    MilestoneNumber: NotRequired[int]
    MilestoneName: NotRequired[str]
    RecordedAt: NotRequired[datetime]
    WorkloadSummary: NotRequired[WorkloadSummaryTypeDef]

class ListNotificationsOutputTypeDef(TypedDict):
    NotificationSummaries: List[NotificationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class VersionDifferencesTypeDef(TypedDict):
    PillarDifferences: NotRequired[List[PillarDifferenceTypeDef]]

class ProfileTypeDef(TypedDict):
    ProfileArn: NotRequired[str]
    ProfileVersion: NotRequired[str]
    ProfileName: NotRequired[str]
    ProfileDescription: NotRequired[str]
    ProfileQuestions: NotRequired[List[ProfileQuestionTypeDef]]
    Owner: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    UpdatedAt: NotRequired[datetime]
    ShareInvitationId: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]

class ProfileTemplateTypeDef(TypedDict):
    TemplateName: NotRequired[str]
    TemplateQuestions: NotRequired[List[ProfileTemplateQuestionTypeDef]]
    CreatedAt: NotRequired[datetime]
    UpdatedAt: NotRequired[datetime]

class GetReviewTemplateLensReviewOutputTypeDef(TypedDict):
    TemplateArn: str
    LensReview: ReviewTemplateLensReviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReviewTemplateLensReviewOutputTypeDef(TypedDict):
    TemplateArn: str
    LensReview: ReviewTemplateLensReviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkloadInputTypeDef(TypedDict):
    WorkloadName: str
    Description: str
    Environment: WorkloadEnvironmentType
    Lenses: Sequence[str]
    ClientRequestToken: str
    AccountIds: NotRequired[Sequence[str]]
    AwsRegions: NotRequired[Sequence[str]]
    NonAwsRegions: NotRequired[Sequence[str]]
    PillarPriorities: NotRequired[Sequence[str]]
    ArchitecturalDesign: NotRequired[str]
    ReviewOwner: NotRequired[str]
    IndustryType: NotRequired[str]
    Industry: NotRequired[str]
    Notes: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    DiscoveryConfig: NotRequired[WorkloadDiscoveryConfigUnionTypeDef]
    Applications: NotRequired[Sequence[str]]
    ProfileArns: NotRequired[Sequence[str]]
    ReviewTemplateArns: NotRequired[Sequence[str]]
    JiraConfiguration: NotRequired[WorkloadJiraConfigurationInputTypeDef]

class UpdateWorkloadInputTypeDef(TypedDict):
    WorkloadId: str
    WorkloadName: NotRequired[str]
    Description: NotRequired[str]
    Environment: NotRequired[WorkloadEnvironmentType]
    AccountIds: NotRequired[Sequence[str]]
    AwsRegions: NotRequired[Sequence[str]]
    NonAwsRegions: NotRequired[Sequence[str]]
    PillarPriorities: NotRequired[Sequence[str]]
    ArchitecturalDesign: NotRequired[str]
    ReviewOwner: NotRequired[str]
    IsReviewOwnerUpdateAcknowledged: NotRequired[bool]
    IndustryType: NotRequired[str]
    Industry: NotRequired[str]
    Notes: NotRequired[str]
    ImprovementStatus: NotRequired[WorkloadImprovementStatusType]
    DiscoveryConfig: NotRequired[WorkloadDiscoveryConfigUnionTypeDef]
    Applications: NotRequired[Sequence[str]]
    JiraConfiguration: NotRequired[WorkloadJiraConfigurationInputTypeDef]

class GetWorkloadOutputTypeDef(TypedDict):
    Workload: WorkloadTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MilestoneTypeDef(TypedDict):
    MilestoneNumber: NotRequired[int]
    MilestoneName: NotRequired[str]
    RecordedAt: NotRequired[datetime]
    Workload: NotRequired[WorkloadTypeDef]

class UpdateWorkloadOutputTypeDef(TypedDict):
    Workload: WorkloadTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

AnswerSummaryTypeDef = TypedDict(
    "AnswerSummaryTypeDef",
    {
        "QuestionId": NotRequired[str],
        "PillarId": NotRequired[str],
        "QuestionTitle": NotRequired[str],
        "Choices": NotRequired[List[ChoiceTypeDef]],
        "SelectedChoices": NotRequired[List[str]],
        "ChoiceAnswerSummaries": NotRequired[List[ChoiceAnswerSummaryTypeDef]],
        "IsApplicable": NotRequired[bool],
        "Risk": NotRequired[RiskType],
        "Reason": NotRequired[AnswerReasonType],
        "QuestionType": NotRequired[QuestionTypeType],
        "JiraConfiguration": NotRequired[JiraConfigurationTypeDef],
    },
)

class AnswerTypeDef(TypedDict):
    QuestionId: NotRequired[str]
    PillarId: NotRequired[str]
    QuestionTitle: NotRequired[str]
    QuestionDescription: NotRequired[str]
    ImprovementPlanUrl: NotRequired[str]
    HelpfulResourceUrl: NotRequired[str]
    HelpfulResourceDisplayText: NotRequired[str]
    Choices: NotRequired[List[ChoiceTypeDef]]
    SelectedChoices: NotRequired[List[str]]
    ChoiceAnswers: NotRequired[List[ChoiceAnswerTypeDef]]
    IsApplicable: NotRequired[bool]
    Risk: NotRequired[RiskType]
    Notes: NotRequired[str]
    Reason: NotRequired[AnswerReasonType]
    JiraConfiguration: NotRequired[JiraConfigurationTypeDef]

ReviewTemplateAnswerSummaryTypeDef = TypedDict(
    "ReviewTemplateAnswerSummaryTypeDef",
    {
        "QuestionId": NotRequired[str],
        "PillarId": NotRequired[str],
        "QuestionTitle": NotRequired[str],
        "Choices": NotRequired[List[ChoiceTypeDef]],
        "SelectedChoices": NotRequired[List[str]],
        "ChoiceAnswerSummaries": NotRequired[List[ChoiceAnswerSummaryTypeDef]],
        "IsApplicable": NotRequired[bool],
        "AnswerStatus": NotRequired[ReviewTemplateAnswerStatusType],
        "Reason": NotRequired[AnswerReasonType],
        "QuestionType": NotRequired[QuestionTypeType],
    },
)

class ReviewTemplateAnswerTypeDef(TypedDict):
    QuestionId: NotRequired[str]
    PillarId: NotRequired[str]
    QuestionTitle: NotRequired[str]
    QuestionDescription: NotRequired[str]
    ImprovementPlanUrl: NotRequired[str]
    HelpfulResourceUrl: NotRequired[str]
    HelpfulResourceDisplayText: NotRequired[str]
    Choices: NotRequired[List[ChoiceTypeDef]]
    SelectedChoices: NotRequired[List[str]]
    ChoiceAnswers: NotRequired[List[ChoiceAnswerTypeDef]]
    IsApplicable: NotRequired[bool]
    AnswerStatus: NotRequired[ReviewTemplateAnswerStatusType]
    Notes: NotRequired[str]
    Reason: NotRequired[AnswerReasonType]

class LensMetricTypeDef(TypedDict):
    LensArn: NotRequired[str]
    Pillars: NotRequired[List[PillarMetricTypeDef]]
    RiskCounts: NotRequired[Dict[RiskType, int]]

class GetLensReviewOutputTypeDef(TypedDict):
    WorkloadId: str
    MilestoneNumber: int
    LensReview: LensReviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLensReviewOutputTypeDef(TypedDict):
    WorkloadId: str
    LensReview: LensReviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLensReviewInputTypeDef(TypedDict):
    WorkloadId: str
    LensAlias: str
    LensNotes: NotRequired[str]
    PillarNotes: NotRequired[Mapping[str, str]]
    JiraConfiguration: NotRequired[JiraSelectedQuestionConfigurationUnionTypeDef]

class ListMilestonesOutputTypeDef(TypedDict):
    WorkloadId: str
    MilestoneSummaries: List[MilestoneSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetLensVersionDifferenceOutputTypeDef(TypedDict):
    LensAlias: str
    LensArn: str
    BaseLensVersion: str
    TargetLensVersion: str
    LatestLensVersion: str
    VersionDifferences: VersionDifferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProfileOutputTypeDef(TypedDict):
    Profile: ProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProfileOutputTypeDef(TypedDict):
    Profile: ProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProfileTemplateOutputTypeDef(TypedDict):
    ProfileTemplate: ProfileTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMilestoneOutputTypeDef(TypedDict):
    WorkloadId: str
    Milestone: MilestoneTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnswersOutputTypeDef(TypedDict):
    WorkloadId: str
    MilestoneNumber: int
    LensAlias: str
    LensArn: str
    AnswerSummaries: List[AnswerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetAnswerOutputTypeDef(TypedDict):
    WorkloadId: str
    MilestoneNumber: int
    LensAlias: str
    LensArn: str
    Answer: AnswerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAnswerOutputTypeDef(TypedDict):
    WorkloadId: str
    LensAlias: str
    LensArn: str
    Answer: AnswerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListReviewTemplateAnswersOutputTypeDef(TypedDict):
    TemplateArn: str
    LensAlias: str
    AnswerSummaries: List[ReviewTemplateAnswerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetReviewTemplateAnswerOutputTypeDef(TypedDict):
    TemplateArn: str
    LensAlias: str
    Answer: ReviewTemplateAnswerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReviewTemplateAnswerOutputTypeDef(TypedDict):
    TemplateArn: str
    LensAlias: str
    Answer: ReviewTemplateAnswerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ConsolidatedReportMetricTypeDef(TypedDict):
    MetricType: NotRequired[Literal["WORKLOAD"]]
    RiskCounts: NotRequired[Dict[RiskType, int]]
    WorkloadId: NotRequired[str]
    WorkloadName: NotRequired[str]
    WorkloadArn: NotRequired[str]
    UpdatedAt: NotRequired[datetime]
    Lenses: NotRequired[List[LensMetricTypeDef]]
    LensesAppliedCount: NotRequired[int]

class GetConsolidatedReportOutputTypeDef(TypedDict):
    Metrics: List[ConsolidatedReportMetricTypeDef]
    Base64String: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
