"""
Type annotations for importexport service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_importexport/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_importexport.client import ImportExportClient
    from mypy_boto3_importexport.paginator import (
        ListJobsPaginator,
    )

    session = Session()
    client: ImportExportClient = session.client("importexport")

    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListJobsInputPaginateTypeDef, ListJobsOutputTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListJobsPaginator",)

if TYPE_CHECKING:
    _ListJobsPaginatorBase = Paginator[ListJobsOutputTypeDef]
else:
    _ListJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListJobsPaginator(_ListJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/importexport/paginator/ListJobs.html#ImportExport.Paginator.ListJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_importexport/paginators/#listjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobsInputPaginateTypeDef]
    ) -> PageIterator[ListJobsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/importexport/paginator/ListJobs.html#ImportExport.Paginator.ListJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_importexport/paginators/#listjobspaginator)
        """
