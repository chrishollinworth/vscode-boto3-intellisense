"""
Type annotations for guardduty service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/literals.html)

Usage::

    ```python
    from mypy_boto3_guardduty.literals import AdminStatusType

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
    "AutoEnableMembersType",
    "CoverageFilterCriterionKeyType",
    "CoverageSortKeyType",
    "CoverageStatisticsTypeType",
    "CoverageStatusType",
    "CriterionKeyType",
    "DataSourceStatusType",
    "DataSourceType",
    "DescribeMalwareScansPaginatorName",
    "DestinationTypeType",
    "DetectorFeatureResultType",
    "DetectorFeatureType",
    "DetectorStatusType",
    "EbsSnapshotPreservationType",
    "FeatureAdditionalConfigurationType",
    "FeatureStatusType",
    "FeedbackType",
    "FilterActionType",
    "FindingPublishingFrequencyType",
    "FindingStatisticTypeType",
    "FreeTrialFeatureResultType",
    "IpSetFormatType",
    "IpSetStatusType",
    "ListCoveragePaginatorName",
    "ListDetectorsPaginatorName",
    "ListFiltersPaginatorName",
    "ListFindingsPaginatorName",
    "ListIPSetsPaginatorName",
    "ListInvitationsPaginatorName",
    "ListMembersPaginatorName",
    "ListOrganizationAdminAccountsPaginatorName",
    "ListThreatIntelSetsPaginatorName",
    "ManagementTypeType",
    "OrderByType",
    "OrgFeatureAdditionalConfigurationType",
    "OrgFeatureStatusType",
    "OrgFeatureType",
    "ProfileSubtypeType",
    "ProfileTypeType",
    "PublishingStatusType",
    "ResourceTypeType",
    "ScanCriterionKeyType",
    "ScanResultType",
    "ScanStatusType",
    "ScanTypeType",
    "ThreatIntelSetFormatType",
    "ThreatIntelSetStatusType",
    "UsageFeatureType",
    "UsageStatisticTypeType",
)

AdminStatusType = Literal["DISABLE_IN_PROGRESS", "ENABLED"]
AutoEnableMembersType = Literal["ALL", "NEW", "NONE"]
CoverageFilterCriterionKeyType = Literal[
    "ACCOUNT_ID",
    "ADDON_VERSION",
    "AGENT_VERSION",
    "CLUSTER_ARN",
    "CLUSTER_NAME",
    "COVERAGE_STATUS",
    "ECS_CLUSTER_NAME",
    "EKS_CLUSTER_NAME",
    "INSTANCE_ID",
    "MANAGEMENT_TYPE",
    "RESOURCE_TYPE",
]
CoverageSortKeyType = Literal[
    "ACCOUNT_ID",
    "ADDON_VERSION",
    "CLUSTER_NAME",
    "COVERAGE_STATUS",
    "ECS_CLUSTER_NAME",
    "EKS_CLUSTER_NAME",
    "INSTANCE_ID",
    "ISSUE",
    "UPDATED_AT",
]
CoverageStatisticsTypeType = Literal["COUNT_BY_COVERAGE_STATUS", "COUNT_BY_RESOURCE_TYPE"]
CoverageStatusType = Literal["HEALTHY", "UNHEALTHY"]
CriterionKeyType = Literal[
    "ACCOUNT_ID",
    "EC2_INSTANCE_ARN",
    "GUARDDUTY_FINDING_ID",
    "SCAN_ID",
    "SCAN_START_TIME",
    "SCAN_STATUS",
    "SCAN_TYPE",
]
DataSourceStatusType = Literal["DISABLED", "ENABLED"]
DataSourceType = Literal[
    "CLOUD_TRAIL", "DNS_LOGS", "EC2_MALWARE_SCAN", "FLOW_LOGS", "KUBERNETES_AUDIT_LOGS", "S3_LOGS"
]
DescribeMalwareScansPaginatorName = Literal["describe_malware_scans"]
DestinationTypeType = Literal["S3"]
DetectorFeatureResultType = Literal[
    "CLOUD_TRAIL",
    "DNS_LOGS",
    "EBS_MALWARE_PROTECTION",
    "EKS_AUDIT_LOGS",
    "EKS_RUNTIME_MONITORING",
    "FLOW_LOGS",
    "LAMBDA_NETWORK_LOGS",
    "RDS_LOGIN_EVENTS",
    "RUNTIME_MONITORING",
    "S3_DATA_EVENTS",
]
DetectorFeatureType = Literal[
    "EBS_MALWARE_PROTECTION",
    "EKS_AUDIT_LOGS",
    "EKS_RUNTIME_MONITORING",
    "LAMBDA_NETWORK_LOGS",
    "RDS_LOGIN_EVENTS",
    "RUNTIME_MONITORING",
    "S3_DATA_EVENTS",
]
DetectorStatusType = Literal["DISABLED", "ENABLED"]
EbsSnapshotPreservationType = Literal["NO_RETENTION", "RETENTION_WITH_FINDING"]
FeatureAdditionalConfigurationType = Literal[
    "EC2_AGENT_MANAGEMENT", "ECS_FARGATE_AGENT_MANAGEMENT", "EKS_ADDON_MANAGEMENT"
]
FeatureStatusType = Literal["DISABLED", "ENABLED"]
FeedbackType = Literal["NOT_USEFUL", "USEFUL"]
FilterActionType = Literal["ARCHIVE", "NOOP"]
FindingPublishingFrequencyType = Literal["FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"]
FindingStatisticTypeType = Literal["COUNT_BY_SEVERITY"]
FreeTrialFeatureResultType = Literal[
    "CLOUD_TRAIL",
    "DNS_LOGS",
    "EBS_MALWARE_PROTECTION",
    "EC2_RUNTIME_MONITORING",
    "EKS_AUDIT_LOGS",
    "EKS_RUNTIME_MONITORING",
    "FARGATE_RUNTIME_MONITORING",
    "FLOW_LOGS",
    "LAMBDA_NETWORK_LOGS",
    "RDS_LOGIN_EVENTS",
    "S3_DATA_EVENTS",
]
IpSetFormatType = Literal["ALIEN_VAULT", "FIRE_EYE", "OTX_CSV", "PROOF_POINT", "STIX", "TXT"]
IpSetStatusType = Literal[
    "ACTIVATING", "ACTIVE", "DEACTIVATING", "DELETED", "DELETE_PENDING", "ERROR", "INACTIVE"
]
ListCoveragePaginatorName = Literal["list_coverage"]
ListDetectorsPaginatorName = Literal["list_detectors"]
ListFiltersPaginatorName = Literal["list_filters"]
ListFindingsPaginatorName = Literal["list_findings"]
ListIPSetsPaginatorName = Literal["list_ip_sets"]
ListInvitationsPaginatorName = Literal["list_invitations"]
ListMembersPaginatorName = Literal["list_members"]
ListOrganizationAdminAccountsPaginatorName = Literal["list_organization_admin_accounts"]
ListThreatIntelSetsPaginatorName = Literal["list_threat_intel_sets"]
ManagementTypeType = Literal["AUTO_MANAGED", "DISABLED", "MANUAL"]
OrderByType = Literal["ASC", "DESC"]
OrgFeatureAdditionalConfigurationType = Literal[
    "EC2_AGENT_MANAGEMENT", "ECS_FARGATE_AGENT_MANAGEMENT", "EKS_ADDON_MANAGEMENT"
]
OrgFeatureStatusType = Literal["ALL", "NEW", "NONE"]
OrgFeatureType = Literal[
    "EBS_MALWARE_PROTECTION",
    "EKS_AUDIT_LOGS",
    "EKS_RUNTIME_MONITORING",
    "LAMBDA_NETWORK_LOGS",
    "RDS_LOGIN_EVENTS",
    "RUNTIME_MONITORING",
    "S3_DATA_EVENTS",
]
ProfileSubtypeType = Literal["FREQUENT", "INFREQUENT", "RARE", "UNSEEN"]
ProfileTypeType = Literal["FREQUENCY"]
PublishingStatusType = Literal[
    "PENDING_VERIFICATION", "PUBLISHING", "STOPPED", "UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY"
]
ResourceTypeType = Literal["EC2", "ECS", "EKS"]
ScanCriterionKeyType = Literal["EC2_INSTANCE_TAG"]
ScanResultType = Literal["CLEAN", "INFECTED"]
ScanStatusType = Literal["COMPLETED", "FAILED", "RUNNING", "SKIPPED"]
ScanTypeType = Literal["GUARDDUTY_INITIATED", "ON_DEMAND"]
ThreatIntelSetFormatType = Literal[
    "ALIEN_VAULT", "FIRE_EYE", "OTX_CSV", "PROOF_POINT", "STIX", "TXT"
]
ThreatIntelSetStatusType = Literal[
    "ACTIVATING", "ACTIVE", "DEACTIVATING", "DELETED", "DELETE_PENDING", "ERROR", "INACTIVE"
]
UsageFeatureType = Literal[
    "CLOUD_TRAIL",
    "DNS_LOGS",
    "EBS_MALWARE_PROTECTION",
    "EC2_RUNTIME_MONITORING",
    "EKS_AUDIT_LOGS",
    "EKS_RUNTIME_MONITORING",
    "FARGATE_RUNTIME_MONITORING",
    "FLOW_LOGS",
    "LAMBDA_NETWORK_LOGS",
    "RDS_DBI_PROTECTION_PROVISIONED",
    "RDS_DBI_PROTECTION_SERVERLESS",
    "RDS_LOGIN_EVENTS",
    "S3_DATA_EVENTS",
]
UsageStatisticTypeType = Literal[
    "SUM_BY_ACCOUNT",
    "SUM_BY_DATA_SOURCE",
    "SUM_BY_FEATURES",
    "SUM_BY_RESOURCE",
    "TOP_ACCOUNTS_BY_FEATURE",
    "TOP_RESOURCES",
]
