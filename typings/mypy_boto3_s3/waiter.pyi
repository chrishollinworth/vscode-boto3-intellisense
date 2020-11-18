# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for s3 service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_s3 import S3Client
    from mypy_boto3_s3.waiter import (
        BucketExistsWaiter,
        BucketNotExistsWaiter,
        ObjectExistsWaiter,
        ObjectNotExistsWaiter,
    )

    client: S3Client = boto3.client("s3")

    bucket_exists_waiter: BucketExistsWaiter = client.get_waiter("bucket_exists")
    bucket_not_exists_waiter: BucketNotExistsWaiter = client.get_waiter("bucket_not_exists")
    object_exists_waiter: ObjectExistsWaiter = client.get_waiter("object_exists")
    object_not_exists_waiter: ObjectNotExistsWaiter = client.get_waiter("object_not_exists")
    ```
"""
import sys
from datetime import datetime

from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_s3.type_defs import WaiterConfigTypeDef

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BucketExistsWaiter",
    "BucketNotExistsWaiter",
    "ObjectExistsWaiter",
    "ObjectNotExistsWaiter",
)


class BucketExistsWaiter(Boto3Waiter):
    """
    [Waiter.BucketExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Waiter.BucketExists)
    """

    def wait(
        self, Bucket: str, ExpectedBucketOwner: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [BucketExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Waiter.BucketExists.wait)
        """


class BucketNotExistsWaiter(Boto3Waiter):
    """
    [Waiter.BucketNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Waiter.BucketNotExists)
    """

    def wait(
        self, Bucket: str, ExpectedBucketOwner: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [BucketNotExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Waiter.BucketNotExists.wait)
        """


class ObjectExistsWaiter(Boto3Waiter):
    """
    [Waiter.ObjectExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Waiter.ObjectExists)
    """

    def wait(
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
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ObjectExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Waiter.ObjectExists.wait)
        """


class ObjectNotExistsWaiter(Boto3Waiter):
    """
    [Waiter.ObjectNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Waiter.ObjectNotExists)
    """

    def wait(
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
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ObjectNotExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Waiter.ObjectNotExists.wait)
        """
