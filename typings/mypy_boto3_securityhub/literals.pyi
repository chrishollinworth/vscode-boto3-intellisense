"""
Type annotations for securityhub service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/literals.html)

Usage::

    ```python
    from mypy_boto3_securityhub.literals import AdminStatusType

    data: AdminStatusType = "DISABLE_IN_PROGRESS"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AdminStatusType",
    "AwsIamAccessKeyStatusType",
    "ComplianceStatusType",
    "ControlStatusType",
    "DateRangeUnitType",
    "GetEnabledStandardsPaginatorName",
    "GetFindingsPaginatorName",
    "GetInsightsPaginatorName",
    "IntegrationTypeType",
    "ListEnabledProductsForImportPaginatorName",
    "ListInvitationsPaginatorName",
    "ListMembersPaginatorName",
    "MalwareStateType",
    "MalwareTypeType",
    "MapFilterComparisonType",
    "NetworkDirectionType",
    "PartitionType",
    "RecordStateType",
    "SeverityLabelType",
    "SeverityRatingType",
    "SortOrderType",
    "StandardsStatusType",
    "StringFilterComparisonType",
    "ThreatIntelIndicatorCategoryType",
    "ThreatIntelIndicatorTypeType",
    "VerificationStateType",
    "WorkflowStateType",
    "WorkflowStatusType",
)

AdminStatusType = Literal["DISABLE_IN_PROGRESS", "ENABLED"]
AwsIamAccessKeyStatusType = Literal["Active", "Inactive"]
ComplianceStatusType = Literal["FAILED", "NOT_AVAILABLE", "PASSED", "WARNING"]
ControlStatusType = Literal["DISABLED", "ENABLED"]
DateRangeUnitType = Literal["DAYS"]
GetEnabledStandardsPaginatorName = Literal["get_enabled_standards"]
GetFindingsPaginatorName = Literal["get_findings"]
GetInsightsPaginatorName = Literal["get_insights"]
IntegrationTypeType = Literal[
    "RECEIVE_FINDINGS_FROM_SECURITY_HUB",
    "SEND_FINDINGS_TO_SECURITY_HUB",
    "UPDATE_FINDINGS_IN_SECURITY_HUB",
]
ListEnabledProductsForImportPaginatorName = Literal["list_enabled_products_for_import"]
ListInvitationsPaginatorName = Literal["list_invitations"]
ListMembersPaginatorName = Literal["list_members"]
MalwareStateType = Literal["OBSERVED", "REMOVAL_FAILED", "REMOVED"]
MalwareTypeType = Literal[
    "ADWARE",
    "BLENDED_THREAT",
    "BOTNET_AGENT",
    "COIN_MINER",
    "EXPLOIT_KIT",
    "KEYLOGGER",
    "MACRO",
    "POTENTIALLY_UNWANTED",
    "RANSOMWARE",
    "REMOTE_ACCESS",
    "ROOTKIT",
    "SPYWARE",
    "TROJAN",
    "VIRUS",
    "WORM",
]
MapFilterComparisonType = Literal["EQUALS", "NOT_EQUALS"]
NetworkDirectionType = Literal["IN", "OUT"]
PartitionType = Literal["aws", "aws-cn", "aws-us-gov"]
RecordStateType = Literal["ACTIVE", "ARCHIVED"]
SeverityLabelType = Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM"]
SeverityRatingType = Literal["CRITICAL", "HIGH", "LOW", "MEDIUM"]
SortOrderType = Literal["asc", "desc"]
StandardsStatusType = Literal["DELETING", "FAILED", "INCOMPLETE", "PENDING", "READY"]
StringFilterComparisonType = Literal["EQUALS", "NOT_EQUALS", "PREFIX", "PREFIX_NOT_EQUALS"]
ThreatIntelIndicatorCategoryType = Literal[
    "BACKDOOR", "CARD_STEALER", "COMMAND_AND_CONTROL", "DROP_SITE", "EXPLOIT_SITE", "KEYLOGGER"
]
ThreatIntelIndicatorTypeType = Literal[
    "DOMAIN",
    "EMAIL_ADDRESS",
    "HASH_MD5",
    "HASH_SHA1",
    "HASH_SHA256",
    "HASH_SHA512",
    "IPV4_ADDRESS",
    "IPV6_ADDRESS",
    "MUTEX",
    "PROCESS",
    "URL",
]
VerificationStateType = Literal["BENIGN_POSITIVE", "FALSE_POSITIVE", "TRUE_POSITIVE", "UNKNOWN"]
WorkflowStateType = Literal["ASSIGNED", "DEFERRED", "IN_PROGRESS", "NEW", "RESOLVED"]
WorkflowStatusType = Literal["NEW", "NOTIFIED", "RESOLVED", "SUPPRESSED"]
