"""
Type annotations for s3 service ServiceResource

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_s3 import S3ServiceResource
    import mypy_boto3_s3.service_resource as s3_resources

    resource: S3ServiceResource = boto3.resource("s3")

    my_bucket: s3_resources.Bucket = resource.Bucket(...)
    my_bucket_acl: s3_resources.BucketAcl = resource.BucketAcl(...)
    my_bucket_cors: s3_resources.BucketCors = resource.BucketCors(...)
    my_bucket_lifecycle: s3_resources.BucketLifecycle = resource.BucketLifecycle(...)
    my_bucket_lifecycle_configuration: s3_resources.BucketLifecycleConfiguration = resource.BucketLifecycleConfiguration(...)
    my_bucket_logging: s3_resources.BucketLogging = resource.BucketLogging(...)
    my_bucket_notification: s3_resources.BucketNotification = resource.BucketNotification(...)
    my_bucket_policy: s3_resources.BucketPolicy = resource.BucketPolicy(...)
    my_bucket_request_payment: s3_resources.BucketRequestPayment = resource.BucketRequestPayment(...)
    my_bucket_tagging: s3_resources.BucketTagging = resource.BucketTagging(...)
    my_bucket_versioning: s3_resources.BucketVersioning = resource.BucketVersioning(...)
    my_bucket_website: s3_resources.BucketWebsite = resource.BucketWebsite(...)
    my_multipart_upload: s3_resources.MultipartUpload = resource.MultipartUpload(...)
    my_multipart_upload_part: s3_resources.MultipartUploadPart = resource.MultipartUploadPart(...)
    my_object: s3_resources.Object = resource.Object(...)
    my_object_acl: s3_resources.ObjectAcl = resource.ObjectAcl(...)
    my_object_summary: s3_resources.ObjectSummary = resource.ObjectSummary(...)
    my_object_version: s3_resources.ObjectVersion = resource.ObjectVersion(...)
```
"""
import sys
from datetime import datetime
from typing import IO, Any, Callable, Dict, Iterator, List, Union

from boto3.resources.base import ResourceMeta
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection
from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient
from botocore.response import StreamingBody

from .client import S3Client
from .literals import (
    BucketCannedACLType,
    ChecksumAlgorithmType,
    MetadataDirectiveType,
    ObjectCannedACLType,
    ObjectLockLegalHoldStatusType,
    ObjectLockModeType,
    ObjectOwnershipType,
    ServerSideEncryptionType,
    StorageClassType,
    TaggingDirectiveType,
)
from .type_defs import (
    AbortMultipartUploadOutputTypeDef,
    AccessControlPolicyTypeDef,
    BucketLifecycleConfigurationTypeDef,
    BucketLoggingStatusTypeDef,
    CompletedMultipartUploadTypeDef,
    CopyObjectOutputTypeDef,
    CopySourceTypeDef,
    CORSConfigurationTypeDef,
    CreateBucketConfigurationTypeDef,
    CreateBucketOutputTypeDef,
    DeleteObjectOutputTypeDef,
    DeleteObjectsOutputTypeDef,
    DeleteTypeDef,
    GetObjectOutputTypeDef,
    HeadObjectOutputTypeDef,
    LifecycleConfigurationTypeDef,
    NotificationConfigurationTypeDef,
    PutObjectAclOutputTypeDef,
    PutObjectOutputTypeDef,
    RequestPaymentConfigurationTypeDef,
    RestoreObjectOutputTypeDef,
    RestoreRequestTypeDef,
    TaggingTypeDef,
    UploadPartCopyOutputTypeDef,
    UploadPartOutputTypeDef,
    VersioningConfigurationTypeDef,
    WebsiteConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "S3ServiceResource",
    "Bucket",
    "BucketAcl",
    "BucketCors",
    "BucketLifecycle",
    "BucketLifecycleConfiguration",
    "BucketLogging",
    "BucketNotification",
    "BucketPolicy",
    "BucketRequestPayment",
    "BucketTagging",
    "BucketVersioning",
    "BucketWebsite",
    "MultipartUpload",
    "MultipartUploadPart",
    "Object",
    "ObjectAcl",
    "ObjectSummary",
    "ObjectVersion",
    "ServiceResourceBucketsCollection",
    "BucketMultipartUploadsCollection",
    "BucketObjectVersionsCollection",
    "BucketObjectsCollection",
    "MultipartUploadPartsCollection",
)

class ServiceResourceBucketsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.buckets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#serviceresourcebucketscollection)
    """

    def all(self) -> "ServiceResourceBucketsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """
    def filter(self) -> "ServiceResourceBucketsCollection":  # type: ignore
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """
    def limit(self, count: int) -> "ServiceResourceBucketsCollection":
        """
        Return at most this many Buckets.
        """
    def page_size(self, count: int) -> "ServiceResourceBucketsCollection":
        """
        Fetch at most this many Buckets per service request.
        """
    def pages(self) -> Iterator[List["Bucket"]]:
        """
        A generator which yields pages of Buckets.
        """
    def __iter__(self) -> Iterator["Bucket"]:
        """
        A generator which yields Buckets.
        """

class BucketMultipartUploadsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.multipart_uploads)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketmultipartuploadscollection)
    """

    def all(self) -> "BucketMultipartUploadsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """
    def filter(  # type: ignore
        self,
        *,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
        ExpectedBucketOwner: str = None,
        RequestPayer: Literal["requester"] = None
    ) -> "BucketMultipartUploadsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """
    def limit(self, count: int) -> "BucketMultipartUploadsCollection":
        """
        Return at most this many MultipartUploads.
        """
    def page_size(self, count: int) -> "BucketMultipartUploadsCollection":
        """
        Fetch at most this many MultipartUploads per service request.
        """
    def pages(self) -> Iterator[List["MultipartUpload"]]:
        """
        A generator which yields pages of MultipartUploads.
        """
    def __iter__(self) -> Iterator["MultipartUpload"]:
        """
        A generator which yields MultipartUploads.
        """

class BucketObjectVersionsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.object_versions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketobjectversionscollection)
    """

    def all(self) -> "BucketObjectVersionsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """
    def filter(  # type: ignore
        self,
        *,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        KeyMarker: str = None,
        MaxKeys: int = None,
        Prefix: str = None,
        VersionIdMarker: str = None,
        ExpectedBucketOwner: str = None,
        RequestPayer: Literal["requester"] = None,
        OptionalObjectAttributes: List[Literal["RestoreStatus"]] = None
    ) -> "BucketObjectVersionsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """
    def delete(
        self,
        *,
        MFA: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
        ExpectedBucketOwner: str = None,
        ChecksumAlgorithm: ChecksumAlgorithmType = None
    ) -> DeleteObjectsOutputTypeDef:
        """
        Batch method.
        """
    def limit(self, count: int) -> "BucketObjectVersionsCollection":
        """
        Return at most this many ObjectVersions.
        """
    def page_size(self, count: int) -> "BucketObjectVersionsCollection":
        """
        Fetch at most this many ObjectVersions per service request.
        """
    def pages(self) -> Iterator[List["ObjectVersion"]]:
        """
        A generator which yields pages of ObjectVersions.
        """
    def __iter__(self) -> Iterator["ObjectVersion"]:
        """
        A generator which yields ObjectVersions.
        """

class BucketObjectsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.objects)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketobjectscollection)
    """

    def all(self) -> "BucketObjectsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """
    def filter(  # type: ignore
        self,
        *,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        Marker: str = None,
        MaxKeys: int = None,
        Prefix: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
        OptionalObjectAttributes: List[Literal["RestoreStatus"]] = None
    ) -> "BucketObjectsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """
    def delete(
        self,
        *,
        MFA: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
        ExpectedBucketOwner: str = None,
        ChecksumAlgorithm: ChecksumAlgorithmType = None
    ) -> DeleteObjectsOutputTypeDef:
        """
        Batch method.
        """
    def limit(self, count: int) -> "BucketObjectsCollection":
        """
        Return at most this many ObjectSummarys.
        """
    def page_size(self, count: int) -> "BucketObjectsCollection":
        """
        Fetch at most this many ObjectSummarys per service request.
        """
    def pages(self) -> Iterator[List["ObjectSummary"]]:
        """
        A generator which yields pages of ObjectSummarys.
        """
    def __iter__(self) -> Iterator["ObjectSummary"]:
        """
        A generator which yields ObjectSummarys.
        """

class MultipartUploadPartsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.MultipartUpload.parts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#multipartuploadpartscollection)
    """

    def all(self) -> "MultipartUploadPartsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """
    def filter(  # type: ignore
        self,
        *,
        MaxParts: int = None,
        PartNumberMarker: int = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None
    ) -> "MultipartUploadPartsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """
    def limit(self, count: int) -> "MultipartUploadPartsCollection":
        """
        Return at most this many MultipartUploadParts.
        """
    def page_size(self, count: int) -> "MultipartUploadPartsCollection":
        """
        Fetch at most this many MultipartUploadParts per service request.
        """
    def pages(self) -> Iterator[List["MultipartUploadPart"]]:
        """
        A generator which yields pages of MultipartUploadParts.
        """
    def __iter__(self) -> Iterator["MultipartUploadPart"]:
        """
        A generator which yields MultipartUploadParts.
        """

class BucketAcl(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketAcl)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketacl)
    """

    owner: Dict[str, Any]
    grants: List[Any]
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketAcl.Bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketaclbucket-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketAcl.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketaclget_available_subresources-method)
        """
    def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_acl` to update the attributes of the
        BucketAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketAcl.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketaclload-method)
        """
    def put(
        self,
        *,
        ACL: BucketCannedACLType = None,
        AccessControlPolicy: "AccessControlPolicyTypeDef" = None,
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Sets the permissions on an existing bucket using access control lists (ACL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketAcl.put)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketaclput-method)
        """
    def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_acl` to update the attributes of the
        BucketAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketAcl.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketaclreload-method)
        """

_BucketAcl = BucketAcl

class BucketCors(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketCors)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketcors)
    """

    cors_rules: List[Any]
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketCors.Bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketcorsbucket-method)
        """
    def delete(self, *, ExpectedBucketOwner: str = None) -> None:
        """
        Deletes the `cors` configuration information set for the bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketCors.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketcorsdelete-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketCors.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketcorsget_available_subresources-method)
        """
    def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_cors` to update the attributes of the
        BucketCors resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketCors.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketcorsload-method)
        """
    def put(
        self,
        *,
        CORSConfiguration: "CORSConfigurationTypeDef",
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Sets the `cors` configuration for your bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketCors.put)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketcorsput-method)
        """
    def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_cors` to update the attributes of the
        BucketCors resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketCors.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketcorsreload-method)
        """

