"""
Type annotations for license-manager-user-subscriptions service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_license_manager_user_subscriptions.type_defs import DomainNetworkSettingsOutputTypeDef

    data: DomainNetworkSettingsOutputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ActiveDirectoryTypeType,
    LicenseServerEndpointProvisioningStatusType,
    LicenseServerHealthStatusType,
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
    "ActiveDirectoryIdentityProviderOutputTypeDef",
    "ActiveDirectoryIdentityProviderTypeDef",
    "ActiveDirectorySettingsOutputTypeDef",
    "ActiveDirectorySettingsTypeDef",
    "AssociateUserRequestTypeDef",
    "AssociateUserResponseTypeDef",
    "CreateLicenseServerEndpointRequestTypeDef",
    "CreateLicenseServerEndpointResponseTypeDef",
    "CredentialsProviderTypeDef",
    "DeleteLicenseServerEndpointRequestTypeDef",
    "DeleteLicenseServerEndpointResponseTypeDef",
    "DeregisterIdentityProviderRequestTypeDef",
    "DeregisterIdentityProviderResponseTypeDef",
    "DisassociateUserRequestTypeDef",
    "DisassociateUserResponseTypeDef",
    "DomainNetworkSettingsOutputTypeDef",
    "DomainNetworkSettingsTypeDef",
    "FilterTypeDef",
    "IdentityProviderOutputTypeDef",
    "IdentityProviderSummaryTypeDef",
    "IdentityProviderTypeDef",
    "IdentityProviderUnionTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceUserSummaryTypeDef",
    "LicenseServerEndpointTypeDef",
    "LicenseServerSettingsTypeDef",
    "LicenseServerTypeDef",
    "ListIdentityProvidersRequestPaginateTypeDef",
    "ListIdentityProvidersRequestTypeDef",
    "ListIdentityProvidersResponseTypeDef",
    "ListInstancesRequestPaginateTypeDef",
    "ListInstancesRequestTypeDef",
    "ListInstancesResponseTypeDef",
    "ListLicenseServerEndpointsRequestPaginateTypeDef",
    "ListLicenseServerEndpointsRequestTypeDef",
    "ListLicenseServerEndpointsResponseTypeDef",
    "ListProductSubscriptionsRequestPaginateTypeDef",
    "ListProductSubscriptionsRequestTypeDef",
    "ListProductSubscriptionsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUserAssociationsRequestPaginateTypeDef",
    "ListUserAssociationsRequestTypeDef",
    "ListUserAssociationsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ProductUserSummaryTypeDef",
    "RdsSalSettingsTypeDef",
    "RegisterIdentityProviderRequestTypeDef",
    "RegisterIdentityProviderResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SecretsManagerCredentialsProviderTypeDef",
    "ServerEndpointTypeDef",
    "ServerSettingsTypeDef",
    "SettingsOutputTypeDef",
    "SettingsTypeDef",
    "SettingsUnionTypeDef",
    "StartProductSubscriptionRequestTypeDef",
    "StartProductSubscriptionResponseTypeDef",
    "StopProductSubscriptionRequestTypeDef",
    "StopProductSubscriptionResponseTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateIdentityProviderSettingsRequestTypeDef",
    "UpdateIdentityProviderSettingsResponseTypeDef",
    "UpdateSettingsTypeDef",
)

class DomainNetworkSettingsOutputTypeDef(TypedDict):
    Subnets: List[str]

class DomainNetworkSettingsTypeDef(TypedDict):
    Subnets: Sequence[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class SecretsManagerCredentialsProviderTypeDef(TypedDict):
    SecretId: NotRequired[str]

class DeleteLicenseServerEndpointRequestTypeDef(TypedDict):
    LicenseServerEndpointArn: str
    ServerType: Literal["RDS_SAL"]

class FilterTypeDef(TypedDict):
    Attribute: NotRequired[str]
    Operation: NotRequired[str]
    Value: NotRequired[str]

class SettingsOutputTypeDef(TypedDict):
    Subnets: List[str]
    SecurityGroupId: str

class LicenseServerTypeDef(TypedDict):
    ProvisioningStatus: NotRequired[LicenseServerEndpointProvisioningStatusType]
    HealthStatus: NotRequired[LicenseServerHealthStatusType]
    Ipv4Address: NotRequired[str]
    Ipv6Address: NotRequired[str]

class ServerEndpointTypeDef(TypedDict):
    Endpoint: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class SettingsTypeDef(TypedDict):
    Subnets: Sequence[str]
    SecurityGroupId: str

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateSettingsTypeDef(TypedDict):
    AddSubnets: Sequence[str]
    RemoveSubnets: Sequence[str]
    SecurityGroupId: NotRequired[str]

class CreateLicenseServerEndpointResponseTypeDef(TypedDict):
    IdentityProviderArn: str
    LicenseServerEndpointArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CredentialsProviderTypeDef(TypedDict):
    SecretsManagerCredentialsProvider: NotRequired[SecretsManagerCredentialsProviderTypeDef]

class ListIdentityProvidersRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    NextToken: NotRequired[str]

class ListInstancesRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class ListLicenseServerEndpointsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    NextToken: NotRequired[str]

class LicenseServerEndpointTypeDef(TypedDict):
    IdentityProviderArn: NotRequired[str]
    ServerType: NotRequired[Literal["RDS_SAL"]]
    ServerEndpoint: NotRequired[ServerEndpointTypeDef]
    StatusMessage: NotRequired[str]
    LicenseServerEndpointId: NotRequired[str]
    LicenseServerEndpointArn: NotRequired[str]
    LicenseServerEndpointProvisioningStatus: NotRequired[
        LicenseServerEndpointProvisioningStatusType
    ]
    LicenseServers: NotRequired[List[LicenseServerTypeDef]]
    CreationTime: NotRequired[datetime]

class ListIdentityProvidersRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListInstancesRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLicenseServerEndpointsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

SettingsUnionTypeDef = Union[SettingsTypeDef, SettingsOutputTypeDef]

class ActiveDirectorySettingsOutputTypeDef(TypedDict):
    DomainName: NotRequired[str]
    DomainIpv4List: NotRequired[List[str]]
    DomainIpv6List: NotRequired[List[str]]
    DomainCredentialsProvider: NotRequired[CredentialsProviderTypeDef]
    DomainNetworkSettings: NotRequired[DomainNetworkSettingsOutputTypeDef]

class ActiveDirectorySettingsTypeDef(TypedDict):
    DomainName: NotRequired[str]
    DomainIpv4List: NotRequired[Sequence[str]]
    DomainIpv6List: NotRequired[Sequence[str]]
    DomainCredentialsProvider: NotRequired[CredentialsProviderTypeDef]
    DomainNetworkSettings: NotRequired[DomainNetworkSettingsTypeDef]

class RdsSalSettingsTypeDef(TypedDict):
    RdsSalCredentialsProvider: CredentialsProviderTypeDef

class DeleteLicenseServerEndpointResponseTypeDef(TypedDict):
    LicenseServerEndpoint: LicenseServerEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLicenseServerEndpointsResponseTypeDef(TypedDict):
    LicenseServerEndpoints: List[LicenseServerEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ActiveDirectoryIdentityProviderOutputTypeDef(TypedDict):
    DirectoryId: NotRequired[str]
    ActiveDirectorySettings: NotRequired[ActiveDirectorySettingsOutputTypeDef]
    ActiveDirectoryType: NotRequired[ActiveDirectoryTypeType]
    IsSharedActiveDirectory: NotRequired[bool]

class ActiveDirectoryIdentityProviderTypeDef(TypedDict):
    DirectoryId: NotRequired[str]
    ActiveDirectorySettings: NotRequired[ActiveDirectorySettingsTypeDef]
    ActiveDirectoryType: NotRequired[ActiveDirectoryTypeType]
    IsSharedActiveDirectory: NotRequired[bool]

class ServerSettingsTypeDef(TypedDict):
    RdsSalSettings: NotRequired[RdsSalSettingsTypeDef]

class IdentityProviderOutputTypeDef(TypedDict):
    ActiveDirectoryIdentityProvider: NotRequired[ActiveDirectoryIdentityProviderOutputTypeDef]

class IdentityProviderTypeDef(TypedDict):
    ActiveDirectoryIdentityProvider: NotRequired[ActiveDirectoryIdentityProviderTypeDef]

class LicenseServerSettingsTypeDef(TypedDict):
    ServerType: Literal["RDS_SAL"]
    ServerSettings: ServerSettingsTypeDef

class IdentityProviderSummaryTypeDef(TypedDict):
    IdentityProvider: IdentityProviderOutputTypeDef
    Settings: SettingsOutputTypeDef
    Product: str
    Status: str
    IdentityProviderArn: NotRequired[str]
    FailureMessage: NotRequired[str]
    OwnerAccountId: NotRequired[str]

class InstanceSummaryTypeDef(TypedDict):
    InstanceId: str
    Status: str
    Products: List[str]
    LastStatusCheckDate: NotRequired[str]
    StatusMessage: NotRequired[str]
    OwnerAccountId: NotRequired[str]
    IdentityProvider: NotRequired[IdentityProviderOutputTypeDef]

class InstanceUserSummaryTypeDef(TypedDict):
    Username: str
    InstanceId: str
    IdentityProvider: IdentityProviderOutputTypeDef
    Status: str
    InstanceUserArn: NotRequired[str]
    StatusMessage: NotRequired[str]
    Domain: NotRequired[str]
    AssociationDate: NotRequired[str]
    DisassociationDate: NotRequired[str]

class ProductUserSummaryTypeDef(TypedDict):
    Username: str
    Product: str
    IdentityProvider: IdentityProviderOutputTypeDef
    Status: str
    ProductUserArn: NotRequired[str]
    StatusMessage: NotRequired[str]
    Domain: NotRequired[str]
    SubscriptionStartDate: NotRequired[str]
    SubscriptionEndDate: NotRequired[str]

IdentityProviderUnionTypeDef = Union[IdentityProviderTypeDef, IdentityProviderOutputTypeDef]

class CreateLicenseServerEndpointRequestTypeDef(TypedDict):
    IdentityProviderArn: str
    LicenseServerSettings: LicenseServerSettingsTypeDef
    Tags: NotRequired[Mapping[str, str]]

class DeregisterIdentityProviderResponseTypeDef(TypedDict):
    IdentityProviderSummary: IdentityProviderSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListIdentityProvidersResponseTypeDef(TypedDict):
    IdentityProviderSummaries: List[IdentityProviderSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RegisterIdentityProviderResponseTypeDef(TypedDict):
    IdentityProviderSummary: IdentityProviderSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIdentityProviderSettingsResponseTypeDef(TypedDict):
    IdentityProviderSummary: IdentityProviderSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstancesResponseTypeDef(TypedDict):
    InstanceSummaries: List[InstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AssociateUserResponseTypeDef(TypedDict):
    InstanceUserSummary: InstanceUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateUserResponseTypeDef(TypedDict):
    InstanceUserSummary: InstanceUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListUserAssociationsResponseTypeDef(TypedDict):
    InstanceUserSummaries: List[InstanceUserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListProductSubscriptionsResponseTypeDef(TypedDict):
    ProductUserSummaries: List[ProductUserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class StartProductSubscriptionResponseTypeDef(TypedDict):
    ProductUserSummary: ProductUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopProductSubscriptionResponseTypeDef(TypedDict):
    ProductUserSummary: ProductUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateUserRequestTypeDef(TypedDict):
    Username: str
    InstanceId: str
    IdentityProvider: IdentityProviderUnionTypeDef
    Domain: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class DeregisterIdentityProviderRequestTypeDef(TypedDict):
    IdentityProvider: NotRequired[IdentityProviderUnionTypeDef]
    Product: NotRequired[str]
    IdentityProviderArn: NotRequired[str]

class DisassociateUserRequestTypeDef(TypedDict):
    Username: NotRequired[str]
    InstanceId: NotRequired[str]
    IdentityProvider: NotRequired[IdentityProviderUnionTypeDef]
    InstanceUserArn: NotRequired[str]
    Domain: NotRequired[str]

class ListProductSubscriptionsRequestPaginateTypeDef(TypedDict):
    IdentityProvider: IdentityProviderUnionTypeDef
    Product: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProductSubscriptionsRequestTypeDef(TypedDict):
    IdentityProvider: IdentityProviderUnionTypeDef
    Product: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    NextToken: NotRequired[str]

class ListUserAssociationsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    IdentityProvider: IdentityProviderUnionTypeDef
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUserAssociationsRequestTypeDef(TypedDict):
    InstanceId: str
    IdentityProvider: IdentityProviderUnionTypeDef
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    NextToken: NotRequired[str]

class RegisterIdentityProviderRequestTypeDef(TypedDict):
    IdentityProvider: IdentityProviderUnionTypeDef
    Product: str
    Settings: NotRequired[SettingsUnionTypeDef]
    Tags: NotRequired[Mapping[str, str]]

class StartProductSubscriptionRequestTypeDef(TypedDict):
    Username: str
    IdentityProvider: IdentityProviderUnionTypeDef
    Product: str
    Domain: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class StopProductSubscriptionRequestTypeDef(TypedDict):
    Username: NotRequired[str]
    IdentityProvider: NotRequired[IdentityProviderUnionTypeDef]
    Product: NotRequired[str]
    ProductUserArn: NotRequired[str]
    Domain: NotRequired[str]

class UpdateIdentityProviderSettingsRequestTypeDef(TypedDict):
    UpdateSettings: UpdateSettingsTypeDef
    IdentityProvider: NotRequired[IdentityProviderUnionTypeDef]
    Product: NotRequired[str]
    IdentityProviderArn: NotRequired[str]
