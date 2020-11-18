# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for opsworks service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_opsworks import OpsWorksClient
    from mypy_boto3_opsworks.paginator import (
        DescribeEcsClustersPaginator,
    )

    client: OpsWorksClient = boto3.client("opsworks")

    describe_ecs_clusters_paginator: DescribeEcsClustersPaginator = client.get_paginator("describe_ecs_clusters")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_opsworks.type_defs import DescribeEcsClustersResultTypeDef, PaginatorConfigTypeDef

__all__ = ("DescribeEcsClustersPaginator",)


class DescribeEcsClustersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEcsClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Paginator.DescribeEcsClusters)
    """

    def paginate(
        self,
        EcsClusterArns: List[str] = None,
        StackId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeEcsClustersResultTypeDef]:
        """
        [DescribeEcsClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Paginator.DescribeEcsClusters.paginate)
        """
