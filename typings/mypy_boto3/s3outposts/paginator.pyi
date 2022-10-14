"""
Type annotations for s3outposts service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_s3outposts import S3OutpostsClient
    from mypy_boto3_s3outposts.paginator import (
        ListEndpointsPaginator,
        ListSharedEndpointsPaginator,
    )

    client: S3OutpostsClient = boto3.client("s3outposts")

    list_endpoints_paginator: ListEndpointsPaginator = client.get_paginator("list_endpoints")
    list_shared_endpoints_paginator: ListSharedEndpointsPaginator = client.get_paginator("list_shared_endpoints")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListEndpointsResultTypeDef,
    ListSharedEndpointsResultTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListEndpointsPaginator", "ListSharedEndpointsPaginator")

class ListEndpointsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/s3outposts.html#S3Outposts.Paginator.ListEndpoints)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/paginators.html#listendpointspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEndpointsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/s3outposts.html#S3Outposts.Paginator.ListEndpoints.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/paginators.html#listendpointspaginator)
        """

class ListSharedEndpointsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/s3outposts.html#S3Outposts.Paginator.ListSharedEndpoints)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/paginators.html#listsharedendpointspaginator)
    """

    def paginate(
        self, *, OutpostId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSharedEndpointsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/s3outposts.html#S3Outposts.Paginator.ListSharedEndpoints.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/paginators.html#listsharedendpointspaginator)
        """
