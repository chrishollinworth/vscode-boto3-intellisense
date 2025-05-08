"""
Main interface for billing service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billing/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_billing import (
        BillingClient,
        Client,
        ListBillingViewsPaginator,
        ListSourceViewsForBillingViewPaginator,
    )

    session = Session()
    client: BillingClient = session.client("billing")

    list_billing_views_paginator: ListBillingViewsPaginator = client.get_paginator("list_billing_views")
    list_source_views_for_billing_view_paginator: ListSourceViewsForBillingViewPaginator = client.get_paginator("list_source_views_for_billing_view")
    ```
"""

from .client import BillingClient
from .paginator import ListBillingViewsPaginator, ListSourceViewsForBillingViewPaginator

Client = BillingClient

__all__ = (
    "BillingClient",
    "Client",
    "ListBillingViewsPaginator",
    "ListSourceViewsForBillingViewPaginator",
)
