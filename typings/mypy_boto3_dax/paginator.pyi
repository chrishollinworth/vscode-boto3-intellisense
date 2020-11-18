# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for dax service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_dax import DAXClient
    from mypy_boto3_dax.paginator import (
        DescribeClustersPaginator,
        DescribeDefaultParametersPaginator,
        DescribeEventsPaginator,
        DescribeParameterGroupsPaginator,
        DescribeParametersPaginator,
        DescribeSubnetGroupsPaginator,
        ListTagsPaginator,
    )

    client: DAXClient = boto3.client("dax")

    describe_clusters_paginator: DescribeClustersPaginator = client.get_paginator("describe_clusters")
    describe_default_parameters_paginator: DescribeDefaultParametersPaginator = client.get_paginator("describe_default_parameters")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_parameter_groups_paginator: DescribeParameterGroupsPaginator = client.get_paginator("describe_parameter_groups")
    describe_parameters_paginator: DescribeParametersPaginator = client.get_paginator("describe_parameters")
    describe_subnet_groups_paginator: DescribeSubnetGroupsPaginator = client.get_paginator("describe_subnet_groups")
    list_tags_paginator: ListTagsPaginator = client.get_paginator("list_tags")
    ```
"""
import sys
from datetime import datetime
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_dax.type_defs import (
    DescribeClustersResponseTypeDef,
    DescribeDefaultParametersResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeParameterGroupsResponseTypeDef,
    DescribeParametersResponseTypeDef,
    DescribeSubnetGroupsResponseTypeDef,
    ListTagsResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeClustersPaginator",
    "DescribeDefaultParametersPaginator",
    "DescribeEventsPaginator",
    "DescribeParameterGroupsPaginator",
    "DescribeParametersPaginator",
    "DescribeSubnetGroupsPaginator",
    "ListTagsPaginator",
)


class DescribeClustersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.DescribeClusters)
    """

    def paginate(
        self, ClusterNames: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeClustersResponseTypeDef]:
        """
        [DescribeClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.DescribeClusters.paginate)
        """


class DescribeDefaultParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDefaultParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.DescribeDefaultParameters)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDefaultParametersResponseTypeDef]:
        """
        [DescribeDefaultParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.DescribeDefaultParameters.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.DescribeEvents)
    """

    def paginate(
        self,
        SourceName: str = None,
        SourceType: Literal["CLUSTER", "PARAMETER_GROUP", "SUBNET_GROUP"] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeEventsResponseTypeDef]:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.DescribeEvents.paginate)
        """


class DescribeParameterGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.DescribeParameterGroups)
    """

    def paginate(
        self, ParameterGroupNames: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeParameterGroupsResponseTypeDef]:
        """
        [DescribeParameterGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.DescribeParameterGroups.paginate)
        """


class DescribeParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.DescribeParameters)
    """

    def paginate(
        self,
        ParameterGroupName: str,
        Source: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeParametersResponseTypeDef]:
        """
        [DescribeParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.DescribeParameters.paginate)
        """


class DescribeSubnetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.DescribeSubnetGroups)
    """

    def paginate(
        self, SubnetGroupNames: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSubnetGroupsResponseTypeDef]:
        """
        [DescribeSubnetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.DescribeSubnetGroups.paginate)
        """


class ListTagsPaginator(Boto3Paginator):
    """
    [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.ListTags)
    """

    def paginate(
        self, ResourceName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsResponseTypeDef]:
        """
        [ListTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.ListTags.paginate)
        """
