# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for importexport service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_importexport import ImportExportClient
    from mypy_boto3_importexport.paginator import (
        ListJobsPaginator,
    )

    client: ImportExportClient = boto3.client("importexport")

    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_importexport.type_defs import ListJobsOutputTypeDef, PaginatorConfigTypeDef

__all__ = ("ListJobsPaginator",)


class ListJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/importexport.html#ImportExport.Paginator.ListJobs)
    """

    def paginate(
        self, APIVersion: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobsOutputTypeDef]:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/importexport.html#ImportExport.Paginator.ListJobs.paginate)
        """