_BucketCors = BucketCors

class BucketLifecycle(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketLifecycle)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketlifecycle)
    """

    rules: List[Any]
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketLifecycle.Bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketlifecyclebucket-method)
        """
    def delete(self, *, ExpectedBucketOwner: str = None) -> None:
        """
        Deletes the lifecycle configuration from the specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketLifecycle.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketlifecycledelete-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketLifecycle.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketlifecycleget_available_subresources-method)
        """
    def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_lifecycle` to update the attributes of the
        BucketLifecycle resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketLifecycle.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketlifecycleload-method)
        """
    def put(
        self,
        *,
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
        LifecycleConfiguration: "LifecycleConfigurationTypeDef" = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketLifecycle.put)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketlifecycleput-method)
        """
    def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_lifecycle` to update the attributes of the
        BucketLifecycle resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketLifecycle.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketlifecyclereload-method)
        """

_BucketLifecycle = BucketLifecycle

class BucketLifecycleConfiguration(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketLifecycleConfiguration)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketlifecycleconfiguration)
    """

    rules: List[Any]
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketLifecycleConfiguration.Bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketlifecycleconfigurationbucket-method)
        """
    def delete(self, *, ExpectedBucketOwner: str = None) -> None:
        """
        Deletes the lifecycle configuration from the specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketLifecycleConfiguration.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketlifecycleconfigurationdelete-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketLifecycleConfiguration.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketlifecycleconfigurationget_available_subresources-method)
        """
    def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_lifecycle_configuration` to update the
        attributes of the BucketLifecycleConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketLifecycleConfiguration.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketlifecycleconfigurationload-method)
        """
    def put(
        self,
        *,
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
        LifecycleConfiguration: "BucketLifecycleConfigurationTypeDef" = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Creates a new lifecycle configuration for the bucket or replaces an existing
        lifecycle configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketLifecycleConfiguration.put)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketlifecycleconfigurationput-method)
        """
    def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_lifecycle_configuration` to update the
        attributes of the BucketLifecycleConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketLifecycleConfiguration.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketlifecycleconfigurationreload-method)
        """

_BucketLifecycleConfiguration = BucketLifecycleConfiguration

