"""
Type annotations for partnercentral-channel service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_partnercentral_channel.client import PartnerCentralChannelAPIClient
    from mypy_boto3_partnercentral_channel.paginator import (
        ListChannelHandshakesPaginator,
        ListProgramManagementAccountsPaginator,
        ListRelationshipsPaginator,
    )

    session = Session()
    client: PartnerCentralChannelAPIClient = session.client("partnercentral-channel")

    list_channel_handshakes_paginator: ListChannelHandshakesPaginator = client.get_paginator("list_channel_handshakes")
    list_program_management_accounts_paginator: ListProgramManagementAccountsPaginator = client.get_paginator("list_program_management_accounts")
    list_relationships_paginator: ListRelationshipsPaginator = client.get_paginator("list_relationships")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListChannelHandshakesRequestPaginateTypeDef,
    ListChannelHandshakesResponseTypeDef,
    ListProgramManagementAccountsRequestPaginateTypeDef,
    ListProgramManagementAccountsResponseTypeDef,
    ListRelationshipsRequestPaginateTypeDef,
    ListRelationshipsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListChannelHandshakesPaginator",
    "ListProgramManagementAccountsPaginator",
    "ListRelationshipsPaginator",
)

if TYPE_CHECKING:
    _ListChannelHandshakesPaginatorBase = Paginator[ListChannelHandshakesResponseTypeDef]
else:
    _ListChannelHandshakesPaginatorBase = Paginator  # type: ignore[assignment]

class ListChannelHandshakesPaginator(_ListChannelHandshakesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/paginator/ListChannelHandshakes.html#PartnerCentralChannelAPI.Paginator.ListChannelHandshakes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/paginators/#listchannelhandshakespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListChannelHandshakesRequestPaginateTypeDef]
    ) -> PageIterator[ListChannelHandshakesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/paginator/ListChannelHandshakes.html#PartnerCentralChannelAPI.Paginator.ListChannelHandshakes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/paginators/#listchannelhandshakespaginator)
        """

if TYPE_CHECKING:
    _ListProgramManagementAccountsPaginatorBase = Paginator[
        ListProgramManagementAccountsResponseTypeDef
    ]
else:
    _ListProgramManagementAccountsPaginatorBase = Paginator  # type: ignore[assignment]

class ListProgramManagementAccountsPaginator(_ListProgramManagementAccountsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/paginator/ListProgramManagementAccounts.html#PartnerCentralChannelAPI.Paginator.ListProgramManagementAccounts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/paginators/#listprogrammanagementaccountspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProgramManagementAccountsRequestPaginateTypeDef]
    ) -> PageIterator[ListProgramManagementAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/paginator/ListProgramManagementAccounts.html#PartnerCentralChannelAPI.Paginator.ListProgramManagementAccounts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/paginators/#listprogrammanagementaccountspaginator)
        """

if TYPE_CHECKING:
    _ListRelationshipsPaginatorBase = Paginator[ListRelationshipsResponseTypeDef]
else:
    _ListRelationshipsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRelationshipsPaginator(_ListRelationshipsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/paginator/ListRelationships.html#PartnerCentralChannelAPI.Paginator.ListRelationships)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/paginators/#listrelationshipspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRelationshipsRequestPaginateTypeDef]
    ) -> PageIterator[ListRelationshipsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/paginator/ListRelationships.html#PartnerCentralChannelAPI.Paginator.ListRelationships.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/paginators/#listrelationshipspaginator)
        """
