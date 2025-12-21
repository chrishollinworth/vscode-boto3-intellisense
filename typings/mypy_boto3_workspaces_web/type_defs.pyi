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
    CategoryType,
    ColorThemeType,
    EnabledTypeType,
    EventType,
    FolderStructureType,
    IdentityProviderTypeType,
    InstanceTypeType,
    LocaleType,
    LogFileFormatType,
    MaxDisplayResolutionType,
    MimeTypeType,
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
    "AssociateSessionLoggerRequestTypeDef",
    "AssociateSessionLoggerResponseTypeDef",
    "AssociateTrustStoreRequestTypeDef",
    "AssociateTrustStoreResponseTypeDef",
    "AssociateUserAccessLoggingSettingsRequestTypeDef",
    "AssociateUserAccessLoggingSettingsResponseTypeDef",
    "AssociateUserSettingsRequestTypeDef",
    "AssociateUserSettingsResponseTypeDef",
    "BlobTypeDef",
    "BrandingConfigurationCreateInputTypeDef",
    "BrandingConfigurationTypeDef",
    "BrandingConfigurationUpdateInputTypeDef",
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
    "CreateSessionLoggerRequestTypeDef",
    "CreateSessionLoggerResponseTypeDef",
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
    "DeleteSessionLoggerRequestTypeDef",
    "DeleteTrustStoreRequestTypeDef",
    "DeleteUserAccessLoggingSettingsRequestTypeDef",
    "DeleteUserSettingsRequestTypeDef",
    "DisassociateBrowserSettingsRequestTypeDef",
    "DisassociateDataProtectionSettingsRequestTypeDef",
    "DisassociateIpAccessSettingsRequestTypeDef",
    "DisassociateNetworkSettingsRequestTypeDef",
    "DisassociateSessionLoggerRequestTypeDef",
    "DisassociateTrustStoreRequestTypeDef",
    "DisassociateUserAccessLoggingSettingsRequestTypeDef",
    "DisassociateUserSettingsRequestTypeDef",
    "EventFilterOutputTypeDef",
    "EventFilterTypeDef",
    "EventFilterUnionTypeDef",
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
    "GetSessionLoggerRequestTypeDef",
    "GetSessionLoggerResponseTypeDef",
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
    "IconImageInputTypeDef",
    "IdentityProviderSummaryTypeDef",
    "IdentityProviderTypeDef",
    "ImageMetadataTypeDef",
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
    "ListSessionLoggersRequestPaginateTypeDef",
    "ListSessionLoggersRequestTypeDef",
    "ListSessionLoggersResponseTypeDef",
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
    "LocalizedBrandingStringsTypeDef",
    "LogConfigurationTypeDef",
    "NetworkSettingsSummaryTypeDef",
    "NetworkSettingsTypeDef",
    "PaginatorConfigTypeDef",
    "PortalSummaryTypeDef",
    "PortalTypeDef",
    "RedactionPlaceHolderTypeDef",
    "ResponseMetadataTypeDef",
    "S3LogConfigurationTypeDef",
    "SessionLoggerSummaryTypeDef",
    "SessionLoggerTypeDef",
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
    "UpdateSessionLoggerRequestTypeDef",
    "UpdateSessionLoggerResponseTypeDef",
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
    "WallpaperImageInputTypeDef",
    "WebContentFilteringPolicyOutputTypeDef",
    "WebContentFilteringPolicyTypeDef",
    "WebContentFilteringPolicyUnionTypeDef",
)

class AssociateBrowserSettingsRequestTypeDef(TypedDict):
    portalArn: str
    browserSettingsArn: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AssociateDataProtectionSettingsRequestTypeDef(TypedDict):
    portalArn: str
    dataProtectionSettingsArn: str

class AssociateIpAccessSettingsRequestTypeDef(TypedDict):
    portalArn: str
    ipAccessSettingsArn: str

class AssociateNetworkSettingsRequestTypeDef(TypedDict):
    portalArn: str
    networkSettingsArn: str

class AssociateSessionLoggerRequestTypeDef(TypedDict):
    portalArn: str
    sessionLoggerArn: str

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

class LocalizedBrandingStringsTypeDef(TypedDict):
    browserTabTitle: str
    welcomeText: str
    loginTitle: NotRequired[str]
    loginDescription: NotRequired[str]
    loginButtonText: NotRequired[str]
    contactLink: NotRequired[str]
    contactButtonText: NotRequired[str]
    loadingText: NotRequired[str]

