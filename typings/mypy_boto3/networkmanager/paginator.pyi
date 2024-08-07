"""
Type annotations for networkmanager service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_networkmanager import NetworkManagerClient
    from mypy_boto3_networkmanager.paginator import (
        DescribeGlobalNetworksPaginator,
        GetConnectPeerAssociationsPaginator,
        GetConnectionsPaginator,
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

    client: NetworkManagerClient = boto3.client("networkmanager")

    describe_global_networks_paginator: DescribeGlobalNetworksPaginator = client.get_paginator("describe_global_networks")
    get_connect_peer_associations_paginator: GetConnectPeerAssociationsPaginator = client.get_paginator("get_connect_peer_associations")
    get_connections_paginator: GetConnectionsPaginator = client.get_paginator("get_connections")
    get_core_network_change_events_paginator: GetCoreNetworkChangeEventsPaginator = client.get_paginator("get_core_network_change_events")
    get_core_network_change_set_paginator: GetCoreNetworkChangeSetPaginator = client.get_paginator("get_core_network_change_set")
    get_customer_gateway_associations_paginator: GetCustomerGatewayAssociationsPaginator = client.get_paginator("get_customer_gateway_associations")
    get_devices_paginator: GetDevicesPaginator = client.get_paginator("get_devices")
    get_link_associations_paginator: GetLinkAssociationsPaginator = client.get_paginator("get_link_associations")
    get_links_paginator: GetLinksPaginator = client.get_paginator("get_links")
    get_network_resource_counts_paginator: GetNetworkResourceCountsPaginator = client.get_paginator("get_network_resource_counts")
    get_network_resource_relationships_paginator: GetNetworkResourceRelationshipsPaginator = client.get_paginator("get_network_resource_relationships")
    get_network_resources_paginator: GetNetworkResourcesPaginator = client.get_paginator("get_network_resources")
    get_network_telemetry_paginator: GetNetworkTelemetryPaginator = client.get_paginator("get_network_telemetry")
    get_sites_paginator: GetSitesPaginator = client.get_paginator("get_sites")
    get_transit_gateway_connect_peer_associations_paginator: GetTransitGatewayConnectPeerAssociationsPaginator = client.get_paginator("get_transit_gateway_connect_peer_associations")
    get_transit_gateway_registrations_paginator: GetTransitGatewayRegistrationsPaginator = client.get_paginator("get_transit_gateway_registrations")
    list_attachments_paginator: ListAttachmentsPaginator = client.get_paginator("list_attachments")
    list_connect_peers_paginator: ListConnectPeersPaginator = client.get_paginator("list_connect_peers")
    list_core_network_policy_versions_paginator: ListCoreNetworkPolicyVersionsPaginator = client.get_paginator("list_core_network_policy_versions")
    list_core_networks_paginator: ListCoreNetworksPaginator = client.get_paginator("list_core_networks")
    list_peerings_paginator: ListPeeringsPaginator = client.get_paginator("list_peerings")
    ```
"""

