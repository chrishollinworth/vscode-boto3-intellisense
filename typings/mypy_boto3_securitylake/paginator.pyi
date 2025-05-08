"""
Type annotations for securitylake service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_securitylake.client import SecurityLakeClient
    from mypy_boto3_securitylake.paginator import (
        GetDataLakeSourcesPaginator,
        ListDataLakeExceptionsPaginator,
        ListLogSourcesPaginator,
        ListSubscribersPaginator,
    )

    session = Session()
    client: SecurityLakeClient = session.client("securitylake")

    get_data_lake_sources_paginator: GetDataLakeSourcesPaginator = client.get_paginator("get_data_lake_sources")
    list_data_lake_exceptions_paginator: ListDataLakeExceptionsPaginator = client.get_paginator("list_data_lake_exceptions")
    list_log_sources_paginator: ListLogSourcesPaginator = client.get_paginator("list_log_sources")
    list_subscribers_paginator: ListSubscribersPaginator = client.get_paginator("list_subscribers")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetDataLakeSourcesRequestPaginateTypeDef,
    GetDataLakeSourcesResponseTypeDef,
    ListDataLakeExceptionsRequestPaginateTypeDef,
    ListDataLakeExceptionsResponseTypeDef,
    ListLogSourcesRequestPaginateTypeDef,
    ListLogSourcesResponseTypeDef,
    ListSubscribersRequestPaginateTypeDef,
    ListSubscribersResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetDataLakeSourcesPaginator",
    "ListDataLakeExceptionsPaginator",
    "ListLogSourcesPaginator",
    "ListSubscribersPaginator",
)

if TYPE_CHECKING:
    _GetDataLakeSourcesPaginatorBase = Paginator[GetDataLakeSourcesResponseTypeDef]
else:
    _GetDataLakeSourcesPaginatorBase = Paginator  # type: ignore[assignment]

class GetDataLakeSourcesPaginator(_GetDataLakeSourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/paginator/GetDataLakeSources.html#SecurityLake.Paginator.GetDataLakeSources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators/#getdatalakesourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetDataLakeSourcesRequestPaginateTypeDef]
    ) -> PageIterator[GetDataLakeSourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/paginator/GetDataLakeSources.html#SecurityLake.Paginator.GetDataLakeSources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators/#getdatalakesourcespaginator)
        """

if TYPE_CHECKING:
    _ListDataLakeExceptionsPaginatorBase = Paginator[ListDataLakeExceptionsResponseTypeDef]
else:
    _ListDataLakeExceptionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataLakeExceptionsPaginator(_ListDataLakeExceptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/paginator/ListDataLakeExceptions.html#SecurityLake.Paginator.ListDataLakeExceptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators/#listdatalakeexceptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataLakeExceptionsRequestPaginateTypeDef]
    ) -> PageIterator[ListDataLakeExceptionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/paginator/ListDataLakeExceptions.html#SecurityLake.Paginator.ListDataLakeExceptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators/#listdatalakeexceptionspaginator)
        """

if TYPE_CHECKING:
    _ListLogSourcesPaginatorBase = Paginator[ListLogSourcesResponseTypeDef]
else:
    _ListLogSourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListLogSourcesPaginator(_ListLogSourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/paginator/ListLogSources.html#SecurityLake.Paginator.ListLogSources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators/#listlogsourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLogSourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListLogSourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/paginator/ListLogSources.html#SecurityLake.Paginator.ListLogSources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators/#listlogsourcespaginator)
        """

if TYPE_CHECKING:
    _ListSubscribersPaginatorBase = Paginator[ListSubscribersResponseTypeDef]
else:
    _ListSubscribersPaginatorBase = Paginator  # type: ignore[assignment]

class ListSubscribersPaginator(_ListSubscribersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/paginator/ListSubscribers.html#SecurityLake.Paginator.ListSubscribers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators/#listsubscriberspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSubscribersRequestPaginateTypeDef]
    ) -> PageIterator[ListSubscribersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/paginator/ListSubscribers.html#SecurityLake.Paginator.ListSubscribers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators/#listsubscriberspaginator)
        """
