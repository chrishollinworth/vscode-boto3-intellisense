"""
Main interface for cur service.

Usage::

    ```python
    import boto3
    from mypy_boto3_cur import (
        Client,
        CostandUsageReportServiceClient,
        DescribeReportDefinitionsPaginator,
    )

    session = boto3.Session()

    client: CostandUsageReportServiceClient = boto3.client("cur")
    session_client: CostandUsageReportServiceClient = session.client("cur")

    describe_report_definitions_paginator: DescribeReportDefinitionsPaginator = client.get_paginator("describe_report_definitions")
    ```
"""
from mypy_boto3_cur.client import CostandUsageReportServiceClient
from mypy_boto3_cur.paginator import DescribeReportDefinitionsPaginator

Client = CostandUsageReportServiceClient


__all__ = ("Client", "CostandUsageReportServiceClient", "DescribeReportDefinitionsPaginator")
