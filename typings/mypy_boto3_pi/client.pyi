"""
Type annotations for pi service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pi/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_pi import PIClient

    client: PIClient = boto3.client("pi")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    DescribeDimensionKeysResponseTypeDef,
    DimensionGroupTypeDef,
    GetDimensionKeyDetailsResponseTypeDef,
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

class PIClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/pi.html#PI.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pi/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        PIClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/pi.html#PI.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pi/client.html#can_paginate)
        """
    def describe_dimension_keys(
        self,
        *,
        ServiceType: Literal["RDS"],
        Identifier: str,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        Metric: str,
        GroupBy: "DimensionGroupTypeDef",
        PeriodInSeconds: int = None,
        PartitionBy: "DimensionGroupTypeDef" = None,
        Filter: Dict[str, str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeDimensionKeysResponseTypeDef:
        """
        For a specific time period, retrieve the top `N` dimension keys for a metric.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/pi.html#PI.Client.describe_dimension_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pi/client.html#describe_dimension_keys)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/pi.html#PI.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pi/client.html#generate_presigned_url)
        """
    def get_dimension_key_details(
        self,
        *,
        ServiceType: Literal["RDS"],
        Identifier: str,
        Group: str,
        GroupIdentifier: str,
        RequestedDimensions: List[str] = None
    ) -> GetDimensionKeyDetailsResponseTypeDef:
        """
        Get the attributes of the specified dimension group for a DB instance or data
        source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/pi.html#PI.Client.get_dimension_key_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pi/client.html#get_dimension_key_details)
        """
    def get_resource_metrics(
        self,
        *,
        ServiceType: Literal["RDS"],
        Identifier: str,
        MetricQueries: List["MetricQueryTypeDef"],
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        PeriodInSeconds: int = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetResourceMetricsResponseTypeDef:
        """
        Retrieve Performance Insights metrics for a set of data sources, over a time
        period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/pi.html#PI.Client.get_resource_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pi/client.html#get_resource_metrics)
        """