class BucketLogging(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketLogging)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketlogging)
    """

    logging_enabled: Dict[str, Any]
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketLogging.Bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketloggingbucket-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketLogging.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketloggingget_available_subresources-method)
        """
    def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_logging` to update the attributes of the
        BucketLogging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketLogging.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketloggingload-method)
        """
    def put(
        self,
        *,
        BucketLoggingStatus: "BucketLoggingStatusTypeDef",
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Set the logging parameters for a bucket and to specify permissions for who can
        view and modify the logging parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketLogging.put)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketloggingput-method)
        """
    def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_logging` to update the attributes of the
        BucketLogging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketLogging.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketloggingreload-method)
        """

_BucketLogging = BucketLogging

class BucketNotification(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketNotification)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketnotification)
    """

    topic_configurations: List[Any]
    queue_configurations: List[Any]
    lambda_function_configurations: List[Any]
    event_bridge_configuration: Dict[str, Any]
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketNotification.Bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketnotificationbucket-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketNotification.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketnotificationget_available_subresources-method)
        """
    def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_notification_configuration` to update the
        attributes of the BucketNotification resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketNotification.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketnotificationload-method)
        """
    def put(
        self,
        *,
        NotificationConfiguration: "NotificationConfigurationTypeDef",
        ExpectedBucketOwner: str = None,
        SkipDestinationValidation: bool = None
    ) -> None:
        """
        Enables notifications of specified events for a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketNotification.put)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketnotificationput-method)
        """
    def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_notification_configuration` to update the
        attributes of the BucketNotification resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketNotification.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketnotificationreload-method)
        """

_BucketNotification = BucketNotification

class BucketPolicy(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketPolicy)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketpolicy)
    """

    policy: str
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketPolicy.Bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketpolicybucket-method)
        """
    def delete(self, *, ExpectedBucketOwner: str = None) -> None:
        """
        This implementation of the DELETE action uses the policy subresource to delete
        the policy of a specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketPolicy.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketpolicydelete-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketPolicy.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketpolicyget_available_subresources-method)
        """
    def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_policy` to update the attributes of the
        BucketPolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketPolicy.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketpolicyload-method)
        """
    def put(
        self,
        *,
        Policy: str,
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
        ConfirmRemoveSelfBucketAccess: bool = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Applies an Amazon S3 bucket policy to an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketPolicy.put)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketpolicyput-method)
        """
    def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_policy` to update the attributes of the
        BucketPolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketPolicy.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketpolicyreload-method)
        """

_BucketPolicy = BucketPolicy

class BucketRequestPayment(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketRequestPayment)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketrequestpayment)
    """

    payer: str
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketRequestPayment.Bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketrequestpaymentbucket-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketRequestPayment.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketrequestpaymentget_available_subresources-method)
        """
    def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_request_payment` to update the attributes
        of the BucketRequestPayment resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketRequestPayment.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketrequestpaymentload-method)
        """
    def put(
        self,
        *,
        RequestPaymentConfiguration: "RequestPaymentConfigurationTypeDef",
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Sets the request payment configuration for a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketRequestPayment.put)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketrequestpaymentput-method)
        """
    def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_request_payment` to update the attributes
        of the BucketRequestPayment resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketRequestPayment.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketrequestpaymentreload-method)
        """

_BucketRequestPayment = BucketRequestPayment

class BucketTagging(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketTagging)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#buckettagging)
    """

    tag_set: List[Any]
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketTagging.Bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#buckettaggingbucket-method)
        """
    def delete(self, *, ExpectedBucketOwner: str = None) -> None:
        """
        Deletes the tags from the bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketTagging.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#buckettaggingdelete-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketTagging.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#buckettaggingget_available_subresources-method)
        """
    def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_tagging` to update the attributes of the
        BucketTagging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketTagging.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#buckettaggingload-method)
        """
    def put(
        self,
        *,
        Tagging: "TaggingTypeDef",
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Sets the tags for a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketTagging.put)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#buckettaggingput-method)
        """
    def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_tagging` to update the attributes of the
        BucketTagging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketTagging.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#buckettaggingreload-method)
        """

_BucketTagging = BucketTagging

class BucketVersioning(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketVersioning)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketversioning)
    """

    status: str
    mfa_delete: str
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketVersioning.Bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketversioningbucket-method)
        """
    def enable(
        self,
        *,
        VersioningConfiguration: "VersioningConfigurationTypeDef",
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
        MFA: str = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Sets the versioning state of an existing bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketVersioning.enable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketversioningenable-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketVersioning.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketversioningget_available_subresources-method)
        """
    def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_versioning` to update the attributes of the
        BucketVersioning resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketVersioning.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketversioningload-method)
        """
    def put(
        self,
        *,
        VersioningConfiguration: "VersioningConfigurationTypeDef",
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
        MFA: str = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Sets the versioning state of an existing bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketVersioning.put)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketversioningput-method)
        """
    def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_versioning` to update the attributes of the
        BucketVersioning resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketVersioning.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketversioningreload-method)
        """
    def suspend(
        self,
        *,
        VersioningConfiguration: "VersioningConfigurationTypeDef",
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
        MFA: str = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Sets the versioning state of an existing bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketVersioning.suspend)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketversioningsuspend-method)
        """

_BucketVersioning = BucketVersioning

class BucketWebsite(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketWebsite)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketwebsite)
    """

    redirect_all_requests_to: Dict[str, Any]
    index_document: Dict[str, Any]
    error_document: Dict[str, Any]
    routing_rules: List[Any]
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketWebsite.Bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketwebsitebucket-method)
        """
    def delete(self, *, ExpectedBucketOwner: str = None) -> None:
        """
        This action removes the website configuration for a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketWebsite.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketwebsitedelete-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketWebsite.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketwebsiteget_available_subresources-method)
        """
    def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_website` to update the attributes of the
        BucketWebsite resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketWebsite.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketwebsiteload-method)
        """
    def put(
        self,
        *,
        WebsiteConfiguration: "WebsiteConfigurationTypeDef",
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
        ExpectedBucketOwner: str = None
    ) -> None:
        """
        Sets the configuration of the website that is specified in the `website`
        subresource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketWebsite.put)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketwebsiteput-method)
        """
    def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_website` to update the attributes of the
        BucketWebsite resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.BucketWebsite.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketwebsitereload-method)
        """

_BucketWebsite = BucketWebsite

class MultipartUploadPart(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.MultipartUploadPart)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#multipartuploadpart)
    """

    last_modified: datetime
    e_tag: str
    size: int
    checksum_crc32: str
    checksum_crc32_c: str
    checksum_sha1: str
    checksum_sha256: str
    bucket_name: str
    object_key: str
    multipart_upload_id: str
    part_number: str

    def MultipartUpload(self) -> "_MultipartUpload":
        """
        Creates a MultipartUpload resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.MultipartUploadPart.MultipartUpload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#multipartuploadpartmultipartupload-method)
        """
    def copy_from(
        self,
        *,
        CopySource: str,
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.MultipartUploadPart.copy_from)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#multipartuploadpartcopy_from-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.MultipartUploadPart.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#multipartuploadpartget_available_subresources-method)
        """
    def upload(
        self,
        *,
        Body: Union[bytes, IO[bytes], StreamingBody] = None,
        ContentLength: int = None,
        ContentMD5: str = None,
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
        ChecksumCRC32: str = None,
        ChecksumCRC32C: str = None,
        ChecksumSHA1: str = None,
        ChecksumSHA256: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None
    ) -> UploadPartOutputTypeDef:
        """
        Uploads a part in a multipart upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.MultipartUploadPart.upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#multipartuploadpartupload-method)
        """

_MultipartUploadPart = MultipartUploadPart

class ObjectAcl(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.ObjectAcl)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectacl)
    """

    owner: Dict[str, Any]
    grants: List[Any]
    request_charged: str
    bucket_name: str
    object_key: str

    def Object(self) -> "_Object":
        """
        Creates a Object resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectAcl.Object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectaclobject-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectAcl.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectaclget_available_subresources-method)
        """
    def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_object_acl` to update the attributes of the
        ObjectAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectAcl.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectaclload-method)
        """
    def put(
        self,
        *,
        ACL: ObjectCannedACLType = None,
        AccessControlPolicy: "AccessControlPolicyTypeDef" = None,
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectAcl.put)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectaclput-method)
        """
    def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_object_acl` to update the attributes of the
        ObjectAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectAcl.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectaclreload-method)
        """

