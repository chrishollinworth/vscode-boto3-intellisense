"""
Type annotations for datasync service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_datasync.client import DataSyncClient
    from mypy_boto3_datasync.paginator import (
        DescribeStorageSystemResourceMetricsPaginator,
        ListAgentsPaginator,
        ListDiscoveryJobsPaginator,
        ListLocationsPaginator,
        ListStorageSystemsPaginator,
        ListTagsForResourcePaginator,
        ListTaskExecutionsPaginator,
        ListTasksPaginator,
    )

    session = Session()
    client: DataSyncClient = session.client("datasync")

    describe_storage_system_resource_metrics_paginator: DescribeStorageSystemResourceMetricsPaginator = client.get_paginator("describe_storage_system_resource_metrics")
    list_agents_paginator: ListAgentsPaginator = client.get_paginator("list_agents")
    list_discovery_jobs_paginator: ListDiscoveryJobsPaginator = client.get_paginator("list_discovery_jobs")
    list_locations_paginator: ListLocationsPaginator = client.get_paginator("list_locations")
    list_storage_systems_paginator: ListStorageSystemsPaginator = client.get_paginator("list_storage_systems")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_task_executions_paginator: ListTaskExecutionsPaginator = client.get_paginator("list_task_executions")
    list_tasks_paginator: ListTasksPaginator = client.get_paginator("list_tasks")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeStorageSystemResourceMetricsRequestPaginateTypeDef,
    DescribeStorageSystemResourceMetricsResponseTypeDef,
    ListAgentsRequestPaginateTypeDef,
    ListAgentsResponseTypeDef,
    ListDiscoveryJobsRequestPaginateTypeDef,
    ListDiscoveryJobsResponseTypeDef,
    ListLocationsRequestPaginateTypeDef,
    ListLocationsResponseTypeDef,
    ListStorageSystemsRequestPaginateTypeDef,
    ListStorageSystemsResponseTypeDef,
    ListTagsForResourceRequestPaginateTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTaskExecutionsRequestPaginateTypeDef,
    ListTaskExecutionsResponseTypeDef,
    ListTasksRequestPaginateTypeDef,
    ListTasksResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeStorageSystemResourceMetricsPaginator",
    "ListAgentsPaginator",
    "ListDiscoveryJobsPaginator",
    "ListLocationsPaginator",
    "ListStorageSystemsPaginator",
    "ListTagsForResourcePaginator",
    "ListTaskExecutionsPaginator",
    "ListTasksPaginator",
)

if TYPE_CHECKING:
    _DescribeStorageSystemResourceMetricsPaginatorBase = Paginator[
        DescribeStorageSystemResourceMetricsResponseTypeDef
    ]
else:
    _DescribeStorageSystemResourceMetricsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeStorageSystemResourceMetricsPaginator(
    _DescribeStorageSystemResourceMetricsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/paginator/DescribeStorageSystemResourceMetrics.html#DataSync.Paginator.DescribeStorageSystemResourceMetrics)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators/#describestoragesystemresourcemetricspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStorageSystemResourceMetricsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeStorageSystemResourceMetricsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/paginator/DescribeStorageSystemResourceMetrics.html#DataSync.Paginator.DescribeStorageSystemResourceMetrics.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators/#describestoragesystemresourcemetricspaginator)
        """

if TYPE_CHECKING:
    _ListAgentsPaginatorBase = Paginator[ListAgentsResponseTypeDef]
else:
    _ListAgentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAgentsPaginator(_ListAgentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/paginator/ListAgents.html#DataSync.Paginator.ListAgents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators/#listagentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAgentsRequestPaginateTypeDef]
    ) -> PageIterator[ListAgentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/paginator/ListAgents.html#DataSync.Paginator.ListAgents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators/#listagentspaginator)
        """

if TYPE_CHECKING:
    _ListDiscoveryJobsPaginatorBase = Paginator[ListDiscoveryJobsResponseTypeDef]
else:
    _ListDiscoveryJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDiscoveryJobsPaginator(_ListDiscoveryJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/paginator/ListDiscoveryJobs.html#DataSync.Paginator.ListDiscoveryJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators/#listdiscoveryjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDiscoveryJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListDiscoveryJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/paginator/ListDiscoveryJobs.html#DataSync.Paginator.ListDiscoveryJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators/#listdiscoveryjobspaginator)
        """

if TYPE_CHECKING:
    _ListLocationsPaginatorBase = Paginator[ListLocationsResponseTypeDef]
else:
    _ListLocationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListLocationsPaginator(_ListLocationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/paginator/ListLocations.html#DataSync.Paginator.ListLocations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators/#listlocationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLocationsRequestPaginateTypeDef]
    ) -> PageIterator[ListLocationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/paginator/ListLocations.html#DataSync.Paginator.ListLocations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators/#listlocationspaginator)
        """

if TYPE_CHECKING:
    _ListStorageSystemsPaginatorBase = Paginator[ListStorageSystemsResponseTypeDef]
else:
    _ListStorageSystemsPaginatorBase = Paginator  # type: ignore[assignment]

class ListStorageSystemsPaginator(_ListStorageSystemsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/paginator/ListStorageSystems.html#DataSync.Paginator.ListStorageSystems)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators/#liststoragesystemspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStorageSystemsRequestPaginateTypeDef]
    ) -> PageIterator[ListStorageSystemsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/paginator/ListStorageSystems.html#DataSync.Paginator.ListStorageSystems.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators/#liststoragesystemspaginator)
        """

if TYPE_CHECKING:
    _ListTagsForResourcePaginatorBase = Paginator[ListTagsForResourceResponseTypeDef]
else:
    _ListTagsForResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsForResourcePaginator(_ListTagsForResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/paginator/ListTagsForResource.html#DataSync.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators/#listtagsforresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsForResourceRequestPaginateTypeDef]
    ) -> PageIterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/paginator/ListTagsForResource.html#DataSync.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators/#listtagsforresourcepaginator)
        """

if TYPE_CHECKING:
    _ListTaskExecutionsPaginatorBase = Paginator[ListTaskExecutionsResponseTypeDef]
else:
    _ListTaskExecutionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTaskExecutionsPaginator(_ListTaskExecutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/paginator/ListTaskExecutions.html#DataSync.Paginator.ListTaskExecutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators/#listtaskexecutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTaskExecutionsRequestPaginateTypeDef]
    ) -> PageIterator[ListTaskExecutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/paginator/ListTaskExecutions.html#DataSync.Paginator.ListTaskExecutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators/#listtaskexecutionspaginator)
        """

if TYPE_CHECKING:
    _ListTasksPaginatorBase = Paginator[ListTasksResponseTypeDef]
else:
    _ListTasksPaginatorBase = Paginator  # type: ignore[assignment]

class ListTasksPaginator(_ListTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/paginator/ListTasks.html#DataSync.Paginator.ListTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators/#listtaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTasksRequestPaginateTypeDef]
    ) -> PageIterator[ListTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/paginator/ListTasks.html#DataSync.Paginator.ListTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators/#listtaskspaginator)
        """
