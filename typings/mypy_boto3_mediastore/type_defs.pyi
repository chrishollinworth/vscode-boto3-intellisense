"""
Main interface for mediastore service type definitions.

Usage::

    ```python
    from mypy_boto3_mediastore.type_defs import ContainerTypeDef

    data: ContainerTypeDef = {...}
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
    "ContainerTypeDef",
    "CorsRuleTypeDef",
    "MetricPolicyRuleTypeDef",
    "MetricPolicyTypeDef",
    "TagTypeDef",
    "CreateContainerOutputTypeDef",
    "DescribeContainerOutputTypeDef",
    "GetContainerPolicyOutputTypeDef",
    "GetCorsPolicyOutputTypeDef",
    "GetLifecyclePolicyOutputTypeDef",
    "GetMetricPolicyOutputTypeDef",
    "ListContainersOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "PaginatorConfigTypeDef",
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "Endpoint": str,
        "CreationTime": datetime,
        "ARN": str,
        "Name": str,
        "Status": Literal["ACTIVE", "CREATING", "DELETING"],
        "AccessLoggingEnabled": bool,
    },
    total=False,
)

_RequiredCorsRuleTypeDef = TypedDict(
    "_RequiredCorsRuleTypeDef", {"AllowedOrigins": List[str], "AllowedHeaders": List[str]}
)
_OptionalCorsRuleTypeDef = TypedDict(
    "_OptionalCorsRuleTypeDef",
    {
        "AllowedMethods": List[Literal["PUT", "GET", "DELETE", "HEAD"]],
        "MaxAgeSeconds": int,
        "ExposeHeaders": List[str],
    },
    total=False,
)


class CorsRuleTypeDef(_RequiredCorsRuleTypeDef, _OptionalCorsRuleTypeDef):
    pass


MetricPolicyRuleTypeDef = TypedDict(
    "MetricPolicyRuleTypeDef", {"ObjectGroup": str, "ObjectGroupName": str}
)

_RequiredMetricPolicyTypeDef = TypedDict(
    "_RequiredMetricPolicyTypeDef", {"ContainerLevelMetrics": Literal["ENABLED", "DISABLED"]}
)
_OptionalMetricPolicyTypeDef = TypedDict(
    "_OptionalMetricPolicyTypeDef",
    {"MetricPolicyRules": List["MetricPolicyRuleTypeDef"]},
    total=False,
)


class MetricPolicyTypeDef(_RequiredMetricPolicyTypeDef, _OptionalMetricPolicyTypeDef):
    pass


_RequiredTagTypeDef = TypedDict("_RequiredTagTypeDef", {"Key": str})
_OptionalTagTypeDef = TypedDict("_OptionalTagTypeDef", {"Value": str}, total=False)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


CreateContainerOutputTypeDef = TypedDict(
    "CreateContainerOutputTypeDef", {"Container": "ContainerTypeDef"}
)

DescribeContainerOutputTypeDef = TypedDict(
    "DescribeContainerOutputTypeDef", {"Container": "ContainerTypeDef"}, total=False
)

GetContainerPolicyOutputTypeDef = TypedDict("GetContainerPolicyOutputTypeDef", {"Policy": str})

GetCorsPolicyOutputTypeDef = TypedDict(
    "GetCorsPolicyOutputTypeDef", {"CorsPolicy": List["CorsRuleTypeDef"]}
)

GetLifecyclePolicyOutputTypeDef = TypedDict(
    "GetLifecyclePolicyOutputTypeDef", {"LifecyclePolicy": str}
)

GetMetricPolicyOutputTypeDef = TypedDict(
    "GetMetricPolicyOutputTypeDef", {"MetricPolicy": "MetricPolicyTypeDef"}
)

_RequiredListContainersOutputTypeDef = TypedDict(
    "_RequiredListContainersOutputTypeDef", {"Containers": List["ContainerTypeDef"]}
)
_OptionalListContainersOutputTypeDef = TypedDict(
    "_OptionalListContainersOutputTypeDef", {"NextToken": str}, total=False
)


class ListContainersOutputTypeDef(
    _RequiredListContainersOutputTypeDef, _OptionalListContainersOutputTypeDef
):
    pass


ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
