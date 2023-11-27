"""
Type annotations for sso-admin service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/literals.html)

Usage::

    ```python
    from mypy_boto3_sso_admin.literals import ApplicationStatusType

    data: ApplicationStatusType = "DISABLED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ApplicationStatusType",
    "ApplicationVisibilityType",
    "AuthenticationMethodTypeType",
    "FederationProtocolType",
    "GrantTypeType",
    "InstanceAccessControlAttributeConfigurationStatusType",
    "InstanceStatusType",
    "JwksRetrievalOptionType",
    "ListAccountAssignmentCreationStatusPaginatorName",
    "ListAccountAssignmentDeletionStatusPaginatorName",
    "ListAccountAssignmentsForPrincipalPaginatorName",
    "ListAccountAssignmentsPaginatorName",
    "ListAccountsForProvisionedPermissionSetPaginatorName",
    "ListApplicationAccessScopesPaginatorName",
    "ListApplicationAssignmentsForPrincipalPaginatorName",
    "ListApplicationAssignmentsPaginatorName",
    "ListApplicationAuthenticationMethodsPaginatorName",
    "ListApplicationGrantsPaginatorName",
    "ListApplicationProvidersPaginatorName",
    "ListApplicationsPaginatorName",
    "ListCustomerManagedPolicyReferencesInPermissionSetPaginatorName",
    "ListInstancesPaginatorName",
    "ListManagedPoliciesInPermissionSetPaginatorName",
    "ListPermissionSetProvisioningStatusPaginatorName",
    "ListPermissionSetsPaginatorName",
    "ListPermissionSetsProvisionedToAccountPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ListTrustedTokenIssuersPaginatorName",
    "PrincipalTypeType",
    "ProvisionTargetTypeType",
    "ProvisioningStatusType",
    "SignInOriginType",
    "StatusValuesType",
    "TargetTypeType",
    "TrustedTokenIssuerTypeType",
)

ApplicationStatusType = Literal["DISABLED", "ENABLED"]
ApplicationVisibilityType = Literal["DISABLED", "ENABLED"]
AuthenticationMethodTypeType = Literal["IAM"]
FederationProtocolType = Literal["OAUTH", "SAML"]
GrantTypeType = Literal[
    "authorization_code",
    "refresh_token",
    "urn:ietf:params:oauth:grant-type:jwt-bearer",
    "urn:ietf:params:oauth:grant-type:token-exchange",
]
InstanceAccessControlAttributeConfigurationStatusType = Literal[
    "CREATION_FAILED", "CREATION_IN_PROGRESS", "ENABLED"
]
InstanceStatusType = Literal["ACTIVE", "CREATE_IN_PROGRESS", "DELETE_IN_PROGRESS"]
JwksRetrievalOptionType = Literal["OPEN_ID_DISCOVERY"]
ListAccountAssignmentCreationStatusPaginatorName = Literal[
    "list_account_assignment_creation_status"
]
ListAccountAssignmentDeletionStatusPaginatorName = Literal[
    "list_account_assignment_deletion_status"
]
ListAccountAssignmentsForPrincipalPaginatorName = Literal["list_account_assignments_for_principal"]
ListAccountAssignmentsPaginatorName = Literal["list_account_assignments"]
ListAccountsForProvisionedPermissionSetPaginatorName = Literal[
    "list_accounts_for_provisioned_permission_set"
]
ListApplicationAccessScopesPaginatorName = Literal["list_application_access_scopes"]
ListApplicationAssignmentsForPrincipalPaginatorName = Literal[
    "list_application_assignments_for_principal"
]
ListApplicationAssignmentsPaginatorName = Literal["list_application_assignments"]
ListApplicationAuthenticationMethodsPaginatorName = Literal[
    "list_application_authentication_methods"
]
ListApplicationGrantsPaginatorName = Literal["list_application_grants"]
ListApplicationProvidersPaginatorName = Literal["list_application_providers"]
ListApplicationsPaginatorName = Literal["list_applications"]
ListCustomerManagedPolicyReferencesInPermissionSetPaginatorName = Literal[
    "list_customer_managed_policy_references_in_permission_set"
]
ListInstancesPaginatorName = Literal["list_instances"]
ListManagedPoliciesInPermissionSetPaginatorName = Literal["list_managed_policies_in_permission_set"]
ListPermissionSetProvisioningStatusPaginatorName = Literal[
    "list_permission_set_provisioning_status"
]
ListPermissionSetsPaginatorName = Literal["list_permission_sets"]
ListPermissionSetsProvisionedToAccountPaginatorName = Literal[
    "list_permission_sets_provisioned_to_account"
]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ListTrustedTokenIssuersPaginatorName = Literal["list_trusted_token_issuers"]
PrincipalTypeType = Literal["GROUP", "USER"]
ProvisionTargetTypeType = Literal["ALL_PROVISIONED_ACCOUNTS", "AWS_ACCOUNT"]
ProvisioningStatusType = Literal[
    "LATEST_PERMISSION_SET_NOT_PROVISIONED", "LATEST_PERMISSION_SET_PROVISIONED"
]
SignInOriginType = Literal["APPLICATION", "IDENTITY_CENTER"]
StatusValuesType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
TargetTypeType = Literal["AWS_ACCOUNT"]
TrustedTokenIssuerTypeType = Literal["OIDC_JWT"]
