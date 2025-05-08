"""
Type annotations for invoicing service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_invoicing/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_invoicing.client import InvoicingClient
    from mypy_boto3_invoicing.paginator import (
        ListInvoiceUnitsPaginator,
    )

    session = Session()
    client: InvoicingClient = session.client("invoicing")

    list_invoice_units_paginator: ListInvoiceUnitsPaginator = client.get_paginator("list_invoice_units")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListInvoiceUnitsRequestPaginateTypeDef, ListInvoiceUnitsResponseTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListInvoiceUnitsPaginator",)

if TYPE_CHECKING:
    _ListInvoiceUnitsPaginatorBase = Paginator[ListInvoiceUnitsResponseTypeDef]
else:
    _ListInvoiceUnitsPaginatorBase = Paginator  # type: ignore[assignment]

class ListInvoiceUnitsPaginator(_ListInvoiceUnitsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/invoicing/paginator/ListInvoiceUnits.html#Invoicing.Paginator.ListInvoiceUnits)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_invoicing/paginators/#listinvoiceunitspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInvoiceUnitsRequestPaginateTypeDef]
    ) -> PageIterator[ListInvoiceUnitsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/invoicing/paginator/ListInvoiceUnits.html#Invoicing.Paginator.ListInvoiceUnits.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_invoicing/paginators/#listinvoiceunitspaginator)
        """
