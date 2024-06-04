"""
Type annotations for s3 service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/waiters.html)

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
from typing import Union

from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/s3.html#S3.Waiter.BucketExists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/waiters.html#bucketexistswaiter)
    """

    def wait(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/s3.html#S3.Waiter.BucketExists.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/waiters.html#bucketexistswaiter)
        """

class BucketNotExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/s3.html#S3.Waiter.BucketNotExists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/waiters.html#bucketnotexistswaiter)
    """

    def wait(
        self,
        *,
        Bucket: str,
        ExpectedBucketOwner: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/s3.html#S3.Waiter.BucketNotExists.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/waiters.html#bucketnotexistswaiter)
        """

class ObjectExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/s3.html#S3.Waiter.ObjectExists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/waiters.html#objectexistswaiter)
    """

    def wait(
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
        ExpectedBucketOwner: str = None,
        ChecksumMode: Literal["ENABLED"] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/s3.html#S3.Waiter.ObjectExists.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/waiters.html#objectexistswaiter)
        """

class ObjectNotExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/s3.html#S3.Waiter.ObjectNotExists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/waiters.html#objectnotexistswaiter)
    """

    def wait(
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
        ExpectedBucketOwner: str = None,
        ChecksumMode: Literal["ENABLED"] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/s3.html#S3.Waiter.ObjectNotExists.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/waiters.html#objectnotexistswaiter)
        """
