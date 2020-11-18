# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for forecastquery service client

Usage::

    ```python
    import boto3
    from mypy_boto3_forecastquery import ForecastQueryServiceClient

    client: ForecastQueryServiceClient = boto3.client("forecastquery")
    ```
"""
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from mypy_boto3_forecastquery.type_defs import QueryForecastResponseTypeDef

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


class ForecastQueryServiceClient:
    """
    [ForecastQueryService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecastquery.html#ForecastQueryService.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecastquery.html#ForecastQueryService.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecastquery.html#ForecastQueryService.Client.generate_presigned_url)
        """

    def query_forecast(
        self,
        ForecastArn: str,
        Filters: Dict[str, str],
        StartDate: str = None,
        EndDate: str = None,
        NextToken: str = None,
    ) -> QueryForecastResponseTypeDef:
        """
        [Client.query_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecastquery.html#ForecastQueryService.Client.query_forecast)
        """
