# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for s3 service ServiceResource

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

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection
from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient

from mypy_boto3_s3.type_defs import (
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
    [ServiceResource.buckets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.buckets)
    """

    def all(self) -> "ServiceResourceBucketsCollection":
        pass

    def filter(self) -> "ServiceResourceBucketsCollection":  # type: ignore
        pass

    def limit(self, count: int) -> "ServiceResourceBucketsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceBucketsCollection":
        pass

    def pages(self) -> Iterator[List["Bucket"]]:
        pass

    def __iter__(self) -> Iterator["Bucket"]:
        pass


class BucketMultipartUploadsCollection(ResourceCollection):
    """
    [Bucket.multipart_uploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.multipart_uploads)
    """

    def all(self) -> "BucketMultipartUploadsCollection":
        pass

    def filter(  # type: ignore
        self,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
        ExpectedBucketOwner: str = None,
    ) -> "BucketMultipartUploadsCollection":
        pass

    def limit(self, count: int) -> "BucketMultipartUploadsCollection":
        pass

    def page_size(self, count: int) -> "BucketMultipartUploadsCollection":
        pass

    def pages(self) -> Iterator[List["MultipartUpload"]]:
        pass

    def __iter__(self) -> Iterator["MultipartUpload"]:
        pass


class BucketObjectVersionsCollection(ResourceCollection):
    """
    [Bucket.object_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.object_versions)
    """

    def all(self) -> "BucketObjectVersionsCollection":
        pass

    def filter(  # type: ignore
        self,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        KeyMarker: str = None,
        MaxKeys: int = None,
        Prefix: str = None,
        VersionIdMarker: str = None,
        ExpectedBucketOwner: str = None,
    ) -> "BucketObjectVersionsCollection":
        pass

    def delete(
        self,
        MFA: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
        ExpectedBucketOwner: str = None,
    ) -> DeleteObjectsOutputTypeDef:
        pass

    def limit(self, count: int) -> "BucketObjectVersionsCollection":
        pass

    def page_size(self, count: int) -> "BucketObjectVersionsCollection":
        pass

    def pages(self) -> Iterator[List["ObjectVersion"]]:
        pass

    def __iter__(self) -> Iterator["ObjectVersion"]:
        pass


class BucketObjectsCollection(ResourceCollection):
    """
    [Bucket.objects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.objects)
    """

    def all(self) -> "BucketObjectsCollection":
        pass

    def filter(  # type: ignore
        self,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        Marker: str = None,
        MaxKeys: int = None,
        Prefix: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
    ) -> "BucketObjectsCollection":
        pass

    def delete(
        self,
        MFA: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
        ExpectedBucketOwner: str = None,
    ) -> DeleteObjectsOutputTypeDef:
        pass

    def limit(self, count: int) -> "BucketObjectsCollection":
        pass

    def page_size(self, count: int) -> "BucketObjectsCollection":
        pass

    def pages(self) -> Iterator[List["ObjectSummary"]]:
        pass

    def __iter__(self) -> Iterator["ObjectSummary"]:
        pass


class MultipartUploadPartsCollection(ResourceCollection):
    """
    [MultipartUpload.parts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.MultipartUpload.parts)
    """

    def all(self) -> "MultipartUploadPartsCollection":
        pass

    def filter(  # type: ignore
        self,
        MaxParts: int = None,
        PartNumberMarker: int = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
    ) -> "MultipartUploadPartsCollection":
        pass

    def limit(self, count: int) -> "MultipartUploadPartsCollection":
        pass

    def page_size(self, count: int) -> "MultipartUploadPartsCollection":
        pass

    def pages(self) -> Iterator[List["MultipartUploadPart"]]:
        pass

    def __iter__(self) -> Iterator["MultipartUploadPart"]:
        pass


class BucketAcl(Boto3ServiceResource):
    """
    [BucketAcl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketAcl)
    """

    owner: Dict[str, Any]
    grants: List[Any]
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        [BucketAcl.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketAcl.Bucket)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [BucketAcl.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketAcl.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketAcl.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketAcl.load)
        """

    def put(
        self,
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
        [BucketAcl.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketAcl.put)
        """

    def reload(self) -> None:
        """
        [BucketAcl.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketAcl.reload)
        """


_BucketAcl = BucketAcl


class BucketCors(Boto3ServiceResource):
    """
    [BucketCors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketCors)
    """

    cors_rules: List[Any]
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        [BucketCors.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketCors.Bucket)
        """

    def delete(self, ExpectedBucketOwner: str = None) -> None:
        """
        [BucketCors.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketCors.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [BucketCors.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketCors.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketCors.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketCors.load)
        """

    def put(
        self, CORSConfiguration: CORSConfigurationTypeDef, ExpectedBucketOwner: str = None
    ) -> None:
        """
        [BucketCors.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketCors.put)
        """

    def reload(self) -> None:
        """
        [BucketCors.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketCors.reload)
        """


_BucketCors = BucketCors


class BucketLifecycle(Boto3ServiceResource):
    """
    [BucketLifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketLifecycle)
    """

    rules: List[Any]
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        [BucketLifecycle.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketLifecycle.Bucket)
        """

    def delete(self, ExpectedBucketOwner: str = None) -> None:
        """
        [BucketLifecycle.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketLifecycle.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [BucketLifecycle.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketLifecycle.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketLifecycle.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketLifecycle.load)
        """

    def put(
        self,
        LifecycleConfiguration: LifecycleConfigurationTypeDef = None,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [BucketLifecycle.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketLifecycle.put)
        """

    def reload(self) -> None:
        """
        [BucketLifecycle.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketLifecycle.reload)
        """


_BucketLifecycle = BucketLifecycle


class BucketLifecycleConfiguration(Boto3ServiceResource):
    """
    [BucketLifecycleConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketLifecycleConfiguration)
    """

    rules: List[Any]
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        [BucketLifecycleConfiguration.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketLifecycleConfiguration.Bucket)
        """

    def delete(self, ExpectedBucketOwner: str = None) -> None:
        """
        [BucketLifecycleConfiguration.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketLifecycleConfiguration.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [BucketLifecycleConfiguration.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketLifecycleConfiguration.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketLifecycleConfiguration.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketLifecycleConfiguration.load)
        """

    def put(
        self,
        LifecycleConfiguration: BucketLifecycleConfigurationTypeDef = None,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [BucketLifecycleConfiguration.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketLifecycleConfiguration.put)
        """

    def reload(self) -> None:
        """
        [BucketLifecycleConfiguration.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketLifecycleConfiguration.reload)
        """


_BucketLifecycleConfiguration = BucketLifecycleConfiguration


class BucketLogging(Boto3ServiceResource):
    """
    [BucketLogging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketLogging)
    """

    logging_enabled: Dict[str, Any]
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        [BucketLogging.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketLogging.Bucket)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [BucketLogging.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketLogging.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketLogging.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketLogging.load)
        """

    def put(
        self, BucketLoggingStatus: BucketLoggingStatusTypeDef, ExpectedBucketOwner: str = None
    ) -> None:
        """
        [BucketLogging.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketLogging.put)
        """

    def reload(self) -> None:
        """
        [BucketLogging.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketLogging.reload)
        """


_BucketLogging = BucketLogging


class BucketNotification(Boto3ServiceResource):
    """
    [BucketNotification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketNotification)
    """

    topic_configurations: List[Any]
    queue_configurations: List[Any]
    lambda_function_configurations: List[Any]
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        [BucketNotification.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketNotification.Bucket)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [BucketNotification.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketNotification.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketNotification.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketNotification.load)
        """

    def put(
        self,
        NotificationConfiguration: NotificationConfigurationTypeDef,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [BucketNotification.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketNotification.put)
        """

    def reload(self) -> None:
        """
        [BucketNotification.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketNotification.reload)
        """


_BucketNotification = BucketNotification


class BucketPolicy(Boto3ServiceResource):
    """
    [BucketPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketPolicy)
    """

    policy: str
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        [BucketPolicy.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketPolicy.Bucket)
        """

    def delete(self, ExpectedBucketOwner: str = None) -> None:
        """
        [BucketPolicy.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketPolicy.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [BucketPolicy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketPolicy.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketPolicy.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketPolicy.load)
        """

    def put(
        self,
        Policy: str,
        ConfirmRemoveSelfBucketAccess: bool = None,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [BucketPolicy.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketPolicy.put)
        """

    def reload(self) -> None:
        """
        [BucketPolicy.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketPolicy.reload)
        """


_BucketPolicy = BucketPolicy


class BucketRequestPayment(Boto3ServiceResource):
    """
    [BucketRequestPayment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketRequestPayment)
    """

    payer: str
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        [BucketRequestPayment.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketRequestPayment.Bucket)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [BucketRequestPayment.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketRequestPayment.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketRequestPayment.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketRequestPayment.load)
        """

    def put(
        self,
        RequestPaymentConfiguration: RequestPaymentConfigurationTypeDef,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [BucketRequestPayment.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketRequestPayment.put)
        """

    def reload(self) -> None:
        """
        [BucketRequestPayment.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketRequestPayment.reload)
        """


_BucketRequestPayment = BucketRequestPayment


class BucketTagging(Boto3ServiceResource):
    """
    [BucketTagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketTagging)
    """

    tag_set: List[Any]
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        [BucketTagging.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketTagging.Bucket)
        """

    def delete(self, ExpectedBucketOwner: str = None) -> None:
        """
        [BucketTagging.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketTagging.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [BucketTagging.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketTagging.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketTagging.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketTagging.load)
        """

    def put(self, Tagging: "TaggingTypeDef", ExpectedBucketOwner: str = None) -> None:
        """
        [BucketTagging.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketTagging.put)
        """

    def reload(self) -> None:
        """
        [BucketTagging.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketTagging.reload)
        """


_BucketTagging = BucketTagging


class BucketVersioning(Boto3ServiceResource):
    """
    [BucketVersioning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketVersioning)
    """

    status: str
    mfa_delete: str
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        [BucketVersioning.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketVersioning.Bucket)
        """

    def enable(
        self,
        VersioningConfiguration: VersioningConfigurationTypeDef,
        MFA: str = None,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [BucketVersioning.enable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketVersioning.enable)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [BucketVersioning.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketVersioning.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketVersioning.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketVersioning.load)
        """

    def put(
        self,
        VersioningConfiguration: VersioningConfigurationTypeDef,
        MFA: str = None,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [BucketVersioning.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketVersioning.put)
        """

    def reload(self) -> None:
        """
        [BucketVersioning.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketVersioning.reload)
        """

    def suspend(
        self,
        VersioningConfiguration: VersioningConfigurationTypeDef,
        MFA: str = None,
        ExpectedBucketOwner: str = None,
    ) -> None:
        """
        [BucketVersioning.suspend documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketVersioning.suspend)
        """


_BucketVersioning = BucketVersioning


class BucketWebsite(Boto3ServiceResource):
    """
    [BucketWebsite documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketWebsite)
    """

    redirect_all_requests_to: Dict[str, Any]
    index_document: Dict[str, Any]
    error_document: Dict[str, Any]
    routing_rules: List[Any]
    bucket_name: str

    def Bucket(self) -> "_Bucket":
        """
        [BucketWebsite.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketWebsite.Bucket)
        """

    def delete(self, ExpectedBucketOwner: str = None) -> None:
        """
        [BucketWebsite.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketWebsite.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [BucketWebsite.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketWebsite.get_available_subresources)
        """

    def load(self) -> None:
        """
        [BucketWebsite.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketWebsite.load)
        """

    def put(
        self, WebsiteConfiguration: WebsiteConfigurationTypeDef, ExpectedBucketOwner: str = None
    ) -> None:
        """
        [BucketWebsite.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketWebsite.put)
        """

    def reload(self) -> None:
        """
        [BucketWebsite.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.BucketWebsite.reload)
        """


_BucketWebsite = BucketWebsite


class MultipartUploadPart(Boto3ServiceResource):
    """
    [MultipartUploadPart documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.MultipartUploadPart)
    """

    last_modified: datetime
    e_tag: str
    size: int
    bucket_name: str
    object_key: str
    multipart_upload_id: str
    part_number: str

    def MultipartUpload(self) -> "_MultipartUpload":
        """
        [MultipartUploadPart.MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.MultipartUploadPart.MultipartUpload)
        """

    def copy_from(
        self,
        CopySource: str,
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
        [MultipartUploadPart.copy_from documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.MultipartUploadPart.copy_from)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [MultipartUploadPart.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.MultipartUploadPart.get_available_subresources)
        """

    def upload(
        self,
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
        [MultipartUploadPart.upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.MultipartUploadPart.upload)
        """


_MultipartUploadPart = MultipartUploadPart


class ObjectAcl(Boto3ServiceResource):
    """
    [ObjectAcl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.ObjectAcl)
    """

    owner: Dict[str, Any]
    grants: List[Any]
    request_charged: str
    bucket_name: str
    object_key: str

    def Object(self) -> "_Object":
        """
        [ObjectAcl.Object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectAcl.Object)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [ObjectAcl.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectAcl.get_available_subresources)
        """

    def load(self) -> None:
        """
        [ObjectAcl.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectAcl.load)
        """

    def put(
        self,
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
        [ObjectAcl.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectAcl.put)
        """

    def reload(self) -> None:
        """
        [ObjectAcl.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectAcl.reload)
        """


_ObjectAcl = ObjectAcl


class ObjectVersion(Boto3ServiceResource):
    """
    [ObjectVersion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.ObjectVersion)
    """

    e_tag: str
    size: int
    storage_class: str
    key: str
    version_id: str
    is_latest: bool
    last_modified: datetime
    owner: Dict[str, Any]
    bucket_name: str
    object_key: str
    id: str

    def Object(self) -> "_Object":
        """
        [ObjectVersion.Object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectVersion.Object)
        """

    def delete(
        self,
        MFA: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
        ExpectedBucketOwner: str = None,
    ) -> DeleteObjectOutputTypeDef:
        """
        [ObjectVersion.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectVersion.delete)
        """

    def get(
        self,
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
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        PartNumber: int = None,
        ExpectedBucketOwner: str = None,
    ) -> GetObjectOutputTypeDef:
        """
        [ObjectVersion.get documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectVersion.get)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [ObjectVersion.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectVersion.get_available_subresources)
        """

    def head(
        self,
        IfMatch: str = None,
        IfModifiedSince: datetime = None,
        IfNoneMatch: str = None,
        IfUnmodifiedSince: datetime = None,
        Range: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        PartNumber: int = None,
        ExpectedBucketOwner: str = None,
    ) -> HeadObjectOutputTypeDef:
        """
        [ObjectVersion.head documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectVersion.head)
        """


_ObjectVersion = ObjectVersion


class MultipartUpload(Boto3ServiceResource):
    """
    [MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.MultipartUpload)
    """

    upload_id: str
    key: str
    initiated: datetime
    storage_class: str
    owner: Dict[str, Any]
    initiator: Dict[str, Any]
    bucket_name: str
    object_key: str
    id: str
    parts: MultipartUploadPartsCollection

    def Object(self) -> "_Object":
        """
        [MultipartUpload.Object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.MultipartUpload.Object)
        """

    def Part(self, part_number: str) -> _MultipartUploadPart:
        """
        [MultipartUpload.Part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.MultipartUpload.Part)
        """

    def abort(
        self, RequestPayer: Literal["requester"] = None, ExpectedBucketOwner: str = None
    ) -> AbortMultipartUploadOutputTypeDef:
        """
        [MultipartUpload.abort documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.MultipartUpload.abort)
        """

    def complete(
        self,
        MultipartUpload: CompletedMultipartUploadTypeDef = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
    ) -> "_Object":
        """
        [MultipartUpload.complete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.MultipartUpload.complete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [MultipartUpload.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.MultipartUpload.get_available_subresources)
        """


_MultipartUpload = MultipartUpload


class Object(Boto3ServiceResource):
    """
    [Object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.Object)
    """

    delete_marker: bool
    accept_ranges: str
    expiration: str
    restore: str
    archive_status: str
    last_modified: datetime
    content_length: int
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
        [Object.Acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Object.Acl)
        """

    def Bucket(self) -> "_Bucket":
        """
        [Object.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Object.Bucket)
        """

    def MultipartUpload(self, id: str) -> _MultipartUpload:
        """
        [Object.MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Object.MultipartUpload)
        """

    def Version(self, id: str) -> _ObjectVersion:
        """
        [Object.Version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Object.Version)
        """

    def copy(
        self,
        CopySource: CopySourceTypeDef,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        SourceClient: BaseClient = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Object.copy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Object.copy)
        """

    def copy_from(
        self,
        CopySource: str,
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
        [Object.copy_from documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Object.copy_from)
        """

    def delete(
        self,
        MFA: str = None,
        VersionId: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
        ExpectedBucketOwner: str = None,
    ) -> DeleteObjectOutputTypeDef:
        """
        [Object.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Object.delete)
        """

    def download_file(
        self,
        Filename: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Object.download_file documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Object.download_file)
        """

    def download_fileobj(
        self,
        Fileobj: IO[Any],
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Object.download_fileobj documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Object.download_fileobj)
        """

    def get(
        self,
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
        [Object.get documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Object.get)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Object.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Object.get_available_subresources)
        """

    def initiate_multipart_upload(
        self,
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
    ) -> _MultipartUpload:
        """
        [Object.initiate_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Object.initiate_multipart_upload)
        """

    def load(self) -> None:
        """
        [Object.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Object.load)
        """

    def put(
        self,
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
        [Object.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Object.put)
        """

    def reload(self) -> None:
        """
        [Object.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Object.reload)
        """

    def restore_object(
        self,
        VersionId: str = None,
        RestoreRequest: RestoreRequestTypeDef = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
    ) -> RestoreObjectOutputTypeDef:
        """
        [Object.restore_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Object.restore_object)
        """

    def upload_file(
        self,
        Filename: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Object.upload_file documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Object.upload_file)
        """

    def upload_fileobj(
        self,
        Fileobj: IO[Any],
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Object.upload_fileobj documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Object.upload_fileobj)
        """

    def wait_until_exists(self) -> None:
        """
        [Object.wait_until_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Object.wait_until_exists)
        """

    def wait_until_not_exists(self) -> None:
        """
        [Object.wait_until_not_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Object.wait_until_not_exists)
        """


_Object = Object


class ObjectSummary(Boto3ServiceResource):
    """
    [ObjectSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.ObjectSummary)
    """

    last_modified: datetime
    e_tag: str
    size: int
    storage_class: str
    owner: Dict[str, Any]
    bucket_name: str
    key: str

    def Acl(self) -> _ObjectAcl:
        """
        [ObjectSummary.Acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectSummary.Acl)
        """

    def Bucket(self) -> "_Bucket":
        """
        [ObjectSummary.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectSummary.Bucket)
        """

    def MultipartUpload(self, id: str) -> _MultipartUpload:
        """
        [ObjectSummary.MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectSummary.MultipartUpload)
        """

    def Object(self) -> _Object:
        """
        [ObjectSummary.Object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectSummary.Object)
        """

    def Version(self, id: str) -> _ObjectVersion:
        """
        [ObjectSummary.Version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectSummary.Version)
        """

    def copy_from(
        self,
        CopySource: str,
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
        [ObjectSummary.copy_from documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectSummary.copy_from)
        """

    def delete(
        self,
        MFA: str = None,
        VersionId: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
        ExpectedBucketOwner: str = None,
    ) -> DeleteObjectOutputTypeDef:
        """
        [ObjectSummary.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectSummary.delete)
        """

    def get(
        self,
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
        [ObjectSummary.get documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectSummary.get)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [ObjectSummary.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectSummary.get_available_subresources)
        """

    def initiate_multipart_upload(
        self,
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
    ) -> _MultipartUpload:
        """
        [ObjectSummary.initiate_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectSummary.initiate_multipart_upload)
        """

    def load(self) -> None:
        """
        [ObjectSummary.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectSummary.load)
        """

    def put(
        self,
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
        [ObjectSummary.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectSummary.put)
        """

    def restore_object(
        self,
        VersionId: str = None,
        RestoreRequest: RestoreRequestTypeDef = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
    ) -> RestoreObjectOutputTypeDef:
        """
        [ObjectSummary.restore_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectSummary.restore_object)
        """

    def wait_until_exists(self) -> None:
        """
        [ObjectSummary.wait_until_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectSummary.wait_until_exists)
        """

    def wait_until_not_exists(self) -> None:
        """
        [ObjectSummary.wait_until_not_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ObjectSummary.wait_until_not_exists)
        """


_ObjectSummary = ObjectSummary


class Bucket(Boto3ServiceResource):
    """
    [Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.Bucket)
    """

    creation_date: datetime
    name: str
    multipart_uploads: BucketMultipartUploadsCollection
    object_versions: BucketObjectVersionsCollection
    objects: BucketObjectsCollection

    def Acl(self) -> _BucketAcl:
        """
        [Bucket.Acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.Acl)
        """

    def Cors(self) -> _BucketCors:
        """
        [Bucket.Cors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.Cors)
        """

    def Lifecycle(self) -> _BucketLifecycle:
        """
        [Bucket.Lifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.Lifecycle)
        """

    def LifecycleConfiguration(self) -> _BucketLifecycleConfiguration:
        """
        [Bucket.LifecycleConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.LifecycleConfiguration)
        """

    def Logging(self) -> _BucketLogging:
        """
        [Bucket.Logging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.Logging)
        """

    def Notification(self) -> _BucketNotification:
        """
        [Bucket.Notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.Notification)
        """

    def Object(self, key: str) -> _Object:
        """
        [Bucket.Object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.Object)
        """

    def Policy(self) -> _BucketPolicy:
        """
        [Bucket.Policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.Policy)
        """

    def RequestPayment(self) -> _BucketRequestPayment:
        """
        [Bucket.RequestPayment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.RequestPayment)
        """

    def Tagging(self) -> _BucketTagging:
        """
        [Bucket.Tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.Tagging)
        """

    def Versioning(self) -> _BucketVersioning:
        """
        [Bucket.Versioning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.Versioning)
        """

    def Website(self) -> _BucketWebsite:
        """
        [Bucket.Website documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.Website)
        """

    def copy(
        self,
        CopySource: CopySourceTypeDef,
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        SourceClient: BaseClient = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Bucket.copy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.copy)
        """

    def create(
        self,
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
        [Bucket.create documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.create)
        """

    def delete(self, ExpectedBucketOwner: str = None) -> None:
        """
        [Bucket.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.delete)
        """

    def delete_objects(
        self,
        Delete: DeleteTypeDef,
        MFA: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
        ExpectedBucketOwner: str = None,
    ) -> DeleteObjectsOutputTypeDef:
        """
        [Bucket.delete_objects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.delete_objects)
        """

    def download_file(
        self,
        Key: str,
        Filename: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Bucket.download_file documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.download_file)
        """

    def download_fileobj(
        self,
        Key: str,
        Fileobj: IO[Any],
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Bucket.download_fileobj documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.download_fileobj)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Bucket.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.get_available_subresources)
        """

    def load(self) -> None:
        """
        [Bucket.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.load)
        """

    def put_object(
        self,
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
    ) -> _Object:
        """
        [Bucket.put_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.put_object)
        """

    def upload_file(
        self,
        Filename: str,
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Bucket.upload_file documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.upload_file)
        """

    def upload_fileobj(
        self,
        Fileobj: IO[Any],
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        [Bucket.upload_fileobj documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.upload_fileobj)
        """

    def wait_until_exists(self) -> None:
        """
        [Bucket.wait_until_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.wait_until_exists)
        """

    def wait_until_not_exists(self) -> None:
        """
        [Bucket.wait_until_not_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Bucket.wait_until_not_exists)
        """


_Bucket = Bucket


class S3ServiceResource(Boto3ServiceResource):
    """
    [S3.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource)
    """

    buckets: ServiceResourceBucketsCollection

    def Bucket(self, name: str) -> _Bucket:
        """
        [ServiceResource.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.Bucket)
        """

    def BucketAcl(self, bucket_name: str) -> _BucketAcl:
        """
        [ServiceResource.BucketAcl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketAcl)
        """

    def BucketCors(self, bucket_name: str) -> _BucketCors:
        """
        [ServiceResource.BucketCors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketCors)
        """

    def BucketLifecycle(self, bucket_name: str) -> _BucketLifecycle:
        """
        [ServiceResource.BucketLifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketLifecycle)
        """

    def BucketLifecycleConfiguration(self, bucket_name: str) -> _BucketLifecycleConfiguration:
        """
        [ServiceResource.BucketLifecycleConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketLifecycleConfiguration)
        """

    def BucketLogging(self, bucket_name: str) -> _BucketLogging:
        """
        [ServiceResource.BucketLogging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketLogging)
        """

    def BucketNotification(self, bucket_name: str) -> _BucketNotification:
        """
        [ServiceResource.BucketNotification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketNotification)
        """

    def BucketPolicy(self, bucket_name: str) -> _BucketPolicy:
        """
        [ServiceResource.BucketPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketPolicy)
        """

    def BucketRequestPayment(self, bucket_name: str) -> _BucketRequestPayment:
        """
        [ServiceResource.BucketRequestPayment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketRequestPayment)
        """

    def BucketTagging(self, bucket_name: str) -> _BucketTagging:
        """
        [ServiceResource.BucketTagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketTagging)
        """

    def BucketVersioning(self, bucket_name: str) -> _BucketVersioning:
        """
        [ServiceResource.BucketVersioning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketVersioning)
        """

    def BucketWebsite(self, bucket_name: str) -> _BucketWebsite:
        """
        [ServiceResource.BucketWebsite documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.BucketWebsite)
        """

    def MultipartUpload(self, bucket_name: str, object_key: str, id: str) -> _MultipartUpload:
        """
        [ServiceResource.MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.MultipartUpload)
        """

    def MultipartUploadPart(
        self, bucket_name: str, object_key: str, multipart_upload_id: str, part_number: str
    ) -> _MultipartUploadPart:
        """
        [ServiceResource.MultipartUploadPart documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.MultipartUploadPart)
        """

    def Object(self, bucket_name: str, key: str) -> _Object:
        """
        [ServiceResource.Object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.Object)
        """

    def ObjectAcl(self, bucket_name: str, object_key: str) -> _ObjectAcl:
        """
        [ServiceResource.ObjectAcl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.ObjectAcl)
        """

    def ObjectSummary(self, bucket_name: str, key: str) -> _ObjectSummary:
        """
        [ServiceResource.ObjectSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.ObjectSummary)
        """

    def ObjectVersion(self, bucket_name: str, object_key: str, id: str) -> _ObjectVersion:
        """
        [ServiceResource.ObjectVersion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.ObjectVersion)
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
    ) -> _Bucket:
        """
        [ServiceResource.create_bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.create_bucket)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.ServiceResource.get_available_subresources)
        """
