"""
Type annotations for s3control service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/type_defs.html)

Usage::

    ```python
    from mypy_boto3_s3control.type_defs import AbortIncompleteMultipartUploadTypeDef

    data: AbortIncompleteMultipartUploadTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    BucketCannedACLType,
    BucketLocationConstraintType,
    ExpirationStatusType,
    FormatType,
    JobManifestFieldNameType,
    JobManifestFormatType,
    JobReportScopeType,
    JobStatusType,
    NetworkOriginType,
    ObjectLambdaAllowedFeatureType,
    OperationNameType,
    RequestedJobStatusType,
    S3CannedAccessControlListType,
    S3GlacierJobTierType,
    S3GranteeTypeIdentifierType,
    S3MetadataDirectiveType,
    S3ObjectLockLegalHoldStatusType,
    S3ObjectLockModeType,
    S3ObjectLockRetentionModeType,
    S3PermissionType,
    S3SSEAlgorithmType,
    S3StorageClassType,
    TransitionStorageClassType,
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
    "AbortIncompleteMultipartUploadTypeDef",
    "AccessPointTypeDef",
    "AccountLevelTypeDef",
    "ActivityMetricsTypeDef",
    "AwsLambdaTransformationTypeDef",
    "BucketLevelTypeDef",
    "CreateAccessPointForObjectLambdaRequestRequestTypeDef",
    "CreateAccessPointForObjectLambdaResultTypeDef",
    "CreateAccessPointRequestRequestTypeDef",
    "CreateAccessPointResultTypeDef",
    "CreateBucketConfigurationTypeDef",
    "CreateBucketRequestRequestTypeDef",
    "CreateBucketResultTypeDef",
    "CreateJobRequestRequestTypeDef",
    "CreateJobResultTypeDef",
    "DeleteAccessPointForObjectLambdaRequestRequestTypeDef",
    "DeleteAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    "DeleteAccessPointPolicyRequestRequestTypeDef",
    "DeleteAccessPointRequestRequestTypeDef",
    "DeleteBucketLifecycleConfigurationRequestRequestTypeDef",
    "DeleteBucketPolicyRequestRequestTypeDef",
    "DeleteBucketRequestRequestTypeDef",
    "DeleteBucketTaggingRequestRequestTypeDef",
    "DeleteJobTaggingRequestRequestTypeDef",
    "DeletePublicAccessBlockRequestRequestTypeDef",
    "DeleteStorageLensConfigurationRequestRequestTypeDef",
    "DeleteStorageLensConfigurationTaggingRequestRequestTypeDef",
    "DescribeJobRequestRequestTypeDef",
    "DescribeJobResultTypeDef",
    "ExcludeTypeDef",
    "GetAccessPointConfigurationForObjectLambdaRequestRequestTypeDef",
    "GetAccessPointConfigurationForObjectLambdaResultTypeDef",
    "GetAccessPointForObjectLambdaRequestRequestTypeDef",
    "GetAccessPointForObjectLambdaResultTypeDef",
    "GetAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    "GetAccessPointPolicyForObjectLambdaResultTypeDef",
    "GetAccessPointPolicyRequestRequestTypeDef",
    "GetAccessPointPolicyResultTypeDef",
    "GetAccessPointPolicyStatusForObjectLambdaRequestRequestTypeDef",
    "GetAccessPointPolicyStatusForObjectLambdaResultTypeDef",
    "GetAccessPointPolicyStatusRequestRequestTypeDef",
    "GetAccessPointPolicyStatusResultTypeDef",
    "GetAccessPointRequestRequestTypeDef",
    "GetAccessPointResultTypeDef",
    "GetBucketLifecycleConfigurationRequestRequestTypeDef",
    "GetBucketLifecycleConfigurationResultTypeDef",
    "GetBucketPolicyRequestRequestTypeDef",
    "GetBucketPolicyResultTypeDef",
    "GetBucketRequestRequestTypeDef",
    "GetBucketResultTypeDef",
    "GetBucketTaggingRequestRequestTypeDef",
    "GetBucketTaggingResultTypeDef",
    "GetJobTaggingRequestRequestTypeDef",
    "GetJobTaggingResultTypeDef",
    "GetPublicAccessBlockOutputTypeDef",
    "GetPublicAccessBlockRequestRequestTypeDef",
    "GetStorageLensConfigurationRequestRequestTypeDef",
    "GetStorageLensConfigurationResultTypeDef",
    "GetStorageLensConfigurationTaggingRequestRequestTypeDef",
    "GetStorageLensConfigurationTaggingResultTypeDef",
    "IncludeTypeDef",
    "JobDescriptorTypeDef",
    "JobFailureTypeDef",
    "JobListDescriptorTypeDef",
    "JobManifestLocationTypeDef",
    "JobManifestSpecTypeDef",
    "JobManifestTypeDef",
    "JobOperationTypeDef",
    "JobProgressSummaryTypeDef",
    "JobReportTypeDef",
    "LambdaInvokeOperationTypeDef",
    "LifecycleConfigurationTypeDef",
    "LifecycleExpirationTypeDef",
    "LifecycleRuleAndOperatorTypeDef",
    "LifecycleRuleFilterTypeDef",
    "LifecycleRuleTypeDef",
    "ListAccessPointsForObjectLambdaRequestRequestTypeDef",
    "ListAccessPointsForObjectLambdaResultTypeDef",
    "ListAccessPointsRequestRequestTypeDef",
    "ListAccessPointsResultTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListJobsResultTypeDef",
    "ListRegionalBucketsRequestRequestTypeDef",
    "ListRegionalBucketsResultTypeDef",
    "ListStorageLensConfigurationEntryTypeDef",
    "ListStorageLensConfigurationsRequestRequestTypeDef",
    "ListStorageLensConfigurationsResultTypeDef",
    "NoncurrentVersionExpirationTypeDef",
    "NoncurrentVersionTransitionTypeDef",
    "ObjectLambdaAccessPointTypeDef",
    "ObjectLambdaConfigurationTypeDef",
    "ObjectLambdaContentTransformationTypeDef",
    "ObjectLambdaTransformationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PolicyStatusTypeDef",
    "PrefixLevelStorageMetricsTypeDef",
    "PrefixLevelTypeDef",
    "PublicAccessBlockConfigurationTypeDef",
    "PutAccessPointConfigurationForObjectLambdaRequestRequestTypeDef",
    "PutAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    "PutAccessPointPolicyRequestRequestTypeDef",
    "PutBucketLifecycleConfigurationRequestRequestTypeDef",
    "PutBucketPolicyRequestRequestTypeDef",
    "PutBucketTaggingRequestRequestTypeDef",
    "PutJobTaggingRequestRequestTypeDef",
    "PutPublicAccessBlockRequestRequestTypeDef",
    "PutStorageLensConfigurationRequestRequestTypeDef",
    "PutStorageLensConfigurationTaggingRequestRequestTypeDef",
    "RegionalBucketTypeDef",
    "ResponseMetadataTypeDef",
    "S3AccessControlListTypeDef",
    "S3AccessControlPolicyTypeDef",
    "S3BucketDestinationTypeDef",
    "S3CopyObjectOperationTypeDef",
    "S3GrantTypeDef",
    "S3GranteeTypeDef",
    "S3InitiateRestoreObjectOperationTypeDef",
    "S3ObjectLockLegalHoldTypeDef",
    "S3ObjectMetadataTypeDef",
    "S3ObjectOwnerTypeDef",
    "S3RetentionTypeDef",
    "S3SetObjectAclOperationTypeDef",
    "S3SetObjectLegalHoldOperationTypeDef",
    "S3SetObjectRetentionOperationTypeDef",
    "S3SetObjectTaggingOperationTypeDef",
    "S3TagTypeDef",
    "SSEKMSTypeDef",
    "SelectionCriteriaTypeDef",
    "StorageLensAwsOrgTypeDef",
    "StorageLensConfigurationTypeDef",
    "StorageLensDataExportEncryptionTypeDef",
    "StorageLensDataExportTypeDef",
    "StorageLensTagTypeDef",
    "TaggingTypeDef",
    "TransitionTypeDef",
    "UpdateJobPriorityRequestRequestTypeDef",
    "UpdateJobPriorityResultTypeDef",
    "UpdateJobStatusRequestRequestTypeDef",
    "UpdateJobStatusResultTypeDef",
    "VpcConfigurationTypeDef",
)

AbortIncompleteMultipartUploadTypeDef = TypedDict(
    "AbortIncompleteMultipartUploadTypeDef",
    {
        "DaysAfterInitiation": int,
    },
    total=False,
)

_RequiredAccessPointTypeDef = TypedDict(
    "_RequiredAccessPointTypeDef",
    {
        "Name": str,
        "NetworkOrigin": NetworkOriginType,
        "Bucket": str,
    },
)
_OptionalAccessPointTypeDef = TypedDict(
    "_OptionalAccessPointTypeDef",
    {
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "AccessPointArn": str,
        "Alias": str,
    },
    total=False,
)

class AccessPointTypeDef(_RequiredAccessPointTypeDef, _OptionalAccessPointTypeDef):
    pass

_RequiredAccountLevelTypeDef = TypedDict(
    "_RequiredAccountLevelTypeDef",
    {
        "BucketLevel": "BucketLevelTypeDef",
    },
)
_OptionalAccountLevelTypeDef = TypedDict(
    "_OptionalAccountLevelTypeDef",
    {
        "ActivityMetrics": "ActivityMetricsTypeDef",
    },
    total=False,
)

class AccountLevelTypeDef(_RequiredAccountLevelTypeDef, _OptionalAccountLevelTypeDef):
    pass

ActivityMetricsTypeDef = TypedDict(
    "ActivityMetricsTypeDef",
    {
        "IsEnabled": bool,
    },
    total=False,
)

_RequiredAwsLambdaTransformationTypeDef = TypedDict(
    "_RequiredAwsLambdaTransformationTypeDef",
    {
        "FunctionArn": str,
    },
)
_OptionalAwsLambdaTransformationTypeDef = TypedDict(
    "_OptionalAwsLambdaTransformationTypeDef",
    {
        "FunctionPayload": str,
    },
    total=False,
)

class AwsLambdaTransformationTypeDef(
    _RequiredAwsLambdaTransformationTypeDef, _OptionalAwsLambdaTransformationTypeDef
):
    pass

BucketLevelTypeDef = TypedDict(
    "BucketLevelTypeDef",
    {
        "ActivityMetrics": "ActivityMetricsTypeDef",
        "PrefixLevel": "PrefixLevelTypeDef",
    },
    total=False,
)

CreateAccessPointForObjectLambdaRequestRequestTypeDef = TypedDict(
    "CreateAccessPointForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Configuration": "ObjectLambdaConfigurationTypeDef",
    },
)

CreateAccessPointForObjectLambdaResultTypeDef = TypedDict(
    "CreateAccessPointForObjectLambdaResultTypeDef",
    {
        "ObjectLambdaAccessPointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAccessPointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Bucket": str,
    },
)
_OptionalCreateAccessPointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccessPointRequestRequestTypeDef",
    {
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
    },
    total=False,
)

class CreateAccessPointRequestRequestTypeDef(
    _RequiredCreateAccessPointRequestRequestTypeDef, _OptionalCreateAccessPointRequestRequestTypeDef
):
    pass

CreateAccessPointResultTypeDef = TypedDict(
    "CreateAccessPointResultTypeDef",
    {
        "AccessPointArn": str,
        "Alias": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBucketConfigurationTypeDef = TypedDict(
    "CreateBucketConfigurationTypeDef",
    {
        "LocationConstraint": BucketLocationConstraintType,
    },
    total=False,
)

_RequiredCreateBucketRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBucketRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalCreateBucketRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBucketRequestRequestTypeDef",
    {
        "ACL": BucketCannedACLType,
        "CreateBucketConfiguration": "CreateBucketConfigurationTypeDef",
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWrite": str,
        "GrantWriteACP": str,
        "ObjectLockEnabledForBucket": bool,
        "OutpostId": str,
    },
    total=False,
)

class CreateBucketRequestRequestTypeDef(
    _RequiredCreateBucketRequestRequestTypeDef, _OptionalCreateBucketRequestRequestTypeDef
):
    pass

CreateBucketResultTypeDef = TypedDict(
    "CreateBucketResultTypeDef",
    {
        "Location": str,
        "BucketArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateJobRequestRequestTypeDef",
    {
        "AccountId": str,
        "Operation": "JobOperationTypeDef",
        "Report": "JobReportTypeDef",
        "ClientRequestToken": str,
        "Manifest": "JobManifestTypeDef",
        "Priority": int,
        "RoleArn": str,
    },
)
_OptionalCreateJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateJobRequestRequestTypeDef",
    {
        "ConfirmationRequired": bool,
        "Description": str,
        "Tags": List["S3TagTypeDef"],
    },
    total=False,
)

class CreateJobRequestRequestTypeDef(
    _RequiredCreateJobRequestRequestTypeDef, _OptionalCreateJobRequestRequestTypeDef
):
    pass

CreateJobResultTypeDef = TypedDict(
    "CreateJobResultTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAccessPointForObjectLambdaRequestRequestTypeDef = TypedDict(
    "DeleteAccessPointForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

DeleteAccessPointPolicyForObjectLambdaRequestRequestTypeDef = TypedDict(
    "DeleteAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

DeleteAccessPointPolicyRequestRequestTypeDef = TypedDict(
    "DeleteAccessPointPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

DeleteAccessPointRequestRequestTypeDef = TypedDict(
    "DeleteAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

DeleteBucketLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteBucketLifecycleConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

DeleteBucketPolicyRequestRequestTypeDef = TypedDict(
    "DeleteBucketPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

DeleteBucketRequestRequestTypeDef = TypedDict(
    "DeleteBucketRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

DeleteBucketTaggingRequestRequestTypeDef = TypedDict(
    "DeleteBucketTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

DeleteJobTaggingRequestRequestTypeDef = TypedDict(
    "DeleteJobTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
    },
)

DeletePublicAccessBlockRequestRequestTypeDef = TypedDict(
    "DeletePublicAccessBlockRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

DeleteStorageLensConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteStorageLensConfigurationRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
    },
)

DeleteStorageLensConfigurationTaggingRequestRequestTypeDef = TypedDict(
    "DeleteStorageLensConfigurationTaggingRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
    },
)

DescribeJobRequestRequestTypeDef = TypedDict(
    "DescribeJobRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
    },
)

DescribeJobResultTypeDef = TypedDict(
    "DescribeJobResultTypeDef",
    {
        "Job": "JobDescriptorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExcludeTypeDef = TypedDict(
    "ExcludeTypeDef",
    {
        "Buckets": List[str],
        "Regions": List[str],
    },
    total=False,
)

GetAccessPointConfigurationForObjectLambdaRequestRequestTypeDef = TypedDict(
    "GetAccessPointConfigurationForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointConfigurationForObjectLambdaResultTypeDef = TypedDict(
    "GetAccessPointConfigurationForObjectLambdaResultTypeDef",
    {
        "Configuration": "ObjectLambdaConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessPointForObjectLambdaRequestRequestTypeDef = TypedDict(
    "GetAccessPointForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointForObjectLambdaResultTypeDef = TypedDict(
    "GetAccessPointForObjectLambdaResultTypeDef",
    {
        "Name": str,
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
        "CreationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessPointPolicyForObjectLambdaRequestRequestTypeDef = TypedDict(
    "GetAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointPolicyForObjectLambdaResultTypeDef = TypedDict(
    "GetAccessPointPolicyForObjectLambdaResultTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessPointPolicyRequestRequestTypeDef = TypedDict(
    "GetAccessPointPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointPolicyResultTypeDef = TypedDict(
    "GetAccessPointPolicyResultTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessPointPolicyStatusForObjectLambdaRequestRequestTypeDef = TypedDict(
    "GetAccessPointPolicyStatusForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointPolicyStatusForObjectLambdaResultTypeDef = TypedDict(
    "GetAccessPointPolicyStatusForObjectLambdaResultTypeDef",
    {
        "PolicyStatus": "PolicyStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessPointPolicyStatusRequestRequestTypeDef = TypedDict(
    "GetAccessPointPolicyStatusRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointPolicyStatusResultTypeDef = TypedDict(
    "GetAccessPointPolicyStatusResultTypeDef",
    {
        "PolicyStatus": "PolicyStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessPointRequestRequestTypeDef = TypedDict(
    "GetAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointResultTypeDef = TypedDict(
    "GetAccessPointResultTypeDef",
    {
        "Name": str,
        "Bucket": str,
        "NetworkOrigin": NetworkOriginType,
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
        "CreationDate": datetime,
        "Alias": str,
        "AccessPointArn": str,
        "Endpoints": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "GetBucketLifecycleConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

GetBucketLifecycleConfigurationResultTypeDef = TypedDict(
    "GetBucketLifecycleConfigurationResultTypeDef",
    {
        "Rules": List["LifecycleRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketPolicyRequestRequestTypeDef = TypedDict(
    "GetBucketPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

GetBucketPolicyResultTypeDef = TypedDict(
    "GetBucketPolicyResultTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketRequestRequestTypeDef = TypedDict(
    "GetBucketRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

GetBucketResultTypeDef = TypedDict(
    "GetBucketResultTypeDef",
    {
        "Bucket": str,
        "PublicAccessBlockEnabled": bool,
        "CreationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketTaggingRequestRequestTypeDef = TypedDict(
    "GetBucketTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

GetBucketTaggingResultTypeDef = TypedDict(
    "GetBucketTaggingResultTypeDef",
    {
        "TagSet": List["S3TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobTaggingRequestRequestTypeDef = TypedDict(
    "GetJobTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
    },
)

GetJobTaggingResultTypeDef = TypedDict(
    "GetJobTaggingResultTypeDef",
    {
        "Tags": List["S3TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPublicAccessBlockOutputTypeDef = TypedDict(
    "GetPublicAccessBlockOutputTypeDef",
    {
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPublicAccessBlockRequestRequestTypeDef = TypedDict(
    "GetPublicAccessBlockRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

GetStorageLensConfigurationRequestRequestTypeDef = TypedDict(
    "GetStorageLensConfigurationRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
    },
)

GetStorageLensConfigurationResultTypeDef = TypedDict(
    "GetStorageLensConfigurationResultTypeDef",
    {
        "StorageLensConfiguration": "StorageLensConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStorageLensConfigurationTaggingRequestRequestTypeDef = TypedDict(
    "GetStorageLensConfigurationTaggingRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
    },
)

GetStorageLensConfigurationTaggingResultTypeDef = TypedDict(
    "GetStorageLensConfigurationTaggingResultTypeDef",
    {
        "Tags": List["StorageLensTagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IncludeTypeDef = TypedDict(
    "IncludeTypeDef",
    {
        "Buckets": List[str],
        "Regions": List[str],
    },
    total=False,
)

JobDescriptorTypeDef = TypedDict(
    "JobDescriptorTypeDef",
    {
        "JobId": str,
        "ConfirmationRequired": bool,
        "Description": str,
        "JobArn": str,
        "Status": JobStatusType,
        "Manifest": "JobManifestTypeDef",
        "Operation": "JobOperationTypeDef",
        "Priority": int,
        "ProgressSummary": "JobProgressSummaryTypeDef",
        "StatusUpdateReason": str,
        "FailureReasons": List["JobFailureTypeDef"],
        "Report": "JobReportTypeDef",
        "CreationTime": datetime,
        "TerminationDate": datetime,
        "RoleArn": str,
        "SuspendedDate": datetime,
        "SuspendedCause": str,
    },
    total=False,
)

JobFailureTypeDef = TypedDict(
    "JobFailureTypeDef",
    {
        "FailureCode": str,
        "FailureReason": str,
    },
    total=False,
)

JobListDescriptorTypeDef = TypedDict(
    "JobListDescriptorTypeDef",
    {
        "JobId": str,
        "Description": str,
        "Operation": OperationNameType,
        "Priority": int,
        "Status": JobStatusType,
        "CreationTime": datetime,
        "TerminationDate": datetime,
        "ProgressSummary": "JobProgressSummaryTypeDef",
    },
    total=False,
)

_RequiredJobManifestLocationTypeDef = TypedDict(
    "_RequiredJobManifestLocationTypeDef",
    {
        "ObjectArn": str,
        "ETag": str,
    },
)
_OptionalJobManifestLocationTypeDef = TypedDict(
    "_OptionalJobManifestLocationTypeDef",
    {
        "ObjectVersionId": str,
    },
    total=False,
)

class JobManifestLocationTypeDef(
    _RequiredJobManifestLocationTypeDef, _OptionalJobManifestLocationTypeDef
):
    pass

_RequiredJobManifestSpecTypeDef = TypedDict(
    "_RequiredJobManifestSpecTypeDef",
    {
        "Format": JobManifestFormatType,
    },
)
_OptionalJobManifestSpecTypeDef = TypedDict(
    "_OptionalJobManifestSpecTypeDef",
    {
        "Fields": List[JobManifestFieldNameType],
    },
    total=False,
)

class JobManifestSpecTypeDef(_RequiredJobManifestSpecTypeDef, _OptionalJobManifestSpecTypeDef):
    pass

JobManifestTypeDef = TypedDict(
    "JobManifestTypeDef",
    {
        "Spec": "JobManifestSpecTypeDef",
        "Location": "JobManifestLocationTypeDef",
    },
)

JobOperationTypeDef = TypedDict(
    "JobOperationTypeDef",
    {
        "LambdaInvoke": "LambdaInvokeOperationTypeDef",
        "S3PutObjectCopy": "S3CopyObjectOperationTypeDef",
        "S3PutObjectAcl": "S3SetObjectAclOperationTypeDef",
        "S3PutObjectTagging": "S3SetObjectTaggingOperationTypeDef",
        "S3DeleteObjectTagging": Dict[str, Any],
        "S3InitiateRestoreObject": "S3InitiateRestoreObjectOperationTypeDef",
        "S3PutObjectLegalHold": "S3SetObjectLegalHoldOperationTypeDef",
        "S3PutObjectRetention": "S3SetObjectRetentionOperationTypeDef",
    },
    total=False,
)

JobProgressSummaryTypeDef = TypedDict(
    "JobProgressSummaryTypeDef",
    {
        "TotalNumberOfTasks": int,
        "NumberOfTasksSucceeded": int,
        "NumberOfTasksFailed": int,
    },
    total=False,
)

_RequiredJobReportTypeDef = TypedDict(
    "_RequiredJobReportTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalJobReportTypeDef = TypedDict(
    "_OptionalJobReportTypeDef",
    {
        "Bucket": str,
        "Format": Literal["Report_CSV_20180820"],
        "Prefix": str,
        "ReportScope": JobReportScopeType,
    },
    total=False,
)

class JobReportTypeDef(_RequiredJobReportTypeDef, _OptionalJobReportTypeDef):
    pass

LambdaInvokeOperationTypeDef = TypedDict(
    "LambdaInvokeOperationTypeDef",
    {
        "FunctionArn": str,
    },
    total=False,
)

LifecycleConfigurationTypeDef = TypedDict(
    "LifecycleConfigurationTypeDef",
    {
        "Rules": List["LifecycleRuleTypeDef"],
    },
    total=False,
)

LifecycleExpirationTypeDef = TypedDict(
    "LifecycleExpirationTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "ExpiredObjectDeleteMarker": bool,
    },
    total=False,
)

LifecycleRuleAndOperatorTypeDef = TypedDict(
    "LifecycleRuleAndOperatorTypeDef",
    {
        "Prefix": str,
        "Tags": List["S3TagTypeDef"],
    },
    total=False,
)

LifecycleRuleFilterTypeDef = TypedDict(
    "LifecycleRuleFilterTypeDef",
    {
        "Prefix": str,
        "Tag": "S3TagTypeDef",
        "And": "LifecycleRuleAndOperatorTypeDef",
    },
    total=False,
)

_RequiredLifecycleRuleTypeDef = TypedDict(
    "_RequiredLifecycleRuleTypeDef",
    {
        "Status": ExpirationStatusType,
    },
)
_OptionalLifecycleRuleTypeDef = TypedDict(
    "_OptionalLifecycleRuleTypeDef",
    {
        "Expiration": "LifecycleExpirationTypeDef",
        "ID": str,
        "Filter": "LifecycleRuleFilterTypeDef",
        "Transitions": List["TransitionTypeDef"],
        "NoncurrentVersionTransitions": List["NoncurrentVersionTransitionTypeDef"],
        "NoncurrentVersionExpiration": "NoncurrentVersionExpirationTypeDef",
        "AbortIncompleteMultipartUpload": "AbortIncompleteMultipartUploadTypeDef",
    },
    total=False,
)

class LifecycleRuleTypeDef(_RequiredLifecycleRuleTypeDef, _OptionalLifecycleRuleTypeDef):
    pass

_RequiredListAccessPointsForObjectLambdaRequestRequestTypeDef = TypedDict(
    "_RequiredListAccessPointsForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListAccessPointsForObjectLambdaRequestRequestTypeDef = TypedDict(
    "_OptionalListAccessPointsForObjectLambdaRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListAccessPointsForObjectLambdaRequestRequestTypeDef(
    _RequiredListAccessPointsForObjectLambdaRequestRequestTypeDef,
    _OptionalListAccessPointsForObjectLambdaRequestRequestTypeDef,
):
    pass

ListAccessPointsForObjectLambdaResultTypeDef = TypedDict(
    "ListAccessPointsForObjectLambdaResultTypeDef",
    {
        "ObjectLambdaAccessPointList": List["ObjectLambdaAccessPointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAccessPointsRequestRequestTypeDef = TypedDict(
    "_RequiredListAccessPointsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListAccessPointsRequestRequestTypeDef = TypedDict(
    "_OptionalListAccessPointsRequestRequestTypeDef",
    {
        "Bucket": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListAccessPointsRequestRequestTypeDef(
    _RequiredListAccessPointsRequestRequestTypeDef, _OptionalListAccessPointsRequestRequestTypeDef
):
    pass

ListAccessPointsResultTypeDef = TypedDict(
    "ListAccessPointsResultTypeDef",
    {
        "AccessPointList": List["AccessPointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListJobsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListJobsRequestRequestTypeDef",
    {
        "JobStatuses": List[JobStatusType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListJobsRequestRequestTypeDef(
    _RequiredListJobsRequestRequestTypeDef, _OptionalListJobsRequestRequestTypeDef
):
    pass

ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef",
    {
        "NextToken": str,
        "Jobs": List["JobListDescriptorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRegionalBucketsRequestRequestTypeDef = TypedDict(
    "_RequiredListRegionalBucketsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListRegionalBucketsRequestRequestTypeDef = TypedDict(
    "_OptionalListRegionalBucketsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "OutpostId": str,
    },
    total=False,
)

class ListRegionalBucketsRequestRequestTypeDef(
    _RequiredListRegionalBucketsRequestRequestTypeDef,
    _OptionalListRegionalBucketsRequestRequestTypeDef,
):
    pass

ListRegionalBucketsResultTypeDef = TypedDict(
    "ListRegionalBucketsResultTypeDef",
    {
        "RegionalBucketList": List["RegionalBucketTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStorageLensConfigurationEntryTypeDef = TypedDict(
    "_RequiredListStorageLensConfigurationEntryTypeDef",
    {
        "Id": str,
        "StorageLensArn": str,
        "HomeRegion": str,
    },
)
_OptionalListStorageLensConfigurationEntryTypeDef = TypedDict(
    "_OptionalListStorageLensConfigurationEntryTypeDef",
    {
        "IsEnabled": bool,
    },
    total=False,
)

class ListStorageLensConfigurationEntryTypeDef(
    _RequiredListStorageLensConfigurationEntryTypeDef,
    _OptionalListStorageLensConfigurationEntryTypeDef,
):
    pass

_RequiredListStorageLensConfigurationsRequestRequestTypeDef = TypedDict(
    "_RequiredListStorageLensConfigurationsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListStorageLensConfigurationsRequestRequestTypeDef = TypedDict(
    "_OptionalListStorageLensConfigurationsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListStorageLensConfigurationsRequestRequestTypeDef(
    _RequiredListStorageLensConfigurationsRequestRequestTypeDef,
    _OptionalListStorageLensConfigurationsRequestRequestTypeDef,
):
    pass

ListStorageLensConfigurationsResultTypeDef = TypedDict(
    "ListStorageLensConfigurationsResultTypeDef",
    {
        "NextToken": str,
        "StorageLensConfigurationList": List["ListStorageLensConfigurationEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NoncurrentVersionExpirationTypeDef = TypedDict(
    "NoncurrentVersionExpirationTypeDef",
    {
        "NoncurrentDays": int,
    },
    total=False,
)

NoncurrentVersionTransitionTypeDef = TypedDict(
    "NoncurrentVersionTransitionTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": TransitionStorageClassType,
    },
    total=False,
)

_RequiredObjectLambdaAccessPointTypeDef = TypedDict(
    "_RequiredObjectLambdaAccessPointTypeDef",
    {
        "Name": str,
    },
)
_OptionalObjectLambdaAccessPointTypeDef = TypedDict(
    "_OptionalObjectLambdaAccessPointTypeDef",
    {
        "ObjectLambdaAccessPointArn": str,
    },
    total=False,
)

class ObjectLambdaAccessPointTypeDef(
    _RequiredObjectLambdaAccessPointTypeDef, _OptionalObjectLambdaAccessPointTypeDef
):
    pass

_RequiredObjectLambdaConfigurationTypeDef = TypedDict(
    "_RequiredObjectLambdaConfigurationTypeDef",
    {
        "SupportingAccessPoint": str,
        "TransformationConfigurations": List["ObjectLambdaTransformationConfigurationTypeDef"],
    },
)
_OptionalObjectLambdaConfigurationTypeDef = TypedDict(
    "_OptionalObjectLambdaConfigurationTypeDef",
    {
        "CloudWatchMetricsEnabled": bool,
        "AllowedFeatures": List[ObjectLambdaAllowedFeatureType],
    },
    total=False,
)

class ObjectLambdaConfigurationTypeDef(
    _RequiredObjectLambdaConfigurationTypeDef, _OptionalObjectLambdaConfigurationTypeDef
):
    pass

ObjectLambdaContentTransformationTypeDef = TypedDict(
    "ObjectLambdaContentTransformationTypeDef",
    {
        "AwsLambda": "AwsLambdaTransformationTypeDef",
    },
    total=False,
)

ObjectLambdaTransformationConfigurationTypeDef = TypedDict(
    "ObjectLambdaTransformationConfigurationTypeDef",
    {
        "Actions": List[Literal["GetObject"]],
        "ContentTransformation": "ObjectLambdaContentTransformationTypeDef",
    },
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

PolicyStatusTypeDef = TypedDict(
    "PolicyStatusTypeDef",
    {
        "IsPublic": bool,
    },
    total=False,
)

PrefixLevelStorageMetricsTypeDef = TypedDict(
    "PrefixLevelStorageMetricsTypeDef",
    {
        "IsEnabled": bool,
        "SelectionCriteria": "SelectionCriteriaTypeDef",
    },
    total=False,
)

PrefixLevelTypeDef = TypedDict(
    "PrefixLevelTypeDef",
    {
        "StorageMetrics": "PrefixLevelStorageMetricsTypeDef",
    },
)

PublicAccessBlockConfigurationTypeDef = TypedDict(
    "PublicAccessBlockConfigurationTypeDef",
    {
        "BlockPublicAcls": bool,
        "IgnorePublicAcls": bool,
        "BlockPublicPolicy": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)

PutAccessPointConfigurationForObjectLambdaRequestRequestTypeDef = TypedDict(
    "PutAccessPointConfigurationForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Configuration": "ObjectLambdaConfigurationTypeDef",
    },
)

PutAccessPointPolicyForObjectLambdaRequestRequestTypeDef = TypedDict(
    "PutAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Policy": str,
    },
)

PutAccessPointPolicyRequestRequestTypeDef = TypedDict(
    "PutAccessPointPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Policy": str,
    },
)

_RequiredPutBucketLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketLifecycleConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)
_OptionalPutBucketLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketLifecycleConfigurationRequestRequestTypeDef",
    {
        "LifecycleConfiguration": "LifecycleConfigurationTypeDef",
    },
    total=False,
)

class PutBucketLifecycleConfigurationRequestRequestTypeDef(
    _RequiredPutBucketLifecycleConfigurationRequestRequestTypeDef,
    _OptionalPutBucketLifecycleConfigurationRequestRequestTypeDef,
):
    pass

_RequiredPutBucketPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Policy": str,
    },
)
_OptionalPutBucketPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketPolicyRequestRequestTypeDef",
    {
        "ConfirmRemoveSelfBucketAccess": bool,
    },
    total=False,
)

class PutBucketPolicyRequestRequestTypeDef(
    _RequiredPutBucketPolicyRequestRequestTypeDef, _OptionalPutBucketPolicyRequestRequestTypeDef
):
    pass

PutBucketTaggingRequestRequestTypeDef = TypedDict(
    "PutBucketTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Tagging": "TaggingTypeDef",
    },
)

PutJobTaggingRequestRequestTypeDef = TypedDict(
    "PutJobTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
        "Tags": List["S3TagTypeDef"],
    },
)

PutPublicAccessBlockRequestRequestTypeDef = TypedDict(
    "PutPublicAccessBlockRequestRequestTypeDef",
    {
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
        "AccountId": str,
    },
)

_RequiredPutStorageLensConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutStorageLensConfigurationRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
        "StorageLensConfiguration": "StorageLensConfigurationTypeDef",
    },
)
_OptionalPutStorageLensConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutStorageLensConfigurationRequestRequestTypeDef",
    {
        "Tags": List["StorageLensTagTypeDef"],
    },
    total=False,
)

class PutStorageLensConfigurationRequestRequestTypeDef(
    _RequiredPutStorageLensConfigurationRequestRequestTypeDef,
    _OptionalPutStorageLensConfigurationRequestRequestTypeDef,
):
    pass

PutStorageLensConfigurationTaggingRequestRequestTypeDef = TypedDict(
    "PutStorageLensConfigurationTaggingRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
        "Tags": List["StorageLensTagTypeDef"],
    },
)

_RequiredRegionalBucketTypeDef = TypedDict(
    "_RequiredRegionalBucketTypeDef",
    {
        "Bucket": str,
        "PublicAccessBlockEnabled": bool,
        "CreationDate": datetime,
    },
)
_OptionalRegionalBucketTypeDef = TypedDict(
    "_OptionalRegionalBucketTypeDef",
    {
        "BucketArn": str,
        "OutpostId": str,
    },
    total=False,
)

class RegionalBucketTypeDef(_RequiredRegionalBucketTypeDef, _OptionalRegionalBucketTypeDef):
    pass

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

_RequiredS3AccessControlListTypeDef = TypedDict(
    "_RequiredS3AccessControlListTypeDef",
    {
        "Owner": "S3ObjectOwnerTypeDef",
    },
)
_OptionalS3AccessControlListTypeDef = TypedDict(
    "_OptionalS3AccessControlListTypeDef",
    {
        "Grants": List["S3GrantTypeDef"],
    },
    total=False,
)

class S3AccessControlListTypeDef(
    _RequiredS3AccessControlListTypeDef, _OptionalS3AccessControlListTypeDef
):
    pass

S3AccessControlPolicyTypeDef = TypedDict(
    "S3AccessControlPolicyTypeDef",
    {
        "AccessControlList": "S3AccessControlListTypeDef",
        "CannedAccessControlList": S3CannedAccessControlListType,
    },
    total=False,
)

_RequiredS3BucketDestinationTypeDef = TypedDict(
    "_RequiredS3BucketDestinationTypeDef",
    {
        "Format": FormatType,
        "OutputSchemaVersion": Literal["V_1"],
        "AccountId": str,
        "Arn": str,
    },
)
_OptionalS3BucketDestinationTypeDef = TypedDict(
    "_OptionalS3BucketDestinationTypeDef",
    {
        "Prefix": str,
        "Encryption": "StorageLensDataExportEncryptionTypeDef",
    },
    total=False,
)

class S3BucketDestinationTypeDef(
    _RequiredS3BucketDestinationTypeDef, _OptionalS3BucketDestinationTypeDef
):
    pass

S3CopyObjectOperationTypeDef = TypedDict(
    "S3CopyObjectOperationTypeDef",
    {
        "TargetResource": str,
        "CannedAccessControlList": S3CannedAccessControlListType,
        "AccessControlGrants": List["S3GrantTypeDef"],
        "MetadataDirective": S3MetadataDirectiveType,
        "ModifiedSinceConstraint": Union[datetime, str],
        "NewObjectMetadata": "S3ObjectMetadataTypeDef",
        "NewObjectTagging": List["S3TagTypeDef"],
        "RedirectLocation": str,
        "RequesterPays": bool,
        "StorageClass": S3StorageClassType,
        "UnModifiedSinceConstraint": Union[datetime, str],
        "SSEAwsKmsKeyId": str,
        "TargetKeyPrefix": str,
        "ObjectLockLegalHoldStatus": S3ObjectLockLegalHoldStatusType,
        "ObjectLockMode": S3ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "BucketKeyEnabled": bool,
    },
    total=False,
)

S3GrantTypeDef = TypedDict(
    "S3GrantTypeDef",
    {
        "Grantee": "S3GranteeTypeDef",
        "Permission": S3PermissionType,
    },
    total=False,
)

S3GranteeTypeDef = TypedDict(
    "S3GranteeTypeDef",
    {
        "TypeIdentifier": S3GranteeTypeIdentifierType,
        "Identifier": str,
        "DisplayName": str,
    },
    total=False,
)

S3InitiateRestoreObjectOperationTypeDef = TypedDict(
    "S3InitiateRestoreObjectOperationTypeDef",
    {
        "ExpirationInDays": int,
        "GlacierJobTier": S3GlacierJobTierType,
    },
    total=False,
)

S3ObjectLockLegalHoldTypeDef = TypedDict(
    "S3ObjectLockLegalHoldTypeDef",
    {
        "Status": S3ObjectLockLegalHoldStatusType,
    },
)

S3ObjectMetadataTypeDef = TypedDict(
    "S3ObjectMetadataTypeDef",
    {
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "UserMetadata": Dict[str, str],
        "ContentLength": int,
        "ContentMD5": str,
        "ContentType": str,
        "HttpExpiresDate": Union[datetime, str],
        "RequesterCharged": bool,
        "SSEAlgorithm": S3SSEAlgorithmType,
    },
    total=False,
)

S3ObjectOwnerTypeDef = TypedDict(
    "S3ObjectOwnerTypeDef",
    {
        "ID": str,
        "DisplayName": str,
    },
    total=False,
)

S3RetentionTypeDef = TypedDict(
    "S3RetentionTypeDef",
    {
        "RetainUntilDate": Union[datetime, str],
        "Mode": S3ObjectLockRetentionModeType,
    },
    total=False,
)

S3SetObjectAclOperationTypeDef = TypedDict(
    "S3SetObjectAclOperationTypeDef",
    {
        "AccessControlPolicy": "S3AccessControlPolicyTypeDef",
    },
    total=False,
)

S3SetObjectLegalHoldOperationTypeDef = TypedDict(
    "S3SetObjectLegalHoldOperationTypeDef",
    {
        "LegalHold": "S3ObjectLockLegalHoldTypeDef",
    },
)

_RequiredS3SetObjectRetentionOperationTypeDef = TypedDict(
    "_RequiredS3SetObjectRetentionOperationTypeDef",
    {
        "Retention": "S3RetentionTypeDef",
    },
)
_OptionalS3SetObjectRetentionOperationTypeDef = TypedDict(
    "_OptionalS3SetObjectRetentionOperationTypeDef",
    {
        "BypassGovernanceRetention": bool,
    },
    total=False,
)

class S3SetObjectRetentionOperationTypeDef(
    _RequiredS3SetObjectRetentionOperationTypeDef, _OptionalS3SetObjectRetentionOperationTypeDef
):
    pass

S3SetObjectTaggingOperationTypeDef = TypedDict(
    "S3SetObjectTaggingOperationTypeDef",
    {
        "TagSet": List["S3TagTypeDef"],
    },
    total=False,
)

S3TagTypeDef = TypedDict(
    "S3TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

SSEKMSTypeDef = TypedDict(
    "SSEKMSTypeDef",
    {
        "KeyId": str,
    },
)

SelectionCriteriaTypeDef = TypedDict(
    "SelectionCriteriaTypeDef",
    {
        "Delimiter": str,
        "MaxDepth": int,
        "MinStorageBytesPercentage": float,
    },
    total=False,
)

StorageLensAwsOrgTypeDef = TypedDict(
    "StorageLensAwsOrgTypeDef",
    {
        "Arn": str,
    },
)

_RequiredStorageLensConfigurationTypeDef = TypedDict(
    "_RequiredStorageLensConfigurationTypeDef",
    {
        "Id": str,
        "AccountLevel": "AccountLevelTypeDef",
        "IsEnabled": bool,
    },
)
_OptionalStorageLensConfigurationTypeDef = TypedDict(
    "_OptionalStorageLensConfigurationTypeDef",
    {
        "Include": "IncludeTypeDef",
        "Exclude": "ExcludeTypeDef",
        "DataExport": "StorageLensDataExportTypeDef",
        "AwsOrg": "StorageLensAwsOrgTypeDef",
        "StorageLensArn": str,
    },
    total=False,
)

class StorageLensConfigurationTypeDef(
    _RequiredStorageLensConfigurationTypeDef, _OptionalStorageLensConfigurationTypeDef
):
    pass

StorageLensDataExportEncryptionTypeDef = TypedDict(
    "StorageLensDataExportEncryptionTypeDef",
    {
        "SSES3": Dict[str, Any],
        "SSEKMS": "SSEKMSTypeDef",
    },
    total=False,
)

StorageLensDataExportTypeDef = TypedDict(
    "StorageLensDataExportTypeDef",
    {
        "S3BucketDestination": "S3BucketDestinationTypeDef",
    },
)

StorageLensTagTypeDef = TypedDict(
    "StorageLensTagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TaggingTypeDef = TypedDict(
    "TaggingTypeDef",
    {
        "TagSet": List["S3TagTypeDef"],
    },
)

TransitionTypeDef = TypedDict(
    "TransitionTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": TransitionStorageClassType,
    },
    total=False,
)

UpdateJobPriorityRequestRequestTypeDef = TypedDict(
    "UpdateJobPriorityRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
        "Priority": int,
    },
)

UpdateJobPriorityResultTypeDef = TypedDict(
    "UpdateJobPriorityResultTypeDef",
    {
        "JobId": str,
        "Priority": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateJobStatusRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateJobStatusRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
        "RequestedJobStatus": RequestedJobStatusType,
    },
)
_OptionalUpdateJobStatusRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateJobStatusRequestRequestTypeDef",
    {
        "StatusUpdateReason": str,
    },
    total=False,
)

class UpdateJobStatusRequestRequestTypeDef(
    _RequiredUpdateJobStatusRequestRequestTypeDef, _OptionalUpdateJobStatusRequestRequestTypeDef
):
    pass

UpdateJobStatusResultTypeDef = TypedDict(
    "UpdateJobStatusResultTypeDef",
    {
        "JobId": str,
        "Status": JobStatusType,
        "StatusUpdateReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "VpcId": str,
    },
)
