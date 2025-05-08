"""
Type annotations for forecastquery service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecastquery/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_forecastquery.client import ForecastQueryServiceClient

    session = Session()
    client: ForecastQueryServiceClient = session.client("forecastquery")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    QueryForecastRequestTypeDef,
    QueryForecastResponseTypeDef,
    QueryWhatIfForecastRequestTypeDef,
    QueryWhatIfForecastResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ForecastQueryServiceClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class ForecastQueryServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecastquery.html#ForecastQueryService.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecastquery/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ForecastQueryServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecastquery.html#ForecastQueryService.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecastquery/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecastquery/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecastquery/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecastquery/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecastquery/client/#generate_presigned_url)
        """

    def query_forecast(
        self, **kwargs: Unpack[QueryForecastRequestTypeDef]
    ) -> QueryForecastResponseTypeDef:
        """
        Retrieves a forecast for a single item, filtered by the supplied criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecastquery/client/query_forecast.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecastquery/client/#query_forecast)
        """

    def query_what_if_forecast(
        self, **kwargs: Unpack[QueryWhatIfForecastRequestTypeDef]
    ) -> QueryWhatIfForecastResponseTypeDef:
        """
        Retrieves a what-if forecast.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecastquery/client/query_what_if_forecast.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecastquery/client/#query_what_if_forecast)
        """
