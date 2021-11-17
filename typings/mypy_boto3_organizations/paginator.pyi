"""
Type annotations for organizations service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_organizations import OrganizationsClient
    from mypy_boto3_organizations.paginator import (
        ListAWSServiceAccessForOrganizationPaginator,
        ListAccountsPaginator,
        ListAccountsForParentPaginator,
        ListChildrenPaginator,
        ListCreateAccountStatusPaginator,
        ListDelegatedAdministratorsPaginator,
        ListDelegatedServicesForAccountPaginator,
        ListHandshakesForAccountPaginator,
        ListHandshakesForOrganizationPaginator,
        ListOrganizationalUnitsForParentPaginator,
        ListParentsPaginator,
        ListPoliciesPaginator,
        ListPoliciesForTargetPaginator,
        ListRootsPaginator,
        ListTagsForResourcePaginator,
        ListTargetsForPolicyPaginator,
    )

    client: OrganizationsClient = boto3.client("organizations")

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
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ChildTypeType, CreateAccountStateType, PolicyTypeType
from .type_defs import (
    HandshakeFilterTypeDef,
    ListAccountsForParentResponseTypeDef,
    ListAccountsResponseTypeDef,
    ListAWSServiceAccessForOrganizationResponseTypeDef,
    ListChildrenResponseTypeDef,
    ListCreateAccountStatusResponseTypeDef,
    ListDelegatedAdministratorsResponseTypeDef,
    ListDelegatedServicesForAccountResponseTypeDef,
    ListHandshakesForAccountResponseTypeDef,
    ListHandshakesForOrganizationResponseTypeDef,
    ListOrganizationalUnitsForParentResponseTypeDef,
    ListParentsResponseTypeDef,
    ListPoliciesForTargetResponseTypeDef,
    ListPoliciesResponseTypeDef,
    ListRootsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetsForPolicyResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListAWSServiceAccessForOrganizationPaginator",
    "ListAccountsPaginator",
    "ListAccountsForParentPaginator",
    "ListChildrenPaginator",
    "ListCreateAccountStatusPaginator",
    "ListDelegatedAdministratorsPaginator",
    "ListDelegatedServicesForAccountPaginator",
    "ListHandshakesForAccountPaginator",
    "ListHandshakesForOrganizationPaginator",
    "ListOrganizationalUnitsForParentPaginator",
    "ListParentsPaginator",
    "ListPoliciesPaginator",
    "ListPoliciesForTargetPaginator",
    "ListRootsPaginator",
    "ListTagsForResourcePaginator",
    "ListTargetsForPolicyPaginator",
)

class ListAWSServiceAccessForOrganizationPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListAWSServiceAccessForOrganization)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listawsserviceaccessfororganizationpaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAWSServiceAccessForOrganizationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListAWSServiceAccessForOrganization.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listawsserviceaccessfororganizationpaginator)
        """

class ListAccountsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListAccounts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listaccountspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListAccounts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listaccountspaginator)
        """

class ListAccountsForParentPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListAccountsForParent)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listaccountsforparentpaginator)
    """

    def paginate(
        self, *, ParentId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountsForParentResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListAccountsForParent.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listaccountsforparentpaginator)
        """

class ListChildrenPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListChildren)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listchildrenpaginator)
    """

    def paginate(
        self,
        *,
        ParentId: str,
        ChildType: ChildTypeType,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListChildrenResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListChildren.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listchildrenpaginator)
        """

class ListCreateAccountStatusPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListCreateAccountStatus)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listcreateaccountstatuspaginator)
    """

    def paginate(
        self,
        *,
        States: List[CreateAccountStateType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCreateAccountStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListCreateAccountStatus.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listcreateaccountstatuspaginator)
        """

class ListDelegatedAdministratorsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListDelegatedAdministrators)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listdelegatedadministratorspaginator)
    """

    def paginate(
        self, *, ServicePrincipal: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDelegatedAdministratorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListDelegatedAdministrators.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listdelegatedadministratorspaginator)
        """

class ListDelegatedServicesForAccountPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListDelegatedServicesForAccount)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listdelegatedservicesforaccountpaginator)
    """

    def paginate(
        self, *, AccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDelegatedServicesForAccountResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListDelegatedServicesForAccount.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listdelegatedservicesforaccountpaginator)
        """

class ListHandshakesForAccountPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForAccount)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listhandshakesforaccountpaginator)
    """

    def paginate(
        self,
        *,
        Filter: "HandshakeFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHandshakesForAccountResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForAccount.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listhandshakesforaccountpaginator)
        """

class ListHandshakesForOrganizationPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForOrganization)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listhandshakesfororganizationpaginator)
    """

    def paginate(
        self,
        *,
        Filter: "HandshakeFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHandshakesForOrganizationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForOrganization.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listhandshakesfororganizationpaginator)
        """

class ListOrganizationalUnitsForParentPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListOrganizationalUnitsForParent)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listorganizationalunitsforparentpaginator)
    """

    def paginate(
        self, *, ParentId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOrganizationalUnitsForParentResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListOrganizationalUnitsForParent.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listorganizationalunitsforparentpaginator)
        """

class ListParentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListParents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listparentspaginator)
    """

    def paginate(
        self, *, ChildId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListParentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListParents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listparentspaginator)
        """

class ListPoliciesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListPolicies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listpoliciespaginator)
    """

    def paginate(
        self, *, Filter: PolicyTypeType, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListPolicies.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listpoliciespaginator)
        """

class ListPoliciesForTargetPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListPoliciesForTarget)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listpoliciesfortargetpaginator)
    """

    def paginate(
        self,
        *,
        TargetId: str,
        Filter: PolicyTypeType,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPoliciesForTargetResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListPoliciesForTarget.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listpoliciesfortargetpaginator)
        """

class ListRootsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListRoots)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listrootspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRootsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListRoots.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listrootspaginator)
        """

class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listtagsforresourcepaginator)
    """

    def paginate(
        self, *, ResourceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listtagsforresourcepaginator)
        """

class ListTargetsForPolicyPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListTargetsForPolicy)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listtargetsforpolicypaginator)
    """

    def paginate(
        self, *, PolicyId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTargetsForPolicyResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/organizations.html#Organizations.Paginator.ListTargetsForPolicy.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listtargetsforpolicypaginator)
        """
