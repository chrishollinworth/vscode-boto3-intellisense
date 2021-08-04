"""
Type annotations for auditmanager service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/literals.html)

Usage::

    ```python
    from mypy_boto3_auditmanager.literals import AccountStatusType

    data: AccountStatusType = "ACTIVE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccountStatusType",
    "ActionEnumType",
    "AssessmentReportDestinationTypeType",
    "AssessmentReportStatusType",
    "AssessmentStatusType",
    "ControlResponseType",
    "ControlSetStatusType",
    "ControlStatusType",
    "ControlTypeType",
    "DelegationStatusType",
    "FrameworkTypeType",
    "KeywordInputTypeType",
    "ObjectTypeEnumType",
    "RoleTypeType",
    "SettingAttributeType",
    "SourceFrequencyType",
    "SourceSetUpOptionType",
    "SourceTypeType",
)

AccountStatusType = Literal["ACTIVE", "INACTIVE", "PENDING_ACTIVATION"]
ActionEnumType = Literal[
    "ACTIVE",
    "CREATE",
    "DELETE",
    "IMPORT_EVIDENCE",
    "INACTIVE",
    "REVIEWED",
    "UNDER_REVIEW",
    "UPDATE_METADATA",
]
AssessmentReportDestinationTypeType = Literal["S3"]
AssessmentReportStatusType = Literal["COMPLETE", "FAILED", "IN_PROGRESS"]
AssessmentStatusType = Literal["ACTIVE", "INACTIVE"]
ControlResponseType = Literal["AUTOMATE", "DEFER", "IGNORE", "MANUAL"]
ControlSetStatusType = Literal["ACTIVE", "REVIEWED", "UNDER_REVIEW"]
ControlStatusType = Literal["INACTIVE", "REVIEWED", "UNDER_REVIEW"]
ControlTypeType = Literal["Custom", "Standard"]
DelegationStatusType = Literal["COMPLETE", "IN_PROGRESS", "UNDER_REVIEW"]
FrameworkTypeType = Literal["Custom", "Standard"]
KeywordInputTypeType = Literal["SELECT_FROM_LIST"]
ObjectTypeEnumType = Literal[
    "ASSESSMENT", "ASSESSMENT_REPORT", "CONTROL", "CONTROL_SET", "DELEGATION"
]
RoleTypeType = Literal["PROCESS_OWNER", "RESOURCE_OWNER"]
SettingAttributeType = Literal[
    "ALL",
    "DEFAULT_ASSESSMENT_REPORTS_DESTINATION",
    "DEFAULT_PROCESS_OWNERS",
    "IS_AWS_ORG_ENABLED",
    "SNS_TOPIC",
]
SourceFrequencyType = Literal["DAILY", "MONTHLY", "WEEKLY"]
SourceSetUpOptionType = Literal["Procedural_Controls_Mapping", "System_Controls_Mapping"]
SourceTypeType = Literal[
    "AWS_API_Call", "AWS_Cloudtrail", "AWS_Config", "AWS_Security_Hub", "MANUAL"
]
