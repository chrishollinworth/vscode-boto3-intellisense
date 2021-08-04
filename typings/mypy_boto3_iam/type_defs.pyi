"""
Type annotations for iam service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iam.type_defs import AccessDetailTypeDef

    data: AccessDetailTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AccessAdvisorUsageGranularityTypeType,
    ContextKeyTypeEnumType,
    DeletionTaskStatusTypeType,
    EntityTypeType,
    PolicyEvaluationDecisionTypeType,
    PolicySourceTypeType,
    PolicyUsageTypeType,
    ReportStateTypeType,
    assignmentStatusTypeType,
    encodingTypeType,
    globalEndpointTokenVersionType,
    jobStatusTypeType,
    policyOwnerEntityTypeType,
    policyScopeTypeType,
    policyTypeType,
    sortKeyTypeType,
    statusTypeType,
    summaryKeyTypeType,
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
    "AccessDetailTypeDef",
    "AccessKeyLastUsedTypeDef",
    "AccessKeyMetadataTypeDef",
    "AccessKeyTypeDef",
    "AddClientIDToOpenIDConnectProviderRequestRequestTypeDef",
    "AddRoleToInstanceProfileRequestInstanceProfileTypeDef",
    "AddRoleToInstanceProfileRequestRequestTypeDef",
    "AddUserToGroupRequestGroupTypeDef",
    "AddUserToGroupRequestRequestTypeDef",
    "AddUserToGroupRequestUserTypeDef",
    "AttachGroupPolicyRequestGroupTypeDef",
    "AttachGroupPolicyRequestPolicyTypeDef",
    "AttachGroupPolicyRequestRequestTypeDef",
    "AttachRolePolicyRequestPolicyTypeDef",
    "AttachRolePolicyRequestRequestTypeDef",
    "AttachRolePolicyRequestRoleTypeDef",
    "AttachUserPolicyRequestPolicyTypeDef",
    "AttachUserPolicyRequestRequestTypeDef",
    "AttachUserPolicyRequestUserTypeDef",
    "AttachedPermissionsBoundaryTypeDef",
    "AttachedPolicyTypeDef",
    "ChangePasswordRequestRequestTypeDef",
    "ChangePasswordRequestServiceResourceTypeDef",
    "ContextEntryTypeDef",
    "CreateAccessKeyRequestRequestTypeDef",
    "CreateAccessKeyResponseTypeDef",
    "CreateAccountAliasRequestRequestTypeDef",
    "CreateAccountAliasRequestServiceResourceTypeDef",
    "CreateGroupRequestGroupTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "CreateGroupRequestServiceResourceTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateInstanceProfileRequestRequestTypeDef",
    "CreateInstanceProfileRequestServiceResourceTypeDef",
    "CreateInstanceProfileResponseTypeDef",
    "CreateLoginProfileRequestLoginProfileTypeDef",
    "CreateLoginProfileRequestRequestTypeDef",
    "CreateLoginProfileRequestUserTypeDef",
    "CreateLoginProfileResponseTypeDef",
    "CreateOpenIDConnectProviderRequestRequestTypeDef",
    "CreateOpenIDConnectProviderResponseTypeDef",
    "CreatePolicyRequestRequestTypeDef",
    "CreatePolicyRequestServiceResourceTypeDef",
    "CreatePolicyResponseTypeDef",
    "CreatePolicyVersionRequestPolicyTypeDef",
    "CreatePolicyVersionRequestRequestTypeDef",
    "CreatePolicyVersionResponseTypeDef",
    "CreateRoleRequestRequestTypeDef",
    "CreateRoleRequestServiceResourceTypeDef",
    "CreateRoleResponseTypeDef",
    "CreateSAMLProviderRequestRequestTypeDef",
    "CreateSAMLProviderRequestServiceResourceTypeDef",
    "CreateSAMLProviderResponseTypeDef",
    "CreateServiceLinkedRoleRequestRequestTypeDef",
    "CreateServiceLinkedRoleResponseTypeDef",
    "CreateServiceSpecificCredentialRequestRequestTypeDef",
    "CreateServiceSpecificCredentialResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateUserRequestServiceResourceTypeDef",
    "CreateUserRequestUserTypeDef",
    "CreateUserResponseTypeDef",
    "CreateVirtualMFADeviceRequestRequestTypeDef",
    "CreateVirtualMFADeviceRequestServiceResourceTypeDef",
    "CreateVirtualMFADeviceResponseTypeDef",
    "DeactivateMFADeviceRequestRequestTypeDef",
    "DeleteAccessKeyRequestRequestTypeDef",
    "DeleteAccountAliasRequestRequestTypeDef",
    "DeleteGroupPolicyRequestRequestTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteInstanceProfileRequestRequestTypeDef",
    "DeleteLoginProfileRequestRequestTypeDef",
    "DeleteOpenIDConnectProviderRequestRequestTypeDef",
    "DeletePolicyRequestRequestTypeDef",
    "DeletePolicyVersionRequestRequestTypeDef",
    "DeleteRolePermissionsBoundaryRequestRequestTypeDef",
    "DeleteRolePolicyRequestRequestTypeDef",
    "DeleteRoleRequestRequestTypeDef",
    "DeleteSAMLProviderRequestRequestTypeDef",
    "DeleteSSHPublicKeyRequestRequestTypeDef",
    "DeleteServerCertificateRequestRequestTypeDef",
    "DeleteServiceLinkedRoleRequestRequestTypeDef",
    "DeleteServiceLinkedRoleResponseTypeDef",
    "DeleteServiceSpecificCredentialRequestRequestTypeDef",
    "DeleteSigningCertificateRequestRequestTypeDef",
    "DeleteUserPermissionsBoundaryRequestRequestTypeDef",
    "DeleteUserPolicyRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeleteVirtualMFADeviceRequestRequestTypeDef",
    "DeletionTaskFailureReasonTypeTypeDef",
    "DetachGroupPolicyRequestGroupTypeDef",
    "DetachGroupPolicyRequestPolicyTypeDef",
    "DetachGroupPolicyRequestRequestTypeDef",
    "DetachRolePolicyRequestPolicyTypeDef",
    "DetachRolePolicyRequestRequestTypeDef",
    "DetachRolePolicyRequestRoleTypeDef",
    "DetachUserPolicyRequestPolicyTypeDef",
    "DetachUserPolicyRequestRequestTypeDef",
    "DetachUserPolicyRequestUserTypeDef",
    "EnableMFADeviceRequestMfaDeviceTypeDef",
    "EnableMFADeviceRequestRequestTypeDef",
    "EnableMFADeviceRequestUserTypeDef",
    "EntityDetailsTypeDef",
    "EntityInfoTypeDef",
    "ErrorDetailsTypeDef",
    "EvaluationResultTypeDef",
    "GenerateCredentialReportResponseTypeDef",
    "GenerateOrganizationsAccessReportRequestRequestTypeDef",
    "GenerateOrganizationsAccessReportResponseTypeDef",
    "GenerateServiceLastAccessedDetailsRequestRequestTypeDef",
    "GenerateServiceLastAccessedDetailsResponseTypeDef",
    "GetAccessKeyLastUsedRequestRequestTypeDef",
    "GetAccessKeyLastUsedResponseTypeDef",
    "GetAccountAuthorizationDetailsRequestRequestTypeDef",
    "GetAccountAuthorizationDetailsResponseTypeDef",
    "GetAccountPasswordPolicyResponseTypeDef",
    "GetAccountSummaryResponseTypeDef",
    "GetContextKeysForCustomPolicyRequestRequestTypeDef",
    "GetContextKeysForPolicyResponseTypeDef",
    "GetContextKeysForPrincipalPolicyRequestRequestTypeDef",
    "GetCredentialReportResponseTypeDef",
    "GetGroupPolicyRequestRequestTypeDef",
    "GetGroupPolicyResponseTypeDef",
    "GetGroupRequestRequestTypeDef",
    "GetGroupResponseTypeDef",
    "GetInstanceProfileRequestRequestTypeDef",
    "GetInstanceProfileResponseTypeDef",
    "GetLoginProfileRequestRequestTypeDef",
    "GetLoginProfileResponseTypeDef",
    "GetOpenIDConnectProviderRequestRequestTypeDef",
    "GetOpenIDConnectProviderResponseTypeDef",
    "GetOrganizationsAccessReportRequestRequestTypeDef",
    "GetOrganizationsAccessReportResponseTypeDef",
    "GetPolicyRequestRequestTypeDef",
    "GetPolicyResponseTypeDef",
    "GetPolicyVersionRequestRequestTypeDef",
    "GetPolicyVersionResponseTypeDef",
    "GetRolePolicyRequestRequestTypeDef",
    "GetRolePolicyResponseTypeDef",
    "GetRoleRequestRequestTypeDef",
    "GetRoleResponseTypeDef",
    "GetSAMLProviderRequestRequestTypeDef",
    "GetSAMLProviderResponseTypeDef",
    "GetSSHPublicKeyRequestRequestTypeDef",
    "GetSSHPublicKeyResponseTypeDef",
    "GetServerCertificateRequestRequestTypeDef",
    "GetServerCertificateResponseTypeDef",
    "GetServiceLastAccessedDetailsRequestRequestTypeDef",
    "GetServiceLastAccessedDetailsResponseTypeDef",
    "GetServiceLastAccessedDetailsWithEntitiesRequestRequestTypeDef",
    "GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef",
    "GetServiceLinkedRoleDeletionStatusRequestRequestTypeDef",
    "GetServiceLinkedRoleDeletionStatusResponseTypeDef",
    "GetUserPolicyRequestRequestTypeDef",
    "GetUserPolicyResponseTypeDef",
    "GetUserRequestRequestTypeDef",
    "GetUserResponseTypeDef",
    "GroupDetailTypeDef",
    "GroupPolicyRequestTypeDef",
    "GroupTypeDef",
    "InstanceProfileTypeDef",
    "ListAccessKeysRequestRequestTypeDef",
    "ListAccessKeysResponseTypeDef",
    "ListAccountAliasesRequestRequestTypeDef",
    "ListAccountAliasesResponseTypeDef",
    "ListAttachedGroupPoliciesRequestRequestTypeDef",
    "ListAttachedGroupPoliciesResponseTypeDef",
    "ListAttachedRolePoliciesRequestRequestTypeDef",
    "ListAttachedRolePoliciesResponseTypeDef",
    "ListAttachedUserPoliciesRequestRequestTypeDef",
    "ListAttachedUserPoliciesResponseTypeDef",
    "ListEntitiesForPolicyRequestRequestTypeDef",
    "ListEntitiesForPolicyResponseTypeDef",
    "ListGroupPoliciesRequestRequestTypeDef",
    "ListGroupPoliciesResponseTypeDef",
    "ListGroupsForUserRequestRequestTypeDef",
    "ListGroupsForUserResponseTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListGroupsResponseTypeDef",
    "ListInstanceProfileTagsRequestRequestTypeDef",
    "ListInstanceProfileTagsResponseTypeDef",
    "ListInstanceProfilesForRoleRequestRequestTypeDef",
    "ListInstanceProfilesForRoleResponseTypeDef",
    "ListInstanceProfilesRequestRequestTypeDef",
    "ListInstanceProfilesResponseTypeDef",
    "ListMFADeviceTagsRequestRequestTypeDef",
    "ListMFADeviceTagsResponseTypeDef",
    "ListMFADevicesRequestRequestTypeDef",
    "ListMFADevicesResponseTypeDef",
    "ListOpenIDConnectProviderTagsRequestRequestTypeDef",
    "ListOpenIDConnectProviderTagsResponseTypeDef",
    "ListOpenIDConnectProvidersResponseTypeDef",
    "ListPoliciesGrantingServiceAccessEntryTypeDef",
    "ListPoliciesGrantingServiceAccessRequestRequestTypeDef",
    "ListPoliciesGrantingServiceAccessResponseTypeDef",
    "ListPoliciesRequestRequestTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListPolicyTagsRequestRequestTypeDef",
    "ListPolicyTagsResponseTypeDef",
    "ListPolicyVersionsRequestRequestTypeDef",
    "ListPolicyVersionsResponseTypeDef",
    "ListRolePoliciesRequestRequestTypeDef",
    "ListRolePoliciesResponseTypeDef",
    "ListRoleTagsRequestRequestTypeDef",
    "ListRoleTagsResponseTypeDef",
    "ListRolesRequestRequestTypeDef",
    "ListRolesResponseTypeDef",
    "ListSAMLProviderTagsRequestRequestTypeDef",
    "ListSAMLProviderTagsResponseTypeDef",
    "ListSAMLProvidersResponseTypeDef",
    "ListSSHPublicKeysRequestRequestTypeDef",
    "ListSSHPublicKeysResponseTypeDef",
    "ListServerCertificateTagsRequestRequestTypeDef",
    "ListServerCertificateTagsResponseTypeDef",
    "ListServerCertificatesRequestRequestTypeDef",
    "ListServerCertificatesResponseTypeDef",
    "ListServiceSpecificCredentialsRequestRequestTypeDef",
    "ListServiceSpecificCredentialsResponseTypeDef",
    "ListSigningCertificatesRequestRequestTypeDef",
    "ListSigningCertificatesResponseTypeDef",
    "ListUserPoliciesRequestRequestTypeDef",
    "ListUserPoliciesResponseTypeDef",
    "ListUserTagsRequestRequestTypeDef",
    "ListUserTagsResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "ListVirtualMFADevicesRequestRequestTypeDef",
    "ListVirtualMFADevicesResponseTypeDef",
    "LoginProfileTypeDef",
    "MFADeviceTypeDef",
    "ManagedPolicyDetailTypeDef",
    "OpenIDConnectProviderListEntryTypeDef",
    "OrganizationsDecisionDetailTypeDef",
    "PaginatorConfigTypeDef",
    "PasswordPolicyTypeDef",
    "PermissionsBoundaryDecisionDetailTypeDef",
    "PolicyDetailTypeDef",
    "PolicyGrantingServiceAccessTypeDef",
    "PolicyGroupTypeDef",
    "PolicyRoleTypeDef",
    "PolicyTypeDef",
    "PolicyUserTypeDef",
    "PolicyVersionTypeDef",
    "PositionTypeDef",
    "PutGroupPolicyRequestGroupPolicyTypeDef",
    "PutGroupPolicyRequestGroupTypeDef",
    "PutGroupPolicyRequestRequestTypeDef",
    "PutRolePermissionsBoundaryRequestRequestTypeDef",
    "PutRolePolicyRequestRequestTypeDef",
    "PutRolePolicyRequestRolePolicyTypeDef",
    "PutUserPermissionsBoundaryRequestRequestTypeDef",
    "PutUserPolicyRequestRequestTypeDef",
    "PutUserPolicyRequestUserPolicyTypeDef",
    "PutUserPolicyRequestUserTypeDef",
    "RemoveClientIDFromOpenIDConnectProviderRequestRequestTypeDef",
    "RemoveRoleFromInstanceProfileRequestInstanceProfileTypeDef",
    "RemoveRoleFromInstanceProfileRequestRequestTypeDef",
    "RemoveUserFromGroupRequestGroupTypeDef",
    "RemoveUserFromGroupRequestRequestTypeDef",
    "RemoveUserFromGroupRequestUserTypeDef",
    "ResetServiceSpecificCredentialRequestRequestTypeDef",
    "ResetServiceSpecificCredentialResponseTypeDef",
    "ResourceSpecificResultTypeDef",
    "ResponseMetadataTypeDef",
    "ResyncMFADeviceRequestMfaDeviceTypeDef",
    "ResyncMFADeviceRequestRequestTypeDef",
    "RoleDetailTypeDef",
    "RoleLastUsedTypeDef",
    "RolePolicyRequestTypeDef",
    "RoleTypeDef",
    "RoleUsageTypeTypeDef",
    "SAMLProviderListEntryTypeDef",
    "SSHPublicKeyMetadataTypeDef",
    "SSHPublicKeyTypeDef",
    "ServerCertificateMetadataTypeDef",
    "ServerCertificateTypeDef",
    "ServiceLastAccessedTypeDef",
    "ServiceResourceAccessKeyPairRequestTypeDef",
    "ServiceResourceAccessKeyRequestTypeDef",
    "ServiceResourceAssumeRolePolicyRequestTypeDef",
    "ServiceResourceGroupPolicyRequestTypeDef",
    "ServiceResourceGroupRequestTypeDef",
    "ServiceResourceInstanceProfileRequestTypeDef",
    "ServiceResourceLoginProfileRequestTypeDef",
    "ServiceResourceMfaDeviceRequestTypeDef",
    "ServiceResourcePolicyRequestTypeDef",
    "ServiceResourcePolicyVersionRequestTypeDef",
    "ServiceResourceRolePolicyRequestTypeDef",
    "ServiceResourceRoleRequestTypeDef",
    "ServiceResourceSamlProviderRequestTypeDef",
    "ServiceResourceServerCertificateRequestTypeDef",
    "ServiceResourceSigningCertificateRequestTypeDef",
    "ServiceResourceUserPolicyRequestTypeDef",
    "ServiceResourceUserRequestTypeDef",
    "ServiceResourceVirtualMfaDeviceRequestTypeDef",
    "ServiceSpecificCredentialMetadataTypeDef",
    "ServiceSpecificCredentialTypeDef",
    "SetDefaultPolicyVersionRequestRequestTypeDef",
    "SetSecurityTokenServicePreferencesRequestRequestTypeDef",
    "SigningCertificateTypeDef",
    "SimulateCustomPolicyRequestRequestTypeDef",
    "SimulatePolicyResponseTypeDef",
    "SimulatePrincipalPolicyRequestRequestTypeDef",
    "StatementTypeDef",
    "TagInstanceProfileRequestRequestTypeDef",
    "TagMFADeviceRequestRequestTypeDef",
    "TagOpenIDConnectProviderRequestRequestTypeDef",
    "TagPolicyRequestRequestTypeDef",
    "TagRoleRequestRequestTypeDef",
    "TagSAMLProviderRequestRequestTypeDef",
    "TagServerCertificateRequestRequestTypeDef",
    "TagTypeDef",
    "TagUserRequestRequestTypeDef",
    "TrackedActionLastAccessedTypeDef",
    "UntagInstanceProfileRequestRequestTypeDef",
    "UntagMFADeviceRequestRequestTypeDef",
    "UntagOpenIDConnectProviderRequestRequestTypeDef",
    "UntagPolicyRequestRequestTypeDef",
    "UntagRoleRequestRequestTypeDef",
    "UntagSAMLProviderRequestRequestTypeDef",
    "UntagServerCertificateRequestRequestTypeDef",
    "UntagUserRequestRequestTypeDef",
    "UpdateAccessKeyRequestAccessKeyPairTypeDef",
    "UpdateAccessKeyRequestAccessKeyTypeDef",
    "UpdateAccessKeyRequestRequestTypeDef",
    "UpdateAccountPasswordPolicyRequestAccountPasswordPolicyTypeDef",
    "UpdateAccountPasswordPolicyRequestRequestTypeDef",
    "UpdateAccountPasswordPolicyRequestServiceResourceTypeDef",
    "UpdateAssumeRolePolicyRequestAssumeRolePolicyTypeDef",
    "UpdateAssumeRolePolicyRequestRequestTypeDef",
    "UpdateGroupRequestGroupTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "UpdateLoginProfileRequestLoginProfileTypeDef",
    "UpdateLoginProfileRequestRequestTypeDef",
    "UpdateOpenIDConnectProviderThumbprintRequestRequestTypeDef",
    "UpdateRoleDescriptionRequestRequestTypeDef",
    "UpdateRoleDescriptionResponseTypeDef",
    "UpdateRoleRequestRequestTypeDef",
    "UpdateSAMLProviderRequestRequestTypeDef",
    "UpdateSAMLProviderRequestSamlProviderTypeDef",
    "UpdateSAMLProviderResponseTypeDef",
    "UpdateSSHPublicKeyRequestRequestTypeDef",
    "UpdateServerCertificateRequestRequestTypeDef",
    "UpdateServerCertificateRequestServerCertificateTypeDef",
    "UpdateServiceSpecificCredentialRequestRequestTypeDef",
    "UpdateSigningCertificateRequestRequestTypeDef",
    "UpdateSigningCertificateRequestSigningCertificateTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UpdateUserRequestUserTypeDef",
    "UploadSSHPublicKeyRequestRequestTypeDef",
    "UploadSSHPublicKeyResponseTypeDef",
    "UploadServerCertificateRequestRequestTypeDef",
    "UploadServerCertificateRequestServiceResourceTypeDef",
    "UploadServerCertificateResponseTypeDef",
    "UploadSigningCertificateRequestRequestTypeDef",
    "UploadSigningCertificateRequestServiceResourceTypeDef",
    "UploadSigningCertificateResponseTypeDef",
    "UserAccessKeyRequestTypeDef",
    "UserDetailTypeDef",
    "UserMfaDeviceRequestTypeDef",
    "UserPolicyRequestTypeDef",
    "UserSigningCertificateRequestTypeDef",
    "UserTypeDef",
    "VirtualMFADeviceTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredAccessDetailTypeDef = TypedDict(
    "_RequiredAccessDetailTypeDef",
    {
        "ServiceName": str,
        "ServiceNamespace": str,
    },
)
_OptionalAccessDetailTypeDef = TypedDict(
    "_OptionalAccessDetailTypeDef",
    {
        "Region": str,
        "EntityPath": str,
        "LastAuthenticatedTime": datetime,
        "TotalAuthenticatedEntities": int,
    },
    total=False,
)

class AccessDetailTypeDef(_RequiredAccessDetailTypeDef, _OptionalAccessDetailTypeDef):
    pass

AccessKeyLastUsedTypeDef = TypedDict(
    "AccessKeyLastUsedTypeDef",
    {
        "LastUsedDate": datetime,
        "ServiceName": str,
        "Region": str,
    },
)

AccessKeyMetadataTypeDef = TypedDict(
    "AccessKeyMetadataTypeDef",
    {
        "UserName": str,
        "AccessKeyId": str,
        "Status": statusTypeType,
        "CreateDate": datetime,
    },
    total=False,
)

_RequiredAccessKeyTypeDef = TypedDict(
    "_RequiredAccessKeyTypeDef",
    {
        "UserName": str,
        "AccessKeyId": str,
        "Status": statusTypeType,
        "SecretAccessKey": str,
    },
)
_OptionalAccessKeyTypeDef = TypedDict(
    "_OptionalAccessKeyTypeDef",
    {
        "CreateDate": datetime,
    },
    total=False,
)

class AccessKeyTypeDef(_RequiredAccessKeyTypeDef, _OptionalAccessKeyTypeDef):
    pass

AddClientIDToOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "AddClientIDToOpenIDConnectProviderRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "ClientID": str,
    },
)

AddRoleToInstanceProfileRequestInstanceProfileTypeDef = TypedDict(
    "AddRoleToInstanceProfileRequestInstanceProfileTypeDef",
    {
        "RoleName": str,
    },
)

AddRoleToInstanceProfileRequestRequestTypeDef = TypedDict(
    "AddRoleToInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
        "RoleName": str,
    },
)

AddUserToGroupRequestGroupTypeDef = TypedDict(
    "AddUserToGroupRequestGroupTypeDef",
    {
        "UserName": str,
    },
)

AddUserToGroupRequestRequestTypeDef = TypedDict(
    "AddUserToGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserName": str,
    },
)

AddUserToGroupRequestUserTypeDef = TypedDict(
    "AddUserToGroupRequestUserTypeDef",
    {
        "GroupName": str,
    },
)

AttachGroupPolicyRequestGroupTypeDef = TypedDict(
    "AttachGroupPolicyRequestGroupTypeDef",
    {
        "PolicyArn": str,
    },
)

AttachGroupPolicyRequestPolicyTypeDef = TypedDict(
    "AttachGroupPolicyRequestPolicyTypeDef",
    {
        "GroupName": str,
    },
)

AttachGroupPolicyRequestRequestTypeDef = TypedDict(
    "AttachGroupPolicyRequestRequestTypeDef",
    {
        "GroupName": str,
        "PolicyArn": str,
    },
)

AttachRolePolicyRequestPolicyTypeDef = TypedDict(
    "AttachRolePolicyRequestPolicyTypeDef",
    {
        "RoleName": str,
    },
)

AttachRolePolicyRequestRequestTypeDef = TypedDict(
    "AttachRolePolicyRequestRequestTypeDef",
    {
        "RoleName": str,
        "PolicyArn": str,
    },
)

AttachRolePolicyRequestRoleTypeDef = TypedDict(
    "AttachRolePolicyRequestRoleTypeDef",
    {
        "PolicyArn": str,
    },
)

AttachUserPolicyRequestPolicyTypeDef = TypedDict(
    "AttachUserPolicyRequestPolicyTypeDef",
    {
        "UserName": str,
    },
)

AttachUserPolicyRequestRequestTypeDef = TypedDict(
    "AttachUserPolicyRequestRequestTypeDef",
    {
        "UserName": str,
        "PolicyArn": str,
    },
)

AttachUserPolicyRequestUserTypeDef = TypedDict(
    "AttachUserPolicyRequestUserTypeDef",
    {
        "PolicyArn": str,
    },
)

AttachedPermissionsBoundaryTypeDef = TypedDict(
    "AttachedPermissionsBoundaryTypeDef",
    {
        "PermissionsBoundaryType": Literal["PermissionsBoundaryPolicy"],
        "PermissionsBoundaryArn": str,
    },
    total=False,
)

AttachedPolicyTypeDef = TypedDict(
    "AttachedPolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyArn": str,
    },
    total=False,
)

ChangePasswordRequestRequestTypeDef = TypedDict(
    "ChangePasswordRequestRequestTypeDef",
    {
        "OldPassword": str,
        "NewPassword": str,
    },
)

ChangePasswordRequestServiceResourceTypeDef = TypedDict(
    "ChangePasswordRequestServiceResourceTypeDef",
    {
        "OldPassword": str,
        "NewPassword": str,
    },
)

ContextEntryTypeDef = TypedDict(
    "ContextEntryTypeDef",
    {
        "ContextKeyName": str,
        "ContextKeyValues": List[str],
        "ContextKeyType": ContextKeyTypeEnumType,
    },
    total=False,
)

CreateAccessKeyRequestRequestTypeDef = TypedDict(
    "CreateAccessKeyRequestRequestTypeDef",
    {
        "UserName": str,
    },
    total=False,
)

CreateAccessKeyResponseTypeDef = TypedDict(
    "CreateAccessKeyResponseTypeDef",
    {
        "AccessKey": "AccessKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAccountAliasRequestRequestTypeDef = TypedDict(
    "CreateAccountAliasRequestRequestTypeDef",
    {
        "AccountAlias": str,
    },
)

CreateAccountAliasRequestServiceResourceTypeDef = TypedDict(
    "CreateAccountAliasRequestServiceResourceTypeDef",
    {
        "AccountAlias": str,
    },
)

CreateGroupRequestGroupTypeDef = TypedDict(
    "CreateGroupRequestGroupTypeDef",
    {
        "Path": str,
    },
    total=False,
)

_RequiredCreateGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
    },
)
_OptionalCreateGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGroupRequestRequestTypeDef",
    {
        "Path": str,
    },
    total=False,
)

class CreateGroupRequestRequestTypeDef(
    _RequiredCreateGroupRequestRequestTypeDef, _OptionalCreateGroupRequestRequestTypeDef
):
    pass

_RequiredCreateGroupRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateGroupRequestServiceResourceTypeDef",
    {
        "GroupName": str,
    },
)
_OptionalCreateGroupRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateGroupRequestServiceResourceTypeDef",
    {
        "Path": str,
    },
    total=False,
)

class CreateGroupRequestServiceResourceTypeDef(
    _RequiredCreateGroupRequestServiceResourceTypeDef,
    _OptionalCreateGroupRequestServiceResourceTypeDef,
):
    pass

CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInstanceProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
    },
)
_OptionalCreateInstanceProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInstanceProfileRequestRequestTypeDef",
    {
        "Path": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateInstanceProfileRequestRequestTypeDef(
    _RequiredCreateInstanceProfileRequestRequestTypeDef,
    _OptionalCreateInstanceProfileRequestRequestTypeDef,
):
    pass

_RequiredCreateInstanceProfileRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateInstanceProfileRequestServiceResourceTypeDef",
    {
        "InstanceProfileName": str,
    },
)
_OptionalCreateInstanceProfileRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateInstanceProfileRequestServiceResourceTypeDef",
    {
        "Path": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateInstanceProfileRequestServiceResourceTypeDef(
    _RequiredCreateInstanceProfileRequestServiceResourceTypeDef,
    _OptionalCreateInstanceProfileRequestServiceResourceTypeDef,
):
    pass

CreateInstanceProfileResponseTypeDef = TypedDict(
    "CreateInstanceProfileResponseTypeDef",
    {
        "InstanceProfile": "InstanceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLoginProfileRequestLoginProfileTypeDef = TypedDict(
    "_RequiredCreateLoginProfileRequestLoginProfileTypeDef",
    {
        "Password": str,
    },
)
_OptionalCreateLoginProfileRequestLoginProfileTypeDef = TypedDict(
    "_OptionalCreateLoginProfileRequestLoginProfileTypeDef",
    {
        "PasswordResetRequired": bool,
    },
    total=False,
)

class CreateLoginProfileRequestLoginProfileTypeDef(
    _RequiredCreateLoginProfileRequestLoginProfileTypeDef,
    _OptionalCreateLoginProfileRequestLoginProfileTypeDef,
):
    pass

_RequiredCreateLoginProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLoginProfileRequestRequestTypeDef",
    {
        "UserName": str,
        "Password": str,
    },
)
_OptionalCreateLoginProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLoginProfileRequestRequestTypeDef",
    {
        "PasswordResetRequired": bool,
    },
    total=False,
)

class CreateLoginProfileRequestRequestTypeDef(
    _RequiredCreateLoginProfileRequestRequestTypeDef,
    _OptionalCreateLoginProfileRequestRequestTypeDef,
):
    pass

_RequiredCreateLoginProfileRequestUserTypeDef = TypedDict(
    "_RequiredCreateLoginProfileRequestUserTypeDef",
    {
        "Password": str,
    },
)
_OptionalCreateLoginProfileRequestUserTypeDef = TypedDict(
    "_OptionalCreateLoginProfileRequestUserTypeDef",
    {
        "PasswordResetRequired": bool,
    },
    total=False,
)

class CreateLoginProfileRequestUserTypeDef(
    _RequiredCreateLoginProfileRequestUserTypeDef, _OptionalCreateLoginProfileRequestUserTypeDef
):
    pass

CreateLoginProfileResponseTypeDef = TypedDict(
    "CreateLoginProfileResponseTypeDef",
    {
        "LoginProfile": "LoginProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "_RequiredCreateOpenIDConnectProviderRequestRequestTypeDef",
    {
        "Url": str,
        "ThumbprintList": List[str],
    },
)
_OptionalCreateOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "_OptionalCreateOpenIDConnectProviderRequestRequestTypeDef",
    {
        "ClientIDList": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateOpenIDConnectProviderRequestRequestTypeDef(
    _RequiredCreateOpenIDConnectProviderRequestRequestTypeDef,
    _OptionalCreateOpenIDConnectProviderRequestRequestTypeDef,
):
    pass

CreateOpenIDConnectProviderResponseTypeDef = TypedDict(
    "CreateOpenIDConnectProviderResponseTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePolicyRequestRequestTypeDef",
    {
        "PolicyName": str,
        "PolicyDocument": str,
    },
)
_OptionalCreatePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePolicyRequestRequestTypeDef",
    {
        "Path": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreatePolicyRequestRequestTypeDef(
    _RequiredCreatePolicyRequestRequestTypeDef, _OptionalCreatePolicyRequestRequestTypeDef
):
    pass

_RequiredCreatePolicyRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreatePolicyRequestServiceResourceTypeDef",
    {
        "PolicyName": str,
        "PolicyDocument": str,
    },
)
_OptionalCreatePolicyRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreatePolicyRequestServiceResourceTypeDef",
    {
        "Path": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreatePolicyRequestServiceResourceTypeDef(
    _RequiredCreatePolicyRequestServiceResourceTypeDef,
    _OptionalCreatePolicyRequestServiceResourceTypeDef,
):
    pass

CreatePolicyResponseTypeDef = TypedDict(
    "CreatePolicyResponseTypeDef",
    {
        "Policy": "PolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePolicyVersionRequestPolicyTypeDef = TypedDict(
    "_RequiredCreatePolicyVersionRequestPolicyTypeDef",
    {
        "PolicyDocument": str,
    },
)
_OptionalCreatePolicyVersionRequestPolicyTypeDef = TypedDict(
    "_OptionalCreatePolicyVersionRequestPolicyTypeDef",
    {
        "SetAsDefault": bool,
    },
    total=False,
)

class CreatePolicyVersionRequestPolicyTypeDef(
    _RequiredCreatePolicyVersionRequestPolicyTypeDef,
    _OptionalCreatePolicyVersionRequestPolicyTypeDef,
):
    pass

_RequiredCreatePolicyVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePolicyVersionRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "PolicyDocument": str,
    },
)
_OptionalCreatePolicyVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePolicyVersionRequestRequestTypeDef",
    {
        "SetAsDefault": bool,
    },
    total=False,
)

class CreatePolicyVersionRequestRequestTypeDef(
    _RequiredCreatePolicyVersionRequestRequestTypeDef,
    _OptionalCreatePolicyVersionRequestRequestTypeDef,
):
    pass

CreatePolicyVersionResponseTypeDef = TypedDict(
    "CreatePolicyVersionResponseTypeDef",
    {
        "PolicyVersion": "PolicyVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRoleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRoleRequestRequestTypeDef",
    {
        "RoleName": str,
        "AssumeRolePolicyDocument": str,
    },
)
_OptionalCreateRoleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRoleRequestRequestTypeDef",
    {
        "Path": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateRoleRequestRequestTypeDef(
    _RequiredCreateRoleRequestRequestTypeDef, _OptionalCreateRoleRequestRequestTypeDef
):
    pass

_RequiredCreateRoleRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateRoleRequestServiceResourceTypeDef",
    {
        "RoleName": str,
        "AssumeRolePolicyDocument": str,
    },
)
_OptionalCreateRoleRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateRoleRequestServiceResourceTypeDef",
    {
        "Path": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateRoleRequestServiceResourceTypeDef(
    _RequiredCreateRoleRequestServiceResourceTypeDef,
    _OptionalCreateRoleRequestServiceResourceTypeDef,
):
    pass

CreateRoleResponseTypeDef = TypedDict(
    "CreateRoleResponseTypeDef",
    {
        "Role": "RoleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSAMLProviderRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSAMLProviderRequestRequestTypeDef",
    {
        "SAMLMetadataDocument": str,
        "Name": str,
    },
)
_OptionalCreateSAMLProviderRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSAMLProviderRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateSAMLProviderRequestRequestTypeDef(
    _RequiredCreateSAMLProviderRequestRequestTypeDef,
    _OptionalCreateSAMLProviderRequestRequestTypeDef,
):
    pass

_RequiredCreateSAMLProviderRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateSAMLProviderRequestServiceResourceTypeDef",
    {
        "SAMLMetadataDocument": str,
        "Name": str,
    },
)
_OptionalCreateSAMLProviderRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateSAMLProviderRequestServiceResourceTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateSAMLProviderRequestServiceResourceTypeDef(
    _RequiredCreateSAMLProviderRequestServiceResourceTypeDef,
    _OptionalCreateSAMLProviderRequestServiceResourceTypeDef,
):
    pass

CreateSAMLProviderResponseTypeDef = TypedDict(
    "CreateSAMLProviderResponseTypeDef",
    {
        "SAMLProviderArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceLinkedRoleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateServiceLinkedRoleRequestRequestTypeDef",
    {
        "AWSServiceName": str,
    },
)
_OptionalCreateServiceLinkedRoleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateServiceLinkedRoleRequestRequestTypeDef",
    {
        "Description": str,
        "CustomSuffix": str,
    },
    total=False,
)

class CreateServiceLinkedRoleRequestRequestTypeDef(
    _RequiredCreateServiceLinkedRoleRequestRequestTypeDef,
    _OptionalCreateServiceLinkedRoleRequestRequestTypeDef,
):
    pass

CreateServiceLinkedRoleResponseTypeDef = TypedDict(
    "CreateServiceLinkedRoleResponseTypeDef",
    {
        "Role": "RoleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateServiceSpecificCredentialRequestRequestTypeDef = TypedDict(
    "CreateServiceSpecificCredentialRequestRequestTypeDef",
    {
        "UserName": str,
        "ServiceName": str,
    },
)

CreateServiceSpecificCredentialResponseTypeDef = TypedDict(
    "CreateServiceSpecificCredentialResponseTypeDef",
    {
        "ServiceSpecificCredential": "ServiceSpecificCredentialTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestRequestTypeDef",
    {
        "UserName": str,
    },
)
_OptionalCreateUserRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestRequestTypeDef",
    {
        "Path": str,
        "PermissionsBoundary": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateUserRequestRequestTypeDef(
    _RequiredCreateUserRequestRequestTypeDef, _OptionalCreateUserRequestRequestTypeDef
):
    pass

_RequiredCreateUserRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateUserRequestServiceResourceTypeDef",
    {
        "UserName": str,
    },
)
_OptionalCreateUserRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateUserRequestServiceResourceTypeDef",
    {
        "Path": str,
        "PermissionsBoundary": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateUserRequestServiceResourceTypeDef(
    _RequiredCreateUserRequestServiceResourceTypeDef,
    _OptionalCreateUserRequestServiceResourceTypeDef,
):
    pass

CreateUserRequestUserTypeDef = TypedDict(
    "CreateUserRequestUserTypeDef",
    {
        "Path": str,
        "PermissionsBoundary": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVirtualMFADeviceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVirtualMFADeviceRequestRequestTypeDef",
    {
        "VirtualMFADeviceName": str,
    },
)
_OptionalCreateVirtualMFADeviceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVirtualMFADeviceRequestRequestTypeDef",
    {
        "Path": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateVirtualMFADeviceRequestRequestTypeDef(
    _RequiredCreateVirtualMFADeviceRequestRequestTypeDef,
    _OptionalCreateVirtualMFADeviceRequestRequestTypeDef,
):
    pass

_RequiredCreateVirtualMFADeviceRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateVirtualMFADeviceRequestServiceResourceTypeDef",
    {
        "VirtualMFADeviceName": str,
    },
)
_OptionalCreateVirtualMFADeviceRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateVirtualMFADeviceRequestServiceResourceTypeDef",
    {
        "Path": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateVirtualMFADeviceRequestServiceResourceTypeDef(
    _RequiredCreateVirtualMFADeviceRequestServiceResourceTypeDef,
    _OptionalCreateVirtualMFADeviceRequestServiceResourceTypeDef,
):
    pass

CreateVirtualMFADeviceResponseTypeDef = TypedDict(
    "CreateVirtualMFADeviceResponseTypeDef",
    {
        "VirtualMFADevice": "VirtualMFADeviceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeactivateMFADeviceRequestRequestTypeDef = TypedDict(
    "DeactivateMFADeviceRequestRequestTypeDef",
    {
        "UserName": str,
        "SerialNumber": str,
    },
)

_RequiredDeleteAccessKeyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAccessKeyRequestRequestTypeDef",
    {
        "AccessKeyId": str,
    },
)
_OptionalDeleteAccessKeyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAccessKeyRequestRequestTypeDef",
    {
        "UserName": str,
    },
    total=False,
)

class DeleteAccessKeyRequestRequestTypeDef(
    _RequiredDeleteAccessKeyRequestRequestTypeDef, _OptionalDeleteAccessKeyRequestRequestTypeDef
):
    pass

DeleteAccountAliasRequestRequestTypeDef = TypedDict(
    "DeleteAccountAliasRequestRequestTypeDef",
    {
        "AccountAlias": str,
    },
)

DeleteGroupPolicyRequestRequestTypeDef = TypedDict(
    "DeleteGroupPolicyRequestRequestTypeDef",
    {
        "GroupName": str,
        "PolicyName": str,
    },
)

DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "GroupName": str,
    },
)

DeleteInstanceProfileRequestRequestTypeDef = TypedDict(
    "DeleteInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
    },
)

DeleteLoginProfileRequestRequestTypeDef = TypedDict(
    "DeleteLoginProfileRequestRequestTypeDef",
    {
        "UserName": str,
    },
)

DeleteOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "DeleteOpenIDConnectProviderRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
    },
)

DeletePolicyRequestRequestTypeDef = TypedDict(
    "DeletePolicyRequestRequestTypeDef",
    {
        "PolicyArn": str,
    },
)

DeletePolicyVersionRequestRequestTypeDef = TypedDict(
    "DeletePolicyVersionRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "VersionId": str,
    },
)

DeleteRolePermissionsBoundaryRequestRequestTypeDef = TypedDict(
    "DeleteRolePermissionsBoundaryRequestRequestTypeDef",
    {
        "RoleName": str,
    },
)

DeleteRolePolicyRequestRequestTypeDef = TypedDict(
    "DeleteRolePolicyRequestRequestTypeDef",
    {
        "RoleName": str,
        "PolicyName": str,
    },
)

DeleteRoleRequestRequestTypeDef = TypedDict(
    "DeleteRoleRequestRequestTypeDef",
    {
        "RoleName": str,
    },
)

DeleteSAMLProviderRequestRequestTypeDef = TypedDict(
    "DeleteSAMLProviderRequestRequestTypeDef",
    {
        "SAMLProviderArn": str,
    },
)

DeleteSSHPublicKeyRequestRequestTypeDef = TypedDict(
    "DeleteSSHPublicKeyRequestRequestTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
    },
)

DeleteServerCertificateRequestRequestTypeDef = TypedDict(
    "DeleteServerCertificateRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
    },
)

DeleteServiceLinkedRoleRequestRequestTypeDef = TypedDict(
    "DeleteServiceLinkedRoleRequestRequestTypeDef",
    {
        "RoleName": str,
    },
)

DeleteServiceLinkedRoleResponseTypeDef = TypedDict(
    "DeleteServiceLinkedRoleResponseTypeDef",
    {
        "DeletionTaskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteServiceSpecificCredentialRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteServiceSpecificCredentialRequestRequestTypeDef",
    {
        "ServiceSpecificCredentialId": str,
    },
)
_OptionalDeleteServiceSpecificCredentialRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteServiceSpecificCredentialRequestRequestTypeDef",
    {
        "UserName": str,
    },
    total=False,
)

class DeleteServiceSpecificCredentialRequestRequestTypeDef(
    _RequiredDeleteServiceSpecificCredentialRequestRequestTypeDef,
    _OptionalDeleteServiceSpecificCredentialRequestRequestTypeDef,
):
    pass

_RequiredDeleteSigningCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteSigningCertificateRequestRequestTypeDef",
    {
        "CertificateId": str,
    },
)
_OptionalDeleteSigningCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteSigningCertificateRequestRequestTypeDef",
    {
        "UserName": str,
    },
    total=False,
)

class DeleteSigningCertificateRequestRequestTypeDef(
    _RequiredDeleteSigningCertificateRequestRequestTypeDef,
    _OptionalDeleteSigningCertificateRequestRequestTypeDef,
):
    pass

DeleteUserPermissionsBoundaryRequestRequestTypeDef = TypedDict(
    "DeleteUserPermissionsBoundaryRequestRequestTypeDef",
    {
        "UserName": str,
    },
)

DeleteUserPolicyRequestRequestTypeDef = TypedDict(
    "DeleteUserPolicyRequestRequestTypeDef",
    {
        "UserName": str,
        "PolicyName": str,
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "UserName": str,
    },
)

DeleteVirtualMFADeviceRequestRequestTypeDef = TypedDict(
    "DeleteVirtualMFADeviceRequestRequestTypeDef",
    {
        "SerialNumber": str,
    },
)

DeletionTaskFailureReasonTypeTypeDef = TypedDict(
    "DeletionTaskFailureReasonTypeTypeDef",
    {
        "Reason": str,
        "RoleUsageList": List["RoleUsageTypeTypeDef"],
    },
    total=False,
)

DetachGroupPolicyRequestGroupTypeDef = TypedDict(
    "DetachGroupPolicyRequestGroupTypeDef",
    {
        "PolicyArn": str,
    },
)

DetachGroupPolicyRequestPolicyTypeDef = TypedDict(
    "DetachGroupPolicyRequestPolicyTypeDef",
    {
        "GroupName": str,
    },
)

DetachGroupPolicyRequestRequestTypeDef = TypedDict(
    "DetachGroupPolicyRequestRequestTypeDef",
    {
        "GroupName": str,
        "PolicyArn": str,
    },
)

DetachRolePolicyRequestPolicyTypeDef = TypedDict(
    "DetachRolePolicyRequestPolicyTypeDef",
    {
        "RoleName": str,
    },
)

DetachRolePolicyRequestRequestTypeDef = TypedDict(
    "DetachRolePolicyRequestRequestTypeDef",
    {
        "RoleName": str,
        "PolicyArn": str,
    },
)

DetachRolePolicyRequestRoleTypeDef = TypedDict(
    "DetachRolePolicyRequestRoleTypeDef",
    {
        "PolicyArn": str,
    },
)

DetachUserPolicyRequestPolicyTypeDef = TypedDict(
    "DetachUserPolicyRequestPolicyTypeDef",
    {
        "UserName": str,
    },
)

DetachUserPolicyRequestRequestTypeDef = TypedDict(
    "DetachUserPolicyRequestRequestTypeDef",
    {
        "UserName": str,
        "PolicyArn": str,
    },
)

DetachUserPolicyRequestUserTypeDef = TypedDict(
    "DetachUserPolicyRequestUserTypeDef",
    {
        "PolicyArn": str,
    },
)

EnableMFADeviceRequestMfaDeviceTypeDef = TypedDict(
    "EnableMFADeviceRequestMfaDeviceTypeDef",
    {
        "AuthenticationCode1": str,
        "AuthenticationCode2": str,
    },
)

EnableMFADeviceRequestRequestTypeDef = TypedDict(
    "EnableMFADeviceRequestRequestTypeDef",
    {
        "UserName": str,
        "SerialNumber": str,
        "AuthenticationCode1": str,
        "AuthenticationCode2": str,
    },
)

EnableMFADeviceRequestUserTypeDef = TypedDict(
    "EnableMFADeviceRequestUserTypeDef",
    {
        "SerialNumber": str,
        "AuthenticationCode1": str,
        "AuthenticationCode2": str,
    },
)

_RequiredEntityDetailsTypeDef = TypedDict(
    "_RequiredEntityDetailsTypeDef",
    {
        "EntityInfo": "EntityInfoTypeDef",
    },
)
_OptionalEntityDetailsTypeDef = TypedDict(
    "_OptionalEntityDetailsTypeDef",
    {
        "LastAuthenticated": datetime,
    },
    total=False,
)

class EntityDetailsTypeDef(_RequiredEntityDetailsTypeDef, _OptionalEntityDetailsTypeDef):
    pass

_RequiredEntityInfoTypeDef = TypedDict(
    "_RequiredEntityInfoTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": policyOwnerEntityTypeType,
        "Id": str,
    },
)
_OptionalEntityInfoTypeDef = TypedDict(
    "_OptionalEntityInfoTypeDef",
    {
        "Path": str,
    },
    total=False,
)

class EntityInfoTypeDef(_RequiredEntityInfoTypeDef, _OptionalEntityInfoTypeDef):
    pass

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "Message": str,
        "Code": str,
    },
)

_RequiredEvaluationResultTypeDef = TypedDict(
    "_RequiredEvaluationResultTypeDef",
    {
        "EvalActionName": str,
        "EvalDecision": PolicyEvaluationDecisionTypeType,
    },
)
_OptionalEvaluationResultTypeDef = TypedDict(
    "_OptionalEvaluationResultTypeDef",
    {
        "EvalResourceName": str,
        "MatchedStatements": List["StatementTypeDef"],
        "MissingContextValues": List[str],
        "OrganizationsDecisionDetail": "OrganizationsDecisionDetailTypeDef",
        "PermissionsBoundaryDecisionDetail": "PermissionsBoundaryDecisionDetailTypeDef",
        "EvalDecisionDetails": Dict[str, PolicyEvaluationDecisionTypeType],
        "ResourceSpecificResults": List["ResourceSpecificResultTypeDef"],
    },
    total=False,
)

class EvaluationResultTypeDef(_RequiredEvaluationResultTypeDef, _OptionalEvaluationResultTypeDef):
    pass

GenerateCredentialReportResponseTypeDef = TypedDict(
    "GenerateCredentialReportResponseTypeDef",
    {
        "State": ReportStateTypeType,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGenerateOrganizationsAccessReportRequestRequestTypeDef = TypedDict(
    "_RequiredGenerateOrganizationsAccessReportRequestRequestTypeDef",
    {
        "EntityPath": str,
    },
)
_OptionalGenerateOrganizationsAccessReportRequestRequestTypeDef = TypedDict(
    "_OptionalGenerateOrganizationsAccessReportRequestRequestTypeDef",
    {
        "OrganizationsPolicyId": str,
    },
    total=False,
)

class GenerateOrganizationsAccessReportRequestRequestTypeDef(
    _RequiredGenerateOrganizationsAccessReportRequestRequestTypeDef,
    _OptionalGenerateOrganizationsAccessReportRequestRequestTypeDef,
):
    pass

GenerateOrganizationsAccessReportResponseTypeDef = TypedDict(
    "GenerateOrganizationsAccessReportResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGenerateServiceLastAccessedDetailsRequestRequestTypeDef = TypedDict(
    "_RequiredGenerateServiceLastAccessedDetailsRequestRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalGenerateServiceLastAccessedDetailsRequestRequestTypeDef = TypedDict(
    "_OptionalGenerateServiceLastAccessedDetailsRequestRequestTypeDef",
    {
        "Granularity": AccessAdvisorUsageGranularityTypeType,
    },
    total=False,
)

class GenerateServiceLastAccessedDetailsRequestRequestTypeDef(
    _RequiredGenerateServiceLastAccessedDetailsRequestRequestTypeDef,
    _OptionalGenerateServiceLastAccessedDetailsRequestRequestTypeDef,
):
    pass

GenerateServiceLastAccessedDetailsResponseTypeDef = TypedDict(
    "GenerateServiceLastAccessedDetailsResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessKeyLastUsedRequestRequestTypeDef = TypedDict(
    "GetAccessKeyLastUsedRequestRequestTypeDef",
    {
        "AccessKeyId": str,
    },
)

GetAccessKeyLastUsedResponseTypeDef = TypedDict(
    "GetAccessKeyLastUsedResponseTypeDef",
    {
        "UserName": str,
        "AccessKeyLastUsed": "AccessKeyLastUsedTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccountAuthorizationDetailsRequestRequestTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsRequestRequestTypeDef",
    {
        "Filter": List[EntityTypeType],
        "MaxItems": int,
        "Marker": str,
    },
    total=False,
)

GetAccountAuthorizationDetailsResponseTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsResponseTypeDef",
    {
        "UserDetailList": List["UserDetailTypeDef"],
        "GroupDetailList": List["GroupDetailTypeDef"],
        "RoleDetailList": List["RoleDetailTypeDef"],
        "Policies": List["ManagedPolicyDetailTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccountPasswordPolicyResponseTypeDef = TypedDict(
    "GetAccountPasswordPolicyResponseTypeDef",
    {
        "PasswordPolicy": "PasswordPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccountSummaryResponseTypeDef = TypedDict(
    "GetAccountSummaryResponseTypeDef",
    {
        "SummaryMap": Dict[summaryKeyTypeType, int],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContextKeysForCustomPolicyRequestRequestTypeDef = TypedDict(
    "GetContextKeysForCustomPolicyRequestRequestTypeDef",
    {
        "PolicyInputList": List[str],
    },
)

GetContextKeysForPolicyResponseTypeDef = TypedDict(
    "GetContextKeysForPolicyResponseTypeDef",
    {
        "ContextKeyNames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetContextKeysForPrincipalPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredGetContextKeysForPrincipalPolicyRequestRequestTypeDef",
    {
        "PolicySourceArn": str,
    },
)
_OptionalGetContextKeysForPrincipalPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalGetContextKeysForPrincipalPolicyRequestRequestTypeDef",
    {
        "PolicyInputList": List[str],
    },
    total=False,
)

class GetContextKeysForPrincipalPolicyRequestRequestTypeDef(
    _RequiredGetContextKeysForPrincipalPolicyRequestRequestTypeDef,
    _OptionalGetContextKeysForPrincipalPolicyRequestRequestTypeDef,
):
    pass

GetCredentialReportResponseTypeDef = TypedDict(
    "GetCredentialReportResponseTypeDef",
    {
        "Content": bytes,
        "ReportFormat": Literal["text/csv"],
        "GeneratedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupPolicyRequestRequestTypeDef = TypedDict(
    "GetGroupPolicyRequestRequestTypeDef",
    {
        "GroupName": str,
        "PolicyName": str,
    },
)

GetGroupPolicyResponseTypeDef = TypedDict(
    "GetGroupPolicyResponseTypeDef",
    {
        "GroupName": str,
        "PolicyName": str,
        "PolicyDocument": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetGroupRequestRequestTypeDef = TypedDict(
    "_RequiredGetGroupRequestRequestTypeDef",
    {
        "GroupName": str,
    },
)
_OptionalGetGroupRequestRequestTypeDef = TypedDict(
    "_OptionalGetGroupRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class GetGroupRequestRequestTypeDef(
    _RequiredGetGroupRequestRequestTypeDef, _OptionalGetGroupRequestRequestTypeDef
):
    pass

GetGroupResponseTypeDef = TypedDict(
    "GetGroupResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "Users": List["UserTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceProfileRequestRequestTypeDef = TypedDict(
    "GetInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
    },
)

GetInstanceProfileResponseTypeDef = TypedDict(
    "GetInstanceProfileResponseTypeDef",
    {
        "InstanceProfile": "InstanceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoginProfileRequestRequestTypeDef = TypedDict(
    "GetLoginProfileRequestRequestTypeDef",
    {
        "UserName": str,
    },
)

GetLoginProfileResponseTypeDef = TypedDict(
    "GetLoginProfileResponseTypeDef",
    {
        "LoginProfile": "LoginProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "GetOpenIDConnectProviderRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
    },
)

GetOpenIDConnectProviderResponseTypeDef = TypedDict(
    "GetOpenIDConnectProviderResponseTypeDef",
    {
        "Url": str,
        "ClientIDList": List[str],
        "ThumbprintList": List[str],
        "CreateDate": datetime,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetOrganizationsAccessReportRequestRequestTypeDef = TypedDict(
    "_RequiredGetOrganizationsAccessReportRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetOrganizationsAccessReportRequestRequestTypeDef = TypedDict(
    "_OptionalGetOrganizationsAccessReportRequestRequestTypeDef",
    {
        "MaxItems": int,
        "Marker": str,
        "SortKey": sortKeyTypeType,
    },
    total=False,
)

class GetOrganizationsAccessReportRequestRequestTypeDef(
    _RequiredGetOrganizationsAccessReportRequestRequestTypeDef,
    _OptionalGetOrganizationsAccessReportRequestRequestTypeDef,
):
    pass

GetOrganizationsAccessReportResponseTypeDef = TypedDict(
    "GetOrganizationsAccessReportResponseTypeDef",
    {
        "JobStatus": jobStatusTypeType,
        "JobCreationDate": datetime,
        "JobCompletionDate": datetime,
        "NumberOfServicesAccessible": int,
        "NumberOfServicesNotAccessed": int,
        "AccessDetails": List["AccessDetailTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ErrorDetails": "ErrorDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyRequestRequestTypeDef = TypedDict(
    "GetPolicyRequestRequestTypeDef",
    {
        "PolicyArn": str,
    },
)

GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef",
    {
        "Policy": "PolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyVersionRequestRequestTypeDef = TypedDict(
    "GetPolicyVersionRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "VersionId": str,
    },
)

GetPolicyVersionResponseTypeDef = TypedDict(
    "GetPolicyVersionResponseTypeDef",
    {
        "PolicyVersion": "PolicyVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRolePolicyRequestRequestTypeDef = TypedDict(
    "GetRolePolicyRequestRequestTypeDef",
    {
        "RoleName": str,
        "PolicyName": str,
    },
)

GetRolePolicyResponseTypeDef = TypedDict(
    "GetRolePolicyResponseTypeDef",
    {
        "RoleName": str,
        "PolicyName": str,
        "PolicyDocument": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRoleRequestRequestTypeDef = TypedDict(
    "GetRoleRequestRequestTypeDef",
    {
        "RoleName": str,
    },
)

GetRoleResponseTypeDef = TypedDict(
    "GetRoleResponseTypeDef",
    {
        "Role": "RoleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSAMLProviderRequestRequestTypeDef = TypedDict(
    "GetSAMLProviderRequestRequestTypeDef",
    {
        "SAMLProviderArn": str,
    },
)

GetSAMLProviderResponseTypeDef = TypedDict(
    "GetSAMLProviderResponseTypeDef",
    {
        "SAMLMetadataDocument": str,
        "CreateDate": datetime,
        "ValidUntil": datetime,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSSHPublicKeyRequestRequestTypeDef = TypedDict(
    "GetSSHPublicKeyRequestRequestTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Encoding": encodingTypeType,
    },
)

GetSSHPublicKeyResponseTypeDef = TypedDict(
    "GetSSHPublicKeyResponseTypeDef",
    {
        "SSHPublicKey": "SSHPublicKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServerCertificateRequestRequestTypeDef = TypedDict(
    "GetServerCertificateRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
    },
)

GetServerCertificateResponseTypeDef = TypedDict(
    "GetServerCertificateResponseTypeDef",
    {
        "ServerCertificate": "ServerCertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetServiceLastAccessedDetailsRequestRequestTypeDef = TypedDict(
    "_RequiredGetServiceLastAccessedDetailsRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetServiceLastAccessedDetailsRequestRequestTypeDef = TypedDict(
    "_OptionalGetServiceLastAccessedDetailsRequestRequestTypeDef",
    {
        "MaxItems": int,
        "Marker": str,
    },
    total=False,
)

class GetServiceLastAccessedDetailsRequestRequestTypeDef(
    _RequiredGetServiceLastAccessedDetailsRequestRequestTypeDef,
    _OptionalGetServiceLastAccessedDetailsRequestRequestTypeDef,
):
    pass

GetServiceLastAccessedDetailsResponseTypeDef = TypedDict(
    "GetServiceLastAccessedDetailsResponseTypeDef",
    {
        "JobStatus": jobStatusTypeType,
        "JobType": AccessAdvisorUsageGranularityTypeType,
        "JobCreationDate": datetime,
        "ServicesLastAccessed": List["ServiceLastAccessedTypeDef"],
        "JobCompletionDate": datetime,
        "IsTruncated": bool,
        "Marker": str,
        "Error": "ErrorDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetServiceLastAccessedDetailsWithEntitiesRequestRequestTypeDef = TypedDict(
    "_RequiredGetServiceLastAccessedDetailsWithEntitiesRequestRequestTypeDef",
    {
        "JobId": str,
        "ServiceNamespace": str,
    },
)
_OptionalGetServiceLastAccessedDetailsWithEntitiesRequestRequestTypeDef = TypedDict(
    "_OptionalGetServiceLastAccessedDetailsWithEntitiesRequestRequestTypeDef",
    {
        "MaxItems": int,
        "Marker": str,
    },
    total=False,
)

class GetServiceLastAccessedDetailsWithEntitiesRequestRequestTypeDef(
    _RequiredGetServiceLastAccessedDetailsWithEntitiesRequestRequestTypeDef,
    _OptionalGetServiceLastAccessedDetailsWithEntitiesRequestRequestTypeDef,
):
    pass

GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef = TypedDict(
    "GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef",
    {
        "JobStatus": jobStatusTypeType,
        "JobCreationDate": datetime,
        "JobCompletionDate": datetime,
        "EntityDetailsList": List["EntityDetailsTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "Error": "ErrorDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceLinkedRoleDeletionStatusRequestRequestTypeDef = TypedDict(
    "GetServiceLinkedRoleDeletionStatusRequestRequestTypeDef",
    {
        "DeletionTaskId": str,
    },
)

GetServiceLinkedRoleDeletionStatusResponseTypeDef = TypedDict(
    "GetServiceLinkedRoleDeletionStatusResponseTypeDef",
    {
        "Status": DeletionTaskStatusTypeType,
        "Reason": "DeletionTaskFailureReasonTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserPolicyRequestRequestTypeDef = TypedDict(
    "GetUserPolicyRequestRequestTypeDef",
    {
        "UserName": str,
        "PolicyName": str,
    },
)

GetUserPolicyResponseTypeDef = TypedDict(
    "GetUserPolicyResponseTypeDef",
    {
        "UserName": str,
        "PolicyName": str,
        "PolicyDocument": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserRequestRequestTypeDef = TypedDict(
    "GetUserRequestRequestTypeDef",
    {
        "UserName": str,
    },
    total=False,
)

GetUserResponseTypeDef = TypedDict(
    "GetUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupDetailTypeDef = TypedDict(
    "GroupDetailTypeDef",
    {
        "Path": str,
        "GroupName": str,
        "GroupId": str,
        "Arn": str,
        "CreateDate": datetime,
        "GroupPolicyList": List["PolicyDetailTypeDef"],
        "AttachedManagedPolicies": List["AttachedPolicyTypeDef"],
    },
    total=False,
)

GroupPolicyRequestTypeDef = TypedDict(
    "GroupPolicyRequestTypeDef",
    {
        "name": str,
    },
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "Path": str,
        "GroupName": str,
        "GroupId": str,
        "Arn": str,
        "CreateDate": datetime,
    },
)

_RequiredInstanceProfileTypeDef = TypedDict(
    "_RequiredInstanceProfileTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List["RoleTypeDef"],
    },
)
_OptionalInstanceProfileTypeDef = TypedDict(
    "_OptionalInstanceProfileTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class InstanceProfileTypeDef(_RequiredInstanceProfileTypeDef, _OptionalInstanceProfileTypeDef):
    pass

ListAccessKeysRequestRequestTypeDef = TypedDict(
    "ListAccessKeysRequestRequestTypeDef",
    {
        "UserName": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListAccessKeysResponseTypeDef = TypedDict(
    "ListAccessKeysResponseTypeDef",
    {
        "AccessKeyMetadata": List["AccessKeyMetadataTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAccountAliasesRequestRequestTypeDef = TypedDict(
    "ListAccountAliasesRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListAccountAliasesResponseTypeDef = TypedDict(
    "ListAccountAliasesResponseTypeDef",
    {
        "AccountAliases": List[str],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAttachedGroupPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredListAttachedGroupPoliciesRequestRequestTypeDef",
    {
        "GroupName": str,
    },
)
_OptionalListAttachedGroupPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalListAttachedGroupPoliciesRequestRequestTypeDef",
    {
        "PathPrefix": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListAttachedGroupPoliciesRequestRequestTypeDef(
    _RequiredListAttachedGroupPoliciesRequestRequestTypeDef,
    _OptionalListAttachedGroupPoliciesRequestRequestTypeDef,
):
    pass

ListAttachedGroupPoliciesResponseTypeDef = TypedDict(
    "ListAttachedGroupPoliciesResponseTypeDef",
    {
        "AttachedPolicies": List["AttachedPolicyTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAttachedRolePoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredListAttachedRolePoliciesRequestRequestTypeDef",
    {
        "RoleName": str,
    },
)
_OptionalListAttachedRolePoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalListAttachedRolePoliciesRequestRequestTypeDef",
    {
        "PathPrefix": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListAttachedRolePoliciesRequestRequestTypeDef(
    _RequiredListAttachedRolePoliciesRequestRequestTypeDef,
    _OptionalListAttachedRolePoliciesRequestRequestTypeDef,
):
    pass

ListAttachedRolePoliciesResponseTypeDef = TypedDict(
    "ListAttachedRolePoliciesResponseTypeDef",
    {
        "AttachedPolicies": List["AttachedPolicyTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAttachedUserPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredListAttachedUserPoliciesRequestRequestTypeDef",
    {
        "UserName": str,
    },
)
_OptionalListAttachedUserPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalListAttachedUserPoliciesRequestRequestTypeDef",
    {
        "PathPrefix": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListAttachedUserPoliciesRequestRequestTypeDef(
    _RequiredListAttachedUserPoliciesRequestRequestTypeDef,
    _OptionalListAttachedUserPoliciesRequestRequestTypeDef,
):
    pass

ListAttachedUserPoliciesResponseTypeDef = TypedDict(
    "ListAttachedUserPoliciesResponseTypeDef",
    {
        "AttachedPolicies": List["AttachedPolicyTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEntitiesForPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredListEntitiesForPolicyRequestRequestTypeDef",
    {
        "PolicyArn": str,
    },
)
_OptionalListEntitiesForPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalListEntitiesForPolicyRequestRequestTypeDef",
    {
        "EntityFilter": EntityTypeType,
        "PathPrefix": str,
        "PolicyUsageFilter": PolicyUsageTypeType,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListEntitiesForPolicyRequestRequestTypeDef(
    _RequiredListEntitiesForPolicyRequestRequestTypeDef,
    _OptionalListEntitiesForPolicyRequestRequestTypeDef,
):
    pass

ListEntitiesForPolicyResponseTypeDef = TypedDict(
    "ListEntitiesForPolicyResponseTypeDef",
    {
        "PolicyGroups": List["PolicyGroupTypeDef"],
        "PolicyUsers": List["PolicyUserTypeDef"],
        "PolicyRoles": List["PolicyRoleTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGroupPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredListGroupPoliciesRequestRequestTypeDef",
    {
        "GroupName": str,
    },
)
_OptionalListGroupPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalListGroupPoliciesRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListGroupPoliciesRequestRequestTypeDef(
    _RequiredListGroupPoliciesRequestRequestTypeDef, _OptionalListGroupPoliciesRequestRequestTypeDef
):
    pass

ListGroupPoliciesResponseTypeDef = TypedDict(
    "ListGroupPoliciesResponseTypeDef",
    {
        "PolicyNames": List[str],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGroupsForUserRequestRequestTypeDef = TypedDict(
    "_RequiredListGroupsForUserRequestRequestTypeDef",
    {
        "UserName": str,
    },
)
_OptionalListGroupsForUserRequestRequestTypeDef = TypedDict(
    "_OptionalListGroupsForUserRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListGroupsForUserRequestRequestTypeDef(
    _RequiredListGroupsForUserRequestRequestTypeDef, _OptionalListGroupsForUserRequestRequestTypeDef
):
    pass

ListGroupsForUserResponseTypeDef = TypedDict(
    "ListGroupsForUserResponseTypeDef",
    {
        "Groups": List["GroupTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroupsRequestRequestTypeDef = TypedDict(
    "ListGroupsRequestRequestTypeDef",
    {
        "PathPrefix": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "Groups": List["GroupTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstanceProfileTagsRequestRequestTypeDef = TypedDict(
    "_RequiredListInstanceProfileTagsRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
    },
)
_OptionalListInstanceProfileTagsRequestRequestTypeDef = TypedDict(
    "_OptionalListInstanceProfileTagsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListInstanceProfileTagsRequestRequestTypeDef(
    _RequiredListInstanceProfileTagsRequestRequestTypeDef,
    _OptionalListInstanceProfileTagsRequestRequestTypeDef,
):
    pass

ListInstanceProfileTagsResponseTypeDef = TypedDict(
    "ListInstanceProfileTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstanceProfilesForRoleRequestRequestTypeDef = TypedDict(
    "_RequiredListInstanceProfilesForRoleRequestRequestTypeDef",
    {
        "RoleName": str,
    },
)
_OptionalListInstanceProfilesForRoleRequestRequestTypeDef = TypedDict(
    "_OptionalListInstanceProfilesForRoleRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListInstanceProfilesForRoleRequestRequestTypeDef(
    _RequiredListInstanceProfilesForRoleRequestRequestTypeDef,
    _OptionalListInstanceProfilesForRoleRequestRequestTypeDef,
):
    pass

ListInstanceProfilesForRoleResponseTypeDef = TypedDict(
    "ListInstanceProfilesForRoleResponseTypeDef",
    {
        "InstanceProfiles": List["InstanceProfileTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstanceProfilesRequestRequestTypeDef = TypedDict(
    "ListInstanceProfilesRequestRequestTypeDef",
    {
        "PathPrefix": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListInstanceProfilesResponseTypeDef = TypedDict(
    "ListInstanceProfilesResponseTypeDef",
    {
        "InstanceProfiles": List["InstanceProfileTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMFADeviceTagsRequestRequestTypeDef = TypedDict(
    "_RequiredListMFADeviceTagsRequestRequestTypeDef",
    {
        "SerialNumber": str,
    },
)
_OptionalListMFADeviceTagsRequestRequestTypeDef = TypedDict(
    "_OptionalListMFADeviceTagsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListMFADeviceTagsRequestRequestTypeDef(
    _RequiredListMFADeviceTagsRequestRequestTypeDef, _OptionalListMFADeviceTagsRequestRequestTypeDef
):
    pass

ListMFADeviceTagsResponseTypeDef = TypedDict(
    "ListMFADeviceTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMFADevicesRequestRequestTypeDef = TypedDict(
    "ListMFADevicesRequestRequestTypeDef",
    {
        "UserName": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListMFADevicesResponseTypeDef = TypedDict(
    "ListMFADevicesResponseTypeDef",
    {
        "MFADevices": List["MFADeviceTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListOpenIDConnectProviderTagsRequestRequestTypeDef = TypedDict(
    "_RequiredListOpenIDConnectProviderTagsRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
    },
)
_OptionalListOpenIDConnectProviderTagsRequestRequestTypeDef = TypedDict(
    "_OptionalListOpenIDConnectProviderTagsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListOpenIDConnectProviderTagsRequestRequestTypeDef(
    _RequiredListOpenIDConnectProviderTagsRequestRequestTypeDef,
    _OptionalListOpenIDConnectProviderTagsRequestRequestTypeDef,
):
    pass

ListOpenIDConnectProviderTagsResponseTypeDef = TypedDict(
    "ListOpenIDConnectProviderTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOpenIDConnectProvidersResponseTypeDef = TypedDict(
    "ListOpenIDConnectProvidersResponseTypeDef",
    {
        "OpenIDConnectProviderList": List["OpenIDConnectProviderListEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPoliciesGrantingServiceAccessEntryTypeDef = TypedDict(
    "ListPoliciesGrantingServiceAccessEntryTypeDef",
    {
        "ServiceNamespace": str,
        "Policies": List["PolicyGrantingServiceAccessTypeDef"],
    },
    total=False,
)

_RequiredListPoliciesGrantingServiceAccessRequestRequestTypeDef = TypedDict(
    "_RequiredListPoliciesGrantingServiceAccessRequestRequestTypeDef",
    {
        "Arn": str,
        "ServiceNamespaces": List[str],
    },
)
_OptionalListPoliciesGrantingServiceAccessRequestRequestTypeDef = TypedDict(
    "_OptionalListPoliciesGrantingServiceAccessRequestRequestTypeDef",
    {
        "Marker": str,
    },
    total=False,
)

class ListPoliciesGrantingServiceAccessRequestRequestTypeDef(
    _RequiredListPoliciesGrantingServiceAccessRequestRequestTypeDef,
    _OptionalListPoliciesGrantingServiceAccessRequestRequestTypeDef,
):
    pass

ListPoliciesGrantingServiceAccessResponseTypeDef = TypedDict(
    "ListPoliciesGrantingServiceAccessResponseTypeDef",
    {
        "PoliciesGrantingServiceAccess": List["ListPoliciesGrantingServiceAccessEntryTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPoliciesRequestRequestTypeDef = TypedDict(
    "ListPoliciesRequestRequestTypeDef",
    {
        "Scope": policyScopeTypeType,
        "OnlyAttached": bool,
        "PathPrefix": str,
        "PolicyUsageFilter": PolicyUsageTypeType,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListPoliciesResponseTypeDef = TypedDict(
    "ListPoliciesResponseTypeDef",
    {
        "Policies": List["PolicyTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPolicyTagsRequestRequestTypeDef = TypedDict(
    "_RequiredListPolicyTagsRequestRequestTypeDef",
    {
        "PolicyArn": str,
    },
)
_OptionalListPolicyTagsRequestRequestTypeDef = TypedDict(
    "_OptionalListPolicyTagsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListPolicyTagsRequestRequestTypeDef(
    _RequiredListPolicyTagsRequestRequestTypeDef, _OptionalListPolicyTagsRequestRequestTypeDef
):
    pass

ListPolicyTagsResponseTypeDef = TypedDict(
    "ListPolicyTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPolicyVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListPolicyVersionsRequestRequestTypeDef",
    {
        "PolicyArn": str,
    },
)
_OptionalListPolicyVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListPolicyVersionsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListPolicyVersionsRequestRequestTypeDef(
    _RequiredListPolicyVersionsRequestRequestTypeDef,
    _OptionalListPolicyVersionsRequestRequestTypeDef,
):
    pass

ListPolicyVersionsResponseTypeDef = TypedDict(
    "ListPolicyVersionsResponseTypeDef",
    {
        "Versions": List["PolicyVersionTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRolePoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredListRolePoliciesRequestRequestTypeDef",
    {
        "RoleName": str,
    },
)
_OptionalListRolePoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalListRolePoliciesRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListRolePoliciesRequestRequestTypeDef(
    _RequiredListRolePoliciesRequestRequestTypeDef, _OptionalListRolePoliciesRequestRequestTypeDef
):
    pass

ListRolePoliciesResponseTypeDef = TypedDict(
    "ListRolePoliciesResponseTypeDef",
    {
        "PolicyNames": List[str],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRoleTagsRequestRequestTypeDef = TypedDict(
    "_RequiredListRoleTagsRequestRequestTypeDef",
    {
        "RoleName": str,
    },
)
_OptionalListRoleTagsRequestRequestTypeDef = TypedDict(
    "_OptionalListRoleTagsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListRoleTagsRequestRequestTypeDef(
    _RequiredListRoleTagsRequestRequestTypeDef, _OptionalListRoleTagsRequestRequestTypeDef
):
    pass

ListRoleTagsResponseTypeDef = TypedDict(
    "ListRoleTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRolesRequestRequestTypeDef = TypedDict(
    "ListRolesRequestRequestTypeDef",
    {
        "PathPrefix": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListRolesResponseTypeDef = TypedDict(
    "ListRolesResponseTypeDef",
    {
        "Roles": List["RoleTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSAMLProviderTagsRequestRequestTypeDef = TypedDict(
    "_RequiredListSAMLProviderTagsRequestRequestTypeDef",
    {
        "SAMLProviderArn": str,
    },
)
_OptionalListSAMLProviderTagsRequestRequestTypeDef = TypedDict(
    "_OptionalListSAMLProviderTagsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListSAMLProviderTagsRequestRequestTypeDef(
    _RequiredListSAMLProviderTagsRequestRequestTypeDef,
    _OptionalListSAMLProviderTagsRequestRequestTypeDef,
):
    pass

ListSAMLProviderTagsResponseTypeDef = TypedDict(
    "ListSAMLProviderTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSAMLProvidersResponseTypeDef = TypedDict(
    "ListSAMLProvidersResponseTypeDef",
    {
        "SAMLProviderList": List["SAMLProviderListEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSSHPublicKeysRequestRequestTypeDef = TypedDict(
    "ListSSHPublicKeysRequestRequestTypeDef",
    {
        "UserName": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListSSHPublicKeysResponseTypeDef = TypedDict(
    "ListSSHPublicKeysResponseTypeDef",
    {
        "SSHPublicKeys": List["SSHPublicKeyMetadataTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServerCertificateTagsRequestRequestTypeDef = TypedDict(
    "_RequiredListServerCertificateTagsRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
    },
)
_OptionalListServerCertificateTagsRequestRequestTypeDef = TypedDict(
    "_OptionalListServerCertificateTagsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListServerCertificateTagsRequestRequestTypeDef(
    _RequiredListServerCertificateTagsRequestRequestTypeDef,
    _OptionalListServerCertificateTagsRequestRequestTypeDef,
):
    pass

ListServerCertificateTagsResponseTypeDef = TypedDict(
    "ListServerCertificateTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServerCertificatesRequestRequestTypeDef = TypedDict(
    "ListServerCertificatesRequestRequestTypeDef",
    {
        "PathPrefix": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListServerCertificatesResponseTypeDef = TypedDict(
    "ListServerCertificatesResponseTypeDef",
    {
        "ServerCertificateMetadataList": List["ServerCertificateMetadataTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceSpecificCredentialsRequestRequestTypeDef = TypedDict(
    "ListServiceSpecificCredentialsRequestRequestTypeDef",
    {
        "UserName": str,
        "ServiceName": str,
    },
    total=False,
)

ListServiceSpecificCredentialsResponseTypeDef = TypedDict(
    "ListServiceSpecificCredentialsResponseTypeDef",
    {
        "ServiceSpecificCredentials": List["ServiceSpecificCredentialMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSigningCertificatesRequestRequestTypeDef = TypedDict(
    "ListSigningCertificatesRequestRequestTypeDef",
    {
        "UserName": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListSigningCertificatesResponseTypeDef = TypedDict(
    "ListSigningCertificatesResponseTypeDef",
    {
        "Certificates": List["SigningCertificateTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUserPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredListUserPoliciesRequestRequestTypeDef",
    {
        "UserName": str,
    },
)
_OptionalListUserPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalListUserPoliciesRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListUserPoliciesRequestRequestTypeDef(
    _RequiredListUserPoliciesRequestRequestTypeDef, _OptionalListUserPoliciesRequestRequestTypeDef
):
    pass

ListUserPoliciesResponseTypeDef = TypedDict(
    "ListUserPoliciesResponseTypeDef",
    {
        "PolicyNames": List[str],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUserTagsRequestRequestTypeDef = TypedDict(
    "_RequiredListUserTagsRequestRequestTypeDef",
    {
        "UserName": str,
    },
)
_OptionalListUserTagsRequestRequestTypeDef = TypedDict(
    "_OptionalListUserTagsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListUserTagsRequestRequestTypeDef(
    _RequiredListUserTagsRequestRequestTypeDef, _OptionalListUserTagsRequestRequestTypeDef
):
    pass

ListUserTagsResponseTypeDef = TypedDict(
    "ListUserTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUsersRequestRequestTypeDef = TypedDict(
    "ListUsersRequestRequestTypeDef",
    {
        "PathPrefix": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "Users": List["UserTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVirtualMFADevicesRequestRequestTypeDef = TypedDict(
    "ListVirtualMFADevicesRequestRequestTypeDef",
    {
        "AssignmentStatus": assignmentStatusTypeType,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListVirtualMFADevicesResponseTypeDef = TypedDict(
    "ListVirtualMFADevicesResponseTypeDef",
    {
        "VirtualMFADevices": List["VirtualMFADeviceTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLoginProfileTypeDef = TypedDict(
    "_RequiredLoginProfileTypeDef",
    {
        "UserName": str,
        "CreateDate": datetime,
    },
)
_OptionalLoginProfileTypeDef = TypedDict(
    "_OptionalLoginProfileTypeDef",
    {
        "PasswordResetRequired": bool,
    },
    total=False,
)

class LoginProfileTypeDef(_RequiredLoginProfileTypeDef, _OptionalLoginProfileTypeDef):
    pass

MFADeviceTypeDef = TypedDict(
    "MFADeviceTypeDef",
    {
        "UserName": str,
        "SerialNumber": str,
        "EnableDate": datetime,
    },
)

ManagedPolicyDetailTypeDef = TypedDict(
    "ManagedPolicyDetailTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
        "PolicyVersionList": List["PolicyVersionTypeDef"],
    },
    total=False,
)

OpenIDConnectProviderListEntryTypeDef = TypedDict(
    "OpenIDConnectProviderListEntryTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

OrganizationsDecisionDetailTypeDef = TypedDict(
    "OrganizationsDecisionDetailTypeDef",
    {
        "AllowedByOrganizations": bool,
    },
    total=False,
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

PasswordPolicyTypeDef = TypedDict(
    "PasswordPolicyTypeDef",
    {
        "MinimumPasswordLength": int,
        "RequireSymbols": bool,
        "RequireNumbers": bool,
        "RequireUppercaseCharacters": bool,
        "RequireLowercaseCharacters": bool,
        "AllowUsersToChangePassword": bool,
        "ExpirePasswords": bool,
        "MaxPasswordAge": int,
        "PasswordReusePrevention": int,
        "HardExpiry": bool,
    },
    total=False,
)

PermissionsBoundaryDecisionDetailTypeDef = TypedDict(
    "PermissionsBoundaryDecisionDetailTypeDef",
    {
        "AllowedByPermissionsBoundary": bool,
    },
    total=False,
)

PolicyDetailTypeDef = TypedDict(
    "PolicyDetailTypeDef",
    {
        "PolicyName": str,
        "PolicyDocument": str,
    },
    total=False,
)

_RequiredPolicyGrantingServiceAccessTypeDef = TypedDict(
    "_RequiredPolicyGrantingServiceAccessTypeDef",
    {
        "PolicyName": str,
        "PolicyType": policyTypeType,
    },
)
_OptionalPolicyGrantingServiceAccessTypeDef = TypedDict(
    "_OptionalPolicyGrantingServiceAccessTypeDef",
    {
        "PolicyArn": str,
        "EntityType": policyOwnerEntityTypeType,
        "EntityName": str,
    },
    total=False,
)

class PolicyGrantingServiceAccessTypeDef(
    _RequiredPolicyGrantingServiceAccessTypeDef, _OptionalPolicyGrantingServiceAccessTypeDef
):
    pass

PolicyGroupTypeDef = TypedDict(
    "PolicyGroupTypeDef",
    {
        "GroupName": str,
        "GroupId": str,
    },
    total=False,
)

PolicyRoleTypeDef = TypedDict(
    "PolicyRoleTypeDef",
    {
        "RoleName": str,
        "RoleId": str,
    },
    total=False,
)

PolicyTypeDef = TypedDict(
    "PolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

PolicyUserTypeDef = TypedDict(
    "PolicyUserTypeDef",
    {
        "UserName": str,
        "UserId": str,
    },
    total=False,
)

PolicyVersionTypeDef = TypedDict(
    "PolicyVersionTypeDef",
    {
        "Document": str,
        "VersionId": str,
        "IsDefaultVersion": bool,
        "CreateDate": datetime,
    },
    total=False,
)

PositionTypeDef = TypedDict(
    "PositionTypeDef",
    {
        "Line": int,
        "Column": int,
    },
    total=False,
)

PutGroupPolicyRequestGroupPolicyTypeDef = TypedDict(
    "PutGroupPolicyRequestGroupPolicyTypeDef",
    {
        "PolicyDocument": str,
    },
)

PutGroupPolicyRequestGroupTypeDef = TypedDict(
    "PutGroupPolicyRequestGroupTypeDef",
    {
        "PolicyName": str,
        "PolicyDocument": str,
    },
)

PutGroupPolicyRequestRequestTypeDef = TypedDict(
    "PutGroupPolicyRequestRequestTypeDef",
    {
        "GroupName": str,
        "PolicyName": str,
        "PolicyDocument": str,
    },
)

PutRolePermissionsBoundaryRequestRequestTypeDef = TypedDict(
    "PutRolePermissionsBoundaryRequestRequestTypeDef",
    {
        "RoleName": str,
        "PermissionsBoundary": str,
    },
)

PutRolePolicyRequestRequestTypeDef = TypedDict(
    "PutRolePolicyRequestRequestTypeDef",
    {
        "RoleName": str,
        "PolicyName": str,
        "PolicyDocument": str,
    },
)

PutRolePolicyRequestRolePolicyTypeDef = TypedDict(
    "PutRolePolicyRequestRolePolicyTypeDef",
    {
        "PolicyDocument": str,
    },
)

PutUserPermissionsBoundaryRequestRequestTypeDef = TypedDict(
    "PutUserPermissionsBoundaryRequestRequestTypeDef",
    {
        "UserName": str,
        "PermissionsBoundary": str,
    },
)

PutUserPolicyRequestRequestTypeDef = TypedDict(
    "PutUserPolicyRequestRequestTypeDef",
    {
        "UserName": str,
        "PolicyName": str,
        "PolicyDocument": str,
    },
)

PutUserPolicyRequestUserPolicyTypeDef = TypedDict(
    "PutUserPolicyRequestUserPolicyTypeDef",
    {
        "PolicyDocument": str,
    },
)

PutUserPolicyRequestUserTypeDef = TypedDict(
    "PutUserPolicyRequestUserTypeDef",
    {
        "PolicyName": str,
        "PolicyDocument": str,
    },
)

RemoveClientIDFromOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "RemoveClientIDFromOpenIDConnectProviderRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "ClientID": str,
    },
)

RemoveRoleFromInstanceProfileRequestInstanceProfileTypeDef = TypedDict(
    "RemoveRoleFromInstanceProfileRequestInstanceProfileTypeDef",
    {
        "RoleName": str,
    },
)

RemoveRoleFromInstanceProfileRequestRequestTypeDef = TypedDict(
    "RemoveRoleFromInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
        "RoleName": str,
    },
)

RemoveUserFromGroupRequestGroupTypeDef = TypedDict(
    "RemoveUserFromGroupRequestGroupTypeDef",
    {
        "UserName": str,
    },
)

RemoveUserFromGroupRequestRequestTypeDef = TypedDict(
    "RemoveUserFromGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserName": str,
    },
)

RemoveUserFromGroupRequestUserTypeDef = TypedDict(
    "RemoveUserFromGroupRequestUserTypeDef",
    {
        "GroupName": str,
    },
)

_RequiredResetServiceSpecificCredentialRequestRequestTypeDef = TypedDict(
    "_RequiredResetServiceSpecificCredentialRequestRequestTypeDef",
    {
        "ServiceSpecificCredentialId": str,
    },
)
_OptionalResetServiceSpecificCredentialRequestRequestTypeDef = TypedDict(
    "_OptionalResetServiceSpecificCredentialRequestRequestTypeDef",
    {
        "UserName": str,
    },
    total=False,
)

class ResetServiceSpecificCredentialRequestRequestTypeDef(
    _RequiredResetServiceSpecificCredentialRequestRequestTypeDef,
    _OptionalResetServiceSpecificCredentialRequestRequestTypeDef,
):
    pass

ResetServiceSpecificCredentialResponseTypeDef = TypedDict(
    "ResetServiceSpecificCredentialResponseTypeDef",
    {
        "ServiceSpecificCredential": "ServiceSpecificCredentialTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredResourceSpecificResultTypeDef = TypedDict(
    "_RequiredResourceSpecificResultTypeDef",
    {
        "EvalResourceName": str,
        "EvalResourceDecision": PolicyEvaluationDecisionTypeType,
    },
)
_OptionalResourceSpecificResultTypeDef = TypedDict(
    "_OptionalResourceSpecificResultTypeDef",
    {
        "MatchedStatements": List["StatementTypeDef"],
        "MissingContextValues": List[str],
        "EvalDecisionDetails": Dict[str, PolicyEvaluationDecisionTypeType],
        "PermissionsBoundaryDecisionDetail": "PermissionsBoundaryDecisionDetailTypeDef",
    },
    total=False,
)

class ResourceSpecificResultTypeDef(
    _RequiredResourceSpecificResultTypeDef, _OptionalResourceSpecificResultTypeDef
):
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

ResyncMFADeviceRequestMfaDeviceTypeDef = TypedDict(
    "ResyncMFADeviceRequestMfaDeviceTypeDef",
    {
        "AuthenticationCode1": str,
        "AuthenticationCode2": str,
    },
)

ResyncMFADeviceRequestRequestTypeDef = TypedDict(
    "ResyncMFADeviceRequestRequestTypeDef",
    {
        "UserName": str,
        "SerialNumber": str,
        "AuthenticationCode1": str,
        "AuthenticationCode2": str,
    },
)

RoleDetailTypeDef = TypedDict(
    "RoleDetailTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "InstanceProfileList": List["InstanceProfileTypeDef"],
        "RolePolicyList": List["PolicyDetailTypeDef"],
        "AttachedManagedPolicies": List["AttachedPolicyTypeDef"],
        "PermissionsBoundary": "AttachedPermissionsBoundaryTypeDef",
        "Tags": List["TagTypeDef"],
        "RoleLastUsed": "RoleLastUsedTypeDef",
    },
    total=False,
)

RoleLastUsedTypeDef = TypedDict(
    "RoleLastUsedTypeDef",
    {
        "LastUsedDate": datetime,
        "Region": str,
    },
    total=False,
)

RolePolicyRequestTypeDef = TypedDict(
    "RolePolicyRequestTypeDef",
    {
        "name": str,
    },
)

_RequiredRoleTypeDef = TypedDict(
    "_RequiredRoleTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
    },
)
_OptionalRoleTypeDef = TypedDict(
    "_OptionalRoleTypeDef",
    {
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": "AttachedPermissionsBoundaryTypeDef",
        "Tags": List["TagTypeDef"],
        "RoleLastUsed": "RoleLastUsedTypeDef",
    },
    total=False,
)

class RoleTypeDef(_RequiredRoleTypeDef, _OptionalRoleTypeDef):
    pass

RoleUsageTypeTypeDef = TypedDict(
    "RoleUsageTypeTypeDef",
    {
        "Region": str,
        "Resources": List[str],
    },
    total=False,
)

SAMLProviderListEntryTypeDef = TypedDict(
    "SAMLProviderListEntryTypeDef",
    {
        "Arn": str,
        "ValidUntil": datetime,
        "CreateDate": datetime,
    },
    total=False,
)

SSHPublicKeyMetadataTypeDef = TypedDict(
    "SSHPublicKeyMetadataTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Status": statusTypeType,
        "UploadDate": datetime,
    },
)

_RequiredSSHPublicKeyTypeDef = TypedDict(
    "_RequiredSSHPublicKeyTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Fingerprint": str,
        "SSHPublicKeyBody": str,
        "Status": statusTypeType,
    },
)
_OptionalSSHPublicKeyTypeDef = TypedDict(
    "_OptionalSSHPublicKeyTypeDef",
    {
        "UploadDate": datetime,
    },
    total=False,
)

class SSHPublicKeyTypeDef(_RequiredSSHPublicKeyTypeDef, _OptionalSSHPublicKeyTypeDef):
    pass

_RequiredServerCertificateMetadataTypeDef = TypedDict(
    "_RequiredServerCertificateMetadataTypeDef",
    {
        "Path": str,
        "ServerCertificateName": str,
        "ServerCertificateId": str,
        "Arn": str,
    },
)
_OptionalServerCertificateMetadataTypeDef = TypedDict(
    "_OptionalServerCertificateMetadataTypeDef",
    {
        "UploadDate": datetime,
        "Expiration": datetime,
    },
    total=False,
)

class ServerCertificateMetadataTypeDef(
    _RequiredServerCertificateMetadataTypeDef, _OptionalServerCertificateMetadataTypeDef
):
    pass

_RequiredServerCertificateTypeDef = TypedDict(
    "_RequiredServerCertificateTypeDef",
    {
        "ServerCertificateMetadata": "ServerCertificateMetadataTypeDef",
        "CertificateBody": str,
    },
)
_OptionalServerCertificateTypeDef = TypedDict(
    "_OptionalServerCertificateTypeDef",
    {
        "CertificateChain": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class ServerCertificateTypeDef(
    _RequiredServerCertificateTypeDef, _OptionalServerCertificateTypeDef
):
    pass

_RequiredServiceLastAccessedTypeDef = TypedDict(
    "_RequiredServiceLastAccessedTypeDef",
    {
        "ServiceName": str,
        "ServiceNamespace": str,
    },
)
_OptionalServiceLastAccessedTypeDef = TypedDict(
    "_OptionalServiceLastAccessedTypeDef",
    {
        "LastAuthenticated": datetime,
        "LastAuthenticatedEntity": str,
        "LastAuthenticatedRegion": str,
        "TotalAuthenticatedEntities": int,
        "TrackedActionsLastAccessed": List["TrackedActionLastAccessedTypeDef"],
    },
    total=False,
)

class ServiceLastAccessedTypeDef(
    _RequiredServiceLastAccessedTypeDef, _OptionalServiceLastAccessedTypeDef
):
    pass

ServiceResourceAccessKeyPairRequestTypeDef = TypedDict(
    "ServiceResourceAccessKeyPairRequestTypeDef",
    {
        "user_name": str,
        "id": str,
        "secret": str,
    },
)

ServiceResourceAccessKeyRequestTypeDef = TypedDict(
    "ServiceResourceAccessKeyRequestTypeDef",
    {
        "user_name": str,
        "id": str,
    },
)

ServiceResourceAssumeRolePolicyRequestTypeDef = TypedDict(
    "ServiceResourceAssumeRolePolicyRequestTypeDef",
    {
        "role_name": str,
    },
)

ServiceResourceGroupPolicyRequestTypeDef = TypedDict(
    "ServiceResourceGroupPolicyRequestTypeDef",
    {
        "group_name": str,
        "name": str,
    },
)

ServiceResourceGroupRequestTypeDef = TypedDict(
    "ServiceResourceGroupRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceInstanceProfileRequestTypeDef = TypedDict(
    "ServiceResourceInstanceProfileRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceLoginProfileRequestTypeDef = TypedDict(
    "ServiceResourceLoginProfileRequestTypeDef",
    {
        "user_name": str,
    },
)

ServiceResourceMfaDeviceRequestTypeDef = TypedDict(
    "ServiceResourceMfaDeviceRequestTypeDef",
    {
        "user_name": str,
        "serial_number": str,
    },
)

ServiceResourcePolicyRequestTypeDef = TypedDict(
    "ServiceResourcePolicyRequestTypeDef",
    {
        "policy_arn": str,
    },
)

ServiceResourcePolicyVersionRequestTypeDef = TypedDict(
    "ServiceResourcePolicyVersionRequestTypeDef",
    {
        "arn": str,
        "version_id": str,
    },
)

ServiceResourceRolePolicyRequestTypeDef = TypedDict(
    "ServiceResourceRolePolicyRequestTypeDef",
    {
        "role_name": str,
        "name": str,
    },
)

ServiceResourceRoleRequestTypeDef = TypedDict(
    "ServiceResourceRoleRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceSamlProviderRequestTypeDef = TypedDict(
    "ServiceResourceSamlProviderRequestTypeDef",
    {
        "arn": str,
    },
)

ServiceResourceServerCertificateRequestTypeDef = TypedDict(
    "ServiceResourceServerCertificateRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceSigningCertificateRequestTypeDef = TypedDict(
    "ServiceResourceSigningCertificateRequestTypeDef",
    {
        "user_name": str,
        "id": str,
    },
)

ServiceResourceUserPolicyRequestTypeDef = TypedDict(
    "ServiceResourceUserPolicyRequestTypeDef",
    {
        "user_name": str,
        "name": str,
    },
)

ServiceResourceUserRequestTypeDef = TypedDict(
    "ServiceResourceUserRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceVirtualMfaDeviceRequestTypeDef = TypedDict(
    "ServiceResourceVirtualMfaDeviceRequestTypeDef",
    {
        "serial_number": str,
    },
)

ServiceSpecificCredentialMetadataTypeDef = TypedDict(
    "ServiceSpecificCredentialMetadataTypeDef",
    {
        "UserName": str,
        "Status": statusTypeType,
        "ServiceUserName": str,
        "CreateDate": datetime,
        "ServiceSpecificCredentialId": str,
        "ServiceName": str,
    },
)

ServiceSpecificCredentialTypeDef = TypedDict(
    "ServiceSpecificCredentialTypeDef",
    {
        "CreateDate": datetime,
        "ServiceName": str,
        "ServiceUserName": str,
        "ServicePassword": str,
        "ServiceSpecificCredentialId": str,
        "UserName": str,
        "Status": statusTypeType,
    },
)

SetDefaultPolicyVersionRequestRequestTypeDef = TypedDict(
    "SetDefaultPolicyVersionRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "VersionId": str,
    },
)

SetSecurityTokenServicePreferencesRequestRequestTypeDef = TypedDict(
    "SetSecurityTokenServicePreferencesRequestRequestTypeDef",
    {
        "GlobalEndpointTokenVersion": globalEndpointTokenVersionType,
    },
)

_RequiredSigningCertificateTypeDef = TypedDict(
    "_RequiredSigningCertificateTypeDef",
    {
        "UserName": str,
        "CertificateId": str,
        "CertificateBody": str,
        "Status": statusTypeType,
    },
)
_OptionalSigningCertificateTypeDef = TypedDict(
    "_OptionalSigningCertificateTypeDef",
    {
        "UploadDate": datetime,
    },
    total=False,
)

class SigningCertificateTypeDef(
    _RequiredSigningCertificateTypeDef, _OptionalSigningCertificateTypeDef
):
    pass

_RequiredSimulateCustomPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredSimulateCustomPolicyRequestRequestTypeDef",
    {
        "PolicyInputList": List[str],
        "ActionNames": List[str],
    },
)
_OptionalSimulateCustomPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalSimulateCustomPolicyRequestRequestTypeDef",
    {
        "PermissionsBoundaryPolicyInputList": List[str],
        "ResourceArns": List[str],
        "ResourcePolicy": str,
        "ResourceOwner": str,
        "CallerArn": str,
        "ContextEntries": List["ContextEntryTypeDef"],
        "ResourceHandlingOption": str,
        "MaxItems": int,
        "Marker": str,
    },
    total=False,
)

class SimulateCustomPolicyRequestRequestTypeDef(
    _RequiredSimulateCustomPolicyRequestRequestTypeDef,
    _OptionalSimulateCustomPolicyRequestRequestTypeDef,
):
    pass

SimulatePolicyResponseTypeDef = TypedDict(
    "SimulatePolicyResponseTypeDef",
    {
        "EvaluationResults": List["EvaluationResultTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSimulatePrincipalPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredSimulatePrincipalPolicyRequestRequestTypeDef",
    {
        "PolicySourceArn": str,
        "ActionNames": List[str],
    },
)
_OptionalSimulatePrincipalPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalSimulatePrincipalPolicyRequestRequestTypeDef",
    {
        "PolicyInputList": List[str],
        "PermissionsBoundaryPolicyInputList": List[str],
        "ResourceArns": List[str],
        "ResourcePolicy": str,
        "ResourceOwner": str,
        "CallerArn": str,
        "ContextEntries": List["ContextEntryTypeDef"],
        "ResourceHandlingOption": str,
        "MaxItems": int,
        "Marker": str,
    },
    total=False,
)

class SimulatePrincipalPolicyRequestRequestTypeDef(
    _RequiredSimulatePrincipalPolicyRequestRequestTypeDef,
    _OptionalSimulatePrincipalPolicyRequestRequestTypeDef,
):
    pass

StatementTypeDef = TypedDict(
    "StatementTypeDef",
    {
        "SourcePolicyId": str,
        "SourcePolicyType": PolicySourceTypeType,
        "StartPosition": "PositionTypeDef",
        "EndPosition": "PositionTypeDef",
    },
    total=False,
)

TagInstanceProfileRequestRequestTypeDef = TypedDict(
    "TagInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
        "Tags": List["TagTypeDef"],
    },
)

TagMFADeviceRequestRequestTypeDef = TypedDict(
    "TagMFADeviceRequestRequestTypeDef",
    {
        "SerialNumber": str,
        "Tags": List["TagTypeDef"],
    },
)

TagOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "TagOpenIDConnectProviderRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagPolicyRequestRequestTypeDef = TypedDict(
    "TagPolicyRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagRoleRequestRequestTypeDef = TypedDict(
    "TagRoleRequestRequestTypeDef",
    {
        "RoleName": str,
        "Tags": List["TagTypeDef"],
    },
)

TagSAMLProviderRequestRequestTypeDef = TypedDict(
    "TagSAMLProviderRequestRequestTypeDef",
    {
        "SAMLProviderArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagServerCertificateRequestRequestTypeDef = TypedDict(
    "TagServerCertificateRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TagUserRequestRequestTypeDef = TypedDict(
    "TagUserRequestRequestTypeDef",
    {
        "UserName": str,
        "Tags": List["TagTypeDef"],
    },
)

TrackedActionLastAccessedTypeDef = TypedDict(
    "TrackedActionLastAccessedTypeDef",
    {
        "ActionName": str,
        "LastAccessedEntity": str,
        "LastAccessedTime": datetime,
        "LastAccessedRegion": str,
    },
    total=False,
)

UntagInstanceProfileRequestRequestTypeDef = TypedDict(
    "UntagInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
        "TagKeys": List[str],
    },
)

UntagMFADeviceRequestRequestTypeDef = TypedDict(
    "UntagMFADeviceRequestRequestTypeDef",
    {
        "SerialNumber": str,
        "TagKeys": List[str],
    },
)

UntagOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "UntagOpenIDConnectProviderRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "TagKeys": List[str],
    },
)

UntagPolicyRequestRequestTypeDef = TypedDict(
    "UntagPolicyRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "TagKeys": List[str],
    },
)

UntagRoleRequestRequestTypeDef = TypedDict(
    "UntagRoleRequestRequestTypeDef",
    {
        "RoleName": str,
        "TagKeys": List[str],
    },
)

UntagSAMLProviderRequestRequestTypeDef = TypedDict(
    "UntagSAMLProviderRequestRequestTypeDef",
    {
        "SAMLProviderArn": str,
        "TagKeys": List[str],
    },
)

UntagServerCertificateRequestRequestTypeDef = TypedDict(
    "UntagServerCertificateRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
        "TagKeys": List[str],
    },
)

UntagUserRequestRequestTypeDef = TypedDict(
    "UntagUserRequestRequestTypeDef",
    {
        "UserName": str,
        "TagKeys": List[str],
    },
)

UpdateAccessKeyRequestAccessKeyPairTypeDef = TypedDict(
    "UpdateAccessKeyRequestAccessKeyPairTypeDef",
    {
        "Status": statusTypeType,
    },
)

UpdateAccessKeyRequestAccessKeyTypeDef = TypedDict(
    "UpdateAccessKeyRequestAccessKeyTypeDef",
    {
        "Status": statusTypeType,
    },
)

_RequiredUpdateAccessKeyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAccessKeyRequestRequestTypeDef",
    {
        "AccessKeyId": str,
        "Status": statusTypeType,
    },
)
_OptionalUpdateAccessKeyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAccessKeyRequestRequestTypeDef",
    {
        "UserName": str,
    },
    total=False,
)

class UpdateAccessKeyRequestRequestTypeDef(
    _RequiredUpdateAccessKeyRequestRequestTypeDef, _OptionalUpdateAccessKeyRequestRequestTypeDef
):
    pass

UpdateAccountPasswordPolicyRequestAccountPasswordPolicyTypeDef = TypedDict(
    "UpdateAccountPasswordPolicyRequestAccountPasswordPolicyTypeDef",
    {
        "MinimumPasswordLength": int,
        "RequireSymbols": bool,
        "RequireNumbers": bool,
        "RequireUppercaseCharacters": bool,
        "RequireLowercaseCharacters": bool,
        "AllowUsersToChangePassword": bool,
        "MaxPasswordAge": int,
        "PasswordReusePrevention": int,
        "HardExpiry": bool,
    },
    total=False,
)

UpdateAccountPasswordPolicyRequestRequestTypeDef = TypedDict(
    "UpdateAccountPasswordPolicyRequestRequestTypeDef",
    {
        "MinimumPasswordLength": int,
        "RequireSymbols": bool,
        "RequireNumbers": bool,
        "RequireUppercaseCharacters": bool,
        "RequireLowercaseCharacters": bool,
        "AllowUsersToChangePassword": bool,
        "MaxPasswordAge": int,
        "PasswordReusePrevention": int,
        "HardExpiry": bool,
    },
    total=False,
)

UpdateAccountPasswordPolicyRequestServiceResourceTypeDef = TypedDict(
    "UpdateAccountPasswordPolicyRequestServiceResourceTypeDef",
    {
        "MinimumPasswordLength": int,
        "RequireSymbols": bool,
        "RequireNumbers": bool,
        "RequireUppercaseCharacters": bool,
        "RequireLowercaseCharacters": bool,
        "AllowUsersToChangePassword": bool,
        "MaxPasswordAge": int,
        "PasswordReusePrevention": int,
        "HardExpiry": bool,
    },
    total=False,
)

UpdateAssumeRolePolicyRequestAssumeRolePolicyTypeDef = TypedDict(
    "UpdateAssumeRolePolicyRequestAssumeRolePolicyTypeDef",
    {
        "PolicyDocument": str,
    },
)

UpdateAssumeRolePolicyRequestRequestTypeDef = TypedDict(
    "UpdateAssumeRolePolicyRequestRequestTypeDef",
    {
        "RoleName": str,
        "PolicyDocument": str,
    },
)

UpdateGroupRequestGroupTypeDef = TypedDict(
    "UpdateGroupRequestGroupTypeDef",
    {
        "NewPath": str,
        "NewGroupName": str,
    },
    total=False,
)

_RequiredUpdateGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
    },
)
_OptionalUpdateGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateGroupRequestRequestTypeDef",
    {
        "NewPath": str,
        "NewGroupName": str,
    },
    total=False,
)

class UpdateGroupRequestRequestTypeDef(
    _RequiredUpdateGroupRequestRequestTypeDef, _OptionalUpdateGroupRequestRequestTypeDef
):
    pass

UpdateLoginProfileRequestLoginProfileTypeDef = TypedDict(
    "UpdateLoginProfileRequestLoginProfileTypeDef",
    {
        "Password": str,
        "PasswordResetRequired": bool,
    },
    total=False,
)

_RequiredUpdateLoginProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLoginProfileRequestRequestTypeDef",
    {
        "UserName": str,
    },
)
_OptionalUpdateLoginProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLoginProfileRequestRequestTypeDef",
    {
        "Password": str,
        "PasswordResetRequired": bool,
    },
    total=False,
)

class UpdateLoginProfileRequestRequestTypeDef(
    _RequiredUpdateLoginProfileRequestRequestTypeDef,
    _OptionalUpdateLoginProfileRequestRequestTypeDef,
):
    pass

UpdateOpenIDConnectProviderThumbprintRequestRequestTypeDef = TypedDict(
    "UpdateOpenIDConnectProviderThumbprintRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "ThumbprintList": List[str],
    },
)

UpdateRoleDescriptionRequestRequestTypeDef = TypedDict(
    "UpdateRoleDescriptionRequestRequestTypeDef",
    {
        "RoleName": str,
        "Description": str,
    },
)

UpdateRoleDescriptionResponseTypeDef = TypedDict(
    "UpdateRoleDescriptionResponseTypeDef",
    {
        "Role": "RoleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRoleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRoleRequestRequestTypeDef",
    {
        "RoleName": str,
    },
)
_OptionalUpdateRoleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRoleRequestRequestTypeDef",
    {
        "Description": str,
        "MaxSessionDuration": int,
    },
    total=False,
)

class UpdateRoleRequestRequestTypeDef(
    _RequiredUpdateRoleRequestRequestTypeDef, _OptionalUpdateRoleRequestRequestTypeDef
):
    pass

UpdateSAMLProviderRequestRequestTypeDef = TypedDict(
    "UpdateSAMLProviderRequestRequestTypeDef",
    {
        "SAMLMetadataDocument": str,
        "SAMLProviderArn": str,
    },
)

UpdateSAMLProviderRequestSamlProviderTypeDef = TypedDict(
    "UpdateSAMLProviderRequestSamlProviderTypeDef",
    {
        "SAMLMetadataDocument": str,
    },
)

UpdateSAMLProviderResponseTypeDef = TypedDict(
    "UpdateSAMLProviderResponseTypeDef",
    {
        "SAMLProviderArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSSHPublicKeyRequestRequestTypeDef = TypedDict(
    "UpdateSSHPublicKeyRequestRequestTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Status": statusTypeType,
    },
)

_RequiredUpdateServerCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateServerCertificateRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
    },
)
_OptionalUpdateServerCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateServerCertificateRequestRequestTypeDef",
    {
        "NewPath": str,
        "NewServerCertificateName": str,
    },
    total=False,
)

class UpdateServerCertificateRequestRequestTypeDef(
    _RequiredUpdateServerCertificateRequestRequestTypeDef,
    _OptionalUpdateServerCertificateRequestRequestTypeDef,
):
    pass

UpdateServerCertificateRequestServerCertificateTypeDef = TypedDict(
    "UpdateServerCertificateRequestServerCertificateTypeDef",
    {
        "NewPath": str,
        "NewServerCertificateName": str,
    },
    total=False,
)

_RequiredUpdateServiceSpecificCredentialRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateServiceSpecificCredentialRequestRequestTypeDef",
    {
        "ServiceSpecificCredentialId": str,
        "Status": statusTypeType,
    },
)
_OptionalUpdateServiceSpecificCredentialRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateServiceSpecificCredentialRequestRequestTypeDef",
    {
        "UserName": str,
    },
    total=False,
)

class UpdateServiceSpecificCredentialRequestRequestTypeDef(
    _RequiredUpdateServiceSpecificCredentialRequestRequestTypeDef,
    _OptionalUpdateServiceSpecificCredentialRequestRequestTypeDef,
):
    pass

_RequiredUpdateSigningCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSigningCertificateRequestRequestTypeDef",
    {
        "CertificateId": str,
        "Status": statusTypeType,
    },
)
_OptionalUpdateSigningCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSigningCertificateRequestRequestTypeDef",
    {
        "UserName": str,
    },
    total=False,
)

class UpdateSigningCertificateRequestRequestTypeDef(
    _RequiredUpdateSigningCertificateRequestRequestTypeDef,
    _OptionalUpdateSigningCertificateRequestRequestTypeDef,
):
    pass

UpdateSigningCertificateRequestSigningCertificateTypeDef = TypedDict(
    "UpdateSigningCertificateRequestSigningCertificateTypeDef",
    {
        "Status": statusTypeType,
    },
)

_RequiredUpdateUserRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserRequestRequestTypeDef",
    {
        "UserName": str,
    },
)
_OptionalUpdateUserRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserRequestRequestTypeDef",
    {
        "NewPath": str,
        "NewUserName": str,
    },
    total=False,
)

class UpdateUserRequestRequestTypeDef(
    _RequiredUpdateUserRequestRequestTypeDef, _OptionalUpdateUserRequestRequestTypeDef
):
    pass

UpdateUserRequestUserTypeDef = TypedDict(
    "UpdateUserRequestUserTypeDef",
    {
        "NewPath": str,
        "NewUserName": str,
    },
    total=False,
)

UploadSSHPublicKeyRequestRequestTypeDef = TypedDict(
    "UploadSSHPublicKeyRequestRequestTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyBody": str,
    },
)

UploadSSHPublicKeyResponseTypeDef = TypedDict(
    "UploadSSHPublicKeyResponseTypeDef",
    {
        "SSHPublicKey": "SSHPublicKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUploadServerCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredUploadServerCertificateRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
        "CertificateBody": str,
        "PrivateKey": str,
    },
)
_OptionalUploadServerCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalUploadServerCertificateRequestRequestTypeDef",
    {
        "Path": str,
        "CertificateChain": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class UploadServerCertificateRequestRequestTypeDef(
    _RequiredUploadServerCertificateRequestRequestTypeDef,
    _OptionalUploadServerCertificateRequestRequestTypeDef,
):
    pass

_RequiredUploadServerCertificateRequestServiceResourceTypeDef = TypedDict(
    "_RequiredUploadServerCertificateRequestServiceResourceTypeDef",
    {
        "ServerCertificateName": str,
        "CertificateBody": str,
        "PrivateKey": str,
    },
)
_OptionalUploadServerCertificateRequestServiceResourceTypeDef = TypedDict(
    "_OptionalUploadServerCertificateRequestServiceResourceTypeDef",
    {
        "Path": str,
        "CertificateChain": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class UploadServerCertificateRequestServiceResourceTypeDef(
    _RequiredUploadServerCertificateRequestServiceResourceTypeDef,
    _OptionalUploadServerCertificateRequestServiceResourceTypeDef,
):
    pass

UploadServerCertificateResponseTypeDef = TypedDict(
    "UploadServerCertificateResponseTypeDef",
    {
        "ServerCertificateMetadata": "ServerCertificateMetadataTypeDef",
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUploadSigningCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredUploadSigningCertificateRequestRequestTypeDef",
    {
        "CertificateBody": str,
    },
)
_OptionalUploadSigningCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalUploadSigningCertificateRequestRequestTypeDef",
    {
        "UserName": str,
    },
    total=False,
)

class UploadSigningCertificateRequestRequestTypeDef(
    _RequiredUploadSigningCertificateRequestRequestTypeDef,
    _OptionalUploadSigningCertificateRequestRequestTypeDef,
):
    pass

_RequiredUploadSigningCertificateRequestServiceResourceTypeDef = TypedDict(
    "_RequiredUploadSigningCertificateRequestServiceResourceTypeDef",
    {
        "CertificateBody": str,
    },
)
_OptionalUploadSigningCertificateRequestServiceResourceTypeDef = TypedDict(
    "_OptionalUploadSigningCertificateRequestServiceResourceTypeDef",
    {
        "UserName": str,
    },
    total=False,
)

class UploadSigningCertificateRequestServiceResourceTypeDef(
    _RequiredUploadSigningCertificateRequestServiceResourceTypeDef,
    _OptionalUploadSigningCertificateRequestServiceResourceTypeDef,
):
    pass

UploadSigningCertificateResponseTypeDef = TypedDict(
    "UploadSigningCertificateResponseTypeDef",
    {
        "Certificate": "SigningCertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserAccessKeyRequestTypeDef = TypedDict(
    "UserAccessKeyRequestTypeDef",
    {
        "id": str,
    },
)

UserDetailTypeDef = TypedDict(
    "UserDetailTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "UserPolicyList": List["PolicyDetailTypeDef"],
        "GroupList": List[str],
        "AttachedManagedPolicies": List["AttachedPolicyTypeDef"],
        "PermissionsBoundary": "AttachedPermissionsBoundaryTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

UserMfaDeviceRequestTypeDef = TypedDict(
    "UserMfaDeviceRequestTypeDef",
    {
        "serial_number": str,
    },
)

UserPolicyRequestTypeDef = TypedDict(
    "UserPolicyRequestTypeDef",
    {
        "name": str,
    },
)

UserSigningCertificateRequestTypeDef = TypedDict(
    "UserSigningCertificateRequestTypeDef",
    {
        "id": str,
    },
)

_RequiredUserTypeDef = TypedDict(
    "_RequiredUserTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
    },
)
_OptionalUserTypeDef = TypedDict(
    "_OptionalUserTypeDef",
    {
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": "AttachedPermissionsBoundaryTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class UserTypeDef(_RequiredUserTypeDef, _OptionalUserTypeDef):
    pass

_RequiredVirtualMFADeviceTypeDef = TypedDict(
    "_RequiredVirtualMFADeviceTypeDef",
    {
        "SerialNumber": str,
    },
)
_OptionalVirtualMFADeviceTypeDef = TypedDict(
    "_OptionalVirtualMFADeviceTypeDef",
    {
        "Base32StringSeed": bytes,
        "QRCodePNG": bytes,
        "User": "UserTypeDef",
        "EnableDate": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class VirtualMFADeviceTypeDef(_RequiredVirtualMFADeviceTypeDef, _OptionalVirtualMFADeviceTypeDef):
    pass

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
