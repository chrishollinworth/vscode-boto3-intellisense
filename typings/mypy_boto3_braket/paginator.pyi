# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for braket service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_braket import BraketClient
    from mypy_boto3_braket.paginator import (
        SearchDevicesPaginator,
        SearchQuantumTasksPaginator,
    )

    client: BraketClient = boto3.client("braket")

    search_devices_paginator: SearchDevicesPaginator = client.get_paginator("search_devices")
    search_quantum_tasks_paginator: SearchQuantumTasksPaginator = client.get_paginator("search_quantum_tasks")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_braket.type_defs import (
    PaginatorConfigTypeDef,
    SearchDevicesFilterTypeDef,
    SearchDevicesResponseTypeDef,
    SearchQuantumTasksFilterTypeDef,
    SearchQuantumTasksResponseTypeDef,
)

__all__ = ("SearchDevicesPaginator", "SearchQuantumTasksPaginator")


class SearchDevicesPaginator(Boto3Paginator):
    """
    [Paginator.SearchDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/braket.html#Braket.Paginator.SearchDevices)
    """

    def paginate(
        self,
        filters: List[SearchDevicesFilterTypeDef],
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[SearchDevicesResponseTypeDef]:
        """
        [SearchDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/braket.html#Braket.Paginator.SearchDevices.paginate)
        """


class SearchQuantumTasksPaginator(Boto3Paginator):
    """
    [Paginator.SearchQuantumTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/braket.html#Braket.Paginator.SearchQuantumTasks)
    """

    def paginate(
        self,
        filters: List[SearchQuantumTasksFilterTypeDef],
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[SearchQuantumTasksResponseTypeDef]:
        """
        [SearchQuantumTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/braket.html#Braket.Paginator.SearchQuantumTasks.paginate)
        """
