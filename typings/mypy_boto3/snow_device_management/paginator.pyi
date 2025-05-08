"""
Type annotations for snow-device-management service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_snow_device_management.client import SnowDeviceManagementClient
    from mypy_boto3_snow_device_management.paginator import (
        ListDeviceResourcesPaginator,
        ListDevicesPaginator,
        ListExecutionsPaginator,
        ListTasksPaginator,
    )

    session = Session()
    client: SnowDeviceManagementClient = session.client("snow-device-management")

    list_device_resources_paginator: ListDeviceResourcesPaginator = client.get_paginator("list_device_resources")
    list_devices_paginator: ListDevicesPaginator = client.get_paginator("list_devices")
    list_executions_paginator: ListExecutionsPaginator = client.get_paginator("list_executions")
    list_tasks_paginator: ListTasksPaginator = client.get_paginator("list_tasks")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListDeviceResourcesInputPaginateTypeDef,
    ListDeviceResourcesOutputTypeDef,
    ListDevicesInputPaginateTypeDef,
    ListDevicesOutputTypeDef,
    ListExecutionsInputPaginateTypeDef,
    ListExecutionsOutputTypeDef,
    ListTasksInputPaginateTypeDef,
    ListTasksOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListDeviceResourcesPaginator",
    "ListDevicesPaginator",
    "ListExecutionsPaginator",
    "ListTasksPaginator",
)

if TYPE_CHECKING:
    _ListDeviceResourcesPaginatorBase = Paginator[ListDeviceResourcesOutputTypeDef]
else:
    _ListDeviceResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeviceResourcesPaginator(_ListDeviceResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/paginator/ListDeviceResources.html#SnowDeviceManagement.Paginator.ListDeviceResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators/#listdeviceresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeviceResourcesInputPaginateTypeDef]
    ) -> PageIterator[ListDeviceResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/paginator/ListDeviceResources.html#SnowDeviceManagement.Paginator.ListDeviceResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators/#listdeviceresourcespaginator)
        """

if TYPE_CHECKING:
    _ListDevicesPaginatorBase = Paginator[ListDevicesOutputTypeDef]
else:
    _ListDevicesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDevicesPaginator(_ListDevicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/paginator/ListDevices.html#SnowDeviceManagement.Paginator.ListDevices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators/#listdevicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDevicesInputPaginateTypeDef]
    ) -> PageIterator[ListDevicesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/paginator/ListDevices.html#SnowDeviceManagement.Paginator.ListDevices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators/#listdevicespaginator)
        """

if TYPE_CHECKING:
    _ListExecutionsPaginatorBase = Paginator[ListExecutionsOutputTypeDef]
else:
    _ListExecutionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListExecutionsPaginator(_ListExecutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/paginator/ListExecutions.html#SnowDeviceManagement.Paginator.ListExecutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators/#listexecutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListExecutionsInputPaginateTypeDef]
    ) -> PageIterator[ListExecutionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/paginator/ListExecutions.html#SnowDeviceManagement.Paginator.ListExecutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators/#listexecutionspaginator)
        """

if TYPE_CHECKING:
    _ListTasksPaginatorBase = Paginator[ListTasksOutputTypeDef]
else:
    _ListTasksPaginatorBase = Paginator  # type: ignore[assignment]

class ListTasksPaginator(_ListTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/paginator/ListTasks.html#SnowDeviceManagement.Paginator.ListTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators/#listtaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTasksInputPaginateTypeDef]
    ) -> PageIterator[ListTasksOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/paginator/ListTasks.html#SnowDeviceManagement.Paginator.ListTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators/#listtaskspaginator)
        """
