"""
Type annotations for securitylake service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_securitylake import SecurityLakeClient
    from mypy_boto3_securitylake.paginator import (
        GetDataLakeSourcesPaginator,
        ListDataLakeExceptionsPaginator,
        ListLogSourcesPaginator,
        ListSubscribersPaginator,
    )

    client: SecurityLakeClient = boto3.client("securitylake")

    get_data_lake_sources_paginator: GetDataLakeSourcesPaginator = client.get_paginator("get_data_lake_sources")
    list_data_lake_exceptions_paginator: ListDataLakeExceptionsPaginator = client.get_paginator("list_data_lake_exceptions")
    list_log_sources_paginator: ListLogSourcesPaginator = client.get_paginator("list_log_sources")
    list_subscribers_paginator: ListSubscribersPaginator = client.get_paginator("list_subscribers")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    GetDataLakeSourcesResponseTypeDef,
    ListDataLakeExceptionsResponseTypeDef,
    ListLogSourcesResponseTypeDef,
    ListSubscribersResponseTypeDef,
    LogSourceResourceTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "GetDataLakeSourcesPaginator",
    "ListDataLakeExceptionsPaginator",
    "ListLogSourcesPaginator",
    "ListSubscribersPaginator",
)

class GetDataLakeSourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/securitylake.html#SecurityLake.Paginator.GetDataLakeSources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html#getdatalakesourcespaginator)
    """

    def paginate(
        self, *, accounts: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDataLakeSourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/securitylake.html#SecurityLake.Paginator.GetDataLakeSources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html#getdatalakesourcespaginator)
        """

class ListDataLakeExceptionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/securitylake.html#SecurityLake.Paginator.ListDataLakeExceptions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html#listdatalakeexceptionspaginator)
    """

    def paginate(
        self, *, regions: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataLakeExceptionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/securitylake.html#SecurityLake.Paginator.ListDataLakeExceptions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html#listdatalakeexceptionspaginator)
        """

class ListLogSourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/securitylake.html#SecurityLake.Paginator.ListLogSources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html#listlogsourcespaginator)
    """

    def paginate(
        self,
        *,
        accounts: List[str] = None,
        regions: List[str] = None,
        sources: List["LogSourceResourceTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLogSourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/securitylake.html#SecurityLake.Paginator.ListLogSources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html#listlogsourcespaginator)
        """

class ListSubscribersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/securitylake.html#SecurityLake.Paginator.ListSubscribers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html#listsubscriberspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSubscribersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/securitylake.html#SecurityLake.Paginator.ListSubscribers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html#listsubscriberspaginator)
        """