_ObjectAcl = ObjectAcl

class ObjectVersion(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.ObjectVersion)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectversion)
    """

    e_tag: str
    checksum_algorithm: List[Any]
    size: int
    storage_class: str
    key: str
    version_id: str
    is_latest: bool
    last_modified: datetime
    owner: Dict[str, Any]
    restore_status: Dict[str, Any]
    bucket_name: str
    object_key: str
    id: str

    def Object(self) -> "_Object":
        """
        Creates a Object resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectVersion.Object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectversionobject-method)
        """
    def delete(
        self,
        *,
        MFA: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
        ExpectedBucketOwner: str = None
    ) -> DeleteObjectOutputTypeDef:
        """
        Removes the null version (if there is one) of an object and inserts a delete
        marker, which becomes the latest version of the object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectVersion.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectversiondelete-method)
        """
    def get(
        self,
        *,
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
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        PartNumber: int = None,
        ExpectedBucketOwner: str = None,
        ChecksumMode: Literal["ENABLED"] = None
    ) -> GetObjectOutputTypeDef:
        """
        Retrieves objects from Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectVersion.get)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectversionget-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectVersion.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectversionget_available_subresources-method)
        """
    def head(
        self,
        *,
        IfMatch: str = None,
        IfModifiedSince: Union[datetime, str] = None,
        IfNoneMatch: str = None,
        IfUnmodifiedSince: Union[datetime, str] = None,
        Range: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        PartNumber: int = None,
        ExpectedBucketOwner: str = None,
        ChecksumMode: Literal["ENABLED"] = None
    ) -> HeadObjectOutputTypeDef:
        """
        The `HEAD` action retrieves metadata from an object without returning the object
        itself.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectVersion.head)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectversionhead-method)
        """

_ObjectVersion = ObjectVersion

class MultipartUpload(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.MultipartUpload)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#multipartupload)
    """

    upload_id: str
    key: str
    initiated: datetime
    storage_class: str
    owner: Dict[str, Any]
    initiator: Dict[str, Any]
    checksum_algorithm: str
    bucket_name: str
    object_key: str
    id: str
    parts: MultipartUploadPartsCollection

    def Object(self) -> "_Object":
        """
        Creates a Object resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.MultipartUpload.Object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#multipartuploadobject-method)
        """
    def Part(self, part_number: str) -> _MultipartUploadPart:
        """
        Creates a MultipartUploadPart resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.MultipartUpload.Part)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#multipartuploadpart-method)
        """
    def abort(
        self, *, RequestPayer: Literal["requester"] = None, ExpectedBucketOwner: str = None
    ) -> AbortMultipartUploadOutputTypeDef:
        """
        This action aborts a multipart upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.MultipartUpload.abort)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#multipartuploadabort-method)
        """
    def complete(
        self,
        *,
        MultipartUpload: "CompletedMultipartUploadTypeDef" = None,
        ChecksumCRC32: str = None,
        ChecksumCRC32C: str = None,
        ChecksumSHA1: str = None,
        ChecksumSHA256: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None
    ) -> "_Object":
        """
        Completes a multipart upload by assembling previously uploaded parts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.MultipartUpload.complete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#multipartuploadcomplete-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.MultipartUpload.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#multipartuploadget_available_subresources-method)
        """

_MultipartUpload = MultipartUpload

