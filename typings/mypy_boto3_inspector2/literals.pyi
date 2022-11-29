"""
Type annotations for inspector2 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/literals.html)

Usage::

    ```python
    from mypy_boto3_inspector2.literals import AccountSortByType

    data: AccountSortByType = "ALL"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccountSortByType",
    "AggregationFindingTypeType",
    "AggregationResourceTypeType",
    "AggregationTypeType",
    "AmiSortByType",
    "ArchitectureType",
    "AwsEcrContainerSortByType",
    "CoverageMapComparisonType",
    "CoverageResourceTypeType",
    "CoverageStringComparisonType",
    "CurrencyType",
    "DelegatedAdminStatusType",
    "Ec2InstanceSortByType",
    "Ec2PlatformType",
    "EcrRescanDurationStatusType",
    "EcrRescanDurationType",
    "EcrScanFrequencyType",
    "ErrorCodeType",
    "ExploitAvailableType",
    "ExternalReportStatusType",
    "FilterActionType",
    "FindingStatusType",
    "FindingTypeSortByType",
    "FindingTypeType",
    "FixAvailableType",
    "FreeTrialInfoErrorCodeType",
    "FreeTrialStatusType",
    "FreeTrialTypeType",
    "GroupKeyType",
    "ImageLayerSortByType",
    "LambdaFunctionSortByType",
    "LambdaLayerSortByType",
    "ListAccountPermissionsPaginatorName",
    "ListCoveragePaginatorName",
    "ListCoverageStatisticsPaginatorName",
    "ListDelegatedAdminAccountsPaginatorName",
    "ListFiltersPaginatorName",
    "ListFindingAggregationsPaginatorName",
    "ListFindingsPaginatorName",
    "ListMembersPaginatorName",
    "ListUsageTotalsPaginatorName",
    "MapComparisonType",
    "NetworkProtocolType",
    "OperationType",
    "PackageManagerType",
    "PackageSortByType",
    "PackageTypeType",
    "RelationshipStatusType",
    "ReportFormatType",
    "ReportingErrorCodeType",
    "RepositorySortByType",
    "ResourceScanTypeType",
    "ResourceTypeType",
    "RuntimeType",
    "ScanStatusCodeType",
    "ScanStatusReasonType",
    "ScanTypeType",
    "ServiceType",
    "SeverityType",
    "SortFieldType",
    "SortOrderType",
    "StatusType",
    "StringComparisonType",
    "TitleSortByType",
    "UsageTypeType",
)

AccountSortByType = Literal["ALL", "CRITICAL", "HIGH"]
AggregationFindingTypeType = Literal["NETWORK_REACHABILITY", "PACKAGE_VULNERABILITY"]
AggregationResourceTypeType = Literal[
    "AWS_EC2_INSTANCE", "AWS_ECR_CONTAINER_IMAGE", "AWS_LAMBDA_FUNCTION"
]
AggregationTypeType = Literal[
    "ACCOUNT",
    "AMI",
    "AWS_EC2_INSTANCE",
    "AWS_ECR_CONTAINER",
    "AWS_LAMBDA_FUNCTION",
    "FINDING_TYPE",
    "IMAGE_LAYER",
    "LAMBDA_LAYER",
    "PACKAGE",
    "REPOSITORY",
    "TITLE",
]
AmiSortByType = Literal["AFFECTED_INSTANCES", "ALL", "CRITICAL", "HIGH"]
ArchitectureType = Literal["ARM64", "X86_64"]
AwsEcrContainerSortByType = Literal["ALL", "CRITICAL", "HIGH"]
CoverageMapComparisonType = Literal["EQUALS"]
CoverageResourceTypeType = Literal[
    "AWS_EC2_INSTANCE", "AWS_ECR_CONTAINER_IMAGE", "AWS_ECR_REPOSITORY", "AWS_LAMBDA_FUNCTION"
]
CoverageStringComparisonType = Literal["EQUALS", "NOT_EQUALS"]
CurrencyType = Literal["USD"]
DelegatedAdminStatusType = Literal["DISABLE_IN_PROGRESS", "ENABLED"]
Ec2InstanceSortByType = Literal["ALL", "CRITICAL", "HIGH", "NETWORK_FINDINGS"]
Ec2PlatformType = Literal["LINUX", "UNKNOWN", "WINDOWS"]
EcrRescanDurationStatusType = Literal["FAILED", "PENDING", "SUCCESS"]
EcrRescanDurationType = Literal["DAYS_180", "DAYS_30", "LIFETIME"]
EcrScanFrequencyType = Literal["CONTINUOUS_SCAN", "MANUAL", "SCAN_ON_PUSH"]
ErrorCodeType = Literal[
    "ACCESS_DENIED",
    "ACCOUNT_IS_ISOLATED",
    "ALREADY_ENABLED",
    "DISABLE_IN_PROGRESS",
    "DISASSOCIATE_ALL_MEMBERS",
    "ENABLE_IN_PROGRESS",
    "EVENTBRIDGE_THROTTLED",
    "EVENTBRIDGE_UNAVAILABLE",
    "INTERNAL_ERROR",
    "RESOURCE_NOT_FOUND",
    "RESOURCE_SCAN_NOT_DISABLED",
    "SSM_THROTTLED",
    "SSM_UNAVAILABLE",
    "SUSPEND_IN_PROGRESS",
]
ExploitAvailableType = Literal["NO", "YES"]
ExternalReportStatusType = Literal["CANCELLED", "FAILED", "IN_PROGRESS", "SUCCEEDED"]
FilterActionType = Literal["NONE", "SUPPRESS"]
FindingStatusType = Literal["ACTIVE", "CLOSED", "SUPPRESSED"]
FindingTypeSortByType = Literal["ALL", "CRITICAL", "HIGH"]
FindingTypeType = Literal["NETWORK_REACHABILITY", "PACKAGE_VULNERABILITY"]
FixAvailableType = Literal["NO", "PARTIAL", "YES"]
FreeTrialInfoErrorCodeType = Literal["ACCESS_DENIED", "INTERNAL_ERROR"]
FreeTrialStatusType = Literal["ACTIVE", "INACTIVE"]
FreeTrialTypeType = Literal["EC2", "ECR", "LAMBDA"]
GroupKeyType = Literal[
    "ACCOUNT_ID", "ECR_REPOSITORY_NAME", "RESOURCE_TYPE", "SCAN_STATUS_CODE", "SCAN_STATUS_REASON"
]
ImageLayerSortByType = Literal["ALL", "CRITICAL", "HIGH"]
LambdaFunctionSortByType = Literal["ALL", "CRITICAL", "HIGH"]
LambdaLayerSortByType = Literal["ALL", "CRITICAL", "HIGH"]
ListAccountPermissionsPaginatorName = Literal["list_account_permissions"]
ListCoveragePaginatorName = Literal["list_coverage"]
ListCoverageStatisticsPaginatorName = Literal["list_coverage_statistics"]
ListDelegatedAdminAccountsPaginatorName = Literal["list_delegated_admin_accounts"]
ListFiltersPaginatorName = Literal["list_filters"]
ListFindingAggregationsPaginatorName = Literal["list_finding_aggregations"]
ListFindingsPaginatorName = Literal["list_findings"]
ListMembersPaginatorName = Literal["list_members"]
ListUsageTotalsPaginatorName = Literal["list_usage_totals"]
MapComparisonType = Literal["EQUALS"]
NetworkProtocolType = Literal["TCP", "UDP"]
OperationType = Literal[
    "DISABLE_REPOSITORY", "DISABLE_SCANNING", "ENABLE_REPOSITORY", "ENABLE_SCANNING"
]
PackageManagerType = Literal[
    "BUNDLER",
    "CARGO",
    "COMPOSER",
    "GOBINARY",
    "GOMOD",
    "JAR",
    "NODEPKG",
    "NPM",
    "NUGET",
    "OS",
    "PIP",
    "PIPENV",
    "POETRY",
    "POM",
    "PYTHONPKG",
    "YARN",
]
PackageSortByType = Literal["ALL", "CRITICAL", "HIGH"]
PackageTypeType = Literal["IMAGE", "ZIP"]
RelationshipStatusType = Literal[
    "ACCOUNT_SUSPENDED",
    "CANNOT_CREATE_DETECTOR_IN_ORG_MASTER",
    "CREATED",
    "DELETED",
    "DISABLED",
    "EMAIL_VERIFICATION_FAILED",
    "EMAIL_VERIFICATION_IN_PROGRESS",
    "ENABLED",
    "INVITED",
    "REGION_DISABLED",
    "REMOVED",
    "RESIGNED",
]
ReportFormatType = Literal["CSV", "JSON"]
ReportingErrorCodeType = Literal[
    "BUCKET_NOT_FOUND",
    "INCOMPATIBLE_BUCKET_REGION",
    "INTERNAL_ERROR",
    "INVALID_PERMISSIONS",
    "MALFORMED_KMS_KEY",
    "NO_FINDINGS_FOUND",
]
RepositorySortByType = Literal["AFFECTED_IMAGES", "ALL", "CRITICAL", "HIGH"]
ResourceScanTypeType = Literal["EC2", "ECR", "LAMBDA"]
ResourceTypeType = Literal[
    "AWS_EC2_INSTANCE", "AWS_ECR_CONTAINER_IMAGE", "AWS_ECR_REPOSITORY", "AWS_LAMBDA_FUNCTION"
]
RuntimeType = Literal[
    "JAVA_11",
    "JAVA_8",
    "JAVA_8_AL2",
    "NODEJS",
    "NODEJS_12_X",
    "NODEJS_14_X",
    "NODEJS_16_X",
    "PYTHON_3_7",
    "PYTHON_3_8",
    "PYTHON_3_9",
    "UNSUPPORTED",
]
ScanStatusCodeType = Literal["ACTIVE", "INACTIVE"]
ScanStatusReasonType = Literal[
    "ACCESS_DENIED",
    "EC2_INSTANCE_STOPPED",
    "EXCLUDED_BY_TAG",
    "IMAGE_SIZE_EXCEEDED",
    "INTERNAL_ERROR",
    "NO_INVENTORY",
    "NO_RESOURCES_FOUND",
    "PENDING_DISABLE",
    "PENDING_INITIAL_SCAN",
    "RESOURCE_TERMINATED",
    "SCAN_ELIGIBILITY_EXPIRED",
    "SCAN_FREQUENCY_MANUAL",
    "SCAN_FREQUENCY_SCAN_ON_PUSH",
    "STALE_INVENTORY",
    "SUCCESSFUL",
    "UNMANAGED_EC2_INSTANCE",
    "UNSUPPORTED_OS",
    "UNSUPPORTED_RUNTIME",
]
ScanTypeType = Literal["NETWORK", "PACKAGE"]
ServiceType = Literal["EC2", "ECR", "LAMBDA"]
SeverityType = Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNTRIAGED"]
SortFieldType = Literal[
    "AWS_ACCOUNT_ID",
    "COMPONENT_TYPE",
    "ECR_IMAGE_PUSHED_AT",
    "ECR_IMAGE_REGISTRY",
    "ECR_IMAGE_REPOSITORY_NAME",
    "FINDING_STATUS",
    "FINDING_TYPE",
    "FIRST_OBSERVED_AT",
    "INSPECTOR_SCORE",
    "LAST_OBSERVED_AT",
    "NETWORK_PROTOCOL",
    "RESOURCE_TYPE",
    "SEVERITY",
    "VENDOR_SEVERITY",
    "VULNERABILITY_ID",
    "VULNERABILITY_SOURCE",
]
SortOrderType = Literal["ASC", "DESC"]
StatusType = Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING", "SUSPENDED", "SUSPENDING"]
StringComparisonType = Literal["EQUALS", "NOT_EQUALS", "PREFIX"]
TitleSortByType = Literal["ALL", "CRITICAL", "HIGH"]
UsageTypeType = Literal[
    "EC2_INSTANCE_HOURS", "ECR_INITIAL_SCAN", "ECR_RESCAN", "LAMBDA_FUNCTION_HOURS"
]
