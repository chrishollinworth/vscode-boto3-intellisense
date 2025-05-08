"""
Type annotations for pricing service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_pricing.client import PricingClient
    from mypy_boto3_pricing.paginator import (
        DescribeServicesPaginator,
        GetAttributeValuesPaginator,
        GetProductsPaginator,
        ListPriceListsPaginator,
    )

    session = Session()
    client: PricingClient = session.client("pricing")

    describe_services_paginator: DescribeServicesPaginator = client.get_paginator("describe_services")
    get_attribute_values_paginator: GetAttributeValuesPaginator = client.get_paginator("get_attribute_values")
    get_products_paginator: GetProductsPaginator = client.get_paginator("get_products")
    list_price_lists_paginator: ListPriceListsPaginator = client.get_paginator("list_price_lists")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeServicesRequestPaginateTypeDef,
    DescribeServicesResponseTypeDef,
    GetAttributeValuesRequestPaginateTypeDef,
    GetAttributeValuesResponseTypeDef,
    GetProductsRequestPaginateTypeDef,
    GetProductsResponseTypeDef,
    ListPriceListsRequestPaginateTypeDef,
    ListPriceListsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeServicesPaginator",
    "GetAttributeValuesPaginator",
    "GetProductsPaginator",
    "ListPriceListsPaginator",
)

if TYPE_CHECKING:
    _DescribeServicesPaginatorBase = Paginator[DescribeServicesResponseTypeDef]
else:
    _DescribeServicesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeServicesPaginator(_DescribeServicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing/paginator/DescribeServices.html#Pricing.Paginator.DescribeServices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators/#describeservicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeServicesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeServicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing/paginator/DescribeServices.html#Pricing.Paginator.DescribeServices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators/#describeservicespaginator)
        """

if TYPE_CHECKING:
    _GetAttributeValuesPaginatorBase = Paginator[GetAttributeValuesResponseTypeDef]
else:
    _GetAttributeValuesPaginatorBase = Paginator  # type: ignore[assignment]

class GetAttributeValuesPaginator(_GetAttributeValuesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing/paginator/GetAttributeValues.html#Pricing.Paginator.GetAttributeValues)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators/#getattributevaluespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetAttributeValuesRequestPaginateTypeDef]
    ) -> PageIterator[GetAttributeValuesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing/paginator/GetAttributeValues.html#Pricing.Paginator.GetAttributeValues.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators/#getattributevaluespaginator)
        """

if TYPE_CHECKING:
    _GetProductsPaginatorBase = Paginator[GetProductsResponseTypeDef]
else:
    _GetProductsPaginatorBase = Paginator  # type: ignore[assignment]

class GetProductsPaginator(_GetProductsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing/paginator/GetProducts.html#Pricing.Paginator.GetProducts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators/#getproductspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetProductsRequestPaginateTypeDef]
    ) -> PageIterator[GetProductsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing/paginator/GetProducts.html#Pricing.Paginator.GetProducts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators/#getproductspaginator)
        """

if TYPE_CHECKING:
    _ListPriceListsPaginatorBase = Paginator[ListPriceListsResponseTypeDef]
else:
    _ListPriceListsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPriceListsPaginator(_ListPriceListsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing/paginator/ListPriceLists.html#Pricing.Paginator.ListPriceLists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators/#listpricelistspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPriceListsRequestPaginateTypeDef]
    ) -> PageIterator[ListPriceListsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing/paginator/ListPriceLists.html#Pricing.Paginator.ListPriceLists.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators/#listpricelistspaginator)
        """
