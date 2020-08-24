# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for efs service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_efs import EFSClient
    from mypy_boto3_efs.paginator import (
        DescribeFileSystemsPaginator,
        DescribeMountTargetsPaginator,
        DescribeTagsPaginator,
    )

    client: EFSClient = boto3.client("efs")

    describe_file_systems_paginator: DescribeFileSystemsPaginator = client.get_paginator("describe_file_systems")
    describe_mount_targets_paginator: DescribeMountTargetsPaginator = client.get_paginator("describe_mount_targets")
    describe_tags_paginator: DescribeTagsPaginator = client.get_paginator("describe_tags")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_efs.type_defs import (
    DescribeFileSystemsResponseTypeDef,
    DescribeMountTargetsResponseTypeDef,
    DescribeTagsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("DescribeFileSystemsPaginator", "DescribeMountTargetsPaginator", "DescribeTagsPaginator")


class DescribeFileSystemsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeFileSystems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/efs.html#EFS.Paginator.DescribeFileSystems)
    """

    def paginate(
        self,
        CreationToken: str = None,
        FileSystemId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeFileSystemsResponseTypeDef]:
        """
        [DescribeFileSystems.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/efs.html#EFS.Paginator.DescribeFileSystems.paginate)
        """


class DescribeMountTargetsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMountTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/efs.html#EFS.Paginator.DescribeMountTargets)
    """

    def paginate(
        self,
        FileSystemId: str = None,
        MountTargetId: str = None,
        AccessPointId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeMountTargetsResponseTypeDef]:
        """
        [DescribeMountTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/efs.html#EFS.Paginator.DescribeMountTargets.paginate)
        """


class DescribeTagsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/efs.html#EFS.Paginator.DescribeTags)
    """

    def paginate(
        self, FileSystemId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTagsResponseTypeDef]:
        """
        [DescribeTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/efs.html#EFS.Paginator.DescribeTags.paginate)
        """