class Object(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.Object)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#object)
    """

    delete_marker: bool
    accept_ranges: str
    expiration: str
    restore: str
    archive_status: str
    last_modified: datetime
    content_length: int
    checksum_crc32: str
    checksum_crc32_c: str
    checksum_sha1: str
    checksum_sha256: str
    e_tag: str
    missing_meta: int
    version_id: str
    cache_control: str
    content_disposition: str
    content_encoding: str
    content_language: str
    content_type: str
    expires: datetime
    website_redirect_location: str
    server_side_encryption: str
    metadata: Dict[str, Any]
    sse_customer_algorithm: str
    sse_customer_key_md5: str
    ssekms_key_id: str
    bucket_key_enabled: bool
    storage_class: str
    request_charged: str
    replication_status: str
    parts_count: int
    object_lock_mode: str
    object_lock_retain_until_date: datetime
    object_lock_legal_hold_status: str
    bucket_name: str
    key: str

    def Acl(self) -> _ObjectAcl:
        """
        Creates a ObjectAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Object.Acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectacl-method)
        """
    def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Object.Bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectbucket-method)
        """
    def MultipartUpload(self, id: str) -> _MultipartUpload:
        """
        Creates a MultipartUpload resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Object.MultipartUpload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectmultipartupload-method)
        """
    def Version(self, id: str) -> _ObjectVersion:
        """
        Creates a ObjectVersion resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Object.Version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectversion-method)
        """
    def copy(
        self,
        *,
        CopySource: "CopySourceTypeDef",
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        SourceClient: BaseClient = None,
        Config: TransferConfig = None
    ) -> None:
        """
        Copy an object from one S3 location to this object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Object.copy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectcopy-method)
        """
    def copy_from(
        self,
        *,
        CopySource: str,
        ACL: ObjectCannedACLType = None,
        CacheControl: str = None,
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Object.copy_from)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectcopy_from-method)
        """
    def delete(
        self,
        *,
        MFA: str = None,
        VersionId: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
        ExpectedBucketOwner: str = None
    ) -> DeleteObjectOutputTypeDef:
        """
        Removes the null version (if there is one) of an object and inserts a delete
        marker, which becomes the latest version of the object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Object.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectdelete-method)
        """
    def download_file(
        self,
        *,
        Filename: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None
    ) -> None:
        """
        Download an S3 object to a file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Object.download_file)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectdownload_file-method)
        """
    def download_fileobj(
        self,
        *,
        Fileobj: IO[Any],
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None
    ) -> None:
        """
        Download this object from S3 to a file-like object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Object.download_fileobj)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectdownload_fileobj-method)
        """
    def get(
        self,
        *,
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
        ExpectedBucketOwner: str = None,
        ChecksumMode: Literal["ENABLED"] = None
    ) -> GetObjectOutputTypeDef:
        """
        Retrieves objects from Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Object.get)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectget-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Object.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectget_available_subresources-method)
        """
    def initiate_multipart_upload(
        self,
        *,
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
        ExpectedBucketOwner: str = None,
        ChecksumAlgorithm: ChecksumAlgorithmType = None
    ) -> _MultipartUpload:
        """
        This action initiates a multipart upload and returns an upload ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Object.initiate_multipart_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectinitiate_multipart_upload-method)
        """
    def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.head_object` to update the attributes of the Object
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Object.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectload-method)
        """
    def put(
        self,
        *,
        ACL: ObjectCannedACLType = None,
        Body: Union[bytes, IO[bytes], StreamingBody] = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentLength: int = None,
        ContentMD5: str = None,
        ContentType: str = None,
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
        ChecksumCRC32: str = None,
        ChecksumCRC32C: str = None,
        ChecksumSHA1: str = None,
        ChecksumSHA256: str = None,
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Object.put)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectput-method)
        """
    def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.head_object` to update the attributes of the Object
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Object.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectreload-method)
        """
    def restore_object(
        self,
        *,
        VersionId: str = None,
        RestoreRequest: "RestoreRequestTypeDef" = None,
        RequestPayer: Literal["requester"] = None,
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
        ExpectedBucketOwner: str = None
    ) -> RestoreObjectOutputTypeDef:
        """
        Restores an archived copy of an object back into Amazon S3 This action is not
        supported by Amazon S3 on Outposts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Object.restore_object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectrestore_object-method)
        """
    def upload_file(
        self,
        *,
        Filename: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None
    ) -> None:
        """
        Upload a file to an S3 object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Object.upload_file)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectupload_file-method)
        """
    def upload_fileobj(
        self,
        *,
        Fileobj: IO[Any],
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None
    ) -> None:
        """
        Upload a file-like object to this object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Object.upload_fileobj)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectupload_fileobj-method)
        """
    def wait_until_exists(self) -> None:
        """
        Waits until this Object is exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Object.wait_until_exists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectwait_until_exists-method)
        """
    def wait_until_not_exists(self) -> None:
        """
        Waits until this Object is not exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Object.wait_until_not_exists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectwait_until_not_exists-method)
        """

_Object = Object

class ObjectSummary(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.ObjectSummary)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectsummary)
    """

    last_modified: datetime
    e_tag: str
    checksum_algorithm: List[Any]
    size: int
    storage_class: str
    owner: Dict[str, Any]
    restore_status: Dict[str, Any]
    bucket_name: str
    key: str

    def Acl(self) -> _ObjectAcl:
        """
        Creates a ObjectAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectSummary.Acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectsummaryacl-method)
        """
    def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectSummary.Bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectsummarybucket-method)
        """
    def MultipartUpload(self, id: str) -> _MultipartUpload:
        """
        Creates a MultipartUpload resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectSummary.MultipartUpload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectsummarymultipartupload-method)
        """
    def Object(self) -> _Object:
        """
        Creates a Object resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectSummary.Object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectsummaryobject-method)
        """
    def Version(self, id: str) -> _ObjectVersion:
        """
        Creates a ObjectVersion resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectSummary.Version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectsummaryversion-method)
        """
    def copy_from(
        self,
        *,
        CopySource: str,
        ACL: ObjectCannedACLType = None,
        CacheControl: str = None,
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectSummary.copy_from)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectsummarycopy_from-method)
        """
    def delete(
        self,
        *,
        MFA: str = None,
        VersionId: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
        ExpectedBucketOwner: str = None
    ) -> DeleteObjectOutputTypeDef:
        """
        Removes the null version (if there is one) of an object and inserts a delete
        marker, which becomes the latest version of the object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectSummary.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectsummarydelete-method)
        """
    def get(
        self,
        *,
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
        ExpectedBucketOwner: str = None,
        ChecksumMode: Literal["ENABLED"] = None
    ) -> GetObjectOutputTypeDef:
        """
        Retrieves objects from Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectSummary.get)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectsummaryget-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectSummary.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectsummaryget_available_subresources-method)
        """
    def initiate_multipart_upload(
        self,
        *,
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
        ExpectedBucketOwner: str = None,
        ChecksumAlgorithm: ChecksumAlgorithmType = None
    ) -> _MultipartUpload:
        """
        This action initiates a multipart upload and returns an upload ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectSummary.initiate_multipart_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectsummaryinitiate_multipart_upload-method)
        """
    def load(self) -> None:
        """
        Calls s3.Client.head_object to update the attributes of the ObjectSummary
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectSummary.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectsummaryload-method)
        """
    def put(
        self,
        *,
        ACL: ObjectCannedACLType = None,
        Body: Union[bytes, IO[bytes], StreamingBody] = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentLength: int = None,
        ContentMD5: str = None,
        ContentType: str = None,
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
        ChecksumCRC32: str = None,
        ChecksumCRC32C: str = None,
        ChecksumSHA1: str = None,
        ChecksumSHA256: str = None,
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectSummary.put)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectsummaryput-method)
        """
    def restore_object(
        self,
        *,
        VersionId: str = None,
        RestoreRequest: "RestoreRequestTypeDef" = None,
        RequestPayer: Literal["requester"] = None,
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
        ExpectedBucketOwner: str = None
    ) -> RestoreObjectOutputTypeDef:
        """
        Restores an archived copy of an object back into Amazon S3 This action is not
        supported by Amazon S3 on Outposts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectSummary.restore_object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectsummaryrestore_object-method)
        """
    def wait_until_exists(self) -> None:
        """
        Waits until this ObjectSummary is exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectSummary.wait_until_exists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectsummarywait_until_exists-method)
        """
    def wait_until_not_exists(self) -> None:
        """
        Waits until this ObjectSummary is not exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ObjectSummary.wait_until_not_exists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#objectsummarywait_until_not_exists-method)
        """

