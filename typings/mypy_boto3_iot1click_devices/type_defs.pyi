"""
Main interface for iot1click-devices service type definitions.

Usage::

    ```python
    from mypy_boto3_iot1click_devices.type_defs import DeviceDescriptionTypeDef

    data: DeviceDescriptionTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DeviceDescriptionTypeDef",
    "DeviceEventTypeDef",
    "DeviceMethodTypeDef",
    "DeviceTypeDef",
    "ClaimDevicesByClaimCodeResponseTypeDef",
    "DescribeDeviceResponseTypeDef",
    "FinalizeDeviceClaimResponseTypeDef",
    "GetDeviceMethodsResponseTypeDef",
    "InitiateDeviceClaimResponseTypeDef",
    "InvokeDeviceMethodResponseTypeDef",
    "ListDeviceEventsResponseTypeDef",
    "ListDevicesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "UnclaimDeviceResponseTypeDef",
)

DeviceDescriptionTypeDef = TypedDict(
    "DeviceDescriptionTypeDef",
    {
        "Arn": str,
        "Attributes": Dict[str, str],
        "DeviceId": str,
        "Enabled": bool,
        "RemainingLife": float,
        "Type": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

DeviceEventTypeDef = TypedDict(
    "DeviceEventTypeDef", {"Device": "DeviceTypeDef", "StdEvent": str}, total=False
)

DeviceMethodTypeDef = TypedDict(
    "DeviceMethodTypeDef", {"DeviceType": str, "MethodName": str}, total=False
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef", {"Attributes": Dict[str, Any], "DeviceId": str, "Type": str}, total=False
)

ClaimDevicesByClaimCodeResponseTypeDef = TypedDict(
    "ClaimDevicesByClaimCodeResponseTypeDef", {"ClaimCode": str, "Total": int}, total=False
)

DescribeDeviceResponseTypeDef = TypedDict(
    "DescribeDeviceResponseTypeDef", {"DeviceDescription": "DeviceDescriptionTypeDef"}, total=False
)

FinalizeDeviceClaimResponseTypeDef = TypedDict(
    "FinalizeDeviceClaimResponseTypeDef", {"State": str}, total=False
)

GetDeviceMethodsResponseTypeDef = TypedDict(
    "GetDeviceMethodsResponseTypeDef", {"DeviceMethods": List["DeviceMethodTypeDef"]}, total=False
)

InitiateDeviceClaimResponseTypeDef = TypedDict(
    "InitiateDeviceClaimResponseTypeDef", {"State": str}, total=False
)

InvokeDeviceMethodResponseTypeDef = TypedDict(
    "InvokeDeviceMethodResponseTypeDef", {"DeviceMethodResponse": str}, total=False
)

ListDeviceEventsResponseTypeDef = TypedDict(
    "ListDeviceEventsResponseTypeDef",
    {"Events": List["DeviceEventTypeDef"], "NextToken": str},
    total=False,
)

ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {"Devices": List["DeviceDescriptionTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UnclaimDeviceResponseTypeDef = TypedDict(
    "UnclaimDeviceResponseTypeDef", {"State": str}, total=False
)
