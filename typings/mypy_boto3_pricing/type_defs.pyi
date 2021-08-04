"""
Type annotations for pricing service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/type_defs.html)

Usage::

    ```python
    from mypy_boto3_pricing.type_defs import AttributeValueTypeDef

    data: AttributeValueTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AttributeValueTypeDef",
    "DescribeServicesRequestRequestTypeDef",
    "DescribeServicesResponseTypeDef",
    "FilterTypeDef",
    "GetAttributeValuesRequestRequestTypeDef",
    "GetAttributeValuesResponseTypeDef",
    "GetProductsRequestRequestTypeDef",
    "GetProductsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "ServiceTypeDef",
)

AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

DescribeServicesRequestRequestTypeDef = TypedDict(
    "DescribeServicesRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "FormatVersion": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeServicesResponseTypeDef = TypedDict(
    "DescribeServicesResponseTypeDef",
    {
        "Services": List["ServiceTypeDef"],
        "FormatVersion": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Type": Literal["TERM_MATCH"],
        "Field": str,
        "Value": str,
    },
)

_RequiredGetAttributeValuesRequestRequestTypeDef = TypedDict(
    "_RequiredGetAttributeValuesRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "AttributeName": str,
    },
)
_OptionalGetAttributeValuesRequestRequestTypeDef = TypedDict(
    "_OptionalGetAttributeValuesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetAttributeValuesRequestRequestTypeDef(
    _RequiredGetAttributeValuesRequestRequestTypeDef,
    _OptionalGetAttributeValuesRequestRequestTypeDef,
):
    pass

GetAttributeValuesResponseTypeDef = TypedDict(
    "GetAttributeValuesResponseTypeDef",
    {
        "AttributeValues": List["AttributeValueTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProductsRequestRequestTypeDef = TypedDict(
    "GetProductsRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "Filters": List["FilterTypeDef"],
        "FormatVersion": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

GetProductsResponseTypeDef = TypedDict(
    "GetProductsResponseTypeDef",
    {
        "FormatVersion": str,
        "PriceList": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "ServiceCode": str,
        "AttributeNames": List[str],
    },
    total=False,
)
