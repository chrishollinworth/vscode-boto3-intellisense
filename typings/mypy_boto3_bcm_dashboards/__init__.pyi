"""
Main interface for bcm-dashboards service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_dashboards/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_bcm_dashboards import (
        BillingandCostManagementDashboardsClient,
        Client,
        ListDashboardsPaginator,
    )

    session = Session()
    client: BillingandCostManagementDashboardsClient = session.client("bcm-dashboards")

    list_dashboards_paginator: ListDashboardsPaginator = client.get_paginator("list_dashboards")
    ```
"""

from .client import BillingandCostManagementDashboardsClient
from .paginator import ListDashboardsPaginator

Client = BillingandCostManagementDashboardsClient

__all__ = ("BillingandCostManagementDashboardsClient", "Client", "ListDashboardsPaginator")
