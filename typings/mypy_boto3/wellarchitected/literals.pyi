"""
Type annotations for wellarchitected service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/literals.html)

Usage::

    ```python
    from mypy_boto3_wellarchitected.literals import AnswerReasonType

    data: AnswerReasonType = "ARCHITECTURE_CONSTRAINTS"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AnswerReasonType",
    "ChoiceReasonType",
    "ChoiceStatusType",
    "DifferenceStatusType",
    "LensStatusType",
    "NotificationTypeType",
    "PermissionTypeType",
    "RiskType",
    "ShareInvitationActionType",
    "ShareStatusType",
    "WorkloadEnvironmentType",
    "WorkloadImprovementStatusType",
)

AnswerReasonType = Literal[
    "ARCHITECTURE_CONSTRAINTS", "BUSINESS_PRIORITIES", "NONE", "OTHER", "OUT_OF_SCOPE"
]
ChoiceReasonType = Literal[
    "ARCHITECTURE_CONSTRAINTS", "BUSINESS_PRIORITIES", "NONE", "OTHER", "OUT_OF_SCOPE"
]
ChoiceStatusType = Literal["NOT_APPLICABLE", "SELECTED", "UNSELECTED"]
DifferenceStatusType = Literal["DELETED", "NEW", "UPDATED"]
LensStatusType = Literal["CURRENT", "DEPRECATED", "NOT_CURRENT"]
NotificationTypeType = Literal["LENS_VERSION_DEPRECATED", "LENS_VERSION_UPGRADED"]
PermissionTypeType = Literal["CONTRIBUTOR", "READONLY"]
RiskType = Literal["HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE", "UNANSWERED"]
ShareInvitationActionType = Literal["ACCEPT", "REJECT"]
ShareStatusType = Literal["ACCEPTED", "EXPIRED", "PENDING", "REJECTED", "REVOKED"]
WorkloadEnvironmentType = Literal["PREPRODUCTION", "PRODUCTION"]
WorkloadImprovementStatusType = Literal[
    "COMPLETE", "IN_PROGRESS", "NOT_APPLICABLE", "NOT_STARTED", "RISK_ACKNOWLEDGED"
]
