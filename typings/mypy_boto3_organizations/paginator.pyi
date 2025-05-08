"""
Type annotations for organizations service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_organizations.client import OrganizationsClient
    from mypy_boto3_organizations.paginator import (
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
    )

    session = Session()
    client: OrganizationsClient = session.client("organizations")

    list_aws_service_access_for_organization_paginator: ListAWSServiceAccessForOrganizationPaginator = client.get_paginator("list_aws_service_access_for_organization")
    list_accounts_for_parent_paginator: ListAccountsForParentPaginator = client.get_paginator("list_accounts_for_parent")
    list_accounts_paginator: ListAccountsPaginator = client.get_paginator("list_accounts")
    list_children_paginator: ListChildrenPaginator = client.get_paginator("list_children")
    list_create_account_status_paginator: ListCreateAccountStatusPaginator = client.get_paginator("list_create_account_status")
    list_delegated_administrators_paginator: ListDelegatedAdministratorsPaginator = client.get_paginator("list_delegated_administrators")
    list_delegated_services_for_account_paginator: ListDelegatedServicesForAccountPaginator = client.get_paginator("list_delegated_services_for_account")
    list_handshakes_for_account_paginator: ListHandshakesForAccountPaginator = client.get_paginator("list_handshakes_for_account")
    list_handshakes_for_organization_paginator: ListHandshakesForOrganizationPaginator = client.get_paginator("list_handshakes_for_organization")
    list_organizational_units_for_parent_paginator: ListOrganizationalUnitsForParentPaginator = client.get_paginator("list_organizational_units_for_parent")
    list_parents_paginator: ListParentsPaginator = client.get_paginator("list_parents")
    list_policies_for_target_paginator: ListPoliciesForTargetPaginator = client.get_paginator("list_policies_for_target")
    list_policies_paginator: ListPoliciesPaginator = client.get_paginator("list_policies")
    list_roots_paginator: ListRootsPaginator = client.get_paginator("list_roots")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_targets_for_policy_paginator: ListTargetsForPolicyPaginator = client.get_paginator("list_targets_for_policy")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAccountsForParentRequestPaginateTypeDef,
    ListAccountsForParentResponseTypeDef,
    ListAccountsRequestPaginateTypeDef,
    ListAccountsResponseTypeDef,
    ListAWSServiceAccessForOrganizationRequestPaginateTypeDef,
    ListAWSServiceAccessForOrganizationResponseTypeDef,
    ListChildrenRequestPaginateTypeDef,
    ListChildrenResponseTypeDef,
    ListCreateAccountStatusRequestPaginateTypeDef,
    ListCreateAccountStatusResponseTypeDef,
    ListDelegatedAdministratorsRequestPaginateTypeDef,
    ListDelegatedAdministratorsResponseTypeDef,
    ListDelegatedServicesForAccountRequestPaginateTypeDef,
    ListDelegatedServicesForAccountResponseTypeDef,
    ListHandshakesForAccountRequestPaginateTypeDef,
    ListHandshakesForAccountResponsePaginatorTypeDef,
    ListHandshakesForOrganizationRequestPaginateTypeDef,
    ListHandshakesForOrganizationResponsePaginatorTypeDef,
    ListOrganizationalUnitsForParentRequestPaginateTypeDef,
    ListOrganizationalUnitsForParentResponseTypeDef,
    ListParentsRequestPaginateTypeDef,
    ListParentsResponseTypeDef,
    ListPoliciesForTargetRequestPaginateTypeDef,
    ListPoliciesForTargetResponseTypeDef,
    ListPoliciesRequestPaginateTypeDef,
    ListPoliciesResponseTypeDef,
    ListRootsRequestPaginateTypeDef,
    ListRootsResponseTypeDef,
    ListTagsForResourceRequestPaginateTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetsForPolicyRequestPaginateTypeDef,
    ListTargetsForPolicyResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
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
)

if TYPE_CHECKING:
    _ListAWSServiceAccessForOrganizationPaginatorBase = Paginator[
        ListAWSServiceAccessForOrganizationResponseTypeDef
    ]
else:
    _ListAWSServiceAccessForOrganizationPaginatorBase = Paginator  # type: ignore[assignment]

class ListAWSServiceAccessForOrganizationPaginator(
    _ListAWSServiceAccessForOrganizationPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListAWSServiceAccessForOrganization.html#Organizations.Paginator.ListAWSServiceAccessForOrganization)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listawsserviceaccessfororganizationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAWSServiceAccessForOrganizationRequestPaginateTypeDef]
    ) -> PageIterator[ListAWSServiceAccessForOrganizationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListAWSServiceAccessForOrganization.html#Organizations.Paginator.ListAWSServiceAccessForOrganization.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listawsserviceaccessfororganizationpaginator)
        """

