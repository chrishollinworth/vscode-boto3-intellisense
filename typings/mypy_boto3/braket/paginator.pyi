"""
Type annotations for braket service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_braket import BraketClient
    from mypy_boto3_braket.paginator import (
        SearchDevicesPaginator,
        SearchJobsPaginator,
        SearchQuantumTasksPaginator,
    )

    client: BraketClient = boto3.client("braket")

    search_devices_paginator: SearchDevicesPaginator = client.get_paginator("search_devices")
    search_jobs_paginator: SearchJobsPaginator = client.get_paginator("search_jobs")
    search_quantum_tasks_paginator: SearchQuantumTasksPaginator = client.get_paginator("search_quantum_tasks")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    PaginatorConfigTypeDef,
    SearchDevicesFilterTypeDef,
    SearchDevicesResponseTypeDef,
    SearchJobsFilterTypeDef,
    SearchJobsResponseTypeDef,
    SearchQuantumTasksFilterTypeDef,
    SearchQuantumTasksResponseTypeDef,
)

__all__ = ("SearchDevicesPaginator", "SearchJobsPaginator", "SearchQuantumTasksPaginator")

class SearchDevicesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/braket.html#Braket.Paginator.SearchDevices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/paginators.html#searchdevicespaginator)
    """

    def paginate(
        self,
        *,
        filters: List["SearchDevicesFilterTypeDef"],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchDevicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/braket.html#Braket.Paginator.SearchDevices.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/paginators.html#searchdevicespaginator)
        """

class SearchJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/braket.html#Braket.Paginator.SearchJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/paginators.html#searchjobspaginator)
    """

    def paginate(
        self,
        *,
        filters: List["SearchJobsFilterTypeDef"],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/braket.html#Braket.Paginator.SearchJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/paginators.html#searchjobspaginator)
        """

class SearchQuantumTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/braket.html#Braket.Paginator.SearchQuantumTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/paginators.html#searchquantumtaskspaginator)
    """

    def paginate(
        self,
        *,
        filters: List["SearchQuantumTasksFilterTypeDef"],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchQuantumTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/braket.html#Braket.Paginator.SearchQuantumTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/paginators.html#searchquantumtaskspaginator)
        """
