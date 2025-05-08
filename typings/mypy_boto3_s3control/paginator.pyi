"""
Type annotations for s3control service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_s3control.client import S3ControlClient
    from mypy_boto3_s3control.paginator import (
        ListAccessPointsForDirectoryBucketsPaginator,
        ListAccessPointsForObjectLambdaPaginator,
        ListCallerAccessGrantsPaginator,
    )

    session = Session()
    client: S3ControlClient = session.client("s3control")

    list_access_points_for_directory_buckets_paginator: ListAccessPointsForDirectoryBucketsPaginator = client.get_paginator("list_access_points_for_directory_buckets")
    list_access_points_for_object_lambda_paginator: ListAccessPointsForObjectLambdaPaginator = client.get_paginator("list_access_points_for_object_lambda")
    list_caller_access_grants_paginator: ListCallerAccessGrantsPaginator = client.get_paginator("list_caller_access_grants")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAccessPointsForDirectoryBucketsRequestPaginateTypeDef,
    ListAccessPointsForDirectoryBucketsResultTypeDef,
    ListAccessPointsForObjectLambdaRequestPaginateTypeDef,
    ListAccessPointsForObjectLambdaResultTypeDef,
    ListCallerAccessGrantsRequestPaginateTypeDef,
    ListCallerAccessGrantsResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAccessPointsForDirectoryBucketsPaginator",
    "ListAccessPointsForObjectLambdaPaginator",
    "ListCallerAccessGrantsPaginator",
)

if TYPE_CHECKING:
    _ListAccessPointsForDirectoryBucketsPaginatorBase = Paginator[
        ListAccessPointsForDirectoryBucketsResultTypeDef
    ]
else:
    _ListAccessPointsForDirectoryBucketsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccessPointsForDirectoryBucketsPaginator(
    _ListAccessPointsForDirectoryBucketsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/paginator/ListAccessPointsForDirectoryBuckets.html#S3Control.Paginator.ListAccessPointsForDirectoryBuckets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/paginators/#listaccesspointsfordirectorybucketspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccessPointsForDirectoryBucketsRequestPaginateTypeDef]
    ) -> PageIterator[ListAccessPointsForDirectoryBucketsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/paginator/ListAccessPointsForDirectoryBuckets.html#S3Control.Paginator.ListAccessPointsForDirectoryBuckets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/paginators/#listaccesspointsfordirectorybucketspaginator)
        """

if TYPE_CHECKING:
    _ListAccessPointsForObjectLambdaPaginatorBase = Paginator[
        ListAccessPointsForObjectLambdaResultTypeDef
    ]
else:
    _ListAccessPointsForObjectLambdaPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccessPointsForObjectLambdaPaginator(_ListAccessPointsForObjectLambdaPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/paginator/ListAccessPointsForObjectLambda.html#S3Control.Paginator.ListAccessPointsForObjectLambda)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/paginators/#listaccesspointsforobjectlambdapaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccessPointsForObjectLambdaRequestPaginateTypeDef]
    ) -> PageIterator[ListAccessPointsForObjectLambdaResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/paginator/ListAccessPointsForObjectLambda.html#S3Control.Paginator.ListAccessPointsForObjectLambda.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/paginators/#listaccesspointsforobjectlambdapaginator)
        """

if TYPE_CHECKING:
    _ListCallerAccessGrantsPaginatorBase = Paginator[ListCallerAccessGrantsResultTypeDef]
else:
    _ListCallerAccessGrantsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCallerAccessGrantsPaginator(_ListCallerAccessGrantsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/paginator/ListCallerAccessGrants.html#S3Control.Paginator.ListCallerAccessGrants)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/paginators/#listcalleraccessgrantspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCallerAccessGrantsRequestPaginateTypeDef]
    ) -> PageIterator[ListCallerAccessGrantsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/paginator/ListCallerAccessGrants.html#S3Control.Paginator.ListCallerAccessGrants.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/paginators/#listcalleraccessgrantspaginator)
        """
