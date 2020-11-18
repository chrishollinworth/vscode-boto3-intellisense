# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for ram service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_ram import RAMClient
    from mypy_boto3_ram.paginator import (
        GetResourcePoliciesPaginator,
        GetResourceShareAssociationsPaginator,
        GetResourceShareInvitationsPaginator,
        GetResourceSharesPaginator,
        ListPrincipalsPaginator,
        ListResourcesPaginator,
    )

    client: RAMClient = boto3.client("ram")

    get_resource_policies_paginator: GetResourcePoliciesPaginator = client.get_paginator("get_resource_policies")
    get_resource_share_associations_paginator: GetResourceShareAssociationsPaginator = client.get_paginator("get_resource_share_associations")
    get_resource_share_invitations_paginator: GetResourceShareInvitationsPaginator = client.get_paginator("get_resource_share_invitations")
    get_resource_shares_paginator: GetResourceSharesPaginator = client.get_paginator("get_resource_shares")
    list_principals_paginator: ListPrincipalsPaginator = client.get_paginator("list_principals")
    list_resources_paginator: ListResourcesPaginator = client.get_paginator("list_resources")
    ```
"""
import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_ram.type_defs import (
    GetResourcePoliciesResponseTypeDef,
    GetResourceShareAssociationsResponseTypeDef,
    GetResourceShareInvitationsResponseTypeDef,
    GetResourceSharesResponseTypeDef,
    ListPrincipalsResponseTypeDef,
    ListResourcesResponseTypeDef,
    PaginatorConfigTypeDef,
    TagFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetResourcePoliciesPaginator",
    "GetResourceShareAssociationsPaginator",
    "GetResourceShareInvitationsPaginator",
    "GetResourceSharesPaginator",
    "ListPrincipalsPaginator",
    "ListResourcesPaginator",
)


class GetResourcePoliciesPaginator(Boto3Paginator):
    """
    [Paginator.GetResourcePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ram.html#RAM.Paginator.GetResourcePolicies)
    """

    def paginate(
        self,
        resourceArns: List[str],
        principal: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetResourcePoliciesResponseTypeDef]:
        """
        [GetResourcePolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ram.html#RAM.Paginator.GetResourcePolicies.paginate)
        """


class GetResourceShareAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.GetResourceShareAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ram.html#RAM.Paginator.GetResourceShareAssociations)
    """

    def paginate(
        self,
        associationType: Literal["PRINCIPAL", "RESOURCE"],
        resourceShareArns: List[str] = None,
        resourceArn: str = None,
        principal: str = None,
        associationStatus: Literal[
            "ASSOCIATING", "ASSOCIATED", "FAILED", "DISASSOCIATING", "DISASSOCIATED"
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetResourceShareAssociationsResponseTypeDef]:
        """
        [GetResourceShareAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ram.html#RAM.Paginator.GetResourceShareAssociations.paginate)
        """


class GetResourceShareInvitationsPaginator(Boto3Paginator):
    """
    [Paginator.GetResourceShareInvitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ram.html#RAM.Paginator.GetResourceShareInvitations)
    """

    def paginate(
        self,
        resourceShareInvitationArns: List[str] = None,
        resourceShareArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetResourceShareInvitationsResponseTypeDef]:
        """
        [GetResourceShareInvitations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ram.html#RAM.Paginator.GetResourceShareInvitations.paginate)
        """


class GetResourceSharesPaginator(Boto3Paginator):
    """
    [Paginator.GetResourceShares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ram.html#RAM.Paginator.GetResourceShares)
    """

    def paginate(
        self,
        resourceOwner: Literal["SELF", "OTHER-ACCOUNTS"],
        resourceShareArns: List[str] = None,
        resourceShareStatus: Literal["PENDING", "ACTIVE", "FAILED", "DELETING", "DELETED"] = None,
        name: str = None,
        tagFilters: List[TagFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetResourceSharesResponseTypeDef]:
        """
        [GetResourceShares.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ram.html#RAM.Paginator.GetResourceShares.paginate)
        """


class ListPrincipalsPaginator(Boto3Paginator):
    """
    [Paginator.ListPrincipals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ram.html#RAM.Paginator.ListPrincipals)
    """

    def paginate(
        self,
        resourceOwner: Literal["SELF", "OTHER-ACCOUNTS"],
        resourceArn: str = None,
        principals: List[str] = None,
        resourceType: str = None,
        resourceShareArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPrincipalsResponseTypeDef]:
        """
        [ListPrincipals.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ram.html#RAM.Paginator.ListPrincipals.paginate)
        """


class ListResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ram.html#RAM.Paginator.ListResources)
    """

    def paginate(
        self,
        resourceOwner: Literal["SELF", "OTHER-ACCOUNTS"],
        principal: str = None,
        resourceType: str = None,
        resourceArns: List[str] = None,
        resourceShareArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListResourcesResponseTypeDef]:
        """
        [ListResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ram.html#RAM.Paginator.ListResources.paginate)
        """
