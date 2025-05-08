"""
Type annotations for networkmanager service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_networkmanager.client import NetworkManagerClient

    session = Session()
    client: NetworkManagerClient = session.client("networkmanager")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeGlobalNetworksPaginator,
    GetConnectionsPaginator,
    GetConnectPeerAssociationsPaginator,
    GetCoreNetworkChangeEventsPaginator,
    GetCoreNetworkChangeSetPaginator,
    GetCustomerGatewayAssociationsPaginator,
    GetDevicesPaginator,
    GetLinkAssociationsPaginator,
    GetLinksPaginator,
    GetNetworkResourceCountsPaginator,
    GetNetworkResourceRelationshipsPaginator,
    GetNetworkResourcesPaginator,
    GetNetworkTelemetryPaginator,
    GetSitesPaginator,
    GetTransitGatewayConnectPeerAssociationsPaginator,
    GetTransitGatewayRegistrationsPaginator,
    ListAttachmentsPaginator,
    ListConnectPeersPaginator,
    ListCoreNetworkPolicyVersionsPaginator,
    ListCoreNetworksPaginator,
    ListPeeringsPaginator,
)
from .type_defs import (
    AcceptAttachmentRequestTypeDef,
    AcceptAttachmentResponseTypeDef,
    AssociateConnectPeerRequestTypeDef,
    AssociateConnectPeerResponseTypeDef,
    AssociateCustomerGatewayRequestTypeDef,
    AssociateCustomerGatewayResponseTypeDef,
    AssociateLinkRequestTypeDef,
    AssociateLinkResponseTypeDef,
    AssociateTransitGatewayConnectPeerRequestTypeDef,
    AssociateTransitGatewayConnectPeerResponseTypeDef,
    CreateConnectAttachmentRequestTypeDef,
    CreateConnectAttachmentResponseTypeDef,
    CreateConnectionRequestTypeDef,
    CreateConnectionResponseTypeDef,
    CreateConnectPeerRequestTypeDef,
    CreateConnectPeerResponseTypeDef,
    CreateCoreNetworkRequestTypeDef,
    CreateCoreNetworkResponseTypeDef,
    CreateDeviceRequestTypeDef,
    CreateDeviceResponseTypeDef,
    CreateDirectConnectGatewayAttachmentRequestTypeDef,
    CreateDirectConnectGatewayAttachmentResponseTypeDef,
    CreateGlobalNetworkRequestTypeDef,
    CreateGlobalNetworkResponseTypeDef,
    CreateLinkRequestTypeDef,
    CreateLinkResponseTypeDef,
    CreateSiteRequestTypeDef,
    CreateSiteResponseTypeDef,
    CreateSiteToSiteVpnAttachmentRequestTypeDef,
    CreateSiteToSiteVpnAttachmentResponseTypeDef,
    CreateTransitGatewayPeeringRequestTypeDef,
    CreateTransitGatewayPeeringResponseTypeDef,
    CreateTransitGatewayRouteTableAttachmentRequestTypeDef,
    CreateTransitGatewayRouteTableAttachmentResponseTypeDef,
    CreateVpcAttachmentRequestTypeDef,
    CreateVpcAttachmentResponseTypeDef,
    DeleteAttachmentRequestTypeDef,
    DeleteAttachmentResponseTypeDef,
    DeleteConnectionRequestTypeDef,
    DeleteConnectionResponseTypeDef,
    DeleteConnectPeerRequestTypeDef,
    DeleteConnectPeerResponseTypeDef,
    DeleteCoreNetworkPolicyVersionRequestTypeDef,
    DeleteCoreNetworkPolicyVersionResponseTypeDef,
    DeleteCoreNetworkRequestTypeDef,
    DeleteCoreNetworkResponseTypeDef,
    DeleteDeviceRequestTypeDef,
    DeleteDeviceResponseTypeDef,
    DeleteGlobalNetworkRequestTypeDef,
    DeleteGlobalNetworkResponseTypeDef,
    DeleteLinkRequestTypeDef,
    DeleteLinkResponseTypeDef,
    DeletePeeringRequestTypeDef,
    DeletePeeringResponseTypeDef,
    DeleteResourcePolicyRequestTypeDef,
    DeleteSiteRequestTypeDef,
    DeleteSiteResponseTypeDef,
    DeregisterTransitGatewayRequestTypeDef,
    DeregisterTransitGatewayResponseTypeDef,
    DescribeGlobalNetworksRequestTypeDef,
    DescribeGlobalNetworksResponseTypeDef,
    DisassociateConnectPeerRequestTypeDef,
    DisassociateConnectPeerResponseTypeDef,
    DisassociateCustomerGatewayRequestTypeDef,
    DisassociateCustomerGatewayResponseTypeDef,
    DisassociateLinkRequestTypeDef,
    DisassociateLinkResponseTypeDef,
    DisassociateTransitGatewayConnectPeerRequestTypeDef,
    DisassociateTransitGatewayConnectPeerResponseTypeDef,
    ExecuteCoreNetworkChangeSetRequestTypeDef,
    GetConnectAttachmentRequestTypeDef,
    GetConnectAttachmentResponseTypeDef,
    GetConnectionsRequestTypeDef,
    GetConnectionsResponseTypeDef,
    GetConnectPeerAssociationsRequestTypeDef,
    GetConnectPeerAssociationsResponseTypeDef,
    GetConnectPeerRequestTypeDef,
    GetConnectPeerResponseTypeDef,
    GetCoreNetworkChangeEventsRequestTypeDef,
    GetCoreNetworkChangeEventsResponseTypeDef,
    GetCoreNetworkChangeSetRequestTypeDef,
    GetCoreNetworkChangeSetResponseTypeDef,
    GetCoreNetworkPolicyRequestTypeDef,
    GetCoreNetworkPolicyResponseTypeDef,
    GetCoreNetworkRequestTypeDef,
    GetCoreNetworkResponseTypeDef,
    GetCustomerGatewayAssociationsRequestTypeDef,
    GetCustomerGatewayAssociationsResponseTypeDef,
    GetDevicesRequestTypeDef,
    GetDevicesResponseTypeDef,
    GetDirectConnectGatewayAttachmentRequestTypeDef,
    GetDirectConnectGatewayAttachmentResponseTypeDef,
    GetLinkAssociationsRequestTypeDef,
    GetLinkAssociationsResponseTypeDef,
    GetLinksRequestTypeDef,
    GetLinksResponseTypeDef,
    GetNetworkResourceCountsRequestTypeDef,
    GetNetworkResourceCountsResponseTypeDef,
    GetNetworkResourceRelationshipsRequestTypeDef,
    GetNetworkResourceRelationshipsResponseTypeDef,
    GetNetworkResourcesRequestTypeDef,
    GetNetworkResourcesResponseTypeDef,
    GetNetworkRoutesRequestTypeDef,
    GetNetworkRoutesResponseTypeDef,
    GetNetworkTelemetryRequestTypeDef,
    GetNetworkTelemetryResponseTypeDef,
    GetResourcePolicyRequestTypeDef,
    GetResourcePolicyResponseTypeDef,
    GetRouteAnalysisRequestTypeDef,
    GetRouteAnalysisResponseTypeDef,
    GetSitesRequestTypeDef,
    GetSitesResponseTypeDef,
    GetSiteToSiteVpnAttachmentRequestTypeDef,
    GetSiteToSiteVpnAttachmentResponseTypeDef,
    GetTransitGatewayConnectPeerAssociationsRequestTypeDef,
    GetTransitGatewayConnectPeerAssociationsResponseTypeDef,
    GetTransitGatewayPeeringRequestTypeDef,
    GetTransitGatewayPeeringResponseTypeDef,
    GetTransitGatewayRegistrationsRequestTypeDef,
    GetTransitGatewayRegistrationsResponseTypeDef,
    GetTransitGatewayRouteTableAttachmentRequestTypeDef,
    GetTransitGatewayRouteTableAttachmentResponseTypeDef,
    GetVpcAttachmentRequestTypeDef,
    GetVpcAttachmentResponseTypeDef,
    ListAttachmentsRequestTypeDef,
    ListAttachmentsResponseTypeDef,
    ListConnectPeersRequestTypeDef,
    ListConnectPeersResponseTypeDef,
    ListCoreNetworkPolicyVersionsRequestTypeDef,
    ListCoreNetworkPolicyVersionsResponseTypeDef,
    ListCoreNetworksRequestTypeDef,
    ListCoreNetworksResponseTypeDef,
    ListOrganizationServiceAccessStatusRequestTypeDef,
    ListOrganizationServiceAccessStatusResponseTypeDef,
    ListPeeringsRequestTypeDef,
    ListPeeringsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutCoreNetworkPolicyRequestTypeDef,
    PutCoreNetworkPolicyResponseTypeDef,
    PutResourcePolicyRequestTypeDef,
    RegisterTransitGatewayRequestTypeDef,
    RegisterTransitGatewayResponseTypeDef,
    RejectAttachmentRequestTypeDef,
    RejectAttachmentResponseTypeDef,
    RestoreCoreNetworkPolicyVersionRequestTypeDef,
    RestoreCoreNetworkPolicyVersionResponseTypeDef,
    StartOrganizationServiceAccessUpdateRequestTypeDef,
    StartOrganizationServiceAccessUpdateResponseTypeDef,
    StartRouteAnalysisRequestTypeDef,
    StartRouteAnalysisResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateConnectionRequestTypeDef,
    UpdateConnectionResponseTypeDef,
    UpdateCoreNetworkRequestTypeDef,
    UpdateCoreNetworkResponseTypeDef,
    UpdateDeviceRequestTypeDef,
    UpdateDeviceResponseTypeDef,
    UpdateDirectConnectGatewayAttachmentRequestTypeDef,
    UpdateDirectConnectGatewayAttachmentResponseTypeDef,
    UpdateGlobalNetworkRequestTypeDef,
    UpdateGlobalNetworkResponseTypeDef,
    UpdateLinkRequestTypeDef,
    UpdateLinkResponseTypeDef,
    UpdateNetworkResourceMetadataRequestTypeDef,
    UpdateNetworkResourceMetadataResponseTypeDef,
    UpdateSiteRequestTypeDef,
    UpdateSiteResponseTypeDef,
    UpdateVpcAttachmentRequestTypeDef,
    UpdateVpcAttachmentResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("NetworkManagerClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    CoreNetworkPolicyException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class NetworkManagerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        NetworkManagerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#generate_presigned_url)
        """

    def accept_attachment(
        self, **kwargs: Unpack[AcceptAttachmentRequestTypeDef]
    ) -> AcceptAttachmentResponseTypeDef:
        """
        Accepts a core network attachment request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/accept_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#accept_attachment)
        """

    def associate_connect_peer(
        self, **kwargs: Unpack[AssociateConnectPeerRequestTypeDef]
    ) -> AssociateConnectPeerResponseTypeDef:
        """
        Associates a core network Connect peer with a device and optionally, with a
        link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/associate_connect_peer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#associate_connect_peer)
        """

    def associate_customer_gateway(
        self, **kwargs: Unpack[AssociateCustomerGatewayRequestTypeDef]
    ) -> AssociateCustomerGatewayResponseTypeDef:
        """
        Associates a customer gateway with a device and optionally, with a link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/associate_customer_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#associate_customer_gateway)
        """

    def associate_link(
        self, **kwargs: Unpack[AssociateLinkRequestTypeDef]
    ) -> AssociateLinkResponseTypeDef:
        """
        Associates a link to a device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/associate_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#associate_link)
        """

    def associate_transit_gateway_connect_peer(
        self, **kwargs: Unpack[AssociateTransitGatewayConnectPeerRequestTypeDef]
    ) -> AssociateTransitGatewayConnectPeerResponseTypeDef:
        """
        Associates a transit gateway Connect peer with a device, and optionally, with a
        link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/associate_transit_gateway_connect_peer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#associate_transit_gateway_connect_peer)
        """

    def create_connect_attachment(
        self, **kwargs: Unpack[CreateConnectAttachmentRequestTypeDef]
    ) -> CreateConnectAttachmentResponseTypeDef:
        """
        Creates a core network Connect attachment from a specified core network
        attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/create_connect_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#create_connect_attachment)
        """

    def create_connect_peer(
        self, **kwargs: Unpack[CreateConnectPeerRequestTypeDef]
    ) -> CreateConnectPeerResponseTypeDef:
        """
        Creates a core network Connect peer for a specified core network connect
        attachment between a core network and an appliance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/create_connect_peer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#create_connect_peer)
        """

    def create_connection(
        self, **kwargs: Unpack[CreateConnectionRequestTypeDef]
    ) -> CreateConnectionResponseTypeDef:
        """
        Creates a connection between two devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/create_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#create_connection)
        """

    def create_core_network(
        self, **kwargs: Unpack[CreateCoreNetworkRequestTypeDef]
    ) -> CreateCoreNetworkResponseTypeDef:
        """
        Creates a core network as part of your global network, and optionally, with a
        core network policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/create_core_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#create_core_network)
        """

    def create_device(
        self, **kwargs: Unpack[CreateDeviceRequestTypeDef]
    ) -> CreateDeviceResponseTypeDef:
        """
        Creates a new device in a global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/create_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#create_device)
        """

    def create_direct_connect_gateway_attachment(
        self, **kwargs: Unpack[CreateDirectConnectGatewayAttachmentRequestTypeDef]
    ) -> CreateDirectConnectGatewayAttachmentResponseTypeDef:
        """
        Creates an Amazon Web Services Direct Connect gateway attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/create_direct_connect_gateway_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#create_direct_connect_gateway_attachment)
        """

    def create_global_network(
        self, **kwargs: Unpack[CreateGlobalNetworkRequestTypeDef]
    ) -> CreateGlobalNetworkResponseTypeDef:
        """
        Creates a new, empty global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/create_global_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#create_global_network)
        """

    def create_link(self, **kwargs: Unpack[CreateLinkRequestTypeDef]) -> CreateLinkResponseTypeDef:
        """
        Creates a new link for a specified site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/create_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#create_link)
        """

    def create_site(self, **kwargs: Unpack[CreateSiteRequestTypeDef]) -> CreateSiteResponseTypeDef:
        """
        Creates a new site in a global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/create_site.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#create_site)
        """

    def create_site_to_site_vpn_attachment(
        self, **kwargs: Unpack[CreateSiteToSiteVpnAttachmentRequestTypeDef]
    ) -> CreateSiteToSiteVpnAttachmentResponseTypeDef:
        """
        Creates an Amazon Web Services site-to-site VPN attachment on an edge location
        of a core network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/create_site_to_site_vpn_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#create_site_to_site_vpn_attachment)
        """

    def create_transit_gateway_peering(
        self, **kwargs: Unpack[CreateTransitGatewayPeeringRequestTypeDef]
    ) -> CreateTransitGatewayPeeringResponseTypeDef:
        """
        Creates a transit gateway peering connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/create_transit_gateway_peering.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#create_transit_gateway_peering)
        """

    def create_transit_gateway_route_table_attachment(
        self, **kwargs: Unpack[CreateTransitGatewayRouteTableAttachmentRequestTypeDef]
    ) -> CreateTransitGatewayRouteTableAttachmentResponseTypeDef:
        """
        Creates a transit gateway route table attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/create_transit_gateway_route_table_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#create_transit_gateway_route_table_attachment)
        """

    def create_vpc_attachment(
        self, **kwargs: Unpack[CreateVpcAttachmentRequestTypeDef]
    ) -> CreateVpcAttachmentResponseTypeDef:
        """
        Creates a VPC attachment on an edge location of a core network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/create_vpc_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#create_vpc_attachment)
        """

    def delete_attachment(
        self, **kwargs: Unpack[DeleteAttachmentRequestTypeDef]
    ) -> DeleteAttachmentResponseTypeDef:
        """
        Deletes an attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/delete_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#delete_attachment)
        """

    def delete_connect_peer(
        self, **kwargs: Unpack[DeleteConnectPeerRequestTypeDef]
    ) -> DeleteConnectPeerResponseTypeDef:
        """
        Deletes a Connect peer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/delete_connect_peer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#delete_connect_peer)
        """

    def delete_connection(
        self, **kwargs: Unpack[DeleteConnectionRequestTypeDef]
    ) -> DeleteConnectionResponseTypeDef:
        """
        Deletes the specified connection in your global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/delete_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#delete_connection)
        """

    def delete_core_network(
        self, **kwargs: Unpack[DeleteCoreNetworkRequestTypeDef]
    ) -> DeleteCoreNetworkResponseTypeDef:
        """
        Deletes a core network along with all core network policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/delete_core_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#delete_core_network)
        """

    def delete_core_network_policy_version(
        self, **kwargs: Unpack[DeleteCoreNetworkPolicyVersionRequestTypeDef]
    ) -> DeleteCoreNetworkPolicyVersionResponseTypeDef:
        """
        Deletes a policy version from a core network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/delete_core_network_policy_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#delete_core_network_policy_version)
        """

    def delete_device(
        self, **kwargs: Unpack[DeleteDeviceRequestTypeDef]
    ) -> DeleteDeviceResponseTypeDef:
        """
        Deletes an existing device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/delete_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#delete_device)
        """

    def delete_global_network(
        self, **kwargs: Unpack[DeleteGlobalNetworkRequestTypeDef]
    ) -> DeleteGlobalNetworkResponseTypeDef:
        """
        Deletes an existing global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/delete_global_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#delete_global_network)
        """

    def delete_link(self, **kwargs: Unpack[DeleteLinkRequestTypeDef]) -> DeleteLinkResponseTypeDef:
        """
        Deletes an existing link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/delete_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#delete_link)
        """

    def delete_peering(
        self, **kwargs: Unpack[DeletePeeringRequestTypeDef]
    ) -> DeletePeeringResponseTypeDef:
        """
        Deletes an existing peering connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/delete_peering.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#delete_peering)
        """

    def delete_resource_policy(
        self, **kwargs: Unpack[DeleteResourcePolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a resource policy for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/delete_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#delete_resource_policy)
        """

    def delete_site(self, **kwargs: Unpack[DeleteSiteRequestTypeDef]) -> DeleteSiteResponseTypeDef:
        """
        Deletes an existing site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/delete_site.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#delete_site)
        """

    def deregister_transit_gateway(
        self, **kwargs: Unpack[DeregisterTransitGatewayRequestTypeDef]
    ) -> DeregisterTransitGatewayResponseTypeDef:
        """
        Deregisters a transit gateway from your global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/deregister_transit_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#deregister_transit_gateway)
        """

    def describe_global_networks(
        self, **kwargs: Unpack[DescribeGlobalNetworksRequestTypeDef]
    ) -> DescribeGlobalNetworksResponseTypeDef:
        """
        Describes one or more global networks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/describe_global_networks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#describe_global_networks)
        """

    def disassociate_connect_peer(
        self, **kwargs: Unpack[DisassociateConnectPeerRequestTypeDef]
    ) -> DisassociateConnectPeerResponseTypeDef:
        """
        Disassociates a core network Connect peer from a device and a link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/disassociate_connect_peer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#disassociate_connect_peer)
        """

    def disassociate_customer_gateway(
        self, **kwargs: Unpack[DisassociateCustomerGatewayRequestTypeDef]
    ) -> DisassociateCustomerGatewayResponseTypeDef:
        """
        Disassociates a customer gateway from a device and a link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/disassociate_customer_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#disassociate_customer_gateway)
        """

    def disassociate_link(
        self, **kwargs: Unpack[DisassociateLinkRequestTypeDef]
    ) -> DisassociateLinkResponseTypeDef:
        """
        Disassociates an existing device from a link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/disassociate_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#disassociate_link)
        """

    def disassociate_transit_gateway_connect_peer(
        self, **kwargs: Unpack[DisassociateTransitGatewayConnectPeerRequestTypeDef]
    ) -> DisassociateTransitGatewayConnectPeerResponseTypeDef:
        """
        Disassociates a transit gateway Connect peer from a device and link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/disassociate_transit_gateway_connect_peer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#disassociate_transit_gateway_connect_peer)
        """

    def execute_core_network_change_set(
        self, **kwargs: Unpack[ExecuteCoreNetworkChangeSetRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Executes a change set on your core network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/execute_core_network_change_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#execute_core_network_change_set)
        """

    def get_connect_attachment(
        self, **kwargs: Unpack[GetConnectAttachmentRequestTypeDef]
    ) -> GetConnectAttachmentResponseTypeDef:
        """
        Returns information about a core network Connect attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_connect_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_connect_attachment)
        """

    def get_connect_peer(
        self, **kwargs: Unpack[GetConnectPeerRequestTypeDef]
    ) -> GetConnectPeerResponseTypeDef:
        """
        Returns information about a core network Connect peer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_connect_peer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_connect_peer)
        """

    def get_connect_peer_associations(
        self, **kwargs: Unpack[GetConnectPeerAssociationsRequestTypeDef]
    ) -> GetConnectPeerAssociationsResponseTypeDef:
        """
        Returns information about a core network Connect peer associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_connect_peer_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_connect_peer_associations)
        """

    def get_connections(
        self, **kwargs: Unpack[GetConnectionsRequestTypeDef]
    ) -> GetConnectionsResponseTypeDef:
        """
        Gets information about one or more of your connections in a global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_connections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_connections)
        """

    def get_core_network(
        self, **kwargs: Unpack[GetCoreNetworkRequestTypeDef]
    ) -> GetCoreNetworkResponseTypeDef:
        """
        Returns information about the LIVE policy for a core network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_core_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_core_network)
        """

    def get_core_network_change_events(
        self, **kwargs: Unpack[GetCoreNetworkChangeEventsRequestTypeDef]
    ) -> GetCoreNetworkChangeEventsResponseTypeDef:
        """
        Returns information about a core network change event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_core_network_change_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_core_network_change_events)
        """

    def get_core_network_change_set(
        self, **kwargs: Unpack[GetCoreNetworkChangeSetRequestTypeDef]
    ) -> GetCoreNetworkChangeSetResponseTypeDef:
        """
        Returns a change set between the LIVE core network policy and a submitted
        policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_core_network_change_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_core_network_change_set)
        """

    def get_core_network_policy(
        self, **kwargs: Unpack[GetCoreNetworkPolicyRequestTypeDef]
    ) -> GetCoreNetworkPolicyResponseTypeDef:
        """
        Returns details about a core network policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_core_network_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_core_network_policy)
        """

    def get_customer_gateway_associations(
        self, **kwargs: Unpack[GetCustomerGatewayAssociationsRequestTypeDef]
    ) -> GetCustomerGatewayAssociationsResponseTypeDef:
        """
        Gets the association information for customer gateways that are associated with
        devices and links in your global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_customer_gateway_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_customer_gateway_associations)
        """

    def get_devices(self, **kwargs: Unpack[GetDevicesRequestTypeDef]) -> GetDevicesResponseTypeDef:
        """
        Gets information about one or more of your devices in a global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_devices.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_devices)
        """

    def get_direct_connect_gateway_attachment(
        self, **kwargs: Unpack[GetDirectConnectGatewayAttachmentRequestTypeDef]
    ) -> GetDirectConnectGatewayAttachmentResponseTypeDef:
        """
        Returns information about a specific Amazon Web Services Direct Connect gateway
        attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_direct_connect_gateway_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_direct_connect_gateway_attachment)
        """

    def get_link_associations(
        self, **kwargs: Unpack[GetLinkAssociationsRequestTypeDef]
    ) -> GetLinkAssociationsResponseTypeDef:
        """
        Gets the link associations for a device or a link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_link_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_link_associations)
        """

    def get_links(self, **kwargs: Unpack[GetLinksRequestTypeDef]) -> GetLinksResponseTypeDef:
        """
        Gets information about one or more links in a specified global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_links.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_links)
        """

    def get_network_resource_counts(
        self, **kwargs: Unpack[GetNetworkResourceCountsRequestTypeDef]
    ) -> GetNetworkResourceCountsResponseTypeDef:
        """
        Gets the count of network resources, by resource type, for the specified global
        network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_network_resource_counts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_network_resource_counts)
        """

    def get_network_resource_relationships(
        self, **kwargs: Unpack[GetNetworkResourceRelationshipsRequestTypeDef]
    ) -> GetNetworkResourceRelationshipsResponseTypeDef:
        """
        Gets the network resource relationships for the specified global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_network_resource_relationships.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_network_resource_relationships)
        """

    def get_network_resources(
        self, **kwargs: Unpack[GetNetworkResourcesRequestTypeDef]
    ) -> GetNetworkResourcesResponseTypeDef:
        """
        Describes the network resources for the specified global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_network_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_network_resources)
        """

    def get_network_routes(
        self, **kwargs: Unpack[GetNetworkRoutesRequestTypeDef]
    ) -> GetNetworkRoutesResponseTypeDef:
        """
        Gets the network routes of the specified global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_network_routes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_network_routes)
        """

    def get_network_telemetry(
        self, **kwargs: Unpack[GetNetworkTelemetryRequestTypeDef]
    ) -> GetNetworkTelemetryResponseTypeDef:
        """
        Gets the network telemetry of the specified global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_network_telemetry.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_network_telemetry)
        """

    def get_resource_policy(
        self, **kwargs: Unpack[GetResourcePolicyRequestTypeDef]
    ) -> GetResourcePolicyResponseTypeDef:
        """
        Returns information about a resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_resource_policy)
        """

    def get_route_analysis(
        self, **kwargs: Unpack[GetRouteAnalysisRequestTypeDef]
    ) -> GetRouteAnalysisResponseTypeDef:
        """
        Gets information about the specified route analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_route_analysis.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_route_analysis)
        """

    def get_site_to_site_vpn_attachment(
        self, **kwargs: Unpack[GetSiteToSiteVpnAttachmentRequestTypeDef]
    ) -> GetSiteToSiteVpnAttachmentResponseTypeDef:
        """
        Returns information about a site-to-site VPN attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_site_to_site_vpn_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_site_to_site_vpn_attachment)
        """

    def get_sites(self, **kwargs: Unpack[GetSitesRequestTypeDef]) -> GetSitesResponseTypeDef:
        """
        Gets information about one or more of your sites in a global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_sites.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_sites)
        """

    def get_transit_gateway_connect_peer_associations(
        self, **kwargs: Unpack[GetTransitGatewayConnectPeerAssociationsRequestTypeDef]
    ) -> GetTransitGatewayConnectPeerAssociationsResponseTypeDef:
        """
        Gets information about one or more of your transit gateway Connect peer
        associations in a global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_transit_gateway_connect_peer_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_transit_gateway_connect_peer_associations)
        """

    def get_transit_gateway_peering(
        self, **kwargs: Unpack[GetTransitGatewayPeeringRequestTypeDef]
    ) -> GetTransitGatewayPeeringResponseTypeDef:
        """
        Returns information about a transit gateway peer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_transit_gateway_peering.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_transit_gateway_peering)
        """

    def get_transit_gateway_registrations(
        self, **kwargs: Unpack[GetTransitGatewayRegistrationsRequestTypeDef]
    ) -> GetTransitGatewayRegistrationsResponseTypeDef:
        """
        Gets information about the transit gateway registrations in a specified global
        network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_transit_gateway_registrations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_transit_gateway_registrations)
        """

    def get_transit_gateway_route_table_attachment(
        self, **kwargs: Unpack[GetTransitGatewayRouteTableAttachmentRequestTypeDef]
    ) -> GetTransitGatewayRouteTableAttachmentResponseTypeDef:
        """
        Returns information about a transit gateway route table attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_transit_gateway_route_table_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_transit_gateway_route_table_attachment)
        """

    def get_vpc_attachment(
        self, **kwargs: Unpack[GetVpcAttachmentRequestTypeDef]
    ) -> GetVpcAttachmentResponseTypeDef:
        """
        Returns information about a VPC attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_vpc_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_vpc_attachment)
        """

    def list_attachments(
        self, **kwargs: Unpack[ListAttachmentsRequestTypeDef]
    ) -> ListAttachmentsResponseTypeDef:
        """
        Returns a list of core network attachments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/list_attachments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#list_attachments)
        """

    def list_connect_peers(
        self, **kwargs: Unpack[ListConnectPeersRequestTypeDef]
    ) -> ListConnectPeersResponseTypeDef:
        """
        Returns a list of core network Connect peers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/list_connect_peers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#list_connect_peers)
        """

    def list_core_network_policy_versions(
        self, **kwargs: Unpack[ListCoreNetworkPolicyVersionsRequestTypeDef]
    ) -> ListCoreNetworkPolicyVersionsResponseTypeDef:
        """
        Returns a list of core network policy versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/list_core_network_policy_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#list_core_network_policy_versions)
        """

    def list_core_networks(
        self, **kwargs: Unpack[ListCoreNetworksRequestTypeDef]
    ) -> ListCoreNetworksResponseTypeDef:
        """
        Returns a list of owned and shared core networks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/list_core_networks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#list_core_networks)
        """

    def list_organization_service_access_status(
        self, **kwargs: Unpack[ListOrganizationServiceAccessStatusRequestTypeDef]
    ) -> ListOrganizationServiceAccessStatusResponseTypeDef:
        """
        Gets the status of the Service Linked Role (SLR) deployment for the accounts in
        a given Amazon Web Services Organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/list_organization_service_access_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#list_organization_service_access_status)
        """

    def list_peerings(
        self, **kwargs: Unpack[ListPeeringsRequestTypeDef]
    ) -> ListPeeringsResponseTypeDef:
        """
        Lists the peerings for a core network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/list_peerings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#list_peerings)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#list_tags_for_resource)
        """

    def put_core_network_policy(
        self, **kwargs: Unpack[PutCoreNetworkPolicyRequestTypeDef]
    ) -> PutCoreNetworkPolicyResponseTypeDef:
        """
        Creates a new, immutable version of a core network policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/put_core_network_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#put_core_network_policy)
        """

    def put_resource_policy(
        self, **kwargs: Unpack[PutResourcePolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates or updates a resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/put_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#put_resource_policy)
        """

    def register_transit_gateway(
        self, **kwargs: Unpack[RegisterTransitGatewayRequestTypeDef]
    ) -> RegisterTransitGatewayResponseTypeDef:
        """
        Registers a transit gateway in your global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/register_transit_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#register_transit_gateway)
        """

    def reject_attachment(
        self, **kwargs: Unpack[RejectAttachmentRequestTypeDef]
    ) -> RejectAttachmentResponseTypeDef:
        """
        Rejects a core network attachment request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/reject_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#reject_attachment)
        """

    def restore_core_network_policy_version(
        self, **kwargs: Unpack[RestoreCoreNetworkPolicyVersionRequestTypeDef]
    ) -> RestoreCoreNetworkPolicyVersionResponseTypeDef:
        """
        Restores a previous policy version as a new, immutable version of a core
        network policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/restore_core_network_policy_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#restore_core_network_policy_version)
        """

    def start_organization_service_access_update(
        self, **kwargs: Unpack[StartOrganizationServiceAccessUpdateRequestTypeDef]
    ) -> StartOrganizationServiceAccessUpdateResponseTypeDef:
        """
        Enables the Network Manager service for an Amazon Web Services Organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/start_organization_service_access_update.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#start_organization_service_access_update)
        """

    def start_route_analysis(
        self, **kwargs: Unpack[StartRouteAnalysisRequestTypeDef]
    ) -> StartRouteAnalysisResponseTypeDef:
        """
        Starts analyzing the routing path between the specified source and destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/start_route_analysis.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#start_route_analysis)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Tags a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#untag_resource)
        """

    def update_connection(
        self, **kwargs: Unpack[UpdateConnectionRequestTypeDef]
    ) -> UpdateConnectionResponseTypeDef:
        """
        Updates the information for an existing connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/update_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#update_connection)
        """

    def update_core_network(
        self, **kwargs: Unpack[UpdateCoreNetworkRequestTypeDef]
    ) -> UpdateCoreNetworkResponseTypeDef:
        """
        Updates the description of a core network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/update_core_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#update_core_network)
        """

    def update_device(
        self, **kwargs: Unpack[UpdateDeviceRequestTypeDef]
    ) -> UpdateDeviceResponseTypeDef:
        """
        Updates the details for an existing device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/update_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#update_device)
        """

    def update_direct_connect_gateway_attachment(
        self, **kwargs: Unpack[UpdateDirectConnectGatewayAttachmentRequestTypeDef]
    ) -> UpdateDirectConnectGatewayAttachmentResponseTypeDef:
        """
        Updates the edge locations associated with an Amazon Web Services Direct
        Connect gateway attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/update_direct_connect_gateway_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#update_direct_connect_gateway_attachment)
        """

    def update_global_network(
        self, **kwargs: Unpack[UpdateGlobalNetworkRequestTypeDef]
    ) -> UpdateGlobalNetworkResponseTypeDef:
        """
        Updates an existing global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/update_global_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#update_global_network)
        """

    def update_link(self, **kwargs: Unpack[UpdateLinkRequestTypeDef]) -> UpdateLinkResponseTypeDef:
        """
        Updates the details for an existing link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/update_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#update_link)
        """

    def update_network_resource_metadata(
        self, **kwargs: Unpack[UpdateNetworkResourceMetadataRequestTypeDef]
    ) -> UpdateNetworkResourceMetadataResponseTypeDef:
        """
        Updates the resource metadata for the specified global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/update_network_resource_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#update_network_resource_metadata)
        """

    def update_site(self, **kwargs: Unpack[UpdateSiteRequestTypeDef]) -> UpdateSiteResponseTypeDef:
        """
        Updates the information for an existing site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/update_site.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#update_site)
        """

    def update_vpc_attachment(
        self, **kwargs: Unpack[UpdateVpcAttachmentRequestTypeDef]
    ) -> UpdateVpcAttachmentResponseTypeDef:
        """
        Updates a VPC attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/update_vpc_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#update_vpc_attachment)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_global_networks"]
    ) -> DescribeGlobalNetworksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_connect_peer_associations"]
    ) -> GetConnectPeerAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_connections"]
    ) -> GetConnectionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_core_network_change_events"]
    ) -> GetCoreNetworkChangeEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_core_network_change_set"]
    ) -> GetCoreNetworkChangeSetPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_customer_gateway_associations"]
    ) -> GetCustomerGatewayAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_devices"]
    ) -> GetDevicesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_link_associations"]
    ) -> GetLinkAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_links"]
    ) -> GetLinksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_network_resource_counts"]
    ) -> GetNetworkResourceCountsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_network_resource_relationships"]
    ) -> GetNetworkResourceRelationshipsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_network_resources"]
    ) -> GetNetworkResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_network_telemetry"]
    ) -> GetNetworkTelemetryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_sites"]
    ) -> GetSitesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_transit_gateway_connect_peer_associations"]
    ) -> GetTransitGatewayConnectPeerAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_transit_gateway_registrations"]
    ) -> GetTransitGatewayRegistrationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_attachments"]
    ) -> ListAttachmentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_connect_peers"]
    ) -> ListConnectPeersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_core_network_policy_versions"]
    ) -> ListCoreNetworkPolicyVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_core_networks"]
    ) -> ListCoreNetworksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_peerings"]
    ) -> ListPeeringsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client/#get_paginator)
        """
