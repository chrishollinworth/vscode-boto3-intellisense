"""
Type annotations for partnercentral-account service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_partnercentral_account.client import PartnerCentralAccountAPIClient
    from mypy_boto3_partnercentral_account.paginator import (
        ListConnectionInvitationsPaginator,
        ListConnectionsPaginator,
        ListPartnersPaginator,
    )

    session = Session()
    client: PartnerCentralAccountAPIClient = session.client("partnercentral-account")

    list_connection_invitations_paginator: ListConnectionInvitationsPaginator = client.get_paginator("list_connection_invitations")
    list_connections_paginator: ListConnectionsPaginator = client.get_paginator("list_connections")
    list_partners_paginator: ListPartnersPaginator = client.get_paginator("list_partners")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListConnectionInvitationsRequestPaginateTypeDef,
    ListConnectionInvitationsResponseTypeDef,
    ListConnectionsRequestPaginateTypeDef,
    ListConnectionsResponseTypeDef,
    ListPartnersRequestPaginateTypeDef,
    ListPartnersResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListConnectionInvitationsPaginator",
    "ListConnectionsPaginator",
    "ListPartnersPaginator",
)

if TYPE_CHECKING:
    _ListConnectionInvitationsPaginatorBase = Paginator[ListConnectionInvitationsResponseTypeDef]
else:
    _ListConnectionInvitationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConnectionInvitationsPaginator(_ListConnectionInvitationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/paginator/ListConnectionInvitations.html#PartnerCentralAccountAPI.Paginator.ListConnectionInvitations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/paginators/#listconnectioninvitationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConnectionInvitationsRequestPaginateTypeDef]
    ) -> PageIterator[ListConnectionInvitationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/paginator/ListConnectionInvitations.html#PartnerCentralAccountAPI.Paginator.ListConnectionInvitations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/paginators/#listconnectioninvitationspaginator)
        """

if TYPE_CHECKING:
    _ListConnectionsPaginatorBase = Paginator[ListConnectionsResponseTypeDef]
else:
    _ListConnectionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConnectionsPaginator(_ListConnectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/paginator/ListConnections.html#PartnerCentralAccountAPI.Paginator.ListConnections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/paginators/#listconnectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConnectionsRequestPaginateTypeDef]
    ) -> PageIterator[ListConnectionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/paginator/ListConnections.html#PartnerCentralAccountAPI.Paginator.ListConnections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/paginators/#listconnectionspaginator)
        """

if TYPE_CHECKING:
    _ListPartnersPaginatorBase = Paginator[ListPartnersResponseTypeDef]
else:
    _ListPartnersPaginatorBase = Paginator  # type: ignore[assignment]

class ListPartnersPaginator(_ListPartnersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/paginator/ListPartners.html#PartnerCentralAccountAPI.Paginator.ListPartners)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/paginators/#listpartnerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPartnersRequestPaginateTypeDef]
    ) -> PageIterator[ListPartnersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/paginator/ListPartners.html#PartnerCentralAccountAPI.Paginator.ListPartners.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/paginators/#listpartnerspaginator)
        """
