"""
Type annotations for codeguruprofiler service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_codeguruprofiler.client import CodeGuruProfilerClient
    from mypy_boto3_codeguruprofiler.paginator import (
        ListProfileTimesPaginator,
    )

    session = Session()
    client: CodeGuruProfilerClient = session.client("codeguruprofiler")

    list_profile_times_paginator: ListProfileTimesPaginator = client.get_paginator("list_profile_times")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListProfileTimesRequestPaginateTypeDef, ListProfileTimesResponseTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListProfileTimesPaginator",)

if TYPE_CHECKING:
    _ListProfileTimesPaginatorBase = Paginator[ListProfileTimesResponseTypeDef]
else:
    _ListProfileTimesPaginatorBase = Paginator  # type: ignore[assignment]

class ListProfileTimesPaginator(_ListProfileTimesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/paginator/ListProfileTimes.html#CodeGuruProfiler.Paginator.ListProfileTimes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/paginators/#listprofiletimespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProfileTimesRequestPaginateTypeDef]
    ) -> PageIterator[ListProfileTimesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/paginator/ListProfileTimes.html#CodeGuruProfiler.Paginator.ListProfileTimes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/paginators/#listprofiletimespaginator)
        """
