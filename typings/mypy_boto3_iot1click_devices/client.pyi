# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for iot1click-devices service client

Usage::

    ```python
    import boto3
    from mypy_boto3_iot1click_devices import IoT1ClickDevicesServiceClient

    client: IoT1ClickDevicesServiceClient = boto3.client("iot1click-devices")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_iot1click_devices.paginator import ListDeviceEventsPaginator, ListDevicesPaginator
from mypy_boto3_iot1click_devices.type_defs import (
    ClaimDevicesByClaimCodeResponseTypeDef,
    DescribeDeviceResponseTypeDef,
    DeviceMethodTypeDef,
    FinalizeDeviceClaimResponseTypeDef,
    GetDeviceMethodsResponseTypeDef,
    InitiateDeviceClaimResponseTypeDef,
    InvokeDeviceMethodResponseTypeDef,
    ListDeviceEventsResponseTypeDef,
    ListDevicesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    UnclaimDeviceResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IoT1ClickDevicesServiceClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    ForbiddenException: Type[Boto3ClientError]
    InternalFailureException: Type[Boto3ClientError]
    InvalidRequestException: Type[Boto3ClientError]
    PreconditionFailedException: Type[Boto3ClientError]
    RangeNotSatisfiableException: Type[Boto3ClientError]
    ResourceConflictException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]


class IoT1ClickDevicesServiceClient:
    """
    [IoT1ClickDevicesService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.can_paginate)
        """

    def claim_devices_by_claim_code(self, ClaimCode: str) -> ClaimDevicesByClaimCodeResponseTypeDef:
        """
        [Client.claim_devices_by_claim_code documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.claim_devices_by_claim_code)
        """

    def describe_device(self, DeviceId: str) -> DescribeDeviceResponseTypeDef:
        """
        [Client.describe_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.describe_device)
        """

    def finalize_device_claim(
        self, DeviceId: str, Tags: Dict[str, str] = None
    ) -> FinalizeDeviceClaimResponseTypeDef:
        """
        [Client.finalize_device_claim documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.finalize_device_claim)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.generate_presigned_url)
        """

    def get_device_methods(self, DeviceId: str) -> GetDeviceMethodsResponseTypeDef:
        """
        [Client.get_device_methods documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.get_device_methods)
        """

    def initiate_device_claim(self, DeviceId: str) -> InitiateDeviceClaimResponseTypeDef:
        """
        [Client.initiate_device_claim documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.initiate_device_claim)
        """

    def invoke_device_method(
        self,
        DeviceId: str,
        DeviceMethod: "DeviceMethodTypeDef" = None,
        DeviceMethodParameters: str = None,
    ) -> InvokeDeviceMethodResponseTypeDef:
        """
        [Client.invoke_device_method documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.invoke_device_method)
        """

    def list_device_events(
        self,
        DeviceId: str,
        FromTimeStamp: datetime,
        ToTimeStamp: datetime,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListDeviceEventsResponseTypeDef:
        """
        [Client.list_device_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.list_device_events)
        """

    def list_devices(
        self, DeviceType: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListDevicesResponseTypeDef:
        """
        [Client.list_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.list_devices)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.list_tags_for_resource)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.tag_resource)
        """

    def unclaim_device(self, DeviceId: str) -> UnclaimDeviceResponseTypeDef:
        """
        [Client.unclaim_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.unclaim_device)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.untag_resource)
        """

    def update_device_state(self, DeviceId: str, Enabled: bool = None) -> Dict[str, Any]:
        """
        [Client.update_device_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.update_device_state)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_events"]
    ) -> ListDeviceEventsPaginator:
        """
        [Paginator.ListDeviceEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Paginator.ListDeviceEvents)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_devices"]) -> ListDevicesPaginator:
        """
        [Paginator.ListDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Paginator.ListDevices)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
