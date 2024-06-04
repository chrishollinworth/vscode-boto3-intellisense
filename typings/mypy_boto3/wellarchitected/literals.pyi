"""
Type annotations for wellarchitected service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/literals.html)

Usage::

    ```python
    from mypy_boto3_wellarchitected.literals import AccountJiraIssueManagementStatusType

    data: AccountJiraIssueManagementStatusType = "DISABLED"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccountJiraIssueManagementStatusType",
    "AdditionalResourceTypeType",
    "AnswerReasonType",
    "CheckFailureReasonType",
    "CheckProviderType",
    "CheckStatusType",
    "ChoiceReasonType",
    "ChoiceStatusType",
    "DefinitionTypeType",
    "DifferenceStatusType",
    "DiscoveryIntegrationStatusType",
    "ImportLensStatusType",
    "IntegratingServiceType",
    "IntegrationStatusInputType",
    "IntegrationStatusType",
    "IssueManagementTypeType",
    "LensStatusType",
    "LensStatusTypeType",
    "LensTypeType",
    "MetricTypeType",
    "NotificationTypeType",
    "OrganizationSharingStatusType",
    "PermissionTypeType",
    "ProfileNotificationTypeType",
    "ProfileOwnerTypeType",
    "QuestionPriorityType",
    "QuestionType",
    "QuestionTypeType",
    "ReportFormatType",
    "ReviewTemplateAnswerStatusType",
    "ReviewTemplateUpdateStatusType",
    "RiskType",
    "ShareInvitationActionType",
    "ShareResourceTypeType",
    "ShareStatusType",
    "TrustedAdvisorIntegrationStatusType",
    "WorkloadEnvironmentType",
    "WorkloadImprovementStatusType",
    "WorkloadIssueManagementStatusType",
)

AccountJiraIssueManagementStatusType = Literal["DISABLED", "ENABLED"]
AdditionalResourceTypeType = Literal["HELPFUL_RESOURCE", "IMPROVEMENT_PLAN"]
AnswerReasonType = Literal[
    "ARCHITECTURE_CONSTRAINTS", "BUSINESS_PRIORITIES", "NONE", "OTHER", "OUT_OF_SCOPE"
]
CheckFailureReasonType = Literal[
    "ACCESS_DENIED", "ASSUME_ROLE_ERROR", "PREMIUM_SUPPORT_REQUIRED", "UNKNOWN_ERROR"
]
CheckProviderType = Literal["TRUSTED_ADVISOR"]
CheckStatusType = Literal["ERROR", "FETCH_FAILED", "NOT_AVAILABLE", "OKAY", "WARNING"]
ChoiceReasonType = Literal[
    "ARCHITECTURE_CONSTRAINTS", "BUSINESS_PRIORITIES", "NONE", "OTHER", "OUT_OF_SCOPE"
]
ChoiceStatusType = Literal["NOT_APPLICABLE", "SELECTED", "UNSELECTED"]
DefinitionTypeType = Literal["APP_REGISTRY", "WORKLOAD_METADATA"]
DifferenceStatusType = Literal["DELETED", "NEW", "UPDATED"]
DiscoveryIntegrationStatusType = Literal["DISABLED", "ENABLED"]
ImportLensStatusType = Literal["COMPLETE", "ERROR", "IN_PROGRESS"]
IntegratingServiceType = Literal["JIRA"]
IntegrationStatusInputType = Literal["NOT_CONFIGURED"]
IntegrationStatusType = Literal["CONFIGURED", "NOT_CONFIGURED"]
IssueManagementTypeType = Literal["AUTO", "MANUAL"]
LensStatusType = Literal["CURRENT", "DELETED", "DEPRECATED", "NOT_CURRENT", "UNSHARED"]
LensStatusTypeType = Literal["ALL", "DRAFT", "PUBLISHED"]
LensTypeType = Literal["AWS_OFFICIAL", "CUSTOM_SELF", "CUSTOM_SHARED"]
MetricTypeType = Literal["WORKLOAD"]
NotificationTypeType = Literal["LENS_VERSION_DEPRECATED", "LENS_VERSION_UPGRADED"]
OrganizationSharingStatusType = Literal["DISABLED", "ENABLED"]
PermissionTypeType = Literal["CONTRIBUTOR", "READONLY"]
ProfileNotificationTypeType = Literal["PROFILE_ANSWERS_UPDATED", "PROFILE_DELETED"]
ProfileOwnerTypeType = Literal["SELF", "SHARED"]
QuestionPriorityType = Literal["NONE", "PRIORITIZED"]
QuestionType = Literal["ANSWERED", "UNANSWERED"]
QuestionTypeType = Literal["NON_PRIORITIZED", "PRIORITIZED"]
ReportFormatType = Literal["JSON", "PDF"]
ReviewTemplateAnswerStatusType = Literal["ANSWERED", "UNANSWERED"]
ReviewTemplateUpdateStatusType = Literal["CURRENT", "LENS_NOT_CURRENT"]
RiskType = Literal["HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE", "UNANSWERED"]
ShareInvitationActionType = Literal["ACCEPT", "REJECT"]
ShareResourceTypeType = Literal["LENS", "PROFILE", "TEMPLATE", "WORKLOAD"]
ShareStatusType = Literal[
    "ACCEPTED", "ASSOCIATED", "ASSOCIATING", "EXPIRED", "FAILED", "PENDING", "REJECTED", "REVOKED"
]
TrustedAdvisorIntegrationStatusType = Literal["DISABLED", "ENABLED"]
WorkloadEnvironmentType = Literal["PREPRODUCTION", "PRODUCTION"]
WorkloadImprovementStatusType = Literal[
    "COMPLETE", "IN_PROGRESS", "NOT_APPLICABLE", "NOT_STARTED", "RISK_ACKNOWLEDGED"
]
WorkloadIssueManagementStatusType = Literal["DISABLED", "ENABLED", "INHERIT"]
