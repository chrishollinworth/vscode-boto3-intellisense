"""
Type annotations for iam service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_iam.client import IAMClient

    session = Session()
    client: IAMClient = session.client("iam")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    GetAccountAuthorizationDetailsPaginator,
    GetGroupPaginator,
    ListAccessKeysPaginator,
    ListAccountAliasesPaginator,
    ListAttachedGroupPoliciesPaginator,
    ListAttachedRolePoliciesPaginator,
    ListAttachedUserPoliciesPaginator,
    ListEntitiesForPolicyPaginator,
    ListGroupPoliciesPaginator,
    ListGroupsForUserPaginator,
    ListGroupsPaginator,
    ListInstanceProfilesForRolePaginator,
    ListInstanceProfilesPaginator,
    ListInstanceProfileTagsPaginator,
    ListMFADevicesPaginator,
    ListMFADeviceTagsPaginator,
    ListOpenIDConnectProviderTagsPaginator,
    ListPoliciesPaginator,
    ListPolicyTagsPaginator,
    ListPolicyVersionsPaginator,
    ListRolePoliciesPaginator,
    ListRolesPaginator,
    ListRoleTagsPaginator,
    ListSAMLProviderTagsPaginator,
    ListServerCertificatesPaginator,
    ListServerCertificateTagsPaginator,
    ListSigningCertificatesPaginator,
    ListSSHPublicKeysPaginator,
    ListUserPoliciesPaginator,
    ListUsersPaginator,
    ListUserTagsPaginator,
    ListVirtualMFADevicesPaginator,
    SimulateCustomPolicyPaginator,
    SimulatePrincipalPolicyPaginator,
)
from .type_defs import (
    AddClientIDToOpenIDConnectProviderRequestTypeDef,
    AddRoleToInstanceProfileRequestTypeDef,
    AddUserToGroupRequestTypeDef,
    AttachGroupPolicyRequestTypeDef,
    AttachRolePolicyRequestTypeDef,
    AttachUserPolicyRequestTypeDef,
    ChangePasswordRequestTypeDef,
    CreateAccessKeyRequestTypeDef,
    CreateAccessKeyResponseTypeDef,
    CreateAccountAliasRequestTypeDef,
    CreateGroupRequestTypeDef,
    CreateGroupResponseTypeDef,
    CreateInstanceProfileRequestTypeDef,
    CreateInstanceProfileResponseTypeDef,
    CreateLoginProfileRequestTypeDef,
    CreateLoginProfileResponseTypeDef,
    CreateOpenIDConnectProviderRequestTypeDef,
    CreateOpenIDConnectProviderResponseTypeDef,
    CreatePolicyRequestTypeDef,
    CreatePolicyResponseTypeDef,
    CreatePolicyVersionRequestTypeDef,
    CreatePolicyVersionResponseTypeDef,
    CreateRoleRequestTypeDef,
    CreateRoleResponseTypeDef,
    CreateSAMLProviderRequestTypeDef,
    CreateSAMLProviderResponseTypeDef,
    CreateServiceLinkedRoleRequestTypeDef,
    CreateServiceLinkedRoleResponseTypeDef,
    CreateServiceSpecificCredentialRequestTypeDef,
    CreateServiceSpecificCredentialResponseTypeDef,
    CreateUserRequestTypeDef,
    CreateUserResponseTypeDef,
    CreateVirtualMFADeviceRequestTypeDef,
    CreateVirtualMFADeviceResponseTypeDef,
    DeactivateMFADeviceRequestTypeDef,
    DeleteAccessKeyRequestTypeDef,
    DeleteAccountAliasRequestTypeDef,
    DeleteGroupPolicyRequestTypeDef,
    DeleteGroupRequestTypeDef,
    DeleteInstanceProfileRequestTypeDef,
    DeleteLoginProfileRequestTypeDef,
    DeleteOpenIDConnectProviderRequestTypeDef,
    DeletePolicyRequestTypeDef,
    DeletePolicyVersionRequestTypeDef,
    DeleteRolePermissionsBoundaryRequestTypeDef,
    DeleteRolePolicyRequestTypeDef,
    DeleteRoleRequestTypeDef,
    DeleteSAMLProviderRequestTypeDef,
    DeleteServerCertificateRequestTypeDef,
    DeleteServiceLinkedRoleRequestTypeDef,
    DeleteServiceLinkedRoleResponseTypeDef,
    DeleteServiceSpecificCredentialRequestTypeDef,
    DeleteSigningCertificateRequestTypeDef,
    DeleteSSHPublicKeyRequestTypeDef,
    DeleteUserPermissionsBoundaryRequestTypeDef,
    DeleteUserPolicyRequestTypeDef,
    DeleteUserRequestTypeDef,
    DeleteVirtualMFADeviceRequestTypeDef,
    DetachGroupPolicyRequestTypeDef,
    DetachRolePolicyRequestTypeDef,
    DetachUserPolicyRequestTypeDef,
    DisableOrganizationsRootCredentialsManagementResponseTypeDef,
    DisableOrganizationsRootSessionsResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    EnableMFADeviceRequestTypeDef,
    EnableOrganizationsRootCredentialsManagementResponseTypeDef,
    EnableOrganizationsRootSessionsResponseTypeDef,
    GenerateCredentialReportResponseTypeDef,
    GenerateOrganizationsAccessReportRequestTypeDef,
    GenerateOrganizationsAccessReportResponseTypeDef,
    GenerateServiceLastAccessedDetailsRequestTypeDef,
    GenerateServiceLastAccessedDetailsResponseTypeDef,
    GetAccessKeyLastUsedRequestTypeDef,
    GetAccessKeyLastUsedResponseTypeDef,
    GetAccountAuthorizationDetailsRequestTypeDef,
    GetAccountAuthorizationDetailsResponseTypeDef,
    GetAccountPasswordPolicyResponseTypeDef,
    GetAccountSummaryResponseTypeDef,
    GetContextKeysForCustomPolicyRequestTypeDef,
    GetContextKeysForPolicyResponseTypeDef,
    GetContextKeysForPrincipalPolicyRequestTypeDef,
    GetCredentialReportResponseTypeDef,
    GetGroupPolicyRequestTypeDef,
    GetGroupPolicyResponseTypeDef,
    GetGroupRequestTypeDef,
    GetGroupResponseTypeDef,
    GetInstanceProfileRequestTypeDef,
    GetInstanceProfileResponseTypeDef,
    GetLoginProfileRequestTypeDef,
    GetLoginProfileResponseTypeDef,
    GetMFADeviceRequestTypeDef,
    GetMFADeviceResponseTypeDef,
    GetOpenIDConnectProviderRequestTypeDef,
    GetOpenIDConnectProviderResponseTypeDef,
    GetOrganizationsAccessReportRequestTypeDef,
    GetOrganizationsAccessReportResponseTypeDef,
    GetPolicyRequestTypeDef,
    GetPolicyResponseTypeDef,
    GetPolicyVersionRequestTypeDef,
    GetPolicyVersionResponseTypeDef,
    GetRolePolicyRequestTypeDef,
    GetRolePolicyResponseTypeDef,
    GetRoleRequestTypeDef,
    GetRoleResponseTypeDef,
    GetSAMLProviderRequestTypeDef,
    GetSAMLProviderResponseTypeDef,
    GetServerCertificateRequestTypeDef,
    GetServerCertificateResponseTypeDef,
    GetServiceLastAccessedDetailsRequestTypeDef,
    GetServiceLastAccessedDetailsResponseTypeDef,
    GetServiceLastAccessedDetailsWithEntitiesRequestTypeDef,
    GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef,
    GetServiceLinkedRoleDeletionStatusRequestTypeDef,
    GetServiceLinkedRoleDeletionStatusResponseTypeDef,
    GetSSHPublicKeyRequestTypeDef,
    GetSSHPublicKeyResponseTypeDef,
    GetUserPolicyRequestTypeDef,
    GetUserPolicyResponseTypeDef,
    GetUserRequestTypeDef,
    GetUserResponseTypeDef,
    ListAccessKeysRequestTypeDef,
    ListAccessKeysResponseTypeDef,
    ListAccountAliasesRequestTypeDef,
    ListAccountAliasesResponseTypeDef,
    ListAttachedGroupPoliciesRequestTypeDef,
    ListAttachedGroupPoliciesResponseTypeDef,
    ListAttachedRolePoliciesRequestTypeDef,
    ListAttachedRolePoliciesResponseTypeDef,
    ListAttachedUserPoliciesRequestTypeDef,
    ListAttachedUserPoliciesResponseTypeDef,
    ListEntitiesForPolicyRequestTypeDef,
    ListEntitiesForPolicyResponseTypeDef,
    ListGroupPoliciesRequestTypeDef,
    ListGroupPoliciesResponseTypeDef,
    ListGroupsForUserRequestTypeDef,
    ListGroupsForUserResponseTypeDef,
    ListGroupsRequestTypeDef,
    ListGroupsResponseTypeDef,
    ListInstanceProfilesForRoleRequestTypeDef,
    ListInstanceProfilesForRoleResponseTypeDef,
    ListInstanceProfilesRequestTypeDef,
    ListInstanceProfilesResponseTypeDef,
    ListInstanceProfileTagsRequestTypeDef,
    ListInstanceProfileTagsResponseTypeDef,
    ListMFADevicesRequestTypeDef,
    ListMFADevicesResponseTypeDef,
    ListMFADeviceTagsRequestTypeDef,
    ListMFADeviceTagsResponseTypeDef,
    ListOpenIDConnectProvidersResponseTypeDef,
    ListOpenIDConnectProviderTagsRequestTypeDef,
    ListOpenIDConnectProviderTagsResponseTypeDef,
    ListOrganizationsFeaturesResponseTypeDef,
    ListPoliciesGrantingServiceAccessRequestTypeDef,
    ListPoliciesGrantingServiceAccessResponseTypeDef,
    ListPoliciesRequestTypeDef,
    ListPoliciesResponseTypeDef,
    ListPolicyTagsRequestTypeDef,
    ListPolicyTagsResponseTypeDef,
    ListPolicyVersionsRequestTypeDef,
    ListPolicyVersionsResponseTypeDef,
    ListRolePoliciesRequestTypeDef,
    ListRolePoliciesResponseTypeDef,
    ListRolesRequestTypeDef,
    ListRolesResponseTypeDef,
    ListRoleTagsRequestTypeDef,
    ListRoleTagsResponseTypeDef,
    ListSAMLProvidersResponseTypeDef,
    ListSAMLProviderTagsRequestTypeDef,
    ListSAMLProviderTagsResponseTypeDef,
    ListServerCertificatesRequestTypeDef,
    ListServerCertificatesResponseTypeDef,
    ListServerCertificateTagsRequestTypeDef,
    ListServerCertificateTagsResponseTypeDef,
    ListServiceSpecificCredentialsRequestTypeDef,
    ListServiceSpecificCredentialsResponseTypeDef,
    ListSigningCertificatesRequestTypeDef,
    ListSigningCertificatesResponseTypeDef,
    ListSSHPublicKeysRequestTypeDef,
    ListSSHPublicKeysResponseTypeDef,
    ListUserPoliciesRequestTypeDef,
    ListUserPoliciesResponseTypeDef,
    ListUsersRequestTypeDef,
    ListUsersResponseTypeDef,
    ListUserTagsRequestTypeDef,
    ListUserTagsResponseTypeDef,
    ListVirtualMFADevicesRequestTypeDef,
    ListVirtualMFADevicesResponseTypeDef,
    PutGroupPolicyRequestTypeDef,
    PutRolePermissionsBoundaryRequestTypeDef,
    PutRolePolicyRequestTypeDef,
    PutUserPermissionsBoundaryRequestTypeDef,
    PutUserPolicyRequestTypeDef,
    RemoveClientIDFromOpenIDConnectProviderRequestTypeDef,
    RemoveRoleFromInstanceProfileRequestTypeDef,
    RemoveUserFromGroupRequestTypeDef,
    ResetServiceSpecificCredentialRequestTypeDef,
    ResetServiceSpecificCredentialResponseTypeDef,
    ResyncMFADeviceRequestTypeDef,
    SetDefaultPolicyVersionRequestTypeDef,
    SetSecurityTokenServicePreferencesRequestTypeDef,
    SimulateCustomPolicyRequestTypeDef,
    SimulatePolicyResponseTypeDef,
    SimulatePrincipalPolicyRequestTypeDef,
    TagInstanceProfileRequestTypeDef,
    TagMFADeviceRequestTypeDef,
    TagOpenIDConnectProviderRequestTypeDef,
    TagPolicyRequestTypeDef,
    TagRoleRequestTypeDef,
    TagSAMLProviderRequestTypeDef,
    TagServerCertificateRequestTypeDef,
    TagUserRequestTypeDef,
    UntagInstanceProfileRequestTypeDef,
    UntagMFADeviceRequestTypeDef,
    UntagOpenIDConnectProviderRequestTypeDef,
    UntagPolicyRequestTypeDef,
    UntagRoleRequestTypeDef,
    UntagSAMLProviderRequestTypeDef,
    UntagServerCertificateRequestTypeDef,
    UntagUserRequestTypeDef,
    UpdateAccessKeyRequestTypeDef,
    UpdateAccountPasswordPolicyRequestTypeDef,
    UpdateAssumeRolePolicyRequestTypeDef,
    UpdateGroupRequestTypeDef,
    UpdateLoginProfileRequestTypeDef,
    UpdateOpenIDConnectProviderThumbprintRequestTypeDef,
    UpdateRoleDescriptionRequestTypeDef,
    UpdateRoleDescriptionResponseTypeDef,
    UpdateRoleRequestTypeDef,
    UpdateSAMLProviderRequestTypeDef,
    UpdateSAMLProviderResponseTypeDef,
    UpdateServerCertificateRequestTypeDef,
    UpdateServiceSpecificCredentialRequestTypeDef,
    UpdateSigningCertificateRequestTypeDef,
    UpdateSSHPublicKeyRequestTypeDef,
    UpdateUserRequestTypeDef,
    UploadServerCertificateRequestTypeDef,
    UploadServerCertificateResponseTypeDef,
    UploadSigningCertificateRequestTypeDef,
    UploadSigningCertificateResponseTypeDef,
    UploadSSHPublicKeyRequestTypeDef,
    UploadSSHPublicKeyResponseTypeDef,
)
from .waiter import (
    InstanceProfileExistsWaiter,
    PolicyExistsWaiter,
    RoleExistsWaiter,
    UserExistsWaiter,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("IAMClient",)

class Exceptions(BaseClientExceptions):
    AccountNotManagementOrDelegatedAdministratorException: Type[BotocoreClientError]
    CallerIsNotManagementAccountException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    CredentialReportExpiredException: Type[BotocoreClientError]
    CredentialReportNotPresentException: Type[BotocoreClientError]
    CredentialReportNotReadyException: Type[BotocoreClientError]
    DeleteConflictException: Type[BotocoreClientError]
    DuplicateCertificateException: Type[BotocoreClientError]
    DuplicateSSHPublicKeyException: Type[BotocoreClientError]
    EntityAlreadyExistsException: Type[BotocoreClientError]
    EntityTemporarilyUnmodifiableException: Type[BotocoreClientError]
    InvalidAuthenticationCodeException: Type[BotocoreClientError]
    InvalidCertificateException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    InvalidPublicKeyException: Type[BotocoreClientError]
    InvalidUserTypeException: Type[BotocoreClientError]
    KeyPairMismatchException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MalformedCertificateException: Type[BotocoreClientError]
    MalformedPolicyDocumentException: Type[BotocoreClientError]
    NoSuchEntityException: Type[BotocoreClientError]
    OpenIdIdpCommunicationErrorException: Type[BotocoreClientError]
    OrganizationNotFoundException: Type[BotocoreClientError]
    OrganizationNotInAllFeaturesModeException: Type[BotocoreClientError]
    PasswordPolicyViolationException: Type[BotocoreClientError]
    PolicyEvaluationException: Type[BotocoreClientError]
    PolicyNotAttachableException: Type[BotocoreClientError]
    ReportGenerationLimitExceededException: Type[BotocoreClientError]
    ServiceAccessNotEnabledException: Type[BotocoreClientError]
    ServiceFailureException: Type[BotocoreClientError]
    ServiceNotSupportedException: Type[BotocoreClientError]
    UnmodifiableEntityException: Type[BotocoreClientError]
    UnrecognizedPublicKeyEncodingException: Type[BotocoreClientError]

class IAMClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IAMClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#generate_presigned_url)
        """

    def add_client_id_to_open_id_connect_provider(
        self, **kwargs: Unpack[AddClientIDToOpenIDConnectProviderRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds a new client ID (also known as audience) to the list of client IDs already
        registered for the specified IAM OpenID Connect (OIDC) provider resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/add_client_id_to_open_id_connect_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#add_client_id_to_open_id_connect_provider)
        """

    def add_role_to_instance_profile(
        self, **kwargs: Unpack[AddRoleToInstanceProfileRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds the specified IAM role to the specified instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/add_role_to_instance_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#add_role_to_instance_profile)
        """

    def add_user_to_group(
        self, **kwargs: Unpack[AddUserToGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds the specified user to the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/add_user_to_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#add_user_to_group)
        """

    def attach_group_policy(
        self, **kwargs: Unpack[AttachGroupPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Attaches the specified managed policy to the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/attach_group_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#attach_group_policy)
        """

    def attach_role_policy(
        self, **kwargs: Unpack[AttachRolePolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Attaches the specified managed policy to the specified IAM role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/attach_role_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#attach_role_policy)
        """

    def attach_user_policy(
        self, **kwargs: Unpack[AttachUserPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Attaches the specified managed policy to the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/attach_user_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#attach_user_policy)
        """

    def change_password(
        self, **kwargs: Unpack[ChangePasswordRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Changes the password of the IAM user who is calling this operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/change_password.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#change_password)
        """

    def create_access_key(
        self, **kwargs: Unpack[CreateAccessKeyRequestTypeDef]
    ) -> CreateAccessKeyResponseTypeDef:
        """
        Creates a new Amazon Web Services secret access key and corresponding Amazon
        Web Services access key ID for the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/create_access_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#create_access_key)
        """

    def create_account_alias(
        self, **kwargs: Unpack[CreateAccountAliasRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates an alias for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/create_account_alias.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#create_account_alias)
        """

    def create_group(
        self, **kwargs: Unpack[CreateGroupRequestTypeDef]
    ) -> CreateGroupResponseTypeDef:
        """
        Creates a new group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/create_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#create_group)
        """

    def create_instance_profile(
        self, **kwargs: Unpack[CreateInstanceProfileRequestTypeDef]
    ) -> CreateInstanceProfileResponseTypeDef:
        """
        Creates a new instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/create_instance_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#create_instance_profile)
        """

    def create_login_profile(
        self, **kwargs: Unpack[CreateLoginProfileRequestTypeDef]
    ) -> CreateLoginProfileResponseTypeDef:
        """
        Creates a password for the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/create_login_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#create_login_profile)
        """

    def create_open_id_connect_provider(
        self, **kwargs: Unpack[CreateOpenIDConnectProviderRequestTypeDef]
    ) -> CreateOpenIDConnectProviderResponseTypeDef:
        """
        Creates an IAM entity to describe an identity provider (IdP) that supports <a
        href="http://openid.net/connect/">OpenID Connect (OIDC)</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/create_open_id_connect_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#create_open_id_connect_provider)
        """

    def create_policy(
        self, **kwargs: Unpack[CreatePolicyRequestTypeDef]
    ) -> CreatePolicyResponseTypeDef:
        """
        Creates a new managed policy for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/create_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#create_policy)
        """

    def create_policy_version(
        self, **kwargs: Unpack[CreatePolicyVersionRequestTypeDef]
    ) -> CreatePolicyVersionResponseTypeDef:
        """
        Creates a new version of the specified managed policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/create_policy_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#create_policy_version)
        """

    def create_role(self, **kwargs: Unpack[CreateRoleRequestTypeDef]) -> CreateRoleResponseTypeDef:
        """
        Creates a new role for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/create_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#create_role)
        """

    def create_saml_provider(
        self, **kwargs: Unpack[CreateSAMLProviderRequestTypeDef]
    ) -> CreateSAMLProviderResponseTypeDef:
        """
        Creates an IAM resource that describes an identity provider (IdP) that supports
        SAML 2.0.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/create_saml_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#create_saml_provider)
        """

    def create_service_linked_role(
        self, **kwargs: Unpack[CreateServiceLinkedRoleRequestTypeDef]
    ) -> CreateServiceLinkedRoleResponseTypeDef:
        """
        Creates an IAM role that is linked to a specific Amazon Web Services service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/create_service_linked_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#create_service_linked_role)
        """

    def create_service_specific_credential(
        self, **kwargs: Unpack[CreateServiceSpecificCredentialRequestTypeDef]
    ) -> CreateServiceSpecificCredentialResponseTypeDef:
        """
        Generates a set of credentials consisting of a user name and password that can
        be used to access the service specified in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/create_service_specific_credential.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#create_service_specific_credential)
        """

    def create_user(self, **kwargs: Unpack[CreateUserRequestTypeDef]) -> CreateUserResponseTypeDef:
        """
        Creates a new IAM user for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/create_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#create_user)
        """

    def create_virtual_mfa_device(
        self, **kwargs: Unpack[CreateVirtualMFADeviceRequestTypeDef]
    ) -> CreateVirtualMFADeviceResponseTypeDef:
        """
        Creates a new virtual MFA device for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/create_virtual_mfa_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#create_virtual_mfa_device)
        """

    def deactivate_mfa_device(
        self, **kwargs: Unpack[DeactivateMFADeviceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deactivates the specified MFA device and removes it from association with the
        user name for which it was originally enabled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/deactivate_mfa_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#deactivate_mfa_device)
        """

    def delete_access_key(
        self, **kwargs: Unpack[DeleteAccessKeyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the access key pair associated with the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_access_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_access_key)
        """

    def delete_account_alias(
        self, **kwargs: Unpack[DeleteAccountAliasRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified Amazon Web Services account alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_account_alias.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_account_alias)
        """

    def delete_account_password_policy(self) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the password policy for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_account_password_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_account_password_policy)
        """

    def delete_group(
        self, **kwargs: Unpack[DeleteGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_group)
        """

    def delete_group_policy(
        self, **kwargs: Unpack[DeleteGroupPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified inline policy that is embedded in the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_group_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_group_policy)
        """

    def delete_instance_profile(
        self, **kwargs: Unpack[DeleteInstanceProfileRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_instance_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_instance_profile)
        """

    def delete_login_profile(
        self, **kwargs: Unpack[DeleteLoginProfileRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the password for the specified IAM user, For more information, see <a
        href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.html">Managing
        passwords for IAM users</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_login_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_login_profile)
        """

    def delete_open_id_connect_provider(
        self, **kwargs: Unpack[DeleteOpenIDConnectProviderRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an OpenID Connect identity provider (IdP) resource object in IAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_open_id_connect_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_open_id_connect_provider)
        """

    def delete_policy(
        self, **kwargs: Unpack[DeletePolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified managed policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_policy)
        """

    def delete_policy_version(
        self, **kwargs: Unpack[DeletePolicyVersionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified version from the specified managed policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_policy_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_policy_version)
        """

    def delete_role(
        self, **kwargs: Unpack[DeleteRoleRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_role)
        """

    def delete_role_permissions_boundary(
        self, **kwargs: Unpack[DeleteRolePermissionsBoundaryRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the permissions boundary for the specified IAM role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_role_permissions_boundary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_role_permissions_boundary)
        """

    def delete_role_policy(
        self, **kwargs: Unpack[DeleteRolePolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified inline policy that is embedded in the specified IAM role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_role_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_role_policy)
        """

    def delete_saml_provider(
        self, **kwargs: Unpack[DeleteSAMLProviderRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a SAML provider resource in IAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_saml_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_saml_provider)
        """

    def delete_ssh_public_key(
        self, **kwargs: Unpack[DeleteSSHPublicKeyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified SSH public key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_ssh_public_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_ssh_public_key)
        """

    def delete_server_certificate(
        self, **kwargs: Unpack[DeleteServerCertificateRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified server certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_server_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_server_certificate)
        """

    def delete_service_linked_role(
        self, **kwargs: Unpack[DeleteServiceLinkedRoleRequestTypeDef]
    ) -> DeleteServiceLinkedRoleResponseTypeDef:
        """
        Submits a service-linked role deletion request and returns a
        <code>DeletionTaskId</code>, which you can use to check the status of the
        deletion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_service_linked_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_service_linked_role)
        """

    def delete_service_specific_credential(
        self, **kwargs: Unpack[DeleteServiceSpecificCredentialRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified service-specific credential.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_service_specific_credential.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_service_specific_credential)
        """

    def delete_signing_certificate(
        self, **kwargs: Unpack[DeleteSigningCertificateRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a signing certificate associated with the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_signing_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_signing_certificate)
        """

    def delete_user(
        self, **kwargs: Unpack[DeleteUserRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_user)
        """

    def delete_user_permissions_boundary(
        self, **kwargs: Unpack[DeleteUserPermissionsBoundaryRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the permissions boundary for the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_user_permissions_boundary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_user_permissions_boundary)
        """

    def delete_user_policy(
        self, **kwargs: Unpack[DeleteUserPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified inline policy that is embedded in the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_user_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_user_policy)
        """

    def delete_virtual_mfa_device(
        self, **kwargs: Unpack[DeleteVirtualMFADeviceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a virtual MFA device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/delete_virtual_mfa_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#delete_virtual_mfa_device)
        """

    def detach_group_policy(
        self, **kwargs: Unpack[DetachGroupPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified managed policy from the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/detach_group_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#detach_group_policy)
        """

    def detach_role_policy(
        self, **kwargs: Unpack[DetachRolePolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified managed policy from the specified role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/detach_role_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#detach_role_policy)
        """

    def detach_user_policy(
        self, **kwargs: Unpack[DetachUserPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified managed policy from the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/detach_user_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#detach_user_policy)
        """

    def disable_organizations_root_credentials_management(
        self,
    ) -> DisableOrganizationsRootCredentialsManagementResponseTypeDef:
        """
        Disables the management of privileged root user credentials across member
        accounts in your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/disable_organizations_root_credentials_management.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#disable_organizations_root_credentials_management)
        """

    def disable_organizations_root_sessions(
        self,
    ) -> DisableOrganizationsRootSessionsResponseTypeDef:
        """
        Disables root user sessions for privileged tasks across member accounts in your
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/disable_organizations_root_sessions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#disable_organizations_root_sessions)
        """

    def enable_mfa_device(
        self, **kwargs: Unpack[EnableMFADeviceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Enables the specified MFA device and associates it with the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/enable_mfa_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#enable_mfa_device)
        """

    def enable_organizations_root_credentials_management(
        self,
    ) -> EnableOrganizationsRootCredentialsManagementResponseTypeDef:
        """
        Enables the management of privileged root user credentials across member
        accounts in your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/enable_organizations_root_credentials_management.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#enable_organizations_root_credentials_management)
        """

    def enable_organizations_root_sessions(self) -> EnableOrganizationsRootSessionsResponseTypeDef:
        """
        Allows the management account or delegated administrator to perform privileged
        tasks on member accounts in your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/enable_organizations_root_sessions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#enable_organizations_root_sessions)
        """

    def generate_credential_report(self) -> GenerateCredentialReportResponseTypeDef:
        """
        Generates a credential report for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/generate_credential_report.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#generate_credential_report)
        """

    def generate_organizations_access_report(
        self, **kwargs: Unpack[GenerateOrganizationsAccessReportRequestTypeDef]
    ) -> GenerateOrganizationsAccessReportResponseTypeDef:
        """
        Generates a report for service last accessed data for Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/generate_organizations_access_report.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#generate_organizations_access_report)
        """

    def generate_service_last_accessed_details(
        self, **kwargs: Unpack[GenerateServiceLastAccessedDetailsRequestTypeDef]
    ) -> GenerateServiceLastAccessedDetailsResponseTypeDef:
        """
        Generates a report that includes details about when an IAM resource (user,
        group, role, or policy) was last used in an attempt to access Amazon Web
        Services services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/generate_service_last_accessed_details.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#generate_service_last_accessed_details)
        """

    def get_access_key_last_used(
        self, **kwargs: Unpack[GetAccessKeyLastUsedRequestTypeDef]
    ) -> GetAccessKeyLastUsedResponseTypeDef:
        """
        Retrieves information about when the specified access key was last used.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_access_key_last_used.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_access_key_last_used)
        """

    def get_account_authorization_details(
        self, **kwargs: Unpack[GetAccountAuthorizationDetailsRequestTypeDef]
    ) -> GetAccountAuthorizationDetailsResponseTypeDef:
        """
        Retrieves information about all IAM users, groups, roles, and policies in your
        Amazon Web Services account, including their relationships to one another.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_account_authorization_details.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_account_authorization_details)
        """

    def get_account_password_policy(self) -> GetAccountPasswordPolicyResponseTypeDef:
        """
        Retrieves the password policy for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_account_password_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_account_password_policy)
        """

    def get_account_summary(self) -> GetAccountSummaryResponseTypeDef:
        """
        Retrieves information about IAM entity usage and IAM quotas in the Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_account_summary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_account_summary)
        """

    def get_context_keys_for_custom_policy(
        self, **kwargs: Unpack[GetContextKeysForCustomPolicyRequestTypeDef]
    ) -> GetContextKeysForPolicyResponseTypeDef:
        """
        Gets a list of all of the context keys referenced in the input policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_context_keys_for_custom_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_context_keys_for_custom_policy)
        """

    def get_context_keys_for_principal_policy(
        self, **kwargs: Unpack[GetContextKeysForPrincipalPolicyRequestTypeDef]
    ) -> GetContextKeysForPolicyResponseTypeDef:
        """
        Gets a list of all of the context keys referenced in all the IAM policies that
        are attached to the specified IAM entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_context_keys_for_principal_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_context_keys_for_principal_policy)
        """

    def get_credential_report(self) -> GetCredentialReportResponseTypeDef:
        """
        Retrieves a credential report for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_credential_report.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_credential_report)
        """

    def get_group(self, **kwargs: Unpack[GetGroupRequestTypeDef]) -> GetGroupResponseTypeDef:
        """
        Returns a list of IAM users that are in the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_group)
        """

    def get_group_policy(
        self, **kwargs: Unpack[GetGroupPolicyRequestTypeDef]
    ) -> GetGroupPolicyResponseTypeDef:
        """
        Retrieves the specified inline policy document that is embedded in the
        specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_group_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_group_policy)
        """

    def get_instance_profile(
        self, **kwargs: Unpack[GetInstanceProfileRequestTypeDef]
    ) -> GetInstanceProfileResponseTypeDef:
        """
        Retrieves information about the specified instance profile, including the
        instance profile's path, GUID, ARN, and role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_instance_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_instance_profile)
        """

    def get_login_profile(
        self, **kwargs: Unpack[GetLoginProfileRequestTypeDef]
    ) -> GetLoginProfileResponseTypeDef:
        """
        Retrieves the user name for the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_login_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_login_profile)
        """

    def get_mfa_device(
        self, **kwargs: Unpack[GetMFADeviceRequestTypeDef]
    ) -> GetMFADeviceResponseTypeDef:
        """
        Retrieves information about an MFA device for a specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_mfa_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_mfa_device)
        """

    def get_open_id_connect_provider(
        self, **kwargs: Unpack[GetOpenIDConnectProviderRequestTypeDef]
    ) -> GetOpenIDConnectProviderResponseTypeDef:
        """
        Returns information about the specified OpenID Connect (OIDC) provider resource
        object in IAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_open_id_connect_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_open_id_connect_provider)
        """

    def get_organizations_access_report(
        self, **kwargs: Unpack[GetOrganizationsAccessReportRequestTypeDef]
    ) -> GetOrganizationsAccessReportResponseTypeDef:
        """
        Retrieves the service last accessed data report for Organizations that was
        previously generated using the <code> <a>GenerateOrganizationsAccessReport</a>
        </code> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_organizations_access_report.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_organizations_access_report)
        """

    def get_policy(self, **kwargs: Unpack[GetPolicyRequestTypeDef]) -> GetPolicyResponseTypeDef:
        """
        Retrieves information about the specified managed policy, including the
        policy's default version and the total number of IAM users, groups, and roles
        to which the policy is attached.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_policy)
        """

    def get_policy_version(
        self, **kwargs: Unpack[GetPolicyVersionRequestTypeDef]
    ) -> GetPolicyVersionResponseTypeDef:
        """
        Retrieves information about the specified version of the specified managed
        policy, including the policy document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_policy_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_policy_version)
        """

    def get_role(self, **kwargs: Unpack[GetRoleRequestTypeDef]) -> GetRoleResponseTypeDef:
        """
        Retrieves information about the specified role, including the role's path,
        GUID, ARN, and the role's trust policy that grants permission to assume the
        role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_role)
        """

    def get_role_policy(
        self, **kwargs: Unpack[GetRolePolicyRequestTypeDef]
    ) -> GetRolePolicyResponseTypeDef:
        """
        Retrieves the specified inline policy document that is embedded with the
        specified IAM role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_role_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_role_policy)
        """

    def get_saml_provider(
        self, **kwargs: Unpack[GetSAMLProviderRequestTypeDef]
    ) -> GetSAMLProviderResponseTypeDef:
        """
        Returns the SAML provider metadocument that was uploaded when the IAM SAML
        provider resource object was created or updated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_saml_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_saml_provider)
        """

    def get_ssh_public_key(
        self, **kwargs: Unpack[GetSSHPublicKeyRequestTypeDef]
    ) -> GetSSHPublicKeyResponseTypeDef:
        """
        Retrieves the specified SSH public key, including metadata about the key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_ssh_public_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_ssh_public_key)
        """

    def get_server_certificate(
        self, **kwargs: Unpack[GetServerCertificateRequestTypeDef]
    ) -> GetServerCertificateResponseTypeDef:
        """
        Retrieves information about the specified server certificate stored in IAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_server_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_server_certificate)
        """

    def get_service_last_accessed_details(
        self, **kwargs: Unpack[GetServiceLastAccessedDetailsRequestTypeDef]
    ) -> GetServiceLastAccessedDetailsResponseTypeDef:
        """
        Retrieves a service last accessed report that was created using the
        <code>GenerateServiceLastAccessedDetails</code> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_service_last_accessed_details.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_service_last_accessed_details)
        """

    def get_service_last_accessed_details_with_entities(
        self, **kwargs: Unpack[GetServiceLastAccessedDetailsWithEntitiesRequestTypeDef]
    ) -> GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef:
        """
        After you generate a group or policy report using the
        <code>GenerateServiceLastAccessedDetails</code> operation, you can use the
        <code>JobId</code> parameter in
        <code>GetServiceLastAccessedDetailsWithEntities</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_service_last_accessed_details_with_entities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_service_last_accessed_details_with_entities)
        """

    def get_service_linked_role_deletion_status(
        self, **kwargs: Unpack[GetServiceLinkedRoleDeletionStatusRequestTypeDef]
    ) -> GetServiceLinkedRoleDeletionStatusResponseTypeDef:
        """
        Retrieves the status of your service-linked role deletion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_service_linked_role_deletion_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_service_linked_role_deletion_status)
        """

    def get_user(self, **kwargs: Unpack[GetUserRequestTypeDef]) -> GetUserResponseTypeDef:
        """
        Retrieves information about the specified IAM user, including the user's
        creation date, path, unique ID, and ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_user)
        """

    def get_user_policy(
        self, **kwargs: Unpack[GetUserPolicyRequestTypeDef]
    ) -> GetUserPolicyResponseTypeDef:
        """
        Retrieves the specified inline policy document that is embedded in the
        specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_user_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_user_policy)
        """

    def list_access_keys(
        self, **kwargs: Unpack[ListAccessKeysRequestTypeDef]
    ) -> ListAccessKeysResponseTypeDef:
        """
        Returns information about the access key IDs associated with the specified IAM
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_access_keys.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_access_keys)
        """

    def list_account_aliases(
        self, **kwargs: Unpack[ListAccountAliasesRequestTypeDef]
    ) -> ListAccountAliasesResponseTypeDef:
        """
        Lists the account alias associated with the Amazon Web Services account (Note:
        you can have only one).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_account_aliases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_account_aliases)
        """

    def list_attached_group_policies(
        self, **kwargs: Unpack[ListAttachedGroupPoliciesRequestTypeDef]
    ) -> ListAttachedGroupPoliciesResponseTypeDef:
        """
        Lists all managed policies that are attached to the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_attached_group_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_attached_group_policies)
        """

    def list_attached_role_policies(
        self, **kwargs: Unpack[ListAttachedRolePoliciesRequestTypeDef]
    ) -> ListAttachedRolePoliciesResponseTypeDef:
        """
        Lists all managed policies that are attached to the specified IAM role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_attached_role_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_attached_role_policies)
        """

    def list_attached_user_policies(
        self, **kwargs: Unpack[ListAttachedUserPoliciesRequestTypeDef]
    ) -> ListAttachedUserPoliciesResponseTypeDef:
        """
        Lists all managed policies that are attached to the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_attached_user_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_attached_user_policies)
        """

    def list_entities_for_policy(
        self, **kwargs: Unpack[ListEntitiesForPolicyRequestTypeDef]
    ) -> ListEntitiesForPolicyResponseTypeDef:
        """
        Lists all IAM users, groups, and roles that the specified managed policy is
        attached to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_entities_for_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_entities_for_policy)
        """

    def list_group_policies(
        self, **kwargs: Unpack[ListGroupPoliciesRequestTypeDef]
    ) -> ListGroupPoliciesResponseTypeDef:
        """
        Lists the names of the inline policies that are embedded in the specified IAM
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_group_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_group_policies)
        """

    def list_groups(self, **kwargs: Unpack[ListGroupsRequestTypeDef]) -> ListGroupsResponseTypeDef:
        """
        Lists the IAM groups that have the specified path prefix.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_groups)
        """

    def list_groups_for_user(
        self, **kwargs: Unpack[ListGroupsForUserRequestTypeDef]
    ) -> ListGroupsForUserResponseTypeDef:
        """
        Lists the IAM groups that the specified IAM user belongs to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_groups_for_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_groups_for_user)
        """

    def list_instance_profile_tags(
        self, **kwargs: Unpack[ListInstanceProfileTagsRequestTypeDef]
    ) -> ListInstanceProfileTagsResponseTypeDef:
        """
        Lists the tags that are attached to the specified IAM instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_instance_profile_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_instance_profile_tags)
        """

    def list_instance_profiles(
        self, **kwargs: Unpack[ListInstanceProfilesRequestTypeDef]
    ) -> ListInstanceProfilesResponseTypeDef:
        """
        Lists the instance profiles that have the specified path prefix.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_instance_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_instance_profiles)
        """

    def list_instance_profiles_for_role(
        self, **kwargs: Unpack[ListInstanceProfilesForRoleRequestTypeDef]
    ) -> ListInstanceProfilesForRoleResponseTypeDef:
        """
        Lists the instance profiles that have the specified associated IAM role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_instance_profiles_for_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_instance_profiles_for_role)
        """

    def list_mfa_device_tags(
        self, **kwargs: Unpack[ListMFADeviceTagsRequestTypeDef]
    ) -> ListMFADeviceTagsResponseTypeDef:
        """
        Lists the tags that are attached to the specified IAM virtual multi-factor
        authentication (MFA) device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_mfa_device_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_mfa_device_tags)
        """

    def list_mfa_devices(
        self, **kwargs: Unpack[ListMFADevicesRequestTypeDef]
    ) -> ListMFADevicesResponseTypeDef:
        """
        Lists the MFA devices for an IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_mfa_devices.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_mfa_devices)
        """

    def list_open_id_connect_provider_tags(
        self, **kwargs: Unpack[ListOpenIDConnectProviderTagsRequestTypeDef]
    ) -> ListOpenIDConnectProviderTagsResponseTypeDef:
        """
        Lists the tags that are attached to the specified OpenID Connect
        (OIDC)-compatible identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_open_id_connect_provider_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_open_id_connect_provider_tags)
        """

    def list_open_id_connect_providers(self) -> ListOpenIDConnectProvidersResponseTypeDef:
        """
        Lists information about the IAM OpenID Connect (OIDC) provider resource objects
        defined in the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_open_id_connect_providers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_open_id_connect_providers)
        """

    def list_organizations_features(self) -> ListOrganizationsFeaturesResponseTypeDef:
        """
        Lists the centralized root access features enabled for your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_organizations_features.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_organizations_features)
        """

    def list_policies(
        self, **kwargs: Unpack[ListPoliciesRequestTypeDef]
    ) -> ListPoliciesResponseTypeDef:
        """
        Lists all the managed policies that are available in your Amazon Web Services
        account, including your own customer-defined managed policies and all Amazon
        Web Services managed policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_policies)
        """

    def list_policies_granting_service_access(
        self, **kwargs: Unpack[ListPoliciesGrantingServiceAccessRequestTypeDef]
    ) -> ListPoliciesGrantingServiceAccessResponseTypeDef:
        """
        Retrieves a list of policies that the IAM identity (user, group, or role) can
        use to access each specified service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_policies_granting_service_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_policies_granting_service_access)
        """

    def list_policy_tags(
        self, **kwargs: Unpack[ListPolicyTagsRequestTypeDef]
    ) -> ListPolicyTagsResponseTypeDef:
        """
        Lists the tags that are attached to the specified IAM customer managed policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_policy_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_policy_tags)
        """

    def list_policy_versions(
        self, **kwargs: Unpack[ListPolicyVersionsRequestTypeDef]
    ) -> ListPolicyVersionsResponseTypeDef:
        """
        Lists information about the versions of the specified managed policy, including
        the version that is currently set as the policy's default version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_policy_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_policy_versions)
        """

    def list_role_policies(
        self, **kwargs: Unpack[ListRolePoliciesRequestTypeDef]
    ) -> ListRolePoliciesResponseTypeDef:
        """
        Lists the names of the inline policies that are embedded in the specified IAM
        role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_role_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_role_policies)
        """

    def list_role_tags(
        self, **kwargs: Unpack[ListRoleTagsRequestTypeDef]
    ) -> ListRoleTagsResponseTypeDef:
        """
        Lists the tags that are attached to the specified role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_role_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_role_tags)
        """

    def list_roles(self, **kwargs: Unpack[ListRolesRequestTypeDef]) -> ListRolesResponseTypeDef:
        """
        Lists the IAM roles that have the specified path prefix.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_roles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_roles)
        """

    def list_saml_provider_tags(
        self, **kwargs: Unpack[ListSAMLProviderTagsRequestTypeDef]
    ) -> ListSAMLProviderTagsResponseTypeDef:
        """
        Lists the tags that are attached to the specified Security Assertion Markup
        Language (SAML) identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_saml_provider_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_saml_provider_tags)
        """

    def list_saml_providers(self) -> ListSAMLProvidersResponseTypeDef:
        """
        Lists the SAML provider resource objects defined in IAM in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_saml_providers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_saml_providers)
        """

    def list_ssh_public_keys(
        self, **kwargs: Unpack[ListSSHPublicKeysRequestTypeDef]
    ) -> ListSSHPublicKeysResponseTypeDef:
        """
        Returns information about the SSH public keys associated with the specified IAM
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_ssh_public_keys.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_ssh_public_keys)
        """

    def list_server_certificate_tags(
        self, **kwargs: Unpack[ListServerCertificateTagsRequestTypeDef]
    ) -> ListServerCertificateTagsResponseTypeDef:
        """
        Lists the tags that are attached to the specified IAM server certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_server_certificate_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_server_certificate_tags)
        """

    def list_server_certificates(
        self, **kwargs: Unpack[ListServerCertificatesRequestTypeDef]
    ) -> ListServerCertificatesResponseTypeDef:
        """
        Lists the server certificates stored in IAM that have the specified path prefix.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_server_certificates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_server_certificates)
        """

    def list_service_specific_credentials(
        self, **kwargs: Unpack[ListServiceSpecificCredentialsRequestTypeDef]
    ) -> ListServiceSpecificCredentialsResponseTypeDef:
        """
        Returns information about the service-specific credentials associated with the
        specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_service_specific_credentials.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_service_specific_credentials)
        """

    def list_signing_certificates(
        self, **kwargs: Unpack[ListSigningCertificatesRequestTypeDef]
    ) -> ListSigningCertificatesResponseTypeDef:
        """
        Returns information about the signing certificates associated with the
        specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_signing_certificates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_signing_certificates)
        """

    def list_user_policies(
        self, **kwargs: Unpack[ListUserPoliciesRequestTypeDef]
    ) -> ListUserPoliciesResponseTypeDef:
        """
        Lists the names of the inline policies embedded in the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_user_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_user_policies)
        """

    def list_user_tags(
        self, **kwargs: Unpack[ListUserTagsRequestTypeDef]
    ) -> ListUserTagsResponseTypeDef:
        """
        Lists the tags that are attached to the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_user_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_user_tags)
        """

    def list_users(self, **kwargs: Unpack[ListUsersRequestTypeDef]) -> ListUsersResponseTypeDef:
        """
        Lists the IAM users that have the specified path prefix.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_users.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_users)
        """

    def list_virtual_mfa_devices(
        self, **kwargs: Unpack[ListVirtualMFADevicesRequestTypeDef]
    ) -> ListVirtualMFADevicesResponseTypeDef:
        """
        Lists the virtual MFA devices defined in the Amazon Web Services account by
        assignment status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_virtual_mfa_devices.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#list_virtual_mfa_devices)
        """

    def put_group_policy(
        self, **kwargs: Unpack[PutGroupPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds or updates an inline policy document that is embedded in the specified IAM
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/put_group_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#put_group_policy)
        """

    def put_role_permissions_boundary(
        self, **kwargs: Unpack[PutRolePermissionsBoundaryRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds or updates the policy that is specified as the IAM role's permissions
        boundary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/put_role_permissions_boundary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#put_role_permissions_boundary)
        """

    def put_role_policy(
        self, **kwargs: Unpack[PutRolePolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds or updates an inline policy document that is embedded in the specified IAM
        role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/put_role_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#put_role_policy)
        """

    def put_user_permissions_boundary(
        self, **kwargs: Unpack[PutUserPermissionsBoundaryRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds or updates the policy that is specified as the IAM user's permissions
        boundary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/put_user_permissions_boundary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#put_user_permissions_boundary)
        """

    def put_user_policy(
        self, **kwargs: Unpack[PutUserPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds or updates an inline policy document that is embedded in the specified IAM
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/put_user_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#put_user_policy)
        """

    def remove_client_id_from_open_id_connect_provider(
        self, **kwargs: Unpack[RemoveClientIDFromOpenIDConnectProviderRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified client ID (also known as audience) from the list of
        client IDs registered for the specified IAM OpenID Connect (OIDC) provider
        resource object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/remove_client_id_from_open_id_connect_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#remove_client_id_from_open_id_connect_provider)
        """

    def remove_role_from_instance_profile(
        self, **kwargs: Unpack[RemoveRoleFromInstanceProfileRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified IAM role from the specified Amazon EC2 instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/remove_role_from_instance_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#remove_role_from_instance_profile)
        """

    def remove_user_from_group(
        self, **kwargs: Unpack[RemoveUserFromGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified user from the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/remove_user_from_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#remove_user_from_group)
        """

    def reset_service_specific_credential(
        self, **kwargs: Unpack[ResetServiceSpecificCredentialRequestTypeDef]
    ) -> ResetServiceSpecificCredentialResponseTypeDef:
        """
        Resets the password for a service-specific credential.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/reset_service_specific_credential.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#reset_service_specific_credential)
        """

    def resync_mfa_device(
        self, **kwargs: Unpack[ResyncMFADeviceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Synchronizes the specified MFA device with its IAM resource object on the
        Amazon Web Services servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/resync_mfa_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#resync_mfa_device)
        """

    def set_default_policy_version(
        self, **kwargs: Unpack[SetDefaultPolicyVersionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Sets the specified version of the specified policy as the policy's default
        (operative) version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/set_default_policy_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#set_default_policy_version)
        """

    def set_security_token_service_preferences(
        self, **kwargs: Unpack[SetSecurityTokenServicePreferencesRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Sets the specified version of the global endpoint token as the token version
        used for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/set_security_token_service_preferences.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#set_security_token_service_preferences)
        """

    def simulate_custom_policy(
        self, **kwargs: Unpack[SimulateCustomPolicyRequestTypeDef]
    ) -> SimulatePolicyResponseTypeDef:
        """
        Simulate how a set of IAM policies and optionally a resource-based policy works
        with a list of API operations and Amazon Web Services resources to determine
        the policies' effective permissions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/simulate_custom_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#simulate_custom_policy)
        """

    def simulate_principal_policy(
        self, **kwargs: Unpack[SimulatePrincipalPolicyRequestTypeDef]
    ) -> SimulatePolicyResponseTypeDef:
        """
        Simulate how a set of IAM policies attached to an IAM entity works with a list
        of API operations and Amazon Web Services resources to determine the policies'
        effective permissions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/simulate_principal_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#simulate_principal_policy)
        """

    def tag_instance_profile(
        self, **kwargs: Unpack[TagInstanceProfileRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more tags to an IAM instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/tag_instance_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#tag_instance_profile)
        """

    def tag_mfa_device(
        self, **kwargs: Unpack[TagMFADeviceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more tags to an IAM virtual multi-factor authentication (MFA)
        device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/tag_mfa_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#tag_mfa_device)
        """

    def tag_open_id_connect_provider(
        self, **kwargs: Unpack[TagOpenIDConnectProviderRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more tags to an OpenID Connect (OIDC)-compatible identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/tag_open_id_connect_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#tag_open_id_connect_provider)
        """

    def tag_policy(self, **kwargs: Unpack[TagPolicyRequestTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more tags to an IAM customer managed policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/tag_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#tag_policy)
        """

    def tag_role(self, **kwargs: Unpack[TagRoleRequestTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more tags to an IAM role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/tag_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#tag_role)
        """

    def tag_saml_provider(
        self, **kwargs: Unpack[TagSAMLProviderRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more tags to a Security Assertion Markup Language (SAML) identity
        provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/tag_saml_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#tag_saml_provider)
        """

    def tag_server_certificate(
        self, **kwargs: Unpack[TagServerCertificateRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more tags to an IAM server certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/tag_server_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#tag_server_certificate)
        """

    def tag_user(self, **kwargs: Unpack[TagUserRequestTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more tags to an IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/tag_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#tag_user)
        """

    def untag_instance_profile(
        self, **kwargs: Unpack[UntagInstanceProfileRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified tags from the IAM instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/untag_instance_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#untag_instance_profile)
        """

    def untag_mfa_device(
        self, **kwargs: Unpack[UntagMFADeviceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified tags from the IAM virtual multi-factor authentication
        (MFA) device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/untag_mfa_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#untag_mfa_device)
        """

    def untag_open_id_connect_provider(
        self, **kwargs: Unpack[UntagOpenIDConnectProviderRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified tags from the specified OpenID Connect (OIDC)-compatible
        identity provider in IAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/untag_open_id_connect_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#untag_open_id_connect_provider)
        """

    def untag_policy(
        self, **kwargs: Unpack[UntagPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified tags from the customer managed policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/untag_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#untag_policy)
        """

    def untag_role(self, **kwargs: Unpack[UntagRoleRequestTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified tags from the role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/untag_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#untag_role)
        """

    def untag_saml_provider(
        self, **kwargs: Unpack[UntagSAMLProviderRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified tags from the specified Security Assertion Markup
        Language (SAML) identity provider in IAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/untag_saml_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#untag_saml_provider)
        """

    def untag_server_certificate(
        self, **kwargs: Unpack[UntagServerCertificateRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified tags from the IAM server certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/untag_server_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#untag_server_certificate)
        """

    def untag_user(self, **kwargs: Unpack[UntagUserRequestTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified tags from the user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/untag_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#untag_user)
        """

    def update_access_key(
        self, **kwargs: Unpack[UpdateAccessKeyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Changes the status of the specified access key from Active to Inactive, or vice
        versa.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/update_access_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#update_access_key)
        """

    def update_account_password_policy(
        self, **kwargs: Unpack[UpdateAccountPasswordPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the password policy settings for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/update_account_password_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#update_account_password_policy)
        """

    def update_assume_role_policy(
        self, **kwargs: Unpack[UpdateAssumeRolePolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the policy that grants an IAM entity permission to assume a role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/update_assume_role_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#update_assume_role_policy)
        """

    def update_group(
        self, **kwargs: Unpack[UpdateGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the name and/or the path of the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/update_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#update_group)
        """

    def update_login_profile(
        self, **kwargs: Unpack[UpdateLoginProfileRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Changes the password for the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/update_login_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#update_login_profile)
        """

    def update_open_id_connect_provider_thumbprint(
        self, **kwargs: Unpack[UpdateOpenIDConnectProviderThumbprintRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Replaces the existing list of server certificate thumbprints associated with an
        OpenID Connect (OIDC) provider resource object with a new list of thumbprints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/update_open_id_connect_provider_thumbprint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#update_open_id_connect_provider_thumbprint)
        """

    def update_role(self, **kwargs: Unpack[UpdateRoleRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates the description or maximum session duration setting of a role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/update_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#update_role)
        """

    def update_role_description(
        self, **kwargs: Unpack[UpdateRoleDescriptionRequestTypeDef]
    ) -> UpdateRoleDescriptionResponseTypeDef:
        """
        Use <a>UpdateRole</a> instead.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/update_role_description.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#update_role_description)
        """

    def update_saml_provider(
        self, **kwargs: Unpack[UpdateSAMLProviderRequestTypeDef]
    ) -> UpdateSAMLProviderResponseTypeDef:
        """
        Updates the metadata document, SAML encryption settings, and private keys for
        an existing SAML provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/update_saml_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#update_saml_provider)
        """

    def update_ssh_public_key(
        self, **kwargs: Unpack[UpdateSSHPublicKeyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Sets the status of an IAM user's SSH public key to active or inactive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/update_ssh_public_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#update_ssh_public_key)
        """

    def update_server_certificate(
        self, **kwargs: Unpack[UpdateServerCertificateRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the name and/or the path of the specified server certificate stored in
        IAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/update_server_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#update_server_certificate)
        """

    def update_service_specific_credential(
        self, **kwargs: Unpack[UpdateServiceSpecificCredentialRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Sets the status of a service-specific credential to <code>Active</code> or
        <code>Inactive</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/update_service_specific_credential.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#update_service_specific_credential)
        """

    def update_signing_certificate(
        self, **kwargs: Unpack[UpdateSigningCertificateRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Changes the status of the specified user signing certificate from active to
        disabled, or vice versa.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/update_signing_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#update_signing_certificate)
        """

    def update_user(
        self, **kwargs: Unpack[UpdateUserRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the name and/or the path of the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/update_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#update_user)
        """

    def upload_ssh_public_key(
        self, **kwargs: Unpack[UploadSSHPublicKeyRequestTypeDef]
    ) -> UploadSSHPublicKeyResponseTypeDef:
        """
        Uploads an SSH public key and associates it with the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/upload_ssh_public_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#upload_ssh_public_key)
        """

    def upload_server_certificate(
        self, **kwargs: Unpack[UploadServerCertificateRequestTypeDef]
    ) -> UploadServerCertificateResponseTypeDef:
        """
        Uploads a server certificate entity for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/upload_server_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#upload_server_certificate)
        """

    def upload_signing_certificate(
        self, **kwargs: Unpack[UploadSigningCertificateRequestTypeDef]
    ) -> UploadSigningCertificateResponseTypeDef:
        """
        Uploads an X.509 signing certificate and associates it with the specified IAM
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/upload_signing_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#upload_signing_certificate)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_account_authorization_details"]
    ) -> GetAccountAuthorizationDetailsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_group"]
    ) -> GetGroupPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_access_keys"]
    ) -> ListAccessKeysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_account_aliases"]
    ) -> ListAccountAliasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_attached_group_policies"]
    ) -> ListAttachedGroupPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_attached_role_policies"]
    ) -> ListAttachedRolePoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_attached_user_policies"]
    ) -> ListAttachedUserPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_entities_for_policy"]
    ) -> ListEntitiesForPolicyPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_group_policies"]
    ) -> ListGroupPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_groups_for_user"]
    ) -> ListGroupsForUserPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_groups"]
    ) -> ListGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_instance_profile_tags"]
    ) -> ListInstanceProfileTagsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_instance_profiles_for_role"]
    ) -> ListInstanceProfilesForRolePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_instance_profiles"]
    ) -> ListInstanceProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_mfa_device_tags"]
    ) -> ListMFADeviceTagsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_mfa_devices"]
    ) -> ListMFADevicesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_open_id_connect_provider_tags"]
    ) -> ListOpenIDConnectProviderTagsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_policies"]
    ) -> ListPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_policy_tags"]
    ) -> ListPolicyTagsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_policy_versions"]
    ) -> ListPolicyVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_role_policies"]
    ) -> ListRolePoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_role_tags"]
    ) -> ListRoleTagsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_roles"]
    ) -> ListRolesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_saml_provider_tags"]
    ) -> ListSAMLProviderTagsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_ssh_public_keys"]
    ) -> ListSSHPublicKeysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_server_certificate_tags"]
    ) -> ListServerCertificateTagsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_server_certificates"]
    ) -> ListServerCertificatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_signing_certificates"]
    ) -> ListSigningCertificatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_user_policies"]
    ) -> ListUserPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_user_tags"]
    ) -> ListUserTagsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_users"]
    ) -> ListUsersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_virtual_mfa_devices"]
    ) -> ListVirtualMFADevicesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["simulate_custom_policy"]
    ) -> SimulateCustomPolicyPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["simulate_principal_policy"]
    ) -> SimulatePrincipalPolicyPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["instance_profile_exists"]
    ) -> InstanceProfileExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["policy_exists"]
    ) -> PolicyExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["role_exists"]
    ) -> RoleExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["user_exists"]
    ) -> UserExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/client/#get_waiter)
        """
