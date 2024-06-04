"""
Main interface for pricing service.

Usage::

    ```python
    import boto3
    from mypy_boto3_pricing import (
        Client,
        DescribeServicesPaginator,
        GetAttributeValuesPaginator,
        GetProductsPaginator,
        ListPriceListsPaginator,
        PricingClient,
    )

    session = boto3.Session()

    client: PricingClient = boto3.client("pricing")
    session_client: PricingClient = session.client("pricing")

    describe_services_paginator: DescribeServicesPaginator = client.get_paginator("describe_services")
    get_attribute_values_paginator: GetAttributeValuesPaginator = client.get_paginator("get_attribute_values")
    get_products_paginator: GetProductsPaginator = client.get_paginator("get_products")
    list_price_lists_paginator: ListPriceListsPaginator = client.get_paginator("list_price_lists")
    ```
"""

from .client import PricingClient
from .paginator import (
    DescribeServicesPaginator,
    GetAttributeValuesPaginator,
    GetProductsPaginator,
    ListPriceListsPaginator,
)

Client = PricingClient

__all__ = (
    "Client",
    "DescribeServicesPaginator",
    "GetAttributeValuesPaginator",
    "GetProductsPaginator",
    "ListPriceListsPaginator",
    "PricingClient",
)
