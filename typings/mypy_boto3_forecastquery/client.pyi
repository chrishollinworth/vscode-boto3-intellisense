"""
Type annotations for forecastquery service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecastquery/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_forecastquery import ForecastQueryServiceClient

    client: ForecastQueryServiceClient = boto3.client("forecastquery")
    ```
"""
from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import QueryForecastResponseTypeDef, QueryWhatIfForecastResponseTypeDef

__all__ = ("ForecastQueryServiceClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class ForecastQueryServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/forecastquery.html#ForecastQueryService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecastquery/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ForecastQueryServiceClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/forecastquery.html#ForecastQueryService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecastquery/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/forecastquery.html#ForecastQueryService.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecastquery/client.html#close)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/forecastquery.html#ForecastQueryService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecastquery/client.html#generate_presigned_url)
        """
    def query_forecast(
        self,
        *,
        ForecastArn: str,
        Filters: Dict[str, str],
        StartDate: str = None,
        EndDate: str = None,
        NextToken: str = None
    ) -> QueryForecastResponseTypeDef:
        """
        Retrieves a forecast for a single item, filtered by the supplied criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/forecastquery.html#ForecastQueryService.Client.query_forecast)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecastquery/client.html#query_forecast)
        """
    def query_what_if_forecast(
        self,
        *,
        WhatIfForecastArn: str,
        Filters: Dict[str, str],
        StartDate: str = None,
        EndDate: str = None,
        NextToken: str = None
    ) -> QueryWhatIfForecastResponseTypeDef:
        """
        Retrieves a what-if forecast.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/forecastquery.html#ForecastQueryService.Client.query_what_if_forecast)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecastquery/client.html#query_what_if_forecast)
        """
