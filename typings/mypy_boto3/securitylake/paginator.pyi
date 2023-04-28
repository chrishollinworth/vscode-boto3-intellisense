"""
Type annotations for securitylake service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_securitylake import SecurityLakeClient
    from mypy_boto3_securitylake.paginator import (
        GetDatalakeStatusPaginator,
        ListDatalakeExceptionsPaginator,
        ListLogSourcesPaginator,
        ListSubscribersPaginator,
    )

    client: SecurityLakeClient = boto3.client("securitylake")

    get_datalake_status_paginator: GetDatalakeStatusPaginator = client.get_paginator("get_datalake_status")
    list_datalake_exceptions_paginator: ListDatalakeExceptionsPaginator = client.get_paginator("list_datalake_exceptions")
    list_log_sources_paginator: ListLogSourcesPaginator = client.get_paginator("list_log_sources")
    list_subscribers_paginator: ListSubscribersPaginator = client.get_paginator("list_subscribers")
    ```
"""
from typing import Dict, Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import DimensionType, RegionType
from .type_defs import (
    GetDatalakeStatusResponseTypeDef,
    ListDatalakeExceptionsResponseTypeDef,
    ListLogSourcesResponseTypeDef,
    ListSubscribersResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "GetDatalakeStatusPaginator",
    "ListDatalakeExceptionsPaginator",
    "ListLogSourcesPaginator",
    "ListSubscribersPaginator",
)

class GetDatalakeStatusPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/securitylake.html#SecurityLake.Paginator.GetDatalakeStatus)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html#getdatalakestatuspaginator)
    """

    def paginate(
        self, *, accountSet: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDatalakeStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/securitylake.html#SecurityLake.Paginator.GetDatalakeStatus.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html#getdatalakestatuspaginator)
        """

class ListDatalakeExceptionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/securitylake.html#SecurityLake.Paginator.ListDatalakeExceptions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html#listdatalakeexceptionspaginator)
    """

    def paginate(
        self, *, regionSet: List[RegionType] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatalakeExceptionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/securitylake.html#SecurityLake.Paginator.ListDatalakeExceptions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html#listdatalakeexceptionspaginator)
        """

class ListLogSourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/securitylake.html#SecurityLake.Paginator.ListLogSources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html#listlogsourcespaginator)
    """

    def paginate(
        self,
        *,
        inputOrder: List[DimensionType] = None,
        listAllDimensions: Dict[str, Dict[str, List[str]]] = None,
        listSingleDimension: List[str] = None,
        listTwoDimensions: Dict[str, List[str]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLogSourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/securitylake.html#SecurityLake.Paginator.ListLogSources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html#listlogsourcespaginator)
        """

class ListSubscribersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/securitylake.html#SecurityLake.Paginator.ListSubscribers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html#listsubscriberspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSubscribersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/securitylake.html#SecurityLake.Paginator.ListSubscribers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html#listsubscriberspaginator)
        """
