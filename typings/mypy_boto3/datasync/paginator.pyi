"""
Type annotations for datasync service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_datasync import DataSyncClient
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

    client: DataSyncClient = boto3.client("datasync")

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
from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import DiscoveryResourceTypeType
from .type_defs import (
    DescribeStorageSystemResourceMetricsResponseTypeDef,
    ListAgentsResponseTypeDef,
    ListDiscoveryJobsResponseTypeDef,
    ListLocationsResponseTypeDef,
    ListStorageSystemsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTaskExecutionsResponseTypeDef,
    ListTasksResponseTypeDef,
    LocationFilterTypeDef,
    PaginatorConfigTypeDef,
    TaskFilterTypeDef,
)

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

class DescribeStorageSystemResourceMetricsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datasync.html#DataSync.Paginator.DescribeStorageSystemResourceMetrics)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#describestoragesystemresourcemetricspaginator)
    """

    def paginate(
        self,
        *,
        DiscoveryJobArn: str,
        ResourceType: DiscoveryResourceTypeType,
        ResourceId: str,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeStorageSystemResourceMetricsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datasync.html#DataSync.Paginator.DescribeStorageSystemResourceMetrics.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#describestoragesystemresourcemetricspaginator)
        """

class ListAgentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datasync.html#DataSync.Paginator.ListAgents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listagentspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAgentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datasync.html#DataSync.Paginator.ListAgents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listagentspaginator)
        """

class ListDiscoveryJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datasync.html#DataSync.Paginator.ListDiscoveryJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listdiscoveryjobspaginator)
    """

    def paginate(
        self, *, StorageSystemArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDiscoveryJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datasync.html#DataSync.Paginator.ListDiscoveryJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listdiscoveryjobspaginator)
        """

class ListLocationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datasync.html#DataSync.Paginator.ListLocations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listlocationspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["LocationFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLocationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datasync.html#DataSync.Paginator.ListLocations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listlocationspaginator)
        """

class ListStorageSystemsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datasync.html#DataSync.Paginator.ListStorageSystems)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#liststoragesystemspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStorageSystemsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datasync.html#DataSync.Paginator.ListStorageSystems.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#liststoragesystemspaginator)
        """

class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datasync.html#DataSync.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listtagsforresourcepaginator)
    """

    def paginate(
        self, *, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datasync.html#DataSync.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listtagsforresourcepaginator)
        """

class ListTaskExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datasync.html#DataSync.Paginator.ListTaskExecutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listtaskexecutionspaginator)
    """

    def paginate(
        self, *, TaskArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTaskExecutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datasync.html#DataSync.Paginator.ListTaskExecutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listtaskexecutionspaginator)
        """

class ListTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datasync.html#DataSync.Paginator.ListTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listtaskspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["TaskFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datasync.html#DataSync.Paginator.ListTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listtaskspaginator)
        """
