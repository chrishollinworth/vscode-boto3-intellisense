"""
Type annotations for timestream-influxdb service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_timestream_influxdb.client import TimestreamInfluxDBClient
    from mypy_boto3_timestream_influxdb.paginator import (
        ListDbClustersPaginator,
        ListDbInstancesForClusterPaginator,
        ListDbInstancesPaginator,
        ListDbParameterGroupsPaginator,
    )

    session = Session()
    client: TimestreamInfluxDBClient = session.client("timestream-influxdb")

    list_db_clusters_paginator: ListDbClustersPaginator = client.get_paginator("list_db_clusters")
    list_db_instances_for_cluster_paginator: ListDbInstancesForClusterPaginator = client.get_paginator("list_db_instances_for_cluster")
    list_db_instances_paginator: ListDbInstancesPaginator = client.get_paginator("list_db_instances")
    list_db_parameter_groups_paginator: ListDbParameterGroupsPaginator = client.get_paginator("list_db_parameter_groups")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListDbClustersInputPaginateTypeDef,
    ListDbClustersOutputTypeDef,
    ListDbInstancesForClusterInputPaginateTypeDef,
    ListDbInstancesForClusterOutputTypeDef,
    ListDbInstancesInputPaginateTypeDef,
    ListDbInstancesOutputTypeDef,
    ListDbParameterGroupsInputPaginateTypeDef,
    ListDbParameterGroupsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListDbClustersPaginator",
    "ListDbInstancesForClusterPaginator",
    "ListDbInstancesPaginator",
    "ListDbParameterGroupsPaginator",
)

if TYPE_CHECKING:
    _ListDbClustersPaginatorBase = Paginator[ListDbClustersOutputTypeDef]
else:
    _ListDbClustersPaginatorBase = Paginator  # type: ignore[assignment]

class ListDbClustersPaginator(_ListDbClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/paginator/ListDbClusters.html#TimestreamInfluxDB.Paginator.ListDbClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/paginators/#listdbclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDbClustersInputPaginateTypeDef]
    ) -> PageIterator[ListDbClustersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/paginator/ListDbClusters.html#TimestreamInfluxDB.Paginator.ListDbClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/paginators/#listdbclusterspaginator)
        """

if TYPE_CHECKING:
    _ListDbInstancesForClusterPaginatorBase = Paginator[ListDbInstancesForClusterOutputTypeDef]
else:
    _ListDbInstancesForClusterPaginatorBase = Paginator  # type: ignore[assignment]

class ListDbInstancesForClusterPaginator(_ListDbInstancesForClusterPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/paginator/ListDbInstancesForCluster.html#TimestreamInfluxDB.Paginator.ListDbInstancesForCluster)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/paginators/#listdbinstancesforclusterpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDbInstancesForClusterInputPaginateTypeDef]
    ) -> PageIterator[ListDbInstancesForClusterOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/paginator/ListDbInstancesForCluster.html#TimestreamInfluxDB.Paginator.ListDbInstancesForCluster.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/paginators/#listdbinstancesforclusterpaginator)
        """

if TYPE_CHECKING:
    _ListDbInstancesPaginatorBase = Paginator[ListDbInstancesOutputTypeDef]
else:
    _ListDbInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDbInstancesPaginator(_ListDbInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/paginator/ListDbInstances.html#TimestreamInfluxDB.Paginator.ListDbInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/paginators/#listdbinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDbInstancesInputPaginateTypeDef]
    ) -> PageIterator[ListDbInstancesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/paginator/ListDbInstances.html#TimestreamInfluxDB.Paginator.ListDbInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/paginators/#listdbinstancespaginator)
        """

if TYPE_CHECKING:
    _ListDbParameterGroupsPaginatorBase = Paginator[ListDbParameterGroupsOutputTypeDef]
else:
    _ListDbParameterGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDbParameterGroupsPaginator(_ListDbParameterGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/paginator/ListDbParameterGroups.html#TimestreamInfluxDB.Paginator.ListDbParameterGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/paginators/#listdbparametergroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDbParameterGroupsInputPaginateTypeDef]
    ) -> PageIterator[ListDbParameterGroupsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/paginator/ListDbParameterGroups.html#TimestreamInfluxDB.Paginator.ListDbParameterGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/paginators/#listdbparametergroupspaginator)
        """
