"""
Main interface for organizations service.

Usage::

    ```python
    import boto3
    from mypy_boto3_organizations import (
        Client,
        ListAWSServiceAccessForOrganizationPaginator,
        ListAccountsForParentPaginator,
        ListAccountsPaginator,
        ListChildrenPaginator,
        ListCreateAccountStatusPaginator,
        ListDelegatedAdministratorsPaginator,
        ListDelegatedServicesForAccountPaginator,
        ListHandshakesForAccountPaginator,
        ListHandshakesForOrganizationPaginator,
        ListOrganizationalUnitsForParentPaginator,
        ListParentsPaginator,
        ListPoliciesForTargetPaginator,
        ListPoliciesPaginator,
        ListRootsPaginator,
        ListTagsForResourcePaginator,
        ListTargetsForPolicyPaginator,
        OrganizationsClient,
    )

    session = boto3.Session()

    client: OrganizationsClient = boto3.client("organizations")
    session_client: OrganizationsClient = session.client("organizations")

    list_aws_service_access_for_organization_paginator: ListAWSServiceAccessForOrganizationPaginator = client.get_paginator("list_aws_service_access_for_organization")
    list_accounts_paginator: ListAccountsPaginator = client.get_paginator("list_accounts")
    list_accounts_for_parent_paginator: ListAccountsForParentPaginator = client.get_paginator("list_accounts_for_parent")
    list_children_paginator: ListChildrenPaginator = client.get_paginator("list_children")
    list_create_account_status_paginator: ListCreateAccountStatusPaginator = client.get_paginator("list_create_account_status")
    list_delegated_administrators_paginator: ListDelegatedAdministratorsPaginator = client.get_paginator("list_delegated_administrators")
    list_delegated_services_for_account_paginator: ListDelegatedServicesForAccountPaginator = client.get_paginator("list_delegated_services_for_account")
    list_handshakes_for_account_paginator: ListHandshakesForAccountPaginator = client.get_paginator("list_handshakes_for_account")
    list_handshakes_for_organization_paginator: ListHandshakesForOrganizationPaginator = client.get_paginator("list_handshakes_for_organization")
    list_organizational_units_for_parent_paginator: ListOrganizationalUnitsForParentPaginator = client.get_paginator("list_organizational_units_for_parent")
    list_parents_paginator: ListParentsPaginator = client.get_paginator("list_parents")
    list_policies_paginator: ListPoliciesPaginator = client.get_paginator("list_policies")
    list_policies_for_target_paginator: ListPoliciesForTargetPaginator = client.get_paginator("list_policies_for_target")
    list_roots_paginator: ListRootsPaginator = client.get_paginator("list_roots")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_targets_for_policy_paginator: ListTargetsForPolicyPaginator = client.get_paginator("list_targets_for_policy")
    ```
"""
from .client import OrganizationsClient
from .paginator import (
    ListAccountsForParentPaginator,
    ListAccountsPaginator,
    ListAWSServiceAccessForOrganizationPaginator,
    ListChildrenPaginator,
    ListCreateAccountStatusPaginator,
    ListDelegatedAdministratorsPaginator,
    ListDelegatedServicesForAccountPaginator,
    ListHandshakesForAccountPaginator,
    ListHandshakesForOrganizationPaginator,
    ListOrganizationalUnitsForParentPaginator,
    ListParentsPaginator,
    ListPoliciesForTargetPaginator,
    ListPoliciesPaginator,
    ListRootsPaginator,
    ListTagsForResourcePaginator,
    ListTargetsForPolicyPaginator,
)

Client = OrganizationsClient

__all__ = (
    "Client",
    "ListAWSServiceAccessForOrganizationPaginator",
    "ListAccountsForParentPaginator",
    "ListAccountsPaginator",
    "ListChildrenPaginator",
    "ListCreateAccountStatusPaginator",
    "ListDelegatedAdministratorsPaginator",
    "ListDelegatedServicesForAccountPaginator",
    "ListHandshakesForAccountPaginator",
    "ListHandshakesForOrganizationPaginator",
    "ListOrganizationalUnitsForParentPaginator",
    "ListParentsPaginator",
    "ListPoliciesForTargetPaginator",
    "ListPoliciesPaginator",
    "ListRootsPaginator",
    "ListTagsForResourcePaginator",
    "ListTargetsForPolicyPaginator",
    "OrganizationsClient",
)