import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import AttachmentStateType, AttachmentTypeType, PeeringStateType
from .type_defs import (
    DescribeGlobalNetworksResponseTypeDef,
    GetConnectionsResponseTypeDef,
    GetConnectPeerAssociationsResponseTypeDef,
    GetCoreNetworkChangeEventsResponseTypeDef,
    GetCoreNetworkChangeSetResponseTypeDef,
    GetCustomerGatewayAssociationsResponseTypeDef,
    GetDevicesResponseTypeDef,
    GetLinkAssociationsResponseTypeDef,
    GetLinksResponseTypeDef,
    GetNetworkResourceCountsResponseTypeDef,
    GetNetworkResourceRelationshipsResponseTypeDef,
    GetNetworkResourcesResponseTypeDef,
    GetNetworkTelemetryResponseTypeDef,
    GetSitesResponseTypeDef,
    GetTransitGatewayConnectPeerAssociationsResponseTypeDef,
    GetTransitGatewayRegistrationsResponseTypeDef,
    ListAttachmentsResponseTypeDef,
    ListConnectPeersResponseTypeDef,
    ListCoreNetworkPolicyVersionsResponseTypeDef,
    ListCoreNetworksResponseTypeDef,
    ListPeeringsResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DescribeGlobalNetworksPaginator",
    "GetConnectPeerAssociationsPaginator",
    "GetConnectionsPaginator",
    "GetCoreNetworkChangeEventsPaginator",
    "GetCoreNetworkChangeSetPaginator",
    "GetCustomerGatewayAssociationsPaginator",
    "GetDevicesPaginator",
    "GetLinkAssociationsPaginator",
    "GetLinksPaginator",
    "GetNetworkResourceCountsPaginator",
    "GetNetworkResourceRelationshipsPaginator",
    "GetNetworkResourcesPaginator",
    "GetNetworkTelemetryPaginator",
    "GetSitesPaginator",
    "GetTransitGatewayConnectPeerAssociationsPaginator",
    "GetTransitGatewayRegistrationsPaginator",
    "ListAttachmentsPaginator",
    "ListConnectPeersPaginator",
    "ListCoreNetworkPolicyVersionsPaginator",
    "ListCoreNetworksPaginator",
    "ListPeeringsPaginator",
)

class DescribeGlobalNetworksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.DescribeGlobalNetworks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#describeglobalnetworkspaginator)
    """

    def paginate(
        self, *, GlobalNetworkIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeGlobalNetworksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.DescribeGlobalNetworks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#describeglobalnetworkspaginator)
        """

class GetConnectPeerAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetConnectPeerAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getconnectpeerassociationspaginator)
    """

    def paginate(
        self,
        *,
        GlobalNetworkId: str,
        ConnectPeerIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetConnectPeerAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetConnectPeerAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getconnectpeerassociationspaginator)
        """

class GetConnectionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetConnections)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getconnectionspaginator)
    """

    def paginate(
        self,
        *,
        GlobalNetworkId: str,
        ConnectionIds: List[str] = None,
        DeviceId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetConnectionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetConnections.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getconnectionspaginator)
        """

class GetCoreNetworkChangeEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetCoreNetworkChangeEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getcorenetworkchangeeventspaginator)
    """

    def paginate(
        self,
        *,
        CoreNetworkId: str,
        PolicyVersionId: int,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetCoreNetworkChangeEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetCoreNetworkChangeEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getcorenetworkchangeeventspaginator)
        """

class GetCoreNetworkChangeSetPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetCoreNetworkChangeSet)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getcorenetworkchangesetpaginator)
    """

    def paginate(
        self,
        *,
        CoreNetworkId: str,
        PolicyVersionId: int,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetCoreNetworkChangeSetResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetCoreNetworkChangeSet.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getcorenetworkchangesetpaginator)
        """

class GetCustomerGatewayAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetCustomerGatewayAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getcustomergatewayassociationspaginator)
    """

    def paginate(
        self,
        *,
        GlobalNetworkId: str,
        CustomerGatewayArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetCustomerGatewayAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetCustomerGatewayAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getcustomergatewayassociationspaginator)
        """

class GetDevicesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetDevices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getdevicespaginator)
    """

    def paginate(
        self,
        *,
        GlobalNetworkId: str,
        DeviceIds: List[str] = None,
        SiteId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDevicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetDevices.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getdevicespaginator)
        """

class GetLinkAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinkAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getlinkassociationspaginator)
    """

    def paginate(
        self,
        *,
        GlobalNetworkId: str,
        DeviceId: str = None,
        LinkId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetLinkAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinkAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getlinkassociationspaginator)
        """

class GetLinksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getlinkspaginator)
    """

    def paginate(
        self,
        *,
        GlobalNetworkId: str,
        LinkIds: List[str] = None,
        SiteId: str = None,
        Type: str = None,
        Provider: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetLinksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getlinkspaginator)
        """

class GetNetworkResourceCountsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetNetworkResourceCounts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getnetworkresourcecountspaginator)
    """

    def paginate(
        self,
        *,
        GlobalNetworkId: str,
        ResourceType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetNetworkResourceCountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetNetworkResourceCounts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getnetworkresourcecountspaginator)
        """

class GetNetworkResourceRelationshipsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetNetworkResourceRelationships)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getnetworkresourcerelationshipspaginator)
    """

    def paginate(
        self,
        *,
        GlobalNetworkId: str,
        CoreNetworkId: str = None,
        RegisteredGatewayArn: str = None,
        AwsRegion: str = None,
        AccountId: str = None,
        ResourceType: str = None,
        ResourceArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetNetworkResourceRelationshipsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetNetworkResourceRelationships.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getnetworkresourcerelationshipspaginator)
        """

class GetNetworkResourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetNetworkResources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getnetworkresourcespaginator)
    """

    def paginate(
        self,
        *,
        GlobalNetworkId: str,
        CoreNetworkId: str = None,
        RegisteredGatewayArn: str = None,
        AwsRegion: str = None,
        AccountId: str = None,
        ResourceType: str = None,
        ResourceArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetNetworkResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetNetworkResources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getnetworkresourcespaginator)
        """

class GetNetworkTelemetryPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetNetworkTelemetry)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getnetworktelemetrypaginator)
    """

    def paginate(
        self,
        *,
        GlobalNetworkId: str,
        CoreNetworkId: str = None,
        RegisteredGatewayArn: str = None,
        AwsRegion: str = None,
        AccountId: str = None,
        ResourceType: str = None,
        ResourceArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetNetworkTelemetryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetNetworkTelemetry.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getnetworktelemetrypaginator)
        """

class GetSitesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetSites)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getsitespaginator)
    """

    def paginate(
        self,
        *,
        GlobalNetworkId: str,
        SiteIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetSitesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetSites.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getsitespaginator)
        """

class GetTransitGatewayConnectPeerAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayConnectPeerAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#gettransitgatewayconnectpeerassociationspaginator)
    """

    def paginate(
        self,
        *,
        GlobalNetworkId: str,
        TransitGatewayConnectPeerArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTransitGatewayConnectPeerAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayConnectPeerAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#gettransitgatewayconnectpeerassociationspaginator)
        """

class GetTransitGatewayRegistrationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayRegistrations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#gettransitgatewayregistrationspaginator)
    """

    def paginate(
        self,
        *,
        GlobalNetworkId: str,
        TransitGatewayArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTransitGatewayRegistrationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayRegistrations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#gettransitgatewayregistrationspaginator)
        """

class ListAttachmentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.ListAttachments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#listattachmentspaginator)
    """

    def paginate(
        self,
        *,
        CoreNetworkId: str = None,
        AttachmentType: AttachmentTypeType = None,
        EdgeLocation: str = None,
        State: AttachmentStateType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAttachmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.ListAttachments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#listattachmentspaginator)
        """

class ListConnectPeersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.ListConnectPeers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#listconnectpeerspaginator)
    """

    def paginate(
        self,
        *,
        CoreNetworkId: str = None,
        ConnectAttachmentId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConnectPeersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.ListConnectPeers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#listconnectpeerspaginator)
        """

class ListCoreNetworkPolicyVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.ListCoreNetworkPolicyVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#listcorenetworkpolicyversionspaginator)
    """

    def paginate(
        self, *, CoreNetworkId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCoreNetworkPolicyVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.ListCoreNetworkPolicyVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#listcorenetworkpolicyversionspaginator)
        """

class ListCoreNetworksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.ListCoreNetworks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#listcorenetworkspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCoreNetworksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.ListCoreNetworks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#listcorenetworkspaginator)
        """

class ListPeeringsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.ListPeerings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#listpeeringspaginator)
    """

    def paginate(
        self,
        *,
        CoreNetworkId: str = None,
        PeeringType: Literal["TRANSIT_GATEWAY"] = None,
        EdgeLocation: str = None,
        State: PeeringStateType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPeeringsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmanager.html#NetworkManager.Paginator.ListPeerings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#listpeeringspaginator)
        """
