"""
Type annotations for efs service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_efs import EFSClient
    from mypy_boto3_efs.paginator import (
        DescribeAccessPointsPaginator,
        DescribeFileSystemsPaginator,
        DescribeMountTargetsPaginator,
        DescribeReplicationConfigurationsPaginator,
        DescribeTagsPaginator,
    )

    client: EFSClient = boto3.client("efs")

    describe_access_points_paginator: DescribeAccessPointsPaginator = client.get_paginator("describe_access_points")
    describe_file_systems_paginator: DescribeFileSystemsPaginator = client.get_paginator("describe_file_systems")
    describe_mount_targets_paginator: DescribeMountTargetsPaginator = client.get_paginator("describe_mount_targets")
    describe_replication_configurations_paginator: DescribeReplicationConfigurationsPaginator = client.get_paginator("describe_replication_configurations")
    describe_tags_paginator: DescribeTagsPaginator = client.get_paginator("describe_tags")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    DescribeAccessPointsResponseTypeDef,
    DescribeFileSystemsResponseTypeDef,
    DescribeMountTargetsResponseTypeDef,
    DescribeReplicationConfigurationsResponseTypeDef,
    DescribeTagsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeAccessPointsPaginator",
    "DescribeFileSystemsPaginator",
    "DescribeMountTargetsPaginator",
    "DescribeReplicationConfigurationsPaginator",
    "DescribeTagsPaginator",
)

class DescribeAccessPointsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/efs.html#EFS.Paginator.DescribeAccessPoints)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators.html#describeaccesspointspaginator)
    """

    def paginate(
        self,
        *,
        AccessPointId: str = None,
        FileSystemId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAccessPointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/efs.html#EFS.Paginator.DescribeAccessPoints.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators.html#describeaccesspointspaginator)
        """

class DescribeFileSystemsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/efs.html#EFS.Paginator.DescribeFileSystems)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators.html#describefilesystemspaginator)
    """

    def paginate(
        self,
        *,
        CreationToken: str = None,
        FileSystemId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFileSystemsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/efs.html#EFS.Paginator.DescribeFileSystems.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators.html#describefilesystemspaginator)
        """

class DescribeMountTargetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/efs.html#EFS.Paginator.DescribeMountTargets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators.html#describemounttargetspaginator)
    """

    def paginate(
        self,
        *,
        FileSystemId: str = None,
        MountTargetId: str = None,
        AccessPointId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMountTargetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/efs.html#EFS.Paginator.DescribeMountTargets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators.html#describemounttargetspaginator)
        """

class DescribeReplicationConfigurationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/efs.html#EFS.Paginator.DescribeReplicationConfigurations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators.html#describereplicationconfigurationspaginator)
    """

    def paginate(
        self, *, FileSystemId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReplicationConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/efs.html#EFS.Paginator.DescribeReplicationConfigurations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators.html#describereplicationconfigurationspaginator)
        """

class DescribeTagsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/efs.html#EFS.Paginator.DescribeTags)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators.html#describetagspaginator)
    """

    def paginate(
        self, *, FileSystemId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/efs.html#EFS.Paginator.DescribeTags.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators.html#describetagspaginator)
        """
