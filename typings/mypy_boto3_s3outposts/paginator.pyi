# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for s3outposts service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_s3outposts import S3OutpostsClient
    from mypy_boto3_s3outposts.paginator import (
        ListEndpointsPaginator,
    )

    client: S3OutpostsClient = boto3.client("s3outposts")

    list_endpoints_paginator: ListEndpointsPaginator = client.get_paginator("list_endpoints")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_s3outposts.type_defs import ListEndpointsResultTypeDef, PaginatorConfigTypeDef

__all__ = ("ListEndpointsPaginator",)


class ListEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.ListEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3outposts.html#S3Outposts.Paginator.ListEndpoints)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEndpointsResultTypeDef]:
        """
        [ListEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3outposts.html#S3Outposts.Paginator.ListEndpoints.paginate)
        """
