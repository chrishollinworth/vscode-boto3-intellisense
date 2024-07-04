"""
Type annotations for macie2 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/literals.html)

Usage::

    ```python
    from mypy_boto3_macie2.literals import AdminStatusType

    data: AdminStatusType = "DISABLING_IN_PROGRESS"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AdminStatusType",
    "AllowListStatusCodeType",
    "AllowsUnencryptedObjectUploadsType",
    "AutoEnableModeType",
    "AutomatedDiscoveryAccountStatusType",
    "AutomatedDiscoveryAccountUpdateErrorCodeType",
    "AutomatedDiscoveryMonitoringStatusType",
    "AutomatedDiscoveryStatusType",
    "AvailabilityCodeType",
    "BucketMetadataErrorCodeType",
    "ClassificationScopeUpdateOperationType",
    "CurrencyType",
    "DataIdentifierSeverityType",
    "DataIdentifierTypeType",
    "DayOfWeekType",
    "DescribeBucketsPaginatorName",
    "EffectivePermissionType",
    "EncryptionTypeType",
    "ErrorCodeType",
    "FindingActionTypeType",
    "FindingCategoryType",
    "FindingPublishingFrequencyType",
    "FindingRevealedWaiterName",
    "FindingStatisticsSortAttributeNameType",
    "FindingTypeType",
    "FindingsFilterActionType",
    "GetUsageStatisticsPaginatorName",
    "GroupByType",
    "IsDefinedInJobType",
    "IsMonitoredByJobType",
    "JobComparatorType",
    "JobStatusType",
    "JobTypeType",
    "LastRunErrorStatusCodeType",
    "ListAllowListsPaginatorName",
    "ListAutomatedDiscoveryAccountsPaginatorName",
    "ListClassificationJobsPaginatorName",
    "ListClassificationScopesPaginatorName",
    "ListCustomDataIdentifiersPaginatorName",
    "ListFindingsFiltersPaginatorName",
    "ListFindingsPaginatorName",
    "ListInvitationsPaginatorName",
    "ListJobsFilterKeyType",
    "ListJobsSortAttributeNameType",
    "ListManagedDataIdentifiersPaginatorName",
    "ListMembersPaginatorName",
    "ListOrganizationAdminAccountsPaginatorName",
    "ListResourceProfileArtifactsPaginatorName",
    "ListResourceProfileDetectionsPaginatorName",
    "ListSensitivityInspectionTemplatesPaginatorName",
    "MacieStatusType",
    "ManagedDataIdentifierSelectorType",
    "OrderByType",
    "OriginTypeType",
    "RelationshipStatusType",
    "RetrievalModeType",
    "RevealRequestStatusType",
    "RevealStatusType",
    "ScopeFilterKeyType",
    "SearchResourcesComparatorType",
    "SearchResourcesPaginatorName",
    "SearchResourcesSimpleCriterionKeyType",
    "SearchResourcesSortAttributeNameType",
    "SensitiveDataItemCategoryType",
    "SeverityDescriptionType",
    "SharedAccessType",
    "SimpleCriterionKeyForJobType",
    "StorageClassType",
    "TagTargetType",
    "TimeRangeType",
    "TypeType",
    "UnavailabilityReasonCodeType",
    "UnitType",
    "UsageStatisticsFilterComparatorType",
    "UsageStatisticsFilterKeyType",
    "UsageStatisticsSortKeyType",
    "UsageTypeType",
    "UserIdentityTypeType",
)

AdminStatusType = Literal["DISABLING_IN_PROGRESS", "ENABLED"]
AllowListStatusCodeType = Literal[
    "OK",
    "S3_OBJECT_ACCESS_DENIED",
    "S3_OBJECT_EMPTY",
    "S3_OBJECT_NOT_FOUND",
    "S3_OBJECT_OVERSIZE",
    "S3_THROTTLED",
    "S3_USER_ACCESS_DENIED",
    "UNKNOWN_ERROR",
]
AllowsUnencryptedObjectUploadsType = Literal["FALSE", "TRUE", "UNKNOWN"]
AutoEnableModeType = Literal["ALL", "NEW", "NONE"]
AutomatedDiscoveryAccountStatusType = Literal["DISABLED", "ENABLED"]
AutomatedDiscoveryAccountUpdateErrorCodeType = Literal["ACCOUNT_NOT_FOUND", "ACCOUNT_PAUSED"]
AutomatedDiscoveryMonitoringStatusType = Literal["MONITORED", "NOT_MONITORED"]
AutomatedDiscoveryStatusType = Literal["DISABLED", "ENABLED"]
AvailabilityCodeType = Literal["AVAILABLE", "UNAVAILABLE"]
BucketMetadataErrorCodeType = Literal["ACCESS_DENIED"]
ClassificationScopeUpdateOperationType = Literal["ADD", "REMOVE", "REPLACE"]
CurrencyType = Literal["USD"]
DataIdentifierSeverityType = Literal["HIGH", "LOW", "MEDIUM"]
DataIdentifierTypeType = Literal["CUSTOM", "MANAGED"]
DayOfWeekType = Literal[
    "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
]
DescribeBucketsPaginatorName = Literal["describe_buckets"]
EffectivePermissionType = Literal["NOT_PUBLIC", "PUBLIC", "UNKNOWN"]
EncryptionTypeType = Literal["AES256", "NONE", "UNKNOWN", "aws:kms", "aws:kms:dsse"]
ErrorCodeType = Literal["ClientError", "InternalError"]
FindingActionTypeType = Literal["AWS_API_CALL"]
FindingCategoryType = Literal["CLASSIFICATION", "POLICY"]
FindingPublishingFrequencyType = Literal["FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"]
FindingRevealedWaiterName = Literal["finding_revealed"]
FindingStatisticsSortAttributeNameType = Literal["count", "groupKey"]
FindingTypeType = Literal[
    "Policy:IAMUser/S3BlockPublicAccessDisabled",
    "Policy:IAMUser/S3BucketEncryptionDisabled",
    "Policy:IAMUser/S3BucketPublic",
    "Policy:IAMUser/S3BucketReplicatedExternally",
    "Policy:IAMUser/S3BucketSharedExternally",
    "Policy:IAMUser/S3BucketSharedWithCloudFront",
    "SensitiveData:S3Object/Credentials",
    "SensitiveData:S3Object/CustomIdentifier",
    "SensitiveData:S3Object/Financial",
    "SensitiveData:S3Object/Multiple",
    "SensitiveData:S3Object/Personal",
]
FindingsFilterActionType = Literal["ARCHIVE", "NOOP"]
GetUsageStatisticsPaginatorName = Literal["get_usage_statistics"]
GroupByType = Literal[
    "classificationDetails.jobId", "resourcesAffected.s3Bucket.name", "severity.description", "type"
]
IsDefinedInJobType = Literal["FALSE", "TRUE", "UNKNOWN"]
IsMonitoredByJobType = Literal["FALSE", "TRUE", "UNKNOWN"]
JobComparatorType = Literal["CONTAINS", "EQ", "GT", "GTE", "LT", "LTE", "NE", "STARTS_WITH"]
JobStatusType = Literal["CANCELLED", "COMPLETE", "IDLE", "PAUSED", "RUNNING", "USER_PAUSED"]
JobTypeType = Literal["ONE_TIME", "SCHEDULED"]
LastRunErrorStatusCodeType = Literal["ERROR", "NONE"]
ListAllowListsPaginatorName = Literal["list_allow_lists"]
ListAutomatedDiscoveryAccountsPaginatorName = Literal["list_automated_discovery_accounts"]
ListClassificationJobsPaginatorName = Literal["list_classification_jobs"]
ListClassificationScopesPaginatorName = Literal["list_classification_scopes"]
ListCustomDataIdentifiersPaginatorName = Literal["list_custom_data_identifiers"]
ListFindingsFiltersPaginatorName = Literal["list_findings_filters"]
ListFindingsPaginatorName = Literal["list_findings"]
ListInvitationsPaginatorName = Literal["list_invitations"]
ListJobsFilterKeyType = Literal["createdAt", "jobStatus", "jobType", "name"]
ListJobsSortAttributeNameType = Literal["createdAt", "jobStatus", "jobType", "name"]
ListManagedDataIdentifiersPaginatorName = Literal["list_managed_data_identifiers"]
ListMembersPaginatorName = Literal["list_members"]
ListOrganizationAdminAccountsPaginatorName = Literal["list_organization_admin_accounts"]
ListResourceProfileArtifactsPaginatorName = Literal["list_resource_profile_artifacts"]
ListResourceProfileDetectionsPaginatorName = Literal["list_resource_profile_detections"]
ListSensitivityInspectionTemplatesPaginatorName = Literal["list_sensitivity_inspection_templates"]
MacieStatusType = Literal["ENABLED", "PAUSED"]
ManagedDataIdentifierSelectorType = Literal["ALL", "EXCLUDE", "INCLUDE", "NONE", "RECOMMENDED"]
OrderByType = Literal["ASC", "DESC"]
OriginTypeType = Literal["AUTOMATED_SENSITIVE_DATA_DISCOVERY", "SENSITIVE_DATA_DISCOVERY_JOB"]
RelationshipStatusType = Literal[
    "AccountSuspended",
    "Created",
    "EmailVerificationFailed",
    "EmailVerificationInProgress",
    "Enabled",
    "Invited",
    "Paused",
    "RegionDisabled",
    "Removed",
    "Resigned",
]
RetrievalModeType = Literal["ASSUME_ROLE", "CALLER_CREDENTIALS"]
RevealRequestStatusType = Literal["ERROR", "PROCESSING", "SUCCESS"]
RevealStatusType = Literal["DISABLED", "ENABLED"]
ScopeFilterKeyType = Literal[
    "OBJECT_EXTENSION", "OBJECT_KEY", "OBJECT_LAST_MODIFIED_DATE", "OBJECT_SIZE"
]
SearchResourcesComparatorType = Literal["EQ", "NE"]
SearchResourcesPaginatorName = Literal["search_resources"]
SearchResourcesSimpleCriterionKeyType = Literal[
    "ACCOUNT_ID",
    "AUTOMATED_DISCOVERY_MONITORING_STATUS",
    "S3_BUCKET_EFFECTIVE_PERMISSION",
    "S3_BUCKET_NAME",
    "S3_BUCKET_SHARED_ACCESS",
]
SearchResourcesSortAttributeNameType = Literal[
    "ACCOUNT_ID", "RESOURCE_NAME", "S3_CLASSIFIABLE_OBJECT_COUNT", "S3_CLASSIFIABLE_SIZE_IN_BYTES"
]
SensitiveDataItemCategoryType = Literal[
    "CREDENTIALS", "CUSTOM_IDENTIFIER", "FINANCIAL_INFORMATION", "PERSONAL_INFORMATION"
]
SeverityDescriptionType = Literal["High", "Low", "Medium"]
SharedAccessType = Literal["EXTERNAL", "INTERNAL", "NOT_SHARED", "UNKNOWN"]
SimpleCriterionKeyForJobType = Literal[
    "ACCOUNT_ID", "S3_BUCKET_EFFECTIVE_PERMISSION", "S3_BUCKET_NAME", "S3_BUCKET_SHARED_ACCESS"
]
StorageClassType = Literal[
    "DEEP_ARCHIVE",
    "GLACIER",
    "GLACIER_IR",
    "INTELLIGENT_TIERING",
    "ONEZONE_IA",
    "OUTPOSTS",
    "REDUCED_REDUNDANCY",
    "STANDARD",
    "STANDARD_IA",
]
TagTargetType = Literal["S3_OBJECT"]
TimeRangeType = Literal["MONTH_TO_DATE", "PAST_30_DAYS"]
TypeType = Literal["AES256", "NONE", "aws:kms", "aws:kms:dsse"]
UnavailabilityReasonCodeType = Literal[
    "ACCOUNT_NOT_IN_ORGANIZATION",
    "INVALID_CLASSIFICATION_RESULT",
    "INVALID_RESULT_SIGNATURE",
    "MEMBER_ROLE_TOO_PERMISSIVE",
    "MISSING_GET_MEMBER_PERMISSION",
    "OBJECT_EXCEEDS_SIZE_QUOTA",
    "OBJECT_UNAVAILABLE",
    "RESULT_NOT_SIGNED",
    "ROLE_TOO_PERMISSIVE",
    "UNSUPPORTED_FINDING_TYPE",
    "UNSUPPORTED_OBJECT_TYPE",
]
UnitType = Literal["TERABYTES"]
UsageStatisticsFilterComparatorType = Literal["CONTAINS", "EQ", "GT", "GTE", "LT", "LTE", "NE"]
UsageStatisticsFilterKeyType = Literal["accountId", "freeTrialStartDate", "serviceLimit", "total"]
UsageStatisticsSortKeyType = Literal[
    "accountId", "freeTrialStartDate", "serviceLimitValue", "total"
]
UsageTypeType = Literal[
    "AUTOMATED_OBJECT_MONITORING",
    "AUTOMATED_SENSITIVE_DATA_DISCOVERY",
    "DATA_INVENTORY_EVALUATION",
    "SENSITIVE_DATA_DISCOVERY",
]
UserIdentityTypeType = Literal[
    "AWSAccount", "AWSService", "AssumedRole", "FederatedUser", "IAMUser", "Root"
]
