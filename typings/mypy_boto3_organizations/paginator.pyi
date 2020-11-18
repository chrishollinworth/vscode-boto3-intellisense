# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for organizations service client paginators.

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
import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_organizations.type_defs import (
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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


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
    [Paginator.ListAWSServiceAccessForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListAWSServiceAccessForOrganization)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAWSServiceAccessForOrganizationResponseTypeDef]:
        """
        [ListAWSServiceAccessForOrganization.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListAWSServiceAccessForOrganization.paginate)
        """


class ListAccountsPaginator(Boto3Paginator):
    """
    [Paginator.ListAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListAccounts)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountsResponseTypeDef]:
        """
        [ListAccounts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListAccounts.paginate)
        """


class ListAccountsForParentPaginator(Boto3Paginator):
    """
    [Paginator.ListAccountsForParent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListAccountsForParent)
    """

    def paginate(
        self, ParentId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountsForParentResponseTypeDef]:
        """
        [ListAccountsForParent.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListAccountsForParent.paginate)
        """


class ListChildrenPaginator(Boto3Paginator):
    """
    [Paginator.ListChildren documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListChildren)
    """

    def paginate(
        self,
        ParentId: str,
        ChildType: Literal["ACCOUNT", "ORGANIZATIONAL_UNIT"],
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListChildrenResponseTypeDef]:
        """
        [ListChildren.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListChildren.paginate)
        """


class ListCreateAccountStatusPaginator(Boto3Paginator):
    """
    [Paginator.ListCreateAccountStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListCreateAccountStatus)
    """

    def paginate(
        self,
        States: List[Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListCreateAccountStatusResponseTypeDef]:
        """
        [ListCreateAccountStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListCreateAccountStatus.paginate)
        """


class ListDelegatedAdministratorsPaginator(Boto3Paginator):
    """
    [Paginator.ListDelegatedAdministrators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListDelegatedAdministrators)
    """

    def paginate(
        self, ServicePrincipal: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDelegatedAdministratorsResponseTypeDef]:
        """
        [ListDelegatedAdministrators.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListDelegatedAdministrators.paginate)
        """


class ListDelegatedServicesForAccountPaginator(Boto3Paginator):
    """
    [Paginator.ListDelegatedServicesForAccount documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListDelegatedServicesForAccount)
    """

    def paginate(
        self, AccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDelegatedServicesForAccountResponseTypeDef]:
        """
        [ListDelegatedServicesForAccount.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListDelegatedServicesForAccount.paginate)
        """


class ListHandshakesForAccountPaginator(Boto3Paginator):
    """
    [Paginator.ListHandshakesForAccount documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForAccount)
    """

    def paginate(
        self, Filter: HandshakeFilterTypeDef = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHandshakesForAccountResponseTypeDef]:
        """
        [ListHandshakesForAccount.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForAccount.paginate)
        """


class ListHandshakesForOrganizationPaginator(Boto3Paginator):
    """
    [Paginator.ListHandshakesForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForOrganization)
    """

    def paginate(
        self, Filter: HandshakeFilterTypeDef = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHandshakesForOrganizationResponseTypeDef]:
        """
        [ListHandshakesForOrganization.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForOrganization.paginate)
        """


class ListOrganizationalUnitsForParentPaginator(Boto3Paginator):
    """
    [Paginator.ListOrganizationalUnitsForParent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListOrganizationalUnitsForParent)
    """

    def paginate(
        self, ParentId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOrganizationalUnitsForParentResponseTypeDef]:
        """
        [ListOrganizationalUnitsForParent.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListOrganizationalUnitsForParent.paginate)
        """


class ListParentsPaginator(Boto3Paginator):
    """
    [Paginator.ListParents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListParents)
    """

    def paginate(
        self, ChildId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListParentsResponseTypeDef]:
        """
        [ListParents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListParents.paginate)
        """


class ListPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListPolicies)
    """

    def paginate(
        self,
        Filter: Literal[
            "SERVICE_CONTROL_POLICY", "TAG_POLICY", "BACKUP_POLICY", "AISERVICES_OPT_OUT_POLICY"
        ],
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPoliciesResponseTypeDef]:
        """
        [ListPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListPolicies.paginate)
        """


class ListPoliciesForTargetPaginator(Boto3Paginator):
    """
    [Paginator.ListPoliciesForTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListPoliciesForTarget)
    """

    def paginate(
        self,
        TargetId: str,
        Filter: Literal[
            "SERVICE_CONTROL_POLICY", "TAG_POLICY", "BACKUP_POLICY", "AISERVICES_OPT_OUT_POLICY"
        ],
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPoliciesForTargetResponseTypeDef]:
        """
        [ListPoliciesForTarget.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListPoliciesForTarget.paginate)
        """


class ListRootsPaginator(Boto3Paginator):
    """
    [Paginator.ListRoots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListRoots)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRootsResponseTypeDef]:
        """
        [ListRoots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListRoots.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListTagsForResource)
    """

    def paginate(
        self, ResourceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListTagsForResource.paginate)
        """


class ListTargetsForPolicyPaginator(Boto3Paginator):
    """
    [Paginator.ListTargetsForPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListTargetsForPolicy)
    """

    def paginate(
        self, PolicyId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTargetsForPolicyResponseTypeDef]:
        """
        [ListTargetsForPolicy.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListTargetsForPolicy.paginate)
        """
