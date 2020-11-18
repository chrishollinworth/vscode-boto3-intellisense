"""
Main interface for s3outposts service type definitions.

Usage::

    ```python
    from mypy_boto3_s3outposts.type_defs import EndpointTypeDef

    data: EndpointTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "EndpointTypeDef",
    "NetworkInterfaceTypeDef",
    "CreateEndpointResultTypeDef",
    "ListEndpointsResultTypeDef",
    "PaginatorConfigTypeDef",
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "EndpointArn": str,
        "OutpostsId": str,
        "CidrBlock": str,
        "Status": Literal["PENDING", "AVAILABLE"],
        "CreationTime": datetime,
        "NetworkInterfaces": List["NetworkInterfaceTypeDef"],
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef", {"NetworkInterfaceId": str}, total=False
)

CreateEndpointResultTypeDef = TypedDict(
    "CreateEndpointResultTypeDef", {"EndpointArn": str}, total=False
)

ListEndpointsResultTypeDef = TypedDict(
    "ListEndpointsResultTypeDef",
    {"Endpoints": List["EndpointTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
