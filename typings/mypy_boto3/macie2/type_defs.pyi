"""
Type annotations for macie2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_macie2.type_defs import AcceptInvitationRequestRequestTypeDef

    data: AcceptInvitationRequestRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AdminStatusType,
    AllowListStatusCodeType,
    AllowsUnencryptedObjectUploadsType,
    AutoEnableModeType,
    AutomatedDiscoveryAccountStatusType,
    AutomatedDiscoveryAccountUpdateErrorCodeType,
    AutomatedDiscoveryMonitoringStatusType,
    AutomatedDiscoveryStatusType,
    AvailabilityCodeType,
    ClassificationScopeUpdateOperationType,
    DataIdentifierSeverityType,
    DataIdentifierTypeType,
    DayOfWeekType,
    EffectivePermissionType,
    EncryptionTypeType,
    ErrorCodeType,
    FindingCategoryType,
    FindingPublishingFrequencyType,
    FindingsFilterActionType,
    FindingStatisticsSortAttributeNameType,
    FindingTypeType,
    GroupByType,
    IsDefinedInJobType,
    IsMonitoredByJobType,
    JobComparatorType,
    JobStatusType,
    JobTypeType,
    LastRunErrorStatusCodeType,
    ListJobsFilterKeyType,
    ListJobsSortAttributeNameType,
    MacieStatusType,
    ManagedDataIdentifierSelectorType,
    OrderByType,
    OriginTypeType,
    RelationshipStatusType,
    RetrievalModeType,
    RevealRequestStatusType,
    RevealStatusType,
    ScopeFilterKeyType,
    SearchResourcesComparatorType,
    SearchResourcesSimpleCriterionKeyType,
    SearchResourcesSortAttributeNameType,
    SensitiveDataItemCategoryType,
    SeverityDescriptionType,
    SharedAccessType,
    SimpleCriterionKeyForJobType,
    StorageClassType,
    TimeRangeType,
    TypeType,
    UnavailabilityReasonCodeType,
    UsageStatisticsFilterComparatorType,
    UsageStatisticsFilterKeyType,
    UsageStatisticsSortKeyType,
    UsageTypeType,
    UserIdentityTypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AcceptInvitationRequestRequestTypeDef",
    "AccessControlListTypeDef",
    "AccountDetailTypeDef",
    "AccountLevelPermissionsTypeDef",
    "AdminAccountTypeDef",
    "AllowListCriteriaTypeDef",
    "AllowListStatusTypeDef",
    "AllowListSummaryTypeDef",
    "ApiCallDetailsTypeDef",
    "AssumedRoleTypeDef",
    "AutomatedDiscoveryAccountTypeDef",
    "AutomatedDiscoveryAccountUpdateErrorTypeDef",
    "AutomatedDiscoveryAccountUpdateTypeDef",
    "AwsAccountTypeDef",
    "AwsServiceTypeDef",
    "BatchGetCustomDataIdentifierSummaryTypeDef",
    "BatchGetCustomDataIdentifiersRequestRequestTypeDef",
    "BatchGetCustomDataIdentifiersResponseTypeDef",
    "BatchUpdateAutomatedDiscoveryAccountsRequestRequestTypeDef",
    "BatchUpdateAutomatedDiscoveryAccountsResponseTypeDef",
    "BlockPublicAccessTypeDef",
    "BucketCountByEffectivePermissionTypeDef",
    "BucketCountByEncryptionTypeTypeDef",
    "BucketCountBySharedAccessTypeTypeDef",
    "BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef",
    "BucketCriteriaAdditionalPropertiesTypeDef",
    "BucketLevelPermissionsTypeDef",
    "BucketMetadataTypeDef",
    "BucketPermissionConfigurationTypeDef",
    "BucketPolicyTypeDef",
    "BucketPublicAccessTypeDef",
    "BucketServerSideEncryptionTypeDef",
    "BucketSortCriteriaTypeDef",
    "BucketStatisticsBySensitivityTypeDef",
    "CellTypeDef",
    "ClassificationDetailsTypeDef",
    "ClassificationExportConfigurationTypeDef",
    "ClassificationResultStatusTypeDef",
    "ClassificationResultTypeDef",
    "ClassificationScopeSummaryTypeDef",
    "CreateAllowListRequestRequestTypeDef",
    "CreateAllowListResponseTypeDef",
    "CreateClassificationJobRequestRequestTypeDef",
    "CreateClassificationJobResponseTypeDef",
    "CreateCustomDataIdentifierRequestRequestTypeDef",
    "CreateCustomDataIdentifierResponseTypeDef",
    "CreateFindingsFilterRequestRequestTypeDef",
    "CreateFindingsFilterResponseTypeDef",
    "CreateInvitationsRequestRequestTypeDef",
    "CreateInvitationsResponseTypeDef",
    "CreateMemberRequestRequestTypeDef",
    "CreateMemberResponseTypeDef",
    "CreateSampleFindingsRequestRequestTypeDef",
    "CriteriaBlockForJobTypeDef",
    "CriteriaForJobTypeDef",
    "CriterionAdditionalPropertiesTypeDef",
    "CustomDataIdentifierSummaryTypeDef",
    "CustomDataIdentifiersTypeDef",
    "CustomDetectionTypeDef",
    "DeclineInvitationsRequestRequestTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DefaultDetectionTypeDef",
    "DeleteAllowListRequestRequestTypeDef",
    "DeleteCustomDataIdentifierRequestRequestTypeDef",
    "DeleteFindingsFilterRequestRequestTypeDef",
    "DeleteInvitationsRequestRequestTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "DeleteMemberRequestRequestTypeDef",
    "DescribeBucketsRequestRequestTypeDef",
    "DescribeBucketsResponseTypeDef",
    "DescribeClassificationJobRequestRequestTypeDef",
    "DescribeClassificationJobResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DetectedDataDetailsTypeDef",
    "DetectionTypeDef",
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    "DisassociateMemberRequestRequestTypeDef",
    "DomainDetailsTypeDef",
    "EnableMacieRequestRequestTypeDef",
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    "FederatedUserTypeDef",
    "FindingActionTypeDef",
    "FindingActorTypeDef",
    "FindingCriteriaTypeDef",
    "FindingStatisticsSortCriteriaTypeDef",
    "FindingTypeDef",
    "FindingsFilterListItemTypeDef",
    "GetAdministratorAccountResponseTypeDef",
    "GetAllowListRequestRequestTypeDef",
    "GetAllowListResponseTypeDef",
    "GetAutomatedDiscoveryConfigurationResponseTypeDef",
    "GetBucketStatisticsRequestRequestTypeDef",
    "GetBucketStatisticsResponseTypeDef",
    "GetClassificationExportConfigurationResponseTypeDef",
    "GetClassificationScopeRequestRequestTypeDef",
    "GetClassificationScopeResponseTypeDef",
    "GetCustomDataIdentifierRequestRequestTypeDef",
    "GetCustomDataIdentifierResponseTypeDef",
    "GetFindingStatisticsRequestRequestTypeDef",
    "GetFindingStatisticsResponseTypeDef",
    "GetFindingsFilterRequestRequestTypeDef",
    "GetFindingsFilterResponseTypeDef",
    "GetFindingsPublicationConfigurationResponseTypeDef",
    "GetFindingsRequestRequestTypeDef",
    "GetFindingsResponseTypeDef",
    "GetInvitationsCountResponseTypeDef",
    "GetMacieSessionResponseTypeDef",
    "GetMasterAccountResponseTypeDef",
    "GetMemberRequestRequestTypeDef",
    "GetMemberResponseTypeDef",
    "GetResourceProfileRequestRequestTypeDef",
    "GetResourceProfileResponseTypeDef",
    "GetRevealConfigurationResponseTypeDef",
    "GetSensitiveDataOccurrencesAvailabilityRequestRequestTypeDef",
    "GetSensitiveDataOccurrencesAvailabilityResponseTypeDef",
    "GetSensitiveDataOccurrencesRequestRequestTypeDef",
    "GetSensitiveDataOccurrencesResponseTypeDef",
    "GetSensitivityInspectionTemplateRequestRequestTypeDef",
    "GetSensitivityInspectionTemplateResponseTypeDef",
    "GetUsageStatisticsRequestRequestTypeDef",
    "GetUsageStatisticsResponseTypeDef",
    "GetUsageTotalsRequestRequestTypeDef",
    "GetUsageTotalsResponseTypeDef",
    "GroupCountTypeDef",
    "IamUserTypeDef",
    "InvitationTypeDef",
    "IpAddressDetailsTypeDef",
    "IpCityTypeDef",
    "IpCountryTypeDef",
    "IpGeoLocationTypeDef",
    "IpOwnerTypeDef",
    "JobDetailsTypeDef",
    "JobScheduleFrequencyTypeDef",
    "JobScopeTermTypeDef",
    "JobScopingBlockTypeDef",
    "JobSummaryTypeDef",
    "KeyValuePairTypeDef",
    "LastRunErrorStatusTypeDef",
    "ListAllowListsRequestRequestTypeDef",
    "ListAllowListsResponseTypeDef",
    "ListAutomatedDiscoveryAccountsRequestRequestTypeDef",
    "ListAutomatedDiscoveryAccountsResponseTypeDef",
    "ListClassificationJobsRequestRequestTypeDef",
    "ListClassificationJobsResponseTypeDef",
    "ListClassificationScopesRequestRequestTypeDef",
    "ListClassificationScopesResponseTypeDef",
    "ListCustomDataIdentifiersRequestRequestTypeDef",
    "ListCustomDataIdentifiersResponseTypeDef",
    "ListFindingsFiltersRequestRequestTypeDef",
    "ListFindingsFiltersResponseTypeDef",
    "ListFindingsRequestRequestTypeDef",
    "ListFindingsResponseTypeDef",
    "ListInvitationsRequestRequestTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListJobsFilterCriteriaTypeDef",
    "ListJobsFilterTermTypeDef",
    "ListJobsSortCriteriaTypeDef",
    "ListManagedDataIdentifiersRequestRequestTypeDef",
    "ListManagedDataIdentifiersResponseTypeDef",
    "ListMembersRequestRequestTypeDef",
    "ListMembersResponseTypeDef",
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListResourceProfileArtifactsRequestRequestTypeDef",
    "ListResourceProfileArtifactsResponseTypeDef",
    "ListResourceProfileDetectionsRequestRequestTypeDef",
    "ListResourceProfileDetectionsResponseTypeDef",
    "ListSensitivityInspectionTemplatesRequestRequestTypeDef",
    "ListSensitivityInspectionTemplatesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ManagedDataIdentifierSummaryTypeDef",
    "MatchingBucketTypeDef",
    "MatchingResourceTypeDef",
    "MemberTypeDef",
    "MonthlyScheduleTypeDef",
    "ObjectCountByEncryptionTypeTypeDef",
    "ObjectLevelStatisticsTypeDef",
    "OccurrencesTypeDef",
    "PageTypeDef",
    "PaginatorConfigTypeDef",
    "PolicyDetailsTypeDef",
    "PutClassificationExportConfigurationRequestRequestTypeDef",
    "PutClassificationExportConfigurationResponseTypeDef",
    "PutFindingsPublicationConfigurationRequestRequestTypeDef",
    "RangeTypeDef",
    "RecordTypeDef",
    "ReplicationDetailsTypeDef",
    "ResourceProfileArtifactTypeDef",
    "ResourceStatisticsTypeDef",
    "ResourcesAffectedTypeDef",
    "ResponseMetadataTypeDef",
    "RetrievalConfigurationTypeDef",
    "RevealConfigurationTypeDef",
    "S3BucketCriteriaForJobTypeDef",
    "S3BucketDefinitionForJobTypeDef",
    "S3BucketOwnerTypeDef",
    "S3BucketTypeDef",
    "S3ClassificationScopeExclusionTypeDef",
    "S3ClassificationScopeExclusionUpdateTypeDef",
    "S3ClassificationScopeTypeDef",
    "S3ClassificationScopeUpdateTypeDef",
    "S3DestinationTypeDef",
    "S3JobDefinitionTypeDef",
    "S3ObjectTypeDef",
    "S3WordsListTypeDef",
    "ScopingTypeDef",
    "SearchResourcesBucketCriteriaTypeDef",
    "SearchResourcesCriteriaBlockTypeDef",
    "SearchResourcesCriteriaTypeDef",
    "SearchResourcesRequestRequestTypeDef",
    "SearchResourcesResponseTypeDef",
    "SearchResourcesSimpleCriterionTypeDef",
    "SearchResourcesSortCriteriaTypeDef",
    "SearchResourcesTagCriterionPairTypeDef",
    "SearchResourcesTagCriterionTypeDef",
    "SecurityHubConfigurationTypeDef",
    "SensitiveDataItemTypeDef",
    "SensitivityAggregationsTypeDef",
    "SensitivityInspectionTemplateExcludesTypeDef",
    "SensitivityInspectionTemplateIncludesTypeDef",
    "SensitivityInspectionTemplatesEntryTypeDef",
    "ServerSideEncryptionTypeDef",
    "ServiceLimitTypeDef",
    "SessionContextAttributesTypeDef",
    "SessionContextTypeDef",
    "SessionIssuerTypeDef",
    "SeverityLevelTypeDef",
    "SeverityTypeDef",
    "SimpleCriterionForJobTypeDef",
    "SimpleScopeTermTypeDef",
    "SortCriteriaTypeDef",
    "StatisticsTypeDef",
    "SuppressDataIdentifierTypeDef",
    "TagCriterionForJobTypeDef",
    "TagCriterionPairForJobTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagScopeTermTypeDef",
    "TagValuePairTypeDef",
    "TestCustomDataIdentifierRequestRequestTypeDef",
    "TestCustomDataIdentifierResponseTypeDef",
    "UnprocessedAccountTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAllowListRequestRequestTypeDef",
    "UpdateAllowListResponseTypeDef",
    "UpdateAutomatedDiscoveryConfigurationRequestRequestTypeDef",
    "UpdateClassificationJobRequestRequestTypeDef",
    "UpdateClassificationScopeRequestRequestTypeDef",
    "UpdateFindingsFilterRequestRequestTypeDef",
    "UpdateFindingsFilterResponseTypeDef",
    "UpdateMacieSessionRequestRequestTypeDef",
    "UpdateMemberSessionRequestRequestTypeDef",
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    "UpdateResourceProfileDetectionsRequestRequestTypeDef",
    "UpdateResourceProfileRequestRequestTypeDef",
    "UpdateRetrievalConfigurationTypeDef",
    "UpdateRevealConfigurationRequestRequestTypeDef",
    "UpdateRevealConfigurationResponseTypeDef",
    "UpdateSensitivityInspectionTemplateRequestRequestTypeDef",
    "UsageByAccountTypeDef",
    "UsageRecordTypeDef",
    "UsageStatisticsFilterTypeDef",
    "UsageStatisticsSortByTypeDef",
    "UsageTotalTypeDef",
    "UserIdentityRootTypeDef",
    "UserIdentityTypeDef",
    "UserPausedDetailsTypeDef",
    "WaiterConfigTypeDef",
    "WeeklyScheduleTypeDef",
)

_RequiredAcceptInvitationRequestRequestTypeDef = TypedDict(
    "_RequiredAcceptInvitationRequestRequestTypeDef",
    {
        "invitationId": str,
    },
)
_OptionalAcceptInvitationRequestRequestTypeDef = TypedDict(
    "_OptionalAcceptInvitationRequestRequestTypeDef",
    {
        "administratorAccountId": str,
        "masterAccount": str,
    },
    total=False,
)

class AcceptInvitationRequestRequestTypeDef(
    _RequiredAcceptInvitationRequestRequestTypeDef, _OptionalAcceptInvitationRequestRequestTypeDef
):
    pass

AccessControlListTypeDef = TypedDict(
    "AccessControlListTypeDef",
    {
        "allowsPublicReadAccess": bool,
        "allowsPublicWriteAccess": bool,
    },
    total=False,
)

AccountDetailTypeDef = TypedDict(
    "AccountDetailTypeDef",
    {
        "accountId": str,
        "email": str,
    },
)

AccountLevelPermissionsTypeDef = TypedDict(
    "AccountLevelPermissionsTypeDef",
    {
        "blockPublicAccess": "BlockPublicAccessTypeDef",
    },
    total=False,
)

AdminAccountTypeDef = TypedDict(
    "AdminAccountTypeDef",
    {
        "accountId": str,
        "status": AdminStatusType,
    },
    total=False,
)

AllowListCriteriaTypeDef = TypedDict(
    "AllowListCriteriaTypeDef",
    {
        "regex": str,
        "s3WordsList": "S3WordsListTypeDef",
    },
    total=False,
)

_RequiredAllowListStatusTypeDef = TypedDict(
    "_RequiredAllowListStatusTypeDef",
    {
        "code": AllowListStatusCodeType,
    },
)
_OptionalAllowListStatusTypeDef = TypedDict(
    "_OptionalAllowListStatusTypeDef",
    {
        "description": str,
    },
    total=False,
)

class AllowListStatusTypeDef(_RequiredAllowListStatusTypeDef, _OptionalAllowListStatusTypeDef):
    pass

AllowListSummaryTypeDef = TypedDict(
    "AllowListSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "description": str,
        "id": str,
        "name": str,
        "updatedAt": datetime,
    },
    total=False,
)

ApiCallDetailsTypeDef = TypedDict(
    "ApiCallDetailsTypeDef",
    {
        "api": str,
        "apiServiceName": str,
        "firstSeen": datetime,
        "lastSeen": datetime,
    },
    total=False,
)

AssumedRoleTypeDef = TypedDict(
    "AssumedRoleTypeDef",
    {
        "accessKeyId": str,
        "accountId": str,
        "arn": str,
        "principalId": str,
        "sessionContext": "SessionContextTypeDef",
    },
    total=False,
)

AutomatedDiscoveryAccountTypeDef = TypedDict(
    "AutomatedDiscoveryAccountTypeDef",
    {
        "accountId": str,
        "status": AutomatedDiscoveryAccountStatusType,
    },
    total=False,
)

AutomatedDiscoveryAccountUpdateErrorTypeDef = TypedDict(
    "AutomatedDiscoveryAccountUpdateErrorTypeDef",
    {
        "accountId": str,
        "errorCode": AutomatedDiscoveryAccountUpdateErrorCodeType,
    },
    total=False,
)

AutomatedDiscoveryAccountUpdateTypeDef = TypedDict(
    "AutomatedDiscoveryAccountUpdateTypeDef",
    {
        "accountId": str,
        "status": AutomatedDiscoveryAccountStatusType,
    },
    total=False,
)

AwsAccountTypeDef = TypedDict(
    "AwsAccountTypeDef",
    {
        "accountId": str,
        "principalId": str,
    },
    total=False,
)

AwsServiceTypeDef = TypedDict(
    "AwsServiceTypeDef",
    {
        "invokedBy": str,
    },
    total=False,
)

BatchGetCustomDataIdentifierSummaryTypeDef = TypedDict(
    "BatchGetCustomDataIdentifierSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deleted": bool,
        "description": str,
        "id": str,
        "name": str,
    },
    total=False,
)

BatchGetCustomDataIdentifiersRequestRequestTypeDef = TypedDict(
    "BatchGetCustomDataIdentifiersRequestRequestTypeDef",
    {
        "ids": List[str],
    },
    total=False,
)

BatchGetCustomDataIdentifiersResponseTypeDef = TypedDict(
    "BatchGetCustomDataIdentifiersResponseTypeDef",
    {
        "customDataIdentifiers": List["BatchGetCustomDataIdentifierSummaryTypeDef"],
        "notFoundIdentifierIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdateAutomatedDiscoveryAccountsRequestRequestTypeDef = TypedDict(
    "BatchUpdateAutomatedDiscoveryAccountsRequestRequestTypeDef",
    {
        "accounts": List["AutomatedDiscoveryAccountUpdateTypeDef"],
    },
    total=False,
)

BatchUpdateAutomatedDiscoveryAccountsResponseTypeDef = TypedDict(
    "BatchUpdateAutomatedDiscoveryAccountsResponseTypeDef",
    {
        "errors": List["AutomatedDiscoveryAccountUpdateErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BlockPublicAccessTypeDef = TypedDict(
    "BlockPublicAccessTypeDef",
    {
        "blockPublicAcls": bool,
        "blockPublicPolicy": bool,
        "ignorePublicAcls": bool,
        "restrictPublicBuckets": bool,
    },
    total=False,
)

BucketCountByEffectivePermissionTypeDef = TypedDict(
    "BucketCountByEffectivePermissionTypeDef",
    {
        "publiclyAccessible": int,
        "publiclyReadable": int,
        "publiclyWritable": int,
        "unknown": int,
    },
    total=False,
)

BucketCountByEncryptionTypeTypeDef = TypedDict(
    "BucketCountByEncryptionTypeTypeDef",
    {
        "kmsManaged": int,
        "s3Managed": int,
        "unencrypted": int,
        "unknown": int,
    },
    total=False,
)

BucketCountBySharedAccessTypeTypeDef = TypedDict(
    "BucketCountBySharedAccessTypeTypeDef",
    {
        "external": int,
        "internal": int,
        "notShared": int,
        "unknown": int,
    },
    total=False,
)

BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef = TypedDict(
    "BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef",
    {
        "allowsUnencryptedObjectUploads": int,
        "deniesUnencryptedObjectUploads": int,
        "unknown": int,
    },
    total=False,
)

BucketCriteriaAdditionalPropertiesTypeDef = TypedDict(
    "BucketCriteriaAdditionalPropertiesTypeDef",
    {
        "eq": List[str],
        "gt": int,
        "gte": int,
        "lt": int,
        "lte": int,
        "neq": List[str],
        "prefix": str,
    },
    total=False,
)

BucketLevelPermissionsTypeDef = TypedDict(
    "BucketLevelPermissionsTypeDef",
    {
        "accessControlList": "AccessControlListTypeDef",
        "blockPublicAccess": "BlockPublicAccessTypeDef",
        "bucketPolicy": "BucketPolicyTypeDef",
    },
    total=False,
)

BucketMetadataTypeDef = TypedDict(
    "BucketMetadataTypeDef",
    {
        "accountId": str,
        "allowsUnencryptedObjectUploads": AllowsUnencryptedObjectUploadsType,
        "automatedDiscoveryMonitoringStatus": AutomatedDiscoveryMonitoringStatusType,
        "bucketArn": str,
        "bucketCreatedAt": datetime,
        "bucketName": str,
        "classifiableObjectCount": int,
        "classifiableSizeInBytes": int,
        "errorCode": Literal["ACCESS_DENIED"],
        "errorMessage": str,
        "jobDetails": "JobDetailsTypeDef",
        "lastAutomatedDiscoveryTime": datetime,
        "lastUpdated": datetime,
        "objectCount": int,
        "objectCountByEncryptionType": "ObjectCountByEncryptionTypeTypeDef",
        "publicAccess": "BucketPublicAccessTypeDef",
        "region": str,
        "replicationDetails": "ReplicationDetailsTypeDef",
        "sensitivityScore": int,
        "serverSideEncryption": "BucketServerSideEncryptionTypeDef",
        "sharedAccess": SharedAccessType,
        "sizeInBytes": int,
        "sizeInBytesCompressed": int,
        "tags": List["KeyValuePairTypeDef"],
        "unclassifiableObjectCount": "ObjectLevelStatisticsTypeDef",
        "unclassifiableObjectSizeInBytes": "ObjectLevelStatisticsTypeDef",
        "versioning": bool,
    },
    total=False,
)

BucketPermissionConfigurationTypeDef = TypedDict(
    "BucketPermissionConfigurationTypeDef",
    {
        "accountLevelPermissions": "AccountLevelPermissionsTypeDef",
        "bucketLevelPermissions": "BucketLevelPermissionsTypeDef",
    },
    total=False,
)

BucketPolicyTypeDef = TypedDict(
    "BucketPolicyTypeDef",
    {
        "allowsPublicReadAccess": bool,
        "allowsPublicWriteAccess": bool,
    },
    total=False,
)

BucketPublicAccessTypeDef = TypedDict(
    "BucketPublicAccessTypeDef",
    {
        "effectivePermission": EffectivePermissionType,
        "permissionConfiguration": "BucketPermissionConfigurationTypeDef",
    },
    total=False,
)

BucketServerSideEncryptionTypeDef = TypedDict(
    "BucketServerSideEncryptionTypeDef",
    {
        "kmsMasterKeyId": str,
        "type": TypeType,
    },
    total=False,
)

BucketSortCriteriaTypeDef = TypedDict(
    "BucketSortCriteriaTypeDef",
    {
        "attributeName": str,
        "orderBy": OrderByType,
    },
    total=False,
)

BucketStatisticsBySensitivityTypeDef = TypedDict(
    "BucketStatisticsBySensitivityTypeDef",
    {
        "classificationError": "SensitivityAggregationsTypeDef",
        "notClassified": "SensitivityAggregationsTypeDef",
        "notSensitive": "SensitivityAggregationsTypeDef",
        "sensitive": "SensitivityAggregationsTypeDef",
    },
    total=False,
)

CellTypeDef = TypedDict(
    "CellTypeDef",
    {
        "cellReference": str,
        "column": int,
        "columnName": str,
        "row": int,
    },
    total=False,
)

ClassificationDetailsTypeDef = TypedDict(
    "ClassificationDetailsTypeDef",
    {
        "detailedResultsLocation": str,
        "jobArn": str,
        "jobId": str,
        "originType": OriginTypeType,
        "result": "ClassificationResultTypeDef",
    },
    total=False,
)

ClassificationExportConfigurationTypeDef = TypedDict(
    "ClassificationExportConfigurationTypeDef",
    {
        "s3Destination": "S3DestinationTypeDef",
    },
    total=False,
)

ClassificationResultStatusTypeDef = TypedDict(
    "ClassificationResultStatusTypeDef",
    {
        "code": str,
        "reason": str,
    },
    total=False,
)

ClassificationResultTypeDef = TypedDict(
    "ClassificationResultTypeDef",
    {
        "additionalOccurrences": bool,
        "customDataIdentifiers": "CustomDataIdentifiersTypeDef",
        "mimeType": str,
        "sensitiveData": List["SensitiveDataItemTypeDef"],
        "sizeClassified": int,
        "status": "ClassificationResultStatusTypeDef",
    },
    total=False,
)

ClassificationScopeSummaryTypeDef = TypedDict(
    "ClassificationScopeSummaryTypeDef",
    {
        "id": str,
        "name": str,
    },
    total=False,
)

_RequiredCreateAllowListRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAllowListRequestRequestTypeDef",
    {
        "clientToken": str,
        "criteria": "AllowListCriteriaTypeDef",
        "name": str,
    },
)
_OptionalCreateAllowListRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAllowListRequestRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateAllowListRequestRequestTypeDef(
    _RequiredCreateAllowListRequestRequestTypeDef, _OptionalCreateAllowListRequestRequestTypeDef
):
    pass

CreateAllowListResponseTypeDef = TypedDict(
    "CreateAllowListResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClassificationJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateClassificationJobRequestRequestTypeDef",
    {
        "clientToken": str,
        "jobType": JobTypeType,
        "name": str,
        "s3JobDefinition": "S3JobDefinitionTypeDef",
    },
)
_OptionalCreateClassificationJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateClassificationJobRequestRequestTypeDef",
    {
        "allowListIds": List[str],
        "customDataIdentifierIds": List[str],
        "description": str,
        "initialRun": bool,
        "managedDataIdentifierIds": List[str],
        "managedDataIdentifierSelector": ManagedDataIdentifierSelectorType,
        "samplingPercentage": int,
        "scheduleFrequency": "JobScheduleFrequencyTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateClassificationJobRequestRequestTypeDef(
    _RequiredCreateClassificationJobRequestRequestTypeDef,
    _OptionalCreateClassificationJobRequestRequestTypeDef,
):
    pass

CreateClassificationJobResponseTypeDef = TypedDict(
    "CreateClassificationJobResponseTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCustomDataIdentifierRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCustomDataIdentifierRequestRequestTypeDef",
    {
        "name": str,
        "regex": str,
    },
)
_OptionalCreateCustomDataIdentifierRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCustomDataIdentifierRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "ignoreWords": List[str],
        "keywords": List[str],
        "maximumMatchDistance": int,
        "severityLevels": List["SeverityLevelTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateCustomDataIdentifierRequestRequestTypeDef(
    _RequiredCreateCustomDataIdentifierRequestRequestTypeDef,
    _OptionalCreateCustomDataIdentifierRequestRequestTypeDef,
):
    pass

CreateCustomDataIdentifierResponseTypeDef = TypedDict(
    "CreateCustomDataIdentifierResponseTypeDef",
    {
        "customDataIdentifierId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFindingsFilterRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFindingsFilterRequestRequestTypeDef",
    {
        "action": FindingsFilterActionType,
        "findingCriteria": "FindingCriteriaTypeDef",
        "name": str,
    },
)
_OptionalCreateFindingsFilterRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFindingsFilterRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "position": int,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateFindingsFilterRequestRequestTypeDef(
    _RequiredCreateFindingsFilterRequestRequestTypeDef,
    _OptionalCreateFindingsFilterRequestRequestTypeDef,
):
    pass

CreateFindingsFilterResponseTypeDef = TypedDict(
    "CreateFindingsFilterResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInvitationsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInvitationsRequestRequestTypeDef",
    {
        "accountIds": List[str],
    },
)
_OptionalCreateInvitationsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInvitationsRequestRequestTypeDef",
    {
        "disableEmailNotification": bool,
        "message": str,
    },
    total=False,
)

class CreateInvitationsRequestRequestTypeDef(
    _RequiredCreateInvitationsRequestRequestTypeDef, _OptionalCreateInvitationsRequestRequestTypeDef
):
    pass

CreateInvitationsResponseTypeDef = TypedDict(
    "CreateInvitationsResponseTypeDef",
    {
        "unprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMemberRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMemberRequestRequestTypeDef",
    {
        "account": "AccountDetailTypeDef",
    },
)
_OptionalCreateMemberRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMemberRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateMemberRequestRequestTypeDef(
    _RequiredCreateMemberRequestRequestTypeDef, _OptionalCreateMemberRequestRequestTypeDef
):
    pass

CreateMemberResponseTypeDef = TypedDict(
    "CreateMemberResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSampleFindingsRequestRequestTypeDef = TypedDict(
    "CreateSampleFindingsRequestRequestTypeDef",
    {
        "findingTypes": List[FindingTypeType],
    },
    total=False,
)

CriteriaBlockForJobTypeDef = TypedDict(
    "CriteriaBlockForJobTypeDef",
    {
        "and": List["CriteriaForJobTypeDef"],
    },
    total=False,
)

CriteriaForJobTypeDef = TypedDict(
    "CriteriaForJobTypeDef",
    {
        "simpleCriterion": "SimpleCriterionForJobTypeDef",
        "tagCriterion": "TagCriterionForJobTypeDef",
    },
    total=False,
)

CriterionAdditionalPropertiesTypeDef = TypedDict(
    "CriterionAdditionalPropertiesTypeDef",
    {
        "eq": List[str],
        "eqExactMatch": List[str],
        "gt": int,
        "gte": int,
        "lt": int,
        "lte": int,
        "neq": List[str],
    },
    total=False,
)

CustomDataIdentifierSummaryTypeDef = TypedDict(
    "CustomDataIdentifierSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "description": str,
        "id": str,
        "name": str,
    },
    total=False,
)

CustomDataIdentifiersTypeDef = TypedDict(
    "CustomDataIdentifiersTypeDef",
    {
        "detections": List["CustomDetectionTypeDef"],
        "totalCount": int,
    },
    total=False,
)

CustomDetectionTypeDef = TypedDict(
    "CustomDetectionTypeDef",
    {
        "arn": str,
        "count": int,
        "name": str,
        "occurrences": "OccurrencesTypeDef",
    },
    total=False,
)

DeclineInvitationsRequestRequestTypeDef = TypedDict(
    "DeclineInvitationsRequestRequestTypeDef",
    {
        "accountIds": List[str],
    },
)

DeclineInvitationsResponseTypeDef = TypedDict(
    "DeclineInvitationsResponseTypeDef",
    {
        "unprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefaultDetectionTypeDef = TypedDict(
    "DefaultDetectionTypeDef",
    {
        "count": int,
        "occurrences": "OccurrencesTypeDef",
        "type": str,
    },
    total=False,
)

_RequiredDeleteAllowListRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAllowListRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalDeleteAllowListRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAllowListRequestRequestTypeDef",
    {
        "ignoreJobChecks": str,
    },
    total=False,
)

class DeleteAllowListRequestRequestTypeDef(
    _RequiredDeleteAllowListRequestRequestTypeDef, _OptionalDeleteAllowListRequestRequestTypeDef
):
    pass

DeleteCustomDataIdentifierRequestRequestTypeDef = TypedDict(
    "DeleteCustomDataIdentifierRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteFindingsFilterRequestRequestTypeDef = TypedDict(
    "DeleteFindingsFilterRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteInvitationsRequestRequestTypeDef = TypedDict(
    "DeleteInvitationsRequestRequestTypeDef",
    {
        "accountIds": List[str],
    },
)

DeleteInvitationsResponseTypeDef = TypedDict(
    "DeleteInvitationsResponseTypeDef",
    {
        "unprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMemberRequestRequestTypeDef = TypedDict(
    "DeleteMemberRequestRequestTypeDef",
    {
        "id": str,
    },
)

DescribeBucketsRequestRequestTypeDef = TypedDict(
    "DescribeBucketsRequestRequestTypeDef",
    {
        "criteria": Dict[str, "BucketCriteriaAdditionalPropertiesTypeDef"],
        "maxResults": int,
        "nextToken": str,
        "sortCriteria": "BucketSortCriteriaTypeDef",
    },
    total=False,
)

DescribeBucketsResponseTypeDef = TypedDict(
    "DescribeBucketsResponseTypeDef",
    {
        "buckets": List["BucketMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClassificationJobRequestRequestTypeDef = TypedDict(
    "DescribeClassificationJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

DescribeClassificationJobResponseTypeDef = TypedDict(
    "DescribeClassificationJobResponseTypeDef",
    {
        "allowListIds": List[str],
        "clientToken": str,
        "createdAt": datetime,
        "customDataIdentifierIds": List[str],
        "description": str,
        "initialRun": bool,
        "jobArn": str,
        "jobId": str,
        "jobStatus": JobStatusType,
        "jobType": JobTypeType,
        "lastRunErrorStatus": "LastRunErrorStatusTypeDef",
        "lastRunTime": datetime,
        "managedDataIdentifierIds": List[str],
        "managedDataIdentifierSelector": ManagedDataIdentifierSelectorType,
        "name": str,
        "s3JobDefinition": "S3JobDefinitionTypeDef",
        "samplingPercentage": int,
        "scheduleFrequency": "JobScheduleFrequencyTypeDef",
        "statistics": "StatisticsTypeDef",
        "tags": Dict[str, str],
        "userPausedDetails": "UserPausedDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {
        "autoEnable": bool,
        "maxAccountLimitReached": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectedDataDetailsTypeDef = TypedDict(
    "DetectedDataDetailsTypeDef",
    {
        "value": str,
    },
)

DetectionTypeDef = TypedDict(
    "DetectionTypeDef",
    {
        "arn": str,
        "count": int,
        "id": str,
        "name": str,
        "suppressed": bool,
        "type": DataIdentifierTypeType,
    },
    total=False,
)

DisableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "adminAccountId": str,
    },
)

DisassociateMemberRequestRequestTypeDef = TypedDict(
    "DisassociateMemberRequestRequestTypeDef",
    {
        "id": str,
    },
)

DomainDetailsTypeDef = TypedDict(
    "DomainDetailsTypeDef",
    {
        "domainName": str,
    },
    total=False,
)

EnableMacieRequestRequestTypeDef = TypedDict(
    "EnableMacieRequestRequestTypeDef",
    {
        "clientToken": str,
        "findingPublishingFrequency": FindingPublishingFrequencyType,
        "status": MacieStatusType,
    },
    total=False,
)

_RequiredEnableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "_RequiredEnableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "adminAccountId": str,
    },
)
_OptionalEnableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "_OptionalEnableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class EnableOrganizationAdminAccountRequestRequestTypeDef(
    _RequiredEnableOrganizationAdminAccountRequestRequestTypeDef,
    _OptionalEnableOrganizationAdminAccountRequestRequestTypeDef,
):
    pass

FederatedUserTypeDef = TypedDict(
    "FederatedUserTypeDef",
    {
        "accessKeyId": str,
        "accountId": str,
        "arn": str,
        "principalId": str,
        "sessionContext": "SessionContextTypeDef",
    },
    total=False,
)

FindingActionTypeDef = TypedDict(
    "FindingActionTypeDef",
    {
        "actionType": Literal["AWS_API_CALL"],
        "apiCallDetails": "ApiCallDetailsTypeDef",
    },
    total=False,
)

FindingActorTypeDef = TypedDict(
    "FindingActorTypeDef",
    {
        "domainDetails": "DomainDetailsTypeDef",
        "ipAddressDetails": "IpAddressDetailsTypeDef",
        "userIdentity": "UserIdentityTypeDef",
    },
    total=False,
)

FindingCriteriaTypeDef = TypedDict(
    "FindingCriteriaTypeDef",
    {
        "criterion": Dict[str, "CriterionAdditionalPropertiesTypeDef"],
    },
    total=False,
)

FindingStatisticsSortCriteriaTypeDef = TypedDict(
    "FindingStatisticsSortCriteriaTypeDef",
    {
        "attributeName": FindingStatisticsSortAttributeNameType,
        "orderBy": OrderByType,
    },
    total=False,
)

FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "accountId": str,
        "archived": bool,
        "category": FindingCategoryType,
        "classificationDetails": "ClassificationDetailsTypeDef",
        "count": int,
        "createdAt": datetime,
        "description": str,
        "id": str,
        "partition": str,
        "policyDetails": "PolicyDetailsTypeDef",
        "region": str,
        "resourcesAffected": "ResourcesAffectedTypeDef",
        "sample": bool,
        "schemaVersion": str,
        "severity": "SeverityTypeDef",
        "title": str,
        "type": FindingTypeType,
        "updatedAt": datetime,
    },
    total=False,
)

FindingsFilterListItemTypeDef = TypedDict(
    "FindingsFilterListItemTypeDef",
    {
        "action": FindingsFilterActionType,
        "arn": str,
        "id": str,
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

GetAdministratorAccountResponseTypeDef = TypedDict(
    "GetAdministratorAccountResponseTypeDef",
    {
        "administrator": "InvitationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAllowListRequestRequestTypeDef = TypedDict(
    "GetAllowListRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetAllowListResponseTypeDef = TypedDict(
    "GetAllowListResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "criteria": "AllowListCriteriaTypeDef",
        "description": str,
        "id": str,
        "name": str,
        "status": "AllowListStatusTypeDef",
        "tags": Dict[str, str],
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAutomatedDiscoveryConfigurationResponseTypeDef = TypedDict(
    "GetAutomatedDiscoveryConfigurationResponseTypeDef",
    {
        "autoEnableOrganizationMembers": AutoEnableModeType,
        "classificationScopeId": str,
        "disabledAt": datetime,
        "firstEnabledAt": datetime,
        "lastUpdatedAt": datetime,
        "sensitivityInspectionTemplateId": str,
        "status": AutomatedDiscoveryStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketStatisticsRequestRequestTypeDef = TypedDict(
    "GetBucketStatisticsRequestRequestTypeDef",
    {
        "accountId": str,
    },
    total=False,
)

GetBucketStatisticsResponseTypeDef = TypedDict(
    "GetBucketStatisticsResponseTypeDef",
    {
        "bucketCount": int,
        "bucketCountByEffectivePermission": "BucketCountByEffectivePermissionTypeDef",
        "bucketCountByEncryptionType": "BucketCountByEncryptionTypeTypeDef",
        "bucketCountByObjectEncryptionRequirement": "BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef",
        "bucketCountBySharedAccessType": "BucketCountBySharedAccessTypeTypeDef",
        "bucketStatisticsBySensitivity": "BucketStatisticsBySensitivityTypeDef",
        "classifiableObjectCount": int,
        "classifiableSizeInBytes": int,
        "lastUpdated": datetime,
        "objectCount": int,
        "sizeInBytes": int,
        "sizeInBytesCompressed": int,
        "unclassifiableObjectCount": "ObjectLevelStatisticsTypeDef",
        "unclassifiableObjectSizeInBytes": "ObjectLevelStatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetClassificationExportConfigurationResponseTypeDef = TypedDict(
    "GetClassificationExportConfigurationResponseTypeDef",
    {
        "configuration": "ClassificationExportConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetClassificationScopeRequestRequestTypeDef = TypedDict(
    "GetClassificationScopeRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetClassificationScopeResponseTypeDef = TypedDict(
    "GetClassificationScopeResponseTypeDef",
    {
        "id": str,
        "name": str,
        "s3": "S3ClassificationScopeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCustomDataIdentifierRequestRequestTypeDef = TypedDict(
    "GetCustomDataIdentifierRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetCustomDataIdentifierResponseTypeDef = TypedDict(
    "GetCustomDataIdentifierResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deleted": bool,
        "description": str,
        "id": str,
        "ignoreWords": List[str],
        "keywords": List[str],
        "maximumMatchDistance": int,
        "name": str,
        "regex": str,
        "severityLevels": List["SeverityLevelTypeDef"],
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFindingStatisticsRequestRequestTypeDef = TypedDict(
    "_RequiredGetFindingStatisticsRequestRequestTypeDef",
    {
        "groupBy": GroupByType,
    },
)
_OptionalGetFindingStatisticsRequestRequestTypeDef = TypedDict(
    "_OptionalGetFindingStatisticsRequestRequestTypeDef",
    {
        "findingCriteria": "FindingCriteriaTypeDef",
        "size": int,
        "sortCriteria": "FindingStatisticsSortCriteriaTypeDef",
    },
    total=False,
)

class GetFindingStatisticsRequestRequestTypeDef(
    _RequiredGetFindingStatisticsRequestRequestTypeDef,
    _OptionalGetFindingStatisticsRequestRequestTypeDef,
):
    pass

GetFindingStatisticsResponseTypeDef = TypedDict(
    "GetFindingStatisticsResponseTypeDef",
    {
        "countsByGroup": List["GroupCountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFindingsFilterRequestRequestTypeDef = TypedDict(
    "GetFindingsFilterRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetFindingsFilterResponseTypeDef = TypedDict(
    "GetFindingsFilterResponseTypeDef",
    {
        "action": FindingsFilterActionType,
        "arn": str,
        "description": str,
        "findingCriteria": "FindingCriteriaTypeDef",
        "id": str,
        "name": str,
        "position": int,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFindingsPublicationConfigurationResponseTypeDef = TypedDict(
    "GetFindingsPublicationConfigurationResponseTypeDef",
    {
        "securityHubConfiguration": "SecurityHubConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFindingsRequestRequestTypeDef = TypedDict(
    "_RequiredGetFindingsRequestRequestTypeDef",
    {
        "findingIds": List[str],
    },
)
_OptionalGetFindingsRequestRequestTypeDef = TypedDict(
    "_OptionalGetFindingsRequestRequestTypeDef",
    {
        "sortCriteria": "SortCriteriaTypeDef",
    },
    total=False,
)

class GetFindingsRequestRequestTypeDef(
    _RequiredGetFindingsRequestRequestTypeDef, _OptionalGetFindingsRequestRequestTypeDef
):
    pass

GetFindingsResponseTypeDef = TypedDict(
    "GetFindingsResponseTypeDef",
    {
        "findings": List["FindingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInvitationsCountResponseTypeDef = TypedDict(
    "GetInvitationsCountResponseTypeDef",
    {
        "invitationsCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMacieSessionResponseTypeDef = TypedDict(
    "GetMacieSessionResponseTypeDef",
    {
        "createdAt": datetime,
        "findingPublishingFrequency": FindingPublishingFrequencyType,
        "serviceRole": str,
        "status": MacieStatusType,
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMasterAccountResponseTypeDef = TypedDict(
    "GetMasterAccountResponseTypeDef",
    {
        "master": "InvitationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMemberRequestRequestTypeDef = TypedDict(
    "GetMemberRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetMemberResponseTypeDef = TypedDict(
    "GetMemberResponseTypeDef",
    {
        "accountId": str,
        "administratorAccountId": str,
        "arn": str,
        "email": str,
        "invitedAt": datetime,
        "masterAccountId": str,
        "relationshipStatus": RelationshipStatusType,
        "tags": Dict[str, str],
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceProfileRequestRequestTypeDef = TypedDict(
    "GetResourceProfileRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

GetResourceProfileResponseTypeDef = TypedDict(
    "GetResourceProfileResponseTypeDef",
    {
        "profileUpdatedAt": datetime,
        "sensitivityScore": int,
        "sensitivityScoreOverridden": bool,
        "statistics": "ResourceStatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRevealConfigurationResponseTypeDef = TypedDict(
    "GetRevealConfigurationResponseTypeDef",
    {
        "configuration": "RevealConfigurationTypeDef",
        "retrievalConfiguration": "RetrievalConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSensitiveDataOccurrencesAvailabilityRequestRequestTypeDef = TypedDict(
    "GetSensitiveDataOccurrencesAvailabilityRequestRequestTypeDef",
    {
        "findingId": str,
    },
)

GetSensitiveDataOccurrencesAvailabilityResponseTypeDef = TypedDict(
    "GetSensitiveDataOccurrencesAvailabilityResponseTypeDef",
    {
        "code": AvailabilityCodeType,
        "reasons": List[UnavailabilityReasonCodeType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSensitiveDataOccurrencesRequestRequestTypeDef = TypedDict(
    "GetSensitiveDataOccurrencesRequestRequestTypeDef",
    {
        "findingId": str,
    },
)

GetSensitiveDataOccurrencesResponseTypeDef = TypedDict(
    "GetSensitiveDataOccurrencesResponseTypeDef",
    {
        "error": str,
        "sensitiveDataOccurrences": Dict[str, List["DetectedDataDetailsTypeDef"]],
        "status": RevealRequestStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSensitivityInspectionTemplateRequestRequestTypeDef = TypedDict(
    "GetSensitivityInspectionTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetSensitivityInspectionTemplateResponseTypeDef = TypedDict(
    "GetSensitivityInspectionTemplateResponseTypeDef",
    {
        "description": str,
        "excludes": "SensitivityInspectionTemplateExcludesTypeDef",
        "includes": "SensitivityInspectionTemplateIncludesTypeDef",
        "name": str,
        "sensitivityInspectionTemplateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUsageStatisticsRequestRequestTypeDef = TypedDict(
    "GetUsageStatisticsRequestRequestTypeDef",
    {
        "filterBy": List["UsageStatisticsFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
        "sortBy": "UsageStatisticsSortByTypeDef",
        "timeRange": TimeRangeType,
    },
    total=False,
)

GetUsageStatisticsResponseTypeDef = TypedDict(
    "GetUsageStatisticsResponseTypeDef",
    {
        "nextToken": str,
        "records": List["UsageRecordTypeDef"],
        "timeRange": TimeRangeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUsageTotalsRequestRequestTypeDef = TypedDict(
    "GetUsageTotalsRequestRequestTypeDef",
    {
        "timeRange": str,
    },
    total=False,
)

GetUsageTotalsResponseTypeDef = TypedDict(
    "GetUsageTotalsResponseTypeDef",
    {
        "timeRange": TimeRangeType,
        "usageTotals": List["UsageTotalTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupCountTypeDef = TypedDict(
    "GroupCountTypeDef",
    {
        "count": int,
        "groupKey": str,
    },
    total=False,
)

IamUserTypeDef = TypedDict(
    "IamUserTypeDef",
    {
        "accountId": str,
        "arn": str,
        "principalId": str,
        "userName": str,
    },
    total=False,
)

InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {
        "accountId": str,
        "invitationId": str,
        "invitedAt": datetime,
        "relationshipStatus": RelationshipStatusType,
    },
    total=False,
)

IpAddressDetailsTypeDef = TypedDict(
    "IpAddressDetailsTypeDef",
    {
        "ipAddressV4": str,
        "ipCity": "IpCityTypeDef",
        "ipCountry": "IpCountryTypeDef",
        "ipGeoLocation": "IpGeoLocationTypeDef",
        "ipOwner": "IpOwnerTypeDef",
    },
    total=False,
)

IpCityTypeDef = TypedDict(
    "IpCityTypeDef",
    {
        "name": str,
    },
    total=False,
)

IpCountryTypeDef = TypedDict(
    "IpCountryTypeDef",
    {
        "code": str,
        "name": str,
    },
    total=False,
)

IpGeoLocationTypeDef = TypedDict(
    "IpGeoLocationTypeDef",
    {
        "lat": float,
        "lon": float,
    },
    total=False,
)

IpOwnerTypeDef = TypedDict(
    "IpOwnerTypeDef",
    {
        "asn": str,
        "asnOrg": str,
        "isp": str,
        "org": str,
    },
    total=False,
)

JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef",
    {
        "isDefinedInJob": IsDefinedInJobType,
        "isMonitoredByJob": IsMonitoredByJobType,
        "lastJobId": str,
        "lastJobRunTime": datetime,
    },
    total=False,
)

JobScheduleFrequencyTypeDef = TypedDict(
    "JobScheduleFrequencyTypeDef",
    {
        "dailySchedule": Dict[str, Any],
        "monthlySchedule": "MonthlyScheduleTypeDef",
        "weeklySchedule": "WeeklyScheduleTypeDef",
    },
    total=False,
)

JobScopeTermTypeDef = TypedDict(
    "JobScopeTermTypeDef",
    {
        "simpleScopeTerm": "SimpleScopeTermTypeDef",
        "tagScopeTerm": "TagScopeTermTypeDef",
    },
    total=False,
)

JobScopingBlockTypeDef = TypedDict(
    "JobScopingBlockTypeDef",
    {
        "and": List["JobScopeTermTypeDef"],
    },
    total=False,
)

JobSummaryTypeDef = TypedDict(
    "JobSummaryTypeDef",
    {
        "bucketCriteria": "S3BucketCriteriaForJobTypeDef",
        "bucketDefinitions": List["S3BucketDefinitionForJobTypeDef"],
        "createdAt": datetime,
        "jobId": str,
        "jobStatus": JobStatusType,
        "jobType": JobTypeType,
        "lastRunErrorStatus": "LastRunErrorStatusTypeDef",
        "name": str,
        "userPausedDetails": "UserPausedDetailsTypeDef",
    },
    total=False,
)

KeyValuePairTypeDef = TypedDict(
    "KeyValuePairTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

LastRunErrorStatusTypeDef = TypedDict(
    "LastRunErrorStatusTypeDef",
    {
        "code": LastRunErrorStatusCodeType,
    },
    total=False,
)

ListAllowListsRequestRequestTypeDef = TypedDict(
    "ListAllowListsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListAllowListsResponseTypeDef = TypedDict(
    "ListAllowListsResponseTypeDef",
    {
        "allowLists": List["AllowListSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAutomatedDiscoveryAccountsRequestRequestTypeDef = TypedDict(
    "ListAutomatedDiscoveryAccountsRequestRequestTypeDef",
    {
        "accountIds": List[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListAutomatedDiscoveryAccountsResponseTypeDef = TypedDict(
    "ListAutomatedDiscoveryAccountsResponseTypeDef",
    {
        "items": List["AutomatedDiscoveryAccountTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClassificationJobsRequestRequestTypeDef = TypedDict(
    "ListClassificationJobsRequestRequestTypeDef",
    {
        "filterCriteria": "ListJobsFilterCriteriaTypeDef",
        "maxResults": int,
        "nextToken": str,
        "sortCriteria": "ListJobsSortCriteriaTypeDef",
    },
    total=False,
)

ListClassificationJobsResponseTypeDef = TypedDict(
    "ListClassificationJobsResponseTypeDef",
    {
        "items": List["JobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClassificationScopesRequestRequestTypeDef = TypedDict(
    "ListClassificationScopesRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": str,
    },
    total=False,
)

ListClassificationScopesResponseTypeDef = TypedDict(
    "ListClassificationScopesResponseTypeDef",
    {
        "classificationScopes": List["ClassificationScopeSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomDataIdentifiersRequestRequestTypeDef = TypedDict(
    "ListCustomDataIdentifiersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListCustomDataIdentifiersResponseTypeDef = TypedDict(
    "ListCustomDataIdentifiersResponseTypeDef",
    {
        "items": List["CustomDataIdentifierSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFindingsFiltersRequestRequestTypeDef = TypedDict(
    "ListFindingsFiltersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListFindingsFiltersResponseTypeDef = TypedDict(
    "ListFindingsFiltersResponseTypeDef",
    {
        "findingsFilterListItems": List["FindingsFilterListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFindingsRequestRequestTypeDef = TypedDict(
    "ListFindingsRequestRequestTypeDef",
    {
        "findingCriteria": "FindingCriteriaTypeDef",
        "maxResults": int,
        "nextToken": str,
        "sortCriteria": "SortCriteriaTypeDef",
    },
    total=False,
)

ListFindingsResponseTypeDef = TypedDict(
    "ListFindingsResponseTypeDef",
    {
        "findingIds": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInvitationsRequestRequestTypeDef = TypedDict(
    "ListInvitationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {
        "invitations": List["InvitationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsFilterCriteriaTypeDef = TypedDict(
    "ListJobsFilterCriteriaTypeDef",
    {
        "excludes": List["ListJobsFilterTermTypeDef"],
        "includes": List["ListJobsFilterTermTypeDef"],
    },
    total=False,
)

ListJobsFilterTermTypeDef = TypedDict(
    "ListJobsFilterTermTypeDef",
    {
        "comparator": JobComparatorType,
        "key": ListJobsFilterKeyType,
        "values": List[str],
    },
    total=False,
)

ListJobsSortCriteriaTypeDef = TypedDict(
    "ListJobsSortCriteriaTypeDef",
    {
        "attributeName": ListJobsSortAttributeNameType,
        "orderBy": OrderByType,
    },
    total=False,
)

ListManagedDataIdentifiersRequestRequestTypeDef = TypedDict(
    "ListManagedDataIdentifiersRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

ListManagedDataIdentifiersResponseTypeDef = TypedDict(
    "ListManagedDataIdentifiersResponseTypeDef",
    {
        "items": List["ManagedDataIdentifierSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMembersRequestRequestTypeDef = TypedDict(
    "ListMembersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "onlyAssociated": str,
    },
    total=False,
)

ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef",
    {
        "members": List["MemberTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOrganizationAdminAccountsRequestRequestTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListOrganizationAdminAccountsResponseTypeDef = TypedDict(
    "ListOrganizationAdminAccountsResponseTypeDef",
    {
        "adminAccounts": List["AdminAccountTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourceProfileArtifactsRequestRequestTypeDef = TypedDict(
    "_RequiredListResourceProfileArtifactsRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListResourceProfileArtifactsRequestRequestTypeDef = TypedDict(
    "_OptionalListResourceProfileArtifactsRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListResourceProfileArtifactsRequestRequestTypeDef(
    _RequiredListResourceProfileArtifactsRequestRequestTypeDef,
    _OptionalListResourceProfileArtifactsRequestRequestTypeDef,
):
    pass

ListResourceProfileArtifactsResponseTypeDef = TypedDict(
    "ListResourceProfileArtifactsResponseTypeDef",
    {
        "artifacts": List["ResourceProfileArtifactTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourceProfileDetectionsRequestRequestTypeDef = TypedDict(
    "_RequiredListResourceProfileDetectionsRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListResourceProfileDetectionsRequestRequestTypeDef = TypedDict(
    "_OptionalListResourceProfileDetectionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListResourceProfileDetectionsRequestRequestTypeDef(
    _RequiredListResourceProfileDetectionsRequestRequestTypeDef,
    _OptionalListResourceProfileDetectionsRequestRequestTypeDef,
):
    pass

ListResourceProfileDetectionsResponseTypeDef = TypedDict(
    "ListResourceProfileDetectionsResponseTypeDef",
    {
        "detections": List["DetectionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSensitivityInspectionTemplatesRequestRequestTypeDef = TypedDict(
    "ListSensitivityInspectionTemplatesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSensitivityInspectionTemplatesResponseTypeDef = TypedDict(
    "ListSensitivityInspectionTemplatesResponseTypeDef",
    {
        "nextToken": str,
        "sensitivityInspectionTemplates": List["SensitivityInspectionTemplatesEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ManagedDataIdentifierSummaryTypeDef = TypedDict(
    "ManagedDataIdentifierSummaryTypeDef",
    {
        "category": SensitiveDataItemCategoryType,
        "id": str,
    },
    total=False,
)

MatchingBucketTypeDef = TypedDict(
    "MatchingBucketTypeDef",
    {
        "accountId": str,
        "automatedDiscoveryMonitoringStatus": AutomatedDiscoveryMonitoringStatusType,
        "bucketName": str,
        "classifiableObjectCount": int,
        "classifiableSizeInBytes": int,
        "errorCode": Literal["ACCESS_DENIED"],
        "errorMessage": str,
        "jobDetails": "JobDetailsTypeDef",
        "lastAutomatedDiscoveryTime": datetime,
        "objectCount": int,
        "objectCountByEncryptionType": "ObjectCountByEncryptionTypeTypeDef",
        "sensitivityScore": int,
        "sizeInBytes": int,
        "sizeInBytesCompressed": int,
        "unclassifiableObjectCount": "ObjectLevelStatisticsTypeDef",
        "unclassifiableObjectSizeInBytes": "ObjectLevelStatisticsTypeDef",
    },
    total=False,
)

MatchingResourceTypeDef = TypedDict(
    "MatchingResourceTypeDef",
    {
        "matchingBucket": "MatchingBucketTypeDef",
    },
    total=False,
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "accountId": str,
        "administratorAccountId": str,
        "arn": str,
        "email": str,
        "invitedAt": datetime,
        "masterAccountId": str,
        "relationshipStatus": RelationshipStatusType,
        "tags": Dict[str, str],
        "updatedAt": datetime,
    },
    total=False,
)

MonthlyScheduleTypeDef = TypedDict(
    "MonthlyScheduleTypeDef",
    {
        "dayOfMonth": int,
    },
    total=False,
)

ObjectCountByEncryptionTypeTypeDef = TypedDict(
    "ObjectCountByEncryptionTypeTypeDef",
    {
        "customerManaged": int,
        "kmsManaged": int,
        "s3Managed": int,
        "unencrypted": int,
        "unknown": int,
    },
    total=False,
)

ObjectLevelStatisticsTypeDef = TypedDict(
    "ObjectLevelStatisticsTypeDef",
    {
        "fileType": int,
        "storageClass": int,
        "total": int,
    },
    total=False,
)

OccurrencesTypeDef = TypedDict(
    "OccurrencesTypeDef",
    {
        "cells": List["CellTypeDef"],
        "lineRanges": List["RangeTypeDef"],
        "offsetRanges": List["RangeTypeDef"],
        "pages": List["PageTypeDef"],
        "records": List["RecordTypeDef"],
    },
    total=False,
)

PageTypeDef = TypedDict(
    "PageTypeDef",
    {
        "lineRange": "RangeTypeDef",
        "offsetRange": "RangeTypeDef",
        "pageNumber": int,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PolicyDetailsTypeDef = TypedDict(
    "PolicyDetailsTypeDef",
    {
        "action": "FindingActionTypeDef",
        "actor": "FindingActorTypeDef",
    },
    total=False,
)

PutClassificationExportConfigurationRequestRequestTypeDef = TypedDict(
    "PutClassificationExportConfigurationRequestRequestTypeDef",
    {
        "configuration": "ClassificationExportConfigurationTypeDef",
    },
)

PutClassificationExportConfigurationResponseTypeDef = TypedDict(
    "PutClassificationExportConfigurationResponseTypeDef",
    {
        "configuration": "ClassificationExportConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutFindingsPublicationConfigurationRequestRequestTypeDef = TypedDict(
    "PutFindingsPublicationConfigurationRequestRequestTypeDef",
    {
        "clientToken": str,
        "securityHubConfiguration": "SecurityHubConfigurationTypeDef",
    },
    total=False,
)

RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "end": int,
        "start": int,
        "startColumn": int,
    },
    total=False,
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "jsonPath": str,
        "recordIndex": int,
    },
    total=False,
)

ReplicationDetailsTypeDef = TypedDict(
    "ReplicationDetailsTypeDef",
    {
        "replicated": bool,
        "replicatedExternally": bool,
        "replicationAccounts": List[str],
    },
    total=False,
)

_RequiredResourceProfileArtifactTypeDef = TypedDict(
    "_RequiredResourceProfileArtifactTypeDef",
    {
        "arn": str,
        "classificationResultStatus": str,
    },
)
_OptionalResourceProfileArtifactTypeDef = TypedDict(
    "_OptionalResourceProfileArtifactTypeDef",
    {
        "sensitive": bool,
    },
    total=False,
)

class ResourceProfileArtifactTypeDef(
    _RequiredResourceProfileArtifactTypeDef, _OptionalResourceProfileArtifactTypeDef
):
    pass

ResourceStatisticsTypeDef = TypedDict(
    "ResourceStatisticsTypeDef",
    {
        "totalBytesClassified": int,
        "totalDetections": int,
        "totalDetectionsSuppressed": int,
        "totalItemsClassified": int,
        "totalItemsSensitive": int,
        "totalItemsSkipped": int,
        "totalItemsSkippedInvalidEncryption": int,
        "totalItemsSkippedInvalidKms": int,
        "totalItemsSkippedPermissionDenied": int,
    },
    total=False,
)

ResourcesAffectedTypeDef = TypedDict(
    "ResourcesAffectedTypeDef",
    {
        "s3Bucket": "S3BucketTypeDef",
        "s3Object": "S3ObjectTypeDef",
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredRetrievalConfigurationTypeDef = TypedDict(
    "_RequiredRetrievalConfigurationTypeDef",
    {
        "retrievalMode": RetrievalModeType,
    },
)
_OptionalRetrievalConfigurationTypeDef = TypedDict(
    "_OptionalRetrievalConfigurationTypeDef",
    {
        "externalId": str,
        "roleName": str,
    },
    total=False,
)

class RetrievalConfigurationTypeDef(
    _RequiredRetrievalConfigurationTypeDef, _OptionalRetrievalConfigurationTypeDef
):
    pass

_RequiredRevealConfigurationTypeDef = TypedDict(
    "_RequiredRevealConfigurationTypeDef",
    {
        "status": RevealStatusType,
    },
)
_OptionalRevealConfigurationTypeDef = TypedDict(
    "_OptionalRevealConfigurationTypeDef",
    {
        "kmsKeyId": str,
    },
    total=False,
)

class RevealConfigurationTypeDef(
    _RequiredRevealConfigurationTypeDef, _OptionalRevealConfigurationTypeDef
):
    pass

S3BucketCriteriaForJobTypeDef = TypedDict(
    "S3BucketCriteriaForJobTypeDef",
    {
        "excludes": "CriteriaBlockForJobTypeDef",
        "includes": "CriteriaBlockForJobTypeDef",
    },
    total=False,
)

S3BucketDefinitionForJobTypeDef = TypedDict(
    "S3BucketDefinitionForJobTypeDef",
    {
        "accountId": str,
        "buckets": List[str],
    },
)

S3BucketOwnerTypeDef = TypedDict(
    "S3BucketOwnerTypeDef",
    {
        "displayName": str,
        "id": str,
    },
    total=False,
)

S3BucketTypeDef = TypedDict(
    "S3BucketTypeDef",
    {
        "allowsUnencryptedObjectUploads": AllowsUnencryptedObjectUploadsType,
        "arn": str,
        "createdAt": datetime,
        "defaultServerSideEncryption": "ServerSideEncryptionTypeDef",
        "name": str,
        "owner": "S3BucketOwnerTypeDef",
        "publicAccess": "BucketPublicAccessTypeDef",
        "tags": List["KeyValuePairTypeDef"],
    },
    total=False,
)

S3ClassificationScopeExclusionTypeDef = TypedDict(
    "S3ClassificationScopeExclusionTypeDef",
    {
        "bucketNames": List[str],
    },
)

S3ClassificationScopeExclusionUpdateTypeDef = TypedDict(
    "S3ClassificationScopeExclusionUpdateTypeDef",
    {
        "bucketNames": List[str],
        "operation": ClassificationScopeUpdateOperationType,
    },
)

S3ClassificationScopeTypeDef = TypedDict(
    "S3ClassificationScopeTypeDef",
    {
        "excludes": "S3ClassificationScopeExclusionTypeDef",
    },
)

S3ClassificationScopeUpdateTypeDef = TypedDict(
    "S3ClassificationScopeUpdateTypeDef",
    {
        "excludes": "S3ClassificationScopeExclusionUpdateTypeDef",
    },
)

_RequiredS3DestinationTypeDef = TypedDict(
    "_RequiredS3DestinationTypeDef",
    {
        "bucketName": str,
        "kmsKeyArn": str,
    },
)
_OptionalS3DestinationTypeDef = TypedDict(
    "_OptionalS3DestinationTypeDef",
    {
        "keyPrefix": str,
    },
    total=False,
)

class S3DestinationTypeDef(_RequiredS3DestinationTypeDef, _OptionalS3DestinationTypeDef):
    pass

S3JobDefinitionTypeDef = TypedDict(
    "S3JobDefinitionTypeDef",
    {
        "bucketCriteria": "S3BucketCriteriaForJobTypeDef",
        "bucketDefinitions": List["S3BucketDefinitionForJobTypeDef"],
        "scoping": "ScopingTypeDef",
    },
    total=False,
)

S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "bucketArn": str,
        "eTag": str,
        "extension": str,
        "key": str,
        "lastModified": datetime,
        "path": str,
        "publicAccess": bool,
        "serverSideEncryption": "ServerSideEncryptionTypeDef",
        "size": int,
        "storageClass": StorageClassType,
        "tags": List["KeyValuePairTypeDef"],
        "versionId": str,
    },
    total=False,
)

S3WordsListTypeDef = TypedDict(
    "S3WordsListTypeDef",
    {
        "bucketName": str,
        "objectKey": str,
    },
)

ScopingTypeDef = TypedDict(
    "ScopingTypeDef",
    {
        "excludes": "JobScopingBlockTypeDef",
        "includes": "JobScopingBlockTypeDef",
    },
    total=False,
)

SearchResourcesBucketCriteriaTypeDef = TypedDict(
    "SearchResourcesBucketCriteriaTypeDef",
    {
        "excludes": "SearchResourcesCriteriaBlockTypeDef",
        "includes": "SearchResourcesCriteriaBlockTypeDef",
    },
    total=False,
)

SearchResourcesCriteriaBlockTypeDef = TypedDict(
    "SearchResourcesCriteriaBlockTypeDef",
    {
        "and": List["SearchResourcesCriteriaTypeDef"],
    },
    total=False,
)

SearchResourcesCriteriaTypeDef = TypedDict(
    "SearchResourcesCriteriaTypeDef",
    {
        "simpleCriterion": "SearchResourcesSimpleCriterionTypeDef",
        "tagCriterion": "SearchResourcesTagCriterionTypeDef",
    },
    total=False,
)

SearchResourcesRequestRequestTypeDef = TypedDict(
    "SearchResourcesRequestRequestTypeDef",
    {
        "bucketCriteria": "SearchResourcesBucketCriteriaTypeDef",
        "maxResults": int,
        "nextToken": str,
        "sortCriteria": "SearchResourcesSortCriteriaTypeDef",
    },
    total=False,
)

SearchResourcesResponseTypeDef = TypedDict(
    "SearchResourcesResponseTypeDef",
    {
        "matchingResources": List["MatchingResourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchResourcesSimpleCriterionTypeDef = TypedDict(
    "SearchResourcesSimpleCriterionTypeDef",
    {
        "comparator": SearchResourcesComparatorType,
        "key": SearchResourcesSimpleCriterionKeyType,
        "values": List[str],
    },
    total=False,
)

SearchResourcesSortCriteriaTypeDef = TypedDict(
    "SearchResourcesSortCriteriaTypeDef",
    {
        "attributeName": SearchResourcesSortAttributeNameType,
        "orderBy": OrderByType,
    },
    total=False,
)

SearchResourcesTagCriterionPairTypeDef = TypedDict(
    "SearchResourcesTagCriterionPairTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

SearchResourcesTagCriterionTypeDef = TypedDict(
    "SearchResourcesTagCriterionTypeDef",
    {
        "comparator": SearchResourcesComparatorType,
        "tagValues": List["SearchResourcesTagCriterionPairTypeDef"],
    },
    total=False,
)

SecurityHubConfigurationTypeDef = TypedDict(
    "SecurityHubConfigurationTypeDef",
    {
        "publishClassificationFindings": bool,
        "publishPolicyFindings": bool,
    },
)

SensitiveDataItemTypeDef = TypedDict(
    "SensitiveDataItemTypeDef",
    {
        "category": SensitiveDataItemCategoryType,
        "detections": List["DefaultDetectionTypeDef"],
        "totalCount": int,
    },
    total=False,
)

SensitivityAggregationsTypeDef = TypedDict(
    "SensitivityAggregationsTypeDef",
    {
        "classifiableSizeInBytes": int,
        "publiclyAccessibleCount": int,
        "totalCount": int,
        "totalSizeInBytes": int,
    },
    total=False,
)

SensitivityInspectionTemplateExcludesTypeDef = TypedDict(
    "SensitivityInspectionTemplateExcludesTypeDef",
    {
        "managedDataIdentifierIds": List[str],
    },
    total=False,
)

SensitivityInspectionTemplateIncludesTypeDef = TypedDict(
    "SensitivityInspectionTemplateIncludesTypeDef",
    {
        "allowListIds": List[str],
        "customDataIdentifierIds": List[str],
        "managedDataIdentifierIds": List[str],
    },
    total=False,
)

SensitivityInspectionTemplatesEntryTypeDef = TypedDict(
    "SensitivityInspectionTemplatesEntryTypeDef",
    {
        "id": str,
        "name": str,
    },
    total=False,
)

ServerSideEncryptionTypeDef = TypedDict(
    "ServerSideEncryptionTypeDef",
    {
        "encryptionType": EncryptionTypeType,
        "kmsMasterKeyId": str,
    },
    total=False,
)

ServiceLimitTypeDef = TypedDict(
    "ServiceLimitTypeDef",
    {
        "isServiceLimited": bool,
        "unit": Literal["TERABYTES"],
        "value": int,
    },
    total=False,
)

SessionContextAttributesTypeDef = TypedDict(
    "SessionContextAttributesTypeDef",
    {
        "creationDate": datetime,
        "mfaAuthenticated": bool,
    },
    total=False,
)

SessionContextTypeDef = TypedDict(
    "SessionContextTypeDef",
    {
        "attributes": "SessionContextAttributesTypeDef",
        "sessionIssuer": "SessionIssuerTypeDef",
    },
    total=False,
)

SessionIssuerTypeDef = TypedDict(
    "SessionIssuerTypeDef",
    {
        "accountId": str,
        "arn": str,
        "principalId": str,
        "type": str,
        "userName": str,
    },
    total=False,
)

SeverityLevelTypeDef = TypedDict(
    "SeverityLevelTypeDef",
    {
        "occurrencesThreshold": int,
        "severity": DataIdentifierSeverityType,
    },
)

SeverityTypeDef = TypedDict(
    "SeverityTypeDef",
    {
        "description": SeverityDescriptionType,
        "score": int,
    },
    total=False,
)

SimpleCriterionForJobTypeDef = TypedDict(
    "SimpleCriterionForJobTypeDef",
    {
        "comparator": JobComparatorType,
        "key": SimpleCriterionKeyForJobType,
        "values": List[str],
    },
    total=False,
)

SimpleScopeTermTypeDef = TypedDict(
    "SimpleScopeTermTypeDef",
    {
        "comparator": JobComparatorType,
        "key": ScopeFilterKeyType,
        "values": List[str],
    },
    total=False,
)

SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef",
    {
        "attributeName": str,
        "orderBy": OrderByType,
    },
    total=False,
)

StatisticsTypeDef = TypedDict(
    "StatisticsTypeDef",
    {
        "approximateNumberOfObjectsToProcess": float,
        "numberOfRuns": float,
    },
    total=False,
)

SuppressDataIdentifierTypeDef = TypedDict(
    "SuppressDataIdentifierTypeDef",
    {
        "id": str,
        "type": DataIdentifierTypeType,
    },
    total=False,
)

TagCriterionForJobTypeDef = TypedDict(
    "TagCriterionForJobTypeDef",
    {
        "comparator": JobComparatorType,
        "tagValues": List["TagCriterionPairForJobTypeDef"],
    },
    total=False,
)

TagCriterionPairForJobTypeDef = TypedDict(
    "TagCriterionPairForJobTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TagScopeTermTypeDef = TypedDict(
    "TagScopeTermTypeDef",
    {
        "comparator": JobComparatorType,
        "key": str,
        "tagValues": List["TagValuePairTypeDef"],
        "target": Literal["S3_OBJECT"],
    },
    total=False,
)

TagValuePairTypeDef = TypedDict(
    "TagValuePairTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

_RequiredTestCustomDataIdentifierRequestRequestTypeDef = TypedDict(
    "_RequiredTestCustomDataIdentifierRequestRequestTypeDef",
    {
        "regex": str,
        "sampleText": str,
    },
)
_OptionalTestCustomDataIdentifierRequestRequestTypeDef = TypedDict(
    "_OptionalTestCustomDataIdentifierRequestRequestTypeDef",
    {
        "ignoreWords": List[str],
        "keywords": List[str],
        "maximumMatchDistance": int,
    },
    total=False,
)

class TestCustomDataIdentifierRequestRequestTypeDef(
    _RequiredTestCustomDataIdentifierRequestRequestTypeDef,
    _OptionalTestCustomDataIdentifierRequestRequestTypeDef,
):
    pass

TestCustomDataIdentifierResponseTypeDef = TypedDict(
    "TestCustomDataIdentifierResponseTypeDef",
    {
        "matchCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnprocessedAccountTypeDef = TypedDict(
    "UnprocessedAccountTypeDef",
    {
        "accountId": str,
        "errorCode": ErrorCodeType,
        "errorMessage": str,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateAllowListRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAllowListRequestRequestTypeDef",
    {
        "criteria": "AllowListCriteriaTypeDef",
        "id": str,
        "name": str,
    },
)
_OptionalUpdateAllowListRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAllowListRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateAllowListRequestRequestTypeDef(
    _RequiredUpdateAllowListRequestRequestTypeDef, _OptionalUpdateAllowListRequestRequestTypeDef
):
    pass

UpdateAllowListResponseTypeDef = TypedDict(
    "UpdateAllowListResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAutomatedDiscoveryConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAutomatedDiscoveryConfigurationRequestRequestTypeDef",
    {
        "status": AutomatedDiscoveryStatusType,
    },
)
_OptionalUpdateAutomatedDiscoveryConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAutomatedDiscoveryConfigurationRequestRequestTypeDef",
    {
        "autoEnableOrganizationMembers": AutoEnableModeType,
    },
    total=False,
)

class UpdateAutomatedDiscoveryConfigurationRequestRequestTypeDef(
    _RequiredUpdateAutomatedDiscoveryConfigurationRequestRequestTypeDef,
    _OptionalUpdateAutomatedDiscoveryConfigurationRequestRequestTypeDef,
):
    pass

UpdateClassificationJobRequestRequestTypeDef = TypedDict(
    "UpdateClassificationJobRequestRequestTypeDef",
    {
        "jobId": str,
        "jobStatus": JobStatusType,
    },
)

_RequiredUpdateClassificationScopeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateClassificationScopeRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateClassificationScopeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateClassificationScopeRequestRequestTypeDef",
    {
        "s3": "S3ClassificationScopeUpdateTypeDef",
    },
    total=False,
)

class UpdateClassificationScopeRequestRequestTypeDef(
    _RequiredUpdateClassificationScopeRequestRequestTypeDef,
    _OptionalUpdateClassificationScopeRequestRequestTypeDef,
):
    pass

_RequiredUpdateFindingsFilterRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFindingsFilterRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateFindingsFilterRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFindingsFilterRequestRequestTypeDef",
    {
        "action": FindingsFilterActionType,
        "clientToken": str,
        "description": str,
        "findingCriteria": "FindingCriteriaTypeDef",
        "name": str,
        "position": int,
    },
    total=False,
)

class UpdateFindingsFilterRequestRequestTypeDef(
    _RequiredUpdateFindingsFilterRequestRequestTypeDef,
    _OptionalUpdateFindingsFilterRequestRequestTypeDef,
):
    pass

UpdateFindingsFilterResponseTypeDef = TypedDict(
    "UpdateFindingsFilterResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMacieSessionRequestRequestTypeDef = TypedDict(
    "UpdateMacieSessionRequestRequestTypeDef",
    {
        "findingPublishingFrequency": FindingPublishingFrequencyType,
        "status": MacieStatusType,
    },
    total=False,
)

UpdateMemberSessionRequestRequestTypeDef = TypedDict(
    "UpdateMemberSessionRequestRequestTypeDef",
    {
        "id": str,
        "status": MacieStatusType,
    },
)

UpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "autoEnable": bool,
    },
)

_RequiredUpdateResourceProfileDetectionsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateResourceProfileDetectionsRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalUpdateResourceProfileDetectionsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateResourceProfileDetectionsRequestRequestTypeDef",
    {
        "suppressDataIdentifiers": List["SuppressDataIdentifierTypeDef"],
    },
    total=False,
)

class UpdateResourceProfileDetectionsRequestRequestTypeDef(
    _RequiredUpdateResourceProfileDetectionsRequestRequestTypeDef,
    _OptionalUpdateResourceProfileDetectionsRequestRequestTypeDef,
):
    pass

_RequiredUpdateResourceProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateResourceProfileRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalUpdateResourceProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateResourceProfileRequestRequestTypeDef",
    {
        "sensitivityScoreOverride": int,
    },
    total=False,
)

class UpdateResourceProfileRequestRequestTypeDef(
    _RequiredUpdateResourceProfileRequestRequestTypeDef,
    _OptionalUpdateResourceProfileRequestRequestTypeDef,
):
    pass

_RequiredUpdateRetrievalConfigurationTypeDef = TypedDict(
    "_RequiredUpdateRetrievalConfigurationTypeDef",
    {
        "retrievalMode": RetrievalModeType,
    },
)
_OptionalUpdateRetrievalConfigurationTypeDef = TypedDict(
    "_OptionalUpdateRetrievalConfigurationTypeDef",
    {
        "roleName": str,
    },
    total=False,
)

class UpdateRetrievalConfigurationTypeDef(
    _RequiredUpdateRetrievalConfigurationTypeDef, _OptionalUpdateRetrievalConfigurationTypeDef
):
    pass

_RequiredUpdateRevealConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRevealConfigurationRequestRequestTypeDef",
    {
        "configuration": "RevealConfigurationTypeDef",
    },
)
_OptionalUpdateRevealConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRevealConfigurationRequestRequestTypeDef",
    {
        "retrievalConfiguration": "UpdateRetrievalConfigurationTypeDef",
    },
    total=False,
)

class UpdateRevealConfigurationRequestRequestTypeDef(
    _RequiredUpdateRevealConfigurationRequestRequestTypeDef,
    _OptionalUpdateRevealConfigurationRequestRequestTypeDef,
):
    pass

UpdateRevealConfigurationResponseTypeDef = TypedDict(
    "UpdateRevealConfigurationResponseTypeDef",
    {
        "configuration": "RevealConfigurationTypeDef",
        "retrievalConfiguration": "RetrievalConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSensitivityInspectionTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSensitivityInspectionTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateSensitivityInspectionTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSensitivityInspectionTemplateRequestRequestTypeDef",
    {
        "description": str,
        "excludes": "SensitivityInspectionTemplateExcludesTypeDef",
        "includes": "SensitivityInspectionTemplateIncludesTypeDef",
    },
    total=False,
)

class UpdateSensitivityInspectionTemplateRequestRequestTypeDef(
    _RequiredUpdateSensitivityInspectionTemplateRequestRequestTypeDef,
    _OptionalUpdateSensitivityInspectionTemplateRequestRequestTypeDef,
):
    pass

UsageByAccountTypeDef = TypedDict(
    "UsageByAccountTypeDef",
    {
        "currency": Literal["USD"],
        "estimatedCost": str,
        "serviceLimit": "ServiceLimitTypeDef",
        "type": UsageTypeType,
    },
    total=False,
)

UsageRecordTypeDef = TypedDict(
    "UsageRecordTypeDef",
    {
        "accountId": str,
        "automatedDiscoveryFreeTrialStartDate": datetime,
        "freeTrialStartDate": datetime,
        "usage": List["UsageByAccountTypeDef"],
    },
    total=False,
)

UsageStatisticsFilterTypeDef = TypedDict(
    "UsageStatisticsFilterTypeDef",
    {
        "comparator": UsageStatisticsFilterComparatorType,
        "key": UsageStatisticsFilterKeyType,
        "values": List[str],
    },
    total=False,
)

UsageStatisticsSortByTypeDef = TypedDict(
    "UsageStatisticsSortByTypeDef",
    {
        "key": UsageStatisticsSortKeyType,
        "orderBy": OrderByType,
    },
    total=False,
)

UsageTotalTypeDef = TypedDict(
    "UsageTotalTypeDef",
    {
        "currency": Literal["USD"],
        "estimatedCost": str,
        "type": UsageTypeType,
    },
    total=False,
)

UserIdentityRootTypeDef = TypedDict(
    "UserIdentityRootTypeDef",
    {
        "accountId": str,
        "arn": str,
        "principalId": str,
    },
    total=False,
)

UserIdentityTypeDef = TypedDict(
    "UserIdentityTypeDef",
    {
        "assumedRole": "AssumedRoleTypeDef",
        "awsAccount": "AwsAccountTypeDef",
        "awsService": "AwsServiceTypeDef",
        "federatedUser": "FederatedUserTypeDef",
        "iamUser": "IamUserTypeDef",
        "root": "UserIdentityRootTypeDef",
        "type": UserIdentityTypeType,
    },
    total=False,
)

UserPausedDetailsTypeDef = TypedDict(
    "UserPausedDetailsTypeDef",
    {
        "jobExpiresAt": datetime,
        "jobImminentExpirationHealthEventArn": str,
        "jobPausedAt": datetime,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

WeeklyScheduleTypeDef = TypedDict(
    "WeeklyScheduleTypeDef",
    {
        "dayOfWeek": DayOfWeekType,
    },
    total=False,
)
