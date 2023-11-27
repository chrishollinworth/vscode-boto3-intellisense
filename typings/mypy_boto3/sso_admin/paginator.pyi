"""
Type annotations for sso-admin service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_sso_admin import SSOAdminClient
    from mypy_boto3_sso_admin.paginator import (
        ListAccountAssignmentCreationStatusPaginator,
        ListAccountAssignmentDeletionStatusPaginator,
        ListAccountAssignmentsPaginator,
        ListAccountAssignmentsForPrincipalPaginator,
        ListAccountsForProvisionedPermissionSetPaginator,
        ListApplicationAccessScopesPaginator,
        ListApplicationAssignmentsPaginator,
        ListApplicationAssignmentsForPrincipalPaginator,
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

    client: SSOAdminClient = boto3.client("sso-admin")

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
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import PrincipalTypeType, ProvisioningStatusType
from .type_defs import (
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
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListAccountAssignmentCreationStatusPaginator",
    "ListAccountAssignmentDeletionStatusPaginator",
    "ListAccountAssignmentsPaginator",
    "ListAccountAssignmentsForPrincipalPaginator",
    "ListAccountsForProvisionedPermissionSetPaginator",
    "ListApplicationAccessScopesPaginator",
    "ListApplicationAssignmentsPaginator",
    "ListApplicationAssignmentsForPrincipalPaginator",
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
)

class ListAccountAssignmentCreationStatusPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentCreationStatus)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountassignmentcreationstatuspaginator)
    """

    def paginate(
        self,
        *,
        InstanceArn: str,
        Filter: "OperationStatusFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountAssignmentCreationStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentCreationStatus.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountassignmentcreationstatuspaginator)
        """

class ListAccountAssignmentDeletionStatusPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentDeletionStatus)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountassignmentdeletionstatuspaginator)
    """

    def paginate(
        self,
        *,
        InstanceArn: str,
        Filter: "OperationStatusFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountAssignmentDeletionStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentDeletionStatus.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountassignmentdeletionstatuspaginator)
        """

class ListAccountAssignmentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountassignmentspaginator)
    """

    def paginate(
        self,
        *,
        AccountId: str,
        InstanceArn: str,
        PermissionSetArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountAssignmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountassignmentspaginator)
        """

class ListAccountAssignmentsForPrincipalPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentsForPrincipal)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountassignmentsforprincipalpaginator)
    """

    def paginate(
        self,
        *,
        InstanceArn: str,
        PrincipalId: str,
        PrincipalType: PrincipalTypeType,
        Filter: "ListAccountAssignmentsFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountAssignmentsForPrincipalResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentsForPrincipal.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountassignmentsforprincipalpaginator)
        """

class ListAccountsForProvisionedPermissionSetPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountsForProvisionedPermissionSet)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountsforprovisionedpermissionsetpaginator)
    """

    def paginate(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        ProvisioningStatus: ProvisioningStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountsForProvisionedPermissionSetResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountsForProvisionedPermissionSet.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountsforprovisionedpermissionsetpaginator)
        """

class ListApplicationAccessScopesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplicationAccessScopes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationaccessscopespaginator)
    """

    def paginate(
        self, *, ApplicationArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationAccessScopesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplicationAccessScopes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationaccessscopespaginator)
        """

class ListApplicationAssignmentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplicationAssignments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationassignmentspaginator)
    """

    def paginate(
        self, *, ApplicationArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationAssignmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplicationAssignments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationassignmentspaginator)
        """

class ListApplicationAssignmentsForPrincipalPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplicationAssignmentsForPrincipal)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationassignmentsforprincipalpaginator)
    """

    def paginate(
        self,
        *,
        InstanceArn: str,
        PrincipalId: str,
        PrincipalType: PrincipalTypeType,
        Filter: "ListApplicationAssignmentsFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationAssignmentsForPrincipalResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplicationAssignmentsForPrincipal.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationassignmentsforprincipalpaginator)
        """

class ListApplicationAuthenticationMethodsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplicationAuthenticationMethods)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationauthenticationmethodspaginator)
    """

    def paginate(
        self, *, ApplicationArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationAuthenticationMethodsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplicationAuthenticationMethods.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationauthenticationmethodspaginator)
        """

class ListApplicationGrantsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplicationGrants)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationgrantspaginator)
    """

    def paginate(
        self, *, ApplicationArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationGrantsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplicationGrants.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationgrantspaginator)
        """

class ListApplicationProvidersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplicationProviders)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationproviderspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationProvidersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplicationProviders.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationproviderspaginator)
        """

class ListApplicationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationspaginator)
    """

    def paginate(
        self,
        *,
        InstanceArn: str,
        Filter: "ListApplicationsFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listapplicationspaginator)
        """

class ListCustomerManagedPolicyReferencesInPermissionSetPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListCustomerManagedPolicyReferencesInPermissionSet)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listcustomermanagedpolicyreferencesinpermissionsetpaginator)
    """

    def paginate(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListCustomerManagedPolicyReferencesInPermissionSet.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listcustomermanagedpolicyreferencesinpermissionsetpaginator)
        """

class ListInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListInstances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listinstancespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListInstances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listinstancespaginator)
        """

class ListManagedPoliciesInPermissionSetPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListManagedPoliciesInPermissionSet)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listmanagedpoliciesinpermissionsetpaginator)
    """

    def paginate(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListManagedPoliciesInPermissionSetResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListManagedPoliciesInPermissionSet.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listmanagedpoliciesinpermissionsetpaginator)
        """

class ListPermissionSetProvisioningStatusPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSetProvisioningStatus)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listpermissionsetprovisioningstatuspaginator)
    """

    def paginate(
        self,
        *,
        InstanceArn: str,
        Filter: "OperationStatusFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPermissionSetProvisioningStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSetProvisioningStatus.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listpermissionsetprovisioningstatuspaginator)
        """

class ListPermissionSetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listpermissionsetspaginator)
    """

    def paginate(
        self, *, InstanceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPermissionSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listpermissionsetspaginator)
        """

class ListPermissionSetsProvisionedToAccountPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSetsProvisionedToAccount)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listpermissionsetsprovisionedtoaccountpaginator)
    """

    def paginate(
        self,
        *,
        AccountId: str,
        InstanceArn: str,
        ProvisioningStatus: ProvisioningStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPermissionSetsProvisionedToAccountResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSetsProvisionedToAccount.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listpermissionsetsprovisionedtoaccountpaginator)
        """

class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listtagsforresourcepaginator)
    """

    def paginate(
        self,
        *,
        ResourceArn: str,
        InstanceArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listtagsforresourcepaginator)
        """

class ListTrustedTokenIssuersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListTrustedTokenIssuers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listtrustedtokenissuerspaginator)
    """

    def paginate(
        self, *, InstanceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTrustedTokenIssuersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sso-admin.html#SSOAdmin.Paginator.ListTrustedTokenIssuers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listtrustedtokenissuerspaginator)
        """
