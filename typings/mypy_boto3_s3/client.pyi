# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for s3 service client

Usage::

    ```python
    import boto3
    from mypy_boto3_s3 import S3Client

    client: S3Client = boto3.client("s3")
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Callable, Dict, List, Type, Union, overload

from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient, ClientMeta

from mypy_boto3_s3.paginator import (
    ListMultipartUploadsPaginator,
    ListObjectsPaginator,
    ListObjectsV2Paginator,
    ListObjectVersionsPaginator,
    ListPartsPaginator,
)
from mypy_boto3_s3.type_defs import (
    AbortMultipartUploadOutputTypeDef,
    AccelerateConfigurationTypeDef,
    AccessControlPolicyTypeDef,
    AnalyticsConfigurationTypeDef,
    BucketLifecycleConfigurationTypeDef,
    BucketLoggingStatusTypeDef,
    CompletedMultipartUploadTypeDef,
    CompleteMultipartUploadOutputTypeDef,
    CopyObjectOutputTypeDef,
    CopySourceTypeDef,
    CORSConfigurationTypeDef,
    CreateBucketConfigurationTypeDef,
    CreateBucketOutputTypeDef,
    CreateMultipartUploadOutputTypeDef,
    DeleteObjectOutputTypeDef,
    DeleteObjectsOutputTypeDef,
    DeleteObjectTaggingOutputTypeDef,
    DeleteTypeDef,
    GetBucketAccelerateConfigurationOutputTypeDef,
    GetBucketAclOutputTypeDef,
    GetBucketAnalyticsConfigurationOutputTypeDef,
    GetBucketCorsOutputTypeDef,
    GetBucketEncryptionOutputTypeDef,
    GetBucketIntelligentTieringConfigurationOutputTypeDef,
    GetBucketInventoryConfigurationOutputTypeDef,
    GetBucketLifecycleConfigurationOutputTypeDef,
    GetBucketLifecycleOutputTypeDef,
    GetBucketLocationOutputTypeDef,
    GetBucketLoggingOutputTypeDef,
    GetBucketMetricsConfigurationOutputTypeDef,
    GetBucketOwnershipControlsOutputTypeDef,
    GetBucketPolicyOutputTypeDef,
    GetBucketPolicyStatusOutputTypeDef,
    GetBucketReplicationOutputTypeDef,
    GetBucketRequestPaymentOutputTypeDef,
    GetBucketTaggingOutputTypeDef,
    GetBucketVersioningOutputTypeDef,
    GetBucketWebsiteOutputTypeDef,
    GetObjectAclOutputTypeDef,
    GetObjectLegalHoldOutputTypeDef,
    GetObjectLockConfigurationOutputTypeDef,
    GetObjectOutputTypeDef,
    GetObjectRetentionOutputTypeDef,
    GetObjectTaggingOutputTypeDef,
    GetObjectTorrentOutputTypeDef,
    GetPublicAccessBlockOutputTypeDef,
    HeadObjectOutputTypeDef,
    InputSerializationTypeDef,
    IntelligentTieringConfigurationTypeDef,
    InventoryConfigurationTypeDef,
    LifecycleConfigurationTypeDef,
    ListBucketAnalyticsConfigurationsOutputTypeDef,
    ListBucketIntelligentTieringConfigurationsOutputTypeDef,
    ListBucketInventoryConfigurationsOutputTypeDef,
    ListBucketMetricsConfigurationsOutputTypeDef,
    ListBucketsOutputTypeDef,
    ListMultipartUploadsOutputTypeDef,
    ListObjectsOutputTypeDef,
    ListObjectsV2OutputTypeDef,
    ListObjectVersionsOutputTypeDef,
    ListPartsOutputTypeDef,
    MetricsConfigurationTypeDef,
    NotificationConfigurationDeprecatedTypeDef,
    NotificationConfigurationTypeDef,
    ObjectLockConfigurationTypeDef,
    ObjectLockLegalHoldTypeDef,
    ObjectLockRetentionTypeDef,
    OutputSerializationTypeDef,
    OwnershipControlsTypeDef,
    PublicAccessBlockConfigurationTypeDef,
    PutObjectAclOutputTypeDef,
    PutObjectLegalHoldOutputTypeDef,
    PutObjectLockConfigurationOutputTypeDef,
    PutObjectOutputTypeDef,
    PutObjectRetentionOutputTypeDef,
    PutObjectTaggingOutputTypeDef,
    ReplicationConfigurationTypeDef,
    RequestPaymentConfigurationTypeDef,
    RequestProgressTypeDef,
    RestoreObjectOutputTypeDef,
    RestoreRequestTypeDef,
    ScanRangeTypeDef,
    SelectObjectContentOutputTypeDef,
    ServerSideEncryptionConfigurationTypeDef,
    TaggingTypeDef,
    UploadPartCopyOutputTypeDef,
    UploadPartOutputTypeDef,
    VersioningConfigurationTypeDef,
    WebsiteConfigurationTypeDef,
)
from mypy_boto3_s3.waiter import (
    BucketExistsWaiter,
    BucketNotExistsWaiter,
    ObjectExistsWaiter,
    ObjectNotExistsWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("S3Client",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BucketAlreadyExists: Type[BotocoreClientError]
    BucketAlreadyOwnedByYou: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InvalidObjectState: Type[BotocoreClientError]
    NoSuchBucket: Type[BotocoreClientError]
    NoSuchKey: Type[BotocoreClientError]
    NoSuchUpload: Type[BotocoreClientError]
    ObjectAlreadyInActiveTierError: Type[BotocoreClientError]
    ObjectNotInActiveTierError: Type[BotocoreClientError]


class S3Client:
    """
    [S3.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def abort_multipart_upload(
        self,
        Bucket: str,
        Key: str,
        UploadId: str,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
    ) -> AbortMultipartUploadOutputTypeDef:
        """
        [Client.abort_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.abort_multipart_upload)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.can_paginate)
        """

    def complete_multipart_upload(
        self,
        Bucket: str,
        Key: str,
        UploadId: str,
        MultipartUpload: CompletedMultipartUploadTypeDef = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
    ) -> CompleteMultipartUploadOutputTypeDef:
        """
        [Client.complete_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.complete_multipart_upload)
        """

    def copy(
        self,
        CopySource: CopySourceTypeDef,
        Bucket: str,
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        SourceClient: BaseClient = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Client.copy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.copy)
        """

    def copy_object(
        self,
        Bucket: str,
        CopySource: Union[str, CopySourceTypeDef],
        Key: str,
        ACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ] = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentType: str = None,
        CopySourceIfMatch: str = None,
        CopySourceIfModifiedSince: datetime = None,
        CopySourceIfNoneMatch: str = None,
        CopySourceIfUnmodifiedSince: datetime = None,
        Expires: datetime = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWriteACP: str = None,
        Metadata: Dict[str, str] = None,
        MetadataDirective: Literal["COPY", "REPLACE"] = None,
        TaggingDirective: Literal["COPY", "REPLACE"] = None,
        ServerSideEncryption: Literal["AES256", "aws:kms"] = None,
        StorageClass: Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
            "OUTPOSTS",
        ] = None,
        WebsiteRedirectLocation: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        SSEKMSKeyId: str = None,
        SSEKMSEncryptionContext: str = None,
        CopySourceSSECustomerAlgorithm: str = None,
        CopySourceSSECustomerKey: str = None,
        CopySourceSSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        Tagging: str = None,
        ObjectLockMode: Literal["GOVERNANCE", "COMPLIANCE"] = None,
        ObjectLockRetainUntilDate: datetime = None,
        ObjectLockLegalHoldStatus: Literal["ON", "OFF"] = None,
        ExpectedBucketOwner: str = None,
        ExpectedSourceBucketOwner: str = None,
    ) -> CopyObjectOutputTypeDef:
        """
        [Client.copy_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.copy_object)
        """

    def create_bucket(
        self,
        Bucket: str,
        ACL: Literal["private", "public-read", "public-read-write", "authenticated-read"] = None,
        CreateBucketConfiguration: CreateBucketConfigurationTypeDef = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
        ObjectLockEnabledForBucket: bool = None,
    ) -> CreateBucketOutputTypeDef:
        """
        [Client.create_bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.create_bucket)
        """

    def create_multipart_upload(
        self,
        Bucket: str,
        Key: str,
        ACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ] = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentType: str = None,
        Expires: datetime = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWriteACP: str = None,
        Metadata: Dict[str, str] = None,
        ServerSideEncryption: Literal["AES256", "aws:kms"] = None,
        StorageClass: Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
            "OUTPOSTS",
        ] = None,
        WebsiteRedirectLocation: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        SSEKMSKeyId: str = None,
        SSEKMSEncryptionContext: str = None,
        RequestPayer: Literal["requester"] = None,
        Tagging: str = None,
        ObjectLockMode: Literal["GOVERNANCE", "COMPLIANCE"] = None,
        ObjectLockRetainUntilDate: datetime = None,
        ObjectLockLegalHoldStatus: Literal["ON", "OFF"] = None,
        ExpectedBucketOwner: str = None,
    ) -> CreateMultipartUploadOutputTypeDef:
        """
        [Client.create_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.create_multipart_upload)
        """

    def delete_bucket(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        """
        [Client.delete_bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.delete_bucket)
        """

    def delete_bucket_analytics_configuration(
        self, Bucket: str, Id: str, ExpectedBucketOwner: str = None
    ) -> None:
        """
        [Client.delete_bucket_analytics_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.delete_bucket_analytics_configuration)
        """

    def delete_bucket_cors(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        """
        [Client.delete_bucket_cors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.delete_bucket_cors)
        """

    def delete_bucket_encryption(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        """
        [Client.delete_bucket_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.delete_bucket_encryption)
        """

    def delete_bucket_intelligent_tiering_configuration(self, Bucket: str, Id: str) -> None:
        """
        [Client.delete_bucket_intelligent_tiering_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.delete_bucket_intelligent_tiering_configuration)
        """

    def delete_bucket_inventory_configuration(
        self, Bucket: str, Id: str, ExpectedBucketOwner: str = None
    ) -> None:
        """
        [Client.delete_bucket_inventory_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.delete_bucket_inventory_configuration)
        """

    def delete_bucket_lifecycle(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        """
        [Client.delete_bucket_lifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.delete_bucket_lifecycle)
        """

    def delete_bucket_metrics_configuration(
        self, Bucket: str, Id: str, ExpectedBucketOwner: str = None
    ) -> None:
        """
        [Client.delete_bucket_metrics_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.delete_bucket_metrics_configuration)
        """

    def delete_bucket_ownership_controls(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> None:
        """
        [Client.delete_bucket_ownership_controls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.delete_bucket_ownership_controls)
        """

    def delete_bucket_policy(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        """
        [Client.delete_bucket_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.delete_bucket_policy)
        """

    def delete_bucket_replication(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        """
        [Client.delete_bucket_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.delete_bucket_replication)
        """

    def delete_bucket_tagging(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        """
        [Client.delete_bucket_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.delete_bucket_tagging)
        """

    def delete_bucket_website(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        """
        [Client.delete_bucket_website documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.delete_bucket_website)
        """

    def delete_object(
        self,
        Bucket: str,
        Key: str,
        MFA: str = None,
        VersionId: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
        ExpectedBucketOwner: str = None,
    ) -> DeleteObjectOutputTypeDef:
        """
        [Client.delete_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.delete_object)
        """

    def delete_object_tagging(
        self, Bucket: str, Key: str, VersionId: str = None, ExpectedBucketOwner: str = None
    ) -> DeleteObjectTaggingOutputTypeDef:
        """
        [Client.delete_object_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.delete_object_tagging)
        """

    def delete_objects(
        self,
        Bucket: str,
        Delete: DeleteTypeDef,
        MFA: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
        ExpectedBucketOwner: str = None,
    ) -> DeleteObjectsOutputTypeDef:
        """
        [Client.delete_objects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.delete_objects)
        """

    def delete_public_access_block(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        """
        [Client.delete_public_access_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.delete_public_access_block)
        """

    def download_file(
        self,
        Bucket: str,
        Key: str,
        Filename: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Client.download_file documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.download_file)
        """

    def download_fileobj(
        self,
        Bucket: str,
        Key: str,
        Fileobj: IO[Any],
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Client.download_fileobj documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.download_fileobj)
        """

    def generate_presigned_post(
        self,
        Bucket: str,
        Key: str,
        Fields: Dict[str, Any] = None,
        Conditions: List[Any] = None,
        ExpiresIn: int = 3600,
    ) -> Dict[str, Any]:
        """
        [Client.generate_presigned_post documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.generate_presigned_post)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.generate_presigned_url)
        """

    def get_bucket_accelerate_configuration(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketAccelerateConfigurationOutputTypeDef:
        """
        [Client.get_bucket_accelerate_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_accelerate_configuration)
        """

    def get_bucket_acl(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketAclOutputTypeDef:
        """
        [Client.get_bucket_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_acl)
        """

    def get_bucket_analytics_configuration(
        self, Bucket: str, Id: str, ExpectedBucketOwner: str = None
    ) -> GetBucketAnalyticsConfigurationOutputTypeDef:
        """
        [Client.get_bucket_analytics_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_analytics_configuration)
        """

    def get_bucket_cors(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketCorsOutputTypeDef:
        """
        [Client.get_bucket_cors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_cors)
        """

    def get_bucket_encryption(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketEncryptionOutputTypeDef:
        """
        [Client.get_bucket_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_encryption)
        """

    def get_bucket_intelligent_tiering_configuration(
        self, Bucket: str, Id: str
    ) -> GetBucketIntelligentTieringConfigurationOutputTypeDef:
        """
        [Client.get_bucket_intelligent_tiering_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_intelligent_tiering_configuration)
        """

    def get_bucket_inventory_configuration(
        self, Bucket: str, Id: str, ExpectedBucketOwner: str = None
    ) -> GetBucketInventoryConfigurationOutputTypeDef:
        """
        [Client.get_bucket_inventory_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_inventory_configuration)
        """

    def get_bucket_lifecycle(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketLifecycleOutputTypeDef:
        """
        [Client.get_bucket_lifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_lifecycle)
        """

    def get_bucket_lifecycle_configuration(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketLifecycleConfigurationOutputTypeDef:
        """
        [Client.get_bucket_lifecycle_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_lifecycle_configuration)
        """

    def get_bucket_location(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketLocationOutputTypeDef:
        """
        [Client.get_bucket_location documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_location)
        """

    def get_bucket_logging(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketLoggingOutputTypeDef:
        """
        [Client.get_bucket_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_logging)
        """

    def get_bucket_metrics_configuration(
        self, Bucket: str, Id: str, ExpectedBucketOwner: str = None
    ) -> GetBucketMetricsConfigurationOutputTypeDef:
        """
        [Client.get_bucket_metrics_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_metrics_configuration)
        """

    def get_bucket_notification(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> NotificationConfigurationDeprecatedTypeDef:
        """
        [Client.get_bucket_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_notification)
        """

    def get_bucket_notification_configuration(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> NotificationConfigurationTypeDef:
        """
        [Client.get_bucket_notification_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_notification_configuration)
        """

    def get_bucket_ownership_controls(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketOwnershipControlsOutputTypeDef:
        """
        [Client.get_bucket_ownership_controls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_ownership_controls)
        """

    def get_bucket_policy(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketPolicyOutputTypeDef:
        """
        [Client.get_bucket_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_policy)
        """

    def get_bucket_policy_status(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketPolicyStatusOutputTypeDef:
        """
        [Client.get_bucket_policy_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_policy_status)
        """

    def get_bucket_replication(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketReplicationOutputTypeDef:
        """
        [Client.get_bucket_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_replication)
        """

    def get_bucket_request_payment(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketRequestPaymentOutputTypeDef:
        """
        [Client.get_bucket_request_payment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_request_payment)
        """

    def get_bucket_tagging(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketTaggingOutputTypeDef:
        """
        [Client.get_bucket_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_tagging)
        """

    def get_bucket_versioning(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketVersioningOutputTypeDef:
        """
        [Client.get_bucket_versioning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_versioning)
        """

    def get_bucket_website(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketWebsiteOutputTypeDef:
        """
        [Client.get_bucket_website documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_bucket_website)
        """

    def get_object(
        self,
        Bucket: str,
        Key: str,
        IfMatch: str = None,
        IfModifiedSince: datetime = None,
        IfNoneMatch: str = None,
        IfUnmodifiedSince: datetime = None,
        Range: str = None,
        ResponseCacheControl: str = None,
        ResponseContentDisposition: str = None,
        ResponseContentEncoding: str = None,
        ResponseContentLanguage: str = None,
        ResponseContentType: str = None,
        ResponseExpires: datetime = None,
        VersionId: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        PartNumber: int = None,
        ExpectedBucketOwner: str = None,
    ) -> GetObjectOutputTypeDef:
        """
        [Client.get_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_object)
        """

    def get_object_acl(
        self,
        Bucket: str,
        Key: str,
        VersionId: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
    ) -> GetObjectAclOutputTypeDef:
        """
        [Client.get_object_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_object_acl)
        """

    def get_object_legal_hold(
        self,
        Bucket: str,
        Key: str,
        VersionId: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
    ) -> GetObjectLegalHoldOutputTypeDef:
        """
        [Client.get_object_legal_hold documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_object_legal_hold)
        """

    def get_object_lock_configuration(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetObjectLockConfigurationOutputTypeDef:
        """
        [Client.get_object_lock_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_object_lock_configuration)
        """

    def get_object_retention(
        self,
        Bucket: str,
        Key: str,
        VersionId: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
    ) -> GetObjectRetentionOutputTypeDef:
        """
        [Client.get_object_retention documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_object_retention)
        """

    def get_object_tagging(
        self, Bucket: str, Key: str, VersionId: str = None, ExpectedBucketOwner: str = None
    ) -> GetObjectTaggingOutputTypeDef:
        """
        [Client.get_object_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_object_tagging)
        """

    def get_object_torrent(
        self,
        Bucket: str,
        Key: str,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
    ) -> GetObjectTorrentOutputTypeDef:
        """
        [Client.get_object_torrent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_object_torrent)
        """

    def get_public_access_block(
        self, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetPublicAccessBlockOutputTypeDef:
        """
        [Client.get_public_access_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.get_public_access_block)
        """

    def head_bucket(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        """
        [Client.head_bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.head_bucket)
        """

    def head_object(
        self,
        Bucket: str,
        Key: str,
        IfMatch: str = None,
        IfModifiedSince: datetime = None,
        IfNoneMatch: str = None,
        IfUnmodifiedSince: datetime = None,
        Range: str = None,
        VersionId: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        PartNumber: int = None,
        ExpectedBucketOwner: str = None,
    ) -> HeadObjectOutputTypeDef:
        """
        [Client.head_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.head_object)
        """

    def list_bucket_analytics_configurations(
        self, Bucket: str, ContinuationToken: str = None, ExpectedBucketOwner: str = None
    ) -> ListBucketAnalyticsConfigurationsOutputTypeDef:
        """
        [Client.list_bucket_analytics_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.list_bucket_analytics_configurations)
        """

    def list_bucket_intelligent_tiering_configurations(
        self, Bucket: str, ContinuationToken: str = None
    ) -> ListBucketIntelligentTieringConfigurationsOutputTypeDef:
        """
        [Client.list_bucket_intelligent_tiering_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.list_bucket_intelligent_tiering_configurations)
        """

    def list_bucket_inventory_configurations(
        self, Bucket: str, ContinuationToken: str = None, ExpectedBucketOwner: str = None
    ) -> ListBucketInventoryConfigurationsOutputTypeDef:
        """
        [Client.list_bucket_inventory_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.list_bucket_inventory_configurations)
        """

    def list_bucket_metrics_configurations(
        self, Bucket: str, ContinuationToken: str = None, ExpectedBucketOwner: str = None
    ) -> ListBucketMetricsConfigurationsOutputTypeDef:
        """
        [Client.list_bucket_metrics_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.list_bucket_metrics_configurations)
        """

    def list_buckets(self) -> ListBucketsOutputTypeDef:
        """
        [Client.list_buckets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.list_buckets)
        """

    def list_multipart_uploads(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
        ExpectedBucketOwner: str = None,
    ) -> ListMultipartUploadsOutputTypeDef:
        """
        [Client.list_multipart_uploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.list_multipart_uploads)
        """

    def list_object_versions(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        KeyMarker: str = None,
        MaxKeys: int = None,
        Prefix: str = None,
        VersionIdMarker: str = None,
        ExpectedBucketOwner: str = None,
    ) -> ListObjectVersionsOutputTypeDef:
        """
        [Client.list_object_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.list_object_versions)
        """

    def list_objects(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        Marker: str = None,
        MaxKeys: int = None,
        Prefix: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
    ) -> ListObjectsOutputTypeDef:
        """
        [Client.list_objects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.list_objects)
        """

    def list_objects_v2(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        MaxKeys: int = None,
        Prefix: str = None,
        ContinuationToken: str = None,
        FetchOwner: bool = None,
        StartAfter: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
    ) -> ListObjectsV2OutputTypeDef:
        """
        [Client.list_objects_v2 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.list_objects_v2)
        """

    def list_parts(
        self,
        Bucket: str,
        Key: str,
        UploadId: str,
        MaxParts: int = None,
        PartNumberMarker: int = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
    ) -> ListPartsOutputTypeDef:
        """
        [Client.list_parts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.list_parts)
        """

    def put_bucket_accelerate_configuration(
        self,
        Bucket: str,
        AccelerateConfiguration: AccelerateConfigurationTypeDef,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [Client.put_bucket_accelerate_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_bucket_accelerate_configuration)
        """

    def put_bucket_acl(
        self,
        Bucket: str,
        ACL: Literal["private", "public-read", "public-read-write", "authenticated-read"] = None,
        AccessControlPolicy: AccessControlPolicyTypeDef = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [Client.put_bucket_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_bucket_acl)
        """

    def put_bucket_analytics_configuration(
        self,
        Bucket: str,
        Id: str,
        AnalyticsConfiguration: "AnalyticsConfigurationTypeDef",
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [Client.put_bucket_analytics_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_bucket_analytics_configuration)
        """

    def put_bucket_cors(
        self,
        Bucket: str,
        CORSConfiguration: CORSConfigurationTypeDef,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [Client.put_bucket_cors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_bucket_cors)
        """

    def put_bucket_encryption(
        self,
        Bucket: str,
        ServerSideEncryptionConfiguration: "ServerSideEncryptionConfigurationTypeDef",
        ContentMD5: str = None,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [Client.put_bucket_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_bucket_encryption)
        """

    def put_bucket_intelligent_tiering_configuration(
        self,
        Bucket: str,
        Id: str,
        IntelligentTieringConfiguration: "IntelligentTieringConfigurationTypeDef",
    ) -> None:
        """
        [Client.put_bucket_intelligent_tiering_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_bucket_intelligent_tiering_configuration)
        """

    def put_bucket_inventory_configuration(
        self,
        Bucket: str,
        Id: str,
        InventoryConfiguration: "InventoryConfigurationTypeDef",
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [Client.put_bucket_inventory_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_bucket_inventory_configuration)
        """

    def put_bucket_lifecycle(
        self,
        Bucket: str,
        LifecycleConfiguration: LifecycleConfigurationTypeDef = None,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [Client.put_bucket_lifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_bucket_lifecycle)
        """

    def put_bucket_lifecycle_configuration(
        self,
        Bucket: str,
        LifecycleConfiguration: BucketLifecycleConfigurationTypeDef = None,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [Client.put_bucket_lifecycle_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_bucket_lifecycle_configuration)
        """

    def put_bucket_logging(
        self,
        Bucket: str,
        BucketLoggingStatus: BucketLoggingStatusTypeDef,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [Client.put_bucket_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_bucket_logging)
        """

    def put_bucket_metrics_configuration(
        self,
        Bucket: str,
        Id: str,
        MetricsConfiguration: "MetricsConfigurationTypeDef",
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [Client.put_bucket_metrics_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_bucket_metrics_configuration)
        """

    def put_bucket_notification(
        self,
        Bucket: str,
        NotificationConfiguration: NotificationConfigurationDeprecatedTypeDef,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [Client.put_bucket_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_bucket_notification)
        """

    def put_bucket_notification_configuration(
        self,
        Bucket: str,
        NotificationConfiguration: NotificationConfigurationTypeDef,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [Client.put_bucket_notification_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_bucket_notification_configuration)
        """

    def put_bucket_ownership_controls(
        self,
        Bucket: str,
        OwnershipControls: "OwnershipControlsTypeDef",
        ContentMD5: str = None,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [Client.put_bucket_ownership_controls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_bucket_ownership_controls)
        """

    def put_bucket_policy(
        self,
        Bucket: str,
        Policy: str,
        ConfirmRemoveSelfBucketAccess: bool = None,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [Client.put_bucket_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_bucket_policy)
        """

    def put_bucket_replication(
        self,
        Bucket: str,
        ReplicationConfiguration: "ReplicationConfigurationTypeDef",
        Token: str = None,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [Client.put_bucket_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_bucket_replication)
        """

    def put_bucket_request_payment(
        self,
        Bucket: str,
        RequestPaymentConfiguration: RequestPaymentConfigurationTypeDef,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [Client.put_bucket_request_payment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_bucket_request_payment)
        """

    def put_bucket_tagging(
        self, Bucket: str, Tagging: "TaggingTypeDef", ExpectedBucketOwner: str = None
    ) -> None:
        """
        [Client.put_bucket_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_bucket_tagging)
        """

    def put_bucket_versioning(
        self,
        Bucket: str,
        VersioningConfiguration: VersioningConfigurationTypeDef,
        MFA: str = None,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [Client.put_bucket_versioning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_bucket_versioning)
        """

    def put_bucket_website(
        self,
        Bucket: str,
        WebsiteConfiguration: WebsiteConfigurationTypeDef,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [Client.put_bucket_website documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_bucket_website)
        """

    def put_object(
        self,
        Bucket: str,
        Key: str,
        ACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ] = None,
        Body: Union[bytes, IO[bytes]] = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentLength: int = None,
        ContentMD5: str = None,
        ContentType: str = None,
        Expires: datetime = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWriteACP: str = None,
        Metadata: Dict[str, str] = None,
        ServerSideEncryption: Literal["AES256", "aws:kms"] = None,
        StorageClass: Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
            "OUTPOSTS",
        ] = None,
        WebsiteRedirectLocation: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        SSEKMSKeyId: str = None,
        SSEKMSEncryptionContext: str = None,
        RequestPayer: Literal["requester"] = None,
        Tagging: str = None,
        ObjectLockMode: Literal["GOVERNANCE", "COMPLIANCE"] = None,
        ObjectLockRetainUntilDate: datetime = None,
        ObjectLockLegalHoldStatus: Literal["ON", "OFF"] = None,
        ExpectedBucketOwner: str = None,
    ) -> PutObjectOutputTypeDef:
        """
        [Client.put_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_object)
        """

    def put_object_acl(
        self,
        Bucket: str,
        Key: str,
        ACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ] = None,
        AccessControlPolicy: AccessControlPolicyTypeDef = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
        RequestPayer: Literal["requester"] = None,
        VersionId: str = None,
        ExpectedBucketOwner: str = None,
    ) -> PutObjectAclOutputTypeDef:
        """
        [Client.put_object_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_object_acl)
        """

    def put_object_legal_hold(
        self,
        Bucket: str,
        Key: str,
        LegalHold: "ObjectLockLegalHoldTypeDef" = None,
        RequestPayer: Literal["requester"] = None,
        VersionId: str = None,
        ContentMD5: str = None,
        ExpectedBucketOwner: str = None,
    ) -> PutObjectLegalHoldOutputTypeDef:
        """
        [Client.put_object_legal_hold documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_object_legal_hold)
        """

    def put_object_lock_configuration(
        self,
        Bucket: str,
        ObjectLockConfiguration: "ObjectLockConfigurationTypeDef" = None,
        RequestPayer: Literal["requester"] = None,
        Token: str = None,
        ContentMD5: str = None,
        ExpectedBucketOwner: str = None,
    ) -> PutObjectLockConfigurationOutputTypeDef:
        """
        [Client.put_object_lock_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_object_lock_configuration)
        """

    def put_object_retention(
        self,
        Bucket: str,
        Key: str,
        Retention: "ObjectLockRetentionTypeDef" = None,
        RequestPayer: Literal["requester"] = None,
        VersionId: str = None,
        BypassGovernanceRetention: bool = None,
        ContentMD5: str = None,
        ExpectedBucketOwner: str = None,
    ) -> PutObjectRetentionOutputTypeDef:
        """
        [Client.put_object_retention documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_object_retention)
        """

    def put_object_tagging(
        self,
        Bucket: str,
        Key: str,
        Tagging: "TaggingTypeDef",
        VersionId: str = None,
        ContentMD5: str = None,
        ExpectedBucketOwner: str = None,
    ) -> PutObjectTaggingOutputTypeDef:
        """
        [Client.put_object_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_object_tagging)
        """

    def put_public_access_block(
        self,
        Bucket: str,
        PublicAccessBlockConfiguration: "PublicAccessBlockConfigurationTypeDef",
        ContentMD5: str = None,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [Client.put_public_access_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.put_public_access_block)
        """

    def restore_object(
        self,
        Bucket: str,
        Key: str,
        VersionId: str = None,
        RestoreRequest: RestoreRequestTypeDef = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
    ) -> RestoreObjectOutputTypeDef:
        """
        [Client.restore_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.restore_object)
        """

    def select_object_content(
        self,
        Bucket: str,
        Key: str,
        Expression: str,
        ExpressionType: Literal["SQL"],
        InputSerialization: "InputSerializationTypeDef",
        OutputSerialization: "OutputSerializationTypeDef",
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestProgress: RequestProgressTypeDef = None,
        ScanRange: ScanRangeTypeDef = None,
        ExpectedBucketOwner: str = None,
    ) -> SelectObjectContentOutputTypeDef:
        """
        [Client.select_object_content documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.select_object_content)
        """

    def upload_file(
        self,
        Filename: str,
        Bucket: str,
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Client.upload_file documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.upload_file)
        """

    def upload_fileobj(
        self,
        Fileobj: IO[Any],
        Bucket: str,
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Client.upload_fileobj documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.upload_fileobj)
        """

    def upload_part(
        self,
        Bucket: str,
        Key: str,
        PartNumber: int,
        UploadId: str,
        Body: Union[bytes, IO[bytes]] = None,
        ContentLength: int = None,
        ContentMD5: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
    ) -> UploadPartOutputTypeDef:
        """
        [Client.upload_part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.upload_part)
        """

    def upload_part_copy(
        self,
        Bucket: str,
        CopySource: Union[str, CopySourceTypeDef],
        Key: str,
        PartNumber: int,
        UploadId: str,
        CopySourceIfMatch: str = None,
        CopySourceIfModifiedSince: datetime = None,
        CopySourceIfNoneMatch: str = None,
        CopySourceIfUnmodifiedSince: datetime = None,
        CopySourceRange: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        CopySourceSSECustomerAlgorithm: str = None,
        CopySourceSSECustomerKey: str = None,
        CopySourceSSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
        ExpectedSourceBucketOwner: str = None,
    ) -> UploadPartCopyOutputTypeDef:
        """
        [Client.upload_part_copy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Client.upload_part_copy)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_multipart_uploads"]
    ) -> ListMultipartUploadsPaginator:
        """
        [Paginator.ListMultipartUploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Paginator.ListMultipartUploads)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_object_versions"]
    ) -> ListObjectVersionsPaginator:
        """
        [Paginator.ListObjectVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Paginator.ListObjectVersions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_objects"]) -> ListObjectsPaginator:
        """
        [Paginator.ListObjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Paginator.ListObjects)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_objects_v2"]) -> ListObjectsV2Paginator:
        """
        [Paginator.ListObjectsV2 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Paginator.ListObjectsV2)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_parts"]) -> ListPartsPaginator:
        """
        [Paginator.ListParts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Paginator.ListParts)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["bucket_exists"]) -> BucketExistsWaiter:
        """
        [Waiter.BucketExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Waiter.BucketExists)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["bucket_not_exists"]) -> BucketNotExistsWaiter:
        """
        [Waiter.BucketNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Waiter.BucketNotExists)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["object_exists"]) -> ObjectExistsWaiter:
        """
        [Waiter.ObjectExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Waiter.ObjectExists)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["object_not_exists"]) -> ObjectNotExistsWaiter:
        """
        [Waiter.ObjectNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Waiter.ObjectNotExists)
        """
