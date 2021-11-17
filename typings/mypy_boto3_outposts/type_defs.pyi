"""
Type annotations for outposts service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/type_defs.html)

Usage::

    ```python
    from mypy_boto3_outposts.type_defs import CreateOrderInputRequestTypeDef

    data: CreateOrderInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import OrderStatusType, PaymentOptionType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateOrderInputRequestTypeDef",
    "CreateOrderOutputTypeDef",
    "CreateOutpostInputRequestTypeDef",
    "CreateOutpostOutputTypeDef",
    "DeleteOutpostInputRequestTypeDef",
    "DeleteSiteInputRequestTypeDef",
    "GetOutpostInputRequestTypeDef",
    "GetOutpostInstanceTypesInputRequestTypeDef",
    "GetOutpostInstanceTypesOutputTypeDef",
    "GetOutpostOutputTypeDef",
    "InstanceTypeItemTypeDef",
    "LineItemRequestTypeDef",
    "LineItemTypeDef",
    "ListOutpostsInputRequestTypeDef",
    "ListOutpostsOutputTypeDef",
    "ListSitesInputRequestTypeDef",
    "ListSitesOutputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OrderTypeDef",
    "OutpostTypeDef",
    "ResponseMetadataTypeDef",
    "SiteTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

_RequiredCreateOrderInputRequestTypeDef = TypedDict(
    "_RequiredCreateOrderInputRequestTypeDef",
    {
        "OutpostIdentifier": str,
        "LineItems": List["LineItemRequestTypeDef"],
        "PaymentOption": PaymentOptionType,
    },
)
_OptionalCreateOrderInputRequestTypeDef = TypedDict(
    "_OptionalCreateOrderInputRequestTypeDef",
    {
        "PaymentTerm": Literal["THREE_YEARS"],
    },
    total=False,
)

class CreateOrderInputRequestTypeDef(
    _RequiredCreateOrderInputRequestTypeDef, _OptionalCreateOrderInputRequestTypeDef
):
    pass

CreateOrderOutputTypeDef = TypedDict(
    "CreateOrderOutputTypeDef",
    {
        "Order": "OrderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateOutpostInputRequestTypeDef = TypedDict(
    "_RequiredCreateOutpostInputRequestTypeDef",
    {
        "Name": str,
        "SiteId": str,
    },
)
_OptionalCreateOutpostInputRequestTypeDef = TypedDict(
    "_OptionalCreateOutpostInputRequestTypeDef",
    {
        "Description": str,
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateOutpostInputRequestTypeDef(
    _RequiredCreateOutpostInputRequestTypeDef, _OptionalCreateOutpostInputRequestTypeDef
):
    pass

CreateOutpostOutputTypeDef = TypedDict(
    "CreateOutpostOutputTypeDef",
    {
        "Outpost": "OutpostTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteOutpostInputRequestTypeDef = TypedDict(
    "DeleteOutpostInputRequestTypeDef",
    {
        "OutpostId": str,
    },
)

DeleteSiteInputRequestTypeDef = TypedDict(
    "DeleteSiteInputRequestTypeDef",
    {
        "SiteId": str,
    },
)

GetOutpostInputRequestTypeDef = TypedDict(
    "GetOutpostInputRequestTypeDef",
    {
        "OutpostId": str,
    },
)

_RequiredGetOutpostInstanceTypesInputRequestTypeDef = TypedDict(
    "_RequiredGetOutpostInstanceTypesInputRequestTypeDef",
    {
        "OutpostId": str,
    },
)
_OptionalGetOutpostInstanceTypesInputRequestTypeDef = TypedDict(
    "_OptionalGetOutpostInstanceTypesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetOutpostInstanceTypesInputRequestTypeDef(
    _RequiredGetOutpostInstanceTypesInputRequestTypeDef,
    _OptionalGetOutpostInstanceTypesInputRequestTypeDef,
):
    pass

GetOutpostInstanceTypesOutputTypeDef = TypedDict(
    "GetOutpostInstanceTypesOutputTypeDef",
    {
        "InstanceTypes": List["InstanceTypeItemTypeDef"],
        "NextToken": str,
        "OutpostId": str,
        "OutpostArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOutpostOutputTypeDef = TypedDict(
    "GetOutpostOutputTypeDef",
    {
        "Outpost": "OutpostTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceTypeItemTypeDef = TypedDict(
    "InstanceTypeItemTypeDef",
    {
        "InstanceType": str,
    },
    total=False,
)

LineItemRequestTypeDef = TypedDict(
    "LineItemRequestTypeDef",
    {
        "CatalogItemId": str,
        "Quantity": int,
    },
    total=False,
)

LineItemTypeDef = TypedDict(
    "LineItemTypeDef",
    {
        "CatalogItemId": str,
        "LineItemId": str,
        "Quantity": int,
        "Status": str,
    },
    total=False,
)

ListOutpostsInputRequestTypeDef = TypedDict(
    "ListOutpostsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "LifeCycleStatusFilter": List[str],
        "AvailabilityZoneFilter": List[str],
        "AvailabilityZoneIdFilter": List[str],
    },
    total=False,
)

ListOutpostsOutputTypeDef = TypedDict(
    "ListOutpostsOutputTypeDef",
    {
        "Outposts": List["OutpostTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSitesInputRequestTypeDef = TypedDict(
    "ListSitesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListSitesOutputTypeDef = TypedDict(
    "ListSitesOutputTypeDef",
    {
        "Sites": List["SiteTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OrderTypeDef = TypedDict(
    "OrderTypeDef",
    {
        "OutpostId": str,
        "OrderId": str,
        "Status": OrderStatusType,
        "LineItems": List["LineItemTypeDef"],
        "PaymentOption": PaymentOptionType,
        "OrderSubmissionDate": datetime,
        "OrderFulfilledDate": datetime,
    },
    total=False,
)

OutpostTypeDef = TypedDict(
    "OutpostTypeDef",
    {
        "OutpostId": str,
        "OwnerId": str,
        "OutpostArn": str,
        "SiteId": str,
        "Name": str,
        "Description": str,
        "LifeCycleStatus": str,
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "Tags": Dict[str, str],
        "SiteArn": str,
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

SiteTypeDef = TypedDict(
    "SiteTypeDef",
    {
        "SiteId": str,
        "AccountId": str,
        "Name": str,
        "Description": str,
        "Tags": Dict[str, str],
        "SiteArn": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)
