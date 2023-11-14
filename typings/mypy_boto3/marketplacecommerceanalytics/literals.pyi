"""
Type annotations for marketplacecommerceanalytics service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/literals.html)

Usage::

    ```python
    from mypy_boto3_marketplacecommerceanalytics.literals import DataSetTypeType

    data: DataSetTypeType = "customer_profile_by_geography"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("DataSetTypeType", "SupportDataSetTypeType")

DataSetTypeType = Literal[
    "customer_profile_by_geography",
    "customer_profile_by_industry",
    "customer_profile_by_revenue",
    "customer_subscriber_annual_subscriptions",
    "customer_subscriber_hourly_monthly_subscriptions",
    "daily_business_canceled_product_subscribers",
    "daily_business_fees",
    "daily_business_free_trial_conversions",
    "daily_business_new_instances",
    "daily_business_new_product_subscribers",
    "daily_business_usage_by_instance_type",
    "disbursed_amount_by_age_of_disbursed_funds",
    "disbursed_amount_by_age_of_past_due_funds",
    "disbursed_amount_by_age_of_uncollected_funds",
    "disbursed_amount_by_customer_geo",
    "disbursed_amount_by_instance_hours",
    "disbursed_amount_by_product",
    "disbursed_amount_by_product_with_uncollected_funds",
    "disbursed_amount_by_uncollected_funds_breakdown",
    "monthly_revenue_annual_subscriptions",
    "monthly_revenue_billing_and_revenue_data",
    "monthly_revenue_field_demonstration_usage",
    "monthly_revenue_flexible_payment_schedule",
    "sales_compensation_billed_revenue",
    "us_sales_and_use_tax_records",
]
SupportDataSetTypeType = Literal[
    "customer_support_contacts_data", "test_customer_support_contacts_data"
]
