"""
Main interface for outposts service type definitions.

Usage::

    ```python
    from mypy_boto3_outposts.type_defs import InstanceTypeItemTypeDef

    data: InstanceTypeItemTypeDef = {...}
    ```
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "InstanceTypeItemTypeDef",
    "OutpostTypeDef",
    "SiteTypeDef",
    "CreateOutpostOutputTypeDef",
    "GetOutpostInstanceTypesOutputTypeDef",
    "GetOutpostOutputTypeDef",
    "ListOutpostsOutputTypeDef",
    "ListSitesOutputTypeDef",
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
    },
    total=False,
)

SiteTypeDef = TypedDict(
    "SiteTypeDef", {"SiteId": str, "AccountId": str, "Name": str, "Description": str}, total=False
)

CreateOutpostOutputTypeDef = TypedDict(
    "CreateOutpostOutputTypeDef", {"Outpost": "OutpostTypeDef"}, total=False
)

GetOutpostInstanceTypesOutputTypeDef = TypedDict(
    "GetOutpostInstanceTypesOutputTypeDef",
    {
        "InstanceTypes": List["InstanceTypeItemTypeDef"],
        "NextToken": str,
        "OutpostId": str,
        "OutpostArn": str,
    },
    total=False,
)

GetOutpostOutputTypeDef = TypedDict(
    "GetOutpostOutputTypeDef", {"Outpost": "OutpostTypeDef"}, total=False
)

ListOutpostsOutputTypeDef = TypedDict(
    "ListOutpostsOutputTypeDef", {"Outposts": List["OutpostTypeDef"], "NextToken": str}, total=False
)

ListSitesOutputTypeDef = TypedDict(
    "ListSitesOutputTypeDef", {"Sites": List["SiteTypeDef"], "NextToken": str}, total=False
)
