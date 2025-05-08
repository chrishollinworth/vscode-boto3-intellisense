"""
Type annotations for workspaces-web service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_workspaces_web.type_defs import AssociateBrowserSettingsRequestTypeDef

    data: AssociateBrowserSettingsRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    AuthenticationTypeType,
    EnabledTypeType,
    IdentityProviderTypeType,
    InstanceTypeType,
    MaxDisplayResolutionType,
    PortalStatusType,
    SessionSortByType,
    SessionStatusType,
    ToolbarItemType,
    ToolbarTypeType,
    VisualModeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AssociateBrowserSettingsRequestTypeDef",
    "AssociateBrowserSettingsResponseTypeDef",
    "AssociateDataProtectionSettingsRequestTypeDef",
    "AssociateDataProtectionSettingsResponseTypeDef",
    "AssociateIpAccessSettingsRequestTypeDef",
    "AssociateIpAccessSettingsResponseTypeDef",
    "AssociateNetworkSettingsRequestTypeDef",
    "AssociateNetworkSettingsResponseTypeDef",
    "AssociateTrustStoreRequestTypeDef",
    "AssociateTrustStoreResponseTypeDef",
    "AssociateUserAccessLoggingSettingsRequestTypeDef",
    "AssociateUserAccessLoggingSettingsResponseTypeDef",
    "AssociateUserSettingsRequestTypeDef",
    "AssociateUserSettingsResponseTypeDef",
    "BlobTypeDef",
    "BrowserSettingsSummaryTypeDef",
    "BrowserSettingsTypeDef",
    "CertificateSummaryTypeDef",
    "CertificateTypeDef",
    "CookieSpecificationTypeDef",
    "CookieSynchronizationConfigurationOutputTypeDef",
    "CookieSynchronizationConfigurationTypeDef",
    "CookieSynchronizationConfigurationUnionTypeDef",
    "CreateBrowserSettingsRequestTypeDef",
    "CreateBrowserSettingsResponseTypeDef",
    "CreateDataProtectionSettingsRequestTypeDef",
    "CreateDataProtectionSettingsResponseTypeDef",
    "CreateIdentityProviderRequestTypeDef",
    "CreateIdentityProviderResponseTypeDef",
    "CreateIpAccessSettingsRequestTypeDef",
    "CreateIpAccessSettingsResponseTypeDef",
    "CreateNetworkSettingsRequestTypeDef",
    "CreateNetworkSettingsResponseTypeDef",
    "CreatePortalRequestTypeDef",
    "CreatePortalResponseTypeDef",
    "CreateTrustStoreRequestTypeDef",
    "CreateTrustStoreResponseTypeDef",
    "CreateUserAccessLoggingSettingsRequestTypeDef",
    "CreateUserAccessLoggingSettingsResponseTypeDef",
    "CreateUserSettingsRequestTypeDef",
    "CreateUserSettingsResponseTypeDef",
    "CustomPatternTypeDef",
    "DataProtectionSettingsSummaryTypeDef",
    "DataProtectionSettingsTypeDef",
    "DeleteBrowserSettingsRequestTypeDef",
    "DeleteDataProtectionSettingsRequestTypeDef",
    "DeleteIdentityProviderRequestTypeDef",
    "DeleteIpAccessSettingsRequestTypeDef",
    "DeleteNetworkSettingsRequestTypeDef",
    "DeletePortalRequestTypeDef",
    "DeleteTrustStoreRequestTypeDef",
    "DeleteUserAccessLoggingSettingsRequestTypeDef",
    "DeleteUserSettingsRequestTypeDef",
    "DisassociateBrowserSettingsRequestTypeDef",
    "DisassociateDataProtectionSettingsRequestTypeDef",
    "DisassociateIpAccessSettingsRequestTypeDef",
    "DisassociateNetworkSettingsRequestTypeDef",
    "DisassociateTrustStoreRequestTypeDef",
    "DisassociateUserAccessLoggingSettingsRequestTypeDef",
    "DisassociateUserSettingsRequestTypeDef",
    "ExpireSessionRequestTypeDef",
    "GetBrowserSettingsRequestTypeDef",
    "GetBrowserSettingsResponseTypeDef",
    "GetDataProtectionSettingsRequestTypeDef",
    "GetDataProtectionSettingsResponseTypeDef",
    "GetIdentityProviderRequestTypeDef",
    "GetIdentityProviderResponseTypeDef",
    "GetIpAccessSettingsRequestTypeDef",
    "GetIpAccessSettingsResponseTypeDef",
    "GetNetworkSettingsRequestTypeDef",
    "GetNetworkSettingsResponseTypeDef",
    "GetPortalRequestTypeDef",
    "GetPortalResponseTypeDef",
    "GetPortalServiceProviderMetadataRequestTypeDef",
    "GetPortalServiceProviderMetadataResponseTypeDef",
    "GetSessionRequestTypeDef",
    "GetSessionResponseTypeDef",
    "GetTrustStoreCertificateRequestTypeDef",
    "GetTrustStoreCertificateResponseTypeDef",
    "GetTrustStoreRequestTypeDef",
    "GetTrustStoreResponseTypeDef",
    "GetUserAccessLoggingSettingsRequestTypeDef",
    "GetUserAccessLoggingSettingsResponseTypeDef",
    "GetUserSettingsRequestTypeDef",
    "GetUserSettingsResponseTypeDef",
    "IdentityProviderSummaryTypeDef",
    "IdentityProviderTypeDef",
    "InlineRedactionConfigurationOutputTypeDef",
    "InlineRedactionConfigurationTypeDef",
    "InlineRedactionConfigurationUnionTypeDef",
    "InlineRedactionPatternOutputTypeDef",
    "InlineRedactionPatternTypeDef",
    "IpAccessSettingsSummaryTypeDef",
    "IpAccessSettingsTypeDef",
    "IpRuleTypeDef",
    "ListBrowserSettingsRequestTypeDef",
    "ListBrowserSettingsResponseTypeDef",
    "ListDataProtectionSettingsRequestPaginateTypeDef",
    "ListDataProtectionSettingsRequestTypeDef",
    "ListDataProtectionSettingsResponseTypeDef",
    "ListIdentityProvidersRequestTypeDef",
    "ListIdentityProvidersResponseTypeDef",
    "ListIpAccessSettingsRequestTypeDef",
    "ListIpAccessSettingsResponseTypeDef",
    "ListNetworkSettingsRequestTypeDef",
    "ListNetworkSettingsResponseTypeDef",
    "ListPortalsRequestTypeDef",
    "ListPortalsResponseTypeDef",
    "ListSessionsRequestPaginateTypeDef",
    "ListSessionsRequestTypeDef",
    "ListSessionsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTrustStoreCertificatesRequestTypeDef",
    "ListTrustStoreCertificatesResponseTypeDef",
    "ListTrustStoresRequestTypeDef",
    "ListTrustStoresResponseTypeDef",
    "ListUserAccessLoggingSettingsRequestTypeDef",
    "ListUserAccessLoggingSettingsResponseTypeDef",
    "ListUserSettingsRequestTypeDef",
    "ListUserSettingsResponseTypeDef",
    "NetworkSettingsSummaryTypeDef",
    "NetworkSettingsTypeDef",
    "PaginatorConfigTypeDef",
    "PortalSummaryTypeDef",
    "PortalTypeDef",
    "RedactionPlaceHolderTypeDef",
    "ResponseMetadataTypeDef",
    "SessionSummaryTypeDef",
    "SessionTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "ToolbarConfigurationOutputTypeDef",
    "ToolbarConfigurationTypeDef",
    "ToolbarConfigurationUnionTypeDef",
    "TrustStoreSummaryTypeDef",
    "TrustStoreTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateBrowserSettingsRequestTypeDef",
    "UpdateBrowserSettingsResponseTypeDef",
    "UpdateDataProtectionSettingsRequestTypeDef",
    "UpdateDataProtectionSettingsResponseTypeDef",
    "UpdateIdentityProviderRequestTypeDef",
    "UpdateIdentityProviderResponseTypeDef",
    "UpdateIpAccessSettingsRequestTypeDef",
    "UpdateIpAccessSettingsResponseTypeDef",
    "UpdateNetworkSettingsRequestTypeDef",
    "UpdateNetworkSettingsResponseTypeDef",
    "UpdatePortalRequestTypeDef",
    "UpdatePortalResponseTypeDef",
    "UpdateTrustStoreRequestTypeDef",
    "UpdateTrustStoreResponseTypeDef",
    "UpdateUserAccessLoggingSettingsRequestTypeDef",
    "UpdateUserAccessLoggingSettingsResponseTypeDef",
    "UpdateUserSettingsRequestTypeDef",
    "UpdateUserSettingsResponseTypeDef",
    "UserAccessLoggingSettingsSummaryTypeDef",
    "UserAccessLoggingSettingsTypeDef",
    "UserSettingsSummaryTypeDef",
    "UserSettingsTypeDef",
)

class AssociateBrowserSettingsRequestTypeDef(TypedDict):
    browserSettingsArn: str
    portalArn: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AssociateDataProtectionSettingsRequestTypeDef(TypedDict):
    dataProtectionSettingsArn: str
    portalArn: str

class AssociateIpAccessSettingsRequestTypeDef(TypedDict):
    ipAccessSettingsArn: str
    portalArn: str

class AssociateNetworkSettingsRequestTypeDef(TypedDict):
    networkSettingsArn: str
    portalArn: str

class AssociateTrustStoreRequestTypeDef(TypedDict):
    portalArn: str
    trustStoreArn: str

class AssociateUserAccessLoggingSettingsRequestTypeDef(TypedDict):
    portalArn: str
    userAccessLoggingSettingsArn: str

class AssociateUserSettingsRequestTypeDef(TypedDict):
    portalArn: str
    userSettingsArn: str

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class BrowserSettingsSummaryTypeDef(TypedDict):
    browserSettingsArn: str

class BrowserSettingsTypeDef(TypedDict):
    browserSettingsArn: str
    additionalEncryptionContext: NotRequired[Dict[str, str]]
    associatedPortalArns: NotRequired[List[str]]
    browserPolicy: NotRequired[str]
    customerManagedKey: NotRequired[str]

class CertificateSummaryTypeDef(TypedDict):
    issuer: NotRequired[str]
    notValidAfter: NotRequired[datetime]
    notValidBefore: NotRequired[datetime]
    subject: NotRequired[str]
    thumbprint: NotRequired[str]

class CertificateTypeDef(TypedDict):
    body: NotRequired[bytes]
    issuer: NotRequired[str]
    notValidAfter: NotRequired[datetime]
    notValidBefore: NotRequired[datetime]
    subject: NotRequired[str]
    thumbprint: NotRequired[str]

class CookieSpecificationTypeDef(TypedDict):
    domain: str
    name: NotRequired[str]
    path: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class IpRuleTypeDef(TypedDict):
    ipRange: str
    description: NotRequired[str]

class CustomPatternTypeDef(TypedDict):
    patternName: str
    patternRegex: str
    keywordRegex: NotRequired[str]
    patternDescription: NotRequired[str]

class DataProtectionSettingsSummaryTypeDef(TypedDict):
    dataProtectionSettingsArn: str
    creationDate: NotRequired[datetime]
    description: NotRequired[str]
    displayName: NotRequired[str]

class DeleteBrowserSettingsRequestTypeDef(TypedDict):
    browserSettingsArn: str

class DeleteDataProtectionSettingsRequestTypeDef(TypedDict):
    dataProtectionSettingsArn: str

class DeleteIdentityProviderRequestTypeDef(TypedDict):
    identityProviderArn: str

class DeleteIpAccessSettingsRequestTypeDef(TypedDict):
    ipAccessSettingsArn: str

class DeleteNetworkSettingsRequestTypeDef(TypedDict):
    networkSettingsArn: str

class DeletePortalRequestTypeDef(TypedDict):
    portalArn: str

class DeleteTrustStoreRequestTypeDef(TypedDict):
    trustStoreArn: str

class DeleteUserAccessLoggingSettingsRequestTypeDef(TypedDict):
    userAccessLoggingSettingsArn: str

class DeleteUserSettingsRequestTypeDef(TypedDict):
    userSettingsArn: str

class DisassociateBrowserSettingsRequestTypeDef(TypedDict):
    portalArn: str

class DisassociateDataProtectionSettingsRequestTypeDef(TypedDict):
    portalArn: str

class DisassociateIpAccessSettingsRequestTypeDef(TypedDict):
    portalArn: str

class DisassociateNetworkSettingsRequestTypeDef(TypedDict):
    portalArn: str

class DisassociateTrustStoreRequestTypeDef(TypedDict):
    portalArn: str

class DisassociateUserAccessLoggingSettingsRequestTypeDef(TypedDict):
    portalArn: str

class DisassociateUserSettingsRequestTypeDef(TypedDict):
    portalArn: str

class ExpireSessionRequestTypeDef(TypedDict):
    portalId: str
    sessionId: str

class GetBrowserSettingsRequestTypeDef(TypedDict):
    browserSettingsArn: str

class GetDataProtectionSettingsRequestTypeDef(TypedDict):
    dataProtectionSettingsArn: str

class GetIdentityProviderRequestTypeDef(TypedDict):
    identityProviderArn: str

class IdentityProviderTypeDef(TypedDict):
    identityProviderArn: str
    identityProviderDetails: NotRequired[Dict[str, str]]
    identityProviderName: NotRequired[str]
    identityProviderType: NotRequired[IdentityProviderTypeType]

class GetIpAccessSettingsRequestTypeDef(TypedDict):
    ipAccessSettingsArn: str

class GetNetworkSettingsRequestTypeDef(TypedDict):
    networkSettingsArn: str

class NetworkSettingsTypeDef(TypedDict):
    networkSettingsArn: str
    associatedPortalArns: NotRequired[List[str]]
    securityGroupIds: NotRequired[List[str]]
    subnetIds: NotRequired[List[str]]
    vpcId: NotRequired[str]

class GetPortalRequestTypeDef(TypedDict):
    portalArn: str

class PortalTypeDef(TypedDict):
    portalArn: str
    additionalEncryptionContext: NotRequired[Dict[str, str]]
    authenticationType: NotRequired[AuthenticationTypeType]
    browserSettingsArn: NotRequired[str]
    browserType: NotRequired[Literal["Chrome"]]
    creationDate: NotRequired[datetime]
    customerManagedKey: NotRequired[str]
    dataProtectionSettingsArn: NotRequired[str]
    displayName: NotRequired[str]
    instanceType: NotRequired[InstanceTypeType]
    ipAccessSettingsArn: NotRequired[str]
    maxConcurrentSessions: NotRequired[int]
    networkSettingsArn: NotRequired[str]
    portalEndpoint: NotRequired[str]
    portalStatus: NotRequired[PortalStatusType]
    rendererType: NotRequired[Literal["AppStream"]]
    statusReason: NotRequired[str]
    trustStoreArn: NotRequired[str]
    userAccessLoggingSettingsArn: NotRequired[str]
    userSettingsArn: NotRequired[str]

class GetPortalServiceProviderMetadataRequestTypeDef(TypedDict):
    portalArn: str

class GetSessionRequestTypeDef(TypedDict):
    portalId: str
    sessionId: str

class SessionTypeDef(TypedDict):
    clientIpAddresses: NotRequired[List[str]]
    endTime: NotRequired[datetime]
    portalArn: NotRequired[str]
    sessionId: NotRequired[str]
    startTime: NotRequired[datetime]
    status: NotRequired[SessionStatusType]
    username: NotRequired[str]

class GetTrustStoreCertificateRequestTypeDef(TypedDict):
    thumbprint: str
    trustStoreArn: str

class GetTrustStoreRequestTypeDef(TypedDict):
    trustStoreArn: str

class TrustStoreTypeDef(TypedDict):
    trustStoreArn: str
    associatedPortalArns: NotRequired[List[str]]

class GetUserAccessLoggingSettingsRequestTypeDef(TypedDict):
    userAccessLoggingSettingsArn: str

class UserAccessLoggingSettingsTypeDef(TypedDict):
    userAccessLoggingSettingsArn: str
    associatedPortalArns: NotRequired[List[str]]
    kinesisStreamArn: NotRequired[str]

class GetUserSettingsRequestTypeDef(TypedDict):
    userSettingsArn: str

class IdentityProviderSummaryTypeDef(TypedDict):
    identityProviderArn: str
    identityProviderName: NotRequired[str]
    identityProviderType: NotRequired[IdentityProviderTypeType]

class RedactionPlaceHolderTypeDef(TypedDict):
    redactionPlaceHolderType: Literal["CustomText"]
    redactionPlaceHolderText: NotRequired[str]

class IpAccessSettingsSummaryTypeDef(TypedDict):
    ipAccessSettingsArn: str
    creationDate: NotRequired[datetime]
    description: NotRequired[str]
    displayName: NotRequired[str]

class ListBrowserSettingsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListDataProtectionSettingsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListIdentityProvidersRequestTypeDef(TypedDict):
    portalArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListIpAccessSettingsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListNetworkSettingsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class NetworkSettingsSummaryTypeDef(TypedDict):
    networkSettingsArn: str
    vpcId: NotRequired[str]

class ListPortalsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class PortalSummaryTypeDef(TypedDict):
    portalArn: str
    authenticationType: NotRequired[AuthenticationTypeType]
    browserSettingsArn: NotRequired[str]
    browserType: NotRequired[Literal["Chrome"]]
    creationDate: NotRequired[datetime]
    dataProtectionSettingsArn: NotRequired[str]
    displayName: NotRequired[str]
    instanceType: NotRequired[InstanceTypeType]
    ipAccessSettingsArn: NotRequired[str]
    maxConcurrentSessions: NotRequired[int]
    networkSettingsArn: NotRequired[str]
    portalEndpoint: NotRequired[str]
    portalStatus: NotRequired[PortalStatusType]
    rendererType: NotRequired[Literal["AppStream"]]
    trustStoreArn: NotRequired[str]
    userAccessLoggingSettingsArn: NotRequired[str]
    userSettingsArn: NotRequired[str]

class ListSessionsRequestTypeDef(TypedDict):
    portalId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sessionId: NotRequired[str]
    sortBy: NotRequired[SessionSortByType]
    status: NotRequired[SessionStatusType]
    username: NotRequired[str]

class SessionSummaryTypeDef(TypedDict):
    endTime: NotRequired[datetime]
    portalArn: NotRequired[str]
    sessionId: NotRequired[str]
    startTime: NotRequired[datetime]
    status: NotRequired[SessionStatusType]
    username: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListTrustStoreCertificatesRequestTypeDef(TypedDict):
    trustStoreArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTrustStoresRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class TrustStoreSummaryTypeDef(TypedDict):
    trustStoreArn: NotRequired[str]

class ListUserAccessLoggingSettingsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class UserAccessLoggingSettingsSummaryTypeDef(TypedDict):
    userAccessLoggingSettingsArn: str
    kinesisStreamArn: NotRequired[str]

class ListUserSettingsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ToolbarConfigurationOutputTypeDef(TypedDict):
    hiddenToolbarItems: NotRequired[List[ToolbarItemType]]
    maxDisplayResolution: NotRequired[MaxDisplayResolutionType]
    toolbarType: NotRequired[ToolbarTypeType]
    visualMode: NotRequired[VisualModeType]

class ToolbarConfigurationTypeDef(TypedDict):
    hiddenToolbarItems: NotRequired[Sequence[ToolbarItemType]]
    maxDisplayResolution: NotRequired[MaxDisplayResolutionType]
    toolbarType: NotRequired[ToolbarTypeType]
    visualMode: NotRequired[VisualModeType]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateBrowserSettingsRequestTypeDef(TypedDict):
    browserSettingsArn: str
    browserPolicy: NotRequired[str]
    clientToken: NotRequired[str]

class UpdateIdentityProviderRequestTypeDef(TypedDict):
    identityProviderArn: str
    clientToken: NotRequired[str]
    identityProviderDetails: NotRequired[Mapping[str, str]]
    identityProviderName: NotRequired[str]
    identityProviderType: NotRequired[IdentityProviderTypeType]

class UpdateNetworkSettingsRequestTypeDef(TypedDict):
    networkSettingsArn: str
    clientToken: NotRequired[str]
    securityGroupIds: NotRequired[Sequence[str]]
    subnetIds: NotRequired[Sequence[str]]
    vpcId: NotRequired[str]

class UpdatePortalRequestTypeDef(TypedDict):
    portalArn: str
    authenticationType: NotRequired[AuthenticationTypeType]
    displayName: NotRequired[str]
    instanceType: NotRequired[InstanceTypeType]
    maxConcurrentSessions: NotRequired[int]

class UpdateUserAccessLoggingSettingsRequestTypeDef(TypedDict):
    userAccessLoggingSettingsArn: str
    clientToken: NotRequired[str]
    kinesisStreamArn: NotRequired[str]

class AssociateBrowserSettingsResponseTypeDef(TypedDict):
    browserSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateDataProtectionSettingsResponseTypeDef(TypedDict):
    dataProtectionSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateIpAccessSettingsResponseTypeDef(TypedDict):
    ipAccessSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateNetworkSettingsResponseTypeDef(TypedDict):
    networkSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateTrustStoreResponseTypeDef(TypedDict):
    portalArn: str
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateUserAccessLoggingSettingsResponseTypeDef(TypedDict):
    portalArn: str
    userAccessLoggingSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateUserSettingsResponseTypeDef(TypedDict):
    portalArn: str
    userSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBrowserSettingsResponseTypeDef(TypedDict):
    browserSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataProtectionSettingsResponseTypeDef(TypedDict):
    dataProtectionSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIdentityProviderResponseTypeDef(TypedDict):
    identityProviderArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIpAccessSettingsResponseTypeDef(TypedDict):
    ipAccessSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNetworkSettingsResponseTypeDef(TypedDict):
    networkSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePortalResponseTypeDef(TypedDict):
    portalArn: str
    portalEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrustStoreResponseTypeDef(TypedDict):
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserAccessLoggingSettingsResponseTypeDef(TypedDict):
    userAccessLoggingSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserSettingsResponseTypeDef(TypedDict):
    userSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPortalServiceProviderMetadataResponseTypeDef(TypedDict):
    portalArn: str
    serviceProviderSamlMetadata: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrustStoreResponseTypeDef(TypedDict):
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrustStoreRequestTypeDef(TypedDict):
    trustStoreArn: str
    certificatesToAdd: NotRequired[Sequence[BlobTypeDef]]
    certificatesToDelete: NotRequired[Sequence[str]]
    clientToken: NotRequired[str]

class ListBrowserSettingsResponseTypeDef(TypedDict):
    browserSettings: List[BrowserSettingsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetBrowserSettingsResponseTypeDef(TypedDict):
    browserSettings: BrowserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBrowserSettingsResponseTypeDef(TypedDict):
    browserSettings: BrowserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrustStoreCertificatesResponseTypeDef(TypedDict):
    certificateList: List[CertificateSummaryTypeDef]
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetTrustStoreCertificateResponseTypeDef(TypedDict):
    certificate: CertificateTypeDef
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CookieSynchronizationConfigurationOutputTypeDef(TypedDict):
    allowlist: List[CookieSpecificationTypeDef]
    blocklist: NotRequired[List[CookieSpecificationTypeDef]]

class CookieSynchronizationConfigurationTypeDef(TypedDict):
    allowlist: Sequence[CookieSpecificationTypeDef]
    blocklist: NotRequired[Sequence[CookieSpecificationTypeDef]]

class CreateBrowserSettingsRequestTypeDef(TypedDict):
    browserPolicy: str
    additionalEncryptionContext: NotRequired[Mapping[str, str]]
    clientToken: NotRequired[str]
    customerManagedKey: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class CreateIdentityProviderRequestTypeDef(TypedDict):
    identityProviderDetails: Mapping[str, str]
    identityProviderName: str
    identityProviderType: IdentityProviderTypeType
    portalArn: str
    clientToken: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class CreateNetworkSettingsRequestTypeDef(TypedDict):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]
    vpcId: str
    clientToken: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class CreatePortalRequestTypeDef(TypedDict):
    additionalEncryptionContext: NotRequired[Mapping[str, str]]
    authenticationType: NotRequired[AuthenticationTypeType]
    clientToken: NotRequired[str]
    customerManagedKey: NotRequired[str]
    displayName: NotRequired[str]
    instanceType: NotRequired[InstanceTypeType]
    maxConcurrentSessions: NotRequired[int]
    tags: NotRequired[Sequence[TagTypeDef]]

class CreateTrustStoreRequestTypeDef(TypedDict):
    certificateList: Sequence[BlobTypeDef]
    clientToken: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class CreateUserAccessLoggingSettingsRequestTypeDef(TypedDict):
    kinesisStreamArn: str
    clientToken: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]
    clientToken: NotRequired[str]

class CreateIpAccessSettingsRequestTypeDef(TypedDict):
    ipRules: Sequence[IpRuleTypeDef]
    additionalEncryptionContext: NotRequired[Mapping[str, str]]
    clientToken: NotRequired[str]
    customerManagedKey: NotRequired[str]
    description: NotRequired[str]
    displayName: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class IpAccessSettingsTypeDef(TypedDict):
    ipAccessSettingsArn: str
    additionalEncryptionContext: NotRequired[Dict[str, str]]
    associatedPortalArns: NotRequired[List[str]]
    creationDate: NotRequired[datetime]
    customerManagedKey: NotRequired[str]
    description: NotRequired[str]
    displayName: NotRequired[str]
    ipRules: NotRequired[List[IpRuleTypeDef]]

class UpdateIpAccessSettingsRequestTypeDef(TypedDict):
    ipAccessSettingsArn: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    displayName: NotRequired[str]
    ipRules: NotRequired[Sequence[IpRuleTypeDef]]

class ListDataProtectionSettingsResponseTypeDef(TypedDict):
    dataProtectionSettings: List[DataProtectionSettingsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetIdentityProviderResponseTypeDef(TypedDict):
    identityProvider: IdentityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIdentityProviderResponseTypeDef(TypedDict):
    identityProvider: IdentityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkSettingsResponseTypeDef(TypedDict):
    networkSettings: NetworkSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNetworkSettingsResponseTypeDef(TypedDict):
    networkSettings: NetworkSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPortalResponseTypeDef(TypedDict):
    portal: PortalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePortalResponseTypeDef(TypedDict):
    portal: PortalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSessionResponseTypeDef(TypedDict):
    session: SessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrustStoreResponseTypeDef(TypedDict):
    trustStore: TrustStoreTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserAccessLoggingSettingsResponseTypeDef(TypedDict):
    userAccessLoggingSettings: UserAccessLoggingSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserAccessLoggingSettingsResponseTypeDef(TypedDict):
    userAccessLoggingSettings: UserAccessLoggingSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListIdentityProvidersResponseTypeDef(TypedDict):
    identityProviders: List[IdentityProviderSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class InlineRedactionPatternOutputTypeDef(TypedDict):
    redactionPlaceHolder: RedactionPlaceHolderTypeDef
    builtInPatternId: NotRequired[str]
    confidenceLevel: NotRequired[int]
    customPattern: NotRequired[CustomPatternTypeDef]
    enforcedUrls: NotRequired[List[str]]
    exemptUrls: NotRequired[List[str]]

class InlineRedactionPatternTypeDef(TypedDict):
    redactionPlaceHolder: RedactionPlaceHolderTypeDef
    builtInPatternId: NotRequired[str]
    confidenceLevel: NotRequired[int]
    customPattern: NotRequired[CustomPatternTypeDef]
    enforcedUrls: NotRequired[Sequence[str]]
    exemptUrls: NotRequired[Sequence[str]]

class ListIpAccessSettingsResponseTypeDef(TypedDict):
    ipAccessSettings: List[IpAccessSettingsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListDataProtectionSettingsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSessionsRequestPaginateTypeDef(TypedDict):
    portalId: str
    sessionId: NotRequired[str]
    sortBy: NotRequired[SessionSortByType]
    status: NotRequired[SessionStatusType]
    username: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListNetworkSettingsResponseTypeDef(TypedDict):
    networkSettings: List[NetworkSettingsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListPortalsResponseTypeDef(TypedDict):
    portals: List[PortalSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSessionsResponseTypeDef(TypedDict):
    sessions: List[SessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTrustStoresResponseTypeDef(TypedDict):
    trustStores: List[TrustStoreSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListUserAccessLoggingSettingsResponseTypeDef(TypedDict):
    userAccessLoggingSettings: List[UserAccessLoggingSettingsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ToolbarConfigurationUnionTypeDef = Union[
    ToolbarConfigurationTypeDef, ToolbarConfigurationOutputTypeDef
]

class UserSettingsSummaryTypeDef(TypedDict):
    userSettingsArn: str
    cookieSynchronizationConfiguration: NotRequired[CookieSynchronizationConfigurationOutputTypeDef]
    copyAllowed: NotRequired[EnabledTypeType]
    deepLinkAllowed: NotRequired[EnabledTypeType]
    disconnectTimeoutInMinutes: NotRequired[int]
    downloadAllowed: NotRequired[EnabledTypeType]
    idleDisconnectTimeoutInMinutes: NotRequired[int]
    pasteAllowed: NotRequired[EnabledTypeType]
    printAllowed: NotRequired[EnabledTypeType]
    toolbarConfiguration: NotRequired[ToolbarConfigurationOutputTypeDef]
    uploadAllowed: NotRequired[EnabledTypeType]

class UserSettingsTypeDef(TypedDict):
    userSettingsArn: str
    additionalEncryptionContext: NotRequired[Dict[str, str]]
    associatedPortalArns: NotRequired[List[str]]
    cookieSynchronizationConfiguration: NotRequired[CookieSynchronizationConfigurationOutputTypeDef]
    copyAllowed: NotRequired[EnabledTypeType]
    customerManagedKey: NotRequired[str]
    deepLinkAllowed: NotRequired[EnabledTypeType]
    disconnectTimeoutInMinutes: NotRequired[int]
    downloadAllowed: NotRequired[EnabledTypeType]
    idleDisconnectTimeoutInMinutes: NotRequired[int]
    pasteAllowed: NotRequired[EnabledTypeType]
    printAllowed: NotRequired[EnabledTypeType]
    toolbarConfiguration: NotRequired[ToolbarConfigurationOutputTypeDef]
    uploadAllowed: NotRequired[EnabledTypeType]

CookieSynchronizationConfigurationUnionTypeDef = Union[
    CookieSynchronizationConfigurationTypeDef, CookieSynchronizationConfigurationOutputTypeDef
]

class GetIpAccessSettingsResponseTypeDef(TypedDict):
    ipAccessSettings: IpAccessSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIpAccessSettingsResponseTypeDef(TypedDict):
    ipAccessSettings: IpAccessSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InlineRedactionConfigurationOutputTypeDef(TypedDict):
    inlineRedactionPatterns: List[InlineRedactionPatternOutputTypeDef]
    globalConfidenceLevel: NotRequired[int]
    globalEnforcedUrls: NotRequired[List[str]]
    globalExemptUrls: NotRequired[List[str]]

class InlineRedactionConfigurationTypeDef(TypedDict):
    inlineRedactionPatterns: Sequence[InlineRedactionPatternTypeDef]
    globalConfidenceLevel: NotRequired[int]
    globalEnforcedUrls: NotRequired[Sequence[str]]
    globalExemptUrls: NotRequired[Sequence[str]]

class ListUserSettingsResponseTypeDef(TypedDict):
    userSettings: List[UserSettingsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetUserSettingsResponseTypeDef(TypedDict):
    userSettings: UserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserSettingsResponseTypeDef(TypedDict):
    userSettings: UserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserSettingsRequestTypeDef(TypedDict):
    copyAllowed: EnabledTypeType
    downloadAllowed: EnabledTypeType
    pasteAllowed: EnabledTypeType
    printAllowed: EnabledTypeType
    uploadAllowed: EnabledTypeType
    additionalEncryptionContext: NotRequired[Mapping[str, str]]
    clientToken: NotRequired[str]
    cookieSynchronizationConfiguration: NotRequired[CookieSynchronizationConfigurationUnionTypeDef]
    customerManagedKey: NotRequired[str]
    deepLinkAllowed: NotRequired[EnabledTypeType]
    disconnectTimeoutInMinutes: NotRequired[int]
    idleDisconnectTimeoutInMinutes: NotRequired[int]
    tags: NotRequired[Sequence[TagTypeDef]]
    toolbarConfiguration: NotRequired[ToolbarConfigurationUnionTypeDef]

class UpdateUserSettingsRequestTypeDef(TypedDict):
    userSettingsArn: str
    clientToken: NotRequired[str]
    cookieSynchronizationConfiguration: NotRequired[CookieSynchronizationConfigurationUnionTypeDef]
    copyAllowed: NotRequired[EnabledTypeType]
    deepLinkAllowed: NotRequired[EnabledTypeType]
    disconnectTimeoutInMinutes: NotRequired[int]
    downloadAllowed: NotRequired[EnabledTypeType]
    idleDisconnectTimeoutInMinutes: NotRequired[int]
    pasteAllowed: NotRequired[EnabledTypeType]
    printAllowed: NotRequired[EnabledTypeType]
    toolbarConfiguration: NotRequired[ToolbarConfigurationUnionTypeDef]
    uploadAllowed: NotRequired[EnabledTypeType]

class DataProtectionSettingsTypeDef(TypedDict):
    dataProtectionSettingsArn: str
    additionalEncryptionContext: NotRequired[Dict[str, str]]
    associatedPortalArns: NotRequired[List[str]]
    creationDate: NotRequired[datetime]
    customerManagedKey: NotRequired[str]
    description: NotRequired[str]
    displayName: NotRequired[str]
    inlineRedactionConfiguration: NotRequired[InlineRedactionConfigurationOutputTypeDef]

InlineRedactionConfigurationUnionTypeDef = Union[
    InlineRedactionConfigurationTypeDef, InlineRedactionConfigurationOutputTypeDef
]

class GetDataProtectionSettingsResponseTypeDef(TypedDict):
    dataProtectionSettings: DataProtectionSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataProtectionSettingsResponseTypeDef(TypedDict):
    dataProtectionSettings: DataProtectionSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataProtectionSettingsRequestTypeDef(TypedDict):
    additionalEncryptionContext: NotRequired[Mapping[str, str]]
    clientToken: NotRequired[str]
    customerManagedKey: NotRequired[str]
    description: NotRequired[str]
    displayName: NotRequired[str]
    inlineRedactionConfiguration: NotRequired[InlineRedactionConfigurationUnionTypeDef]
    tags: NotRequired[Sequence[TagTypeDef]]

class UpdateDataProtectionSettingsRequestTypeDef(TypedDict):
    dataProtectionSettingsArn: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    displayName: NotRequired[str]
    inlineRedactionConfiguration: NotRequired[InlineRedactionConfigurationUnionTypeDef]
