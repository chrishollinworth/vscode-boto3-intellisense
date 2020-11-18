# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for s3 service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_s3 import S3Client
    from mypy_boto3_s3.paginator import (
        ListMultipartUploadsPaginator,
        ListObjectVersionsPaginator,
        ListObjectsPaginator,
        ListObjectsV2Paginator,
        ListPartsPaginator,
    )

    client: S3Client = boto3.client("s3")

    list_multipart_uploads_paginator: ListMultipartUploadsPaginator = client.get_paginator("list_multipart_uploads")
    list_object_versions_paginator: ListObjectVersionsPaginator = client.get_paginator("list_object_versions")
    list_objects_paginator: ListObjectsPaginator = client.get_paginator("list_objects")
    list_objects_v2_paginator: ListObjectsV2Paginator = client.get_paginator("list_objects_v2")
    list_parts_paginator: ListPartsPaginator = client.get_paginator("list_parts")
    ```
"""
import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_s3.type_defs import (
    ListMultipartUploadsOutputTypeDef,
    ListObjectsOutputTypeDef,
    ListObjectsV2OutputTypeDef,
    ListObjectVersionsOutputTypeDef,
    ListPartsOutputTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListMultipartUploadsPaginator",
    "ListObjectVersionsPaginator",
    "ListObjectsPaginator",
    "ListObjectsV2Paginator",
    "ListPartsPaginator",
)


class ListMultipartUploadsPaginator(Boto3Paginator):
    """
    [Paginator.ListMultipartUploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Paginator.ListMultipartUploads)
    """

    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        Prefix: str = None,
        ExpectedBucketOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListMultipartUploadsOutputTypeDef]:
        """
        [ListMultipartUploads.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Paginator.ListMultipartUploads.paginate)
        """


class ListObjectVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListObjectVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Paginator.ListObjectVersions)
    """

    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        Prefix: str = None,
        ExpectedBucketOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListObjectVersionsOutputTypeDef]:
        """
        [ListObjectVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Paginator.ListObjectVersions.paginate)
        """


class ListObjectsPaginator(Boto3Paginator):
    """
    [Paginator.ListObjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Paginator.ListObjects)
    """

    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        Prefix: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListObjectsOutputTypeDef]:
        """
        [ListObjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Paginator.ListObjects.paginate)
        """


class ListObjectsV2Paginator(Boto3Paginator):
    """
    [Paginator.ListObjectsV2 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Paginator.ListObjectsV2)
    """

    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        Prefix: str = None,
        FetchOwner: bool = None,
        StartAfter: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListObjectsV2OutputTypeDef]:
        """
        [ListObjectsV2.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Paginator.ListObjectsV2.paginate)
        """


class ListPartsPaginator(Boto3Paginator):
    """
    [Paginator.ListParts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Paginator.ListParts)
    """

    def paginate(
        self,
        Bucket: str,
        Key: str,
        UploadId: str,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPartsOutputTypeDef]:
        """
        [ListParts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3.html#S3.Paginator.ListParts.paginate)
        """
