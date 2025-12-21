"""
Main interface for invoicing service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_invoicing/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_invoicing import (
        Client,
        InvoicingClient,
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

from .client import InvoicingClient
from .paginator import (
    ListInvoiceSummariesPaginator,
    ListInvoiceUnitsPaginator,
    ListProcurementPortalPreferencesPaginator,
)

Client = InvoicingClient

__all__ = (
    "Client",
    "InvoicingClient",
    "ListInvoiceSummariesPaginator",
    "ListInvoiceUnitsPaginator",
    "ListProcurementPortalPreferencesPaginator",
)
