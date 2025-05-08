"""
Type annotations for networkmanager service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_networkmanager.client import NetworkManagerClient
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

    session = Session()
    client: NetworkManagerClient = session.client("networkmanager")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeGlobalNetworksRequestPaginateTypeDef,
    DescribeGlobalNetworksResponseTypeDef,
    GetConnectionsRequestPaginateTypeDef,
    GetConnectionsResponseTypeDef,
    GetConnectPeerAssociationsRequestPaginateTypeDef,
    GetConnectPeerAssociationsResponseTypeDef,
    GetCoreNetworkChangeEventsRequestPaginateTypeDef,
    GetCoreNetworkChangeEventsResponseTypeDef,
    GetCoreNetworkChangeSetRequestPaginateTypeDef,
    GetCoreNetworkChangeSetResponseTypeDef,
    GetCustomerGatewayAssociationsRequestPaginateTypeDef,
    GetCustomerGatewayAssociationsResponseTypeDef,
    GetDevicesRequestPaginateTypeDef,
    GetDevicesResponseTypeDef,
    GetLinkAssociationsRequestPaginateTypeDef,
    GetLinkAssociationsResponseTypeDef,
    GetLinksRequestPaginateTypeDef,
    GetLinksResponseTypeDef,
    GetNetworkResourceCountsRequestPaginateTypeDef,
    GetNetworkResourceCountsResponseTypeDef,
    GetNetworkResourceRelationshipsRequestPaginateTypeDef,
    GetNetworkResourceRelationshipsResponseTypeDef,
    GetNetworkResourcesRequestPaginateTypeDef,
    GetNetworkResourcesResponseTypeDef,
    GetNetworkTelemetryRequestPaginateTypeDef,
    GetNetworkTelemetryResponseTypeDef,
    GetSitesRequestPaginateTypeDef,
    GetSitesResponseTypeDef,
    GetTransitGatewayConnectPeerAssociationsRequestPaginateTypeDef,
    GetTransitGatewayConnectPeerAssociationsResponseTypeDef,
    GetTransitGatewayRegistrationsRequestPaginateTypeDef,
    GetTransitGatewayRegistrationsResponseTypeDef,
    ListAttachmentsRequestPaginateTypeDef,
    ListAttachmentsResponseTypeDef,
    ListConnectPeersRequestPaginateTypeDef,
    ListConnectPeersResponseTypeDef,
    ListCoreNetworkPolicyVersionsRequestPaginateTypeDef,
    ListCoreNetworkPolicyVersionsResponseTypeDef,
    ListCoreNetworksRequestPaginateTypeDef,
    ListCoreNetworksResponseTypeDef,
    ListPeeringsRequestPaginateTypeDef,
    ListPeeringsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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

if TYPE_CHECKING:
    _DescribeGlobalNetworksPaginatorBase = Paginator[DescribeGlobalNetworksResponseTypeDef]
else:
    _DescribeGlobalNetworksPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeGlobalNetworksPaginator(_DescribeGlobalNetworksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/DescribeGlobalNetworks.html#NetworkManager.Paginator.DescribeGlobalNetworks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#describeglobalnetworkspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeGlobalNetworksRequestPaginateTypeDef]
    ) -> PageIterator[DescribeGlobalNetworksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/DescribeGlobalNetworks.html#NetworkManager.Paginator.DescribeGlobalNetworks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#describeglobalnetworkspaginator)
        """

if TYPE_CHECKING:
    _GetConnectPeerAssociationsPaginatorBase = Paginator[GetConnectPeerAssociationsResponseTypeDef]
