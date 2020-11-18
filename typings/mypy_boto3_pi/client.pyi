# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for pi service client

Usage::

    ```python
    import boto3
    from mypy_boto3_pi import PIClient

    client: PIClient = boto3.client("pi")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_pi.type_defs import (
    DescribeDimensionKeysResponseTypeDef,
    DimensionGroupTypeDef,
    GetResourceMetricsResponseTypeDef,
    MetricQueryTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("PIClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServiceError: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    NotAuthorizedException: Type[BotocoreClientError]


class PIClient:
    """
    [PI.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pi.html#PI.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pi.html#PI.Client.can_paginate)
        """

    def describe_dimension_keys(
        self,
        ServiceType: Literal["RDS"],
        Identifier: str,
        StartTime: datetime,
        EndTime: datetime,
        Metric: str,
        GroupBy: "DimensionGroupTypeDef",
        PeriodInSeconds: int = None,
        PartitionBy: "DimensionGroupTypeDef" = None,
        Filter: Dict[str, str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeDimensionKeysResponseTypeDef:
        """
        [Client.describe_dimension_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pi.html#PI.Client.describe_dimension_keys)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pi.html#PI.Client.generate_presigned_url)
        """

    def get_resource_metrics(
        self,
        ServiceType: Literal["RDS"],
        Identifier: str,
        MetricQueries: List[MetricQueryTypeDef],
        StartTime: datetime,
        EndTime: datetime,
        PeriodInSeconds: int = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetResourceMetricsResponseTypeDef:
        """
        [Client.get_resource_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pi.html#PI.Client.get_resource_metrics)
        """
