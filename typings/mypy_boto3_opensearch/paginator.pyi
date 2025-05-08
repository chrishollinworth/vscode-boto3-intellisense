"""
Type annotations for opensearch service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearch/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_opensearch.client import OpenSearchServiceClient
    from mypy_boto3_opensearch.paginator import (
        ListApplicationsPaginator,
    )

    session = Session()
    client: OpenSearchServiceClient = session.client("opensearch")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListApplicationsRequestPaginateTypeDef, ListApplicationsResponseTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListApplicationsPaginator",)

if TYPE_CHECKING:
    _ListApplicationsPaginatorBase = Paginator[ListApplicationsResponseTypeDef]
else:
    _ListApplicationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationsPaginator(_ListApplicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/paginator/ListApplications.html#OpenSearchService.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearch/paginators/#listapplicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationsRequestPaginateTypeDef]
    ) -> PageIterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/paginator/ListApplications.html#OpenSearchService.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearch/paginators/#listapplicationspaginator)
        """
