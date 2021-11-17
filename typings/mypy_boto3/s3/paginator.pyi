"""
Type annotations for s3 service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/paginators.html)

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

from .type_defs import (
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Paginator.ListMultipartUploads)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/paginators.html#listmultipartuploadspaginator)
    """

    def paginate(
        self,
        *,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        Prefix: str = None,
        ExpectedBucketOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMultipartUploadsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Paginator.ListMultipartUploads.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/paginators.html#listmultipartuploadspaginator)
        """

class ListObjectVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Paginator.ListObjectVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/paginators.html#listobjectversionspaginator)
    """

    def paginate(
        self,
        *,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        Prefix: str = None,
        ExpectedBucketOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListObjectVersionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Paginator.ListObjectVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/paginators.html#listobjectversionspaginator)
        """

class ListObjectsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Paginator.ListObjects)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/paginators.html#listobjectspaginator)
    """

    def paginate(
        self,
        *,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        Prefix: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListObjectsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Paginator.ListObjects.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/paginators.html#listobjectspaginator)
        """

class ListObjectsV2Paginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Paginator.ListObjectsV2)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/paginators.html#listobjectsv2paginator)
    """

    def paginate(
        self,
        *,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        Prefix: str = None,
        FetchOwner: bool = None,
        StartAfter: str = None,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListObjectsV2OutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Paginator.ListObjectsV2.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/paginators.html#listobjectsv2paginator)
        """

class ListPartsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Paginator.ListParts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/paginators.html#listpartspaginator)
    """

    def paginate(
        self,
        *,
        Bucket: str,
        Key: str,
        UploadId: str,
        RequestPayer: Literal["requester"] = None,
        ExpectedBucketOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPartsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3.html#S3.Paginator.ListParts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/paginators.html#listpartspaginator)
        """
