"""
Type annotations for snow-device-management service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_snow_device_management import SnowDeviceManagementClient
    from mypy_boto3_snow_device_management.paginator import (
        ListDeviceResourcesPaginator,
        ListDevicesPaginator,
        ListExecutionsPaginator,
        ListTasksPaginator,
    )

    client: SnowDeviceManagementClient = boto3.client("snow-device-management")

    list_device_resources_paginator: ListDeviceResourcesPaginator = client.get_paginator("list_device_resources")
    list_devices_paginator: ListDevicesPaginator = client.get_paginator("list_devices")
    list_executions_paginator: ListExecutionsPaginator = client.get_paginator("list_executions")
    list_tasks_paginator: ListTasksPaginator = client.get_paginator("list_tasks")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ExecutionStateType, TaskStateType
from .type_defs import (
    ListDeviceResourcesOutputTypeDef,
    ListDevicesOutputTypeDef,
    ListExecutionsOutputTypeDef,
    ListTasksOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListDeviceResourcesPaginator",
    "ListDevicesPaginator",
    "ListExecutionsPaginator",
    "ListTasksPaginator",
)

class ListDeviceResourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/snow-device-management.html#SnowDeviceManagement.Paginator.ListDeviceResources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators.html#listdeviceresourcespaginator)
    """

    def paginate(
        self,
        *,
        managedDeviceId: str,
        type: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeviceResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/snow-device-management.html#SnowDeviceManagement.Paginator.ListDeviceResources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators.html#listdeviceresourcespaginator)
        """

class ListDevicesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/snow-device-management.html#SnowDeviceManagement.Paginator.ListDevices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators.html#listdevicespaginator)
    """

    def paginate(
        self, *, jobId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDevicesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/snow-device-management.html#SnowDeviceManagement.Paginator.ListDevices.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators.html#listdevicespaginator)
        """

class ListExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/snow-device-management.html#SnowDeviceManagement.Paginator.ListExecutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators.html#listexecutionspaginator)
    """

    def paginate(
        self,
        *,
        taskId: str,
        state: ExecutionStateType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListExecutionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/snow-device-management.html#SnowDeviceManagement.Paginator.ListExecutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators.html#listexecutionspaginator)
        """

class ListTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/snow-device-management.html#SnowDeviceManagement.Paginator.ListTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators.html#listtaskspaginator)
    """

    def paginate(
        self, *, state: TaskStateType = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTasksOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/snow-device-management.html#SnowDeviceManagement.Paginator.ListTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators.html#listtaskspaginator)
        """
