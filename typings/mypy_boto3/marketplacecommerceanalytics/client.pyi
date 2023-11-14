"""
Type annotations for marketplacecommerceanalytics service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_marketplacecommerceanalytics import MarketplaceCommerceAnalyticsClient

    client: MarketplaceCommerceAnalyticsClient = boto3.client("marketplacecommerceanalytics")
    ```
"""
from datetime import datetime
from typing import Any, Dict, Type, Union

from botocore.client import BaseClient, ClientMeta

from .literals import DataSetTypeType, SupportDataSetTypeType
from .type_defs import GenerateDataSetResultTypeDef, StartSupportDataExportResultTypeDef

__all__ = ("MarketplaceCommerceAnalyticsClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    MarketplaceCommerceAnalyticsException: Type[BotocoreClientError]

class MarketplaceCommerceAnalyticsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MarketplaceCommerceAnalyticsClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/client.html#close)
        """
    def generate_data_set(
        self,
        *,
        dataSetType: DataSetTypeType,
        dataSetPublicationDate: Union[datetime, str],
        roleNameArn: str,
        destinationS3BucketName: str,
        snsTopicArn: str,
        destinationS3Prefix: str = None,
        customerDefinedValues: Dict[str, str] = None
    ) -> GenerateDataSetResultTypeDef:
        """
        Given a data set type and data set publication date, asynchronously publishes
        the requested data set to the specified S3 bucket and notifies the specified SNS
        topic once the data is available.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.generate_data_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/client.html#generate_data_set)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/client.html#generate_presigned_url)
        """
    def start_support_data_export(
        self,
        *,
        dataSetType: SupportDataSetTypeType,
        fromDate: Union[datetime, str],
        roleNameArn: str,
        destinationS3BucketName: str,
        snsTopicArn: str,
        destinationS3Prefix: str = None,
        customerDefinedValues: Dict[str, str] = None
    ) -> StartSupportDataExportResultTypeDef:
        """
        *This target has been deprecated.* Given a data set type and a from date,
        asynchronously publishes the requested customer support data to the specified S3
        bucket and notifies the specified SNS topic once the data is available.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.start_support_data_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/client.html#start_support_data_export)
        """