class ImageMetadataTypeDef(TypedDict):
    mimeType: MimeTypeType
    fileExtension: str
    lastUploadTimestamp: datetime

class BrowserSettingsSummaryTypeDef(TypedDict):
    browserSettingsArn: str

class WebContentFilteringPolicyOutputTypeDef(TypedDict):
    blockedCategories: NotRequired[List[CategoryType]]
    allowedUrls: NotRequired[List[str]]
    blockedUrls: NotRequired[List[str]]

class CertificateSummaryTypeDef(TypedDict):
    thumbprint: NotRequired[str]
    subject: NotRequired[str]
    issuer: NotRequired[str]
    notValidBefore: NotRequired[datetime]
    notValidAfter: NotRequired[datetime]

class CertificateTypeDef(TypedDict):
    thumbprint: NotRequired[str]
    subject: NotRequired[str]
    issuer: NotRequired[str]
    notValidBefore: NotRequired[datetime]
    notValidAfter: NotRequired[datetime]
    body: NotRequired[bytes]

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
    patternDescription: NotRequired[str]
    keywordRegex: NotRequired[str]

class DataProtectionSettingsSummaryTypeDef(TypedDict):
    dataProtectionSettingsArn: str
    displayName: NotRequired[str]
    description: NotRequired[str]
    creationDate: NotRequired[datetime]

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

class DeleteSessionLoggerRequestTypeDef(TypedDict):
    sessionLoggerArn: str

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

class DisassociateSessionLoggerRequestTypeDef(TypedDict):
    portalArn: str

class DisassociateTrustStoreRequestTypeDef(TypedDict):
    portalArn: str

class DisassociateUserAccessLoggingSettingsRequestTypeDef(TypedDict):
    portalArn: str

class DisassociateUserSettingsRequestTypeDef(TypedDict):
    portalArn: str

EventFilterOutputTypeDef = TypedDict(
    "EventFilterOutputTypeDef",
    {
        "all": NotRequired[Dict[str, Any]],
        "include": NotRequired[List[EventType]],
    },
)
EventFilterTypeDef = TypedDict(
    "EventFilterTypeDef",
    {
        "all": NotRequired[Mapping[str, Any]],
        "include": NotRequired[Sequence[EventType]],
    },
)

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
    identityProviderName: NotRequired[str]
    identityProviderType: NotRequired[IdentityProviderTypeType]
    identityProviderDetails: NotRequired[Dict[str, str]]

class GetIpAccessSettingsRequestTypeDef(TypedDict):
    ipAccessSettingsArn: str

class GetNetworkSettingsRequestTypeDef(TypedDict):
    networkSettingsArn: str

class NetworkSettingsTypeDef(TypedDict):
    networkSettingsArn: str
    associatedPortalArns: NotRequired[List[str]]
    vpcId: NotRequired[str]
    subnetIds: NotRequired[List[str]]
    securityGroupIds: NotRequired[List[str]]

class GetPortalRequestTypeDef(TypedDict):
    portalArn: str

class PortalTypeDef(TypedDict):
    portalArn: str
    rendererType: NotRequired[Literal["AppStream"]]
    browserType: NotRequired[Literal["Chrome"]]
    portalStatus: NotRequired[PortalStatusType]
    portalEndpoint: NotRequired[str]
    displayName: NotRequired[str]
    creationDate: NotRequired[datetime]
    browserSettingsArn: NotRequired[str]
    dataProtectionSettingsArn: NotRequired[str]
    userSettingsArn: NotRequired[str]
    networkSettingsArn: NotRequired[str]
    sessionLoggerArn: NotRequired[str]
    trustStoreArn: NotRequired[str]
    statusReason: NotRequired[str]
    userAccessLoggingSettingsArn: NotRequired[str]
    authenticationType: NotRequired[AuthenticationTypeType]
    ipAccessSettingsArn: NotRequired[str]
    customerManagedKey: NotRequired[str]
    additionalEncryptionContext: NotRequired[Dict[str, str]]
    instanceType: NotRequired[InstanceTypeType]
    maxConcurrentSessions: NotRequired[int]

class GetPortalServiceProviderMetadataRequestTypeDef(TypedDict):
    portalArn: str

class GetSessionLoggerRequestTypeDef(TypedDict):
    sessionLoggerArn: str

