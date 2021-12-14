"""
Type annotations for networkmanager service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/literals.html)

Usage::

    ```python
    from mypy_boto3_networkmanager.literals import AttachmentStateType

    data: AttachmentStateType = "AVAILABLE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AttachmentStateType",
    "AttachmentTypeType",
    "ChangeActionType",
    "ChangeSetStateType",
    "ChangeTypeType",
    "ConnectPeerAssociationStateType",
    "ConnectPeerStateType",
    "ConnectionStateType",
    "ConnectionStatusType",
    "ConnectionTypeType",
    "CoreNetworkPolicyAliasType",
    "CoreNetworkStateType",
    "CustomerGatewayAssociationStateType",
    "DescribeGlobalNetworksPaginatorName",
    "DeviceStateType",
    "GetConnectPeerAssociationsPaginatorName",
    "GetConnectionsPaginatorName",
    "GetCoreNetworkChangeSetPaginatorName",
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
    "ListAttachmentsPaginatorName",
    "ListConnectPeersPaginatorName",
    "ListCoreNetworkPolicyVersionsPaginatorName",
    "ListCoreNetworksPaginatorName",
    "RouteAnalysisCompletionReasonCodeType",
    "RouteAnalysisCompletionResultCodeType",
    "RouteAnalysisStatusType",
    "RouteStateType",
    "RouteTableTypeType",
    "RouteTypeType",
    "SiteStateType",
    "TransitGatewayConnectPeerAssociationStateType",
    "TransitGatewayRegistrationStateType",
    "TunnelProtocolType",
)

AttachmentStateType = Literal[
    "AVAILABLE",
    "CREATING",
    "DELETING",
    "FAILED",
    "PENDING_ATTACHMENT_ACCEPTANCE",
    "PENDING_NETWORK_UPDATE",
    "PENDING_TAG_ACCEPTANCE",
    "REJECTED",
    "UPDATING",
]
AttachmentTypeType = Literal["CONNECT", "SITE_TO_SITE_VPN", "VPC"]
ChangeActionType = Literal["ADD", "MODIFY", "REMOVE"]
ChangeSetStateType = Literal[
    "EXECUTING",
    "EXECUTION_SUCCEEDED",
    "FAILED_GENERATION",
    "OUT_OF_DATE",
    "PENDING_GENERATION",
    "READY_TO_EXECUTE",
]
ChangeTypeType = Literal[
    "ATTACHMENT_MAPPING",
    "ATTACHMENT_ROUTE_PROPAGATION",
    "ATTACHMENT_ROUTE_STATIC",
    "CORE_NETWORK_EDGE",
    "CORE_NETWORK_SEGMENT",
]
ConnectPeerAssociationStateType = Literal["AVAILABLE", "DELETED", "DELETING", "PENDING"]
ConnectPeerStateType = Literal["AVAILABLE", "CREATING", "DELETING", "FAILED"]
ConnectionStateType = Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]
ConnectionStatusType = Literal["DOWN", "UP"]
ConnectionTypeType = Literal["BGP", "IPSEC"]
CoreNetworkPolicyAliasType = Literal["LATEST", "LIVE"]
CoreNetworkStateType = Literal["AVAILABLE", "CREATING", "DELETING", "UPDATING"]
CustomerGatewayAssociationStateType = Literal["AVAILABLE", "DELETED", "DELETING", "PENDING"]
DescribeGlobalNetworksPaginatorName = Literal["describe_global_networks"]
DeviceStateType = Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]
GetConnectPeerAssociationsPaginatorName = Literal["get_connect_peer_associations"]
GetConnectionsPaginatorName = Literal["get_connections"]
GetCoreNetworkChangeSetPaginatorName = Literal["get_core_network_change_set"]
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
ListAttachmentsPaginatorName = Literal["list_attachments"]
ListConnectPeersPaginatorName = Literal["list_connect_peers"]
ListCoreNetworkPolicyVersionsPaginatorName = Literal["list_core_network_policy_versions"]
ListCoreNetworksPaginatorName = Literal["list_core_networks"]
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
RouteTableTypeType = Literal["CORE_NETWORK_SEGMENT", "TRANSIT_GATEWAY_ROUTE_TABLE"]
RouteTypeType = Literal["PROPAGATED", "STATIC"]
SiteStateType = Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]
TransitGatewayConnectPeerAssociationStateType = Literal[
    "AVAILABLE", "DELETED", "DELETING", "PENDING"
]
TransitGatewayRegistrationStateType = Literal[
    "AVAILABLE", "DELETED", "DELETING", "FAILED", "PENDING"
]
TunnelProtocolType = Literal["GRE"]
