"""
Main interface for fms service.

Usage::

    ```python
    import boto3
    from mypy_boto3_fms import (
        Client,
        FMSClient,
        ListAdminAccountsForOrganizationPaginator,
        ListAdminsManagingAccountPaginator,
        ListAppsListsPaginator,
        ListComplianceStatusPaginator,
        ListMemberAccountsPaginator,
        ListPoliciesPaginator,
        ListProtocolsListsPaginator,
        ListThirdPartyFirewallFirewallPoliciesPaginator,
    )

    session = boto3.Session()

    client: FMSClient = boto3.client("fms")
    session_client: FMSClient = session.client("fms")

    list_admin_accounts_for_organization_paginator: ListAdminAccountsForOrganizationPaginator = client.get_paginator("list_admin_accounts_for_organization")
    list_admins_managing_account_paginator: ListAdminsManagingAccountPaginator = client.get_paginator("list_admins_managing_account")
    list_apps_lists_paginator: ListAppsListsPaginator = client.get_paginator("list_apps_lists")
    list_compliance_status_paginator: ListComplianceStatusPaginator = client.get_paginator("list_compliance_status")
    list_member_accounts_paginator: ListMemberAccountsPaginator = client.get_paginator("list_member_accounts")
    list_policies_paginator: ListPoliciesPaginator = client.get_paginator("list_policies")
    list_protocols_lists_paginator: ListProtocolsListsPaginator = client.get_paginator("list_protocols_lists")
    list_third_party_firewall_firewall_policies_paginator: ListThirdPartyFirewallFirewallPoliciesPaginator = client.get_paginator("list_third_party_firewall_firewall_policies")
    ```
"""
from .client import FMSClient
from .paginator import (
    ListAdminAccountsForOrganizationPaginator,
    ListAdminsManagingAccountPaginator,
    ListAppsListsPaginator,
    ListComplianceStatusPaginator,
    ListMemberAccountsPaginator,
    ListPoliciesPaginator,
    ListProtocolsListsPaginator,
    ListThirdPartyFirewallFirewallPoliciesPaginator,
)

Client = FMSClient

__all__ = (
    "Client",
    "FMSClient",
    "ListAdminAccountsForOrganizationPaginator",
    "ListAdminsManagingAccountPaginator",
    "ListAppsListsPaginator",
    "ListComplianceStatusPaginator",
    "ListMemberAccountsPaginator",
    "ListPoliciesPaginator",
    "ListProtocolsListsPaginator",
    "ListThirdPartyFirewallFirewallPoliciesPaginator",
)
