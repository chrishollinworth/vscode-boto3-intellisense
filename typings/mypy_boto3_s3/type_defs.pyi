"""
Type annotations for s3 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/type_defs.html)

Usage::

    ```python
    from mypy_boto3_s3.type_defs import AbortIncompleteMultipartUploadTypeDef

    data: AbortIncompleteMultipartUploadTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Callable, Dict, List, Union

from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient
from botocore.response import StreamingBody

from .literals import (
    ArchiveStatusType,
    BucketAccelerateStatusType,
    BucketCannedACLType,
    BucketLocationConstraintType,
    BucketLogsPermissionType,
    BucketVersioningStatusType,
    CompressionTypeType,
    DeleteMarkerReplicationStatusType,
    EventType,
    ExistingObjectReplicationStatusType,
    ExpirationStatusType,
    FileHeaderInfoType,
    FilterRuleNameType,
    IntelligentTieringAccessTierType,
    IntelligentTieringStatusType,
    InventoryFormatType,
    InventoryFrequencyType,
    InventoryIncludedObjectVersionsType,
    InventoryOptionalFieldType,
    JSONTypeType,
    MetadataDirectiveType,
    MetricsStatusType,
    MFADeleteStatusType,
    MFADeleteType,
    ObjectCannedACLType,
    ObjectLockLegalHoldStatusType,
    ObjectLockModeType,
    ObjectLockRetentionModeType,
    ObjectOwnershipType,
    ObjectStorageClassType,
    PayerType,
    PermissionType,
    ProtocolType,
    QuoteFieldsType,
    ReplicaModificationsStatusType,
    ReplicationRuleStatusType,
    ReplicationStatusType,
    ReplicationTimeStatusType,
    ServerSideEncryptionType,
    SseKmsEncryptedObjectsStatusType,
    StorageClassType,
    TaggingDirectiveType,
    TierType,
    TransitionStorageClassType,
    TypeType,
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
    "AbortMultipartUploadOutputTypeDef",
    "AbortMultipartUploadRequestMultipartUploadTypeDef",
    "AbortMultipartUploadRequestRequestTypeDef",
    "AccelerateConfigurationTypeDef",
    "AccessControlPolicyTypeDef",
    "AccessControlTranslationTypeDef",
    "AnalyticsAndOperatorTypeDef",
    "AnalyticsConfigurationTypeDef",
    "AnalyticsExportDestinationTypeDef",
    "AnalyticsFilterTypeDef",
    "AnalyticsS3BucketDestinationTypeDef",
    "BucketCopyRequestTypeDef",
    "BucketDownloadFileRequestTypeDef",
    "BucketDownloadFileobjRequestTypeDef",
    "BucketLifecycleConfigurationTypeDef",
    "BucketLoggingStatusTypeDef",
    "BucketObjectRequestTypeDef",
    "BucketTypeDef",
    "BucketUploadFileRequestTypeDef",
    "BucketUploadFileobjRequestTypeDef",
    "CORSConfigurationTypeDef",
    "CORSRuleTypeDef",
    "CSVInputTypeDef",
    "CSVOutputTypeDef",
    "ClientCopyRequestTypeDef",
    "ClientDownloadFileRequestTypeDef",
    "ClientDownloadFileobjRequestTypeDef",
    "ClientGeneratePresignedPostRequestTypeDef",
    "ClientUploadFileRequestTypeDef",
    "ClientUploadFileobjRequestTypeDef",
    "CloudFunctionConfigurationTypeDef",
    "CommonPrefixTypeDef",
    "CompleteMultipartUploadOutputTypeDef",
    "CompleteMultipartUploadRequestMultipartUploadTypeDef",
    "CompleteMultipartUploadRequestRequestTypeDef",
    "CompletedMultipartUploadTypeDef",
    "CompletedPartTypeDef",
    "ConditionTypeDef",
    "CopyObjectOutputTypeDef",
    "CopyObjectRequestObjectSummaryTypeDef",
    "CopyObjectRequestObjectTypeDef",
    "CopyObjectRequestRequestTypeDef",
    "CopyObjectResultTypeDef",
    "CopyPartResultTypeDef",
    "CopySourceTypeDef",
    "CreateBucketConfigurationTypeDef",
    "CreateBucketOutputTypeDef",
    "CreateBucketRequestBucketTypeDef",
    "CreateBucketRequestRequestTypeDef",
    "CreateBucketRequestServiceResourceTypeDef",
    "CreateMultipartUploadOutputTypeDef",
    "CreateMultipartUploadRequestObjectSummaryTypeDef",
    "CreateMultipartUploadRequestObjectTypeDef",
    "CreateMultipartUploadRequestRequestTypeDef",
    "DefaultRetentionTypeDef",
    "DeleteBucketAnalyticsConfigurationRequestRequestTypeDef",
    "DeleteBucketCorsRequestBucketCorsTypeDef",
    "DeleteBucketCorsRequestRequestTypeDef",
    "DeleteBucketEncryptionRequestRequestTypeDef",
    "DeleteBucketIntelligentTieringConfigurationRequestRequestTypeDef",
    "DeleteBucketInventoryConfigurationRequestRequestTypeDef",
    "DeleteBucketLifecycleRequestBucketLifecycleConfigurationTypeDef",
    "DeleteBucketLifecycleRequestBucketLifecycleTypeDef",
    "DeleteBucketLifecycleRequestRequestTypeDef",
    "DeleteBucketMetricsConfigurationRequestRequestTypeDef",
    "DeleteBucketOwnershipControlsRequestRequestTypeDef",
    "DeleteBucketPolicyRequestBucketPolicyTypeDef",
    "DeleteBucketPolicyRequestRequestTypeDef",
    "DeleteBucketReplicationRequestRequestTypeDef",
    "DeleteBucketRequestBucketTypeDef",
    "DeleteBucketRequestRequestTypeDef",
    "DeleteBucketTaggingRequestBucketTaggingTypeDef",
    "DeleteBucketTaggingRequestRequestTypeDef",
    "DeleteBucketWebsiteRequestBucketWebsiteTypeDef",
    "DeleteBucketWebsiteRequestRequestTypeDef",
    "DeleteMarkerEntryTypeDef",
    "DeleteMarkerReplicationTypeDef",
    "DeleteObjectOutputTypeDef",
    "DeleteObjectRequestObjectSummaryTypeDef",
    "DeleteObjectRequestObjectTypeDef",
    "DeleteObjectRequestObjectVersionTypeDef",
    "DeleteObjectRequestRequestTypeDef",
    "DeleteObjectTaggingOutputTypeDef",
    "DeleteObjectTaggingRequestRequestTypeDef",
    "DeleteObjectsOutputTypeDef",
    "DeleteObjectsRequestBucketTypeDef",
    "DeleteObjectsRequestRequestTypeDef",
    "DeletePublicAccessBlockRequestRequestTypeDef",
    "DeleteTypeDef",
    "DeletedObjectTypeDef",
    "DestinationTypeDef",
    "EncryptionConfigurationTypeDef",
    "EncryptionTypeDef",
    "ErrorDocumentTypeDef",
    "ErrorTypeDef",
    "ExistingObjectReplicationTypeDef",
    "FilterRuleTypeDef",
    "GetBucketAccelerateConfigurationOutputTypeDef",
    "GetBucketAccelerateConfigurationRequestRequestTypeDef",
    "GetBucketAclOutputTypeDef",
    "GetBucketAclRequestRequestTypeDef",
    "GetBucketAnalyticsConfigurationOutputTypeDef",
    "GetBucketAnalyticsConfigurationRequestRequestTypeDef",
    "GetBucketCorsOutputTypeDef",
    "GetBucketCorsRequestRequestTypeDef",
    "GetBucketEncryptionOutputTypeDef",
    "GetBucketEncryptionRequestRequestTypeDef",
    "GetBucketIntelligentTieringConfigurationOutputTypeDef",
    "GetBucketIntelligentTieringConfigurationRequestRequestTypeDef",
    "GetBucketInventoryConfigurationOutputTypeDef",
    "GetBucketInventoryConfigurationRequestRequestTypeDef",
    "GetBucketLifecycleConfigurationOutputTypeDef",
    "GetBucketLifecycleConfigurationRequestRequestTypeDef",
    "GetBucketLifecycleOutputTypeDef",
    "GetBucketLifecycleRequestRequestTypeDef",
    "GetBucketLocationOutputTypeDef",
    "GetBucketLocationRequestRequestTypeDef",
    "GetBucketLoggingOutputTypeDef",
    "GetBucketLoggingRequestRequestTypeDef",
    "GetBucketMetricsConfigurationOutputTypeDef",
    "GetBucketMetricsConfigurationRequestRequestTypeDef",
    "GetBucketNotificationConfigurationRequestRequestTypeDef",
    "GetBucketOwnershipControlsOutputTypeDef",
    "GetBucketOwnershipControlsRequestRequestTypeDef",
    "GetBucketPolicyOutputTypeDef",
    "GetBucketPolicyRequestRequestTypeDef",
    "GetBucketPolicyStatusOutputTypeDef",
    "GetBucketPolicyStatusRequestRequestTypeDef",
    "GetBucketReplicationOutputTypeDef",
    "GetBucketReplicationRequestRequestTypeDef",
    "GetBucketRequestPaymentOutputTypeDef",
    "GetBucketRequestPaymentRequestRequestTypeDef",
    "GetBucketTaggingOutputTypeDef",
    "GetBucketTaggingRequestRequestTypeDef",
    "GetBucketVersioningOutputTypeDef",
    "GetBucketVersioningRequestRequestTypeDef",
    "GetBucketWebsiteOutputTypeDef",
    "GetBucketWebsiteRequestRequestTypeDef",
    "GetObjectAclOutputTypeDef",
    "GetObjectAclRequestRequestTypeDef",
    "GetObjectLegalHoldOutputTypeDef",
    "GetObjectLegalHoldRequestRequestTypeDef",
    "GetObjectLockConfigurationOutputTypeDef",
    "GetObjectLockConfigurationRequestRequestTypeDef",
    "GetObjectOutputTypeDef",
    "GetObjectRequestObjectSummaryTypeDef",
    "GetObjectRequestObjectTypeDef",
    "GetObjectRequestObjectVersionTypeDef",
    "GetObjectRequestRequestTypeDef",
    "GetObjectRetentionOutputTypeDef",
    "GetObjectRetentionRequestRequestTypeDef",
    "GetObjectTaggingOutputTypeDef",
    "GetObjectTaggingRequestRequestTypeDef",
    "GetObjectTorrentOutputTypeDef",
    "GetObjectTorrentRequestRequestTypeDef",
    "GetPublicAccessBlockOutputTypeDef",
    "GetPublicAccessBlockRequestRequestTypeDef",
    "GlacierJobParametersTypeDef",
    "GrantTypeDef",
    "GranteeTypeDef",
    "HeadBucketRequestRequestTypeDef",
    "HeadObjectOutputTypeDef",
    "HeadObjectRequestObjectVersionTypeDef",
    "HeadObjectRequestRequestTypeDef",
    "IndexDocumentTypeDef",
    "InitiatorTypeDef",
    "InputSerializationTypeDef",
    "IntelligentTieringAndOperatorTypeDef",
    "IntelligentTieringConfigurationTypeDef",
    "IntelligentTieringFilterTypeDef",
    "InventoryConfigurationTypeDef",
    "InventoryDestinationTypeDef",
    "InventoryEncryptionTypeDef",
    "InventoryFilterTypeDef",
    "InventoryS3BucketDestinationTypeDef",
    "InventoryScheduleTypeDef",
    "JSONInputTypeDef",
    "JSONOutputTypeDef",
    "LambdaFunctionConfigurationTypeDef",
    "LifecycleConfigurationTypeDef",
    "LifecycleExpirationTypeDef",
    "LifecycleRuleAndOperatorTypeDef",
    "LifecycleRuleFilterTypeDef",
    "LifecycleRuleTypeDef",
    "ListBucketAnalyticsConfigurationsOutputTypeDef",
    "ListBucketAnalyticsConfigurationsRequestRequestTypeDef",
    "ListBucketIntelligentTieringConfigurationsOutputTypeDef",
    "ListBucketIntelligentTieringConfigurationsRequestRequestTypeDef",
    "ListBucketInventoryConfigurationsOutputTypeDef",
    "ListBucketInventoryConfigurationsRequestRequestTypeDef",
    "ListBucketMetricsConfigurationsOutputTypeDef",
    "ListBucketMetricsConfigurationsRequestRequestTypeDef",
    "ListBucketsOutputTypeDef",
    "ListMultipartUploadsOutputTypeDef",
    "ListMultipartUploadsRequestRequestTypeDef",
    "ListObjectVersionsOutputTypeDef",
    "ListObjectVersionsRequestRequestTypeDef",
    "ListObjectsOutputTypeDef",
    "ListObjectsRequestRequestTypeDef",
    "ListObjectsV2OutputTypeDef",
    "ListObjectsV2RequestRequestTypeDef",
    "ListPartsOutputTypeDef",
    "ListPartsRequestRequestTypeDef",
    "LoggingEnabledTypeDef",
    "MetadataEntryTypeDef",
    "MetricsAndOperatorTypeDef",
    "MetricsConfigurationTypeDef",
    "MetricsFilterTypeDef",
    "MetricsTypeDef",
    "MultipartUploadPartRequestTypeDef",
    "MultipartUploadTypeDef",
    "NoncurrentVersionExpirationTypeDef",
    "NoncurrentVersionTransitionTypeDef",
    "NotificationConfigurationDeprecatedResponseMetadataTypeDef",
    "NotificationConfigurationDeprecatedTypeDef",
    "NotificationConfigurationFilterTypeDef",
    "NotificationConfigurationResponseMetadataTypeDef",
    "NotificationConfigurationTypeDef",
    "ObjectCopyRequestTypeDef",
    "ObjectDownloadFileRequestTypeDef",
    "ObjectDownloadFileobjRequestTypeDef",
    "ObjectIdentifierTypeDef",
    "ObjectLockConfigurationTypeDef",
    "ObjectLockLegalHoldTypeDef",
    "ObjectLockRetentionTypeDef",
    "ObjectLockRuleTypeDef",
    "ObjectMultipartUploadRequestTypeDef",
    "ObjectSummaryMultipartUploadRequestTypeDef",
    "ObjectSummaryVersionRequestTypeDef",
    "ObjectTypeDef",
    "ObjectUploadFileRequestTypeDef",
    "ObjectUploadFileobjRequestTypeDef",
    "ObjectVersionRequestTypeDef",
    "ObjectVersionTypeDef",
    "OutputLocationTypeDef",
    "OutputSerializationTypeDef",
    "OwnerTypeDef",
    "OwnershipControlsRuleTypeDef",
    "OwnershipControlsTypeDef",
    "PaginatorConfigTypeDef",
    "PartTypeDef",
    "PolicyStatusTypeDef",
    "ProgressEventTypeDef",
    "ProgressTypeDef",
    "PublicAccessBlockConfigurationTypeDef",
    "PutBucketAccelerateConfigurationRequestRequestTypeDef",
    "PutBucketAclRequestBucketAclTypeDef",
    "PutBucketAclRequestRequestTypeDef",
    "PutBucketAnalyticsConfigurationRequestRequestTypeDef",
    "PutBucketCorsRequestBucketCorsTypeDef",
    "PutBucketCorsRequestRequestTypeDef",
    "PutBucketEncryptionRequestRequestTypeDef",
    "PutBucketIntelligentTieringConfigurationRequestRequestTypeDef",
    "PutBucketInventoryConfigurationRequestRequestTypeDef",
    "PutBucketLifecycleConfigurationRequestBucketLifecycleConfigurationTypeDef",
    "PutBucketLifecycleConfigurationRequestRequestTypeDef",
    "PutBucketLifecycleRequestBucketLifecycleTypeDef",
    "PutBucketLifecycleRequestRequestTypeDef",
    "PutBucketLoggingRequestBucketLoggingTypeDef",
    "PutBucketLoggingRequestRequestTypeDef",
    "PutBucketMetricsConfigurationRequestRequestTypeDef",
    "PutBucketNotificationConfigurationRequestBucketNotificationTypeDef",
    "PutBucketNotificationConfigurationRequestRequestTypeDef",
    "PutBucketNotificationRequestRequestTypeDef",
    "PutBucketOwnershipControlsRequestRequestTypeDef",
    "PutBucketPolicyRequestBucketPolicyTypeDef",
    "PutBucketPolicyRequestRequestTypeDef",
    "PutBucketReplicationRequestRequestTypeDef",
    "PutBucketRequestPaymentRequestBucketRequestPaymentTypeDef",
    "PutBucketRequestPaymentRequestRequestTypeDef",
    "PutBucketTaggingRequestBucketTaggingTypeDef",
    "PutBucketTaggingRequestRequestTypeDef",
    "PutBucketVersioningRequestBucketVersioningTypeDef",
    "PutBucketVersioningRequestRequestTypeDef",
    "PutBucketWebsiteRequestBucketWebsiteTypeDef",
    "PutBucketWebsiteRequestRequestTypeDef",
    "PutObjectAclOutputTypeDef",
    "PutObjectAclRequestObjectAclTypeDef",
    "PutObjectAclRequestRequestTypeDef",
    "PutObjectLegalHoldOutputTypeDef",
    "PutObjectLegalHoldRequestRequestTypeDef",
    "PutObjectLockConfigurationOutputTypeDef",
    "PutObjectLockConfigurationRequestRequestTypeDef",
    "PutObjectOutputTypeDef",
    "PutObjectRequestBucketTypeDef",
    "PutObjectRequestObjectSummaryTypeDef",
    "PutObjectRequestObjectTypeDef",
    "PutObjectRequestRequestTypeDef",
    "PutObjectRetentionOutputTypeDef",
    "PutObjectRetentionRequestRequestTypeDef",
    "PutObjectTaggingOutputTypeDef",
    "PutObjectTaggingRequestRequestTypeDef",
    "PutPublicAccessBlockRequestRequestTypeDef",
    "QueueConfigurationDeprecatedTypeDef",
    "QueueConfigurationTypeDef",
    "RecordsEventTypeDef",
    "RedirectAllRequestsToTypeDef",
    "RedirectTypeDef",
    "ReplicaModificationsTypeDef",
    "ReplicationConfigurationTypeDef",
    "ReplicationRuleAndOperatorTypeDef",
    "ReplicationRuleFilterTypeDef",
    "ReplicationRuleTypeDef",
    "ReplicationTimeTypeDef",
    "ReplicationTimeValueTypeDef",
    "RequestPaymentConfigurationTypeDef",
    "RequestProgressTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreObjectOutputTypeDef",
    "RestoreObjectRequestObjectSummaryTypeDef",
    "RestoreObjectRequestObjectTypeDef",
    "RestoreObjectRequestRequestTypeDef",
    "RestoreRequestTypeDef",
    "RoutingRuleTypeDef",
    "RuleTypeDef",
    "S3KeyFilterTypeDef",
    "S3LocationTypeDef",
    "SSEKMSTypeDef",
    "ScanRangeTypeDef",
    "SelectObjectContentEventStreamTypeDef",
    "SelectObjectContentOutputTypeDef",
    "SelectObjectContentRequestRequestTypeDef",
    "SelectParametersTypeDef",
    "ServerSideEncryptionByDefaultTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "ServerSideEncryptionRuleTypeDef",
    "ServiceResourceBucketAclRequestTypeDef",
    "ServiceResourceBucketCorsRequestTypeDef",
    "ServiceResourceBucketLifecycleConfigurationRequestTypeDef",
    "ServiceResourceBucketLifecycleRequestTypeDef",
    "ServiceResourceBucketLoggingRequestTypeDef",
    "ServiceResourceBucketNotificationRequestTypeDef",
    "ServiceResourceBucketPolicyRequestTypeDef",
    "ServiceResourceBucketRequestPaymentRequestTypeDef",
    "ServiceResourceBucketRequestTypeDef",
    "ServiceResourceBucketTaggingRequestTypeDef",
    "ServiceResourceBucketVersioningRequestTypeDef",
    "ServiceResourceBucketWebsiteRequestTypeDef",
    "ServiceResourceMultipartUploadPartRequestTypeDef",
    "ServiceResourceMultipartUploadRequestTypeDef",
    "ServiceResourceObjectAclRequestTypeDef",
    "ServiceResourceObjectRequestTypeDef",
    "ServiceResourceObjectSummaryRequestTypeDef",
    "ServiceResourceObjectVersionRequestTypeDef",
    "SourceSelectionCriteriaTypeDef",
    "SseKmsEncryptedObjectsTypeDef",
    "StatsEventTypeDef",
    "StatsTypeDef",
    "StorageClassAnalysisDataExportTypeDef",
    "StorageClassAnalysisTypeDef",
    "TagTypeDef",
    "TaggingTypeDef",
    "TargetGrantTypeDef",
    "TieringTypeDef",
    "TopicConfigurationDeprecatedTypeDef",
    "TopicConfigurationTypeDef",
    "TransitionTypeDef",
    "UploadPartCopyOutputTypeDef",
    "UploadPartCopyRequestMultipartUploadPartTypeDef",
    "UploadPartCopyRequestRequestTypeDef",
    "UploadPartOutputTypeDef",
    "UploadPartRequestMultipartUploadPartTypeDef",
    "UploadPartRequestRequestTypeDef",
    "VersioningConfigurationTypeDef",
    "WaiterConfigTypeDef",
    "WebsiteConfigurationTypeDef",
    "WriteGetObjectResponseRequestRequestTypeDef",
)

AbortIncompleteMultipartUploadTypeDef = TypedDict(
    "AbortIncompleteMultipartUploadTypeDef",
    {
        "DaysAfterInitiation": int,
    },
    total=False,
)

AbortMultipartUploadOutputTypeDef = TypedDict(
    "AbortMultipartUploadOutputTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AbortMultipartUploadRequestMultipartUploadTypeDef = TypedDict(
    "AbortMultipartUploadRequestMultipartUploadTypeDef",
    {
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredAbortMultipartUploadRequestRequestTypeDef = TypedDict(
    "_RequiredAbortMultipartUploadRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "UploadId": str,
    },
)
_OptionalAbortMultipartUploadRequestRequestTypeDef = TypedDict(
    "_OptionalAbortMultipartUploadRequestRequestTypeDef",
    {
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class AbortMultipartUploadRequestRequestTypeDef(
    _RequiredAbortMultipartUploadRequestRequestTypeDef,
    _OptionalAbortMultipartUploadRequestRequestTypeDef,
):
    pass

AccelerateConfigurationTypeDef = TypedDict(
    "AccelerateConfigurationTypeDef",
    {
        "Status": BucketAccelerateStatusType,
    },
    total=False,
)

AccessControlPolicyTypeDef = TypedDict(
    "AccessControlPolicyTypeDef",
    {
        "Grants": List["GrantTypeDef"],
        "Owner": "OwnerTypeDef",
    },
    total=False,
)

AccessControlTranslationTypeDef = TypedDict(
    "AccessControlTranslationTypeDef",
    {
        "Owner": Literal["Destination"],
    },
)

AnalyticsAndOperatorTypeDef = TypedDict(
    "AnalyticsAndOperatorTypeDef",
    {
        "Prefix": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredAnalyticsConfigurationTypeDef = TypedDict(
    "_RequiredAnalyticsConfigurationTypeDef",
    {
        "Id": str,
        "StorageClassAnalysis": "StorageClassAnalysisTypeDef",
    },
)
_OptionalAnalyticsConfigurationTypeDef = TypedDict(
    "_OptionalAnalyticsConfigurationTypeDef",
    {
        "Filter": "AnalyticsFilterTypeDef",
    },
    total=False,
)

class AnalyticsConfigurationTypeDef(
    _RequiredAnalyticsConfigurationTypeDef, _OptionalAnalyticsConfigurationTypeDef
):
    pass

AnalyticsExportDestinationTypeDef = TypedDict(
    "AnalyticsExportDestinationTypeDef",
    {
        "S3BucketDestination": "AnalyticsS3BucketDestinationTypeDef",
    },
)

AnalyticsFilterTypeDef = TypedDict(
    "AnalyticsFilterTypeDef",
    {
        "Prefix": str,
        "Tag": "TagTypeDef",
        "And": "AnalyticsAndOperatorTypeDef",
    },
    total=False,
)

_RequiredAnalyticsS3BucketDestinationTypeDef = TypedDict(
    "_RequiredAnalyticsS3BucketDestinationTypeDef",
    {
        "Format": Literal["CSV"],
        "Bucket": str,
    },
)
_OptionalAnalyticsS3BucketDestinationTypeDef = TypedDict(
    "_OptionalAnalyticsS3BucketDestinationTypeDef",
    {
        "BucketAccountId": str,
        "Prefix": str,
    },
    total=False,
)

class AnalyticsS3BucketDestinationTypeDef(
    _RequiredAnalyticsS3BucketDestinationTypeDef, _OptionalAnalyticsS3BucketDestinationTypeDef
):
    pass

_RequiredBucketCopyRequestTypeDef = TypedDict(
    "_RequiredBucketCopyRequestTypeDef",
    {
        "CopySource": "CopySourceTypeDef",
        "Key": str,
    },
)
_OptionalBucketCopyRequestTypeDef = TypedDict(
    "_OptionalBucketCopyRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "SourceClient": BaseClient,
        "Config": TransferConfig,
    },
    total=False,
)

class BucketCopyRequestTypeDef(
    _RequiredBucketCopyRequestTypeDef, _OptionalBucketCopyRequestTypeDef
):
    pass

_RequiredBucketDownloadFileRequestTypeDef = TypedDict(
    "_RequiredBucketDownloadFileRequestTypeDef",
    {
        "Key": str,
        "Filename": str,
    },
)
_OptionalBucketDownloadFileRequestTypeDef = TypedDict(
    "_OptionalBucketDownloadFileRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)

class BucketDownloadFileRequestTypeDef(
    _RequiredBucketDownloadFileRequestTypeDef, _OptionalBucketDownloadFileRequestTypeDef
):
    pass

_RequiredBucketDownloadFileobjRequestTypeDef = TypedDict(
    "_RequiredBucketDownloadFileobjRequestTypeDef",
    {
        "Key": str,
        "Fileobj": IO[Any],
    },
)
_OptionalBucketDownloadFileobjRequestTypeDef = TypedDict(
    "_OptionalBucketDownloadFileobjRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)

class BucketDownloadFileobjRequestTypeDef(
    _RequiredBucketDownloadFileobjRequestTypeDef, _OptionalBucketDownloadFileobjRequestTypeDef
):
    pass

BucketLifecycleConfigurationTypeDef = TypedDict(
    "BucketLifecycleConfigurationTypeDef",
    {
        "Rules": List["LifecycleRuleTypeDef"],
    },
)

BucketLoggingStatusTypeDef = TypedDict(
    "BucketLoggingStatusTypeDef",
    {
        "LoggingEnabled": "LoggingEnabledTypeDef",
    },
    total=False,
)

BucketObjectRequestTypeDef = TypedDict(
    "BucketObjectRequestTypeDef",
    {
        "key": str,
    },
)

BucketTypeDef = TypedDict(
    "BucketTypeDef",
    {
        "Name": str,
        "CreationDate": datetime,
    },
    total=False,
)

_RequiredBucketUploadFileRequestTypeDef = TypedDict(
    "_RequiredBucketUploadFileRequestTypeDef",
    {
        "Filename": str,
        "Key": str,
    },
)
_OptionalBucketUploadFileRequestTypeDef = TypedDict(
    "_OptionalBucketUploadFileRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)

class BucketUploadFileRequestTypeDef(
    _RequiredBucketUploadFileRequestTypeDef, _OptionalBucketUploadFileRequestTypeDef
):
    pass

_RequiredBucketUploadFileobjRequestTypeDef = TypedDict(
    "_RequiredBucketUploadFileobjRequestTypeDef",
    {
        "Fileobj": IO[Any],
        "Key": str,
    },
)
_OptionalBucketUploadFileobjRequestTypeDef = TypedDict(
    "_OptionalBucketUploadFileobjRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)

class BucketUploadFileobjRequestTypeDef(
    _RequiredBucketUploadFileobjRequestTypeDef, _OptionalBucketUploadFileobjRequestTypeDef
):
    pass

CORSConfigurationTypeDef = TypedDict(
    "CORSConfigurationTypeDef",
    {
        "CORSRules": List["CORSRuleTypeDef"],
    },
)

_RequiredCORSRuleTypeDef = TypedDict(
    "_RequiredCORSRuleTypeDef",
    {
        "AllowedMethods": List[str],
        "AllowedOrigins": List[str],
    },
)
_OptionalCORSRuleTypeDef = TypedDict(
    "_OptionalCORSRuleTypeDef",
    {
        "ID": str,
        "AllowedHeaders": List[str],
        "ExposeHeaders": List[str],
        "MaxAgeSeconds": int,
    },
    total=False,
)

class CORSRuleTypeDef(_RequiredCORSRuleTypeDef, _OptionalCORSRuleTypeDef):
    pass

CSVInputTypeDef = TypedDict(
    "CSVInputTypeDef",
    {
        "FileHeaderInfo": FileHeaderInfoType,
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
        "AllowQuotedRecordDelimiter": bool,
    },
    total=False,
)

CSVOutputTypeDef = TypedDict(
    "CSVOutputTypeDef",
    {
        "QuoteFields": QuoteFieldsType,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

_RequiredClientCopyRequestTypeDef = TypedDict(
    "_RequiredClientCopyRequestTypeDef",
    {
        "CopySource": "CopySourceTypeDef",
        "Bucket": str,
        "Key": str,
    },
)
_OptionalClientCopyRequestTypeDef = TypedDict(
    "_OptionalClientCopyRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "SourceClient": BaseClient,
        "Config": TransferConfig,
    },
    total=False,
)

class ClientCopyRequestTypeDef(
    _RequiredClientCopyRequestTypeDef, _OptionalClientCopyRequestTypeDef
):
    pass

_RequiredClientDownloadFileRequestTypeDef = TypedDict(
    "_RequiredClientDownloadFileRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "Filename": str,
    },
)
_OptionalClientDownloadFileRequestTypeDef = TypedDict(
    "_OptionalClientDownloadFileRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)

class ClientDownloadFileRequestTypeDef(
    _RequiredClientDownloadFileRequestTypeDef, _OptionalClientDownloadFileRequestTypeDef
):
    pass

_RequiredClientDownloadFileobjRequestTypeDef = TypedDict(
    "_RequiredClientDownloadFileobjRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "Fileobj": IO[Any],
    },
)
_OptionalClientDownloadFileobjRequestTypeDef = TypedDict(
    "_OptionalClientDownloadFileobjRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)

class ClientDownloadFileobjRequestTypeDef(
    _RequiredClientDownloadFileobjRequestTypeDef, _OptionalClientDownloadFileobjRequestTypeDef
):
    pass

_RequiredClientGeneratePresignedPostRequestTypeDef = TypedDict(
    "_RequiredClientGeneratePresignedPostRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalClientGeneratePresignedPostRequestTypeDef = TypedDict(
    "_OptionalClientGeneratePresignedPostRequestTypeDef",
    {
        "Fields": Dict[str, Any],
        "Conditions": List[Any],
        "ExpiresIn": int,
    },
    total=False,
)

class ClientGeneratePresignedPostRequestTypeDef(
    _RequiredClientGeneratePresignedPostRequestTypeDef,
    _OptionalClientGeneratePresignedPostRequestTypeDef,
):
    pass

_RequiredClientUploadFileRequestTypeDef = TypedDict(
    "_RequiredClientUploadFileRequestTypeDef",
    {
        "Filename": str,
        "Bucket": str,
        "Key": str,
    },
)
_OptionalClientUploadFileRequestTypeDef = TypedDict(
    "_OptionalClientUploadFileRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)

class ClientUploadFileRequestTypeDef(
    _RequiredClientUploadFileRequestTypeDef, _OptionalClientUploadFileRequestTypeDef
):
    pass

_RequiredClientUploadFileobjRequestTypeDef = TypedDict(
    "_RequiredClientUploadFileobjRequestTypeDef",
    {
        "Fileobj": IO[Any],
        "Bucket": str,
        "Key": str,
    },
)
_OptionalClientUploadFileobjRequestTypeDef = TypedDict(
    "_OptionalClientUploadFileobjRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)

class ClientUploadFileobjRequestTypeDef(
    _RequiredClientUploadFileobjRequestTypeDef, _OptionalClientUploadFileobjRequestTypeDef
):
    pass

CloudFunctionConfigurationTypeDef = TypedDict(
    "CloudFunctionConfigurationTypeDef",
    {
        "Id": str,
        "Event": EventType,
        "Events": List[EventType],
        "CloudFunction": str,
        "InvocationRole": str,
    },
    total=False,
)

CommonPrefixTypeDef = TypedDict(
    "CommonPrefixTypeDef",
    {
        "Prefix": str,
    },
    total=False,
)

CompleteMultipartUploadOutputTypeDef = TypedDict(
    "CompleteMultipartUploadOutputTypeDef",
    {
        "Location": str,
        "Bucket": str,
        "Key": str,
        "Expiration": str,
        "ETag": str,
        "ServerSideEncryption": ServerSideEncryptionType,
        "VersionId": str,
        "SSEKMSKeyId": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CompleteMultipartUploadRequestMultipartUploadTypeDef = TypedDict(
    "CompleteMultipartUploadRequestMultipartUploadTypeDef",
    {
        "MultipartUpload": "CompletedMultipartUploadTypeDef",
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredCompleteMultipartUploadRequestRequestTypeDef = TypedDict(
    "_RequiredCompleteMultipartUploadRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "UploadId": str,
    },
)
_OptionalCompleteMultipartUploadRequestRequestTypeDef = TypedDict(
    "_OptionalCompleteMultipartUploadRequestRequestTypeDef",
    {
        "MultipartUpload": "CompletedMultipartUploadTypeDef",
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class CompleteMultipartUploadRequestRequestTypeDef(
    _RequiredCompleteMultipartUploadRequestRequestTypeDef,
    _OptionalCompleteMultipartUploadRequestRequestTypeDef,
):
    pass

CompletedMultipartUploadTypeDef = TypedDict(
    "CompletedMultipartUploadTypeDef",
    {
        "Parts": List["CompletedPartTypeDef"],
    },
    total=False,
)

CompletedPartTypeDef = TypedDict(
    "CompletedPartTypeDef",
    {
        "ETag": str,
        "PartNumber": int,
    },
    total=False,
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "HttpErrorCodeReturnedEquals": str,
        "KeyPrefixEquals": str,
    },
    total=False,
)

CopyObjectOutputTypeDef = TypedDict(
    "CopyObjectOutputTypeDef",
    {
        "CopyObjectResult": "CopyObjectResultTypeDef",
        "Expiration": str,
        "CopySourceVersionId": str,
        "VersionId": str,
        "ServerSideEncryption": ServerSideEncryptionType,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCopyObjectRequestObjectSummaryTypeDef = TypedDict(
    "_RequiredCopyObjectRequestObjectSummaryTypeDef",
    {
        "CopySource": str,
    },
)
_OptionalCopyObjectRequestObjectSummaryTypeDef = TypedDict(
    "_OptionalCopyObjectRequestObjectSummaryTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "CopySourceIfMatch": str,
        "CopySourceIfModifiedSince": Union[datetime, str],
        "CopySourceIfNoneMatch": str,
        "CopySourceIfUnmodifiedSince": Union[datetime, str],
        "Expires": Union[datetime, str],
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWriteACP": str,
        "Metadata": Dict[str, str],
        "MetadataDirective": MetadataDirectiveType,
        "TaggingDirective": TaggingDirectiveType,
        "ServerSideEncryption": ServerSideEncryptionType,
        "StorageClass": StorageClassType,
        "WebsiteRedirectLocation": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "CopySourceSSECustomerAlgorithm": str,
        "CopySourceSSECustomerKey": str,
        "CopySourceSSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "Tagging": str,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ExpectedBucketOwner": str,
        "ExpectedSourceBucketOwner": str,
    },
    total=False,
)

class CopyObjectRequestObjectSummaryTypeDef(
    _RequiredCopyObjectRequestObjectSummaryTypeDef, _OptionalCopyObjectRequestObjectSummaryTypeDef
):
    pass

_RequiredCopyObjectRequestObjectTypeDef = TypedDict(
    "_RequiredCopyObjectRequestObjectTypeDef",
    {
        "CopySource": str,
    },
)
_OptionalCopyObjectRequestObjectTypeDef = TypedDict(
    "_OptionalCopyObjectRequestObjectTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "CopySourceIfMatch": str,
        "CopySourceIfModifiedSince": Union[datetime, str],
        "CopySourceIfNoneMatch": str,
        "CopySourceIfUnmodifiedSince": Union[datetime, str],
        "Expires": Union[datetime, str],
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWriteACP": str,
        "Metadata": Dict[str, str],
        "MetadataDirective": MetadataDirectiveType,
        "TaggingDirective": TaggingDirectiveType,
        "ServerSideEncryption": ServerSideEncryptionType,
        "StorageClass": StorageClassType,
        "WebsiteRedirectLocation": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "CopySourceSSECustomerAlgorithm": str,
        "CopySourceSSECustomerKey": str,
        "CopySourceSSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "Tagging": str,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ExpectedBucketOwner": str,
        "ExpectedSourceBucketOwner": str,
    },
    total=False,
)

class CopyObjectRequestObjectTypeDef(
    _RequiredCopyObjectRequestObjectTypeDef, _OptionalCopyObjectRequestObjectTypeDef
):
    pass

_RequiredCopyObjectRequestRequestTypeDef = TypedDict(
    "_RequiredCopyObjectRequestRequestTypeDef",
    {
        "Bucket": str,
        "CopySource": Union[str, "CopySourceTypeDef"],
        "Key": str,
    },
)
_OptionalCopyObjectRequestRequestTypeDef = TypedDict(
    "_OptionalCopyObjectRequestRequestTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "CopySourceIfMatch": str,
        "CopySourceIfModifiedSince": Union[datetime, str],
        "CopySourceIfNoneMatch": str,
        "CopySourceIfUnmodifiedSince": Union[datetime, str],
        "Expires": Union[datetime, str],
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWriteACP": str,
        "Metadata": Dict[str, str],
        "MetadataDirective": MetadataDirectiveType,
        "TaggingDirective": TaggingDirectiveType,
        "ServerSideEncryption": ServerSideEncryptionType,
        "StorageClass": StorageClassType,
        "WebsiteRedirectLocation": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "CopySourceSSECustomerAlgorithm": str,
        "CopySourceSSECustomerKey": str,
        "CopySourceSSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "Tagging": str,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ExpectedBucketOwner": str,
        "ExpectedSourceBucketOwner": str,
    },
    total=False,
)

class CopyObjectRequestRequestTypeDef(
    _RequiredCopyObjectRequestRequestTypeDef, _OptionalCopyObjectRequestRequestTypeDef
):
    pass

CopyObjectResultTypeDef = TypedDict(
    "CopyObjectResultTypeDef",
    {
        "ETag": str,
        "LastModified": datetime,
    },
    total=False,
)

CopyPartResultTypeDef = TypedDict(
    "CopyPartResultTypeDef",
    {
        "ETag": str,
        "LastModified": datetime,
    },
    total=False,
)

_RequiredCopySourceTypeDef = TypedDict(
    "_RequiredCopySourceTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalCopySourceTypeDef = TypedDict(
    "_OptionalCopySourceTypeDef",
    {
        "VersionId": str,
    },
    total=False,
)

class CopySourceTypeDef(_RequiredCopySourceTypeDef, _OptionalCopySourceTypeDef):
    pass

CreateBucketConfigurationTypeDef = TypedDict(
    "CreateBucketConfigurationTypeDef",
    {
        "LocationConstraint": BucketLocationConstraintType,
    },
    total=False,
)

CreateBucketOutputTypeDef = TypedDict(
    "CreateBucketOutputTypeDef",
    {
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBucketRequestBucketTypeDef = TypedDict(
    "CreateBucketRequestBucketTypeDef",
    {
        "ACL": BucketCannedACLType,
        "CreateBucketConfiguration": "CreateBucketConfigurationTypeDef",
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWrite": str,
        "GrantWriteACP": str,
        "ObjectLockEnabledForBucket": bool,
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
    },
    total=False,
)

class CreateBucketRequestRequestTypeDef(
    _RequiredCreateBucketRequestRequestTypeDef, _OptionalCreateBucketRequestRequestTypeDef
):
    pass

_RequiredCreateBucketRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateBucketRequestServiceResourceTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalCreateBucketRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateBucketRequestServiceResourceTypeDef",
    {
        "ACL": BucketCannedACLType,
        "CreateBucketConfiguration": "CreateBucketConfigurationTypeDef",
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWrite": str,
        "GrantWriteACP": str,
        "ObjectLockEnabledForBucket": bool,
    },
    total=False,
)

class CreateBucketRequestServiceResourceTypeDef(
    _RequiredCreateBucketRequestServiceResourceTypeDef,
    _OptionalCreateBucketRequestServiceResourceTypeDef,
):
    pass

CreateMultipartUploadOutputTypeDef = TypedDict(
    "CreateMultipartUploadOutputTypeDef",
    {
        "AbortDate": datetime,
        "AbortRuleId": str,
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "ServerSideEncryption": ServerSideEncryptionType,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMultipartUploadRequestObjectSummaryTypeDef = TypedDict(
    "CreateMultipartUploadRequestObjectSummaryTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "Expires": Union[datetime, str],
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWriteACP": str,
        "Metadata": Dict[str, str],
        "ServerSideEncryption": ServerSideEncryptionType,
        "StorageClass": StorageClassType,
        "WebsiteRedirectLocation": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestPayer": Literal["requester"],
        "Tagging": str,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

CreateMultipartUploadRequestObjectTypeDef = TypedDict(
    "CreateMultipartUploadRequestObjectTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "Expires": Union[datetime, str],
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWriteACP": str,
        "Metadata": Dict[str, str],
        "ServerSideEncryption": ServerSideEncryptionType,
        "StorageClass": StorageClassType,
        "WebsiteRedirectLocation": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestPayer": Literal["requester"],
        "Tagging": str,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredCreateMultipartUploadRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMultipartUploadRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalCreateMultipartUploadRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMultipartUploadRequestRequestTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "Expires": Union[datetime, str],
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWriteACP": str,
        "Metadata": Dict[str, str],
        "ServerSideEncryption": ServerSideEncryptionType,
        "StorageClass": StorageClassType,
        "WebsiteRedirectLocation": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestPayer": Literal["requester"],
        "Tagging": str,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class CreateMultipartUploadRequestRequestTypeDef(
    _RequiredCreateMultipartUploadRequestRequestTypeDef,
    _OptionalCreateMultipartUploadRequestRequestTypeDef,
):
    pass

DefaultRetentionTypeDef = TypedDict(
    "DefaultRetentionTypeDef",
    {
        "Mode": ObjectLockRetentionModeType,
        "Days": int,
        "Years": int,
    },
    total=False,
)

_RequiredDeleteBucketAnalyticsConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketAnalyticsConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
    },
)
_OptionalDeleteBucketAnalyticsConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketAnalyticsConfigurationRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class DeleteBucketAnalyticsConfigurationRequestRequestTypeDef(
    _RequiredDeleteBucketAnalyticsConfigurationRequestRequestTypeDef,
    _OptionalDeleteBucketAnalyticsConfigurationRequestRequestTypeDef,
):
    pass

DeleteBucketCorsRequestBucketCorsTypeDef = TypedDict(
    "DeleteBucketCorsRequestBucketCorsTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredDeleteBucketCorsRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketCorsRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDeleteBucketCorsRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketCorsRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class DeleteBucketCorsRequestRequestTypeDef(
    _RequiredDeleteBucketCorsRequestRequestTypeDef, _OptionalDeleteBucketCorsRequestRequestTypeDef
):
    pass

_RequiredDeleteBucketEncryptionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketEncryptionRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDeleteBucketEncryptionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketEncryptionRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class DeleteBucketEncryptionRequestRequestTypeDef(
    _RequiredDeleteBucketEncryptionRequestRequestTypeDef,
    _OptionalDeleteBucketEncryptionRequestRequestTypeDef,
):
    pass

DeleteBucketIntelligentTieringConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteBucketIntelligentTieringConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
    },
)

_RequiredDeleteBucketInventoryConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketInventoryConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
    },
)
_OptionalDeleteBucketInventoryConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketInventoryConfigurationRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class DeleteBucketInventoryConfigurationRequestRequestTypeDef(
    _RequiredDeleteBucketInventoryConfigurationRequestRequestTypeDef,
    _OptionalDeleteBucketInventoryConfigurationRequestRequestTypeDef,
):
    pass

DeleteBucketLifecycleRequestBucketLifecycleConfigurationTypeDef = TypedDict(
    "DeleteBucketLifecycleRequestBucketLifecycleConfigurationTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

DeleteBucketLifecycleRequestBucketLifecycleTypeDef = TypedDict(
    "DeleteBucketLifecycleRequestBucketLifecycleTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredDeleteBucketLifecycleRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketLifecycleRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDeleteBucketLifecycleRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketLifecycleRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class DeleteBucketLifecycleRequestRequestTypeDef(
    _RequiredDeleteBucketLifecycleRequestRequestTypeDef,
    _OptionalDeleteBucketLifecycleRequestRequestTypeDef,
):
    pass

_RequiredDeleteBucketMetricsConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketMetricsConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
    },
)
_OptionalDeleteBucketMetricsConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketMetricsConfigurationRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class DeleteBucketMetricsConfigurationRequestRequestTypeDef(
    _RequiredDeleteBucketMetricsConfigurationRequestRequestTypeDef,
    _OptionalDeleteBucketMetricsConfigurationRequestRequestTypeDef,
):
    pass

_RequiredDeleteBucketOwnershipControlsRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketOwnershipControlsRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDeleteBucketOwnershipControlsRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketOwnershipControlsRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class DeleteBucketOwnershipControlsRequestRequestTypeDef(
    _RequiredDeleteBucketOwnershipControlsRequestRequestTypeDef,
    _OptionalDeleteBucketOwnershipControlsRequestRequestTypeDef,
):
    pass

DeleteBucketPolicyRequestBucketPolicyTypeDef = TypedDict(
    "DeleteBucketPolicyRequestBucketPolicyTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredDeleteBucketPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketPolicyRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDeleteBucketPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketPolicyRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class DeleteBucketPolicyRequestRequestTypeDef(
    _RequiredDeleteBucketPolicyRequestRequestTypeDef,
    _OptionalDeleteBucketPolicyRequestRequestTypeDef,
):
    pass

_RequiredDeleteBucketReplicationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketReplicationRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDeleteBucketReplicationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketReplicationRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class DeleteBucketReplicationRequestRequestTypeDef(
    _RequiredDeleteBucketReplicationRequestRequestTypeDef,
    _OptionalDeleteBucketReplicationRequestRequestTypeDef,
):
    pass

DeleteBucketRequestBucketTypeDef = TypedDict(
    "DeleteBucketRequestBucketTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredDeleteBucketRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDeleteBucketRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class DeleteBucketRequestRequestTypeDef(
    _RequiredDeleteBucketRequestRequestTypeDef, _OptionalDeleteBucketRequestRequestTypeDef
):
    pass

DeleteBucketTaggingRequestBucketTaggingTypeDef = TypedDict(
    "DeleteBucketTaggingRequestBucketTaggingTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredDeleteBucketTaggingRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketTaggingRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDeleteBucketTaggingRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketTaggingRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class DeleteBucketTaggingRequestRequestTypeDef(
    _RequiredDeleteBucketTaggingRequestRequestTypeDef,
    _OptionalDeleteBucketTaggingRequestRequestTypeDef,
):
    pass

DeleteBucketWebsiteRequestBucketWebsiteTypeDef = TypedDict(
    "DeleteBucketWebsiteRequestBucketWebsiteTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredDeleteBucketWebsiteRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketWebsiteRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDeleteBucketWebsiteRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketWebsiteRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class DeleteBucketWebsiteRequestRequestTypeDef(
    _RequiredDeleteBucketWebsiteRequestRequestTypeDef,
    _OptionalDeleteBucketWebsiteRequestRequestTypeDef,
):
    pass

DeleteMarkerEntryTypeDef = TypedDict(
    "DeleteMarkerEntryTypeDef",
    {
        "Owner": "OwnerTypeDef",
        "Key": str,
        "VersionId": str,
        "IsLatest": bool,
        "LastModified": datetime,
    },
    total=False,
)

DeleteMarkerReplicationTypeDef = TypedDict(
    "DeleteMarkerReplicationTypeDef",
    {
        "Status": DeleteMarkerReplicationStatusType,
    },
    total=False,
)

DeleteObjectOutputTypeDef = TypedDict(
    "DeleteObjectOutputTypeDef",
    {
        "DeleteMarker": bool,
        "VersionId": str,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteObjectRequestObjectSummaryTypeDef = TypedDict(
    "DeleteObjectRequestObjectSummaryTypeDef",
    {
        "MFA": str,
        "VersionId": str,
        "RequestPayer": Literal["requester"],
        "BypassGovernanceRetention": bool,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

DeleteObjectRequestObjectTypeDef = TypedDict(
    "DeleteObjectRequestObjectTypeDef",
    {
        "MFA": str,
        "VersionId": str,
        "RequestPayer": Literal["requester"],
        "BypassGovernanceRetention": bool,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

DeleteObjectRequestObjectVersionTypeDef = TypedDict(
    "DeleteObjectRequestObjectVersionTypeDef",
    {
        "MFA": str,
        "RequestPayer": Literal["requester"],
        "BypassGovernanceRetention": bool,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredDeleteObjectRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteObjectRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalDeleteObjectRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteObjectRequestRequestTypeDef",
    {
        "MFA": str,
        "VersionId": str,
        "RequestPayer": Literal["requester"],
        "BypassGovernanceRetention": bool,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class DeleteObjectRequestRequestTypeDef(
    _RequiredDeleteObjectRequestRequestTypeDef, _OptionalDeleteObjectRequestRequestTypeDef
):
    pass

DeleteObjectTaggingOutputTypeDef = TypedDict(
    "DeleteObjectTaggingOutputTypeDef",
    {
        "VersionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteObjectTaggingRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteObjectTaggingRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalDeleteObjectTaggingRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteObjectTaggingRequestRequestTypeDef",
    {
        "VersionId": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class DeleteObjectTaggingRequestRequestTypeDef(
    _RequiredDeleteObjectTaggingRequestRequestTypeDef,
    _OptionalDeleteObjectTaggingRequestRequestTypeDef,
):
    pass

DeleteObjectsOutputTypeDef = TypedDict(
    "DeleteObjectsOutputTypeDef",
    {
        "Deleted": List["DeletedObjectTypeDef"],
        "RequestCharged": Literal["requester"],
        "Errors": List["ErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteObjectsRequestBucketTypeDef = TypedDict(
    "_RequiredDeleteObjectsRequestBucketTypeDef",
    {
        "Delete": "DeleteTypeDef",
    },
)
_OptionalDeleteObjectsRequestBucketTypeDef = TypedDict(
    "_OptionalDeleteObjectsRequestBucketTypeDef",
    {
        "MFA": str,
        "RequestPayer": Literal["requester"],
        "BypassGovernanceRetention": bool,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class DeleteObjectsRequestBucketTypeDef(
    _RequiredDeleteObjectsRequestBucketTypeDef, _OptionalDeleteObjectsRequestBucketTypeDef
):
    pass

_RequiredDeleteObjectsRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteObjectsRequestRequestTypeDef",
    {
        "Bucket": str,
        "Delete": "DeleteTypeDef",
    },
)
_OptionalDeleteObjectsRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteObjectsRequestRequestTypeDef",
    {
        "MFA": str,
        "RequestPayer": Literal["requester"],
        "BypassGovernanceRetention": bool,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class DeleteObjectsRequestRequestTypeDef(
    _RequiredDeleteObjectsRequestRequestTypeDef, _OptionalDeleteObjectsRequestRequestTypeDef
):
    pass

_RequiredDeletePublicAccessBlockRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePublicAccessBlockRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDeletePublicAccessBlockRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePublicAccessBlockRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class DeletePublicAccessBlockRequestRequestTypeDef(
    _RequiredDeletePublicAccessBlockRequestRequestTypeDef,
    _OptionalDeletePublicAccessBlockRequestRequestTypeDef,
):
    pass

_RequiredDeleteTypeDef = TypedDict(
    "_RequiredDeleteTypeDef",
    {
        "Objects": List["ObjectIdentifierTypeDef"],
    },
)
_OptionalDeleteTypeDef = TypedDict(
    "_OptionalDeleteTypeDef",
    {
        "Quiet": bool,
    },
    total=False,
)

class DeleteTypeDef(_RequiredDeleteTypeDef, _OptionalDeleteTypeDef):
    pass

DeletedObjectTypeDef = TypedDict(
    "DeletedObjectTypeDef",
    {
        "Key": str,
        "VersionId": str,
        "DeleteMarker": bool,
        "DeleteMarkerVersionId": str,
    },
    total=False,
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
        "StorageClass": StorageClassType,
        "AccessControlTranslation": "AccessControlTranslationTypeDef",
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "ReplicationTime": "ReplicationTimeTypeDef",
        "Metrics": "MetricsTypeDef",
    },
    total=False,
)

class DestinationTypeDef(_RequiredDestinationTypeDef, _OptionalDestinationTypeDef):
    pass

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "ReplicaKmsKeyID": str,
    },
    total=False,
)

_RequiredEncryptionTypeDef = TypedDict(
    "_RequiredEncryptionTypeDef",
    {
        "EncryptionType": ServerSideEncryptionType,
    },
)
_OptionalEncryptionTypeDef = TypedDict(
    "_OptionalEncryptionTypeDef",
    {
        "KMSKeyId": str,
        "KMSContext": str,
    },
    total=False,
)

class EncryptionTypeDef(_RequiredEncryptionTypeDef, _OptionalEncryptionTypeDef):
    pass

ErrorDocumentTypeDef = TypedDict(
    "ErrorDocumentTypeDef",
    {
        "Key": str,
    },
)

ErrorTypeDef = TypedDict(
    "ErrorTypeDef",
    {
        "Key": str,
        "VersionId": str,
        "Code": str,
        "Message": str,
    },
    total=False,
)

ExistingObjectReplicationTypeDef = TypedDict(
    "ExistingObjectReplicationTypeDef",
    {
        "Status": ExistingObjectReplicationStatusType,
    },
)

FilterRuleTypeDef = TypedDict(
    "FilterRuleTypeDef",
    {
        "Name": FilterRuleNameType,
        "Value": str,
    },
    total=False,
)

GetBucketAccelerateConfigurationOutputTypeDef = TypedDict(
    "GetBucketAccelerateConfigurationOutputTypeDef",
    {
        "Status": BucketAccelerateStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketAccelerateConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketAccelerateConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketAccelerateConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketAccelerateConfigurationRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetBucketAccelerateConfigurationRequestRequestTypeDef(
    _RequiredGetBucketAccelerateConfigurationRequestRequestTypeDef,
    _OptionalGetBucketAccelerateConfigurationRequestRequestTypeDef,
):
    pass

GetBucketAclOutputTypeDef = TypedDict(
    "GetBucketAclOutputTypeDef",
    {
        "Owner": "OwnerTypeDef",
        "Grants": List["GrantTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketAclRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketAclRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketAclRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketAclRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetBucketAclRequestRequestTypeDef(
    _RequiredGetBucketAclRequestRequestTypeDef, _OptionalGetBucketAclRequestRequestTypeDef
):
    pass

GetBucketAnalyticsConfigurationOutputTypeDef = TypedDict(
    "GetBucketAnalyticsConfigurationOutputTypeDef",
    {
        "AnalyticsConfiguration": "AnalyticsConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketAnalyticsConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketAnalyticsConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
    },
)
_OptionalGetBucketAnalyticsConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketAnalyticsConfigurationRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetBucketAnalyticsConfigurationRequestRequestTypeDef(
    _RequiredGetBucketAnalyticsConfigurationRequestRequestTypeDef,
    _OptionalGetBucketAnalyticsConfigurationRequestRequestTypeDef,
):
    pass

GetBucketCorsOutputTypeDef = TypedDict(
    "GetBucketCorsOutputTypeDef",
    {
        "CORSRules": List["CORSRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketCorsRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketCorsRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketCorsRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketCorsRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetBucketCorsRequestRequestTypeDef(
    _RequiredGetBucketCorsRequestRequestTypeDef, _OptionalGetBucketCorsRequestRequestTypeDef
):
    pass

GetBucketEncryptionOutputTypeDef = TypedDict(
    "GetBucketEncryptionOutputTypeDef",
    {
        "ServerSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketEncryptionRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketEncryptionRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketEncryptionRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketEncryptionRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetBucketEncryptionRequestRequestTypeDef(
    _RequiredGetBucketEncryptionRequestRequestTypeDef,
    _OptionalGetBucketEncryptionRequestRequestTypeDef,
):
    pass

GetBucketIntelligentTieringConfigurationOutputTypeDef = TypedDict(
    "GetBucketIntelligentTieringConfigurationOutputTypeDef",
    {
        "IntelligentTieringConfiguration": "IntelligentTieringConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketIntelligentTieringConfigurationRequestRequestTypeDef = TypedDict(
    "GetBucketIntelligentTieringConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
    },
)

GetBucketInventoryConfigurationOutputTypeDef = TypedDict(
    "GetBucketInventoryConfigurationOutputTypeDef",
    {
        "InventoryConfiguration": "InventoryConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketInventoryConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketInventoryConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
    },
)
_OptionalGetBucketInventoryConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketInventoryConfigurationRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetBucketInventoryConfigurationRequestRequestTypeDef(
    _RequiredGetBucketInventoryConfigurationRequestRequestTypeDef,
    _OptionalGetBucketInventoryConfigurationRequestRequestTypeDef,
):
    pass

GetBucketLifecycleConfigurationOutputTypeDef = TypedDict(
    "GetBucketLifecycleConfigurationOutputTypeDef",
    {
        "Rules": List["LifecycleRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketLifecycleConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketLifecycleConfigurationRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetBucketLifecycleConfigurationRequestRequestTypeDef(
    _RequiredGetBucketLifecycleConfigurationRequestRequestTypeDef,
    _OptionalGetBucketLifecycleConfigurationRequestRequestTypeDef,
):
    pass

GetBucketLifecycleOutputTypeDef = TypedDict(
    "GetBucketLifecycleOutputTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketLifecycleRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketLifecycleRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketLifecycleRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketLifecycleRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetBucketLifecycleRequestRequestTypeDef(
    _RequiredGetBucketLifecycleRequestRequestTypeDef,
    _OptionalGetBucketLifecycleRequestRequestTypeDef,
):
    pass

GetBucketLocationOutputTypeDef = TypedDict(
    "GetBucketLocationOutputTypeDef",
    {
        "LocationConstraint": BucketLocationConstraintType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketLocationRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketLocationRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketLocationRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketLocationRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetBucketLocationRequestRequestTypeDef(
    _RequiredGetBucketLocationRequestRequestTypeDef, _OptionalGetBucketLocationRequestRequestTypeDef
):
    pass

GetBucketLoggingOutputTypeDef = TypedDict(
    "GetBucketLoggingOutputTypeDef",
    {
        "LoggingEnabled": "LoggingEnabledTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketLoggingRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketLoggingRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketLoggingRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketLoggingRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetBucketLoggingRequestRequestTypeDef(
    _RequiredGetBucketLoggingRequestRequestTypeDef, _OptionalGetBucketLoggingRequestRequestTypeDef
):
    pass

GetBucketMetricsConfigurationOutputTypeDef = TypedDict(
    "GetBucketMetricsConfigurationOutputTypeDef",
    {
        "MetricsConfiguration": "MetricsConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketMetricsConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketMetricsConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
    },
)
_OptionalGetBucketMetricsConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketMetricsConfigurationRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetBucketMetricsConfigurationRequestRequestTypeDef(
    _RequiredGetBucketMetricsConfigurationRequestRequestTypeDef,
    _OptionalGetBucketMetricsConfigurationRequestRequestTypeDef,
):
    pass

_RequiredGetBucketNotificationConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketNotificationConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketNotificationConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketNotificationConfigurationRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetBucketNotificationConfigurationRequestRequestTypeDef(
    _RequiredGetBucketNotificationConfigurationRequestRequestTypeDef,
    _OptionalGetBucketNotificationConfigurationRequestRequestTypeDef,
):
    pass

GetBucketOwnershipControlsOutputTypeDef = TypedDict(
    "GetBucketOwnershipControlsOutputTypeDef",
    {
        "OwnershipControls": "OwnershipControlsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketOwnershipControlsRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketOwnershipControlsRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketOwnershipControlsRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketOwnershipControlsRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetBucketOwnershipControlsRequestRequestTypeDef(
    _RequiredGetBucketOwnershipControlsRequestRequestTypeDef,
    _OptionalGetBucketOwnershipControlsRequestRequestTypeDef,
):
    pass

GetBucketPolicyOutputTypeDef = TypedDict(
    "GetBucketPolicyOutputTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketPolicyRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketPolicyRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetBucketPolicyRequestRequestTypeDef(
    _RequiredGetBucketPolicyRequestRequestTypeDef, _OptionalGetBucketPolicyRequestRequestTypeDef
):
    pass

GetBucketPolicyStatusOutputTypeDef = TypedDict(
    "GetBucketPolicyStatusOutputTypeDef",
    {
        "PolicyStatus": "PolicyStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketPolicyStatusRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketPolicyStatusRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketPolicyStatusRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketPolicyStatusRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetBucketPolicyStatusRequestRequestTypeDef(
    _RequiredGetBucketPolicyStatusRequestRequestTypeDef,
    _OptionalGetBucketPolicyStatusRequestRequestTypeDef,
):
    pass

GetBucketReplicationOutputTypeDef = TypedDict(
    "GetBucketReplicationOutputTypeDef",
    {
        "ReplicationConfiguration": "ReplicationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketReplicationRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketReplicationRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketReplicationRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketReplicationRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetBucketReplicationRequestRequestTypeDef(
    _RequiredGetBucketReplicationRequestRequestTypeDef,
    _OptionalGetBucketReplicationRequestRequestTypeDef,
):
    pass

GetBucketRequestPaymentOutputTypeDef = TypedDict(
    "GetBucketRequestPaymentOutputTypeDef",
    {
        "Payer": PayerType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketRequestPaymentRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketRequestPaymentRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketRequestPaymentRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketRequestPaymentRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetBucketRequestPaymentRequestRequestTypeDef(
    _RequiredGetBucketRequestPaymentRequestRequestTypeDef,
    _OptionalGetBucketRequestPaymentRequestRequestTypeDef,
):
    pass

GetBucketTaggingOutputTypeDef = TypedDict(
    "GetBucketTaggingOutputTypeDef",
    {
        "TagSet": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketTaggingRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketTaggingRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketTaggingRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketTaggingRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetBucketTaggingRequestRequestTypeDef(
    _RequiredGetBucketTaggingRequestRequestTypeDef, _OptionalGetBucketTaggingRequestRequestTypeDef
):
    pass

GetBucketVersioningOutputTypeDef = TypedDict(
    "GetBucketVersioningOutputTypeDef",
    {
        "Status": BucketVersioningStatusType,
        "MFADelete": MFADeleteStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketVersioningRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketVersioningRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketVersioningRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketVersioningRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetBucketVersioningRequestRequestTypeDef(
    _RequiredGetBucketVersioningRequestRequestTypeDef,
    _OptionalGetBucketVersioningRequestRequestTypeDef,
):
    pass

GetBucketWebsiteOutputTypeDef = TypedDict(
    "GetBucketWebsiteOutputTypeDef",
    {
        "RedirectAllRequestsTo": "RedirectAllRequestsToTypeDef",
        "IndexDocument": "IndexDocumentTypeDef",
        "ErrorDocument": "ErrorDocumentTypeDef",
        "RoutingRules": List["RoutingRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketWebsiteRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketWebsiteRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketWebsiteRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketWebsiteRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetBucketWebsiteRequestRequestTypeDef(
    _RequiredGetBucketWebsiteRequestRequestTypeDef, _OptionalGetBucketWebsiteRequestRequestTypeDef
):
    pass

GetObjectAclOutputTypeDef = TypedDict(
    "GetObjectAclOutputTypeDef",
    {
        "Owner": "OwnerTypeDef",
        "Grants": List["GrantTypeDef"],
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetObjectAclRequestRequestTypeDef = TypedDict(
    "_RequiredGetObjectAclRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalGetObjectAclRequestRequestTypeDef = TypedDict(
    "_OptionalGetObjectAclRequestRequestTypeDef",
    {
        "VersionId": str,
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetObjectAclRequestRequestTypeDef(
    _RequiredGetObjectAclRequestRequestTypeDef, _OptionalGetObjectAclRequestRequestTypeDef
):
    pass

GetObjectLegalHoldOutputTypeDef = TypedDict(
    "GetObjectLegalHoldOutputTypeDef",
    {
        "LegalHold": "ObjectLockLegalHoldTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetObjectLegalHoldRequestRequestTypeDef = TypedDict(
    "_RequiredGetObjectLegalHoldRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalGetObjectLegalHoldRequestRequestTypeDef = TypedDict(
    "_OptionalGetObjectLegalHoldRequestRequestTypeDef",
    {
        "VersionId": str,
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetObjectLegalHoldRequestRequestTypeDef(
    _RequiredGetObjectLegalHoldRequestRequestTypeDef,
    _OptionalGetObjectLegalHoldRequestRequestTypeDef,
):
    pass

GetObjectLockConfigurationOutputTypeDef = TypedDict(
    "GetObjectLockConfigurationOutputTypeDef",
    {
        "ObjectLockConfiguration": "ObjectLockConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetObjectLockConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredGetObjectLockConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetObjectLockConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalGetObjectLockConfigurationRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetObjectLockConfigurationRequestRequestTypeDef(
    _RequiredGetObjectLockConfigurationRequestRequestTypeDef,
    _OptionalGetObjectLockConfigurationRequestRequestTypeDef,
):
    pass

GetObjectOutputTypeDef = TypedDict(
    "GetObjectOutputTypeDef",
    {
        "Body": StreamingBody,
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentRange": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": ServerSideEncryptionType,
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "BucketKeyEnabled": bool,
        "StorageClass": StorageClassType,
        "RequestCharged": Literal["requester"],
        "ReplicationStatus": ReplicationStatusType,
        "PartsCount": int,
        "TagCount": int,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetObjectRequestObjectSummaryTypeDef = TypedDict(
    "GetObjectRequestObjectSummaryTypeDef",
    {
        "IfMatch": str,
        "IfModifiedSince": Union[datetime, str],
        "IfNoneMatch": str,
        "IfUnmodifiedSince": Union[datetime, str],
        "Range": str,
        "ResponseCacheControl": str,
        "ResponseContentDisposition": str,
        "ResponseContentEncoding": str,
        "ResponseContentLanguage": str,
        "ResponseContentType": str,
        "ResponseExpires": Union[datetime, str],
        "VersionId": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "PartNumber": int,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

GetObjectRequestObjectTypeDef = TypedDict(
    "GetObjectRequestObjectTypeDef",
    {
        "IfMatch": str,
        "IfModifiedSince": Union[datetime, str],
        "IfNoneMatch": str,
        "IfUnmodifiedSince": Union[datetime, str],
        "Range": str,
        "ResponseCacheControl": str,
        "ResponseContentDisposition": str,
        "ResponseContentEncoding": str,
        "ResponseContentLanguage": str,
        "ResponseContentType": str,
        "ResponseExpires": Union[datetime, str],
        "VersionId": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "PartNumber": int,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

GetObjectRequestObjectVersionTypeDef = TypedDict(
    "GetObjectRequestObjectVersionTypeDef",
    {
        "IfMatch": str,
        "IfModifiedSince": Union[datetime, str],
        "IfNoneMatch": str,
        "IfUnmodifiedSince": Union[datetime, str],
        "Range": str,
        "ResponseCacheControl": str,
        "ResponseContentDisposition": str,
        "ResponseContentEncoding": str,
        "ResponseContentLanguage": str,
        "ResponseContentType": str,
        "ResponseExpires": Union[datetime, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "PartNumber": int,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredGetObjectRequestRequestTypeDef = TypedDict(
    "_RequiredGetObjectRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalGetObjectRequestRequestTypeDef = TypedDict(
    "_OptionalGetObjectRequestRequestTypeDef",
    {
        "IfMatch": str,
        "IfModifiedSince": Union[datetime, str],
        "IfNoneMatch": str,
        "IfUnmodifiedSince": Union[datetime, str],
        "Range": str,
        "ResponseCacheControl": str,
        "ResponseContentDisposition": str,
        "ResponseContentEncoding": str,
        "ResponseContentLanguage": str,
        "ResponseContentType": str,
        "ResponseExpires": Union[datetime, str],
        "VersionId": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "PartNumber": int,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetObjectRequestRequestTypeDef(
    _RequiredGetObjectRequestRequestTypeDef, _OptionalGetObjectRequestRequestTypeDef
):
    pass

GetObjectRetentionOutputTypeDef = TypedDict(
    "GetObjectRetentionOutputTypeDef",
    {
        "Retention": "ObjectLockRetentionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetObjectRetentionRequestRequestTypeDef = TypedDict(
    "_RequiredGetObjectRetentionRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalGetObjectRetentionRequestRequestTypeDef = TypedDict(
    "_OptionalGetObjectRetentionRequestRequestTypeDef",
    {
        "VersionId": str,
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetObjectRetentionRequestRequestTypeDef(
    _RequiredGetObjectRetentionRequestRequestTypeDef,
    _OptionalGetObjectRetentionRequestRequestTypeDef,
):
    pass

GetObjectTaggingOutputTypeDef = TypedDict(
    "GetObjectTaggingOutputTypeDef",
    {
        "VersionId": str,
        "TagSet": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetObjectTaggingRequestRequestTypeDef = TypedDict(
    "_RequiredGetObjectTaggingRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalGetObjectTaggingRequestRequestTypeDef = TypedDict(
    "_OptionalGetObjectTaggingRequestRequestTypeDef",
    {
        "VersionId": str,
        "ExpectedBucketOwner": str,
        "RequestPayer": Literal["requester"],
    },
    total=False,
)

class GetObjectTaggingRequestRequestTypeDef(
    _RequiredGetObjectTaggingRequestRequestTypeDef, _OptionalGetObjectTaggingRequestRequestTypeDef
):
    pass

GetObjectTorrentOutputTypeDef = TypedDict(
    "GetObjectTorrentOutputTypeDef",
    {
        "Body": StreamingBody,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetObjectTorrentRequestRequestTypeDef = TypedDict(
    "_RequiredGetObjectTorrentRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalGetObjectTorrentRequestRequestTypeDef = TypedDict(
    "_OptionalGetObjectTorrentRequestRequestTypeDef",
    {
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetObjectTorrentRequestRequestTypeDef(
    _RequiredGetObjectTorrentRequestRequestTypeDef, _OptionalGetObjectTorrentRequestRequestTypeDef
):
    pass

GetPublicAccessBlockOutputTypeDef = TypedDict(
    "GetPublicAccessBlockOutputTypeDef",
    {
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPublicAccessBlockRequestRequestTypeDef = TypedDict(
    "_RequiredGetPublicAccessBlockRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetPublicAccessBlockRequestRequestTypeDef = TypedDict(
    "_OptionalGetPublicAccessBlockRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class GetPublicAccessBlockRequestRequestTypeDef(
    _RequiredGetPublicAccessBlockRequestRequestTypeDef,
    _OptionalGetPublicAccessBlockRequestRequestTypeDef,
):
    pass

GlacierJobParametersTypeDef = TypedDict(
    "GlacierJobParametersTypeDef",
    {
        "Tier": TierType,
    },
)

GrantTypeDef = TypedDict(
    "GrantTypeDef",
    {
        "Grantee": "GranteeTypeDef",
        "Permission": PermissionType,
    },
    total=False,
)

_RequiredGranteeTypeDef = TypedDict(
    "_RequiredGranteeTypeDef",
    {
        "Type": TypeType,
    },
)
_OptionalGranteeTypeDef = TypedDict(
    "_OptionalGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "URI": str,
    },
    total=False,
)

class GranteeTypeDef(_RequiredGranteeTypeDef, _OptionalGranteeTypeDef):
    pass

_RequiredHeadBucketRequestRequestTypeDef = TypedDict(
    "_RequiredHeadBucketRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalHeadBucketRequestRequestTypeDef = TypedDict(
    "_OptionalHeadBucketRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class HeadBucketRequestRequestTypeDef(
    _RequiredHeadBucketRequestRequestTypeDef, _OptionalHeadBucketRequestRequestTypeDef
):
    pass

HeadObjectOutputTypeDef = TypedDict(
    "HeadObjectOutputTypeDef",
    {
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "ArchiveStatus": ArchiveStatusType,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": ServerSideEncryptionType,
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "BucketKeyEnabled": bool,
        "StorageClass": StorageClassType,
        "RequestCharged": Literal["requester"],
        "ReplicationStatus": ReplicationStatusType,
        "PartsCount": int,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HeadObjectRequestObjectVersionTypeDef = TypedDict(
    "HeadObjectRequestObjectVersionTypeDef",
    {
        "IfMatch": str,
        "IfModifiedSince": Union[datetime, str],
        "IfNoneMatch": str,
        "IfUnmodifiedSince": Union[datetime, str],
        "Range": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "PartNumber": int,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredHeadObjectRequestRequestTypeDef = TypedDict(
    "_RequiredHeadObjectRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalHeadObjectRequestRequestTypeDef = TypedDict(
    "_OptionalHeadObjectRequestRequestTypeDef",
    {
        "IfMatch": str,
        "IfModifiedSince": Union[datetime, str],
        "IfNoneMatch": str,
        "IfUnmodifiedSince": Union[datetime, str],
        "Range": str,
        "VersionId": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "PartNumber": int,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class HeadObjectRequestRequestTypeDef(
    _RequiredHeadObjectRequestRequestTypeDef, _OptionalHeadObjectRequestRequestTypeDef
):
    pass

IndexDocumentTypeDef = TypedDict(
    "IndexDocumentTypeDef",
    {
        "Suffix": str,
    },
)

InitiatorTypeDef = TypedDict(
    "InitiatorTypeDef",
    {
        "ID": str,
        "DisplayName": str,
    },
    total=False,
)

InputSerializationTypeDef = TypedDict(
    "InputSerializationTypeDef",
    {
        "CSV": "CSVInputTypeDef",
        "CompressionType": CompressionTypeType,
        "JSON": "JSONInputTypeDef",
        "Parquet": Dict[str, Any],
    },
    total=False,
)

IntelligentTieringAndOperatorTypeDef = TypedDict(
    "IntelligentTieringAndOperatorTypeDef",
    {
        "Prefix": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredIntelligentTieringConfigurationTypeDef = TypedDict(
    "_RequiredIntelligentTieringConfigurationTypeDef",
    {
        "Id": str,
        "Status": IntelligentTieringStatusType,
        "Tierings": List["TieringTypeDef"],
    },
)
_OptionalIntelligentTieringConfigurationTypeDef = TypedDict(
    "_OptionalIntelligentTieringConfigurationTypeDef",
    {
        "Filter": "IntelligentTieringFilterTypeDef",
    },
    total=False,
)

class IntelligentTieringConfigurationTypeDef(
    _RequiredIntelligentTieringConfigurationTypeDef, _OptionalIntelligentTieringConfigurationTypeDef
):
    pass

IntelligentTieringFilterTypeDef = TypedDict(
    "IntelligentTieringFilterTypeDef",
    {
        "Prefix": str,
        "Tag": "TagTypeDef",
        "And": "IntelligentTieringAndOperatorTypeDef",
    },
    total=False,
)

_RequiredInventoryConfigurationTypeDef = TypedDict(
    "_RequiredInventoryConfigurationTypeDef",
    {
        "Destination": "InventoryDestinationTypeDef",
        "IsEnabled": bool,
        "Id": str,
        "IncludedObjectVersions": InventoryIncludedObjectVersionsType,
        "Schedule": "InventoryScheduleTypeDef",
    },
)
_OptionalInventoryConfigurationTypeDef = TypedDict(
    "_OptionalInventoryConfigurationTypeDef",
    {
        "Filter": "InventoryFilterTypeDef",
        "OptionalFields": List[InventoryOptionalFieldType],
    },
    total=False,
)

class InventoryConfigurationTypeDef(
    _RequiredInventoryConfigurationTypeDef, _OptionalInventoryConfigurationTypeDef
):
    pass

InventoryDestinationTypeDef = TypedDict(
    "InventoryDestinationTypeDef",
    {
        "S3BucketDestination": "InventoryS3BucketDestinationTypeDef",
    },
)

InventoryEncryptionTypeDef = TypedDict(
    "InventoryEncryptionTypeDef",
    {
        "SSES3": Dict[str, Any],
        "SSEKMS": "SSEKMSTypeDef",
    },
    total=False,
)

InventoryFilterTypeDef = TypedDict(
    "InventoryFilterTypeDef",
    {
        "Prefix": str,
    },
)

_RequiredInventoryS3BucketDestinationTypeDef = TypedDict(
    "_RequiredInventoryS3BucketDestinationTypeDef",
    {
        "Bucket": str,
        "Format": InventoryFormatType,
    },
)
_OptionalInventoryS3BucketDestinationTypeDef = TypedDict(
    "_OptionalInventoryS3BucketDestinationTypeDef",
    {
        "AccountId": str,
        "Prefix": str,
        "Encryption": "InventoryEncryptionTypeDef",
    },
    total=False,
)

class InventoryS3BucketDestinationTypeDef(
    _RequiredInventoryS3BucketDestinationTypeDef, _OptionalInventoryS3BucketDestinationTypeDef
):
    pass

InventoryScheduleTypeDef = TypedDict(
    "InventoryScheduleTypeDef",
    {
        "Frequency": InventoryFrequencyType,
    },
)

JSONInputTypeDef = TypedDict(
    "JSONInputTypeDef",
    {
        "Type": JSONTypeType,
    },
    total=False,
)

JSONOutputTypeDef = TypedDict(
    "JSONOutputTypeDef",
    {
        "RecordDelimiter": str,
    },
    total=False,
)

_RequiredLambdaFunctionConfigurationTypeDef = TypedDict(
    "_RequiredLambdaFunctionConfigurationTypeDef",
    {
        "LambdaFunctionArn": str,
        "Events": List[EventType],
    },
)
_OptionalLambdaFunctionConfigurationTypeDef = TypedDict(
    "_OptionalLambdaFunctionConfigurationTypeDef",
    {
        "Id": str,
        "Filter": "NotificationConfigurationFilterTypeDef",
    },
    total=False,
)

class LambdaFunctionConfigurationTypeDef(
    _RequiredLambdaFunctionConfigurationTypeDef, _OptionalLambdaFunctionConfigurationTypeDef
):
    pass

LifecycleConfigurationTypeDef = TypedDict(
    "LifecycleConfigurationTypeDef",
    {
        "Rules": List["RuleTypeDef"],
    },
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
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LifecycleRuleFilterTypeDef = TypedDict(
    "LifecycleRuleFilterTypeDef",
    {
        "Prefix": str,
        "Tag": "TagTypeDef",
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
        "Prefix": str,
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

ListBucketAnalyticsConfigurationsOutputTypeDef = TypedDict(
    "ListBucketAnalyticsConfigurationsOutputTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "AnalyticsConfigurationList": List["AnalyticsConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBucketAnalyticsConfigurationsRequestRequestTypeDef = TypedDict(
    "_RequiredListBucketAnalyticsConfigurationsRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalListBucketAnalyticsConfigurationsRequestRequestTypeDef = TypedDict(
    "_OptionalListBucketAnalyticsConfigurationsRequestRequestTypeDef",
    {
        "ContinuationToken": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class ListBucketAnalyticsConfigurationsRequestRequestTypeDef(
    _RequiredListBucketAnalyticsConfigurationsRequestRequestTypeDef,
    _OptionalListBucketAnalyticsConfigurationsRequestRequestTypeDef,
):
    pass

ListBucketIntelligentTieringConfigurationsOutputTypeDef = TypedDict(
    "ListBucketIntelligentTieringConfigurationsOutputTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "IntelligentTieringConfigurationList": List["IntelligentTieringConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBucketIntelligentTieringConfigurationsRequestRequestTypeDef = TypedDict(
    "_RequiredListBucketIntelligentTieringConfigurationsRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalListBucketIntelligentTieringConfigurationsRequestRequestTypeDef = TypedDict(
    "_OptionalListBucketIntelligentTieringConfigurationsRequestRequestTypeDef",
    {
        "ContinuationToken": str,
    },
    total=False,
)

class ListBucketIntelligentTieringConfigurationsRequestRequestTypeDef(
    _RequiredListBucketIntelligentTieringConfigurationsRequestRequestTypeDef,
    _OptionalListBucketIntelligentTieringConfigurationsRequestRequestTypeDef,
):
    pass

ListBucketInventoryConfigurationsOutputTypeDef = TypedDict(
    "ListBucketInventoryConfigurationsOutputTypeDef",
    {
        "ContinuationToken": str,
        "InventoryConfigurationList": List["InventoryConfigurationTypeDef"],
        "IsTruncated": bool,
        "NextContinuationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBucketInventoryConfigurationsRequestRequestTypeDef = TypedDict(
    "_RequiredListBucketInventoryConfigurationsRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalListBucketInventoryConfigurationsRequestRequestTypeDef = TypedDict(
    "_OptionalListBucketInventoryConfigurationsRequestRequestTypeDef",
    {
        "ContinuationToken": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class ListBucketInventoryConfigurationsRequestRequestTypeDef(
    _RequiredListBucketInventoryConfigurationsRequestRequestTypeDef,
    _OptionalListBucketInventoryConfigurationsRequestRequestTypeDef,
):
    pass

ListBucketMetricsConfigurationsOutputTypeDef = TypedDict(
    "ListBucketMetricsConfigurationsOutputTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "MetricsConfigurationList": List["MetricsConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBucketMetricsConfigurationsRequestRequestTypeDef = TypedDict(
    "_RequiredListBucketMetricsConfigurationsRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalListBucketMetricsConfigurationsRequestRequestTypeDef = TypedDict(
    "_OptionalListBucketMetricsConfigurationsRequestRequestTypeDef",
    {
        "ContinuationToken": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class ListBucketMetricsConfigurationsRequestRequestTypeDef(
    _RequiredListBucketMetricsConfigurationsRequestRequestTypeDef,
    _OptionalListBucketMetricsConfigurationsRequestRequestTypeDef,
):
    pass

ListBucketsOutputTypeDef = TypedDict(
    "ListBucketsOutputTypeDef",
    {
        "Buckets": List["BucketTypeDef"],
        "Owner": "OwnerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMultipartUploadsOutputTypeDef = TypedDict(
    "ListMultipartUploadsOutputTypeDef",
    {
        "Bucket": str,
        "KeyMarker": str,
        "UploadIdMarker": str,
        "NextKeyMarker": str,
        "Prefix": str,
        "Delimiter": str,
        "NextUploadIdMarker": str,
        "MaxUploads": int,
        "IsTruncated": bool,
        "Uploads": List["MultipartUploadTypeDef"],
        "CommonPrefixes": List["CommonPrefixTypeDef"],
        "EncodingType": Literal["url"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMultipartUploadsRequestRequestTypeDef = TypedDict(
    "_RequiredListMultipartUploadsRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalListMultipartUploadsRequestRequestTypeDef = TypedDict(
    "_OptionalListMultipartUploadsRequestRequestTypeDef",
    {
        "Delimiter": str,
        "EncodingType": Literal["url"],
        "KeyMarker": str,
        "MaxUploads": int,
        "Prefix": str,
        "UploadIdMarker": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class ListMultipartUploadsRequestRequestTypeDef(
    _RequiredListMultipartUploadsRequestRequestTypeDef,
    _OptionalListMultipartUploadsRequestRequestTypeDef,
):
    pass

ListObjectVersionsOutputTypeDef = TypedDict(
    "ListObjectVersionsOutputTypeDef",
    {
        "IsTruncated": bool,
        "KeyMarker": str,
        "VersionIdMarker": str,
        "NextKeyMarker": str,
        "NextVersionIdMarker": str,
        "Versions": List["ObjectVersionTypeDef"],
        "DeleteMarkers": List["DeleteMarkerEntryTypeDef"],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List["CommonPrefixTypeDef"],
        "EncodingType": Literal["url"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListObjectVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListObjectVersionsRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalListObjectVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListObjectVersionsRequestRequestTypeDef",
    {
        "Delimiter": str,
        "EncodingType": Literal["url"],
        "KeyMarker": str,
        "MaxKeys": int,
        "Prefix": str,
        "VersionIdMarker": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class ListObjectVersionsRequestRequestTypeDef(
    _RequiredListObjectVersionsRequestRequestTypeDef,
    _OptionalListObjectVersionsRequestRequestTypeDef,
):
    pass

ListObjectsOutputTypeDef = TypedDict(
    "ListObjectsOutputTypeDef",
    {
        "IsTruncated": bool,
        "Marker": str,
        "NextMarker": str,
        "Contents": List["ObjectTypeDef"],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List["CommonPrefixTypeDef"],
        "EncodingType": Literal["url"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListObjectsRequestRequestTypeDef = TypedDict(
    "_RequiredListObjectsRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalListObjectsRequestRequestTypeDef = TypedDict(
    "_OptionalListObjectsRequestRequestTypeDef",
    {
        "Delimiter": str,
        "EncodingType": Literal["url"],
        "Marker": str,
        "MaxKeys": int,
        "Prefix": str,
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class ListObjectsRequestRequestTypeDef(
    _RequiredListObjectsRequestRequestTypeDef, _OptionalListObjectsRequestRequestTypeDef
):
    pass

ListObjectsV2OutputTypeDef = TypedDict(
    "ListObjectsV2OutputTypeDef",
    {
        "IsTruncated": bool,
        "Contents": List["ObjectTypeDef"],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List["CommonPrefixTypeDef"],
        "EncodingType": Literal["url"],
        "KeyCount": int,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "StartAfter": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListObjectsV2RequestRequestTypeDef = TypedDict(
    "_RequiredListObjectsV2RequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalListObjectsV2RequestRequestTypeDef = TypedDict(
    "_OptionalListObjectsV2RequestRequestTypeDef",
    {
        "Delimiter": str,
        "EncodingType": Literal["url"],
        "MaxKeys": int,
        "Prefix": str,
        "ContinuationToken": str,
        "FetchOwner": bool,
        "StartAfter": str,
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class ListObjectsV2RequestRequestTypeDef(
    _RequiredListObjectsV2RequestRequestTypeDef, _OptionalListObjectsV2RequestRequestTypeDef
):
    pass

ListPartsOutputTypeDef = TypedDict(
    "ListPartsOutputTypeDef",
    {
        "AbortDate": datetime,
        "AbortRuleId": str,
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "PartNumberMarker": int,
        "NextPartNumberMarker": int,
        "MaxParts": int,
        "IsTruncated": bool,
        "Parts": List["PartTypeDef"],
        "Initiator": "InitiatorTypeDef",
        "Owner": "OwnerTypeDef",
        "StorageClass": StorageClassType,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPartsRequestRequestTypeDef = TypedDict(
    "_RequiredListPartsRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "UploadId": str,
    },
)
_OptionalListPartsRequestRequestTypeDef = TypedDict(
    "_OptionalListPartsRequestRequestTypeDef",
    {
        "MaxParts": int,
        "PartNumberMarker": int,
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class ListPartsRequestRequestTypeDef(
    _RequiredListPartsRequestRequestTypeDef, _OptionalListPartsRequestRequestTypeDef
):
    pass

_RequiredLoggingEnabledTypeDef = TypedDict(
    "_RequiredLoggingEnabledTypeDef",
    {
        "TargetBucket": str,
        "TargetPrefix": str,
    },
)
_OptionalLoggingEnabledTypeDef = TypedDict(
    "_OptionalLoggingEnabledTypeDef",
    {
        "TargetGrants": List["TargetGrantTypeDef"],
    },
    total=False,
)

class LoggingEnabledTypeDef(_RequiredLoggingEnabledTypeDef, _OptionalLoggingEnabledTypeDef):
    pass

MetadataEntryTypeDef = TypedDict(
    "MetadataEntryTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

MetricsAndOperatorTypeDef = TypedDict(
    "MetricsAndOperatorTypeDef",
    {
        "Prefix": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredMetricsConfigurationTypeDef = TypedDict(
    "_RequiredMetricsConfigurationTypeDef",
    {
        "Id": str,
    },
)
_OptionalMetricsConfigurationTypeDef = TypedDict(
    "_OptionalMetricsConfigurationTypeDef",
    {
        "Filter": "MetricsFilterTypeDef",
    },
    total=False,
)

class MetricsConfigurationTypeDef(
    _RequiredMetricsConfigurationTypeDef, _OptionalMetricsConfigurationTypeDef
):
    pass

MetricsFilterTypeDef = TypedDict(
    "MetricsFilterTypeDef",
    {
        "Prefix": str,
        "Tag": "TagTypeDef",
        "And": "MetricsAndOperatorTypeDef",
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

MultipartUploadPartRequestTypeDef = TypedDict(
    "MultipartUploadPartRequestTypeDef",
    {
        "part_number": str,
    },
)

MultipartUploadTypeDef = TypedDict(
    "MultipartUploadTypeDef",
    {
        "UploadId": str,
        "Key": str,
        "Initiated": datetime,
        "StorageClass": StorageClassType,
        "Owner": "OwnerTypeDef",
        "Initiator": "InitiatorTypeDef",
    },
    total=False,
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

NotificationConfigurationDeprecatedResponseMetadataTypeDef = TypedDict(
    "NotificationConfigurationDeprecatedResponseMetadataTypeDef",
    {
        "TopicConfiguration": "TopicConfigurationDeprecatedTypeDef",
        "QueueConfiguration": "QueueConfigurationDeprecatedTypeDef",
        "CloudFunctionConfiguration": "CloudFunctionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationConfigurationDeprecatedTypeDef = TypedDict(
    "NotificationConfigurationDeprecatedTypeDef",
    {
        "TopicConfiguration": "TopicConfigurationDeprecatedTypeDef",
        "QueueConfiguration": "QueueConfigurationDeprecatedTypeDef",
        "CloudFunctionConfiguration": "CloudFunctionConfigurationTypeDef",
    },
    total=False,
)

NotificationConfigurationFilterTypeDef = TypedDict(
    "NotificationConfigurationFilterTypeDef",
    {
        "Key": "S3KeyFilterTypeDef",
    },
    total=False,
)

NotificationConfigurationResponseMetadataTypeDef = TypedDict(
    "NotificationConfigurationResponseMetadataTypeDef",
    {
        "TopicConfigurations": List["TopicConfigurationTypeDef"],
        "QueueConfigurations": List["QueueConfigurationTypeDef"],
        "LambdaFunctionConfigurations": List["LambdaFunctionConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "TopicConfigurations": List["TopicConfigurationTypeDef"],
        "QueueConfigurations": List["QueueConfigurationTypeDef"],
        "LambdaFunctionConfigurations": List["LambdaFunctionConfigurationTypeDef"],
    },
    total=False,
)

_RequiredObjectCopyRequestTypeDef = TypedDict(
    "_RequiredObjectCopyRequestTypeDef",
    {
        "CopySource": "CopySourceTypeDef",
    },
)
_OptionalObjectCopyRequestTypeDef = TypedDict(
    "_OptionalObjectCopyRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "SourceClient": BaseClient,
        "Config": TransferConfig,
    },
    total=False,
)

class ObjectCopyRequestTypeDef(
    _RequiredObjectCopyRequestTypeDef, _OptionalObjectCopyRequestTypeDef
):
    pass

_RequiredObjectDownloadFileRequestTypeDef = TypedDict(
    "_RequiredObjectDownloadFileRequestTypeDef",
    {
        "Filename": str,
    },
)
_OptionalObjectDownloadFileRequestTypeDef = TypedDict(
    "_OptionalObjectDownloadFileRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)

class ObjectDownloadFileRequestTypeDef(
    _RequiredObjectDownloadFileRequestTypeDef, _OptionalObjectDownloadFileRequestTypeDef
):
    pass

_RequiredObjectDownloadFileobjRequestTypeDef = TypedDict(
    "_RequiredObjectDownloadFileobjRequestTypeDef",
    {
        "Fileobj": IO[Any],
    },
)
_OptionalObjectDownloadFileobjRequestTypeDef = TypedDict(
    "_OptionalObjectDownloadFileobjRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)

class ObjectDownloadFileobjRequestTypeDef(
    _RequiredObjectDownloadFileobjRequestTypeDef, _OptionalObjectDownloadFileobjRequestTypeDef
):
    pass

_RequiredObjectIdentifierTypeDef = TypedDict(
    "_RequiredObjectIdentifierTypeDef",
    {
        "Key": str,
    },
)
_OptionalObjectIdentifierTypeDef = TypedDict(
    "_OptionalObjectIdentifierTypeDef",
    {
        "VersionId": str,
    },
    total=False,
)

class ObjectIdentifierTypeDef(_RequiredObjectIdentifierTypeDef, _OptionalObjectIdentifierTypeDef):
    pass

ObjectLockConfigurationTypeDef = TypedDict(
    "ObjectLockConfigurationTypeDef",
    {
        "ObjectLockEnabled": Literal["Enabled"],
        "Rule": "ObjectLockRuleTypeDef",
    },
    total=False,
)

ObjectLockLegalHoldTypeDef = TypedDict(
    "ObjectLockLegalHoldTypeDef",
    {
        "Status": ObjectLockLegalHoldStatusType,
    },
    total=False,
)

ObjectLockRetentionTypeDef = TypedDict(
    "ObjectLockRetentionTypeDef",
    {
        "Mode": ObjectLockRetentionModeType,
        "RetainUntilDate": datetime,
    },
    total=False,
)

ObjectLockRuleTypeDef = TypedDict(
    "ObjectLockRuleTypeDef",
    {
        "DefaultRetention": "DefaultRetentionTypeDef",
    },
    total=False,
)

ObjectMultipartUploadRequestTypeDef = TypedDict(
    "ObjectMultipartUploadRequestTypeDef",
    {
        "id": str,
    },
)

ObjectSummaryMultipartUploadRequestTypeDef = TypedDict(
    "ObjectSummaryMultipartUploadRequestTypeDef",
    {
        "id": str,
    },
)

ObjectSummaryVersionRequestTypeDef = TypedDict(
    "ObjectSummaryVersionRequestTypeDef",
    {
        "id": str,
    },
)

ObjectTypeDef = TypedDict(
    "ObjectTypeDef",
    {
        "Key": str,
        "LastModified": datetime,
        "ETag": str,
        "Size": int,
        "StorageClass": ObjectStorageClassType,
        "Owner": "OwnerTypeDef",
    },
    total=False,
)

_RequiredObjectUploadFileRequestTypeDef = TypedDict(
    "_RequiredObjectUploadFileRequestTypeDef",
    {
        "Filename": str,
    },
)
_OptionalObjectUploadFileRequestTypeDef = TypedDict(
    "_OptionalObjectUploadFileRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)

class ObjectUploadFileRequestTypeDef(
    _RequiredObjectUploadFileRequestTypeDef, _OptionalObjectUploadFileRequestTypeDef
):
    pass

_RequiredObjectUploadFileobjRequestTypeDef = TypedDict(
    "_RequiredObjectUploadFileobjRequestTypeDef",
    {
        "Fileobj": IO[Any],
    },
)
_OptionalObjectUploadFileobjRequestTypeDef = TypedDict(
    "_OptionalObjectUploadFileobjRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)

class ObjectUploadFileobjRequestTypeDef(
    _RequiredObjectUploadFileobjRequestTypeDef, _OptionalObjectUploadFileobjRequestTypeDef
):
    pass

ObjectVersionRequestTypeDef = TypedDict(
    "ObjectVersionRequestTypeDef",
    {
        "id": str,
    },
)

ObjectVersionTypeDef = TypedDict(
    "ObjectVersionTypeDef",
    {
        "ETag": str,
        "Size": int,
        "StorageClass": Literal["STANDARD"],
        "Key": str,
        "VersionId": str,
        "IsLatest": bool,
        "LastModified": datetime,
        "Owner": "OwnerTypeDef",
    },
    total=False,
)

OutputLocationTypeDef = TypedDict(
    "OutputLocationTypeDef",
    {
        "S3": "S3LocationTypeDef",
    },
    total=False,
)

OutputSerializationTypeDef = TypedDict(
    "OutputSerializationTypeDef",
    {
        "CSV": "CSVOutputTypeDef",
        "JSON": "JSONOutputTypeDef",
    },
    total=False,
)

OwnerTypeDef = TypedDict(
    "OwnerTypeDef",
    {
        "DisplayName": str,
        "ID": str,
    },
    total=False,
)

OwnershipControlsRuleTypeDef = TypedDict(
    "OwnershipControlsRuleTypeDef",
    {
        "ObjectOwnership": ObjectOwnershipType,
    },
)

OwnershipControlsTypeDef = TypedDict(
    "OwnershipControlsTypeDef",
    {
        "Rules": List["OwnershipControlsRuleTypeDef"],
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

PartTypeDef = TypedDict(
    "PartTypeDef",
    {
        "PartNumber": int,
        "LastModified": datetime,
        "ETag": str,
        "Size": int,
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

ProgressEventTypeDef = TypedDict(
    "ProgressEventTypeDef",
    {
        "Details": "ProgressTypeDef",
    },
    total=False,
)

ProgressTypeDef = TypedDict(
    "ProgressTypeDef",
    {
        "BytesScanned": int,
        "BytesProcessed": int,
        "BytesReturned": int,
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

_RequiredPutBucketAccelerateConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketAccelerateConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "AccelerateConfiguration": "AccelerateConfigurationTypeDef",
    },
)
_OptionalPutBucketAccelerateConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketAccelerateConfigurationRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketAccelerateConfigurationRequestRequestTypeDef(
    _RequiredPutBucketAccelerateConfigurationRequestRequestTypeDef,
    _OptionalPutBucketAccelerateConfigurationRequestRequestTypeDef,
):
    pass

PutBucketAclRequestBucketAclTypeDef = TypedDict(
    "PutBucketAclRequestBucketAclTypeDef",
    {
        "ACL": BucketCannedACLType,
        "AccessControlPolicy": "AccessControlPolicyTypeDef",
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWrite": str,
        "GrantWriteACP": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredPutBucketAclRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketAclRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalPutBucketAclRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketAclRequestRequestTypeDef",
    {
        "ACL": BucketCannedACLType,
        "AccessControlPolicy": "AccessControlPolicyTypeDef",
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWrite": str,
        "GrantWriteACP": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketAclRequestRequestTypeDef(
    _RequiredPutBucketAclRequestRequestTypeDef, _OptionalPutBucketAclRequestRequestTypeDef
):
    pass

_RequiredPutBucketAnalyticsConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketAnalyticsConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
        "AnalyticsConfiguration": "AnalyticsConfigurationTypeDef",
    },
)
_OptionalPutBucketAnalyticsConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketAnalyticsConfigurationRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketAnalyticsConfigurationRequestRequestTypeDef(
    _RequiredPutBucketAnalyticsConfigurationRequestRequestTypeDef,
    _OptionalPutBucketAnalyticsConfigurationRequestRequestTypeDef,
):
    pass

_RequiredPutBucketCorsRequestBucketCorsTypeDef = TypedDict(
    "_RequiredPutBucketCorsRequestBucketCorsTypeDef",
    {
        "CORSConfiguration": "CORSConfigurationTypeDef",
    },
)
_OptionalPutBucketCorsRequestBucketCorsTypeDef = TypedDict(
    "_OptionalPutBucketCorsRequestBucketCorsTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketCorsRequestBucketCorsTypeDef(
    _RequiredPutBucketCorsRequestBucketCorsTypeDef, _OptionalPutBucketCorsRequestBucketCorsTypeDef
):
    pass

_RequiredPutBucketCorsRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketCorsRequestRequestTypeDef",
    {
        "Bucket": str,
        "CORSConfiguration": "CORSConfigurationTypeDef",
    },
)
_OptionalPutBucketCorsRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketCorsRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketCorsRequestRequestTypeDef(
    _RequiredPutBucketCorsRequestRequestTypeDef, _OptionalPutBucketCorsRequestRequestTypeDef
):
    pass

_RequiredPutBucketEncryptionRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketEncryptionRequestRequestTypeDef",
    {
        "Bucket": str,
        "ServerSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
    },
)
_OptionalPutBucketEncryptionRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketEncryptionRequestRequestTypeDef",
    {
        "ContentMD5": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketEncryptionRequestRequestTypeDef(
    _RequiredPutBucketEncryptionRequestRequestTypeDef,
    _OptionalPutBucketEncryptionRequestRequestTypeDef,
):
    pass

PutBucketIntelligentTieringConfigurationRequestRequestTypeDef = TypedDict(
    "PutBucketIntelligentTieringConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
        "IntelligentTieringConfiguration": "IntelligentTieringConfigurationTypeDef",
    },
)

_RequiredPutBucketInventoryConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketInventoryConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
        "InventoryConfiguration": "InventoryConfigurationTypeDef",
    },
)
_OptionalPutBucketInventoryConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketInventoryConfigurationRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketInventoryConfigurationRequestRequestTypeDef(
    _RequiredPutBucketInventoryConfigurationRequestRequestTypeDef,
    _OptionalPutBucketInventoryConfigurationRequestRequestTypeDef,
):
    pass

PutBucketLifecycleConfigurationRequestBucketLifecycleConfigurationTypeDef = TypedDict(
    "PutBucketLifecycleConfigurationRequestBucketLifecycleConfigurationTypeDef",
    {
        "LifecycleConfiguration": "BucketLifecycleConfigurationTypeDef",
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredPutBucketLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketLifecycleConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalPutBucketLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketLifecycleConfigurationRequestRequestTypeDef",
    {
        "LifecycleConfiguration": "BucketLifecycleConfigurationTypeDef",
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketLifecycleConfigurationRequestRequestTypeDef(
    _RequiredPutBucketLifecycleConfigurationRequestRequestTypeDef,
    _OptionalPutBucketLifecycleConfigurationRequestRequestTypeDef,
):
    pass

PutBucketLifecycleRequestBucketLifecycleTypeDef = TypedDict(
    "PutBucketLifecycleRequestBucketLifecycleTypeDef",
    {
        "LifecycleConfiguration": "LifecycleConfigurationTypeDef",
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredPutBucketLifecycleRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketLifecycleRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalPutBucketLifecycleRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketLifecycleRequestRequestTypeDef",
    {
        "LifecycleConfiguration": "LifecycleConfigurationTypeDef",
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketLifecycleRequestRequestTypeDef(
    _RequiredPutBucketLifecycleRequestRequestTypeDef,
    _OptionalPutBucketLifecycleRequestRequestTypeDef,
):
    pass

_RequiredPutBucketLoggingRequestBucketLoggingTypeDef = TypedDict(
    "_RequiredPutBucketLoggingRequestBucketLoggingTypeDef",
    {
        "BucketLoggingStatus": "BucketLoggingStatusTypeDef",
    },
)
_OptionalPutBucketLoggingRequestBucketLoggingTypeDef = TypedDict(
    "_OptionalPutBucketLoggingRequestBucketLoggingTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketLoggingRequestBucketLoggingTypeDef(
    _RequiredPutBucketLoggingRequestBucketLoggingTypeDef,
    _OptionalPutBucketLoggingRequestBucketLoggingTypeDef,
):
    pass

_RequiredPutBucketLoggingRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketLoggingRequestRequestTypeDef",
    {
        "Bucket": str,
        "BucketLoggingStatus": "BucketLoggingStatusTypeDef",
    },
)
_OptionalPutBucketLoggingRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketLoggingRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketLoggingRequestRequestTypeDef(
    _RequiredPutBucketLoggingRequestRequestTypeDef, _OptionalPutBucketLoggingRequestRequestTypeDef
):
    pass

_RequiredPutBucketMetricsConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketMetricsConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
        "MetricsConfiguration": "MetricsConfigurationTypeDef",
    },
)
_OptionalPutBucketMetricsConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketMetricsConfigurationRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketMetricsConfigurationRequestRequestTypeDef(
    _RequiredPutBucketMetricsConfigurationRequestRequestTypeDef,
    _OptionalPutBucketMetricsConfigurationRequestRequestTypeDef,
):
    pass

_RequiredPutBucketNotificationConfigurationRequestBucketNotificationTypeDef = TypedDict(
    "_RequiredPutBucketNotificationConfigurationRequestBucketNotificationTypeDef",
    {
        "NotificationConfiguration": "NotificationConfigurationTypeDef",
    },
)
_OptionalPutBucketNotificationConfigurationRequestBucketNotificationTypeDef = TypedDict(
    "_OptionalPutBucketNotificationConfigurationRequestBucketNotificationTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketNotificationConfigurationRequestBucketNotificationTypeDef(
    _RequiredPutBucketNotificationConfigurationRequestBucketNotificationTypeDef,
    _OptionalPutBucketNotificationConfigurationRequestBucketNotificationTypeDef,
):
    pass

_RequiredPutBucketNotificationConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketNotificationConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "NotificationConfiguration": "NotificationConfigurationTypeDef",
    },
)
_OptionalPutBucketNotificationConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketNotificationConfigurationRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketNotificationConfigurationRequestRequestTypeDef(
    _RequiredPutBucketNotificationConfigurationRequestRequestTypeDef,
    _OptionalPutBucketNotificationConfigurationRequestRequestTypeDef,
):
    pass

_RequiredPutBucketNotificationRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketNotificationRequestRequestTypeDef",
    {
        "Bucket": str,
        "NotificationConfiguration": "NotificationConfigurationDeprecatedTypeDef",
    },
)
_OptionalPutBucketNotificationRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketNotificationRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketNotificationRequestRequestTypeDef(
    _RequiredPutBucketNotificationRequestRequestTypeDef,
    _OptionalPutBucketNotificationRequestRequestTypeDef,
):
    pass

_RequiredPutBucketOwnershipControlsRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketOwnershipControlsRequestRequestTypeDef",
    {
        "Bucket": str,
        "OwnershipControls": "OwnershipControlsTypeDef",
    },
)
_OptionalPutBucketOwnershipControlsRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketOwnershipControlsRequestRequestTypeDef",
    {
        "ContentMD5": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketOwnershipControlsRequestRequestTypeDef(
    _RequiredPutBucketOwnershipControlsRequestRequestTypeDef,
    _OptionalPutBucketOwnershipControlsRequestRequestTypeDef,
):
    pass

_RequiredPutBucketPolicyRequestBucketPolicyTypeDef = TypedDict(
    "_RequiredPutBucketPolicyRequestBucketPolicyTypeDef",
    {
        "Policy": str,
    },
)
_OptionalPutBucketPolicyRequestBucketPolicyTypeDef = TypedDict(
    "_OptionalPutBucketPolicyRequestBucketPolicyTypeDef",
    {
        "ConfirmRemoveSelfBucketAccess": bool,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketPolicyRequestBucketPolicyTypeDef(
    _RequiredPutBucketPolicyRequestBucketPolicyTypeDef,
    _OptionalPutBucketPolicyRequestBucketPolicyTypeDef,
):
    pass

_RequiredPutBucketPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketPolicyRequestRequestTypeDef",
    {
        "Bucket": str,
        "Policy": str,
    },
)
_OptionalPutBucketPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketPolicyRequestRequestTypeDef",
    {
        "ConfirmRemoveSelfBucketAccess": bool,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketPolicyRequestRequestTypeDef(
    _RequiredPutBucketPolicyRequestRequestTypeDef, _OptionalPutBucketPolicyRequestRequestTypeDef
):
    pass

_RequiredPutBucketReplicationRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketReplicationRequestRequestTypeDef",
    {
        "Bucket": str,
        "ReplicationConfiguration": "ReplicationConfigurationTypeDef",
    },
)
_OptionalPutBucketReplicationRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketReplicationRequestRequestTypeDef",
    {
        "Token": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketReplicationRequestRequestTypeDef(
    _RequiredPutBucketReplicationRequestRequestTypeDef,
    _OptionalPutBucketReplicationRequestRequestTypeDef,
):
    pass

_RequiredPutBucketRequestPaymentRequestBucketRequestPaymentTypeDef = TypedDict(
    "_RequiredPutBucketRequestPaymentRequestBucketRequestPaymentTypeDef",
    {
        "RequestPaymentConfiguration": "RequestPaymentConfigurationTypeDef",
    },
)
_OptionalPutBucketRequestPaymentRequestBucketRequestPaymentTypeDef = TypedDict(
    "_OptionalPutBucketRequestPaymentRequestBucketRequestPaymentTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketRequestPaymentRequestBucketRequestPaymentTypeDef(
    _RequiredPutBucketRequestPaymentRequestBucketRequestPaymentTypeDef,
    _OptionalPutBucketRequestPaymentRequestBucketRequestPaymentTypeDef,
):
    pass

_RequiredPutBucketRequestPaymentRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketRequestPaymentRequestRequestTypeDef",
    {
        "Bucket": str,
        "RequestPaymentConfiguration": "RequestPaymentConfigurationTypeDef",
    },
)
_OptionalPutBucketRequestPaymentRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketRequestPaymentRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketRequestPaymentRequestRequestTypeDef(
    _RequiredPutBucketRequestPaymentRequestRequestTypeDef,
    _OptionalPutBucketRequestPaymentRequestRequestTypeDef,
):
    pass

_RequiredPutBucketTaggingRequestBucketTaggingTypeDef = TypedDict(
    "_RequiredPutBucketTaggingRequestBucketTaggingTypeDef",
    {
        "Tagging": "TaggingTypeDef",
    },
)
_OptionalPutBucketTaggingRequestBucketTaggingTypeDef = TypedDict(
    "_OptionalPutBucketTaggingRequestBucketTaggingTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketTaggingRequestBucketTaggingTypeDef(
    _RequiredPutBucketTaggingRequestBucketTaggingTypeDef,
    _OptionalPutBucketTaggingRequestBucketTaggingTypeDef,
):
    pass

_RequiredPutBucketTaggingRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketTaggingRequestRequestTypeDef",
    {
        "Bucket": str,
        "Tagging": "TaggingTypeDef",
    },
)
_OptionalPutBucketTaggingRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketTaggingRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketTaggingRequestRequestTypeDef(
    _RequiredPutBucketTaggingRequestRequestTypeDef, _OptionalPutBucketTaggingRequestRequestTypeDef
):
    pass

_RequiredPutBucketVersioningRequestBucketVersioningTypeDef = TypedDict(
    "_RequiredPutBucketVersioningRequestBucketVersioningTypeDef",
    {
        "VersioningConfiguration": "VersioningConfigurationTypeDef",
    },
)
_OptionalPutBucketVersioningRequestBucketVersioningTypeDef = TypedDict(
    "_OptionalPutBucketVersioningRequestBucketVersioningTypeDef",
    {
        "MFA": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketVersioningRequestBucketVersioningTypeDef(
    _RequiredPutBucketVersioningRequestBucketVersioningTypeDef,
    _OptionalPutBucketVersioningRequestBucketVersioningTypeDef,
):
    pass

_RequiredPutBucketVersioningRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketVersioningRequestRequestTypeDef",
    {
        "Bucket": str,
        "VersioningConfiguration": "VersioningConfigurationTypeDef",
    },
)
_OptionalPutBucketVersioningRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketVersioningRequestRequestTypeDef",
    {
        "MFA": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketVersioningRequestRequestTypeDef(
    _RequiredPutBucketVersioningRequestRequestTypeDef,
    _OptionalPutBucketVersioningRequestRequestTypeDef,
):
    pass

_RequiredPutBucketWebsiteRequestBucketWebsiteTypeDef = TypedDict(
    "_RequiredPutBucketWebsiteRequestBucketWebsiteTypeDef",
    {
        "WebsiteConfiguration": "WebsiteConfigurationTypeDef",
    },
)
_OptionalPutBucketWebsiteRequestBucketWebsiteTypeDef = TypedDict(
    "_OptionalPutBucketWebsiteRequestBucketWebsiteTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketWebsiteRequestBucketWebsiteTypeDef(
    _RequiredPutBucketWebsiteRequestBucketWebsiteTypeDef,
    _OptionalPutBucketWebsiteRequestBucketWebsiteTypeDef,
):
    pass

_RequiredPutBucketWebsiteRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketWebsiteRequestRequestTypeDef",
    {
        "Bucket": str,
        "WebsiteConfiguration": "WebsiteConfigurationTypeDef",
    },
)
_OptionalPutBucketWebsiteRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketWebsiteRequestRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutBucketWebsiteRequestRequestTypeDef(
    _RequiredPutBucketWebsiteRequestRequestTypeDef, _OptionalPutBucketWebsiteRequestRequestTypeDef
):
    pass

PutObjectAclOutputTypeDef = TypedDict(
    "PutObjectAclOutputTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutObjectAclRequestObjectAclTypeDef = TypedDict(
    "PutObjectAclRequestObjectAclTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "AccessControlPolicy": "AccessControlPolicyTypeDef",
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWrite": str,
        "GrantWriteACP": str,
        "RequestPayer": Literal["requester"],
        "VersionId": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredPutObjectAclRequestRequestTypeDef = TypedDict(
    "_RequiredPutObjectAclRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalPutObjectAclRequestRequestTypeDef = TypedDict(
    "_OptionalPutObjectAclRequestRequestTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "AccessControlPolicy": "AccessControlPolicyTypeDef",
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWrite": str,
        "GrantWriteACP": str,
        "RequestPayer": Literal["requester"],
        "VersionId": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutObjectAclRequestRequestTypeDef(
    _RequiredPutObjectAclRequestRequestTypeDef, _OptionalPutObjectAclRequestRequestTypeDef
):
    pass

PutObjectLegalHoldOutputTypeDef = TypedDict(
    "PutObjectLegalHoldOutputTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutObjectLegalHoldRequestRequestTypeDef = TypedDict(
    "_RequiredPutObjectLegalHoldRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalPutObjectLegalHoldRequestRequestTypeDef = TypedDict(
    "_OptionalPutObjectLegalHoldRequestRequestTypeDef",
    {
        "LegalHold": "ObjectLockLegalHoldTypeDef",
        "RequestPayer": Literal["requester"],
        "VersionId": str,
        "ContentMD5": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutObjectLegalHoldRequestRequestTypeDef(
    _RequiredPutObjectLegalHoldRequestRequestTypeDef,
    _OptionalPutObjectLegalHoldRequestRequestTypeDef,
):
    pass

PutObjectLockConfigurationOutputTypeDef = TypedDict(
    "PutObjectLockConfigurationOutputTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutObjectLockConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutObjectLockConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalPutObjectLockConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutObjectLockConfigurationRequestRequestTypeDef",
    {
        "ObjectLockConfiguration": "ObjectLockConfigurationTypeDef",
        "RequestPayer": Literal["requester"],
        "Token": str,
        "ContentMD5": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutObjectLockConfigurationRequestRequestTypeDef(
    _RequiredPutObjectLockConfigurationRequestRequestTypeDef,
    _OptionalPutObjectLockConfigurationRequestRequestTypeDef,
):
    pass

PutObjectOutputTypeDef = TypedDict(
    "PutObjectOutputTypeDef",
    {
        "Expiration": str,
        "ETag": str,
        "ServerSideEncryption": ServerSideEncryptionType,
        "VersionId": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutObjectRequestBucketTypeDef = TypedDict(
    "_RequiredPutObjectRequestBucketTypeDef",
    {
        "Key": str,
    },
)
_OptionalPutObjectRequestBucketTypeDef = TypedDict(
    "_OptionalPutObjectRequestBucketTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentLength": int,
        "ContentMD5": str,
        "ContentType": str,
        "Expires": Union[datetime, str],
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWriteACP": str,
        "Metadata": Dict[str, str],
        "ServerSideEncryption": ServerSideEncryptionType,
        "StorageClass": StorageClassType,
        "WebsiteRedirectLocation": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestPayer": Literal["requester"],
        "Tagging": str,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutObjectRequestBucketTypeDef(
    _RequiredPutObjectRequestBucketTypeDef, _OptionalPutObjectRequestBucketTypeDef
):
    pass

PutObjectRequestObjectSummaryTypeDef = TypedDict(
    "PutObjectRequestObjectSummaryTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentLength": int,
        "ContentMD5": str,
        "ContentType": str,
        "Expires": Union[datetime, str],
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWriteACP": str,
        "Metadata": Dict[str, str],
        "ServerSideEncryption": ServerSideEncryptionType,
        "StorageClass": StorageClassType,
        "WebsiteRedirectLocation": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestPayer": Literal["requester"],
        "Tagging": str,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

PutObjectRequestObjectTypeDef = TypedDict(
    "PutObjectRequestObjectTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentLength": int,
        "ContentMD5": str,
        "ContentType": str,
        "Expires": Union[datetime, str],
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWriteACP": str,
        "Metadata": Dict[str, str],
        "ServerSideEncryption": ServerSideEncryptionType,
        "StorageClass": StorageClassType,
        "WebsiteRedirectLocation": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestPayer": Literal["requester"],
        "Tagging": str,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredPutObjectRequestRequestTypeDef = TypedDict(
    "_RequiredPutObjectRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalPutObjectRequestRequestTypeDef = TypedDict(
    "_OptionalPutObjectRequestRequestTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentLength": int,
        "ContentMD5": str,
        "ContentType": str,
        "Expires": Union[datetime, str],
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWriteACP": str,
        "Metadata": Dict[str, str],
        "ServerSideEncryption": ServerSideEncryptionType,
        "StorageClass": StorageClassType,
        "WebsiteRedirectLocation": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestPayer": Literal["requester"],
        "Tagging": str,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutObjectRequestRequestTypeDef(
    _RequiredPutObjectRequestRequestTypeDef, _OptionalPutObjectRequestRequestTypeDef
):
    pass

PutObjectRetentionOutputTypeDef = TypedDict(
    "PutObjectRetentionOutputTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutObjectRetentionRequestRequestTypeDef = TypedDict(
    "_RequiredPutObjectRetentionRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalPutObjectRetentionRequestRequestTypeDef = TypedDict(
    "_OptionalPutObjectRetentionRequestRequestTypeDef",
    {
        "Retention": "ObjectLockRetentionTypeDef",
        "RequestPayer": Literal["requester"],
        "VersionId": str,
        "BypassGovernanceRetention": bool,
        "ContentMD5": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutObjectRetentionRequestRequestTypeDef(
    _RequiredPutObjectRetentionRequestRequestTypeDef,
    _OptionalPutObjectRetentionRequestRequestTypeDef,
):
    pass

PutObjectTaggingOutputTypeDef = TypedDict(
    "PutObjectTaggingOutputTypeDef",
    {
        "VersionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutObjectTaggingRequestRequestTypeDef = TypedDict(
    "_RequiredPutObjectTaggingRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "Tagging": "TaggingTypeDef",
    },
)
_OptionalPutObjectTaggingRequestRequestTypeDef = TypedDict(
    "_OptionalPutObjectTaggingRequestRequestTypeDef",
    {
        "VersionId": str,
        "ContentMD5": str,
        "ExpectedBucketOwner": str,
        "RequestPayer": Literal["requester"],
    },
    total=False,
)

class PutObjectTaggingRequestRequestTypeDef(
    _RequiredPutObjectTaggingRequestRequestTypeDef, _OptionalPutObjectTaggingRequestRequestTypeDef
):
    pass

_RequiredPutPublicAccessBlockRequestRequestTypeDef = TypedDict(
    "_RequiredPutPublicAccessBlockRequestRequestTypeDef",
    {
        "Bucket": str,
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
    },
)
_OptionalPutPublicAccessBlockRequestRequestTypeDef = TypedDict(
    "_OptionalPutPublicAccessBlockRequestRequestTypeDef",
    {
        "ContentMD5": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class PutPublicAccessBlockRequestRequestTypeDef(
    _RequiredPutPublicAccessBlockRequestRequestTypeDef,
    _OptionalPutPublicAccessBlockRequestRequestTypeDef,
):
    pass

QueueConfigurationDeprecatedTypeDef = TypedDict(
    "QueueConfigurationDeprecatedTypeDef",
    {
        "Id": str,
        "Event": EventType,
        "Events": List[EventType],
        "Queue": str,
    },
    total=False,
)

_RequiredQueueConfigurationTypeDef = TypedDict(
    "_RequiredQueueConfigurationTypeDef",
    {
        "QueueArn": str,
        "Events": List[EventType],
    },
)
_OptionalQueueConfigurationTypeDef = TypedDict(
    "_OptionalQueueConfigurationTypeDef",
    {
        "Id": str,
        "Filter": "NotificationConfigurationFilterTypeDef",
    },
    total=False,
)

class QueueConfigurationTypeDef(
    _RequiredQueueConfigurationTypeDef, _OptionalQueueConfigurationTypeDef
):
    pass

RecordsEventTypeDef = TypedDict(
    "RecordsEventTypeDef",
    {
        "Payload": bytes,
    },
    total=False,
)

_RequiredRedirectAllRequestsToTypeDef = TypedDict(
    "_RequiredRedirectAllRequestsToTypeDef",
    {
        "HostName": str,
    },
)
_OptionalRedirectAllRequestsToTypeDef = TypedDict(
    "_OptionalRedirectAllRequestsToTypeDef",
    {
        "Protocol": ProtocolType,
    },
    total=False,
)

class RedirectAllRequestsToTypeDef(
    _RequiredRedirectAllRequestsToTypeDef, _OptionalRedirectAllRequestsToTypeDef
):
    pass

RedirectTypeDef = TypedDict(
    "RedirectTypeDef",
    {
        "HostName": str,
        "HttpRedirectCode": str,
        "Protocol": ProtocolType,
        "ReplaceKeyPrefixWith": str,
        "ReplaceKeyWith": str,
    },
    total=False,
)

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
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ReplicationRuleFilterTypeDef = TypedDict(
    "ReplicationRuleFilterTypeDef",
    {
        "Prefix": str,
        "Tag": "TagTypeDef",
        "And": "ReplicationRuleAndOperatorTypeDef",
    },
    total=False,
)

_RequiredReplicationRuleTypeDef = TypedDict(
    "_RequiredReplicationRuleTypeDef",
    {
        "Status": ReplicationRuleStatusType,
        "Destination": "DestinationTypeDef",
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

RequestPaymentConfigurationTypeDef = TypedDict(
    "RequestPaymentConfigurationTypeDef",
    {
        "Payer": PayerType,
    },
)

RequestProgressTypeDef = TypedDict(
    "RequestProgressTypeDef",
    {
        "Enabled": bool,
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

RestoreObjectOutputTypeDef = TypedDict(
    "RestoreObjectOutputTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "RestoreOutputPath": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreObjectRequestObjectSummaryTypeDef = TypedDict(
    "RestoreObjectRequestObjectSummaryTypeDef",
    {
        "VersionId": str,
        "RestoreRequest": "RestoreRequestTypeDef",
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

RestoreObjectRequestObjectTypeDef = TypedDict(
    "RestoreObjectRequestObjectTypeDef",
    {
        "VersionId": str,
        "RestoreRequest": "RestoreRequestTypeDef",
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredRestoreObjectRequestRequestTypeDef = TypedDict(
    "_RequiredRestoreObjectRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalRestoreObjectRequestRequestTypeDef = TypedDict(
    "_OptionalRestoreObjectRequestRequestTypeDef",
    {
        "VersionId": str,
        "RestoreRequest": "RestoreRequestTypeDef",
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class RestoreObjectRequestRequestTypeDef(
    _RequiredRestoreObjectRequestRequestTypeDef, _OptionalRestoreObjectRequestRequestTypeDef
):
    pass

RestoreRequestTypeDef = TypedDict(
    "RestoreRequestTypeDef",
    {
        "Days": int,
        "GlacierJobParameters": "GlacierJobParametersTypeDef",
        "Type": Literal["SELECT"],
        "Tier": TierType,
        "Description": str,
        "SelectParameters": "SelectParametersTypeDef",
        "OutputLocation": "OutputLocationTypeDef",
    },
    total=False,
)

_RequiredRoutingRuleTypeDef = TypedDict(
    "_RequiredRoutingRuleTypeDef",
    {
        "Redirect": "RedirectTypeDef",
    },
)
_OptionalRoutingRuleTypeDef = TypedDict(
    "_OptionalRoutingRuleTypeDef",
    {
        "Condition": "ConditionTypeDef",
    },
    total=False,
)

class RoutingRuleTypeDef(_RequiredRoutingRuleTypeDef, _OptionalRoutingRuleTypeDef):
    pass

_RequiredRuleTypeDef = TypedDict(
    "_RequiredRuleTypeDef",
    {
        "Prefix": str,
        "Status": ExpirationStatusType,
    },
)
_OptionalRuleTypeDef = TypedDict(
    "_OptionalRuleTypeDef",
    {
        "Expiration": "LifecycleExpirationTypeDef",
        "ID": str,
        "Transition": "TransitionTypeDef",
        "NoncurrentVersionTransition": "NoncurrentVersionTransitionTypeDef",
        "NoncurrentVersionExpiration": "NoncurrentVersionExpirationTypeDef",
        "AbortIncompleteMultipartUpload": "AbortIncompleteMultipartUploadTypeDef",
    },
    total=False,
)

class RuleTypeDef(_RequiredRuleTypeDef, _OptionalRuleTypeDef):
    pass

S3KeyFilterTypeDef = TypedDict(
    "S3KeyFilterTypeDef",
    {
        "FilterRules": List["FilterRuleTypeDef"],
    },
    total=False,
)

_RequiredS3LocationTypeDef = TypedDict(
    "_RequiredS3LocationTypeDef",
    {
        "BucketName": str,
        "Prefix": str,
    },
)
_OptionalS3LocationTypeDef = TypedDict(
    "_OptionalS3LocationTypeDef",
    {
        "Encryption": "EncryptionTypeDef",
        "CannedACL": ObjectCannedACLType,
        "AccessControlList": List["GrantTypeDef"],
        "Tagging": "TaggingTypeDef",
        "UserMetadata": List["MetadataEntryTypeDef"],
        "StorageClass": StorageClassType,
    },
    total=False,
)

class S3LocationTypeDef(_RequiredS3LocationTypeDef, _OptionalS3LocationTypeDef):
    pass

SSEKMSTypeDef = TypedDict(
    "SSEKMSTypeDef",
    {
        "KeyId": str,
    },
)

ScanRangeTypeDef = TypedDict(
    "ScanRangeTypeDef",
    {
        "Start": int,
        "End": int,
    },
    total=False,
)

SelectObjectContentEventStreamTypeDef = TypedDict(
    "SelectObjectContentEventStreamTypeDef",
    {
        "Records": "RecordsEventTypeDef",
        "Stats": "StatsEventTypeDef",
        "Progress": "ProgressEventTypeDef",
        "Cont": Dict[str, Any],
        "End": Dict[str, Any],
    },
    total=False,
)

SelectObjectContentOutputTypeDef = TypedDict(
    "SelectObjectContentOutputTypeDef",
    {
        "Payload": "SelectObjectContentEventStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSelectObjectContentRequestRequestTypeDef = TypedDict(
    "_RequiredSelectObjectContentRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "Expression": str,
        "ExpressionType": Literal["SQL"],
        "InputSerialization": "InputSerializationTypeDef",
        "OutputSerialization": "OutputSerializationTypeDef",
    },
)
_OptionalSelectObjectContentRequestRequestTypeDef = TypedDict(
    "_OptionalSelectObjectContentRequestRequestTypeDef",
    {
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "RequestProgress": "RequestProgressTypeDef",
        "ScanRange": "ScanRangeTypeDef",
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class SelectObjectContentRequestRequestTypeDef(
    _RequiredSelectObjectContentRequestRequestTypeDef,
    _OptionalSelectObjectContentRequestRequestTypeDef,
):
    pass

SelectParametersTypeDef = TypedDict(
    "SelectParametersTypeDef",
    {
        "InputSerialization": "InputSerializationTypeDef",
        "ExpressionType": Literal["SQL"],
        "Expression": str,
        "OutputSerialization": "OutputSerializationTypeDef",
    },
)

_RequiredServerSideEncryptionByDefaultTypeDef = TypedDict(
    "_RequiredServerSideEncryptionByDefaultTypeDef",
    {
        "SSEAlgorithm": ServerSideEncryptionType,
    },
)
_OptionalServerSideEncryptionByDefaultTypeDef = TypedDict(
    "_OptionalServerSideEncryptionByDefaultTypeDef",
    {
        "KMSMasterKeyID": str,
    },
    total=False,
)

class ServerSideEncryptionByDefaultTypeDef(
    _RequiredServerSideEncryptionByDefaultTypeDef, _OptionalServerSideEncryptionByDefaultTypeDef
):
    pass

ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef",
    {
        "Rules": List["ServerSideEncryptionRuleTypeDef"],
    },
)

ServerSideEncryptionRuleTypeDef = TypedDict(
    "ServerSideEncryptionRuleTypeDef",
    {
        "ApplyServerSideEncryptionByDefault": "ServerSideEncryptionByDefaultTypeDef",
        "BucketKeyEnabled": bool,
    },
    total=False,
)

ServiceResourceBucketAclRequestTypeDef = TypedDict(
    "ServiceResourceBucketAclRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketCorsRequestTypeDef = TypedDict(
    "ServiceResourceBucketCorsRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketLifecycleConfigurationRequestTypeDef = TypedDict(
    "ServiceResourceBucketLifecycleConfigurationRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketLifecycleRequestTypeDef = TypedDict(
    "ServiceResourceBucketLifecycleRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketLoggingRequestTypeDef = TypedDict(
    "ServiceResourceBucketLoggingRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketNotificationRequestTypeDef = TypedDict(
    "ServiceResourceBucketNotificationRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketPolicyRequestTypeDef = TypedDict(
    "ServiceResourceBucketPolicyRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketRequestPaymentRequestTypeDef = TypedDict(
    "ServiceResourceBucketRequestPaymentRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketRequestTypeDef = TypedDict(
    "ServiceResourceBucketRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceBucketTaggingRequestTypeDef = TypedDict(
    "ServiceResourceBucketTaggingRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketVersioningRequestTypeDef = TypedDict(
    "ServiceResourceBucketVersioningRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketWebsiteRequestTypeDef = TypedDict(
    "ServiceResourceBucketWebsiteRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceMultipartUploadPartRequestTypeDef = TypedDict(
    "ServiceResourceMultipartUploadPartRequestTypeDef",
    {
        "bucket_name": str,
        "object_key": str,
        "multipart_upload_id": str,
        "part_number": str,
    },
)

ServiceResourceMultipartUploadRequestTypeDef = TypedDict(
    "ServiceResourceMultipartUploadRequestTypeDef",
    {
        "bucket_name": str,
        "object_key": str,
        "id": str,
    },
)

ServiceResourceObjectAclRequestTypeDef = TypedDict(
    "ServiceResourceObjectAclRequestTypeDef",
    {
        "bucket_name": str,
        "object_key": str,
    },
)

ServiceResourceObjectRequestTypeDef = TypedDict(
    "ServiceResourceObjectRequestTypeDef",
    {
        "bucket_name": str,
        "key": str,
    },
)

ServiceResourceObjectSummaryRequestTypeDef = TypedDict(
    "ServiceResourceObjectSummaryRequestTypeDef",
    {
        "bucket_name": str,
        "key": str,
    },
)

ServiceResourceObjectVersionRequestTypeDef = TypedDict(
    "ServiceResourceObjectVersionRequestTypeDef",
    {
        "bucket_name": str,
        "object_key": str,
        "id": str,
    },
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

StatsEventTypeDef = TypedDict(
    "StatsEventTypeDef",
    {
        "Details": "StatsTypeDef",
    },
    total=False,
)

StatsTypeDef = TypedDict(
    "StatsTypeDef",
    {
        "BytesScanned": int,
        "BytesProcessed": int,
        "BytesReturned": int,
    },
    total=False,
)

StorageClassAnalysisDataExportTypeDef = TypedDict(
    "StorageClassAnalysisDataExportTypeDef",
    {
        "OutputSchemaVersion": Literal["V_1"],
        "Destination": "AnalyticsExportDestinationTypeDef",
    },
)

StorageClassAnalysisTypeDef = TypedDict(
    "StorageClassAnalysisTypeDef",
    {
        "DataExport": "StorageClassAnalysisDataExportTypeDef",
    },
    total=False,
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
        "TagSet": List["TagTypeDef"],
    },
)

TargetGrantTypeDef = TypedDict(
    "TargetGrantTypeDef",
    {
        "Grantee": "GranteeTypeDef",
        "Permission": BucketLogsPermissionType,
    },
    total=False,
)

TieringTypeDef = TypedDict(
    "TieringTypeDef",
    {
        "Days": int,
        "AccessTier": IntelligentTieringAccessTierType,
    },
)

TopicConfigurationDeprecatedTypeDef = TypedDict(
    "TopicConfigurationDeprecatedTypeDef",
    {
        "Id": str,
        "Events": List[EventType],
        "Event": EventType,
        "Topic": str,
    },
    total=False,
)

_RequiredTopicConfigurationTypeDef = TypedDict(
    "_RequiredTopicConfigurationTypeDef",
    {
        "TopicArn": str,
        "Events": List[EventType],
    },
)
_OptionalTopicConfigurationTypeDef = TypedDict(
    "_OptionalTopicConfigurationTypeDef",
    {
        "Id": str,
        "Filter": "NotificationConfigurationFilterTypeDef",
    },
    total=False,
)

class TopicConfigurationTypeDef(
    _RequiredTopicConfigurationTypeDef, _OptionalTopicConfigurationTypeDef
):
    pass

TransitionTypeDef = TypedDict(
    "TransitionTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": TransitionStorageClassType,
    },
    total=False,
)

UploadPartCopyOutputTypeDef = TypedDict(
    "UploadPartCopyOutputTypeDef",
    {
        "CopySourceVersionId": str,
        "CopyPartResult": "CopyPartResultTypeDef",
        "ServerSideEncryption": ServerSideEncryptionType,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUploadPartCopyRequestMultipartUploadPartTypeDef = TypedDict(
    "_RequiredUploadPartCopyRequestMultipartUploadPartTypeDef",
    {
        "CopySource": str,
    },
)
_OptionalUploadPartCopyRequestMultipartUploadPartTypeDef = TypedDict(
    "_OptionalUploadPartCopyRequestMultipartUploadPartTypeDef",
    {
        "CopySourceIfMatch": str,
        "CopySourceIfModifiedSince": Union[datetime, str],
        "CopySourceIfNoneMatch": str,
        "CopySourceIfUnmodifiedSince": Union[datetime, str],
        "CopySourceRange": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "CopySourceSSECustomerAlgorithm": str,
        "CopySourceSSECustomerKey": str,
        "CopySourceSSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
        "ExpectedSourceBucketOwner": str,
    },
    total=False,
)

class UploadPartCopyRequestMultipartUploadPartTypeDef(
    _RequiredUploadPartCopyRequestMultipartUploadPartTypeDef,
    _OptionalUploadPartCopyRequestMultipartUploadPartTypeDef,
):
    pass

_RequiredUploadPartCopyRequestRequestTypeDef = TypedDict(
    "_RequiredUploadPartCopyRequestRequestTypeDef",
    {
        "Bucket": str,
        "CopySource": Union[str, "CopySourceTypeDef"],
        "Key": str,
        "PartNumber": int,
        "UploadId": str,
    },
)
_OptionalUploadPartCopyRequestRequestTypeDef = TypedDict(
    "_OptionalUploadPartCopyRequestRequestTypeDef",
    {
        "CopySourceIfMatch": str,
        "CopySourceIfModifiedSince": Union[datetime, str],
        "CopySourceIfNoneMatch": str,
        "CopySourceIfUnmodifiedSince": Union[datetime, str],
        "CopySourceRange": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "CopySourceSSECustomerAlgorithm": str,
        "CopySourceSSECustomerKey": str,
        "CopySourceSSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
        "ExpectedSourceBucketOwner": str,
    },
    total=False,
)

class UploadPartCopyRequestRequestTypeDef(
    _RequiredUploadPartCopyRequestRequestTypeDef, _OptionalUploadPartCopyRequestRequestTypeDef
):
    pass

UploadPartOutputTypeDef = TypedDict(
    "UploadPartOutputTypeDef",
    {
        "ServerSideEncryption": ServerSideEncryptionType,
        "ETag": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UploadPartRequestMultipartUploadPartTypeDef = TypedDict(
    "UploadPartRequestMultipartUploadPartTypeDef",
    {
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "ContentLength": int,
        "ContentMD5": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredUploadPartRequestRequestTypeDef = TypedDict(
    "_RequiredUploadPartRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "PartNumber": int,
        "UploadId": str,
    },
)
_OptionalUploadPartRequestRequestTypeDef = TypedDict(
    "_OptionalUploadPartRequestRequestTypeDef",
    {
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "ContentLength": int,
        "ContentMD5": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

class UploadPartRequestRequestTypeDef(
    _RequiredUploadPartRequestRequestTypeDef, _OptionalUploadPartRequestRequestTypeDef
):
    pass

VersioningConfigurationTypeDef = TypedDict(
    "VersioningConfigurationTypeDef",
    {
        "MFADelete": MFADeleteType,
        "Status": BucketVersioningStatusType,
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

WebsiteConfigurationTypeDef = TypedDict(
    "WebsiteConfigurationTypeDef",
    {
        "ErrorDocument": "ErrorDocumentTypeDef",
        "IndexDocument": "IndexDocumentTypeDef",
        "RedirectAllRequestsTo": "RedirectAllRequestsToTypeDef",
        "RoutingRules": List["RoutingRuleTypeDef"],
    },
    total=False,
)

_RequiredWriteGetObjectResponseRequestRequestTypeDef = TypedDict(
    "_RequiredWriteGetObjectResponseRequestRequestTypeDef",
    {
        "RequestRoute": str,
        "RequestToken": str,
    },
)
_OptionalWriteGetObjectResponseRequestRequestTypeDef = TypedDict(
    "_OptionalWriteGetObjectResponseRequestRequestTypeDef",
    {
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "StatusCode": int,
        "ErrorCode": str,
        "ErrorMessage": str,
        "AcceptRanges": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentLength": int,
        "ContentRange": str,
        "ContentType": str,
        "DeleteMarker": bool,
        "ETag": str,
        "Expires": Union[datetime, str],
        "Expiration": str,
        "LastModified": Union[datetime, str],
        "MissingMeta": int,
        "Metadata": Dict[str, str],
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "PartsCount": int,
        "ReplicationStatus": ReplicationStatusType,
        "RequestCharged": Literal["requester"],
        "Restore": str,
        "ServerSideEncryption": ServerSideEncryptionType,
        "SSECustomerAlgorithm": str,
        "SSEKMSKeyId": str,
        "SSECustomerKeyMD5": str,
        "StorageClass": StorageClassType,
        "TagCount": int,
        "VersionId": str,
        "BucketKeyEnabled": bool,
    },
    total=False,
)

class WriteGetObjectResponseRequestRequestTypeDef(
    _RequiredWriteGetObjectResponseRequestRequestTypeDef,
    _OptionalWriteGetObjectResponseRequestRequestTypeDef,
):
    pass
