"""
Type annotations for grafana service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_grafana.type_defs import AssertionAttributesTypeDef

    data: AssertionAttributesTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AccountAccessTypeType,
    AuthenticationProviderTypesType,
    DataSourceTypeType,
    LicenseTypeType,
    PermissionTypeType,
    RoleType,
    SamlConfigurationStatusType,
    UpdateActionType,
    UserTypeType,
    WorkspaceStatusType,
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
    "AssertionAttributesTypeDef",
    "AssociateLicenseRequestTypeDef",
    "AssociateLicenseResponseTypeDef",
    "AuthenticationDescriptionTypeDef",
    "AuthenticationSummaryTypeDef",
    "AwsSsoAuthenticationTypeDef",
    "CreateWorkspaceApiKeyRequestTypeDef",
    "CreateWorkspaceApiKeyResponseTypeDef",
    "CreateWorkspaceRequestTypeDef",
    "CreateWorkspaceResponseTypeDef",
    "CreateWorkspaceServiceAccountRequestTypeDef",
    "CreateWorkspaceServiceAccountResponseTypeDef",
    "CreateWorkspaceServiceAccountTokenRequestTypeDef",
    "CreateWorkspaceServiceAccountTokenResponseTypeDef",
    "DeleteWorkspaceApiKeyRequestTypeDef",
    "DeleteWorkspaceApiKeyResponseTypeDef",
    "DeleteWorkspaceRequestTypeDef",
    "DeleteWorkspaceResponseTypeDef",
    "DeleteWorkspaceServiceAccountRequestTypeDef",
    "DeleteWorkspaceServiceAccountResponseTypeDef",
    "DeleteWorkspaceServiceAccountTokenRequestTypeDef",
    "DeleteWorkspaceServiceAccountTokenResponseTypeDef",
    "DescribeWorkspaceAuthenticationRequestTypeDef",
    "DescribeWorkspaceAuthenticationResponseTypeDef",
    "DescribeWorkspaceConfigurationRequestTypeDef",
    "DescribeWorkspaceConfigurationResponseTypeDef",
    "DescribeWorkspaceRequestTypeDef",
    "DescribeWorkspaceResponseTypeDef",
    "DisassociateLicenseRequestTypeDef",
    "DisassociateLicenseResponseTypeDef",
    "IdpMetadataTypeDef",
    "ListPermissionsRequestPaginateTypeDef",
    "ListPermissionsRequestTypeDef",
    "ListPermissionsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVersionsRequestPaginateTypeDef",
    "ListVersionsRequestTypeDef",
    "ListVersionsResponseTypeDef",
    "ListWorkspaceServiceAccountTokensRequestPaginateTypeDef",
    "ListWorkspaceServiceAccountTokensRequestTypeDef",
    "ListWorkspaceServiceAccountTokensResponseTypeDef",
    "ListWorkspaceServiceAccountsRequestPaginateTypeDef",
    "ListWorkspaceServiceAccountsRequestTypeDef",
    "ListWorkspaceServiceAccountsResponseTypeDef",
    "ListWorkspacesRequestPaginateTypeDef",
    "ListWorkspacesRequestTypeDef",
    "ListWorkspacesResponseTypeDef",
    "NetworkAccessConfigurationOutputTypeDef",
    "NetworkAccessConfigurationTypeDef",
    "NetworkAccessConfigurationUnionTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionEntryTypeDef",
    "ResponseMetadataTypeDef",
    "RoleValuesOutputTypeDef",
    "RoleValuesTypeDef",
    "SamlAuthenticationTypeDef",
    "SamlConfigurationOutputTypeDef",
    "SamlConfigurationTypeDef",
    "SamlConfigurationUnionTypeDef",
    "ServiceAccountSummaryTypeDef",
    "ServiceAccountTokenSummaryTypeDef",
    "ServiceAccountTokenSummaryWithKeyTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateErrorTypeDef",
    "UpdateInstructionOutputTypeDef",
    "UpdateInstructionTypeDef",
    "UpdateInstructionUnionTypeDef",
    "UpdatePermissionsRequestTypeDef",
    "UpdatePermissionsResponseTypeDef",
    "UpdateWorkspaceAuthenticationRequestTypeDef",
    "UpdateWorkspaceAuthenticationResponseTypeDef",
    "UpdateWorkspaceConfigurationRequestTypeDef",
    "UpdateWorkspaceRequestTypeDef",
    "UpdateWorkspaceResponseTypeDef",
    "UserTypeDef",
    "VpcConfigurationOutputTypeDef",
    "VpcConfigurationTypeDef",
    "VpcConfigurationUnionTypeDef",
    "WorkspaceDescriptionTypeDef",
    "WorkspaceSummaryTypeDef",
)

class AssertionAttributesTypeDef(TypedDict):
    email: NotRequired[str]
    groups: NotRequired[str]
    login: NotRequired[str]
    name: NotRequired[str]
    org: NotRequired[str]
    role: NotRequired[str]

class AssociateLicenseRequestTypeDef(TypedDict):
    licenseType: LicenseTypeType
    workspaceId: str
    grafanaToken: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AwsSsoAuthenticationTypeDef(TypedDict):
    ssoClientId: NotRequired[str]

class AuthenticationSummaryTypeDef(TypedDict):
    providers: List[AuthenticationProviderTypesType]
    samlConfigurationStatus: NotRequired[SamlConfigurationStatusType]

class CreateWorkspaceApiKeyRequestTypeDef(TypedDict):
    keyName: str
    keyRole: str
    secondsToLive: int
    workspaceId: str

class CreateWorkspaceServiceAccountRequestTypeDef(TypedDict):
    grafanaRole: RoleType
    name: str
    workspaceId: str

class CreateWorkspaceServiceAccountTokenRequestTypeDef(TypedDict):
    name: str
    secondsToLive: int
    serviceAccountId: str
    workspaceId: str

ServiceAccountTokenSummaryWithKeyTypeDef = TypedDict(
    "ServiceAccountTokenSummaryWithKeyTypeDef",
    {
        "id": str,
        "key": str,
        "name": str,
    },
)

class DeleteWorkspaceApiKeyRequestTypeDef(TypedDict):
    keyName: str
    workspaceId: str

class DeleteWorkspaceRequestTypeDef(TypedDict):
    workspaceId: str

class DeleteWorkspaceServiceAccountRequestTypeDef(TypedDict):
    serviceAccountId: str
    workspaceId: str

class DeleteWorkspaceServiceAccountTokenRequestTypeDef(TypedDict):
    serviceAccountId: str
    tokenId: str
    workspaceId: str

class DescribeWorkspaceAuthenticationRequestTypeDef(TypedDict):
    workspaceId: str

class DescribeWorkspaceConfigurationRequestTypeDef(TypedDict):
    workspaceId: str

class DescribeWorkspaceRequestTypeDef(TypedDict):
    workspaceId: str

class DisassociateLicenseRequestTypeDef(TypedDict):
    licenseType: LicenseTypeType
    workspaceId: str

class IdpMetadataTypeDef(TypedDict):
    url: NotRequired[str]
    xml: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListPermissionsRequestTypeDef(TypedDict):
    workspaceId: str
    groupId: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    userId: NotRequired[str]
    userType: NotRequired[UserTypeType]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListVersionsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    workspaceId: NotRequired[str]

class ListWorkspaceServiceAccountTokensRequestTypeDef(TypedDict):
    serviceAccountId: str
    workspaceId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

ServiceAccountTokenSummaryTypeDef = TypedDict(
    "ServiceAccountTokenSummaryTypeDef",
    {
        "createdAt": datetime,
        "expiresAt": datetime,
        "id": str,
        "name": str,
        "lastUsedAt": NotRequired[datetime],
    },
)

class ListWorkspaceServiceAccountsRequestTypeDef(TypedDict):
    workspaceId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

ServiceAccountSummaryTypeDef = TypedDict(
    "ServiceAccountSummaryTypeDef",
    {
        "grafanaRole": RoleType,
        "id": str,
        "isDisabled": str,
        "name": str,
    },
)

class ListWorkspacesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class NetworkAccessConfigurationOutputTypeDef(TypedDict):
    prefixListIds: List[str]
    vpceIds: List[str]

class NetworkAccessConfigurationTypeDef(TypedDict):
    prefixListIds: Sequence[str]
    vpceIds: Sequence[str]

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "id": str,
        "type": UserTypeType,
    },
)

class RoleValuesOutputTypeDef(TypedDict):
    admin: NotRequired[List[str]]
    editor: NotRequired[List[str]]

class RoleValuesTypeDef(TypedDict):
    admin: NotRequired[Sequence[str]]
    editor: NotRequired[Sequence[str]]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateWorkspaceConfigurationRequestTypeDef(TypedDict):
    configuration: str
    workspaceId: str
    grafanaVersion: NotRequired[str]

class VpcConfigurationOutputTypeDef(TypedDict):
    securityGroupIds: List[str]
    subnetIds: List[str]

class VpcConfigurationTypeDef(TypedDict):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]

class CreateWorkspaceApiKeyResponseTypeDef(TypedDict):
    key: str
    keyName: str
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

CreateWorkspaceServiceAccountResponseTypeDef = TypedDict(
    "CreateWorkspaceServiceAccountResponseTypeDef",
    {
        "grafanaRole": RoleType,
        "id": str,
        "name": str,
        "workspaceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class DeleteWorkspaceApiKeyResponseTypeDef(TypedDict):
    keyName: str
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkspaceServiceAccountResponseTypeDef(TypedDict):
    serviceAccountId: str
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkspaceServiceAccountTokenResponseTypeDef(TypedDict):
    serviceAccountId: str
    tokenId: str
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkspaceConfigurationResponseTypeDef(TypedDict):
    configuration: str
    grafanaVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVersionsResponseTypeDef(TypedDict):
    grafanaVersions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

WorkspaceSummaryTypeDef = TypedDict(
    "WorkspaceSummaryTypeDef",
    {
        "authentication": AuthenticationSummaryTypeDef,
        "created": datetime,
        "endpoint": str,
        "grafanaVersion": str,
        "id": str,
        "modified": datetime,
        "status": WorkspaceStatusType,
        "description": NotRequired[str],
        "grafanaToken": NotRequired[str],
        "licenseType": NotRequired[LicenseTypeType],
        "name": NotRequired[str],
        "notificationDestinations": NotRequired[List[Literal["SNS"]]],
        "tags": NotRequired[Dict[str, str]],
    },
)

class CreateWorkspaceServiceAccountTokenResponseTypeDef(TypedDict):
    serviceAccountId: str
    serviceAccountToken: ServiceAccountTokenSummaryWithKeyTypeDef
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPermissionsRequestPaginateTypeDef(TypedDict):
    workspaceId: str
    groupId: NotRequired[str]
    userId: NotRequired[str]
    userType: NotRequired[UserTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListVersionsRequestPaginateTypeDef(TypedDict):
    workspaceId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkspaceServiceAccountTokensRequestPaginateTypeDef(TypedDict):
    serviceAccountId: str
    workspaceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkspaceServiceAccountsRequestPaginateTypeDef(TypedDict):
    workspaceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkspacesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkspaceServiceAccountTokensResponseTypeDef(TypedDict):
    serviceAccountId: str
    serviceAccountTokens: List[ServiceAccountTokenSummaryTypeDef]
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListWorkspaceServiceAccountsResponseTypeDef(TypedDict):
    serviceAccounts: List[ServiceAccountSummaryTypeDef]
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

NetworkAccessConfigurationUnionTypeDef = Union[
    NetworkAccessConfigurationTypeDef, NetworkAccessConfigurationOutputTypeDef
]

class PermissionEntryTypeDef(TypedDict):
    role: RoleType
    user: UserTypeDef

class UpdateInstructionOutputTypeDef(TypedDict):
    action: UpdateActionType
    role: RoleType
    users: List[UserTypeDef]

class UpdateInstructionTypeDef(TypedDict):
    action: UpdateActionType
    role: RoleType
    users: Sequence[UserTypeDef]

class SamlConfigurationOutputTypeDef(TypedDict):
    idpMetadata: IdpMetadataTypeDef
    allowedOrganizations: NotRequired[List[str]]
    assertionAttributes: NotRequired[AssertionAttributesTypeDef]
    loginValidityDuration: NotRequired[int]
    roleValues: NotRequired[RoleValuesOutputTypeDef]

class SamlConfigurationTypeDef(TypedDict):
    idpMetadata: IdpMetadataTypeDef
    allowedOrganizations: NotRequired[Sequence[str]]
    assertionAttributes: NotRequired[AssertionAttributesTypeDef]
    loginValidityDuration: NotRequired[int]
    roleValues: NotRequired[RoleValuesTypeDef]

WorkspaceDescriptionTypeDef = TypedDict(
    "WorkspaceDescriptionTypeDef",
    {
        "authentication": AuthenticationSummaryTypeDef,
        "created": datetime,
        "dataSources": List[DataSourceTypeType],
        "endpoint": str,
        "grafanaVersion": str,
        "id": str,
        "modified": datetime,
        "status": WorkspaceStatusType,
        "accountAccessType": NotRequired[AccountAccessTypeType],
        "description": NotRequired[str],
        "freeTrialConsumed": NotRequired[bool],
        "freeTrialExpiration": NotRequired[datetime],
        "grafanaToken": NotRequired[str],
        "licenseExpiration": NotRequired[datetime],
        "licenseType": NotRequired[LicenseTypeType],
        "name": NotRequired[str],
        "networkAccessControl": NotRequired[NetworkAccessConfigurationOutputTypeDef],
        "notificationDestinations": NotRequired[List[Literal["SNS"]]],
        "organizationRoleName": NotRequired[str],
        "organizationalUnits": NotRequired[List[str]],
        "permissionType": NotRequired[PermissionTypeType],
        "stackSetName": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "vpcConfiguration": NotRequired[VpcConfigurationOutputTypeDef],
        "workspaceRoleArn": NotRequired[str],
    },
)
VpcConfigurationUnionTypeDef = Union[VpcConfigurationTypeDef, VpcConfigurationOutputTypeDef]

class ListWorkspacesResponseTypeDef(TypedDict):
    workspaces: List[WorkspaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListPermissionsResponseTypeDef(TypedDict):
    permissions: List[PermissionEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateErrorTypeDef(TypedDict):
    causedBy: UpdateInstructionOutputTypeDef
    code: int
    message: str

UpdateInstructionUnionTypeDef = Union[UpdateInstructionTypeDef, UpdateInstructionOutputTypeDef]

class SamlAuthenticationTypeDef(TypedDict):
    status: SamlConfigurationStatusType
    configuration: NotRequired[SamlConfigurationOutputTypeDef]

SamlConfigurationUnionTypeDef = Union[SamlConfigurationTypeDef, SamlConfigurationOutputTypeDef]

class AssociateLicenseResponseTypeDef(TypedDict):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkspaceResponseTypeDef(TypedDict):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkspaceResponseTypeDef(TypedDict):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkspaceResponseTypeDef(TypedDict):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateLicenseResponseTypeDef(TypedDict):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkspaceResponseTypeDef(TypedDict):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkspaceRequestTypeDef(TypedDict):
    accountAccessType: AccountAccessTypeType
    authenticationProviders: Sequence[AuthenticationProviderTypesType]
    permissionType: PermissionTypeType
    clientToken: NotRequired[str]
    configuration: NotRequired[str]
    grafanaVersion: NotRequired[str]
    networkAccessControl: NotRequired[NetworkAccessConfigurationUnionTypeDef]
    organizationRoleName: NotRequired[str]
    stackSetName: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    vpcConfiguration: NotRequired[VpcConfigurationUnionTypeDef]
    workspaceDataSources: NotRequired[Sequence[DataSourceTypeType]]
    workspaceDescription: NotRequired[str]
    workspaceName: NotRequired[str]
    workspaceNotificationDestinations: NotRequired[Sequence[Literal["SNS"]]]
    workspaceOrganizationalUnits: NotRequired[Sequence[str]]
    workspaceRoleArn: NotRequired[str]

class UpdateWorkspaceRequestTypeDef(TypedDict):
    workspaceId: str
    accountAccessType: NotRequired[AccountAccessTypeType]
    networkAccessControl: NotRequired[NetworkAccessConfigurationUnionTypeDef]
    organizationRoleName: NotRequired[str]
    permissionType: NotRequired[PermissionTypeType]
    removeNetworkAccessConfiguration: NotRequired[bool]
    removeVpcConfiguration: NotRequired[bool]
    stackSetName: NotRequired[str]
    vpcConfiguration: NotRequired[VpcConfigurationUnionTypeDef]
    workspaceDataSources: NotRequired[Sequence[DataSourceTypeType]]
    workspaceDescription: NotRequired[str]
    workspaceName: NotRequired[str]
    workspaceNotificationDestinations: NotRequired[Sequence[Literal["SNS"]]]
    workspaceOrganizationalUnits: NotRequired[Sequence[str]]
    workspaceRoleArn: NotRequired[str]

class UpdatePermissionsResponseTypeDef(TypedDict):
    errors: List[UpdateErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePermissionsRequestTypeDef(TypedDict):
    updateInstructionBatch: Sequence[UpdateInstructionUnionTypeDef]
    workspaceId: str

class AuthenticationDescriptionTypeDef(TypedDict):
    providers: List[AuthenticationProviderTypesType]
    awsSso: NotRequired[AwsSsoAuthenticationTypeDef]
    saml: NotRequired[SamlAuthenticationTypeDef]

class UpdateWorkspaceAuthenticationRequestTypeDef(TypedDict):
    authenticationProviders: Sequence[AuthenticationProviderTypesType]
    workspaceId: str
    samlConfiguration: NotRequired[SamlConfigurationUnionTypeDef]

class DescribeWorkspaceAuthenticationResponseTypeDef(TypedDict):
    authentication: AuthenticationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkspaceAuthenticationResponseTypeDef(TypedDict):
    authentication: AuthenticationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
