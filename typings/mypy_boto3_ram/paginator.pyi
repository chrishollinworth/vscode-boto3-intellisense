"""
Type annotations for ram service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ram.client import RAMClient
    from mypy_boto3_ram.paginator import (
        GetResourcePoliciesPaginator,
        GetResourceShareAssociationsPaginator,
        GetResourceShareInvitationsPaginator,
        GetResourceSharesPaginator,
        ListPrincipalsPaginator,
        ListResourcesPaginator,
    )

    session = Session()
    client: RAMClient = session.client("ram")

    get_resource_policies_paginator: GetResourcePoliciesPaginator = client.get_paginator("get_resource_policies")
    get_resource_share_associations_paginator: GetResourceShareAssociationsPaginator = client.get_paginator("get_resource_share_associations")
    get_resource_share_invitations_paginator: GetResourceShareInvitationsPaginator = client.get_paginator("get_resource_share_invitations")
    get_resource_shares_paginator: GetResourceSharesPaginator = client.get_paginator("get_resource_shares")
    list_principals_paginator: ListPrincipalsPaginator = client.get_paginator("list_principals")
    list_resources_paginator: ListResourcesPaginator = client.get_paginator("list_resources")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetResourcePoliciesRequestPaginateTypeDef,
    GetResourcePoliciesResponseTypeDef,
    GetResourceShareAssociationsRequestPaginateTypeDef,
    GetResourceShareAssociationsResponseTypeDef,
    GetResourceShareInvitationsRequestPaginateTypeDef,
    GetResourceShareInvitationsResponseTypeDef,
    GetResourceSharesRequestPaginateTypeDef,
    GetResourceSharesResponseTypeDef,
    ListPrincipalsRequestPaginateTypeDef,
    ListPrincipalsResponseTypeDef,
    ListResourcesRequestPaginateTypeDef,
    ListResourcesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetResourcePoliciesPaginator",
    "GetResourceShareAssociationsPaginator",
    "GetResourceShareInvitationsPaginator",
    "GetResourceSharesPaginator",
    "ListPrincipalsPaginator",
    "ListResourcesPaginator",
)

if TYPE_CHECKING:
    _GetResourcePoliciesPaginatorBase = Paginator[GetResourcePoliciesResponseTypeDef]
else:
    _GetResourcePoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class GetResourcePoliciesPaginator(_GetResourcePoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/paginator/GetResourcePolicies.html#RAM.Paginator.GetResourcePolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/paginators/#getresourcepoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetResourcePoliciesRequestPaginateTypeDef]
    ) -> PageIterator[GetResourcePoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/paginator/GetResourcePolicies.html#RAM.Paginator.GetResourcePolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/paginators/#getresourcepoliciespaginator)
        """

if TYPE_CHECKING:
    _GetResourceShareAssociationsPaginatorBase = Paginator[
        GetResourceShareAssociationsResponseTypeDef
    ]
else:
    _GetResourceShareAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class GetResourceShareAssociationsPaginator(_GetResourceShareAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/paginator/GetResourceShareAssociations.html#RAM.Paginator.GetResourceShareAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/paginators/#getresourceshareassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetResourceShareAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[GetResourceShareAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/paginator/GetResourceShareAssociations.html#RAM.Paginator.GetResourceShareAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/paginators/#getresourceshareassociationspaginator)
        """

if TYPE_CHECKING:
    _GetResourceShareInvitationsPaginatorBase = Paginator[
        GetResourceShareInvitationsResponseTypeDef
    ]
else:
    _GetResourceShareInvitationsPaginatorBase = Paginator  # type: ignore[assignment]

class GetResourceShareInvitationsPaginator(_GetResourceShareInvitationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/paginator/GetResourceShareInvitations.html#RAM.Paginator.GetResourceShareInvitations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/paginators/#getresourceshareinvitationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetResourceShareInvitationsRequestPaginateTypeDef]
    ) -> PageIterator[GetResourceShareInvitationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/paginator/GetResourceShareInvitations.html#RAM.Paginator.GetResourceShareInvitations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/paginators/#getresourceshareinvitationspaginator)
        """

if TYPE_CHECKING:
    _GetResourceSharesPaginatorBase = Paginator[GetResourceSharesResponseTypeDef]
else:
    _GetResourceSharesPaginatorBase = Paginator  # type: ignore[assignment]

class GetResourceSharesPaginator(_GetResourceSharesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/paginator/GetResourceShares.html#RAM.Paginator.GetResourceShares)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/paginators/#getresourcesharespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetResourceSharesRequestPaginateTypeDef]
    ) -> PageIterator[GetResourceSharesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/paginator/GetResourceShares.html#RAM.Paginator.GetResourceShares.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/paginators/#getresourcesharespaginator)
        """

if TYPE_CHECKING:
    _ListPrincipalsPaginatorBase = Paginator[ListPrincipalsResponseTypeDef]
else:
    _ListPrincipalsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPrincipalsPaginator(_ListPrincipalsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/paginator/ListPrincipals.html#RAM.Paginator.ListPrincipals)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/paginators/#listprincipalspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPrincipalsRequestPaginateTypeDef]
    ) -> PageIterator[ListPrincipalsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/paginator/ListPrincipals.html#RAM.Paginator.ListPrincipals.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/paginators/#listprincipalspaginator)
        """

if TYPE_CHECKING:
    _ListResourcesPaginatorBase = Paginator[ListResourcesResponseTypeDef]
else:
    _ListResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourcesPaginator(_ListResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/paginator/ListResources.html#RAM.Paginator.ListResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/paginators/#listresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/paginator/ListResources.html#RAM.Paginator.ListResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/paginators/#listresourcespaginator)
        """
