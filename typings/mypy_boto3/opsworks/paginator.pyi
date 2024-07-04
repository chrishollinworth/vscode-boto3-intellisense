"""
Type annotations for opsworks service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/paginators.html)

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

from .type_defs import DescribeEcsClustersResultTypeDef, PaginatorConfigTypeDef

__all__ = ("DescribeEcsClustersPaginator",)

class DescribeEcsClustersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/opsworks.html#OpsWorks.Paginator.DescribeEcsClusters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/paginators.html#describeecsclusterspaginator)
    """

    def paginate(
        self,
        *,
        EcsClusterArns: List[str] = None,
        StackId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEcsClustersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/opsworks.html#OpsWorks.Paginator.DescribeEcsClusters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/paginators.html#describeecsclusterspaginator)
        """
