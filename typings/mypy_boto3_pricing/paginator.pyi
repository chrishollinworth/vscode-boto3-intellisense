# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for pricing service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_pricing import PricingClient
    from mypy_boto3_pricing.paginator import (
        DescribeServicesPaginator,
        GetAttributeValuesPaginator,
        GetProductsPaginator,
    )

    client: PricingClient = boto3.client("pricing")

    describe_services_paginator: DescribeServicesPaginator = client.get_paginator("describe_services")
    get_attribute_values_paginator: GetAttributeValuesPaginator = client.get_paginator("get_attribute_values")
    get_products_paginator: GetProductsPaginator = client.get_paginator("get_products")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_pricing.type_defs import (
    DescribeServicesResponseTypeDef,
    FilterTypeDef,
    GetAttributeValuesResponseTypeDef,
    GetProductsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("DescribeServicesPaginator", "GetAttributeValuesPaginator", "GetProductsPaginator")


class DescribeServicesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pricing.html#Pricing.Paginator.DescribeServices)
    """

    def paginate(
        self,
        ServiceCode: str = None,
        FormatVersion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeServicesResponseTypeDef]:
        """
        [DescribeServices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pricing.html#Pricing.Paginator.DescribeServices.paginate)
        """


class GetAttributeValuesPaginator(Boto3Paginator):
    """
    [Paginator.GetAttributeValues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pricing.html#Pricing.Paginator.GetAttributeValues)
    """

    def paginate(
        self, ServiceCode: str, AttributeName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetAttributeValuesResponseTypeDef]:
        """
        [GetAttributeValues.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pricing.html#Pricing.Paginator.GetAttributeValues.paginate)
        """


class GetProductsPaginator(Boto3Paginator):
    """
    [Paginator.GetProducts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pricing.html#Pricing.Paginator.GetProducts)
    """

    def paginate(
        self,
        ServiceCode: str = None,
        Filters: List[FilterTypeDef] = None,
        FormatVersion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetProductsResponseTypeDef]:
        """
        [GetProducts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pricing.html#Pricing.Paginator.GetProducts.paginate)
        """
