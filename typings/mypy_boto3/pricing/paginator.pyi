"""
Type annotations for pricing service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_pricing import PricingClient
    from mypy_boto3_pricing.paginator import (
        DescribeServicesPaginator,
        GetAttributeValuesPaginator,
        GetProductsPaginator,
        ListPriceListsPaginator,
    )

    client: PricingClient = boto3.client("pricing")

    describe_services_paginator: DescribeServicesPaginator = client.get_paginator("describe_services")
    get_attribute_values_paginator: GetAttributeValuesPaginator = client.get_paginator("get_attribute_values")
    get_products_paginator: GetProductsPaginator = client.get_paginator("get_products")
    list_price_lists_paginator: ListPriceListsPaginator = client.get_paginator("list_price_lists")
    ```
"""

from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    DescribeServicesResponseTypeDef,
    FilterTypeDef,
    GetAttributeValuesResponseTypeDef,
    GetProductsResponseTypeDef,
    ListPriceListsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeServicesPaginator",
    "GetAttributeValuesPaginator",
    "GetProductsPaginator",
    "ListPriceListsPaginator",
)

class DescribeServicesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pricing.html#Pricing.Paginator.DescribeServices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators.html#describeservicespaginator)
    """

    def paginate(
        self,
        *,
        ServiceCode: str = None,
        FormatVersion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeServicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pricing.html#Pricing.Paginator.DescribeServices.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators.html#describeservicespaginator)
        """

class GetAttributeValuesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pricing.html#Pricing.Paginator.GetAttributeValues)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators.html#getattributevaluespaginator)
    """

    def paginate(
        self,
        *,
        ServiceCode: str,
        AttributeName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetAttributeValuesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pricing.html#Pricing.Paginator.GetAttributeValues.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators.html#getattributevaluespaginator)
        """

class GetProductsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pricing.html#Pricing.Paginator.GetProducts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators.html#getproductspaginator)
    """

    def paginate(
        self,
        *,
        ServiceCode: str,
        Filters: List["FilterTypeDef"] = None,
        FormatVersion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetProductsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pricing.html#Pricing.Paginator.GetProducts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators.html#getproductspaginator)
        """

class ListPriceListsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pricing.html#Pricing.Paginator.ListPriceLists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators.html#listpricelistspaginator)
    """

    def paginate(
        self,
        *,
        ServiceCode: str,
        EffectiveDate: Union[datetime, str],
        CurrencyCode: str,
        RegionCode: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPriceListsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pricing.html#Pricing.Paginator.ListPriceLists.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators.html#listpricelistspaginator)
        """
