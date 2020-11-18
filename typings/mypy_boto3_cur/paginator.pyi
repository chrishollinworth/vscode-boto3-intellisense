# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for cur service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_cur import CostandUsageReportServiceClient
    from mypy_boto3_cur.paginator import (
        DescribeReportDefinitionsPaginator,
    )

    client: CostandUsageReportServiceClient = boto3.client("cur")

    describe_report_definitions_paginator: DescribeReportDefinitionsPaginator = client.get_paginator("describe_report_definitions")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_cur.type_defs import (
    DescribeReportDefinitionsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("DescribeReportDefinitionsPaginator",)


class DescribeReportDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReportDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cur.html#CostandUsageReportService.Paginator.DescribeReportDefinitions)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReportDefinitionsResponseTypeDef]:
        """
        [DescribeReportDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cur.html#CostandUsageReportService.Paginator.DescribeReportDefinitions.paginate)
        """
