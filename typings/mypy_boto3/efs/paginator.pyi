"""
Type annotations for efs service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_efs.client import EFSClient
    from mypy_boto3_efs.paginator import (
        DescribeAccessPointsPaginator,
        DescribeFileSystemsPaginator,
        DescribeMountTargetsPaginator,
        DescribeReplicationConfigurationsPaginator,
        DescribeTagsPaginator,
    )

    session = Session()
    client: EFSClient = session.client("efs")

    describe_access_points_paginator: DescribeAccessPointsPaginator = client.get_paginator("describe_access_points")
    describe_file_systems_paginator: DescribeFileSystemsPaginator = client.get_paginator("describe_file_systems")
    describe_mount_targets_paginator: DescribeMountTargetsPaginator = client.get_paginator("describe_mount_targets")
    describe_replication_configurations_paginator: DescribeReplicationConfigurationsPaginator = client.get_paginator("describe_replication_configurations")
    describe_tags_paginator: DescribeTagsPaginator = client.get_paginator("describe_tags")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeAccessPointsRequestPaginateTypeDef,
    DescribeAccessPointsResponseTypeDef,
    DescribeFileSystemsRequestPaginateTypeDef,
    DescribeFileSystemsResponseTypeDef,
    DescribeMountTargetsRequestPaginateTypeDef,
    DescribeMountTargetsResponseTypeDef,
    DescribeReplicationConfigurationsRequestPaginateTypeDef,
    DescribeReplicationConfigurationsResponseTypeDef,
    DescribeTagsRequestPaginateTypeDef,
    DescribeTagsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeAccessPointsPaginator",
    "DescribeFileSystemsPaginator",
    "DescribeMountTargetsPaginator",
    "DescribeReplicationConfigurationsPaginator",
    "DescribeTagsPaginator",
)

if TYPE_CHECKING:
    _DescribeAccessPointsPaginatorBase = Paginator[DescribeAccessPointsResponseTypeDef]
else:
    _DescribeAccessPointsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAccessPointsPaginator(_DescribeAccessPointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs/paginator/DescribeAccessPoints.html#EFS.Paginator.DescribeAccessPoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators/#describeaccesspointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAccessPointsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeAccessPointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs/paginator/DescribeAccessPoints.html#EFS.Paginator.DescribeAccessPoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators/#describeaccesspointspaginator)
        """

if TYPE_CHECKING:
    _DescribeFileSystemsPaginatorBase = Paginator[DescribeFileSystemsResponseTypeDef]
else:
    _DescribeFileSystemsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeFileSystemsPaginator(_DescribeFileSystemsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs/paginator/DescribeFileSystems.html#EFS.Paginator.DescribeFileSystems)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators/#describefilesystemspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeFileSystemsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeFileSystemsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs/paginator/DescribeFileSystems.html#EFS.Paginator.DescribeFileSystems.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators/#describefilesystemspaginator)
        """

if TYPE_CHECKING:
    _DescribeMountTargetsPaginatorBase = Paginator[DescribeMountTargetsResponseTypeDef]
else:
    _DescribeMountTargetsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeMountTargetsPaginator(_DescribeMountTargetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs/paginator/DescribeMountTargets.html#EFS.Paginator.DescribeMountTargets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators/#describemounttargetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeMountTargetsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeMountTargetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs/paginator/DescribeMountTargets.html#EFS.Paginator.DescribeMountTargets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators/#describemounttargetspaginator)
        """

if TYPE_CHECKING:
    _DescribeReplicationConfigurationsPaginatorBase = Paginator[
        DescribeReplicationConfigurationsResponseTypeDef
    ]
else:
    _DescribeReplicationConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReplicationConfigurationsPaginator(_DescribeReplicationConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs/paginator/DescribeReplicationConfigurations.html#EFS.Paginator.DescribeReplicationConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators/#describereplicationconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReplicationConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeReplicationConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs/paginator/DescribeReplicationConfigurations.html#EFS.Paginator.DescribeReplicationConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators/#describereplicationconfigurationspaginator)
        """

if TYPE_CHECKING:
    _DescribeTagsPaginatorBase = Paginator[DescribeTagsResponseTypeDef]
else:
    _DescribeTagsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTagsPaginator(_DescribeTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs/paginator/DescribeTags.html#EFS.Paginator.DescribeTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators/#describetagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTagsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs/paginator/DescribeTags.html#EFS.Paginator.DescribeTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators/#describetagspaginator)
        """