_ObjectSummary = ObjectSummary

class Bucket(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.Bucket)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucket)
    """

    creation_date: datetime
    name: str
    multipart_uploads: BucketMultipartUploadsCollection
    object_versions: BucketObjectVersionsCollection
    objects: BucketObjectsCollection

    def Acl(self) -> _BucketAcl:
        """
        Creates a BucketAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.Acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketacl-method)
        """
    def Cors(self) -> _BucketCors:
        """
        Creates a BucketCors resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.Cors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketcors-method)
        """
    def Lifecycle(self) -> _BucketLifecycle:
        """
        Creates a BucketLifecycle resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.Lifecycle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketlifecycle-method)
        """
    def LifecycleConfiguration(self) -> _BucketLifecycleConfiguration:
        """
        Creates a BucketLifecycleConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.LifecycleConfiguration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketlifecycleconfiguration-method)
        """
    def Logging(self) -> _BucketLogging:
        """
        Creates a BucketLogging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.Logging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketlogging-method)
        """
    def Notification(self) -> _BucketNotification:
        """
        Creates a BucketNotification resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.Notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketnotification-method)
        """
    def Object(self, key: str) -> _Object:
        """
        Creates a Object resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.Object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketobject-method)
        """
    def Policy(self) -> _BucketPolicy:
        """
        Creates a BucketPolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.Policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketpolicy-method)
        """
    def RequestPayment(self) -> _BucketRequestPayment:
        """
        Creates a BucketRequestPayment resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.RequestPayment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketrequestpayment-method)
        """
    def Tagging(self) -> _BucketTagging:
        """
        Creates a BucketTagging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.Tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#buckettagging-method)
        """
    def Versioning(self) -> _BucketVersioning:
        """
        Creates a BucketVersioning resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.Versioning)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketversioning-method)
        """
    def Website(self) -> _BucketWebsite:
        """
        Creates a BucketWebsite resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.Website)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketwebsite-method)
        """
    def copy(
        self,
        *,
        CopySource: "CopySourceTypeDef",
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        SourceClient: BaseClient = None,
        Config: TransferConfig = None
    ) -> None:
        """
        Copy an object from one S3 location to an object in this bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.copy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketcopy-method)
        """
    def create(
        self,
        *,
        ACL: BucketCannedACLType = None,
        CreateBucketConfiguration: "CreateBucketConfigurationTypeDef" = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
        ObjectLockEnabledForBucket: bool = None,
        ObjectOwnership: ObjectOwnershipType = None
    ) -> CreateBucketOutputTypeDef:
        """
        Creates a new S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.create)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketcreate-method)
        """
    def delete(self, *, ExpectedBucketOwner: str = None) -> None:
        """
        Deletes the S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketdelete-method)
        """
    def delete_objects(
        self,
        *,
        Delete: "DeleteTypeDef",
        MFA: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
        ExpectedBucketOwner: str = None,
        ChecksumAlgorithm: ChecksumAlgorithmType = None
    ) -> DeleteObjectsOutputTypeDef:
        """
        This action enables you to delete multiple objects from a bucket using a single
        HTTP request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.delete_objects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketdelete_objects-method)
        """
    def download_file(
        self,
        *,
        Key: str,
        Filename: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None
    ) -> None:
        """
        Download an S3 object to a file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.download_file)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketdownload_file-method)
        """
    def download_fileobj(
        self,
        *,
        Key: str,
        Fileobj: IO[Any],
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None
    ) -> None:
        """
        Download an object from this bucket to a file-like-object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.download_fileobj)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketdownload_fileobj-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketget_available_subresources-method)
        """
    def load(self) -> None:
        """
        Calls s3.Client.list_buckets() to update the attributes of the Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketload-method)
        """
    def put_object(
        self,
        *,
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
        ChecksumAlgorithm: ChecksumAlgorithmType = None,
        ChecksumCRC32: str = None,
        ChecksumCRC32C: str = None,
        ChecksumSHA1: str = None,
        ChecksumSHA256: str = None,
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
    ) -> _Object:
        """
        Adds an object to a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.put_object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketput_object-method)
        """
    def upload_file(
        self,
        *,
        Filename: str,
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None
    ) -> None:
        """
        Upload a file to an S3 object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.upload_file)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketupload_file-method)
        """
    def upload_fileobj(
        self,
        *,
        Fileobj: IO[Any],
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None
    ) -> None:
        """
        Upload a file-like object to this bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.upload_fileobj)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketupload_fileobj-method)
        """
    def wait_until_exists(self) -> None:
        """
        Waits until this Bucket is exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.wait_until_exists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketwait_until_exists-method)
        """
    def wait_until_not_exists(self) -> None:
        """
        Waits until this Bucket is not exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.Bucket.wait_until_not_exists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#bucketwait_until_not_exists-method)
        """

_Bucket = Bucket

class S3ResourceMeta(ResourceMeta):
    client: S3Client

class S3ServiceResource(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html)
    """

    meta: "S3ResourceMeta"
    buckets: ServiceResourceBucketsCollection

    def Bucket(self, name: str) -> _Bucket:
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.Bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#s3serviceresourcebucket-method)
        """
    def BucketAcl(self, bucket_name: str) -> _BucketAcl:
        """
        Creates a BucketAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketAcl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#s3serviceresourcebucketacl-method)
        """
    def BucketCors(self, bucket_name: str) -> _BucketCors:
        """
        Creates a BucketCors resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketCors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#s3serviceresourcebucketcors-method)
        """
    def BucketLifecycle(self, bucket_name: str) -> _BucketLifecycle:
        """
        Creates a BucketLifecycle resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketLifecycle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#s3serviceresourcebucketlifecycle-method)
        """
    def BucketLifecycleConfiguration(self, bucket_name: str) -> _BucketLifecycleConfiguration:
        """
        Creates a BucketLifecycleConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketLifecycleConfiguration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#s3serviceresourcebucketlifecycleconfiguration-method)
        """
    def BucketLogging(self, bucket_name: str) -> _BucketLogging:
        """
        Creates a BucketLogging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketLogging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#s3serviceresourcebucketlogging-method)
        """
    def BucketNotification(self, bucket_name: str) -> _BucketNotification:
        """
        Creates a BucketNotification resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketNotification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#s3serviceresourcebucketnotification-method)
        """
    def BucketPolicy(self, bucket_name: str) -> _BucketPolicy:
        """
        Creates a BucketPolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketPolicy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#s3serviceresourcebucketpolicy-method)
        """
    def BucketRequestPayment(self, bucket_name: str) -> _BucketRequestPayment:
        """
        Creates a BucketRequestPayment resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketRequestPayment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#s3serviceresourcebucketrequestpayment-method)
        """
    def BucketTagging(self, bucket_name: str) -> _BucketTagging:
        """
        Creates a BucketTagging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketTagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#s3serviceresourcebuckettagging-method)
        """
    def BucketVersioning(self, bucket_name: str) -> _BucketVersioning:
        """
        Creates a BucketVersioning resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketVersioning)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#s3serviceresourcebucketversioning-method)
        """
    def BucketWebsite(self, bucket_name: str) -> _BucketWebsite:
        """
        Creates a BucketWebsite resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.BucketWebsite)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#s3serviceresourcebucketwebsite-method)
        """
    def MultipartUpload(self, bucket_name: str, object_key: str, id: str) -> _MultipartUpload:
        """
        Creates a MultipartUpload resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.MultipartUpload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#s3serviceresourcemultipartupload-method)
        """
    def MultipartUploadPart(
        self, bucket_name: str, object_key: str, multipart_upload_id: str, part_number: str
    ) -> _MultipartUploadPart:
        """
        Creates a MultipartUploadPart resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.MultipartUploadPart)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#s3serviceresourcemultipartuploadpart-method)
        """
    def Object(self, bucket_name: str, key: str) -> _Object:
        """
        Creates a Object resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.Object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#s3serviceresourceobject-method)
        """
    def ObjectAcl(self, bucket_name: str, object_key: str) -> _ObjectAcl:
        """
        Creates a ObjectAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.ObjectAcl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#s3serviceresourceobjectacl-method)
        """
    def ObjectSummary(self, bucket_name: str, key: str) -> _ObjectSummary:
        """
        Creates a ObjectSummary resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.ObjectSummary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#s3serviceresourceobjectsummary-method)
        """
    def ObjectVersion(self, bucket_name: str, object_key: str, id: str) -> _ObjectVersion:
        """
        Creates a ObjectVersion resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.ObjectVersion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#s3serviceresourceobjectversion-method)
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
        ObjectLockEnabledForBucket: bool = None,
        ObjectOwnership: ObjectOwnershipType = None
    ) -> _Bucket:
        """
        Creates a new S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.create_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#s3serviceresourcecreate_bucket-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3.html#S3.ServiceResource.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/service_resource.html#s3serviceresourceget_available_subresources-method)
        """
