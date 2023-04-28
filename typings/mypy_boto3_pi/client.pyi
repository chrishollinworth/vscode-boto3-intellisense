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
from datetime import datetime
from typing import Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta

from .literals import PeriodAlignmentType, ServiceTypeType
from .type_defs import (
    DescribeDimensionKeysResponseTypeDef,
    DimensionGroupTypeDef,
    GetDimensionKeyDetailsResponseTypeDef,
    GetResourceMetadataResponseTypeDef,
    GetResourceMetricsResponseTypeDef,
    ListAvailableResourceDimensionsResponseTypeDef,
    ListAvailableResourceMetricsResponseTypeDef,
    MetricQueryTypeDef,
)

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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/pi.html#PI.Client)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/pi.html#PI.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pi/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/pi.html#PI.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pi/client.html#close)
        """
    def describe_dimension_keys(
        self,
        *,
        ServiceType: ServiceTypeType,
        Identifier: str,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        Metric: str,
        GroupBy: "DimensionGroupTypeDef",
        PeriodInSeconds: int = None,
        AdditionalMetrics: List[str] = None,
        PartitionBy: "DimensionGroupTypeDef" = None,
        Filter: Dict[str, str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeDimensionKeysResponseTypeDef:
        """
        For a specific time period, retrieve the top `N` dimension keys for a metric.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/pi.html#PI.Client.describe_dimension_keys)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/pi.html#PI.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pi/client.html#generate_presigned_url)
        """
    def get_dimension_key_details(
        self,
        *,
        ServiceType: ServiceTypeType,
        Identifier: str,
        Group: str,
        GroupIdentifier: str,
        RequestedDimensions: List[str] = None
    ) -> GetDimensionKeyDetailsResponseTypeDef:
        """
        Get the attributes of the specified dimension group for a DB instance or data
        source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/pi.html#PI.Client.get_dimension_key_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pi/client.html#get_dimension_key_details)
        """
    def get_resource_metadata(
        self, *, ServiceType: ServiceTypeType, Identifier: str
    ) -> GetResourceMetadataResponseTypeDef:
        """
        Retrieve the metadata for different features.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/pi.html#PI.Client.get_resource_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pi/client.html#get_resource_metadata)
        """
    def get_resource_metrics(
        self,
        *,
        ServiceType: ServiceTypeType,
        Identifier: str,
        MetricQueries: List["MetricQueryTypeDef"],
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        PeriodInSeconds: int = None,
        MaxResults: int = None,
        NextToken: str = None,
        PeriodAlignment: PeriodAlignmentType = None
    ) -> GetResourceMetricsResponseTypeDef:
        """
        Retrieve Performance Insights metrics for a set of data sources over a time
        period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/pi.html#PI.Client.get_resource_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pi/client.html#get_resource_metrics)
        """
    def list_available_resource_dimensions(
        self,
        *,
        ServiceType: ServiceTypeType,
        Identifier: str,
        Metrics: List[str],
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListAvailableResourceDimensionsResponseTypeDef:
        """
        Retrieve the dimensions that can be queried for each specified metric type on a
        specified DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/pi.html#PI.Client.list_available_resource_dimensions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pi/client.html#list_available_resource_dimensions)
        """
    def list_available_resource_metrics(
        self,
        *,
        ServiceType: ServiceTypeType,
        Identifier: str,
        MetricTypes: List[str],
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListAvailableResourceMetricsResponseTypeDef:
        """
        Retrieve metrics of the specified types that can be queried for a specified DB
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/pi.html#PI.Client.list_available_resource_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pi/client.html#list_available_resource_metrics)
        """
