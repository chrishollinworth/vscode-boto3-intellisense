"""
Type annotations for s3vectors service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3vectors/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_s3vectors.client import S3VectorsClient
    from mypy_boto3_s3vectors.paginator import (
        ListIndexesPaginator,
        ListVectorBucketsPaginator,
        ListVectorsPaginator,
    )

    session = Session()
    client: S3VectorsClient = session.client("s3vectors")

    list_indexes_paginator: ListIndexesPaginator = client.get_paginator("list_indexes")
    list_vector_buckets_paginator: ListVectorBucketsPaginator = client.get_paginator("list_vector_buckets")
    list_vectors_paginator: ListVectorsPaginator = client.get_paginator("list_vectors")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListIndexesInputPaginateTypeDef,
    ListIndexesOutputTypeDef,
    ListVectorBucketsInputPaginateTypeDef,
    ListVectorBucketsOutputTypeDef,
    ListVectorsInputPaginateTypeDef,
    ListVectorsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListIndexesPaginator", "ListVectorBucketsPaginator", "ListVectorsPaginator")

if TYPE_CHECKING:
    _ListIndexesPaginatorBase = Paginator[ListIndexesOutputTypeDef]
else:
    _ListIndexesPaginatorBase = Paginator  # type: ignore[assignment]

class ListIndexesPaginator(_ListIndexesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3vectors/paginator/ListIndexes.html#S3Vectors.Paginator.ListIndexes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3vectors/paginators/#listindexespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIndexesInputPaginateTypeDef]
    ) -> PageIterator[ListIndexesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3vectors/paginator/ListIndexes.html#S3Vectors.Paginator.ListIndexes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3vectors/paginators/#listindexespaginator)
        """

if TYPE_CHECKING:
    _ListVectorBucketsPaginatorBase = Paginator[ListVectorBucketsOutputTypeDef]
else:
    _ListVectorBucketsPaginatorBase = Paginator  # type: ignore[assignment]

class ListVectorBucketsPaginator(_ListVectorBucketsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3vectors/paginator/ListVectorBuckets.html#S3Vectors.Paginator.ListVectorBuckets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3vectors/paginators/#listvectorbucketspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListVectorBucketsInputPaginateTypeDef]
    ) -> PageIterator[ListVectorBucketsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3vectors/paginator/ListVectorBuckets.html#S3Vectors.Paginator.ListVectorBuckets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3vectors/paginators/#listvectorbucketspaginator)
        """

if TYPE_CHECKING:
    _ListVectorsPaginatorBase = Paginator[ListVectorsOutputTypeDef]
else:
    _ListVectorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListVectorsPaginator(_ListVectorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3vectors/paginator/ListVectors.html#S3Vectors.Paginator.ListVectors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3vectors/paginators/#listvectorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListVectorsInputPaginateTypeDef]
    ) -> PageIterator[ListVectorsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3vectors/paginator/ListVectors.html#S3Vectors.Paginator.ListVectors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3vectors/paginators/#listvectorspaginator)
        """
