"""
Type annotations for iam service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_iam.type_defs import AccessDetailTypeDef

    data: AccessDetailTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AccessAdvisorUsageGranularityTypeType,
    AssertionEncryptionModeTypeType,
    AssignmentStatusTypeType,
    ContextKeyTypeEnumType,
    DeletionTaskStatusTypeType,
    EncodingTypeType,
    EntityTypeType,
    FeatureTypeType,
    GlobalEndpointTokenVersionType,
    JobStatusTypeType,
    PolicyEvaluationDecisionTypeType,
    PolicyOwnerEntityTypeType,
    PolicyScopeTypeType,
    PolicySourceTypeType,
    PolicyTypeType,
    PolicyUsageTypeType,
    ReportStateTypeType,
    SortKeyTypeType,
    StatusTypeType,
    SummaryKeyTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccessDetailTypeDef",
    "AccessKeyLastUsedTypeDef",
    "AccessKeyMetadataTypeDef",
    "AccessKeyTypeDef",
    "AddClientIDToOpenIDConnectProviderRequestTypeDef",
    "AddRoleToInstanceProfileRequestInstanceProfileAddRoleTypeDef",
    "AddRoleToInstanceProfileRequestTypeDef",
    "AddUserToGroupRequestGroupAddUserTypeDef",
    "AddUserToGroupRequestTypeDef",
    "AddUserToGroupRequestUserAddGroupTypeDef",
    "AttachGroupPolicyRequestGroupAttachPolicyTypeDef",
    "AttachGroupPolicyRequestPolicyAttachGroupTypeDef",
    "AttachGroupPolicyRequestTypeDef",
    "AttachRolePolicyRequestPolicyAttachRoleTypeDef",
    "AttachRolePolicyRequestRoleAttachPolicyTypeDef",
    "AttachRolePolicyRequestTypeDef",
    "AttachUserPolicyRequestPolicyAttachUserTypeDef",
    "AttachUserPolicyRequestTypeDef",
    "AttachUserPolicyRequestUserAttachPolicyTypeDef",
    "AttachedPermissionsBoundaryTypeDef",
    "AttachedPolicyTypeDef",
    "ChangePasswordRequestServiceResourceChangePasswordTypeDef",
    "ChangePasswordRequestTypeDef",
    "ContextEntryTypeDef",
    "CreateAccessKeyRequestTypeDef",
    "CreateAccessKeyResponseTypeDef",
    "CreateAccountAliasRequestServiceResourceCreateAccountAliasTypeDef",
    "CreateAccountAliasRequestTypeDef",
    "CreateGroupRequestGroupCreateTypeDef",
    "CreateGroupRequestServiceResourceCreateGroupTypeDef",
    "CreateGroupRequestTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateInstanceProfileRequestServiceResourceCreateInstanceProfileTypeDef",
    "CreateInstanceProfileRequestTypeDef",
    "CreateInstanceProfileResponseTypeDef",
    "CreateLoginProfileRequestLoginProfileCreateTypeDef",
    "CreateLoginProfileRequestTypeDef",
    "CreateLoginProfileRequestUserCreateLoginProfileTypeDef",
    "CreateLoginProfileResponseTypeDef",
    "CreateOpenIDConnectProviderRequestTypeDef",
    "CreateOpenIDConnectProviderResponseTypeDef",
    "CreatePolicyRequestServiceResourceCreatePolicyTypeDef",
    "CreatePolicyRequestTypeDef",
    "CreatePolicyResponseTypeDef",
    "CreatePolicyVersionRequestPolicyCreateVersionTypeDef",
    "CreatePolicyVersionRequestTypeDef",
    "CreatePolicyVersionResponseTypeDef",
    "CreateRoleRequestServiceResourceCreateRoleTypeDef",
    "CreateRoleRequestTypeDef",
    "CreateRoleResponseTypeDef",
    "CreateSAMLProviderRequestServiceResourceCreateSamlProviderTypeDef",
    "CreateSAMLProviderRequestTypeDef",
    "CreateSAMLProviderResponseTypeDef",
    "CreateServiceLinkedRoleRequestTypeDef",
    "CreateServiceLinkedRoleResponseTypeDef",
    "CreateServiceSpecificCredentialRequestTypeDef",
    "CreateServiceSpecificCredentialResponseTypeDef",
    "CreateUserRequestServiceResourceCreateUserTypeDef",
    "CreateUserRequestTypeDef",
    "CreateUserRequestUserCreateTypeDef",
    "CreateUserResponseTypeDef",
    "CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDeviceTypeDef",
    "CreateVirtualMFADeviceRequestTypeDef",
    "CreateVirtualMFADeviceResponseTypeDef",
    "DeactivateMFADeviceRequestTypeDef",
    "DeleteAccessKeyRequestTypeDef",
    "DeleteAccountAliasRequestTypeDef",
    "DeleteGroupPolicyRequestTypeDef",
    "DeleteGroupRequestTypeDef",
    "DeleteInstanceProfileRequestTypeDef",
    "DeleteLoginProfileRequestTypeDef",
    "DeleteOpenIDConnectProviderRequestTypeDef",
    "DeletePolicyRequestTypeDef",
    "DeletePolicyVersionRequestTypeDef",
    "DeleteRolePermissionsBoundaryRequestTypeDef",
    "DeleteRolePolicyRequestTypeDef",
    "DeleteRoleRequestTypeDef",
    "DeleteSAMLProviderRequestTypeDef",
    "DeleteSSHPublicKeyRequestTypeDef",
    "DeleteServerCertificateRequestTypeDef",
    "DeleteServiceLinkedRoleRequestTypeDef",
    "DeleteServiceLinkedRoleResponseTypeDef",
    "DeleteServiceSpecificCredentialRequestTypeDef",
    "DeleteSigningCertificateRequestTypeDef",
    "DeleteUserPermissionsBoundaryRequestTypeDef",
    "DeleteUserPolicyRequestTypeDef",
    "DeleteUserRequestTypeDef",
    "DeleteVirtualMFADeviceRequestTypeDef",
    "DeletionTaskFailureReasonTypeTypeDef",
    "DetachGroupPolicyRequestGroupDetachPolicyTypeDef",
    "DetachGroupPolicyRequestPolicyDetachGroupTypeDef",
    "DetachGroupPolicyRequestTypeDef",
    "DetachRolePolicyRequestPolicyDetachRoleTypeDef",
    "DetachRolePolicyRequestRoleDetachPolicyTypeDef",
    "DetachRolePolicyRequestTypeDef",
    "DetachUserPolicyRequestPolicyDetachUserTypeDef",
    "DetachUserPolicyRequestTypeDef",
    "DetachUserPolicyRequestUserDetachPolicyTypeDef",
    "DisableOrganizationsRootCredentialsManagementResponseTypeDef",
    "DisableOrganizationsRootSessionsResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableMFADeviceRequestMfaDeviceAssociateTypeDef",
    "EnableMFADeviceRequestTypeDef",
    "EnableMFADeviceRequestUserEnableMfaTypeDef",
    "EnableOrganizationsRootCredentialsManagementResponseTypeDef",
    "EnableOrganizationsRootSessionsResponseTypeDef",
    "EntityDetailsTypeDef",
    "EntityInfoTypeDef",
    "ErrorDetailsTypeDef",
    "EvaluationResultTypeDef",
    "GenerateCredentialReportResponseTypeDef",
    "GenerateOrganizationsAccessReportRequestTypeDef",
    "GenerateOrganizationsAccessReportResponseTypeDef",
    "GenerateServiceLastAccessedDetailsRequestTypeDef",
    "GenerateServiceLastAccessedDetailsResponseTypeDef",
    "GetAccessKeyLastUsedRequestTypeDef",
    "GetAccessKeyLastUsedResponseTypeDef",
    "GetAccountAuthorizationDetailsRequestPaginateTypeDef",
    "GetAccountAuthorizationDetailsRequestTypeDef",
    "GetAccountAuthorizationDetailsResponseTypeDef",
    "GetAccountPasswordPolicyResponseTypeDef",
    "GetAccountSummaryResponseTypeDef",
    "GetContextKeysForCustomPolicyRequestTypeDef",
    "GetContextKeysForPolicyResponseTypeDef",
    "GetContextKeysForPrincipalPolicyRequestTypeDef",
    "GetCredentialReportResponseTypeDef",
    "GetGroupPolicyRequestTypeDef",
    "GetGroupPolicyResponseTypeDef",
    "GetGroupRequestPaginateTypeDef",
    "GetGroupRequestTypeDef",
    "GetGroupResponseTypeDef",
    "GetInstanceProfileRequestTypeDef",
    "GetInstanceProfileRequestWaitTypeDef",
    "GetInstanceProfileResponseTypeDef",
    "GetLoginProfileRequestTypeDef",
    "GetLoginProfileResponseTypeDef",
    "GetMFADeviceRequestTypeDef",
    "GetMFADeviceResponseTypeDef",
    "GetOpenIDConnectProviderRequestTypeDef",
    "GetOpenIDConnectProviderResponseTypeDef",
    "GetOrganizationsAccessReportRequestTypeDef",
    "GetOrganizationsAccessReportResponseTypeDef",
    "GetPolicyRequestTypeDef",
    "GetPolicyRequestWaitTypeDef",
    "GetPolicyResponseTypeDef",
    "GetPolicyVersionRequestTypeDef",
    "GetPolicyVersionResponseTypeDef",
    "GetRolePolicyRequestTypeDef",
    "GetRolePolicyResponseTypeDef",
    "GetRoleRequestTypeDef",
    "GetRoleRequestWaitTypeDef",
    "GetRoleResponseTypeDef",
    "GetSAMLProviderRequestTypeDef",
    "GetSAMLProviderResponseTypeDef",
    "GetSSHPublicKeyRequestTypeDef",
    "GetSSHPublicKeyResponseTypeDef",
    "GetServerCertificateRequestTypeDef",
    "GetServerCertificateResponseTypeDef",
    "GetServiceLastAccessedDetailsRequestTypeDef",
    "GetServiceLastAccessedDetailsResponseTypeDef",
    "GetServiceLastAccessedDetailsWithEntitiesRequestTypeDef",
    "GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef",
    "GetServiceLinkedRoleDeletionStatusRequestTypeDef",
    "GetServiceLinkedRoleDeletionStatusResponseTypeDef",
    "GetUserPolicyRequestTypeDef",
    "GetUserPolicyResponseTypeDef",
    "GetUserRequestTypeDef",
    "GetUserRequestWaitTypeDef",
    "GetUserResponseTypeDef",
    "GroupDetailTypeDef",
    "GroupTypeDef",
    "InstanceProfileTypeDef",
    "ListAccessKeysRequestPaginateTypeDef",
    "ListAccessKeysRequestTypeDef",
    "ListAccessKeysResponseTypeDef",
    "ListAccountAliasesRequestPaginateTypeDef",
    "ListAccountAliasesRequestTypeDef",
    "ListAccountAliasesResponseTypeDef",
    "ListAttachedGroupPoliciesRequestPaginateTypeDef",
    "ListAttachedGroupPoliciesRequestTypeDef",
    "ListAttachedGroupPoliciesResponseTypeDef",
    "ListAttachedRolePoliciesRequestPaginateTypeDef",
    "ListAttachedRolePoliciesRequestTypeDef",
    "ListAttachedRolePoliciesResponseTypeDef",
    "ListAttachedUserPoliciesRequestPaginateTypeDef",
    "ListAttachedUserPoliciesRequestTypeDef",
    "ListAttachedUserPoliciesResponseTypeDef",
    "ListEntitiesForPolicyRequestPaginateTypeDef",
    "ListEntitiesForPolicyRequestTypeDef",
    "ListEntitiesForPolicyResponseTypeDef",
    "ListGroupPoliciesRequestPaginateTypeDef",
    "ListGroupPoliciesRequestTypeDef",
    "ListGroupPoliciesResponseTypeDef",
    "ListGroupsForUserRequestPaginateTypeDef",
    "ListGroupsForUserRequestTypeDef",
    "ListGroupsForUserResponseTypeDef",
    "ListGroupsRequestPaginateTypeDef",
    "ListGroupsRequestTypeDef",
    "ListGroupsResponseTypeDef",
    "ListInstanceProfileTagsRequestPaginateTypeDef",
    "ListInstanceProfileTagsRequestTypeDef",
    "ListInstanceProfileTagsResponseTypeDef",
    "ListInstanceProfilesForRoleRequestPaginateTypeDef",
    "ListInstanceProfilesForRoleRequestTypeDef",
    "ListInstanceProfilesForRoleResponseTypeDef",
    "ListInstanceProfilesRequestPaginateTypeDef",
    "ListInstanceProfilesRequestTypeDef",
    "ListInstanceProfilesResponseTypeDef",
    "ListMFADeviceTagsRequestPaginateTypeDef",
    "ListMFADeviceTagsRequestTypeDef",
    "ListMFADeviceTagsResponseTypeDef",
    "ListMFADevicesRequestPaginateTypeDef",
    "ListMFADevicesRequestTypeDef",
    "ListMFADevicesResponseTypeDef",
    "ListOpenIDConnectProviderTagsRequestPaginateTypeDef",
    "ListOpenIDConnectProviderTagsRequestTypeDef",
    "ListOpenIDConnectProviderTagsResponseTypeDef",
    "ListOpenIDConnectProvidersResponseTypeDef",
    "ListOrganizationsFeaturesResponseTypeDef",
    "ListPoliciesGrantingServiceAccessEntryTypeDef",
    "ListPoliciesGrantingServiceAccessRequestTypeDef",
    "ListPoliciesGrantingServiceAccessResponseTypeDef",
    "ListPoliciesRequestPaginateTypeDef",
    "ListPoliciesRequestTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListPolicyTagsRequestPaginateTypeDef",
    "ListPolicyTagsRequestTypeDef",
    "ListPolicyTagsResponseTypeDef",
    "ListPolicyVersionsRequestPaginateTypeDef",
    "ListPolicyVersionsRequestTypeDef",
    "ListPolicyVersionsResponseTypeDef",
    "ListRolePoliciesRequestPaginateTypeDef",
    "ListRolePoliciesRequestTypeDef",
    "ListRolePoliciesResponseTypeDef",
    "ListRoleTagsRequestPaginateTypeDef",
    "ListRoleTagsRequestTypeDef",
    "ListRoleTagsResponseTypeDef",
    "ListRolesRequestPaginateTypeDef",
    "ListRolesRequestTypeDef",
    "ListRolesResponseTypeDef",
    "ListSAMLProviderTagsRequestPaginateTypeDef",
    "ListSAMLProviderTagsRequestTypeDef",
    "ListSAMLProviderTagsResponseTypeDef",
    "ListSAMLProvidersResponseTypeDef",
    "ListSSHPublicKeysRequestPaginateTypeDef",
    "ListSSHPublicKeysRequestTypeDef",
    "ListSSHPublicKeysResponseTypeDef",
    "ListServerCertificateTagsRequestPaginateTypeDef",
    "ListServerCertificateTagsRequestTypeDef",
    "ListServerCertificateTagsResponseTypeDef",
    "ListServerCertificatesRequestPaginateTypeDef",
    "ListServerCertificatesRequestTypeDef",
    "ListServerCertificatesResponseTypeDef",
    "ListServiceSpecificCredentialsRequestTypeDef",
    "ListServiceSpecificCredentialsResponseTypeDef",
    "ListSigningCertificatesRequestPaginateTypeDef",
    "ListSigningCertificatesRequestTypeDef",
    "ListSigningCertificatesResponseTypeDef",
    "ListUserPoliciesRequestPaginateTypeDef",
    "ListUserPoliciesRequestTypeDef",
    "ListUserPoliciesResponseTypeDef",
    "ListUserTagsRequestPaginateTypeDef",
    "ListUserTagsRequestTypeDef",
    "ListUserTagsResponseTypeDef",
    "ListUsersRequestPaginateTypeDef",
    "ListUsersRequestTypeDef",
    "ListUsersResponseTypeDef",
    "ListVirtualMFADevicesRequestPaginateTypeDef",
    "ListVirtualMFADevicesRequestTypeDef",
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
    "PolicyDocumentDictTypeDef",
    "PolicyDocumentStatementTypeDef",
    "PolicyDocumentTypeDef",
    "PolicyGrantingServiceAccessTypeDef",
    "PolicyGroupTypeDef",
    "PolicyRoleTypeDef",
    "PolicyTypeDef",
    "PolicyUserTypeDef",
    "PolicyVersionTypeDef",
    "PositionTypeDef",
    "PutGroupPolicyRequestGroupCreatePolicyTypeDef",
    "PutGroupPolicyRequestGroupPolicyPutTypeDef",
    "PutGroupPolicyRequestTypeDef",
    "PutRolePermissionsBoundaryRequestTypeDef",
    "PutRolePolicyRequestRolePolicyPutTypeDef",
    "PutRolePolicyRequestTypeDef",
    "PutUserPermissionsBoundaryRequestTypeDef",
    "PutUserPolicyRequestTypeDef",
    "PutUserPolicyRequestUserCreatePolicyTypeDef",
    "PutUserPolicyRequestUserPolicyPutTypeDef",
    "RemoveClientIDFromOpenIDConnectProviderRequestTypeDef",
    "RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRoleTypeDef",
    "RemoveRoleFromInstanceProfileRequestTypeDef",
    "RemoveUserFromGroupRequestGroupRemoveUserTypeDef",
    "RemoveUserFromGroupRequestTypeDef",
    "RemoveUserFromGroupRequestUserRemoveGroupTypeDef",
    "ResetServiceSpecificCredentialRequestTypeDef",
    "ResetServiceSpecificCredentialResponseTypeDef",
    "ResourceSpecificResultTypeDef",
    "ResponseMetadataTypeDef",
    "ResyncMFADeviceRequestMfaDeviceResyncTypeDef",
    "ResyncMFADeviceRequestTypeDef",
    "RoleDetailTypeDef",
    "RoleLastUsedTypeDef",
    "RoleTypeDef",
    "RoleUsageTypeTypeDef",
    "SAMLPrivateKeyTypeDef",
    "SAMLProviderListEntryTypeDef",
    "SSHPublicKeyMetadataTypeDef",
    "SSHPublicKeyTypeDef",
    "ServerCertificateMetadataTypeDef",
    "ServerCertificateTypeDef",
    "ServiceLastAccessedTypeDef",
    "ServiceSpecificCredentialMetadataTypeDef",
    "ServiceSpecificCredentialTypeDef",
    "SetDefaultPolicyVersionRequestTypeDef",
    "SetSecurityTokenServicePreferencesRequestTypeDef",
    "SigningCertificateTypeDef",
    "SimulateCustomPolicyRequestPaginateTypeDef",
    "SimulateCustomPolicyRequestTypeDef",
    "SimulatePolicyResponseTypeDef",
    "SimulatePrincipalPolicyRequestPaginateTypeDef",
    "SimulatePrincipalPolicyRequestTypeDef",
    "StatementTypeDef",
    "TagInstanceProfileRequestTypeDef",
    "TagMFADeviceRequestTypeDef",
    "TagOpenIDConnectProviderRequestTypeDef",
    "TagPolicyRequestTypeDef",
    "TagRoleRequestTypeDef",
    "TagSAMLProviderRequestTypeDef",
    "TagServerCertificateRequestTypeDef",
    "TagTypeDef",
    "TagUserRequestTypeDef",
    "TrackedActionLastAccessedTypeDef",
    "UntagInstanceProfileRequestTypeDef",
    "UntagMFADeviceRequestTypeDef",
    "UntagOpenIDConnectProviderRequestTypeDef",
    "UntagPolicyRequestTypeDef",
    "UntagRoleRequestTypeDef",
    "UntagSAMLProviderRequestTypeDef",
    "UntagServerCertificateRequestTypeDef",
    "UntagUserRequestTypeDef",
    "UpdateAccessKeyRequestAccessKeyActivateTypeDef",
    "UpdateAccessKeyRequestAccessKeyDeactivateTypeDef",
    "UpdateAccessKeyRequestAccessKeyPairActivateTypeDef",
    "UpdateAccessKeyRequestAccessKeyPairDeactivateTypeDef",
    "UpdateAccessKeyRequestTypeDef",
    "UpdateAccountPasswordPolicyRequestAccountPasswordPolicyUpdateTypeDef",
    "UpdateAccountPasswordPolicyRequestServiceResourceCreateAccountPasswordPolicyTypeDef",
    "UpdateAccountPasswordPolicyRequestTypeDef",
    "UpdateAssumeRolePolicyRequestAssumeRolePolicyUpdateTypeDef",
    "UpdateAssumeRolePolicyRequestTypeDef",
    "UpdateGroupRequestGroupUpdateTypeDef",
    "UpdateGroupRequestTypeDef",
    "UpdateLoginProfileRequestLoginProfileUpdateTypeDef",
    "UpdateLoginProfileRequestTypeDef",
    "UpdateOpenIDConnectProviderThumbprintRequestTypeDef",
    "UpdateRoleDescriptionRequestTypeDef",
    "UpdateRoleDescriptionResponseTypeDef",
    "UpdateRoleRequestTypeDef",
    "UpdateSAMLProviderRequestSamlProviderUpdateTypeDef",
    "UpdateSAMLProviderRequestTypeDef",
    "UpdateSAMLProviderResponseTypeDef",
    "UpdateSSHPublicKeyRequestTypeDef",
    "UpdateServerCertificateRequestServerCertificateUpdateTypeDef",
    "UpdateServerCertificateRequestTypeDef",
    "UpdateServiceSpecificCredentialRequestTypeDef",
    "UpdateSigningCertificateRequestSigningCertificateActivateTypeDef",
    "UpdateSigningCertificateRequestSigningCertificateDeactivateTypeDef",
    "UpdateSigningCertificateRequestTypeDef",
    "UpdateUserRequestTypeDef",
    "UpdateUserRequestUserUpdateTypeDef",
    "UploadSSHPublicKeyRequestTypeDef",
    "UploadSSHPublicKeyResponseTypeDef",
    "UploadServerCertificateRequestServiceResourceCreateServerCertificateTypeDef",
    "UploadServerCertificateRequestTypeDef",
    "UploadServerCertificateResponseTypeDef",
    "UploadSigningCertificateRequestServiceResourceCreateSigningCertificateTypeDef",
    "UploadSigningCertificateRequestTypeDef",
    "UploadSigningCertificateResponseTypeDef",
    "UserDetailTypeDef",
    "UserTypeDef",
    "VirtualMFADeviceTypeDef",
    "WaiterConfigTypeDef",
)

AccessDetailTypeDef = TypedDict(
    "AccessDetailTypeDef",
    {
        "ServiceName": str,
        "ServiceNamespace": str,
        "Region": NotRequired[str],
        "EntityPath": NotRequired[str],
        "LastAuthenticatedTime": NotRequired[datetime],
        "TotalAuthenticatedEntities": NotRequired[int],
    },
)
AccessKeyLastUsedTypeDef = TypedDict(
    "AccessKeyLastUsedTypeDef",
    {
        "ServiceName": str,
        "Region": str,
        "LastUsedDate": NotRequired[datetime],
    },
)

class AccessKeyMetadataTypeDef(TypedDict):
    UserName: NotRequired[str]
    AccessKeyId: NotRequired[str]
    Status: NotRequired[StatusTypeType]
    CreateDate: NotRequired[datetime]

class AccessKeyTypeDef(TypedDict):
    UserName: str
    AccessKeyId: str
    Status: StatusTypeType
    SecretAccessKey: str
    CreateDate: NotRequired[datetime]

class AddClientIDToOpenIDConnectProviderRequestTypeDef(TypedDict):
    OpenIDConnectProviderArn: str
    ClientID: str

class AddRoleToInstanceProfileRequestInstanceProfileAddRoleTypeDef(TypedDict):
    RoleName: str

class AddRoleToInstanceProfileRequestTypeDef(TypedDict):
    InstanceProfileName: str
    RoleName: str

class AddUserToGroupRequestGroupAddUserTypeDef(TypedDict):
    UserName: str

class AddUserToGroupRequestTypeDef(TypedDict):
    GroupName: str
    UserName: str

class AddUserToGroupRequestUserAddGroupTypeDef(TypedDict):
    GroupName: str

class AttachGroupPolicyRequestGroupAttachPolicyTypeDef(TypedDict):
    PolicyArn: str

class AttachGroupPolicyRequestPolicyAttachGroupTypeDef(TypedDict):
    GroupName: str

class AttachGroupPolicyRequestTypeDef(TypedDict):
    GroupName: str
    PolicyArn: str

class AttachRolePolicyRequestPolicyAttachRoleTypeDef(TypedDict):
    RoleName: str

class AttachRolePolicyRequestRoleAttachPolicyTypeDef(TypedDict):
    PolicyArn: str

class AttachRolePolicyRequestTypeDef(TypedDict):
    RoleName: str
    PolicyArn: str

class AttachUserPolicyRequestPolicyAttachUserTypeDef(TypedDict):
    UserName: str

class AttachUserPolicyRequestTypeDef(TypedDict):
    UserName: str
    PolicyArn: str

class AttachUserPolicyRequestUserAttachPolicyTypeDef(TypedDict):
    PolicyArn: str

class AttachedPermissionsBoundaryTypeDef(TypedDict):
    PermissionsBoundaryType: NotRequired[Literal["PermissionsBoundaryPolicy"]]
    PermissionsBoundaryArn: NotRequired[str]

class AttachedPolicyTypeDef(TypedDict):
    PolicyName: NotRequired[str]
    PolicyArn: NotRequired[str]

class ChangePasswordRequestServiceResourceChangePasswordTypeDef(TypedDict):
    OldPassword: str
    NewPassword: str

class ChangePasswordRequestTypeDef(TypedDict):
    OldPassword: str
    NewPassword: str

class ContextEntryTypeDef(TypedDict):
    ContextKeyName: NotRequired[str]
    ContextKeyValues: NotRequired[Sequence[str]]
    ContextKeyType: NotRequired[ContextKeyTypeEnumType]

class CreateAccessKeyRequestTypeDef(TypedDict):
    UserName: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateAccountAliasRequestServiceResourceCreateAccountAliasTypeDef(TypedDict):
    AccountAlias: str

class CreateAccountAliasRequestTypeDef(TypedDict):
    AccountAlias: str

class CreateGroupRequestGroupCreateTypeDef(TypedDict):
    Path: NotRequired[str]

class CreateGroupRequestServiceResourceCreateGroupTypeDef(TypedDict):
    GroupName: str
    Path: NotRequired[str]

class CreateGroupRequestTypeDef(TypedDict):
    GroupName: str
    Path: NotRequired[str]

class GroupTypeDef(TypedDict):
    Path: str
    GroupName: str
    GroupId: str
    Arn: str
    CreateDate: datetime

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class CreateLoginProfileRequestLoginProfileCreateTypeDef(TypedDict):
    Password: NotRequired[str]
    PasswordResetRequired: NotRequired[bool]

class CreateLoginProfileRequestTypeDef(TypedDict):
    UserName: NotRequired[str]
    Password: NotRequired[str]
    PasswordResetRequired: NotRequired[bool]

class CreateLoginProfileRequestUserCreateLoginProfileTypeDef(TypedDict):
    Password: NotRequired[str]
    PasswordResetRequired: NotRequired[bool]

class LoginProfileTypeDef(TypedDict):
    UserName: str
    CreateDate: datetime
    PasswordResetRequired: NotRequired[bool]

class CreatePolicyVersionRequestPolicyCreateVersionTypeDef(TypedDict):
    PolicyDocument: str
    SetAsDefault: NotRequired[bool]

class CreatePolicyVersionRequestTypeDef(TypedDict):
    PolicyArn: str
    PolicyDocument: str
    SetAsDefault: NotRequired[bool]

class CreateServiceLinkedRoleRequestTypeDef(TypedDict):
    AWSServiceName: str
    Description: NotRequired[str]
    CustomSuffix: NotRequired[str]

CreateServiceSpecificCredentialRequestTypeDef = TypedDict(
    "CreateServiceSpecificCredentialRequestTypeDef",
    {
        "UserName": str,
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
        "Status": StatusTypeType,
    },
)

class DeactivateMFADeviceRequestTypeDef(TypedDict):
    SerialNumber: str
    UserName: NotRequired[str]

class DeleteAccessKeyRequestTypeDef(TypedDict):
    AccessKeyId: str
    UserName: NotRequired[str]

class DeleteAccountAliasRequestTypeDef(TypedDict):
    AccountAlias: str

class DeleteGroupPolicyRequestTypeDef(TypedDict):
    GroupName: str
    PolicyName: str

class DeleteGroupRequestTypeDef(TypedDict):
    GroupName: str

class DeleteInstanceProfileRequestTypeDef(TypedDict):
    InstanceProfileName: str

class DeleteLoginProfileRequestTypeDef(TypedDict):
    UserName: NotRequired[str]

class DeleteOpenIDConnectProviderRequestTypeDef(TypedDict):
    OpenIDConnectProviderArn: str

class DeletePolicyRequestTypeDef(TypedDict):
    PolicyArn: str

class DeletePolicyVersionRequestTypeDef(TypedDict):
    PolicyArn: str
    VersionId: str

class DeleteRolePermissionsBoundaryRequestTypeDef(TypedDict):
    RoleName: str

class DeleteRolePolicyRequestTypeDef(TypedDict):
    RoleName: str
    PolicyName: str

class DeleteRoleRequestTypeDef(TypedDict):
    RoleName: str

class DeleteSAMLProviderRequestTypeDef(TypedDict):
    SAMLProviderArn: str

class DeleteSSHPublicKeyRequestTypeDef(TypedDict):
    UserName: str
    SSHPublicKeyId: str

class DeleteServerCertificateRequestTypeDef(TypedDict):
    ServerCertificateName: str

class DeleteServiceLinkedRoleRequestTypeDef(TypedDict):
    RoleName: str

class DeleteServiceSpecificCredentialRequestTypeDef(TypedDict):
    ServiceSpecificCredentialId: str
    UserName: NotRequired[str]

class DeleteSigningCertificateRequestTypeDef(TypedDict):
    CertificateId: str
    UserName: NotRequired[str]

class DeleteUserPermissionsBoundaryRequestTypeDef(TypedDict):
    UserName: str

class DeleteUserPolicyRequestTypeDef(TypedDict):
    UserName: str
    PolicyName: str

class DeleteUserRequestTypeDef(TypedDict):
    UserName: str

class DeleteVirtualMFADeviceRequestTypeDef(TypedDict):
    SerialNumber: str

class RoleUsageTypeTypeDef(TypedDict):
    Region: NotRequired[str]
    Resources: NotRequired[List[str]]

class DetachGroupPolicyRequestGroupDetachPolicyTypeDef(TypedDict):
    PolicyArn: str

class DetachGroupPolicyRequestPolicyDetachGroupTypeDef(TypedDict):
    GroupName: str

class DetachGroupPolicyRequestTypeDef(TypedDict):
    GroupName: str
    PolicyArn: str

class DetachRolePolicyRequestPolicyDetachRoleTypeDef(TypedDict):
    RoleName: str

class DetachRolePolicyRequestRoleDetachPolicyTypeDef(TypedDict):
    PolicyArn: str

class DetachRolePolicyRequestTypeDef(TypedDict):
    RoleName: str
    PolicyArn: str

class DetachUserPolicyRequestPolicyDetachUserTypeDef(TypedDict):
    UserName: str

class DetachUserPolicyRequestTypeDef(TypedDict):
    UserName: str
    PolicyArn: str

class DetachUserPolicyRequestUserDetachPolicyTypeDef(TypedDict):
    PolicyArn: str

class EnableMFADeviceRequestMfaDeviceAssociateTypeDef(TypedDict):
    AuthenticationCode1: str
    AuthenticationCode2: str

class EnableMFADeviceRequestTypeDef(TypedDict):
    UserName: str
    SerialNumber: str
    AuthenticationCode1: str
    AuthenticationCode2: str

class EnableMFADeviceRequestUserEnableMfaTypeDef(TypedDict):
    SerialNumber: str
    AuthenticationCode1: str
    AuthenticationCode2: str

EntityInfoTypeDef = TypedDict(
    "EntityInfoTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": PolicyOwnerEntityTypeType,
        "Id": str,
        "Path": NotRequired[str],
    },
)

class ErrorDetailsTypeDef(TypedDict):
    Message: str
    Code: str

class OrganizationsDecisionDetailTypeDef(TypedDict):
    AllowedByOrganizations: NotRequired[bool]

class PermissionsBoundaryDecisionDetailTypeDef(TypedDict):
    AllowedByPermissionsBoundary: NotRequired[bool]

class GenerateOrganizationsAccessReportRequestTypeDef(TypedDict):
    EntityPath: str
    OrganizationsPolicyId: NotRequired[str]

class GenerateServiceLastAccessedDetailsRequestTypeDef(TypedDict):
    Arn: str
    Granularity: NotRequired[AccessAdvisorUsageGranularityTypeType]

class GetAccessKeyLastUsedRequestTypeDef(TypedDict):
    AccessKeyId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetAccountAuthorizationDetailsRequestTypeDef(TypedDict):
    Filter: NotRequired[Sequence[EntityTypeType]]
    MaxItems: NotRequired[int]
    Marker: NotRequired[str]

class PasswordPolicyTypeDef(TypedDict):
    MinimumPasswordLength: NotRequired[int]
    RequireSymbols: NotRequired[bool]
    RequireNumbers: NotRequired[bool]
    RequireUppercaseCharacters: NotRequired[bool]
    RequireLowercaseCharacters: NotRequired[bool]
    AllowUsersToChangePassword: NotRequired[bool]
    ExpirePasswords: NotRequired[bool]
    MaxPasswordAge: NotRequired[int]
    PasswordReusePrevention: NotRequired[int]
    HardExpiry: NotRequired[bool]

class GetContextKeysForCustomPolicyRequestTypeDef(TypedDict):
    PolicyInputList: Sequence[str]

class GetContextKeysForPrincipalPolicyRequestTypeDef(TypedDict):
    PolicySourceArn: str
    PolicyInputList: NotRequired[Sequence[str]]

class GetGroupPolicyRequestTypeDef(TypedDict):
    GroupName: str
    PolicyName: str

class GetGroupRequestTypeDef(TypedDict):
    GroupName: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class GetInstanceProfileRequestTypeDef(TypedDict):
    InstanceProfileName: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class GetLoginProfileRequestTypeDef(TypedDict):
    UserName: NotRequired[str]

class GetMFADeviceRequestTypeDef(TypedDict):
    SerialNumber: str
    UserName: NotRequired[str]

class GetOpenIDConnectProviderRequestTypeDef(TypedDict):
    OpenIDConnectProviderArn: str

class GetOrganizationsAccessReportRequestTypeDef(TypedDict):
    JobId: str
    MaxItems: NotRequired[int]
    Marker: NotRequired[str]
    SortKey: NotRequired[SortKeyTypeType]

class GetPolicyRequestTypeDef(TypedDict):
    PolicyArn: str

class GetPolicyVersionRequestTypeDef(TypedDict):
    PolicyArn: str
    VersionId: str

class GetRolePolicyRequestTypeDef(TypedDict):
    RoleName: str
    PolicyName: str

class GetRoleRequestTypeDef(TypedDict):
    RoleName: str

class GetSAMLProviderRequestTypeDef(TypedDict):
    SAMLProviderArn: str

class SAMLPrivateKeyTypeDef(TypedDict):
    KeyId: NotRequired[str]
    Timestamp: NotRequired[datetime]

class GetSSHPublicKeyRequestTypeDef(TypedDict):
    UserName: str
    SSHPublicKeyId: str
    Encoding: EncodingTypeType

class SSHPublicKeyTypeDef(TypedDict):
    UserName: str
    SSHPublicKeyId: str
    Fingerprint: str
    SSHPublicKeyBody: str
    Status: StatusTypeType
    UploadDate: NotRequired[datetime]

class GetServerCertificateRequestTypeDef(TypedDict):
    ServerCertificateName: str

class GetServiceLastAccessedDetailsRequestTypeDef(TypedDict):
    JobId: str
    MaxItems: NotRequired[int]
    Marker: NotRequired[str]

class GetServiceLastAccessedDetailsWithEntitiesRequestTypeDef(TypedDict):
    JobId: str
    ServiceNamespace: str
    MaxItems: NotRequired[int]
    Marker: NotRequired[str]

class GetServiceLinkedRoleDeletionStatusRequestTypeDef(TypedDict):
    DeletionTaskId: str

class GetUserPolicyRequestTypeDef(TypedDict):
    UserName: str
    PolicyName: str

class GetUserRequestTypeDef(TypedDict):
    UserName: NotRequired[str]

class ListAccessKeysRequestTypeDef(TypedDict):
    UserName: NotRequired[str]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListAccountAliasesRequestTypeDef(TypedDict):
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListAttachedGroupPoliciesRequestTypeDef(TypedDict):
    GroupName: str
    PathPrefix: NotRequired[str]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListAttachedRolePoliciesRequestTypeDef(TypedDict):
    RoleName: str
    PathPrefix: NotRequired[str]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListAttachedUserPoliciesRequestTypeDef(TypedDict):
    UserName: str
    PathPrefix: NotRequired[str]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListEntitiesForPolicyRequestTypeDef(TypedDict):
    PolicyArn: str
    EntityFilter: NotRequired[EntityTypeType]
    PathPrefix: NotRequired[str]
    PolicyUsageFilter: NotRequired[PolicyUsageTypeType]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class PolicyGroupTypeDef(TypedDict):
    GroupName: NotRequired[str]
    GroupId: NotRequired[str]

class PolicyRoleTypeDef(TypedDict):
    RoleName: NotRequired[str]
    RoleId: NotRequired[str]

class PolicyUserTypeDef(TypedDict):
    UserName: NotRequired[str]
    UserId: NotRequired[str]

class ListGroupPoliciesRequestTypeDef(TypedDict):
    GroupName: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListGroupsForUserRequestTypeDef(TypedDict):
    UserName: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListGroupsRequestTypeDef(TypedDict):
    PathPrefix: NotRequired[str]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListInstanceProfileTagsRequestTypeDef(TypedDict):
    InstanceProfileName: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListInstanceProfilesForRoleRequestTypeDef(TypedDict):
    RoleName: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListInstanceProfilesRequestTypeDef(TypedDict):
    PathPrefix: NotRequired[str]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListMFADeviceTagsRequestTypeDef(TypedDict):
    SerialNumber: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListMFADevicesRequestTypeDef(TypedDict):
    UserName: NotRequired[str]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class MFADeviceTypeDef(TypedDict):
    UserName: str
    SerialNumber: str
    EnableDate: datetime

class ListOpenIDConnectProviderTagsRequestTypeDef(TypedDict):
    OpenIDConnectProviderArn: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class OpenIDConnectProviderListEntryTypeDef(TypedDict):
    Arn: NotRequired[str]

class PolicyGrantingServiceAccessTypeDef(TypedDict):
    PolicyName: str
    PolicyType: PolicyTypeType
    PolicyArn: NotRequired[str]
    EntityType: NotRequired[PolicyOwnerEntityTypeType]
    EntityName: NotRequired[str]

class ListPoliciesGrantingServiceAccessRequestTypeDef(TypedDict):
    Arn: str
    ServiceNamespaces: Sequence[str]
    Marker: NotRequired[str]

class ListPoliciesRequestTypeDef(TypedDict):
    Scope: NotRequired[PolicyScopeTypeType]
    OnlyAttached: NotRequired[bool]
    PathPrefix: NotRequired[str]
    PolicyUsageFilter: NotRequired[PolicyUsageTypeType]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListPolicyTagsRequestTypeDef(TypedDict):
    PolicyArn: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListPolicyVersionsRequestTypeDef(TypedDict):
    PolicyArn: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListRolePoliciesRequestTypeDef(TypedDict):
    RoleName: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListRoleTagsRequestTypeDef(TypedDict):
    RoleName: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListRolesRequestTypeDef(TypedDict):
    PathPrefix: NotRequired[str]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListSAMLProviderTagsRequestTypeDef(TypedDict):
    SAMLProviderArn: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class SAMLProviderListEntryTypeDef(TypedDict):
    Arn: NotRequired[str]
    ValidUntil: NotRequired[datetime]
    CreateDate: NotRequired[datetime]

class ListSSHPublicKeysRequestTypeDef(TypedDict):
    UserName: NotRequired[str]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class SSHPublicKeyMetadataTypeDef(TypedDict):
    UserName: str
    SSHPublicKeyId: str
    Status: StatusTypeType
    UploadDate: datetime

class ListServerCertificateTagsRequestTypeDef(TypedDict):
    ServerCertificateName: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListServerCertificatesRequestTypeDef(TypedDict):
    PathPrefix: NotRequired[str]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ServerCertificateMetadataTypeDef(TypedDict):
    Path: str
    ServerCertificateName: str
    ServerCertificateId: str
    Arn: str
    UploadDate: NotRequired[datetime]
    Expiration: NotRequired[datetime]

ListServiceSpecificCredentialsRequestTypeDef = TypedDict(
    "ListServiceSpecificCredentialsRequestTypeDef",
    {
        "UserName": NotRequired[str],
        "ServiceName": NotRequired[str],
    },
)
ServiceSpecificCredentialMetadataTypeDef = TypedDict(
    "ServiceSpecificCredentialMetadataTypeDef",
    {
        "UserName": str,
        "Status": StatusTypeType,
        "ServiceUserName": str,
        "CreateDate": datetime,
        "ServiceSpecificCredentialId": str,
        "ServiceName": str,
    },
)

class ListSigningCertificatesRequestTypeDef(TypedDict):
    UserName: NotRequired[str]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class SigningCertificateTypeDef(TypedDict):
    UserName: str
    CertificateId: str
    CertificateBody: str
    Status: StatusTypeType
    UploadDate: NotRequired[datetime]

class ListUserPoliciesRequestTypeDef(TypedDict):
    UserName: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListUserTagsRequestTypeDef(TypedDict):
    UserName: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListUsersRequestTypeDef(TypedDict):
    PathPrefix: NotRequired[str]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListVirtualMFADevicesRequestTypeDef(TypedDict):
    AssignmentStatus: NotRequired[AssignmentStatusTypeType]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class PolicyDocumentStatementTypeDef(TypedDict):
    Effect: str
    Resource: str | List[str]
    Sid: str
    Action: str | List[str]

class PositionTypeDef(TypedDict):
    Line: NotRequired[int]
    Column: NotRequired[int]

class PutGroupPolicyRequestGroupCreatePolicyTypeDef(TypedDict):
    PolicyName: str
    PolicyDocument: str

class PutGroupPolicyRequestGroupPolicyPutTypeDef(TypedDict):
    PolicyDocument: str

class PutGroupPolicyRequestTypeDef(TypedDict):
    GroupName: str
    PolicyName: str
    PolicyDocument: str

class PutRolePermissionsBoundaryRequestTypeDef(TypedDict):
    RoleName: str
    PermissionsBoundary: str

class PutRolePolicyRequestRolePolicyPutTypeDef(TypedDict):
    PolicyDocument: str

class PutRolePolicyRequestTypeDef(TypedDict):
    RoleName: str
    PolicyName: str
    PolicyDocument: str

class PutUserPermissionsBoundaryRequestTypeDef(TypedDict):
    UserName: str
    PermissionsBoundary: str

class PutUserPolicyRequestTypeDef(TypedDict):
    UserName: str
    PolicyName: str
    PolicyDocument: str

class PutUserPolicyRequestUserCreatePolicyTypeDef(TypedDict):
    PolicyName: str
    PolicyDocument: str

class PutUserPolicyRequestUserPolicyPutTypeDef(TypedDict):
    PolicyDocument: str

class RemoveClientIDFromOpenIDConnectProviderRequestTypeDef(TypedDict):
    OpenIDConnectProviderArn: str
    ClientID: str

class RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRoleTypeDef(TypedDict):
    RoleName: str

class RemoveRoleFromInstanceProfileRequestTypeDef(TypedDict):
    InstanceProfileName: str
    RoleName: str

class RemoveUserFromGroupRequestGroupRemoveUserTypeDef(TypedDict):
    UserName: str

class RemoveUserFromGroupRequestTypeDef(TypedDict):
    GroupName: str
    UserName: str

class RemoveUserFromGroupRequestUserRemoveGroupTypeDef(TypedDict):
    GroupName: str

class ResetServiceSpecificCredentialRequestTypeDef(TypedDict):
    ServiceSpecificCredentialId: str
    UserName: NotRequired[str]

class ResyncMFADeviceRequestMfaDeviceResyncTypeDef(TypedDict):
    AuthenticationCode1: str
    AuthenticationCode2: str

class ResyncMFADeviceRequestTypeDef(TypedDict):
    UserName: str
    SerialNumber: str
    AuthenticationCode1: str
    AuthenticationCode2: str

class RoleLastUsedTypeDef(TypedDict):
    LastUsedDate: NotRequired[datetime]
    Region: NotRequired[str]

class TrackedActionLastAccessedTypeDef(TypedDict):
    ActionName: NotRequired[str]
    LastAccessedEntity: NotRequired[str]
    LastAccessedTime: NotRequired[datetime]
    LastAccessedRegion: NotRequired[str]

class SetDefaultPolicyVersionRequestTypeDef(TypedDict):
    PolicyArn: str
    VersionId: str

class SetSecurityTokenServicePreferencesRequestTypeDef(TypedDict):
    GlobalEndpointTokenVersion: GlobalEndpointTokenVersionType

class UntagInstanceProfileRequestTypeDef(TypedDict):
    InstanceProfileName: str
    TagKeys: Sequence[str]

class UntagMFADeviceRequestTypeDef(TypedDict):
    SerialNumber: str
    TagKeys: Sequence[str]

class UntagOpenIDConnectProviderRequestTypeDef(TypedDict):
    OpenIDConnectProviderArn: str
    TagKeys: Sequence[str]

class UntagPolicyRequestTypeDef(TypedDict):
    PolicyArn: str
    TagKeys: Sequence[str]

class UntagRoleRequestTypeDef(TypedDict):
    RoleName: str
    TagKeys: Sequence[str]

class UntagSAMLProviderRequestTypeDef(TypedDict):
    SAMLProviderArn: str
    TagKeys: Sequence[str]

class UntagServerCertificateRequestTypeDef(TypedDict):
    ServerCertificateName: str
    TagKeys: Sequence[str]

class UntagUserRequestTypeDef(TypedDict):
    UserName: str
    TagKeys: Sequence[str]

class UpdateAccessKeyRequestAccessKeyActivateTypeDef(TypedDict):
    Status: NotRequired[StatusTypeType]

class UpdateAccessKeyRequestAccessKeyDeactivateTypeDef(TypedDict):
    Status: NotRequired[StatusTypeType]

class UpdateAccessKeyRequestAccessKeyPairActivateTypeDef(TypedDict):
    Status: NotRequired[StatusTypeType]

class UpdateAccessKeyRequestAccessKeyPairDeactivateTypeDef(TypedDict):
    Status: NotRequired[StatusTypeType]

class UpdateAccessKeyRequestTypeDef(TypedDict):
    AccessKeyId: str
    Status: StatusTypeType
    UserName: NotRequired[str]

class UpdateAccountPasswordPolicyRequestAccountPasswordPolicyUpdateTypeDef(TypedDict):
    MinimumPasswordLength: NotRequired[int]
    RequireSymbols: NotRequired[bool]
    RequireNumbers: NotRequired[bool]
    RequireUppercaseCharacters: NotRequired[bool]
    RequireLowercaseCharacters: NotRequired[bool]
    AllowUsersToChangePassword: NotRequired[bool]
    MaxPasswordAge: NotRequired[int]
    PasswordReusePrevention: NotRequired[int]
    HardExpiry: NotRequired[bool]

class UpdateAccountPasswordPolicyRequestServiceResourceCreateAccountPasswordPolicyTypeDef(
    TypedDict
):
    MinimumPasswordLength: NotRequired[int]
    RequireSymbols: NotRequired[bool]
    RequireNumbers: NotRequired[bool]
    RequireUppercaseCharacters: NotRequired[bool]
    RequireLowercaseCharacters: NotRequired[bool]
    AllowUsersToChangePassword: NotRequired[bool]
    MaxPasswordAge: NotRequired[int]
    PasswordReusePrevention: NotRequired[int]
    HardExpiry: NotRequired[bool]

class UpdateAccountPasswordPolicyRequestTypeDef(TypedDict):
    MinimumPasswordLength: NotRequired[int]
    RequireSymbols: NotRequired[bool]
    RequireNumbers: NotRequired[bool]
    RequireUppercaseCharacters: NotRequired[bool]
    RequireLowercaseCharacters: NotRequired[bool]
    AllowUsersToChangePassword: NotRequired[bool]
    MaxPasswordAge: NotRequired[int]
    PasswordReusePrevention: NotRequired[int]
    HardExpiry: NotRequired[bool]

class UpdateAssumeRolePolicyRequestAssumeRolePolicyUpdateTypeDef(TypedDict):
    PolicyDocument: str

class UpdateAssumeRolePolicyRequestTypeDef(TypedDict):
    RoleName: str
    PolicyDocument: str

class UpdateGroupRequestGroupUpdateTypeDef(TypedDict):
    NewPath: NotRequired[str]
    NewGroupName: NotRequired[str]

class UpdateGroupRequestTypeDef(TypedDict):
    GroupName: str
    NewPath: NotRequired[str]
    NewGroupName: NotRequired[str]

class UpdateLoginProfileRequestLoginProfileUpdateTypeDef(TypedDict):
    Password: NotRequired[str]
    PasswordResetRequired: NotRequired[bool]

class UpdateLoginProfileRequestTypeDef(TypedDict):
    UserName: str
    Password: NotRequired[str]
    PasswordResetRequired: NotRequired[bool]

class UpdateOpenIDConnectProviderThumbprintRequestTypeDef(TypedDict):
    OpenIDConnectProviderArn: str
    ThumbprintList: Sequence[str]

class UpdateRoleDescriptionRequestTypeDef(TypedDict):
    RoleName: str
    Description: str

class UpdateRoleRequestTypeDef(TypedDict):
    RoleName: str
    Description: NotRequired[str]
    MaxSessionDuration: NotRequired[int]

class UpdateSAMLProviderRequestSamlProviderUpdateTypeDef(TypedDict):
    SAMLMetadataDocument: NotRequired[str]
    AssertionEncryptionMode: NotRequired[AssertionEncryptionModeTypeType]
    AddPrivateKey: NotRequired[str]
    RemovePrivateKey: NotRequired[str]

class UpdateSAMLProviderRequestTypeDef(TypedDict):
    SAMLProviderArn: str
    SAMLMetadataDocument: NotRequired[str]
    AssertionEncryptionMode: NotRequired[AssertionEncryptionModeTypeType]
    AddPrivateKey: NotRequired[str]
    RemovePrivateKey: NotRequired[str]

class UpdateSSHPublicKeyRequestTypeDef(TypedDict):
    UserName: str
    SSHPublicKeyId: str
    Status: StatusTypeType

class UpdateServerCertificateRequestServerCertificateUpdateTypeDef(TypedDict):
    NewPath: NotRequired[str]
    NewServerCertificateName: NotRequired[str]

class UpdateServerCertificateRequestTypeDef(TypedDict):
    ServerCertificateName: str
    NewPath: NotRequired[str]
    NewServerCertificateName: NotRequired[str]

class UpdateServiceSpecificCredentialRequestTypeDef(TypedDict):
    ServiceSpecificCredentialId: str
    Status: StatusTypeType
    UserName: NotRequired[str]

class UpdateSigningCertificateRequestSigningCertificateActivateTypeDef(TypedDict):
    Status: NotRequired[StatusTypeType]

class UpdateSigningCertificateRequestSigningCertificateDeactivateTypeDef(TypedDict):
    Status: NotRequired[StatusTypeType]

class UpdateSigningCertificateRequestTypeDef(TypedDict):
    CertificateId: str
    Status: StatusTypeType
    UserName: NotRequired[str]

class UpdateUserRequestTypeDef(TypedDict):
    UserName: str
    NewPath: NotRequired[str]
    NewUserName: NotRequired[str]

class UpdateUserRequestUserUpdateTypeDef(TypedDict):
    NewPath: NotRequired[str]
    NewUserName: NotRequired[str]

class UploadSSHPublicKeyRequestTypeDef(TypedDict):
    UserName: str
    SSHPublicKeyBody: str

class UploadSigningCertificateRequestServiceResourceCreateSigningCertificateTypeDef(TypedDict):
    CertificateBody: str
    UserName: NotRequired[str]

class UploadSigningCertificateRequestTypeDef(TypedDict):
    CertificateBody: str
    UserName: NotRequired[str]

class SimulateCustomPolicyRequestTypeDef(TypedDict):
    PolicyInputList: Sequence[str]
    ActionNames: Sequence[str]
    PermissionsBoundaryPolicyInputList: NotRequired[Sequence[str]]
    ResourceArns: NotRequired[Sequence[str]]
    ResourcePolicy: NotRequired[str]
    ResourceOwner: NotRequired[str]
    CallerArn: NotRequired[str]
    ContextEntries: NotRequired[Sequence[ContextEntryTypeDef]]
    ResourceHandlingOption: NotRequired[str]
    MaxItems: NotRequired[int]
    Marker: NotRequired[str]

class SimulatePrincipalPolicyRequestTypeDef(TypedDict):
    PolicySourceArn: str
    ActionNames: Sequence[str]
    PolicyInputList: NotRequired[Sequence[str]]
    PermissionsBoundaryPolicyInputList: NotRequired[Sequence[str]]
    ResourceArns: NotRequired[Sequence[str]]
    ResourcePolicy: NotRequired[str]
    ResourceOwner: NotRequired[str]
    CallerArn: NotRequired[str]
    ContextEntries: NotRequired[Sequence[ContextEntryTypeDef]]
    ResourceHandlingOption: NotRequired[str]
    MaxItems: NotRequired[int]
    Marker: NotRequired[str]

class CreateAccessKeyResponseTypeDef(TypedDict):
    AccessKey: AccessKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceLinkedRoleResponseTypeDef(TypedDict):
    DeletionTaskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableOrganizationsRootCredentialsManagementResponseTypeDef(TypedDict):
    OrganizationId: str
    EnabledFeatures: List[FeatureTypeType]
    ResponseMetadata: ResponseMetadataTypeDef

class DisableOrganizationsRootSessionsResponseTypeDef(TypedDict):
    OrganizationId: str
    EnabledFeatures: List[FeatureTypeType]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class EnableOrganizationsRootCredentialsManagementResponseTypeDef(TypedDict):
    OrganizationId: str
    EnabledFeatures: List[FeatureTypeType]
    ResponseMetadata: ResponseMetadataTypeDef

class EnableOrganizationsRootSessionsResponseTypeDef(TypedDict):
    OrganizationId: str
    EnabledFeatures: List[FeatureTypeType]
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateCredentialReportResponseTypeDef(TypedDict):
    State: ReportStateTypeType
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateOrganizationsAccessReportResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateServiceLastAccessedDetailsResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessKeyLastUsedResponseTypeDef(TypedDict):
    UserName: str
    AccessKeyLastUsed: AccessKeyLastUsedTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountSummaryResponseTypeDef(TypedDict):
    SummaryMap: Dict[SummaryKeyTypeType, int]
    ResponseMetadata: ResponseMetadataTypeDef

class GetContextKeysForPolicyResponseTypeDef(TypedDict):
    ContextKeyNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCredentialReportResponseTypeDef(TypedDict):
    Content: bytes
    ReportFormat: Literal["text/csv"]
    GeneratedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetMFADeviceResponseTypeDef(TypedDict):
    UserName: str
    SerialNumber: str
    EnableDate: datetime
    Certifications: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessKeysResponseTypeDef(TypedDict):
    AccessKeyMetadata: List[AccessKeyMetadataTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountAliasesResponseTypeDef(TypedDict):
    AccountAliases: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttachedGroupPoliciesResponseTypeDef(TypedDict):
    AttachedPolicies: List[AttachedPolicyTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttachedRolePoliciesResponseTypeDef(TypedDict):
    AttachedPolicies: List[AttachedPolicyTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttachedUserPoliciesResponseTypeDef(TypedDict):
    AttachedPolicies: List[AttachedPolicyTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupPoliciesResponseTypeDef(TypedDict):
    PolicyNames: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOrganizationsFeaturesResponseTypeDef(TypedDict):
    OrganizationId: str
    EnabledFeatures: List[FeatureTypeType]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRolePoliciesResponseTypeDef(TypedDict):
    PolicyNames: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListUserPoliciesResponseTypeDef(TypedDict):
    PolicyNames: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSAMLProviderResponseTypeDef(TypedDict):
    SAMLProviderArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupResponseTypeDef(TypedDict):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsForUserResponseTypeDef(TypedDict):
    Groups: List[GroupTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsResponseTypeDef(TypedDict):
    Groups: List[GroupTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceProfileRequestServiceResourceCreateInstanceProfileTypeDef(TypedDict):
    InstanceProfileName: str
    Path: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateInstanceProfileRequestTypeDef(TypedDict):
    InstanceProfileName: str
    Path: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateOpenIDConnectProviderRequestTypeDef(TypedDict):
    Url: str
    ClientIDList: NotRequired[Sequence[str]]
    ThumbprintList: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateOpenIDConnectProviderResponseTypeDef(TypedDict):
    OpenIDConnectProviderArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePolicyRequestServiceResourceCreatePolicyTypeDef(TypedDict):
    PolicyName: str
    PolicyDocument: str
    Path: NotRequired[str]
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreatePolicyRequestTypeDef(TypedDict):
    PolicyName: str
    PolicyDocument: str
    Path: NotRequired[str]
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateRoleRequestServiceResourceCreateRoleTypeDef(TypedDict):
    RoleName: str
    AssumeRolePolicyDocument: str
    Path: NotRequired[str]
    Description: NotRequired[str]
    MaxSessionDuration: NotRequired[int]
    PermissionsBoundary: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateRoleRequestTypeDef(TypedDict):
    RoleName: str
    AssumeRolePolicyDocument: str
    Path: NotRequired[str]
    Description: NotRequired[str]
    MaxSessionDuration: NotRequired[int]
    PermissionsBoundary: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateSAMLProviderRequestServiceResourceCreateSamlProviderTypeDef(TypedDict):
    SAMLMetadataDocument: str
    Name: str
    Tags: NotRequired[Sequence[TagTypeDef]]
    AssertionEncryptionMode: NotRequired[AssertionEncryptionModeTypeType]
    AddPrivateKey: NotRequired[str]

class CreateSAMLProviderRequestTypeDef(TypedDict):
    SAMLMetadataDocument: str
    Name: str
    Tags: NotRequired[Sequence[TagTypeDef]]
    AssertionEncryptionMode: NotRequired[AssertionEncryptionModeTypeType]
    AddPrivateKey: NotRequired[str]

class CreateSAMLProviderResponseTypeDef(TypedDict):
    SAMLProviderArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserRequestServiceResourceCreateUserTypeDef(TypedDict):
    UserName: str
    Path: NotRequired[str]
    PermissionsBoundary: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateUserRequestTypeDef(TypedDict):
    UserName: str
    Path: NotRequired[str]
    PermissionsBoundary: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateUserRequestUserCreateTypeDef(TypedDict):
    Path: NotRequired[str]
    PermissionsBoundary: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDeviceTypeDef(TypedDict):
    VirtualMFADeviceName: str
    Path: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateVirtualMFADeviceRequestTypeDef(TypedDict):
    VirtualMFADeviceName: str
    Path: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class GetOpenIDConnectProviderResponseTypeDef(TypedDict):
    Url: str
    ClientIDList: List[str]
    ThumbprintList: List[str]
    CreateDate: datetime
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceProfileTagsResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMFADeviceTagsResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOpenIDConnectProviderTagsResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPolicyTagsResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRoleTagsResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSAMLProviderTagsResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServerCertificateTagsResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListUserTagsResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class PolicyTypeDef(TypedDict):
    PolicyName: NotRequired[str]
    PolicyId: NotRequired[str]
    Arn: NotRequired[str]
    Path: NotRequired[str]
    DefaultVersionId: NotRequired[str]
    AttachmentCount: NotRequired[int]
    PermissionsBoundaryUsageCount: NotRequired[int]
    IsAttachable: NotRequired[bool]
    Description: NotRequired[str]
    CreateDate: NotRequired[datetime]
    UpdateDate: NotRequired[datetime]
    Tags: NotRequired[List[TagTypeDef]]

class TagInstanceProfileRequestTypeDef(TypedDict):
    InstanceProfileName: str
    Tags: Sequence[TagTypeDef]

class TagMFADeviceRequestTypeDef(TypedDict):
    SerialNumber: str
    Tags: Sequence[TagTypeDef]

class TagOpenIDConnectProviderRequestTypeDef(TypedDict):
    OpenIDConnectProviderArn: str
    Tags: Sequence[TagTypeDef]

class TagPolicyRequestTypeDef(TypedDict):
    PolicyArn: str
    Tags: Sequence[TagTypeDef]

class TagRoleRequestTypeDef(TypedDict):
    RoleName: str
    Tags: Sequence[TagTypeDef]

class TagSAMLProviderRequestTypeDef(TypedDict):
    SAMLProviderArn: str
    Tags: Sequence[TagTypeDef]

class TagServerCertificateRequestTypeDef(TypedDict):
    ServerCertificateName: str
    Tags: Sequence[TagTypeDef]

class TagUserRequestTypeDef(TypedDict):
    UserName: str
    Tags: Sequence[TagTypeDef]

class UploadServerCertificateRequestServiceResourceCreateServerCertificateTypeDef(TypedDict):
    ServerCertificateName: str
    CertificateBody: str
    PrivateKey: str
    Path: NotRequired[str]
    CertificateChain: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class UploadServerCertificateRequestTypeDef(TypedDict):
    ServerCertificateName: str
    CertificateBody: str
    PrivateKey: str
    Path: NotRequired[str]
    CertificateChain: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class UserTypeDef(TypedDict):
    Path: str
    UserName: str
    UserId: str
    Arn: str
    CreateDate: datetime
    PasswordLastUsed: NotRequired[datetime]
    PermissionsBoundary: NotRequired[AttachedPermissionsBoundaryTypeDef]
    Tags: NotRequired[List[TagTypeDef]]

class CreateLoginProfileResponseTypeDef(TypedDict):
    LoginProfile: LoginProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLoginProfileResponseTypeDef(TypedDict):
    LoginProfile: LoginProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceSpecificCredentialResponseTypeDef(TypedDict):
    ServiceSpecificCredential: ServiceSpecificCredentialTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResetServiceSpecificCredentialResponseTypeDef(TypedDict):
    ServiceSpecificCredential: ServiceSpecificCredentialTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeletionTaskFailureReasonTypeTypeDef(TypedDict):
    Reason: NotRequired[str]
    RoleUsageList: NotRequired[List[RoleUsageTypeTypeDef]]

class EntityDetailsTypeDef(TypedDict):
    EntityInfo: EntityInfoTypeDef
    LastAuthenticated: NotRequired[datetime]

class GetOrganizationsAccessReportResponseTypeDef(TypedDict):
    JobStatus: JobStatusTypeType
    JobCreationDate: datetime
    JobCompletionDate: datetime
    NumberOfServicesAccessible: int
    NumberOfServicesNotAccessed: int
    AccessDetails: List[AccessDetailTypeDef]
    IsTruncated: bool
    Marker: str
    ErrorDetails: ErrorDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountAuthorizationDetailsRequestPaginateTypeDef(TypedDict):
    Filter: NotRequired[Sequence[EntityTypeType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetGroupRequestPaginateTypeDef(TypedDict):
    GroupName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAccessKeysRequestPaginateTypeDef(TypedDict):
    UserName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAccountAliasesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAttachedGroupPoliciesRequestPaginateTypeDef(TypedDict):
    GroupName: str
    PathPrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAttachedRolePoliciesRequestPaginateTypeDef(TypedDict):
    RoleName: str
    PathPrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAttachedUserPoliciesRequestPaginateTypeDef(TypedDict):
    UserName: str
    PathPrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEntitiesForPolicyRequestPaginateTypeDef(TypedDict):
    PolicyArn: str
    EntityFilter: NotRequired[EntityTypeType]
    PathPrefix: NotRequired[str]
    PolicyUsageFilter: NotRequired[PolicyUsageTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGroupPoliciesRequestPaginateTypeDef(TypedDict):
    GroupName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGroupsForUserRequestPaginateTypeDef(TypedDict):
    UserName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGroupsRequestPaginateTypeDef(TypedDict):
    PathPrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListInstanceProfileTagsRequestPaginateTypeDef(TypedDict):
    InstanceProfileName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListInstanceProfilesForRoleRequestPaginateTypeDef(TypedDict):
    RoleName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListInstanceProfilesRequestPaginateTypeDef(TypedDict):
    PathPrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMFADeviceTagsRequestPaginateTypeDef(TypedDict):
    SerialNumber: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMFADevicesRequestPaginateTypeDef(TypedDict):
    UserName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOpenIDConnectProviderTagsRequestPaginateTypeDef(TypedDict):
    OpenIDConnectProviderArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPoliciesRequestPaginateTypeDef(TypedDict):
    Scope: NotRequired[PolicyScopeTypeType]
    OnlyAttached: NotRequired[bool]
    PathPrefix: NotRequired[str]
    PolicyUsageFilter: NotRequired[PolicyUsageTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPolicyTagsRequestPaginateTypeDef(TypedDict):
    PolicyArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPolicyVersionsRequestPaginateTypeDef(TypedDict):
    PolicyArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRolePoliciesRequestPaginateTypeDef(TypedDict):
    RoleName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRoleTagsRequestPaginateTypeDef(TypedDict):
    RoleName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRolesRequestPaginateTypeDef(TypedDict):
    PathPrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSAMLProviderTagsRequestPaginateTypeDef(TypedDict):
    SAMLProviderArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSSHPublicKeysRequestPaginateTypeDef(TypedDict):
    UserName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServerCertificateTagsRequestPaginateTypeDef(TypedDict):
    ServerCertificateName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServerCertificatesRequestPaginateTypeDef(TypedDict):
    PathPrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSigningCertificatesRequestPaginateTypeDef(TypedDict):
    UserName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUserPoliciesRequestPaginateTypeDef(TypedDict):
    UserName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUserTagsRequestPaginateTypeDef(TypedDict):
    UserName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUsersRequestPaginateTypeDef(TypedDict):
    PathPrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListVirtualMFADevicesRequestPaginateTypeDef(TypedDict):
    AssignmentStatus: NotRequired[AssignmentStatusTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SimulateCustomPolicyRequestPaginateTypeDef(TypedDict):
    PolicyInputList: Sequence[str]
    ActionNames: Sequence[str]
    PermissionsBoundaryPolicyInputList: NotRequired[Sequence[str]]
    ResourceArns: NotRequired[Sequence[str]]
    ResourcePolicy: NotRequired[str]
    ResourceOwner: NotRequired[str]
    CallerArn: NotRequired[str]
    ContextEntries: NotRequired[Sequence[ContextEntryTypeDef]]
    ResourceHandlingOption: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SimulatePrincipalPolicyRequestPaginateTypeDef(TypedDict):
    PolicySourceArn: str
    ActionNames: Sequence[str]
    PolicyInputList: NotRequired[Sequence[str]]
    PermissionsBoundaryPolicyInputList: NotRequired[Sequence[str]]
    ResourceArns: NotRequired[Sequence[str]]
    ResourcePolicy: NotRequired[str]
    ResourceOwner: NotRequired[str]
    CallerArn: NotRequired[str]
    ContextEntries: NotRequired[Sequence[ContextEntryTypeDef]]
    ResourceHandlingOption: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetAccountPasswordPolicyResponseTypeDef(TypedDict):
    PasswordPolicy: PasswordPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceProfileRequestWaitTypeDef(TypedDict):
    InstanceProfileName: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetPolicyRequestWaitTypeDef(TypedDict):
    PolicyArn: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetRoleRequestWaitTypeDef(TypedDict):
    RoleName: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetUserRequestWaitTypeDef(TypedDict):
    UserName: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetSAMLProviderResponseTypeDef(TypedDict):
    SAMLProviderUUID: str
    SAMLMetadataDocument: str
    CreateDate: datetime
    ValidUntil: datetime
    Tags: List[TagTypeDef]
    AssertionEncryptionMode: AssertionEncryptionModeTypeType
    PrivateKeyList: List[SAMLPrivateKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSSHPublicKeyResponseTypeDef(TypedDict):
    SSHPublicKey: SSHPublicKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UploadSSHPublicKeyResponseTypeDef(TypedDict):
    SSHPublicKey: SSHPublicKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEntitiesForPolicyResponseTypeDef(TypedDict):
    PolicyGroups: List[PolicyGroupTypeDef]
    PolicyUsers: List[PolicyUserTypeDef]
    PolicyRoles: List[PolicyRoleTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMFADevicesResponseTypeDef(TypedDict):
    MFADevices: List[MFADeviceTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOpenIDConnectProvidersResponseTypeDef(TypedDict):
    OpenIDConnectProviderList: List[OpenIDConnectProviderListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPoliciesGrantingServiceAccessEntryTypeDef(TypedDict):
    ServiceNamespace: NotRequired[str]
    Policies: NotRequired[List[PolicyGrantingServiceAccessTypeDef]]

class ListSAMLProvidersResponseTypeDef(TypedDict):
    SAMLProviderList: List[SAMLProviderListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSSHPublicKeysResponseTypeDef(TypedDict):
    SSHPublicKeys: List[SSHPublicKeyMetadataTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServerCertificatesResponseTypeDef(TypedDict):
    ServerCertificateMetadataList: List[ServerCertificateMetadataTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ServerCertificateTypeDef(TypedDict):
    ServerCertificateMetadata: ServerCertificateMetadataTypeDef
    CertificateBody: str
    CertificateChain: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]

class UploadServerCertificateResponseTypeDef(TypedDict):
    ServerCertificateMetadata: ServerCertificateMetadataTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceSpecificCredentialsResponseTypeDef(TypedDict):
    ServiceSpecificCredentials: List[ServiceSpecificCredentialMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSigningCertificatesResponseTypeDef(TypedDict):
    Certificates: List[SigningCertificateTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class UploadSigningCertificateResponseTypeDef(TypedDict):
    Certificate: SigningCertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PolicyDocumentDictTypeDef(TypedDict):
    Version: str
    Statement: List[PolicyDocumentStatementTypeDef]

class StatementTypeDef(TypedDict):
    SourcePolicyId: NotRequired[str]
    SourcePolicyType: NotRequired[PolicySourceTypeType]
    StartPosition: NotRequired[PositionTypeDef]
    EndPosition: NotRequired[PositionTypeDef]

ServiceLastAccessedTypeDef = TypedDict(
    "ServiceLastAccessedTypeDef",
    {
        "ServiceName": str,
        "ServiceNamespace": str,
        "LastAuthenticated": NotRequired[datetime],
        "LastAuthenticatedEntity": NotRequired[str],
        "LastAuthenticatedRegion": NotRequired[str],
        "TotalAuthenticatedEntities": NotRequired[int],
        "TrackedActionsLastAccessed": NotRequired[List[TrackedActionLastAccessedTypeDef]],
    },
)

class CreatePolicyResponseTypeDef(TypedDict):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPolicyResponseTypeDef(TypedDict):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPoliciesResponseTypeDef(TypedDict):
    Policies: List[PolicyTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserResponseTypeDef(TypedDict):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupResponseTypeDef(TypedDict):
    Group: GroupTypeDef
    Users: List[UserTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserResponseTypeDef(TypedDict):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListUsersResponseTypeDef(TypedDict):
    Users: List[UserTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class VirtualMFADeviceTypeDef(TypedDict):
    SerialNumber: str
    Base32StringSeed: NotRequired[bytes]
    QRCodePNG: NotRequired[bytes]
    User: NotRequired[UserTypeDef]
    EnableDate: NotRequired[datetime]
    Tags: NotRequired[List[TagTypeDef]]

class GetServiceLinkedRoleDeletionStatusResponseTypeDef(TypedDict):
    Status: DeletionTaskStatusTypeType
    Reason: DeletionTaskFailureReasonTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef(TypedDict):
    JobStatus: JobStatusTypeType
    JobCreationDate: datetime
    JobCompletionDate: datetime
    EntityDetailsList: List[EntityDetailsTypeDef]
    IsTruncated: bool
    Marker: str
    Error: ErrorDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPoliciesGrantingServiceAccessResponseTypeDef(TypedDict):
    PoliciesGrantingServiceAccess: List[ListPoliciesGrantingServiceAccessEntryTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetServerCertificateResponseTypeDef(TypedDict):
    ServerCertificate: ServerCertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

PolicyDocumentTypeDef = Union[str, PolicyDocumentDictTypeDef]

class ResourceSpecificResultTypeDef(TypedDict):
    EvalResourceName: str
    EvalResourceDecision: PolicyEvaluationDecisionTypeType
    MatchedStatements: NotRequired[List[StatementTypeDef]]
    MissingContextValues: NotRequired[List[str]]
    EvalDecisionDetails: NotRequired[Dict[str, PolicyEvaluationDecisionTypeType]]
    PermissionsBoundaryDecisionDetail: NotRequired[PermissionsBoundaryDecisionDetailTypeDef]

class GetServiceLastAccessedDetailsResponseTypeDef(TypedDict):
    JobStatus: JobStatusTypeType
    JobType: AccessAdvisorUsageGranularityTypeType
    JobCreationDate: datetime
    ServicesLastAccessed: List[ServiceLastAccessedTypeDef]
    JobCompletionDate: datetime
    IsTruncated: bool
    Marker: str
    Error: ErrorDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVirtualMFADeviceResponseTypeDef(TypedDict):
    VirtualMFADevice: VirtualMFADeviceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVirtualMFADevicesResponseTypeDef(TypedDict):
    VirtualMFADevices: List[VirtualMFADeviceTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupPolicyResponseTypeDef(TypedDict):
    GroupName: str
    PolicyName: str
    PolicyDocument: PolicyDocumentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRolePolicyResponseTypeDef(TypedDict):
    RoleName: str
    PolicyName: str
    PolicyDocument: PolicyDocumentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserPolicyResponseTypeDef(TypedDict):
    UserName: str
    PolicyName: str
    PolicyDocument: PolicyDocumentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PolicyDetailTypeDef(TypedDict):
    PolicyName: NotRequired[str]
    PolicyDocument: NotRequired[PolicyDocumentTypeDef]

class PolicyVersionTypeDef(TypedDict):
    Document: NotRequired[PolicyDocumentTypeDef]
    VersionId: NotRequired[str]
    IsDefaultVersion: NotRequired[bool]
    CreateDate: NotRequired[datetime]

class RoleTypeDef(TypedDict):
    Path: str
    RoleName: str
    RoleId: str
    Arn: str
    CreateDate: datetime
    AssumeRolePolicyDocument: NotRequired[PolicyDocumentTypeDef]
    Description: NotRequired[str]
    MaxSessionDuration: NotRequired[int]
    PermissionsBoundary: NotRequired[AttachedPermissionsBoundaryTypeDef]
    Tags: NotRequired[List[TagTypeDef]]
    RoleLastUsed: NotRequired[RoleLastUsedTypeDef]

class EvaluationResultTypeDef(TypedDict):
    EvalActionName: str
    EvalDecision: PolicyEvaluationDecisionTypeType
    EvalResourceName: NotRequired[str]
    MatchedStatements: NotRequired[List[StatementTypeDef]]
    MissingContextValues: NotRequired[List[str]]
    OrganizationsDecisionDetail: NotRequired[OrganizationsDecisionDetailTypeDef]
    PermissionsBoundaryDecisionDetail: NotRequired[PermissionsBoundaryDecisionDetailTypeDef]
    EvalDecisionDetails: NotRequired[Dict[str, PolicyEvaluationDecisionTypeType]]
    ResourceSpecificResults: NotRequired[List[ResourceSpecificResultTypeDef]]

class GroupDetailTypeDef(TypedDict):
    Path: NotRequired[str]
    GroupName: NotRequired[str]
    GroupId: NotRequired[str]
    Arn: NotRequired[str]
    CreateDate: NotRequired[datetime]
    GroupPolicyList: NotRequired[List[PolicyDetailTypeDef]]
    AttachedManagedPolicies: NotRequired[List[AttachedPolicyTypeDef]]

class UserDetailTypeDef(TypedDict):
    Path: NotRequired[str]
    UserName: NotRequired[str]
    UserId: NotRequired[str]
    Arn: NotRequired[str]
    CreateDate: NotRequired[datetime]
    UserPolicyList: NotRequired[List[PolicyDetailTypeDef]]
    GroupList: NotRequired[List[str]]
    AttachedManagedPolicies: NotRequired[List[AttachedPolicyTypeDef]]
    PermissionsBoundary: NotRequired[AttachedPermissionsBoundaryTypeDef]
    Tags: NotRequired[List[TagTypeDef]]

class CreatePolicyVersionResponseTypeDef(TypedDict):
    PolicyVersion: PolicyVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPolicyVersionResponseTypeDef(TypedDict):
    PolicyVersion: PolicyVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPolicyVersionsResponseTypeDef(TypedDict):
    Versions: List[PolicyVersionTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ManagedPolicyDetailTypeDef(TypedDict):
    PolicyName: NotRequired[str]
    PolicyId: NotRequired[str]
    Arn: NotRequired[str]
    Path: NotRequired[str]
    DefaultVersionId: NotRequired[str]
    AttachmentCount: NotRequired[int]
    PermissionsBoundaryUsageCount: NotRequired[int]
    IsAttachable: NotRequired[bool]
    Description: NotRequired[str]
    CreateDate: NotRequired[datetime]
    UpdateDate: NotRequired[datetime]
    PolicyVersionList: NotRequired[List[PolicyVersionTypeDef]]

class CreateRoleResponseTypeDef(TypedDict):
    Role: RoleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceLinkedRoleResponseTypeDef(TypedDict):
    Role: RoleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRoleResponseTypeDef(TypedDict):
    Role: RoleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceProfileTypeDef(TypedDict):
    Path: str
    InstanceProfileName: str
    InstanceProfileId: str
    Arn: str
    CreateDate: datetime
    Roles: List[RoleTypeDef]
    Tags: NotRequired[List[TagTypeDef]]

class ListRolesResponseTypeDef(TypedDict):
    Roles: List[RoleTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRoleDescriptionResponseTypeDef(TypedDict):
    Role: RoleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SimulatePolicyResponseTypeDef(TypedDict):
    EvaluationResults: List[EvaluationResultTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceProfileResponseTypeDef(TypedDict):
    InstanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceProfileResponseTypeDef(TypedDict):
    InstanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceProfilesForRoleResponseTypeDef(TypedDict):
    InstanceProfiles: List[InstanceProfileTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceProfilesResponseTypeDef(TypedDict):
    InstanceProfiles: List[InstanceProfileTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class RoleDetailTypeDef(TypedDict):
    Path: NotRequired[str]
    RoleName: NotRequired[str]
    RoleId: NotRequired[str]
    Arn: NotRequired[str]
    CreateDate: NotRequired[datetime]
    AssumeRolePolicyDocument: NotRequired[PolicyDocumentTypeDef]
    InstanceProfileList: NotRequired[List[InstanceProfileTypeDef]]
    RolePolicyList: NotRequired[List[PolicyDetailTypeDef]]
    AttachedManagedPolicies: NotRequired[List[AttachedPolicyTypeDef]]
    PermissionsBoundary: NotRequired[AttachedPermissionsBoundaryTypeDef]
    Tags: NotRequired[List[TagTypeDef]]
    RoleLastUsed: NotRequired[RoleLastUsedTypeDef]

class GetAccountAuthorizationDetailsResponseTypeDef(TypedDict):
    UserDetailList: List[UserDetailTypeDef]
    GroupDetailList: List[GroupDetailTypeDef]
    RoleDetailList: List[RoleDetailTypeDef]
    Policies: List[ManagedPolicyDetailTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef
