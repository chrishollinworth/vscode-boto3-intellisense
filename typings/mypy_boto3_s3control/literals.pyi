"""
Type annotations for s3control service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/literals.html)

Usage::

    ```python
    from mypy_boto3_s3control.literals import AsyncOperationNameType

    data: AsyncOperationNameType = "CreateMultiRegionAccessPoint"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AsyncOperationNameType",
    "BucketCannedACLType",
    "BucketLocationConstraintType",
    "BucketVersioningStatusType",
    "DeleteMarkerReplicationStatusType",
    "ExistingObjectReplicationStatusType",
    "ExpirationStatusType",
    "FormatType",
    "GeneratedManifestFormatType",
    "GranteeTypeType",
    "JobManifestFieldNameType",
    "JobManifestFormatType",
    "JobReportFormatType",
    "JobReportScopeType",
    "JobStatusType",
    "ListAccessPointsForObjectLambdaPaginatorName",
    "MFADeleteStatusType",
    "MFADeleteType",
    "MetricsStatusType",
    "MultiRegionAccessPointStatusType",
    "NetworkOriginType",
    "ObjectLambdaAccessPointAliasStatusType",
    "ObjectLambdaAllowedFeatureType",
    "ObjectLambdaTransformationConfigurationActionType",
    "OperationNameType",
    "OutputSchemaVersionType",
    "OwnerOverrideType",
    "PermissionType",
    "PrivilegeType",
    "ReplicaModificationsStatusType",
    "ReplicationRuleStatusType",
    "ReplicationStatusType",
    "ReplicationStorageClassType",
    "ReplicationTimeStatusType",
    "RequestedJobStatusType",
    "S3CannedAccessControlListType",
    "S3ChecksumAlgorithmType",
    "S3GlacierJobTierType",
    "S3GranteeTypeIdentifierType",
    "S3MetadataDirectiveType",
    "S3ObjectLockLegalHoldStatusType",
    "S3ObjectLockModeType",
    "S3ObjectLockRetentionModeType",
    "S3PermissionType",
    "S3PrefixTypeType",
    "S3SSEAlgorithmType",
    "S3StorageClassType",
    "SseKmsEncryptedObjectsStatusType",
    "TransitionStorageClassType",
)

AsyncOperationNameType = Literal[
    "CreateMultiRegionAccessPoint",
    "DeleteMultiRegionAccessPoint",
    "PutMultiRegionAccessPointPolicy",
]
BucketCannedACLType = Literal["authenticated-read", "private", "public-read", "public-read-write"]
BucketLocationConstraintType = Literal[
    "EU",
    "ap-northeast-1",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "cn-north-1",
    "eu-central-1",
    "eu-west-1",
    "sa-east-1",
    "us-west-1",
    "us-west-2",
]
BucketVersioningStatusType = Literal["Enabled", "Suspended"]
DeleteMarkerReplicationStatusType = Literal["Disabled", "Enabled"]
ExistingObjectReplicationStatusType = Literal["Disabled", "Enabled"]
ExpirationStatusType = Literal["Disabled", "Enabled"]
FormatType = Literal["CSV", "Parquet"]
GeneratedManifestFormatType = Literal["S3InventoryReport_CSV_20211130"]
GranteeTypeType = Literal["DIRECTORY_GROUP", "DIRECTORY_USER", "IAM"]
JobManifestFieldNameType = Literal["Bucket", "Ignore", "Key", "VersionId"]
JobManifestFormatType = Literal["S3BatchOperations_CSV_20180820", "S3InventoryReport_CSV_20161130"]
JobReportFormatType = Literal["Report_CSV_20180820"]
JobReportScopeType = Literal["AllTasks", "FailedTasksOnly"]
JobStatusType = Literal[
    "Active",
    "Cancelled",
    "Cancelling",
    "Complete",
    "Completing",
    "Failed",
    "Failing",
    "New",
    "Paused",
    "Pausing",
    "Preparing",
    "Ready",
    "Suspended",
]
ListAccessPointsForObjectLambdaPaginatorName = Literal["list_access_points_for_object_lambda"]
MFADeleteStatusType = Literal["Disabled", "Enabled"]
MFADeleteType = Literal["Disabled", "Enabled"]
MetricsStatusType = Literal["Disabled", "Enabled"]
MultiRegionAccessPointStatusType = Literal[
    "CREATING",
    "DELETING",
    "INCONSISTENT_ACROSS_REGIONS",
    "PARTIALLY_CREATED",
    "PARTIALLY_DELETED",
    "READY",
]
NetworkOriginType = Literal["Internet", "VPC"]
ObjectLambdaAccessPointAliasStatusType = Literal["PROVISIONING", "READY"]
ObjectLambdaAllowedFeatureType = Literal[
    "GetObject-PartNumber", "GetObject-Range", "HeadObject-PartNumber", "HeadObject-Range"
]
ObjectLambdaTransformationConfigurationActionType = Literal[
    "GetObject", "HeadObject", "ListObjects", "ListObjectsV2"
]
OperationNameType = Literal[
    "LambdaInvoke",
    "S3DeleteObjectTagging",
    "S3InitiateRestoreObject",
    "S3PutObjectAcl",
    "S3PutObjectCopy",
    "S3PutObjectLegalHold",
    "S3PutObjectRetention",
    "S3PutObjectTagging",
    "S3ReplicateObject",
]
OutputSchemaVersionType = Literal["V_1"]
OwnerOverrideType = Literal["Destination"]
PermissionType = Literal["READ", "READWRITE", "WRITE"]
PrivilegeType = Literal["Default", "Minimal"]
ReplicaModificationsStatusType = Literal["Disabled", "Enabled"]
ReplicationRuleStatusType = Literal["Disabled", "Enabled"]
ReplicationStatusType = Literal["COMPLETED", "FAILED", "NONE", "REPLICA"]
ReplicationStorageClassType = Literal[
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
ReplicationTimeStatusType = Literal["Disabled", "Enabled"]
RequestedJobStatusType = Literal["Cancelled", "Ready"]
S3CannedAccessControlListType = Literal[
    "authenticated-read",
    "aws-exec-read",
    "bucket-owner-full-control",
    "bucket-owner-read",
    "private",
    "public-read",
    "public-read-write",
]
S3ChecksumAlgorithmType = Literal["CRC32", "CRC32C", "SHA1", "SHA256"]
S3GlacierJobTierType = Literal["BULK", "STANDARD"]
S3GranteeTypeIdentifierType = Literal["emailAddress", "id", "uri"]
S3MetadataDirectiveType = Literal["COPY", "REPLACE"]
S3ObjectLockLegalHoldStatusType = Literal["OFF", "ON"]
S3ObjectLockModeType = Literal["COMPLIANCE", "GOVERNANCE"]
S3ObjectLockRetentionModeType = Literal["COMPLIANCE", "GOVERNANCE"]
S3PermissionType = Literal["FULL_CONTROL", "READ", "READ_ACP", "WRITE", "WRITE_ACP"]
S3PrefixTypeType = Literal["Object"]
S3SSEAlgorithmType = Literal["AES256", "KMS"]
S3StorageClassType = Literal[
    "DEEP_ARCHIVE",
    "GLACIER",
    "GLACIER_IR",
    "INTELLIGENT_TIERING",
    "ONEZONE_IA",
    "STANDARD",
    "STANDARD_IA",
]
SseKmsEncryptedObjectsStatusType = Literal["Disabled", "Enabled"]
TransitionStorageClassType = Literal[
    "DEEP_ARCHIVE", "GLACIER", "INTELLIGENT_TIERING", "ONEZONE_IA", "STANDARD_IA"
]
