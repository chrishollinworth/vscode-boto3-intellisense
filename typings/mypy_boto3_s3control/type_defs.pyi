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
    AsyncOperationNameType,
    BucketCannedACLType,
    BucketLocationConstraintType,
    BucketVersioningStatusType,
    DeleteMarkerReplicationStatusType,
    ExistingObjectReplicationStatusType,
    ExpirationStatusType,
    FormatType,
    GranteeTypeType,
    JobManifestFieldNameType,
    JobManifestFormatType,
    JobReportScopeType,
    JobStatusType,
    MetricsStatusType,
    MFADeleteStatusType,
    MFADeleteType,
    MultiRegionAccessPointStatusType,
    NetworkOriginType,
    ObjectLambdaAccessPointAliasStatusType,
    ObjectLambdaAllowedFeatureType,
    ObjectLambdaTransformationConfigurationActionType,
    OperationNameType,
    PermissionType,
    PrivilegeType,
    ReplicaModificationsStatusType,
    ReplicationRuleStatusType,
    ReplicationStatusType,
    ReplicationStorageClassType,
    ReplicationTimeStatusType,
    RequestedJobStatusType,
    S3CannedAccessControlListType,
    S3ChecksumAlgorithmType,
    S3GlacierJobTierType,
    S3GranteeTypeIdentifierType,
    S3MetadataDirectiveType,
    S3ObjectLockLegalHoldStatusType,
    S3ObjectLockModeType,
    S3ObjectLockRetentionModeType,
    S3PermissionType,
    S3SSEAlgorithmType,
    S3StorageClassType,
    SseKmsEncryptedObjectsStatusType,
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
    "AccessControlTranslationTypeDef",
    "AccessGrantsLocationConfigurationTypeDef",
    "AccessPointTypeDef",
    "AccountLevelTypeDef",
    "ActivityMetricsTypeDef",
    "AdvancedCostOptimizationMetricsTypeDef",
    "AdvancedDataProtectionMetricsTypeDef",
    "AssociateAccessGrantsIdentityCenterRequestRequestTypeDef",
    "AsyncErrorDetailsTypeDef",
    "AsyncOperationTypeDef",
    "AsyncRequestParametersTypeDef",
    "AsyncResponseDetailsTypeDef",
    "AwsLambdaTransformationTypeDef",
    "BucketLevelTypeDef",
    "CloudWatchMetricsTypeDef",
    "CreateAccessGrantRequestRequestTypeDef",
    "CreateAccessGrantResultTypeDef",
    "CreateAccessGrantsInstanceRequestRequestTypeDef",
    "CreateAccessGrantsInstanceResultTypeDef",
    "CreateAccessGrantsLocationRequestRequestTypeDef",
    "CreateAccessGrantsLocationResultTypeDef",
    "CreateAccessPointForObjectLambdaRequestRequestTypeDef",
    "CreateAccessPointForObjectLambdaResultTypeDef",
    "CreateAccessPointRequestRequestTypeDef",
    "CreateAccessPointResultTypeDef",
    "CreateBucketConfigurationTypeDef",
    "CreateBucketRequestRequestTypeDef",
    "CreateBucketResultTypeDef",
    "CreateJobRequestRequestTypeDef",
    "CreateJobResultTypeDef",
    "CreateMultiRegionAccessPointInputTypeDef",
    "CreateMultiRegionAccessPointRequestRequestTypeDef",
    "CreateMultiRegionAccessPointResultTypeDef",
    "CreateStorageLensGroupRequestRequestTypeDef",
    "CredentialsTypeDef",
    "DeleteAccessGrantRequestRequestTypeDef",
    "DeleteAccessGrantsInstanceRequestRequestTypeDef",
    "DeleteAccessGrantsInstanceResourcePolicyRequestRequestTypeDef",
    "DeleteAccessGrantsLocationRequestRequestTypeDef",
    "DeleteAccessPointForObjectLambdaRequestRequestTypeDef",
    "DeleteAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    "DeleteAccessPointPolicyRequestRequestTypeDef",
    "DeleteAccessPointRequestRequestTypeDef",
    "DeleteBucketLifecycleConfigurationRequestRequestTypeDef",
    "DeleteBucketPolicyRequestRequestTypeDef",
    "DeleteBucketReplicationRequestRequestTypeDef",
    "DeleteBucketRequestRequestTypeDef",
    "DeleteBucketTaggingRequestRequestTypeDef",
    "DeleteJobTaggingRequestRequestTypeDef",
    "DeleteMarkerReplicationTypeDef",
    "DeleteMultiRegionAccessPointInputTypeDef",
    "DeleteMultiRegionAccessPointRequestRequestTypeDef",
    "DeleteMultiRegionAccessPointResultTypeDef",
    "DeletePublicAccessBlockRequestRequestTypeDef",
    "DeleteStorageLensConfigurationRequestRequestTypeDef",
    "DeleteStorageLensConfigurationTaggingRequestRequestTypeDef",
    "DeleteStorageLensGroupRequestRequestTypeDef",
    "DescribeJobRequestRequestTypeDef",
    "DescribeJobResultTypeDef",
    "DescribeMultiRegionAccessPointOperationRequestRequestTypeDef",
    "DescribeMultiRegionAccessPointOperationResultTypeDef",
    "DestinationTypeDef",
    "DetailedStatusCodesMetricsTypeDef",
    "DissociateAccessGrantsIdentityCenterRequestRequestTypeDef",
    "EncryptionConfigurationTypeDef",
    "EstablishedMultiRegionAccessPointPolicyTypeDef",
    "ExcludeTypeDef",
    "ExistingObjectReplicationTypeDef",
    "GeneratedManifestEncryptionTypeDef",
    "GetAccessGrantRequestRequestTypeDef",
    "GetAccessGrantResultTypeDef",
    "GetAccessGrantsInstanceForPrefixRequestRequestTypeDef",
    "GetAccessGrantsInstanceForPrefixResultTypeDef",
    "GetAccessGrantsInstanceRequestRequestTypeDef",
    "GetAccessGrantsInstanceResourcePolicyRequestRequestTypeDef",
    "GetAccessGrantsInstanceResourcePolicyResultTypeDef",
    "GetAccessGrantsInstanceResultTypeDef",
    "GetAccessGrantsLocationRequestRequestTypeDef",
    "GetAccessGrantsLocationResultTypeDef",
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
    "GetBucketReplicationRequestRequestTypeDef",
    "GetBucketReplicationResultTypeDef",
    "GetBucketRequestRequestTypeDef",
    "GetBucketResultTypeDef",
    "GetBucketTaggingRequestRequestTypeDef",
    "GetBucketTaggingResultTypeDef",
    "GetBucketVersioningRequestRequestTypeDef",
    "GetBucketVersioningResultTypeDef",
    "GetDataAccessRequestRequestTypeDef",
    "GetDataAccessResultTypeDef",
    "GetJobTaggingRequestRequestTypeDef",
    "GetJobTaggingResultTypeDef",
    "GetMultiRegionAccessPointPolicyRequestRequestTypeDef",
    "GetMultiRegionAccessPointPolicyResultTypeDef",
    "GetMultiRegionAccessPointPolicyStatusRequestRequestTypeDef",
    "GetMultiRegionAccessPointPolicyStatusResultTypeDef",
    "GetMultiRegionAccessPointRequestRequestTypeDef",
    "GetMultiRegionAccessPointResultTypeDef",
    "GetMultiRegionAccessPointRoutesRequestRequestTypeDef",
    "GetMultiRegionAccessPointRoutesResultTypeDef",
    "GetPublicAccessBlockOutputTypeDef",
    "GetPublicAccessBlockRequestRequestTypeDef",
    "GetStorageLensConfigurationRequestRequestTypeDef",
    "GetStorageLensConfigurationResultTypeDef",
    "GetStorageLensConfigurationTaggingRequestRequestTypeDef",
    "GetStorageLensConfigurationTaggingResultTypeDef",
    "GetStorageLensGroupRequestRequestTypeDef",
    "GetStorageLensGroupResultTypeDef",
    "GranteeTypeDef",
    "IncludeTypeDef",
    "JobDescriptorTypeDef",
    "JobFailureTypeDef",
    "JobListDescriptorTypeDef",
    "JobManifestGeneratorFilterTypeDef",
    "JobManifestGeneratorTypeDef",
    "JobManifestLocationTypeDef",
    "JobManifestSpecTypeDef",
    "JobManifestTypeDef",
    "JobOperationTypeDef",
    "JobProgressSummaryTypeDef",
    "JobReportTypeDef",
    "JobTimersTypeDef",
    "KeyNameConstraintTypeDef",
    "LambdaInvokeOperationTypeDef",
    "LifecycleConfigurationTypeDef",
    "LifecycleExpirationTypeDef",
    "LifecycleRuleAndOperatorTypeDef",
    "LifecycleRuleFilterTypeDef",
    "LifecycleRuleTypeDef",
    "ListAccessGrantEntryTypeDef",
    "ListAccessGrantsInstanceEntryTypeDef",
    "ListAccessGrantsInstancesRequestRequestTypeDef",
    "ListAccessGrantsInstancesResultTypeDef",
    "ListAccessGrantsLocationsEntryTypeDef",
    "ListAccessGrantsLocationsRequestRequestTypeDef",
    "ListAccessGrantsLocationsResultTypeDef",
    "ListAccessGrantsRequestRequestTypeDef",
    "ListAccessGrantsResultTypeDef",
    "ListAccessPointsForObjectLambdaRequestRequestTypeDef",
    "ListAccessPointsForObjectLambdaResultTypeDef",
    "ListAccessPointsRequestRequestTypeDef",
    "ListAccessPointsResultTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListJobsResultTypeDef",
    "ListMultiRegionAccessPointsRequestRequestTypeDef",
    "ListMultiRegionAccessPointsResultTypeDef",
    "ListRegionalBucketsRequestRequestTypeDef",
    "ListRegionalBucketsResultTypeDef",
    "ListStorageLensConfigurationEntryTypeDef",
    "ListStorageLensConfigurationsRequestRequestTypeDef",
    "ListStorageLensConfigurationsResultTypeDef",
    "ListStorageLensGroupEntryTypeDef",
    "ListStorageLensGroupsRequestRequestTypeDef",
    "ListStorageLensGroupsResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "MatchObjectAgeTypeDef",
    "MatchObjectSizeTypeDef",
    "MetricsTypeDef",
    "MultiRegionAccessPointPolicyDocumentTypeDef",
    "MultiRegionAccessPointRegionalResponseTypeDef",
    "MultiRegionAccessPointReportTypeDef",
    "MultiRegionAccessPointRouteTypeDef",
    "MultiRegionAccessPointsAsyncResponseTypeDef",
    "NoncurrentVersionExpirationTypeDef",
    "NoncurrentVersionTransitionTypeDef",
    "ObjectLambdaAccessPointAliasTypeDef",
    "ObjectLambdaAccessPointTypeDef",
    "ObjectLambdaConfigurationTypeDef",
    "ObjectLambdaContentTransformationTypeDef",
    "ObjectLambdaTransformationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PolicyStatusTypeDef",
    "PrefixLevelStorageMetricsTypeDef",
    "PrefixLevelTypeDef",
    "ProposedMultiRegionAccessPointPolicyTypeDef",
    "PublicAccessBlockConfigurationTypeDef",
    "PutAccessGrantsInstanceResourcePolicyRequestRequestTypeDef",
    "PutAccessGrantsInstanceResourcePolicyResultTypeDef",
    "PutAccessPointConfigurationForObjectLambdaRequestRequestTypeDef",
    "PutAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    "PutAccessPointPolicyRequestRequestTypeDef",
    "PutBucketLifecycleConfigurationRequestRequestTypeDef",
    "PutBucketPolicyRequestRequestTypeDef",
    "PutBucketReplicationRequestRequestTypeDef",
    "PutBucketTaggingRequestRequestTypeDef",
    "PutBucketVersioningRequestRequestTypeDef",
    "PutJobTaggingRequestRequestTypeDef",
    "PutMultiRegionAccessPointPolicyInputTypeDef",
    "PutMultiRegionAccessPointPolicyRequestRequestTypeDef",
    "PutMultiRegionAccessPointPolicyResultTypeDef",
    "PutPublicAccessBlockRequestRequestTypeDef",
    "PutStorageLensConfigurationRequestRequestTypeDef",
    "PutStorageLensConfigurationTaggingRequestRequestTypeDef",
    "RegionReportTypeDef",
    "RegionTypeDef",
    "RegionalBucketTypeDef",
    "ReplicaModificationsTypeDef",
    "ReplicationConfigurationTypeDef",
    "ReplicationRuleAndOperatorTypeDef",
    "ReplicationRuleFilterTypeDef",
    "ReplicationRuleTypeDef",
    "ReplicationTimeTypeDef",
    "ReplicationTimeValueTypeDef",
    "ResponseMetadataTypeDef",
    "S3AccessControlListTypeDef",
    "S3AccessControlPolicyTypeDef",
    "S3BucketDestinationTypeDef",
    "S3CopyObjectOperationTypeDef",
    "S3GeneratedManifestDescriptorTypeDef",
    "S3GrantTypeDef",
    "S3GranteeTypeDef",
    "S3InitiateRestoreObjectOperationTypeDef",
    "S3JobManifestGeneratorTypeDef",
    "S3ManifestOutputLocationTypeDef",
    "S3ObjectLockLegalHoldTypeDef",
    "S3ObjectMetadataTypeDef",
    "S3ObjectOwnerTypeDef",
    "S3RetentionTypeDef",
    "S3SetObjectAclOperationTypeDef",
    "S3SetObjectLegalHoldOperationTypeDef",
    "S3SetObjectRetentionOperationTypeDef",
    "S3SetObjectTaggingOperationTypeDef",
    "S3TagTypeDef",
    "SSEKMSEncryptionTypeDef",
    "SSEKMSTypeDef",
    "SelectionCriteriaTypeDef",
    "SourceSelectionCriteriaTypeDef",
    "SseKmsEncryptedObjectsTypeDef",
    "StorageLensAwsOrgTypeDef",
    "StorageLensConfigurationTypeDef",
    "StorageLensDataExportEncryptionTypeDef",
    "StorageLensDataExportTypeDef",
    "StorageLensGroupAndOperatorTypeDef",
    "StorageLensGroupFilterTypeDef",
    "StorageLensGroupLevelSelectionCriteriaTypeDef",
    "StorageLensGroupLevelTypeDef",
    "StorageLensGroupOrOperatorTypeDef",
    "StorageLensGroupTypeDef",
    "StorageLensTagTypeDef",
    "SubmitMultiRegionAccessPointRoutesRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TaggingTypeDef",
    "TransitionTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccessGrantsLocationRequestRequestTypeDef",
    "UpdateAccessGrantsLocationResultTypeDef",
    "UpdateJobPriorityRequestRequestTypeDef",
    "UpdateJobPriorityResultTypeDef",
    "UpdateJobStatusRequestRequestTypeDef",
    "UpdateJobStatusResultTypeDef",
    "UpdateStorageLensGroupRequestRequestTypeDef",
    "VersioningConfigurationTypeDef",
    "VpcConfigurationTypeDef",
)

