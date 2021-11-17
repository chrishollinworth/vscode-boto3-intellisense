"""
Type annotations for s3 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html)

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
from botocore.response import StreamingBody

from .literals import (
    BucketCannedACLType,
    MetadataDirectiveType,
    ObjectCannedACLType,
    ObjectLockLegalHoldStatusType,
    ObjectLockModeType,
    ReplicationStatusType,
    ServerSideEncryptionType,
    StorageClassType,
    TaggingDirectiveType,
)
from .paginator import (
    ListMultipartUploadsPaginator,
    ListObjectsPaginator,
    ListObjectsV2Paginator,
    ListObjectVersionsPaginator,
    ListPartsPaginator,
)
from .type_defs import (
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
    NotificationConfigurationDeprecatedResponseMetadataTypeDef,
    NotificationConfigurationDeprecatedTypeDef,
    NotificationConfigurationResponseMetadataTypeDef,
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
from .waiter import (
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

class S3Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        S3Client exceptions.
        """
    def abort_multipart_upload(
        self,
        *,
        Bucket: str,
        Key: str,
        UploadId: str,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None
    ) -> AbortMultipartUploadOutputTypeDef:
        """
        This action aborts a multipart upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.abort_multipart_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#abort_multipart_upload)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#can_paginate)
        """
    def complete_multipart_upload(
        self,
        *,
        Bucket: str,
        Key: str,
        UploadId: str,
        MultipartUpload: "CompletedMultipartUploadTypeDef" = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None
    ) -> CompleteMultipartUploadOutputTypeDef:
        """
        Completes a multipart upload by assembling previously uploaded parts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.complete_multipart_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#complete_multipart_upload)
        """
    def copy(
        self,
        *,
        CopySource: "CopySourceTypeDef",
        Bucket: str,
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        SourceClient: BaseClient = None,
        Config: TransferConfig = None
    ) -> None:
        """
        Copy an object from one S3 location to another.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.copy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#copy)
        """
    def copy_object(
        self,
        *,
        Bucket: str,
        CopySource: Union[str, "CopySourceTypeDef"],
        Key: str,
        ACL: ObjectCannedACLType = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentType: str = None,
        CopySourceIfMatch: str = None,
        CopySourceIfModifiedSince: Union[datetime, str] = None,
        CopySourceIfNoneMatch: str = None,
        CopySourceIfUnmodifiedSince: Union[datetime, str] = None,
        Expires: Union[datetime, str] = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWriteACP: str = None,
        Metadata: Dict[str, str] = None,
        MetadataDirective: MetadataDirectiveType = None,
        TaggingDirective: TaggingDirectiveType = None,
        ServerSideEncryption: ServerSideEncryptionType = None,
        StorageClass: StorageClassType = None,
        WebsiteRedirectLocation: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        SSEKMSKeyId: str = None,
        SSEKMSEncryptionContext: str = None,
        BucketKeyEnabled: bool = None,
        CopySourceSSECustomerAlgorithm: str = None,
        CopySourceSSECustomerKey: str = None,
        CopySourceSSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        Tagging: str = None,
        ObjectLockMode: ObjectLockModeType = None,
        ObjectLockRetainUntilDate: Union[datetime, str] = None,
        ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType = None,
        ExpectedBucketOwner: str = None,
        ExpectedSourceBucketOwner: str = None
    ) -> CopyObjectOutputTypeDef:
        """
        Creates a copy of an object that is already stored in Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.copy_object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#copy_object)
        """
    def create_bucket(
        self,
        *,
        Bucket: str,
        ACL: BucketCannedACLType = None,
        CreateBucketConfiguration: "CreateBucketConfigurationTypeDef" = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
        ObjectLockEnabledForBucket: bool = None
    ) -> CreateBucketOutputTypeDef:
        """
        Creates a new S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.create_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#create_bucket)
        """
    def create_multipart_upload(
        self,
        *,
        Bucket: str,
        Key: str,
        ACL: ObjectCannedACLType = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentType: str = None,
        Expires: Union[datetime, str] = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWriteACP: str = None,
        Metadata: Dict[str, str] = None,
        ServerSideEncryption: ServerSideEncryptionType = None,
        StorageClass: StorageClassType = None,
        WebsiteRedirectLocation: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        SSEKMSKeyId: str = None,
        SSEKMSEncryptionContext: str = None,
        BucketKeyEnabled: bool = None,
        RequestPayer: Literal["requester"] = None,
        Tagging: str = None,
        ObjectLockMode: ObjectLockModeType = None,
        ObjectLockRetainUntilDate: Union[datetime, str] = None,
        ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType = None,
        ExpectedBucketOwner: str = None
    ) -> CreateMultipartUploadOutputTypeDef:
        """
        This action initiates a multipart upload and returns an upload ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.create_multipart_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#create_multipart_upload)
        """
    def delete_bucket(self, *, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        """
        Deletes the S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.delete_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#delete_bucket)
        """
    def delete_bucket_analytics_configuration(
        self, *, Bucket: str, Id: str, ExpectedBucketOwner: str = None
    ) -> None:
        """
        Deletes an analytics configuration for the bucket (specified by the analytics
        configuration ID).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.delete_bucket_analytics_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#delete_bucket_analytics_configuration)
        """
    def delete_bucket_cors(self, *, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        """
        Deletes the `cors` configuration information set for the bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.delete_bucket_cors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#delete_bucket_cors)
        """
    def delete_bucket_encryption(self, *, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        """
        This implementation of the DELETE action removes default encryption from the
        bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.delete_bucket_encryption)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#delete_bucket_encryption)
        """
    def delete_bucket_intelligent_tiering_configuration(self, *, Bucket: str, Id: str) -> None:
        """
        Deletes the S3 Intelligent-Tiering configuration from the specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.delete_bucket_intelligent_tiering_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#delete_bucket_intelligent_tiering_configuration)
        """
    def delete_bucket_inventory_configuration(
        self, *, Bucket: str, Id: str, ExpectedBucketOwner: str = None
    ) -> None:
        """
        Deletes an inventory configuration (identified by the inventory ID) from the
        bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.delete_bucket_inventory_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#delete_bucket_inventory_configuration)
        """
    def delete_bucket_lifecycle(self, *, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        """
        Deletes the lifecycle configuration from the specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.delete_bucket_lifecycle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#delete_bucket_lifecycle)
        """
    def delete_bucket_metrics_configuration(
        self, *, Bucket: str, Id: str, ExpectedBucketOwner: str = None
    ) -> None:
        """
        Deletes a metrics configuration for the Amazon CloudWatch request metrics
        (specified by the metrics configuration ID) from the bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.delete_bucket_metrics_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#delete_bucket_metrics_configuration)
        """
    def delete_bucket_ownership_controls(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> None:
        """
        Removes `OwnershipControls` for an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.delete_bucket_ownership_controls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#delete_bucket_ownership_controls)
        """
    def delete_bucket_policy(self, *, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        """
        This implementation of the DELETE action uses the policy subresource to delete
        the policy of a specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.delete_bucket_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#delete_bucket_policy)
        """
    def delete_bucket_replication(self, *, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        """
        Deletes the replication configuration from the bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.delete_bucket_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#delete_bucket_replication)
        """
    def delete_bucket_tagging(self, *, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        """
        Deletes the tags from the bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.delete_bucket_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#delete_bucket_tagging)
        """
    def delete_bucket_website(self, *, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        """
        This action removes the website configuration for a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.delete_bucket_website)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#delete_bucket_website)
        """
    def delete_object(
        self,
        *,
        Bucket: str,
        Key: str,
        MFA: str = None,
        VersionId: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
        ExpectedBucketOwner: str = None
    ) -> DeleteObjectOutputTypeDef:
        """
        Removes the null version (if there is one) of an object and inserts a delete
        marker, which becomes the latest version of the object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.delete_object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#delete_object)
        """
    def delete_object_tagging(
        self, *, Bucket: str, Key: str, VersionId: str = None, ExpectedBucketOwner: str = None
    ) -> DeleteObjectTaggingOutputTypeDef:
        """
        Removes the entire tag set from the specified object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.delete_object_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#delete_object_tagging)
        """
    def delete_objects(
        self,
        *,
        Bucket: str,
        Delete: "DeleteTypeDef",
        MFA: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
        ExpectedBucketOwner: str = None
    ) -> DeleteObjectsOutputTypeDef:
        """
        This action enables you to delete multiple objects from a bucket using a single
        HTTP request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.delete_objects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#delete_objects)
        """
    def delete_public_access_block(self, *, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        """
        Removes the `PublicAccessBlock` configuration for an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.delete_public_access_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#delete_public_access_block)
        """
    def download_file(
        self,
        *,
        Bucket: str,
        Key: str,
        Filename: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None
    ) -> None:
        """
        Download an S3 object to a file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.download_file)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#download_file)
        """
    def download_fileobj(
        self,
        *,
        Bucket: str,
        Key: str,
        Fileobj: IO[Any],
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None
    ) -> None:
        """
        Download an object from S3 to a file-like object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.download_fileobj)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#download_fileobj)
        """
    def generate_presigned_post(
        self,
        *,
        Bucket: str,
        Key: str,
        Fields: Dict[str, Any] = None,
        Conditions: List[Any] = None,
        ExpiresIn: int = 3600
    ) -> Dict[str, Any]:
        """
        Builds the url and the form fields used for a presigned s3 post.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.generate_presigned_post)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#generate_presigned_post)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#generate_presigned_url)
        """
    def get_bucket_accelerate_configuration(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketAccelerateConfigurationOutputTypeDef:
        """
        This implementation of the GET action uses the `accelerate` subresource to
        return the Transfer Acceleration state of a bucket, which is either `Enabled` or
        `Suspended`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_accelerate_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_accelerate_configuration)
        """
    def get_bucket_acl(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketAclOutputTypeDef:
        """
        This implementation of the `GET` action uses the `acl` subresource to return the
        access control list (ACL) of a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_acl)
        """
    def get_bucket_analytics_configuration(
        self, *, Bucket: str, Id: str, ExpectedBucketOwner: str = None
    ) -> GetBucketAnalyticsConfigurationOutputTypeDef:
        """
        This implementation of the GET action returns an analytics configuration
        (identified by the analytics configuration ID) from the bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_analytics_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_analytics_configuration)
        """
    def get_bucket_cors(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketCorsOutputTypeDef:
        """
        Returns the cors configuration information set for the bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_cors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_cors)
        """
    def get_bucket_encryption(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketEncryptionOutputTypeDef:
        """
        Returns the default encryption configuration for an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_encryption)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_encryption)
        """
    def get_bucket_intelligent_tiering_configuration(
        self, *, Bucket: str, Id: str
    ) -> GetBucketIntelligentTieringConfigurationOutputTypeDef:
        """
        Gets the S3 Intelligent-Tiering configuration from the specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_intelligent_tiering_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_intelligent_tiering_configuration)
        """
    def get_bucket_inventory_configuration(
        self, *, Bucket: str, Id: str, ExpectedBucketOwner: str = None
    ) -> GetBucketInventoryConfigurationOutputTypeDef:
        """
        Returns an inventory configuration (identified by the inventory configuration
        ID) from the bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_inventory_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_inventory_configuration)
        """
    def get_bucket_lifecycle(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketLifecycleOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_lifecycle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_lifecycle)
        """
    def get_bucket_lifecycle_configuration(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketLifecycleConfigurationOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_lifecycle_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_lifecycle_configuration)
        """
    def get_bucket_location(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketLocationOutputTypeDef:
        """
        Returns the Region the bucket resides in.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_location)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_location)
        """
    def get_bucket_logging(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketLoggingOutputTypeDef:
        """
        Returns the logging status of a bucket and the permissions users have to view
        and modify that status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_logging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_logging)
        """
    def get_bucket_metrics_configuration(
        self, *, Bucket: str, Id: str, ExpectedBucketOwner: str = None
    ) -> GetBucketMetricsConfigurationOutputTypeDef:
        """
        Gets a metrics configuration (specified by the metrics configuration ID) from
        the bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_metrics_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_metrics_configuration)
        """
    def get_bucket_notification(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> NotificationConfigurationDeprecatedResponseMetadataTypeDef:
        """
        No longer used, see `GetBucketNotificationConfiguration <https://docs.aws.amazon
        .com/AmazonS3/latest/API/API_GetBucketNotificationConfiguration.html>`__ .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_notification)
        """
    def get_bucket_notification_configuration(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> NotificationConfigurationResponseMetadataTypeDef:
        """
        Returns the notification configuration of a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_notification_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_notification_configuration)
        """
    def get_bucket_ownership_controls(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketOwnershipControlsOutputTypeDef:
        """
        Retrieves `OwnershipControls` for an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_ownership_controls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_ownership_controls)
        """
    def get_bucket_policy(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketPolicyOutputTypeDef:
        """
        Returns the policy of a specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_policy)
        """
    def get_bucket_policy_status(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketPolicyStatusOutputTypeDef:
        """
        Retrieves the policy status for an Amazon S3 bucket, indicating whether the
        bucket is public.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_policy_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_policy_status)
        """
    def get_bucket_replication(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketReplicationOutputTypeDef:
        """
        Returns the replication configuration of a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_replication)
        """
    def get_bucket_request_payment(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketRequestPaymentOutputTypeDef:
        """
        Returns the request payment configuration of a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_request_payment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_request_payment)
        """
    def get_bucket_tagging(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketTaggingOutputTypeDef:
        """
        Returns the tag set associated with the bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_tagging)
        """
    def get_bucket_versioning(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketVersioningOutputTypeDef:
        """
        Returns the versioning state of a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_versioning)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_versioning)
        """
    def get_bucket_website(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetBucketWebsiteOutputTypeDef:
        """
        Returns the website configuration for a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_bucket_website)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_bucket_website)
        """
    def get_object(
        self,
        *,
        Bucket: str,
        Key: str,
        IfMatch: str = None,
        IfModifiedSince: Union[datetime, str] = None,
        IfNoneMatch: str = None,
        IfUnmodifiedSince: Union[datetime, str] = None,
        Range: str = None,
        ResponseCacheControl: str = None,
        ResponseContentDisposition: str = None,
        ResponseContentEncoding: str = None,
        ResponseContentLanguage: str = None,
        ResponseContentType: str = None,
        ResponseExpires: Union[datetime, str] = None,
        VersionId: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        PartNumber: int = None,
        ExpectedBucketOwner: str = None
    ) -> GetObjectOutputTypeDef:
        """
        Retrieves objects from Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_object)
        """
    def get_object_acl(
        self,
        *,
        Bucket: str,
        Key: str,
        VersionId: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None
    ) -> GetObjectAclOutputTypeDef:
        """
        Returns the access control list (ACL) of an object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_object_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_object_acl)
        """
    def get_object_legal_hold(
        self,
        *,
        Bucket: str,
        Key: str,
        VersionId: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None
    ) -> GetObjectLegalHoldOutputTypeDef:
        """
        Gets an object's current Legal Hold status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_object_legal_hold)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_object_legal_hold)
        """
    def get_object_lock_configuration(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetObjectLockConfigurationOutputTypeDef:
        """
        Gets the Object Lock configuration for a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_object_lock_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_object_lock_configuration)
        """
    def get_object_retention(
        self,
        *,
        Bucket: str,
        Key: str,
        VersionId: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None
    ) -> GetObjectRetentionOutputTypeDef:
        """
        Retrieves an object's retention settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_object_retention)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_object_retention)
        """
    def get_object_tagging(
        self,
        *,
        Bucket: str,
        Key: str,
        VersionId: str = None,
        ExpectedBucketOwner: str = None,
        RequestPayer: Literal["requester"] = None
    ) -> GetObjectTaggingOutputTypeDef:
        """
        Returns the tag-set of an object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_object_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_object_tagging)
        """
    def get_object_torrent(
        self,
        *,
        Bucket: str,
        Key: str,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None
    ) -> GetObjectTorrentOutputTypeDef:
        """
        Returns torrent files from a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_object_torrent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_object_torrent)
        """
    def get_public_access_block(
        self, *, Bucket: str, ExpectedBucketOwner: str = None
    ) -> GetPublicAccessBlockOutputTypeDef:
        """
        Retrieves the `PublicAccessBlock` configuration for an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.get_public_access_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#get_public_access_block)
        """
    def head_bucket(self, *, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        """
        This action is useful to determine if a bucket exists and you have permission to
        access it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.head_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#head_bucket)
        """
    def head_object(
        self,
        *,
        Bucket: str,
        Key: str,
        IfMatch: str = None,
        IfModifiedSince: Union[datetime, str] = None,
        IfNoneMatch: str = None,
        IfUnmodifiedSince: Union[datetime, str] = None,
        Range: str = None,
        VersionId: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        PartNumber: int = None,
        ExpectedBucketOwner: str = None
    ) -> HeadObjectOutputTypeDef:
        """
        The HEAD action retrieves metadata from an object without returning the object
        itself.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.head_object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#head_object)
        """
    def list_bucket_analytics_configurations(
        self, *, Bucket: str, ContinuationToken: str = None, ExpectedBucketOwner: str = None
    ) -> ListBucketAnalyticsConfigurationsOutputTypeDef:
        """
        Lists the analytics configurations for the bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.list_bucket_analytics_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#list_bucket_analytics_configurations)
        """
    def list_bucket_intelligent_tiering_configurations(
        self, *, Bucket: str, ContinuationToken: str = None
    ) -> ListBucketIntelligentTieringConfigurationsOutputTypeDef:
        """
        Lists the S3 Intelligent-Tiering configuration from the specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.list_bucket_intelligent_tiering_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#list_bucket_intelligent_tiering_configurations)
        """
    def list_bucket_inventory_configurations(
        self, *, Bucket: str, ContinuationToken: str = None, ExpectedBucketOwner: str = None
    ) -> ListBucketInventoryConfigurationsOutputTypeDef:
        """
        Returns a list of inventory configurations for the bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.list_bucket_inventory_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#list_bucket_inventory_configurations)
        """
    def list_bucket_metrics_configurations(
        self, *, Bucket: str, ContinuationToken: str = None, ExpectedBucketOwner: str = None
    ) -> ListBucketMetricsConfigurationsOutputTypeDef:
        """
        Lists the metrics configurations for the bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.list_bucket_metrics_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#list_bucket_metrics_configurations)
        """
    def list_buckets(self) -> ListBucketsOutputTypeDef:
        """
        Returns a list of all buckets owned by the authenticated sender of the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.list_buckets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#list_buckets)
        """
    def list_multipart_uploads(
        self,
        *,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
        ExpectedBucketOwner: str = None
    ) -> ListMultipartUploadsOutputTypeDef:
        """
        This action lists in-progress multipart uploads.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.list_multipart_uploads)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#list_multipart_uploads)
        """
    def list_object_versions(
        self,
        *,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        KeyMarker: str = None,
        MaxKeys: int = None,
        Prefix: str = None,
        VersionIdMarker: str = None,
        ExpectedBucketOwner: str = None
    ) -> ListObjectVersionsOutputTypeDef:
        """
        Returns metadata about all versions of the objects in a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.list_object_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#list_object_versions)
        """
    def list_objects(
        self,
        *,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        Marker: str = None,
        MaxKeys: int = None,
        Prefix: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None
    ) -> ListObjectsOutputTypeDef:
        """
        Returns some or all (up to 1,000) of the objects in a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.list_objects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#list_objects)
        """
    def list_objects_v2(
        self,
        *,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        MaxKeys: int = None,
        Prefix: str = None,
        ContinuationToken: str = None,
        FetchOwner: bool = None,
        StartAfter: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None
    ) -> ListObjectsV2OutputTypeDef:
        """
        Returns some or all (up to 1,000) of the objects in a bucket with each request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.list_objects_v2)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#list_objects_v2)
        """
    def list_parts(
        self,
        *,
        Bucket: str,
        Key: str,
        UploadId: str,
        MaxParts: int = None,
        PartNumberMarker: int = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None
    ) -> ListPartsOutputTypeDef:
        """
        Lists the parts that have been uploaded for a specific multipart upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.list_parts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#list_parts)
        """
    def put_bucket_accelerate_configuration(
        self,
        *,
        Bucket: str,
        AccelerateConfiguration: "AccelerateConfigurationTypeDef",
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Sets the accelerate configuration of an existing bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_bucket_accelerate_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_bucket_accelerate_configuration)
        """
    def put_bucket_acl(
        self,
        *,
        Bucket: str,
        ACL: BucketCannedACLType = None,
        AccessControlPolicy: "AccessControlPolicyTypeDef" = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Sets the permissions on an existing bucket using access control lists (ACL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_bucket_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_bucket_acl)
        """
    def put_bucket_analytics_configuration(
        self,
        *,
        Bucket: str,
        Id: str,
        AnalyticsConfiguration: "AnalyticsConfigurationTypeDef",
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Sets an analytics configuration for the bucket (specified by the analytics
        configuration ID).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_bucket_analytics_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_bucket_analytics_configuration)
        """
    def put_bucket_cors(
        self,
        *,
        Bucket: str,
        CORSConfiguration: "CORSConfigurationTypeDef",
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Sets the `cors` configuration for your bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_bucket_cors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_bucket_cors)
        """
    def put_bucket_encryption(
        self,
        *,
        Bucket: str,
        ServerSideEncryptionConfiguration: "ServerSideEncryptionConfigurationTypeDef",
        ContentMD5: str = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        This action uses the `encryption` subresource to configure default encryption
        and Amazon S3 Bucket Key for an existing bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_bucket_encryption)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_bucket_encryption)
        """
    def put_bucket_intelligent_tiering_configuration(
        self,
        *,
        Bucket: str,
        Id: str,
        IntelligentTieringConfiguration: "IntelligentTieringConfigurationTypeDef"
    ) -> None:
        """
        Puts a S3 Intelligent-Tiering configuration to the specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_bucket_intelligent_tiering_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_bucket_intelligent_tiering_configuration)
        """
    def put_bucket_inventory_configuration(
        self,
        *,
        Bucket: str,
        Id: str,
        InventoryConfiguration: "InventoryConfigurationTypeDef",
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        This implementation of the `PUT` action adds an inventory configuration
        (identified by the inventory ID) to the bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_bucket_inventory_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_bucket_inventory_configuration)
        """
    def put_bucket_lifecycle(
        self,
        *,
        Bucket: str,
        LifecycleConfiguration: "LifecycleConfigurationTypeDef" = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_bucket_lifecycle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_bucket_lifecycle)
        """
    def put_bucket_lifecycle_configuration(
        self,
        *,
        Bucket: str,
        LifecycleConfiguration: "BucketLifecycleConfigurationTypeDef" = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Creates a new lifecycle configuration for the bucket or replaces an existing
        lifecycle configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_bucket_lifecycle_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_bucket_lifecycle_configuration)
        """
    def put_bucket_logging(
        self,
        *,
        Bucket: str,
        BucketLoggingStatus: "BucketLoggingStatusTypeDef",
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Set the logging parameters for a bucket and to specify permissions for who can
        view and modify the logging parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_bucket_logging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_bucket_logging)
        """
    def put_bucket_metrics_configuration(
        self,
        *,
        Bucket: str,
        Id: str,
        MetricsConfiguration: "MetricsConfigurationTypeDef",
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Sets a metrics configuration (specified by the metrics configuration ID) for the
        bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_bucket_metrics_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_bucket_metrics_configuration)
        """
    def put_bucket_notification(
        self,
        *,
        Bucket: str,
        NotificationConfiguration: "NotificationConfigurationDeprecatedTypeDef",
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        No longer used, see the `PutBucketNotificationConfiguration <https://docs.aws.am
        azon.com/AmazonS3/latest/API/API_PutBucketNotificationConfiguration.html>`__
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_bucket_notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_bucket_notification)
        """
    def put_bucket_notification_configuration(
        self,
        *,
        Bucket: str,
        NotificationConfiguration: "NotificationConfigurationTypeDef",
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Enables notifications of specified events for a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_bucket_notification_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_bucket_notification_configuration)
        """
    def put_bucket_ownership_controls(
        self,
        *,
        Bucket: str,
        OwnershipControls: "OwnershipControlsTypeDef",
        ContentMD5: str = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Creates or modifies `OwnershipControls` for an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_bucket_ownership_controls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_bucket_ownership_controls)
        """
    def put_bucket_policy(
        self,
        *,
        Bucket: str,
        Policy: str,
        ConfirmRemoveSelfBucketAccess: bool = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Applies an Amazon S3 bucket policy to an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_bucket_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_bucket_policy)
        """
    def put_bucket_replication(
        self,
        *,
        Bucket: str,
        ReplicationConfiguration: "ReplicationConfigurationTypeDef",
        Token: str = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Creates a replication configuration or replaces an existing one.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_bucket_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_bucket_replication)
        """
    def put_bucket_request_payment(
        self,
        *,
        Bucket: str,
        RequestPaymentConfiguration: "RequestPaymentConfigurationTypeDef",
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Sets the request payment configuration for a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_bucket_request_payment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_bucket_request_payment)
        """
    def put_bucket_tagging(
        self, *, Bucket: str, Tagging: "TaggingTypeDef", ExpectedBucketOwner: str = None
    ) -> None:
        """
        Sets the tags for a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_bucket_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_bucket_tagging)
        """
    def put_bucket_versioning(
        self,
        *,
        Bucket: str,
        VersioningConfiguration: "VersioningConfigurationTypeDef",
        MFA: str = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Sets the versioning state of an existing bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_bucket_versioning)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_bucket_versioning)
        """
    def put_bucket_website(
        self,
        *,
        Bucket: str,
        WebsiteConfiguration: "WebsiteConfigurationTypeDef",
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Sets the configuration of the website that is specified in the `website`
        subresource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_bucket_website)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_bucket_website)
        """
    def put_object(
        self,
        *,
        Bucket: str,
        Key: str,
        ACL: ObjectCannedACLType = None,
        Body: Union[bytes, IO[bytes], StreamingBody] = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentLength: int = None,
        ContentMD5: str = None,
        ContentType: str = None,
        Expires: Union[datetime, str] = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWriteACP: str = None,
        Metadata: Dict[str, str] = None,
        ServerSideEncryption: ServerSideEncryptionType = None,
        StorageClass: StorageClassType = None,
        WebsiteRedirectLocation: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        SSEKMSKeyId: str = None,
        SSEKMSEncryptionContext: str = None,
        BucketKeyEnabled: bool = None,
        RequestPayer: Literal["requester"] = None,
        Tagging: str = None,
        ObjectLockMode: ObjectLockModeType = None,
        ObjectLockRetainUntilDate: Union[datetime, str] = None,
        ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType = None,
        ExpectedBucketOwner: str = None
    ) -> PutObjectOutputTypeDef:
        """
        Adds an object to a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_object)
        """
    def put_object_acl(
        self,
        *,
        Bucket: str,
        Key: str,
        ACL: ObjectCannedACLType = None,
        AccessControlPolicy: "AccessControlPolicyTypeDef" = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
        RequestPayer: Literal["requester"] = None,
        VersionId: str = None,
        ExpectedBucketOwner: str = None
    ) -> PutObjectAclOutputTypeDef:
        """
        Uses the `acl` subresource to set the access control list (ACL) permissions for
        a new or existing object in an S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_object_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_object_acl)
        """
    def put_object_legal_hold(
        self,
        *,
        Bucket: str,
        Key: str,
        LegalHold: "ObjectLockLegalHoldTypeDef" = None,
        RequestPayer: Literal["requester"] = None,
        VersionId: str = None,
        ContentMD5: str = None,
        ExpectedBucketOwner: str = None
    ) -> PutObjectLegalHoldOutputTypeDef:
        """
        Applies a Legal Hold configuration to the specified object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_object_legal_hold)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_object_legal_hold)
        """
    def put_object_lock_configuration(
        self,
        *,
        Bucket: str,
        ObjectLockConfiguration: "ObjectLockConfigurationTypeDef" = None,
        RequestPayer: Literal["requester"] = None,
        Token: str = None,
        ContentMD5: str = None,
        ExpectedBucketOwner: str = None
    ) -> PutObjectLockConfigurationOutputTypeDef:
        """
        Places an Object Lock configuration on the specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_object_lock_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_object_lock_configuration)
        """
    def put_object_retention(
        self,
        *,
        Bucket: str,
        Key: str,
        Retention: "ObjectLockRetentionTypeDef" = None,
        RequestPayer: Literal["requester"] = None,
        VersionId: str = None,
        BypassGovernanceRetention: bool = None,
        ContentMD5: str = None,
        ExpectedBucketOwner: str = None
    ) -> PutObjectRetentionOutputTypeDef:
        """
        Places an Object Retention configuration on an object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_object_retention)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_object_retention)
        """
    def put_object_tagging(
        self,
        *,
        Bucket: str,
        Key: str,
        Tagging: "TaggingTypeDef",
        VersionId: str = None,
        ContentMD5: str = None,
        ExpectedBucketOwner: str = None,
        RequestPayer: Literal["requester"] = None
    ) -> PutObjectTaggingOutputTypeDef:
        """
        Sets the supplied tag-set to an object that already exists in a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_object_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_object_tagging)
        """
    def put_public_access_block(
        self,
        *,
        Bucket: str,
        PublicAccessBlockConfiguration: "PublicAccessBlockConfigurationTypeDef",
        ContentMD5: str = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Creates or modifies the `PublicAccessBlock` configuration for an Amazon S3
        bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.put_public_access_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#put_public_access_block)
        """
    def restore_object(
        self,
        *,
        Bucket: str,
        Key: str,
        VersionId: str = None,
        RestoreRequest: "RestoreRequestTypeDef" = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None
    ) -> RestoreObjectOutputTypeDef:
        """
        Restores an archived copy of an object back into Amazon S3 This action is not
        supported by Amazon S3 on Outposts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.restore_object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#restore_object)
        """
    def select_object_content(
        self,
        *,
        Bucket: str,
        Key: str,
        Expression: str,
        ExpressionType: Literal["SQL"],
        InputSerialization: "InputSerializationTypeDef",
        OutputSerialization: "OutputSerializationTypeDef",
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestProgress: "RequestProgressTypeDef" = None,
        ScanRange: "ScanRangeTypeDef" = None,
        ExpectedBucketOwner: str = None
    ) -> SelectObjectContentOutputTypeDef:
        """
        This action filters the contents of an Amazon S3 object based on a simple
        structured query language (SQL) statement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.select_object_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#select_object_content)
        """
    def upload_file(
        self,
        *,
        Filename: str,
        Bucket: str,
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None
    ) -> None:
        """
        Upload a file to an S3 object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.upload_file)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#upload_file)
        """
    def upload_fileobj(
        self,
        *,
        Fileobj: IO[Any],
        Bucket: str,
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None
    ) -> None:
        """
        Upload a file-like object to S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.upload_fileobj)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#upload_fileobj)
        """
    def upload_part(
        self,
        *,
        Bucket: str,
        Key: str,
        PartNumber: int,
        UploadId: str,
        Body: Union[bytes, IO[bytes], StreamingBody] = None,
        ContentLength: int = None,
        ContentMD5: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None
    ) -> UploadPartOutputTypeDef:
        """
        Uploads a part in a multipart upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.upload_part)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#upload_part)
        """
    def upload_part_copy(
        self,
        *,
        Bucket: str,
        CopySource: Union[str, "CopySourceTypeDef"],
        Key: str,
        PartNumber: int,
        UploadId: str,
        CopySourceIfMatch: str = None,
        CopySourceIfModifiedSince: Union[datetime, str] = None,
        CopySourceIfNoneMatch: str = None,
        CopySourceIfUnmodifiedSince: Union[datetime, str] = None,
        CopySourceRange: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        CopySourceSSECustomerAlgorithm: str = None,
        CopySourceSSECustomerKey: str = None,
        CopySourceSSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
        ExpectedSourceBucketOwner: str = None
    ) -> UploadPartCopyOutputTypeDef:
        """
        Uploads a part by copying data from an existing object as data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.upload_part_copy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#upload_part_copy)
        """
    def write_get_object_response(
        self,
        *,
        RequestRoute: str,
        RequestToken: str,
        Body: Union[bytes, IO[bytes], StreamingBody] = None,
        StatusCode: int = None,
        ErrorCode: str = None,
        ErrorMessage: str = None,
        AcceptRanges: str = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentLength: int = None,
        ContentRange: str = None,
        ContentType: str = None,
        DeleteMarker: bool = None,
        ETag: str = None,
        Expires: Union[datetime, str] = None,
        Expiration: str = None,
        LastModified: Union[datetime, str] = None,
        MissingMeta: int = None,
        Metadata: Dict[str, str] = None,
        ObjectLockMode: ObjectLockModeType = None,
        ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType = None,
        ObjectLockRetainUntilDate: Union[datetime, str] = None,
        PartsCount: int = None,
        ReplicationStatus: ReplicationStatusType = None,
        RequestCharged: Literal["requester"] = None,
        Restore: str = None,
        ServerSideEncryption: ServerSideEncryptionType = None,
        SSECustomerAlgorithm: str = None,
        SSEKMSKeyId: str = None,
        SSECustomerKeyMD5: str = None,
        StorageClass: StorageClassType = None,
        TagCount: int = None,
        VersionId: str = None,
        BucketKeyEnabled: bool = None
    ) -> None:
        """
        Passes transformed objects to a `GetObject` operation when using Object Lambda
        access points.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Client.write_get_object_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/client.html#write_get_object_response)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_multipart_uploads"]
    ) -> ListMultipartUploadsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Paginator.ListMultipartUploads)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/paginators.html#listmultipartuploadspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_object_versions"]
    ) -> ListObjectVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Paginator.ListObjectVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/paginators.html#listobjectversionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_objects"]) -> ListObjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Paginator.ListObjects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/paginators.html#listobjectspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_objects_v2"]) -> ListObjectsV2Paginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Paginator.ListObjectsV2)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/paginators.html#listobjectsv2paginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_parts"]) -> ListPartsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Paginator.ListParts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/paginators.html#listpartspaginator)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["bucket_exists"]) -> BucketExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Waiter.BucketExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/waiters.html#bucketexistswaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["bucket_not_exists"]) -> BucketNotExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Waiter.BucketNotExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/waiters.html#bucketnotexistswaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["object_exists"]) -> ObjectExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Waiter.ObjectExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/waiters.html#objectexistswaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["object_not_exists"]) -> ObjectNotExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Waiter.ObjectNotExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/waiters.html#objectnotexistswaiter)
        """
