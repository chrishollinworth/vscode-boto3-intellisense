"""
Type annotations for invoicing service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_invoicing/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_invoicing.client import InvoicingClient
    from mypy_boto3_invoicing.paginator import (
        ListInvoiceSummariesPaginator,
        ListInvoiceUnitsPaginator,
        ListProcurementPortalPreferencesPaginator,
    )

    session = Session()
    client: InvoicingClient = session.client("invoicing")

    list_invoice_summaries_paginator: ListInvoiceSummariesPaginator = client.get_paginator("list_invoice_summaries")
    list_invoice_units_paginator: ListInvoiceUnitsPaginator = client.get_paginator("list_invoice_units")
    list_procurement_portal_preferences_paginator: ListProcurementPortalPreferencesPaginator = client.get_paginator("list_procurement_portal_preferences")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListInvoiceSummariesRequestPaginateTypeDef,
    ListInvoiceSummariesResponseTypeDef,
    ListInvoiceUnitsRequestPaginateTypeDef,
    ListInvoiceUnitsResponseTypeDef,
    ListProcurementPortalPreferencesRequestPaginateTypeDef,
    ListProcurementPortalPreferencesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListInvoiceSummariesPaginator",
    "ListInvoiceUnitsPaginator",
    "ListProcurementPortalPreferencesPaginator",
)

if TYPE_CHECKING:
    _ListInvoiceSummariesPaginatorBase = Paginator[ListInvoiceSummariesResponseTypeDef]
else:
    _ListInvoiceSummariesPaginatorBase = Paginator  # type: ignore[assignment]

class ListInvoiceSummariesPaginator(_ListInvoiceSummariesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/invoicing/paginator/ListInvoiceSummaries.html#Invoicing.Paginator.ListInvoiceSummaries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_invoicing/paginators/#listinvoicesummariespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInvoiceSummariesRequestPaginateTypeDef]
    ) -> PageIterator[ListInvoiceSummariesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/invoicing/paginator/ListInvoiceSummaries.html#Invoicing.Paginator.ListInvoiceSummaries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_invoicing/paginators/#listinvoicesummariespaginator)
        """

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

if TYPE_CHECKING:
    _ListProcurementPortalPreferencesPaginatorBase = Paginator[
        ListProcurementPortalPreferencesResponseTypeDef
    ]
else:
    _ListProcurementPortalPreferencesPaginatorBase = Paginator  # type: ignore[assignment]

class ListProcurementPortalPreferencesPaginator(_ListProcurementPortalPreferencesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/invoicing/paginator/ListProcurementPortalPreferences.html#Invoicing.Paginator.ListProcurementPortalPreferences)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_invoicing/paginators/#listprocurementportalpreferencespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProcurementPortalPreferencesRequestPaginateTypeDef]
    ) -> PageIterator[ListProcurementPortalPreferencesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/invoicing/paginator/ListProcurementPortalPreferences.html#Invoicing.Paginator.ListProcurementPortalPreferences.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_invoicing/paginators/#listprocurementportalpreferencespaginator)
        """
