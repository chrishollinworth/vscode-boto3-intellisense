"""
Type annotations for fms service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_fms.client import FMSClient
    from mypy_boto3_fms.paginator import (
        ListAdminAccountsForOrganizationPaginator,
        ListAdminsManagingAccountPaginator,
        ListAppsListsPaginator,
        ListComplianceStatusPaginator,
        ListMemberAccountsPaginator,
        ListPoliciesPaginator,
        ListProtocolsListsPaginator,
        ListThirdPartyFirewallFirewallPoliciesPaginator,
    )

    session = Session()
    client: FMSClient = session.client("fms")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAdminAccountsForOrganizationRequestPaginateTypeDef,
    ListAdminAccountsForOrganizationResponseTypeDef,
    ListAdminsManagingAccountRequestPaginateTypeDef,
    ListAdminsManagingAccountResponseTypeDef,
    ListAppsListsRequestPaginateTypeDef,
    ListAppsListsResponseTypeDef,
    ListComplianceStatusRequestPaginateTypeDef,
    ListComplianceStatusResponseTypeDef,
    ListMemberAccountsRequestPaginateTypeDef,
    ListMemberAccountsResponseTypeDef,
    ListPoliciesRequestPaginateTypeDef,
    ListPoliciesResponseTypeDef,
    ListProtocolsListsRequestPaginateTypeDef,
    ListProtocolsListsResponseTypeDef,
    ListThirdPartyFirewallFirewallPoliciesRequestPaginateTypeDef,
    ListThirdPartyFirewallFirewallPoliciesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAdminAccountsForOrganizationPaginator",
    "ListAdminsManagingAccountPaginator",
    "ListAppsListsPaginator",
    "ListComplianceStatusPaginator",
    "ListMemberAccountsPaginator",
    "ListPoliciesPaginator",
    "ListProtocolsListsPaginator",
    "ListThirdPartyFirewallFirewallPoliciesPaginator",
)

if TYPE_CHECKING:
    _ListAdminAccountsForOrganizationPaginatorBase = Paginator[
        ListAdminAccountsForOrganizationResponseTypeDef
    ]
else:
    _ListAdminAccountsForOrganizationPaginatorBase = Paginator  # type: ignore[assignment]

class ListAdminAccountsForOrganizationPaginator(_ListAdminAccountsForOrganizationPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/paginator/ListAdminAccountsForOrganization.html#FMS.Paginator.ListAdminAccountsForOrganization)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators/#listadminaccountsfororganizationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAdminAccountsForOrganizationRequestPaginateTypeDef]
    ) -> PageIterator[ListAdminAccountsForOrganizationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/paginator/ListAdminAccountsForOrganization.html#FMS.Paginator.ListAdminAccountsForOrganization.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators/#listadminaccountsfororganizationpaginator)
        """

if TYPE_CHECKING:
    _ListAdminsManagingAccountPaginatorBase = Paginator[ListAdminsManagingAccountResponseTypeDef]
else:
    _ListAdminsManagingAccountPaginatorBase = Paginator  # type: ignore[assignment]

class ListAdminsManagingAccountPaginator(_ListAdminsManagingAccountPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/paginator/ListAdminsManagingAccount.html#FMS.Paginator.ListAdminsManagingAccount)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators/#listadminsmanagingaccountpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAdminsManagingAccountRequestPaginateTypeDef]
    ) -> PageIterator[ListAdminsManagingAccountResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/paginator/ListAdminsManagingAccount.html#FMS.Paginator.ListAdminsManagingAccount.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators/#listadminsmanagingaccountpaginator)
        """

if TYPE_CHECKING:
    _ListAppsListsPaginatorBase = Paginator[ListAppsListsResponseTypeDef]
else:
    _ListAppsListsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAppsListsPaginator(_ListAppsListsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/paginator/ListAppsLists.html#FMS.Paginator.ListAppsLists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators/#listappslistspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAppsListsRequestPaginateTypeDef]
    ) -> PageIterator[ListAppsListsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/paginator/ListAppsLists.html#FMS.Paginator.ListAppsLists.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators/#listappslistspaginator)
        """

if TYPE_CHECKING:
    _ListComplianceStatusPaginatorBase = Paginator[ListComplianceStatusResponseTypeDef]
else:
    _ListComplianceStatusPaginatorBase = Paginator  # type: ignore[assignment]

class ListComplianceStatusPaginator(_ListComplianceStatusPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/paginator/ListComplianceStatus.html#FMS.Paginator.ListComplianceStatus)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators/#listcompliancestatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListComplianceStatusRequestPaginateTypeDef]
    ) -> PageIterator[ListComplianceStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/paginator/ListComplianceStatus.html#FMS.Paginator.ListComplianceStatus.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators/#listcompliancestatuspaginator)
        """

if TYPE_CHECKING:
    _ListMemberAccountsPaginatorBase = Paginator[ListMemberAccountsResponseTypeDef]
else:
    _ListMemberAccountsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMemberAccountsPaginator(_ListMemberAccountsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/paginator/ListMemberAccounts.html#FMS.Paginator.ListMemberAccounts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators/#listmemberaccountspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMemberAccountsRequestPaginateTypeDef]
    ) -> PageIterator[ListMemberAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/paginator/ListMemberAccounts.html#FMS.Paginator.ListMemberAccounts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators/#listmemberaccountspaginator)
        """

if TYPE_CHECKING:
    _ListPoliciesPaginatorBase = Paginator[ListPoliciesResponseTypeDef]
else:
    _ListPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListPoliciesPaginator(_ListPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/paginator/ListPolicies.html#FMS.Paginator.ListPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators/#listpoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/paginator/ListPolicies.html#FMS.Paginator.ListPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators/#listpoliciespaginator)
        """

if TYPE_CHECKING:
    _ListProtocolsListsPaginatorBase = Paginator[ListProtocolsListsResponseTypeDef]
else:
    _ListProtocolsListsPaginatorBase = Paginator  # type: ignore[assignment]

class ListProtocolsListsPaginator(_ListProtocolsListsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/paginator/ListProtocolsLists.html#FMS.Paginator.ListProtocolsLists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators/#listprotocolslistspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProtocolsListsRequestPaginateTypeDef]
    ) -> PageIterator[ListProtocolsListsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/paginator/ListProtocolsLists.html#FMS.Paginator.ListProtocolsLists.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators/#listprotocolslistspaginator)
        """

if TYPE_CHECKING:
    _ListThirdPartyFirewallFirewallPoliciesPaginatorBase = Paginator[
        ListThirdPartyFirewallFirewallPoliciesResponseTypeDef
    ]
else:
    _ListThirdPartyFirewallFirewallPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListThirdPartyFirewallFirewallPoliciesPaginator(
    _ListThirdPartyFirewallFirewallPoliciesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/paginator/ListThirdPartyFirewallFirewallPolicies.html#FMS.Paginator.ListThirdPartyFirewallFirewallPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators/#listthirdpartyfirewallfirewallpoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListThirdPartyFirewallFirewallPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListThirdPartyFirewallFirewallPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/paginator/ListThirdPartyFirewallFirewallPolicies.html#FMS.Paginator.ListThirdPartyFirewallFirewallPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators/#listthirdpartyfirewallfirewallpoliciespaginator)
        """
