"""
Type annotations for worklink service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_worklink/type_defs.html)

Usage::

    ```python
    from mypy_boto3_worklink.type_defs import AssociateDomainRequestRequestTypeDef

    data: AssociateDomainRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import DeviceStatusType, DomainStatusType, FleetStatusType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssociateDomainRequestRequestTypeDef",
    "AssociateWebsiteAuthorizationProviderRequestRequestTypeDef",
    "AssociateWebsiteAuthorizationProviderResponseTypeDef",
    "AssociateWebsiteCertificateAuthorityRequestRequestTypeDef",
    "AssociateWebsiteCertificateAuthorityResponseTypeDef",
    "CreateFleetRequestRequestTypeDef",
    "CreateFleetResponseTypeDef",
    "DeleteFleetRequestRequestTypeDef",
    "DescribeAuditStreamConfigurationRequestRequestTypeDef",
    "DescribeAuditStreamConfigurationResponseTypeDef",
    "DescribeCompanyNetworkConfigurationRequestRequestTypeDef",
    "DescribeCompanyNetworkConfigurationResponseTypeDef",
    "DescribeDevicePolicyConfigurationRequestRequestTypeDef",
    "DescribeDevicePolicyConfigurationResponseTypeDef",
    "DescribeDeviceRequestRequestTypeDef",
    "DescribeDeviceResponseTypeDef",
    "DescribeDomainRequestRequestTypeDef",
    "DescribeDomainResponseTypeDef",
    "DescribeFleetMetadataRequestRequestTypeDef",
    "DescribeFleetMetadataResponseTypeDef",
    "DescribeIdentityProviderConfigurationRequestRequestTypeDef",
    "DescribeIdentityProviderConfigurationResponseTypeDef",
    "DescribeWebsiteCertificateAuthorityRequestRequestTypeDef",
    "DescribeWebsiteCertificateAuthorityResponseTypeDef",
    "DeviceSummaryTypeDef",
    "DisassociateDomainRequestRequestTypeDef",
    "DisassociateWebsiteAuthorizationProviderRequestRequestTypeDef",
    "DisassociateWebsiteCertificateAuthorityRequestRequestTypeDef",
    "DomainSummaryTypeDef",
    "FleetSummaryTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "ListDevicesResponseTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListDomainsResponseTypeDef",
    "ListFleetsRequestRequestTypeDef",
    "ListFleetsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWebsiteAuthorizationProvidersRequestRequestTypeDef",
    "ListWebsiteAuthorizationProvidersResponseTypeDef",
    "ListWebsiteCertificateAuthoritiesRequestRequestTypeDef",
    "ListWebsiteCertificateAuthoritiesResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreDomainAccessRequestRequestTypeDef",
    "RevokeDomainAccessRequestRequestTypeDef",
    "SignOutUserRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAuditStreamConfigurationRequestRequestTypeDef",
    "UpdateCompanyNetworkConfigurationRequestRequestTypeDef",
    "UpdateDevicePolicyConfigurationRequestRequestTypeDef",
    "UpdateDomainMetadataRequestRequestTypeDef",
    "UpdateFleetMetadataRequestRequestTypeDef",
    "UpdateIdentityProviderConfigurationRequestRequestTypeDef",
    "WebsiteAuthorizationProviderSummaryTypeDef",
    "WebsiteCaSummaryTypeDef",
)

_RequiredAssociateDomainRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateDomainRequestRequestTypeDef",
    {
        "FleetArn": str,
        "DomainName": str,
        "AcmCertificateArn": str,
    },
)
_OptionalAssociateDomainRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateDomainRequestRequestTypeDef",
    {
        "DisplayName": str,
    },
    total=False,
)

class AssociateDomainRequestRequestTypeDef(
    _RequiredAssociateDomainRequestRequestTypeDef, _OptionalAssociateDomainRequestRequestTypeDef
):
    pass

_RequiredAssociateWebsiteAuthorizationProviderRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateWebsiteAuthorizationProviderRequestRequestTypeDef",
    {
        "FleetArn": str,
        "AuthorizationProviderType": Literal["SAML"],
    },
)
_OptionalAssociateWebsiteAuthorizationProviderRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateWebsiteAuthorizationProviderRequestRequestTypeDef",
    {
        "DomainName": str,
    },
    total=False,
)

class AssociateWebsiteAuthorizationProviderRequestRequestTypeDef(
    _RequiredAssociateWebsiteAuthorizationProviderRequestRequestTypeDef,
    _OptionalAssociateWebsiteAuthorizationProviderRequestRequestTypeDef,
):
    pass

AssociateWebsiteAuthorizationProviderResponseTypeDef = TypedDict(
    "AssociateWebsiteAuthorizationProviderResponseTypeDef",
    {
        "AuthorizationProviderId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateWebsiteCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateWebsiteCertificateAuthorityRequestRequestTypeDef",
    {
        "FleetArn": str,
        "Certificate": str,
    },
)
_OptionalAssociateWebsiteCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateWebsiteCertificateAuthorityRequestRequestTypeDef",
    {
        "DisplayName": str,
    },
    total=False,
)

class AssociateWebsiteCertificateAuthorityRequestRequestTypeDef(
    _RequiredAssociateWebsiteCertificateAuthorityRequestRequestTypeDef,
    _OptionalAssociateWebsiteCertificateAuthorityRequestRequestTypeDef,
):
    pass

AssociateWebsiteCertificateAuthorityResponseTypeDef = TypedDict(
    "AssociateWebsiteCertificateAuthorityResponseTypeDef",
    {
        "WebsiteCaId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFleetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFleetRequestRequestTypeDef",
    {
        "FleetName": str,
    },
)
_OptionalCreateFleetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFleetRequestRequestTypeDef",
    {
        "DisplayName": str,
        "OptimizeForEndUserLocation": bool,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateFleetRequestRequestTypeDef(
    _RequiredCreateFleetRequestRequestTypeDef, _OptionalCreateFleetRequestRequestTypeDef
):
    pass

CreateFleetResponseTypeDef = TypedDict(
    "CreateFleetResponseTypeDef",
    {
        "FleetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFleetRequestRequestTypeDef = TypedDict(
    "DeleteFleetRequestRequestTypeDef",
    {
        "FleetArn": str,
    },
)

DescribeAuditStreamConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeAuditStreamConfigurationRequestRequestTypeDef",
    {
        "FleetArn": str,
    },
)

DescribeAuditStreamConfigurationResponseTypeDef = TypedDict(
    "DescribeAuditStreamConfigurationResponseTypeDef",
    {
        "AuditStreamArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCompanyNetworkConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeCompanyNetworkConfigurationRequestRequestTypeDef",
    {
        "FleetArn": str,
    },
)

DescribeCompanyNetworkConfigurationResponseTypeDef = TypedDict(
    "DescribeCompanyNetworkConfigurationResponseTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDevicePolicyConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeDevicePolicyConfigurationRequestRequestTypeDef",
    {
        "FleetArn": str,
    },
)

DescribeDevicePolicyConfigurationResponseTypeDef = TypedDict(
    "DescribeDevicePolicyConfigurationResponseTypeDef",
    {
        "DeviceCaCertificate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeviceRequestRequestTypeDef = TypedDict(
    "DescribeDeviceRequestRequestTypeDef",
    {
        "FleetArn": str,
        "DeviceId": str,
    },
)

DescribeDeviceResponseTypeDef = TypedDict(
    "DescribeDeviceResponseTypeDef",
    {
        "Status": DeviceStatusType,
        "Model": str,
        "Manufacturer": str,
        "OperatingSystem": str,
        "OperatingSystemVersion": str,
        "PatchLevel": str,
        "FirstAccessedTime": datetime,
        "LastAccessedTime": datetime,
        "Username": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainRequestRequestTypeDef = TypedDict(
    "DescribeDomainRequestRequestTypeDef",
    {
        "FleetArn": str,
        "DomainName": str,
    },
)

DescribeDomainResponseTypeDef = TypedDict(
    "DescribeDomainResponseTypeDef",
    {
        "DomainName": str,
        "DisplayName": str,
        "CreatedTime": datetime,
        "DomainStatus": DomainStatusType,
        "AcmCertificateArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetMetadataRequestRequestTypeDef = TypedDict(
    "DescribeFleetMetadataRequestRequestTypeDef",
    {
        "FleetArn": str,
    },
)

DescribeFleetMetadataResponseTypeDef = TypedDict(
    "DescribeFleetMetadataResponseTypeDef",
    {
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "FleetName": str,
        "DisplayName": str,
        "OptimizeForEndUserLocation": bool,
        "CompanyCode": str,
        "FleetStatus": FleetStatusType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIdentityProviderConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeIdentityProviderConfigurationRequestRequestTypeDef",
    {
        "FleetArn": str,
    },
)

DescribeIdentityProviderConfigurationResponseTypeDef = TypedDict(
    "DescribeIdentityProviderConfigurationResponseTypeDef",
    {
        "IdentityProviderType": Literal["SAML"],
        "ServiceProviderSamlMetadata": str,
        "IdentityProviderSamlMetadata": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWebsiteCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "DescribeWebsiteCertificateAuthorityRequestRequestTypeDef",
    {
        "FleetArn": str,
        "WebsiteCaId": str,
    },
)

DescribeWebsiteCertificateAuthorityResponseTypeDef = TypedDict(
    "DescribeWebsiteCertificateAuthorityResponseTypeDef",
    {
        "Certificate": str,
        "CreatedTime": datetime,
        "DisplayName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceSummaryTypeDef = TypedDict(
    "DeviceSummaryTypeDef",
    {
        "DeviceId": str,
        "DeviceStatus": DeviceStatusType,
    },
    total=False,
)

DisassociateDomainRequestRequestTypeDef = TypedDict(
    "DisassociateDomainRequestRequestTypeDef",
    {
        "FleetArn": str,
        "DomainName": str,
    },
)

DisassociateWebsiteAuthorizationProviderRequestRequestTypeDef = TypedDict(
    "DisassociateWebsiteAuthorizationProviderRequestRequestTypeDef",
    {
        "FleetArn": str,
        "AuthorizationProviderId": str,
    },
)

DisassociateWebsiteCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "DisassociateWebsiteCertificateAuthorityRequestRequestTypeDef",
    {
        "FleetArn": str,
        "WebsiteCaId": str,
    },
)

_RequiredDomainSummaryTypeDef = TypedDict(
    "_RequiredDomainSummaryTypeDef",
    {
        "DomainName": str,
        "CreatedTime": datetime,
        "DomainStatus": DomainStatusType,
    },
)
_OptionalDomainSummaryTypeDef = TypedDict(
    "_OptionalDomainSummaryTypeDef",
    {
        "DisplayName": str,
    },
    total=False,
)

class DomainSummaryTypeDef(_RequiredDomainSummaryTypeDef, _OptionalDomainSummaryTypeDef):
    pass

FleetSummaryTypeDef = TypedDict(
    "FleetSummaryTypeDef",
    {
        "FleetArn": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "FleetName": str,
        "DisplayName": str,
        "CompanyCode": str,
        "FleetStatus": FleetStatusType,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredListDevicesRequestRequestTypeDef = TypedDict(
    "_RequiredListDevicesRequestRequestTypeDef",
    {
        "FleetArn": str,
    },
)
_OptionalListDevicesRequestRequestTypeDef = TypedDict(
    "_OptionalListDevicesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListDevicesRequestRequestTypeDef(
    _RequiredListDevicesRequestRequestTypeDef, _OptionalListDevicesRequestRequestTypeDef
):
    pass

ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {
        "Devices": List["DeviceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDomainsRequestRequestTypeDef = TypedDict(
    "_RequiredListDomainsRequestRequestTypeDef",
    {
        "FleetArn": str,
    },
)
_OptionalListDomainsRequestRequestTypeDef = TypedDict(
    "_OptionalListDomainsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListDomainsRequestRequestTypeDef(
    _RequiredListDomainsRequestRequestTypeDef, _OptionalListDomainsRequestRequestTypeDef
):
    pass

ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {
        "Domains": List["DomainSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFleetsRequestRequestTypeDef = TypedDict(
    "ListFleetsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListFleetsResponseTypeDef = TypedDict(
    "ListFleetsResponseTypeDef",
    {
        "FleetSummaryList": List["FleetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWebsiteAuthorizationProvidersRequestRequestTypeDef = TypedDict(
    "_RequiredListWebsiteAuthorizationProvidersRequestRequestTypeDef",
    {
        "FleetArn": str,
    },
)
_OptionalListWebsiteAuthorizationProvidersRequestRequestTypeDef = TypedDict(
    "_OptionalListWebsiteAuthorizationProvidersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListWebsiteAuthorizationProvidersRequestRequestTypeDef(
    _RequiredListWebsiteAuthorizationProvidersRequestRequestTypeDef,
    _OptionalListWebsiteAuthorizationProvidersRequestRequestTypeDef,
):
    pass

ListWebsiteAuthorizationProvidersResponseTypeDef = TypedDict(
    "ListWebsiteAuthorizationProvidersResponseTypeDef",
    {
        "WebsiteAuthorizationProviders": List["WebsiteAuthorizationProviderSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWebsiteCertificateAuthoritiesRequestRequestTypeDef = TypedDict(
    "_RequiredListWebsiteCertificateAuthoritiesRequestRequestTypeDef",
    {
        "FleetArn": str,
    },
)
_OptionalListWebsiteCertificateAuthoritiesRequestRequestTypeDef = TypedDict(
    "_OptionalListWebsiteCertificateAuthoritiesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListWebsiteCertificateAuthoritiesRequestRequestTypeDef(
    _RequiredListWebsiteCertificateAuthoritiesRequestRequestTypeDef,
    _OptionalListWebsiteCertificateAuthoritiesRequestRequestTypeDef,
):
    pass

ListWebsiteCertificateAuthoritiesResponseTypeDef = TypedDict(
    "ListWebsiteCertificateAuthoritiesResponseTypeDef",
    {
        "WebsiteCertificateAuthorities": List["WebsiteCaSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RestoreDomainAccessRequestRequestTypeDef = TypedDict(
    "RestoreDomainAccessRequestRequestTypeDef",
    {
        "FleetArn": str,
        "DomainName": str,
    },
)

RevokeDomainAccessRequestRequestTypeDef = TypedDict(
    "RevokeDomainAccessRequestRequestTypeDef",
    {
        "FleetArn": str,
        "DomainName": str,
    },
)

SignOutUserRequestRequestTypeDef = TypedDict(
    "SignOutUserRequestRequestTypeDef",
    {
        "FleetArn": str,
        "Username": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAuditStreamConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAuditStreamConfigurationRequestRequestTypeDef",
    {
        "FleetArn": str,
    },
)
_OptionalUpdateAuditStreamConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAuditStreamConfigurationRequestRequestTypeDef",
    {
        "AuditStreamArn": str,
    },
    total=False,
)

class UpdateAuditStreamConfigurationRequestRequestTypeDef(
    _RequiredUpdateAuditStreamConfigurationRequestRequestTypeDef,
    _OptionalUpdateAuditStreamConfigurationRequestRequestTypeDef,
):
    pass

UpdateCompanyNetworkConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateCompanyNetworkConfigurationRequestRequestTypeDef",
    {
        "FleetArn": str,
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
    },
)

_RequiredUpdateDevicePolicyConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDevicePolicyConfigurationRequestRequestTypeDef",
    {
        "FleetArn": str,
    },
)
_OptionalUpdateDevicePolicyConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDevicePolicyConfigurationRequestRequestTypeDef",
    {
        "DeviceCaCertificate": str,
    },
    total=False,
)

class UpdateDevicePolicyConfigurationRequestRequestTypeDef(
    _RequiredUpdateDevicePolicyConfigurationRequestRequestTypeDef,
    _OptionalUpdateDevicePolicyConfigurationRequestRequestTypeDef,
):
    pass

_RequiredUpdateDomainMetadataRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainMetadataRequestRequestTypeDef",
    {
        "FleetArn": str,
        "DomainName": str,
    },
)
_OptionalUpdateDomainMetadataRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainMetadataRequestRequestTypeDef",
    {
        "DisplayName": str,
    },
    total=False,
)

class UpdateDomainMetadataRequestRequestTypeDef(
    _RequiredUpdateDomainMetadataRequestRequestTypeDef,
    _OptionalUpdateDomainMetadataRequestRequestTypeDef,
):
    pass

_RequiredUpdateFleetMetadataRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFleetMetadataRequestRequestTypeDef",
    {
        "FleetArn": str,
    },
)
_OptionalUpdateFleetMetadataRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFleetMetadataRequestRequestTypeDef",
    {
        "DisplayName": str,
        "OptimizeForEndUserLocation": bool,
    },
    total=False,
)

class UpdateFleetMetadataRequestRequestTypeDef(
    _RequiredUpdateFleetMetadataRequestRequestTypeDef,
    _OptionalUpdateFleetMetadataRequestRequestTypeDef,
):
    pass

_RequiredUpdateIdentityProviderConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIdentityProviderConfigurationRequestRequestTypeDef",
    {
        "FleetArn": str,
        "IdentityProviderType": Literal["SAML"],
    },
)
_OptionalUpdateIdentityProviderConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIdentityProviderConfigurationRequestRequestTypeDef",
    {
        "IdentityProviderSamlMetadata": str,
    },
    total=False,
)

class UpdateIdentityProviderConfigurationRequestRequestTypeDef(
    _RequiredUpdateIdentityProviderConfigurationRequestRequestTypeDef,
    _OptionalUpdateIdentityProviderConfigurationRequestRequestTypeDef,
):
    pass

_RequiredWebsiteAuthorizationProviderSummaryTypeDef = TypedDict(
    "_RequiredWebsiteAuthorizationProviderSummaryTypeDef",
    {
        "AuthorizationProviderType": Literal["SAML"],
    },
)
_OptionalWebsiteAuthorizationProviderSummaryTypeDef = TypedDict(
    "_OptionalWebsiteAuthorizationProviderSummaryTypeDef",
    {
        "AuthorizationProviderId": str,
        "DomainName": str,
        "CreatedTime": datetime,
    },
    total=False,
)

class WebsiteAuthorizationProviderSummaryTypeDef(
    _RequiredWebsiteAuthorizationProviderSummaryTypeDef,
    _OptionalWebsiteAuthorizationProviderSummaryTypeDef,
):
    pass

WebsiteCaSummaryTypeDef = TypedDict(
    "WebsiteCaSummaryTypeDef",
    {
        "WebsiteCaId": str,
        "CreatedTime": datetime,
        "DisplayName": str,
    },
    total=False,
)
