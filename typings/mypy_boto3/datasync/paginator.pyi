"""
Type annotations for datasync service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html)

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

from .type_defs import (
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/datasync.html#DataSync.Paginator.ListAgents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listagentspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAgentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/datasync.html#DataSync.Paginator.ListAgents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listagentspaginator)
        """

class ListLocationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/datasync.html#DataSync.Paginator.ListLocations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listlocationspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["LocationFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLocationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/datasync.html#DataSync.Paginator.ListLocations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listlocationspaginator)
        """

class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/datasync.html#DataSync.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listtagsforresourcepaginator)
    """

    def paginate(
        self, *, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/datasync.html#DataSync.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listtagsforresourcepaginator)
        """

class ListTaskExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/datasync.html#DataSync.Paginator.ListTaskExecutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listtaskexecutionspaginator)
    """

    def paginate(
        self, *, TaskArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTaskExecutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/datasync.html#DataSync.Paginator.ListTaskExecutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listtaskexecutionspaginator)
        """

class ListTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/datasync.html#DataSync.Paginator.ListTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listtaskspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["TaskFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/datasync.html#DataSync.Paginator.ListTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listtaskspaginator)
        """
