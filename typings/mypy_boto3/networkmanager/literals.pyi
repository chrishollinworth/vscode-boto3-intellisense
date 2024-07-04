"""
Type annotations for networkmanager service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/literals.html)

Usage::

    ```python
    from mypy_boto3_networkmanager.literals import AttachmentErrorCodeType

    data: AttachmentErrorCodeType = "MAXIMUM_NO_ENCAP_LIMIT_EXCEEDED"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AttachmentErrorCodeType",
    "AttachmentStateType",
    "AttachmentTypeType",
    "ChangeActionType",
    "ChangeSetStateType",
    "ChangeStatusType",
    "ChangeTypeType",
    "ConnectPeerAssociationStateType",
    "ConnectPeerErrorCodeType",
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
    "GetCoreNetworkChangeEventsPaginatorName",
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
    "ListPeeringsPaginatorName",
    "PeeringErrorCodeType",
    "PeeringStateType",
    "PeeringTypeType",
    "RouteAnalysisCompletionReasonCodeType",
    "RouteAnalysisCompletionResultCodeType",
    "RouteAnalysisStatusType",
    "RouteStateType",
    "RouteTableTypeType",
    "RouteTypeType",
    "SegmentActionServiceInsertionType",
    "SendViaModeType",
    "SiteStateType",
    "TransitGatewayConnectPeerAssociationStateType",
    "TransitGatewayRegistrationStateType",
    "TunnelProtocolType",
)

AttachmentErrorCodeType = Literal[
    "MAXIMUM_NO_ENCAP_LIMIT_EXCEEDED",
    "SUBNET_DUPLICATED_IN_AVAILABILITY_ZONE",
    "SUBNET_NOT_FOUND",
    "SUBNET_NO_FREE_ADDRESSES",
    "SUBNET_NO_IPV6_CIDRS",
    "SUBNET_UNSUPPORTED_AVAILABILITY_ZONE",
    "VPC_NOT_FOUND",
    "VPN_CONNECTION_NOT_FOUND",
]
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
AttachmentTypeType = Literal["CONNECT", "SITE_TO_SITE_VPN", "TRANSIT_GATEWAY_ROUTE_TABLE", "VPC"]
ChangeActionType = Literal["ADD", "MODIFY", "REMOVE"]
ChangeSetStateType = Literal[
    "EXECUTING",
    "EXECUTION_SUCCEEDED",
    "FAILED_GENERATION",
    "OUT_OF_DATE",
    "PENDING_GENERATION",
    "READY_TO_EXECUTE",
]
ChangeStatusType = Literal["COMPLETE", "FAILED", "IN_PROGRESS", "NOT_STARTED"]
ChangeTypeType = Literal[
    "ATTACHMENT_MAPPING",
    "ATTACHMENT_POLICIES_CONFIGURATION",
    "ATTACHMENT_ROUTE_PROPAGATION",
    "ATTACHMENT_ROUTE_STATIC",
    "CORE_NETWORK_CONFIGURATION",
    "CORE_NETWORK_EDGE",
    "CORE_NETWORK_SEGMENT",
    "NETWORK_FUNCTION_GROUP",
    "SEGMENTS_CONFIGURATION",
    "SEGMENT_ACTIONS_CONFIGURATION",
]
ConnectPeerAssociationStateType = Literal["AVAILABLE", "DELETED", "DELETING", "PENDING"]
ConnectPeerErrorCodeType = Literal[
    "EDGE_LOCATION_NO_FREE_IPS",
    "EDGE_LOCATION_PEER_DUPLICATE",
    "INVALID_INSIDE_CIDR_BLOCK",
    "IP_OUTSIDE_SUBNET_CIDR_RANGE",
    "NO_ASSOCIATED_CIDR_BLOCK",
    "SUBNET_NOT_FOUND",
]
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
GetCoreNetworkChangeEventsPaginatorName = Literal["get_core_network_change_events"]
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
ListPeeringsPaginatorName = Literal["list_peerings"]
PeeringErrorCodeType = Literal[
    "EDGE_LOCATION_PEER_DUPLICATE",
    "INTERNAL_ERROR",
    "INVALID_TRANSIT_GATEWAY_STATE",
    "MISSING_PERMISSIONS",
    "TRANSIT_GATEWAY_NOT_FOUND",
    "TRANSIT_GATEWAY_PEERS_LIMIT_EXCEEDED",
]
PeeringStateType = Literal["AVAILABLE", "CREATING", "DELETING", "FAILED"]
PeeringTypeType = Literal["TRANSIT_GATEWAY"]
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
RouteTableTypeType = Literal[
    "CORE_NETWORK_SEGMENT", "NETWORK_FUNCTION_GROUP", "TRANSIT_GATEWAY_ROUTE_TABLE"
]
RouteTypeType = Literal["PROPAGATED", "STATIC"]
SegmentActionServiceInsertionType = Literal["send-to", "send-via"]
SendViaModeType = Literal["dual-hop", "single-hop"]
SiteStateType = Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]
TransitGatewayConnectPeerAssociationStateType = Literal[
    "AVAILABLE", "DELETED", "DELETING", "PENDING"
]
TransitGatewayRegistrationStateType = Literal[
    "AVAILABLE", "DELETED", "DELETING", "FAILED", "PENDING"
]
TunnelProtocolType = Literal["GRE", "NO_ENCAP"]