class GetSessionRequestTypeDef(TypedDict):
    portalId: str
    sessionId: str

class SessionTypeDef(TypedDict):
    portalArn: NotRequired[str]
    sessionId: NotRequired[str]
    username: NotRequired[str]
    clientIpAddresses: NotRequired[List[str]]
    status: NotRequired[SessionStatusType]
    startTime: NotRequired[datetime]
    endTime: NotRequired[datetime]

class GetTrustStoreCertificateRequestTypeDef(TypedDict):
    trustStoreArn: str
    thumbprint: str

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
    displayName: NotRequired[str]
    description: NotRequired[str]
    creationDate: NotRequired[datetime]

class ListBrowserSettingsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListDataProtectionSettingsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListIdentityProvidersRequestTypeDef(TypedDict):
    portalArn: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListIpAccessSettingsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListNetworkSettingsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class NetworkSettingsSummaryTypeDef(TypedDict):
    networkSettingsArn: str
    vpcId: NotRequired[str]

class ListPortalsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class PortalSummaryTypeDef(TypedDict):
    portalArn: str
    rendererType: NotRequired[Literal["AppStream"]]
    browserType: NotRequired[Literal["Chrome"]]
    portalStatus: NotRequired[PortalStatusType]
    portalEndpoint: NotRequired[str]
    displayName: NotRequired[str]
    creationDate: NotRequired[datetime]
    browserSettingsArn: NotRequired[str]
    dataProtectionSettingsArn: NotRequired[str]
    userSettingsArn: NotRequired[str]
    networkSettingsArn: NotRequired[str]
    sessionLoggerArn: NotRequired[str]
    trustStoreArn: NotRequired[str]
    userAccessLoggingSettingsArn: NotRequired[str]
    authenticationType: NotRequired[AuthenticationTypeType]
    ipAccessSettingsArn: NotRequired[str]
    instanceType: NotRequired[InstanceTypeType]
    maxConcurrentSessions: NotRequired[int]

class ListSessionLoggersRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListSessionsRequestTypeDef(TypedDict):
    portalId: str
    username: NotRequired[str]
    sessionId: NotRequired[str]
    sortBy: NotRequired[SessionSortByType]
    status: NotRequired[SessionStatusType]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class SessionSummaryTypeDef(TypedDict):
    portalArn: NotRequired[str]
    sessionId: NotRequired[str]
    username: NotRequired[str]
    status: NotRequired[SessionStatusType]
    startTime: NotRequired[datetime]
    endTime: NotRequired[datetime]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListTrustStoreCertificatesRequestTypeDef(TypedDict):
    trustStoreArn: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListTrustStoresRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class TrustStoreSummaryTypeDef(TypedDict):
    trustStoreArn: NotRequired[str]

class ListUserAccessLoggingSettingsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class UserAccessLoggingSettingsSummaryTypeDef(TypedDict):
    userAccessLoggingSettingsArn: str
    kinesisStreamArn: NotRequired[str]

class ListUserSettingsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class S3LogConfigurationTypeDef(TypedDict):
    bucket: str
    logFileFormat: LogFileFormatType
    folderStructure: FolderStructureType
    keyPrefix: NotRequired[str]
    bucketOwner: NotRequired[str]

class ToolbarConfigurationOutputTypeDef(TypedDict):
    toolbarType: NotRequired[ToolbarTypeType]
    visualMode: NotRequired[VisualModeType]
    hiddenToolbarItems: NotRequired[List[ToolbarItemType]]
    maxDisplayResolution: NotRequired[MaxDisplayResolutionType]

class ToolbarConfigurationTypeDef(TypedDict):
    toolbarType: NotRequired[ToolbarTypeType]
    visualMode: NotRequired[VisualModeType]
    hiddenToolbarItems: NotRequired[Sequence[ToolbarItemType]]
    maxDisplayResolution: NotRequired[MaxDisplayResolutionType]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateIdentityProviderRequestTypeDef(TypedDict):
    identityProviderArn: str
    identityProviderName: NotRequired[str]
    identityProviderType: NotRequired[IdentityProviderTypeType]
    identityProviderDetails: NotRequired[Mapping[str, str]]
    clientToken: NotRequired[str]

