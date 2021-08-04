"""
Type annotations for globalaccelerator service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/type_defs.html)

Usage::

    ```python
    from mypy_boto3_globalaccelerator.type_defs import AcceleratorAttributesTypeDef

    data: AcceleratorAttributesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AcceleratorStatusType,
    ByoipCidrStateType,
    ClientAffinityType,
    CustomRoutingAcceleratorStatusType,
    CustomRoutingDestinationTrafficStateType,
    CustomRoutingProtocolType,
    HealthCheckProtocolType,
    HealthStateType,
    ProtocolType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AcceleratorAttributesTypeDef",
    "AcceleratorTypeDef",
    "AddCustomRoutingEndpointsRequestRequestTypeDef",
    "AddCustomRoutingEndpointsResponseTypeDef",
    "AdvertiseByoipCidrRequestRequestTypeDef",
    "AdvertiseByoipCidrResponseTypeDef",
    "AllowCustomRoutingTrafficRequestRequestTypeDef",
    "ByoipCidrEventTypeDef",
    "ByoipCidrTypeDef",
    "CidrAuthorizationContextTypeDef",
    "CreateAcceleratorRequestRequestTypeDef",
    "CreateAcceleratorResponseTypeDef",
    "CreateCustomRoutingAcceleratorRequestRequestTypeDef",
    "CreateCustomRoutingAcceleratorResponseTypeDef",
    "CreateCustomRoutingEndpointGroupRequestRequestTypeDef",
    "CreateCustomRoutingEndpointGroupResponseTypeDef",
    "CreateCustomRoutingListenerRequestRequestTypeDef",
    "CreateCustomRoutingListenerResponseTypeDef",
    "CreateEndpointGroupRequestRequestTypeDef",
    "CreateEndpointGroupResponseTypeDef",
    "CreateListenerRequestRequestTypeDef",
    "CreateListenerResponseTypeDef",
    "CustomRoutingAcceleratorAttributesTypeDef",
    "CustomRoutingAcceleratorTypeDef",
    "CustomRoutingDestinationConfigurationTypeDef",
    "CustomRoutingDestinationDescriptionTypeDef",
    "CustomRoutingEndpointConfigurationTypeDef",
    "CustomRoutingEndpointDescriptionTypeDef",
    "CustomRoutingEndpointGroupTypeDef",
    "CustomRoutingListenerTypeDef",
    "DeleteAcceleratorRequestRequestTypeDef",
    "DeleteCustomRoutingAcceleratorRequestRequestTypeDef",
    "DeleteCustomRoutingEndpointGroupRequestRequestTypeDef",
    "DeleteCustomRoutingListenerRequestRequestTypeDef",
    "DeleteEndpointGroupRequestRequestTypeDef",
    "DeleteListenerRequestRequestTypeDef",
    "DenyCustomRoutingTrafficRequestRequestTypeDef",
    "DeprovisionByoipCidrRequestRequestTypeDef",
    "DeprovisionByoipCidrResponseTypeDef",
    "DescribeAcceleratorAttributesRequestRequestTypeDef",
    "DescribeAcceleratorAttributesResponseTypeDef",
    "DescribeAcceleratorRequestRequestTypeDef",
    "DescribeAcceleratorResponseTypeDef",
    "DescribeCustomRoutingAcceleratorAttributesRequestRequestTypeDef",
    "DescribeCustomRoutingAcceleratorAttributesResponseTypeDef",
    "DescribeCustomRoutingAcceleratorRequestRequestTypeDef",
    "DescribeCustomRoutingAcceleratorResponseTypeDef",
    "DescribeCustomRoutingEndpointGroupRequestRequestTypeDef",
    "DescribeCustomRoutingEndpointGroupResponseTypeDef",
    "DescribeCustomRoutingListenerRequestRequestTypeDef",
    "DescribeCustomRoutingListenerResponseTypeDef",
    "DescribeEndpointGroupRequestRequestTypeDef",
    "DescribeEndpointGroupResponseTypeDef",
    "DescribeListenerRequestRequestTypeDef",
    "DescribeListenerResponseTypeDef",
    "DestinationPortMappingTypeDef",
    "EndpointConfigurationTypeDef",
    "EndpointDescriptionTypeDef",
    "EndpointGroupTypeDef",
    "IpSetTypeDef",
    "ListAcceleratorsRequestRequestTypeDef",
    "ListAcceleratorsResponseTypeDef",
    "ListByoipCidrsRequestRequestTypeDef",
    "ListByoipCidrsResponseTypeDef",
    "ListCustomRoutingAcceleratorsRequestRequestTypeDef",
    "ListCustomRoutingAcceleratorsResponseTypeDef",
    "ListCustomRoutingEndpointGroupsRequestRequestTypeDef",
    "ListCustomRoutingEndpointGroupsResponseTypeDef",
    "ListCustomRoutingListenersRequestRequestTypeDef",
    "ListCustomRoutingListenersResponseTypeDef",
    "ListCustomRoutingPortMappingsByDestinationRequestRequestTypeDef",
    "ListCustomRoutingPortMappingsByDestinationResponseTypeDef",
    "ListCustomRoutingPortMappingsRequestRequestTypeDef",
    "ListCustomRoutingPortMappingsResponseTypeDef",
    "ListEndpointGroupsRequestRequestTypeDef",
    "ListEndpointGroupsResponseTypeDef",
    "ListListenersRequestRequestTypeDef",
    "ListListenersResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListenerTypeDef",
    "PaginatorConfigTypeDef",
    "PortMappingTypeDef",
    "PortOverrideTypeDef",
    "PortRangeTypeDef",
    "ProvisionByoipCidrRequestRequestTypeDef",
    "ProvisionByoipCidrResponseTypeDef",
    "RemoveCustomRoutingEndpointsRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SocketAddressTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAcceleratorAttributesRequestRequestTypeDef",
    "UpdateAcceleratorAttributesResponseTypeDef",
    "UpdateAcceleratorRequestRequestTypeDef",
    "UpdateAcceleratorResponseTypeDef",
    "UpdateCustomRoutingAcceleratorAttributesRequestRequestTypeDef",
    "UpdateCustomRoutingAcceleratorAttributesResponseTypeDef",
    "UpdateCustomRoutingAcceleratorRequestRequestTypeDef",
    "UpdateCustomRoutingAcceleratorResponseTypeDef",
    "UpdateCustomRoutingListenerRequestRequestTypeDef",
    "UpdateCustomRoutingListenerResponseTypeDef",
    "UpdateEndpointGroupRequestRequestTypeDef",
    "UpdateEndpointGroupResponseTypeDef",
    "UpdateListenerRequestRequestTypeDef",
    "UpdateListenerResponseTypeDef",
    "WithdrawByoipCidrRequestRequestTypeDef",
    "WithdrawByoipCidrResponseTypeDef",
)

AcceleratorAttributesTypeDef = TypedDict(
    "AcceleratorAttributesTypeDef",
    {
        "FlowLogsEnabled": bool,
        "FlowLogsS3Bucket": str,
        "FlowLogsS3Prefix": str,
    },
    total=False,
)

AcceleratorTypeDef = TypedDict(
    "AcceleratorTypeDef",
    {
        "AcceleratorArn": str,
        "Name": str,
        "IpAddressType": Literal["IPV4"],
        "Enabled": bool,
        "IpSets": List["IpSetTypeDef"],
        "DnsName": str,
        "Status": AcceleratorStatusType,
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

AddCustomRoutingEndpointsRequestRequestTypeDef = TypedDict(
    "AddCustomRoutingEndpointsRequestRequestTypeDef",
    {
        "EndpointConfigurations": List["CustomRoutingEndpointConfigurationTypeDef"],
        "EndpointGroupArn": str,
    },
)

AddCustomRoutingEndpointsResponseTypeDef = TypedDict(
    "AddCustomRoutingEndpointsResponseTypeDef",
    {
        "EndpointDescriptions": List["CustomRoutingEndpointDescriptionTypeDef"],
        "EndpointGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdvertiseByoipCidrRequestRequestTypeDef = TypedDict(
    "AdvertiseByoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
    },
)

AdvertiseByoipCidrResponseTypeDef = TypedDict(
    "AdvertiseByoipCidrResponseTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAllowCustomRoutingTrafficRequestRequestTypeDef = TypedDict(
    "_RequiredAllowCustomRoutingTrafficRequestRequestTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointId": str,
    },
)
_OptionalAllowCustomRoutingTrafficRequestRequestTypeDef = TypedDict(
    "_OptionalAllowCustomRoutingTrafficRequestRequestTypeDef",
    {
        "DestinationAddresses": List[str],
        "DestinationPorts": List[int],
        "AllowAllTrafficToEndpoint": bool,
    },
    total=False,
)

class AllowCustomRoutingTrafficRequestRequestTypeDef(
    _RequiredAllowCustomRoutingTrafficRequestRequestTypeDef,
    _OptionalAllowCustomRoutingTrafficRequestRequestTypeDef,
):
    pass

ByoipCidrEventTypeDef = TypedDict(
    "ByoipCidrEventTypeDef",
    {
        "Message": str,
        "Timestamp": datetime,
    },
    total=False,
)

ByoipCidrTypeDef = TypedDict(
    "ByoipCidrTypeDef",
    {
        "Cidr": str,
        "State": ByoipCidrStateType,
        "Events": List["ByoipCidrEventTypeDef"],
    },
    total=False,
)

CidrAuthorizationContextTypeDef = TypedDict(
    "CidrAuthorizationContextTypeDef",
    {
        "Message": str,
        "Signature": str,
    },
)

_RequiredCreateAcceleratorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAcceleratorRequestRequestTypeDef",
    {
        "Name": str,
        "IdempotencyToken": str,
    },
)
_OptionalCreateAcceleratorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAcceleratorRequestRequestTypeDef",
    {
        "IpAddressType": Literal["IPV4"],
        "IpAddresses": List[str],
        "Enabled": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateAcceleratorRequestRequestTypeDef(
    _RequiredCreateAcceleratorRequestRequestTypeDef, _OptionalCreateAcceleratorRequestRequestTypeDef
):
    pass

CreateAcceleratorResponseTypeDef = TypedDict(
    "CreateAcceleratorResponseTypeDef",
    {
        "Accelerator": "AcceleratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCustomRoutingAcceleratorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCustomRoutingAcceleratorRequestRequestTypeDef",
    {
        "Name": str,
        "IdempotencyToken": str,
    },
)
_OptionalCreateCustomRoutingAcceleratorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCustomRoutingAcceleratorRequestRequestTypeDef",
    {
        "IpAddressType": Literal["IPV4"],
        "IpAddresses": List[str],
        "Enabled": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateCustomRoutingAcceleratorRequestRequestTypeDef(
    _RequiredCreateCustomRoutingAcceleratorRequestRequestTypeDef,
    _OptionalCreateCustomRoutingAcceleratorRequestRequestTypeDef,
):
    pass

CreateCustomRoutingAcceleratorResponseTypeDef = TypedDict(
    "CreateCustomRoutingAcceleratorResponseTypeDef",
    {
        "Accelerator": "CustomRoutingAcceleratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCustomRoutingEndpointGroupRequestRequestTypeDef = TypedDict(
    "CreateCustomRoutingEndpointGroupRequestRequestTypeDef",
    {
        "ListenerArn": str,
        "EndpointGroupRegion": str,
        "DestinationConfigurations": List["CustomRoutingDestinationConfigurationTypeDef"],
        "IdempotencyToken": str,
    },
)

CreateCustomRoutingEndpointGroupResponseTypeDef = TypedDict(
    "CreateCustomRoutingEndpointGroupResponseTypeDef",
    {
        "EndpointGroup": "CustomRoutingEndpointGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCustomRoutingListenerRequestRequestTypeDef = TypedDict(
    "CreateCustomRoutingListenerRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
        "PortRanges": List["PortRangeTypeDef"],
        "IdempotencyToken": str,
    },
)

CreateCustomRoutingListenerResponseTypeDef = TypedDict(
    "CreateCustomRoutingListenerResponseTypeDef",
    {
        "Listener": "CustomRoutingListenerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEndpointGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEndpointGroupRequestRequestTypeDef",
    {
        "ListenerArn": str,
        "EndpointGroupRegion": str,
        "IdempotencyToken": str,
    },
)
_OptionalCreateEndpointGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEndpointGroupRequestRequestTypeDef",
    {
        "EndpointConfigurations": List["EndpointConfigurationTypeDef"],
        "TrafficDialPercentage": float,
        "HealthCheckPort": int,
        "HealthCheckProtocol": HealthCheckProtocolType,
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
        "PortOverrides": List["PortOverrideTypeDef"],
    },
    total=False,
)

class CreateEndpointGroupRequestRequestTypeDef(
    _RequiredCreateEndpointGroupRequestRequestTypeDef,
    _OptionalCreateEndpointGroupRequestRequestTypeDef,
):
    pass

CreateEndpointGroupResponseTypeDef = TypedDict(
    "CreateEndpointGroupResponseTypeDef",
    {
        "EndpointGroup": "EndpointGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateListenerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateListenerRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
        "PortRanges": List["PortRangeTypeDef"],
        "Protocol": ProtocolType,
        "IdempotencyToken": str,
    },
)
_OptionalCreateListenerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateListenerRequestRequestTypeDef",
    {
        "ClientAffinity": ClientAffinityType,
    },
    total=False,
)

class CreateListenerRequestRequestTypeDef(
    _RequiredCreateListenerRequestRequestTypeDef, _OptionalCreateListenerRequestRequestTypeDef
):
    pass

CreateListenerResponseTypeDef = TypedDict(
    "CreateListenerResponseTypeDef",
    {
        "Listener": "ListenerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomRoutingAcceleratorAttributesTypeDef = TypedDict(
    "CustomRoutingAcceleratorAttributesTypeDef",
    {
        "FlowLogsEnabled": bool,
        "FlowLogsS3Bucket": str,
        "FlowLogsS3Prefix": str,
    },
    total=False,
)

CustomRoutingAcceleratorTypeDef = TypedDict(
    "CustomRoutingAcceleratorTypeDef",
    {
        "AcceleratorArn": str,
        "Name": str,
        "IpAddressType": Literal["IPV4"],
        "Enabled": bool,
        "IpSets": List["IpSetTypeDef"],
        "DnsName": str,
        "Status": CustomRoutingAcceleratorStatusType,
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

CustomRoutingDestinationConfigurationTypeDef = TypedDict(
    "CustomRoutingDestinationConfigurationTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
        "Protocols": List[CustomRoutingProtocolType],
    },
)

CustomRoutingDestinationDescriptionTypeDef = TypedDict(
    "CustomRoutingDestinationDescriptionTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
        "Protocols": List[ProtocolType],
    },
    total=False,
)

CustomRoutingEndpointConfigurationTypeDef = TypedDict(
    "CustomRoutingEndpointConfigurationTypeDef",
    {
        "EndpointId": str,
    },
    total=False,
)

CustomRoutingEndpointDescriptionTypeDef = TypedDict(
    "CustomRoutingEndpointDescriptionTypeDef",
    {
        "EndpointId": str,
    },
    total=False,
)

CustomRoutingEndpointGroupTypeDef = TypedDict(
    "CustomRoutingEndpointGroupTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointGroupRegion": str,
        "DestinationDescriptions": List["CustomRoutingDestinationDescriptionTypeDef"],
        "EndpointDescriptions": List["CustomRoutingEndpointDescriptionTypeDef"],
    },
    total=False,
)

CustomRoutingListenerTypeDef = TypedDict(
    "CustomRoutingListenerTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List["PortRangeTypeDef"],
    },
    total=False,
)

DeleteAcceleratorRequestRequestTypeDef = TypedDict(
    "DeleteAcceleratorRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)

DeleteCustomRoutingAcceleratorRequestRequestTypeDef = TypedDict(
    "DeleteCustomRoutingAcceleratorRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)

DeleteCustomRoutingEndpointGroupRequestRequestTypeDef = TypedDict(
    "DeleteCustomRoutingEndpointGroupRequestRequestTypeDef",
    {
        "EndpointGroupArn": str,
    },
)

DeleteCustomRoutingListenerRequestRequestTypeDef = TypedDict(
    "DeleteCustomRoutingListenerRequestRequestTypeDef",
    {
        "ListenerArn": str,
    },
)

DeleteEndpointGroupRequestRequestTypeDef = TypedDict(
    "DeleteEndpointGroupRequestRequestTypeDef",
    {
        "EndpointGroupArn": str,
    },
)

DeleteListenerRequestRequestTypeDef = TypedDict(
    "DeleteListenerRequestRequestTypeDef",
    {
        "ListenerArn": str,
    },
)

_RequiredDenyCustomRoutingTrafficRequestRequestTypeDef = TypedDict(
    "_RequiredDenyCustomRoutingTrafficRequestRequestTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointId": str,
    },
)
_OptionalDenyCustomRoutingTrafficRequestRequestTypeDef = TypedDict(
    "_OptionalDenyCustomRoutingTrafficRequestRequestTypeDef",
    {
        "DestinationAddresses": List[str],
        "DestinationPorts": List[int],
        "DenyAllTrafficToEndpoint": bool,
    },
    total=False,
)

class DenyCustomRoutingTrafficRequestRequestTypeDef(
    _RequiredDenyCustomRoutingTrafficRequestRequestTypeDef,
    _OptionalDenyCustomRoutingTrafficRequestRequestTypeDef,
):
    pass

DeprovisionByoipCidrRequestRequestTypeDef = TypedDict(
    "DeprovisionByoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
    },
)

DeprovisionByoipCidrResponseTypeDef = TypedDict(
    "DeprovisionByoipCidrResponseTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAcceleratorAttributesRequestRequestTypeDef = TypedDict(
    "DescribeAcceleratorAttributesRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)

DescribeAcceleratorAttributesResponseTypeDef = TypedDict(
    "DescribeAcceleratorAttributesResponseTypeDef",
    {
        "AcceleratorAttributes": "AcceleratorAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAcceleratorRequestRequestTypeDef = TypedDict(
    "DescribeAcceleratorRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)

DescribeAcceleratorResponseTypeDef = TypedDict(
    "DescribeAcceleratorResponseTypeDef",
    {
        "Accelerator": "AcceleratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomRoutingAcceleratorAttributesRequestRequestTypeDef = TypedDict(
    "DescribeCustomRoutingAcceleratorAttributesRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)

DescribeCustomRoutingAcceleratorAttributesResponseTypeDef = TypedDict(
    "DescribeCustomRoutingAcceleratorAttributesResponseTypeDef",
    {
        "AcceleratorAttributes": "CustomRoutingAcceleratorAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomRoutingAcceleratorRequestRequestTypeDef = TypedDict(
    "DescribeCustomRoutingAcceleratorRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)

DescribeCustomRoutingAcceleratorResponseTypeDef = TypedDict(
    "DescribeCustomRoutingAcceleratorResponseTypeDef",
    {
        "Accelerator": "CustomRoutingAcceleratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomRoutingEndpointGroupRequestRequestTypeDef = TypedDict(
    "DescribeCustomRoutingEndpointGroupRequestRequestTypeDef",
    {
        "EndpointGroupArn": str,
    },
)

DescribeCustomRoutingEndpointGroupResponseTypeDef = TypedDict(
    "DescribeCustomRoutingEndpointGroupResponseTypeDef",
    {
        "EndpointGroup": "CustomRoutingEndpointGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomRoutingListenerRequestRequestTypeDef = TypedDict(
    "DescribeCustomRoutingListenerRequestRequestTypeDef",
    {
        "ListenerArn": str,
    },
)

DescribeCustomRoutingListenerResponseTypeDef = TypedDict(
    "DescribeCustomRoutingListenerResponseTypeDef",
    {
        "Listener": "CustomRoutingListenerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointGroupRequestRequestTypeDef = TypedDict(
    "DescribeEndpointGroupRequestRequestTypeDef",
    {
        "EndpointGroupArn": str,
    },
)

DescribeEndpointGroupResponseTypeDef = TypedDict(
    "DescribeEndpointGroupResponseTypeDef",
    {
        "EndpointGroup": "EndpointGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeListenerRequestRequestTypeDef = TypedDict(
    "DescribeListenerRequestRequestTypeDef",
    {
        "ListenerArn": str,
    },
)

DescribeListenerResponseTypeDef = TypedDict(
    "DescribeListenerResponseTypeDef",
    {
        "Listener": "ListenerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationPortMappingTypeDef = TypedDict(
    "DestinationPortMappingTypeDef",
    {
        "AcceleratorArn": str,
        "AcceleratorSocketAddresses": List["SocketAddressTypeDef"],
        "EndpointGroupArn": str,
        "EndpointId": str,
        "EndpointGroupRegion": str,
        "DestinationSocketAddress": "SocketAddressTypeDef",
        "IpAddressType": Literal["IPV4"],
        "DestinationTrafficState": CustomRoutingDestinationTrafficStateType,
    },
    total=False,
)

EndpointConfigurationTypeDef = TypedDict(
    "EndpointConfigurationTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "ClientIPPreservationEnabled": bool,
    },
    total=False,
)

EndpointDescriptionTypeDef = TypedDict(
    "EndpointDescriptionTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "HealthState": HealthStateType,
        "HealthReason": str,
        "ClientIPPreservationEnabled": bool,
    },
    total=False,
)

EndpointGroupTypeDef = TypedDict(
    "EndpointGroupTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointGroupRegion": str,
        "EndpointDescriptions": List["EndpointDescriptionTypeDef"],
        "TrafficDialPercentage": float,
        "HealthCheckPort": int,
        "HealthCheckProtocol": HealthCheckProtocolType,
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
        "PortOverrides": List["PortOverrideTypeDef"],
    },
    total=False,
)

IpSetTypeDef = TypedDict(
    "IpSetTypeDef",
    {
        "IpFamily": str,
        "IpAddresses": List[str],
    },
    total=False,
)

ListAcceleratorsRequestRequestTypeDef = TypedDict(
    "ListAcceleratorsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListAcceleratorsResponseTypeDef = TypedDict(
    "ListAcceleratorsResponseTypeDef",
    {
        "Accelerators": List["AcceleratorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListByoipCidrsRequestRequestTypeDef = TypedDict(
    "ListByoipCidrsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListByoipCidrsResponseTypeDef = TypedDict(
    "ListByoipCidrsResponseTypeDef",
    {
        "ByoipCidrs": List["ByoipCidrTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomRoutingAcceleratorsRequestRequestTypeDef = TypedDict(
    "ListCustomRoutingAcceleratorsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListCustomRoutingAcceleratorsResponseTypeDef = TypedDict(
    "ListCustomRoutingAcceleratorsResponseTypeDef",
    {
        "Accelerators": List["CustomRoutingAcceleratorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCustomRoutingEndpointGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListCustomRoutingEndpointGroupsRequestRequestTypeDef",
    {
        "ListenerArn": str,
    },
)
_OptionalListCustomRoutingEndpointGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListCustomRoutingEndpointGroupsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListCustomRoutingEndpointGroupsRequestRequestTypeDef(
    _RequiredListCustomRoutingEndpointGroupsRequestRequestTypeDef,
    _OptionalListCustomRoutingEndpointGroupsRequestRequestTypeDef,
):
    pass

ListCustomRoutingEndpointGroupsResponseTypeDef = TypedDict(
    "ListCustomRoutingEndpointGroupsResponseTypeDef",
    {
        "EndpointGroups": List["CustomRoutingEndpointGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCustomRoutingListenersRequestRequestTypeDef = TypedDict(
    "_RequiredListCustomRoutingListenersRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)
_OptionalListCustomRoutingListenersRequestRequestTypeDef = TypedDict(
    "_OptionalListCustomRoutingListenersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListCustomRoutingListenersRequestRequestTypeDef(
    _RequiredListCustomRoutingListenersRequestRequestTypeDef,
    _OptionalListCustomRoutingListenersRequestRequestTypeDef,
):
    pass

ListCustomRoutingListenersResponseTypeDef = TypedDict(
    "ListCustomRoutingListenersResponseTypeDef",
    {
        "Listeners": List["CustomRoutingListenerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCustomRoutingPortMappingsByDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredListCustomRoutingPortMappingsByDestinationRequestRequestTypeDef",
    {
        "EndpointId": str,
        "DestinationAddress": str,
    },
)
_OptionalListCustomRoutingPortMappingsByDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalListCustomRoutingPortMappingsByDestinationRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListCustomRoutingPortMappingsByDestinationRequestRequestTypeDef(
    _RequiredListCustomRoutingPortMappingsByDestinationRequestRequestTypeDef,
    _OptionalListCustomRoutingPortMappingsByDestinationRequestRequestTypeDef,
):
    pass

ListCustomRoutingPortMappingsByDestinationResponseTypeDef = TypedDict(
    "ListCustomRoutingPortMappingsByDestinationResponseTypeDef",
    {
        "DestinationPortMappings": List["DestinationPortMappingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCustomRoutingPortMappingsRequestRequestTypeDef = TypedDict(
    "_RequiredListCustomRoutingPortMappingsRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)
_OptionalListCustomRoutingPortMappingsRequestRequestTypeDef = TypedDict(
    "_OptionalListCustomRoutingPortMappingsRequestRequestTypeDef",
    {
        "EndpointGroupArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListCustomRoutingPortMappingsRequestRequestTypeDef(
    _RequiredListCustomRoutingPortMappingsRequestRequestTypeDef,
    _OptionalListCustomRoutingPortMappingsRequestRequestTypeDef,
):
    pass

ListCustomRoutingPortMappingsResponseTypeDef = TypedDict(
    "ListCustomRoutingPortMappingsResponseTypeDef",
    {
        "PortMappings": List["PortMappingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEndpointGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListEndpointGroupsRequestRequestTypeDef",
    {
        "ListenerArn": str,
    },
)
_OptionalListEndpointGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListEndpointGroupsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListEndpointGroupsRequestRequestTypeDef(
    _RequiredListEndpointGroupsRequestRequestTypeDef,
    _OptionalListEndpointGroupsRequestRequestTypeDef,
):
    pass

ListEndpointGroupsResponseTypeDef = TypedDict(
    "ListEndpointGroupsResponseTypeDef",
    {
        "EndpointGroups": List["EndpointGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListListenersRequestRequestTypeDef = TypedDict(
    "_RequiredListListenersRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)
_OptionalListListenersRequestRequestTypeDef = TypedDict(
    "_OptionalListListenersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListListenersRequestRequestTypeDef(
    _RequiredListListenersRequestRequestTypeDef, _OptionalListListenersRequestRequestTypeDef
):
    pass

ListListenersResponseTypeDef = TypedDict(
    "ListListenersResponseTypeDef",
    {
        "Listeners": List["ListenerTypeDef"],
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
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List["PortRangeTypeDef"],
        "Protocol": ProtocolType,
        "ClientAffinity": ClientAffinityType,
    },
    total=False,
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

PortMappingTypeDef = TypedDict(
    "PortMappingTypeDef",
    {
        "AcceleratorPort": int,
        "EndpointGroupArn": str,
        "EndpointId": str,
        "DestinationSocketAddress": "SocketAddressTypeDef",
        "Protocols": List[CustomRoutingProtocolType],
        "DestinationTrafficState": CustomRoutingDestinationTrafficStateType,
    },
    total=False,
)

PortOverrideTypeDef = TypedDict(
    "PortOverrideTypeDef",
    {
        "ListenerPort": int,
        "EndpointPort": int,
    },
    total=False,
)

PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
    },
    total=False,
)

ProvisionByoipCidrRequestRequestTypeDef = TypedDict(
    "ProvisionByoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
        "CidrAuthorizationContext": "CidrAuthorizationContextTypeDef",
    },
)

ProvisionByoipCidrResponseTypeDef = TypedDict(
    "ProvisionByoipCidrResponseTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveCustomRoutingEndpointsRequestRequestTypeDef = TypedDict(
    "RemoveCustomRoutingEndpointsRequestRequestTypeDef",
    {
        "EndpointIds": List[str],
        "EndpointGroupArn": str,
    },
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

SocketAddressTypeDef = TypedDict(
    "SocketAddressTypeDef",
    {
        "IpAddress": str,
        "Port": int,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAcceleratorAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAcceleratorAttributesRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)
_OptionalUpdateAcceleratorAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAcceleratorAttributesRequestRequestTypeDef",
    {
        "FlowLogsEnabled": bool,
        "FlowLogsS3Bucket": str,
        "FlowLogsS3Prefix": str,
    },
    total=False,
)

class UpdateAcceleratorAttributesRequestRequestTypeDef(
    _RequiredUpdateAcceleratorAttributesRequestRequestTypeDef,
    _OptionalUpdateAcceleratorAttributesRequestRequestTypeDef,
):
    pass

UpdateAcceleratorAttributesResponseTypeDef = TypedDict(
    "UpdateAcceleratorAttributesResponseTypeDef",
    {
        "AcceleratorAttributes": "AcceleratorAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAcceleratorRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAcceleratorRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)
_OptionalUpdateAcceleratorRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAcceleratorRequestRequestTypeDef",
    {
        "Name": str,
        "IpAddressType": Literal["IPV4"],
        "Enabled": bool,
    },
    total=False,
)

class UpdateAcceleratorRequestRequestTypeDef(
    _RequiredUpdateAcceleratorRequestRequestTypeDef, _OptionalUpdateAcceleratorRequestRequestTypeDef
):
    pass

UpdateAcceleratorResponseTypeDef = TypedDict(
    "UpdateAcceleratorResponseTypeDef",
    {
        "Accelerator": "AcceleratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateCustomRoutingAcceleratorAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCustomRoutingAcceleratorAttributesRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)
_OptionalUpdateCustomRoutingAcceleratorAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCustomRoutingAcceleratorAttributesRequestRequestTypeDef",
    {
        "FlowLogsEnabled": bool,
        "FlowLogsS3Bucket": str,
        "FlowLogsS3Prefix": str,
    },
    total=False,
)

class UpdateCustomRoutingAcceleratorAttributesRequestRequestTypeDef(
    _RequiredUpdateCustomRoutingAcceleratorAttributesRequestRequestTypeDef,
    _OptionalUpdateCustomRoutingAcceleratorAttributesRequestRequestTypeDef,
):
    pass

UpdateCustomRoutingAcceleratorAttributesResponseTypeDef = TypedDict(
    "UpdateCustomRoutingAcceleratorAttributesResponseTypeDef",
    {
        "AcceleratorAttributes": "CustomRoutingAcceleratorAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateCustomRoutingAcceleratorRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCustomRoutingAcceleratorRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)
_OptionalUpdateCustomRoutingAcceleratorRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCustomRoutingAcceleratorRequestRequestTypeDef",
    {
        "Name": str,
        "IpAddressType": Literal["IPV4"],
        "Enabled": bool,
    },
    total=False,
)

class UpdateCustomRoutingAcceleratorRequestRequestTypeDef(
    _RequiredUpdateCustomRoutingAcceleratorRequestRequestTypeDef,
    _OptionalUpdateCustomRoutingAcceleratorRequestRequestTypeDef,
):
    pass

UpdateCustomRoutingAcceleratorResponseTypeDef = TypedDict(
    "UpdateCustomRoutingAcceleratorResponseTypeDef",
    {
        "Accelerator": "CustomRoutingAcceleratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCustomRoutingListenerRequestRequestTypeDef = TypedDict(
    "UpdateCustomRoutingListenerRequestRequestTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List["PortRangeTypeDef"],
    },
)

UpdateCustomRoutingListenerResponseTypeDef = TypedDict(
    "UpdateCustomRoutingListenerResponseTypeDef",
    {
        "Listener": "CustomRoutingListenerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEndpointGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEndpointGroupRequestRequestTypeDef",
    {
        "EndpointGroupArn": str,
    },
)
_OptionalUpdateEndpointGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEndpointGroupRequestRequestTypeDef",
    {
        "EndpointConfigurations": List["EndpointConfigurationTypeDef"],
        "TrafficDialPercentage": float,
        "HealthCheckPort": int,
        "HealthCheckProtocol": HealthCheckProtocolType,
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
        "PortOverrides": List["PortOverrideTypeDef"],
    },
    total=False,
)

class UpdateEndpointGroupRequestRequestTypeDef(
    _RequiredUpdateEndpointGroupRequestRequestTypeDef,
    _OptionalUpdateEndpointGroupRequestRequestTypeDef,
):
    pass

UpdateEndpointGroupResponseTypeDef = TypedDict(
    "UpdateEndpointGroupResponseTypeDef",
    {
        "EndpointGroup": "EndpointGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateListenerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateListenerRequestRequestTypeDef",
    {
        "ListenerArn": str,
    },
)
_OptionalUpdateListenerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateListenerRequestRequestTypeDef",
    {
        "PortRanges": List["PortRangeTypeDef"],
        "Protocol": ProtocolType,
        "ClientAffinity": ClientAffinityType,
    },
    total=False,
)

class UpdateListenerRequestRequestTypeDef(
    _RequiredUpdateListenerRequestRequestTypeDef, _OptionalUpdateListenerRequestRequestTypeDef
):
    pass

UpdateListenerResponseTypeDef = TypedDict(
    "UpdateListenerResponseTypeDef",
    {
        "Listener": "ListenerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WithdrawByoipCidrRequestRequestTypeDef = TypedDict(
    "WithdrawByoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
    },
)

WithdrawByoipCidrResponseTypeDef = TypedDict(
    "WithdrawByoipCidrResponseTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
