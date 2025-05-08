"""
Type annotations for mediastore service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_mediastore.type_defs import ContainerTypeDef

    data: ContainerTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import ContainerLevelMetricsType, ContainerStatusType, MethodNameType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ContainerTypeDef",
    "CorsRuleOutputTypeDef",
    "CorsRuleTypeDef",
    "CorsRuleUnionTypeDef",
    "CreateContainerInputTypeDef",
    "CreateContainerOutputTypeDef",
    "DeleteContainerInputTypeDef",
    "DeleteContainerPolicyInputTypeDef",
    "DeleteCorsPolicyInputTypeDef",
    "DeleteLifecyclePolicyInputTypeDef",
    "DeleteMetricPolicyInputTypeDef",
    "DescribeContainerInputTypeDef",
    "DescribeContainerOutputTypeDef",
    "GetContainerPolicyInputTypeDef",
    "GetContainerPolicyOutputTypeDef",
    "GetCorsPolicyInputTypeDef",
    "GetCorsPolicyOutputTypeDef",
    "GetLifecyclePolicyInputTypeDef",
    "GetLifecyclePolicyOutputTypeDef",
    "GetMetricPolicyInputTypeDef",
    "GetMetricPolicyOutputTypeDef",
    "ListContainersInputPaginateTypeDef",
    "ListContainersInputTypeDef",
    "ListContainersOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MetricPolicyOutputTypeDef",
    "MetricPolicyRuleTypeDef",
    "MetricPolicyTypeDef",
    "MetricPolicyUnionTypeDef",
    "PaginatorConfigTypeDef",
    "PutContainerPolicyInputTypeDef",
    "PutCorsPolicyInputTypeDef",
    "PutLifecyclePolicyInputTypeDef",
    "PutMetricPolicyInputTypeDef",
    "ResponseMetadataTypeDef",
    "StartAccessLoggingInputTypeDef",
    "StopAccessLoggingInputTypeDef",
    "TagResourceInputTypeDef",
    "TagTypeDef",
    "UntagResourceInputTypeDef",
)

class ContainerTypeDef(TypedDict):
    Endpoint: NotRequired[str]
    CreationTime: NotRequired[datetime]
    ARN: NotRequired[str]
    Name: NotRequired[str]
    Status: NotRequired[ContainerStatusType]
    AccessLoggingEnabled: NotRequired[bool]

class CorsRuleOutputTypeDef(TypedDict):
    AllowedOrigins: List[str]
    AllowedHeaders: List[str]
    AllowedMethods: NotRequired[List[MethodNameType]]
    MaxAgeSeconds: NotRequired[int]
    ExposeHeaders: NotRequired[List[str]]

class CorsRuleTypeDef(TypedDict):
    AllowedOrigins: Sequence[str]
    AllowedHeaders: Sequence[str]
    AllowedMethods: NotRequired[Sequence[MethodNameType]]
    MaxAgeSeconds: NotRequired[int]
    ExposeHeaders: NotRequired[Sequence[str]]

class TagTypeDef(TypedDict):
    Key: str
    Value: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteContainerInputTypeDef(TypedDict):
    ContainerName: str

class DeleteContainerPolicyInputTypeDef(TypedDict):
    ContainerName: str

class DeleteCorsPolicyInputTypeDef(TypedDict):
    ContainerName: str

class DeleteLifecyclePolicyInputTypeDef(TypedDict):
    ContainerName: str

class DeleteMetricPolicyInputTypeDef(TypedDict):
    ContainerName: str

class DescribeContainerInputTypeDef(TypedDict):
    ContainerName: NotRequired[str]

class GetContainerPolicyInputTypeDef(TypedDict):
    ContainerName: str

class GetCorsPolicyInputTypeDef(TypedDict):
    ContainerName: str

class GetLifecyclePolicyInputTypeDef(TypedDict):
    ContainerName: str

class GetMetricPolicyInputTypeDef(TypedDict):
    ContainerName: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListContainersInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTagsForResourceInputTypeDef(TypedDict):
    Resource: str

class MetricPolicyRuleTypeDef(TypedDict):
    ObjectGroup: str
    ObjectGroupName: str

class PutContainerPolicyInputTypeDef(TypedDict):
    ContainerName: str
    Policy: str

class PutLifecyclePolicyInputTypeDef(TypedDict):
    ContainerName: str
    LifecyclePolicy: str

class StartAccessLoggingInputTypeDef(TypedDict):
    ContainerName: str

class StopAccessLoggingInputTypeDef(TypedDict):
    ContainerName: str

class UntagResourceInputTypeDef(TypedDict):
    Resource: str
    TagKeys: Sequence[str]

CorsRuleUnionTypeDef = Union[CorsRuleTypeDef, CorsRuleOutputTypeDef]

class CreateContainerInputTypeDef(TypedDict):
    ContainerName: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class TagResourceInputTypeDef(TypedDict):
    Resource: str
    Tags: Sequence[TagTypeDef]

CreateContainerOutputTypeDef = TypedDict(
    "CreateContainerOutputTypeDef",
    {
        "Container": ContainerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeContainerOutputTypeDef = TypedDict(
    "DescribeContainerOutputTypeDef",
    {
        "Container": ContainerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetContainerPolicyOutputTypeDef(TypedDict):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCorsPolicyOutputTypeDef(TypedDict):
    CorsPolicy: List[CorsRuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetLifecyclePolicyOutputTypeDef(TypedDict):
    LifecyclePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListContainersOutputTypeDef(TypedDict):
    Containers: List[ContainerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceOutputTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListContainersInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class MetricPolicyOutputTypeDef(TypedDict):
    ContainerLevelMetrics: ContainerLevelMetricsType
    MetricPolicyRules: NotRequired[List[MetricPolicyRuleTypeDef]]

class MetricPolicyTypeDef(TypedDict):
    ContainerLevelMetrics: ContainerLevelMetricsType
    MetricPolicyRules: NotRequired[Sequence[MetricPolicyRuleTypeDef]]

class PutCorsPolicyInputTypeDef(TypedDict):
    ContainerName: str
    CorsPolicy: Sequence[CorsRuleUnionTypeDef]

class GetMetricPolicyOutputTypeDef(TypedDict):
    MetricPolicy: MetricPolicyOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

MetricPolicyUnionTypeDef = Union[MetricPolicyTypeDef, MetricPolicyOutputTypeDef]

class PutMetricPolicyInputTypeDef(TypedDict):
    ContainerName: str
    MetricPolicy: MetricPolicyUnionTypeDef
