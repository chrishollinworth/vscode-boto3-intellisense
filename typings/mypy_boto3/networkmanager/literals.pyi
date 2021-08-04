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
    "CustomerGatewayAssociationStateType",
    "DescribeGlobalNetworksPaginatorName",
    "DeviceStateType",
    "GetConnectionsPaginatorName",
    "GetCustomerGatewayAssociationsPaginatorName",
    "GetDevicesPaginatorName",
    "GetLinkAssociationsPaginatorName",
    "GetLinksPaginatorName",
    "GetSitesPaginatorName",
    "GetTransitGatewayConnectPeerAssociationsPaginatorName",
    "GetTransitGatewayRegistrationsPaginatorName",
    "GlobalNetworkStateType",
    "LinkAssociationStateType",
    "LinkStateType",
    "SiteStateType",
    "TransitGatewayConnectPeerAssociationStateType",
    "TransitGatewayRegistrationStateType",
)

ConnectionStateType = Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]
CustomerGatewayAssociationStateType = Literal["AVAILABLE", "DELETED", "DELETING", "PENDING"]
DescribeGlobalNetworksPaginatorName = Literal["describe_global_networks"]
DeviceStateType = Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]
GetConnectionsPaginatorName = Literal["get_connections"]
GetCustomerGatewayAssociationsPaginatorName = Literal["get_customer_gateway_associations"]
GetDevicesPaginatorName = Literal["get_devices"]
GetLinkAssociationsPaginatorName = Literal["get_link_associations"]
GetLinksPaginatorName = Literal["get_links"]
GetSitesPaginatorName = Literal["get_sites"]
GetTransitGatewayConnectPeerAssociationsPaginatorName = Literal[
    "get_transit_gateway_connect_peer_associations"
]
GetTransitGatewayRegistrationsPaginatorName = Literal["get_transit_gateway_registrations"]
GlobalNetworkStateType = Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]
LinkAssociationStateType = Literal["AVAILABLE", "DELETED", "DELETING", "PENDING"]
LinkStateType = Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]
SiteStateType = Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]
TransitGatewayConnectPeerAssociationStateType = Literal[
    "AVAILABLE", "DELETED", "DELETING", "PENDING"
]
TransitGatewayRegistrationStateType = Literal[
    "AVAILABLE", "DELETED", "DELETING", "FAILED", "PENDING"
]
