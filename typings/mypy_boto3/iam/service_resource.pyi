"""
Type annotations for iam service ServiceResource.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_iam.service_resource import IAMServiceResource
    import mypy_boto3_iam.service_resource as iam_resources

    session = Session()
    resource: IAMServiceResource = session.resource("iam")

    my_access_key: iam_resources.AccessKey = resource.AccessKey(...)
    my_access_key_pair: iam_resources.AccessKeyPair = resource.AccessKeyPair(...)
    my_account_password_policy: iam_resources.AccountPasswordPolicy = resource.AccountPasswordPolicy(...)
    my_account_summary: iam_resources.AccountSummary = resource.AccountSummary(...)
    my_assume_role_policy: iam_resources.AssumeRolePolicy = resource.AssumeRolePolicy(...)
    my_current_user: iam_resources.CurrentUser = resource.CurrentUser(...)
    my_group: iam_resources.Group = resource.Group(...)
    my_group_policy: iam_resources.GroupPolicy = resource.GroupPolicy(...)
    my_instance_profile: iam_resources.InstanceProfile = resource.InstanceProfile(...)
    my_login_profile: iam_resources.LoginProfile = resource.LoginProfile(...)
    my_mfa_device: iam_resources.MfaDevice = resource.MfaDevice(...)
    my_policy: iam_resources.Policy = resource.Policy(...)
    my_policy_version: iam_resources.PolicyVersion = resource.PolicyVersion(...)
    my_role: iam_resources.Role = resource.Role(...)
    my_role_policy: iam_resources.RolePolicy = resource.RolePolicy(...)
    my_saml_provider: iam_resources.SamlProvider = resource.SamlProvider(...)
    my_server_certificate: iam_resources.ServerCertificate = resource.ServerCertificate(...)
    my_signing_certificate: iam_resources.SigningCertificate = resource.SigningCertificate(...)
    my_user: iam_resources.User = resource.User(...)
    my_user_policy: iam_resources.UserPolicy = resource.UserPolicy(...)
    my_virtual_mfa_device: iam_resources.VirtualMfaDevice = resource.VirtualMfaDevice(...)
```
"""

from __future__ import annotations

import sys
from datetime import datetime

from boto3.resources.base import ResourceMeta, ServiceResource
from boto3.resources.collection import ResourceCollection

from .client import IAMClient
from .literals import (
    AssertionEncryptionModeTypeType,
    AssignmentStatusTypeType,
    EntityTypeType,
    PolicyScopeTypeType,
    PolicyUsageTypeType,
    StatusTypeType,
    SummaryKeyTypeType,
)
from .type_defs import (
    AddRoleToInstanceProfileRequestInstanceProfileAddRoleTypeDef,
    AddUserToGroupRequestGroupAddUserTypeDef,
    AddUserToGroupRequestUserAddGroupTypeDef,
    AttachedPermissionsBoundaryTypeDef,
    AttachGroupPolicyRequestGroupAttachPolicyTypeDef,
    AttachGroupPolicyRequestPolicyAttachGroupTypeDef,
    AttachRolePolicyRequestPolicyAttachRoleTypeDef,
    AttachRolePolicyRequestRoleAttachPolicyTypeDef,
    AttachUserPolicyRequestPolicyAttachUserTypeDef,
    AttachUserPolicyRequestUserAttachPolicyTypeDef,
    ChangePasswordRequestServiceResourceChangePasswordTypeDef,
    CreateAccountAliasRequestServiceResourceCreateAccountAliasTypeDef,
    CreateGroupRequestGroupCreateTypeDef,
    CreateGroupRequestServiceResourceCreateGroupTypeDef,
    CreateInstanceProfileRequestServiceResourceCreateInstanceProfileTypeDef,
    CreateLoginProfileRequestLoginProfileCreateTypeDef,
    CreateLoginProfileRequestUserCreateLoginProfileTypeDef,
    CreatePolicyRequestServiceResourceCreatePolicyTypeDef,
    CreatePolicyVersionRequestPolicyCreateVersionTypeDef,
    CreateRoleRequestServiceResourceCreateRoleTypeDef,
    CreateSAMLProviderRequestServiceResourceCreateSamlProviderTypeDef,
    CreateUserRequestServiceResourceCreateUserTypeDef,
    CreateUserRequestUserCreateTypeDef,
    CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDeviceTypeDef,
    DetachGroupPolicyRequestGroupDetachPolicyTypeDef,
    DetachGroupPolicyRequestPolicyDetachGroupTypeDef,
    DetachRolePolicyRequestPolicyDetachRoleTypeDef,
    DetachRolePolicyRequestRoleDetachPolicyTypeDef,
    DetachUserPolicyRequestPolicyDetachUserTypeDef,
    DetachUserPolicyRequestUserDetachPolicyTypeDef,
    EnableMFADeviceRequestMfaDeviceAssociateTypeDef,
    EnableMFADeviceRequestUserEnableMfaTypeDef,
    PolicyDocumentTypeDef,
    PutGroupPolicyRequestGroupCreatePolicyTypeDef,
    PutGroupPolicyRequestGroupPolicyPutTypeDef,
    PutRolePolicyRequestRolePolicyPutTypeDef,
    PutUserPolicyRequestUserCreatePolicyTypeDef,
    PutUserPolicyRequestUserPolicyPutTypeDef,
    RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRoleTypeDef,
    RemoveUserFromGroupRequestGroupRemoveUserTypeDef,
    RemoveUserFromGroupRequestUserRemoveGroupTypeDef,
    ResyncMFADeviceRequestMfaDeviceResyncTypeDef,
    RoleLastUsedTypeDef,
    RoleTypeDef,
    SAMLPrivateKeyTypeDef,
    ServerCertificateMetadataTypeDef,
    TagTypeDef,
    UpdateAccessKeyRequestAccessKeyActivateTypeDef,
    UpdateAccessKeyRequestAccessKeyDeactivateTypeDef,
    UpdateAccessKeyRequestAccessKeyPairActivateTypeDef,
    UpdateAccessKeyRequestAccessKeyPairDeactivateTypeDef,
    UpdateAccountPasswordPolicyRequestAccountPasswordPolicyUpdateTypeDef,
    UpdateAccountPasswordPolicyRequestServiceResourceCreateAccountPasswordPolicyTypeDef,
    UpdateAssumeRolePolicyRequestAssumeRolePolicyUpdateTypeDef,
    UpdateGroupRequestGroupUpdateTypeDef,
    UpdateLoginProfileRequestLoginProfileUpdateTypeDef,
    UpdateSAMLProviderRequestSamlProviderUpdateTypeDef,
    UpdateSAMLProviderResponseTypeDef,
    UpdateServerCertificateRequestServerCertificateUpdateTypeDef,
    UpdateSigningCertificateRequestSigningCertificateActivateTypeDef,
    UpdateSigningCertificateRequestSigningCertificateDeactivateTypeDef,
    UpdateUserRequestUserUpdateTypeDef,
    UploadServerCertificateRequestServiceResourceCreateServerCertificateTypeDef,
    UploadSigningCertificateRequestServiceResourceCreateSigningCertificateTypeDef,
    UserTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Iterator, Sequence
else:
    from typing import Dict, Iterator, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "AccessKey",
    "AccessKeyPair",
    "AccountPasswordPolicy",
    "AccountSummary",
    "AssumeRolePolicy",
    "CurrentUser",
    "CurrentUserAccessKeysCollection",
    "CurrentUserMfaDevicesCollection",
    "CurrentUserSigningCertificatesCollection",
    "Group",
    "GroupAttachedPoliciesCollection",
    "GroupPoliciesCollection",
    "GroupPolicy",
    "GroupUsersCollection",
    "IAMServiceResource",
    "InstanceProfile",
    "LoginProfile",
    "MfaDevice",
    "Policy",
    "PolicyAttachedGroupsCollection",
    "PolicyAttachedRolesCollection",
    "PolicyAttachedUsersCollection",
    "PolicyVersion",
    "PolicyVersionsCollection",
    "Role",
    "RoleAttachedPoliciesCollection",
    "RoleInstanceProfilesCollection",
    "RolePoliciesCollection",
    "RolePolicy",
    "SamlProvider",
    "ServerCertificate",
    "ServiceResourceGroupsCollection",
    "ServiceResourceInstanceProfilesCollection",
    "ServiceResourcePoliciesCollection",
    "ServiceResourceRolesCollection",
    "ServiceResourceSamlProvidersCollection",
    "ServiceResourceServerCertificatesCollection",
    "ServiceResourceUsersCollection",
    "ServiceResourceVirtualMfaDevicesCollection",
    "SigningCertificate",
    "User",
    "UserAccessKeysCollection",
    "UserAttachedPoliciesCollection",
    "UserGroupsCollection",
    "UserMfaDevicesCollection",
    "UserPoliciesCollection",
    "UserPolicy",
    "UserSigningCertificatesCollection",
    "VirtualMfaDevice",
)

class ServiceResourceGroupsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/groups.html#IAM.ServiceResource.groups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcegroupscollection)
    """
    def all(self) -> ServiceResourceGroupsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/groups.html#IAM.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcegroupscollection)
        """

    def filter(  # type: ignore[override]
        self, *, PathPrefix: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> ServiceResourceGroupsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/groups.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcegroupscollection)
        """

    def limit(self, count: int) -> ServiceResourceGroupsCollection:
        """
        Return at most this many Groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/groups.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcegroupscollection)
        """

    def page_size(self, count: int) -> ServiceResourceGroupsCollection:
        """
        Fetch at most this many Groups per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/groups.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcegroupscollection)
        """

    def pages(self) -> Iterator[List[Group]]:
        """
        A generator which yields pages of Groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/groups.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcegroupscollection)
        """

    def __iter__(self) -> Iterator[Group]:
        """
        A generator which yields Groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/groups.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcegroupscollection)
        """

class ServiceResourceInstanceProfilesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/instance_profiles.html#IAM.ServiceResource.instance_profiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceinstanceprofilescollection)
    """
    def all(self) -> ServiceResourceInstanceProfilesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/instance_profiles.html#IAM.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceinstanceprofilescollection)
        """

    def filter(  # type: ignore[override]
        self, *, PathPrefix: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> ServiceResourceInstanceProfilesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/instance_profiles.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceinstanceprofilescollection)
        """

    def limit(self, count: int) -> ServiceResourceInstanceProfilesCollection:
        """
        Return at most this many InstanceProfiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/instance_profiles.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceinstanceprofilescollection)
        """

    def page_size(self, count: int) -> ServiceResourceInstanceProfilesCollection:
        """
        Fetch at most this many InstanceProfiles per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/instance_profiles.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceinstanceprofilescollection)
        """

    def pages(self) -> Iterator[List[InstanceProfile]]:
        """
        A generator which yields pages of InstanceProfiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/instance_profiles.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceinstanceprofilescollection)
        """

    def __iter__(self) -> Iterator[InstanceProfile]:
        """
        A generator which yields InstanceProfiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/instance_profiles.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceinstanceprofilescollection)
        """

class ServiceResourcePoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/policies.html#IAM.ServiceResource.policies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcepoliciescollection)
    """
    def all(self) -> ServiceResourcePoliciesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/policies.html#IAM.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcepoliciescollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        Scope: PolicyScopeTypeType = ...,
        OnlyAttached: bool = ...,
        PathPrefix: str = ...,
        PolicyUsageFilter: PolicyUsageTypeType = ...,
        Marker: str = ...,
        MaxItems: int = ...,
    ) -> ServiceResourcePoliciesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/policies.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcepoliciescollection)
        """

    def limit(self, count: int) -> ServiceResourcePoliciesCollection:
        """
        Return at most this many Policys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/policies.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcepoliciescollection)
        """

    def page_size(self, count: int) -> ServiceResourcePoliciesCollection:
        """
        Fetch at most this many Policys per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/policies.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcepoliciescollection)
        """

    def pages(self) -> Iterator[List[Policy]]:
        """
        A generator which yields pages of Policys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/policies.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcepoliciescollection)
        """

    def __iter__(self) -> Iterator[Policy]:
        """
        A generator which yields Policys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/policies.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcepoliciescollection)
        """

class ServiceResourceRolesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/roles.html#IAM.ServiceResource.roles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcerolescollection)
    """
    def all(self) -> ServiceResourceRolesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/roles.html#IAM.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcerolescollection)
        """

    def filter(  # type: ignore[override]
        self, *, PathPrefix: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> ServiceResourceRolesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/roles.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcerolescollection)
        """

    def limit(self, count: int) -> ServiceResourceRolesCollection:
        """
        Return at most this many Roles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/roles.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcerolescollection)
        """

    def page_size(self, count: int) -> ServiceResourceRolesCollection:
        """
        Fetch at most this many Roles per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/roles.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcerolescollection)
        """

    def pages(self) -> Iterator[List[Role]]:
        """
        A generator which yields pages of Roles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/roles.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcerolescollection)
        """

    def __iter__(self) -> Iterator[Role]:
        """
        A generator which yields Roles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/roles.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcerolescollection)
        """

class ServiceResourceSamlProvidersCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/saml_providers.html#IAM.ServiceResource.saml_providers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcesamlproviderscollection)
    """
    def all(self) -> ServiceResourceSamlProvidersCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/saml_providers.html#IAM.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcesamlproviderscollection)
        """

    def filter(  # type: ignore[override]
        self,
    ) -> ServiceResourceSamlProvidersCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/saml_providers.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcesamlproviderscollection)
        """

    def limit(self, count: int) -> ServiceResourceSamlProvidersCollection:
        """
        Return at most this many SamlProviders.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/saml_providers.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcesamlproviderscollection)
        """

    def page_size(self, count: int) -> ServiceResourceSamlProvidersCollection:
        """
        Fetch at most this many SamlProviders per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/saml_providers.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcesamlproviderscollection)
        """

    def pages(self) -> Iterator[List[SamlProvider]]:
        """
        A generator which yields pages of SamlProviders.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/saml_providers.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcesamlproviderscollection)
        """

    def __iter__(self) -> Iterator[SamlProvider]:
        """
        A generator which yields SamlProviders.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/saml_providers.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcesamlproviderscollection)
        """

class ServiceResourceServerCertificatesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/server_certificates.html#IAM.ServiceResource.server_certificates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceservercertificatescollection)
    """
    def all(self) -> ServiceResourceServerCertificatesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/server_certificates.html#IAM.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceservercertificatescollection)
        """

    def filter(  # type: ignore[override]
        self, *, PathPrefix: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> ServiceResourceServerCertificatesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/server_certificates.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceservercertificatescollection)
        """

    def limit(self, count: int) -> ServiceResourceServerCertificatesCollection:
        """
        Return at most this many ServerCertificates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/server_certificates.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceservercertificatescollection)
        """

    def page_size(self, count: int) -> ServiceResourceServerCertificatesCollection:
        """
        Fetch at most this many ServerCertificates per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/server_certificates.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceservercertificatescollection)
        """

    def pages(self) -> Iterator[List[ServerCertificate]]:
        """
        A generator which yields pages of ServerCertificates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/server_certificates.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceservercertificatescollection)
        """

    def __iter__(self) -> Iterator[ServerCertificate]:
        """
        A generator which yields ServerCertificates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/server_certificates.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceservercertificatescollection)
        """

class ServiceResourceUsersCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/users.html#IAM.ServiceResource.users)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceuserscollection)
    """
    def all(self) -> ServiceResourceUsersCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/users.html#IAM.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceuserscollection)
        """

    def filter(  # type: ignore[override]
        self, *, PathPrefix: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> ServiceResourceUsersCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/users.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceuserscollection)
        """

    def limit(self, count: int) -> ServiceResourceUsersCollection:
        """
        Return at most this many Users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/users.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceuserscollection)
        """

    def page_size(self, count: int) -> ServiceResourceUsersCollection:
        """
        Fetch at most this many Users per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/users.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceuserscollection)
        """

    def pages(self) -> Iterator[List[User]]:
        """
        A generator which yields pages of Users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/users.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceuserscollection)
        """

    def __iter__(self) -> Iterator[User]:
        """
        A generator which yields Users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/users.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceuserscollection)
        """

class ServiceResourceVirtualMfaDevicesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/virtual_mfa_devices.html#IAM.ServiceResource.virtual_mfa_devices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcevirtualmfadevicescollection)
    """
    def all(self) -> ServiceResourceVirtualMfaDevicesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/virtual_mfa_devices.html#IAM.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcevirtualmfadevicescollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        AssignmentStatus: AssignmentStatusTypeType = ...,
        Marker: str = ...,
        MaxItems: int = ...,
    ) -> ServiceResourceVirtualMfaDevicesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/virtual_mfa_devices.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcevirtualmfadevicescollection)
        """

    def limit(self, count: int) -> ServiceResourceVirtualMfaDevicesCollection:
        """
        Return at most this many VirtualMfaDevices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/virtual_mfa_devices.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcevirtualmfadevicescollection)
        """

    def page_size(self, count: int) -> ServiceResourceVirtualMfaDevicesCollection:
        """
        Fetch at most this many VirtualMfaDevices per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/virtual_mfa_devices.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcevirtualmfadevicescollection)
        """

    def pages(self) -> Iterator[List[VirtualMfaDevice]]:
        """
        A generator which yields pages of VirtualMfaDevices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/virtual_mfa_devices.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcevirtualmfadevicescollection)
        """

    def __iter__(self) -> Iterator[VirtualMfaDevice]:
        """
        A generator which yields VirtualMfaDevices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/virtual_mfa_devices.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcevirtualmfadevicescollection)
        """

class CurrentUserAccessKeysCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/access_keys.html#IAM.CurrentUser.access_keys)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentuseraccess_keys)
    """
    def all(self) -> CurrentUserAccessKeysCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/access_keys.html#IAM.CurrentUser.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentuseraccess_keys)
        """

    def filter(  # type: ignore[override]
        self, *, UserName: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> CurrentUserAccessKeysCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/access_keys.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentuseraccess_keys)
        """

    def limit(self, count: int) -> CurrentUserAccessKeysCollection:
        """
        Return at most this many AccessKeys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/access_keys.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentuseraccess_keys)
        """

    def page_size(self, count: int) -> CurrentUserAccessKeysCollection:
        """
        Fetch at most this many AccessKeys per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/access_keys.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentuseraccess_keys)
        """

    def pages(self) -> Iterator[List[AccessKey]]:
        """
        A generator which yields pages of AccessKeys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/access_keys.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentuseraccess_keys)
        """

    def __iter__(self) -> Iterator[AccessKey]:
        """
        A generator which yields AccessKeys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/access_keys.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentuseraccess_keys)
        """

class CurrentUserMfaDevicesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/mfa_devices.html#IAM.CurrentUser.mfa_devices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentusermfa_devices)
    """
    def all(self) -> CurrentUserMfaDevicesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/mfa_devices.html#IAM.CurrentUser.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentusermfa_devices)
        """

    def filter(  # type: ignore[override]
        self, *, UserName: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> CurrentUserMfaDevicesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/mfa_devices.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentusermfa_devices)
        """

    def limit(self, count: int) -> CurrentUserMfaDevicesCollection:
        """
        Return at most this many MfaDevices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/mfa_devices.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentusermfa_devices)
        """

    def page_size(self, count: int) -> CurrentUserMfaDevicesCollection:
        """
        Fetch at most this many MfaDevices per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/mfa_devices.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentusermfa_devices)
        """

    def pages(self) -> Iterator[List[MfaDevice]]:
        """
        A generator which yields pages of MfaDevices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/mfa_devices.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentusermfa_devices)
        """

    def __iter__(self) -> Iterator[MfaDevice]:
        """
        A generator which yields MfaDevices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/mfa_devices.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentusermfa_devices)
        """

class CurrentUserSigningCertificatesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/signing_certificates.html#IAM.CurrentUser.signing_certificates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentusersigning_certificates)
    """
    def all(self) -> CurrentUserSigningCertificatesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/signing_certificates.html#IAM.CurrentUser.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentusersigning_certificates)
        """

    def filter(  # type: ignore[override]
        self, *, UserName: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> CurrentUserSigningCertificatesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/signing_certificates.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentusersigning_certificates)
        """

    def limit(self, count: int) -> CurrentUserSigningCertificatesCollection:
        """
        Return at most this many SigningCertificates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/signing_certificates.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentusersigning_certificates)
        """

    def page_size(self, count: int) -> CurrentUserSigningCertificatesCollection:
        """
        Fetch at most this many SigningCertificates per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/signing_certificates.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentusersigning_certificates)
        """

    def pages(self) -> Iterator[List[SigningCertificate]]:
        """
        A generator which yields pages of SigningCertificates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/signing_certificates.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentusersigning_certificates)
        """

    def __iter__(self) -> Iterator[SigningCertificate]:
        """
        A generator which yields SigningCertificates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/signing_certificates.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentusersigning_certificates)
        """

class GroupAttachedPoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/attached_policies.html#IAM.Group.attached_policies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupattached_policies)
    """
    def all(self) -> GroupAttachedPoliciesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/attached_policies.html#IAM.Group.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupattached_policies)
        """

    def filter(  # type: ignore[override]
        self, *, PathPrefix: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> GroupAttachedPoliciesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/attached_policies.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupattached_policies)
        """

    def limit(self, count: int) -> GroupAttachedPoliciesCollection:
        """
        Return at most this many Policys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/attached_policies.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupattached_policies)
        """

    def page_size(self, count: int) -> GroupAttachedPoliciesCollection:
        """
        Fetch at most this many Policys per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/attached_policies.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupattached_policies)
        """

    def pages(self) -> Iterator[List[Policy]]:
        """
        A generator which yields pages of Policys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/attached_policies.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupattached_policies)
        """

    def __iter__(self) -> Iterator[Policy]:
        """
        A generator which yields Policys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/attached_policies.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupattached_policies)
        """

class GroupPoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/policies.html#IAM.Group.policies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicies)
    """
    def all(self) -> GroupPoliciesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/policies.html#IAM.Group.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicies)
        """

    def filter(  # type: ignore[override]
        self, *, Marker: str = ..., MaxItems: int = ...
    ) -> GroupPoliciesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/policies.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicies)
        """

    def limit(self, count: int) -> GroupPoliciesCollection:
        """
        Return at most this many GroupPolicys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/policies.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicies)
        """

    def page_size(self, count: int) -> GroupPoliciesCollection:
        """
        Fetch at most this many GroupPolicys per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/policies.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicies)
        """

    def pages(self) -> Iterator[List[GroupPolicy]]:
        """
        A generator which yields pages of GroupPolicys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/policies.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicies)
        """

    def __iter__(self) -> Iterator[GroupPolicy]:
        """
        A generator which yields GroupPolicys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/policies.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicies)
        """

class GroupUsersCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/users.html#IAM.Group.users)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupusers)
    """
    def all(self) -> GroupUsersCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/users.html#IAM.Group.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupusers)
        """

    def filter(  # type: ignore[override]
        self, *, Marker: str = ..., MaxItems: int = ...
    ) -> GroupUsersCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/users.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupusers)
        """

    def limit(self, count: int) -> GroupUsersCollection:
        """
        Return at most this many Users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/users.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupusers)
        """

    def page_size(self, count: int) -> GroupUsersCollection:
        """
        Fetch at most this many Users per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/users.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupusers)
        """

    def pages(self) -> Iterator[List[User]]:
        """
        A generator which yields pages of Users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/users.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupusers)
        """

    def __iter__(self) -> Iterator[User]:
        """
        A generator which yields Users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/users.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupusers)
        """

class PolicyAttachedGroupsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_groups.html#IAM.Policy.attached_groups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_groups)
    """
    def all(self) -> PolicyAttachedGroupsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_groups.html#IAM.Policy.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_groups)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        EntityFilter: EntityTypeType = ...,
        PathPrefix: str = ...,
        PolicyUsageFilter: PolicyUsageTypeType = ...,
        Marker: str = ...,
        MaxItems: int = ...,
    ) -> PolicyAttachedGroupsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_groups.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_groups)
        """

    def limit(self, count: int) -> PolicyAttachedGroupsCollection:
        """
        Return at most this many Groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_groups.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_groups)
        """

    def page_size(self, count: int) -> PolicyAttachedGroupsCollection:
        """
        Fetch at most this many Groups per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_groups.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_groups)
        """

    def pages(self) -> Iterator[List[Group]]:
        """
        A generator which yields pages of Groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_groups.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_groups)
        """

    def __iter__(self) -> Iterator[Group]:
        """
        A generator which yields Groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_groups.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_groups)
        """

class PolicyAttachedRolesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_roles.html#IAM.Policy.attached_roles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_roles)
    """
    def all(self) -> PolicyAttachedRolesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_roles.html#IAM.Policy.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_roles)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        EntityFilter: EntityTypeType = ...,
        PathPrefix: str = ...,
        PolicyUsageFilter: PolicyUsageTypeType = ...,
        Marker: str = ...,
        MaxItems: int = ...,
    ) -> PolicyAttachedRolesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_roles.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_roles)
        """

    def limit(self, count: int) -> PolicyAttachedRolesCollection:
        """
        Return at most this many Roles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_roles.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_roles)
        """

    def page_size(self, count: int) -> PolicyAttachedRolesCollection:
        """
        Fetch at most this many Roles per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_roles.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_roles)
        """

    def pages(self) -> Iterator[List[Role]]:
        """
        A generator which yields pages of Roles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_roles.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_roles)
        """

    def __iter__(self) -> Iterator[Role]:
        """
        A generator which yields Roles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_roles.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_roles)
        """

class PolicyAttachedUsersCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_users.html#IAM.Policy.attached_users)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_users)
    """
    def all(self) -> PolicyAttachedUsersCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_users.html#IAM.Policy.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_users)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        EntityFilter: EntityTypeType = ...,
        PathPrefix: str = ...,
        PolicyUsageFilter: PolicyUsageTypeType = ...,
        Marker: str = ...,
        MaxItems: int = ...,
    ) -> PolicyAttachedUsersCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_users.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_users)
        """

    def limit(self, count: int) -> PolicyAttachedUsersCollection:
        """
        Return at most this many Users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_users.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_users)
        """

    def page_size(self, count: int) -> PolicyAttachedUsersCollection:
        """
        Fetch at most this many Users per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_users.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_users)
        """

    def pages(self) -> Iterator[List[User]]:
        """
        A generator which yields pages of Users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_users.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_users)
        """

    def __iter__(self) -> Iterator[User]:
        """
        A generator which yields Users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attached_users.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattached_users)
        """

class PolicyVersionsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/versions.html#IAM.Policy.versions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyversions)
    """
    def all(self) -> PolicyVersionsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/versions.html#IAM.Policy.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyversions)
        """

    def filter(  # type: ignore[override]
        self, *, Marker: str = ..., MaxItems: int = ...
    ) -> PolicyVersionsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/versions.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyversions)
        """

    def limit(self, count: int) -> PolicyVersionsCollection:
        """
        Return at most this many PolicyVersions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/versions.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyversions)
        """

    def page_size(self, count: int) -> PolicyVersionsCollection:
        """
        Fetch at most this many PolicyVersions per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/versions.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyversions)
        """

    def pages(self) -> Iterator[List[PolicyVersion]]:
        """
        A generator which yields pages of PolicyVersions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/versions.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyversions)
        """

    def __iter__(self) -> Iterator[PolicyVersion]:
        """
        A generator which yields PolicyVersions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/versions.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyversions)
        """

class RoleAttachedPoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/attached_policies.html#IAM.Role.attached_policies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleattached_policies)
    """
    def all(self) -> RoleAttachedPoliciesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/attached_policies.html#IAM.Role.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleattached_policies)
        """

    def filter(  # type: ignore[override]
        self, *, PathPrefix: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> RoleAttachedPoliciesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/attached_policies.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleattached_policies)
        """

    def limit(self, count: int) -> RoleAttachedPoliciesCollection:
        """
        Return at most this many Policys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/attached_policies.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleattached_policies)
        """

    def page_size(self, count: int) -> RoleAttachedPoliciesCollection:
        """
        Fetch at most this many Policys per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/attached_policies.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleattached_policies)
        """

    def pages(self) -> Iterator[List[Policy]]:
        """
        A generator which yields pages of Policys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/attached_policies.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleattached_policies)
        """

    def __iter__(self) -> Iterator[Policy]:
        """
        A generator which yields Policys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/attached_policies.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleattached_policies)
        """

class RoleInstanceProfilesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/instance_profiles.html#IAM.Role.instance_profiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleinstance_profiles)
    """
    def all(self) -> RoleInstanceProfilesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/instance_profiles.html#IAM.Role.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleinstance_profiles)
        """

    def filter(  # type: ignore[override]
        self, *, Marker: str = ..., MaxItems: int = ...
    ) -> RoleInstanceProfilesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/instance_profiles.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleinstance_profiles)
        """

    def limit(self, count: int) -> RoleInstanceProfilesCollection:
        """
        Return at most this many InstanceProfiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/instance_profiles.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleinstance_profiles)
        """

    def page_size(self, count: int) -> RoleInstanceProfilesCollection:
        """
        Fetch at most this many InstanceProfiles per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/instance_profiles.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleinstance_profiles)
        """

    def pages(self) -> Iterator[List[InstanceProfile]]:
        """
        A generator which yields pages of InstanceProfiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/instance_profiles.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleinstance_profiles)
        """

    def __iter__(self) -> Iterator[InstanceProfile]:
        """
        A generator which yields InstanceProfiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/instance_profiles.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleinstance_profiles)
        """

class RolePoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/policies.html#IAM.Role.policies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicies)
    """
    def all(self) -> RolePoliciesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/policies.html#IAM.Role.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicies)
        """

    def filter(  # type: ignore[override]
        self, *, Marker: str = ..., MaxItems: int = ...
    ) -> RolePoliciesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/policies.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicies)
        """

    def limit(self, count: int) -> RolePoliciesCollection:
        """
        Return at most this many RolePolicys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/policies.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicies)
        """

    def page_size(self, count: int) -> RolePoliciesCollection:
        """
        Fetch at most this many RolePolicys per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/policies.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicies)
        """

    def pages(self) -> Iterator[List[RolePolicy]]:
        """
        A generator which yields pages of RolePolicys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/policies.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicies)
        """

    def __iter__(self) -> Iterator[RolePolicy]:
        """
        A generator which yields RolePolicys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/policies.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicies)
        """

class UserAccessKeysCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/access_keys.html#IAM.User.access_keys)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#useraccess_keys)
    """
    def all(self) -> UserAccessKeysCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/access_keys.html#IAM.User.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#useraccess_keys)
        """

    def filter(  # type: ignore[override]
        self, *, UserName: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> UserAccessKeysCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/access_keys.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#useraccess_keys)
        """

    def limit(self, count: int) -> UserAccessKeysCollection:
        """
        Return at most this many AccessKeys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/access_keys.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#useraccess_keys)
        """

    def page_size(self, count: int) -> UserAccessKeysCollection:
        """
        Fetch at most this many AccessKeys per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/access_keys.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#useraccess_keys)
        """

    def pages(self) -> Iterator[List[AccessKey]]:
        """
        A generator which yields pages of AccessKeys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/access_keys.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#useraccess_keys)
        """

    def __iter__(self) -> Iterator[AccessKey]:
        """
        A generator which yields AccessKeys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/access_keys.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#useraccess_keys)
        """

class UserAttachedPoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/attached_policies.html#IAM.User.attached_policies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userattached_policies)
    """
    def all(self) -> UserAttachedPoliciesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/attached_policies.html#IAM.User.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userattached_policies)
        """

    def filter(  # type: ignore[override]
        self, *, PathPrefix: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> UserAttachedPoliciesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/attached_policies.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userattached_policies)
        """

    def limit(self, count: int) -> UserAttachedPoliciesCollection:
        """
        Return at most this many Policys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/attached_policies.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userattached_policies)
        """

    def page_size(self, count: int) -> UserAttachedPoliciesCollection:
        """
        Fetch at most this many Policys per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/attached_policies.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userattached_policies)
        """

    def pages(self) -> Iterator[List[Policy]]:
        """
        A generator which yields pages of Policys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/attached_policies.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userattached_policies)
        """

    def __iter__(self) -> Iterator[Policy]:
        """
        A generator which yields Policys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/attached_policies.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userattached_policies)
        """

class UserGroupsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/groups.html#IAM.User.groups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usergroups)
    """
    def all(self) -> UserGroupsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/groups.html#IAM.User.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usergroups)
        """

    def filter(  # type: ignore[override]
        self, *, Marker: str = ..., MaxItems: int = ...
    ) -> UserGroupsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/groups.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usergroups)
        """

    def limit(self, count: int) -> UserGroupsCollection:
        """
        Return at most this many Groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/groups.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usergroups)
        """

    def page_size(self, count: int) -> UserGroupsCollection:
        """
        Fetch at most this many Groups per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/groups.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usergroups)
        """

    def pages(self) -> Iterator[List[Group]]:
        """
        A generator which yields pages of Groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/groups.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usergroups)
        """

    def __iter__(self) -> Iterator[Group]:
        """
        A generator which yields Groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/groups.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usergroups)
        """

class UserMfaDevicesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/mfa_devices.html#IAM.User.mfa_devices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usermfa_devices)
    """
    def all(self) -> UserMfaDevicesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/mfa_devices.html#IAM.User.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usermfa_devices)
        """

    def filter(  # type: ignore[override]
        self, *, UserName: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> UserMfaDevicesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/mfa_devices.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usermfa_devices)
        """

    def limit(self, count: int) -> UserMfaDevicesCollection:
        """
        Return at most this many MfaDevices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/mfa_devices.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usermfa_devices)
        """

    def page_size(self, count: int) -> UserMfaDevicesCollection:
        """
        Fetch at most this many MfaDevices per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/mfa_devices.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usermfa_devices)
        """

    def pages(self) -> Iterator[List[MfaDevice]]:
        """
        A generator which yields pages of MfaDevices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/mfa_devices.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usermfa_devices)
        """

    def __iter__(self) -> Iterator[MfaDevice]:
        """
        A generator which yields MfaDevices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/mfa_devices.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usermfa_devices)
        """

class UserPoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/policies.html#IAM.User.policies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicies)
    """
    def all(self) -> UserPoliciesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/policies.html#IAM.User.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicies)
        """

    def filter(  # type: ignore[override]
        self, *, Marker: str = ..., MaxItems: int = ...
    ) -> UserPoliciesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/policies.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicies)
        """

    def limit(self, count: int) -> UserPoliciesCollection:
        """
        Return at most this many UserPolicys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/policies.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicies)
        """

    def page_size(self, count: int) -> UserPoliciesCollection:
        """
        Fetch at most this many UserPolicys per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/policies.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicies)
        """

    def pages(self) -> Iterator[List[UserPolicy]]:
        """
        A generator which yields pages of UserPolicys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/policies.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicies)
        """

    def __iter__(self) -> Iterator[UserPolicy]:
        """
        A generator which yields UserPolicys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/policies.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicies)
        """

class UserSigningCertificatesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/signing_certificates.html#IAM.User.signing_certificates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usersigning_certificates)
    """
    def all(self) -> UserSigningCertificatesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/signing_certificates.html#IAM.User.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usersigning_certificates)
        """

    def filter(  # type: ignore[override]
        self, *, UserName: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> UserSigningCertificatesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/signing_certificates.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usersigning_certificates)
        """

    def limit(self, count: int) -> UserSigningCertificatesCollection:
        """
        Return at most this many SigningCertificates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/signing_certificates.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usersigning_certificates)
        """

    def page_size(self, count: int) -> UserSigningCertificatesCollection:
        """
        Fetch at most this many SigningCertificates per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/signing_certificates.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usersigning_certificates)
        """

    def pages(self) -> Iterator[List[SigningCertificate]]:
        """
        A generator which yields pages of SigningCertificates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/signing_certificates.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usersigning_certificates)
        """

    def __iter__(self) -> Iterator[SigningCertificate]:
        """
        A generator which yields SigningCertificates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/signing_certificates.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usersigning_certificates)
        """