else:
    _GetConnectPeerAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class GetConnectPeerAssociationsPaginator(_GetConnectPeerAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetConnectPeerAssociations.html#NetworkManager.Paginator.GetConnectPeerAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getconnectpeerassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetConnectPeerAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[GetConnectPeerAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetConnectPeerAssociations.html#NetworkManager.Paginator.GetConnectPeerAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getconnectpeerassociationspaginator)
        """

if TYPE_CHECKING:
    _GetConnectionsPaginatorBase = Paginator[GetConnectionsResponseTypeDef]
else:
    _GetConnectionsPaginatorBase = Paginator  # type: ignore[assignment]

class GetConnectionsPaginator(_GetConnectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetConnections.html#NetworkManager.Paginator.GetConnections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getconnectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetConnectionsRequestPaginateTypeDef]
    ) -> PageIterator[GetConnectionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetConnections.html#NetworkManager.Paginator.GetConnections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getconnectionspaginator)
        """

if TYPE_CHECKING:
    _GetCoreNetworkChangeEventsPaginatorBase = Paginator[GetCoreNetworkChangeEventsResponseTypeDef]
else:
    _GetCoreNetworkChangeEventsPaginatorBase = Paginator  # type: ignore[assignment]

class GetCoreNetworkChangeEventsPaginator(_GetCoreNetworkChangeEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetCoreNetworkChangeEvents.html#NetworkManager.Paginator.GetCoreNetworkChangeEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getcorenetworkchangeeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetCoreNetworkChangeEventsRequestPaginateTypeDef]
    ) -> PageIterator[GetCoreNetworkChangeEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetCoreNetworkChangeEvents.html#NetworkManager.Paginator.GetCoreNetworkChangeEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getcorenetworkchangeeventspaginator)
        """

if TYPE_CHECKING:
    _GetCoreNetworkChangeSetPaginatorBase = Paginator[GetCoreNetworkChangeSetResponseTypeDef]
else:
    _GetCoreNetworkChangeSetPaginatorBase = Paginator  # type: ignore[assignment]

class GetCoreNetworkChangeSetPaginator(_GetCoreNetworkChangeSetPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetCoreNetworkChangeSet.html#NetworkManager.Paginator.GetCoreNetworkChangeSet)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getcorenetworkchangesetpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetCoreNetworkChangeSetRequestPaginateTypeDef]
    ) -> PageIterator[GetCoreNetworkChangeSetResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetCoreNetworkChangeSet.html#NetworkManager.Paginator.GetCoreNetworkChangeSet.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getcorenetworkchangesetpaginator)
        """

if TYPE_CHECKING:
    _GetCustomerGatewayAssociationsPaginatorBase = Paginator[
        GetCustomerGatewayAssociationsResponseTypeDef
    ]
else:
    _GetCustomerGatewayAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class GetCustomerGatewayAssociationsPaginator(_GetCustomerGatewayAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetCustomerGatewayAssociations.html#NetworkManager.Paginator.GetCustomerGatewayAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getcustomergatewayassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetCustomerGatewayAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[GetCustomerGatewayAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetCustomerGatewayAssociations.html#NetworkManager.Paginator.GetCustomerGatewayAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getcustomergatewayassociationspaginator)
        """

if TYPE_CHECKING:
    _GetDevicesPaginatorBase = Paginator[GetDevicesResponseTypeDef]
else:
    _GetDevicesPaginatorBase = Paginator  # type: ignore[assignment]

class GetDevicesPaginator(_GetDevicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetDevices.html#NetworkManager.Paginator.GetDevices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getdevicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetDevicesRequestPaginateTypeDef]
    ) -> PageIterator[GetDevicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetDevices.html#NetworkManager.Paginator.GetDevices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getdevicespaginator)
        """

if TYPE_CHECKING:
    _GetLinkAssociationsPaginatorBase = Paginator[GetLinkAssociationsResponseTypeDef]
else:
    _GetLinkAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class GetLinkAssociationsPaginator(_GetLinkAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetLinkAssociations.html#NetworkManager.Paginator.GetLinkAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getlinkassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetLinkAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[GetLinkAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetLinkAssociations.html#NetworkManager.Paginator.GetLinkAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getlinkassociationspaginator)
        """

if TYPE_CHECKING:
    _GetLinksPaginatorBase = Paginator[GetLinksResponseTypeDef]
else:
    _GetLinksPaginatorBase = Paginator  # type: ignore[assignment]

class GetLinksPaginator(_GetLinksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetLinks.html#NetworkManager.Paginator.GetLinks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getlinkspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetLinksRequestPaginateTypeDef]
    ) -> PageIterator[GetLinksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetLinks.html#NetworkManager.Paginator.GetLinks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getlinkspaginator)
        """

if TYPE_CHECKING:
    _GetNetworkResourceCountsPaginatorBase = Paginator[GetNetworkResourceCountsResponseTypeDef]
else:
    _GetNetworkResourceCountsPaginatorBase = Paginator  # type: ignore[assignment]

class GetNetworkResourceCountsPaginator(_GetNetworkResourceCountsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetNetworkResourceCounts.html#NetworkManager.Paginator.GetNetworkResourceCounts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getnetworkresourcecountspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetNetworkResourceCountsRequestPaginateTypeDef]
    ) -> PageIterator[GetNetworkResourceCountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetNetworkResourceCounts.html#NetworkManager.Paginator.GetNetworkResourceCounts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getnetworkresourcecountspaginator)
        """

if TYPE_CHECKING:
    _GetNetworkResourceRelationshipsPaginatorBase = Paginator[
        GetNetworkResourceRelationshipsResponseTypeDef
    ]
else:
    _GetNetworkResourceRelationshipsPaginatorBase = Paginator  # type: ignore[assignment]

class GetNetworkResourceRelationshipsPaginator(_GetNetworkResourceRelationshipsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetNetworkResourceRelationships.html#NetworkManager.Paginator.GetNetworkResourceRelationships)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getnetworkresourcerelationshipspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetNetworkResourceRelationshipsRequestPaginateTypeDef]
    ) -> PageIterator[GetNetworkResourceRelationshipsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetNetworkResourceRelationships.html#NetworkManager.Paginator.GetNetworkResourceRelationships.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getnetworkresourcerelationshipspaginator)
        """

if TYPE_CHECKING:
    _GetNetworkResourcesPaginatorBase = Paginator[GetNetworkResourcesResponseTypeDef]
else:
    _GetNetworkResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class GetNetworkResourcesPaginator(_GetNetworkResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetNetworkResources.html#NetworkManager.Paginator.GetNetworkResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getnetworkresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetNetworkResourcesRequestPaginateTypeDef]
    ) -> PageIterator[GetNetworkResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetNetworkResources.html#NetworkManager.Paginator.GetNetworkResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getnetworkresourcespaginator)
        """

if TYPE_CHECKING:
    _GetNetworkTelemetryPaginatorBase = Paginator[GetNetworkTelemetryResponseTypeDef]
else:
    _GetNetworkTelemetryPaginatorBase = Paginator  # type: ignore[assignment]

class GetNetworkTelemetryPaginator(_GetNetworkTelemetryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetNetworkTelemetry.html#NetworkManager.Paginator.GetNetworkTelemetry)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getnetworktelemetrypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetNetworkTelemetryRequestPaginateTypeDef]
    ) -> PageIterator[GetNetworkTelemetryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetNetworkTelemetry.html#NetworkManager.Paginator.GetNetworkTelemetry.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getnetworktelemetrypaginator)
        """

if TYPE_CHECKING:
    _GetSitesPaginatorBase = Paginator[GetSitesResponseTypeDef]
else:
    _GetSitesPaginatorBase = Paginator  # type: ignore[assignment]

class GetSitesPaginator(_GetSitesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetSites.html#NetworkManager.Paginator.GetSites)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getsitespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetSitesRequestPaginateTypeDef]
    ) -> PageIterator[GetSitesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetSites.html#NetworkManager.Paginator.GetSites.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#getsitespaginator)
        """

if TYPE_CHECKING:
    _GetTransitGatewayConnectPeerAssociationsPaginatorBase = Paginator[
        GetTransitGatewayConnectPeerAssociationsResponseTypeDef
    ]
else:
    _GetTransitGatewayConnectPeerAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class GetTransitGatewayConnectPeerAssociationsPaginator(
    _GetTransitGatewayConnectPeerAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetTransitGatewayConnectPeerAssociations.html#NetworkManager.Paginator.GetTransitGatewayConnectPeerAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#gettransitgatewayconnectpeerassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetTransitGatewayConnectPeerAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[GetTransitGatewayConnectPeerAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetTransitGatewayConnectPeerAssociations.html#NetworkManager.Paginator.GetTransitGatewayConnectPeerAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#gettransitgatewayconnectpeerassociationspaginator)
        """

if TYPE_CHECKING:
    _GetTransitGatewayRegistrationsPaginatorBase = Paginator[
        GetTransitGatewayRegistrationsResponseTypeDef
    ]
else:
    _GetTransitGatewayRegistrationsPaginatorBase = Paginator  # type: ignore[assignment]

class GetTransitGatewayRegistrationsPaginator(_GetTransitGatewayRegistrationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetTransitGatewayRegistrations.html#NetworkManager.Paginator.GetTransitGatewayRegistrations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#gettransitgatewayregistrationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetTransitGatewayRegistrationsRequestPaginateTypeDef]
    ) -> PageIterator[GetTransitGatewayRegistrationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/GetTransitGatewayRegistrations.html#NetworkManager.Paginator.GetTransitGatewayRegistrations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#gettransitgatewayregistrationspaginator)
        """

if TYPE_CHECKING:
    _ListAttachmentsPaginatorBase = Paginator[ListAttachmentsResponseTypeDef]
else:
    _ListAttachmentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAttachmentsPaginator(_ListAttachmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/ListAttachments.html#NetworkManager.Paginator.ListAttachments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#listattachmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAttachmentsRequestPaginateTypeDef]
    ) -> PageIterator[ListAttachmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/ListAttachments.html#NetworkManager.Paginator.ListAttachments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#listattachmentspaginator)
        """

if TYPE_CHECKING:
    _ListConnectPeersPaginatorBase = Paginator[ListConnectPeersResponseTypeDef]
else:
    _ListConnectPeersPaginatorBase = Paginator  # type: ignore[assignment]

class ListConnectPeersPaginator(_ListConnectPeersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/ListConnectPeers.html#NetworkManager.Paginator.ListConnectPeers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#listconnectpeerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConnectPeersRequestPaginateTypeDef]
    ) -> PageIterator[ListConnectPeersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/ListConnectPeers.html#NetworkManager.Paginator.ListConnectPeers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#listconnectpeerspaginator)
        """

if TYPE_CHECKING:
    _ListCoreNetworkPolicyVersionsPaginatorBase = Paginator[
        ListCoreNetworkPolicyVersionsResponseTypeDef
    ]
else:
    _ListCoreNetworkPolicyVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCoreNetworkPolicyVersionsPaginator(_ListCoreNetworkPolicyVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/ListCoreNetworkPolicyVersions.html#NetworkManager.Paginator.ListCoreNetworkPolicyVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#listcorenetworkpolicyversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCoreNetworkPolicyVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListCoreNetworkPolicyVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/ListCoreNetworkPolicyVersions.html#NetworkManager.Paginator.ListCoreNetworkPolicyVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#listcorenetworkpolicyversionspaginator)
        """

if TYPE_CHECKING:
    _ListCoreNetworksPaginatorBase = Paginator[ListCoreNetworksResponseTypeDef]
else:
    _ListCoreNetworksPaginatorBase = Paginator  # type: ignore[assignment]

class ListCoreNetworksPaginator(_ListCoreNetworksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/ListCoreNetworks.html#NetworkManager.Paginator.ListCoreNetworks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#listcorenetworkspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCoreNetworksRequestPaginateTypeDef]
    ) -> PageIterator[ListCoreNetworksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/ListCoreNetworks.html#NetworkManager.Paginator.ListCoreNetworks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#listcorenetworkspaginator)
        """

if TYPE_CHECKING:
    _ListPeeringsPaginatorBase = Paginator[ListPeeringsResponseTypeDef]
else:
    _ListPeeringsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPeeringsPaginator(_ListPeeringsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/ListPeerings.html#NetworkManager.Paginator.ListPeerings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#listpeeringspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPeeringsRequestPaginateTypeDef]
    ) -> PageIterator[ListPeeringsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager/paginator/ListPeerings.html#NetworkManager.Paginator.ListPeerings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators/#listpeeringspaginator)
        """
