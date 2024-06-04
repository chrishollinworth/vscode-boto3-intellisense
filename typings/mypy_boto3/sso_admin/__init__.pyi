"""
Main interface for sso-admin service.

Usage::

    ```python
    import boto3
    from mypy_boto3_sso_admin import (
        Client,
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
        SSOAdminClient,
    )

    session = boto3.Session()

    client: SSOAdminClient = boto3.client("sso-admin")
    session_client: SSOAdminClient = session.client("sso-admin")

    list_account_assignment_creation_status_paginator: ListAccountAssignmentCreationStatusPaginator = client.get_paginator("list_account_assignment_creation_status")
    list_account_assignment_deletion_status_paginator: ListAccountAssignmentDeletionStatusPaginator = client.get_paginator("list_account_assignment_deletion_status")
    list_account_assignments_paginator: ListAccountAssignmentsPaginator = client.get_paginator("list_account_assignments")
    list_account_assignments_for_principal_paginator: ListAccountAssignmentsForPrincipalPaginator = client.get_paginator("list_account_assignments_for_principal")
    list_accounts_for_provisioned_permission_set_paginator: ListAccountsForProvisionedPermissionSetPaginator = client.get_paginator("list_accounts_for_provisioned_permission_set")
    list_application_access_scopes_paginator: ListApplicationAccessScopesPaginator = client.get_paginator("list_application_access_scopes")
    list_application_assignments_paginator: ListApplicationAssignmentsPaginator = client.get_paginator("list_application_assignments")
    list_application_assignments_for_principal_paginator: ListApplicationAssignmentsForPrincipalPaginator = client.get_paginator("list_application_assignments_for_principal")
    list_application_authentication_methods_paginator: ListApplicationAuthenticationMethodsPaginator = client.get_paginator("list_application_authentication_methods")
    list_application_grants_paginator: ListApplicationGrantsPaginator = client.get_paginator("list_application_grants")
    list_application_providers_paginator: ListApplicationProvidersPaginator = client.get_paginator("list_application_providers")
    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_customer_managed_policy_references_in_permission_set_paginator: ListCustomerManagedPolicyReferencesInPermissionSetPaginator = client.get_paginator("list_customer_managed_policy_references_in_permission_set")
    list_instances_paginator: ListInstancesPaginator = client.get_paginator("list_instances")
    list_managed_policies_in_permission_set_paginator: ListManagedPoliciesInPermissionSetPaginator = client.get_paginator("list_managed_policies_in_permission_set")
    list_permission_set_provisioning_status_paginator: ListPermissionSetProvisioningStatusPaginator = client.get_paginator("list_permission_set_provisioning_status")
    list_permission_sets_paginator: ListPermissionSetsPaginator = client.get_paginator("list_permission_sets")
    list_permission_sets_provisioned_to_account_paginator: ListPermissionSetsProvisionedToAccountPaginator = client.get_paginator("list_permission_sets_provisioned_to_account")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_trusted_token_issuers_paginator: ListTrustedTokenIssuersPaginator = client.get_paginator("list_trusted_token_issuers")
    ```
"""

from .client import SSOAdminClient
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

Client = SSOAdminClient

__all__ = (
    "Client",
    "ListAccountAssignmentCreationStatusPaginator",
    "ListAccountAssignmentDeletionStatusPaginator",
    "ListAccountAssignmentsForPrincipalPaginator",
    "ListAccountAssignmentsPaginator",
    "ListAccountsForProvisionedPermissionSetPaginator",
    "ListApplicationAccessScopesPaginator",
    "ListApplicationAssignmentsForPrincipalPaginator",
    "ListApplicationAssignmentsPaginator",
    "ListApplicationAuthenticationMethodsPaginator",
    "ListApplicationGrantsPaginator",
    "ListApplicationProvidersPaginator",
    "ListApplicationsPaginator",
    "ListCustomerManagedPolicyReferencesInPermissionSetPaginator",
    "ListInstancesPaginator",
    "ListManagedPoliciesInPermissionSetPaginator",
    "ListPermissionSetProvisioningStatusPaginator",
    "ListPermissionSetsPaginator",
    "ListPermissionSetsProvisionedToAccountPaginator",
    "ListTagsForResourcePaginator",
    "ListTrustedTokenIssuersPaginator",
    "SSOAdminClient",
)
