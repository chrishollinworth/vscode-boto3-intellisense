"""
Type annotations for workspaces-web service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/type_defs.html)

Usage::

    ```python
    from mypy_boto3_workspaces_web.type_defs import AssociateBrowserSettingsRequestRequestTypeDef

    data: AssociateBrowserSettingsRequestRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AuthenticationTypeType,
    EnabledTypeType,
    IdentityProviderTypeType,
    InstanceTypeType,
    PortalStatusType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssociateBrowserSettingsRequestRequestTypeDef",
    "AssociateBrowserSettingsResponseTypeDef",
    "AssociateIpAccessSettingsRequestRequestTypeDef",
    "AssociateIpAccessSettingsResponseTypeDef",
    "AssociateNetworkSettingsRequestRequestTypeDef",
    "AssociateNetworkSettingsResponseTypeDef",
    "AssociateTrustStoreRequestRequestTypeDef",
    "AssociateTrustStoreResponseTypeDef",
    "AssociateUserAccessLoggingSettingsRequestRequestTypeDef",
    "AssociateUserAccessLoggingSettingsResponseTypeDef",
    "AssociateUserSettingsRequestRequestTypeDef",
    "AssociateUserSettingsResponseTypeDef",
    "BrowserSettingsSummaryTypeDef",
    "BrowserSettingsTypeDef",
    "CertificateSummaryTypeDef",
    "CertificateTypeDef",
    "CookieSpecificationTypeDef",
    "CookieSynchronizationConfigurationTypeDef",
    "CreateBrowserSettingsRequestRequestTypeDef",
    "CreateBrowserSettingsResponseTypeDef",
    "CreateIdentityProviderRequestRequestTypeDef",
    "CreateIdentityProviderResponseTypeDef",
    "CreateIpAccessSettingsRequestRequestTypeDef",
    "CreateIpAccessSettingsResponseTypeDef",
    "CreateNetworkSettingsRequestRequestTypeDef",
    "CreateNetworkSettingsResponseTypeDef",
    "CreatePortalRequestRequestTypeDef",
    "CreatePortalResponseTypeDef",
    "CreateTrustStoreRequestRequestTypeDef",
    "CreateTrustStoreResponseTypeDef",
    "CreateUserAccessLoggingSettingsRequestRequestTypeDef",
    "CreateUserAccessLoggingSettingsResponseTypeDef",
    "CreateUserSettingsRequestRequestTypeDef",
    "CreateUserSettingsResponseTypeDef",
    "DeleteBrowserSettingsRequestRequestTypeDef",
    "DeleteIdentityProviderRequestRequestTypeDef",
    "DeleteIpAccessSettingsRequestRequestTypeDef",
    "DeleteNetworkSettingsRequestRequestTypeDef",
    "DeletePortalRequestRequestTypeDef",
    "DeleteTrustStoreRequestRequestTypeDef",
    "DeleteUserAccessLoggingSettingsRequestRequestTypeDef",
    "DeleteUserSettingsRequestRequestTypeDef",
    "DisassociateBrowserSettingsRequestRequestTypeDef",
    "DisassociateIpAccessSettingsRequestRequestTypeDef",
    "DisassociateNetworkSettingsRequestRequestTypeDef",
    "DisassociateTrustStoreRequestRequestTypeDef",
    "DisassociateUserAccessLoggingSettingsRequestRequestTypeDef",
    "DisassociateUserSettingsRequestRequestTypeDef",
    "GetBrowserSettingsRequestRequestTypeDef",
    "GetBrowserSettingsResponseTypeDef",
    "GetIdentityProviderRequestRequestTypeDef",
    "GetIdentityProviderResponseTypeDef",
    "GetIpAccessSettingsRequestRequestTypeDef",
    "GetIpAccessSettingsResponseTypeDef",
    "GetNetworkSettingsRequestRequestTypeDef",
    "GetNetworkSettingsResponseTypeDef",
    "GetPortalRequestRequestTypeDef",
    "GetPortalResponseTypeDef",
    "GetPortalServiceProviderMetadataRequestRequestTypeDef",
    "GetPortalServiceProviderMetadataResponseTypeDef",
    "GetTrustStoreCertificateRequestRequestTypeDef",
    "GetTrustStoreCertificateResponseTypeDef",
    "GetTrustStoreRequestRequestTypeDef",
    "GetTrustStoreResponseTypeDef",
    "GetUserAccessLoggingSettingsRequestRequestTypeDef",
    "GetUserAccessLoggingSettingsResponseTypeDef",
    "GetUserSettingsRequestRequestTypeDef",
    "GetUserSettingsResponseTypeDef",
    "IdentityProviderSummaryTypeDef",
    "IdentityProviderTypeDef",
    "IpAccessSettingsSummaryTypeDef",
    "IpAccessSettingsTypeDef",
    "IpRuleTypeDef",
    "ListBrowserSettingsRequestRequestTypeDef",
    "ListBrowserSettingsResponseTypeDef",
    "ListIdentityProvidersRequestRequestTypeDef",
    "ListIdentityProvidersResponseTypeDef",
    "ListIpAccessSettingsRequestRequestTypeDef",
    "ListIpAccessSettingsResponseTypeDef",
    "ListNetworkSettingsRequestRequestTypeDef",
    "ListNetworkSettingsResponseTypeDef",
    "ListPortalsRequestRequestTypeDef",
    "ListPortalsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTrustStoreCertificatesRequestRequestTypeDef",
    "ListTrustStoreCertificatesResponseTypeDef",
    "ListTrustStoresRequestRequestTypeDef",
    "ListTrustStoresResponseTypeDef",
    "ListUserAccessLoggingSettingsRequestRequestTypeDef",
    "ListUserAccessLoggingSettingsResponseTypeDef",
    "ListUserSettingsRequestRequestTypeDef",
    "ListUserSettingsResponseTypeDef",
    "NetworkSettingsSummaryTypeDef",
    "NetworkSettingsTypeDef",
    "PortalSummaryTypeDef",
    "PortalTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TrustStoreSummaryTypeDef",
    "TrustStoreTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBrowserSettingsRequestRequestTypeDef",
    "UpdateBrowserSettingsResponseTypeDef",
    "UpdateIdentityProviderRequestRequestTypeDef",
    "UpdateIdentityProviderResponseTypeDef",
    "UpdateIpAccessSettingsRequestRequestTypeDef",
    "UpdateIpAccessSettingsResponseTypeDef",
    "UpdateNetworkSettingsRequestRequestTypeDef",
    "UpdateNetworkSettingsResponseTypeDef",
    "UpdatePortalRequestRequestTypeDef",
    "UpdatePortalResponseTypeDef",
    "UpdateTrustStoreRequestRequestTypeDef",
    "UpdateTrustStoreResponseTypeDef",
    "UpdateUserAccessLoggingSettingsRequestRequestTypeDef",
    "UpdateUserAccessLoggingSettingsResponseTypeDef",
    "UpdateUserSettingsRequestRequestTypeDef",
    "UpdateUserSettingsResponseTypeDef",
    "UserAccessLoggingSettingsSummaryTypeDef",
    "UserAccessLoggingSettingsTypeDef",
    "UserSettingsSummaryTypeDef",
    "UserSettingsTypeDef",
)

AssociateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "AssociateBrowserSettingsRequestRequestTypeDef",
    {
        "browserSettingsArn": str,
        "portalArn": str,
    },
)

AssociateBrowserSettingsResponseTypeDef = TypedDict(
    "AssociateBrowserSettingsResponseTypeDef",
    {
        "browserSettingsArn": str,
        "portalArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "AssociateIpAccessSettingsRequestRequestTypeDef",
    {
        "ipAccessSettingsArn": str,
        "portalArn": str,
    },
)

AssociateIpAccessSettingsResponseTypeDef = TypedDict(
    "AssociateIpAccessSettingsResponseTypeDef",
    {
        "ipAccessSettingsArn": str,
        "portalArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "AssociateNetworkSettingsRequestRequestTypeDef",
    {
        "networkSettingsArn": str,
        "portalArn": str,
    },
)

AssociateNetworkSettingsResponseTypeDef = TypedDict(
    "AssociateNetworkSettingsResponseTypeDef",
    {
        "networkSettingsArn": str,
        "portalArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateTrustStoreRequestRequestTypeDef = TypedDict(
    "AssociateTrustStoreRequestRequestTypeDef",
    {
        "portalArn": str,
        "trustStoreArn": str,
    },
)

AssociateTrustStoreResponseTypeDef = TypedDict(
    "AssociateTrustStoreResponseTypeDef",
    {
        "portalArn": str,
        "trustStoreArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "AssociateUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
        "userAccessLoggingSettingsArn": str,
    },
)

AssociateUserAccessLoggingSettingsResponseTypeDef = TypedDict(
    "AssociateUserAccessLoggingSettingsResponseTypeDef",
    {
        "portalArn": str,
        "userAccessLoggingSettingsArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateUserSettingsRequestRequestTypeDef = TypedDict(
    "AssociateUserSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
        "userSettingsArn": str,
    },
)

AssociateUserSettingsResponseTypeDef = TypedDict(
    "AssociateUserSettingsResponseTypeDef",
    {
        "portalArn": str,
        "userSettingsArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BrowserSettingsSummaryTypeDef = TypedDict(
    "BrowserSettingsSummaryTypeDef",
    {
        "browserSettingsArn": str,
    },
)

_RequiredBrowserSettingsTypeDef = TypedDict(
    "_RequiredBrowserSettingsTypeDef",
    {
        "browserSettingsArn": str,
    },
)
_OptionalBrowserSettingsTypeDef = TypedDict(
    "_OptionalBrowserSettingsTypeDef",
    {
        "additionalEncryptionContext": Dict[str, str],
        "associatedPortalArns": List[str],
        "browserPolicy": str,
        "customerManagedKey": str,
    },
    total=False,
)

class BrowserSettingsTypeDef(_RequiredBrowserSettingsTypeDef, _OptionalBrowserSettingsTypeDef):
    pass

CertificateSummaryTypeDef = TypedDict(
    "CertificateSummaryTypeDef",
    {
        "issuer": str,
        "notValidAfter": datetime,
        "notValidBefore": datetime,
        "subject": str,
        "thumbprint": str,
    },
    total=False,
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "body": bytes,
        "issuer": str,
        "notValidAfter": datetime,
        "notValidBefore": datetime,
        "subject": str,
        "thumbprint": str,
    },
    total=False,
)

_RequiredCookieSpecificationTypeDef = TypedDict(
    "_RequiredCookieSpecificationTypeDef",
    {
        "domain": str,
    },
)
_OptionalCookieSpecificationTypeDef = TypedDict(
    "_OptionalCookieSpecificationTypeDef",
    {
        "name": str,
        "path": str,
    },
    total=False,
)

class CookieSpecificationTypeDef(
    _RequiredCookieSpecificationTypeDef, _OptionalCookieSpecificationTypeDef
):
    pass

_RequiredCookieSynchronizationConfigurationTypeDef = TypedDict(
    "_RequiredCookieSynchronizationConfigurationTypeDef",
    {
        "allowlist": List["CookieSpecificationTypeDef"],
    },
)
_OptionalCookieSynchronizationConfigurationTypeDef = TypedDict(
    "_OptionalCookieSynchronizationConfigurationTypeDef",
    {
        "blocklist": List["CookieSpecificationTypeDef"],
    },
    total=False,
)

class CookieSynchronizationConfigurationTypeDef(
    _RequiredCookieSynchronizationConfigurationTypeDef,
    _OptionalCookieSynchronizationConfigurationTypeDef,
):
    pass

_RequiredCreateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBrowserSettingsRequestRequestTypeDef",
    {
        "browserPolicy": str,
    },
)
_OptionalCreateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBrowserSettingsRequestRequestTypeDef",
    {
        "additionalEncryptionContext": Dict[str, str],
        "clientToken": str,
        "customerManagedKey": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateBrowserSettingsRequestRequestTypeDef(
    _RequiredCreateBrowserSettingsRequestRequestTypeDef,
    _OptionalCreateBrowserSettingsRequestRequestTypeDef,
):
    pass

CreateBrowserSettingsResponseTypeDef = TypedDict(
    "CreateBrowserSettingsResponseTypeDef",
    {
        "browserSettingsArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIdentityProviderRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIdentityProviderRequestRequestTypeDef",
    {
        "identityProviderDetails": Dict[str, str],
        "identityProviderName": str,
        "identityProviderType": IdentityProviderTypeType,
        "portalArn": str,
    },
)
_OptionalCreateIdentityProviderRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIdentityProviderRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateIdentityProviderRequestRequestTypeDef(
    _RequiredCreateIdentityProviderRequestRequestTypeDef,
    _OptionalCreateIdentityProviderRequestRequestTypeDef,
):
    pass

CreateIdentityProviderResponseTypeDef = TypedDict(
    "CreateIdentityProviderResponseTypeDef",
    {
        "identityProviderArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIpAccessSettingsRequestRequestTypeDef",
    {
        "ipRules": List["IpRuleTypeDef"],
    },
)
_OptionalCreateIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIpAccessSettingsRequestRequestTypeDef",
    {
        "additionalEncryptionContext": Dict[str, str],
        "clientToken": str,
        "customerManagedKey": str,
        "description": str,
        "displayName": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateIpAccessSettingsRequestRequestTypeDef(
    _RequiredCreateIpAccessSettingsRequestRequestTypeDef,
    _OptionalCreateIpAccessSettingsRequestRequestTypeDef,
):
    pass

CreateIpAccessSettingsResponseTypeDef = TypedDict(
    "CreateIpAccessSettingsResponseTypeDef",
    {
        "ipAccessSettingsArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkSettingsRequestRequestTypeDef",
    {
        "securityGroupIds": List[str],
        "subnetIds": List[str],
        "vpcId": str,
    },
)
_OptionalCreateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkSettingsRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateNetworkSettingsRequestRequestTypeDef(
    _RequiredCreateNetworkSettingsRequestRequestTypeDef,
    _OptionalCreateNetworkSettingsRequestRequestTypeDef,
):
    pass

CreateNetworkSettingsResponseTypeDef = TypedDict(
    "CreateNetworkSettingsResponseTypeDef",
    {
        "networkSettingsArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePortalRequestRequestTypeDef = TypedDict(
    "CreatePortalRequestRequestTypeDef",
    {
        "additionalEncryptionContext": Dict[str, str],
        "authenticationType": AuthenticationTypeType,
        "clientToken": str,
        "customerManagedKey": str,
        "displayName": str,
        "instanceType": InstanceTypeType,
        "maxConcurrentSessions": int,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

CreatePortalResponseTypeDef = TypedDict(
    "CreatePortalResponseTypeDef",
    {
        "portalArn": str,
        "portalEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrustStoreRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrustStoreRequestRequestTypeDef",
    {
        "certificateList": List[Union[bytes, IO[bytes], StreamingBody]],
    },
)
_OptionalCreateTrustStoreRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrustStoreRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateTrustStoreRequestRequestTypeDef(
    _RequiredCreateTrustStoreRequestRequestTypeDef, _OptionalCreateTrustStoreRequestRequestTypeDef
):
    pass

CreateTrustStoreResponseTypeDef = TypedDict(
    "CreateTrustStoreResponseTypeDef",
    {
        "trustStoreArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "kinesisStreamArn": str,
    },
)
_OptionalCreateUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateUserAccessLoggingSettingsRequestRequestTypeDef(
    _RequiredCreateUserAccessLoggingSettingsRequestRequestTypeDef,
    _OptionalCreateUserAccessLoggingSettingsRequestRequestTypeDef,
):
    pass

CreateUserAccessLoggingSettingsResponseTypeDef = TypedDict(
    "CreateUserAccessLoggingSettingsResponseTypeDef",
    {
        "userAccessLoggingSettingsArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserSettingsRequestRequestTypeDef",
    {
        "copyAllowed": EnabledTypeType,
        "downloadAllowed": EnabledTypeType,
        "pasteAllowed": EnabledTypeType,
        "printAllowed": EnabledTypeType,
        "uploadAllowed": EnabledTypeType,
    },
)
_OptionalCreateUserSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserSettingsRequestRequestTypeDef",
    {
        "additionalEncryptionContext": Dict[str, str],
        "clientToken": str,
        "cookieSynchronizationConfiguration": "CookieSynchronizationConfigurationTypeDef",
        "customerManagedKey": str,
        "disconnectTimeoutInMinutes": int,
        "idleDisconnectTimeoutInMinutes": int,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateUserSettingsRequestRequestTypeDef(
    _RequiredCreateUserSettingsRequestRequestTypeDef,
    _OptionalCreateUserSettingsRequestRequestTypeDef,
):
    pass

CreateUserSettingsResponseTypeDef = TypedDict(
    "CreateUserSettingsResponseTypeDef",
    {
        "userSettingsArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBrowserSettingsRequestRequestTypeDef = TypedDict(
    "DeleteBrowserSettingsRequestRequestTypeDef",
    {
        "browserSettingsArn": str,
    },
)

DeleteIdentityProviderRequestRequestTypeDef = TypedDict(
    "DeleteIdentityProviderRequestRequestTypeDef",
    {
        "identityProviderArn": str,
    },
)

DeleteIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "DeleteIpAccessSettingsRequestRequestTypeDef",
    {
        "ipAccessSettingsArn": str,
    },
)

DeleteNetworkSettingsRequestRequestTypeDef = TypedDict(
    "DeleteNetworkSettingsRequestRequestTypeDef",
    {
        "networkSettingsArn": str,
    },
)

DeletePortalRequestRequestTypeDef = TypedDict(
    "DeletePortalRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

DeleteTrustStoreRequestRequestTypeDef = TypedDict(
    "DeleteTrustStoreRequestRequestTypeDef",
    {
        "trustStoreArn": str,
    },
)

DeleteUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "DeleteUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "userAccessLoggingSettingsArn": str,
    },
)

DeleteUserSettingsRequestRequestTypeDef = TypedDict(
    "DeleteUserSettingsRequestRequestTypeDef",
    {
        "userSettingsArn": str,
    },
)

DisassociateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateBrowserSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

DisassociateIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateIpAccessSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

DisassociateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateNetworkSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

DisassociateTrustStoreRequestRequestTypeDef = TypedDict(
    "DisassociateTrustStoreRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

DisassociateUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

DisassociateUserSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateUserSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

GetBrowserSettingsRequestRequestTypeDef = TypedDict(
    "GetBrowserSettingsRequestRequestTypeDef",
    {
        "browserSettingsArn": str,
    },
)

GetBrowserSettingsResponseTypeDef = TypedDict(
    "GetBrowserSettingsResponseTypeDef",
    {
        "browserSettings": "BrowserSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityProviderRequestRequestTypeDef = TypedDict(
    "GetIdentityProviderRequestRequestTypeDef",
    {
        "identityProviderArn": str,
    },
)

GetIdentityProviderResponseTypeDef = TypedDict(
    "GetIdentityProviderResponseTypeDef",
    {
        "identityProvider": "IdentityProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "GetIpAccessSettingsRequestRequestTypeDef",
    {
        "ipAccessSettingsArn": str,
    },
)

GetIpAccessSettingsResponseTypeDef = TypedDict(
    "GetIpAccessSettingsResponseTypeDef",
    {
        "ipAccessSettings": "IpAccessSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkSettingsRequestRequestTypeDef = TypedDict(
    "GetNetworkSettingsRequestRequestTypeDef",
    {
        "networkSettingsArn": str,
    },
)

GetNetworkSettingsResponseTypeDef = TypedDict(
    "GetNetworkSettingsResponseTypeDef",
    {
        "networkSettings": "NetworkSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPortalRequestRequestTypeDef = TypedDict(
    "GetPortalRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

GetPortalResponseTypeDef = TypedDict(
    "GetPortalResponseTypeDef",
    {
        "portal": "PortalTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPortalServiceProviderMetadataRequestRequestTypeDef = TypedDict(
    "GetPortalServiceProviderMetadataRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

GetPortalServiceProviderMetadataResponseTypeDef = TypedDict(
    "GetPortalServiceProviderMetadataResponseTypeDef",
    {
        "portalArn": str,
        "serviceProviderSamlMetadata": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrustStoreCertificateRequestRequestTypeDef = TypedDict(
    "GetTrustStoreCertificateRequestRequestTypeDef",
    {
        "thumbprint": str,
        "trustStoreArn": str,
    },
)

GetTrustStoreCertificateResponseTypeDef = TypedDict(
    "GetTrustStoreCertificateResponseTypeDef",
    {
        "certificate": "CertificateTypeDef",
        "trustStoreArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrustStoreRequestRequestTypeDef = TypedDict(
    "GetTrustStoreRequestRequestTypeDef",
    {
        "trustStoreArn": str,
    },
)

GetTrustStoreResponseTypeDef = TypedDict(
    "GetTrustStoreResponseTypeDef",
    {
        "trustStore": "TrustStoreTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "GetUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "userAccessLoggingSettingsArn": str,
    },
)

GetUserAccessLoggingSettingsResponseTypeDef = TypedDict(
    "GetUserAccessLoggingSettingsResponseTypeDef",
    {
        "userAccessLoggingSettings": "UserAccessLoggingSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserSettingsRequestRequestTypeDef = TypedDict(
    "GetUserSettingsRequestRequestTypeDef",
    {
        "userSettingsArn": str,
    },
)

GetUserSettingsResponseTypeDef = TypedDict(
    "GetUserSettingsResponseTypeDef",
    {
        "userSettings": "UserSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredIdentityProviderSummaryTypeDef = TypedDict(
    "_RequiredIdentityProviderSummaryTypeDef",
    {
        "identityProviderArn": str,
    },
)
_OptionalIdentityProviderSummaryTypeDef = TypedDict(
    "_OptionalIdentityProviderSummaryTypeDef",
    {
        "identityProviderName": str,
        "identityProviderType": IdentityProviderTypeType,
    },
    total=False,
)

class IdentityProviderSummaryTypeDef(
    _RequiredIdentityProviderSummaryTypeDef, _OptionalIdentityProviderSummaryTypeDef
):
    pass

_RequiredIdentityProviderTypeDef = TypedDict(
    "_RequiredIdentityProviderTypeDef",
    {
        "identityProviderArn": str,
    },
)
_OptionalIdentityProviderTypeDef = TypedDict(
    "_OptionalIdentityProviderTypeDef",
    {
        "identityProviderDetails": Dict[str, str],
        "identityProviderName": str,
        "identityProviderType": IdentityProviderTypeType,
    },
    total=False,
)

class IdentityProviderTypeDef(_RequiredIdentityProviderTypeDef, _OptionalIdentityProviderTypeDef):
    pass

_RequiredIpAccessSettingsSummaryTypeDef = TypedDict(
    "_RequiredIpAccessSettingsSummaryTypeDef",
    {
        "ipAccessSettingsArn": str,
    },
)
_OptionalIpAccessSettingsSummaryTypeDef = TypedDict(
    "_OptionalIpAccessSettingsSummaryTypeDef",
    {
        "creationDate": datetime,
        "description": str,
        "displayName": str,
    },
    total=False,
)

class IpAccessSettingsSummaryTypeDef(
    _RequiredIpAccessSettingsSummaryTypeDef, _OptionalIpAccessSettingsSummaryTypeDef
):
    pass

_RequiredIpAccessSettingsTypeDef = TypedDict(
    "_RequiredIpAccessSettingsTypeDef",
    {
        "ipAccessSettingsArn": str,
    },
)
_OptionalIpAccessSettingsTypeDef = TypedDict(
    "_OptionalIpAccessSettingsTypeDef",
    {
        "additionalEncryptionContext": Dict[str, str],
        "associatedPortalArns": List[str],
        "creationDate": datetime,
        "customerManagedKey": str,
        "description": str,
        "displayName": str,
        "ipRules": List["IpRuleTypeDef"],
    },
    total=False,
)

class IpAccessSettingsTypeDef(_RequiredIpAccessSettingsTypeDef, _OptionalIpAccessSettingsTypeDef):
    pass

_RequiredIpRuleTypeDef = TypedDict(
    "_RequiredIpRuleTypeDef",
    {
        "ipRange": str,
    },
)
_OptionalIpRuleTypeDef = TypedDict(
    "_OptionalIpRuleTypeDef",
    {
        "description": str,
    },
    total=False,
)

class IpRuleTypeDef(_RequiredIpRuleTypeDef, _OptionalIpRuleTypeDef):
    pass

ListBrowserSettingsRequestRequestTypeDef = TypedDict(
    "ListBrowserSettingsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListBrowserSettingsResponseTypeDef = TypedDict(
    "ListBrowserSettingsResponseTypeDef",
    {
        "browserSettings": List["BrowserSettingsSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIdentityProvidersRequestRequestTypeDef = TypedDict(
    "_RequiredListIdentityProvidersRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)
_OptionalListIdentityProvidersRequestRequestTypeDef = TypedDict(
    "_OptionalListIdentityProvidersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListIdentityProvidersRequestRequestTypeDef(
    _RequiredListIdentityProvidersRequestRequestTypeDef,
    _OptionalListIdentityProvidersRequestRequestTypeDef,
):
    pass

ListIdentityProvidersResponseTypeDef = TypedDict(
    "ListIdentityProvidersResponseTypeDef",
    {
        "identityProviders": List["IdentityProviderSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "ListIpAccessSettingsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListIpAccessSettingsResponseTypeDef = TypedDict(
    "ListIpAccessSettingsResponseTypeDef",
    {
        "ipAccessSettings": List["IpAccessSettingsSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNetworkSettingsRequestRequestTypeDef = TypedDict(
    "ListNetworkSettingsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListNetworkSettingsResponseTypeDef = TypedDict(
    "ListNetworkSettingsResponseTypeDef",
    {
        "networkSettings": List["NetworkSettingsSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPortalsRequestRequestTypeDef = TypedDict(
    "ListPortalsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListPortalsResponseTypeDef = TypedDict(
    "ListPortalsResponseTypeDef",
    {
        "nextToken": str,
        "portals": List["PortalSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTrustStoreCertificatesRequestRequestTypeDef = TypedDict(
    "_RequiredListTrustStoreCertificatesRequestRequestTypeDef",
    {
        "trustStoreArn": str,
    },
)
_OptionalListTrustStoreCertificatesRequestRequestTypeDef = TypedDict(
    "_OptionalListTrustStoreCertificatesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListTrustStoreCertificatesRequestRequestTypeDef(
    _RequiredListTrustStoreCertificatesRequestRequestTypeDef,
    _OptionalListTrustStoreCertificatesRequestRequestTypeDef,
):
    pass

ListTrustStoreCertificatesResponseTypeDef = TypedDict(
    "ListTrustStoreCertificatesResponseTypeDef",
    {
        "certificateList": List["CertificateSummaryTypeDef"],
        "nextToken": str,
        "trustStoreArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrustStoresRequestRequestTypeDef = TypedDict(
    "ListTrustStoresRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListTrustStoresResponseTypeDef = TypedDict(
    "ListTrustStoresResponseTypeDef",
    {
        "nextToken": str,
        "trustStores": List["TrustStoreSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "ListUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListUserAccessLoggingSettingsResponseTypeDef = TypedDict(
    "ListUserAccessLoggingSettingsResponseTypeDef",
    {
        "nextToken": str,
        "userAccessLoggingSettings": List["UserAccessLoggingSettingsSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserSettingsRequestRequestTypeDef = TypedDict(
    "ListUserSettingsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListUserSettingsResponseTypeDef = TypedDict(
    "ListUserSettingsResponseTypeDef",
    {
        "nextToken": str,
        "userSettings": List["UserSettingsSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredNetworkSettingsSummaryTypeDef = TypedDict(
    "_RequiredNetworkSettingsSummaryTypeDef",
    {
        "networkSettingsArn": str,
    },
)
_OptionalNetworkSettingsSummaryTypeDef = TypedDict(
    "_OptionalNetworkSettingsSummaryTypeDef",
    {
        "vpcId": str,
    },
    total=False,
)

class NetworkSettingsSummaryTypeDef(
    _RequiredNetworkSettingsSummaryTypeDef, _OptionalNetworkSettingsSummaryTypeDef
):
    pass

_RequiredNetworkSettingsTypeDef = TypedDict(
    "_RequiredNetworkSettingsTypeDef",
    {
        "networkSettingsArn": str,
    },
)
_OptionalNetworkSettingsTypeDef = TypedDict(
    "_OptionalNetworkSettingsTypeDef",
    {
        "associatedPortalArns": List[str],
        "securityGroupIds": List[str],
        "subnetIds": List[str],
        "vpcId": str,
    },
    total=False,
)

class NetworkSettingsTypeDef(_RequiredNetworkSettingsTypeDef, _OptionalNetworkSettingsTypeDef):
    pass

_RequiredPortalSummaryTypeDef = TypedDict(
    "_RequiredPortalSummaryTypeDef",
    {
        "portalArn": str,
    },
)
_OptionalPortalSummaryTypeDef = TypedDict(
    "_OptionalPortalSummaryTypeDef",
    {
        "authenticationType": AuthenticationTypeType,
        "browserSettingsArn": str,
        "browserType": Literal["Chrome"],
        "creationDate": datetime,
        "displayName": str,
        "instanceType": InstanceTypeType,
        "ipAccessSettingsArn": str,
        "maxConcurrentSessions": int,
        "networkSettingsArn": str,
        "portalEndpoint": str,
        "portalStatus": PortalStatusType,
        "rendererType": Literal["AppStream"],
        "trustStoreArn": str,
        "userAccessLoggingSettingsArn": str,
        "userSettingsArn": str,
    },
    total=False,
)

class PortalSummaryTypeDef(_RequiredPortalSummaryTypeDef, _OptionalPortalSummaryTypeDef):
    pass

_RequiredPortalTypeDef = TypedDict(
    "_RequiredPortalTypeDef",
    {
        "portalArn": str,
    },
)
_OptionalPortalTypeDef = TypedDict(
    "_OptionalPortalTypeDef",
    {
        "additionalEncryptionContext": Dict[str, str],
        "authenticationType": AuthenticationTypeType,
        "browserSettingsArn": str,
        "browserType": Literal["Chrome"],
        "creationDate": datetime,
        "customerManagedKey": str,
        "displayName": str,
        "instanceType": InstanceTypeType,
        "ipAccessSettingsArn": str,
        "maxConcurrentSessions": int,
        "networkSettingsArn": str,
        "portalEndpoint": str,
        "portalStatus": PortalStatusType,
        "rendererType": Literal["AppStream"],
        "statusReason": str,
        "trustStoreArn": str,
        "userAccessLoggingSettingsArn": str,
        "userSettingsArn": str,
    },
    total=False,
)

class PortalTypeDef(_RequiredPortalTypeDef, _OptionalPortalTypeDef):
    pass

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

_RequiredTagResourceRequestRequestTypeDef = TypedDict(
    "_RequiredTagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)
_OptionalTagResourceRequestRequestTypeDef = TypedDict(
    "_OptionalTagResourceRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class TagResourceRequestRequestTypeDef(
    _RequiredTagResourceRequestRequestTypeDef, _OptionalTagResourceRequestRequestTypeDef
):
    pass

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TrustStoreSummaryTypeDef = TypedDict(
    "TrustStoreSummaryTypeDef",
    {
        "trustStoreArn": str,
    },
    total=False,
)

_RequiredTrustStoreTypeDef = TypedDict(
    "_RequiredTrustStoreTypeDef",
    {
        "trustStoreArn": str,
    },
)
_OptionalTrustStoreTypeDef = TypedDict(
    "_OptionalTrustStoreTypeDef",
    {
        "associatedPortalArns": List[str],
    },
    total=False,
)

class TrustStoreTypeDef(_RequiredTrustStoreTypeDef, _OptionalTrustStoreTypeDef):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBrowserSettingsRequestRequestTypeDef",
    {
        "browserSettingsArn": str,
    },
)
_OptionalUpdateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBrowserSettingsRequestRequestTypeDef",
    {
        "browserPolicy": str,
        "clientToken": str,
    },
    total=False,
)

class UpdateBrowserSettingsRequestRequestTypeDef(
    _RequiredUpdateBrowserSettingsRequestRequestTypeDef,
    _OptionalUpdateBrowserSettingsRequestRequestTypeDef,
):
    pass

UpdateBrowserSettingsResponseTypeDef = TypedDict(
    "UpdateBrowserSettingsResponseTypeDef",
    {
        "browserSettings": "BrowserSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateIdentityProviderRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIdentityProviderRequestRequestTypeDef",
    {
        "identityProviderArn": str,
    },
)
_OptionalUpdateIdentityProviderRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIdentityProviderRequestRequestTypeDef",
    {
        "clientToken": str,
        "identityProviderDetails": Dict[str, str],
        "identityProviderName": str,
        "identityProviderType": IdentityProviderTypeType,
    },
    total=False,
)

class UpdateIdentityProviderRequestRequestTypeDef(
    _RequiredUpdateIdentityProviderRequestRequestTypeDef,
    _OptionalUpdateIdentityProviderRequestRequestTypeDef,
):
    pass

UpdateIdentityProviderResponseTypeDef = TypedDict(
    "UpdateIdentityProviderResponseTypeDef",
    {
        "identityProvider": "IdentityProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIpAccessSettingsRequestRequestTypeDef",
    {
        "ipAccessSettingsArn": str,
    },
)
_OptionalUpdateIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIpAccessSettingsRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "displayName": str,
        "ipRules": List["IpRuleTypeDef"],
    },
    total=False,
)

class UpdateIpAccessSettingsRequestRequestTypeDef(
    _RequiredUpdateIpAccessSettingsRequestRequestTypeDef,
    _OptionalUpdateIpAccessSettingsRequestRequestTypeDef,
):
    pass

UpdateIpAccessSettingsResponseTypeDef = TypedDict(
    "UpdateIpAccessSettingsResponseTypeDef",
    {
        "ipAccessSettings": "IpAccessSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateNetworkSettingsRequestRequestTypeDef",
    {
        "networkSettingsArn": str,
    },
)
_OptionalUpdateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateNetworkSettingsRequestRequestTypeDef",
    {
        "clientToken": str,
        "securityGroupIds": List[str],
        "subnetIds": List[str],
        "vpcId": str,
    },
    total=False,
)

class UpdateNetworkSettingsRequestRequestTypeDef(
    _RequiredUpdateNetworkSettingsRequestRequestTypeDef,
    _OptionalUpdateNetworkSettingsRequestRequestTypeDef,
):
    pass

UpdateNetworkSettingsResponseTypeDef = TypedDict(
    "UpdateNetworkSettingsResponseTypeDef",
    {
        "networkSettings": "NetworkSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePortalRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePortalRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)
_OptionalUpdatePortalRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePortalRequestRequestTypeDef",
    {
        "authenticationType": AuthenticationTypeType,
        "displayName": str,
        "instanceType": InstanceTypeType,
        "maxConcurrentSessions": int,
    },
    total=False,
)

class UpdatePortalRequestRequestTypeDef(
    _RequiredUpdatePortalRequestRequestTypeDef, _OptionalUpdatePortalRequestRequestTypeDef
):
    pass

UpdatePortalResponseTypeDef = TypedDict(
    "UpdatePortalResponseTypeDef",
    {
        "portal": "PortalTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTrustStoreRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTrustStoreRequestRequestTypeDef",
    {
        "trustStoreArn": str,
    },
)
_OptionalUpdateTrustStoreRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTrustStoreRequestRequestTypeDef",
    {
        "certificatesToAdd": List[Union[bytes, IO[bytes], StreamingBody]],
        "certificatesToDelete": List[str],
        "clientToken": str,
    },
    total=False,
)

class UpdateTrustStoreRequestRequestTypeDef(
    _RequiredUpdateTrustStoreRequestRequestTypeDef, _OptionalUpdateTrustStoreRequestRequestTypeDef
):
    pass

UpdateTrustStoreResponseTypeDef = TypedDict(
    "UpdateTrustStoreResponseTypeDef",
    {
        "trustStoreArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "userAccessLoggingSettingsArn": str,
    },
)
_OptionalUpdateUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "clientToken": str,
        "kinesisStreamArn": str,
    },
    total=False,
)

class UpdateUserAccessLoggingSettingsRequestRequestTypeDef(
    _RequiredUpdateUserAccessLoggingSettingsRequestRequestTypeDef,
    _OptionalUpdateUserAccessLoggingSettingsRequestRequestTypeDef,
):
    pass

UpdateUserAccessLoggingSettingsResponseTypeDef = TypedDict(
    "UpdateUserAccessLoggingSettingsResponseTypeDef",
    {
        "userAccessLoggingSettings": "UserAccessLoggingSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserSettingsRequestRequestTypeDef",
    {
        "userSettingsArn": str,
    },
)
_OptionalUpdateUserSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserSettingsRequestRequestTypeDef",
    {
        "clientToken": str,
        "cookieSynchronizationConfiguration": "CookieSynchronizationConfigurationTypeDef",
        "copyAllowed": EnabledTypeType,
        "disconnectTimeoutInMinutes": int,
        "downloadAllowed": EnabledTypeType,
        "idleDisconnectTimeoutInMinutes": int,
        "pasteAllowed": EnabledTypeType,
        "printAllowed": EnabledTypeType,
        "uploadAllowed": EnabledTypeType,
    },
    total=False,
)

class UpdateUserSettingsRequestRequestTypeDef(
    _RequiredUpdateUserSettingsRequestRequestTypeDef,
    _OptionalUpdateUserSettingsRequestRequestTypeDef,
):
    pass

UpdateUserSettingsResponseTypeDef = TypedDict(
    "UpdateUserSettingsResponseTypeDef",
    {
        "userSettings": "UserSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUserAccessLoggingSettingsSummaryTypeDef = TypedDict(
    "_RequiredUserAccessLoggingSettingsSummaryTypeDef",
    {
        "userAccessLoggingSettingsArn": str,
    },
)
_OptionalUserAccessLoggingSettingsSummaryTypeDef = TypedDict(
    "_OptionalUserAccessLoggingSettingsSummaryTypeDef",
    {
        "kinesisStreamArn": str,
    },
    total=False,
)

class UserAccessLoggingSettingsSummaryTypeDef(
    _RequiredUserAccessLoggingSettingsSummaryTypeDef,
    _OptionalUserAccessLoggingSettingsSummaryTypeDef,
):
    pass

_RequiredUserAccessLoggingSettingsTypeDef = TypedDict(
    "_RequiredUserAccessLoggingSettingsTypeDef",
    {
        "userAccessLoggingSettingsArn": str,
    },
)
_OptionalUserAccessLoggingSettingsTypeDef = TypedDict(
    "_OptionalUserAccessLoggingSettingsTypeDef",
    {
        "associatedPortalArns": List[str],
        "kinesisStreamArn": str,
    },
    total=False,
)

class UserAccessLoggingSettingsTypeDef(
    _RequiredUserAccessLoggingSettingsTypeDef, _OptionalUserAccessLoggingSettingsTypeDef
):
    pass

_RequiredUserSettingsSummaryTypeDef = TypedDict(
    "_RequiredUserSettingsSummaryTypeDef",
    {
        "userSettingsArn": str,
    },
)
_OptionalUserSettingsSummaryTypeDef = TypedDict(
    "_OptionalUserSettingsSummaryTypeDef",
    {
        "cookieSynchronizationConfiguration": "CookieSynchronizationConfigurationTypeDef",
        "copyAllowed": EnabledTypeType,
        "disconnectTimeoutInMinutes": int,
        "downloadAllowed": EnabledTypeType,
        "idleDisconnectTimeoutInMinutes": int,
        "pasteAllowed": EnabledTypeType,
        "printAllowed": EnabledTypeType,
        "uploadAllowed": EnabledTypeType,
    },
    total=False,
)

class UserSettingsSummaryTypeDef(
    _RequiredUserSettingsSummaryTypeDef, _OptionalUserSettingsSummaryTypeDef
):
    pass

_RequiredUserSettingsTypeDef = TypedDict(
    "_RequiredUserSettingsTypeDef",
    {
        "userSettingsArn": str,
    },
)
_OptionalUserSettingsTypeDef = TypedDict(
    "_OptionalUserSettingsTypeDef",
    {
        "additionalEncryptionContext": Dict[str, str],
        "associatedPortalArns": List[str],
        "cookieSynchronizationConfiguration": "CookieSynchronizationConfigurationTypeDef",
        "copyAllowed": EnabledTypeType,
        "customerManagedKey": str,
        "disconnectTimeoutInMinutes": int,
        "downloadAllowed": EnabledTypeType,
        "idleDisconnectTimeoutInMinutes": int,
        "pasteAllowed": EnabledTypeType,
        "printAllowed": EnabledTypeType,
        "uploadAllowed": EnabledTypeType,
    },
    total=False,
)

class UserSettingsTypeDef(_RequiredUserSettingsTypeDef, _OptionalUserSettingsTypeDef):
    pass
