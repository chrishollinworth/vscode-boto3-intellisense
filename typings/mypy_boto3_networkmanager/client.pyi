# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for networkmanager service client

Usage::

    ```python
    import boto3
    from mypy_boto3_networkmanager import NetworkManagerClient

    client: NetworkManagerClient = boto3.client("networkmanager")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_networkmanager.paginator import (
    DescribeGlobalNetworksPaginator,
    GetCustomerGatewayAssociationsPaginator,
    GetDevicesPaginator,
    GetLinkAssociationsPaginator,
    GetLinksPaginator,
    GetSitesPaginator,
    GetTransitGatewayRegistrationsPaginator,
)
from mypy_boto3_networkmanager.type_defs import (
    AssociateCustomerGatewayResponseTypeDef,
    AssociateLinkResponseTypeDef,
    BandwidthTypeDef,
    CreateDeviceResponseTypeDef,
    CreateGlobalNetworkResponseTypeDef,
    CreateLinkResponseTypeDef,
    CreateSiteResponseTypeDef,
    DeleteDeviceResponseTypeDef,
    DeleteGlobalNetworkResponseTypeDef,
    DeleteLinkResponseTypeDef,
    DeleteSiteResponseTypeDef,
    DeregisterTransitGatewayResponseTypeDef,
    DescribeGlobalNetworksResponseTypeDef,
    DisassociateCustomerGatewayResponseTypeDef,
    DisassociateLinkResponseTypeDef,
    GetCustomerGatewayAssociationsResponseTypeDef,
    GetDevicesResponseTypeDef,
    GetLinkAssociationsResponseTypeDef,
    GetLinksResponseTypeDef,
    GetSitesResponseTypeDef,
    GetTransitGatewayRegistrationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LocationTypeDef,
    RegisterTransitGatewayResponseTypeDef,
    TagTypeDef,
    UpdateDeviceResponseTypeDef,
    UpdateGlobalNetworkResponseTypeDef,
    UpdateLinkResponseTypeDef,
    UpdateSiteResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("NetworkManagerClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class NetworkManagerClient:
    """
    [NetworkManager.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_customer_gateway(
        self, CustomerGatewayArn: str, GlobalNetworkId: str, DeviceId: str, LinkId: str = None
    ) -> AssociateCustomerGatewayResponseTypeDef:
        """
        [Client.associate_customer_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.associate_customer_gateway)
        """

    def associate_link(
        self, GlobalNetworkId: str, DeviceId: str, LinkId: str
    ) -> AssociateLinkResponseTypeDef:
        """
        [Client.associate_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.associate_link)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.can_paginate)
        """

    def create_device(
        self,
        GlobalNetworkId: str,
        Description: str = None,
        Type: str = None,
        Vendor: str = None,
        Model: str = None,
        SerialNumber: str = None,
        Location: "LocationTypeDef" = None,
        SiteId: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDeviceResponseTypeDef:
        """
        [Client.create_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.create_device)
        """

    def create_global_network(
        self, Description: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateGlobalNetworkResponseTypeDef:
        """
        [Client.create_global_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.create_global_network)
        """

    def create_link(
        self,
        GlobalNetworkId: str,
        Bandwidth: "BandwidthTypeDef",
        SiteId: str,
        Description: str = None,
        Type: str = None,
        Provider: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateLinkResponseTypeDef:
        """
        [Client.create_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.create_link)
        """

    def create_site(
        self,
        GlobalNetworkId: str,
        Description: str = None,
        Location: "LocationTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateSiteResponseTypeDef:
        """
        [Client.create_site documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.create_site)
        """

    def delete_device(self, GlobalNetworkId: str, DeviceId: str) -> DeleteDeviceResponseTypeDef:
        """
        [Client.delete_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.delete_device)
        """

    def delete_global_network(self, GlobalNetworkId: str) -> DeleteGlobalNetworkResponseTypeDef:
        """
        [Client.delete_global_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.delete_global_network)
        """

    def delete_link(self, GlobalNetworkId: str, LinkId: str) -> DeleteLinkResponseTypeDef:
        """
        [Client.delete_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.delete_link)
        """

    def delete_site(self, GlobalNetworkId: str, SiteId: str) -> DeleteSiteResponseTypeDef:
        """
        [Client.delete_site documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.delete_site)
        """

    def deregister_transit_gateway(
        self, GlobalNetworkId: str, TransitGatewayArn: str
    ) -> DeregisterTransitGatewayResponseTypeDef:
        """
        [Client.deregister_transit_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.deregister_transit_gateway)
        """

    def describe_global_networks(
        self, GlobalNetworkIds: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeGlobalNetworksResponseTypeDef:
        """
        [Client.describe_global_networks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.describe_global_networks)
        """

    def disassociate_customer_gateway(
        self, GlobalNetworkId: str, CustomerGatewayArn: str
    ) -> DisassociateCustomerGatewayResponseTypeDef:
        """
        [Client.disassociate_customer_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.disassociate_customer_gateway)
        """

    def disassociate_link(
        self, GlobalNetworkId: str, DeviceId: str, LinkId: str
    ) -> DisassociateLinkResponseTypeDef:
        """
        [Client.disassociate_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.disassociate_link)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.generate_presigned_url)
        """

    def get_customer_gateway_associations(
        self,
        GlobalNetworkId: str,
        CustomerGatewayArns: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetCustomerGatewayAssociationsResponseTypeDef:
        """
        [Client.get_customer_gateway_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.get_customer_gateway_associations)
        """

    def get_devices(
        self,
        GlobalNetworkId: str,
        DeviceIds: List[str] = None,
        SiteId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetDevicesResponseTypeDef:
        """
        [Client.get_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.get_devices)
        """

    def get_link_associations(
        self,
        GlobalNetworkId: str,
        DeviceId: str = None,
        LinkId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetLinkAssociationsResponseTypeDef:
        """
        [Client.get_link_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.get_link_associations)
        """

    def get_links(
        self,
        GlobalNetworkId: str,
        LinkIds: List[str] = None,
        SiteId: str = None,
        Type: str = None,
        Provider: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetLinksResponseTypeDef:
        """
        [Client.get_links documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.get_links)
        """

    def get_sites(
        self,
        GlobalNetworkId: str,
        SiteIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetSitesResponseTypeDef:
        """
        [Client.get_sites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.get_sites)
        """

    def get_transit_gateway_registrations(
        self,
        GlobalNetworkId: str,
        TransitGatewayArns: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetTransitGatewayRegistrationsResponseTypeDef:
        """
        [Client.get_transit_gateway_registrations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.get_transit_gateway_registrations)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.list_tags_for_resource)
        """

    def register_transit_gateway(
        self, GlobalNetworkId: str, TransitGatewayArn: str
    ) -> RegisterTransitGatewayResponseTypeDef:
        """
        [Client.register_transit_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.register_transit_gateway)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.untag_resource)
        """

    def update_device(
        self,
        GlobalNetworkId: str,
        DeviceId: str,
        Description: str = None,
        Type: str = None,
        Vendor: str = None,
        Model: str = None,
        SerialNumber: str = None,
        Location: "LocationTypeDef" = None,
        SiteId: str = None,
    ) -> UpdateDeviceResponseTypeDef:
        """
        [Client.update_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.update_device)
        """

    def update_global_network(
        self, GlobalNetworkId: str, Description: str = None
    ) -> UpdateGlobalNetworkResponseTypeDef:
        """
        [Client.update_global_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.update_global_network)
        """

    def update_link(
        self,
        GlobalNetworkId: str,
        LinkId: str,
        Description: str = None,
        Type: str = None,
        Bandwidth: "BandwidthTypeDef" = None,
        Provider: str = None,
    ) -> UpdateLinkResponseTypeDef:
        """
        [Client.update_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.update_link)
        """

    def update_site(
        self,
        GlobalNetworkId: str,
        SiteId: str,
        Description: str = None,
        Location: "LocationTypeDef" = None,
    ) -> UpdateSiteResponseTypeDef:
        """
        [Client.update_site documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Client.update_site)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_global_networks"]
    ) -> DescribeGlobalNetworksPaginator:
        """
        [Paginator.DescribeGlobalNetworks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Paginator.DescribeGlobalNetworks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_customer_gateway_associations"]
    ) -> GetCustomerGatewayAssociationsPaginator:
        """
        [Paginator.GetCustomerGatewayAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Paginator.GetCustomerGatewayAssociations)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_devices"]) -> GetDevicesPaginator:
        """
        [Paginator.GetDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Paginator.GetDevices)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_link_associations"]
    ) -> GetLinkAssociationsPaginator:
        """
        [Paginator.GetLinkAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinkAssociations)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_links"]) -> GetLinksPaginator:
        """
        [Paginator.GetLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinks)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_sites"]) -> GetSitesPaginator:
        """
        [Paginator.GetSites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Paginator.GetSites)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_registrations"]
    ) -> GetTransitGatewayRegistrationsPaginator:
        """
        [Paginator.GetTransitGatewayRegistrations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayRegistrations)
        """
