"""
Type annotations for s3control service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/literals.html)

Usage::

    ```python
    from mypy_boto3_s3control.literals import BucketCannedACLType

    data: BucketCannedACLType = "authenticated-read"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "BucketCannedACLType",
    "BucketLocationConstraintType",
    "ExpirationStatusType",
    "FormatType",
    "JobManifestFieldNameType",
    "JobManifestFormatType",
    "JobReportFormatType",
    "JobReportScopeType",
    "JobStatusType",
    "ListAccessPointsForObjectLambdaPaginatorName",
    "NetworkOriginType",
    "ObjectLambdaAllowedFeatureType",
    "ObjectLambdaTransformationConfigurationActionType",
    "OperationNameType",
    "OutputSchemaVersionType",
    "RequestedJobStatusType",
    "S3CannedAccessControlListType",
    "S3GlacierJobTierType",
    "S3GranteeTypeIdentifierType",
    "S3MetadataDirectiveType",
    "S3ObjectLockLegalHoldStatusType",
    "S3ObjectLockModeType",
    "S3ObjectLockRetentionModeType",
    "S3PermissionType",
    "S3SSEAlgorithmType",
    "S3StorageClassType",
    "TransitionStorageClassType",
)

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
ExpirationStatusType = Literal["Disabled", "Enabled"]
FormatType = Literal["CSV", "Parquet"]
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
NetworkOriginType = Literal["Internet", "VPC"]
ObjectLambdaAllowedFeatureType = Literal["GetObject-PartNumber", "GetObject-Range"]
ObjectLambdaTransformationConfigurationActionType = Literal["GetObject"]
OperationNameType = Literal[
    "LambdaInvoke",
    "S3DeleteObjectTagging",
    "S3InitiateRestoreObject",
    "S3PutObjectAcl",
    "S3PutObjectCopy",
    "S3PutObjectLegalHold",
    "S3PutObjectRetention",
    "S3PutObjectTagging",
]
OutputSchemaVersionType = Literal["V_1"]
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
S3GlacierJobTierType = Literal["BULK", "STANDARD"]
S3GranteeTypeIdentifierType = Literal["emailAddress", "id", "uri"]
S3MetadataDirectiveType = Literal["COPY", "REPLACE"]
S3ObjectLockLegalHoldStatusType = Literal["OFF", "ON"]
S3ObjectLockModeType = Literal["COMPLIANCE", "GOVERNANCE"]
S3ObjectLockRetentionModeType = Literal["COMPLIANCE", "GOVERNANCE"]
S3PermissionType = Literal["FULL_CONTROL", "READ", "READ_ACP", "WRITE", "WRITE_ACP"]
S3SSEAlgorithmType = Literal["AES256", "KMS"]
S3StorageClassType = Literal[
    "DEEP_ARCHIVE", "GLACIER", "INTELLIGENT_TIERING", "ONEZONE_IA", "STANDARD", "STANDARD_IA"
]
TransitionStorageClassType = Literal[
    "DEEP_ARCHIVE", "GLACIER", "INTELLIGENT_TIERING", "ONEZONE_IA", "STANDARD_IA"
]
