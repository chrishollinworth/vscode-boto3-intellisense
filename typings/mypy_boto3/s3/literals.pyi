"""
Type annotations for s3 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/literals.html)

Usage::

    ```python
    from mypy_boto3_s3.literals import AnalyticsS3ExportFileFormatType

    data: AnalyticsS3ExportFileFormatType = "CSV"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AnalyticsS3ExportFileFormatType",
    "ArchiveStatusType",
    "BucketAccelerateStatusType",
    "BucketCannedACLType",
    "BucketExistsWaiterName",
    "BucketLocationConstraintType",
    "BucketLogsPermissionType",
    "BucketNotExistsWaiterName",
    "BucketTypeType",
    "BucketVersioningStatusType",
    "ChecksumAlgorithmType",
    "ChecksumModeType",
    "CompressionTypeType",
    "DataRedundancyType",
    "DeleteMarkerReplicationStatusType",
    "EncodingTypeType",
    "EventType",
    "ExistingObjectReplicationStatusType",
    "ExpirationStatusType",
    "ExpressionTypeType",
    "FileHeaderInfoType",
    "FilterRuleNameType",
    "IntelligentTieringAccessTierType",
    "IntelligentTieringStatusType",
    "InventoryFormatType",
    "InventoryFrequencyType",
    "InventoryIncludedObjectVersionsType",
    "InventoryOptionalFieldType",
    "JSONTypeType",
    "ListDirectoryBucketsPaginatorName",
    "ListMultipartUploadsPaginatorName",
    "ListObjectVersionsPaginatorName",
    "ListObjectsPaginatorName",
    "ListObjectsV2PaginatorName",
    "ListPartsPaginatorName",
    "LocationTypeType",
    "MFADeleteStatusType",
    "MFADeleteType",
    "MetadataDirectiveType",
    "MetricsStatusType",
    "ObjectAttributesType",
    "ObjectCannedACLType",
    "ObjectExistsWaiterName",
    "ObjectLockEnabledType",
    "ObjectLockLegalHoldStatusType",
    "ObjectLockModeType",
    "ObjectLockRetentionModeType",
    "ObjectNotExistsWaiterName",
    "ObjectOwnershipType",
    "ObjectStorageClassType",
    "ObjectVersionStorageClassType",
    "OptionalObjectAttributesType",
    "OwnerOverrideType",
    "PartitionDateSourceType",
    "PayerType",
    "PermissionType",
    "ProtocolType",
    "QuoteFieldsType",
    "ReplicaModificationsStatusType",
    "ReplicationRuleStatusType",
    "ReplicationStatusType",
    "ReplicationTimeStatusType",
    "RequestChargedType",
    "RequestPayerType",
    "RestoreRequestTypeType",
    "ServerSideEncryptionType",
    "SessionModeType",
    "SseKmsEncryptedObjectsStatusType",
    "StorageClassAnalysisSchemaVersionType",
    "StorageClassType",
    "TaggingDirectiveType",
    "TierType",
    "TransitionStorageClassType",
    "TypeType",
)

AnalyticsS3ExportFileFormatType = Literal["CSV"]
ArchiveStatusType = Literal["ARCHIVE_ACCESS", "DEEP_ARCHIVE_ACCESS"]
BucketAccelerateStatusType = Literal["Enabled", "Suspended"]
BucketCannedACLType = Literal["authenticated-read", "private", "public-read", "public-read-write"]
BucketExistsWaiterName = Literal["bucket_exists"]
BucketLocationConstraintType = Literal[
    "EU",
    "af-south-1",
    "ap-east-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-northeast-3",
    "ap-south-1",
    "ap-south-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-southeast-3",
    "ca-central-1",
    "cn-north-1",
    "cn-northwest-1",
    "eu-central-1",
    "eu-north-1",
    "eu-south-1",
    "eu-south-2",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "me-south-1",
    "sa-east-1",
    "us-east-2",
    "us-gov-east-1",
    "us-gov-west-1",
    "us-west-1",
    "us-west-2",
]
BucketLogsPermissionType = Literal["FULL_CONTROL", "READ", "WRITE"]
BucketNotExistsWaiterName = Literal["bucket_not_exists"]
BucketTypeType = Literal["Directory"]
BucketVersioningStatusType = Literal["Enabled", "Suspended"]
ChecksumAlgorithmType = Literal["CRC32", "CRC32C", "SHA1", "SHA256"]
ChecksumModeType = Literal["ENABLED"]
CompressionTypeType = Literal["BZIP2", "GZIP", "NONE"]
DataRedundancyType = Literal["SingleAvailabilityZone"]
DeleteMarkerReplicationStatusType = Literal["Disabled", "Enabled"]
EncodingTypeType = Literal["url"]
EventType = Literal[
    "s3:IntelligentTiering",
    "s3:LifecycleExpiration:*",
    "s3:LifecycleExpiration:Delete",
    "s3:LifecycleExpiration:DeleteMarkerCreated",
    "s3:LifecycleTransition",
    "s3:ObjectAcl:Put",
    "s3:ObjectCreated:*",
    "s3:ObjectCreated:CompleteMultipartUpload",
    "s3:ObjectCreated:Copy",
    "s3:ObjectCreated:Post",
    "s3:ObjectCreated:Put",
    "s3:ObjectRemoved:*",
    "s3:ObjectRemoved:Delete",
    "s3:ObjectRemoved:DeleteMarkerCreated",
    "s3:ObjectRestore:*",
    "s3:ObjectRestore:Completed",
    "s3:ObjectRestore:Delete",
    "s3:ObjectRestore:Post",
    "s3:ObjectTagging:*",
    "s3:ObjectTagging:Delete",
    "s3:ObjectTagging:Put",
    "s3:ReducedRedundancyLostObject",
    "s3:Replication:*",
    "s3:Replication:OperationFailedReplication",
    "s3:Replication:OperationMissedThreshold",
    "s3:Replication:OperationNotTracked",
    "s3:Replication:OperationReplicatedAfterThreshold",
]
ExistingObjectReplicationStatusType = Literal["Disabled", "Enabled"]
ExpirationStatusType = Literal["Disabled", "Enabled"]
ExpressionTypeType = Literal["SQL"]
FileHeaderInfoType = Literal["IGNORE", "NONE", "USE"]
FilterRuleNameType = Literal["prefix", "suffix"]
IntelligentTieringAccessTierType = Literal["ARCHIVE_ACCESS", "DEEP_ARCHIVE_ACCESS"]
IntelligentTieringStatusType = Literal["Disabled", "Enabled"]
InventoryFormatType = Literal["CSV", "ORC", "Parquet"]
InventoryFrequencyType = Literal["Daily", "Weekly"]
InventoryIncludedObjectVersionsType = Literal["All", "Current"]
InventoryOptionalFieldType = Literal[
    "BucketKeyStatus",
    "ChecksumAlgorithm",
    "ETag",
    "EncryptionStatus",
    "IntelligentTieringAccessTier",
    "IsMultipartUploaded",
    "LastModifiedDate",
    "ObjectAccessControlList",
    "ObjectLockLegalHoldStatus",
    "ObjectLockMode",
    "ObjectLockRetainUntilDate",
    "ObjectOwner",
    "ReplicationStatus",
    "Size",
    "StorageClass",
]
JSONTypeType = Literal["DOCUMENT", "LINES"]
ListDirectoryBucketsPaginatorName = Literal["list_directory_buckets"]
ListMultipartUploadsPaginatorName = Literal["list_multipart_uploads"]
ListObjectVersionsPaginatorName = Literal["list_object_versions"]
ListObjectsPaginatorName = Literal["list_objects"]
ListObjectsV2PaginatorName = Literal["list_objects_v2"]
ListPartsPaginatorName = Literal["list_parts"]
LocationTypeType = Literal["AvailabilityZone"]
MFADeleteStatusType = Literal["Disabled", "Enabled"]
MFADeleteType = Literal["Disabled", "Enabled"]
MetadataDirectiveType = Literal["COPY", "REPLACE"]
MetricsStatusType = Literal["Disabled", "Enabled"]
ObjectAttributesType = Literal["Checksum", "ETag", "ObjectParts", "ObjectSize", "StorageClass"]
ObjectCannedACLType = Literal[
    "authenticated-read",
    "aws-exec-read",
    "bucket-owner-full-control",
    "bucket-owner-read",
    "private",
    "public-read",
    "public-read-write",
]
ObjectExistsWaiterName = Literal["object_exists"]
ObjectLockEnabledType = Literal["Enabled"]
ObjectLockLegalHoldStatusType = Literal["OFF", "ON"]
ObjectLockModeType = Literal["COMPLIANCE", "GOVERNANCE"]
ObjectLockRetentionModeType = Literal["COMPLIANCE", "GOVERNANCE"]
ObjectNotExistsWaiterName = Literal["object_not_exists"]
ObjectOwnershipType = Literal["BucketOwnerEnforced", "BucketOwnerPreferred", "ObjectWriter"]
ObjectStorageClassType = Literal[
    "DEEP_ARCHIVE",
    "EXPRESS_ONEZONE",
    "GLACIER",
    "GLACIER_IR",
    "INTELLIGENT_TIERING",
    "ONEZONE_IA",
    "OUTPOSTS",
    "REDUCED_REDUNDANCY",
    "SNOW",
    "STANDARD",
    "STANDARD_IA",
]
ObjectVersionStorageClassType = Literal["STANDARD"]
OptionalObjectAttributesType = Literal["RestoreStatus"]
OwnerOverrideType = Literal["Destination"]
PartitionDateSourceType = Literal["DeliveryTime", "EventTime"]
PayerType = Literal["BucketOwner", "Requester"]
PermissionType = Literal["FULL_CONTROL", "READ", "READ_ACP", "WRITE", "WRITE_ACP"]
ProtocolType = Literal["http", "https"]
QuoteFieldsType = Literal["ALWAYS", "ASNEEDED"]
ReplicaModificationsStatusType = Literal["Disabled", "Enabled"]
ReplicationRuleStatusType = Literal["Disabled", "Enabled"]
ReplicationStatusType = Literal["COMPLETE", "COMPLETED", "FAILED", "PENDING", "REPLICA"]
ReplicationTimeStatusType = Literal["Disabled", "Enabled"]
RequestChargedType = Literal["requester"]
RequestPayerType = Literal["requester"]
RestoreRequestTypeType = Literal["SELECT"]
ServerSideEncryptionType = Literal["AES256", "aws:kms", "aws:kms:dsse"]
SessionModeType = Literal["ReadOnly", "ReadWrite"]
SseKmsEncryptedObjectsStatusType = Literal["Disabled", "Enabled"]
StorageClassAnalysisSchemaVersionType = Literal["V_1"]
StorageClassType = Literal[
    "DEEP_ARCHIVE",
    "EXPRESS_ONEZONE",
    "GLACIER",
    "GLACIER_IR",
    "INTELLIGENT_TIERING",
    "ONEZONE_IA",
    "OUTPOSTS",
    "REDUCED_REDUNDANCY",
    "SNOW",
    "STANDARD",
    "STANDARD_IA",
]
TaggingDirectiveType = Literal["COPY", "REPLACE"]
TierType = Literal["Bulk", "Expedited", "Standard"]
TransitionStorageClassType = Literal[
    "DEEP_ARCHIVE", "GLACIER", "GLACIER_IR", "INTELLIGENT_TIERING", "ONEZONE_IA", "STANDARD_IA"
]
TypeType = Literal["AmazonCustomerByEmail", "CanonicalUser", "Group"]
