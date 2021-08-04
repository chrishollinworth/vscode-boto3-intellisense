"""
Main interface for applicationcostprofiler service.

Usage::

    ```python
    import boto3
    from mypy_boto3_applicationcostprofiler import (
        ApplicationCostProfilerClient,
        Client,
        ListReportDefinitionsPaginator,
    )

    session = boto3.Session()

    client: ApplicationCostProfilerClient = boto3.client("applicationcostprofiler")
    session_client: ApplicationCostProfilerClient = session.client("applicationcostprofiler")

    list_report_definitions_paginator: ListReportDefinitionsPaginator = client.get_paginator("list_report_definitions")
    ```
"""
from .client import ApplicationCostProfilerClient
from .paginator import ListReportDefinitionsPaginator

Client = ApplicationCostProfilerClient

__all__ = ("ApplicationCostProfilerClient", "Client", "ListReportDefinitionsPaginator")
