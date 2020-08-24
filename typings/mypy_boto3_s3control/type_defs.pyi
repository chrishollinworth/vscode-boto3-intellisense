"""
Main interface for s3control service type definitions.

Usage::

    ```python
    from mypy_boto3_s3control.type_defs import AccessPointTypeDef

    data: AccessPointTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
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
    "PolicyStatusTypeDef",
    "PublicAccessBlockConfigurationTypeDef",
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
    "VpcConfigurationTypeDef",
    "CreateJobResultTypeDef",
    "DescribeJobResultTypeDef",
    "GetAccessPointPolicyResultTypeDef",
    "GetAccessPointPolicyStatusResultTypeDef",
    "GetAccessPointResultTypeDef",
    "GetJobTaggingResultTypeDef",
    "GetPublicAccessBlockOutputTypeDef",
    "ListAccessPointsResultTypeDef",
    "ListJobsResultTypeDef",
    "UpdateJobPriorityResultTypeDef",
    "UpdateJobStatusResultTypeDef",
)

_RequiredAccessPointTypeDef = TypedDict(
    "_RequiredAccessPointTypeDef",
    {"Name": str, "NetworkOrigin": Literal["Internet", "VPC"], "Bucket": str},
)
_OptionalAccessPointTypeDef = TypedDict(
    "_OptionalAccessPointTypeDef", {"VpcConfiguration": "VpcConfigurationTypeDef"}, total=False
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

VpcConfigurationTypeDef = TypedDict("VpcConfigurationTypeDef", {"VpcId": str})

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

GetJobTaggingResultTypeDef = TypedDict(
    "GetJobTaggingResultTypeDef", {"Tags": List["S3TagTypeDef"]}, total=False
)

GetPublicAccessBlockOutputTypeDef = TypedDict(
    "GetPublicAccessBlockOutputTypeDef",
    {"PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef"},
    total=False,
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
