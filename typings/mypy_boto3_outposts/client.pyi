"""
Type annotations for outposts service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_outposts import OutpostsClient

    client: OutpostsClient = boto3.client("outposts")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AddressTypeType,
    AssetStateType,
    CatalogItemClassType,
    FiberOpticCableTypeType,
    MaximumSupportedWeightLbsType,
    OpticalStandardType,
    PaymentOptionType,
    PaymentTermType,
    PowerConnectorType,
    PowerDrawKvaType,
    PowerFeedDropType,
    PowerPhaseType,
    SupportedHardwareTypeType,
    SupportedStorageEnumType,
    UplinkCountType,
    UplinkGbpsType,
)
from .type_defs import (
    AddressTypeDef,
    CreateOrderOutputTypeDef,
    CreateOutpostOutputTypeDef,
    CreateSiteOutputTypeDef,
    GetCatalogItemOutputTypeDef,
    GetConnectionResponseTypeDef,
    GetOrderOutputTypeDef,
    GetOutpostInstanceTypesOutputTypeDef,
    GetOutpostOutputTypeDef,
    GetSiteAddressOutputTypeDef,
    GetSiteOutputTypeDef,
    LineItemRequestTypeDef,
    ListAssetsOutputTypeDef,
    ListCatalogItemsOutputTypeDef,
    ListOrdersOutputTypeDef,
    ListOutpostsOutputTypeDef,
    ListSitesOutputTypeDef,
    ListTagsForResourceResponseTypeDef,
    RackPhysicalPropertiesTypeDef,
    StartConnectionResponseTypeDef,
    UpdateOutpostOutputTypeDef,
    UpdateSiteAddressOutputTypeDef,
    UpdateSiteOutputTypeDef,
    UpdateSiteRackPhysicalPropertiesOutputTypeDef,
)

__all__ = ("OutpostsClient",)

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
    NotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class OutpostsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        OutpostsClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#can_paginate)
        """
    def cancel_order(self, *, OrderId: str) -> Dict[str, Any]:
        """
        Cancels the specified order for an Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.cancel_order)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#cancel_order)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#close)
        """
    def create_order(
        self,
        *,
        OutpostIdentifier: str,
        LineItems: List["LineItemRequestTypeDef"],
        PaymentOption: PaymentOptionType,
        PaymentTerm: PaymentTermType = None
    ) -> CreateOrderOutputTypeDef:
        """
        Creates an order for an Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.create_order)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#create_order)
        """
    def create_outpost(
        self,
        *,
        Name: str,
        SiteId: str,
        Description: str = None,
        AvailabilityZone: str = None,
        AvailabilityZoneId: str = None,
        Tags: Dict[str, str] = None,
        SupportedHardwareType: SupportedHardwareTypeType = None
    ) -> CreateOutpostOutputTypeDef:
        """
        Creates an Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.create_outpost)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#create_outpost)
        """
    def create_site(
        self,
        *,
        Name: str,
        Description: str = None,
        Notes: str = None,
        Tags: Dict[str, str] = None,
        OperatingAddress: "AddressTypeDef" = None,
        ShippingAddress: "AddressTypeDef" = None,
        RackPhysicalProperties: "RackPhysicalPropertiesTypeDef" = None
    ) -> CreateSiteOutputTypeDef:
        """
        Creates a site for an Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.create_site)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#create_site)
        """
    def delete_outpost(self, *, OutpostId: str) -> Dict[str, Any]:
        """
        Deletes the specified Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.delete_outpost)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#delete_outpost)
        """
    def delete_site(self, *, SiteId: str) -> Dict[str, Any]:
        """
        Deletes the specified site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.delete_site)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#delete_site)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#generate_presigned_url)
        """
    def get_catalog_item(self, *, CatalogItemId: str) -> GetCatalogItemOutputTypeDef:
        """
        Gets information about the specified catalog item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.get_catalog_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#get_catalog_item)
        """
    def get_connection(self, *, ConnectionId: str) -> GetConnectionResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.get_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#get_connection)
        """
    def get_order(self, *, OrderId: str) -> GetOrderOutputTypeDef:
        """
        Gets information about the specified order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.get_order)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#get_order)
        """
    def get_outpost(self, *, OutpostId: str) -> GetOutpostOutputTypeDef:
        """
        Gets information about the specified Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.get_outpost)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#get_outpost)
        """
    def get_outpost_instance_types(
        self, *, OutpostId: str, NextToken: str = None, MaxResults: int = None
    ) -> GetOutpostInstanceTypesOutputTypeDef:
        """
        Gets the instance types for the specified Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.get_outpost_instance_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#get_outpost_instance_types)
        """
    def get_site(self, *, SiteId: str) -> GetSiteOutputTypeDef:
        """
        Gets information about the specified Outpost site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.get_site)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#get_site)
        """
    def get_site_address(
        self, *, SiteId: str, AddressType: AddressTypeType
    ) -> GetSiteAddressOutputTypeDef:
        """
        Gets the site address of the specified site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.get_site_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#get_site_address)
        """
    def list_assets(
        self,
        *,
        OutpostIdentifier: str,
        HostIdFilter: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        StatusFilter: List[AssetStateType] = None
    ) -> ListAssetsOutputTypeDef:
        """
        Lists the hardware assets for the specified Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.list_assets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#list_assets)
        """
    def list_catalog_items(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        ItemClassFilter: List[CatalogItemClassType] = None,
        SupportedStorageFilter: List[SupportedStorageEnumType] = None,
        EC2FamilyFilter: List[str] = None
    ) -> ListCatalogItemsOutputTypeDef:
        """
        Lists the items in the catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.list_catalog_items)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#list_catalog_items)
        """
    def list_orders(
        self, *, OutpostIdentifierFilter: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListOrdersOutputTypeDef:
        """
        Lists the Outpost orders for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.list_orders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#list_orders)
        """
    def list_outposts(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        LifeCycleStatusFilter: List[str] = None,
        AvailabilityZoneFilter: List[str] = None,
        AvailabilityZoneIdFilter: List[str] = None
    ) -> ListOutpostsOutputTypeDef:
        """
        Lists the Outposts for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.list_outposts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#list_outposts)
        """
    def list_sites(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        OperatingAddressCountryCodeFilter: List[str] = None,
        OperatingAddressStateOrRegionFilter: List[str] = None,
        OperatingAddressCityFilter: List[str] = None
    ) -> ListSitesOutputTypeDef:
        """
        Lists the Outpost sites for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.list_sites)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#list_sites)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#list_tags_for_resource)
        """
    def start_connection(
        self,
        *,
        DeviceSerialNumber: str,
        AssetId: str,
        ClientPublicKey: str,
        NetworkInterfaceDeviceIndex: int
    ) -> StartConnectionResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.start_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#start_connection)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#untag_resource)
        """
    def update_outpost(
        self,
        *,
        OutpostId: str,
        Name: str = None,
        Description: str = None,
        SupportedHardwareType: SupportedHardwareTypeType = None
    ) -> UpdateOutpostOutputTypeDef:
        """
        Updates an Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.update_outpost)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#update_outpost)
        """
    def update_site(
        self, *, SiteId: str, Name: str = None, Description: str = None, Notes: str = None
    ) -> UpdateSiteOutputTypeDef:
        """
        Updates the specified site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.update_site)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#update_site)
        """
    def update_site_address(
        self, *, SiteId: str, AddressType: AddressTypeType, Address: "AddressTypeDef"
    ) -> UpdateSiteAddressOutputTypeDef:
        """
        Updates the address of the specified site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.update_site_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#update_site_address)
        """
    def update_site_rack_physical_properties(
        self,
        *,
        SiteId: str,
        PowerDrawKva: PowerDrawKvaType = None,
        PowerPhase: PowerPhaseType = None,
        PowerConnector: PowerConnectorType = None,
        PowerFeedDrop: PowerFeedDropType = None,
        UplinkGbps: UplinkGbpsType = None,
        UplinkCount: UplinkCountType = None,
        FiberOpticCableType: FiberOpticCableTypeType = None,
        OpticalStandard: OpticalStandardType = None,
        MaximumSupportedWeightLbs: MaximumSupportedWeightLbsType = None
    ) -> UpdateSiteRackPhysicalPropertiesOutputTypeDef:
        """
        Update the physical and logistical details for a rack at a site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/outposts.html#Outposts.Client.update_site_rack_physical_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#update_site_rack_physical_properties)
        """
