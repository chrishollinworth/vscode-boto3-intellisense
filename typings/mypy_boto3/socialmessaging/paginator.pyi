"""
Type annotations for socialmessaging service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_socialmessaging.client import EndUserMessagingSocialClient
    from mypy_boto3_socialmessaging.paginator import (
        ListLinkedWhatsAppBusinessAccountsPaginator,
    )

    session = Session()
    client: EndUserMessagingSocialClient = session.client("socialmessaging")

    list_linked_whatsapp_business_accounts_paginator: ListLinkedWhatsAppBusinessAccountsPaginator = client.get_paginator("list_linked_whatsapp_business_accounts")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListLinkedWhatsAppBusinessAccountsInputPaginateTypeDef,
    ListLinkedWhatsAppBusinessAccountsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListLinkedWhatsAppBusinessAccountsPaginator",)

if TYPE_CHECKING:
    _ListLinkedWhatsAppBusinessAccountsPaginatorBase = Paginator[
        ListLinkedWhatsAppBusinessAccountsOutputTypeDef
    ]
else:
    _ListLinkedWhatsAppBusinessAccountsPaginatorBase = Paginator  # type: ignore[assignment]

class ListLinkedWhatsAppBusinessAccountsPaginator(_ListLinkedWhatsAppBusinessAccountsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/paginator/ListLinkedWhatsAppBusinessAccounts.html#EndUserMessagingSocial.Paginator.ListLinkedWhatsAppBusinessAccounts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/paginators/#listlinkedwhatsappbusinessaccountspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLinkedWhatsAppBusinessAccountsInputPaginateTypeDef]
    ) -> PageIterator[ListLinkedWhatsAppBusinessAccountsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/paginator/ListLinkedWhatsAppBusinessAccounts.html#EndUserMessagingSocial.Paginator.ListLinkedWhatsAppBusinessAccounts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/paginators/#listlinkedwhatsappbusinessaccountspaginator)
        """
