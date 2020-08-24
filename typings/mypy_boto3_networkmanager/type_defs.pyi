"""
Main interface for networkmanager service type definitions.

Usage::

    ```python
    from mypy_boto3_networkmanager.type_defs import BandwidthTypeDef

    data: BandwidthTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BandwidthTypeDef",
    "CustomerGatewayAssociationTypeDef",
    "DeviceTypeDef",
    "GlobalNetworkTypeDef",
    "LinkAssociationTypeDef",
    "LinkTypeDef",
    "LocationTypeDef",
    "SiteTypeDef",
    "TagTypeDef",
    "TransitGatewayRegistrationStateReasonTypeDef",
    "TransitGatewayRegistrationTypeDef",
    "AssociateCustomerGatewayResponseTypeDef",
    "AssociateLinkResponseTypeDef",
    "CreateDeviceResponseTypeDef",
    "CreateGlobalNetworkResponseTypeDef",
    "CreateLinkResponseTypeDef",
    "CreateSiteResponseTypeDef",
    "DeleteDeviceResponseTypeDef",
    "DeleteGlobalNetworkResponseTypeDef",
    "DeleteLinkResponseTypeDef",
    "DeleteSiteResponseTypeDef",
    "DeregisterTransitGatewayResponseTypeDef",
    "DescribeGlobalNetworksResponseTypeDef",
    "DisassociateCustomerGatewayResponseTypeDef",
    "DisassociateLinkResponseTypeDef",
    "GetCustomerGatewayAssociationsResponseTypeDef",
    "GetDevicesResponseTypeDef",
    "GetLinkAssociationsResponseTypeDef",
    "GetLinksResponseTypeDef",
    "GetSitesResponseTypeDef",
    "GetTransitGatewayRegistrationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterTransitGatewayResponseTypeDef",
    "UpdateDeviceResponseTypeDef",
    "UpdateGlobalNetworkResponseTypeDef",
    "UpdateLinkResponseTypeDef",
    "UpdateSiteResponseTypeDef",
)

BandwidthTypeDef = TypedDict(
    "BandwidthTypeDef", {"UploadSpeed": int, "DownloadSpeed": int}, total=False
)

CustomerGatewayAssociationTypeDef = TypedDict(
    "CustomerGatewayAssociationTypeDef",
    {
        "CustomerGatewayArn": str,
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "DELETED"],
    },
    total=False,
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "DeviceId": str,
        "DeviceArn": str,
        "GlobalNetworkId": str,
        "Description": str,
        "Type": str,
        "Vendor": str,
        "Model": str,
        "SerialNumber": str,
        "Location": "LocationTypeDef",
        "SiteId": str,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

GlobalNetworkTypeDef = TypedDict(
    "GlobalNetworkTypeDef",
    {
        "GlobalNetworkId": str,
        "GlobalNetworkArn": str,
        "Description": str,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LinkAssociationTypeDef = TypedDict(
    "LinkAssociationTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
        "LinkAssociationState": Literal["PENDING", "AVAILABLE", "DELETING", "DELETED"],
    },
    total=False,
)

LinkTypeDef = TypedDict(
    "LinkTypeDef",
    {
        "LinkId": str,
        "LinkArn": str,
        "GlobalNetworkId": str,
        "SiteId": str,
        "Description": str,
        "Type": str,
        "Bandwidth": "BandwidthTypeDef",
        "Provider": str,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LocationTypeDef = TypedDict(
    "LocationTypeDef", {"Address": str, "Latitude": str, "Longitude": str}, total=False
)

SiteTypeDef = TypedDict(
    "SiteTypeDef",
    {
        "SiteId": str,
        "SiteArn": str,
        "GlobalNetworkId": str,
        "Description": str,
        "Location": "LocationTypeDef",
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

TransitGatewayRegistrationStateReasonTypeDef = TypedDict(
    "TransitGatewayRegistrationStateReasonTypeDef",
    {"Code": Literal["PENDING", "AVAILABLE", "DELETING", "DELETED", "FAILED"], "Message": str},
    total=False,
)

TransitGatewayRegistrationTypeDef = TypedDict(
    "TransitGatewayRegistrationTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayArn": str,
        "State": "TransitGatewayRegistrationStateReasonTypeDef",
    },
    total=False,
)

AssociateCustomerGatewayResponseTypeDef = TypedDict(
    "AssociateCustomerGatewayResponseTypeDef",
    {"CustomerGatewayAssociation": "CustomerGatewayAssociationTypeDef"},
    total=False,
)

AssociateLinkResponseTypeDef = TypedDict(
    "AssociateLinkResponseTypeDef", {"LinkAssociation": "LinkAssociationTypeDef"}, total=False
)

CreateDeviceResponseTypeDef = TypedDict(
    "CreateDeviceResponseTypeDef", {"Device": "DeviceTypeDef"}, total=False
)

CreateGlobalNetworkResponseTypeDef = TypedDict(
    "CreateGlobalNetworkResponseTypeDef", {"GlobalNetwork": "GlobalNetworkTypeDef"}, total=False
)

CreateLinkResponseTypeDef = TypedDict(
    "CreateLinkResponseTypeDef", {"Link": "LinkTypeDef"}, total=False
)

CreateSiteResponseTypeDef = TypedDict(
    "CreateSiteResponseTypeDef", {"Site": "SiteTypeDef"}, total=False
)

DeleteDeviceResponseTypeDef = TypedDict(
    "DeleteDeviceResponseTypeDef", {"Device": "DeviceTypeDef"}, total=False
)

DeleteGlobalNetworkResponseTypeDef = TypedDict(
    "DeleteGlobalNetworkResponseTypeDef", {"GlobalNetwork": "GlobalNetworkTypeDef"}, total=False
)

DeleteLinkResponseTypeDef = TypedDict(
    "DeleteLinkResponseTypeDef", {"Link": "LinkTypeDef"}, total=False
)

DeleteSiteResponseTypeDef = TypedDict(
    "DeleteSiteResponseTypeDef", {"Site": "SiteTypeDef"}, total=False
)

DeregisterTransitGatewayResponseTypeDef = TypedDict(
    "DeregisterTransitGatewayResponseTypeDef",
    {"TransitGatewayRegistration": "TransitGatewayRegistrationTypeDef"},
    total=False,
)

DescribeGlobalNetworksResponseTypeDef = TypedDict(
    "DescribeGlobalNetworksResponseTypeDef",
    {"GlobalNetworks": List["GlobalNetworkTypeDef"], "NextToken": str},
    total=False,
)

DisassociateCustomerGatewayResponseTypeDef = TypedDict(
    "DisassociateCustomerGatewayResponseTypeDef",
    {"CustomerGatewayAssociation": "CustomerGatewayAssociationTypeDef"},
    total=False,
)

DisassociateLinkResponseTypeDef = TypedDict(
    "DisassociateLinkResponseTypeDef", {"LinkAssociation": "LinkAssociationTypeDef"}, total=False
)

GetCustomerGatewayAssociationsResponseTypeDef = TypedDict(
    "GetCustomerGatewayAssociationsResponseTypeDef",
    {"CustomerGatewayAssociations": List["CustomerGatewayAssociationTypeDef"], "NextToken": str},
    total=False,
)

GetDevicesResponseTypeDef = TypedDict(
    "GetDevicesResponseTypeDef", {"Devices": List["DeviceTypeDef"], "NextToken": str}, total=False
)

GetLinkAssociationsResponseTypeDef = TypedDict(
    "GetLinkAssociationsResponseTypeDef",
    {"LinkAssociations": List["LinkAssociationTypeDef"], "NextToken": str},
    total=False,
)

GetLinksResponseTypeDef = TypedDict(
    "GetLinksResponseTypeDef", {"Links": List["LinkTypeDef"], "NextToken": str}, total=False
)

GetSitesResponseTypeDef = TypedDict(
    "GetSitesResponseTypeDef", {"Sites": List["SiteTypeDef"], "NextToken": str}, total=False
)

GetTransitGatewayRegistrationsResponseTypeDef = TypedDict(
    "GetTransitGatewayRegistrationsResponseTypeDef",
    {"TransitGatewayRegistrations": List["TransitGatewayRegistrationTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"TagList": List["TagTypeDef"]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RegisterTransitGatewayResponseTypeDef = TypedDict(
    "RegisterTransitGatewayResponseTypeDef",
    {"TransitGatewayRegistration": "TransitGatewayRegistrationTypeDef"},
    total=False,
)

UpdateDeviceResponseTypeDef = TypedDict(
    "UpdateDeviceResponseTypeDef", {"Device": "DeviceTypeDef"}, total=False
)

UpdateGlobalNetworkResponseTypeDef = TypedDict(
    "UpdateGlobalNetworkResponseTypeDef", {"GlobalNetwork": "GlobalNetworkTypeDef"}, total=False
)

UpdateLinkResponseTypeDef = TypedDict(
    "UpdateLinkResponseTypeDef", {"Link": "LinkTypeDef"}, total=False
)

UpdateSiteResponseTypeDef = TypedDict(
    "UpdateSiteResponseTypeDef", {"Site": "SiteTypeDef"}, total=False
)
