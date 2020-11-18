# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for pricing service client

Usage::

    ```python
    import boto3
    from mypy_boto3_pricing import PricingClient

    client: PricingClient = boto3.client("pricing")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_pricing.paginator import (
    DescribeServicesPaginator,
    GetAttributeValuesPaginator,
    GetProductsPaginator,
)
from mypy_boto3_pricing.type_defs import (
    DescribeServicesResponseTypeDef,
    FilterTypeDef,
    GetAttributeValuesResponseTypeDef,
    GetProductsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("PricingClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ExpiredNextTokenException: Type[BotocoreClientError]
    InternalErrorException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]


class PricingClient:
    """
    [Pricing.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pricing.html#Pricing.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pricing.html#Pricing.Client.can_paginate)
        """

    def describe_services(
        self,
        ServiceCode: str = None,
        FormatVersion: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeServicesResponseTypeDef:
        """
        [Client.describe_services documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pricing.html#Pricing.Client.describe_services)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pricing.html#Pricing.Client.generate_presigned_url)
        """

    def get_attribute_values(
        self, ServiceCode: str, AttributeName: str, NextToken: str = None, MaxResults: int = None
    ) -> GetAttributeValuesResponseTypeDef:
        """
        [Client.get_attribute_values documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pricing.html#Pricing.Client.get_attribute_values)
        """

    def get_products(
        self,
        ServiceCode: str = None,
        Filters: List[FilterTypeDef] = None,
        FormatVersion: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetProductsResponseTypeDef:
        """
        [Client.get_products documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pricing.html#Pricing.Client.get_products)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_services"]
    ) -> DescribeServicesPaginator:
        """
        [Paginator.DescribeServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pricing.html#Pricing.Paginator.DescribeServices)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_attribute_values"]
    ) -> GetAttributeValuesPaginator:
        """
        [Paginator.GetAttributeValues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pricing.html#Pricing.Paginator.GetAttributeValues)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_products"]) -> GetProductsPaginator:
        """
        [Paginator.GetProducts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pricing.html#Pricing.Paginator.GetProducts)
        """
