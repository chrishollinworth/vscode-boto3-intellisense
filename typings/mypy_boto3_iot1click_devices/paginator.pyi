# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for iot1click-devices service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_iot1click_devices import IoT1ClickDevicesServiceClient
    from mypy_boto3_iot1click_devices.paginator import (
        ListDeviceEventsPaginator,
        ListDevicesPaginator,
    )

    client: IoT1ClickDevicesServiceClient = boto3.client("iot1click-devices")

    list_device_events_paginator: ListDeviceEventsPaginator = client.get_paginator("list_device_events")
    list_devices_paginator: ListDevicesPaginator = client.get_paginator("list_devices")
    ```
"""
from datetime import datetime
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_iot1click_devices.type_defs import (
    ListDeviceEventsResponseTypeDef,
    ListDevicesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListDeviceEventsPaginator", "ListDevicesPaginator")


class ListDeviceEventsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeviceEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Paginator.ListDeviceEvents)
    """

    def paginate(
        self,
        DeviceId: str,
        FromTimeStamp: datetime,
        ToTimeStamp: datetime,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDeviceEventsResponseTypeDef]:
        """
        [ListDeviceEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Paginator.ListDeviceEvents.paginate)
        """


class ListDevicesPaginator(Boto3Paginator):
    """
    [Paginator.ListDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Paginator.ListDevices)
    """

    def paginate(
        self, DeviceType: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDevicesResponseTypeDef]:
        """
        [ListDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Paginator.ListDevices.paginate)
        """
