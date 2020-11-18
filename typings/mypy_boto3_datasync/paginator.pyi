# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for datasync service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_datasync import DataSyncClient
    from mypy_boto3_datasync.paginator import (
        ListAgentsPaginator,
        ListLocationsPaginator,
        ListTagsForResourcePaginator,
        ListTaskExecutionsPaginator,
        ListTasksPaginator,
    )

    client: DataSyncClient = boto3.client("datasync")

    list_agents_paginator: ListAgentsPaginator = client.get_paginator("list_agents")
    list_locations_paginator: ListLocationsPaginator = client.get_paginator("list_locations")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_task_executions_paginator: ListTaskExecutionsPaginator = client.get_paginator("list_task_executions")
    list_tasks_paginator: ListTasksPaginator = client.get_paginator("list_tasks")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_datasync.type_defs import (
    ListAgentsResponseTypeDef,
    ListLocationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTaskExecutionsResponseTypeDef,
    ListTasksResponseTypeDef,
    LocationFilterTypeDef,
    PaginatorConfigTypeDef,
    TaskFilterTypeDef,
)

__all__ = (
    "ListAgentsPaginator",
    "ListLocationsPaginator",
    "ListTagsForResourcePaginator",
    "ListTaskExecutionsPaginator",
    "ListTasksPaginator",
)


class ListAgentsPaginator(Boto3Paginator):
    """
    [Paginator.ListAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/datasync.html#DataSync.Paginator.ListAgents)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAgentsResponseTypeDef]:
        """
        [ListAgents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/datasync.html#DataSync.Paginator.ListAgents.paginate)
        """


class ListLocationsPaginator(Boto3Paginator):
    """
    [Paginator.ListLocations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/datasync.html#DataSync.Paginator.ListLocations)
    """

    def paginate(
        self,
        Filters: List[LocationFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListLocationsResponseTypeDef]:
        """
        [ListLocations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/datasync.html#DataSync.Paginator.ListLocations.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/datasync.html#DataSync.Paginator.ListTagsForResource)
    """

    def paginate(
        self, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/datasync.html#DataSync.Paginator.ListTagsForResource.paginate)
        """


class ListTaskExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListTaskExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/datasync.html#DataSync.Paginator.ListTaskExecutions)
    """

    def paginate(
        self, TaskArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTaskExecutionsResponseTypeDef]:
        """
        [ListTaskExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/datasync.html#DataSync.Paginator.ListTaskExecutions.paginate)
        """


class ListTasksPaginator(Boto3Paginator):
    """
    [Paginator.ListTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/datasync.html#DataSync.Paginator.ListTasks)
    """

    def paginate(
        self,
        Filters: List[TaskFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTasksResponseTypeDef]:
        """
        [ListTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/datasync.html#DataSync.Paginator.ListTasks.paginate)
        """