AbortIncompleteMultipartUploadTypeDef = TypedDict(
    "AbortIncompleteMultipartUploadTypeDef",
    {
        "DaysAfterInitiation": int,
    },
    total=False,
)

AccessControlTranslationTypeDef = TypedDict(
    "AccessControlTranslationTypeDef",
    {
        "Owner": Literal["Destination"],
    },
)

AccessGrantsLocationConfigurationTypeDef = TypedDict(
    "AccessGrantsLocationConfigurationTypeDef",
    {
        "S3SubPrefix": str,
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
        "BucketAccountId": str,
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
        "AdvancedCostOptimizationMetrics": "AdvancedCostOptimizationMetricsTypeDef",
        "AdvancedDataProtectionMetrics": "AdvancedDataProtectionMetricsTypeDef",
        "DetailedStatusCodesMetrics": "DetailedStatusCodesMetricsTypeDef",
        "StorageLensGroupLevel": "StorageLensGroupLevelTypeDef",
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

AdvancedCostOptimizationMetricsTypeDef = TypedDict(
    "AdvancedCostOptimizationMetricsTypeDef",
    {
        "IsEnabled": bool,
    },
    total=False,
)

AdvancedDataProtectionMetricsTypeDef = TypedDict(
    "AdvancedDataProtectionMetricsTypeDef",
    {
        "IsEnabled": bool,
    },
    total=False,
)

AssociateAccessGrantsIdentityCenterRequestRequestTypeDef = TypedDict(
    "AssociateAccessGrantsIdentityCenterRequestRequestTypeDef",
    {
        "AccountId": str,
        "IdentityCenterArn": str,
    },
)

AsyncErrorDetailsTypeDef = TypedDict(
    "AsyncErrorDetailsTypeDef",
    {
        "Code": str,
        "Message": str,
        "Resource": str,
        "RequestId": str,
    },
    total=False,
)

AsyncOperationTypeDef = TypedDict(
    "AsyncOperationTypeDef",
    {
        "CreationTime": datetime,
        "Operation": AsyncOperationNameType,
        "RequestTokenARN": str,
        "RequestParameters": "AsyncRequestParametersTypeDef",
        "RequestStatus": str,
        "ResponseDetails": "AsyncResponseDetailsTypeDef",
    },
    total=False,
)

AsyncRequestParametersTypeDef = TypedDict(
    "AsyncRequestParametersTypeDef",
    {
        "CreateMultiRegionAccessPointRequest": "CreateMultiRegionAccessPointInputTypeDef",
        "DeleteMultiRegionAccessPointRequest": "DeleteMultiRegionAccessPointInputTypeDef",
        "PutMultiRegionAccessPointPolicyRequest": "PutMultiRegionAccessPointPolicyInputTypeDef",
    },
    total=False,
)

AsyncResponseDetailsTypeDef = TypedDict(
    "AsyncResponseDetailsTypeDef",
    {
        "MultiRegionAccessPointDetails": "MultiRegionAccessPointsAsyncResponseTypeDef",
        "ErrorDetails": "AsyncErrorDetailsTypeDef",
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
        "AdvancedCostOptimizationMetrics": "AdvancedCostOptimizationMetricsTypeDef",
        "AdvancedDataProtectionMetrics": "AdvancedDataProtectionMetricsTypeDef",
        "DetailedStatusCodesMetrics": "DetailedStatusCodesMetricsTypeDef",
    },
    total=False,
)

CloudWatchMetricsTypeDef = TypedDict(
    "CloudWatchMetricsTypeDef",
    {
        "IsEnabled": bool,
    },
)

_RequiredCreateAccessGrantRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccessGrantRequestRequestTypeDef",
    {
        "AccountId": str,
        "AccessGrantsLocationId": str,
        "Grantee": "GranteeTypeDef",
        "Permission": PermissionType,
    },
)
_OptionalCreateAccessGrantRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccessGrantRequestRequestTypeDef",
    {
        "AccessGrantsLocationConfiguration": "AccessGrantsLocationConfigurationTypeDef",
        "ApplicationArn": str,
        "S3PrefixType": Literal["Object"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateAccessGrantRequestRequestTypeDef(
    _RequiredCreateAccessGrantRequestRequestTypeDef, _OptionalCreateAccessGrantRequestRequestTypeDef
):
    pass

CreateAccessGrantResultTypeDef = TypedDict(
    "CreateAccessGrantResultTypeDef",
    {
        "CreatedAt": datetime,
        "AccessGrantId": str,
        "AccessGrantArn": str,
        "Grantee": "GranteeTypeDef",
        "AccessGrantsLocationId": str,
        "AccessGrantsLocationConfiguration": "AccessGrantsLocationConfigurationTypeDef",
        "Permission": PermissionType,
        "ApplicationArn": str,
        "GrantScope": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAccessGrantsInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccessGrantsInstanceRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalCreateAccessGrantsInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccessGrantsInstanceRequestRequestTypeDef",
    {
        "IdentityCenterArn": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateAccessGrantsInstanceRequestRequestTypeDef(
    _RequiredCreateAccessGrantsInstanceRequestRequestTypeDef,
    _OptionalCreateAccessGrantsInstanceRequestRequestTypeDef,
):
    pass

CreateAccessGrantsInstanceResultTypeDef = TypedDict(
    "CreateAccessGrantsInstanceResultTypeDef",
    {
        "CreatedAt": datetime,
        "AccessGrantsInstanceId": str,
        "AccessGrantsInstanceArn": str,
        "IdentityCenterArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAccessGrantsLocationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccessGrantsLocationRequestRequestTypeDef",
    {
        "AccountId": str,
        "LocationScope": str,
        "IAMRoleArn": str,
    },
)
_OptionalCreateAccessGrantsLocationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccessGrantsLocationRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateAccessGrantsLocationRequestRequestTypeDef(
    _RequiredCreateAccessGrantsLocationRequestRequestTypeDef,
    _OptionalCreateAccessGrantsLocationRequestRequestTypeDef,
):
    pass

CreateAccessGrantsLocationResultTypeDef = TypedDict(
    "CreateAccessGrantsLocationResultTypeDef",
    {
        "CreatedAt": datetime,
        "AccessGrantsLocationId": str,
        "AccessGrantsLocationArn": str,
        "LocationScope": str,
        "IAMRoleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "Alias": "ObjectLambdaAccessPointAliasTypeDef",
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
        "BucketAccountId": str,
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
        "Priority": int,
        "RoleArn": str,
    },
)
_OptionalCreateJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateJobRequestRequestTypeDef",
    {
        "ConfirmationRequired": bool,
        "Manifest": "JobManifestTypeDef",
        "Description": str,
        "Tags": List["S3TagTypeDef"],
        "ManifestGenerator": "JobManifestGeneratorTypeDef",
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

_RequiredCreateMultiRegionAccessPointInputTypeDef = TypedDict(
    "_RequiredCreateMultiRegionAccessPointInputTypeDef",
    {
        "Name": str,
        "Regions": List["RegionTypeDef"],
    },
)
_OptionalCreateMultiRegionAccessPointInputTypeDef = TypedDict(
    "_OptionalCreateMultiRegionAccessPointInputTypeDef",
    {
        "PublicAccessBlock": "PublicAccessBlockConfigurationTypeDef",
    },
    total=False,
)

class CreateMultiRegionAccessPointInputTypeDef(
    _RequiredCreateMultiRegionAccessPointInputTypeDef,
    _OptionalCreateMultiRegionAccessPointInputTypeDef,
):
    pass

CreateMultiRegionAccessPointRequestRequestTypeDef = TypedDict(
    "CreateMultiRegionAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "ClientToken": str,
        "Details": "CreateMultiRegionAccessPointInputTypeDef",
    },
)

CreateMultiRegionAccessPointResultTypeDef = TypedDict(
    "CreateMultiRegionAccessPointResultTypeDef",
    {
        "RequestTokenARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStorageLensGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStorageLensGroupRequestRequestTypeDef",
    {
        "AccountId": str,
        "StorageLensGroup": "StorageLensGroupTypeDef",
    },
)
_OptionalCreateStorageLensGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStorageLensGroupRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateStorageLensGroupRequestRequestTypeDef(
    _RequiredCreateStorageLensGroupRequestRequestTypeDef,
    _OptionalCreateStorageLensGroupRequestRequestTypeDef,
):
    pass

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "AccessKeyId": str,
        "SecretAccessKey": str,
        "SessionToken": str,
        "Expiration": datetime,
    },
    total=False,
)

DeleteAccessGrantRequestRequestTypeDef = TypedDict(
    "DeleteAccessGrantRequestRequestTypeDef",
    {
        "AccountId": str,
        "AccessGrantId": str,
    },
)

DeleteAccessGrantsInstanceRequestRequestTypeDef = TypedDict(
    "DeleteAccessGrantsInstanceRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

DeleteAccessGrantsInstanceResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteAccessGrantsInstanceResourcePolicyRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

DeleteAccessGrantsLocationRequestRequestTypeDef = TypedDict(
    "DeleteAccessGrantsLocationRequestRequestTypeDef",
    {
        "AccountId": str,
        "AccessGrantsLocationId": str,
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

DeleteBucketReplicationRequestRequestTypeDef = TypedDict(
    "DeleteBucketReplicationRequestRequestTypeDef",
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

DeleteMarkerReplicationTypeDef = TypedDict(
    "DeleteMarkerReplicationTypeDef",
    {
        "Status": DeleteMarkerReplicationStatusType,
    },
)

DeleteMultiRegionAccessPointInputTypeDef = TypedDict(
    "DeleteMultiRegionAccessPointInputTypeDef",
    {
        "Name": str,
    },
)

DeleteMultiRegionAccessPointRequestRequestTypeDef = TypedDict(
    "DeleteMultiRegionAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "ClientToken": str,
        "Details": "DeleteMultiRegionAccessPointInputTypeDef",
    },
)

DeleteMultiRegionAccessPointResultTypeDef = TypedDict(
    "DeleteMultiRegionAccessPointResultTypeDef",
    {
        "RequestTokenARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

DeleteStorageLensGroupRequestRequestTypeDef = TypedDict(
    "DeleteStorageLensGroupRequestRequestTypeDef",
    {
        "Name": str,
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

DescribeMultiRegionAccessPointOperationRequestRequestTypeDef = TypedDict(
    "DescribeMultiRegionAccessPointOperationRequestRequestTypeDef",
    {
        "AccountId": str,
        "RequestTokenARN": str,
    },
)

DescribeMultiRegionAccessPointOperationResultTypeDef = TypedDict(
    "DescribeMultiRegionAccessPointOperationResultTypeDef",
    {
        "AsyncOperation": "AsyncOperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDestinationTypeDef = TypedDict(
    "_RequiredDestinationTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDestinationTypeDef = TypedDict(
    "_OptionalDestinationTypeDef",
    {
        "Account": str,
        "ReplicationTime": "ReplicationTimeTypeDef",
        "AccessControlTranslation": "AccessControlTranslationTypeDef",
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "Metrics": "MetricsTypeDef",
        "StorageClass": ReplicationStorageClassType,
    },
    total=False,
)

class DestinationTypeDef(_RequiredDestinationTypeDef, _OptionalDestinationTypeDef):
    pass

DetailedStatusCodesMetricsTypeDef = TypedDict(
    "DetailedStatusCodesMetricsTypeDef",
    {
        "IsEnabled": bool,
    },
    total=False,
)

DissociateAccessGrantsIdentityCenterRequestRequestTypeDef = TypedDict(
    "DissociateAccessGrantsIdentityCenterRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "ReplicaKmsKeyID": str,
    },
    total=False,
)

EstablishedMultiRegionAccessPointPolicyTypeDef = TypedDict(
    "EstablishedMultiRegionAccessPointPolicyTypeDef",
    {
        "Policy": str,
    },
    total=False,
)

ExcludeTypeDef = TypedDict(
    "ExcludeTypeDef",
    {
        "Buckets": List[str],
        "Regions": List[str],
    },
    total=False,
)

ExistingObjectReplicationTypeDef = TypedDict(
    "ExistingObjectReplicationTypeDef",
    {
        "Status": ExistingObjectReplicationStatusType,
    },
)

GeneratedManifestEncryptionTypeDef = TypedDict(
    "GeneratedManifestEncryptionTypeDef",
    {
        "SSES3": Dict[str, Any],
        "SSEKMS": "SSEKMSEncryptionTypeDef",
    },
    total=False,
)

GetAccessGrantRequestRequestTypeDef = TypedDict(
    "GetAccessGrantRequestRequestTypeDef",
    {
        "AccountId": str,
        "AccessGrantId": str,
    },
)

GetAccessGrantResultTypeDef = TypedDict(
    "GetAccessGrantResultTypeDef",
    {
        "CreatedAt": datetime,
        "AccessGrantId": str,
        "AccessGrantArn": str,
        "Grantee": "GranteeTypeDef",
        "Permission": PermissionType,
        "AccessGrantsLocationId": str,
        "AccessGrantsLocationConfiguration": "AccessGrantsLocationConfigurationTypeDef",
        "GrantScope": str,
        "ApplicationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessGrantsInstanceForPrefixRequestRequestTypeDef = TypedDict(
    "GetAccessGrantsInstanceForPrefixRequestRequestTypeDef",
    {
        "AccountId": str,
        "S3Prefix": str,
    },
)

GetAccessGrantsInstanceForPrefixResultTypeDef = TypedDict(
    "GetAccessGrantsInstanceForPrefixResultTypeDef",
    {
        "AccessGrantsInstanceArn": str,
        "AccessGrantsInstanceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessGrantsInstanceRequestRequestTypeDef = TypedDict(
    "GetAccessGrantsInstanceRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

GetAccessGrantsInstanceResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetAccessGrantsInstanceResourcePolicyRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

GetAccessGrantsInstanceResourcePolicyResultTypeDef = TypedDict(
    "GetAccessGrantsInstanceResourcePolicyResultTypeDef",
    {
        "Policy": str,
        "Organization": str,
        "CreatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessGrantsInstanceResultTypeDef = TypedDict(
    "GetAccessGrantsInstanceResultTypeDef",
    {
        "AccessGrantsInstanceArn": str,
        "AccessGrantsInstanceId": str,
        "IdentityCenterArn": str,
        "CreatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessGrantsLocationRequestRequestTypeDef = TypedDict(
    "GetAccessGrantsLocationRequestRequestTypeDef",
    {
        "AccountId": str,
        "AccessGrantsLocationId": str,
    },
)

GetAccessGrantsLocationResultTypeDef = TypedDict(
    "GetAccessGrantsLocationResultTypeDef",
    {
        "CreatedAt": datetime,
        "AccessGrantsLocationId": str,
        "AccessGrantsLocationArn": str,
        "LocationScope": str,
        "IAMRoleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "Alias": "ObjectLambdaAccessPointAliasTypeDef",
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
        "BucketAccountId": str,
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

GetBucketReplicationRequestRequestTypeDef = TypedDict(
    "GetBucketReplicationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

GetBucketReplicationResultTypeDef = TypedDict(
    "GetBucketReplicationResultTypeDef",
    {
        "ReplicationConfiguration": "ReplicationConfigurationTypeDef",
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

GetBucketVersioningRequestRequestTypeDef = TypedDict(
    "GetBucketVersioningRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

GetBucketVersioningResultTypeDef = TypedDict(
    "GetBucketVersioningResultTypeDef",
    {
        "Status": BucketVersioningStatusType,
        "MFADelete": MFADeleteStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDataAccessRequestRequestTypeDef = TypedDict(
    "_RequiredGetDataAccessRequestRequestTypeDef",
    {
        "AccountId": str,
        "Target": str,
        "Permission": PermissionType,
    },
)
_OptionalGetDataAccessRequestRequestTypeDef = TypedDict(
    "_OptionalGetDataAccessRequestRequestTypeDef",
    {
        "DurationSeconds": int,
        "Privilege": PrivilegeType,
        "TargetType": Literal["Object"],
    },
    total=False,
)

class GetDataAccessRequestRequestTypeDef(
    _RequiredGetDataAccessRequestRequestTypeDef, _OptionalGetDataAccessRequestRequestTypeDef
):
    pass

GetDataAccessResultTypeDef = TypedDict(
    "GetDataAccessResultTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "MatchedGrantTarget": str,
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

GetMultiRegionAccessPointPolicyRequestRequestTypeDef = TypedDict(
    "GetMultiRegionAccessPointPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetMultiRegionAccessPointPolicyResultTypeDef = TypedDict(
    "GetMultiRegionAccessPointPolicyResultTypeDef",
    {
        "Policy": "MultiRegionAccessPointPolicyDocumentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMultiRegionAccessPointPolicyStatusRequestRequestTypeDef = TypedDict(
    "GetMultiRegionAccessPointPolicyStatusRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetMultiRegionAccessPointPolicyStatusResultTypeDef = TypedDict(
    "GetMultiRegionAccessPointPolicyStatusResultTypeDef",
    {
        "Established": "PolicyStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMultiRegionAccessPointRequestRequestTypeDef = TypedDict(
    "GetMultiRegionAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetMultiRegionAccessPointResultTypeDef = TypedDict(
    "GetMultiRegionAccessPointResultTypeDef",
    {
        "AccessPoint": "MultiRegionAccessPointReportTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMultiRegionAccessPointRoutesRequestRequestTypeDef = TypedDict(
    "GetMultiRegionAccessPointRoutesRequestRequestTypeDef",
    {
        "AccountId": str,
        "Mrap": str,
    },
)

GetMultiRegionAccessPointRoutesResultTypeDef = TypedDict(
    "GetMultiRegionAccessPointRoutesResultTypeDef",
    {
        "Mrap": str,
        "Routes": List["MultiRegionAccessPointRouteTypeDef"],
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

GetStorageLensGroupRequestRequestTypeDef = TypedDict(
    "GetStorageLensGroupRequestRequestTypeDef",
    {
        "Name": str,
        "AccountId": str,
    },
)

GetStorageLensGroupResultTypeDef = TypedDict(
    "GetStorageLensGroupResultTypeDef",
    {
        "StorageLensGroup": "StorageLensGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GranteeTypeDef = TypedDict(
    "GranteeTypeDef",
    {
        "GranteeType": GranteeTypeType,
        "GranteeIdentifier": str,
    },
    total=False,
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
        "ManifestGenerator": "JobManifestGeneratorTypeDef",
        "GeneratedManifestDescriptor": "S3GeneratedManifestDescriptorTypeDef",
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

JobManifestGeneratorFilterTypeDef = TypedDict(
    "JobManifestGeneratorFilterTypeDef",
    {
        "EligibleForReplication": bool,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "ObjectReplicationStatuses": List[ReplicationStatusType],
        "KeyNameConstraint": "KeyNameConstraintTypeDef",
        "ObjectSizeGreaterThanBytes": int,
        "ObjectSizeLessThanBytes": int,
        "MatchAnyStorageClass": List[S3StorageClassType],
    },
    total=False,
)

JobManifestGeneratorTypeDef = TypedDict(
    "JobManifestGeneratorTypeDef",
    {
        "S3JobManifestGenerator": "S3JobManifestGeneratorTypeDef",
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
        "S3ReplicateObject": Dict[str, Any],
    },
    total=False,
)

JobProgressSummaryTypeDef = TypedDict(
    "JobProgressSummaryTypeDef",
    {
        "TotalNumberOfTasks": int,
        "NumberOfTasksSucceeded": int,
        "NumberOfTasksFailed": int,
        "Timers": "JobTimersTypeDef",
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

JobTimersTypeDef = TypedDict(
    "JobTimersTypeDef",
    {
        "ElapsedTimeInActiveSeconds": int,
    },
    total=False,
)

KeyNameConstraintTypeDef = TypedDict(
    "KeyNameConstraintTypeDef",
    {
        "MatchAnyPrefix": List[str],
        "MatchAnySuffix": List[str],
        "MatchAnySubstring": List[str],
    },
    total=False,
)

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
        "ObjectSizeGreaterThan": int,
        "ObjectSizeLessThan": int,
    },
    total=False,
)

LifecycleRuleFilterTypeDef = TypedDict(
    "LifecycleRuleFilterTypeDef",
    {
        "Prefix": str,
        "Tag": "S3TagTypeDef",
        "And": "LifecycleRuleAndOperatorTypeDef",
        "ObjectSizeGreaterThan": int,
        "ObjectSizeLessThan": int,
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

ListAccessGrantEntryTypeDef = TypedDict(
    "ListAccessGrantEntryTypeDef",
    {
        "CreatedAt": datetime,
        "AccessGrantId": str,
        "AccessGrantArn": str,
        "Grantee": "GranteeTypeDef",
        "Permission": PermissionType,
        "AccessGrantsLocationId": str,
        "AccessGrantsLocationConfiguration": "AccessGrantsLocationConfigurationTypeDef",
        "GrantScope": str,
        "ApplicationArn": str,
    },
    total=False,
)

ListAccessGrantsInstanceEntryTypeDef = TypedDict(
    "ListAccessGrantsInstanceEntryTypeDef",
    {
        "AccessGrantsInstanceId": str,
        "AccessGrantsInstanceArn": str,
        "CreatedAt": datetime,
        "IdentityCenterArn": str,
    },
    total=False,
)

_RequiredListAccessGrantsInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredListAccessGrantsInstancesRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListAccessGrantsInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalListAccessGrantsInstancesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListAccessGrantsInstancesRequestRequestTypeDef(
    _RequiredListAccessGrantsInstancesRequestRequestTypeDef,
    _OptionalListAccessGrantsInstancesRequestRequestTypeDef,
):
    pass

ListAccessGrantsInstancesResultTypeDef = TypedDict(
    "ListAccessGrantsInstancesResultTypeDef",
    {
        "NextToken": str,
        "AccessGrantsInstancesList": List["ListAccessGrantsInstanceEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAccessGrantsLocationsEntryTypeDef = TypedDict(
    "ListAccessGrantsLocationsEntryTypeDef",
    {
        "CreatedAt": datetime,
        "AccessGrantsLocationId": str,
        "AccessGrantsLocationArn": str,
        "LocationScope": str,
        "IAMRoleArn": str,
    },
    total=False,
)

_RequiredListAccessGrantsLocationsRequestRequestTypeDef = TypedDict(
    "_RequiredListAccessGrantsLocationsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListAccessGrantsLocationsRequestRequestTypeDef = TypedDict(
    "_OptionalListAccessGrantsLocationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "LocationScope": str,
    },
    total=False,
)

class ListAccessGrantsLocationsRequestRequestTypeDef(
    _RequiredListAccessGrantsLocationsRequestRequestTypeDef,
    _OptionalListAccessGrantsLocationsRequestRequestTypeDef,
):
    pass

ListAccessGrantsLocationsResultTypeDef = TypedDict(
    "ListAccessGrantsLocationsResultTypeDef",
    {
        "NextToken": str,
        "AccessGrantsLocationsList": List["ListAccessGrantsLocationsEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAccessGrantsRequestRequestTypeDef = TypedDict(
    "_RequiredListAccessGrantsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListAccessGrantsRequestRequestTypeDef = TypedDict(
    "_OptionalListAccessGrantsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "GranteeType": GranteeTypeType,
        "GranteeIdentifier": str,
        "Permission": PermissionType,
        "GrantScope": str,
        "ApplicationArn": str,
    },
    total=False,
)

class ListAccessGrantsRequestRequestTypeDef(
    _RequiredListAccessGrantsRequestRequestTypeDef, _OptionalListAccessGrantsRequestRequestTypeDef
):
    pass

ListAccessGrantsResultTypeDef = TypedDict(
    "ListAccessGrantsResultTypeDef",
    {
        "NextToken": str,
        "AccessGrantsList": List["ListAccessGrantEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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

_RequiredListMultiRegionAccessPointsRequestRequestTypeDef = TypedDict(
    "_RequiredListMultiRegionAccessPointsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListMultiRegionAccessPointsRequestRequestTypeDef = TypedDict(
    "_OptionalListMultiRegionAccessPointsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListMultiRegionAccessPointsRequestRequestTypeDef(
    _RequiredListMultiRegionAccessPointsRequestRequestTypeDef,
    _OptionalListMultiRegionAccessPointsRequestRequestTypeDef,
):
    pass

ListMultiRegionAccessPointsResultTypeDef = TypedDict(
    "ListMultiRegionAccessPointsResultTypeDef",
    {
        "AccessPoints": List["MultiRegionAccessPointReportTypeDef"],
        "NextToken": str,
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

ListStorageLensGroupEntryTypeDef = TypedDict(
    "ListStorageLensGroupEntryTypeDef",
    {
        "Name": str,
        "StorageLensGroupArn": str,
        "HomeRegion": str,
    },
)

_RequiredListStorageLensGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListStorageLensGroupsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListStorageLensGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListStorageLensGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListStorageLensGroupsRequestRequestTypeDef(
    _RequiredListStorageLensGroupsRequestRequestTypeDef,
    _OptionalListStorageLensGroupsRequestRequestTypeDef,
):
    pass

ListStorageLensGroupsResultTypeDef = TypedDict(
    "ListStorageLensGroupsResultTypeDef",
    {
        "NextToken": str,
        "StorageLensGroupList": List["ListStorageLensGroupEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "AccountId": str,
        "ResourceArn": str,
    },
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MatchObjectAgeTypeDef = TypedDict(
    "MatchObjectAgeTypeDef",
    {
        "DaysGreaterThan": int,
        "DaysLessThan": int,
    },
    total=False,
)

MatchObjectSizeTypeDef = TypedDict(
    "MatchObjectSizeTypeDef",
    {
        "BytesGreaterThan": int,
        "BytesLessThan": int,
    },
    total=False,
)

_RequiredMetricsTypeDef = TypedDict(
    "_RequiredMetricsTypeDef",
    {
        "Status": MetricsStatusType,
    },
)
_OptionalMetricsTypeDef = TypedDict(
    "_OptionalMetricsTypeDef",
    {
        "EventThreshold": "ReplicationTimeValueTypeDef",
    },
    total=False,
)

class MetricsTypeDef(_RequiredMetricsTypeDef, _OptionalMetricsTypeDef):
    pass

MultiRegionAccessPointPolicyDocumentTypeDef = TypedDict(
    "MultiRegionAccessPointPolicyDocumentTypeDef",
    {
        "Established": "EstablishedMultiRegionAccessPointPolicyTypeDef",
        "Proposed": "ProposedMultiRegionAccessPointPolicyTypeDef",
    },
    total=False,
)

MultiRegionAccessPointRegionalResponseTypeDef = TypedDict(
    "MultiRegionAccessPointRegionalResponseTypeDef",
    {
        "Name": str,
        "RequestStatus": str,
    },
    total=False,
)

MultiRegionAccessPointReportTypeDef = TypedDict(
    "MultiRegionAccessPointReportTypeDef",
    {
        "Name": str,
        "Alias": str,
        "CreatedAt": datetime,
        "PublicAccessBlock": "PublicAccessBlockConfigurationTypeDef",
        "Status": MultiRegionAccessPointStatusType,
        "Regions": List["RegionReportTypeDef"],
    },
    total=False,
)

_RequiredMultiRegionAccessPointRouteTypeDef = TypedDict(
    "_RequiredMultiRegionAccessPointRouteTypeDef",
    {
        "TrafficDialPercentage": int,
    },
)
_OptionalMultiRegionAccessPointRouteTypeDef = TypedDict(
    "_OptionalMultiRegionAccessPointRouteTypeDef",
    {
        "Bucket": str,
        "Region": str,
    },
    total=False,
)

class MultiRegionAccessPointRouteTypeDef(
    _RequiredMultiRegionAccessPointRouteTypeDef, _OptionalMultiRegionAccessPointRouteTypeDef
):
    pass

MultiRegionAccessPointsAsyncResponseTypeDef = TypedDict(
    "MultiRegionAccessPointsAsyncResponseTypeDef",
    {
        "Regions": List["MultiRegionAccessPointRegionalResponseTypeDef"],
    },
    total=False,
)

NoncurrentVersionExpirationTypeDef = TypedDict(
    "NoncurrentVersionExpirationTypeDef",
    {
        "NoncurrentDays": int,
        "NewerNoncurrentVersions": int,
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

ObjectLambdaAccessPointAliasTypeDef = TypedDict(
    "ObjectLambdaAccessPointAliasTypeDef",
    {
        "Value": str,
        "Status": ObjectLambdaAccessPointAliasStatusType,
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
        "Alias": "ObjectLambdaAccessPointAliasTypeDef",
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
        "Actions": List[ObjectLambdaTransformationConfigurationActionType],
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

ProposedMultiRegionAccessPointPolicyTypeDef = TypedDict(
    "ProposedMultiRegionAccessPointPolicyTypeDef",
    {
        "Policy": str,
    },
    total=False,
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

_RequiredPutAccessGrantsInstanceResourcePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutAccessGrantsInstanceResourcePolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Policy": str,
    },
)
_OptionalPutAccessGrantsInstanceResourcePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutAccessGrantsInstanceResourcePolicyRequestRequestTypeDef",
    {
        "Organization": str,
    },
    total=False,
)

class PutAccessGrantsInstanceResourcePolicyRequestRequestTypeDef(
    _RequiredPutAccessGrantsInstanceResourcePolicyRequestRequestTypeDef,
    _OptionalPutAccessGrantsInstanceResourcePolicyRequestRequestTypeDef,
):
    pass

PutAccessGrantsInstanceResourcePolicyResultTypeDef = TypedDict(
    "PutAccessGrantsInstanceResourcePolicyResultTypeDef",
    {
        "Policy": str,
        "Organization": str,
        "CreatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

PutBucketReplicationRequestRequestTypeDef = TypedDict(
    "PutBucketReplicationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "ReplicationConfiguration": "ReplicationConfigurationTypeDef",
    },
)

PutBucketTaggingRequestRequestTypeDef = TypedDict(
    "PutBucketTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Tagging": "TaggingTypeDef",
    },
)

_RequiredPutBucketVersioningRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketVersioningRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "VersioningConfiguration": "VersioningConfigurationTypeDef",
    },
)
_OptionalPutBucketVersioningRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketVersioningRequestRequestTypeDef",
    {
        "MFA": str,
    },
    total=False,
)

class PutBucketVersioningRequestRequestTypeDef(
    _RequiredPutBucketVersioningRequestRequestTypeDef,
    _OptionalPutBucketVersioningRequestRequestTypeDef,
):
    pass

PutJobTaggingRequestRequestTypeDef = TypedDict(
    "PutJobTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
        "Tags": List["S3TagTypeDef"],
    },
)

PutMultiRegionAccessPointPolicyInputTypeDef = TypedDict(
    "PutMultiRegionAccessPointPolicyInputTypeDef",
    {
        "Name": str,
        "Policy": str,
    },
)

PutMultiRegionAccessPointPolicyRequestRequestTypeDef = TypedDict(
    "PutMultiRegionAccessPointPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "ClientToken": str,
        "Details": "PutMultiRegionAccessPointPolicyInputTypeDef",
    },
)

PutMultiRegionAccessPointPolicyResultTypeDef = TypedDict(
    "PutMultiRegionAccessPointPolicyResultTypeDef",
    {
        "RequestTokenARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

RegionReportTypeDef = TypedDict(
    "RegionReportTypeDef",
    {
        "Bucket": str,
        "Region": str,
        "BucketAccountId": str,
    },
    total=False,
)

_RequiredRegionTypeDef = TypedDict(
    "_RequiredRegionTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalRegionTypeDef = TypedDict(
    "_OptionalRegionTypeDef",
    {
        "BucketAccountId": str,
    },
    total=False,
)

class RegionTypeDef(_RequiredRegionTypeDef, _OptionalRegionTypeDef):
    pass

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

ReplicaModificationsTypeDef = TypedDict(
    "ReplicaModificationsTypeDef",
    {
        "Status": ReplicaModificationsStatusType,
    },
)

ReplicationConfigurationTypeDef = TypedDict(
    "ReplicationConfigurationTypeDef",
    {
        "Role": str,
        "Rules": List["ReplicationRuleTypeDef"],
    },
)

ReplicationRuleAndOperatorTypeDef = TypedDict(
    "ReplicationRuleAndOperatorTypeDef",
    {
        "Prefix": str,
        "Tags": List["S3TagTypeDef"],
    },
    total=False,
)

ReplicationRuleFilterTypeDef = TypedDict(
    "ReplicationRuleFilterTypeDef",
    {
        "Prefix": str,
        "Tag": "S3TagTypeDef",
        "And": "ReplicationRuleAndOperatorTypeDef",
    },
    total=False,
)

_RequiredReplicationRuleTypeDef = TypedDict(
    "_RequiredReplicationRuleTypeDef",
    {
        "Status": ReplicationRuleStatusType,
        "Destination": "DestinationTypeDef",
        "Bucket": str,
    },
)
_OptionalReplicationRuleTypeDef = TypedDict(
    "_OptionalReplicationRuleTypeDef",
    {
        "ID": str,
        "Priority": int,
        "Prefix": str,
        "Filter": "ReplicationRuleFilterTypeDef",
        "SourceSelectionCriteria": "SourceSelectionCriteriaTypeDef",
        "ExistingObjectReplication": "ExistingObjectReplicationTypeDef",
        "DeleteMarkerReplication": "DeleteMarkerReplicationTypeDef",
    },
    total=False,
)

class ReplicationRuleTypeDef(_RequiredReplicationRuleTypeDef, _OptionalReplicationRuleTypeDef):
    pass

ReplicationTimeTypeDef = TypedDict(
    "ReplicationTimeTypeDef",
    {
        "Status": ReplicationTimeStatusType,
        "Time": "ReplicationTimeValueTypeDef",
    },
)

ReplicationTimeValueTypeDef = TypedDict(
    "ReplicationTimeValueTypeDef",
    {
        "Minutes": int,
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
        "ChecksumAlgorithm": S3ChecksumAlgorithmType,
    },
    total=False,
)

S3GeneratedManifestDescriptorTypeDef = TypedDict(
    "S3GeneratedManifestDescriptorTypeDef",
    {
        "Format": Literal["S3InventoryReport_CSV_20211130"],
        "Location": "JobManifestLocationTypeDef",
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

_RequiredS3JobManifestGeneratorTypeDef = TypedDict(
    "_RequiredS3JobManifestGeneratorTypeDef",
    {
        "SourceBucket": str,
        "EnableManifestOutput": bool,
    },
)
_OptionalS3JobManifestGeneratorTypeDef = TypedDict(
    "_OptionalS3JobManifestGeneratorTypeDef",
    {
        "ExpectedBucketOwner": str,
        "ManifestOutputLocation": "S3ManifestOutputLocationTypeDef",
        "Filter": "JobManifestGeneratorFilterTypeDef",
    },
    total=False,
)

class S3JobManifestGeneratorTypeDef(
    _RequiredS3JobManifestGeneratorTypeDef, _OptionalS3JobManifestGeneratorTypeDef
):
    pass

_RequiredS3ManifestOutputLocationTypeDef = TypedDict(
    "_RequiredS3ManifestOutputLocationTypeDef",
    {
        "Bucket": str,
        "ManifestFormat": Literal["S3InventoryReport_CSV_20211130"],
    },
)
_OptionalS3ManifestOutputLocationTypeDef = TypedDict(
    "_OptionalS3ManifestOutputLocationTypeDef",
    {
        "ExpectedManifestBucketOwner": str,
        "ManifestPrefix": str,
        "ManifestEncryption": "GeneratedManifestEncryptionTypeDef",
    },
    total=False,
)

class S3ManifestOutputLocationTypeDef(
    _RequiredS3ManifestOutputLocationTypeDef, _OptionalS3ManifestOutputLocationTypeDef
):
    pass

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

SSEKMSEncryptionTypeDef = TypedDict(
    "SSEKMSEncryptionTypeDef",
    {
        "KeyId": str,
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

SourceSelectionCriteriaTypeDef = TypedDict(
    "SourceSelectionCriteriaTypeDef",
    {
        "SseKmsEncryptedObjects": "SseKmsEncryptedObjectsTypeDef",
        "ReplicaModifications": "ReplicaModificationsTypeDef",
    },
    total=False,
)

SseKmsEncryptedObjectsTypeDef = TypedDict(
    "SseKmsEncryptedObjectsTypeDef",
    {
        "Status": SseKmsEncryptedObjectsStatusType,
    },
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
        "CloudWatchMetrics": "CloudWatchMetricsTypeDef",
    },
    total=False,
)

StorageLensGroupAndOperatorTypeDef = TypedDict(
    "StorageLensGroupAndOperatorTypeDef",
    {
        "MatchAnyPrefix": List[str],
        "MatchAnySuffix": List[str],
        "MatchAnyTag": List["S3TagTypeDef"],
        "MatchObjectAge": "MatchObjectAgeTypeDef",
        "MatchObjectSize": "MatchObjectSizeTypeDef",
    },
    total=False,
)

StorageLensGroupFilterTypeDef = TypedDict(
    "StorageLensGroupFilterTypeDef",
    {
        "MatchAnyPrefix": List[str],
        "MatchAnySuffix": List[str],
        "MatchAnyTag": List["S3TagTypeDef"],
        "MatchObjectAge": "MatchObjectAgeTypeDef",
        "MatchObjectSize": "MatchObjectSizeTypeDef",
        "And": "StorageLensGroupAndOperatorTypeDef",
        "Or": "StorageLensGroupOrOperatorTypeDef",
    },
    total=False,
)

StorageLensGroupLevelSelectionCriteriaTypeDef = TypedDict(
    "StorageLensGroupLevelSelectionCriteriaTypeDef",
    {
        "Include": List[str],
        "Exclude": List[str],
    },
    total=False,
)

StorageLensGroupLevelTypeDef = TypedDict(
    "StorageLensGroupLevelTypeDef",
    {
        "SelectionCriteria": "StorageLensGroupLevelSelectionCriteriaTypeDef",
    },
    total=False,
)

StorageLensGroupOrOperatorTypeDef = TypedDict(
    "StorageLensGroupOrOperatorTypeDef",
    {
        "MatchAnyPrefix": List[str],
        "MatchAnySuffix": List[str],
        "MatchAnyTag": List["S3TagTypeDef"],
        "MatchObjectAge": "MatchObjectAgeTypeDef",
        "MatchObjectSize": "MatchObjectSizeTypeDef",
    },
    total=False,
)

_RequiredStorageLensGroupTypeDef = TypedDict(
    "_RequiredStorageLensGroupTypeDef",
    {
        "Name": str,
        "Filter": "StorageLensGroupFilterTypeDef",
    },
)
_OptionalStorageLensGroupTypeDef = TypedDict(
    "_OptionalStorageLensGroupTypeDef",
    {
        "StorageLensGroupArn": str,
    },
    total=False,
)

class StorageLensGroupTypeDef(_RequiredStorageLensGroupTypeDef, _OptionalStorageLensGroupTypeDef):
    pass

StorageLensTagTypeDef = TypedDict(
    "StorageLensTagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

SubmitMultiRegionAccessPointRoutesRequestRequestTypeDef = TypedDict(
    "SubmitMultiRegionAccessPointRoutesRequestRequestTypeDef",
    {
        "AccountId": str,
        "Mrap": str,
        "RouteUpdates": List["MultiRegionAccessPointRouteTypeDef"],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "AccountId": str,
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
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

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "AccountId": str,
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateAccessGrantsLocationRequestRequestTypeDef = TypedDict(
    "UpdateAccessGrantsLocationRequestRequestTypeDef",
    {
        "AccountId": str,
        "AccessGrantsLocationId": str,
        "IAMRoleArn": str,
    },
)

UpdateAccessGrantsLocationResultTypeDef = TypedDict(
    "UpdateAccessGrantsLocationResultTypeDef",
    {
        "CreatedAt": datetime,
        "AccessGrantsLocationId": str,
        "AccessGrantsLocationArn": str,
        "LocationScope": str,
        "IAMRoleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

UpdateStorageLensGroupRequestRequestTypeDef = TypedDict(
    "UpdateStorageLensGroupRequestRequestTypeDef",
    {
        "Name": str,
        "AccountId": str,
        "StorageLensGroup": "StorageLensGroupTypeDef",
    },
)

VersioningConfigurationTypeDef = TypedDict(
    "VersioningConfigurationTypeDef",
    {
        "MFADelete": MFADeleteType,
        "Status": BucketVersioningStatusType,
    },
    total=False,
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "VpcId": str,
    },
)
