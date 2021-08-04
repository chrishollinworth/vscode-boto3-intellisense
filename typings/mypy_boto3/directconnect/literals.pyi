"""
Type annotations for directconnect service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/literals.html)

Usage::

    ```python
    from mypy_boto3_directconnect.literals import AddressFamilyType

    data: AddressFamilyType = "ipv4"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AddressFamilyType",
    "BGPPeerStateType",
    "BGPStatusType",
    "ConnectionStateType",
    "DescribeDirectConnectGatewayAssociationsPaginatorName",
    "DescribeDirectConnectGatewayAttachmentsPaginatorName",
    "DescribeDirectConnectGatewaysPaginatorName",
    "DirectConnectGatewayAssociationProposalStateType",
    "DirectConnectGatewayAssociationStateType",
    "DirectConnectGatewayAttachmentStateType",
    "DirectConnectGatewayAttachmentTypeType",
    "DirectConnectGatewayStateType",
    "GatewayTypeType",
    "HasLogicalRedundancyType",
    "InterconnectStateType",
    "LagStateType",
    "LoaContentTypeType",
    "VirtualInterfaceStateType",
)

AddressFamilyType = Literal["ipv4", "ipv6"]
BGPPeerStateType = Literal["available", "deleted", "deleting", "pending", "verifying"]
BGPStatusType = Literal["down", "unknown", "up"]
ConnectionStateType = Literal[
    "available",
    "deleted",
    "deleting",
    "down",
    "ordering",
    "pending",
    "rejected",
    "requested",
    "unknown",
]
DescribeDirectConnectGatewayAssociationsPaginatorName = Literal[
    "describe_direct_connect_gateway_associations"
]
DescribeDirectConnectGatewayAttachmentsPaginatorName = Literal[
    "describe_direct_connect_gateway_attachments"
]
DescribeDirectConnectGatewaysPaginatorName = Literal["describe_direct_connect_gateways"]
DirectConnectGatewayAssociationProposalStateType = Literal["accepted", "deleted", "requested"]
DirectConnectGatewayAssociationStateType = Literal[
    "associated", "associating", "disassociated", "disassociating", "updating"
]
DirectConnectGatewayAttachmentStateType = Literal["attached", "attaching", "detached", "detaching"]
DirectConnectGatewayAttachmentTypeType = Literal[
    "PrivateVirtualInterface", "TransitVirtualInterface"
]
DirectConnectGatewayStateType = Literal["available", "deleted", "deleting", "pending"]
GatewayTypeType = Literal["transitGateway", "virtualPrivateGateway"]
HasLogicalRedundancyType = Literal["no", "unknown", "yes"]
InterconnectStateType = Literal[
    "available", "deleted", "deleting", "down", "pending", "requested", "unknown"
]
LagStateType = Literal[
    "available", "deleted", "deleting", "down", "pending", "requested", "unknown"
]
LoaContentTypeType = Literal["application/pdf"]
VirtualInterfaceStateType = Literal[
    "available",
    "confirming",
    "deleted",
    "deleting",
    "down",
    "pending",
    "rejected",
    "unknown",
    "verifying",
]
