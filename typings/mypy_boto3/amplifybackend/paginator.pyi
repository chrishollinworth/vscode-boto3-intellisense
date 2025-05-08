"""
Type annotations for amplifybackend service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_amplifybackend.client import AmplifyBackendClient
    from mypy_boto3_amplifybackend.paginator import (
        ListBackendJobsPaginator,
    )

    session = Session()
    client: AmplifyBackendClient = session.client("amplifybackend")

    list_backend_jobs_paginator: ListBackendJobsPaginator = client.get_paginator("list_backend_jobs")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListBackendJobsRequestPaginateTypeDef, ListBackendJobsResponseTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListBackendJobsPaginator",)

if TYPE_CHECKING:
    _ListBackendJobsPaginatorBase = Paginator[ListBackendJobsResponseTypeDef]
else:
    _ListBackendJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBackendJobsPaginator(_ListBackendJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend/paginator/ListBackendJobs.html#AmplifyBackend.Paginator.ListBackendJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/paginators/#listbackendjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBackendJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListBackendJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend/paginator/ListBackendJobs.html#AmplifyBackend.Paginator.ListBackendJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/paginators/#listbackendjobspaginator)
        """
