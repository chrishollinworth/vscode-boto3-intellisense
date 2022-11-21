"""
Type annotations for wellarchitected service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/literals.html)

Usage::

    ```python
    from mypy_boto3_wellarchitected.literals import AdditionalResourceTypeType

    data: AdditionalResourceTypeType = "HELPFUL_RESOURCE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AdditionalResourceTypeType",
    "AnswerReasonType",
    "CheckFailureReasonType",
    "CheckProviderType",
    "CheckStatusType",
    "ChoiceReasonType",
    "ChoiceStatusType",
    "DifferenceStatusType",
    "ImportLensStatusType",
    "LensStatusType",
    "LensStatusTypeType",
    "LensTypeType",
    "NotificationTypeType",
    "OrganizationSharingStatusType",
    "PermissionTypeType",
    "RiskType",
    "ShareInvitationActionType",
    "ShareResourceTypeType",
    "ShareStatusType",
    "TrustedAdvisorIntegrationStatusType",
    "WorkloadEnvironmentType",
    "WorkloadImprovementStatusType",
)

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
DifferenceStatusType = Literal["DELETED", "NEW", "UPDATED"]
ImportLensStatusType = Literal["COMPLETE", "ERROR", "IN_PROGRESS"]
LensStatusType = Literal["CURRENT", "DELETED", "DEPRECATED", "NOT_CURRENT", "UNSHARED"]
LensStatusTypeType = Literal["ALL", "DRAFT", "PUBLISHED"]
LensTypeType = Literal["AWS_OFFICIAL", "CUSTOM_SELF", "CUSTOM_SHARED"]
NotificationTypeType = Literal["LENS_VERSION_DEPRECATED", "LENS_VERSION_UPGRADED"]
OrganizationSharingStatusType = Literal["DISABLED", "ENABLED"]
PermissionTypeType = Literal["CONTRIBUTOR", "READONLY"]
RiskType = Literal["HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE", "UNANSWERED"]
ShareInvitationActionType = Literal["ACCEPT", "REJECT"]
ShareResourceTypeType = Literal["LENS", "WORKLOAD"]
ShareStatusType = Literal[
    "ACCEPTED", "ASSOCIATED", "ASSOCIATING", "EXPIRED", "FAILED", "PENDING", "REJECTED", "REVOKED"
]
TrustedAdvisorIntegrationStatusType = Literal["DISABLED", "ENABLED"]
WorkloadEnvironmentType = Literal["PREPRODUCTION", "PRODUCTION"]
WorkloadImprovementStatusType = Literal[
    "COMPLETE", "IN_PROGRESS", "NOT_APPLICABLE", "NOT_STARTED", "RISK_ACKNOWLEDGED"
]
