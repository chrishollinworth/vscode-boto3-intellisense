"""
Type annotations for sso-admin service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_sso_admin import SSOAdminClient

    client: SSOAdminClient = boto3.client("sso-admin")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ApplicationStatusType,
    GrantTypeType,
    PrincipalTypeType,
    ProvisioningStatusType,
    ProvisionTargetTypeType,
)
from .paginator import (
    ListAccountAssignmentCreationStatusPaginator,
    ListAccountAssignmentDeletionStatusPaginator,
    ListAccountAssignmentsForPrincipalPaginator,
    ListAccountAssignmentsPaginator,
    ListAccountsForProvisionedPermissionSetPaginator,
    ListApplicationAccessScopesPaginator,
    ListApplicationAssignmentsForPrincipalPaginator,
    ListApplicationAssignmentsPaginator,
    ListApplicationAuthenticationMethodsPaginator,
    ListApplicationGrantsPaginator,
    ListApplicationProvidersPaginator,
    ListApplicationsPaginator,
    ListCustomerManagedPolicyReferencesInPermissionSetPaginator,
    ListInstancesPaginator,
    ListManagedPoliciesInPermissionSetPaginator,
    ListPermissionSetProvisioningStatusPaginator,
    ListPermissionSetsPaginator,
    ListPermissionSetsProvisionedToAccountPaginator,
    ListTagsForResourcePaginator,
    ListTrustedTokenIssuersPaginator,
)
from .type_defs import (
    AuthenticationMethodTypeDef,
    CreateAccountAssignmentResponseTypeDef,
    CreateApplicationResponseTypeDef,
    CreateInstanceResponseTypeDef,
    CreatePermissionSetResponseTypeDef,
    CreateTrustedTokenIssuerResponseTypeDef,
    CustomerManagedPolicyReferenceTypeDef,
    DeleteAccountAssignmentResponseTypeDef,
    DescribeAccountAssignmentCreationStatusResponseTypeDef,
    DescribeAccountAssignmentDeletionStatusResponseTypeDef,
    DescribeApplicationAssignmentResponseTypeDef,
    DescribeApplicationProviderResponseTypeDef,
    DescribeApplicationResponseTypeDef,
    DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef,
    DescribeInstanceResponseTypeDef,
    DescribePermissionSetProvisioningStatusResponseTypeDef,
    DescribePermissionSetResponseTypeDef,
    DescribeTrustedTokenIssuerResponseTypeDef,
    GetApplicationAccessScopeResponseTypeDef,
    GetApplicationAssignmentConfigurationResponseTypeDef,
    GetApplicationAuthenticationMethodResponseTypeDef,
    GetApplicationGrantResponseTypeDef,
    GetInlinePolicyForPermissionSetResponseTypeDef,
    GetPermissionsBoundaryForPermissionSetResponseTypeDef,
    GrantTypeDef,
    InstanceAccessControlAttributeConfigurationTypeDef,
    ListAccountAssignmentCreationStatusResponseTypeDef,
    ListAccountAssignmentDeletionStatusResponseTypeDef,
    ListAccountAssignmentsFilterTypeDef,
    ListAccountAssignmentsForPrincipalResponseTypeDef,
    ListAccountAssignmentsResponseTypeDef,
    ListAccountsForProvisionedPermissionSetResponseTypeDef,
    ListApplicationAccessScopesResponseTypeDef,
    ListApplicationAssignmentsFilterTypeDef,
    ListApplicationAssignmentsForPrincipalResponseTypeDef,
    ListApplicationAssignmentsResponseTypeDef,
    ListApplicationAuthenticationMethodsResponseTypeDef,
    ListApplicationGrantsResponseTypeDef,
    ListApplicationProvidersResponseTypeDef,
    ListApplicationsFilterTypeDef,
    ListApplicationsResponseTypeDef,
    ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef,
    ListInstancesResponseTypeDef,
    ListManagedPoliciesInPermissionSetResponseTypeDef,
    ListPermissionSetProvisioningStatusResponseTypeDef,
    ListPermissionSetsProvisionedToAccountResponseTypeDef,
    ListPermissionSetsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTrustedTokenIssuersResponseTypeDef,
    OperationStatusFilterTypeDef,
    PermissionsBoundaryTypeDef,
    PortalOptionsTypeDef,
    ProvisionPermissionSetResponseTypeDef,
    TagTypeDef,
    TrustedTokenIssuerConfigurationTypeDef,
    TrustedTokenIssuerUpdateConfigurationTypeDef,
    UpdateApplicationPortalOptionsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("SSOAdminClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class SSOAdminClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SSOAdminClient exceptions.
        """
    def attach_customer_managed_policy_reference_to_permission_set(
        self,
        *,
        CustomerManagedPolicyReference: "CustomerManagedPolicyReferenceTypeDef",
        InstanceArn: str,
        PermissionSetArn: str
    ) -> Dict[str, Any]:
        """
        Attaches the specified customer managed policy to the specified  PermissionSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.attach_customer_managed_policy_reference_to_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#attach_customer_managed_policy_reference_to_permission_set)
        """
    def attach_managed_policy_to_permission_set(
        self, *, InstanceArn: str, ManagedPolicyArn: str, PermissionSetArn: str
    ) -> Dict[str, Any]:
        """
        Attaches an Amazon Web Services managed policy ARN to a permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.attach_managed_policy_to_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#attach_managed_policy_to_permission_set)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#close)
        """
    def create_account_assignment(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        PrincipalId: str,
        PrincipalType: PrincipalTypeType,
        TargetId: str,
        TargetType: Literal["AWS_ACCOUNT"]
    ) -> CreateAccountAssignmentResponseTypeDef:
        """
        Assigns access to a principal for a specified Amazon Web Services account using
        a specified permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.create_account_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#create_account_assignment)
        """
    def create_application(
        self,
        *,
        ApplicationProviderArn: str,
        InstanceArn: str,
        Name: str,
        ClientToken: str = None,
        Description: str = None,
        PortalOptions: "PortalOptionsTypeDef" = None,
        Status: ApplicationStatusType = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateApplicationResponseTypeDef:
        """
        Creates an application in IAM Identity Center for the given application
        provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.create_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#create_application)
        """
    def create_application_assignment(
        self, *, ApplicationArn: str, PrincipalId: str, PrincipalType: PrincipalTypeType
    ) -> Dict[str, Any]:
        """
        Grant application access to a user or group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.create_application_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#create_application_assignment)
        """
    def create_instance(
        self, *, ClientToken: str = None, Name: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateInstanceResponseTypeDef:
        """
        Creates an instance of IAM Identity Center for a standalone Amazon Web Services
        account that is not managed by Organizations or a member Amazon Web Services
        account in an organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.create_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#create_instance)
        """
    def create_instance_access_control_attribute_configuration(
        self,
        *,
        InstanceAccessControlAttributeConfiguration: "InstanceAccessControlAttributeConfigurationTypeDef",
        InstanceArn: str
    ) -> Dict[str, Any]:
        """
        Enables the attributes-based access control (ABAC) feature for the specified IAM
        Identity Center instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.create_instance_access_control_attribute_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#create_instance_access_control_attribute_configuration)
        """
    def create_permission_set(
        self,
        *,
        InstanceArn: str,
        Name: str,
        Description: str = None,
        RelayState: str = None,
        SessionDuration: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreatePermissionSetResponseTypeDef:
        """
        Creates a permission set within a specified IAM Identity Center instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.create_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#create_permission_set)
        """
    def create_trusted_token_issuer(
        self,
        *,
        InstanceArn: str,
        Name: str,
        TrustedTokenIssuerConfiguration: "TrustedTokenIssuerConfigurationTypeDef",
        TrustedTokenIssuerType: Literal["OIDC_JWT"],
        ClientToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateTrustedTokenIssuerResponseTypeDef:
        """
        Creates a connection to a trusted token issuer in an instance of IAM Identity
        Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.create_trusted_token_issuer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#create_trusted_token_issuer)
        """
    def delete_account_assignment(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        PrincipalId: str,
        PrincipalType: PrincipalTypeType,
        TargetId: str,
        TargetType: Literal["AWS_ACCOUNT"]
    ) -> DeleteAccountAssignmentResponseTypeDef:
        """
        Deletes a principal's access from a specified Amazon Web Services account using
        a specified permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.delete_account_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_account_assignment)
        """
    def delete_application(self, *, ApplicationArn: str) -> Dict[str, Any]:
        """
        Deletes the association with the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.delete_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_application)
        """
    def delete_application_access_scope(self, *, ApplicationArn: str, Scope: str) -> None:
        """
        Deletes an IAM Identity Center access scope from an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.delete_application_access_scope)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_application_access_scope)
        """
    def delete_application_assignment(
        self, *, ApplicationArn: str, PrincipalId: str, PrincipalType: PrincipalTypeType
    ) -> Dict[str, Any]:
        """
        Revoke application access to an application by deleting application assignments
        for a user or group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.delete_application_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_application_assignment)
        """
    def delete_application_authentication_method(
        self, *, ApplicationArn: str, AuthenticationMethodType: Literal["IAM"]
    ) -> None:
        """
        Deletes an authentication method from an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.delete_application_authentication_method)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_application_authentication_method)
        """
    def delete_application_grant(self, *, ApplicationArn: str, GrantType: GrantTypeType) -> None:
        """
        Deletes a grant from an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.delete_application_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_application_grant)
        """
    def delete_inline_policy_from_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str
    ) -> Dict[str, Any]:
        """
        Deletes the inline policy from a specified permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.delete_inline_policy_from_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_inline_policy_from_permission_set)
        """
    def delete_instance(self, *, InstanceArn: str) -> Dict[str, Any]:
        """
        Deletes the instance of IAM Identity Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.delete_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_instance)
        """
    def delete_instance_access_control_attribute_configuration(
        self, *, InstanceArn: str
    ) -> Dict[str, Any]:
        """
        Disables the attributes-based access control (ABAC) feature for the specified
        IAM Identity Center instance and deletes all of the attribute mappings that have
        been configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.delete_instance_access_control_attribute_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_instance_access_control_attribute_configuration)
        """
    def delete_permission_set(self, *, InstanceArn: str, PermissionSetArn: str) -> Dict[str, Any]:
        """
        Deletes the specified permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.delete_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_permission_set)
        """
    def delete_permissions_boundary_from_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str
    ) -> Dict[str, Any]:
        """
        Deletes the permissions boundary from a specified  PermissionSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.delete_permissions_boundary_from_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_permissions_boundary_from_permission_set)
        """
    def delete_trusted_token_issuer(self, *, TrustedTokenIssuerArn: str) -> Dict[str, Any]:
        """
        Deletes a trusted token issuer configuration from an instance of IAM Identity
        Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.delete_trusted_token_issuer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_trusted_token_issuer)
        """
    def describe_account_assignment_creation_status(
        self, *, AccountAssignmentCreationRequestId: str, InstanceArn: str
    ) -> DescribeAccountAssignmentCreationStatusResponseTypeDef:
        """
        Describes the status of the assignment creation request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.describe_account_assignment_creation_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#describe_account_assignment_creation_status)
        """
    def describe_account_assignment_deletion_status(
        self, *, AccountAssignmentDeletionRequestId: str, InstanceArn: str
    ) -> DescribeAccountAssignmentDeletionStatusResponseTypeDef:
        """
        Describes the status of the assignment deletion request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.describe_account_assignment_deletion_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#describe_account_assignment_deletion_status)
        """
    def describe_application(self, *, ApplicationArn: str) -> DescribeApplicationResponseTypeDef:
        """
        Retrieves the details of an application associated with an instance of IAM
        Identity Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.describe_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#describe_application)
        """
    def describe_application_assignment(
        self, *, ApplicationArn: str, PrincipalId: str, PrincipalType: PrincipalTypeType
    ) -> DescribeApplicationAssignmentResponseTypeDef:
        """
        Retrieves a direct assignment of a user or group to an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.describe_application_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#describe_application_assignment)
        """
    def describe_application_provider(
        self, *, ApplicationProviderArn: str
    ) -> DescribeApplicationProviderResponseTypeDef:
        """
        Retrieves details about a provider that can be used to connect an Amazon Web
        Services managed application or customer managed application to IAM Identity
        Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.describe_application_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#describe_application_provider)
        """
    def describe_instance(self, *, InstanceArn: str) -> DescribeInstanceResponseTypeDef:
        """
        Returns the details of an instance of IAM Identity Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.describe_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#describe_instance)
        """
    def describe_instance_access_control_attribute_configuration(
        self, *, InstanceArn: str
    ) -> DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef:
        """
        Returns the list of IAM Identity Center identity store attributes that have been
        configured to work with attributes-based access control (ABAC) for the specified
        IAM Identity Center instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.describe_instance_access_control_attribute_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#describe_instance_access_control_attribute_configuration)
        """
    def describe_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str
    ) -> DescribePermissionSetResponseTypeDef:
        """
        Gets the details of the permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.describe_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#describe_permission_set)
        """
    def describe_permission_set_provisioning_status(
        self, *, InstanceArn: str, ProvisionPermissionSetRequestId: str
    ) -> DescribePermissionSetProvisioningStatusResponseTypeDef:
        """
        Describes the status for the given permission set provisioning request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.describe_permission_set_provisioning_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#describe_permission_set_provisioning_status)
        """
    def describe_trusted_token_issuer(
        self, *, TrustedTokenIssuerArn: str
    ) -> DescribeTrustedTokenIssuerResponseTypeDef:
        """
        Retrieves details about a trusted token issuer configuration stored in an
        instance of IAM Identity Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.describe_trusted_token_issuer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#describe_trusted_token_issuer)
        """
    def detach_customer_managed_policy_reference_from_permission_set(
        self,
        *,
        CustomerManagedPolicyReference: "CustomerManagedPolicyReferenceTypeDef",
        InstanceArn: str,
        PermissionSetArn: str
    ) -> Dict[str, Any]:
        """
        Detaches the specified customer managed policy from the specified
        PermissionSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.detach_customer_managed_policy_reference_from_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#detach_customer_managed_policy_reference_from_permission_set)
        """
    def detach_managed_policy_from_permission_set(
        self, *, InstanceArn: str, ManagedPolicyArn: str, PermissionSetArn: str
    ) -> Dict[str, Any]:
        """
        Detaches the attached Amazon Web Services managed policy ARN from the specified
        permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.detach_managed_policy_from_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#detach_managed_policy_from_permission_set)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#generate_presigned_url)
        """
    def get_application_access_scope(
        self, *, ApplicationArn: str, Scope: str
    ) -> GetApplicationAccessScopeResponseTypeDef:
        """
        Retrieves the authorized targets for an IAM Identity Center access scope for an
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.get_application_access_scope)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#get_application_access_scope)
        """
    def get_application_assignment_configuration(
        self, *, ApplicationArn: str
    ) -> GetApplicationAssignmentConfigurationResponseTypeDef:
        """
        Retrieves the configuration of  PutApplicationAssignmentConfiguration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.get_application_assignment_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#get_application_assignment_configuration)
        """
    def get_application_authentication_method(
        self, *, ApplicationArn: str, AuthenticationMethodType: Literal["IAM"]
    ) -> GetApplicationAuthenticationMethodResponseTypeDef:
        """
        Retrieves details about an authentication method used by an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.get_application_authentication_method)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#get_application_authentication_method)
        """
    def get_application_grant(
        self, *, ApplicationArn: str, GrantType: GrantTypeType
    ) -> GetApplicationGrantResponseTypeDef:
        """
        Retrieves details about an application grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.get_application_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#get_application_grant)
        """
    def get_inline_policy_for_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str
    ) -> GetInlinePolicyForPermissionSetResponseTypeDef:
        """
        Obtains the inline policy assigned to the permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.get_inline_policy_for_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#get_inline_policy_for_permission_set)
        """
    def get_permissions_boundary_for_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str
    ) -> GetPermissionsBoundaryForPermissionSetResponseTypeDef:
        """
        Obtains the permissions boundary for a specified  PermissionSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.get_permissions_boundary_for_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#get_permissions_boundary_for_permission_set)
        """
    def list_account_assignment_creation_status(
        self,
        *,
        InstanceArn: str,
        Filter: "OperationStatusFilterTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListAccountAssignmentCreationStatusResponseTypeDef:
        """
        Lists the status of the Amazon Web Services account assignment creation requests
        for a specified IAM Identity Center instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.list_account_assignment_creation_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_account_assignment_creation_status)
        """
    def list_account_assignment_deletion_status(
        self,
        *,
        InstanceArn: str,
        Filter: "OperationStatusFilterTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListAccountAssignmentDeletionStatusResponseTypeDef:
        """
        Lists the status of the Amazon Web Services account assignment deletion requests
        for a specified IAM Identity Center instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.list_account_assignment_deletion_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_account_assignment_deletion_status)
        """
    def list_account_assignments(
        self,
        *,
        AccountId: str,
        InstanceArn: str,
        PermissionSetArn: str,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListAccountAssignmentsResponseTypeDef:
        """
        Lists the assignee of the specified Amazon Web Services account with the
        specified permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.list_account_assignments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_account_assignments)
        """
    def list_account_assignments_for_principal(
        self,
        *,
        InstanceArn: str,
        PrincipalId: str,
        PrincipalType: PrincipalTypeType,
        Filter: "ListAccountAssignmentsFilterTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListAccountAssignmentsForPrincipalResponseTypeDef:
        """
        Retrieves a list of the IAM Identity Center associated Amazon Web Services
        accounts that the principal has access to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.list_account_assignments_for_principal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_account_assignments_for_principal)
        """
    def list_accounts_for_provisioned_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        ProvisioningStatus: ProvisioningStatusType = None
    ) -> ListAccountsForProvisionedPermissionSetResponseTypeDef:
        """
        Lists all the Amazon Web Services accounts where the specified permission set is
        provisioned.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.list_accounts_for_provisioned_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_accounts_for_provisioned_permission_set)
        """
    def list_application_access_scopes(
        self, *, ApplicationArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListApplicationAccessScopesResponseTypeDef:
        """
        Lists the access scopes and authorized targets associated with an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.list_application_access_scopes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_application_access_scopes)
        """
    def list_application_assignments(
        self, *, ApplicationArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListApplicationAssignmentsResponseTypeDef:
        """
        Lists Amazon Web Services account users that are assigned to an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.list_application_assignments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_application_assignments)
        """
    def list_application_assignments_for_principal(
        self,
        *,
        InstanceArn: str,
        PrincipalId: str,
        PrincipalType: PrincipalTypeType,
        Filter: "ListApplicationAssignmentsFilterTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListApplicationAssignmentsForPrincipalResponseTypeDef:
        """
        Lists the applications to which a specified principal is assigned.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.list_application_assignments_for_principal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_application_assignments_for_principal)
        """
    def list_application_authentication_methods(
        self, *, ApplicationArn: str, NextToken: str = None
    ) -> ListApplicationAuthenticationMethodsResponseTypeDef:
        """
        Lists all of the authentication methods supported by the specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.list_application_authentication_methods)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_application_authentication_methods)
        """
    def list_application_grants(
        self, *, ApplicationArn: str, NextToken: str = None
    ) -> ListApplicationGrantsResponseTypeDef:
        """
        List the grants associated with an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.list_application_grants)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_application_grants)
        """
    def list_application_providers(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListApplicationProvidersResponseTypeDef:
        """
        Lists the application providers configured in the IAM Identity Center identity
        store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.list_application_providers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_application_providers)
        """
    def list_applications(
        self,
        *,
        InstanceArn: str,
        Filter: "ListApplicationsFilterTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListApplicationsResponseTypeDef:
        """
        Lists all applications associated with the instance of IAM Identity Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.list_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_applications)
        """
    def list_customer_managed_policy_references_in_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef:
        """
        Lists all customer managed policies attached to a specified  PermissionSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.list_customer_managed_policy_references_in_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_customer_managed_policy_references_in_permission_set)
        """
    def list_instances(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListInstancesResponseTypeDef:
        """
        Lists the details of the organization and account instances of IAM Identity
        Center that were created in or visible to the account calling this API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.list_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_instances)
        """
    def list_managed_policies_in_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListManagedPoliciesInPermissionSetResponseTypeDef:
        """
        Lists the Amazon Web Services managed policy that is attached to a specified
        permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.list_managed_policies_in_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_managed_policies_in_permission_set)
        """
    def list_permission_set_provisioning_status(
        self,
        *,
        InstanceArn: str,
        Filter: "OperationStatusFilterTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListPermissionSetProvisioningStatusResponseTypeDef:
        """
        Lists the status of the permission set provisioning requests for a specified IAM
        Identity Center instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.list_permission_set_provisioning_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_permission_set_provisioning_status)
        """
    def list_permission_sets(
        self, *, InstanceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListPermissionSetsResponseTypeDef:
        """
        Lists the  PermissionSets in an IAM Identity Center instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.list_permission_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_permission_sets)
        """
    def list_permission_sets_provisioned_to_account(
        self,
        *,
        AccountId: str,
        InstanceArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        ProvisioningStatus: ProvisioningStatusType = None
    ) -> ListPermissionSetsProvisionedToAccountResponseTypeDef:
        """
        Lists all the permission sets that are provisioned to a specified Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.list_permission_sets_provisioned_to_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_permission_sets_provisioned_to_account)
        """
    def list_tags_for_resource(
        self, *, ResourceArn: str, InstanceArn: str = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags that are attached to a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_tags_for_resource)
        """
    def list_trusted_token_issuers(
        self, *, InstanceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTrustedTokenIssuersResponseTypeDef:
        """
        Lists all the trusted token issuers configured in an instance of IAM Identity
        Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.list_trusted_token_issuers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_trusted_token_issuers)
        """
    def provision_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        TargetType: ProvisionTargetTypeType,
        TargetId: str = None
    ) -> ProvisionPermissionSetResponseTypeDef:
        """
        The process by which a specified permission set is provisioned to the specified
        target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.provision_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#provision_permission_set)
        """
    def put_application_access_scope(
        self, *, ApplicationArn: str, Scope: str, AuthorizedTargets: List[str] = None
    ) -> None:
        """
        Adds or updates the list of authorized targets for an IAM Identity Center access
        scope for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.put_application_access_scope)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#put_application_access_scope)
        """
    def put_application_assignment_configuration(
        self, *, ApplicationArn: str, AssignmentRequired: bool
    ) -> Dict[str, Any]:
        """
        Configure how users gain access to an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.put_application_assignment_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#put_application_assignment_configuration)
        """
    def put_application_authentication_method(
        self,
        *,
        ApplicationArn: str,
        AuthenticationMethod: "AuthenticationMethodTypeDef",
        AuthenticationMethodType: Literal["IAM"]
    ) -> None:
        """
        Adds or updates an authentication method for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.put_application_authentication_method)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#put_application_authentication_method)
        """
    def put_application_grant(
        self, *, ApplicationArn: str, Grant: "GrantTypeDef", GrantType: GrantTypeType
    ) -> None:
        """
        Adds a grant to an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.put_application_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#put_application_grant)
        """
    def put_inline_policy_to_permission_set(
        self, *, InlinePolicy: str, InstanceArn: str, PermissionSetArn: str
    ) -> Dict[str, Any]:
        """
        Attaches an inline policy to a permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.put_inline_policy_to_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#put_inline_policy_to_permission_set)
        """
    def put_permissions_boundary_to_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        PermissionsBoundary: "PermissionsBoundaryTypeDef"
    ) -> Dict[str, Any]:
        """
        Attaches an Amazon Web Services managed or customer managed policy to the
        specified  PermissionSet as a permissions boundary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.put_permissions_boundary_to_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#put_permissions_boundary_to_permission_set)
        """
    def tag_resource(
        self, *, ResourceArn: str, Tags: List["TagTypeDef"], InstanceArn: str = None
    ) -> Dict[str, Any]:
        """
        Associates a set of tags with a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#tag_resource)
        """
    def untag_resource(
        self, *, ResourceArn: str, TagKeys: List[str], InstanceArn: str = None
    ) -> Dict[str, Any]:
        """
        Disassociates a set of tags from a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#untag_resource)
        """
    def update_application(
        self,
        *,
        ApplicationArn: str,
        Description: str = None,
        Name: str = None,
        PortalOptions: "UpdateApplicationPortalOptionsTypeDef" = None,
        Status: ApplicationStatusType = None
    ) -> Dict[str, Any]:
        """
        Updates application properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.update_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#update_application)
        """
    def update_instance(self, *, InstanceArn: str, Name: str) -> Dict[str, Any]:
        """
        Update the details for the instance of IAM Identity Center that is owned by the
        Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.update_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#update_instance)
        """
    def update_instance_access_control_attribute_configuration(
        self,
        *,
        InstanceAccessControlAttributeConfiguration: "InstanceAccessControlAttributeConfigurationTypeDef",
        InstanceArn: str
    ) -> Dict[str, Any]:
        """
        Updates the IAM Identity Center identity store attributes that you can use with
        the IAM Identity Center instance for attributes-based access control (ABAC).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.update_instance_access_control_attribute_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#update_instance_access_control_attribute_configuration)
        """
    def update_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        Description: str = None,
        RelayState: str = None,
        SessionDuration: str = None
    ) -> Dict[str, Any]:
        """
        Updates an existing permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.update_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#update_permission_set)
        """
    def update_trusted_token_issuer(
        self,
        *,
        TrustedTokenIssuerArn: str,
        Name: str = None,
        TrustedTokenIssuerConfiguration: "TrustedTokenIssuerUpdateConfigurationTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates the name of the trusted token issuer, or the path of a source attribute
        or destination attribute for a trusted token issuer configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Client.update_trusted_token_issuer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#update_trusted_token_issuer)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_assignment_creation_status"]
    ) -> ListAccountAssignmentCreationStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentCreationStatus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountassignmentcreationstatuspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_assignment_deletion_status"]
    ) -> ListAccountAssignmentDeletionStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentDeletionStatus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountassignmentdeletionstatuspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_assignments"]
    ) -> ListAccountAssignmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountassignmentspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_assignments_for_principal"]
    ) -> ListAccountAssignmentsForPrincipalPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentsForPrincipal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountassignmentsforprincipalpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_accounts_for_provisioned_permission_set"]
    ) -> ListAccountsForProvisionedPermissionSetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountsForProvisionedPermissionSet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountsforprovisionedpermissionsetpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_access_scopes"]
    ) -> ListApplicationAccessScopesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplicationAccessScopes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationaccessscopespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_assignments"]
    ) -> ListApplicationAssignmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplicationAssignments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationassignmentspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_assignments_for_principal"]
    ) -> ListApplicationAssignmentsForPrincipalPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplicationAssignmentsForPrincipal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationassignmentsforprincipalpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_authentication_methods"]
    ) -> ListApplicationAuthenticationMethodsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplicationAuthenticationMethods)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationauthenticationmethodspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_grants"]
    ) -> ListApplicationGrantsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplicationGrants)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationgrantspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_providers"]
    ) -> ListApplicationProvidersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplicationProviders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationproviderspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_customer_managed_policy_references_in_permission_set"]
    ) -> ListCustomerManagedPolicyReferencesInPermissionSetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListCustomerManagedPolicyReferencesInPermissionSet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listcustomermanagedpolicyreferencesinpermissionsetpaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_instances"]) -> ListInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listinstancespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_managed_policies_in_permission_set"]
    ) -> ListManagedPoliciesInPermissionSetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListManagedPoliciesInPermissionSet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listmanagedpoliciesinpermissionsetpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_permission_set_provisioning_status"]
    ) -> ListPermissionSetProvisioningStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSetProvisioningStatus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listpermissionsetprovisioningstatuspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_permission_sets"]
    ) -> ListPermissionSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listpermissionsetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_permission_sets_provisioned_to_account"]
    ) -> ListPermissionSetsProvisionedToAccountPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSetsProvisionedToAccount)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listpermissionsetsprovisionedtoaccountpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListTagsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listtagsforresourcepaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_trusted_token_issuers"]
    ) -> ListTrustedTokenIssuersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListTrustedTokenIssuers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listtrustedtokenissuerspaginator)
        """
