"""
Type annotations for mediastore service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediastore.type_defs import ContainerTypeDef

    data: ContainerTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import ContainerLevelMetricsType, ContainerStatusType, MethodNameType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ContainerTypeDef",
    "CorsRuleTypeDef",
    "CreateContainerInputRequestTypeDef",
    "CreateContainerOutputTypeDef",
    "DeleteContainerInputRequestTypeDef",
    "DeleteContainerPolicyInputRequestTypeDef",
    "DeleteCorsPolicyInputRequestTypeDef",
    "DeleteLifecyclePolicyInputRequestTypeDef",
    "DeleteMetricPolicyInputRequestTypeDef",
    "DescribeContainerInputRequestTypeDef",
    "DescribeContainerOutputTypeDef",
    "GetContainerPolicyInputRequestTypeDef",
    "GetContainerPolicyOutputTypeDef",
    "GetCorsPolicyInputRequestTypeDef",
    "GetCorsPolicyOutputTypeDef",
    "GetLifecyclePolicyInputRequestTypeDef",
    "GetLifecyclePolicyOutputTypeDef",
    "GetMetricPolicyInputRequestTypeDef",
    "GetMetricPolicyOutputTypeDef",
    "ListContainersInputRequestTypeDef",
    "ListContainersOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MetricPolicyRuleTypeDef",
    "MetricPolicyTypeDef",
    "PaginatorConfigTypeDef",
    "PutContainerPolicyInputRequestTypeDef",
    "PutCorsPolicyInputRequestTypeDef",
    "PutLifecyclePolicyInputRequestTypeDef",
    "PutMetricPolicyInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "StartAccessLoggingInputRequestTypeDef",
    "StopAccessLoggingInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagTypeDef",
    "UntagResourceInputRequestTypeDef",
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "Endpoint": str,
        "CreationTime": datetime,
        "ARN": str,
        "Name": str,
        "Status": ContainerStatusType,
        "AccessLoggingEnabled": bool,
    },
    total=False,
)

_RequiredCorsRuleTypeDef = TypedDict(
    "_RequiredCorsRuleTypeDef",
    {
        "AllowedOrigins": List[str],
        "AllowedHeaders": List[str],
    },
)
_OptionalCorsRuleTypeDef = TypedDict(
    "_OptionalCorsRuleTypeDef",
    {
        "AllowedMethods": List[MethodNameType],
        "MaxAgeSeconds": int,
        "ExposeHeaders": List[str],
    },
    total=False,
)

class CorsRuleTypeDef(_RequiredCorsRuleTypeDef, _OptionalCorsRuleTypeDef):
    pass

_RequiredCreateContainerInputRequestTypeDef = TypedDict(
    "_RequiredCreateContainerInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)
_OptionalCreateContainerInputRequestTypeDef = TypedDict(
    "_OptionalCreateContainerInputRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateContainerInputRequestTypeDef(
    _RequiredCreateContainerInputRequestTypeDef, _OptionalCreateContainerInputRequestTypeDef
):
    pass

CreateContainerOutputTypeDef = TypedDict(
    "CreateContainerOutputTypeDef",
    {
        "Container": "ContainerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteContainerInputRequestTypeDef = TypedDict(
    "DeleteContainerInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

DeleteContainerPolicyInputRequestTypeDef = TypedDict(
    "DeleteContainerPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

DeleteCorsPolicyInputRequestTypeDef = TypedDict(
    "DeleteCorsPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

DeleteLifecyclePolicyInputRequestTypeDef = TypedDict(
    "DeleteLifecyclePolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

DeleteMetricPolicyInputRequestTypeDef = TypedDict(
    "DeleteMetricPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

DescribeContainerInputRequestTypeDef = TypedDict(
    "DescribeContainerInputRequestTypeDef",
    {
        "ContainerName": str,
    },
    total=False,
)

DescribeContainerOutputTypeDef = TypedDict(
    "DescribeContainerOutputTypeDef",
    {
        "Container": "ContainerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerPolicyInputRequestTypeDef = TypedDict(
    "GetContainerPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

GetContainerPolicyOutputTypeDef = TypedDict(
    "GetContainerPolicyOutputTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCorsPolicyInputRequestTypeDef = TypedDict(
    "GetCorsPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

GetCorsPolicyOutputTypeDef = TypedDict(
    "GetCorsPolicyOutputTypeDef",
    {
        "CorsPolicy": List["CorsRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLifecyclePolicyInputRequestTypeDef = TypedDict(
    "GetLifecyclePolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

GetLifecyclePolicyOutputTypeDef = TypedDict(
    "GetLifecyclePolicyOutputTypeDef",
    {
        "LifecyclePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMetricPolicyInputRequestTypeDef = TypedDict(
    "GetMetricPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

GetMetricPolicyOutputTypeDef = TypedDict(
    "GetMetricPolicyOutputTypeDef",
    {
        "MetricPolicy": "MetricPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContainersInputRequestTypeDef = TypedDict(
    "ListContainersInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListContainersOutputTypeDef = TypedDict(
    "ListContainersOutputTypeDef",
    {
        "Containers": List["ContainerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "Resource": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricPolicyRuleTypeDef = TypedDict(
    "MetricPolicyRuleTypeDef",
    {
        "ObjectGroup": str,
        "ObjectGroupName": str,
    },
)

_RequiredMetricPolicyTypeDef = TypedDict(
    "_RequiredMetricPolicyTypeDef",
    {
        "ContainerLevelMetrics": ContainerLevelMetricsType,
    },
)
_OptionalMetricPolicyTypeDef = TypedDict(
    "_OptionalMetricPolicyTypeDef",
    {
        "MetricPolicyRules": List["MetricPolicyRuleTypeDef"],
    },
    total=False,
)

class MetricPolicyTypeDef(_RequiredMetricPolicyTypeDef, _OptionalMetricPolicyTypeDef):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PutContainerPolicyInputRequestTypeDef = TypedDict(
    "PutContainerPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
        "Policy": str,
    },
)

PutCorsPolicyInputRequestTypeDef = TypedDict(
    "PutCorsPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
        "CorsPolicy": List["CorsRuleTypeDef"],
    },
)

PutLifecyclePolicyInputRequestTypeDef = TypedDict(
    "PutLifecyclePolicyInputRequestTypeDef",
    {
        "ContainerName": str,
        "LifecyclePolicy": str,
    },
)

PutMetricPolicyInputRequestTypeDef = TypedDict(
    "PutMetricPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
        "MetricPolicy": "MetricPolicyTypeDef",
    },
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

StartAccessLoggingInputRequestTypeDef = TypedDict(
    "StartAccessLoggingInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

StopAccessLoggingInputRequestTypeDef = TypedDict(
    "StopAccessLoggingInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "Resource": str,
        "Tags": List["TagTypeDef"],
    },
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "Resource": str,
        "TagKeys": List[str],
    },
)
