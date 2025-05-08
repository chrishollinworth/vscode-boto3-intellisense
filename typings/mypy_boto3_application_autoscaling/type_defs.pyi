"""
Type annotations for application-autoscaling service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_application_autoscaling.type_defs import AlarmTypeDef

    data: AlarmTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AdjustmentTypeType,
    MetricAggregationTypeType,
    MetricStatisticType,
    MetricTypeType,
    PolicyTypeType,
    PredictiveScalingMaxCapacityBreachBehaviorType,
    PredictiveScalingModeType,
    ScalableDimensionType,
    ScalingActivityStatusCodeType,
    ServiceNamespaceType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AlarmTypeDef",
    "CapacityForecastTypeDef",
    "CustomizedMetricSpecificationOutputTypeDef",
    "CustomizedMetricSpecificationTypeDef",
    "DeleteScalingPolicyRequestTypeDef",
    "DeleteScheduledActionRequestTypeDef",
    "DeregisterScalableTargetRequestTypeDef",
    "DescribeScalableTargetsRequestPaginateTypeDef",
    "DescribeScalableTargetsRequestTypeDef",
    "DescribeScalableTargetsResponseTypeDef",
    "DescribeScalingActivitiesRequestPaginateTypeDef",
    "DescribeScalingActivitiesRequestTypeDef",
    "DescribeScalingActivitiesResponseTypeDef",
    "DescribeScalingPoliciesRequestPaginateTypeDef",
    "DescribeScalingPoliciesRequestTypeDef",
    "DescribeScalingPoliciesResponseTypeDef",
    "DescribeScheduledActionsRequestPaginateTypeDef",
    "DescribeScheduledActionsRequestTypeDef",
    "DescribeScheduledActionsResponseTypeDef",
    "GetPredictiveScalingForecastRequestTypeDef",
    "GetPredictiveScalingForecastResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoadForecastTypeDef",
    "MetricDimensionTypeDef",
    "NotScaledReasonTypeDef",
    "PaginatorConfigTypeDef",
    "PredefinedMetricSpecificationTypeDef",
    "PredictiveScalingCustomizedMetricSpecificationOutputTypeDef",
    "PredictiveScalingCustomizedMetricSpecificationTypeDef",
    "PredictiveScalingMetricDataQueryOutputTypeDef",
    "PredictiveScalingMetricDataQueryTypeDef",
    "PredictiveScalingMetricDimensionTypeDef",
    "PredictiveScalingMetricOutputTypeDef",
    "PredictiveScalingMetricSpecificationOutputTypeDef",
    "PredictiveScalingMetricSpecificationTypeDef",
    "PredictiveScalingMetricStatOutputTypeDef",
    "PredictiveScalingMetricStatTypeDef",
    "PredictiveScalingMetricTypeDef",
    "PredictiveScalingPolicyConfigurationOutputTypeDef",
    "PredictiveScalingPolicyConfigurationTypeDef",
    "PredictiveScalingPolicyConfigurationUnionTypeDef",
    "PredictiveScalingPredefinedLoadMetricSpecificationTypeDef",
    "PredictiveScalingPredefinedMetricPairSpecificationTypeDef",
    "PredictiveScalingPredefinedScalingMetricSpecificationTypeDef",
    "PutScalingPolicyRequestTypeDef",
    "PutScalingPolicyResponseTypeDef",
    "PutScheduledActionRequestTypeDef",
    "RegisterScalableTargetRequestTypeDef",
    "RegisterScalableTargetResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ScalableTargetActionTypeDef",
    "ScalableTargetTypeDef",
    "ScalingActivityTypeDef",
    "ScalingPolicyTypeDef",
    "ScheduledActionTypeDef",
    "StepAdjustmentTypeDef",
    "StepScalingPolicyConfigurationOutputTypeDef",
    "StepScalingPolicyConfigurationTypeDef",
    "StepScalingPolicyConfigurationUnionTypeDef",
    "SuspendedStateTypeDef",
    "TagResourceRequestTypeDef",
    "TargetTrackingMetricDataQueryOutputTypeDef",
    "TargetTrackingMetricDataQueryTypeDef",
    "TargetTrackingMetricDimensionTypeDef",
    "TargetTrackingMetricOutputTypeDef",
    "TargetTrackingMetricStatOutputTypeDef",
    "TargetTrackingMetricStatTypeDef",
    "TargetTrackingMetricTypeDef",
    "TargetTrackingScalingPolicyConfigurationOutputTypeDef",
    "TargetTrackingScalingPolicyConfigurationTypeDef",
    "TargetTrackingScalingPolicyConfigurationUnionTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
)

class AlarmTypeDef(TypedDict):
    AlarmName: str
    AlarmARN: str

class CapacityForecastTypeDef(TypedDict):
    Timestamps: List[datetime]
    Values: List[float]

class MetricDimensionTypeDef(TypedDict):
    Name: str
    Value: str

class DeleteScalingPolicyRequestTypeDef(TypedDict):
    PolicyName: str
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType

class DeleteScheduledActionRequestTypeDef(TypedDict):
    ServiceNamespace: ServiceNamespaceType
    ScheduledActionName: str
    ResourceId: str
    ScalableDimension: ScalableDimensionType

class DeregisterScalableTargetRequestTypeDef(TypedDict):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeScalableTargetsRequestTypeDef(TypedDict):
    ServiceNamespace: ServiceNamespaceType
    ResourceIds: NotRequired[Sequence[str]]
    ScalableDimension: NotRequired[ScalableDimensionType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DescribeScalingActivitiesRequestTypeDef(TypedDict):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: NotRequired[str]
    ScalableDimension: NotRequired[ScalableDimensionType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    IncludeNotScaledActivities: NotRequired[bool]

class DescribeScalingPoliciesRequestTypeDef(TypedDict):
    ServiceNamespace: ServiceNamespaceType
    PolicyNames: NotRequired[Sequence[str]]
    ResourceId: NotRequired[str]
    ScalableDimension: NotRequired[ScalableDimensionType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeScheduledActionsRequestTypeDef(TypedDict):
    ServiceNamespace: ServiceNamespaceType
    ScheduledActionNames: NotRequired[Sequence[str]]
    ResourceId: NotRequired[str]
    ScalableDimension: NotRequired[ScalableDimensionType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str

class NotScaledReasonTypeDef(TypedDict):
    Code: str
    MaxCapacity: NotRequired[int]
    MinCapacity: NotRequired[int]
    CurrentCapacity: NotRequired[int]

class PredefinedMetricSpecificationTypeDef(TypedDict):
    PredefinedMetricType: MetricTypeType
    ResourceLabel: NotRequired[str]

class PredictiveScalingMetricDimensionTypeDef(TypedDict):
    Name: str
    Value: str

class PredictiveScalingPredefinedLoadMetricSpecificationTypeDef(TypedDict):
    PredefinedMetricType: str
    ResourceLabel: NotRequired[str]

class PredictiveScalingPredefinedMetricPairSpecificationTypeDef(TypedDict):
    PredefinedMetricType: str
    ResourceLabel: NotRequired[str]

class PredictiveScalingPredefinedScalingMetricSpecificationTypeDef(TypedDict):
    PredefinedMetricType: str
    ResourceLabel: NotRequired[str]

class ScalableTargetActionTypeDef(TypedDict):
    MinCapacity: NotRequired[int]
    MaxCapacity: NotRequired[int]

class SuspendedStateTypeDef(TypedDict):
    DynamicScalingInSuspended: NotRequired[bool]
    DynamicScalingOutSuspended: NotRequired[bool]
    ScheduledScalingSuspended: NotRequired[bool]

class StepAdjustmentTypeDef(TypedDict):
    ScalingAdjustment: int
    MetricIntervalLowerBound: NotRequired[float]
    MetricIntervalUpperBound: NotRequired[float]

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Mapping[str, str]

class TargetTrackingMetricDimensionTypeDef(TypedDict):
    Name: str
    Value: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class DescribeScalableTargetsRequestPaginateTypeDef(TypedDict):
    ServiceNamespace: ServiceNamespaceType
    ResourceIds: NotRequired[Sequence[str]]
    ScalableDimension: NotRequired[ScalableDimensionType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeScalingActivitiesRequestPaginateTypeDef(TypedDict):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: NotRequired[str]
    ScalableDimension: NotRequired[ScalableDimensionType]
    IncludeNotScaledActivities: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeScalingPoliciesRequestPaginateTypeDef(TypedDict):
    ServiceNamespace: ServiceNamespaceType
    PolicyNames: NotRequired[Sequence[str]]
    ResourceId: NotRequired[str]
    ScalableDimension: NotRequired[ScalableDimensionType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeScheduledActionsRequestPaginateTypeDef(TypedDict):
    ServiceNamespace: ServiceNamespaceType
    ScheduledActionNames: NotRequired[Sequence[str]]
    ResourceId: NotRequired[str]
    ScalableDimension: NotRequired[ScalableDimensionType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutScalingPolicyResponseTypeDef(TypedDict):
    PolicyARN: str
    Alarms: List[AlarmTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterScalableTargetResponseTypeDef(TypedDict):
    ScalableTargetARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPredictiveScalingForecastRequestTypeDef(TypedDict):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    PolicyName: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef

class ScalingActivityTypeDef(TypedDict):
    ActivityId: str
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    Description: str
    Cause: str
    StartTime: datetime
    StatusCode: ScalingActivityStatusCodeType
    EndTime: NotRequired[datetime]
    StatusMessage: NotRequired[str]
    Details: NotRequired[str]
    NotScaledReasons: NotRequired[List[NotScaledReasonTypeDef]]

class PredictiveScalingMetricOutputTypeDef(TypedDict):
    Dimensions: NotRequired[List[PredictiveScalingMetricDimensionTypeDef]]
    MetricName: NotRequired[str]
    Namespace: NotRequired[str]

class PredictiveScalingMetricTypeDef(TypedDict):
    Dimensions: NotRequired[Sequence[PredictiveScalingMetricDimensionTypeDef]]
    MetricName: NotRequired[str]
    Namespace: NotRequired[str]

class PutScheduledActionRequestTypeDef(TypedDict):
    ServiceNamespace: ServiceNamespaceType
    ScheduledActionName: str
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    Schedule: NotRequired[str]
    Timezone: NotRequired[str]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    ScalableTargetAction: NotRequired[ScalableTargetActionTypeDef]

class ScheduledActionTypeDef(TypedDict):
    ScheduledActionName: str
    ScheduledActionARN: str
    ServiceNamespace: ServiceNamespaceType
    Schedule: str
    ResourceId: str
    CreationTime: datetime
    Timezone: NotRequired[str]
    ScalableDimension: NotRequired[ScalableDimensionType]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    ScalableTargetAction: NotRequired[ScalableTargetActionTypeDef]

class RegisterScalableTargetRequestTypeDef(TypedDict):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    MinCapacity: NotRequired[int]
    MaxCapacity: NotRequired[int]
    RoleARN: NotRequired[str]
    SuspendedState: NotRequired[SuspendedStateTypeDef]
    Tags: NotRequired[Mapping[str, str]]

class ScalableTargetTypeDef(TypedDict):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    MinCapacity: int
    MaxCapacity: int
    RoleARN: str
    CreationTime: datetime
    PredictedCapacity: NotRequired[int]
    SuspendedState: NotRequired[SuspendedStateTypeDef]
    ScalableTargetARN: NotRequired[str]

class StepScalingPolicyConfigurationOutputTypeDef(TypedDict):
    AdjustmentType: NotRequired[AdjustmentTypeType]
    StepAdjustments: NotRequired[List[StepAdjustmentTypeDef]]
    MinAdjustmentMagnitude: NotRequired[int]
    Cooldown: NotRequired[int]
    MetricAggregationType: NotRequired[MetricAggregationTypeType]

class StepScalingPolicyConfigurationTypeDef(TypedDict):
    AdjustmentType: NotRequired[AdjustmentTypeType]
    StepAdjustments: NotRequired[Sequence[StepAdjustmentTypeDef]]
    MinAdjustmentMagnitude: NotRequired[int]
    Cooldown: NotRequired[int]
    MetricAggregationType: NotRequired[MetricAggregationTypeType]

class TargetTrackingMetricOutputTypeDef(TypedDict):
    Dimensions: NotRequired[List[TargetTrackingMetricDimensionTypeDef]]
    MetricName: NotRequired[str]
    Namespace: NotRequired[str]

class TargetTrackingMetricTypeDef(TypedDict):
    Dimensions: NotRequired[Sequence[TargetTrackingMetricDimensionTypeDef]]
    MetricName: NotRequired[str]
    Namespace: NotRequired[str]

class DescribeScalingActivitiesResponseTypeDef(TypedDict):
    ScalingActivities: List[ScalingActivityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PredictiveScalingMetricStatOutputTypeDef(TypedDict):
    Metric: PredictiveScalingMetricOutputTypeDef
    Stat: str
    Unit: NotRequired[str]

class PredictiveScalingMetricStatTypeDef(TypedDict):
    Metric: PredictiveScalingMetricTypeDef
    Stat: str
    Unit: NotRequired[str]

class DescribeScheduledActionsResponseTypeDef(TypedDict):
    ScheduledActions: List[ScheduledActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeScalableTargetsResponseTypeDef(TypedDict):
    ScalableTargets: List[ScalableTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

StepScalingPolicyConfigurationUnionTypeDef = Union[
    StepScalingPolicyConfigurationTypeDef, StepScalingPolicyConfigurationOutputTypeDef
]

class TargetTrackingMetricStatOutputTypeDef(TypedDict):
    Metric: TargetTrackingMetricOutputTypeDef
    Stat: str
    Unit: NotRequired[str]

class TargetTrackingMetricStatTypeDef(TypedDict):
    Metric: TargetTrackingMetricTypeDef
    Stat: str
    Unit: NotRequired[str]

class PredictiveScalingMetricDataQueryOutputTypeDef(TypedDict):
    Id: str
    Expression: NotRequired[str]
    MetricStat: NotRequired[PredictiveScalingMetricStatOutputTypeDef]
    Label: NotRequired[str]
    ReturnData: NotRequired[bool]

class PredictiveScalingMetricDataQueryTypeDef(TypedDict):
    Id: str
    Expression: NotRequired[str]
    MetricStat: NotRequired[PredictiveScalingMetricStatTypeDef]
    Label: NotRequired[str]
    ReturnData: NotRequired[bool]

class TargetTrackingMetricDataQueryOutputTypeDef(TypedDict):
    Id: str
    Expression: NotRequired[str]
    Label: NotRequired[str]
    MetricStat: NotRequired[TargetTrackingMetricStatOutputTypeDef]
    ReturnData: NotRequired[bool]

class TargetTrackingMetricDataQueryTypeDef(TypedDict):
    Id: str
    Expression: NotRequired[str]
    Label: NotRequired[str]
    MetricStat: NotRequired[TargetTrackingMetricStatTypeDef]
    ReturnData: NotRequired[bool]

class PredictiveScalingCustomizedMetricSpecificationOutputTypeDef(TypedDict):
    MetricDataQueries: List[PredictiveScalingMetricDataQueryOutputTypeDef]

class PredictiveScalingCustomizedMetricSpecificationTypeDef(TypedDict):
    MetricDataQueries: Sequence[PredictiveScalingMetricDataQueryTypeDef]

class CustomizedMetricSpecificationOutputTypeDef(TypedDict):
    MetricName: NotRequired[str]
    Namespace: NotRequired[str]
    Dimensions: NotRequired[List[MetricDimensionTypeDef]]
    Statistic: NotRequired[MetricStatisticType]
    Unit: NotRequired[str]
    Metrics: NotRequired[List[TargetTrackingMetricDataQueryOutputTypeDef]]

class CustomizedMetricSpecificationTypeDef(TypedDict):
    MetricName: NotRequired[str]
    Namespace: NotRequired[str]
    Dimensions: NotRequired[Sequence[MetricDimensionTypeDef]]
    Statistic: NotRequired[MetricStatisticType]
    Unit: NotRequired[str]
    Metrics: NotRequired[Sequence[TargetTrackingMetricDataQueryTypeDef]]

class PredictiveScalingMetricSpecificationOutputTypeDef(TypedDict):
    TargetValue: float
    PredefinedMetricPairSpecification: NotRequired[
        PredictiveScalingPredefinedMetricPairSpecificationTypeDef
    ]
    PredefinedScalingMetricSpecification: NotRequired[
        PredictiveScalingPredefinedScalingMetricSpecificationTypeDef
    ]
    PredefinedLoadMetricSpecification: NotRequired[
        PredictiveScalingPredefinedLoadMetricSpecificationTypeDef
    ]
    CustomizedScalingMetricSpecification: NotRequired[
        PredictiveScalingCustomizedMetricSpecificationOutputTypeDef
    ]
    CustomizedLoadMetricSpecification: NotRequired[
        PredictiveScalingCustomizedMetricSpecificationOutputTypeDef
    ]
    CustomizedCapacityMetricSpecification: NotRequired[
        PredictiveScalingCustomizedMetricSpecificationOutputTypeDef
    ]

class PredictiveScalingMetricSpecificationTypeDef(TypedDict):
    TargetValue: float
    PredefinedMetricPairSpecification: NotRequired[
        PredictiveScalingPredefinedMetricPairSpecificationTypeDef
    ]
    PredefinedScalingMetricSpecification: NotRequired[
        PredictiveScalingPredefinedScalingMetricSpecificationTypeDef
    ]
    PredefinedLoadMetricSpecification: NotRequired[
        PredictiveScalingPredefinedLoadMetricSpecificationTypeDef
    ]
    CustomizedScalingMetricSpecification: NotRequired[
        PredictiveScalingCustomizedMetricSpecificationTypeDef
    ]
    CustomizedLoadMetricSpecification: NotRequired[
        PredictiveScalingCustomizedMetricSpecificationTypeDef
    ]
    CustomizedCapacityMetricSpecification: NotRequired[
        PredictiveScalingCustomizedMetricSpecificationTypeDef
    ]

class TargetTrackingScalingPolicyConfigurationOutputTypeDef(TypedDict):
    TargetValue: float
    PredefinedMetricSpecification: NotRequired[PredefinedMetricSpecificationTypeDef]
    CustomizedMetricSpecification: NotRequired[CustomizedMetricSpecificationOutputTypeDef]
    ScaleOutCooldown: NotRequired[int]
    ScaleInCooldown: NotRequired[int]
    DisableScaleIn: NotRequired[bool]

class TargetTrackingScalingPolicyConfigurationTypeDef(TypedDict):
    TargetValue: float
    PredefinedMetricSpecification: NotRequired[PredefinedMetricSpecificationTypeDef]
    CustomizedMetricSpecification: NotRequired[CustomizedMetricSpecificationTypeDef]
    ScaleOutCooldown: NotRequired[int]
    ScaleInCooldown: NotRequired[int]
    DisableScaleIn: NotRequired[bool]

class LoadForecastTypeDef(TypedDict):
    Timestamps: List[datetime]
    Values: List[float]
    MetricSpecification: PredictiveScalingMetricSpecificationOutputTypeDef

class PredictiveScalingPolicyConfigurationOutputTypeDef(TypedDict):
    MetricSpecifications: List[PredictiveScalingMetricSpecificationOutputTypeDef]
    Mode: NotRequired[PredictiveScalingModeType]
    SchedulingBufferTime: NotRequired[int]
    MaxCapacityBreachBehavior: NotRequired[PredictiveScalingMaxCapacityBreachBehaviorType]
    MaxCapacityBuffer: NotRequired[int]

class PredictiveScalingPolicyConfigurationTypeDef(TypedDict):
    MetricSpecifications: Sequence[PredictiveScalingMetricSpecificationTypeDef]
    Mode: NotRequired[PredictiveScalingModeType]
    SchedulingBufferTime: NotRequired[int]
    MaxCapacityBreachBehavior: NotRequired[PredictiveScalingMaxCapacityBreachBehaviorType]
    MaxCapacityBuffer: NotRequired[int]

TargetTrackingScalingPolicyConfigurationUnionTypeDef = Union[
    TargetTrackingScalingPolicyConfigurationTypeDef,
    TargetTrackingScalingPolicyConfigurationOutputTypeDef,
]

class GetPredictiveScalingForecastResponseTypeDef(TypedDict):
    LoadForecast: List[LoadForecastTypeDef]
    CapacityForecast: CapacityForecastTypeDef
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ScalingPolicyTypeDef(TypedDict):
    PolicyARN: str
    PolicyName: str
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    PolicyType: PolicyTypeType
    CreationTime: datetime
    StepScalingPolicyConfiguration: NotRequired[StepScalingPolicyConfigurationOutputTypeDef]
    TargetTrackingScalingPolicyConfiguration: NotRequired[
        TargetTrackingScalingPolicyConfigurationOutputTypeDef
    ]
    PredictiveScalingPolicyConfiguration: NotRequired[
        PredictiveScalingPolicyConfigurationOutputTypeDef
    ]
    Alarms: NotRequired[List[AlarmTypeDef]]

PredictiveScalingPolicyConfigurationUnionTypeDef = Union[
    PredictiveScalingPolicyConfigurationTypeDef, PredictiveScalingPolicyConfigurationOutputTypeDef
]

class DescribeScalingPoliciesResponseTypeDef(TypedDict):
    ScalingPolicies: List[ScalingPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutScalingPolicyRequestTypeDef(TypedDict):
    PolicyName: str
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    PolicyType: NotRequired[PolicyTypeType]
    StepScalingPolicyConfiguration: NotRequired[StepScalingPolicyConfigurationUnionTypeDef]
    TargetTrackingScalingPolicyConfiguration: NotRequired[
        TargetTrackingScalingPolicyConfigurationUnionTypeDef
    ]
    PredictiveScalingPolicyConfiguration: NotRequired[
        PredictiveScalingPolicyConfigurationUnionTypeDef
    ]
