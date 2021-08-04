"""
Type annotations for iot1click-devices service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iot1click_devices.type_defs import ClaimDevicesByClaimCodeRequestRequestTypeDef

    data: ClaimDevicesByClaimCodeRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ClaimDevicesByClaimCodeRequestRequestTypeDef",
    "ClaimDevicesByClaimCodeResponseTypeDef",
    "DescribeDeviceRequestRequestTypeDef",
    "DescribeDeviceResponseTypeDef",
    "DeviceDescriptionTypeDef",
    "DeviceEventTypeDef",
    "DeviceMethodTypeDef",
    "DeviceTypeDef",
    "FinalizeDeviceClaimRequestRequestTypeDef",
    "FinalizeDeviceClaimResponseTypeDef",
    "GetDeviceMethodsRequestRequestTypeDef",
    "GetDeviceMethodsResponseTypeDef",
    "InitiateDeviceClaimRequestRequestTypeDef",
    "InitiateDeviceClaimResponseTypeDef",
    "InvokeDeviceMethodRequestRequestTypeDef",
    "InvokeDeviceMethodResponseTypeDef",
    "ListDeviceEventsRequestRequestTypeDef",
    "ListDeviceEventsResponseTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "ListDevicesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UnclaimDeviceRequestRequestTypeDef",
    "UnclaimDeviceResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDeviceStateRequestRequestTypeDef",
)

ClaimDevicesByClaimCodeRequestRequestTypeDef = TypedDict(
    "ClaimDevicesByClaimCodeRequestRequestTypeDef",
    {
        "ClaimCode": str,
    },
)

ClaimDevicesByClaimCodeResponseTypeDef = TypedDict(
    "ClaimDevicesByClaimCodeResponseTypeDef",
    {
        "ClaimCode": str,
        "Total": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeviceRequestRequestTypeDef = TypedDict(
    "DescribeDeviceRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)

DescribeDeviceResponseTypeDef = TypedDict(
    "DescribeDeviceResponseTypeDef",
    {
        "DeviceDescription": "DeviceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
    "DeviceEventTypeDef",
    {
        "Device": "DeviceTypeDef",
        "StdEvent": str,
    },
    total=False,
)

DeviceMethodTypeDef = TypedDict(
    "DeviceMethodTypeDef",
    {
        "DeviceType": str,
        "MethodName": str,
    },
    total=False,
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "Attributes": Dict[str, Any],
        "DeviceId": str,
        "Type": str,
    },
    total=False,
)

_RequiredFinalizeDeviceClaimRequestRequestTypeDef = TypedDict(
    "_RequiredFinalizeDeviceClaimRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)
_OptionalFinalizeDeviceClaimRequestRequestTypeDef = TypedDict(
    "_OptionalFinalizeDeviceClaimRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class FinalizeDeviceClaimRequestRequestTypeDef(
    _RequiredFinalizeDeviceClaimRequestRequestTypeDef,
    _OptionalFinalizeDeviceClaimRequestRequestTypeDef,
):
    pass

FinalizeDeviceClaimResponseTypeDef = TypedDict(
    "FinalizeDeviceClaimResponseTypeDef",
    {
        "State": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceMethodsRequestRequestTypeDef = TypedDict(
    "GetDeviceMethodsRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)

GetDeviceMethodsResponseTypeDef = TypedDict(
    "GetDeviceMethodsResponseTypeDef",
    {
        "DeviceMethods": List["DeviceMethodTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InitiateDeviceClaimRequestRequestTypeDef = TypedDict(
    "InitiateDeviceClaimRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)

InitiateDeviceClaimResponseTypeDef = TypedDict(
    "InitiateDeviceClaimResponseTypeDef",
    {
        "State": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredInvokeDeviceMethodRequestRequestTypeDef = TypedDict(
    "_RequiredInvokeDeviceMethodRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)
_OptionalInvokeDeviceMethodRequestRequestTypeDef = TypedDict(
    "_OptionalInvokeDeviceMethodRequestRequestTypeDef",
    {
        "DeviceMethod": "DeviceMethodTypeDef",
        "DeviceMethodParameters": str,
    },
    total=False,
)

class InvokeDeviceMethodRequestRequestTypeDef(
    _RequiredInvokeDeviceMethodRequestRequestTypeDef,
    _OptionalInvokeDeviceMethodRequestRequestTypeDef,
):
    pass

InvokeDeviceMethodResponseTypeDef = TypedDict(
    "InvokeDeviceMethodResponseTypeDef",
    {
        "DeviceMethodResponse": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDeviceEventsRequestRequestTypeDef = TypedDict(
    "_RequiredListDeviceEventsRequestRequestTypeDef",
    {
        "DeviceId": str,
        "FromTimeStamp": Union[datetime, str],
        "ToTimeStamp": Union[datetime, str],
    },
)
_OptionalListDeviceEventsRequestRequestTypeDef = TypedDict(
    "_OptionalListDeviceEventsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListDeviceEventsRequestRequestTypeDef(
    _RequiredListDeviceEventsRequestRequestTypeDef, _OptionalListDeviceEventsRequestRequestTypeDef
):
    pass

ListDeviceEventsResponseTypeDef = TypedDict(
    "ListDeviceEventsResponseTypeDef",
    {
        "Events": List["DeviceEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevicesRequestRequestTypeDef = TypedDict(
    "ListDevicesRequestRequestTypeDef",
    {
        "DeviceType": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {
        "Devices": List["DeviceDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UnclaimDeviceRequestRequestTypeDef = TypedDict(
    "UnclaimDeviceRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)

UnclaimDeviceResponseTypeDef = TypedDict(
    "UnclaimDeviceResponseTypeDef",
    {
        "State": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateDeviceStateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDeviceStateRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)
_OptionalUpdateDeviceStateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDeviceStateRequestRequestTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

class UpdateDeviceStateRequestRequestTypeDef(
    _RequiredUpdateDeviceStateRequestRequestTypeDef, _OptionalUpdateDeviceStateRequestRequestTypeDef
):
    pass
