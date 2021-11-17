"""
Type annotations for networkmanager service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/literals.html)

Usage::

    ```python
    from mypy_boto3_networkmanager.literals import ConnectionStateType

    data: ConnectionStateType = "AVAILABLE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ConnectionStateType",
    "ConnectionStatusType",
    "ConnectionTypeType",
    "CustomerGatewayAssociationStateType",
    "DescribeGlobalNetworksPaginatorName",
    "DeviceStateType",
    "GetConnectionsPaginatorName",
    "GetCustomerGatewayAssociationsPaginatorName",
    "GetDevicesPaginatorName",
    "GetLinkAssociationsPaginatorName",
    "GetLinksPaginatorName",
    "GetNetworkResourceCountsPaginatorName",
    "GetNetworkResourceRelationshipsPaginatorName",
    "GetNetworkResourcesPaginatorName",
    "GetNetworkTelemetryPaginatorName",
    "GetSitesPaginatorName",
    "GetTransitGatewayConnectPeerAssociationsPaginatorName",
    "GetTransitGatewayRegistrationsPaginatorName",
    "GlobalNetworkStateType",
    "LinkAssociationStateType",
    "LinkStateType",
    "RouteAnalysisCompletionReasonCodeType",
    "RouteAnalysisCompletionResultCodeType",
    "RouteAnalysisStatusType",
    "RouteStateType",
    "RouteTableTypeType",
    "RouteTypeType",
    "SiteStateType",
    "TransitGatewayConnectPeerAssociationStateType",
    "TransitGatewayRegistrationStateType",
)

ConnectionStateType = Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]
ConnectionStatusType = Literal["DOWN", "UP"]
ConnectionTypeType = Literal["BGP", "IPSEC"]
CustomerGatewayAssociationStateType = Literal["AVAILABLE", "DELETED", "DELETING", "PENDING"]
DescribeGlobalNetworksPaginatorName = Literal["describe_global_networks"]
DeviceStateType = Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]
GetConnectionsPaginatorName = Literal["get_connections"]
GetCustomerGatewayAssociationsPaginatorName = Literal["get_customer_gateway_associations"]
GetDevicesPaginatorName = Literal["get_devices"]
GetLinkAssociationsPaginatorName = Literal["get_link_associations"]
GetLinksPaginatorName = Literal["get_links"]
GetNetworkResourceCountsPaginatorName = Literal["get_network_resource_counts"]
GetNetworkResourceRelationshipsPaginatorName = Literal["get_network_resource_relationships"]
GetNetworkResourcesPaginatorName = Literal["get_network_resources"]
GetNetworkTelemetryPaginatorName = Literal["get_network_telemetry"]
GetSitesPaginatorName = Literal["get_sites"]
GetTransitGatewayConnectPeerAssociationsPaginatorName = Literal[
    "get_transit_gateway_connect_peer_associations"
]
GetTransitGatewayRegistrationsPaginatorName = Literal["get_transit_gateway_registrations"]
GlobalNetworkStateType = Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]
LinkAssociationStateType = Literal["AVAILABLE", "DELETED", "DELETING", "PENDING"]
LinkStateType = Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]
RouteAnalysisCompletionReasonCodeType = Literal[
    "BLACKHOLE_ROUTE_FOR_DESTINATION_FOUND",
    "CYCLIC_PATH_DETECTED",
    "INACTIVE_ROUTE_FOR_DESTINATION_FOUND",
    "MAX_HOPS_EXCEEDED",
    "NO_DESTINATION_ARN_PROVIDED",
    "POSSIBLE_MIDDLEBOX",
    "ROUTE_NOT_FOUND",
    "TRANSIT_GATEWAY_ATTACHMENT_ATTACH_ARN_NO_MATCH",
    "TRANSIT_GATEWAY_ATTACHMENT_NOT_FOUND",
    "TRANSIT_GATEWAY_ATTACHMENT_NOT_IN_TRANSIT_GATEWAY",
    "TRANSIT_GATEWAY_ATTACHMENT_STABLE_ROUTE_TABLE_NOT_FOUND",
]
RouteAnalysisCompletionResultCodeType = Literal["CONNECTED", "NOT_CONNECTED"]
RouteAnalysisStatusType = Literal["COMPLETED", "FAILED", "RUNNING"]
RouteStateType = Literal["ACTIVE", "BLACKHOLE"]
RouteTableTypeType = Literal["TRANSIT_GATEWAY_ROUTE_TABLE"]
RouteTypeType = Literal["PROPAGATED", "STATIC"]
SiteStateType = Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]
TransitGatewayConnectPeerAssociationStateType = Literal[
    "AVAILABLE", "DELETED", "DELETING", "PENDING"
]
TransitGatewayRegistrationStateType = Literal[
    "AVAILABLE", "DELETED", "DELETING", "FAILED", "PENDING"
]