class UpdateNetworkSettingsRequestTypeDef(TypedDict):
    networkSettingsArn: str
    vpcId: NotRequired[str]
    subnetIds: NotRequired[Sequence[str]]
    securityGroupIds: NotRequired[Sequence[str]]
    clientToken: NotRequired[str]

class UpdatePortalRequestTypeDef(TypedDict):
    portalArn: str
    displayName: NotRequired[str]
    authenticationType: NotRequired[AuthenticationTypeType]
    instanceType: NotRequired[InstanceTypeType]
    maxConcurrentSessions: NotRequired[int]

class UpdateUserAccessLoggingSettingsRequestTypeDef(TypedDict):
    userAccessLoggingSettingsArn: str
    kinesisStreamArn: NotRequired[str]
    clientToken: NotRequired[str]

class WebContentFilteringPolicyTypeDef(TypedDict):
    blockedCategories: NotRequired[Sequence[CategoryType]]
    allowedUrls: NotRequired[Sequence[str]]
    blockedUrls: NotRequired[Sequence[str]]

class AssociateBrowserSettingsResponseTypeDef(TypedDict):
    portalArn: str
    browserSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateDataProtectionSettingsResponseTypeDef(TypedDict):
    portalArn: str
    dataProtectionSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateIpAccessSettingsResponseTypeDef(TypedDict):
    portalArn: str
    ipAccessSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateNetworkSettingsResponseTypeDef(TypedDict):
    portalArn: str
    networkSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateSessionLoggerResponseTypeDef(TypedDict):
    portalArn: str
    sessionLoggerArn: str
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

class CreateSessionLoggerResponseTypeDef(TypedDict):
    sessionLoggerArn: str
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

class IconImageInputTypeDef(TypedDict):
    blob: NotRequired[BlobTypeDef]
    s3Uri: NotRequired[str]

class UpdateTrustStoreRequestTypeDef(TypedDict):
    trustStoreArn: str
    certificatesToAdd: NotRequired[Sequence[BlobTypeDef]]
    certificatesToDelete: NotRequired[Sequence[str]]
    clientToken: NotRequired[str]

class WallpaperImageInputTypeDef(TypedDict):
    blob: NotRequired[BlobTypeDef]
    s3Uri: NotRequired[str]

class BrandingConfigurationTypeDef(TypedDict):
    logo: ImageMetadataTypeDef
    wallpaper: ImageMetadataTypeDef
    favicon: ImageMetadataTypeDef
    localizedStrings: Dict[LocaleType, LocalizedBrandingStringsTypeDef]
    colorTheme: ColorThemeType
    termsOfService: NotRequired[str]

