"""
Type annotations for globalaccelerator service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/literals.html)

Usage::

    ```python
    from mypy_boto3_globalaccelerator.literals import AcceleratorStatusType

    data: AcceleratorStatusType = "DEPLOYED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AcceleratorStatusType",
    "ByoipCidrStateType",
    "ClientAffinityType",
    "CustomRoutingAcceleratorStatusType",
    "CustomRoutingDestinationTrafficStateType",
    "CustomRoutingProtocolType",
    "HealthCheckProtocolType",
    "HealthStateType",
    "IpAddressTypeType",
    "ListAcceleratorsPaginatorName",
    "ListByoipCidrsPaginatorName",
    "ListCustomRoutingAcceleratorsPaginatorName",
    "ListCustomRoutingListenersPaginatorName",
    "ListCustomRoutingPortMappingsByDestinationPaginatorName",
    "ListCustomRoutingPortMappingsPaginatorName",
    "ListEndpointGroupsPaginatorName",
    "ListListenersPaginatorName",
    "ProtocolType",
)

AcceleratorStatusType = Literal["DEPLOYED", "IN_PROGRESS"]
ByoipCidrStateType = Literal[
    "ADVERTISING",
    "DEPROVISIONED",
    "FAILED_ADVERTISING",
    "FAILED_DEPROVISION",
    "FAILED_PROVISION",
    "FAILED_WITHDRAW",
    "PENDING_ADVERTISING",
    "PENDING_DEPROVISIONING",
    "PENDING_PROVISIONING",
    "PENDING_WITHDRAWING",
    "READY",
]
ClientAffinityType = Literal["NONE", "SOURCE_IP"]
CustomRoutingAcceleratorStatusType = Literal["DEPLOYED", "IN_PROGRESS"]
CustomRoutingDestinationTrafficStateType = Literal["ALLOW", "DENY"]
CustomRoutingProtocolType = Literal["TCP", "UDP"]
HealthCheckProtocolType = Literal["HTTP", "HTTPS", "TCP"]
HealthStateType = Literal["HEALTHY", "INITIAL", "UNHEALTHY"]
IpAddressTypeType = Literal["IPV4"]
ListAcceleratorsPaginatorName = Literal["list_accelerators"]
ListByoipCidrsPaginatorName = Literal["list_byoip_cidrs"]
ListCustomRoutingAcceleratorsPaginatorName = Literal["list_custom_routing_accelerators"]
ListCustomRoutingListenersPaginatorName = Literal["list_custom_routing_listeners"]
ListCustomRoutingPortMappingsByDestinationPaginatorName = Literal[
    "list_custom_routing_port_mappings_by_destination"
]
ListCustomRoutingPortMappingsPaginatorName = Literal["list_custom_routing_port_mappings"]
ListEndpointGroupsPaginatorName = Literal["list_endpoint_groups"]
ListListenersPaginatorName = Literal["list_listeners"]
ProtocolType = Literal["TCP", "UDP"]
