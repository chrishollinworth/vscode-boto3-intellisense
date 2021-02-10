"""
Main interface for outposts service type definitions.

Usage::

    ```python
    from mypy_boto3_outposts.type_defs import InstanceTypeItemTypeDef

    data: InstanceTypeItemTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "InstanceTypeItemTypeDef",
    "OutpostTypeDef",
    "ResponseMetadata",
    "SiteTypeDef",
    "CreateOutpostOutputTypeDef",
    "GetOutpostInstanceTypesOutputTypeDef",
    "GetOutpostOutputTypeDef",
    "ListOutpostsOutputTypeDef",
    "ListSitesOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
)

InstanceTypeItemTypeDef = TypedDict("InstanceTypeItemTypeDef", {"InstanceType": str}, total=False)

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
    },
    total=False,
)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
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
    {"SiteId": str, "AccountId": str, "Name": str, "Description": str, "Tags": Dict[str, str]},
    total=False,
)

CreateOutpostOutputTypeDef = TypedDict(
    "CreateOutpostOutputTypeDef",
    {"Outpost": "OutpostTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetOutpostInstanceTypesOutputTypeDef = TypedDict(
    "GetOutpostInstanceTypesOutputTypeDef",
    {
        "InstanceTypes": List["InstanceTypeItemTypeDef"],
        "NextToken": str,
        "OutpostId": str,
        "OutpostArn": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetOutpostOutputTypeDef = TypedDict(
    "GetOutpostOutputTypeDef",
    {"Outpost": "OutpostTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListOutpostsOutputTypeDef = TypedDict(
    "ListOutpostsOutputTypeDef",
    {"Outposts": List["OutpostTypeDef"], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListSitesOutputTypeDef = TypedDict(
    "ListSitesOutputTypeDef",
    {"Sites": List["SiteTypeDef"], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)
