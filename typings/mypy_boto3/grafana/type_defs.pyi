"""
Type annotations for grafana service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/type_defs.html)

Usage::

    ```python
    from mypy_boto3_grafana.type_defs import AssertionAttributesTypeDef

    data: AssertionAttributesTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssertionAttributesTypeDef",
    "AssociateLicenseRequestRequestTypeDef",
    "AssociateLicenseResponseTypeDef",
    "AuthenticationDescriptionTypeDef",
    "AuthenticationSummaryTypeDef",
    "AwsSsoAuthenticationTypeDef",
    "CreateWorkspaceApiKeyRequestRequestTypeDef",
    "CreateWorkspaceApiKeyResponseTypeDef",
    "CreateWorkspaceRequestRequestTypeDef",
    "CreateWorkspaceResponseTypeDef",
    "CreateWorkspaceServiceAccountRequestRequestTypeDef",
    "CreateWorkspaceServiceAccountResponseTypeDef",
    "CreateWorkspaceServiceAccountTokenRequestRequestTypeDef",
    "CreateWorkspaceServiceAccountTokenResponseTypeDef",
    "DeleteWorkspaceApiKeyRequestRequestTypeDef",
    "DeleteWorkspaceApiKeyResponseTypeDef",
    "DeleteWorkspaceRequestRequestTypeDef",
    "DeleteWorkspaceResponseTypeDef",
    "DeleteWorkspaceServiceAccountRequestRequestTypeDef",
    "DeleteWorkspaceServiceAccountResponseTypeDef",
    "DeleteWorkspaceServiceAccountTokenRequestRequestTypeDef",
    "DeleteWorkspaceServiceAccountTokenResponseTypeDef",
    "DescribeWorkspaceAuthenticationRequestRequestTypeDef",
    "DescribeWorkspaceAuthenticationResponseTypeDef",
    "DescribeWorkspaceConfigurationRequestRequestTypeDef",
    "DescribeWorkspaceConfigurationResponseTypeDef",
    "DescribeWorkspaceRequestRequestTypeDef",
    "DescribeWorkspaceResponseTypeDef",
    "DisassociateLicenseRequestRequestTypeDef",
    "DisassociateLicenseResponseTypeDef",
    "IdpMetadataTypeDef",
    "ListPermissionsRequestRequestTypeDef",
    "ListPermissionsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVersionsRequestRequestTypeDef",
    "ListVersionsResponseTypeDef",
    "ListWorkspaceServiceAccountTokensRequestRequestTypeDef",
    "ListWorkspaceServiceAccountTokensResponseTypeDef",
    "ListWorkspaceServiceAccountsRequestRequestTypeDef",
    "ListWorkspaceServiceAccountsResponseTypeDef",
    "ListWorkspacesRequestRequestTypeDef",
    "ListWorkspacesResponseTypeDef",
    "NetworkAccessConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionEntryTypeDef",
    "ResponseMetadataTypeDef",
    "RoleValuesTypeDef",
    "SamlAuthenticationTypeDef",
    "SamlConfigurationTypeDef",
    "ServiceAccountSummaryTypeDef",
    "ServiceAccountTokenSummaryTypeDef",
    "ServiceAccountTokenSummaryWithKeyTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateErrorTypeDef",
    "UpdateInstructionTypeDef",
    "UpdatePermissionsRequestRequestTypeDef",
    "UpdatePermissionsResponseTypeDef",
    "UpdateWorkspaceAuthenticationRequestRequestTypeDef",
    "UpdateWorkspaceAuthenticationResponseTypeDef",
    "UpdateWorkspaceConfigurationRequestRequestTypeDef",
    "UpdateWorkspaceRequestRequestTypeDef",
    "UpdateWorkspaceResponseTypeDef",
    "UserTypeDef",
    "VpcConfigurationTypeDef",
    "WorkspaceDescriptionTypeDef",
    "WorkspaceSummaryTypeDef",
)

AssertionAttributesTypeDef = TypedDict(
    "AssertionAttributesTypeDef",
    {
        "email": str,
        "groups": str,
        "login": str,
        "name": str,
        "org": str,
        "role": str,
    },
    total=False,
)

_RequiredAssociateLicenseRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateLicenseRequestRequestTypeDef",
    {
        "licenseType": LicenseTypeType,
        "workspaceId": str,
    },
)
_OptionalAssociateLicenseRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateLicenseRequestRequestTypeDef",
    {
        "grafanaToken": str,
    },
    total=False,
)

class AssociateLicenseRequestRequestTypeDef(
    _RequiredAssociateLicenseRequestRequestTypeDef, _OptionalAssociateLicenseRequestRequestTypeDef
):
    pass

AssociateLicenseResponseTypeDef = TypedDict(
    "AssociateLicenseResponseTypeDef",
    {
        "workspace": "WorkspaceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAuthenticationDescriptionTypeDef = TypedDict(
    "_RequiredAuthenticationDescriptionTypeDef",
    {
        "providers": List[AuthenticationProviderTypesType],
    },
)
_OptionalAuthenticationDescriptionTypeDef = TypedDict(
    "_OptionalAuthenticationDescriptionTypeDef",
    {
        "awsSso": "AwsSsoAuthenticationTypeDef",
        "saml": "SamlAuthenticationTypeDef",
    },
    total=False,
)

class AuthenticationDescriptionTypeDef(
    _RequiredAuthenticationDescriptionTypeDef, _OptionalAuthenticationDescriptionTypeDef
):
    pass

_RequiredAuthenticationSummaryTypeDef = TypedDict(
    "_RequiredAuthenticationSummaryTypeDef",
    {
        "providers": List[AuthenticationProviderTypesType],
    },
)
_OptionalAuthenticationSummaryTypeDef = TypedDict(
    "_OptionalAuthenticationSummaryTypeDef",
    {
        "samlConfigurationStatus": SamlConfigurationStatusType,
    },
    total=False,
)

class AuthenticationSummaryTypeDef(
    _RequiredAuthenticationSummaryTypeDef, _OptionalAuthenticationSummaryTypeDef
):
    pass

AwsSsoAuthenticationTypeDef = TypedDict(
    "AwsSsoAuthenticationTypeDef",
    {
        "ssoClientId": str,
    },
    total=False,
)

CreateWorkspaceApiKeyRequestRequestTypeDef = TypedDict(
    "CreateWorkspaceApiKeyRequestRequestTypeDef",
    {
        "keyName": str,
        "keyRole": str,
        "secondsToLive": int,
        "workspaceId": str,
    },
)

CreateWorkspaceApiKeyResponseTypeDef = TypedDict(
    "CreateWorkspaceApiKeyResponseTypeDef",
    {
        "key": str,
        "keyName": str,
        "workspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorkspaceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWorkspaceRequestRequestTypeDef",
    {
        "accountAccessType": AccountAccessTypeType,
        "authenticationProviders": List[AuthenticationProviderTypesType],
        "permissionType": PermissionTypeType,
    },
)
_OptionalCreateWorkspaceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWorkspaceRequestRequestTypeDef",
    {
        "clientToken": str,
        "configuration": str,
        "grafanaVersion": str,
        "networkAccessControl": "NetworkAccessConfigurationTypeDef",
        "organizationRoleName": str,
        "stackSetName": str,
        "tags": Dict[str, str],
        "vpcConfiguration": "VpcConfigurationTypeDef",
        "workspaceDataSources": List[DataSourceTypeType],
        "workspaceDescription": str,
        "workspaceName": str,
        "workspaceNotificationDestinations": List[Literal["SNS"]],
        "workspaceOrganizationalUnits": List[str],
        "workspaceRoleArn": str,
    },
    total=False,
)

class CreateWorkspaceRequestRequestTypeDef(
    _RequiredCreateWorkspaceRequestRequestTypeDef, _OptionalCreateWorkspaceRequestRequestTypeDef
):
    pass

CreateWorkspaceResponseTypeDef = TypedDict(
    "CreateWorkspaceResponseTypeDef",
    {
        "workspace": "WorkspaceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorkspaceServiceAccountRequestRequestTypeDef = TypedDict(
    "CreateWorkspaceServiceAccountRequestRequestTypeDef",
    {
        "grafanaRole": RoleType,
        "name": str,
        "workspaceId": str,
    },
)

CreateWorkspaceServiceAccountResponseTypeDef = TypedDict(
    "CreateWorkspaceServiceAccountResponseTypeDef",
    {
        "grafanaRole": RoleType,
        "id": str,
        "name": str,
        "workspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorkspaceServiceAccountTokenRequestRequestTypeDef = TypedDict(
    "CreateWorkspaceServiceAccountTokenRequestRequestTypeDef",
    {
        "name": str,
        "secondsToLive": int,
        "serviceAccountId": str,
        "workspaceId": str,
    },
)

CreateWorkspaceServiceAccountTokenResponseTypeDef = TypedDict(
    "CreateWorkspaceServiceAccountTokenResponseTypeDef",
    {
        "serviceAccountId": str,
        "serviceAccountToken": "ServiceAccountTokenSummaryWithKeyTypeDef",
        "workspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWorkspaceApiKeyRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceApiKeyRequestRequestTypeDef",
    {
        "keyName": str,
        "workspaceId": str,
    },
)

DeleteWorkspaceApiKeyResponseTypeDef = TypedDict(
    "DeleteWorkspaceApiKeyResponseTypeDef",
    {
        "keyName": str,
        "workspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWorkspaceRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)

DeleteWorkspaceResponseTypeDef = TypedDict(
    "DeleteWorkspaceResponseTypeDef",
    {
        "workspace": "WorkspaceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWorkspaceServiceAccountRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceServiceAccountRequestRequestTypeDef",
    {
        "serviceAccountId": str,
        "workspaceId": str,
    },
)

DeleteWorkspaceServiceAccountResponseTypeDef = TypedDict(
    "DeleteWorkspaceServiceAccountResponseTypeDef",
    {
        "serviceAccountId": str,
        "workspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWorkspaceServiceAccountTokenRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceServiceAccountTokenRequestRequestTypeDef",
    {
        "serviceAccountId": str,
        "tokenId": str,
        "workspaceId": str,
    },
)

DeleteWorkspaceServiceAccountTokenResponseTypeDef = TypedDict(
    "DeleteWorkspaceServiceAccountTokenResponseTypeDef",
    {
        "serviceAccountId": str,
        "tokenId": str,
        "workspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspaceAuthenticationRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceAuthenticationRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)

DescribeWorkspaceAuthenticationResponseTypeDef = TypedDict(
    "DescribeWorkspaceAuthenticationResponseTypeDef",
    {
        "authentication": "AuthenticationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspaceConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceConfigurationRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)

DescribeWorkspaceConfigurationResponseTypeDef = TypedDict(
    "DescribeWorkspaceConfigurationResponseTypeDef",
    {
        "configuration": str,
        "grafanaVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspaceRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)

DescribeWorkspaceResponseTypeDef = TypedDict(
    "DescribeWorkspaceResponseTypeDef",
    {
        "workspace": "WorkspaceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateLicenseRequestRequestTypeDef = TypedDict(
    "DisassociateLicenseRequestRequestTypeDef",
    {
        "licenseType": LicenseTypeType,
        "workspaceId": str,
    },
)

DisassociateLicenseResponseTypeDef = TypedDict(
    "DisassociateLicenseResponseTypeDef",
    {
        "workspace": "WorkspaceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdpMetadataTypeDef = TypedDict(
    "IdpMetadataTypeDef",
    {
        "url": str,
        "xml": str,
    },
    total=False,
)

_RequiredListPermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredListPermissionsRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
_OptionalListPermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalListPermissionsRequestRequestTypeDef",
    {
        "groupId": str,
        "maxResults": int,
        "nextToken": str,
        "userId": str,
        "userType": UserTypeType,
    },
    total=False,
)

class ListPermissionsRequestRequestTypeDef(
    _RequiredListPermissionsRequestRequestTypeDef, _OptionalListPermissionsRequestRequestTypeDef
):
    pass

ListPermissionsResponseTypeDef = TypedDict(
    "ListPermissionsResponseTypeDef",
    {
        "nextToken": str,
        "permissions": List["PermissionEntryTypeDef"],
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
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVersionsRequestRequestTypeDef = TypedDict(
    "ListVersionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "workspaceId": str,
    },
    total=False,
)

ListVersionsResponseTypeDef = TypedDict(
    "ListVersionsResponseTypeDef",
    {
        "grafanaVersions": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWorkspaceServiceAccountTokensRequestRequestTypeDef = TypedDict(
    "_RequiredListWorkspaceServiceAccountTokensRequestRequestTypeDef",
    {
        "serviceAccountId": str,
        "workspaceId": str,
    },
)
_OptionalListWorkspaceServiceAccountTokensRequestRequestTypeDef = TypedDict(
    "_OptionalListWorkspaceServiceAccountTokensRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListWorkspaceServiceAccountTokensRequestRequestTypeDef(
    _RequiredListWorkspaceServiceAccountTokensRequestRequestTypeDef,
    _OptionalListWorkspaceServiceAccountTokensRequestRequestTypeDef,
):
    pass

ListWorkspaceServiceAccountTokensResponseTypeDef = TypedDict(
    "ListWorkspaceServiceAccountTokensResponseTypeDef",
    {
        "nextToken": str,
        "serviceAccountId": str,
        "serviceAccountTokens": List["ServiceAccountTokenSummaryTypeDef"],
        "workspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWorkspaceServiceAccountsRequestRequestTypeDef = TypedDict(
    "_RequiredListWorkspaceServiceAccountsRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
_OptionalListWorkspaceServiceAccountsRequestRequestTypeDef = TypedDict(
    "_OptionalListWorkspaceServiceAccountsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListWorkspaceServiceAccountsRequestRequestTypeDef(
    _RequiredListWorkspaceServiceAccountsRequestRequestTypeDef,
    _OptionalListWorkspaceServiceAccountsRequestRequestTypeDef,
):
    pass

ListWorkspaceServiceAccountsResponseTypeDef = TypedDict(
    "ListWorkspaceServiceAccountsResponseTypeDef",
    {
        "nextToken": str,
        "serviceAccounts": List["ServiceAccountSummaryTypeDef"],
        "workspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkspacesRequestRequestTypeDef = TypedDict(
    "ListWorkspacesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListWorkspacesResponseTypeDef = TypedDict(
    "ListWorkspacesResponseTypeDef",
    {
        "nextToken": str,
        "workspaces": List["WorkspaceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkAccessConfigurationTypeDef = TypedDict(
    "NetworkAccessConfigurationTypeDef",
    {
        "prefixListIds": List[str],
        "vpceIds": List[str],
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PermissionEntryTypeDef = TypedDict(
    "PermissionEntryTypeDef",
    {
        "role": RoleType,
        "user": "UserTypeDef",
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

RoleValuesTypeDef = TypedDict(
    "RoleValuesTypeDef",
    {
        "admin": List[str],
        "editor": List[str],
    },
    total=False,
)

_RequiredSamlAuthenticationTypeDef = TypedDict(
    "_RequiredSamlAuthenticationTypeDef",
    {
        "status": SamlConfigurationStatusType,
    },
)
_OptionalSamlAuthenticationTypeDef = TypedDict(
    "_OptionalSamlAuthenticationTypeDef",
    {
        "configuration": "SamlConfigurationTypeDef",
    },
    total=False,
)

class SamlAuthenticationTypeDef(
    _RequiredSamlAuthenticationTypeDef, _OptionalSamlAuthenticationTypeDef
):
    pass

_RequiredSamlConfigurationTypeDef = TypedDict(
    "_RequiredSamlConfigurationTypeDef",
    {
        "idpMetadata": "IdpMetadataTypeDef",
    },
)
_OptionalSamlConfigurationTypeDef = TypedDict(
    "_OptionalSamlConfigurationTypeDef",
    {
        "allowedOrganizations": List[str],
        "assertionAttributes": "AssertionAttributesTypeDef",
        "loginValidityDuration": int,
        "roleValues": "RoleValuesTypeDef",
    },
    total=False,
)

class SamlConfigurationTypeDef(
    _RequiredSamlConfigurationTypeDef, _OptionalSamlConfigurationTypeDef
):
    pass

ServiceAccountSummaryTypeDef = TypedDict(
    "ServiceAccountSummaryTypeDef",
    {
        "grafanaRole": RoleType,
        "id": str,
        "isDisabled": str,
        "name": str,
    },
)

_RequiredServiceAccountTokenSummaryTypeDef = TypedDict(
    "_RequiredServiceAccountTokenSummaryTypeDef",
    {
        "createdAt": datetime,
        "expiresAt": datetime,
        "id": str,
        "name": str,
    },
)
_OptionalServiceAccountTokenSummaryTypeDef = TypedDict(
    "_OptionalServiceAccountTokenSummaryTypeDef",
    {
        "lastUsedAt": datetime,
    },
    total=False,
)

class ServiceAccountTokenSummaryTypeDef(
    _RequiredServiceAccountTokenSummaryTypeDef, _OptionalServiceAccountTokenSummaryTypeDef
):
    pass

ServiceAccountTokenSummaryWithKeyTypeDef = TypedDict(
    "ServiceAccountTokenSummaryWithKeyTypeDef",
    {
        "id": str,
        "key": str,
        "name": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateErrorTypeDef = TypedDict(
    "UpdateErrorTypeDef",
    {
        "causedBy": "UpdateInstructionTypeDef",
        "code": int,
        "message": str,
    },
)

UpdateInstructionTypeDef = TypedDict(
    "UpdateInstructionTypeDef",
    {
        "action": UpdateActionType,
        "role": RoleType,
        "users": List["UserTypeDef"],
    },
)

UpdatePermissionsRequestRequestTypeDef = TypedDict(
    "UpdatePermissionsRequestRequestTypeDef",
    {
        "updateInstructionBatch": List["UpdateInstructionTypeDef"],
        "workspaceId": str,
    },
)

UpdatePermissionsResponseTypeDef = TypedDict(
    "UpdatePermissionsResponseTypeDef",
    {
        "errors": List["UpdateErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWorkspaceAuthenticationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkspaceAuthenticationRequestRequestTypeDef",
    {
        "authenticationProviders": List[AuthenticationProviderTypesType],
        "workspaceId": str,
    },
)
_OptionalUpdateWorkspaceAuthenticationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkspaceAuthenticationRequestRequestTypeDef",
    {
        "samlConfiguration": "SamlConfigurationTypeDef",
    },
    total=False,
)

class UpdateWorkspaceAuthenticationRequestRequestTypeDef(
    _RequiredUpdateWorkspaceAuthenticationRequestRequestTypeDef,
    _OptionalUpdateWorkspaceAuthenticationRequestRequestTypeDef,
):
    pass

UpdateWorkspaceAuthenticationResponseTypeDef = TypedDict(
    "UpdateWorkspaceAuthenticationResponseTypeDef",
    {
        "authentication": "AuthenticationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWorkspaceConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkspaceConfigurationRequestRequestTypeDef",
    {
        "configuration": str,
        "workspaceId": str,
    },
)
_OptionalUpdateWorkspaceConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkspaceConfigurationRequestRequestTypeDef",
    {
        "grafanaVersion": str,
    },
    total=False,
)

class UpdateWorkspaceConfigurationRequestRequestTypeDef(
    _RequiredUpdateWorkspaceConfigurationRequestRequestTypeDef,
    _OptionalUpdateWorkspaceConfigurationRequestRequestTypeDef,
):
    pass

_RequiredUpdateWorkspaceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
_OptionalUpdateWorkspaceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkspaceRequestRequestTypeDef",
    {
        "accountAccessType": AccountAccessTypeType,
        "networkAccessControl": "NetworkAccessConfigurationTypeDef",
        "organizationRoleName": str,
        "permissionType": PermissionTypeType,
        "removeNetworkAccessConfiguration": bool,
        "removeVpcConfiguration": bool,
        "stackSetName": str,
        "vpcConfiguration": "VpcConfigurationTypeDef",
        "workspaceDataSources": List[DataSourceTypeType],
        "workspaceDescription": str,
        "workspaceName": str,
        "workspaceNotificationDestinations": List[Literal["SNS"]],
        "workspaceOrganizationalUnits": List[str],
        "workspaceRoleArn": str,
    },
    total=False,
)

class UpdateWorkspaceRequestRequestTypeDef(
    _RequiredUpdateWorkspaceRequestRequestTypeDef, _OptionalUpdateWorkspaceRequestRequestTypeDef
):
    pass

UpdateWorkspaceResponseTypeDef = TypedDict(
    "UpdateWorkspaceResponseTypeDef",
    {
        "workspace": "WorkspaceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "id": str,
        "type": UserTypeType,
    },
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "securityGroupIds": List[str],
        "subnetIds": List[str],
    },
)

_RequiredWorkspaceDescriptionTypeDef = TypedDict(
    "_RequiredWorkspaceDescriptionTypeDef",
    {
        "authentication": "AuthenticationSummaryTypeDef",
        "created": datetime,
        "dataSources": List[DataSourceTypeType],
        "endpoint": str,
        "grafanaVersion": str,
        "id": str,
        "modified": datetime,
        "status": WorkspaceStatusType,
    },
)
_OptionalWorkspaceDescriptionTypeDef = TypedDict(
    "_OptionalWorkspaceDescriptionTypeDef",
    {
        "accountAccessType": AccountAccessTypeType,
        "description": str,
        "freeTrialConsumed": bool,
        "freeTrialExpiration": datetime,
        "grafanaToken": str,
        "licenseExpiration": datetime,
        "licenseType": LicenseTypeType,
        "name": str,
        "networkAccessControl": "NetworkAccessConfigurationTypeDef",
        "notificationDestinations": List[Literal["SNS"]],
        "organizationRoleName": str,
        "organizationalUnits": List[str],
        "permissionType": PermissionTypeType,
        "stackSetName": str,
        "tags": Dict[str, str],
        "vpcConfiguration": "VpcConfigurationTypeDef",
        "workspaceRoleArn": str,
    },
    total=False,
)

class WorkspaceDescriptionTypeDef(
    _RequiredWorkspaceDescriptionTypeDef, _OptionalWorkspaceDescriptionTypeDef
):
    pass

_RequiredWorkspaceSummaryTypeDef = TypedDict(
    "_RequiredWorkspaceSummaryTypeDef",
    {
        "authentication": "AuthenticationSummaryTypeDef",
        "created": datetime,
        "endpoint": str,
        "grafanaVersion": str,
        "id": str,
        "modified": datetime,
        "status": WorkspaceStatusType,
    },
)
_OptionalWorkspaceSummaryTypeDef = TypedDict(
    "_OptionalWorkspaceSummaryTypeDef",
    {
        "description": str,
        "grafanaToken": str,
        "licenseType": LicenseTypeType,
        "name": str,
        "notificationDestinations": List[Literal["SNS"]],
        "tags": Dict[str, str],
    },
    total=False,
)

class WorkspaceSummaryTypeDef(_RequiredWorkspaceSummaryTypeDef, _OptionalWorkspaceSummaryTypeDef):
    pass
