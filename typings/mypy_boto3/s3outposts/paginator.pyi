"""
Type annotations for s3outposts service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_s3outposts.client import S3OutpostsClient
    from mypy_boto3_s3outposts.paginator import (
        ListEndpointsPaginator,
        ListOutpostsWithS3Paginator,
        ListSharedEndpointsPaginator,
    )

    session = Session()
    client: S3OutpostsClient = session.client("s3outposts")

    list_endpoints_paginator: ListEndpointsPaginator = client.get_paginator("list_endpoints")
    list_outposts_with_s3_paginator: ListOutpostsWithS3Paginator = client.get_paginator("list_outposts_with_s3")
    list_shared_endpoints_paginator: ListSharedEndpointsPaginator = client.get_paginator("list_shared_endpoints")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListEndpointsRequestPaginateTypeDef,
    ListEndpointsResultTypeDef,
    ListOutpostsWithS3RequestPaginateTypeDef,
    ListOutpostsWithS3ResultTypeDef,
    ListSharedEndpointsRequestPaginateTypeDef,
    ListSharedEndpointsResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListEndpointsPaginator", "ListOutpostsWithS3Paginator", "ListSharedEndpointsPaginator")

if TYPE_CHECKING:
    _ListEndpointsPaginatorBase = Paginator[ListEndpointsResultTypeDef]
else:
    _ListEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEndpointsPaginator(_ListEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts/paginator/ListEndpoints.html#S3Outposts.Paginator.ListEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/paginators/#listendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEndpointsRequestPaginateTypeDef]
    ) -> PageIterator[ListEndpointsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts/paginator/ListEndpoints.html#S3Outposts.Paginator.ListEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/paginators/#listendpointspaginator)
        """

if TYPE_CHECKING:
    _ListOutpostsWithS3PaginatorBase = Paginator[ListOutpostsWithS3ResultTypeDef]
else:
    _ListOutpostsWithS3PaginatorBase = Paginator  # type: ignore[assignment]

class ListOutpostsWithS3Paginator(_ListOutpostsWithS3PaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts/paginator/ListOutpostsWithS3.html#S3Outposts.Paginator.ListOutpostsWithS3)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/paginators/#listoutpostswiths3paginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOutpostsWithS3RequestPaginateTypeDef]
    ) -> PageIterator[ListOutpostsWithS3ResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts/paginator/ListOutpostsWithS3.html#S3Outposts.Paginator.ListOutpostsWithS3.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/paginators/#listoutpostswiths3paginator)
        """

if TYPE_CHECKING:
    _ListSharedEndpointsPaginatorBase = Paginator[ListSharedEndpointsResultTypeDef]
else:
    _ListSharedEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSharedEndpointsPaginator(_ListSharedEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts/paginator/ListSharedEndpoints.html#S3Outposts.Paginator.ListSharedEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/paginators/#listsharedendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSharedEndpointsRequestPaginateTypeDef]
    ) -> PageIterator[ListSharedEndpointsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts/paginator/ListSharedEndpoints.html#S3Outposts.Paginator.ListSharedEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/paginators/#listsharedendpointspaginator)
        """
