# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for timestream-query service client

Usage::

    ```python
    import boto3
    from mypy_boto3_timestream_query import TimestreamQueryClient

    client: TimestreamQueryClient = boto3.client("timestream-query")
    ```
"""
import sys
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from mypy_boto3_timestream_query.paginator import QueryPaginator
from mypy_boto3_timestream_query.type_defs import (
    CancelQueryResponseTypeDef,
    DescribeEndpointsResponseTypeDef,
    QueryResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("TimestreamQueryClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidEndpointException: Type[BotocoreClientError]
    QueryExecutionException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class TimestreamQueryClient:
    """
    [TimestreamQuery.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-query.html#TimestreamQuery.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-query.html#TimestreamQuery.Client.can_paginate)
        """

    def cancel_query(self, QueryId: str) -> CancelQueryResponseTypeDef:
        """
        [Client.cancel_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-query.html#TimestreamQuery.Client.cancel_query)
        """

    def describe_endpoints(self) -> DescribeEndpointsResponseTypeDef:
        """
        [Client.describe_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-query.html#TimestreamQuery.Client.describe_endpoints)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-query.html#TimestreamQuery.Client.generate_presigned_url)
        """

    def query(
        self, QueryString: str, ClientToken: str = None, NextToken: str = None, MaxRows: int = None
    ) -> QueryResponseTypeDef:
        """
        [Client.query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-query.html#TimestreamQuery.Client.query)
        """

    def get_paginator(self, operation_name: Literal["query"]) -> QueryPaginator:
        """
        [Paginator.Query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-query.html#TimestreamQuery.Paginator.Query)
        """
