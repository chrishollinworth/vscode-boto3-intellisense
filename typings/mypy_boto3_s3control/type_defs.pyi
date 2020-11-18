"""
Main interface for s3control service type definitions.

Usage::

    ```python
    from mypy_boto3_s3control.type_defs import AbortIncompleteMultipartUploadTypeDef

    data: AbortIncompleteMultipartUploadTypeDef = {...}
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
    "AbortIncompleteMultipartUploadTypeDef",
    "AccessPointTypeDef",
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
    "LifecycleExpirationTypeDef",
    "LifecycleRuleAndOperatorTypeDef",
    "LifecycleRuleFilterTypeDef",
    "LifecycleRuleTypeDef",
    "NoncurrentVersionExpirationTypeDef",
    "NoncurrentVersionTransitionTypeDef",
    "PolicyStatusTypeDef",
    "PublicAccessBlockConfigurationTypeDef",
    "RegionalBucketTypeDef",
    "ResponseMetadata",
    "S3AccessControlListTypeDef",
    "S3AccessControlPolicyTypeDef",
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
    "TransitionTypeDef",
    "VpcConfigurationTypeDef",
    "CreateAccessPointResultTypeDef",
    "CreateBucketConfigurationTypeDef",
    "CreateBucketResultTypeDef",
    "CreateJobResultTypeDef",
    "DescribeJobResultTypeDef",
    "GetAccessPointPolicyResultTypeDef",
    "GetAccessPointPolicyStatusResultTypeDef",
    "GetAccessPointResultTypeDef",
    "GetBucketLifecycleConfigurationResultTypeDef",
    "GetBucketPolicyResultTypeDef",
    "GetBucketResultTypeDef",
    "GetBucketTaggingResultTypeDef",
    "GetJobTaggingResultTypeDef",
    "GetPublicAccessBlockOutputTypeDef",
    "LifecycleConfigurationTypeDef",
    "ListAccessPointsResultTypeDef",
    "ListJobsResultTypeDef",
    "ListRegionalBucketsResultTypeDef",
    "TaggingTypeDef",
    "UpdateJobPriorityResultTypeDef",
    "UpdateJobStatusResultTypeDef",
)

AbortIncompleteMultipartUploadTypeDef = TypedDict(
    "AbortIncompleteMultipartUploadTypeDef", {"DaysAfterInitiation": int}, total=False
)

_RequiredAccessPointTypeDef = TypedDict(
    "_RequiredAccessPointTypeDef",
    {"Name": str, "NetworkOrigin": Literal["Internet", "VPC"], "Bucket": str},
)
_OptionalAccessPointTypeDef = TypedDict(
    "_OptionalAccessPointTypeDef",
    {"VpcConfiguration": "VpcConfigurationTypeDef", "AccessPointArn": str},
    total=False,
)


class AccessPointTypeDef(_RequiredAccessPointTypeDef, _OptionalAccessPointTypeDef):
    pass


JobDescriptorTypeDef = TypedDict(
    "JobDescriptorTypeDef",
    {
        "JobId": str,
        "ConfirmationRequired": bool,
        "Description": str,
        "JobArn": str,
        "Status": Literal[
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
        ],
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
    "JobFailureTypeDef", {"FailureCode": str, "FailureReason": str}, total=False
)

JobListDescriptorTypeDef = TypedDict(
    "JobListDescriptorTypeDef",
    {
        "JobId": str,
        "Description": str,
        "Operation": Literal[
            "LambdaInvoke",
            "S3PutObjectCopy",
            "S3PutObjectAcl",
            "S3PutObjectTagging",
            "S3InitiateRestoreObject",
            "S3PutObjectLegalHold",
            "S3PutObjectRetention",
        ],
        "Priority": int,
        "Status": Literal[
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
        ],
        "CreationTime": datetime,
        "TerminationDate": datetime,
        "ProgressSummary": "JobProgressSummaryTypeDef",
    },
    total=False,
)

_RequiredJobManifestLocationTypeDef = TypedDict(
    "_RequiredJobManifestLocationTypeDef", {"ObjectArn": str, "ETag": str}
)
_OptionalJobManifestLocationTypeDef = TypedDict(
    "_OptionalJobManifestLocationTypeDef", {"ObjectVersionId": str}, total=False
)


class JobManifestLocationTypeDef(
    _RequiredJobManifestLocationTypeDef, _OptionalJobManifestLocationTypeDef
):
    pass


_RequiredJobManifestSpecTypeDef = TypedDict(
    "_RequiredJobManifestSpecTypeDef",
    {"Format": Literal["S3BatchOperations_CSV_20180820", "S3InventoryReport_CSV_20161130"]},
)
_OptionalJobManifestSpecTypeDef = TypedDict(
    "_OptionalJobManifestSpecTypeDef",
    {"Fields": List[Literal["Ignore", "Bucket", "Key", "VersionId"]]},
    total=False,
)


class JobManifestSpecTypeDef(_RequiredJobManifestSpecTypeDef, _OptionalJobManifestSpecTypeDef):
    pass


JobManifestTypeDef = TypedDict(
    "JobManifestTypeDef",
    {"Spec": "JobManifestSpecTypeDef", "Location": "JobManifestLocationTypeDef"},
)

JobOperationTypeDef = TypedDict(
    "JobOperationTypeDef",
    {
        "LambdaInvoke": "LambdaInvokeOperationTypeDef",
        "S3PutObjectCopy": "S3CopyObjectOperationTypeDef",
        "S3PutObjectAcl": "S3SetObjectAclOperationTypeDef",
        "S3PutObjectTagging": "S3SetObjectTaggingOperationTypeDef",
        "S3InitiateRestoreObject": "S3InitiateRestoreObjectOperationTypeDef",
        "S3PutObjectLegalHold": "S3SetObjectLegalHoldOperationTypeDef",
        "S3PutObjectRetention": "S3SetObjectRetentionOperationTypeDef",
    },
    total=False,
)

JobProgressSummaryTypeDef = TypedDict(
    "JobProgressSummaryTypeDef",
    {"TotalNumberOfTasks": int, "NumberOfTasksSucceeded": int, "NumberOfTasksFailed": int},
    total=False,
)

_RequiredJobReportTypeDef = TypedDict("_RequiredJobReportTypeDef", {"Enabled": bool})
_OptionalJobReportTypeDef = TypedDict(
    "_OptionalJobReportTypeDef",
    {
        "Bucket": str,
        "Format": Literal["Report_CSV_20180820"],
        "Prefix": str,
        "ReportScope": Literal["AllTasks", "FailedTasksOnly"],
    },
    total=False,
)


class JobReportTypeDef(_RequiredJobReportTypeDef, _OptionalJobReportTypeDef):
    pass


LambdaInvokeOperationTypeDef = TypedDict(
    "LambdaInvokeOperationTypeDef", {"FunctionArn": str}, total=False
)

LifecycleExpirationTypeDef = TypedDict(
    "LifecycleExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)

LifecycleRuleAndOperatorTypeDef = TypedDict(
    "LifecycleRuleAndOperatorTypeDef", {"Prefix": str, "Tags": List["S3TagTypeDef"]}, total=False
)

LifecycleRuleFilterTypeDef = TypedDict(
    "LifecycleRuleFilterTypeDef",
    {"Prefix": str, "Tag": "S3TagTypeDef", "And": "LifecycleRuleAndOperatorTypeDef"},
    total=False,
)

_RequiredLifecycleRuleTypeDef = TypedDict(
    "_RequiredLifecycleRuleTypeDef", {"Status": Literal["Enabled", "Disabled"]}
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


NoncurrentVersionExpirationTypeDef = TypedDict(
    "NoncurrentVersionExpirationTypeDef", {"NoncurrentDays": int}, total=False
)

NoncurrentVersionTransitionTypeDef = TypedDict(
    "NoncurrentVersionTransitionTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

PolicyStatusTypeDef = TypedDict("PolicyStatusTypeDef", {"IsPublic": bool}, total=False)

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

_RequiredRegionalBucketTypeDef = TypedDict(
    "_RequiredRegionalBucketTypeDef",
    {"Bucket": str, "PublicAccessBlockEnabled": bool, "CreationDate": datetime},
)
_OptionalRegionalBucketTypeDef = TypedDict(
    "_OptionalRegionalBucketTypeDef", {"BucketArn": str, "OutpostId": str}, total=False
)


class RegionalBucketTypeDef(_RequiredRegionalBucketTypeDef, _OptionalRegionalBucketTypeDef):
    pass


ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredS3AccessControlListTypeDef = TypedDict(
    "_RequiredS3AccessControlListTypeDef", {"Owner": "S3ObjectOwnerTypeDef"}
)
_OptionalS3AccessControlListTypeDef = TypedDict(
    "_OptionalS3AccessControlListTypeDef", {"Grants": List["S3GrantTypeDef"]}, total=False
)


class S3AccessControlListTypeDef(
    _RequiredS3AccessControlListTypeDef, _OptionalS3AccessControlListTypeDef
):
    pass


S3AccessControlPolicyTypeDef = TypedDict(
    "S3AccessControlPolicyTypeDef",
    {
        "AccessControlList": "S3AccessControlListTypeDef",
        "CannedAccessControlList": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
    },
    total=False,
)

S3CopyObjectOperationTypeDef = TypedDict(
    "S3CopyObjectOperationTypeDef",
    {
        "TargetResource": str,
        "CannedAccessControlList": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
        "AccessControlGrants": List["S3GrantTypeDef"],
        "MetadataDirective": Literal["COPY", "REPLACE"],
        "ModifiedSinceConstraint": datetime,
        "NewObjectMetadata": "S3ObjectMetadataTypeDef",
        "NewObjectTagging": List["S3TagTypeDef"],
        "RedirectLocation": str,
        "RequesterPays": bool,
        "StorageClass": Literal[
            "STANDARD",
            "STANDARD_IA",
            "ONEZONE_IA",
            "GLACIER",
            "INTELLIGENT_TIERING",
            "DEEP_ARCHIVE",
        ],
        "UnModifiedSinceConstraint": datetime,
        "SSEAwsKmsKeyId": str,
        "TargetKeyPrefix": str,
        "ObjectLockLegalHoldStatus": Literal["OFF", "ON"],
        "ObjectLockMode": Literal["COMPLIANCE", "GOVERNANCE"],
        "ObjectLockRetainUntilDate": datetime,
    },
    total=False,
)

S3GrantTypeDef = TypedDict(
    "S3GrantTypeDef",
    {
        "Grantee": "S3GranteeTypeDef",
        "Permission": Literal["FULL_CONTROL", "READ", "WRITE", "READ_ACP", "WRITE_ACP"],
    },
    total=False,
)

S3GranteeTypeDef = TypedDict(
    "S3GranteeTypeDef",
    {"TypeIdentifier": Literal["id", "emailAddress", "uri"], "Identifier": str, "DisplayName": str},
    total=False,
)

S3InitiateRestoreObjectOperationTypeDef = TypedDict(
    "S3InitiateRestoreObjectOperationTypeDef",
    {"ExpirationInDays": int, "GlacierJobTier": Literal["BULK", "STANDARD"]},
    total=False,
)

S3ObjectLockLegalHoldTypeDef = TypedDict(
    "S3ObjectLockLegalHoldTypeDef", {"Status": Literal["OFF", "ON"]}
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
        "HttpExpiresDate": datetime,
        "RequesterCharged": bool,
        "SSEAlgorithm": Literal["AES256", "KMS"],
    },
    total=False,
)

S3ObjectOwnerTypeDef = TypedDict(
    "S3ObjectOwnerTypeDef", {"ID": str, "DisplayName": str}, total=False
)

S3RetentionTypeDef = TypedDict(
    "S3RetentionTypeDef",
    {"RetainUntilDate": datetime, "Mode": Literal["COMPLIANCE", "GOVERNANCE"]},
    total=False,
)

S3SetObjectAclOperationTypeDef = TypedDict(
    "S3SetObjectAclOperationTypeDef",
    {"AccessControlPolicy": "S3AccessControlPolicyTypeDef"},
    total=False,
)

S3SetObjectLegalHoldOperationTypeDef = TypedDict(
    "S3SetObjectLegalHoldOperationTypeDef", {"LegalHold": "S3ObjectLockLegalHoldTypeDef"}
)

_RequiredS3SetObjectRetentionOperationTypeDef = TypedDict(
    "_RequiredS3SetObjectRetentionOperationTypeDef", {"Retention": "S3RetentionTypeDef"}
)
_OptionalS3SetObjectRetentionOperationTypeDef = TypedDict(
    "_OptionalS3SetObjectRetentionOperationTypeDef",
    {"BypassGovernanceRetention": bool},
    total=False,
)


class S3SetObjectRetentionOperationTypeDef(
    _RequiredS3SetObjectRetentionOperationTypeDef, _OptionalS3SetObjectRetentionOperationTypeDef
):
    pass


S3SetObjectTaggingOperationTypeDef = TypedDict(
    "S3SetObjectTaggingOperationTypeDef", {"TagSet": List["S3TagTypeDef"]}, total=False
)

S3TagTypeDef = TypedDict("S3TagTypeDef", {"Key": str, "Value": str})

TransitionTypeDef = TypedDict(
    "TransitionTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

VpcConfigurationTypeDef = TypedDict("VpcConfigurationTypeDef", {"VpcId": str})

CreateAccessPointResultTypeDef = TypedDict(
    "CreateAccessPointResultTypeDef", {"AccessPointArn": str}, total=False
)

CreateBucketConfigurationTypeDef = TypedDict(
    "CreateBucketConfigurationTypeDef",
    {
        "LocationConstraint": Literal[
            "EU",
            "eu-west-1",
            "us-west-1",
            "us-west-2",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "sa-east-1",
            "cn-north-1",
            "eu-central-1",
        ]
    },
    total=False,
)

CreateBucketResultTypeDef = TypedDict(
    "CreateBucketResultTypeDef", {"Location": str, "BucketArn": str}, total=False
)

CreateJobResultTypeDef = TypedDict("CreateJobResultTypeDef", {"JobId": str}, total=False)

DescribeJobResultTypeDef = TypedDict(
    "DescribeJobResultTypeDef", {"Job": "JobDescriptorTypeDef"}, total=False
)

GetAccessPointPolicyResultTypeDef = TypedDict(
    "GetAccessPointPolicyResultTypeDef", {"Policy": str}, total=False
)

GetAccessPointPolicyStatusResultTypeDef = TypedDict(
    "GetAccessPointPolicyStatusResultTypeDef", {"PolicyStatus": "PolicyStatusTypeDef"}, total=False
)

GetAccessPointResultTypeDef = TypedDict(
    "GetAccessPointResultTypeDef",
    {
        "Name": str,
        "Bucket": str,
        "NetworkOrigin": Literal["Internet", "VPC"],
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
        "CreationDate": datetime,
    },
    total=False,
)

GetBucketLifecycleConfigurationResultTypeDef = TypedDict(
    "GetBucketLifecycleConfigurationResultTypeDef",
    {"Rules": List["LifecycleRuleTypeDef"]},
    total=False,
)

GetBucketPolicyResultTypeDef = TypedDict(
    "GetBucketPolicyResultTypeDef", {"Policy": str}, total=False
)

GetBucketResultTypeDef = TypedDict(
    "GetBucketResultTypeDef",
    {"Bucket": str, "PublicAccessBlockEnabled": bool, "CreationDate": datetime},
    total=False,
)

GetBucketTaggingResultTypeDef = TypedDict(
    "GetBucketTaggingResultTypeDef", {"TagSet": List["S3TagTypeDef"]}
)

GetJobTaggingResultTypeDef = TypedDict(
    "GetJobTaggingResultTypeDef", {"Tags": List["S3TagTypeDef"]}, total=False
)

GetPublicAccessBlockOutputTypeDef = TypedDict(
    "GetPublicAccessBlockOutputTypeDef",
    {
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

LifecycleConfigurationTypeDef = TypedDict(
    "LifecycleConfigurationTypeDef", {"Rules": List["LifecycleRuleTypeDef"]}, total=False
)

ListAccessPointsResultTypeDef = TypedDict(
    "ListAccessPointsResultTypeDef",
    {"AccessPointList": List["AccessPointTypeDef"], "NextToken": str},
    total=False,
)

ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef",
    {"NextToken": str, "Jobs": List["JobListDescriptorTypeDef"]},
    total=False,
)

ListRegionalBucketsResultTypeDef = TypedDict(
    "ListRegionalBucketsResultTypeDef",
    {"RegionalBucketList": List["RegionalBucketTypeDef"], "NextToken": str},
    total=False,
)

TaggingTypeDef = TypedDict("TaggingTypeDef", {"TagSet": List["S3TagTypeDef"]})

UpdateJobPriorityResultTypeDef = TypedDict(
    "UpdateJobPriorityResultTypeDef", {"JobId": str, "Priority": int}
)

UpdateJobStatusResultTypeDef = TypedDict(
    "UpdateJobStatusResultTypeDef",
    {
        "JobId": str,
        "Status": Literal[
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
        ],
        "StatusUpdateReason": str,
    },
    total=False,
)
