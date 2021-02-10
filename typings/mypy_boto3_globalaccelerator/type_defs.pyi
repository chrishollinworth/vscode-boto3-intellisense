"""
Main interface for globalaccelerator service type definitions.

Usage::

    ```python
    from mypy_boto3_globalaccelerator.type_defs import AcceleratorAttributesTypeDef

    data: AcceleratorAttributesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

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
    "ByoipCidrEventTypeDef",
    "ByoipCidrTypeDef",
    "CustomRoutingAcceleratorAttributesTypeDef",
    "CustomRoutingAcceleratorTypeDef",
    "CustomRoutingDestinationDescriptionTypeDef",
    "CustomRoutingEndpointDescriptionTypeDef",
    "CustomRoutingEndpointGroupTypeDef",
    "CustomRoutingListenerTypeDef",
    "DestinationPortMappingTypeDef",
    "EndpointDescriptionTypeDef",
    "EndpointGroupTypeDef",
    "IpSetTypeDef",
    "ListenerTypeDef",
    "PortMappingTypeDef",
    "PortOverrideTypeDef",
    "PortRangeTypeDef",
    "SocketAddressTypeDef",
    "TagTypeDef",
    "AddCustomRoutingEndpointsResponseTypeDef",
    "AdvertiseByoipCidrResponseTypeDef",
    "CidrAuthorizationContextTypeDef",
    "CreateAcceleratorResponseTypeDef",
    "CreateCustomRoutingAcceleratorResponseTypeDef",
    "CreateCustomRoutingEndpointGroupResponseTypeDef",
    "CreateCustomRoutingListenerResponseTypeDef",
    "CreateEndpointGroupResponseTypeDef",
    "CreateListenerResponseTypeDef",
    "CustomRoutingDestinationConfigurationTypeDef",
    "CustomRoutingEndpointConfigurationTypeDef",
    "DeprovisionByoipCidrResponseTypeDef",
    "DescribeAcceleratorAttributesResponseTypeDef",
    "DescribeAcceleratorResponseTypeDef",
    "DescribeCustomRoutingAcceleratorAttributesResponseTypeDef",
    "DescribeCustomRoutingAcceleratorResponseTypeDef",
    "DescribeCustomRoutingEndpointGroupResponseTypeDef",
    "DescribeCustomRoutingListenerResponseTypeDef",
    "DescribeEndpointGroupResponseTypeDef",
    "DescribeListenerResponseTypeDef",
    "EndpointConfigurationTypeDef",
    "ListAcceleratorsResponseTypeDef",
    "ListByoipCidrsResponseTypeDef",
    "ListCustomRoutingAcceleratorsResponseTypeDef",
    "ListCustomRoutingEndpointGroupsResponseTypeDef",
    "ListCustomRoutingListenersResponseTypeDef",
    "ListCustomRoutingPortMappingsByDestinationResponseTypeDef",
    "ListCustomRoutingPortMappingsResponseTypeDef",
    "ListEndpointGroupsResponseTypeDef",
    "ListListenersResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ProvisionByoipCidrResponseTypeDef",
    "UpdateAcceleratorAttributesResponseTypeDef",
    "UpdateAcceleratorResponseTypeDef",
    "UpdateCustomRoutingAcceleratorAttributesResponseTypeDef",
    "UpdateCustomRoutingAcceleratorResponseTypeDef",
    "UpdateCustomRoutingListenerResponseTypeDef",
    "UpdateEndpointGroupResponseTypeDef",
    "UpdateListenerResponseTypeDef",
    "WithdrawByoipCidrResponseTypeDef",
)

AcceleratorAttributesTypeDef = TypedDict(
    "AcceleratorAttributesTypeDef",
    {"FlowLogsEnabled": bool, "FlowLogsS3Bucket": str, "FlowLogsS3Prefix": str},
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
        "Status": Literal["DEPLOYED", "IN_PROGRESS"],
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ByoipCidrEventTypeDef = TypedDict(
    "ByoipCidrEventTypeDef", {"Message": str, "Timestamp": datetime}, total=False
)

ByoipCidrTypeDef = TypedDict(
    "ByoipCidrTypeDef",
    {
        "Cidr": str,
        "State": Literal[
            "PENDING_PROVISIONING",
            "READY",
            "PENDING_ADVERTISING",
            "ADVERTISING",
            "PENDING_WITHDRAWING",
            "PENDING_DEPROVISIONING",
            "DEPROVISIONED",
            "FAILED_PROVISION",
            "FAILED_ADVERTISING",
            "FAILED_WITHDRAW",
            "FAILED_DEPROVISION",
        ],
        "Events": List["ByoipCidrEventTypeDef"],
    },
    total=False,
)

CustomRoutingAcceleratorAttributesTypeDef = TypedDict(
    "CustomRoutingAcceleratorAttributesTypeDef",
    {"FlowLogsEnabled": bool, "FlowLogsS3Bucket": str, "FlowLogsS3Prefix": str},
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
        "Status": Literal["DEPLOYED", "IN_PROGRESS"],
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

CustomRoutingDestinationDescriptionTypeDef = TypedDict(
    "CustomRoutingDestinationDescriptionTypeDef",
    {"FromPort": int, "ToPort": int, "Protocols": List[Literal["TCP", "UDP"]]},
    total=False,
)

CustomRoutingEndpointDescriptionTypeDef = TypedDict(
    "CustomRoutingEndpointDescriptionTypeDef", {"EndpointId": str}, total=False
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
    {"ListenerArn": str, "PortRanges": List["PortRangeTypeDef"]},
    total=False,
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
        "DestinationTrafficState": Literal["ALLOW", "DENY"],
    },
    total=False,
)

EndpointDescriptionTypeDef = TypedDict(
    "EndpointDescriptionTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "HealthState": Literal["INITIAL", "HEALTHY", "UNHEALTHY"],
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
        "HealthCheckProtocol": Literal["TCP", "HTTP", "HTTPS"],
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
        "PortOverrides": List["PortOverrideTypeDef"],
    },
    total=False,
)

IpSetTypeDef = TypedDict("IpSetTypeDef", {"IpFamily": str, "IpAddresses": List[str]}, total=False)

ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List["PortRangeTypeDef"],
        "Protocol": Literal["TCP", "UDP"],
        "ClientAffinity": Literal["NONE", "SOURCE_IP"],
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
        "Protocols": List[Literal["TCP", "UDP"]],
        "DestinationTrafficState": Literal["ALLOW", "DENY"],
    },
    total=False,
)

PortOverrideTypeDef = TypedDict(
    "PortOverrideTypeDef", {"ListenerPort": int, "EndpointPort": int}, total=False
)

PortRangeTypeDef = TypedDict("PortRangeTypeDef", {"FromPort": int, "ToPort": int}, total=False)

SocketAddressTypeDef = TypedDict(
    "SocketAddressTypeDef", {"IpAddress": str, "Port": int}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

AddCustomRoutingEndpointsResponseTypeDef = TypedDict(
    "AddCustomRoutingEndpointsResponseTypeDef",
    {
        "EndpointDescriptions": List["CustomRoutingEndpointDescriptionTypeDef"],
        "EndpointGroupArn": str,
    },
    total=False,
)

AdvertiseByoipCidrResponseTypeDef = TypedDict(
    "AdvertiseByoipCidrResponseTypeDef", {"ByoipCidr": "ByoipCidrTypeDef"}, total=False
)

CidrAuthorizationContextTypeDef = TypedDict(
    "CidrAuthorizationContextTypeDef", {"Message": str, "Signature": str}
)

CreateAcceleratorResponseTypeDef = TypedDict(
    "CreateAcceleratorResponseTypeDef", {"Accelerator": "AcceleratorTypeDef"}, total=False
)

CreateCustomRoutingAcceleratorResponseTypeDef = TypedDict(
    "CreateCustomRoutingAcceleratorResponseTypeDef",
    {"Accelerator": "CustomRoutingAcceleratorTypeDef"},
    total=False,
)

CreateCustomRoutingEndpointGroupResponseTypeDef = TypedDict(
    "CreateCustomRoutingEndpointGroupResponseTypeDef",
    {"EndpointGroup": "CustomRoutingEndpointGroupTypeDef"},
    total=False,
)

CreateCustomRoutingListenerResponseTypeDef = TypedDict(
    "CreateCustomRoutingListenerResponseTypeDef",
    {"Listener": "CustomRoutingListenerTypeDef"},
    total=False,
)

CreateEndpointGroupResponseTypeDef = TypedDict(
    "CreateEndpointGroupResponseTypeDef", {"EndpointGroup": "EndpointGroupTypeDef"}, total=False
)

CreateListenerResponseTypeDef = TypedDict(
    "CreateListenerResponseTypeDef", {"Listener": "ListenerTypeDef"}, total=False
)

CustomRoutingDestinationConfigurationTypeDef = TypedDict(
    "CustomRoutingDestinationConfigurationTypeDef",
    {"FromPort": int, "ToPort": int, "Protocols": List[Literal["TCP", "UDP"]]},
)

CustomRoutingEndpointConfigurationTypeDef = TypedDict(
    "CustomRoutingEndpointConfigurationTypeDef", {"EndpointId": str}, total=False
)

DeprovisionByoipCidrResponseTypeDef = TypedDict(
    "DeprovisionByoipCidrResponseTypeDef", {"ByoipCidr": "ByoipCidrTypeDef"}, total=False
)

DescribeAcceleratorAttributesResponseTypeDef = TypedDict(
    "DescribeAcceleratorAttributesResponseTypeDef",
    {"AcceleratorAttributes": "AcceleratorAttributesTypeDef"},
    total=False,
)

DescribeAcceleratorResponseTypeDef = TypedDict(
    "DescribeAcceleratorResponseTypeDef", {"Accelerator": "AcceleratorTypeDef"}, total=False
)

DescribeCustomRoutingAcceleratorAttributesResponseTypeDef = TypedDict(
    "DescribeCustomRoutingAcceleratorAttributesResponseTypeDef",
    {"AcceleratorAttributes": "CustomRoutingAcceleratorAttributesTypeDef"},
    total=False,
)

DescribeCustomRoutingAcceleratorResponseTypeDef = TypedDict(
    "DescribeCustomRoutingAcceleratorResponseTypeDef",
    {"Accelerator": "CustomRoutingAcceleratorTypeDef"},
    total=False,
)

DescribeCustomRoutingEndpointGroupResponseTypeDef = TypedDict(
    "DescribeCustomRoutingEndpointGroupResponseTypeDef",
    {"EndpointGroup": "CustomRoutingEndpointGroupTypeDef"},
    total=False,
)

DescribeCustomRoutingListenerResponseTypeDef = TypedDict(
    "DescribeCustomRoutingListenerResponseTypeDef",
    {"Listener": "CustomRoutingListenerTypeDef"},
    total=False,
)

DescribeEndpointGroupResponseTypeDef = TypedDict(
    "DescribeEndpointGroupResponseTypeDef", {"EndpointGroup": "EndpointGroupTypeDef"}, total=False
)

DescribeListenerResponseTypeDef = TypedDict(
    "DescribeListenerResponseTypeDef", {"Listener": "ListenerTypeDef"}, total=False
)

EndpointConfigurationTypeDef = TypedDict(
    "EndpointConfigurationTypeDef",
    {"EndpointId": str, "Weight": int, "ClientIPPreservationEnabled": bool},
    total=False,
)

ListAcceleratorsResponseTypeDef = TypedDict(
    "ListAcceleratorsResponseTypeDef",
    {"Accelerators": List["AcceleratorTypeDef"], "NextToken": str},
    total=False,
)

ListByoipCidrsResponseTypeDef = TypedDict(
    "ListByoipCidrsResponseTypeDef",
    {"ByoipCidrs": List["ByoipCidrTypeDef"], "NextToken": str},
    total=False,
)

ListCustomRoutingAcceleratorsResponseTypeDef = TypedDict(
    "ListCustomRoutingAcceleratorsResponseTypeDef",
    {"Accelerators": List["CustomRoutingAcceleratorTypeDef"], "NextToken": str},
    total=False,
)

ListCustomRoutingEndpointGroupsResponseTypeDef = TypedDict(
    "ListCustomRoutingEndpointGroupsResponseTypeDef",
    {"EndpointGroups": List["CustomRoutingEndpointGroupTypeDef"], "NextToken": str},
    total=False,
)

ListCustomRoutingListenersResponseTypeDef = TypedDict(
    "ListCustomRoutingListenersResponseTypeDef",
    {"Listeners": List["CustomRoutingListenerTypeDef"], "NextToken": str},
    total=False,
)

ListCustomRoutingPortMappingsByDestinationResponseTypeDef = TypedDict(
    "ListCustomRoutingPortMappingsByDestinationResponseTypeDef",
    {"DestinationPortMappings": List["DestinationPortMappingTypeDef"], "NextToken": str},
    total=False,
)

ListCustomRoutingPortMappingsResponseTypeDef = TypedDict(
    "ListCustomRoutingPortMappingsResponseTypeDef",
    {"PortMappings": List["PortMappingTypeDef"], "NextToken": str},
    total=False,
)

ListEndpointGroupsResponseTypeDef = TypedDict(
    "ListEndpointGroupsResponseTypeDef",
    {"EndpointGroups": List["EndpointGroupTypeDef"], "NextToken": str},
    total=False,
)

ListListenersResponseTypeDef = TypedDict(
    "ListListenersResponseTypeDef",
    {"Listeners": List["ListenerTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

ProvisionByoipCidrResponseTypeDef = TypedDict(
    "ProvisionByoipCidrResponseTypeDef", {"ByoipCidr": "ByoipCidrTypeDef"}, total=False
)

UpdateAcceleratorAttributesResponseTypeDef = TypedDict(
    "UpdateAcceleratorAttributesResponseTypeDef",
    {"AcceleratorAttributes": "AcceleratorAttributesTypeDef"},
    total=False,
)

UpdateAcceleratorResponseTypeDef = TypedDict(
    "UpdateAcceleratorResponseTypeDef", {"Accelerator": "AcceleratorTypeDef"}, total=False
)

UpdateCustomRoutingAcceleratorAttributesResponseTypeDef = TypedDict(
    "UpdateCustomRoutingAcceleratorAttributesResponseTypeDef",
    {"AcceleratorAttributes": "CustomRoutingAcceleratorAttributesTypeDef"},
    total=False,
)

UpdateCustomRoutingAcceleratorResponseTypeDef = TypedDict(
    "UpdateCustomRoutingAcceleratorResponseTypeDef",
    {"Accelerator": "CustomRoutingAcceleratorTypeDef"},
    total=False,
)

UpdateCustomRoutingListenerResponseTypeDef = TypedDict(
    "UpdateCustomRoutingListenerResponseTypeDef",
    {"Listener": "CustomRoutingListenerTypeDef"},
    total=False,
)

UpdateEndpointGroupResponseTypeDef = TypedDict(
    "UpdateEndpointGroupResponseTypeDef", {"EndpointGroup": "EndpointGroupTypeDef"}, total=False
)

UpdateListenerResponseTypeDef = TypedDict(
    "UpdateListenerResponseTypeDef", {"Listener": "ListenerTypeDef"}, total=False
)

WithdrawByoipCidrResponseTypeDef = TypedDict(
    "WithdrawByoipCidrResponseTypeDef", {"ByoipCidr": "ByoipCidrTypeDef"}, total=False
)
