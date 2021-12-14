"""
Type annotations for pricing service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_pricing import PricingClient

    client: PricingClient = boto3.client("pricing")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import DescribeServicesPaginator, GetAttributeValuesPaginator, GetProductsPaginator
from .type_defs import (
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

class PricingClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/pricing.html#Pricing.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        PricingClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/pricing.html#Pricing.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/client.html#can_paginate)
        """
    def describe_services(
        self,
        *,
        ServiceCode: str = None,
        FormatVersion: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeServicesResponseTypeDef:
        """
        Returns the metadata for one service or a list of the metadata for all services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/pricing.html#Pricing.Client.describe_services)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/client.html#describe_services)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/pricing.html#Pricing.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/client.html#generate_presigned_url)
        """
    def get_attribute_values(
        self, *, ServiceCode: str, AttributeName: str, NextToken: str = None, MaxResults: int = None
    ) -> GetAttributeValuesResponseTypeDef:
        """
        Returns a list of attribute values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/pricing.html#Pricing.Client.get_attribute_values)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/client.html#get_attribute_values)
        """
    def get_products(
        self,
        *,
        ServiceCode: str = None,
        Filters: List["FilterTypeDef"] = None,
        FormatVersion: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetProductsResponseTypeDef:
        """
        Returns a list of all products that match the filter criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/pricing.html#Pricing.Client.get_products)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/client.html#get_products)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_services"]
    ) -> DescribeServicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/pricing.html#Pricing.Paginator.DescribeServices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators.html#describeservicespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_attribute_values"]
    ) -> GetAttributeValuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/pricing.html#Pricing.Paginator.GetAttributeValues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators.html#getattributevaluespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_products"]) -> GetProductsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/pricing.html#Pricing.Paginator.GetProducts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/paginators.html#getproductspaginator)
        """
