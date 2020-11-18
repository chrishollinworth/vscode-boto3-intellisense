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
    "ContainerTypeDef",
    "CorsRuleTypeDef",
    "MetricPolicyRuleTypeDef",
    "MetricPolicyTypeDef",
    "ResponseMetadata",
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

_RequiredTagTypeDef = TypedDict("_RequiredTagTypeDef", {"Key": str})
_OptionalTagTypeDef = TypedDict("_OptionalTagTypeDef", {"Value": str}, total=False)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


_RequiredCreateContainerOutputTypeDef = TypedDict(
    "_RequiredCreateContainerOutputTypeDef", {"Container": "ContainerTypeDef"}
)
_OptionalCreateContainerOutputTypeDef = TypedDict(
    "_OptionalCreateContainerOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class CreateContainerOutputTypeDef(
    _RequiredCreateContainerOutputTypeDef, _OptionalCreateContainerOutputTypeDef
):
    pass


DescribeContainerOutputTypeDef = TypedDict(
    "DescribeContainerOutputTypeDef",
    {"Container": "ContainerTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredGetContainerPolicyOutputTypeDef = TypedDict(
    "_RequiredGetContainerPolicyOutputTypeDef", {"Policy": str}
)
_OptionalGetContainerPolicyOutputTypeDef = TypedDict(
    "_OptionalGetContainerPolicyOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class GetContainerPolicyOutputTypeDef(
    _RequiredGetContainerPolicyOutputTypeDef, _OptionalGetContainerPolicyOutputTypeDef
):
    pass


_RequiredGetCorsPolicyOutputTypeDef = TypedDict(
    "_RequiredGetCorsPolicyOutputTypeDef", {"CorsPolicy": List["CorsRuleTypeDef"]}
)
_OptionalGetCorsPolicyOutputTypeDef = TypedDict(
    "_OptionalGetCorsPolicyOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class GetCorsPolicyOutputTypeDef(
    _RequiredGetCorsPolicyOutputTypeDef, _OptionalGetCorsPolicyOutputTypeDef
):
    pass


_RequiredGetLifecyclePolicyOutputTypeDef = TypedDict(
    "_RequiredGetLifecyclePolicyOutputTypeDef", {"LifecyclePolicy": str}
)
_OptionalGetLifecyclePolicyOutputTypeDef = TypedDict(
    "_OptionalGetLifecyclePolicyOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class GetLifecyclePolicyOutputTypeDef(
    _RequiredGetLifecyclePolicyOutputTypeDef, _OptionalGetLifecyclePolicyOutputTypeDef
):
    pass


_RequiredGetMetricPolicyOutputTypeDef = TypedDict(
    "_RequiredGetMetricPolicyOutputTypeDef", {"MetricPolicy": "MetricPolicyTypeDef"}
)
_OptionalGetMetricPolicyOutputTypeDef = TypedDict(
    "_OptionalGetMetricPolicyOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class GetMetricPolicyOutputTypeDef(
    _RequiredGetMetricPolicyOutputTypeDef, _OptionalGetMetricPolicyOutputTypeDef
):
    pass


_RequiredListContainersOutputTypeDef = TypedDict(
    "_RequiredListContainersOutputTypeDef", {"Containers": List["ContainerTypeDef"]}
)
_OptionalListContainersOutputTypeDef = TypedDict(
    "_OptionalListContainersOutputTypeDef",
    {"NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListContainersOutputTypeDef(
    _RequiredListContainersOutputTypeDef, _OptionalListContainersOutputTypeDef
):
    pass


ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {"Tags": List["TagTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
