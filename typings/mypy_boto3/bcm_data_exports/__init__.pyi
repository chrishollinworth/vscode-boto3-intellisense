"""
Main interface for bcm-data-exports service.

Usage::

    ```python
    import boto3
    from mypy_boto3_bcm_data_exports import (
        BillingandCostManagementDataExportsClient,
        Client,
        ListExecutionsPaginator,
        ListExportsPaginator,
        ListTablesPaginator,
    )

    session = boto3.Session()

    client: BillingandCostManagementDataExportsClient = boto3.client("bcm-data-exports")
    session_client: BillingandCostManagementDataExportsClient = session.client("bcm-data-exports")

    list_executions_paginator: ListExecutionsPaginator = client.get_paginator("list_executions")
    list_exports_paginator: ListExportsPaginator = client.get_paginator("list_exports")
    list_tables_paginator: ListTablesPaginator = client.get_paginator("list_tables")
    ```
"""
from .client import BillingandCostManagementDataExportsClient
from .paginator import ListExecutionsPaginator, ListExportsPaginator, ListTablesPaginator

Client = BillingandCostManagementDataExportsClient

__all__ = (
    "BillingandCostManagementDataExportsClient",
    "Client",
    "ListExecutionsPaginator",
    "ListExportsPaginator",
    "ListTablesPaginator",
)
