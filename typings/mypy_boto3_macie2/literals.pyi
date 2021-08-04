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
    "AllowsUnencryptedObjectUploadsType",
    "CurrencyType",
    "DayOfWeekType",
    "DescribeBucketsPaginatorName",
    "EffectivePermissionType",
    "EncryptionTypeType",
    "ErrorCodeType",
    "FindingActionTypeType",
    "FindingCategoryType",
    "FindingPublishingFrequencyType",
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
    "ListClassificationJobsPaginatorName",
    "ListCustomDataIdentifiersPaginatorName",
    "ListFindingsFiltersPaginatorName",
    "ListFindingsPaginatorName",
    "ListInvitationsPaginatorName",
    "ListJobsFilterKeyType",
    "ListJobsSortAttributeNameType",
    "ListMembersPaginatorName",
    "ListOrganizationAdminAccountsPaginatorName",
    "MacieStatusType",
    "OrderByType",
    "RelationshipStatusType",
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
    "UnitType",
    "UsageStatisticsFilterComparatorType",
    "UsageStatisticsFilterKeyType",
    "UsageStatisticsSortKeyType",
    "UsageTypeType",
    "UserIdentityTypeType",
)

AdminStatusType = Literal["DISABLING_IN_PROGRESS", "ENABLED"]
AllowsUnencryptedObjectUploadsType = Literal["FALSE", "TRUE", "UNKNOWN"]
CurrencyType = Literal["USD"]
DayOfWeekType = Literal[
    "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
]
DescribeBucketsPaginatorName = Literal["describe_buckets"]
EffectivePermissionType = Literal["NOT_PUBLIC", "PUBLIC", "UNKNOWN"]
EncryptionTypeType = Literal["AES256", "NONE", "UNKNOWN", "aws:kms"]
ErrorCodeType = Literal["ClientError", "InternalError"]
FindingActionTypeType = Literal["AWS_API_CALL"]
FindingCategoryType = Literal["CLASSIFICATION", "POLICY"]
FindingPublishingFrequencyType = Literal["FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"]
FindingStatisticsSortAttributeNameType = Literal["count", "groupKey"]
FindingTypeType = Literal[
    "Policy:IAMUser/S3BlockPublicAccessDisabled",
    "Policy:IAMUser/S3BucketEncryptionDisabled",
    "Policy:IAMUser/S3BucketPublic",
    "Policy:IAMUser/S3BucketReplicatedExternally",
    "Policy:IAMUser/S3BucketSharedExternally",
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
ListClassificationJobsPaginatorName = Literal["list_classification_jobs"]
ListCustomDataIdentifiersPaginatorName = Literal["list_custom_data_identifiers"]
ListFindingsFiltersPaginatorName = Literal["list_findings_filters"]
ListFindingsPaginatorName = Literal["list_findings"]
ListInvitationsPaginatorName = Literal["list_invitations"]
ListJobsFilterKeyType = Literal["createdAt", "jobStatus", "jobType", "name"]
ListJobsSortAttributeNameType = Literal["createdAt", "jobStatus", "jobType", "name"]
ListMembersPaginatorName = Literal["list_members"]
ListOrganizationAdminAccountsPaginatorName = Literal["list_organization_admin_accounts"]
MacieStatusType = Literal["ENABLED", "PAUSED"]
OrderByType = Literal["ASC", "DESC"]
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
ScopeFilterKeyType = Literal[
    "OBJECT_EXTENSION", "OBJECT_KEY", "OBJECT_LAST_MODIFIED_DATE", "OBJECT_SIZE"
]
SearchResourcesComparatorType = Literal["EQ", "NE"]
SearchResourcesPaginatorName = Literal["search_resources"]
SearchResourcesSimpleCriterionKeyType = Literal[
    "ACCOUNT_ID", "S3_BUCKET_EFFECTIVE_PERMISSION", "S3_BUCKET_NAME", "S3_BUCKET_SHARED_ACCESS"
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
    "INTELLIGENT_TIERING",
    "ONEZONE_IA",
    "REDUCED_REDUNDANCY",
    "STANDARD",
    "STANDARD_IA",
]
TagTargetType = Literal["S3_OBJECT"]
TimeRangeType = Literal["MONTH_TO_DATE", "PAST_30_DAYS"]
TypeType = Literal["AES256", "NONE", "aws:kms"]
UnitType = Literal["TERABYTES"]
UsageStatisticsFilterComparatorType = Literal["CONTAINS", "EQ", "GT", "GTE", "LT", "LTE", "NE"]
UsageStatisticsFilterKeyType = Literal["accountId", "freeTrialStartDate", "serviceLimit", "total"]
UsageStatisticsSortKeyType = Literal[
    "accountId", "freeTrialStartDate", "serviceLimitValue", "total"
]
UsageTypeType = Literal["DATA_INVENTORY_EVALUATION", "SENSITIVE_DATA_DISCOVERY"]
UserIdentityTypeType = Literal[
    "AWSAccount", "AWSService", "AssumedRole", "FederatedUser", "IAMUser", "Root"
]
