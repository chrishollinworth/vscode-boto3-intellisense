"""
Type annotations for pricing service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_pricing.client import PricingClient

    session = Session()
    client: PricingClient = session.client("pricing")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeServicesPaginator,
    GetAttributeValuesPaginator,
    GetProductsPaginator,
    ListPriceListsPaginator,
)
from .type_defs import (
    DescribeServicesRequestTypeDef,
    DescribeServicesResponseTypeDef,
    GetAttributeValuesRequestTypeDef,
    GetAttributeValuesResponseTypeDef,
    GetPriceListFileUrlRequestTypeDef,
    GetPriceListFileUrlResponseTypeDef,
    GetProductsRequestTypeDef,
    GetProductsResponseTypeDef,
    ListPriceListsRequestTypeDef,
    ListPriceListsResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("PricingClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ExpiredNextTokenException: Type[BotocoreClientError]
    InternalErrorException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class PricingClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing.html#Pricing.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PricingClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing.html#Pricing.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/client/#generate_presigned_url)
        """

    def describe_services(
        self, **kwargs: Unpack[DescribeServicesRequestTypeDef]
    ) -> DescribeServicesResponseTypeDef:
        """
        Returns the metadata for one service or a list of the metadata for all services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing/client/describe_services.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/client/#describe_services)
        """

    def get_attribute_values(
        self, **kwargs: Unpack[GetAttributeValuesRequestTypeDef]
    ) -> GetAttributeValuesResponseTypeDef:
        """
        Returns a list of attribute values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing/client/get_attribute_values.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/client/#get_attribute_values)
        """

    def get_price_list_file_url(
        self, **kwargs: Unpack[GetPriceListFileUrlRequestTypeDef]
    ) -> GetPriceListFileUrlResponseTypeDef:
        """
        <i> <b>This feature is in preview release and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing/client/get_price_list_file_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/client/#get_price_list_file_url)
        """

    def get_products(
        self, **kwargs: Unpack[GetProductsRequestTypeDef]
    ) -> GetProductsResponseTypeDef:
        """
        Returns a list of all products that match the filter criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing/client/get_products.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/client/#get_products)
        """

    def list_price_lists(
        self, **kwargs: Unpack[ListPriceListsRequestTypeDef]
    ) -> ListPriceListsResponseTypeDef:
        """
        <i> <b>This feature is in preview release and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing/client/list_price_lists.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/client/#list_price_lists)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_services"]
    ) -> DescribeServicesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_attribute_values"]
    ) -> GetAttributeValuesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_products"]
    ) -> GetProductsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_price_lists"]
    ) -> ListPriceListsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/client/#get_paginator)
        """
