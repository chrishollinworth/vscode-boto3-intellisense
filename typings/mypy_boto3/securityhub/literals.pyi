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
    "AssociationStatusType",
    "AutoEnableStandardsType",
    "AwsIamAccessKeyStatusType",
    "AwsS3BucketNotificationConfigurationS3KeyFilterRuleNameType",
    "ComplianceStatusType",
    "ControlFindingGeneratorType",
    "ControlStatusType",
    "DateRangeUnitType",
    "DescribeActionTargetsPaginatorName",
    "DescribeProductsPaginatorName",
    "DescribeStandardsControlsPaginatorName",
    "DescribeStandardsPaginatorName",
    "GetEnabledStandardsPaginatorName",
    "GetFindingsPaginatorName",
    "GetInsightsPaginatorName",
    "IntegrationTypeType",
    "ListEnabledProductsForImportPaginatorName",
    "ListFindingAggregatorsPaginatorName",
    "ListInvitationsPaginatorName",
    "ListMembersPaginatorName",
    "ListOrganizationAdminAccountsPaginatorName",
    "ListSecurityControlDefinitionsPaginatorName",
    "ListStandardsControlAssociationsPaginatorName",
    "MalwareStateType",
    "MalwareTypeType",
    "MapFilterComparisonType",
    "NetworkDirectionType",
    "PartitionType",
    "RecordStateType",
    "RegionAvailabilityStatusType",
    "SeverityLabelType",
    "SeverityRatingType",
    "SortOrderType",
    "StandardsStatusType",
    "StatusReasonCodeType",
    "StringFilterComparisonType",
    "ThreatIntelIndicatorCategoryType",
    "ThreatIntelIndicatorTypeType",
    "UnprocessedErrorCodeType",
    "VerificationStateType",
    "VulnerabilityFixAvailableType",
    "WorkflowStateType",
    "WorkflowStatusType",
)

AdminStatusType = Literal["DISABLE_IN_PROGRESS", "ENABLED"]
AssociationStatusType = Literal["DISABLED", "ENABLED"]
AutoEnableStandardsType = Literal["DEFAULT", "NONE"]
AwsIamAccessKeyStatusType = Literal["Active", "Inactive"]
AwsS3BucketNotificationConfigurationS3KeyFilterRuleNameType = Literal["Prefix", "Suffix"]
ComplianceStatusType = Literal["FAILED", "NOT_AVAILABLE", "PASSED", "WARNING"]
ControlFindingGeneratorType = Literal["SECURITY_CONTROL", "STANDARD_CONTROL"]
ControlStatusType = Literal["DISABLED", "ENABLED"]
DateRangeUnitType = Literal["DAYS"]
DescribeActionTargetsPaginatorName = Literal["describe_action_targets"]
DescribeProductsPaginatorName = Literal["describe_products"]
DescribeStandardsControlsPaginatorName = Literal["describe_standards_controls"]
DescribeStandardsPaginatorName = Literal["describe_standards"]
GetEnabledStandardsPaginatorName = Literal["get_enabled_standards"]
GetFindingsPaginatorName = Literal["get_findings"]
GetInsightsPaginatorName = Literal["get_insights"]
IntegrationTypeType = Literal[
    "RECEIVE_FINDINGS_FROM_SECURITY_HUB",
    "SEND_FINDINGS_TO_SECURITY_HUB",
    "UPDATE_FINDINGS_IN_SECURITY_HUB",
]
ListEnabledProductsForImportPaginatorName = Literal["list_enabled_products_for_import"]
ListFindingAggregatorsPaginatorName = Literal["list_finding_aggregators"]
ListInvitationsPaginatorName = Literal["list_invitations"]
ListMembersPaginatorName = Literal["list_members"]
ListOrganizationAdminAccountsPaginatorName = Literal["list_organization_admin_accounts"]
ListSecurityControlDefinitionsPaginatorName = Literal["list_security_control_definitions"]
ListStandardsControlAssociationsPaginatorName = Literal["list_standards_control_associations"]
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
RegionAvailabilityStatusType = Literal["AVAILABLE", "UNAVAILABLE"]
SeverityLabelType = Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM"]
SeverityRatingType = Literal["CRITICAL", "HIGH", "LOW", "MEDIUM"]
SortOrderType = Literal["asc", "desc"]
StandardsStatusType = Literal["DELETING", "FAILED", "INCOMPLETE", "PENDING", "READY"]
StatusReasonCodeType = Literal["INTERNAL_ERROR", "NO_AVAILABLE_CONFIGURATION_RECORDER"]
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
UnprocessedErrorCodeType = Literal["ACCESS_DENIED", "INVALID_INPUT", "LIMIT_EXCEEDED", "NOT_FOUND"]
VerificationStateType = Literal["BENIGN_POSITIVE", "FALSE_POSITIVE", "TRUE_POSITIVE", "UNKNOWN"]
VulnerabilityFixAvailableType = Literal["NO", "PARTIAL", "YES"]
WorkflowStateType = Literal["ASSIGNED", "DEFERRED", "IN_PROGRESS", "NEW", "RESOLVED"]
WorkflowStatusType = Literal["NEW", "NOTIFIED", "RESOLVED", "SUPPRESSED"]
