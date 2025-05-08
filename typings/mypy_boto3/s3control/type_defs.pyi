"""
Type annotations for s3control service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_s3control.type_defs import AbortIncompleteMultipartUploadTypeDef

    data: AbortIncompleteMultipartUploadTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

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
    ScopePermissionType,
    SseKmsEncryptedObjectsStatusType,
    TransitionStorageClassType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AbortIncompleteMultipartUploadTypeDef",
    "AccessControlTranslationTypeDef",
    "AccessGrantsLocationConfigurationTypeDef",
    "AccessPointTypeDef",
    "AccountLevelOutputTypeDef",
    "AccountLevelTypeDef",
    "ActivityMetricsTypeDef",
    "AdvancedCostOptimizationMetricsTypeDef",
    "AdvancedDataProtectionMetricsTypeDef",
    "AssociateAccessGrantsIdentityCenterRequestTypeDef",
    "AsyncErrorDetailsTypeDef",
    "AsyncOperationTypeDef",
    "AsyncRequestParametersTypeDef",
    "AsyncResponseDetailsTypeDef",
    "AwsLambdaTransformationTypeDef",
    "BucketLevelTypeDef",
    "CloudWatchMetricsTypeDef",
    "CreateAccessGrantRequestTypeDef",
    "CreateAccessGrantResultTypeDef",
    "CreateAccessGrantsInstanceRequestTypeDef",
    "CreateAccessGrantsInstanceResultTypeDef",
    "CreateAccessGrantsLocationRequestTypeDef",
    "CreateAccessGrantsLocationResultTypeDef",
    "CreateAccessPointForObjectLambdaRequestTypeDef",
    "CreateAccessPointForObjectLambdaResultTypeDef",
    "CreateAccessPointRequestTypeDef",
    "CreateAccessPointResultTypeDef",
    "CreateBucketConfigurationTypeDef",
    "CreateBucketRequestTypeDef",
    "CreateBucketResultTypeDef",
    "CreateJobRequestTypeDef",
    "CreateJobResultTypeDef",
    "CreateMultiRegionAccessPointInputOutputTypeDef",
    "CreateMultiRegionAccessPointInputTypeDef",
    "CreateMultiRegionAccessPointInputUnionTypeDef",
    "CreateMultiRegionAccessPointRequestTypeDef",
    "CreateMultiRegionAccessPointResultTypeDef",
    "CreateStorageLensGroupRequestTypeDef",
    "CredentialsTypeDef",
    "DeleteAccessGrantRequestTypeDef",
    "DeleteAccessGrantsInstanceRequestTypeDef",
    "DeleteAccessGrantsInstanceResourcePolicyRequestTypeDef",
    "DeleteAccessGrantsLocationRequestTypeDef",
    "DeleteAccessPointForObjectLambdaRequestTypeDef",
    "DeleteAccessPointPolicyForObjectLambdaRequestTypeDef",
    "DeleteAccessPointPolicyRequestTypeDef",
    "DeleteAccessPointRequestTypeDef",
    "DeleteAccessPointScopeRequestTypeDef",
    "DeleteBucketLifecycleConfigurationRequestTypeDef",
    "DeleteBucketPolicyRequestTypeDef",
    "DeleteBucketReplicationRequestTypeDef",
    "DeleteBucketRequestTypeDef",
    "DeleteBucketTaggingRequestTypeDef",
    "DeleteJobTaggingRequestTypeDef",
    "DeleteMarkerReplicationTypeDef",
    "DeleteMultiRegionAccessPointInputTypeDef",
    "DeleteMultiRegionAccessPointRequestTypeDef",
    "DeleteMultiRegionAccessPointResultTypeDef",
    "DeletePublicAccessBlockRequestTypeDef",
    "DeleteStorageLensConfigurationRequestTypeDef",
    "DeleteStorageLensConfigurationTaggingRequestTypeDef",
    "DeleteStorageLensGroupRequestTypeDef",
    "DescribeJobRequestTypeDef",
    "DescribeJobResultTypeDef",
    "DescribeMultiRegionAccessPointOperationRequestTypeDef",
    "DescribeMultiRegionAccessPointOperationResultTypeDef",
    "DestinationTypeDef",
    "DetailedStatusCodesMetricsTypeDef",
    "DissociateAccessGrantsIdentityCenterRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EncryptionConfigurationTypeDef",
    "EstablishedMultiRegionAccessPointPolicyTypeDef",
    "ExcludeOutputTypeDef",
    "ExcludeTypeDef",
    "ExistingObjectReplicationTypeDef",
    "GeneratedManifestEncryptionOutputTypeDef",
    "GeneratedManifestEncryptionTypeDef",
    "GetAccessGrantRequestTypeDef",
    "GetAccessGrantResultTypeDef",
    "GetAccessGrantsInstanceForPrefixRequestTypeDef",
    "GetAccessGrantsInstanceForPrefixResultTypeDef",
    "GetAccessGrantsInstanceRequestTypeDef",
    "GetAccessGrantsInstanceResourcePolicyRequestTypeDef",
    "GetAccessGrantsInstanceResourcePolicyResultTypeDef",
    "GetAccessGrantsInstanceResultTypeDef",
    "GetAccessGrantsLocationRequestTypeDef",
    "GetAccessGrantsLocationResultTypeDef",
    "GetAccessPointConfigurationForObjectLambdaRequestTypeDef",
    "GetAccessPointConfigurationForObjectLambdaResultTypeDef",
    "GetAccessPointForObjectLambdaRequestTypeDef",
    "GetAccessPointForObjectLambdaResultTypeDef",
    "GetAccessPointPolicyForObjectLambdaRequestTypeDef",
    "GetAccessPointPolicyForObjectLambdaResultTypeDef",
    "GetAccessPointPolicyRequestTypeDef",
    "GetAccessPointPolicyResultTypeDef",
    "GetAccessPointPolicyStatusForObjectLambdaRequestTypeDef",
    "GetAccessPointPolicyStatusForObjectLambdaResultTypeDef",
    "GetAccessPointPolicyStatusRequestTypeDef",
    "GetAccessPointPolicyStatusResultTypeDef",
    "GetAccessPointRequestTypeDef",
    "GetAccessPointResultTypeDef",
    "GetAccessPointScopeRequestTypeDef",
    "GetAccessPointScopeResultTypeDef",
    "GetBucketLifecycleConfigurationRequestTypeDef",
    "GetBucketLifecycleConfigurationResultTypeDef",
    "GetBucketPolicyRequestTypeDef",
    "GetBucketPolicyResultTypeDef",
    "GetBucketReplicationRequestTypeDef",
    "GetBucketReplicationResultTypeDef",
    "GetBucketRequestTypeDef",
    "GetBucketResultTypeDef",
    "GetBucketTaggingRequestTypeDef",
    "GetBucketTaggingResultTypeDef",
    "GetBucketVersioningRequestTypeDef",
    "GetBucketVersioningResultTypeDef",
    "GetDataAccessRequestTypeDef",
    "GetDataAccessResultTypeDef",
    "GetJobTaggingRequestTypeDef",
    "GetJobTaggingResultTypeDef",
    "GetMultiRegionAccessPointPolicyRequestTypeDef",
    "GetMultiRegionAccessPointPolicyResultTypeDef",
    "GetMultiRegionAccessPointPolicyStatusRequestTypeDef",
    "GetMultiRegionAccessPointPolicyStatusResultTypeDef",
    "GetMultiRegionAccessPointRequestTypeDef",
    "GetMultiRegionAccessPointResultTypeDef",
    "GetMultiRegionAccessPointRoutesRequestTypeDef",
    "GetMultiRegionAccessPointRoutesResultTypeDef",
    "GetPublicAccessBlockOutputTypeDef",
    "GetPublicAccessBlockRequestTypeDef",
    "GetStorageLensConfigurationRequestTypeDef",
    "GetStorageLensConfigurationResultTypeDef",
    "GetStorageLensConfigurationTaggingRequestTypeDef",
    "GetStorageLensConfigurationTaggingResultTypeDef",
    "GetStorageLensGroupRequestTypeDef",
    "GetStorageLensGroupResultTypeDef",
    "GranteeTypeDef",
    "IncludeOutputTypeDef",
    "IncludeTypeDef",
    "JobDescriptorTypeDef",
    "JobFailureTypeDef",
    "JobListDescriptorTypeDef",
    "JobManifestGeneratorFilterOutputTypeDef",
    "JobManifestGeneratorFilterTypeDef",
    "JobManifestGeneratorOutputTypeDef",
    "JobManifestGeneratorTypeDef",
    "JobManifestGeneratorUnionTypeDef",
    "JobManifestLocationTypeDef",
    "JobManifestOutputTypeDef",
    "JobManifestSpecOutputTypeDef",
    "JobManifestSpecTypeDef",
    "JobManifestTypeDef",
    "JobManifestUnionTypeDef",
    "JobOperationOutputTypeDef",
    "JobOperationTypeDef",
    "JobOperationUnionTypeDef",
    "JobProgressSummaryTypeDef",
    "JobReportTypeDef",
    "JobTimersTypeDef",
    "KeyNameConstraintOutputTypeDef",
    "KeyNameConstraintTypeDef",
    "LambdaInvokeOperationOutputTypeDef",
    "LambdaInvokeOperationTypeDef",
    "LifecycleConfigurationTypeDef",
    "LifecycleExpirationOutputTypeDef",
    "LifecycleExpirationTypeDef",
    "LifecycleExpirationUnionTypeDef",
    "LifecycleRuleAndOperatorOutputTypeDef",
    "LifecycleRuleAndOperatorTypeDef",
    "LifecycleRuleAndOperatorUnionTypeDef",
    "LifecycleRuleFilterOutputTypeDef",
    "LifecycleRuleFilterTypeDef",
    "LifecycleRuleFilterUnionTypeDef",
    "LifecycleRuleOutputTypeDef",
    "LifecycleRuleTypeDef",
    "LifecycleRuleUnionTypeDef",
    "ListAccessGrantEntryTypeDef",
    "ListAccessGrantsInstanceEntryTypeDef",
    "ListAccessGrantsInstancesRequestTypeDef",
    "ListAccessGrantsInstancesResultTypeDef",
    "ListAccessGrantsLocationsEntryTypeDef",
    "ListAccessGrantsLocationsRequestTypeDef",
    "ListAccessGrantsLocationsResultTypeDef",
    "ListAccessGrantsRequestTypeDef",
    "ListAccessGrantsResultTypeDef",
    "ListAccessPointsForDirectoryBucketsRequestPaginateTypeDef",
    "ListAccessPointsForDirectoryBucketsRequestTypeDef",
    "ListAccessPointsForDirectoryBucketsResultTypeDef",
    "ListAccessPointsForObjectLambdaRequestPaginateTypeDef",
    "ListAccessPointsForObjectLambdaRequestTypeDef",
    "ListAccessPointsForObjectLambdaResultTypeDef",
    "ListAccessPointsRequestTypeDef",
    "ListAccessPointsResultTypeDef",
    "ListCallerAccessGrantsEntryTypeDef",
    "ListCallerAccessGrantsRequestPaginateTypeDef",
    "ListCallerAccessGrantsRequestTypeDef",
    "ListCallerAccessGrantsResultTypeDef",
    "ListJobsRequestTypeDef",
    "ListJobsResultTypeDef",
    "ListMultiRegionAccessPointsRequestTypeDef",
    "ListMultiRegionAccessPointsResultTypeDef",
    "ListRegionalBucketsRequestTypeDef",
    "ListRegionalBucketsResultTypeDef",
    "ListStorageLensConfigurationEntryTypeDef",
    "ListStorageLensConfigurationsRequestTypeDef",
    "ListStorageLensConfigurationsResultTypeDef",
    "ListStorageLensGroupEntryTypeDef",
    "ListStorageLensGroupsRequestTypeDef",
    "ListStorageLensGroupsResultTypeDef",
    "ListTagsForResourceRequestTypeDef",
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
    "ObjectLambdaConfigurationOutputTypeDef",
    "ObjectLambdaConfigurationTypeDef",
    "ObjectLambdaConfigurationUnionTypeDef",
    "ObjectLambdaContentTransformationTypeDef",
    "ObjectLambdaTransformationConfigurationOutputTypeDef",
    "ObjectLambdaTransformationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PolicyStatusTypeDef",
    "PrefixLevelStorageMetricsTypeDef",
    "PrefixLevelTypeDef",
    "ProposedMultiRegionAccessPointPolicyTypeDef",
    "PublicAccessBlockConfigurationTypeDef",
    "PutAccessGrantsInstanceResourcePolicyRequestTypeDef",
    "PutAccessGrantsInstanceResourcePolicyResultTypeDef",
    "PutAccessPointConfigurationForObjectLambdaRequestTypeDef",
    "PutAccessPointPolicyForObjectLambdaRequestTypeDef",
    "PutAccessPointPolicyRequestTypeDef",
    "PutAccessPointScopeRequestTypeDef",
    "PutBucketLifecycleConfigurationRequestTypeDef",
    "PutBucketPolicyRequestTypeDef",
    "PutBucketReplicationRequestTypeDef",
    "PutBucketTaggingRequestTypeDef",
    "PutBucketVersioningRequestTypeDef",
    "PutJobTaggingRequestTypeDef",
    "PutMultiRegionAccessPointPolicyInputTypeDef",
    "PutMultiRegionAccessPointPolicyRequestTypeDef",
    "PutMultiRegionAccessPointPolicyResultTypeDef",
    "PutPublicAccessBlockRequestTypeDef",
    "PutStorageLensConfigurationRequestTypeDef",
    "PutStorageLensConfigurationTaggingRequestTypeDef",
    "RegionReportTypeDef",
    "RegionTypeDef",
    "RegionalBucketTypeDef",
    "ReplicaModificationsTypeDef",
    "ReplicationConfigurationOutputTypeDef",
    "ReplicationConfigurationTypeDef",
    "ReplicationConfigurationUnionTypeDef",
    "ReplicationRuleAndOperatorOutputTypeDef",
    "ReplicationRuleAndOperatorTypeDef",
    "ReplicationRuleFilterOutputTypeDef",
    "ReplicationRuleFilterTypeDef",
    "ReplicationRuleOutputTypeDef",
    "ReplicationRuleTypeDef",
    "ReplicationTimeTypeDef",
    "ReplicationTimeValueTypeDef",
    "ResponseMetadataTypeDef",
    "S3AccessControlListOutputTypeDef",
    "S3AccessControlListTypeDef",
    "S3AccessControlPolicyOutputTypeDef",
    "S3AccessControlPolicyTypeDef",
    "S3BucketDestinationOutputTypeDef",
    "S3BucketDestinationTypeDef",
    "S3CopyObjectOperationOutputTypeDef",
    "S3CopyObjectOperationTypeDef",
    "S3GeneratedManifestDescriptorTypeDef",
    "S3GrantTypeDef",
    "S3GranteeTypeDef",
    "S3InitiateRestoreObjectOperationTypeDef",
    "S3JobManifestGeneratorOutputTypeDef",
    "S3JobManifestGeneratorTypeDef",
    "S3ManifestOutputLocationOutputTypeDef",
    "S3ManifestOutputLocationTypeDef",
    "S3ObjectLockLegalHoldTypeDef",
    "S3ObjectMetadataOutputTypeDef",
    "S3ObjectMetadataTypeDef",
    "S3ObjectOwnerTypeDef",
    "S3RetentionOutputTypeDef",
    "S3RetentionTypeDef",
    "S3SetObjectAclOperationOutputTypeDef",
    "S3SetObjectAclOperationTypeDef",
    "S3SetObjectLegalHoldOperationTypeDef",
    "S3SetObjectRetentionOperationOutputTypeDef",
    "S3SetObjectRetentionOperationTypeDef",
    "S3SetObjectTaggingOperationOutputTypeDef",
    "S3SetObjectTaggingOperationTypeDef",
    "S3TagTypeDef",
    "SSEKMSEncryptionTypeDef",
    "SSEKMSTypeDef",
    "ScopeOutputTypeDef",
    "ScopeTypeDef",
    "ScopeUnionTypeDef",
    "SelectionCriteriaTypeDef",
    "SourceSelectionCriteriaTypeDef",
    "SseKmsEncryptedObjectsTypeDef",
    "StorageLensAwsOrgTypeDef",
    "StorageLensConfigurationOutputTypeDef",
    "StorageLensConfigurationTypeDef",
    "StorageLensConfigurationUnionTypeDef",
    "StorageLensDataExportEncryptionOutputTypeDef",
    "StorageLensDataExportEncryptionTypeDef",
    "StorageLensDataExportOutputTypeDef",
    "StorageLensDataExportTypeDef",
    "StorageLensGroupAndOperatorOutputTypeDef",
    "StorageLensGroupAndOperatorTypeDef",
    "StorageLensGroupFilterOutputTypeDef",
    "StorageLensGroupFilterTypeDef",
    "StorageLensGroupLevelOutputTypeDef",
    "StorageLensGroupLevelSelectionCriteriaOutputTypeDef",
    "StorageLensGroupLevelSelectionCriteriaTypeDef",
    "StorageLensGroupLevelTypeDef",
    "StorageLensGroupOrOperatorOutputTypeDef",
    "StorageLensGroupOrOperatorTypeDef",
    "StorageLensGroupOutputTypeDef",
    "StorageLensGroupTypeDef",
    "StorageLensGroupUnionTypeDef",
    "StorageLensTagTypeDef",
    "SubmitMultiRegionAccessPointRoutesRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TaggingTypeDef",
    "TimestampTypeDef",
    "TransitionOutputTypeDef",
    "TransitionTypeDef",
    "TransitionUnionTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAccessGrantsLocationRequestTypeDef",
    "UpdateAccessGrantsLocationResultTypeDef",
    "UpdateJobPriorityRequestTypeDef",
    "UpdateJobPriorityResultTypeDef",
    "UpdateJobStatusRequestTypeDef",
    "UpdateJobStatusResultTypeDef",
    "UpdateStorageLensGroupRequestTypeDef",
    "VersioningConfigurationTypeDef",
    "VpcConfigurationTypeDef",
)

class AbortIncompleteMultipartUploadTypeDef(TypedDict):
    DaysAfterInitiation: NotRequired[int]

class AccessControlTranslationTypeDef(TypedDict):
    Owner: Literal["Destination"]

class AccessGrantsLocationConfigurationTypeDef(TypedDict):
    S3SubPrefix: NotRequired[str]

class VpcConfigurationTypeDef(TypedDict):
    VpcId: str

class ActivityMetricsTypeDef(TypedDict):
    IsEnabled: NotRequired[bool]

class AdvancedCostOptimizationMetricsTypeDef(TypedDict):
    IsEnabled: NotRequired[bool]

class AdvancedDataProtectionMetricsTypeDef(TypedDict):
    IsEnabled: NotRequired[bool]

class DetailedStatusCodesMetricsTypeDef(TypedDict):
    IsEnabled: NotRequired[bool]

class AssociateAccessGrantsIdentityCenterRequestTypeDef(TypedDict):
    AccountId: str
    IdentityCenterArn: str

class AsyncErrorDetailsTypeDef(TypedDict):
    Code: NotRequired[str]
    Message: NotRequired[str]
    Resource: NotRequired[str]
    RequestId: NotRequired[str]

class DeleteMultiRegionAccessPointInputTypeDef(TypedDict):
    Name: str

class PutMultiRegionAccessPointPolicyInputTypeDef(TypedDict):
    Name: str
    Policy: str

class AwsLambdaTransformationTypeDef(TypedDict):
    FunctionArn: str
    FunctionPayload: NotRequired[str]

class CloudWatchMetricsTypeDef(TypedDict):
    IsEnabled: bool

class GranteeTypeDef(TypedDict):
    GranteeType: NotRequired[GranteeTypeType]
    GranteeIdentifier: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ObjectLambdaAccessPointAliasTypeDef(TypedDict):
    Value: NotRequired[str]
    Status: NotRequired[ObjectLambdaAccessPointAliasStatusType]

class PublicAccessBlockConfigurationTypeDef(TypedDict):
    BlockPublicAcls: NotRequired[bool]
    IgnorePublicAcls: NotRequired[bool]
    BlockPublicPolicy: NotRequired[bool]
    RestrictPublicBuckets: NotRequired[bool]

class CreateBucketConfigurationTypeDef(TypedDict):
    LocationConstraint: NotRequired[BucketLocationConstraintType]

class JobReportTypeDef(TypedDict):
    Enabled: bool
    Bucket: NotRequired[str]
    Format: NotRequired[Literal["Report_CSV_20180820"]]
    Prefix: NotRequired[str]
    ReportScope: NotRequired[JobReportScopeType]

class S3TagTypeDef(TypedDict):
    Key: str
    Value: str

class RegionTypeDef(TypedDict):
    Bucket: str
    BucketAccountId: NotRequired[str]

class CredentialsTypeDef(TypedDict):
    AccessKeyId: NotRequired[str]
    SecretAccessKey: NotRequired[str]
    SessionToken: NotRequired[str]
    Expiration: NotRequired[datetime]

class DeleteAccessGrantRequestTypeDef(TypedDict):
    AccountId: str
    AccessGrantId: str

class DeleteAccessGrantsInstanceRequestTypeDef(TypedDict):
    AccountId: str

class DeleteAccessGrantsInstanceResourcePolicyRequestTypeDef(TypedDict):
    AccountId: str

class DeleteAccessGrantsLocationRequestTypeDef(TypedDict):
    AccountId: str
    AccessGrantsLocationId: str

class DeleteAccessPointForObjectLambdaRequestTypeDef(TypedDict):
    AccountId: str
    Name: str

class DeleteAccessPointPolicyForObjectLambdaRequestTypeDef(TypedDict):
    AccountId: str
    Name: str

class DeleteAccessPointPolicyRequestTypeDef(TypedDict):
    AccountId: str
    Name: str

class DeleteAccessPointRequestTypeDef(TypedDict):
    AccountId: str
    Name: str

class DeleteAccessPointScopeRequestTypeDef(TypedDict):
    AccountId: str
    Name: str

class DeleteBucketLifecycleConfigurationRequestTypeDef(TypedDict):
    AccountId: str
    Bucket: str

class DeleteBucketPolicyRequestTypeDef(TypedDict):
    AccountId: str
    Bucket: str

class DeleteBucketReplicationRequestTypeDef(TypedDict):
    AccountId: str
    Bucket: str

class DeleteBucketRequestTypeDef(TypedDict):
    AccountId: str
    Bucket: str

class DeleteBucketTaggingRequestTypeDef(TypedDict):
    AccountId: str
    Bucket: str

class DeleteJobTaggingRequestTypeDef(TypedDict):
    AccountId: str
    JobId: str

class DeleteMarkerReplicationTypeDef(TypedDict):
    Status: DeleteMarkerReplicationStatusType

class DeletePublicAccessBlockRequestTypeDef(TypedDict):
    AccountId: str

class DeleteStorageLensConfigurationRequestTypeDef(TypedDict):
    ConfigId: str
    AccountId: str

class DeleteStorageLensConfigurationTaggingRequestTypeDef(TypedDict):
    ConfigId: str
    AccountId: str

class DeleteStorageLensGroupRequestTypeDef(TypedDict):
    Name: str
    AccountId: str

class DescribeJobRequestTypeDef(TypedDict):
    AccountId: str
    JobId: str

class DescribeMultiRegionAccessPointOperationRequestTypeDef(TypedDict):
    AccountId: str
    RequestTokenARN: str

class EncryptionConfigurationTypeDef(TypedDict):
    ReplicaKmsKeyID: NotRequired[str]

class DissociateAccessGrantsIdentityCenterRequestTypeDef(TypedDict):
    AccountId: str

class EstablishedMultiRegionAccessPointPolicyTypeDef(TypedDict):
    Policy: NotRequired[str]

class ExcludeOutputTypeDef(TypedDict):
    Buckets: NotRequired[List[str]]
    Regions: NotRequired[List[str]]

class ExcludeTypeDef(TypedDict):
    Buckets: NotRequired[Sequence[str]]
    Regions: NotRequired[Sequence[str]]

class ExistingObjectReplicationTypeDef(TypedDict):
    Status: ExistingObjectReplicationStatusType

class SSEKMSEncryptionTypeDef(TypedDict):
    KeyId: str

class GetAccessGrantRequestTypeDef(TypedDict):
    AccountId: str
    AccessGrantId: str

class GetAccessGrantsInstanceForPrefixRequestTypeDef(TypedDict):
    AccountId: str
    S3Prefix: str

class GetAccessGrantsInstanceRequestTypeDef(TypedDict):
    AccountId: str

class GetAccessGrantsInstanceResourcePolicyRequestTypeDef(TypedDict):
    AccountId: str

class GetAccessGrantsLocationRequestTypeDef(TypedDict):
    AccountId: str
    AccessGrantsLocationId: str

class GetAccessPointConfigurationForObjectLambdaRequestTypeDef(TypedDict):
    AccountId: str
    Name: str

class GetAccessPointForObjectLambdaRequestTypeDef(TypedDict):
    AccountId: str
    Name: str

class GetAccessPointPolicyForObjectLambdaRequestTypeDef(TypedDict):
    AccountId: str
    Name: str

class GetAccessPointPolicyRequestTypeDef(TypedDict):
    AccountId: str
    Name: str

class GetAccessPointPolicyStatusForObjectLambdaRequestTypeDef(TypedDict):
    AccountId: str
    Name: str

class PolicyStatusTypeDef(TypedDict):
    IsPublic: NotRequired[bool]

class GetAccessPointPolicyStatusRequestTypeDef(TypedDict):
    AccountId: str
    Name: str

class GetAccessPointRequestTypeDef(TypedDict):
    AccountId: str
    Name: str

class GetAccessPointScopeRequestTypeDef(TypedDict):
    AccountId: str
    Name: str

class ScopeOutputTypeDef(TypedDict):
    Prefixes: NotRequired[List[str]]
    Permissions: NotRequired[List[ScopePermissionType]]

class GetBucketLifecycleConfigurationRequestTypeDef(TypedDict):
    AccountId: str
    Bucket: str

class GetBucketPolicyRequestTypeDef(TypedDict):
    AccountId: str
    Bucket: str

class GetBucketReplicationRequestTypeDef(TypedDict):
    AccountId: str
    Bucket: str

class GetBucketRequestTypeDef(TypedDict):
    AccountId: str
    Bucket: str

class GetBucketTaggingRequestTypeDef(TypedDict):
    AccountId: str
    Bucket: str

class GetBucketVersioningRequestTypeDef(TypedDict):
    AccountId: str
    Bucket: str

class GetDataAccessRequestTypeDef(TypedDict):
    AccountId: str
    Target: str
    Permission: PermissionType
    DurationSeconds: NotRequired[int]
    Privilege: NotRequired[PrivilegeType]
    TargetType: NotRequired[Literal["Object"]]

class GetJobTaggingRequestTypeDef(TypedDict):
    AccountId: str
    JobId: str

class GetMultiRegionAccessPointPolicyRequestTypeDef(TypedDict):
    AccountId: str
    Name: str

class GetMultiRegionAccessPointPolicyStatusRequestTypeDef(TypedDict):
    AccountId: str
    Name: str

class GetMultiRegionAccessPointRequestTypeDef(TypedDict):
    AccountId: str
    Name: str

class GetMultiRegionAccessPointRoutesRequestTypeDef(TypedDict):
    AccountId: str
    Mrap: str

class MultiRegionAccessPointRouteTypeDef(TypedDict):
    TrafficDialPercentage: int
    Bucket: NotRequired[str]
    Region: NotRequired[str]

class GetPublicAccessBlockRequestTypeDef(TypedDict):
    AccountId: str

class GetStorageLensConfigurationRequestTypeDef(TypedDict):
    ConfigId: str
    AccountId: str

class GetStorageLensConfigurationTaggingRequestTypeDef(TypedDict):
    ConfigId: str
    AccountId: str

class StorageLensTagTypeDef(TypedDict):
    Key: str
    Value: str

class GetStorageLensGroupRequestTypeDef(TypedDict):
    Name: str
    AccountId: str

class IncludeOutputTypeDef(TypedDict):
    Buckets: NotRequired[List[str]]
    Regions: NotRequired[List[str]]

class IncludeTypeDef(TypedDict):
    Buckets: NotRequired[Sequence[str]]
    Regions: NotRequired[Sequence[str]]

class JobFailureTypeDef(TypedDict):
    FailureCode: NotRequired[str]
    FailureReason: NotRequired[str]

class KeyNameConstraintOutputTypeDef(TypedDict):
    MatchAnyPrefix: NotRequired[List[str]]
    MatchAnySuffix: NotRequired[List[str]]
    MatchAnySubstring: NotRequired[List[str]]

class KeyNameConstraintTypeDef(TypedDict):
    MatchAnyPrefix: NotRequired[Sequence[str]]
    MatchAnySuffix: NotRequired[Sequence[str]]
    MatchAnySubstring: NotRequired[Sequence[str]]

TimestampTypeDef = Union[datetime, str]

class JobManifestLocationTypeDef(TypedDict):
    ObjectArn: str
    ETag: str
    ObjectVersionId: NotRequired[str]

class JobManifestSpecOutputTypeDef(TypedDict):
    Format: JobManifestFormatType
    Fields: NotRequired[List[JobManifestFieldNameType]]

class JobManifestSpecTypeDef(TypedDict):
    Format: JobManifestFormatType
    Fields: NotRequired[Sequence[JobManifestFieldNameType]]

class LambdaInvokeOperationOutputTypeDef(TypedDict):
    FunctionArn: NotRequired[str]
    InvocationSchemaVersion: NotRequired[str]
    UserArguments: NotRequired[Dict[str, str]]

class S3InitiateRestoreObjectOperationTypeDef(TypedDict):
    ExpirationInDays: NotRequired[int]
    GlacierJobTier: NotRequired[S3GlacierJobTierType]

class LambdaInvokeOperationTypeDef(TypedDict):
    FunctionArn: NotRequired[str]
    InvocationSchemaVersion: NotRequired[str]
    UserArguments: NotRequired[Mapping[str, str]]

class JobTimersTypeDef(TypedDict):
    ElapsedTimeInActiveSeconds: NotRequired[int]

class LifecycleExpirationOutputTypeDef(TypedDict):
    Date: NotRequired[datetime]
    Days: NotRequired[int]
    ExpiredObjectDeleteMarker: NotRequired[bool]

class NoncurrentVersionExpirationTypeDef(TypedDict):
    NoncurrentDays: NotRequired[int]
    NewerNoncurrentVersions: NotRequired[int]

class NoncurrentVersionTransitionTypeDef(TypedDict):
    NoncurrentDays: NotRequired[int]
    StorageClass: NotRequired[TransitionStorageClassType]

class TransitionOutputTypeDef(TypedDict):
    Date: NotRequired[datetime]
    Days: NotRequired[int]
    StorageClass: NotRequired[TransitionStorageClassType]

class ListAccessGrantsInstanceEntryTypeDef(TypedDict):
    AccessGrantsInstanceId: NotRequired[str]
    AccessGrantsInstanceArn: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    IdentityCenterArn: NotRequired[str]
    IdentityCenterInstanceArn: NotRequired[str]
    IdentityCenterApplicationArn: NotRequired[str]

class ListAccessGrantsInstancesRequestTypeDef(TypedDict):
    AccountId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListAccessGrantsLocationsEntryTypeDef(TypedDict):
    CreatedAt: NotRequired[datetime]
    AccessGrantsLocationId: NotRequired[str]
    AccessGrantsLocationArn: NotRequired[str]
    LocationScope: NotRequired[str]
    IAMRoleArn: NotRequired[str]

class ListAccessGrantsLocationsRequestTypeDef(TypedDict):
    AccountId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    LocationScope: NotRequired[str]

class ListAccessGrantsRequestTypeDef(TypedDict):
    AccountId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    GranteeType: NotRequired[GranteeTypeType]
    GranteeIdentifier: NotRequired[str]
    Permission: NotRequired[PermissionType]
    GrantScope: NotRequired[str]
    ApplicationArn: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAccessPointsForDirectoryBucketsRequestTypeDef(TypedDict):
    AccountId: str
    DirectoryBucket: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListAccessPointsForObjectLambdaRequestTypeDef(TypedDict):
    AccountId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListAccessPointsRequestTypeDef(TypedDict):
    AccountId: str
    Bucket: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListCallerAccessGrantsEntryTypeDef(TypedDict):
    Permission: NotRequired[PermissionType]
    GrantScope: NotRequired[str]
    ApplicationArn: NotRequired[str]

class ListCallerAccessGrantsRequestTypeDef(TypedDict):
    AccountId: str
    GrantScope: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    AllowedByApplication: NotRequired[bool]

class ListJobsRequestTypeDef(TypedDict):
    AccountId: str
    JobStatuses: NotRequired[Sequence[JobStatusType]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListMultiRegionAccessPointsRequestTypeDef(TypedDict):
    AccountId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListRegionalBucketsRequestTypeDef(TypedDict):
    AccountId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    OutpostId: NotRequired[str]

class RegionalBucketTypeDef(TypedDict):
    Bucket: str
    PublicAccessBlockEnabled: bool
    CreationDate: datetime
    BucketArn: NotRequired[str]
    OutpostId: NotRequired[str]

class ListStorageLensConfigurationEntryTypeDef(TypedDict):
    Id: str
    StorageLensArn: str
    HomeRegion: str
    IsEnabled: NotRequired[bool]

class ListStorageLensConfigurationsRequestTypeDef(TypedDict):
    AccountId: str
    NextToken: NotRequired[str]

class ListStorageLensGroupEntryTypeDef(TypedDict):
    Name: str
    StorageLensGroupArn: str
    HomeRegion: str

class ListStorageLensGroupsRequestTypeDef(TypedDict):
    AccountId: str
    NextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    AccountId: str
    ResourceArn: str

class MatchObjectAgeTypeDef(TypedDict):
    DaysGreaterThan: NotRequired[int]
    DaysLessThan: NotRequired[int]

class MatchObjectSizeTypeDef(TypedDict):
    BytesGreaterThan: NotRequired[int]
    BytesLessThan: NotRequired[int]

class ReplicationTimeValueTypeDef(TypedDict):
    Minutes: NotRequired[int]

class ProposedMultiRegionAccessPointPolicyTypeDef(TypedDict):
    Policy: NotRequired[str]

class MultiRegionAccessPointRegionalResponseTypeDef(TypedDict):
    Name: NotRequired[str]
    RequestStatus: NotRequired[str]

class RegionReportTypeDef(TypedDict):
    Bucket: NotRequired[str]
    Region: NotRequired[str]
    BucketAccountId: NotRequired[str]

class SelectionCriteriaTypeDef(TypedDict):
    Delimiter: NotRequired[str]
    MaxDepth: NotRequired[int]
    MinStorageBytesPercentage: NotRequired[float]

class PutAccessGrantsInstanceResourcePolicyRequestTypeDef(TypedDict):
    AccountId: str
    Policy: str
    Organization: NotRequired[str]

class PutAccessPointPolicyForObjectLambdaRequestTypeDef(TypedDict):
    AccountId: str
    Name: str
    Policy: str

class PutAccessPointPolicyRequestTypeDef(TypedDict):
    AccountId: str
    Name: str
    Policy: str

class PutBucketPolicyRequestTypeDef(TypedDict):
    AccountId: str
    Bucket: str
    Policy: str
    ConfirmRemoveSelfBucketAccess: NotRequired[bool]

class VersioningConfigurationTypeDef(TypedDict):
    MFADelete: NotRequired[MFADeleteType]
    Status: NotRequired[BucketVersioningStatusType]

class ReplicaModificationsTypeDef(TypedDict):
    Status: ReplicaModificationsStatusType

class S3ObjectOwnerTypeDef(TypedDict):
    ID: NotRequired[str]
    DisplayName: NotRequired[str]

class S3ObjectMetadataOutputTypeDef(TypedDict):
    CacheControl: NotRequired[str]
    ContentDisposition: NotRequired[str]
    ContentEncoding: NotRequired[str]
    ContentLanguage: NotRequired[str]
    UserMetadata: NotRequired[Dict[str, str]]
    ContentLength: NotRequired[int]
    ContentMD5: NotRequired[str]
    ContentType: NotRequired[str]
    HttpExpiresDate: NotRequired[datetime]
    RequesterCharged: NotRequired[bool]
    SSEAlgorithm: NotRequired[S3SSEAlgorithmType]

class S3GranteeTypeDef(TypedDict):
    TypeIdentifier: NotRequired[S3GranteeTypeIdentifierType]
    Identifier: NotRequired[str]
    DisplayName: NotRequired[str]

class S3ObjectLockLegalHoldTypeDef(TypedDict):
    Status: S3ObjectLockLegalHoldStatusType

class S3RetentionOutputTypeDef(TypedDict):
    RetainUntilDate: NotRequired[datetime]
    Mode: NotRequired[S3ObjectLockRetentionModeType]

class SSEKMSTypeDef(TypedDict):
    KeyId: str

class ScopeTypeDef(TypedDict):
    Prefixes: NotRequired[Sequence[str]]
    Permissions: NotRequired[Sequence[ScopePermissionType]]

class SseKmsEncryptedObjectsTypeDef(TypedDict):
    Status: SseKmsEncryptedObjectsStatusType

class StorageLensAwsOrgTypeDef(TypedDict):
    Arn: str

class StorageLensGroupLevelSelectionCriteriaOutputTypeDef(TypedDict):
    Include: NotRequired[List[str]]
    Exclude: NotRequired[List[str]]

class StorageLensGroupLevelSelectionCriteriaTypeDef(TypedDict):
    Include: NotRequired[Sequence[str]]
    Exclude: NotRequired[Sequence[str]]

class UntagResourceRequestTypeDef(TypedDict):
    AccountId: str
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateAccessGrantsLocationRequestTypeDef(TypedDict):
    AccountId: str
    AccessGrantsLocationId: str
    IAMRoleArn: str

class UpdateJobPriorityRequestTypeDef(TypedDict):
    AccountId: str
    JobId: str
    Priority: int

class UpdateJobStatusRequestTypeDef(TypedDict):
    AccountId: str
    JobId: str
    RequestedJobStatus: RequestedJobStatusType
    StatusUpdateReason: NotRequired[str]

class AccessPointTypeDef(TypedDict):
    Name: str
    NetworkOrigin: NetworkOriginType
    Bucket: str
    VpcConfiguration: NotRequired[VpcConfigurationTypeDef]
    AccessPointArn: NotRequired[str]
    Alias: NotRequired[str]
    BucketAccountId: NotRequired[str]

class DeleteMultiRegionAccessPointRequestTypeDef(TypedDict):
    AccountId: str
    ClientToken: str
    Details: DeleteMultiRegionAccessPointInputTypeDef

class PutMultiRegionAccessPointPolicyRequestTypeDef(TypedDict):
    AccountId: str
    ClientToken: str
    Details: PutMultiRegionAccessPointPolicyInputTypeDef

class ObjectLambdaContentTransformationTypeDef(TypedDict):
    AwsLambda: NotRequired[AwsLambdaTransformationTypeDef]

class ListAccessGrantEntryTypeDef(TypedDict):
    CreatedAt: NotRequired[datetime]
    AccessGrantId: NotRequired[str]
    AccessGrantArn: NotRequired[str]
    Grantee: NotRequired[GranteeTypeDef]
    Permission: NotRequired[PermissionType]
    AccessGrantsLocationId: NotRequired[str]
    AccessGrantsLocationConfiguration: NotRequired[AccessGrantsLocationConfigurationTypeDef]
    GrantScope: NotRequired[str]
    ApplicationArn: NotRequired[str]

class CreateAccessGrantRequestTypeDef(TypedDict):
    AccountId: str
    AccessGrantsLocationId: str
    Grantee: GranteeTypeDef
    Permission: PermissionType
    AccessGrantsLocationConfiguration: NotRequired[AccessGrantsLocationConfigurationTypeDef]
    ApplicationArn: NotRequired[str]
    S3PrefixType: NotRequired[Literal["Object"]]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateAccessGrantsInstanceRequestTypeDef(TypedDict):
    AccountId: str
    IdentityCenterArn: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateAccessGrantsLocationRequestTypeDef(TypedDict):
    AccountId: str
    LocationScope: str
    IAMRoleArn: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class TagResourceRequestTypeDef(TypedDict):
    AccountId: str
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateAccessGrantResultTypeDef(TypedDict):
    CreatedAt: datetime
    AccessGrantId: str
    AccessGrantArn: str
    Grantee: GranteeTypeDef
    AccessGrantsLocationId: str
    AccessGrantsLocationConfiguration: AccessGrantsLocationConfigurationTypeDef
    Permission: PermissionType
    ApplicationArn: str
    GrantScope: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessGrantsInstanceResultTypeDef(TypedDict):
    CreatedAt: datetime
    AccessGrantsInstanceId: str
    AccessGrantsInstanceArn: str
    IdentityCenterArn: str
    IdentityCenterInstanceArn: str
    IdentityCenterApplicationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessGrantsLocationResultTypeDef(TypedDict):
    CreatedAt: datetime
    AccessGrantsLocationId: str
    AccessGrantsLocationArn: str
    LocationScope: str
    IAMRoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessPointResultTypeDef(TypedDict):
    AccessPointArn: str
    Alias: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBucketResultTypeDef(TypedDict):
    Location: str
    BucketArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobResultTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMultiRegionAccessPointResultTypeDef(TypedDict):
    RequestTokenARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMultiRegionAccessPointResultTypeDef(TypedDict):
    RequestTokenARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessGrantResultTypeDef(TypedDict):
    CreatedAt: datetime
    AccessGrantId: str
    AccessGrantArn: str
    Grantee: GranteeTypeDef
    Permission: PermissionType
    AccessGrantsLocationId: str
    AccessGrantsLocationConfiguration: AccessGrantsLocationConfigurationTypeDef
    GrantScope: str
    ApplicationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessGrantsInstanceForPrefixResultTypeDef(TypedDict):
    AccessGrantsInstanceArn: str
    AccessGrantsInstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessGrantsInstanceResourcePolicyResultTypeDef(TypedDict):
    Policy: str
    Organization: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessGrantsInstanceResultTypeDef(TypedDict):
    AccessGrantsInstanceArn: str
    AccessGrantsInstanceId: str
    IdentityCenterArn: str
    IdentityCenterInstanceArn: str
    IdentityCenterApplicationArn: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessGrantsLocationResultTypeDef(TypedDict):
    CreatedAt: datetime
    AccessGrantsLocationId: str
    AccessGrantsLocationArn: str
    LocationScope: str
    IAMRoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessPointPolicyForObjectLambdaResultTypeDef(TypedDict):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessPointPolicyResultTypeDef(TypedDict):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBucketPolicyResultTypeDef(TypedDict):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBucketResultTypeDef(TypedDict):
    Bucket: str
    PublicAccessBlockEnabled: bool
    CreationDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetBucketVersioningResultTypeDef(TypedDict):
    Status: BucketVersioningStatusType
    MFADelete: MFADeleteStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResultTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutAccessGrantsInstanceResourcePolicyResultTypeDef(TypedDict):
    Policy: str
    Organization: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PutMultiRegionAccessPointPolicyResultTypeDef(TypedDict):
    RequestTokenARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccessGrantsLocationResultTypeDef(TypedDict):
    CreatedAt: datetime
    AccessGrantsLocationId: str
    AccessGrantsLocationArn: str
    LocationScope: str
    IAMRoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateJobPriorityResultTypeDef(TypedDict):
    JobId: str
    Priority: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateJobStatusResultTypeDef(TypedDict):
    JobId: str
    Status: JobStatusType
    StatusUpdateReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessPointForObjectLambdaResultTypeDef(TypedDict):
    ObjectLambdaAccessPointArn: str
    Alias: ObjectLambdaAccessPointAliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ObjectLambdaAccessPointTypeDef(TypedDict):
    Name: str
    ObjectLambdaAccessPointArn: NotRequired[str]
    Alias: NotRequired[ObjectLambdaAccessPointAliasTypeDef]

class GetAccessPointForObjectLambdaResultTypeDef(TypedDict):
    Name: str
    PublicAccessBlockConfiguration: PublicAccessBlockConfigurationTypeDef
    CreationDate: datetime
    Alias: ObjectLambdaAccessPointAliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessPointResultTypeDef(TypedDict):
    Name: str
    Bucket: str
    NetworkOrigin: NetworkOriginType
    VpcConfiguration: VpcConfigurationTypeDef
    PublicAccessBlockConfiguration: PublicAccessBlockConfigurationTypeDef
    CreationDate: datetime
    Alias: str
    AccessPointArn: str
    Endpoints: Dict[str, str]
    BucketAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPublicAccessBlockOutputTypeDef(TypedDict):
    PublicAccessBlockConfiguration: PublicAccessBlockConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutPublicAccessBlockRequestTypeDef(TypedDict):
    PublicAccessBlockConfiguration: PublicAccessBlockConfigurationTypeDef
    AccountId: str

class CreateBucketRequestTypeDef(TypedDict):
    Bucket: str
    ACL: NotRequired[BucketCannedACLType]
    CreateBucketConfiguration: NotRequired[CreateBucketConfigurationTypeDef]
    GrantFullControl: NotRequired[str]
    GrantRead: NotRequired[str]
    GrantReadACP: NotRequired[str]
    GrantWrite: NotRequired[str]
    GrantWriteACP: NotRequired[str]
    ObjectLockEnabledForBucket: NotRequired[bool]
    OutpostId: NotRequired[str]

class GetBucketTaggingResultTypeDef(TypedDict):
    TagSet: List[S3TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobTaggingResultTypeDef(TypedDict):
    Tags: List[S3TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LifecycleRuleAndOperatorOutputTypeDef(TypedDict):
    Prefix: NotRequired[str]
    Tags: NotRequired[List[S3TagTypeDef]]
    ObjectSizeGreaterThan: NotRequired[int]
    ObjectSizeLessThan: NotRequired[int]

class LifecycleRuleAndOperatorTypeDef(TypedDict):
    Prefix: NotRequired[str]
    Tags: NotRequired[Sequence[S3TagTypeDef]]
    ObjectSizeGreaterThan: NotRequired[int]
    ObjectSizeLessThan: NotRequired[int]

class PutJobTaggingRequestTypeDef(TypedDict):
    AccountId: str
    JobId: str
    Tags: Sequence[S3TagTypeDef]

class ReplicationRuleAndOperatorOutputTypeDef(TypedDict):
    Prefix: NotRequired[str]
    Tags: NotRequired[List[S3TagTypeDef]]

class ReplicationRuleAndOperatorTypeDef(TypedDict):
    Prefix: NotRequired[str]
    Tags: NotRequired[Sequence[S3TagTypeDef]]

class S3SetObjectTaggingOperationOutputTypeDef(TypedDict):
    TagSet: NotRequired[List[S3TagTypeDef]]

class S3SetObjectTaggingOperationTypeDef(TypedDict):
    TagSet: NotRequired[Sequence[S3TagTypeDef]]

class TaggingTypeDef(TypedDict):
    TagSet: Sequence[S3TagTypeDef]

class CreateMultiRegionAccessPointInputOutputTypeDef(TypedDict):
    Name: str
    Regions: List[RegionTypeDef]
    PublicAccessBlock: NotRequired[PublicAccessBlockConfigurationTypeDef]

class CreateMultiRegionAccessPointInputTypeDef(TypedDict):
    Name: str
    Regions: Sequence[RegionTypeDef]
    PublicAccessBlock: NotRequired[PublicAccessBlockConfigurationTypeDef]

class GetDataAccessResultTypeDef(TypedDict):
    Credentials: CredentialsTypeDef
    MatchedGrantTarget: str
    Grantee: GranteeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GeneratedManifestEncryptionOutputTypeDef(TypedDict):
    SSES3: NotRequired[Dict[str, Any]]
    SSEKMS: NotRequired[SSEKMSEncryptionTypeDef]

class GeneratedManifestEncryptionTypeDef(TypedDict):
    SSES3: NotRequired[Mapping[str, Any]]
    SSEKMS: NotRequired[SSEKMSEncryptionTypeDef]

class GetAccessPointPolicyStatusForObjectLambdaResultTypeDef(TypedDict):
    PolicyStatus: PolicyStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessPointPolicyStatusResultTypeDef(TypedDict):
    PolicyStatus: PolicyStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMultiRegionAccessPointPolicyStatusResultTypeDef(TypedDict):
    Established: PolicyStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessPointScopeResultTypeDef(TypedDict):
    Scope: ScopeOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMultiRegionAccessPointRoutesResultTypeDef(TypedDict):
    Mrap: str
    Routes: List[MultiRegionAccessPointRouteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SubmitMultiRegionAccessPointRoutesRequestTypeDef(TypedDict):
    AccountId: str
    Mrap: str
    RouteUpdates: Sequence[MultiRegionAccessPointRouteTypeDef]

class GetStorageLensConfigurationTaggingResultTypeDef(TypedDict):
    Tags: List[StorageLensTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutStorageLensConfigurationTaggingRequestTypeDef(TypedDict):
    ConfigId: str
    AccountId: str
    Tags: Sequence[StorageLensTagTypeDef]

class JobManifestGeneratorFilterOutputTypeDef(TypedDict):
    EligibleForReplication: NotRequired[bool]
    CreatedAfter: NotRequired[datetime]
    CreatedBefore: NotRequired[datetime]
    ObjectReplicationStatuses: NotRequired[List[ReplicationStatusType]]
    KeyNameConstraint: NotRequired[KeyNameConstraintOutputTypeDef]
    ObjectSizeGreaterThanBytes: NotRequired[int]
    ObjectSizeLessThanBytes: NotRequired[int]
    MatchAnyStorageClass: NotRequired[List[S3StorageClassType]]

class JobManifestGeneratorFilterTypeDef(TypedDict):
    EligibleForReplication: NotRequired[bool]
    CreatedAfter: NotRequired[TimestampTypeDef]
    CreatedBefore: NotRequired[TimestampTypeDef]
    ObjectReplicationStatuses: NotRequired[Sequence[ReplicationStatusType]]
    KeyNameConstraint: NotRequired[KeyNameConstraintTypeDef]
    ObjectSizeGreaterThanBytes: NotRequired[int]
    ObjectSizeLessThanBytes: NotRequired[int]
    MatchAnyStorageClass: NotRequired[Sequence[S3StorageClassType]]

class LifecycleExpirationTypeDef(TypedDict):
    Date: NotRequired[TimestampTypeDef]
    Days: NotRequired[int]
    ExpiredObjectDeleteMarker: NotRequired[bool]

class S3ObjectMetadataTypeDef(TypedDict):
    CacheControl: NotRequired[str]
    ContentDisposition: NotRequired[str]
    ContentEncoding: NotRequired[str]
    ContentLanguage: NotRequired[str]
    UserMetadata: NotRequired[Mapping[str, str]]
    ContentLength: NotRequired[int]
    ContentMD5: NotRequired[str]
    ContentType: NotRequired[str]
    HttpExpiresDate: NotRequired[TimestampTypeDef]
    RequesterCharged: NotRequired[bool]
    SSEAlgorithm: NotRequired[S3SSEAlgorithmType]

class S3RetentionTypeDef(TypedDict):
    RetainUntilDate: NotRequired[TimestampTypeDef]
    Mode: NotRequired[S3ObjectLockRetentionModeType]

class TransitionTypeDef(TypedDict):
    Date: NotRequired[TimestampTypeDef]
    Days: NotRequired[int]
    StorageClass: NotRequired[TransitionStorageClassType]

class S3GeneratedManifestDescriptorTypeDef(TypedDict):
    Format: NotRequired[Literal["S3InventoryReport_CSV_20211130"]]
    Location: NotRequired[JobManifestLocationTypeDef]

class JobManifestOutputTypeDef(TypedDict):
    Spec: JobManifestSpecOutputTypeDef
    Location: JobManifestLocationTypeDef

class JobManifestTypeDef(TypedDict):
    Spec: JobManifestSpecTypeDef
    Location: JobManifestLocationTypeDef

class JobProgressSummaryTypeDef(TypedDict):
    TotalNumberOfTasks: NotRequired[int]
    NumberOfTasksSucceeded: NotRequired[int]
    NumberOfTasksFailed: NotRequired[int]
    Timers: NotRequired[JobTimersTypeDef]

class ListAccessGrantsInstancesResultTypeDef(TypedDict):
    AccessGrantsInstancesList: List[ListAccessGrantsInstanceEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListAccessGrantsLocationsResultTypeDef(TypedDict):
    AccessGrantsLocationsList: List[ListAccessGrantsLocationsEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListAccessPointsForDirectoryBucketsRequestPaginateTypeDef(TypedDict):
    AccountId: str
    DirectoryBucket: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAccessPointsForObjectLambdaRequestPaginateTypeDef(TypedDict):
    AccountId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCallerAccessGrantsRequestPaginateTypeDef(TypedDict):
    AccountId: str
    GrantScope: NotRequired[str]
    AllowedByApplication: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCallerAccessGrantsResultTypeDef(TypedDict):
    CallerAccessGrantsList: List[ListCallerAccessGrantsEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRegionalBucketsResultTypeDef(TypedDict):
    RegionalBucketList: List[RegionalBucketTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListStorageLensConfigurationsResultTypeDef(TypedDict):
    StorageLensConfigurationList: List[ListStorageLensConfigurationEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListStorageLensGroupsResultTypeDef(TypedDict):
    StorageLensGroupList: List[ListStorageLensGroupEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class StorageLensGroupAndOperatorOutputTypeDef(TypedDict):
    MatchAnyPrefix: NotRequired[List[str]]
    MatchAnySuffix: NotRequired[List[str]]
    MatchAnyTag: NotRequired[List[S3TagTypeDef]]
    MatchObjectAge: NotRequired[MatchObjectAgeTypeDef]
    MatchObjectSize: NotRequired[MatchObjectSizeTypeDef]

class StorageLensGroupAndOperatorTypeDef(TypedDict):
    MatchAnyPrefix: NotRequired[Sequence[str]]
    MatchAnySuffix: NotRequired[Sequence[str]]
    MatchAnyTag: NotRequired[Sequence[S3TagTypeDef]]
    MatchObjectAge: NotRequired[MatchObjectAgeTypeDef]
    MatchObjectSize: NotRequired[MatchObjectSizeTypeDef]

class StorageLensGroupOrOperatorOutputTypeDef(TypedDict):
    MatchAnyPrefix: NotRequired[List[str]]
    MatchAnySuffix: NotRequired[List[str]]
    MatchAnyTag: NotRequired[List[S3TagTypeDef]]
    MatchObjectAge: NotRequired[MatchObjectAgeTypeDef]
    MatchObjectSize: NotRequired[MatchObjectSizeTypeDef]

class StorageLensGroupOrOperatorTypeDef(TypedDict):
    MatchAnyPrefix: NotRequired[Sequence[str]]
    MatchAnySuffix: NotRequired[Sequence[str]]
    MatchAnyTag: NotRequired[Sequence[S3TagTypeDef]]
    MatchObjectAge: NotRequired[MatchObjectAgeTypeDef]
    MatchObjectSize: NotRequired[MatchObjectSizeTypeDef]

class MetricsTypeDef(TypedDict):
    Status: MetricsStatusType
    EventThreshold: NotRequired[ReplicationTimeValueTypeDef]

class ReplicationTimeTypeDef(TypedDict):
    Status: ReplicationTimeStatusType
    Time: ReplicationTimeValueTypeDef

class MultiRegionAccessPointPolicyDocumentTypeDef(TypedDict):
    Established: NotRequired[EstablishedMultiRegionAccessPointPolicyTypeDef]
    Proposed: NotRequired[ProposedMultiRegionAccessPointPolicyTypeDef]

class MultiRegionAccessPointsAsyncResponseTypeDef(TypedDict):
    Regions: NotRequired[List[MultiRegionAccessPointRegionalResponseTypeDef]]

class MultiRegionAccessPointReportTypeDef(TypedDict):
    Name: NotRequired[str]
    Alias: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    PublicAccessBlock: NotRequired[PublicAccessBlockConfigurationTypeDef]
    Status: NotRequired[MultiRegionAccessPointStatusType]
    Regions: NotRequired[List[RegionReportTypeDef]]

class PrefixLevelStorageMetricsTypeDef(TypedDict):
    IsEnabled: NotRequired[bool]
    SelectionCriteria: NotRequired[SelectionCriteriaTypeDef]

class PutBucketVersioningRequestTypeDef(TypedDict):
    AccountId: str
    Bucket: str
    VersioningConfiguration: VersioningConfigurationTypeDef
    MFA: NotRequired[str]

class S3GrantTypeDef(TypedDict):
    Grantee: NotRequired[S3GranteeTypeDef]
    Permission: NotRequired[S3PermissionType]

class S3SetObjectLegalHoldOperationTypeDef(TypedDict):
    LegalHold: S3ObjectLockLegalHoldTypeDef

class S3SetObjectRetentionOperationOutputTypeDef(TypedDict):
    Retention: S3RetentionOutputTypeDef
    BypassGovernanceRetention: NotRequired[bool]

class StorageLensDataExportEncryptionOutputTypeDef(TypedDict):
    SSES3: NotRequired[Dict[str, Any]]
    SSEKMS: NotRequired[SSEKMSTypeDef]

class StorageLensDataExportEncryptionTypeDef(TypedDict):
    SSES3: NotRequired[Mapping[str, Any]]
    SSEKMS: NotRequired[SSEKMSTypeDef]

ScopeUnionTypeDef = Union[ScopeTypeDef, ScopeOutputTypeDef]

class SourceSelectionCriteriaTypeDef(TypedDict):
    SseKmsEncryptedObjects: NotRequired[SseKmsEncryptedObjectsTypeDef]
    ReplicaModifications: NotRequired[ReplicaModificationsTypeDef]

class StorageLensGroupLevelOutputTypeDef(TypedDict):
    SelectionCriteria: NotRequired[StorageLensGroupLevelSelectionCriteriaOutputTypeDef]

class StorageLensGroupLevelTypeDef(TypedDict):
    SelectionCriteria: NotRequired[StorageLensGroupLevelSelectionCriteriaTypeDef]

class ListAccessPointsForDirectoryBucketsResultTypeDef(TypedDict):
    AccessPointList: List[AccessPointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListAccessPointsResultTypeDef(TypedDict):
    AccessPointList: List[AccessPointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ObjectLambdaTransformationConfigurationOutputTypeDef(TypedDict):
    Actions: List[ObjectLambdaTransformationConfigurationActionType]
    ContentTransformation: ObjectLambdaContentTransformationTypeDef

class ObjectLambdaTransformationConfigurationTypeDef(TypedDict):
    Actions: Sequence[ObjectLambdaTransformationConfigurationActionType]
    ContentTransformation: ObjectLambdaContentTransformationTypeDef

class ListAccessGrantsResultTypeDef(TypedDict):
    AccessGrantsList: List[ListAccessGrantEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListAccessPointsForObjectLambdaResultTypeDef(TypedDict):
    ObjectLambdaAccessPointList: List[ObjectLambdaAccessPointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class LifecycleRuleFilterOutputTypeDef(TypedDict):
    Prefix: NotRequired[str]
    Tag: NotRequired[S3TagTypeDef]
    And: NotRequired[LifecycleRuleAndOperatorOutputTypeDef]
    ObjectSizeGreaterThan: NotRequired[int]
    ObjectSizeLessThan: NotRequired[int]

LifecycleRuleAndOperatorUnionTypeDef = Union[
    LifecycleRuleAndOperatorTypeDef, LifecycleRuleAndOperatorOutputTypeDef
]

class ReplicationRuleFilterOutputTypeDef(TypedDict):
    Prefix: NotRequired[str]
    Tag: NotRequired[S3TagTypeDef]
    And: NotRequired[ReplicationRuleAndOperatorOutputTypeDef]

class ReplicationRuleFilterTypeDef(TypedDict):
    Prefix: NotRequired[str]
    Tag: NotRequired[S3TagTypeDef]
    And: NotRequired[ReplicationRuleAndOperatorTypeDef]

class PutBucketTaggingRequestTypeDef(TypedDict):
    AccountId: str
    Bucket: str
    Tagging: TaggingTypeDef

class AsyncRequestParametersTypeDef(TypedDict):
    CreateMultiRegionAccessPointRequest: NotRequired[CreateMultiRegionAccessPointInputOutputTypeDef]
    DeleteMultiRegionAccessPointRequest: NotRequired[DeleteMultiRegionAccessPointInputTypeDef]
    PutMultiRegionAccessPointPolicyRequest: NotRequired[PutMultiRegionAccessPointPolicyInputTypeDef]

CreateMultiRegionAccessPointInputUnionTypeDef = Union[
    CreateMultiRegionAccessPointInputTypeDef, CreateMultiRegionAccessPointInputOutputTypeDef
]

class S3ManifestOutputLocationOutputTypeDef(TypedDict):
    Bucket: str
    ManifestFormat: Literal["S3InventoryReport_CSV_20211130"]
    ExpectedManifestBucketOwner: NotRequired[str]
    ManifestPrefix: NotRequired[str]
    ManifestEncryption: NotRequired[GeneratedManifestEncryptionOutputTypeDef]

class S3ManifestOutputLocationTypeDef(TypedDict):
    Bucket: str
    ManifestFormat: Literal["S3InventoryReport_CSV_20211130"]
    ExpectedManifestBucketOwner: NotRequired[str]
    ManifestPrefix: NotRequired[str]
    ManifestEncryption: NotRequired[GeneratedManifestEncryptionTypeDef]

LifecycleExpirationUnionTypeDef = Union[
    LifecycleExpirationTypeDef, LifecycleExpirationOutputTypeDef
]

class S3SetObjectRetentionOperationTypeDef(TypedDict):
    Retention: S3RetentionTypeDef
    BypassGovernanceRetention: NotRequired[bool]

TransitionUnionTypeDef = Union[TransitionTypeDef, TransitionOutputTypeDef]
JobManifestUnionTypeDef = Union[JobManifestTypeDef, JobManifestOutputTypeDef]

class JobListDescriptorTypeDef(TypedDict):
    JobId: NotRequired[str]
    Description: NotRequired[str]
    Operation: NotRequired[OperationNameType]
    Priority: NotRequired[int]
    Status: NotRequired[JobStatusType]
    CreationTime: NotRequired[datetime]
    TerminationDate: NotRequired[datetime]
    ProgressSummary: NotRequired[JobProgressSummaryTypeDef]

class StorageLensGroupFilterOutputTypeDef(TypedDict):
    MatchAnyPrefix: NotRequired[List[str]]
    MatchAnySuffix: NotRequired[List[str]]
    MatchAnyTag: NotRequired[List[S3TagTypeDef]]
    MatchObjectAge: NotRequired[MatchObjectAgeTypeDef]
    MatchObjectSize: NotRequired[MatchObjectSizeTypeDef]
    And: NotRequired[StorageLensGroupAndOperatorOutputTypeDef]
    Or: NotRequired[StorageLensGroupOrOperatorOutputTypeDef]

class StorageLensGroupFilterTypeDef(TypedDict):
    MatchAnyPrefix: NotRequired[Sequence[str]]
    MatchAnySuffix: NotRequired[Sequence[str]]
    MatchAnyTag: NotRequired[Sequence[S3TagTypeDef]]
    MatchObjectAge: NotRequired[MatchObjectAgeTypeDef]
    MatchObjectSize: NotRequired[MatchObjectSizeTypeDef]
    And: NotRequired[StorageLensGroupAndOperatorTypeDef]
    Or: NotRequired[StorageLensGroupOrOperatorTypeDef]

class DestinationTypeDef(TypedDict):
    Bucket: str
    Account: NotRequired[str]
    ReplicationTime: NotRequired[ReplicationTimeTypeDef]
    AccessControlTranslation: NotRequired[AccessControlTranslationTypeDef]
    EncryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]
    Metrics: NotRequired[MetricsTypeDef]
    StorageClass: NotRequired[ReplicationStorageClassType]

class GetMultiRegionAccessPointPolicyResultTypeDef(TypedDict):
    Policy: MultiRegionAccessPointPolicyDocumentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AsyncResponseDetailsTypeDef(TypedDict):
    MultiRegionAccessPointDetails: NotRequired[MultiRegionAccessPointsAsyncResponseTypeDef]
    ErrorDetails: NotRequired[AsyncErrorDetailsTypeDef]

class GetMultiRegionAccessPointResultTypeDef(TypedDict):
    AccessPoint: MultiRegionAccessPointReportTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListMultiRegionAccessPointsResultTypeDef(TypedDict):
    AccessPoints: List[MultiRegionAccessPointReportTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PrefixLevelTypeDef(TypedDict):
    StorageMetrics: PrefixLevelStorageMetricsTypeDef

class S3AccessControlListOutputTypeDef(TypedDict):
    Owner: S3ObjectOwnerTypeDef
    Grants: NotRequired[List[S3GrantTypeDef]]

class S3AccessControlListTypeDef(TypedDict):
    Owner: S3ObjectOwnerTypeDef
    Grants: NotRequired[Sequence[S3GrantTypeDef]]

class S3CopyObjectOperationOutputTypeDef(TypedDict):
    TargetResource: NotRequired[str]
    CannedAccessControlList: NotRequired[S3CannedAccessControlListType]
    AccessControlGrants: NotRequired[List[S3GrantTypeDef]]
    MetadataDirective: NotRequired[S3MetadataDirectiveType]
    ModifiedSinceConstraint: NotRequired[datetime]
    NewObjectMetadata: NotRequired[S3ObjectMetadataOutputTypeDef]
    NewObjectTagging: NotRequired[List[S3TagTypeDef]]
    RedirectLocation: NotRequired[str]
    RequesterPays: NotRequired[bool]
    StorageClass: NotRequired[S3StorageClassType]
    UnModifiedSinceConstraint: NotRequired[datetime]
    SSEAwsKmsKeyId: NotRequired[str]
    TargetKeyPrefix: NotRequired[str]
    ObjectLockLegalHoldStatus: NotRequired[S3ObjectLockLegalHoldStatusType]
    ObjectLockMode: NotRequired[S3ObjectLockModeType]
    ObjectLockRetainUntilDate: NotRequired[datetime]
    BucketKeyEnabled: NotRequired[bool]
    ChecksumAlgorithm: NotRequired[S3ChecksumAlgorithmType]

class S3CopyObjectOperationTypeDef(TypedDict):
    TargetResource: NotRequired[str]
    CannedAccessControlList: NotRequired[S3CannedAccessControlListType]
    AccessControlGrants: NotRequired[Sequence[S3GrantTypeDef]]
    MetadataDirective: NotRequired[S3MetadataDirectiveType]
    ModifiedSinceConstraint: NotRequired[TimestampTypeDef]
    NewObjectMetadata: NotRequired[S3ObjectMetadataTypeDef]
    NewObjectTagging: NotRequired[Sequence[S3TagTypeDef]]
    RedirectLocation: NotRequired[str]
    RequesterPays: NotRequired[bool]
    StorageClass: NotRequired[S3StorageClassType]
    UnModifiedSinceConstraint: NotRequired[TimestampTypeDef]
    SSEAwsKmsKeyId: NotRequired[str]
    TargetKeyPrefix: NotRequired[str]
    ObjectLockLegalHoldStatus: NotRequired[S3ObjectLockLegalHoldStatusType]
    ObjectLockMode: NotRequired[S3ObjectLockModeType]
    ObjectLockRetainUntilDate: NotRequired[TimestampTypeDef]
    BucketKeyEnabled: NotRequired[bool]
    ChecksumAlgorithm: NotRequired[S3ChecksumAlgorithmType]

class S3BucketDestinationOutputTypeDef(TypedDict):
    Format: FormatType
    OutputSchemaVersion: Literal["V_1"]
    AccountId: str
    Arn: str
    Prefix: NotRequired[str]
    Encryption: NotRequired[StorageLensDataExportEncryptionOutputTypeDef]

class S3BucketDestinationTypeDef(TypedDict):
    Format: FormatType
    OutputSchemaVersion: Literal["V_1"]
    AccountId: str
    Arn: str
    Prefix: NotRequired[str]
    Encryption: NotRequired[StorageLensDataExportEncryptionTypeDef]

class CreateAccessPointRequestTypeDef(TypedDict):
    AccountId: str
    Name: str
    Bucket: str
    VpcConfiguration: NotRequired[VpcConfigurationTypeDef]
    PublicAccessBlockConfiguration: NotRequired[PublicAccessBlockConfigurationTypeDef]
    BucketAccountId: NotRequired[str]
    Scope: NotRequired[ScopeUnionTypeDef]

class PutAccessPointScopeRequestTypeDef(TypedDict):
    AccountId: str
    Name: str
    Scope: ScopeUnionTypeDef

class ObjectLambdaConfigurationOutputTypeDef(TypedDict):
    SupportingAccessPoint: str
    TransformationConfigurations: List[ObjectLambdaTransformationConfigurationOutputTypeDef]
    CloudWatchMetricsEnabled: NotRequired[bool]
    AllowedFeatures: NotRequired[List[ObjectLambdaAllowedFeatureType]]

class ObjectLambdaConfigurationTypeDef(TypedDict):
    SupportingAccessPoint: str
    TransformationConfigurations: Sequence[ObjectLambdaTransformationConfigurationTypeDef]
    CloudWatchMetricsEnabled: NotRequired[bool]
    AllowedFeatures: NotRequired[Sequence[ObjectLambdaAllowedFeatureType]]

class LifecycleRuleOutputTypeDef(TypedDict):
    Status: ExpirationStatusType
    Expiration: NotRequired[LifecycleExpirationOutputTypeDef]
    ID: NotRequired[str]
    Filter: NotRequired[LifecycleRuleFilterOutputTypeDef]
    Transitions: NotRequired[List[TransitionOutputTypeDef]]
    NoncurrentVersionTransitions: NotRequired[List[NoncurrentVersionTransitionTypeDef]]
    NoncurrentVersionExpiration: NotRequired[NoncurrentVersionExpirationTypeDef]
    AbortIncompleteMultipartUpload: NotRequired[AbortIncompleteMultipartUploadTypeDef]

class LifecycleRuleFilterTypeDef(TypedDict):
    Prefix: NotRequired[str]
    Tag: NotRequired[S3TagTypeDef]
    And: NotRequired[LifecycleRuleAndOperatorUnionTypeDef]
    ObjectSizeGreaterThan: NotRequired[int]
    ObjectSizeLessThan: NotRequired[int]

class CreateMultiRegionAccessPointRequestTypeDef(TypedDict):
    AccountId: str
    ClientToken: str
    Details: CreateMultiRegionAccessPointInputUnionTypeDef

class S3JobManifestGeneratorOutputTypeDef(TypedDict):
    SourceBucket: str
    EnableManifestOutput: bool
    ExpectedBucketOwner: NotRequired[str]
    ManifestOutputLocation: NotRequired[S3ManifestOutputLocationOutputTypeDef]
    Filter: NotRequired[JobManifestGeneratorFilterOutputTypeDef]

class S3JobManifestGeneratorTypeDef(TypedDict):
    SourceBucket: str
    EnableManifestOutput: bool
    ExpectedBucketOwner: NotRequired[str]
    ManifestOutputLocation: NotRequired[S3ManifestOutputLocationTypeDef]
    Filter: NotRequired[JobManifestGeneratorFilterTypeDef]

class ListJobsResultTypeDef(TypedDict):
    Jobs: List[JobListDescriptorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class StorageLensGroupOutputTypeDef(TypedDict):
    Name: str
    Filter: StorageLensGroupFilterOutputTypeDef
    StorageLensGroupArn: NotRequired[str]

class StorageLensGroupTypeDef(TypedDict):
    Name: str
    Filter: StorageLensGroupFilterTypeDef
    StorageLensGroupArn: NotRequired[str]

class ReplicationRuleOutputTypeDef(TypedDict):
    Status: ReplicationRuleStatusType
    Destination: DestinationTypeDef
    Bucket: str
    ID: NotRequired[str]
    Priority: NotRequired[int]
    Prefix: NotRequired[str]
    Filter: NotRequired[ReplicationRuleFilterOutputTypeDef]
    SourceSelectionCriteria: NotRequired[SourceSelectionCriteriaTypeDef]
    ExistingObjectReplication: NotRequired[ExistingObjectReplicationTypeDef]
    DeleteMarkerReplication: NotRequired[DeleteMarkerReplicationTypeDef]

class ReplicationRuleTypeDef(TypedDict):
    Status: ReplicationRuleStatusType
    Destination: DestinationTypeDef
    Bucket: str
    ID: NotRequired[str]
    Priority: NotRequired[int]
    Prefix: NotRequired[str]
    Filter: NotRequired[ReplicationRuleFilterTypeDef]
    SourceSelectionCriteria: NotRequired[SourceSelectionCriteriaTypeDef]
    ExistingObjectReplication: NotRequired[ExistingObjectReplicationTypeDef]
    DeleteMarkerReplication: NotRequired[DeleteMarkerReplicationTypeDef]

class AsyncOperationTypeDef(TypedDict):
    CreationTime: NotRequired[datetime]
    Operation: NotRequired[AsyncOperationNameType]
    RequestTokenARN: NotRequired[str]
    RequestParameters: NotRequired[AsyncRequestParametersTypeDef]
    RequestStatus: NotRequired[str]
    ResponseDetails: NotRequired[AsyncResponseDetailsTypeDef]

class BucketLevelTypeDef(TypedDict):
    ActivityMetrics: NotRequired[ActivityMetricsTypeDef]
    PrefixLevel: NotRequired[PrefixLevelTypeDef]
    AdvancedCostOptimizationMetrics: NotRequired[AdvancedCostOptimizationMetricsTypeDef]
    AdvancedDataProtectionMetrics: NotRequired[AdvancedDataProtectionMetricsTypeDef]
    DetailedStatusCodesMetrics: NotRequired[DetailedStatusCodesMetricsTypeDef]

class S3AccessControlPolicyOutputTypeDef(TypedDict):
    AccessControlList: NotRequired[S3AccessControlListOutputTypeDef]
    CannedAccessControlList: NotRequired[S3CannedAccessControlListType]

class S3AccessControlPolicyTypeDef(TypedDict):
    AccessControlList: NotRequired[S3AccessControlListTypeDef]
    CannedAccessControlList: NotRequired[S3CannedAccessControlListType]

class StorageLensDataExportOutputTypeDef(TypedDict):
    S3BucketDestination: NotRequired[S3BucketDestinationOutputTypeDef]
    CloudWatchMetrics: NotRequired[CloudWatchMetricsTypeDef]

class StorageLensDataExportTypeDef(TypedDict):
    S3BucketDestination: NotRequired[S3BucketDestinationTypeDef]
    CloudWatchMetrics: NotRequired[CloudWatchMetricsTypeDef]

class GetAccessPointConfigurationForObjectLambdaResultTypeDef(TypedDict):
    Configuration: ObjectLambdaConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

ObjectLambdaConfigurationUnionTypeDef = Union[
    ObjectLambdaConfigurationTypeDef, ObjectLambdaConfigurationOutputTypeDef
]

class GetBucketLifecycleConfigurationResultTypeDef(TypedDict):
    Rules: List[LifecycleRuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

LifecycleRuleFilterUnionTypeDef = Union[
    LifecycleRuleFilterTypeDef, LifecycleRuleFilterOutputTypeDef
]

class JobManifestGeneratorOutputTypeDef(TypedDict):
    S3JobManifestGenerator: NotRequired[S3JobManifestGeneratorOutputTypeDef]

class JobManifestGeneratorTypeDef(TypedDict):
    S3JobManifestGenerator: NotRequired[S3JobManifestGeneratorTypeDef]

class GetStorageLensGroupResultTypeDef(TypedDict):
    StorageLensGroup: StorageLensGroupOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

StorageLensGroupUnionTypeDef = Union[StorageLensGroupTypeDef, StorageLensGroupOutputTypeDef]

class ReplicationConfigurationOutputTypeDef(TypedDict):
    Role: str
    Rules: List[ReplicationRuleOutputTypeDef]

class ReplicationConfigurationTypeDef(TypedDict):
    Role: str
    Rules: Sequence[ReplicationRuleTypeDef]

class DescribeMultiRegionAccessPointOperationResultTypeDef(TypedDict):
    AsyncOperation: AsyncOperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AccountLevelOutputTypeDef(TypedDict):
    BucketLevel: BucketLevelTypeDef
    ActivityMetrics: NotRequired[ActivityMetricsTypeDef]
    AdvancedCostOptimizationMetrics: NotRequired[AdvancedCostOptimizationMetricsTypeDef]
    AdvancedDataProtectionMetrics: NotRequired[AdvancedDataProtectionMetricsTypeDef]
    DetailedStatusCodesMetrics: NotRequired[DetailedStatusCodesMetricsTypeDef]
    StorageLensGroupLevel: NotRequired[StorageLensGroupLevelOutputTypeDef]

class AccountLevelTypeDef(TypedDict):
    BucketLevel: BucketLevelTypeDef
    ActivityMetrics: NotRequired[ActivityMetricsTypeDef]
    AdvancedCostOptimizationMetrics: NotRequired[AdvancedCostOptimizationMetricsTypeDef]
    AdvancedDataProtectionMetrics: NotRequired[AdvancedDataProtectionMetricsTypeDef]
    DetailedStatusCodesMetrics: NotRequired[DetailedStatusCodesMetricsTypeDef]
    StorageLensGroupLevel: NotRequired[StorageLensGroupLevelTypeDef]

class S3SetObjectAclOperationOutputTypeDef(TypedDict):
    AccessControlPolicy: NotRequired[S3AccessControlPolicyOutputTypeDef]

class S3SetObjectAclOperationTypeDef(TypedDict):
    AccessControlPolicy: NotRequired[S3AccessControlPolicyTypeDef]

class CreateAccessPointForObjectLambdaRequestTypeDef(TypedDict):
    AccountId: str
    Name: str
    Configuration: ObjectLambdaConfigurationUnionTypeDef

class PutAccessPointConfigurationForObjectLambdaRequestTypeDef(TypedDict):
    AccountId: str
    Name: str
    Configuration: ObjectLambdaConfigurationUnionTypeDef

class LifecycleRuleTypeDef(TypedDict):
    Status: ExpirationStatusType
    Expiration: NotRequired[LifecycleExpirationUnionTypeDef]
    ID: NotRequired[str]
    Filter: NotRequired[LifecycleRuleFilterUnionTypeDef]
    Transitions: NotRequired[Sequence[TransitionUnionTypeDef]]
    NoncurrentVersionTransitions: NotRequired[Sequence[NoncurrentVersionTransitionTypeDef]]
    NoncurrentVersionExpiration: NotRequired[NoncurrentVersionExpirationTypeDef]
    AbortIncompleteMultipartUpload: NotRequired[AbortIncompleteMultipartUploadTypeDef]

JobManifestGeneratorUnionTypeDef = Union[
    JobManifestGeneratorTypeDef, JobManifestGeneratorOutputTypeDef
]

class CreateStorageLensGroupRequestTypeDef(TypedDict):
    AccountId: str
    StorageLensGroup: StorageLensGroupUnionTypeDef
    Tags: NotRequired[Sequence[TagTypeDef]]

class UpdateStorageLensGroupRequestTypeDef(TypedDict):
    Name: str
    AccountId: str
    StorageLensGroup: StorageLensGroupUnionTypeDef

class GetBucketReplicationResultTypeDef(TypedDict):
    ReplicationConfiguration: ReplicationConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

ReplicationConfigurationUnionTypeDef = Union[
    ReplicationConfigurationTypeDef, ReplicationConfigurationOutputTypeDef
]

class StorageLensConfigurationOutputTypeDef(TypedDict):
    Id: str
    AccountLevel: AccountLevelOutputTypeDef
    IsEnabled: bool
    Include: NotRequired[IncludeOutputTypeDef]
    Exclude: NotRequired[ExcludeOutputTypeDef]
    DataExport: NotRequired[StorageLensDataExportOutputTypeDef]
    AwsOrg: NotRequired[StorageLensAwsOrgTypeDef]
    StorageLensArn: NotRequired[str]

class StorageLensConfigurationTypeDef(TypedDict):
    Id: str
    AccountLevel: AccountLevelTypeDef
    IsEnabled: bool
    Include: NotRequired[IncludeTypeDef]
    Exclude: NotRequired[ExcludeTypeDef]
    DataExport: NotRequired[StorageLensDataExportTypeDef]
    AwsOrg: NotRequired[StorageLensAwsOrgTypeDef]
    StorageLensArn: NotRequired[str]

class JobOperationOutputTypeDef(TypedDict):
    LambdaInvoke: NotRequired[LambdaInvokeOperationOutputTypeDef]
    S3PutObjectCopy: NotRequired[S3CopyObjectOperationOutputTypeDef]
    S3PutObjectAcl: NotRequired[S3SetObjectAclOperationOutputTypeDef]
    S3PutObjectTagging: NotRequired[S3SetObjectTaggingOperationOutputTypeDef]
    S3DeleteObjectTagging: NotRequired[Dict[str, Any]]
    S3InitiateRestoreObject: NotRequired[S3InitiateRestoreObjectOperationTypeDef]
    S3PutObjectLegalHold: NotRequired[S3SetObjectLegalHoldOperationTypeDef]
    S3PutObjectRetention: NotRequired[S3SetObjectRetentionOperationOutputTypeDef]
    S3ReplicateObject: NotRequired[Dict[str, Any]]

class JobOperationTypeDef(TypedDict):
    LambdaInvoke: NotRequired[LambdaInvokeOperationTypeDef]
    S3PutObjectCopy: NotRequired[S3CopyObjectOperationTypeDef]
    S3PutObjectAcl: NotRequired[S3SetObjectAclOperationTypeDef]
    S3PutObjectTagging: NotRequired[S3SetObjectTaggingOperationTypeDef]
    S3DeleteObjectTagging: NotRequired[Mapping[str, Any]]
    S3InitiateRestoreObject: NotRequired[S3InitiateRestoreObjectOperationTypeDef]
    S3PutObjectLegalHold: NotRequired[S3SetObjectLegalHoldOperationTypeDef]
    S3PutObjectRetention: NotRequired[S3SetObjectRetentionOperationTypeDef]
    S3ReplicateObject: NotRequired[Mapping[str, Any]]

LifecycleRuleUnionTypeDef = Union[LifecycleRuleTypeDef, LifecycleRuleOutputTypeDef]

class PutBucketReplicationRequestTypeDef(TypedDict):
    AccountId: str
    Bucket: str
    ReplicationConfiguration: ReplicationConfigurationUnionTypeDef

class GetStorageLensConfigurationResultTypeDef(TypedDict):
    StorageLensConfiguration: StorageLensConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

StorageLensConfigurationUnionTypeDef = Union[
    StorageLensConfigurationTypeDef, StorageLensConfigurationOutputTypeDef
]

class JobDescriptorTypeDef(TypedDict):
    JobId: NotRequired[str]
    ConfirmationRequired: NotRequired[bool]
    Description: NotRequired[str]
    JobArn: NotRequired[str]
    Status: NotRequired[JobStatusType]
    Manifest: NotRequired[JobManifestOutputTypeDef]
    Operation: NotRequired[JobOperationOutputTypeDef]
    Priority: NotRequired[int]
    ProgressSummary: NotRequired[JobProgressSummaryTypeDef]
    StatusUpdateReason: NotRequired[str]
    FailureReasons: NotRequired[List[JobFailureTypeDef]]
    Report: NotRequired[JobReportTypeDef]
    CreationTime: NotRequired[datetime]
    TerminationDate: NotRequired[datetime]
    RoleArn: NotRequired[str]
    SuspendedDate: NotRequired[datetime]
    SuspendedCause: NotRequired[str]
    ManifestGenerator: NotRequired[JobManifestGeneratorOutputTypeDef]
    GeneratedManifestDescriptor: NotRequired[S3GeneratedManifestDescriptorTypeDef]

JobOperationUnionTypeDef = Union[JobOperationTypeDef, JobOperationOutputTypeDef]

class LifecycleConfigurationTypeDef(TypedDict):
    Rules: NotRequired[Sequence[LifecycleRuleUnionTypeDef]]

class PutStorageLensConfigurationRequestTypeDef(TypedDict):
    ConfigId: str
    AccountId: str
    StorageLensConfiguration: StorageLensConfigurationUnionTypeDef
    Tags: NotRequired[Sequence[StorageLensTagTypeDef]]

class DescribeJobResultTypeDef(TypedDict):
    Job: JobDescriptorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobRequestTypeDef(TypedDict):
    AccountId: str
    Operation: JobOperationUnionTypeDef
    Report: JobReportTypeDef
    ClientRequestToken: str
    Priority: int
    RoleArn: str
    ConfirmationRequired: NotRequired[bool]
    Manifest: NotRequired[JobManifestUnionTypeDef]
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[S3TagTypeDef]]
    ManifestGenerator: NotRequired[JobManifestGeneratorUnionTypeDef]

class PutBucketLifecycleConfigurationRequestTypeDef(TypedDict):
    AccountId: str
    Bucket: str
    LifecycleConfiguration: NotRequired[LifecycleConfigurationTypeDef]
