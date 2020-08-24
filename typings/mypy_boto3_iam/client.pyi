# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for iam service client

Usage::

    ```python
    import boto3
    from mypy_boto3_iam import IAMClient

    client: IAMClient = boto3.client("iam")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_iam.paginator import (
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
    ListMFADevicesPaginator,
    ListPoliciesPaginator,
    ListPolicyVersionsPaginator,
    ListRolePoliciesPaginator,
    ListRolesPaginator,
    ListServerCertificatesPaginator,
    ListSigningCertificatesPaginator,
    ListSSHPublicKeysPaginator,
    ListUserPoliciesPaginator,
    ListUsersPaginator,
    ListVirtualMFADevicesPaginator,
    SimulateCustomPolicyPaginator,
    SimulatePrincipalPolicyPaginator,
)
from mypy_boto3_iam.type_defs import (
    ContextEntryTypeDef,
    CreateAccessKeyResponseTypeDef,
    CreateGroupResponseTypeDef,
    CreateInstanceProfileResponseTypeDef,
    CreateLoginProfileResponseTypeDef,
    CreateOpenIDConnectProviderResponseTypeDef,
    CreatePolicyResponseTypeDef,
    CreatePolicyVersionResponseTypeDef,
    CreateRoleResponseTypeDef,
    CreateSAMLProviderResponseTypeDef,
    CreateServiceLinkedRoleResponseTypeDef,
    CreateServiceSpecificCredentialResponseTypeDef,
    CreateUserResponseTypeDef,
    CreateVirtualMFADeviceResponseTypeDef,
    DeleteServiceLinkedRoleResponseTypeDef,
    GenerateCredentialReportResponseTypeDef,
    GenerateOrganizationsAccessReportResponseTypeDef,
    GenerateServiceLastAccessedDetailsResponseTypeDef,
    GetAccessKeyLastUsedResponseTypeDef,
    GetAccountAuthorizationDetailsResponseTypeDef,
    GetAccountPasswordPolicyResponseTypeDef,
    GetAccountSummaryResponseTypeDef,
    GetContextKeysForPolicyResponseTypeDef,
    GetCredentialReportResponseTypeDef,
    GetGroupPolicyResponseTypeDef,
    GetGroupResponseTypeDef,
    GetInstanceProfileResponseTypeDef,
    GetLoginProfileResponseTypeDef,
    GetOpenIDConnectProviderResponseTypeDef,
    GetOrganizationsAccessReportResponseTypeDef,
    GetPolicyResponseTypeDef,
    GetPolicyVersionResponseTypeDef,
    GetRolePolicyResponseTypeDef,
    GetRoleResponseTypeDef,
    GetSAMLProviderResponseTypeDef,
    GetServerCertificateResponseTypeDef,
    GetServiceLastAccessedDetailsResponseTypeDef,
    GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef,
    GetServiceLinkedRoleDeletionStatusResponseTypeDef,
    GetSSHPublicKeyResponseTypeDef,
    GetUserPolicyResponseTypeDef,
    GetUserResponseTypeDef,
    ListAccessKeysResponseTypeDef,
    ListAccountAliasesResponseTypeDef,
    ListAttachedGroupPoliciesResponseTypeDef,
    ListAttachedRolePoliciesResponseTypeDef,
    ListAttachedUserPoliciesResponseTypeDef,
    ListEntitiesForPolicyResponseTypeDef,
    ListGroupPoliciesResponseTypeDef,
    ListGroupsForUserResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListInstanceProfilesForRoleResponseTypeDef,
    ListInstanceProfilesResponseTypeDef,
    ListMFADevicesResponseTypeDef,
    ListOpenIDConnectProvidersResponseTypeDef,
    ListPoliciesGrantingServiceAccessResponseTypeDef,
    ListPoliciesResponseTypeDef,
    ListPolicyVersionsResponseTypeDef,
    ListRolePoliciesResponseTypeDef,
    ListRolesResponseTypeDef,
    ListRoleTagsResponseTypeDef,
    ListSAMLProvidersResponseTypeDef,
    ListServerCertificatesResponseTypeDef,
    ListServiceSpecificCredentialsResponseTypeDef,
    ListSigningCertificatesResponseTypeDef,
    ListSSHPublicKeysResponseTypeDef,
    ListUserPoliciesResponseTypeDef,
    ListUsersResponseTypeDef,
    ListUserTagsResponseTypeDef,
    ListVirtualMFADevicesResponseTypeDef,
    ResetServiceSpecificCredentialResponseTypeDef,
    SimulatePolicyResponseTypeDef,
    TagTypeDef,
    UpdateRoleDescriptionResponseTypeDef,
    UpdateSAMLProviderResponseTypeDef,
    UploadServerCertificateResponseTypeDef,
    UploadSigningCertificateResponseTypeDef,
    UploadSSHPublicKeyResponseTypeDef,
)
from mypy_boto3_iam.waiter import (
    InstanceProfileExistsWaiter,
    PolicyExistsWaiter,
    RoleExistsWaiter,
    UserExistsWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IAMClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    ConcurrentModificationException: Type[Boto3ClientError]
    CredentialReportExpiredException: Type[Boto3ClientError]
    CredentialReportNotPresentException: Type[Boto3ClientError]
    CredentialReportNotReadyException: Type[Boto3ClientError]
    DeleteConflictException: Type[Boto3ClientError]
    DuplicateCertificateException: Type[Boto3ClientError]
    DuplicateSSHPublicKeyException: Type[Boto3ClientError]
    EntityAlreadyExistsException: Type[Boto3ClientError]
    EntityTemporarilyUnmodifiableException: Type[Boto3ClientError]
    InvalidAuthenticationCodeException: Type[Boto3ClientError]
    InvalidCertificateException: Type[Boto3ClientError]
    InvalidInputException: Type[Boto3ClientError]
    InvalidPublicKeyException: Type[Boto3ClientError]
    InvalidUserTypeException: Type[Boto3ClientError]
    KeyPairMismatchException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    MalformedCertificateException: Type[Boto3ClientError]
    MalformedPolicyDocumentException: Type[Boto3ClientError]
    NoSuchEntityException: Type[Boto3ClientError]
    PasswordPolicyViolationException: Type[Boto3ClientError]
    PolicyEvaluationException: Type[Boto3ClientError]
    PolicyNotAttachableException: Type[Boto3ClientError]
    ReportGenerationLimitExceededException: Type[Boto3ClientError]
    ServiceFailureException: Type[Boto3ClientError]
    ServiceNotSupportedException: Type[Boto3ClientError]
    UnmodifiableEntityException: Type[Boto3ClientError]
    UnrecognizedPublicKeyEncodingException: Type[Boto3ClientError]


class IAMClient:
    """
    [IAM.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client)
    """

    exceptions: Exceptions

    def add_client_id_to_open_id_connect_provider(
        self, OpenIDConnectProviderArn: str, ClientID: str
    ) -> None:
        """
        [Client.add_client_id_to_open_id_connect_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.add_client_id_to_open_id_connect_provider)
        """

    def add_role_to_instance_profile(self, InstanceProfileName: str, RoleName: str) -> None:
        """
        [Client.add_role_to_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.add_role_to_instance_profile)
        """

    def add_user_to_group(self, GroupName: str, UserName: str) -> None:
        """
        [Client.add_user_to_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.add_user_to_group)
        """

    def attach_group_policy(self, GroupName: str, PolicyArn: str) -> None:
        """
        [Client.attach_group_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.attach_group_policy)
        """

    def attach_role_policy(self, RoleName: str, PolicyArn: str) -> None:
        """
        [Client.attach_role_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.attach_role_policy)
        """

    def attach_user_policy(self, UserName: str, PolicyArn: str) -> None:
        """
        [Client.attach_user_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.attach_user_policy)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.can_paginate)
        """

    def change_password(self, OldPassword: str, NewPassword: str) -> None:
        """
        [Client.change_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.change_password)
        """

    def create_access_key(self, UserName: str = None) -> CreateAccessKeyResponseTypeDef:
        """
        [Client.create_access_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.create_access_key)
        """

    def create_account_alias(self, AccountAlias: str) -> None:
        """
        [Client.create_account_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.create_account_alias)
        """

    def create_group(self, GroupName: str, Path: str = None) -> CreateGroupResponseTypeDef:
        """
        [Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.create_group)
        """

    def create_instance_profile(
        self, InstanceProfileName: str, Path: str = None
    ) -> CreateInstanceProfileResponseTypeDef:
        """
        [Client.create_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.create_instance_profile)
        """

    def create_login_profile(
        self, UserName: str, Password: str, PasswordResetRequired: bool = None
    ) -> CreateLoginProfileResponseTypeDef:
        """
        [Client.create_login_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.create_login_profile)
        """

    def create_open_id_connect_provider(
        self, Url: str, ThumbprintList: List[str], ClientIDList: List[str] = None
    ) -> CreateOpenIDConnectProviderResponseTypeDef:
        """
        [Client.create_open_id_connect_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.create_open_id_connect_provider)
        """

    def create_policy(
        self, PolicyName: str, PolicyDocument: str, Path: str = None, Description: str = None
    ) -> CreatePolicyResponseTypeDef:
        """
        [Client.create_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.create_policy)
        """

    def create_policy_version(
        self, PolicyArn: str, PolicyDocument: str, SetAsDefault: bool = None
    ) -> CreatePolicyVersionResponseTypeDef:
        """
        [Client.create_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.create_policy_version)
        """

    def create_role(
        self,
        RoleName: str,
        AssumeRolePolicyDocument: str,
        Path: str = None,
        Description: str = None,
        MaxSessionDuration: int = None,
        PermissionsBoundary: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateRoleResponseTypeDef:
        """
        [Client.create_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.create_role)
        """

    def create_saml_provider(
        self, SAMLMetadataDocument: str, Name: str
    ) -> CreateSAMLProviderResponseTypeDef:
        """
        [Client.create_saml_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.create_saml_provider)
        """

    def create_service_linked_role(
        self, AWSServiceName: str, Description: str = None, CustomSuffix: str = None
    ) -> CreateServiceLinkedRoleResponseTypeDef:
        """
        [Client.create_service_linked_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.create_service_linked_role)
        """

    def create_service_specific_credential(
        self, UserName: str, ServiceName: str
    ) -> CreateServiceSpecificCredentialResponseTypeDef:
        """
        [Client.create_service_specific_credential documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.create_service_specific_credential)
        """

    def create_user(
        self,
        UserName: str,
        Path: str = None,
        PermissionsBoundary: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateUserResponseTypeDef:
        """
        [Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.create_user)
        """

    def create_virtual_mfa_device(
        self, VirtualMFADeviceName: str, Path: str = None
    ) -> CreateVirtualMFADeviceResponseTypeDef:
        """
        [Client.create_virtual_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.create_virtual_mfa_device)
        """

    def deactivate_mfa_device(self, UserName: str, SerialNumber: str) -> None:
        """
        [Client.deactivate_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.deactivate_mfa_device)
        """

    def delete_access_key(self, AccessKeyId: str, UserName: str = None) -> None:
        """
        [Client.delete_access_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_access_key)
        """

    def delete_account_alias(self, AccountAlias: str) -> None:
        """
        [Client.delete_account_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_account_alias)
        """

    def delete_account_password_policy(self) -> None:
        """
        [Client.delete_account_password_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_account_password_policy)
        """

    def delete_group(self, GroupName: str) -> None:
        """
        [Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_group)
        """

    def delete_group_policy(self, GroupName: str, PolicyName: str) -> None:
        """
        [Client.delete_group_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_group_policy)
        """

    def delete_instance_profile(self, InstanceProfileName: str) -> None:
        """
        [Client.delete_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_instance_profile)
        """

    def delete_login_profile(self, UserName: str) -> None:
        """
        [Client.delete_login_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_login_profile)
        """

    def delete_open_id_connect_provider(self, OpenIDConnectProviderArn: str) -> None:
        """
        [Client.delete_open_id_connect_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_open_id_connect_provider)
        """

    def delete_policy(self, PolicyArn: str) -> None:
        """
        [Client.delete_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_policy)
        """

    def delete_policy_version(self, PolicyArn: str, VersionId: str) -> None:
        """
        [Client.delete_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_policy_version)
        """

    def delete_role(self, RoleName: str) -> None:
        """
        [Client.delete_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_role)
        """

    def delete_role_permissions_boundary(self, RoleName: str) -> None:
        """
        [Client.delete_role_permissions_boundary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_role_permissions_boundary)
        """

    def delete_role_policy(self, RoleName: str, PolicyName: str) -> None:
        """
        [Client.delete_role_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_role_policy)
        """

    def delete_saml_provider(self, SAMLProviderArn: str) -> None:
        """
        [Client.delete_saml_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_saml_provider)
        """

    def delete_server_certificate(self, ServerCertificateName: str) -> None:
        """
        [Client.delete_server_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_server_certificate)
        """

    def delete_service_linked_role(self, RoleName: str) -> DeleteServiceLinkedRoleResponseTypeDef:
        """
        [Client.delete_service_linked_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_service_linked_role)
        """

    def delete_service_specific_credential(
        self, ServiceSpecificCredentialId: str, UserName: str = None
    ) -> None:
        """
        [Client.delete_service_specific_credential documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_service_specific_credential)
        """

    def delete_signing_certificate(self, CertificateId: str, UserName: str = None) -> None:
        """
        [Client.delete_signing_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_signing_certificate)
        """

    def delete_ssh_public_key(self, UserName: str, SSHPublicKeyId: str) -> None:
        """
        [Client.delete_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_ssh_public_key)
        """

    def delete_user(self, UserName: str) -> None:
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_user)
        """

    def delete_user_permissions_boundary(self, UserName: str) -> None:
        """
        [Client.delete_user_permissions_boundary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_user_permissions_boundary)
        """

    def delete_user_policy(self, UserName: str, PolicyName: str) -> None:
        """
        [Client.delete_user_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_user_policy)
        """

    def delete_virtual_mfa_device(self, SerialNumber: str) -> None:
        """
        [Client.delete_virtual_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.delete_virtual_mfa_device)
        """

    def detach_group_policy(self, GroupName: str, PolicyArn: str) -> None:
        """
        [Client.detach_group_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.detach_group_policy)
        """

    def detach_role_policy(self, RoleName: str, PolicyArn: str) -> None:
        """
        [Client.detach_role_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.detach_role_policy)
        """

    def detach_user_policy(self, UserName: str, PolicyArn: str) -> None:
        """
        [Client.detach_user_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.detach_user_policy)
        """

    def enable_mfa_device(
        self, UserName: str, SerialNumber: str, AuthenticationCode1: str, AuthenticationCode2: str
    ) -> None:
        """
        [Client.enable_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.enable_mfa_device)
        """

    def generate_credential_report(self) -> GenerateCredentialReportResponseTypeDef:
        """
        [Client.generate_credential_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.generate_credential_report)
        """

    def generate_organizations_access_report(
        self, EntityPath: str, OrganizationsPolicyId: str = None
    ) -> GenerateOrganizationsAccessReportResponseTypeDef:
        """
        [Client.generate_organizations_access_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.generate_organizations_access_report)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.generate_presigned_url)
        """

    def generate_service_last_accessed_details(
        self, Arn: str, Granularity: Literal["SERVICE_LEVEL", "ACTION_LEVEL"] = None
    ) -> GenerateServiceLastAccessedDetailsResponseTypeDef:
        """
        [Client.generate_service_last_accessed_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.generate_service_last_accessed_details)
        """

    def get_access_key_last_used(self, AccessKeyId: str) -> GetAccessKeyLastUsedResponseTypeDef:
        """
        [Client.get_access_key_last_used documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_access_key_last_used)
        """

    def get_account_authorization_details(
        self,
        Filter: List[
            Literal["User", "Role", "Group", "LocalManagedPolicy", "AWSManagedPolicy"]
        ] = None,
        MaxItems: int = None,
        Marker: str = None,
    ) -> GetAccountAuthorizationDetailsResponseTypeDef:
        """
        [Client.get_account_authorization_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_account_authorization_details)
        """

    def get_account_password_policy(self) -> GetAccountPasswordPolicyResponseTypeDef:
        """
        [Client.get_account_password_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_account_password_policy)
        """

    def get_account_summary(self) -> GetAccountSummaryResponseTypeDef:
        """
        [Client.get_account_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_account_summary)
        """

    def get_context_keys_for_custom_policy(
        self, PolicyInputList: List[str]
    ) -> GetContextKeysForPolicyResponseTypeDef:
        """
        [Client.get_context_keys_for_custom_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_context_keys_for_custom_policy)
        """

    def get_context_keys_for_principal_policy(
        self, PolicySourceArn: str, PolicyInputList: List[str] = None
    ) -> GetContextKeysForPolicyResponseTypeDef:
        """
        [Client.get_context_keys_for_principal_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_context_keys_for_principal_policy)
        """

    def get_credential_report(self) -> GetCredentialReportResponseTypeDef:
        """
        [Client.get_credential_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_credential_report)
        """

    def get_group(
        self, GroupName: str, Marker: str = None, MaxItems: int = None
    ) -> GetGroupResponseTypeDef:
        """
        [Client.get_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_group)
        """

    def get_group_policy(self, GroupName: str, PolicyName: str) -> GetGroupPolicyResponseTypeDef:
        """
        [Client.get_group_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_group_policy)
        """

    def get_instance_profile(self, InstanceProfileName: str) -> GetInstanceProfileResponseTypeDef:
        """
        [Client.get_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_instance_profile)
        """

    def get_login_profile(self, UserName: str) -> GetLoginProfileResponseTypeDef:
        """
        [Client.get_login_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_login_profile)
        """

    def get_open_id_connect_provider(
        self, OpenIDConnectProviderArn: str
    ) -> GetOpenIDConnectProviderResponseTypeDef:
        """
        [Client.get_open_id_connect_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_open_id_connect_provider)
        """

    def get_organizations_access_report(
        self,
        JobId: str,
        MaxItems: int = None,
        Marker: str = None,
        SortKey: Literal[
            "SERVICE_NAMESPACE_ASCENDING",
            "SERVICE_NAMESPACE_DESCENDING",
            "LAST_AUTHENTICATED_TIME_ASCENDING",
            "LAST_AUTHENTICATED_TIME_DESCENDING",
        ] = None,
    ) -> GetOrganizationsAccessReportResponseTypeDef:
        """
        [Client.get_organizations_access_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_organizations_access_report)
        """

    def get_policy(self, PolicyArn: str) -> GetPolicyResponseTypeDef:
        """
        [Client.get_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_policy)
        """

    def get_policy_version(self, PolicyArn: str, VersionId: str) -> GetPolicyVersionResponseTypeDef:
        """
        [Client.get_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_policy_version)
        """

    def get_role(self, RoleName: str) -> GetRoleResponseTypeDef:
        """
        [Client.get_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_role)
        """

    def get_role_policy(self, RoleName: str, PolicyName: str) -> GetRolePolicyResponseTypeDef:
        """
        [Client.get_role_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_role_policy)
        """

    def get_saml_provider(self, SAMLProviderArn: str) -> GetSAMLProviderResponseTypeDef:
        """
        [Client.get_saml_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_saml_provider)
        """

    def get_server_certificate(
        self, ServerCertificateName: str
    ) -> GetServerCertificateResponseTypeDef:
        """
        [Client.get_server_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_server_certificate)
        """

    def get_service_last_accessed_details(
        self, JobId: str, MaxItems: int = None, Marker: str = None
    ) -> GetServiceLastAccessedDetailsResponseTypeDef:
        """
        [Client.get_service_last_accessed_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_service_last_accessed_details)
        """

    def get_service_last_accessed_details_with_entities(
        self, JobId: str, ServiceNamespace: str, MaxItems: int = None, Marker: str = None
    ) -> GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef:
        """
        [Client.get_service_last_accessed_details_with_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_service_last_accessed_details_with_entities)
        """

    def get_service_linked_role_deletion_status(
        self, DeletionTaskId: str
    ) -> GetServiceLinkedRoleDeletionStatusResponseTypeDef:
        """
        [Client.get_service_linked_role_deletion_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_service_linked_role_deletion_status)
        """

    def get_ssh_public_key(
        self, UserName: str, SSHPublicKeyId: str, Encoding: Literal["SSH", "PEM"]
    ) -> GetSSHPublicKeyResponseTypeDef:
        """
        [Client.get_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_ssh_public_key)
        """

    def get_user(self, UserName: str = None) -> GetUserResponseTypeDef:
        """
        [Client.get_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_user)
        """

    def get_user_policy(self, UserName: str, PolicyName: str) -> GetUserPolicyResponseTypeDef:
        """
        [Client.get_user_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.get_user_policy)
        """

    def list_access_keys(
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListAccessKeysResponseTypeDef:
        """
        [Client.list_access_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_access_keys)
        """

    def list_account_aliases(
        self, Marker: str = None, MaxItems: int = None
    ) -> ListAccountAliasesResponseTypeDef:
        """
        [Client.list_account_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_account_aliases)
        """

    def list_attached_group_policies(
        self, GroupName: str, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListAttachedGroupPoliciesResponseTypeDef:
        """
        [Client.list_attached_group_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_attached_group_policies)
        """

    def list_attached_role_policies(
        self, RoleName: str, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListAttachedRolePoliciesResponseTypeDef:
        """
        [Client.list_attached_role_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_attached_role_policies)
        """

    def list_attached_user_policies(
        self, UserName: str, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListAttachedUserPoliciesResponseTypeDef:
        """
        [Client.list_attached_user_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_attached_user_policies)
        """

    def list_entities_for_policy(
        self,
        PolicyArn: str,
        EntityFilter: Literal[
            "User", "Role", "Group", "LocalManagedPolicy", "AWSManagedPolicy"
        ] = None,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> ListEntitiesForPolicyResponseTypeDef:
        """
        [Client.list_entities_for_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_entities_for_policy)
        """

    def list_group_policies(
        self, GroupName: str, Marker: str = None, MaxItems: int = None
    ) -> ListGroupPoliciesResponseTypeDef:
        """
        [Client.list_group_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_group_policies)
        """

    def list_groups(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListGroupsResponseTypeDef:
        """
        [Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_groups)
        """

    def list_groups_for_user(
        self, UserName: str, Marker: str = None, MaxItems: int = None
    ) -> ListGroupsForUserResponseTypeDef:
        """
        [Client.list_groups_for_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_groups_for_user)
        """

    def list_instance_profiles(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListInstanceProfilesResponseTypeDef:
        """
        [Client.list_instance_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_instance_profiles)
        """

    def list_instance_profiles_for_role(
        self, RoleName: str, Marker: str = None, MaxItems: int = None
    ) -> ListInstanceProfilesForRoleResponseTypeDef:
        """
        [Client.list_instance_profiles_for_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_instance_profiles_for_role)
        """

    def list_mfa_devices(
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListMFADevicesResponseTypeDef:
        """
        [Client.list_mfa_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_mfa_devices)
        """

    def list_open_id_connect_providers(self) -> ListOpenIDConnectProvidersResponseTypeDef:
        """
        [Client.list_open_id_connect_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_open_id_connect_providers)
        """

    def list_policies(
        self,
        Scope: Literal["All", "AWS", "Local"] = None,
        OnlyAttached: bool = None,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> ListPoliciesResponseTypeDef:
        """
        [Client.list_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_policies)
        """

    def list_policies_granting_service_access(
        self, Arn: str, ServiceNamespaces: List[str], Marker: str = None
    ) -> ListPoliciesGrantingServiceAccessResponseTypeDef:
        """
        [Client.list_policies_granting_service_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_policies_granting_service_access)
        """

    def list_policy_versions(
        self, PolicyArn: str, Marker: str = None, MaxItems: int = None
    ) -> ListPolicyVersionsResponseTypeDef:
        """
        [Client.list_policy_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_policy_versions)
        """

    def list_role_policies(
        self, RoleName: str, Marker: str = None, MaxItems: int = None
    ) -> ListRolePoliciesResponseTypeDef:
        """
        [Client.list_role_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_role_policies)
        """

    def list_role_tags(
        self, RoleName: str, Marker: str = None, MaxItems: int = None
    ) -> ListRoleTagsResponseTypeDef:
        """
        [Client.list_role_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_role_tags)
        """

    def list_roles(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListRolesResponseTypeDef:
        """
        [Client.list_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_roles)
        """

    def list_saml_providers(self) -> ListSAMLProvidersResponseTypeDef:
        """
        [Client.list_saml_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_saml_providers)
        """

    def list_server_certificates(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListServerCertificatesResponseTypeDef:
        """
        [Client.list_server_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_server_certificates)
        """

    def list_service_specific_credentials(
        self, UserName: str = None, ServiceName: str = None
    ) -> ListServiceSpecificCredentialsResponseTypeDef:
        """
        [Client.list_service_specific_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_service_specific_credentials)
        """

    def list_signing_certificates(
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListSigningCertificatesResponseTypeDef:
        """
        [Client.list_signing_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_signing_certificates)
        """

    def list_ssh_public_keys(
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListSSHPublicKeysResponseTypeDef:
        """
        [Client.list_ssh_public_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_ssh_public_keys)
        """

    def list_user_policies(
        self, UserName: str, Marker: str = None, MaxItems: int = None
    ) -> ListUserPoliciesResponseTypeDef:
        """
        [Client.list_user_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_user_policies)
        """

    def list_user_tags(
        self, UserName: str, Marker: str = None, MaxItems: int = None
    ) -> ListUserTagsResponseTypeDef:
        """
        [Client.list_user_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_user_tags)
        """

    def list_users(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListUsersResponseTypeDef:
        """
        [Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_users)
        """

    def list_virtual_mfa_devices(
        self,
        AssignmentStatus: Literal["Assigned", "Unassigned", "Any"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> ListVirtualMFADevicesResponseTypeDef:
        """
        [Client.list_virtual_mfa_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.list_virtual_mfa_devices)
        """

    def put_group_policy(self, GroupName: str, PolicyName: str, PolicyDocument: str) -> None:
        """
        [Client.put_group_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.put_group_policy)
        """

    def put_role_permissions_boundary(self, RoleName: str, PermissionsBoundary: str) -> None:
        """
        [Client.put_role_permissions_boundary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.put_role_permissions_boundary)
        """

    def put_role_policy(self, RoleName: str, PolicyName: str, PolicyDocument: str) -> None:
        """
        [Client.put_role_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.put_role_policy)
        """

    def put_user_permissions_boundary(self, UserName: str, PermissionsBoundary: str) -> None:
        """
        [Client.put_user_permissions_boundary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.put_user_permissions_boundary)
        """

    def put_user_policy(self, UserName: str, PolicyName: str, PolicyDocument: str) -> None:
        """
        [Client.put_user_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.put_user_policy)
        """

    def remove_client_id_from_open_id_connect_provider(
        self, OpenIDConnectProviderArn: str, ClientID: str
    ) -> None:
        """
        [Client.remove_client_id_from_open_id_connect_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.remove_client_id_from_open_id_connect_provider)
        """

    def remove_role_from_instance_profile(self, InstanceProfileName: str, RoleName: str) -> None:
        """
        [Client.remove_role_from_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.remove_role_from_instance_profile)
        """

    def remove_user_from_group(self, GroupName: str, UserName: str) -> None:
        """
        [Client.remove_user_from_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.remove_user_from_group)
        """

    def reset_service_specific_credential(
        self, ServiceSpecificCredentialId: str, UserName: str = None
    ) -> ResetServiceSpecificCredentialResponseTypeDef:
        """
        [Client.reset_service_specific_credential documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.reset_service_specific_credential)
        """

    def resync_mfa_device(
        self, UserName: str, SerialNumber: str, AuthenticationCode1: str, AuthenticationCode2: str
    ) -> None:
        """
        [Client.resync_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.resync_mfa_device)
        """

    def set_default_policy_version(self, PolicyArn: str, VersionId: str) -> None:
        """
        [Client.set_default_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.set_default_policy_version)
        """

    def set_security_token_service_preferences(
        self, GlobalEndpointTokenVersion: Literal["v1Token", "v2Token"]
    ) -> None:
        """
        [Client.set_security_token_service_preferences documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.set_security_token_service_preferences)
        """

    def simulate_custom_policy(
        self,
        PolicyInputList: List[str],
        ActionNames: List[str],
        PermissionsBoundaryPolicyInputList: List[str] = None,
        ResourceArns: List[str] = None,
        ResourcePolicy: str = None,
        ResourceOwner: str = None,
        CallerArn: str = None,
        ContextEntries: List[ContextEntryTypeDef] = None,
        ResourceHandlingOption: str = None,
        MaxItems: int = None,
        Marker: str = None,
    ) -> SimulatePolicyResponseTypeDef:
        """
        [Client.simulate_custom_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.simulate_custom_policy)
        """

    def simulate_principal_policy(
        self,
        PolicySourceArn: str,
        ActionNames: List[str],
        PolicyInputList: List[str] = None,
        PermissionsBoundaryPolicyInputList: List[str] = None,
        ResourceArns: List[str] = None,
        ResourcePolicy: str = None,
        ResourceOwner: str = None,
        CallerArn: str = None,
        ContextEntries: List[ContextEntryTypeDef] = None,
        ResourceHandlingOption: str = None,
        MaxItems: int = None,
        Marker: str = None,
    ) -> SimulatePolicyResponseTypeDef:
        """
        [Client.simulate_principal_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.simulate_principal_policy)
        """

    def tag_role(self, RoleName: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Client.tag_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.tag_role)
        """

    def tag_user(self, UserName: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Client.tag_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.tag_user)
        """

    def untag_role(self, RoleName: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.untag_role)
        """

    def untag_user(self, UserName: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.untag_user)
        """

    def update_access_key(
        self, AccessKeyId: str, Status: Literal["Active", "Inactive"], UserName: str = None
    ) -> None:
        """
        [Client.update_access_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.update_access_key)
        """

    def update_account_password_policy(
        self,
        MinimumPasswordLength: int = None,
        RequireSymbols: bool = None,
        RequireNumbers: bool = None,
        RequireUppercaseCharacters: bool = None,
        RequireLowercaseCharacters: bool = None,
        AllowUsersToChangePassword: bool = None,
        MaxPasswordAge: int = None,
        PasswordReusePrevention: int = None,
        HardExpiry: bool = None,
    ) -> None:
        """
        [Client.update_account_password_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.update_account_password_policy)
        """

    def update_assume_role_policy(self, RoleName: str, PolicyDocument: str) -> None:
        """
        [Client.update_assume_role_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.update_assume_role_policy)
        """

    def update_group(self, GroupName: str, NewPath: str = None, NewGroupName: str = None) -> None:
        """
        [Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.update_group)
        """

    def update_login_profile(
        self, UserName: str, Password: str = None, PasswordResetRequired: bool = None
    ) -> None:
        """
        [Client.update_login_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.update_login_profile)
        """

    def update_open_id_connect_provider_thumbprint(
        self, OpenIDConnectProviderArn: str, ThumbprintList: List[str]
    ) -> None:
        """
        [Client.update_open_id_connect_provider_thumbprint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.update_open_id_connect_provider_thumbprint)
        """

    def update_role(
        self, RoleName: str, Description: str = None, MaxSessionDuration: int = None
    ) -> Dict[str, Any]:
        """
        [Client.update_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.update_role)
        """

    def update_role_description(
        self, RoleName: str, Description: str
    ) -> UpdateRoleDescriptionResponseTypeDef:
        """
        [Client.update_role_description documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.update_role_description)
        """

    def update_saml_provider(
        self, SAMLMetadataDocument: str, SAMLProviderArn: str
    ) -> UpdateSAMLProviderResponseTypeDef:
        """
        [Client.update_saml_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.update_saml_provider)
        """

    def update_server_certificate(
        self, ServerCertificateName: str, NewPath: str = None, NewServerCertificateName: str = None
    ) -> None:
        """
        [Client.update_server_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.update_server_certificate)
        """

    def update_service_specific_credential(
        self,
        ServiceSpecificCredentialId: str,
        Status: Literal["Active", "Inactive"],
        UserName: str = None,
    ) -> None:
        """
        [Client.update_service_specific_credential documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.update_service_specific_credential)
        """

    def update_signing_certificate(
        self, CertificateId: str, Status: Literal["Active", "Inactive"], UserName: str = None
    ) -> None:
        """
        [Client.update_signing_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.update_signing_certificate)
        """

    def update_ssh_public_key(
        self, UserName: str, SSHPublicKeyId: str, Status: Literal["Active", "Inactive"]
    ) -> None:
        """
        [Client.update_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.update_ssh_public_key)
        """

    def update_user(self, UserName: str, NewPath: str = None, NewUserName: str = None) -> None:
        """
        [Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.update_user)
        """

    def upload_server_certificate(
        self,
        ServerCertificateName: str,
        CertificateBody: str,
        PrivateKey: str,
        Path: str = None,
        CertificateChain: str = None,
    ) -> UploadServerCertificateResponseTypeDef:
        """
        [Client.upload_server_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.upload_server_certificate)
        """

    def upload_signing_certificate(
        self, CertificateBody: str, UserName: str = None
    ) -> UploadSigningCertificateResponseTypeDef:
        """
        [Client.upload_signing_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.upload_signing_certificate)
        """

    def upload_ssh_public_key(
        self, UserName: str, SSHPublicKeyBody: str
    ) -> UploadSSHPublicKeyResponseTypeDef:
        """
        [Client.upload_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Client.upload_ssh_public_key)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_account_authorization_details"]
    ) -> GetAccountAuthorizationDetailsPaginator:
        """
        [Paginator.GetAccountAuthorizationDetails documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.GetAccountAuthorizationDetails)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_group"]) -> GetGroupPaginator:
        """
        [Paginator.GetGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.GetGroup)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_access_keys"]) -> ListAccessKeysPaginator:
        """
        [Paginator.ListAccessKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListAccessKeys)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_aliases"]
    ) -> ListAccountAliasesPaginator:
        """
        [Paginator.ListAccountAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListAccountAliases)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_attached_group_policies"]
    ) -> ListAttachedGroupPoliciesPaginator:
        """
        [Paginator.ListAttachedGroupPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListAttachedGroupPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_attached_role_policies"]
    ) -> ListAttachedRolePoliciesPaginator:
        """
        [Paginator.ListAttachedRolePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListAttachedRolePolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_attached_user_policies"]
    ) -> ListAttachedUserPoliciesPaginator:
        """
        [Paginator.ListAttachedUserPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListAttachedUserPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_entities_for_policy"]
    ) -> ListEntitiesForPolicyPaginator:
        """
        [Paginator.ListEntitiesForPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListEntitiesForPolicy)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_group_policies"]
    ) -> ListGroupPoliciesPaginator:
        """
        [Paginator.ListGroupPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListGroupPolicies)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_groups"]) -> ListGroupsPaginator:
        """
        [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_groups_for_user"]
    ) -> ListGroupsForUserPaginator:
        """
        [Paginator.ListGroupsForUser documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListGroupsForUser)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_profiles"]
    ) -> ListInstanceProfilesPaginator:
        """
        [Paginator.ListInstanceProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListInstanceProfiles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_profiles_for_role"]
    ) -> ListInstanceProfilesForRolePaginator:
        """
        [Paginator.ListInstanceProfilesForRole documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListInstanceProfilesForRole)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_mfa_devices"]) -> ListMFADevicesPaginator:
        """
        [Paginator.ListMFADevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListMFADevices)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_policies"]) -> ListPoliciesPaginator:
        """
        [Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_policy_versions"]
    ) -> ListPolicyVersionsPaginator:
        """
        [Paginator.ListPolicyVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListPolicyVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_role_policies"]
    ) -> ListRolePoliciesPaginator:
        """
        [Paginator.ListRolePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListRolePolicies)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_roles"]) -> ListRolesPaginator:
        """
        [Paginator.ListRoles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListRoles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_ssh_public_keys"]
    ) -> ListSSHPublicKeysPaginator:
        """
        [Paginator.ListSSHPublicKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListSSHPublicKeys)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_server_certificates"]
    ) -> ListServerCertificatesPaginator:
        """
        [Paginator.ListServerCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListServerCertificates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_signing_certificates"]
    ) -> ListSigningCertificatesPaginator:
        """
        [Paginator.ListSigningCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListSigningCertificates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_policies"]
    ) -> ListUserPoliciesPaginator:
        """
        [Paginator.ListUserPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListUserPolicies)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListUsers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_virtual_mfa_devices"]
    ) -> ListVirtualMFADevicesPaginator:
        """
        [Paginator.ListVirtualMFADevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.ListVirtualMFADevices)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["simulate_custom_policy"]
    ) -> SimulateCustomPolicyPaginator:
        """
        [Paginator.SimulateCustomPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.SimulateCustomPolicy)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["simulate_principal_policy"]
    ) -> SimulatePrincipalPolicyPaginator:
        """
        [Paginator.SimulatePrincipalPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Paginator.SimulatePrincipalPolicy)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass

    @overload
    def get_waiter(
        self, waiter_name: Literal["instance_profile_exists"]
    ) -> InstanceProfileExistsWaiter:
        """
        [Waiter.InstanceProfileExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Waiter.InstanceProfileExists)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["policy_exists"]) -> PolicyExistsWaiter:
        """
        [Waiter.PolicyExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Waiter.PolicyExists)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["role_exists"]) -> RoleExistsWaiter:
        """
        [Waiter.RoleExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Waiter.RoleExists)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["user_exists"]) -> UserExistsWaiter:
        """
        [Waiter.UserExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iam.html#IAM.Waiter.UserExists)
        """

    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        pass
