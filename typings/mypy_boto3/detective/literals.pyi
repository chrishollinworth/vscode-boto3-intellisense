"""
Type annotations for detective service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/literals.html)

Usage::

    ```python
    from mypy_boto3_detective.literals import DatasourcePackageIngestStateType

    data: DatasourcePackageIngestStateType = "DISABLED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DatasourcePackageIngestStateType",
    "DatasourcePackageType",
    "EntityTypeType",
    "FieldType",
    "IndicatorTypeType",
    "InvitationTypeType",
    "MemberDisabledReasonType",
    "MemberStatusType",
    "ReasonType",
    "SeverityType",
    "SortOrderType",
    "StateType",
    "StatusType",
)

DatasourcePackageIngestStateType = Literal["DISABLED", "STARTED", "STOPPED"]
DatasourcePackageType = Literal["ASFF_SECURITYHUB_FINDING", "DETECTIVE_CORE", "EKS_AUDIT"]
EntityTypeType = Literal["IAM_ROLE", "IAM_USER"]
FieldType = Literal["CREATED_TIME", "SEVERITY", "STATUS"]
IndicatorTypeType = Literal[
    "FLAGGED_IP_ADDRESS",
    "IMPOSSIBLE_TRAVEL",
    "NEW_ASO",
    "NEW_GEOLOCATION",
    "NEW_USER_AGENT",
    "RELATED_FINDING",
    "RELATED_FINDING_GROUP",
    "TTP_OBSERVED",
]
InvitationTypeType = Literal["INVITATION", "ORGANIZATION"]
MemberDisabledReasonType = Literal["VOLUME_TOO_HIGH", "VOLUME_UNKNOWN"]
MemberStatusType = Literal[
    "ACCEPTED_BUT_DISABLED", "ENABLED", "INVITED", "VERIFICATION_FAILED", "VERIFICATION_IN_PROGRESS"
]
ReasonType = Literal["AWS_THREAT_INTELLIGENCE"]
SeverityType = Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM"]
SortOrderType = Literal["ASC", "DESC"]
StateType = Literal["ACTIVE", "ARCHIVED"]
StatusType = Literal["FAILED", "RUNNING", "SUCCESSFUL"]
