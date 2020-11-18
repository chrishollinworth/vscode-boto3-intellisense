# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for marketplacecommerceanalytics service client

Usage::

    ```python
    import boto3
    from mypy_boto3_marketplacecommerceanalytics import MarketplaceCommerceAnalyticsClient

    client: MarketplaceCommerceAnalyticsClient = boto3.client("marketplacecommerceanalytics")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from mypy_boto3_marketplacecommerceanalytics.type_defs import (
    GenerateDataSetResultTypeDef,
    StartSupportDataExportResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MarketplaceCommerceAnalyticsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    MarketplaceCommerceAnalyticsException: Type[BotocoreClientError]


class MarketplaceCommerceAnalyticsClient:
    """
    [MarketplaceCommerceAnalytics.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.can_paginate)
        """

    def generate_data_set(
        self,
        dataSetType: Literal[
            "customer_subscriber_hourly_monthly_subscriptions",
            "customer_subscriber_annual_subscriptions",
            "daily_business_usage_by_instance_type",
            "daily_business_fees",
            "daily_business_free_trial_conversions",
            "daily_business_new_instances",
            "daily_business_new_product_subscribers",
            "daily_business_canceled_product_subscribers",
            "monthly_revenue_billing_and_revenue_data",
            "monthly_revenue_annual_subscriptions",
            "monthly_revenue_field_demonstration_usage",
            "monthly_revenue_flexible_payment_schedule",
            "disbursed_amount_by_product",
            "disbursed_amount_by_product_with_uncollected_funds",
            "disbursed_amount_by_instance_hours",
            "disbursed_amount_by_customer_geo",
            "disbursed_amount_by_age_of_uncollected_funds",
            "disbursed_amount_by_age_of_disbursed_funds",
            "disbursed_amount_by_age_of_past_due_funds",
            "disbursed_amount_by_uncollected_funds_breakdown",
            "customer_profile_by_industry",
            "customer_profile_by_revenue",
            "customer_profile_by_geography",
            "sales_compensation_billed_revenue",
            "us_sales_and_use_tax_records",
        ],
        dataSetPublicationDate: datetime,
        roleNameArn: str,
        destinationS3BucketName: str,
        snsTopicArn: str,
        destinationS3Prefix: str = None,
        customerDefinedValues: Dict[str, str] = None,
    ) -> GenerateDataSetResultTypeDef:
        """
        [Client.generate_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.generate_data_set)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.generate_presigned_url)
        """

    def start_support_data_export(
        self,
        dataSetType: Literal[
            "customer_support_contacts_data", "test_customer_support_contacts_data"
        ],
        fromDate: datetime,
        roleNameArn: str,
        destinationS3BucketName: str,
        snsTopicArn: str,
        destinationS3Prefix: str = None,
        customerDefinedValues: Dict[str, str] = None,
    ) -> StartSupportDataExportResultTypeDef:
        """
        [Client.start_support_data_export documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.start_support_data_export)
        """