class AccessKey(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accesskey/index.html#IAM.AccessKey)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskey)
    """

    user_name: str
    id: str
    access_key_id: str
    status: StatusTypeType
    create_date: datetime
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this AccessKey.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accesskey/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskeyget_available_subresources-method)
        """

    def activate(self, **kwargs: Unpack[UpdateAccessKeyRequestAccessKeyActivateTypeDef]) -> None:
        """
        Changes the status of the specified access key from Active to Inactive, or vice
        versa.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accesskey/activate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskeyactivate-method)
        """

    def deactivate(
        self, **kwargs: Unpack[UpdateAccessKeyRequestAccessKeyDeactivateTypeDef]
    ) -> None:
        """
        Changes the status of the specified access key from Active to Inactive, or vice
        versa.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accesskey/deactivate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskeydeactivate-method)
        """

    def delete(self) -> None:
        """
        Deletes the access key pair associated with the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accesskey/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskeydelete-method)
        """

    def User(self) -> _User:
        """
        Creates a User resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accesskey/User.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskeyuser-method)
        """

_AccessKey = AccessKey

class AccessKeyPair(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accesskeypair/index.html#IAM.AccessKeyPair)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskeypair)
    """

    user_name: str
    id: str
    secret: str
    access_key_id: str
    status: StatusTypeType
    secret_access_key: str
    create_date: datetime
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this AccessKeyPair.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accesskeypair/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskeypairget_available_subresources-method)
        """

    def activate(
        self, **kwargs: Unpack[UpdateAccessKeyRequestAccessKeyPairActivateTypeDef]
    ) -> None:
        """
        Changes the status of the specified access key from Active to Inactive, or vice
        versa.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accesskeypair/activate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskeypairactivate-method)
        """

    def deactivate(
        self, **kwargs: Unpack[UpdateAccessKeyRequestAccessKeyPairDeactivateTypeDef]
    ) -> None:
        """
        Changes the status of the specified access key from Active to Inactive, or vice
        versa.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accesskeypair/deactivate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskeypairdeactivate-method)
        """

    def delete(self) -> None:
        """
        Deletes the access key pair associated with the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accesskeypair/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskeypairdelete-method)
        """

_AccessKeyPair = AccessKeyPair

class AccountPasswordPolicy(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accountpasswordpolicy/index.html#IAM.AccountPasswordPolicy)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accountpasswordpolicy)
    """

    minimum_password_length: int
    require_symbols: bool
    require_numbers: bool
    require_uppercase_characters: bool
    require_lowercase_characters: bool
    allow_users_to_change_password: bool
    expire_passwords: bool
    max_password_age: int
    password_reuse_prevention: int
    hard_expiry: bool
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this
        AccountPasswordPolicy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accountpasswordpolicy/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accountpasswordpolicyget_available_subresources-method)
        """

    def delete(self) -> None:
        """
        Deletes the password policy for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accountpasswordpolicy/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accountpasswordpolicydelete-method)
        """

    def update(
        self, **kwargs: Unpack[UpdateAccountPasswordPolicyRequestAccountPasswordPolicyUpdateTypeDef]
    ) -> None:
        """
        Updates the password policy settings for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accountpasswordpolicy/update.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accountpasswordpolicyupdate-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accountpasswordpolicy/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accountpasswordpolicyload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accountpasswordpolicy/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accountpasswordpolicyreload-method)
        """

_AccountPasswordPolicy = AccountPasswordPolicy

class AccountSummary(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accountsummary/index.html#IAM.AccountSummary)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accountsummary)
    """

    summary_map: Dict[SummaryKeyTypeType, int]
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this AccountSummary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accountsummary/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accountsummaryget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accountsummary/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accountsummaryload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/accountsummary/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accountsummaryreload-method)
        """

_AccountSummary = AccountSummary

class AssumeRolePolicy(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/assumerolepolicy/index.html#IAM.AssumeRolePolicy)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#assumerolepolicy)
    """

    role_name: str
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this AssumeRolePolicy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/assumerolepolicy/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#assumerolepolicyget_available_subresources-method)
        """

    def update(
        self, **kwargs: Unpack[UpdateAssumeRolePolicyRequestAssumeRolePolicyUpdateTypeDef]
    ) -> None:
        """
        Updates the policy that grants an IAM entity permission to assume a role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/assumerolepolicy/update.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#assumerolepolicyupdate-method)
        """

    def Role(self) -> _Role:
        """
        Creates a Role resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/assumerolepolicy/Role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#assumerolepolicyrole-method)
        """

_AssumeRolePolicy = AssumeRolePolicy

class CurrentUser(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/index.html#IAM.CurrentUser)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentuser)
    """

    user: User
    access_keys: CurrentUserAccessKeysCollection
    mfa_devices: CurrentUserMfaDevicesCollection
    signing_certificates: CurrentUserSigningCertificatesCollection
    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime
    permissions_boundary: AttachedPermissionsBoundaryTypeDef
    tags: List[TagTypeDef]
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this CurrentUser.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentuserget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentuserload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/currentuser/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentuserreload-method)
        """

_CurrentUser = CurrentUser

class Group(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/index.html#IAM.Group)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#group)
    """

    name: str
    attached_policies: GroupAttachedPoliciesCollection
    policies: GroupPoliciesCollection
    users: GroupUsersCollection
    path: str
    group_name: str
    group_id: str
    arn: str
    create_date: datetime
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupget_available_subresources-method)
        """

    def add_user(self, **kwargs: Unpack[AddUserToGroupRequestGroupAddUserTypeDef]) -> None:
        """
        Adds the specified user to the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/add_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupadd_user-method)
        """

    def attach_policy(
        self, **kwargs: Unpack[AttachGroupPolicyRequestGroupAttachPolicyTypeDef]
    ) -> None:
        """
        Attaches the specified managed policy to the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/attach_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupattach_policy-method)
        """

    def create(self, **kwargs: Unpack[CreateGroupRequestGroupCreateTypeDef]) -> _Group:
        """
        Creates a new group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/create.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupcreate-method)
        """

    def create_policy(
        self, **kwargs: Unpack[PutGroupPolicyRequestGroupCreatePolicyTypeDef]
    ) -> _GroupPolicy:
        """
        Adds or updates an inline policy document that is embedded in the specified IAM
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/create_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupcreate_policy-method)
        """

    def delete(self) -> None:
        """
        Deletes the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupdelete-method)
        """

    def detach_policy(
        self, **kwargs: Unpack[DetachGroupPolicyRequestGroupDetachPolicyTypeDef]
    ) -> None:
        """
        Removes the specified managed policy from the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/detach_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupdetach_policy-method)
        """

    def remove_user(
        self, **kwargs: Unpack[RemoveUserFromGroupRequestGroupRemoveUserTypeDef]
    ) -> None:
        """
        Removes the specified user from the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/remove_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupremove_user-method)
        """

    def update(self, **kwargs: Unpack[UpdateGroupRequestGroupUpdateTypeDef]) -> _Group:
        """
        Updates the name and/or the path of the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/update.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupupdate-method)
        """

    def Policy(self, name: str) -> _GroupPolicy:
        """
        Creates a GroupPolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/Policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicy-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/group/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupreload-method)
        """

_Group = Group

class GroupPolicy(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/grouppolicy/index.html#IAM.GroupPolicy)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicy)
    """

    group_name: str
    name: str
    policy_name: str
    policy_document: PolicyDocumentTypeDef
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this GroupPolicy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/grouppolicy/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicyget_available_subresources-method)
        """

    def delete(self) -> None:
        """
        Deletes the specified inline policy that is embedded in the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/grouppolicy/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicydelete-method)
        """

    def put(self, **kwargs: Unpack[PutGroupPolicyRequestGroupPolicyPutTypeDef]) -> None:
        """
        Adds or updates an inline policy document that is embedded in the specified IAM
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/grouppolicy/put.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicyput-method)
        """

    def Group(self) -> _Group:
        """
        Creates a Group resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/grouppolicy/Group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicygroup-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/grouppolicy/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicyload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/grouppolicy/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicyreload-method)
        """

_GroupPolicy = GroupPolicy

class InstanceProfile(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/instanceprofile/index.html#IAM.InstanceProfile)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#instanceprofile)
    """

    name: str
    roles: List[Role]
    path: str
    instance_profile_name: str
    instance_profile_id: str
    arn: str
    create_date: datetime
    roles_attribute: List[RoleTypeDef]
    tags: List[TagTypeDef]
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this InstanceProfile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/instanceprofile/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#instanceprofileget_available_subresources-method)
        """

    def add_role(
        self, **kwargs: Unpack[AddRoleToInstanceProfileRequestInstanceProfileAddRoleTypeDef]
    ) -> None:
        """
        Adds the specified IAM role to the specified instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/instanceprofile/add_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#instanceprofileadd_role-method)
        """

    def delete(self) -> None:
        """
        Deletes the specified instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/instanceprofile/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#instanceprofiledelete-method)
        """

    def remove_role(
        self, **kwargs: Unpack[RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRoleTypeDef]
    ) -> None:
        """
        Removes the specified IAM role from the specified Amazon EC2 instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/instanceprofile/remove_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#instanceprofileremove_role-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/instanceprofile/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#instanceprofileload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/instanceprofile/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#instanceprofilereload-method)
        """

_InstanceProfile = InstanceProfile

class LoginProfile(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/loginprofile/index.html#IAM.LoginProfile)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#loginprofile)
    """

    user_name: str
    create_date: datetime
    password_reset_required: bool
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this LoginProfile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/loginprofile/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#loginprofileget_available_subresources-method)
        """

    def create(
        self, **kwargs: Unpack[CreateLoginProfileRequestLoginProfileCreateTypeDef]
    ) -> _LoginProfile:
        """
        Creates a password for the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/loginprofile/create.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#loginprofilecreate-method)
        """

    def delete(self) -> None:
        """
        Deletes the password for the specified IAM user, For more information, see <a
        href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.html">Managing
        passwords for IAM users</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/loginprofile/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#loginprofiledelete-method)
        """

    def update(self, **kwargs: Unpack[UpdateLoginProfileRequestLoginProfileUpdateTypeDef]) -> None:
        """
        Changes the password for the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/loginprofile/update.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#loginprofileupdate-method)
        """

    def User(self) -> _User:
        """
        Creates a User resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/loginprofile/User.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#loginprofileuser-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/loginprofile/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#loginprofileload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/loginprofile/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#loginprofilereload-method)
        """

_LoginProfile = LoginProfile

class MfaDevice(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/mfadevice/index.html#IAM.MfaDevice)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#mfadevice)
    """

    user_name: str
    serial_number: str
    enable_date: datetime
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this MfaDevice.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/mfadevice/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#mfadeviceget_available_subresources-method)
        """

    def associate(self, **kwargs: Unpack[EnableMFADeviceRequestMfaDeviceAssociateTypeDef]) -> None:
        """
        Enables the specified MFA device and associates it with the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/mfadevice/associate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#mfadeviceassociate-method)
        """

    def disassociate(self) -> None:
        """
        Deactivates the specified MFA device and removes it from association with the
        user name for which it was originally enabled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/mfadevice/disassociate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#mfadevicedisassociate-method)
        """

    def resync(self, **kwargs: Unpack[ResyncMFADeviceRequestMfaDeviceResyncTypeDef]) -> None:
        """
        Synchronizes the specified MFA device with its IAM resource object on the
        Amazon Web Services servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/mfadevice/resync.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#mfadeviceresync-method)
        """

    def User(self) -> _User:
        """
        Creates a User resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/mfadevice/User.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#mfadeviceuser-method)
        """

_MfaDevice = MfaDevice

class Policy(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/index.html#IAM.Policy)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policy)
    """

    arn: str
    default_version: PolicyVersion
    attached_groups: PolicyAttachedGroupsCollection
    attached_roles: PolicyAttachedRolesCollection
    attached_users: PolicyAttachedUsersCollection
    versions: PolicyVersionsCollection
    policy_name: str
    policy_id: str
    path: str
    default_version_id: str
    attachment_count: int
    permissions_boundary_usage_count: int
    is_attachable: bool
    description: str
    create_date: datetime
    update_date: datetime
    tags: List[TagTypeDef]
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyget_available_subresources-method)
        """

    def attach_group(
        self, **kwargs: Unpack[AttachGroupPolicyRequestPolicyAttachGroupTypeDef]
    ) -> None:
        """
        Attaches the specified managed policy to the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attach_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattach_group-method)
        """

    def attach_role(self, **kwargs: Unpack[AttachRolePolicyRequestPolicyAttachRoleTypeDef]) -> None:
        """
        Attaches the specified managed policy to the specified IAM role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attach_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattach_role-method)
        """

    def attach_user(self, **kwargs: Unpack[AttachUserPolicyRequestPolicyAttachUserTypeDef]) -> None:
        """
        Attaches the specified managed policy to the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/attach_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattach_user-method)
        """

    def create_version(
        self, **kwargs: Unpack[CreatePolicyVersionRequestPolicyCreateVersionTypeDef]
    ) -> _PolicyVersion:
        """
        Creates a new version of the specified managed policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/create_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policycreate_version-method)
        """

    def delete(self) -> None:
        """
        Deletes the specified managed policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policydelete-method)
        """

    def detach_group(
        self, **kwargs: Unpack[DetachGroupPolicyRequestPolicyDetachGroupTypeDef]
    ) -> None:
        """
        Removes the specified managed policy from the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/detach_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policydetach_group-method)
        """

    def detach_role(self, **kwargs: Unpack[DetachRolePolicyRequestPolicyDetachRoleTypeDef]) -> None:
        """
        Removes the specified managed policy from the specified role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/detach_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policydetach_role-method)
        """

    def detach_user(self, **kwargs: Unpack[DetachUserPolicyRequestPolicyDetachUserTypeDef]) -> None:
        """
        Removes the specified managed policy from the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/detach_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policydetach_user-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policy/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyreload-method)
        """

_Policy = Policy

class PolicyVersion(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policyversion/index.html#IAM.PolicyVersion)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyversion)
    """

    arn: str
    version_id: str
    document: PolicyDocumentTypeDef
    is_default_version: bool
    create_date: datetime
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this PolicyVersion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policyversion/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyversionget_available_subresources-method)
        """

    def delete(self) -> None:
        """
        Deletes the specified version from the specified managed policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policyversion/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyversiondelete-method)
        """

    def set_as_default(self) -> None:
        """
        Sets the specified version of the specified policy as the policy's default
        (operative) version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policyversion/set_as_default.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyversionset_as_default-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policyversion/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyversionload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/policyversion/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyversionreload-method)
        """

_PolicyVersion = PolicyVersion

class Role(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/index.html#IAM.Role)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#role)
    """

    name: str
    attached_policies: RoleAttachedPoliciesCollection
    instance_profiles: RoleInstanceProfilesCollection
    policies: RolePoliciesCollection
    path: str
    role_name: str
    role_id: str
    arn: str
    create_date: datetime
    assume_role_policy_document: PolicyDocumentTypeDef
    description: str
    max_session_duration: int
    permissions_boundary: AttachedPermissionsBoundaryTypeDef
    tags: List[TagTypeDef]
    role_last_used: RoleLastUsedTypeDef
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleget_available_subresources-method)
        """

    def attach_policy(
        self, **kwargs: Unpack[AttachRolePolicyRequestRoleAttachPolicyTypeDef]
    ) -> None:
        """
        Attaches the specified managed policy to the specified IAM role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/attach_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleattach_policy-method)
        """

    def delete(self) -> None:
        """
        Deletes the specified role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roledelete-method)
        """

    def detach_policy(
        self, **kwargs: Unpack[DetachRolePolicyRequestRoleDetachPolicyTypeDef]
    ) -> None:
        """
        Removes the specified managed policy from the specified role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/detach_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roledetach_policy-method)
        """

    def AssumeRolePolicy(self) -> _AssumeRolePolicy:
        """
        Creates a AssumeRolePolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/AssumeRolePolicy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleassumerolepolicy-method)
        """

    def Policy(self, name: str) -> _RolePolicy:
        """
        Creates a RolePolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/Policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicy-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/role/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolereload-method)
        """

_Role = Role

class RolePolicy(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/rolepolicy/index.html#IAM.RolePolicy)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicy)
    """

    role_name: str
    name: str
    policy_name: str
    policy_document: PolicyDocumentTypeDef
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this RolePolicy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/rolepolicy/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicyget_available_subresources-method)
        """

    def delete(self) -> None:
        """
        Deletes the specified inline policy that is embedded in the specified IAM role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/rolepolicy/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicydelete-method)
        """

    def put(self, **kwargs: Unpack[PutRolePolicyRequestRolePolicyPutTypeDef]) -> None:
        """
        Adds or updates an inline policy document that is embedded in the specified IAM
        role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/rolepolicy/put.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicyput-method)
        """

    def Role(self) -> _Role:
        """
        Creates a Role resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/rolepolicy/Role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicyrole-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/rolepolicy/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicyload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/rolepolicy/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicyreload-method)
        """

_RolePolicy = RolePolicy

class SamlProvider(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/samlprovider/index.html#IAM.SamlProvider)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#samlprovider)
    """

    arn: str
    saml_provider_uuid: str
    saml_metadata_document: str
    create_date: datetime
    valid_until: datetime
    tags: List[TagTypeDef]
    assertion_encryption_mode: AssertionEncryptionModeTypeType
    private_key_list: List[SAMLPrivateKeyTypeDef]
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this SamlProvider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/samlprovider/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#samlproviderget_available_subresources-method)
        """

    def delete(self) -> None:
        """
        Deletes a SAML provider resource in IAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/samlprovider/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#samlproviderdelete-method)
        """

    def update(
        self, **kwargs: Unpack[UpdateSAMLProviderRequestSamlProviderUpdateTypeDef]
    ) -> UpdateSAMLProviderResponseTypeDef:
        """
        Updates the metadata document, SAML encryption settings, and private keys for
        an existing SAML provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/samlprovider/update.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#samlproviderupdate-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/samlprovider/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#samlproviderload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/samlprovider/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#samlproviderreload-method)
        """

_SamlProvider = SamlProvider

class ServerCertificate(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/servercertificate/index.html#IAM.ServerCertificate)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#servercertificate)
    """

    name: str
    server_certificate_metadata: ServerCertificateMetadataTypeDef
    certificate_body: str
    certificate_chain: str
    tags: List[TagTypeDef]
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this ServerCertificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/servercertificate/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#servercertificateget_available_subresources-method)
        """

    def delete(self) -> None:
        """
        Deletes the specified server certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/servercertificate/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#servercertificatedelete-method)
        """

    def update(
        self, **kwargs: Unpack[UpdateServerCertificateRequestServerCertificateUpdateTypeDef]
    ) -> _ServerCertificate:
        """
        Updates the name and/or the path of the specified server certificate stored in
        IAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/servercertificate/update.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#servercertificateupdate-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/servercertificate/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#servercertificateload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/servercertificate/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#servercertificatereload-method)
        """

_ServerCertificate = ServerCertificate

class SigningCertificate(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/signingcertificate/index.html#IAM.SigningCertificate)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#signingcertificate)
    """

    user_name: str
    id: str
    certificate_id: str
    certificate_body: str
    status: StatusTypeType
    upload_date: datetime
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this SigningCertificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/signingcertificate/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#signingcertificateget_available_subresources-method)
        """

    def activate(
        self, **kwargs: Unpack[UpdateSigningCertificateRequestSigningCertificateActivateTypeDef]
    ) -> None:
        """
        Changes the status of the specified user signing certificate from active to
        disabled, or vice versa.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/signingcertificate/activate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#signingcertificateactivate-method)
        """

    def deactivate(
        self, **kwargs: Unpack[UpdateSigningCertificateRequestSigningCertificateDeactivateTypeDef]
    ) -> None:
        """
        Changes the status of the specified user signing certificate from active to
        disabled, or vice versa.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/signingcertificate/deactivate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#signingcertificatedeactivate-method)
        """

    def delete(self) -> None:
        """
        Deletes a signing certificate associated with the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/signingcertificate/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#signingcertificatedelete-method)
        """

    def User(self) -> _User:
        """
        Creates a User resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/signingcertificate/User.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#signingcertificateuser-method)
        """

_SigningCertificate = SigningCertificate

class User(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/index.html#IAM.User)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#user)
    """

    name: str
    access_keys: UserAccessKeysCollection
    attached_policies: UserAttachedPoliciesCollection
    groups: UserGroupsCollection
    mfa_devices: UserMfaDevicesCollection
    policies: UserPoliciesCollection
    signing_certificates: UserSigningCertificatesCollection
    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime
    permissions_boundary: AttachedPermissionsBoundaryTypeDef
    tags: List[TagTypeDef]
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this User.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userget_available_subresources-method)
        """

    def add_group(self, **kwargs: Unpack[AddUserToGroupRequestUserAddGroupTypeDef]) -> None:
        """
        Adds the specified user to the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/add_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#useradd_group-method)
        """

    def attach_policy(
        self, **kwargs: Unpack[AttachUserPolicyRequestUserAttachPolicyTypeDef]
    ) -> None:
        """
        Attaches the specified managed policy to the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/attach_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userattach_policy-method)
        """

    def create(self, **kwargs: Unpack[CreateUserRequestUserCreateTypeDef]) -> _User:
        """
        Creates a new IAM user for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/create.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usercreate-method)
        """

    def create_access_key_pair(self) -> _AccessKeyPair:
        """
        Creates a new Amazon Web Services secret access key and corresponding Amazon
        Web Services access key ID for the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/create_access_key_pair.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usercreate_access_key_pair-method)
        """

    def create_login_profile(
        self, **kwargs: Unpack[CreateLoginProfileRequestUserCreateLoginProfileTypeDef]
    ) -> _LoginProfile:
        """
        Creates a password for the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/create_login_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usercreate_login_profile-method)
        """

    def create_policy(
        self, **kwargs: Unpack[PutUserPolicyRequestUserCreatePolicyTypeDef]
    ) -> _UserPolicy:
        """
        Adds or updates an inline policy document that is embedded in the specified IAM
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/create_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usercreate_policy-method)
        """

    def delete(self) -> None:
        """
        Deletes the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userdelete-method)
        """

    def detach_policy(
        self, **kwargs: Unpack[DetachUserPolicyRequestUserDetachPolicyTypeDef]
    ) -> None:
        """
        Removes the specified managed policy from the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/detach_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userdetach_policy-method)
        """

    def enable_mfa(
        self, **kwargs: Unpack[EnableMFADeviceRequestUserEnableMfaTypeDef]
    ) -> _MfaDevice:
        """
        Enables the specified MFA device and associates it with the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/enable_mfa.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userenable_mfa-method)
        """

    def remove_group(
        self, **kwargs: Unpack[RemoveUserFromGroupRequestUserRemoveGroupTypeDef]
    ) -> None:
        """
        Removes the specified user from the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/remove_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userremove_group-method)
        """

    def update(self, **kwargs: Unpack[UpdateUserRequestUserUpdateTypeDef]) -> _User:
        """
        Updates the name and/or the path of the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/update.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userupdate-method)
        """

    def AccessKey(self, id: str) -> _AccessKey:
        """
        Creates a AccessKey resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/AccessKey.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#useraccesskey-method)
        """

    def LoginProfile(self) -> _LoginProfile:
        """
        Creates a LoginProfile resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/LoginProfile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userloginprofile-method)
        """

    def MfaDevice(self, serial_number: str) -> _MfaDevice:
        """
        Creates a MfaDevice resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/MfaDevice.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usermfadevice-method)
        """

    def Policy(self, name: str) -> _UserPolicy:
        """
        Creates a UserPolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/Policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicy-method)
        """

    def SigningCertificate(self, id: str) -> _SigningCertificate:
        """
        Creates a SigningCertificate resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/SigningCertificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usersigningcertificate-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userreload-method)
        """

_User = User

class UserPolicy(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/userpolicy/index.html#IAM.UserPolicy)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicy)
    """

    user_name: str
    name: str
    policy_name: str
    policy_document: PolicyDocumentTypeDef
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this UserPolicy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/userpolicy/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicyget_available_subresources-method)
        """

    def delete(self) -> None:
        """
        Deletes the specified inline policy that is embedded in the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/userpolicy/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicydelete-method)
        """

    def put(self, **kwargs: Unpack[PutUserPolicyRequestUserPolicyPutTypeDef]) -> None:
        """
        Adds or updates an inline policy document that is embedded in the specified IAM
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/userpolicy/put.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicyput-method)
        """

    def User(self) -> _User:
        """
        Creates a User resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/userpolicy/User.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicyuser-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/userpolicy/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicyload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/userpolicy/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicyreload-method)
        """

_UserPolicy = UserPolicy

class VirtualMfaDevice(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/virtualmfadevice/index.html#IAM.VirtualMfaDevice)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#virtualmfadevice)
    """

    serial_number: str
    user: User
    base32_string_seed: bytes
    qr_code_png: bytes
    user_attribute: UserTypeDef
    enable_date: datetime
    tags: List[TagTypeDef]
    meta: IAMResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this VirtualMfaDevice.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/virtualmfadevice/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#virtualmfadeviceget_available_subresources-method)
        """

    def delete(self) -> None:
        """
        Deletes a virtual MFA device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/virtualmfadevice/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#virtualmfadevicedelete-method)
        """

_VirtualMfaDevice = VirtualMfaDevice

class IAMResourceMeta(ResourceMeta):
    client: IAMClient  # type: ignore[override]

class IAMServiceResource(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/index.html)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/)
    """

    meta: IAMResourceMeta  # type: ignore[override]
    groups: ServiceResourceGroupsCollection
    instance_profiles: ServiceResourceInstanceProfilesCollection
    policies: ServiceResourcePoliciesCollection
    roles: ServiceResourceRolesCollection
    saml_providers: ServiceResourceSamlProvidersCollection
    server_certificates: ServiceResourceServerCertificatesCollection
    users: ServiceResourceUsersCollection
    virtual_mfa_devices: ServiceResourceVirtualMfaDevicesCollection

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceget_available_subresources-method)
        """

    def change_password(
        self, **kwargs: Unpack[ChangePasswordRequestServiceResourceChangePasswordTypeDef]
    ) -> None:
        """
        Changes the password of the IAM user who is calling this operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/change_password.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcechange_password-method)
        """

    def create_account_alias(
        self, **kwargs: Unpack[CreateAccountAliasRequestServiceResourceCreateAccountAliasTypeDef]
    ) -> None:
        """
        Creates an alias for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/create_account_alias.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_account_alias-method)
        """

    def create_account_password_policy(
        self,
        **kwargs: Unpack[
            UpdateAccountPasswordPolicyRequestServiceResourceCreateAccountPasswordPolicyTypeDef
        ],
    ) -> _AccountPasswordPolicy:
        """
        Updates the password policy settings for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/create_account_password_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_account_password_policy-method)
        """

    def create_group(
        self, **kwargs: Unpack[CreateGroupRequestServiceResourceCreateGroupTypeDef]
    ) -> _Group:
        """
        Creates a new group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/create_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_group-method)
        """

    def create_instance_profile(
        self,
        **kwargs: Unpack[CreateInstanceProfileRequestServiceResourceCreateInstanceProfileTypeDef],
    ) -> _InstanceProfile:
        """
        Creates a new instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/create_instance_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_instance_profile-method)
        """

    def create_policy(
        self, **kwargs: Unpack[CreatePolicyRequestServiceResourceCreatePolicyTypeDef]
    ) -> _Policy:
        """
        Creates a new managed policy for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/create_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_policy-method)
        """

    def create_role(
        self, **kwargs: Unpack[CreateRoleRequestServiceResourceCreateRoleTypeDef]
    ) -> _Role:
        """
        Creates a new role for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/create_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_role-method)
        """

    def create_saml_provider(
        self, **kwargs: Unpack[CreateSAMLProviderRequestServiceResourceCreateSamlProviderTypeDef]
    ) -> _SamlProvider:
        """
        Creates an IAM resource that describes an identity provider (IdP) that supports
        SAML 2.0.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/create_saml_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_saml_provider-method)
        """

    def create_server_certificate(
        self,
        **kwargs: Unpack[
            UploadServerCertificateRequestServiceResourceCreateServerCertificateTypeDef
        ],
    ) -> _ServerCertificate:
        """
        Uploads a server certificate entity for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/create_server_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_server_certificate-method)
        """

    def create_signing_certificate(
        self,
        **kwargs: Unpack[
            UploadSigningCertificateRequestServiceResourceCreateSigningCertificateTypeDef
        ],
    ) -> _SigningCertificate:
        """
        Uploads an X.509 signing certificate and associates it with the specified IAM
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/create_signing_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_signing_certificate-method)
        """

    def create_user(
        self, **kwargs: Unpack[CreateUserRequestServiceResourceCreateUserTypeDef]
    ) -> _User:
        """
        Creates a new IAM user for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/create_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_user-method)
        """

    def create_virtual_mfa_device(
        self,
        **kwargs: Unpack[CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDeviceTypeDef],
    ) -> _VirtualMfaDevice:
        """
        Creates a new virtual MFA device for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/create_virtual_mfa_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_virtual_mfa_device-method)
        """

    def AccessKey(self, user_name: str, id: str) -> _AccessKey:
        """
        Creates a AccessKey resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/AccessKey.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceaccesskey-method)
        """

    def AccessKeyPair(self, user_name: str, id: str, secret: str) -> _AccessKeyPair:
        """
        Creates a AccessKeyPair resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/AccessKeyPair.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceaccesskeypair-method)
        """

    def AccountPasswordPolicy(self) -> _AccountPasswordPolicy:
        """
        Creates a AccountPasswordPolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/AccountPasswordPolicy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceaccountpasswordpolicy-method)
        """

    def AccountSummary(self) -> _AccountSummary:
        """
        Creates a AccountSummary resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/AccountSummary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceaccountsummary-method)
        """

    def AssumeRolePolicy(self, role_name: str) -> _AssumeRolePolicy:
        """
        Creates a AssumeRolePolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/AssumeRolePolicy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceassumerolepolicy-method)
        """

    def CurrentUser(self) -> _CurrentUser:
        """
        Creates a CurrentUser resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/CurrentUser.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecurrentuser-method)
        """

    def Group(self, name: str) -> _Group:
        """
        Creates a Group resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/Group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcegroup-method)
        """

    def GroupPolicy(self, group_name: str, name: str) -> _GroupPolicy:
        """
        Creates a GroupPolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/GroupPolicy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcegrouppolicy-method)
        """

    def InstanceProfile(self, name: str) -> _InstanceProfile:
        """
        Creates a InstanceProfile resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/InstanceProfile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceinstanceprofile-method)
        """

    def LoginProfile(self, user_name: str) -> _LoginProfile:
        """
        Creates a LoginProfile resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/LoginProfile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceloginprofile-method)
        """

    def MfaDevice(self, user_name: str, serial_number: str) -> _MfaDevice:
        """
        Creates a MfaDevice resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/MfaDevice.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcemfadevice-method)
        """

    def Policy(self, arn: str) -> _Policy:
        """
        Creates a Policy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/Policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcepolicy-method)
        """

    def PolicyVersion(self, arn: str, version_id: str) -> _PolicyVersion:
        """
        Creates a PolicyVersion resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/PolicyVersion.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcepolicyversion-method)
        """

    def Role(self, name: str) -> _Role:
        """
        Creates a Role resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/Role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcerole-method)
        """

    def RolePolicy(self, role_name: str, name: str) -> _RolePolicy:
        """
        Creates a RolePolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/RolePolicy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcerolepolicy-method)
        """

    def SamlProvider(self, arn: str) -> _SamlProvider:
        """
        Creates a SamlProvider resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/SamlProvider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcesamlprovider-method)
        """

    def ServerCertificate(self, name: str) -> _ServerCertificate:
        """
        Creates a ServerCertificate resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/ServerCertificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceservercertificate-method)
        """

    def SigningCertificate(self, user_name: str, id: str) -> _SigningCertificate:
        """
        Creates a SigningCertificate resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/SigningCertificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcesigningcertificate-method)
        """

    def User(self, name: str) -> _User:
        """
        Creates a User resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/User.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceuser-method)
        """

    def UserPolicy(self, user_name: str, name: str) -> _UserPolicy:
        """
        Creates a UserPolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/UserPolicy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceuserpolicy-method)
        """

    def VirtualMfaDevice(self, serial_number: str) -> _VirtualMfaDevice:
        """
        Creates a VirtualMfaDevice resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/service-resource/VirtualMfaDevice.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcevirtualmfadevice-method)
        """