if TYPE_CHECKING:
    _ListAccountsForParentPaginatorBase = Paginator[ListAccountsForParentResponseTypeDef]
else:
    _ListAccountsForParentPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccountsForParentPaginator(_ListAccountsForParentPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListAccountsForParent.html#Organizations.Paginator.ListAccountsForParent)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listaccountsforparentpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccountsForParentRequestPaginateTypeDef]
    ) -> PageIterator[ListAccountsForParentResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListAccountsForParent.html#Organizations.Paginator.ListAccountsForParent.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listaccountsforparentpaginator)
        """

if TYPE_CHECKING:
    _ListAccountsPaginatorBase = Paginator[ListAccountsResponseTypeDef]
else:
    _ListAccountsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccountsPaginator(_ListAccountsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListAccounts.html#Organizations.Paginator.ListAccounts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listaccountspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccountsRequestPaginateTypeDef]
    ) -> PageIterator[ListAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListAccounts.html#Organizations.Paginator.ListAccounts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listaccountspaginator)
        """

if TYPE_CHECKING:
    _ListChildrenPaginatorBase = Paginator[ListChildrenResponseTypeDef]
else:
    _ListChildrenPaginatorBase = Paginator  # type: ignore[assignment]

class ListChildrenPaginator(_ListChildrenPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListChildren.html#Organizations.Paginator.ListChildren)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listchildrenpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListChildrenRequestPaginateTypeDef]
    ) -> PageIterator[ListChildrenResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListChildren.html#Organizations.Paginator.ListChildren.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listchildrenpaginator)
        """

if TYPE_CHECKING:
    _ListCreateAccountStatusPaginatorBase = Paginator[ListCreateAccountStatusResponseTypeDef]
else:
    _ListCreateAccountStatusPaginatorBase = Paginator  # type: ignore[assignment]

class ListCreateAccountStatusPaginator(_ListCreateAccountStatusPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListCreateAccountStatus.html#Organizations.Paginator.ListCreateAccountStatus)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listcreateaccountstatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCreateAccountStatusRequestPaginateTypeDef]
    ) -> PageIterator[ListCreateAccountStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListCreateAccountStatus.html#Organizations.Paginator.ListCreateAccountStatus.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listcreateaccountstatuspaginator)
        """

if TYPE_CHECKING:
    _ListDelegatedAdministratorsPaginatorBase = Paginator[
        ListDelegatedAdministratorsResponseTypeDef
    ]
else:
    _ListDelegatedAdministratorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDelegatedAdministratorsPaginator(_ListDelegatedAdministratorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListDelegatedAdministrators.html#Organizations.Paginator.ListDelegatedAdministrators)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listdelegatedadministratorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDelegatedAdministratorsRequestPaginateTypeDef]
    ) -> PageIterator[ListDelegatedAdministratorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListDelegatedAdministrators.html#Organizations.Paginator.ListDelegatedAdministrators.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listdelegatedadministratorspaginator)
        """

if TYPE_CHECKING:
    _ListDelegatedServicesForAccountPaginatorBase = Paginator[
        ListDelegatedServicesForAccountResponseTypeDef
    ]
else:
    _ListDelegatedServicesForAccountPaginatorBase = Paginator  # type: ignore[assignment]

class ListDelegatedServicesForAccountPaginator(_ListDelegatedServicesForAccountPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListDelegatedServicesForAccount.html#Organizations.Paginator.ListDelegatedServicesForAccount)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listdelegatedservicesforaccountpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDelegatedServicesForAccountRequestPaginateTypeDef]
    ) -> PageIterator[ListDelegatedServicesForAccountResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListDelegatedServicesForAccount.html#Organizations.Paginator.ListDelegatedServicesForAccount.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listdelegatedservicesforaccountpaginator)
        """

if TYPE_CHECKING:
    _ListHandshakesForAccountPaginatorBase = Paginator[
        ListHandshakesForAccountResponsePaginatorTypeDef
    ]
else:
    _ListHandshakesForAccountPaginatorBase = Paginator  # type: ignore[assignment]

class ListHandshakesForAccountPaginator(_ListHandshakesForAccountPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListHandshakesForAccount.html#Organizations.Paginator.ListHandshakesForAccount)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listhandshakesforaccountpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListHandshakesForAccountRequestPaginateTypeDef]
    ) -> PageIterator[ListHandshakesForAccountResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListHandshakesForAccount.html#Organizations.Paginator.ListHandshakesForAccount.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listhandshakesforaccountpaginator)
        """

if TYPE_CHECKING:
    _ListHandshakesForOrganizationPaginatorBase = Paginator[
        ListHandshakesForOrganizationResponsePaginatorTypeDef
    ]
else:
    _ListHandshakesForOrganizationPaginatorBase = Paginator  # type: ignore[assignment]

class ListHandshakesForOrganizationPaginator(_ListHandshakesForOrganizationPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListHandshakesForOrganization.html#Organizations.Paginator.ListHandshakesForOrganization)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listhandshakesfororganizationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListHandshakesForOrganizationRequestPaginateTypeDef]
    ) -> PageIterator[ListHandshakesForOrganizationResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListHandshakesForOrganization.html#Organizations.Paginator.ListHandshakesForOrganization.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listhandshakesfororganizationpaginator)
        """

if TYPE_CHECKING:
    _ListOrganizationalUnitsForParentPaginatorBase = Paginator[
        ListOrganizationalUnitsForParentResponseTypeDef
    ]
else:
    _ListOrganizationalUnitsForParentPaginatorBase = Paginator  # type: ignore[assignment]

class ListOrganizationalUnitsForParentPaginator(_ListOrganizationalUnitsForParentPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListOrganizationalUnitsForParent.html#Organizations.Paginator.ListOrganizationalUnitsForParent)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listorganizationalunitsforparentpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOrganizationalUnitsForParentRequestPaginateTypeDef]
    ) -> PageIterator[ListOrganizationalUnitsForParentResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListOrganizationalUnitsForParent.html#Organizations.Paginator.ListOrganizationalUnitsForParent.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listorganizationalunitsforparentpaginator)
        """

if TYPE_CHECKING:
    _ListParentsPaginatorBase = Paginator[ListParentsResponseTypeDef]
else:
    _ListParentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListParentsPaginator(_ListParentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListParents.html#Organizations.Paginator.ListParents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listparentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListParentsRequestPaginateTypeDef]
    ) -> PageIterator[ListParentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListParents.html#Organizations.Paginator.ListParents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listparentspaginator)
        """

if TYPE_CHECKING:
    _ListPoliciesForTargetPaginatorBase = Paginator[ListPoliciesForTargetResponseTypeDef]
else:
    _ListPoliciesForTargetPaginatorBase = Paginator  # type: ignore[assignment]

class ListPoliciesForTargetPaginator(_ListPoliciesForTargetPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListPoliciesForTarget.html#Organizations.Paginator.ListPoliciesForTarget)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listpoliciesfortargetpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPoliciesForTargetRequestPaginateTypeDef]
    ) -> PageIterator[ListPoliciesForTargetResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListPoliciesForTarget.html#Organizations.Paginator.ListPoliciesForTarget.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listpoliciesfortargetpaginator)
        """

if TYPE_CHECKING:
    _ListPoliciesPaginatorBase = Paginator[ListPoliciesResponseTypeDef]
else:
    _ListPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListPoliciesPaginator(_ListPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListPolicies.html#Organizations.Paginator.ListPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listpoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListPolicies.html#Organizations.Paginator.ListPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listpoliciespaginator)
        """

if TYPE_CHECKING:
    _ListRootsPaginatorBase = Paginator[ListRootsResponseTypeDef]
else:
    _ListRootsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRootsPaginator(_ListRootsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListRoots.html#Organizations.Paginator.ListRoots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listrootspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRootsRequestPaginateTypeDef]
    ) -> PageIterator[ListRootsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListRoots.html#Organizations.Paginator.ListRoots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listrootspaginator)
        """

if TYPE_CHECKING:
    _ListTagsForResourcePaginatorBase = Paginator[ListTagsForResourceResponseTypeDef]
else:
    _ListTagsForResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsForResourcePaginator(_ListTagsForResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListTagsForResource.html#Organizations.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listtagsforresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsForResourceRequestPaginateTypeDef]
    ) -> PageIterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListTagsForResource.html#Organizations.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listtagsforresourcepaginator)
        """

if TYPE_CHECKING:
    _ListTargetsForPolicyPaginatorBase = Paginator[ListTargetsForPolicyResponseTypeDef]
else:
    _ListTargetsForPolicyPaginatorBase = Paginator  # type: ignore[assignment]

class ListTargetsForPolicyPaginator(_ListTargetsForPolicyPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListTargetsForPolicy.html#Organizations.Paginator.ListTargetsForPolicy)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listtargetsforpolicypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTargetsForPolicyRequestPaginateTypeDef]
    ) -> PageIterator[ListTargetsForPolicyResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/paginator/ListTargetsForPolicy.html#Organizations.Paginator.ListTargetsForPolicy.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators/#listtargetsforpolicypaginator)
        """