class ListBrowserSettingsResponseTypeDef(TypedDict):
    browserSettings: List[BrowserSettingsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class BrowserSettingsTypeDef(TypedDict):
    browserSettingsArn: str
    associatedPortalArns: NotRequired[List[str]]
    browserPolicy: NotRequired[str]
    customerManagedKey: NotRequired[str]
    additionalEncryptionContext: NotRequired[Dict[str, str]]
    webContentFilteringPolicy: NotRequired[WebContentFilteringPolicyOutputTypeDef]

class ListTrustStoreCertificatesResponseTypeDef(TypedDict):
    certificateList: List[CertificateSummaryTypeDef]
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetTrustStoreCertificateResponseTypeDef(TypedDict):
    trustStoreArn: str
    certificate: CertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CookieSynchronizationConfigurationOutputTypeDef(TypedDict):
    allowlist: List[CookieSpecificationTypeDef]
    blocklist: NotRequired[List[CookieSpecificationTypeDef]]

class CookieSynchronizationConfigurationTypeDef(TypedDict):
    allowlist: Sequence[CookieSpecificationTypeDef]
    blocklist: NotRequired[Sequence[CookieSpecificationTypeDef]]

class CreateIdentityProviderRequestTypeDef(TypedDict):
    portalArn: str
    identityProviderName: str
    identityProviderType: IdentityProviderTypeType
    identityProviderDetails: Mapping[str, str]
    clientToken: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class CreateNetworkSettingsRequestTypeDef(TypedDict):
    vpcId: str
    subnetIds: Sequence[str]
    securityGroupIds: Sequence[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    clientToken: NotRequired[str]

class CreatePortalRequestTypeDef(TypedDict):
    displayName: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    customerManagedKey: NotRequired[str]
    additionalEncryptionContext: NotRequired[Mapping[str, str]]
    clientToken: NotRequired[str]
    authenticationType: NotRequired[AuthenticationTypeType]
    instanceType: NotRequired[InstanceTypeType]
    maxConcurrentSessions: NotRequired[int]

class CreateTrustStoreRequestTypeDef(TypedDict):
    certificateList: Sequence[BlobTypeDef]
    tags: NotRequired[Sequence[TagTypeDef]]
    clientToken: NotRequired[str]

class CreateUserAccessLoggingSettingsRequestTypeDef(TypedDict):
    kinesisStreamArn: str
    tags: NotRequired[Sequence[TagTypeDef]]
    clientToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]
    clientToken: NotRequired[str]

class CreateIpAccessSettingsRequestTypeDef(TypedDict):
    ipRules: Sequence[IpRuleTypeDef]
    displayName: NotRequired[str]
    description: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    customerManagedKey: NotRequired[str]
    additionalEncryptionContext: NotRequired[Mapping[str, str]]
    clientToken: NotRequired[str]

class IpAccessSettingsTypeDef(TypedDict):
    ipAccessSettingsArn: str
    associatedPortalArns: NotRequired[List[str]]
    ipRules: NotRequired[List[IpRuleTypeDef]]
    displayName: NotRequired[str]
    description: NotRequired[str]
    creationDate: NotRequired[datetime]
    customerManagedKey: NotRequired[str]
    additionalEncryptionContext: NotRequired[Dict[str, str]]

class UpdateIpAccessSettingsRequestTypeDef(TypedDict):
    ipAccessSettingsArn: str
    displayName: NotRequired[str]
    description: NotRequired[str]
    ipRules: NotRequired[Sequence[IpRuleTypeDef]]
    clientToken: NotRequired[str]

class ListDataProtectionSettingsResponseTypeDef(TypedDict):
    dataProtectionSettings: List[DataProtectionSettingsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

EventFilterUnionTypeDef = Union[EventFilterTypeDef, EventFilterOutputTypeDef]

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
    customPattern: NotRequired[CustomPatternTypeDef]
    enforcedUrls: NotRequired[List[str]]
    exemptUrls: NotRequired[List[str]]
    confidenceLevel: NotRequired[int]

class InlineRedactionPatternTypeDef(TypedDict):
    redactionPlaceHolder: RedactionPlaceHolderTypeDef
    builtInPatternId: NotRequired[str]
    customPattern: NotRequired[CustomPatternTypeDef]
    enforcedUrls: NotRequired[Sequence[str]]
    exemptUrls: NotRequired[Sequence[str]]
    confidenceLevel: NotRequired[int]

class ListIpAccessSettingsResponseTypeDef(TypedDict):
    ipAccessSettings: List[IpAccessSettingsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListDataProtectionSettingsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSessionLoggersRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSessionsRequestPaginateTypeDef(TypedDict):
    portalId: str
    username: NotRequired[str]
    sessionId: NotRequired[str]
    sortBy: NotRequired[SessionSortByType]
    status: NotRequired[SessionStatusType]
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

class LogConfigurationTypeDef(TypedDict):
    s3: NotRequired[S3LogConfigurationTypeDef]

ToolbarConfigurationUnionTypeDef = Union[
    ToolbarConfigurationTypeDef, ToolbarConfigurationOutputTypeDef
]
WebContentFilteringPolicyUnionTypeDef = Union[
    WebContentFilteringPolicyTypeDef, WebContentFilteringPolicyOutputTypeDef
]

class BrandingConfigurationCreateInputTypeDef(TypedDict):
    logo: IconImageInputTypeDef
    wallpaper: WallpaperImageInputTypeDef
    favicon: IconImageInputTypeDef
    localizedStrings: Mapping[LocaleType, LocalizedBrandingStringsTypeDef]
    colorTheme: ColorThemeType
    termsOfService: NotRequired[str]

class BrandingConfigurationUpdateInputTypeDef(TypedDict):
    logo: NotRequired[IconImageInputTypeDef]
    wallpaper: NotRequired[WallpaperImageInputTypeDef]
    favicon: NotRequired[IconImageInputTypeDef]
    localizedStrings: NotRequired[Mapping[LocaleType, LocalizedBrandingStringsTypeDef]]
    colorTheme: NotRequired[ColorThemeType]
    termsOfService: NotRequired[str]

class GetBrowserSettingsResponseTypeDef(TypedDict):
    browserSettings: BrowserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBrowserSettingsResponseTypeDef(TypedDict):
    browserSettings: BrowserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UserSettingsSummaryTypeDef(TypedDict):
    userSettingsArn: str
    copyAllowed: NotRequired[EnabledTypeType]
    pasteAllowed: NotRequired[EnabledTypeType]
    downloadAllowed: NotRequired[EnabledTypeType]
    uploadAllowed: NotRequired[EnabledTypeType]
    printAllowed: NotRequired[EnabledTypeType]
    disconnectTimeoutInMinutes: NotRequired[int]
    idleDisconnectTimeoutInMinutes: NotRequired[int]
    cookieSynchronizationConfiguration: NotRequired[CookieSynchronizationConfigurationOutputTypeDef]
    deepLinkAllowed: NotRequired[EnabledTypeType]
    toolbarConfiguration: NotRequired[ToolbarConfigurationOutputTypeDef]
    brandingConfiguration: NotRequired[BrandingConfigurationTypeDef]
    webAuthnAllowed: NotRequired[EnabledTypeType]

class UserSettingsTypeDef(TypedDict):
    userSettingsArn: str
    associatedPortalArns: NotRequired[List[str]]
    copyAllowed: NotRequired[EnabledTypeType]
    pasteAllowed: NotRequired[EnabledTypeType]
    downloadAllowed: NotRequired[EnabledTypeType]
    uploadAllowed: NotRequired[EnabledTypeType]
    printAllowed: NotRequired[EnabledTypeType]
    disconnectTimeoutInMinutes: NotRequired[int]
    idleDisconnectTimeoutInMinutes: NotRequired[int]
    cookieSynchronizationConfiguration: NotRequired[CookieSynchronizationConfigurationOutputTypeDef]
    customerManagedKey: NotRequired[str]
    additionalEncryptionContext: NotRequired[Dict[str, str]]
    deepLinkAllowed: NotRequired[EnabledTypeType]
    toolbarConfiguration: NotRequired[ToolbarConfigurationOutputTypeDef]
    brandingConfiguration: NotRequired[BrandingConfigurationTypeDef]
    webAuthnAllowed: NotRequired[EnabledTypeType]

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
    globalEnforcedUrls: NotRequired[List[str]]
    globalExemptUrls: NotRequired[List[str]]
    globalConfidenceLevel: NotRequired[int]

class InlineRedactionConfigurationTypeDef(TypedDict):
    inlineRedactionPatterns: Sequence[InlineRedactionPatternTypeDef]
    globalEnforcedUrls: NotRequired[Sequence[str]]
    globalExemptUrls: NotRequired[Sequence[str]]
    globalConfidenceLevel: NotRequired[int]

class CreateSessionLoggerRequestTypeDef(TypedDict):
    eventFilter: EventFilterUnionTypeDef
    logConfiguration: LogConfigurationTypeDef
    displayName: NotRequired[str]
    customerManagedKey: NotRequired[str]
    additionalEncryptionContext: NotRequired[Mapping[str, str]]
    tags: NotRequired[Sequence[TagTypeDef]]
    clientToken: NotRequired[str]

class SessionLoggerSummaryTypeDef(TypedDict):
    sessionLoggerArn: str
    logConfiguration: NotRequired[LogConfigurationTypeDef]
    displayName: NotRequired[str]
    creationDate: NotRequired[datetime]

class SessionLoggerTypeDef(TypedDict):
    sessionLoggerArn: str
    eventFilter: NotRequired[EventFilterOutputTypeDef]
    logConfiguration: NotRequired[LogConfigurationTypeDef]
    customerManagedKey: NotRequired[str]
    additionalEncryptionContext: NotRequired[Dict[str, str]]
    associatedPortalArns: NotRequired[List[str]]
    displayName: NotRequired[str]
    creationDate: NotRequired[datetime]

class UpdateSessionLoggerRequestTypeDef(TypedDict):
    sessionLoggerArn: str
    eventFilter: NotRequired[EventFilterUnionTypeDef]
    logConfiguration: NotRequired[LogConfigurationTypeDef]
    displayName: NotRequired[str]

class CreateBrowserSettingsRequestTypeDef(TypedDict):
    tags: NotRequired[Sequence[TagTypeDef]]
    customerManagedKey: NotRequired[str]
    additionalEncryptionContext: NotRequired[Mapping[str, str]]
    browserPolicy: NotRequired[str]
    clientToken: NotRequired[str]
    webContentFilteringPolicy: NotRequired[WebContentFilteringPolicyUnionTypeDef]

class UpdateBrowserSettingsRequestTypeDef(TypedDict):
    browserSettingsArn: str
    browserPolicy: NotRequired[str]
    clientToken: NotRequired[str]
    webContentFilteringPolicy: NotRequired[WebContentFilteringPolicyUnionTypeDef]

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
    pasteAllowed: EnabledTypeType
    downloadAllowed: EnabledTypeType
    uploadAllowed: EnabledTypeType
    printAllowed: EnabledTypeType
    tags: NotRequired[Sequence[TagTypeDef]]
    disconnectTimeoutInMinutes: NotRequired[int]
    idleDisconnectTimeoutInMinutes: NotRequired[int]
    clientToken: NotRequired[str]
    cookieSynchronizationConfiguration: NotRequired[CookieSynchronizationConfigurationUnionTypeDef]
    customerManagedKey: NotRequired[str]
    additionalEncryptionContext: NotRequired[Mapping[str, str]]
    deepLinkAllowed: NotRequired[EnabledTypeType]
    toolbarConfiguration: NotRequired[ToolbarConfigurationUnionTypeDef]
    brandingConfigurationInput: NotRequired[BrandingConfigurationCreateInputTypeDef]
    webAuthnAllowed: NotRequired[EnabledTypeType]

class UpdateUserSettingsRequestTypeDef(TypedDict):
    userSettingsArn: str
    copyAllowed: NotRequired[EnabledTypeType]
    pasteAllowed: NotRequired[EnabledTypeType]
    downloadAllowed: NotRequired[EnabledTypeType]
    uploadAllowed: NotRequired[EnabledTypeType]
    printAllowed: NotRequired[EnabledTypeType]
    disconnectTimeoutInMinutes: NotRequired[int]
    idleDisconnectTimeoutInMinutes: NotRequired[int]
    clientToken: NotRequired[str]
    cookieSynchronizationConfiguration: NotRequired[CookieSynchronizationConfigurationUnionTypeDef]
    deepLinkAllowed: NotRequired[EnabledTypeType]
    toolbarConfiguration: NotRequired[ToolbarConfigurationUnionTypeDef]
    brandingConfigurationInput: NotRequired[BrandingConfigurationUpdateInputTypeDef]
    webAuthnAllowed: NotRequired[EnabledTypeType]

class DataProtectionSettingsTypeDef(TypedDict):
    dataProtectionSettingsArn: str
    inlineRedactionConfiguration: NotRequired[InlineRedactionConfigurationOutputTypeDef]
    associatedPortalArns: NotRequired[List[str]]
    displayName: NotRequired[str]
    description: NotRequired[str]
    creationDate: NotRequired[datetime]
    customerManagedKey: NotRequired[str]
    additionalEncryptionContext: NotRequired[Dict[str, str]]

InlineRedactionConfigurationUnionTypeDef = Union[
    InlineRedactionConfigurationTypeDef, InlineRedactionConfigurationOutputTypeDef
]

class ListSessionLoggersResponseTypeDef(TypedDict):
    sessionLoggers: List[SessionLoggerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetSessionLoggerResponseTypeDef(TypedDict):
    sessionLogger: SessionLoggerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSessionLoggerResponseTypeDef(TypedDict):
    sessionLogger: SessionLoggerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataProtectionSettingsResponseTypeDef(TypedDict):
    dataProtectionSettings: DataProtectionSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataProtectionSettingsResponseTypeDef(TypedDict):
    dataProtectionSettings: DataProtectionSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataProtectionSettingsRequestTypeDef(TypedDict):
    displayName: NotRequired[str]
    description: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    customerManagedKey: NotRequired[str]
    additionalEncryptionContext: NotRequired[Mapping[str, str]]
    inlineRedactionConfiguration: NotRequired[InlineRedactionConfigurationUnionTypeDef]
    clientToken: NotRequired[str]

class UpdateDataProtectionSettingsRequestTypeDef(TypedDict):
    dataProtectionSettingsArn: str
    inlineRedactionConfiguration: NotRequired[InlineRedactionConfigurationUnionTypeDef]
    displayName: NotRequired[str]
    description: NotRequired[str]
    clientToken: NotRequired[str]
