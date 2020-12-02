"""
Main interface for macie2 service type definitions.

Usage::

    ```python
    from mypy_boto3_macie2.type_defs import AccessControlListTypeDef

    data: AccessControlListTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessControlListTypeDef",
    "AccountLevelPermissionsTypeDef",
    "AdminAccountTypeDef",
    "ApiCallDetailsTypeDef",
    "AssumedRoleTypeDef",
    "AwsAccountTypeDef",
    "AwsServiceTypeDef",
    "BatchGetCustomDataIdentifierSummaryTypeDef",
    "BlockPublicAccessTypeDef",
    "BucketCountByEffectivePermissionTypeDef",
    "BucketCountByEncryptionTypeTypeDef",
    "BucketCountBySharedAccessTypeTypeDef",
    "BucketLevelPermissionsTypeDef",
    "BucketMetadataTypeDef",
    "BucketPermissionConfigurationTypeDef",
    "BucketPolicyTypeDef",
    "BucketPublicAccessTypeDef",
    "CellTypeDef",
    "ClassificationDetailsTypeDef",
    "ClassificationExportConfigurationTypeDef",
    "ClassificationResultStatusTypeDef",
    "ClassificationResultTypeDef",
    "CriterionAdditionalPropertiesTypeDef",
    "CustomDataIdentifierSummaryTypeDef",
    "CustomDataIdentifiersTypeDef",
    "CustomDetectionTypeDef",
    "DefaultDetectionTypeDef",
    "DomainDetailsTypeDef",
    "FederatedUserTypeDef",
    "FindingActionTypeDef",
    "FindingActorTypeDef",
    "FindingCriteriaTypeDef",
    "FindingTypeDef",
    "FindingsFilterListItemTypeDef",
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
    "ListJobsFilterTermTypeDef",
    "MemberTypeDef",
    "MonthlyScheduleTypeDef",
    "ObjectCountByEncryptionTypeTypeDef",
    "ObjectLevelStatisticsTypeDef",
    "OccurrencesTypeDef",
    "PageTypeDef",
    "PolicyDetailsTypeDef",
    "RangeTypeDef",
    "RecordTypeDef",
    "ReplicationDetailsTypeDef",
    "ResourcesAffectedTypeDef",
    "S3BucketDefinitionForJobTypeDef",
    "S3BucketOwnerTypeDef",
    "S3BucketTypeDef",
    "S3DestinationTypeDef",
    "S3JobDefinitionTypeDef",
    "S3ObjectTypeDef",
    "ScopingTypeDef",
    "SensitiveDataItemTypeDef",
    "ServerSideEncryptionTypeDef",
    "ServiceLimitTypeDef",
    "SessionContextAttributesTypeDef",
    "SessionContextTypeDef",
    "SessionIssuerTypeDef",
    "SeverityTypeDef",
    "SimpleScopeTermTypeDef",
    "StatisticsTypeDef",
    "TagScopeTermTypeDef",
    "TagValuePairTypeDef",
    "UnprocessedAccountTypeDef",
    "UsageByAccountTypeDef",
    "UsageRecordTypeDef",
    "UsageTotalTypeDef",
    "UserIdentityRootTypeDef",
    "UserIdentityTypeDef",
    "UserPausedDetailsTypeDef",
    "WeeklyScheduleTypeDef",
    "AccountDetailTypeDef",
    "BatchGetCustomDataIdentifiersResponseTypeDef",
    "BucketCriteriaAdditionalPropertiesTypeDef",
    "BucketSortCriteriaTypeDef",
    "CreateClassificationJobResponseTypeDef",
    "CreateCustomDataIdentifierResponseTypeDef",
    "CreateFindingsFilterResponseTypeDef",
    "CreateInvitationsResponseTypeDef",
    "CreateMemberResponseTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "DescribeBucketsResponseTypeDef",
    "DescribeClassificationJobResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "FindingStatisticsSortCriteriaTypeDef",
    "GetBucketStatisticsResponseTypeDef",
    "GetClassificationExportConfigurationResponseTypeDef",
    "GetCustomDataIdentifierResponseTypeDef",
    "GetFindingStatisticsResponseTypeDef",
    "GetFindingsFilterResponseTypeDef",
    "GetFindingsResponseTypeDef",
    "GetInvitationsCountResponseTypeDef",
    "GetMacieSessionResponseTypeDef",
    "GetMasterAccountResponseTypeDef",
    "GetMemberResponseTypeDef",
    "GetUsageStatisticsResponseTypeDef",
    "GetUsageTotalsResponseTypeDef",
    "ListClassificationJobsResponseTypeDef",
    "ListCustomDataIdentifiersResponseTypeDef",
    "ListFindingsFiltersResponseTypeDef",
    "ListFindingsResponseTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListJobsFilterCriteriaTypeDef",
    "ListJobsSortCriteriaTypeDef",
    "ListMembersResponseTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutClassificationExportConfigurationResponseTypeDef",
    "SortCriteriaTypeDef",
    "TestCustomDataIdentifierResponseTypeDef",
    "UpdateFindingsFilterResponseTypeDef",
    "UsageStatisticsFilterTypeDef",
    "UsageStatisticsSortByTypeDef",
)

AccessControlListTypeDef = TypedDict(
    "AccessControlListTypeDef",
    {"allowsPublicReadAccess": bool, "allowsPublicWriteAccess": bool},
    total=False,
)

AccountLevelPermissionsTypeDef = TypedDict(
    "AccountLevelPermissionsTypeDef", {"blockPublicAccess": "BlockPublicAccessTypeDef"}, total=False
)

AdminAccountTypeDef = TypedDict(
    "AdminAccountTypeDef",
    {"accountId": str, "status": Literal["ENABLED", "DISABLING_IN_PROGRESS"]},
    total=False,
)

ApiCallDetailsTypeDef = TypedDict(
    "ApiCallDetailsTypeDef",
    {"api": str, "apiServiceName": str, "firstSeen": datetime, "lastSeen": datetime},
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

AwsAccountTypeDef = TypedDict(
    "AwsAccountTypeDef", {"accountId": str, "principalId": str}, total=False
)

AwsServiceTypeDef = TypedDict("AwsServiceTypeDef", {"invokedBy": str}, total=False)

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
    {"publiclyAccessible": int, "publiclyReadable": int, "publiclyWritable": int, "unknown": int},
    total=False,
)

BucketCountByEncryptionTypeTypeDef = TypedDict(
    "BucketCountByEncryptionTypeTypeDef",
    {"kmsManaged": int, "s3Managed": int, "unencrypted": int},
    total=False,
)

BucketCountBySharedAccessTypeTypeDef = TypedDict(
    "BucketCountBySharedAccessTypeTypeDef",
    {"external": int, "internal": int, "notShared": int, "unknown": int},
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
        "bucketArn": str,
        "bucketCreatedAt": datetime,
        "bucketName": str,
        "classifiableObjectCount": int,
        "classifiableSizeInBytes": int,
        "jobDetails": "JobDetailsTypeDef",
        "lastUpdated": datetime,
        "objectCount": int,
        "objectCountByEncryptionType": "ObjectCountByEncryptionTypeTypeDef",
        "publicAccess": "BucketPublicAccessTypeDef",
        "region": str,
        "replicationDetails": "ReplicationDetailsTypeDef",
        "sharedAccess": Literal["EXTERNAL", "INTERNAL", "NOT_SHARED", "UNKNOWN"],
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
    {"allowsPublicReadAccess": bool, "allowsPublicWriteAccess": bool},
    total=False,
)

BucketPublicAccessTypeDef = TypedDict(
    "BucketPublicAccessTypeDef",
    {
        "effectivePermission": Literal["PUBLIC", "NOT_PUBLIC", "UNKNOWN"],
        "permissionConfiguration": "BucketPermissionConfigurationTypeDef",
    },
    total=False,
)

CellTypeDef = TypedDict(
    "CellTypeDef", {"cellReference": str, "column": int, "columnName": str, "row": int}, total=False
)

ClassificationDetailsTypeDef = TypedDict(
    "ClassificationDetailsTypeDef",
    {
        "detailedResultsLocation": str,
        "jobArn": str,
        "jobId": str,
        "result": "ClassificationResultTypeDef",
    },
    total=False,
)

ClassificationExportConfigurationTypeDef = TypedDict(
    "ClassificationExportConfigurationTypeDef",
    {"s3Destination": "S3DestinationTypeDef"},
    total=False,
)

ClassificationResultStatusTypeDef = TypedDict(
    "ClassificationResultStatusTypeDef", {"code": str, "reason": str}, total=False
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
    {"arn": str, "createdAt": datetime, "description": str, "id": str, "name": str},
    total=False,
)

CustomDataIdentifiersTypeDef = TypedDict(
    "CustomDataIdentifiersTypeDef",
    {"detections": List["CustomDetectionTypeDef"], "totalCount": int},
    total=False,
)

CustomDetectionTypeDef = TypedDict(
    "CustomDetectionTypeDef",
    {"arn": str, "count": int, "name": str, "occurrences": "OccurrencesTypeDef"},
    total=False,
)

DefaultDetectionTypeDef = TypedDict(
    "DefaultDetectionTypeDef",
    {"count": int, "occurrences": "OccurrencesTypeDef", "type": str},
    total=False,
)

DomainDetailsTypeDef = TypedDict("DomainDetailsTypeDef", {"domainName": str}, total=False)

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
    {"actionType": Literal["AWS_API_CALL"], "apiCallDetails": "ApiCallDetailsTypeDef"},
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
    {"criterion": Dict[str, "CriterionAdditionalPropertiesTypeDef"]},
    total=False,
)

FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "accountId": str,
        "archived": bool,
        "category": Literal["CLASSIFICATION", "POLICY"],
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
        "type": Literal[
            "SensitiveData:S3Object/Multiple",
            "SensitiveData:S3Object/Financial",
            "SensitiveData:S3Object/Personal",
            "SensitiveData:S3Object/Credentials",
            "SensitiveData:S3Object/CustomIdentifier",
            "Policy:IAMUser/S3BucketPublic",
            "Policy:IAMUser/S3BucketSharedExternally",
            "Policy:IAMUser/S3BucketReplicatedExternally",
            "Policy:IAMUser/S3BucketEncryptionDisabled",
            "Policy:IAMUser/S3BlockPublicAccessDisabled",
        ],
        "updatedAt": datetime,
    },
    total=False,
)

FindingsFilterListItemTypeDef = TypedDict(
    "FindingsFilterListItemTypeDef",
    {
        "action": Literal["ARCHIVE", "NOOP"],
        "arn": str,
        "id": str,
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

GroupCountTypeDef = TypedDict("GroupCountTypeDef", {"count": int, "groupKey": str}, total=False)

IamUserTypeDef = TypedDict(
    "IamUserTypeDef",
    {"accountId": str, "arn": str, "principalId": str, "userName": str},
    total=False,
)

InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {
        "accountId": str,
        "invitationId": str,
        "invitedAt": datetime,
        "relationshipStatus": Literal[
            "Enabled",
            "Paused",
            "Invited",
            "Created",
            "Removed",
            "Resigned",
            "EmailVerificationInProgress",
            "EmailVerificationFailed",
            "RegionDisabled",
            "AccountSuspended",
        ],
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

IpCityTypeDef = TypedDict("IpCityTypeDef", {"name": str}, total=False)

IpCountryTypeDef = TypedDict("IpCountryTypeDef", {"code": str, "name": str}, total=False)

IpGeoLocationTypeDef = TypedDict("IpGeoLocationTypeDef", {"lat": float, "lon": float}, total=False)

IpOwnerTypeDef = TypedDict(
    "IpOwnerTypeDef", {"asn": str, "asnOrg": str, "isp": str, "org": str}, total=False
)

JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef",
    {
        "isDefinedInJob": Literal["TRUE", "FALSE", "UNKNOWN"],
        "isMonitoredByJob": Literal["TRUE", "FALSE", "UNKNOWN"],
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
    {"simpleScopeTerm": "SimpleScopeTermTypeDef", "tagScopeTerm": "TagScopeTermTypeDef"},
    total=False,
)

JobScopingBlockTypeDef = TypedDict(
    "JobScopingBlockTypeDef", {"and": List["JobScopeTermTypeDef"]}, total=False
)

JobSummaryTypeDef = TypedDict(
    "JobSummaryTypeDef",
    {
        "bucketDefinitions": List["S3BucketDefinitionForJobTypeDef"],
        "createdAt": datetime,
        "jobId": str,
        "jobStatus": Literal["RUNNING", "PAUSED", "CANCELLED", "COMPLETE", "IDLE", "USER_PAUSED"],
        "jobType": Literal["ONE_TIME", "SCHEDULED"],
        "lastRunErrorStatus": "LastRunErrorStatusTypeDef",
        "name": str,
        "userPausedDetails": "UserPausedDetailsTypeDef",
    },
    total=False,
)

KeyValuePairTypeDef = TypedDict("KeyValuePairTypeDef", {"key": str, "value": str}, total=False)

LastRunErrorStatusTypeDef = TypedDict(
    "LastRunErrorStatusTypeDef", {"code": Literal["NONE", "ERROR"]}, total=False
)

ListJobsFilterTermTypeDef = TypedDict(
    "ListJobsFilterTermTypeDef",
    {
        "comparator": Literal["EQ", "GT", "GTE", "LT", "LTE", "NE", "CONTAINS"],
        "key": Literal["jobType", "jobStatus", "createdAt", "name"],
        "values": List[str],
    },
    total=False,
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "accountId": str,
        "arn": str,
        "email": str,
        "invitedAt": datetime,
        "masterAccountId": str,
        "relationshipStatus": Literal[
            "Enabled",
            "Paused",
            "Invited",
            "Created",
            "Removed",
            "Resigned",
            "EmailVerificationInProgress",
            "EmailVerificationFailed",
            "RegionDisabled",
            "AccountSuspended",
        ],
        "tags": Dict[str, str],
        "updatedAt": datetime,
    },
    total=False,
)

MonthlyScheduleTypeDef = TypedDict("MonthlyScheduleTypeDef", {"dayOfMonth": int}, total=False)

ObjectCountByEncryptionTypeTypeDef = TypedDict(
    "ObjectCountByEncryptionTypeTypeDef",
    {"customerManaged": int, "kmsManaged": int, "s3Managed": int, "unencrypted": int},
    total=False,
)

ObjectLevelStatisticsTypeDef = TypedDict(
    "ObjectLevelStatisticsTypeDef",
    {"fileType": int, "storageClass": int, "total": int},
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
    {"lineRange": "RangeTypeDef", "offsetRange": "RangeTypeDef", "pageNumber": int},
    total=False,
)

PolicyDetailsTypeDef = TypedDict(
    "PolicyDetailsTypeDef",
    {"action": "FindingActionTypeDef", "actor": "FindingActorTypeDef"},
    total=False,
)

RangeTypeDef = TypedDict(
    "RangeTypeDef", {"end": int, "start": int, "startColumn": int}, total=False
)

RecordTypeDef = TypedDict("RecordTypeDef", {"jsonPath": str, "recordIndex": int}, total=False)

ReplicationDetailsTypeDef = TypedDict(
    "ReplicationDetailsTypeDef",
    {"replicated": bool, "replicatedExternally": bool, "replicationAccounts": List[str]},
    total=False,
)

ResourcesAffectedTypeDef = TypedDict(
    "ResourcesAffectedTypeDef",
    {"s3Bucket": "S3BucketTypeDef", "s3Object": "S3ObjectTypeDef"},
    total=False,
)

S3BucketDefinitionForJobTypeDef = TypedDict(
    "S3BucketDefinitionForJobTypeDef", {"accountId": str, "buckets": List[str]}, total=False
)

S3BucketOwnerTypeDef = TypedDict(
    "S3BucketOwnerTypeDef", {"displayName": str, "id": str}, total=False
)

S3BucketTypeDef = TypedDict(
    "S3BucketTypeDef",
    {
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

_RequiredS3DestinationTypeDef = TypedDict(
    "_RequiredS3DestinationTypeDef", {"bucketName": str, "kmsKeyArn": str}
)
_OptionalS3DestinationTypeDef = TypedDict(
    "_OptionalS3DestinationTypeDef", {"keyPrefix": str}, total=False
)


class S3DestinationTypeDef(_RequiredS3DestinationTypeDef, _OptionalS3DestinationTypeDef):
    pass


S3JobDefinitionTypeDef = TypedDict(
    "S3JobDefinitionTypeDef",
    {"bucketDefinitions": List["S3BucketDefinitionForJobTypeDef"], "scoping": "ScopingTypeDef"},
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
        "storageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "INTELLIGENT_TIERING",
            "DEEP_ARCHIVE",
            "ONEZONE_IA",
            "GLACIER",
        ],
        "tags": List["KeyValuePairTypeDef"],
        "versionId": str,
    },
    total=False,
)

ScopingTypeDef = TypedDict(
    "ScopingTypeDef",
    {"excludes": "JobScopingBlockTypeDef", "includes": "JobScopingBlockTypeDef"},
    total=False,
)

SensitiveDataItemTypeDef = TypedDict(
    "SensitiveDataItemTypeDef",
    {
        "category": Literal[
            "FINANCIAL_INFORMATION", "PERSONAL_INFORMATION", "CREDENTIALS", "CUSTOM_IDENTIFIER"
        ],
        "detections": List["DefaultDetectionTypeDef"],
        "totalCount": int,
    },
    total=False,
)

ServerSideEncryptionTypeDef = TypedDict(
    "ServerSideEncryptionTypeDef",
    {"encryptionType": Literal["NONE", "AES256", "aws:kms", "UNKNOWN"], "kmsMasterKeyId": str},
    total=False,
)

ServiceLimitTypeDef = TypedDict(
    "ServiceLimitTypeDef",
    {"isServiceLimited": bool, "unit": Literal["TERABYTES"], "value": int},
    total=False,
)

SessionContextAttributesTypeDef = TypedDict(
    "SessionContextAttributesTypeDef",
    {"creationDate": datetime, "mfaAuthenticated": bool},
    total=False,
)

SessionContextTypeDef = TypedDict(
    "SessionContextTypeDef",
    {"attributes": "SessionContextAttributesTypeDef", "sessionIssuer": "SessionIssuerTypeDef"},
    total=False,
)

SessionIssuerTypeDef = TypedDict(
    "SessionIssuerTypeDef",
    {"accountId": str, "arn": str, "principalId": str, "type": str, "userName": str},
    total=False,
)

SeverityTypeDef = TypedDict(
    "SeverityTypeDef", {"description": Literal["Low", "Medium", "High"], "score": int}, total=False
)

SimpleScopeTermTypeDef = TypedDict(
    "SimpleScopeTermTypeDef",
    {
        "comparator": Literal["EQ", "GT", "GTE", "LT", "LTE", "NE", "CONTAINS"],
        "key": Literal[
            "BUCKET_CREATION_DATE",
            "OBJECT_EXTENSION",
            "OBJECT_LAST_MODIFIED_DATE",
            "OBJECT_SIZE",
            "TAG",
        ],
        "values": List[str],
    },
    total=False,
)

StatisticsTypeDef = TypedDict(
    "StatisticsTypeDef",
    {"approximateNumberOfObjectsToProcess": float, "numberOfRuns": float},
    total=False,
)

TagScopeTermTypeDef = TypedDict(
    "TagScopeTermTypeDef",
    {
        "comparator": Literal["EQ", "GT", "GTE", "LT", "LTE", "NE", "CONTAINS"],
        "key": str,
        "tagValues": List["TagValuePairTypeDef"],
        "target": Literal["S3_OBJECT"],
    },
    total=False,
)

TagValuePairTypeDef = TypedDict("TagValuePairTypeDef", {"key": str, "value": str}, total=False)

UnprocessedAccountTypeDef = TypedDict(
    "UnprocessedAccountTypeDef",
    {"accountId": str, "errorCode": Literal["ClientError", "InternalError"], "errorMessage": str},
    total=False,
)

UsageByAccountTypeDef = TypedDict(
    "UsageByAccountTypeDef",
    {
        "currency": Literal["USD"],
        "estimatedCost": str,
        "serviceLimit": "ServiceLimitTypeDef",
        "type": Literal["DATA_INVENTORY_EVALUATION", "SENSITIVE_DATA_DISCOVERY"],
    },
    total=False,
)

UsageRecordTypeDef = TypedDict(
    "UsageRecordTypeDef",
    {"accountId": str, "freeTrialStartDate": datetime, "usage": List["UsageByAccountTypeDef"]},
    total=False,
)

UsageTotalTypeDef = TypedDict(
    "UsageTotalTypeDef",
    {
        "currency": Literal["USD"],
        "estimatedCost": str,
        "type": Literal["DATA_INVENTORY_EVALUATION", "SENSITIVE_DATA_DISCOVERY"],
    },
    total=False,
)

UserIdentityRootTypeDef = TypedDict(
    "UserIdentityRootTypeDef", {"accountId": str, "arn": str, "principalId": str}, total=False
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
        "type": Literal[
            "AssumedRole", "IAMUser", "FederatedUser", "Root", "AWSAccount", "AWSService"
        ],
    },
    total=False,
)

UserPausedDetailsTypeDef = TypedDict(
    "UserPausedDetailsTypeDef",
    {"jobExpiresAt": datetime, "jobImminentExpirationHealthEventArn": str, "jobPausedAt": datetime},
    total=False,
)

WeeklyScheduleTypeDef = TypedDict(
    "WeeklyScheduleTypeDef",
    {
        "dayOfWeek": Literal[
            "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"
        ]
    },
    total=False,
)

AccountDetailTypeDef = TypedDict("AccountDetailTypeDef", {"accountId": str, "email": str})

BatchGetCustomDataIdentifiersResponseTypeDef = TypedDict(
    "BatchGetCustomDataIdentifiersResponseTypeDef",
    {
        "customDataIdentifiers": List["BatchGetCustomDataIdentifierSummaryTypeDef"],
        "notFoundIdentifierIds": List[str],
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

BucketSortCriteriaTypeDef = TypedDict(
    "BucketSortCriteriaTypeDef",
    {"attributeName": str, "orderBy": Literal["ASC", "DESC"]},
    total=False,
)

CreateClassificationJobResponseTypeDef = TypedDict(
    "CreateClassificationJobResponseTypeDef", {"jobArn": str, "jobId": str}, total=False
)

CreateCustomDataIdentifierResponseTypeDef = TypedDict(
    "CreateCustomDataIdentifierResponseTypeDef", {"customDataIdentifierId": str}, total=False
)

CreateFindingsFilterResponseTypeDef = TypedDict(
    "CreateFindingsFilterResponseTypeDef", {"arn": str, "id": str}, total=False
)

CreateInvitationsResponseTypeDef = TypedDict(
    "CreateInvitationsResponseTypeDef",
    {"unprocessedAccounts": List["UnprocessedAccountTypeDef"]},
    total=False,
)

CreateMemberResponseTypeDef = TypedDict("CreateMemberResponseTypeDef", {"arn": str}, total=False)

DeclineInvitationsResponseTypeDef = TypedDict(
    "DeclineInvitationsResponseTypeDef",
    {"unprocessedAccounts": List["UnprocessedAccountTypeDef"]},
    total=False,
)

DeleteInvitationsResponseTypeDef = TypedDict(
    "DeleteInvitationsResponseTypeDef",
    {"unprocessedAccounts": List["UnprocessedAccountTypeDef"]},
    total=False,
)

DescribeBucketsResponseTypeDef = TypedDict(
    "DescribeBucketsResponseTypeDef",
    {"buckets": List["BucketMetadataTypeDef"], "nextToken": str},
    total=False,
)

DescribeClassificationJobResponseTypeDef = TypedDict(
    "DescribeClassificationJobResponseTypeDef",
    {
        "clientToken": str,
        "createdAt": datetime,
        "customDataIdentifierIds": List[str],
        "description": str,
        "initialRun": bool,
        "jobArn": str,
        "jobId": str,
        "jobStatus": Literal["RUNNING", "PAUSED", "CANCELLED", "COMPLETE", "IDLE", "USER_PAUSED"],
        "jobType": Literal["ONE_TIME", "SCHEDULED"],
        "lastRunErrorStatus": "LastRunErrorStatusTypeDef",
        "lastRunTime": datetime,
        "name": str,
        "s3JobDefinition": "S3JobDefinitionTypeDef",
        "samplingPercentage": int,
        "scheduleFrequency": "JobScheduleFrequencyTypeDef",
        "statistics": "StatisticsTypeDef",
        "tags": Dict[str, str],
        "userPausedDetails": "UserPausedDetailsTypeDef",
    },
    total=False,
)

DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {"autoEnable": bool, "maxAccountLimitReached": bool},
    total=False,
)

FindingStatisticsSortCriteriaTypeDef = TypedDict(
    "FindingStatisticsSortCriteriaTypeDef",
    {"attributeName": Literal["groupKey", "count"], "orderBy": Literal["ASC", "DESC"]},
    total=False,
)

GetBucketStatisticsResponseTypeDef = TypedDict(
    "GetBucketStatisticsResponseTypeDef",
    {
        "bucketCount": int,
        "bucketCountByEffectivePermission": "BucketCountByEffectivePermissionTypeDef",
        "bucketCountByEncryptionType": "BucketCountByEncryptionTypeTypeDef",
        "bucketCountBySharedAccessType": "BucketCountBySharedAccessTypeTypeDef",
        "classifiableObjectCount": int,
        "classifiableSizeInBytes": int,
        "lastUpdated": datetime,
        "objectCount": int,
        "sizeInBytes": int,
        "sizeInBytesCompressed": int,
        "unclassifiableObjectCount": "ObjectLevelStatisticsTypeDef",
        "unclassifiableObjectSizeInBytes": "ObjectLevelStatisticsTypeDef",
    },
    total=False,
)

GetClassificationExportConfigurationResponseTypeDef = TypedDict(
    "GetClassificationExportConfigurationResponseTypeDef",
    {"configuration": "ClassificationExportConfigurationTypeDef"},
    total=False,
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
        "tags": Dict[str, str],
    },
    total=False,
)

GetFindingStatisticsResponseTypeDef = TypedDict(
    "GetFindingStatisticsResponseTypeDef", {"countsByGroup": List["GroupCountTypeDef"]}, total=False
)

GetFindingsFilterResponseTypeDef = TypedDict(
    "GetFindingsFilterResponseTypeDef",
    {
        "action": Literal["ARCHIVE", "NOOP"],
        "arn": str,
        "description": str,
        "findingCriteria": "FindingCriteriaTypeDef",
        "id": str,
        "name": str,
        "position": int,
        "tags": Dict[str, str],
    },
    total=False,
)

GetFindingsResponseTypeDef = TypedDict(
    "GetFindingsResponseTypeDef", {"findings": List["FindingTypeDef"]}, total=False
)

GetInvitationsCountResponseTypeDef = TypedDict(
    "GetInvitationsCountResponseTypeDef", {"invitationsCount": int}, total=False
)

GetMacieSessionResponseTypeDef = TypedDict(
    "GetMacieSessionResponseTypeDef",
    {
        "createdAt": datetime,
        "findingPublishingFrequency": Literal["FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"],
        "serviceRole": str,
        "status": Literal["PAUSED", "ENABLED"],
        "updatedAt": datetime,
    },
    total=False,
)

GetMasterAccountResponseTypeDef = TypedDict(
    "GetMasterAccountResponseTypeDef", {"master": "InvitationTypeDef"}, total=False
)

GetMemberResponseTypeDef = TypedDict(
    "GetMemberResponseTypeDef",
    {
        "accountId": str,
        "arn": str,
        "email": str,
        "invitedAt": datetime,
        "masterAccountId": str,
        "relationshipStatus": Literal[
            "Enabled",
            "Paused",
            "Invited",
            "Created",
            "Removed",
            "Resigned",
            "EmailVerificationInProgress",
            "EmailVerificationFailed",
            "RegionDisabled",
            "AccountSuspended",
        ],
        "tags": Dict[str, str],
        "updatedAt": datetime,
    },
    total=False,
)

GetUsageStatisticsResponseTypeDef = TypedDict(
    "GetUsageStatisticsResponseTypeDef",
    {"nextToken": str, "records": List["UsageRecordTypeDef"]},
    total=False,
)

GetUsageTotalsResponseTypeDef = TypedDict(
    "GetUsageTotalsResponseTypeDef", {"usageTotals": List["UsageTotalTypeDef"]}, total=False
)

ListClassificationJobsResponseTypeDef = TypedDict(
    "ListClassificationJobsResponseTypeDef",
    {"items": List["JobSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListCustomDataIdentifiersResponseTypeDef = TypedDict(
    "ListCustomDataIdentifiersResponseTypeDef",
    {"items": List["CustomDataIdentifierSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListFindingsFiltersResponseTypeDef = TypedDict(
    "ListFindingsFiltersResponseTypeDef",
    {"findingsFilterListItems": List["FindingsFilterListItemTypeDef"], "nextToken": str},
    total=False,
)

ListFindingsResponseTypeDef = TypedDict(
    "ListFindingsResponseTypeDef", {"findingIds": List[str], "nextToken": str}, total=False
)

ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {"invitations": List["InvitationTypeDef"], "nextToken": str},
    total=False,
)

ListJobsFilterCriteriaTypeDef = TypedDict(
    "ListJobsFilterCriteriaTypeDef",
    {"excludes": List["ListJobsFilterTermTypeDef"], "includes": List["ListJobsFilterTermTypeDef"]},
    total=False,
)

ListJobsSortCriteriaTypeDef = TypedDict(
    "ListJobsSortCriteriaTypeDef",
    {
        "attributeName": Literal["createdAt", "jobStatus", "name", "jobType"],
        "orderBy": Literal["ASC", "DESC"],
    },
    total=False,
)

ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef", {"members": List["MemberTypeDef"], "nextToken": str}, total=False
)

ListOrganizationAdminAccountsResponseTypeDef = TypedDict(
    "ListOrganizationAdminAccountsResponseTypeDef",
    {"adminAccounts": List["AdminAccountTypeDef"], "nextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutClassificationExportConfigurationResponseTypeDef = TypedDict(
    "PutClassificationExportConfigurationResponseTypeDef",
    {"configuration": "ClassificationExportConfigurationTypeDef"},
    total=False,
)

SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef", {"attributeName": str, "orderBy": Literal["ASC", "DESC"]}, total=False
)

TestCustomDataIdentifierResponseTypeDef = TypedDict(
    "TestCustomDataIdentifierResponseTypeDef", {"matchCount": int}, total=False
)

UpdateFindingsFilterResponseTypeDef = TypedDict(
    "UpdateFindingsFilterResponseTypeDef", {"arn": str, "id": str}, total=False
)

UsageStatisticsFilterTypeDef = TypedDict(
    "UsageStatisticsFilterTypeDef",
    {
        "comparator": Literal["GT", "GTE", "LT", "LTE", "EQ", "NE", "CONTAINS"],
        "key": Literal["accountId", "serviceLimit", "freeTrialStartDate", "total"],
        "values": List[str],
    },
    total=False,
)

UsageStatisticsSortByTypeDef = TypedDict(
    "UsageStatisticsSortByTypeDef",
    {
        "key": Literal["accountId", "total", "serviceLimitValue", "freeTrialStartDate"],
        "orderBy": Literal["ASC", "DESC"],
    },
    total=False,
)
