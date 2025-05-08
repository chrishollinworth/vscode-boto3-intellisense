"""
Type annotations for autoscaling service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_autoscaling.type_defs import AcceleratorCountRequestTypeDef

    data: AcceleratorCountRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AcceleratorManufacturerType,
    AcceleratorNameType,
    AcceleratorTypeType,
    BareMetalType,
    BurstablePerformanceType,
    CapacityDistributionStrategyType,
    CapacityReservationPreferenceType,
    CpuManufacturerType,
    ImpairedZoneHealthCheckBehaviorType,
    InstanceGenerationType,
    InstanceMetadataEndpointStateType,
    InstanceMetadataHttpTokensStateType,
    InstanceRefreshStatusType,
    LifecycleStateType,
    LocalStorageType,
    LocalStorageTypeType,
    MetricStatisticType,
    MetricTypeType,
    PredefinedLoadMetricTypeType,
    PredefinedMetricPairTypeType,
    PredefinedScalingMetricTypeType,
    PredictiveScalingMaxCapacityBreachBehaviorType,
    PredictiveScalingModeType,
    ScaleInProtectedInstancesType,
    ScalingActivityStatusCodeType,
    StandbyInstancesType,
    WarmPoolStateType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AcceleratorCountRequestTypeDef",
    "AcceleratorTotalMemoryMiBRequestTypeDef",
    "ActivitiesTypeTypeDef",
    "ActivityTypeDef",
    "ActivityTypeTypeDef",
    "AdjustmentTypeTypeDef",
    "AlarmSpecificationOutputTypeDef",
    "AlarmSpecificationTypeDef",
    "AlarmTypeDef",
    "AttachInstancesQueryTypeDef",
    "AttachLoadBalancerTargetGroupsTypeTypeDef",
    "AttachLoadBalancersTypeTypeDef",
    "AttachTrafficSourcesTypeTypeDef",
    "AutoScalingGroupNamesTypePaginateTypeDef",
    "AutoScalingGroupNamesTypeTypeDef",
    "AutoScalingGroupTypeDef",
    "AutoScalingGroupsTypeTypeDef",
    "AutoScalingInstanceDetailsTypeDef",
    "AutoScalingInstancesTypeTypeDef",
    "AvailabilityZoneDistributionTypeDef",
    "AvailabilityZoneImpairmentPolicyTypeDef",
    "BaselineEbsBandwidthMbpsRequestTypeDef",
    "BaselinePerformanceFactorsRequestOutputTypeDef",
    "BaselinePerformanceFactorsRequestTypeDef",
    "BatchDeleteScheduledActionAnswerTypeDef",
    "BatchDeleteScheduledActionTypeTypeDef",
    "BatchPutScheduledUpdateGroupActionAnswerTypeDef",
    "BatchPutScheduledUpdateGroupActionTypeTypeDef",
    "BlockDeviceMappingTypeDef",
    "CancelInstanceRefreshAnswerTypeDef",
    "CancelInstanceRefreshTypeTypeDef",
    "CapacityForecastTypeDef",
    "CapacityReservationSpecificationOutputTypeDef",
    "CapacityReservationSpecificationTypeDef",
    "CapacityReservationSpecificationUnionTypeDef",
    "CapacityReservationTargetOutputTypeDef",
    "CapacityReservationTargetTypeDef",
    "CompleteLifecycleActionTypeTypeDef",
    "CpuPerformanceFactorRequestOutputTypeDef",
    "CpuPerformanceFactorRequestTypeDef",
    "CreateAutoScalingGroupTypeTypeDef",
    "CreateLaunchConfigurationTypeTypeDef",
    "CreateOrUpdateTagsTypeTypeDef",
    "CustomizedMetricSpecificationOutputTypeDef",
    "CustomizedMetricSpecificationTypeDef",
    "DeleteAutoScalingGroupTypeTypeDef",
    "DeleteLifecycleHookTypeTypeDef",
    "DeleteNotificationConfigurationTypeTypeDef",
    "DeletePolicyTypeTypeDef",
    "DeleteScheduledActionTypeTypeDef",
    "DeleteTagsTypeTypeDef",
    "DeleteWarmPoolTypeTypeDef",
    "DescribeAccountLimitsAnswerTypeDef",
    "DescribeAdjustmentTypesAnswerTypeDef",
    "DescribeAutoScalingInstancesTypePaginateTypeDef",
    "DescribeAutoScalingInstancesTypeTypeDef",
    "DescribeAutoScalingNotificationTypesAnswerTypeDef",
    "DescribeInstanceRefreshesAnswerTypeDef",
    "DescribeInstanceRefreshesTypeTypeDef",
    "DescribeLifecycleHookTypesAnswerTypeDef",
    "DescribeLifecycleHooksAnswerTypeDef",
    "DescribeLifecycleHooksTypeTypeDef",
    "DescribeLoadBalancerTargetGroupsRequestPaginateTypeDef",
    "DescribeLoadBalancerTargetGroupsRequestTypeDef",
    "DescribeLoadBalancerTargetGroupsResponseTypeDef",
    "DescribeLoadBalancersRequestPaginateTypeDef",
    "DescribeLoadBalancersRequestTypeDef",
    "DescribeLoadBalancersResponseTypeDef",
    "DescribeMetricCollectionTypesAnswerTypeDef",
    "DescribeNotificationConfigurationsAnswerTypeDef",
    "DescribeNotificationConfigurationsTypePaginateTypeDef",
    "DescribeNotificationConfigurationsTypeTypeDef",
    "DescribePoliciesTypePaginateTypeDef",
    "DescribePoliciesTypeTypeDef",
    "DescribeScalingActivitiesTypePaginateTypeDef",
    "DescribeScalingActivitiesTypeTypeDef",
    "DescribeScheduledActionsTypePaginateTypeDef",
    "DescribeScheduledActionsTypeTypeDef",
    "DescribeTagsTypePaginateTypeDef",
    "DescribeTagsTypeTypeDef",
    "DescribeTerminationPolicyTypesAnswerTypeDef",
    "DescribeTrafficSourcesRequestTypeDef",
    "DescribeTrafficSourcesResponseTypeDef",
    "DescribeWarmPoolAnswerTypeDef",
    "DescribeWarmPoolTypePaginateTypeDef",
    "DescribeWarmPoolTypeTypeDef",
    "DesiredConfigurationOutputTypeDef",
    "DesiredConfigurationTypeDef",
    "DesiredConfigurationUnionTypeDef",
    "DetachInstancesAnswerTypeDef",
    "DetachInstancesQueryTypeDef",
    "DetachLoadBalancerTargetGroupsTypeTypeDef",
    "DetachLoadBalancersTypeTypeDef",
    "DetachTrafficSourcesTypeTypeDef",
    "DisableMetricsCollectionQueryTypeDef",
    "EbsTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableMetricsCollectionQueryTypeDef",
    "EnabledMetricTypeDef",
    "EnterStandbyAnswerTypeDef",
    "EnterStandbyQueryTypeDef",
    "ExecutePolicyTypeTypeDef",
    "ExitStandbyAnswerTypeDef",
    "ExitStandbyQueryTypeDef",
    "FailedScheduledUpdateGroupActionRequestTypeDef",
    "FilterTypeDef",
    "GetPredictiveScalingForecastAnswerTypeDef",
    "GetPredictiveScalingForecastTypeTypeDef",
    "InstanceMaintenancePolicyTypeDef",
    "InstanceMetadataOptionsTypeDef",
    "InstanceMonitoringTypeDef",
    "InstanceRefreshLivePoolProgressTypeDef",
    "InstanceRefreshProgressDetailsTypeDef",
    "InstanceRefreshTypeDef",
    "InstanceRefreshWarmPoolProgressTypeDef",
    "InstanceRequirementsOutputTypeDef",
    "InstanceRequirementsTypeDef",
    "InstanceReusePolicyTypeDef",
    "InstanceTypeDef",
    "InstancesDistributionTypeDef",
    "LaunchConfigurationNameTypeTypeDef",
    "LaunchConfigurationNamesTypePaginateTypeDef",
    "LaunchConfigurationNamesTypeTypeDef",
    "LaunchConfigurationTypeDef",
    "LaunchConfigurationsTypeTypeDef",
    "LaunchTemplateOutputTypeDef",
    "LaunchTemplateOverridesOutputTypeDef",
    "LaunchTemplateOverridesTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "LaunchTemplateTypeDef",
    "LifecycleHookSpecificationTypeDef",
    "LifecycleHookTypeDef",
    "LoadBalancerStateTypeDef",
    "LoadBalancerTargetGroupStateTypeDef",
    "LoadForecastTypeDef",
    "MemoryGiBPerVCpuRequestTypeDef",
    "MemoryMiBRequestTypeDef",
    "MetricCollectionTypeTypeDef",
    "MetricDataQueryOutputTypeDef",
    "MetricDataQueryTypeDef",
    "MetricDimensionTypeDef",
    "MetricGranularityTypeTypeDef",
    "MetricOutputTypeDef",
    "MetricStatOutputTypeDef",
    "MetricStatTypeDef",
    "MetricTypeDef",
    "MixedInstancesPolicyOutputTypeDef",
    "MixedInstancesPolicyTypeDef",
    "MixedInstancesPolicyUnionTypeDef",
    "NetworkBandwidthGbpsRequestTypeDef",
    "NetworkInterfaceCountRequestTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PerformanceFactorReferenceRequestTypeDef",
    "PoliciesTypeTypeDef",
    "PolicyARNTypeTypeDef",
    "PredefinedMetricSpecificationTypeDef",
    "PredictiveScalingConfigurationOutputTypeDef",
    "PredictiveScalingConfigurationTypeDef",
    "PredictiveScalingConfigurationUnionTypeDef",
    "PredictiveScalingCustomizedCapacityMetricOutputTypeDef",
    "PredictiveScalingCustomizedCapacityMetricTypeDef",
    "PredictiveScalingCustomizedLoadMetricOutputTypeDef",
    "PredictiveScalingCustomizedLoadMetricTypeDef",
    "PredictiveScalingCustomizedScalingMetricOutputTypeDef",
    "PredictiveScalingCustomizedScalingMetricTypeDef",
    "PredictiveScalingMetricSpecificationOutputTypeDef",
    "PredictiveScalingMetricSpecificationTypeDef",
    "PredictiveScalingPredefinedLoadMetricTypeDef",
    "PredictiveScalingPredefinedMetricPairTypeDef",
    "PredictiveScalingPredefinedScalingMetricTypeDef",
    "ProcessTypeTypeDef",
    "ProcessesTypeTypeDef",
    "PutLifecycleHookTypeTypeDef",
    "PutNotificationConfigurationTypeTypeDef",
    "PutScalingPolicyTypeTypeDef",
    "PutScheduledUpdateGroupActionTypeTypeDef",
    "PutWarmPoolTypeTypeDef",
    "RecordLifecycleActionHeartbeatTypeTypeDef",
    "RefreshPreferencesOutputTypeDef",
    "RefreshPreferencesTypeDef",
    "RefreshPreferencesUnionTypeDef",
    "ResponseMetadataTypeDef",
    "RollbackDetailsTypeDef",
    "RollbackInstanceRefreshAnswerTypeDef",
    "RollbackInstanceRefreshTypeTypeDef",
    "ScalingPolicyTypeDef",
    "ScalingProcessQueryRequestTypeDef",
    "ScalingProcessQueryTypeDef",
    "ScheduledActionsTypeTypeDef",
    "ScheduledUpdateGroupActionRequestTypeDef",
    "ScheduledUpdateGroupActionTypeDef",
    "SetDesiredCapacityTypeTypeDef",
    "SetInstanceHealthQueryTypeDef",
    "SetInstanceProtectionQueryTypeDef",
    "StartInstanceRefreshAnswerTypeDef",
    "StartInstanceRefreshTypeTypeDef",
    "StepAdjustmentTypeDef",
    "SuspendedProcessTypeDef",
    "TagDescriptionTypeDef",
    "TagTypeDef",
    "TagsTypeTypeDef",
    "TargetTrackingConfigurationOutputTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "TargetTrackingConfigurationUnionTypeDef",
    "TargetTrackingMetricDataQueryOutputTypeDef",
    "TargetTrackingMetricDataQueryTypeDef",
    "TargetTrackingMetricStatOutputTypeDef",
    "TargetTrackingMetricStatTypeDef",
    "TerminateInstanceInAutoScalingGroupTypeTypeDef",
    "TimestampTypeDef",
    "TotalLocalStorageGBRequestTypeDef",
    "TrafficSourceIdentifierTypeDef",
    "TrafficSourceStateTypeDef",
    "UpdateAutoScalingGroupTypeTypeDef",
    "VCpuCountRequestTypeDef",
    "WarmPoolConfigurationTypeDef",
)

class AcceleratorCountRequestTypeDef(TypedDict):
    Min: NotRequired[int]
    Max: NotRequired[int]

class AcceleratorTotalMemoryMiBRequestTypeDef(TypedDict):
    Min: NotRequired[int]
    Max: NotRequired[int]

class ActivityTypeDef(TypedDict):
    ActivityId: str
    AutoScalingGroupName: str
    Cause: str
    StartTime: datetime
    StatusCode: ScalingActivityStatusCodeType
    Description: NotRequired[str]
    EndTime: NotRequired[datetime]
    StatusMessage: NotRequired[str]
    Progress: NotRequired[int]
    Details: NotRequired[str]
    AutoScalingGroupState: NotRequired[str]
    AutoScalingGroupARN: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AdjustmentTypeTypeDef(TypedDict):
    AdjustmentType: NotRequired[str]

class AlarmSpecificationOutputTypeDef(TypedDict):
    Alarms: NotRequired[List[str]]

class AlarmSpecificationTypeDef(TypedDict):
    Alarms: NotRequired[Sequence[str]]

class AlarmTypeDef(TypedDict):
    AlarmName: NotRequired[str]
    AlarmARN: NotRequired[str]

class AttachInstancesQueryTypeDef(TypedDict):
    AutoScalingGroupName: str
    InstanceIds: NotRequired[Sequence[str]]

class AttachLoadBalancerTargetGroupsTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    TargetGroupARNs: Sequence[str]

class AttachLoadBalancersTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    LoadBalancerNames: Sequence[str]

TrafficSourceIdentifierTypeDef = TypedDict(
    "TrafficSourceIdentifierTypeDef",
    {
        "Identifier": str,
        "Type": NotRequired[str],
    },
)

class FilterTypeDef(TypedDict):
    Name: NotRequired[str]
    Values: NotRequired[Sequence[str]]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class AvailabilityZoneDistributionTypeDef(TypedDict):
    CapacityDistributionStrategy: NotRequired[CapacityDistributionStrategyType]

class AvailabilityZoneImpairmentPolicyTypeDef(TypedDict):
    ZonalShiftEnabled: NotRequired[bool]
    ImpairedZoneHealthCheckBehavior: NotRequired[ImpairedZoneHealthCheckBehaviorType]

class EnabledMetricTypeDef(TypedDict):
    Metric: NotRequired[str]
    Granularity: NotRequired[str]

class InstanceMaintenancePolicyTypeDef(TypedDict):
    MinHealthyPercentage: NotRequired[int]
    MaxHealthyPercentage: NotRequired[int]

class LaunchTemplateSpecificationTypeDef(TypedDict):
    LaunchTemplateId: NotRequired[str]
    LaunchTemplateName: NotRequired[str]
    Version: NotRequired[str]

class SuspendedProcessTypeDef(TypedDict):
    ProcessName: NotRequired[str]
    SuspensionReason: NotRequired[str]

class TagDescriptionTypeDef(TypedDict):
    ResourceId: NotRequired[str]
    ResourceType: NotRequired[str]
    Key: NotRequired[str]
    Value: NotRequired[str]
    PropagateAtLaunch: NotRequired[bool]

class BaselineEbsBandwidthMbpsRequestTypeDef(TypedDict):
    Min: NotRequired[int]
    Max: NotRequired[int]

class FailedScheduledUpdateGroupActionRequestTypeDef(TypedDict):
    ScheduledActionName: str
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

class BatchDeleteScheduledActionTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    ScheduledActionNames: Sequence[str]

class EbsTypeDef(TypedDict):
    SnapshotId: NotRequired[str]
    VolumeSize: NotRequired[int]
    VolumeType: NotRequired[str]
    DeleteOnTermination: NotRequired[bool]
    Iops: NotRequired[int]
    Encrypted: NotRequired[bool]
    Throughput: NotRequired[int]

class CancelInstanceRefreshTypeTypeDef(TypedDict):
    AutoScalingGroupName: str

class CapacityForecastTypeDef(TypedDict):
    Timestamps: List[datetime]
    Values: List[float]

class CapacityReservationTargetOutputTypeDef(TypedDict):
    CapacityReservationIds: NotRequired[List[str]]
    CapacityReservationResourceGroupArns: NotRequired[List[str]]

class CapacityReservationTargetTypeDef(TypedDict):
    CapacityReservationIds: NotRequired[Sequence[str]]
    CapacityReservationResourceGroupArns: NotRequired[Sequence[str]]

class CompleteLifecycleActionTypeTypeDef(TypedDict):
    LifecycleHookName: str
    AutoScalingGroupName: str
    LifecycleActionResult: str
    LifecycleActionToken: NotRequired[str]
    InstanceId: NotRequired[str]

class PerformanceFactorReferenceRequestTypeDef(TypedDict):
    InstanceFamily: NotRequired[str]

class LifecycleHookSpecificationTypeDef(TypedDict):
    LifecycleHookName: str
    LifecycleTransition: str
    NotificationMetadata: NotRequired[str]
    HeartbeatTimeout: NotRequired[int]
    DefaultResult: NotRequired[str]
    NotificationTargetARN: NotRequired[str]
    RoleARN: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    ResourceId: NotRequired[str]
    ResourceType: NotRequired[str]
    Value: NotRequired[str]
    PropagateAtLaunch: NotRequired[bool]

class InstanceMetadataOptionsTypeDef(TypedDict):
    HttpTokens: NotRequired[InstanceMetadataHttpTokensStateType]
    HttpPutResponseHopLimit: NotRequired[int]
    HttpEndpoint: NotRequired[InstanceMetadataEndpointStateType]

class InstanceMonitoringTypeDef(TypedDict):
    Enabled: NotRequired[bool]

class MetricDimensionTypeDef(TypedDict):
    Name: str
    Value: str

class DeleteAutoScalingGroupTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    ForceDelete: NotRequired[bool]

class DeleteLifecycleHookTypeTypeDef(TypedDict):
    LifecycleHookName: str
    AutoScalingGroupName: str

class DeleteNotificationConfigurationTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    TopicARN: str

class DeletePolicyTypeTypeDef(TypedDict):
    PolicyName: str
    AutoScalingGroupName: NotRequired[str]

class DeleteScheduledActionTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    ScheduledActionName: str

class DeleteWarmPoolTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    ForceDelete: NotRequired[bool]

class DescribeAutoScalingInstancesTypeTypeDef(TypedDict):
    InstanceIds: NotRequired[Sequence[str]]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeInstanceRefreshesTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    InstanceRefreshIds: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxRecords: NotRequired[int]

class LifecycleHookTypeDef(TypedDict):
    LifecycleHookName: NotRequired[str]
    AutoScalingGroupName: NotRequired[str]
    LifecycleTransition: NotRequired[str]
    NotificationTargetARN: NotRequired[str]
    RoleARN: NotRequired[str]
    NotificationMetadata: NotRequired[str]
    HeartbeatTimeout: NotRequired[int]
    GlobalTimeout: NotRequired[int]
    DefaultResult: NotRequired[str]

class DescribeLifecycleHooksTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    LifecycleHookNames: NotRequired[Sequence[str]]

class DescribeLoadBalancerTargetGroupsRequestTypeDef(TypedDict):
    AutoScalingGroupName: str
    NextToken: NotRequired[str]
    MaxRecords: NotRequired[int]

class LoadBalancerTargetGroupStateTypeDef(TypedDict):
    LoadBalancerTargetGroupARN: NotRequired[str]
    State: NotRequired[str]

class DescribeLoadBalancersRequestTypeDef(TypedDict):
    AutoScalingGroupName: str
    NextToken: NotRequired[str]
    MaxRecords: NotRequired[int]

class LoadBalancerStateTypeDef(TypedDict):
    LoadBalancerName: NotRequired[str]
    State: NotRequired[str]

class MetricCollectionTypeTypeDef(TypedDict):
    Metric: NotRequired[str]

class MetricGranularityTypeTypeDef(TypedDict):
    Granularity: NotRequired[str]

class NotificationConfigurationTypeDef(TypedDict):
    AutoScalingGroupName: NotRequired[str]
    TopicARN: NotRequired[str]
    NotificationType: NotRequired[str]

class DescribeNotificationConfigurationsTypeTypeDef(TypedDict):
    AutoScalingGroupNames: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxRecords: NotRequired[int]

class DescribePoliciesTypeTypeDef(TypedDict):
    AutoScalingGroupName: NotRequired[str]
    PolicyNames: NotRequired[Sequence[str]]
    PolicyTypes: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxRecords: NotRequired[int]

class DescribeScalingActivitiesTypeTypeDef(TypedDict):
    ActivityIds: NotRequired[Sequence[str]]
    AutoScalingGroupName: NotRequired[str]
    IncludeDeletedGroups: NotRequired[bool]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class DescribeTrafficSourcesRequestTypeDef(TypedDict):
    AutoScalingGroupName: str
    TrafficSourceType: NotRequired[str]
    NextToken: NotRequired[str]
    MaxRecords: NotRequired[int]

TrafficSourceStateTypeDef = TypedDict(
    "TrafficSourceStateTypeDef",
    {
        "TrafficSource": NotRequired[str],
        "State": NotRequired[str],
        "Identifier": NotRequired[str],
        "Type": NotRequired[str],
    },
)

class DescribeWarmPoolTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]

class DetachInstancesQueryTypeDef(TypedDict):
    AutoScalingGroupName: str
    ShouldDecrementDesiredCapacity: bool
    InstanceIds: NotRequired[Sequence[str]]

class DetachLoadBalancerTargetGroupsTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    TargetGroupARNs: Sequence[str]

class DetachLoadBalancersTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    LoadBalancerNames: Sequence[str]

class DisableMetricsCollectionQueryTypeDef(TypedDict):
    AutoScalingGroupName: str
    Metrics: NotRequired[Sequence[str]]

class EnableMetricsCollectionQueryTypeDef(TypedDict):
    AutoScalingGroupName: str
    Granularity: str
    Metrics: NotRequired[Sequence[str]]

class EnterStandbyQueryTypeDef(TypedDict):
    AutoScalingGroupName: str
    ShouldDecrementDesiredCapacity: bool
    InstanceIds: NotRequired[Sequence[str]]

class ExecutePolicyTypeTypeDef(TypedDict):
    PolicyName: str
    AutoScalingGroupName: NotRequired[str]
    HonorCooldown: NotRequired[bool]
    MetricValue: NotRequired[float]
    BreachThreshold: NotRequired[float]

class ExitStandbyQueryTypeDef(TypedDict):
    AutoScalingGroupName: str
    InstanceIds: NotRequired[Sequence[str]]

class InstanceRefreshLivePoolProgressTypeDef(TypedDict):
    PercentageComplete: NotRequired[int]
    InstancesToUpdate: NotRequired[int]

class InstanceRefreshWarmPoolProgressTypeDef(TypedDict):
    PercentageComplete: NotRequired[int]
    InstancesToUpdate: NotRequired[int]

class MemoryGiBPerVCpuRequestTypeDef(TypedDict):
    Min: NotRequired[float]
    Max: NotRequired[float]

class MemoryMiBRequestTypeDef(TypedDict):
    Min: int
    Max: NotRequired[int]

class NetworkBandwidthGbpsRequestTypeDef(TypedDict):
    Min: NotRequired[float]
    Max: NotRequired[float]

class NetworkInterfaceCountRequestTypeDef(TypedDict):
    Min: NotRequired[int]
    Max: NotRequired[int]

class TotalLocalStorageGBRequestTypeDef(TypedDict):
    Min: NotRequired[float]
    Max: NotRequired[float]

class VCpuCountRequestTypeDef(TypedDict):
    Min: int
    Max: NotRequired[int]

class InstanceReusePolicyTypeDef(TypedDict):
    ReuseOnScaleIn: NotRequired[bool]

class InstancesDistributionTypeDef(TypedDict):
    OnDemandAllocationStrategy: NotRequired[str]
    OnDemandBaseCapacity: NotRequired[int]
    OnDemandPercentageAboveBaseCapacity: NotRequired[int]
    SpotAllocationStrategy: NotRequired[str]
    SpotInstancePools: NotRequired[int]
    SpotMaxPrice: NotRequired[str]

class LaunchConfigurationNameTypeTypeDef(TypedDict):
    LaunchConfigurationName: str

class LaunchConfigurationNamesTypeTypeDef(TypedDict):
    LaunchConfigurationNames: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxRecords: NotRequired[int]

class PredefinedMetricSpecificationTypeDef(TypedDict):
    PredefinedMetricType: MetricTypeType
    ResourceLabel: NotRequired[str]

class PredictiveScalingPredefinedLoadMetricTypeDef(TypedDict):
    PredefinedMetricType: PredefinedLoadMetricTypeType
    ResourceLabel: NotRequired[str]

class PredictiveScalingPredefinedMetricPairTypeDef(TypedDict):
    PredefinedMetricType: PredefinedMetricPairTypeType
    ResourceLabel: NotRequired[str]

class PredictiveScalingPredefinedScalingMetricTypeDef(TypedDict):
    PredefinedMetricType: PredefinedScalingMetricTypeType
    ResourceLabel: NotRequired[str]

class ProcessTypeTypeDef(TypedDict):
    ProcessName: str

class PutLifecycleHookTypeTypeDef(TypedDict):
    LifecycleHookName: str
    AutoScalingGroupName: str
    LifecycleTransition: NotRequired[str]
    RoleARN: NotRequired[str]
    NotificationTargetARN: NotRequired[str]
    NotificationMetadata: NotRequired[str]
    HeartbeatTimeout: NotRequired[int]
    DefaultResult: NotRequired[str]

class PutNotificationConfigurationTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    TopicARN: str
    NotificationTypes: Sequence[str]

class StepAdjustmentTypeDef(TypedDict):
    ScalingAdjustment: int
    MetricIntervalLowerBound: NotRequired[float]
    MetricIntervalUpperBound: NotRequired[float]

class RecordLifecycleActionHeartbeatTypeTypeDef(TypedDict):
    LifecycleHookName: str
    AutoScalingGroupName: str
    LifecycleActionToken: NotRequired[str]
    InstanceId: NotRequired[str]

class RollbackInstanceRefreshTypeTypeDef(TypedDict):
    AutoScalingGroupName: str

class ScalingProcessQueryRequestTypeDef(TypedDict):
    AutoScalingGroupName: str
    ScalingProcesses: NotRequired[Sequence[str]]

class ScalingProcessQueryTypeDef(TypedDict):
    AutoScalingGroupName: str
    ScalingProcesses: NotRequired[Sequence[str]]

class ScheduledUpdateGroupActionTypeDef(TypedDict):
    AutoScalingGroupName: NotRequired[str]
    ScheduledActionName: NotRequired[str]
    ScheduledActionARN: NotRequired[str]
    Time: NotRequired[datetime]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    Recurrence: NotRequired[str]
    MinSize: NotRequired[int]
    MaxSize: NotRequired[int]
    DesiredCapacity: NotRequired[int]
    TimeZone: NotRequired[str]

class SetDesiredCapacityTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    DesiredCapacity: int
    HonorCooldown: NotRequired[bool]

class SetInstanceHealthQueryTypeDef(TypedDict):
    InstanceId: str
    HealthStatus: str
    ShouldRespectGracePeriod: NotRequired[bool]

class SetInstanceProtectionQueryTypeDef(TypedDict):
    InstanceIds: Sequence[str]
    AutoScalingGroupName: str
    ProtectedFromScaleIn: bool

class TerminateInstanceInAutoScalingGroupTypeTypeDef(TypedDict):
    InstanceId: str
    ShouldDecrementDesiredCapacity: bool

class ActivitiesTypeTypeDef(TypedDict):
    Activities: List[ActivityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ActivityTypeTypeDef(TypedDict):
    Activity: ActivityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CancelInstanceRefreshAnswerTypeDef(TypedDict):
    InstanceRefreshId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountLimitsAnswerTypeDef(TypedDict):
    MaxNumberOfAutoScalingGroups: int
    MaxNumberOfLaunchConfigurations: int
    NumberOfAutoScalingGroups: int
    NumberOfLaunchConfigurations: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAutoScalingNotificationTypesAnswerTypeDef(TypedDict):
    AutoScalingNotificationTypes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLifecycleHookTypesAnswerTypeDef(TypedDict):
    LifecycleHookTypes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTerminationPolicyTypesAnswerTypeDef(TypedDict):
    TerminationPolicyTypes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DetachInstancesAnswerTypeDef(TypedDict):
    Activities: List[ActivityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class EnterStandbyAnswerTypeDef(TypedDict):
    Activities: List[ActivityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ExitStandbyAnswerTypeDef(TypedDict):
    Activities: List[ActivityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RollbackInstanceRefreshAnswerTypeDef(TypedDict):
    InstanceRefreshId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartInstanceRefreshAnswerTypeDef(TypedDict):
    InstanceRefreshId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAdjustmentTypesAnswerTypeDef(TypedDict):
    AdjustmentTypes: List[AdjustmentTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RefreshPreferencesOutputTypeDef(TypedDict):
    MinHealthyPercentage: NotRequired[int]
    InstanceWarmup: NotRequired[int]
    CheckpointPercentages: NotRequired[List[int]]
    CheckpointDelay: NotRequired[int]
    SkipMatching: NotRequired[bool]
    AutoRollback: NotRequired[bool]
    ScaleInProtectedInstances: NotRequired[ScaleInProtectedInstancesType]
    StandbyInstances: NotRequired[StandbyInstancesType]
    AlarmSpecification: NotRequired[AlarmSpecificationOutputTypeDef]
    MaxHealthyPercentage: NotRequired[int]
    BakeTime: NotRequired[int]

class RefreshPreferencesTypeDef(TypedDict):
    MinHealthyPercentage: NotRequired[int]
    InstanceWarmup: NotRequired[int]
    CheckpointPercentages: NotRequired[Sequence[int]]
    CheckpointDelay: NotRequired[int]
    SkipMatching: NotRequired[bool]
    AutoRollback: NotRequired[bool]
    ScaleInProtectedInstances: NotRequired[ScaleInProtectedInstancesType]
    StandbyInstances: NotRequired[StandbyInstancesType]
    AlarmSpecification: NotRequired[AlarmSpecificationTypeDef]
    MaxHealthyPercentage: NotRequired[int]
    BakeTime: NotRequired[int]

class PolicyARNTypeTypeDef(TypedDict):
    PolicyARN: str
    Alarms: List[AlarmTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AttachTrafficSourcesTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    TrafficSources: Sequence[TrafficSourceIdentifierTypeDef]
    SkipZonalShiftValidation: NotRequired[bool]

class DetachTrafficSourcesTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    TrafficSources: Sequence[TrafficSourceIdentifierTypeDef]

class AutoScalingGroupNamesTypeTypeDef(TypedDict):
    AutoScalingGroupNames: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxRecords: NotRequired[int]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class DescribeTagsTypeTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    NextToken: NotRequired[str]
    MaxRecords: NotRequired[int]

class AutoScalingGroupNamesTypePaginateTypeDef(TypedDict):
    AutoScalingGroupNames: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeAutoScalingInstancesTypePaginateTypeDef(TypedDict):
    InstanceIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeLoadBalancerTargetGroupsRequestPaginateTypeDef(TypedDict):
    AutoScalingGroupName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeLoadBalancersRequestPaginateTypeDef(TypedDict):
    AutoScalingGroupName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeNotificationConfigurationsTypePaginateTypeDef(TypedDict):
    AutoScalingGroupNames: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribePoliciesTypePaginateTypeDef(TypedDict):
    AutoScalingGroupName: NotRequired[str]
    PolicyNames: NotRequired[Sequence[str]]
    PolicyTypes: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeScalingActivitiesTypePaginateTypeDef(TypedDict):
    ActivityIds: NotRequired[Sequence[str]]
    AutoScalingGroupName: NotRequired[str]
    IncludeDeletedGroups: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeTagsTypePaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeWarmPoolTypePaginateTypeDef(TypedDict):
    AutoScalingGroupName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class LaunchConfigurationNamesTypePaginateTypeDef(TypedDict):
    LaunchConfigurationNames: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class AutoScalingInstanceDetailsTypeDef(TypedDict):
    InstanceId: str
    AutoScalingGroupName: str
    AvailabilityZone: str
    LifecycleState: str
    HealthStatus: str
    ProtectedFromScaleIn: bool
    InstanceType: NotRequired[str]
    LaunchConfigurationName: NotRequired[str]
    LaunchTemplate: NotRequired[LaunchTemplateSpecificationTypeDef]
    WeightedCapacity: NotRequired[str]

class InstanceTypeDef(TypedDict):
    InstanceId: str
    AvailabilityZone: str
    LifecycleState: LifecycleStateType
    HealthStatus: str
    ProtectedFromScaleIn: bool
    InstanceType: NotRequired[str]
    LaunchConfigurationName: NotRequired[str]
    LaunchTemplate: NotRequired[LaunchTemplateSpecificationTypeDef]
    WeightedCapacity: NotRequired[str]

class TagsTypeTypeDef(TypedDict):
    Tags: List[TagDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BatchDeleteScheduledActionAnswerTypeDef(TypedDict):
    FailedScheduledActions: List[FailedScheduledUpdateGroupActionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutScheduledUpdateGroupActionAnswerTypeDef(TypedDict):
    FailedScheduledUpdateGroupActions: List[FailedScheduledUpdateGroupActionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BlockDeviceMappingTypeDef(TypedDict):
    DeviceName: str
    VirtualName: NotRequired[str]
    Ebs: NotRequired[EbsTypeDef]
    NoDevice: NotRequired[bool]

class CapacityReservationSpecificationOutputTypeDef(TypedDict):
    CapacityReservationPreference: NotRequired[CapacityReservationPreferenceType]
    CapacityReservationTarget: NotRequired[CapacityReservationTargetOutputTypeDef]

class CapacityReservationSpecificationTypeDef(TypedDict):
    CapacityReservationPreference: NotRequired[CapacityReservationPreferenceType]
    CapacityReservationTarget: NotRequired[CapacityReservationTargetTypeDef]

class CpuPerformanceFactorRequestOutputTypeDef(TypedDict):
    References: NotRequired[List[PerformanceFactorReferenceRequestTypeDef]]

class CpuPerformanceFactorRequestTypeDef(TypedDict):
    References: NotRequired[Sequence[PerformanceFactorReferenceRequestTypeDef]]

class CreateOrUpdateTagsTypeTypeDef(TypedDict):
    Tags: Sequence[TagTypeDef]

class DeleteTagsTypeTypeDef(TypedDict):
    Tags: Sequence[TagTypeDef]

class MetricOutputTypeDef(TypedDict):
    Namespace: str
    MetricName: str
    Dimensions: NotRequired[List[MetricDimensionTypeDef]]

class MetricTypeDef(TypedDict):
    Namespace: str
    MetricName: str
    Dimensions: NotRequired[Sequence[MetricDimensionTypeDef]]

class DescribeLifecycleHooksAnswerTypeDef(TypedDict):
    LifecycleHooks: List[LifecycleHookTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLoadBalancerTargetGroupsResponseTypeDef(TypedDict):
    LoadBalancerTargetGroups: List[LoadBalancerTargetGroupStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeLoadBalancersResponseTypeDef(TypedDict):
    LoadBalancers: List[LoadBalancerStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeMetricCollectionTypesAnswerTypeDef(TypedDict):
    Metrics: List[MetricCollectionTypeTypeDef]
    Granularities: List[MetricGranularityTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNotificationConfigurationsAnswerTypeDef(TypedDict):
    NotificationConfigurations: List[NotificationConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeScheduledActionsTypePaginateTypeDef(TypedDict):
    AutoScalingGroupName: NotRequired[str]
    ScheduledActionNames: NotRequired[Sequence[str]]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeScheduledActionsTypeTypeDef(TypedDict):
    AutoScalingGroupName: NotRequired[str]
    ScheduledActionNames: NotRequired[Sequence[str]]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    NextToken: NotRequired[str]
    MaxRecords: NotRequired[int]

class GetPredictiveScalingForecastTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    PolicyName: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef

class PutScheduledUpdateGroupActionTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    ScheduledActionName: str
    Time: NotRequired[TimestampTypeDef]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    Recurrence: NotRequired[str]
    MinSize: NotRequired[int]
    MaxSize: NotRequired[int]
    DesiredCapacity: NotRequired[int]
    TimeZone: NotRequired[str]

class ScheduledUpdateGroupActionRequestTypeDef(TypedDict):
    ScheduledActionName: str
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    Recurrence: NotRequired[str]
    MinSize: NotRequired[int]
    MaxSize: NotRequired[int]
    DesiredCapacity: NotRequired[int]
    TimeZone: NotRequired[str]

class DescribeTrafficSourcesResponseTypeDef(TypedDict):
    TrafficSources: List[TrafficSourceStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class InstanceRefreshProgressDetailsTypeDef(TypedDict):
    LivePoolProgress: NotRequired[InstanceRefreshLivePoolProgressTypeDef]
    WarmPoolProgress: NotRequired[InstanceRefreshWarmPoolProgressTypeDef]

class PutWarmPoolTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    MaxGroupPreparedCapacity: NotRequired[int]
    MinSize: NotRequired[int]
    PoolState: NotRequired[WarmPoolStateType]
    InstanceReusePolicy: NotRequired[InstanceReusePolicyTypeDef]

class WarmPoolConfigurationTypeDef(TypedDict):
    MaxGroupPreparedCapacity: NotRequired[int]
    MinSize: NotRequired[int]
    PoolState: NotRequired[WarmPoolStateType]
    Status: NotRequired[Literal["PendingDelete"]]
    InstanceReusePolicy: NotRequired[InstanceReusePolicyTypeDef]

class ProcessesTypeTypeDef(TypedDict):
    Processes: List[ProcessTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ScheduledActionsTypeTypeDef(TypedDict):
    ScheduledUpdateGroupActions: List[ScheduledUpdateGroupActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

RefreshPreferencesUnionTypeDef = Union[RefreshPreferencesTypeDef, RefreshPreferencesOutputTypeDef]

class AutoScalingInstancesTypeTypeDef(TypedDict):
    AutoScalingInstances: List[AutoScalingInstanceDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateLaunchConfigurationTypeTypeDef(TypedDict):
    LaunchConfigurationName: str
    ImageId: NotRequired[str]
    KeyName: NotRequired[str]
    SecurityGroups: NotRequired[Sequence[str]]
    ClassicLinkVPCId: NotRequired[str]
    ClassicLinkVPCSecurityGroups: NotRequired[Sequence[str]]
    UserData: NotRequired[str]
    InstanceId: NotRequired[str]
    InstanceType: NotRequired[str]
    KernelId: NotRequired[str]
    RamdiskId: NotRequired[str]
    BlockDeviceMappings: NotRequired[Sequence[BlockDeviceMappingTypeDef]]
    InstanceMonitoring: NotRequired[InstanceMonitoringTypeDef]
    SpotPrice: NotRequired[str]
    IamInstanceProfile: NotRequired[str]
    EbsOptimized: NotRequired[bool]
    AssociatePublicIpAddress: NotRequired[bool]
    PlacementTenancy: NotRequired[str]
    MetadataOptions: NotRequired[InstanceMetadataOptionsTypeDef]

class LaunchConfigurationTypeDef(TypedDict):
    LaunchConfigurationName: str
    ImageId: str
    InstanceType: str
    CreatedTime: datetime
    LaunchConfigurationARN: NotRequired[str]
    KeyName: NotRequired[str]
    SecurityGroups: NotRequired[List[str]]
    ClassicLinkVPCId: NotRequired[str]
    ClassicLinkVPCSecurityGroups: NotRequired[List[str]]
    UserData: NotRequired[str]
    KernelId: NotRequired[str]
    RamdiskId: NotRequired[str]
    BlockDeviceMappings: NotRequired[List[BlockDeviceMappingTypeDef]]
    InstanceMonitoring: NotRequired[InstanceMonitoringTypeDef]
    SpotPrice: NotRequired[str]
    IamInstanceProfile: NotRequired[str]
    EbsOptimized: NotRequired[bool]
    AssociatePublicIpAddress: NotRequired[bool]
    PlacementTenancy: NotRequired[str]
    MetadataOptions: NotRequired[InstanceMetadataOptionsTypeDef]

CapacityReservationSpecificationUnionTypeDef = Union[
    CapacityReservationSpecificationTypeDef, CapacityReservationSpecificationOutputTypeDef
]

class BaselinePerformanceFactorsRequestOutputTypeDef(TypedDict):
    Cpu: NotRequired[CpuPerformanceFactorRequestOutputTypeDef]

class BaselinePerformanceFactorsRequestTypeDef(TypedDict):
    Cpu: NotRequired[CpuPerformanceFactorRequestTypeDef]

class MetricStatOutputTypeDef(TypedDict):
    Metric: MetricOutputTypeDef
    Stat: str
    Unit: NotRequired[str]

class TargetTrackingMetricStatOutputTypeDef(TypedDict):
    Metric: MetricOutputTypeDef
    Stat: str
    Unit: NotRequired[str]
    Period: NotRequired[int]

class MetricStatTypeDef(TypedDict):
    Metric: MetricTypeDef
    Stat: str
    Unit: NotRequired[str]

class TargetTrackingMetricStatTypeDef(TypedDict):
    Metric: MetricTypeDef
    Stat: str
    Unit: NotRequired[str]
    Period: NotRequired[int]

class BatchPutScheduledUpdateGroupActionTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    ScheduledUpdateGroupActions: Sequence[ScheduledUpdateGroupActionRequestTypeDef]

class RollbackDetailsTypeDef(TypedDict):
    RollbackReason: NotRequired[str]
    RollbackStartTime: NotRequired[datetime]
    PercentageCompleteOnRollback: NotRequired[int]
    InstancesToUpdateOnRollback: NotRequired[int]
    ProgressDetailsOnRollback: NotRequired[InstanceRefreshProgressDetailsTypeDef]

class DescribeWarmPoolAnswerTypeDef(TypedDict):
    WarmPoolConfiguration: WarmPoolConfigurationTypeDef
    Instances: List[InstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class LaunchConfigurationsTypeTypeDef(TypedDict):
    LaunchConfigurations: List[LaunchConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class InstanceRequirementsOutputTypeDef(TypedDict):
    VCpuCount: VCpuCountRequestTypeDef
    MemoryMiB: MemoryMiBRequestTypeDef
    CpuManufacturers: NotRequired[List[CpuManufacturerType]]
    MemoryGiBPerVCpu: NotRequired[MemoryGiBPerVCpuRequestTypeDef]
    ExcludedInstanceTypes: NotRequired[List[str]]
    InstanceGenerations: NotRequired[List[InstanceGenerationType]]
    SpotMaxPricePercentageOverLowestPrice: NotRequired[int]
    MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: NotRequired[int]
    OnDemandMaxPricePercentageOverLowestPrice: NotRequired[int]
    BareMetal: NotRequired[BareMetalType]
    BurstablePerformance: NotRequired[BurstablePerformanceType]
    RequireHibernateSupport: NotRequired[bool]
    NetworkInterfaceCount: NotRequired[NetworkInterfaceCountRequestTypeDef]
    LocalStorage: NotRequired[LocalStorageType]
    LocalStorageTypes: NotRequired[List[LocalStorageTypeType]]
    TotalLocalStorageGB: NotRequired[TotalLocalStorageGBRequestTypeDef]
    BaselineEbsBandwidthMbps: NotRequired[BaselineEbsBandwidthMbpsRequestTypeDef]
    AcceleratorTypes: NotRequired[List[AcceleratorTypeType]]
    AcceleratorCount: NotRequired[AcceleratorCountRequestTypeDef]
    AcceleratorManufacturers: NotRequired[List[AcceleratorManufacturerType]]
    AcceleratorNames: NotRequired[List[AcceleratorNameType]]
    AcceleratorTotalMemoryMiB: NotRequired[AcceleratorTotalMemoryMiBRequestTypeDef]
    NetworkBandwidthGbps: NotRequired[NetworkBandwidthGbpsRequestTypeDef]
    AllowedInstanceTypes: NotRequired[List[str]]
    BaselinePerformanceFactors: NotRequired[BaselinePerformanceFactorsRequestOutputTypeDef]

class InstanceRequirementsTypeDef(TypedDict):
    VCpuCount: VCpuCountRequestTypeDef
    MemoryMiB: MemoryMiBRequestTypeDef
    CpuManufacturers: NotRequired[Sequence[CpuManufacturerType]]
    MemoryGiBPerVCpu: NotRequired[MemoryGiBPerVCpuRequestTypeDef]
    ExcludedInstanceTypes: NotRequired[Sequence[str]]
    InstanceGenerations: NotRequired[Sequence[InstanceGenerationType]]
    SpotMaxPricePercentageOverLowestPrice: NotRequired[int]
    MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: NotRequired[int]
    OnDemandMaxPricePercentageOverLowestPrice: NotRequired[int]
    BareMetal: NotRequired[BareMetalType]
    BurstablePerformance: NotRequired[BurstablePerformanceType]
    RequireHibernateSupport: NotRequired[bool]
    NetworkInterfaceCount: NotRequired[NetworkInterfaceCountRequestTypeDef]
    LocalStorage: NotRequired[LocalStorageType]
    LocalStorageTypes: NotRequired[Sequence[LocalStorageTypeType]]
    TotalLocalStorageGB: NotRequired[TotalLocalStorageGBRequestTypeDef]
    BaselineEbsBandwidthMbps: NotRequired[BaselineEbsBandwidthMbpsRequestTypeDef]
    AcceleratorTypes: NotRequired[Sequence[AcceleratorTypeType]]
    AcceleratorCount: NotRequired[AcceleratorCountRequestTypeDef]
    AcceleratorManufacturers: NotRequired[Sequence[AcceleratorManufacturerType]]
    AcceleratorNames: NotRequired[Sequence[AcceleratorNameType]]
    AcceleratorTotalMemoryMiB: NotRequired[AcceleratorTotalMemoryMiBRequestTypeDef]
    NetworkBandwidthGbps: NotRequired[NetworkBandwidthGbpsRequestTypeDef]
    AllowedInstanceTypes: NotRequired[Sequence[str]]
    BaselinePerformanceFactors: NotRequired[BaselinePerformanceFactorsRequestTypeDef]

class MetricDataQueryOutputTypeDef(TypedDict):
    Id: str
    Expression: NotRequired[str]
    MetricStat: NotRequired[MetricStatOutputTypeDef]
    Label: NotRequired[str]
    ReturnData: NotRequired[bool]

class TargetTrackingMetricDataQueryOutputTypeDef(TypedDict):
    Id: str
    Expression: NotRequired[str]
    MetricStat: NotRequired[TargetTrackingMetricStatOutputTypeDef]
    Label: NotRequired[str]
    Period: NotRequired[int]
    ReturnData: NotRequired[bool]

class MetricDataQueryTypeDef(TypedDict):
    Id: str
    Expression: NotRequired[str]
    MetricStat: NotRequired[MetricStatTypeDef]
    Label: NotRequired[str]
    ReturnData: NotRequired[bool]

class TargetTrackingMetricDataQueryTypeDef(TypedDict):
    Id: str
    Expression: NotRequired[str]
    MetricStat: NotRequired[TargetTrackingMetricStatTypeDef]
    Label: NotRequired[str]
    Period: NotRequired[int]
    ReturnData: NotRequired[bool]

class LaunchTemplateOverridesOutputTypeDef(TypedDict):
    InstanceType: NotRequired[str]
    WeightedCapacity: NotRequired[str]
    LaunchTemplateSpecification: NotRequired[LaunchTemplateSpecificationTypeDef]
    InstanceRequirements: NotRequired[InstanceRequirementsOutputTypeDef]

class LaunchTemplateOverridesTypeDef(TypedDict):
    InstanceType: NotRequired[str]
    WeightedCapacity: NotRequired[str]
    LaunchTemplateSpecification: NotRequired[LaunchTemplateSpecificationTypeDef]
    InstanceRequirements: NotRequired[InstanceRequirementsTypeDef]

class PredictiveScalingCustomizedCapacityMetricOutputTypeDef(TypedDict):
    MetricDataQueries: List[MetricDataQueryOutputTypeDef]

class PredictiveScalingCustomizedLoadMetricOutputTypeDef(TypedDict):
    MetricDataQueries: List[MetricDataQueryOutputTypeDef]

class PredictiveScalingCustomizedScalingMetricOutputTypeDef(TypedDict):
    MetricDataQueries: List[MetricDataQueryOutputTypeDef]

class CustomizedMetricSpecificationOutputTypeDef(TypedDict):
    MetricName: NotRequired[str]
    Namespace: NotRequired[str]
    Dimensions: NotRequired[List[MetricDimensionTypeDef]]
    Statistic: NotRequired[MetricStatisticType]
    Unit: NotRequired[str]
    Period: NotRequired[int]
    Metrics: NotRequired[List[TargetTrackingMetricDataQueryOutputTypeDef]]

class PredictiveScalingCustomizedCapacityMetricTypeDef(TypedDict):
    MetricDataQueries: Sequence[MetricDataQueryTypeDef]

class PredictiveScalingCustomizedLoadMetricTypeDef(TypedDict):
    MetricDataQueries: Sequence[MetricDataQueryTypeDef]

class PredictiveScalingCustomizedScalingMetricTypeDef(TypedDict):
    MetricDataQueries: Sequence[MetricDataQueryTypeDef]

class CustomizedMetricSpecificationTypeDef(TypedDict):
    MetricName: NotRequired[str]
    Namespace: NotRequired[str]
    Dimensions: NotRequired[Sequence[MetricDimensionTypeDef]]
    Statistic: NotRequired[MetricStatisticType]
    Unit: NotRequired[str]
    Period: NotRequired[int]
    Metrics: NotRequired[Sequence[TargetTrackingMetricDataQueryTypeDef]]

class LaunchTemplateOutputTypeDef(TypedDict):
    LaunchTemplateSpecification: NotRequired[LaunchTemplateSpecificationTypeDef]
    Overrides: NotRequired[List[LaunchTemplateOverridesOutputTypeDef]]

class LaunchTemplateTypeDef(TypedDict):
    LaunchTemplateSpecification: NotRequired[LaunchTemplateSpecificationTypeDef]
    Overrides: NotRequired[Sequence[LaunchTemplateOverridesTypeDef]]

class PredictiveScalingMetricSpecificationOutputTypeDef(TypedDict):
    TargetValue: float
    PredefinedMetricPairSpecification: NotRequired[PredictiveScalingPredefinedMetricPairTypeDef]
    PredefinedScalingMetricSpecification: NotRequired[
        PredictiveScalingPredefinedScalingMetricTypeDef
    ]
    PredefinedLoadMetricSpecification: NotRequired[PredictiveScalingPredefinedLoadMetricTypeDef]
    CustomizedScalingMetricSpecification: NotRequired[
        PredictiveScalingCustomizedScalingMetricOutputTypeDef
    ]
    CustomizedLoadMetricSpecification: NotRequired[
        PredictiveScalingCustomizedLoadMetricOutputTypeDef
    ]
    CustomizedCapacityMetricSpecification: NotRequired[
        PredictiveScalingCustomizedCapacityMetricOutputTypeDef
    ]

class TargetTrackingConfigurationOutputTypeDef(TypedDict):
    TargetValue: float
    PredefinedMetricSpecification: NotRequired[PredefinedMetricSpecificationTypeDef]
    CustomizedMetricSpecification: NotRequired[CustomizedMetricSpecificationOutputTypeDef]
    DisableScaleIn: NotRequired[bool]

class PredictiveScalingMetricSpecificationTypeDef(TypedDict):
    TargetValue: float
    PredefinedMetricPairSpecification: NotRequired[PredictiveScalingPredefinedMetricPairTypeDef]
    PredefinedScalingMetricSpecification: NotRequired[
        PredictiveScalingPredefinedScalingMetricTypeDef
    ]
    PredefinedLoadMetricSpecification: NotRequired[PredictiveScalingPredefinedLoadMetricTypeDef]
    CustomizedScalingMetricSpecification: NotRequired[
        PredictiveScalingCustomizedScalingMetricTypeDef
    ]
    CustomizedLoadMetricSpecification: NotRequired[PredictiveScalingCustomizedLoadMetricTypeDef]
    CustomizedCapacityMetricSpecification: NotRequired[
        PredictiveScalingCustomizedCapacityMetricTypeDef
    ]

class TargetTrackingConfigurationTypeDef(TypedDict):
    TargetValue: float
    PredefinedMetricSpecification: NotRequired[PredefinedMetricSpecificationTypeDef]
    CustomizedMetricSpecification: NotRequired[CustomizedMetricSpecificationTypeDef]
    DisableScaleIn: NotRequired[bool]

class MixedInstancesPolicyOutputTypeDef(TypedDict):
    LaunchTemplate: NotRequired[LaunchTemplateOutputTypeDef]
    InstancesDistribution: NotRequired[InstancesDistributionTypeDef]

class MixedInstancesPolicyTypeDef(TypedDict):
    LaunchTemplate: NotRequired[LaunchTemplateTypeDef]
    InstancesDistribution: NotRequired[InstancesDistributionTypeDef]

class LoadForecastTypeDef(TypedDict):
    Timestamps: List[datetime]
    Values: List[float]
    MetricSpecification: PredictiveScalingMetricSpecificationOutputTypeDef

class PredictiveScalingConfigurationOutputTypeDef(TypedDict):
    MetricSpecifications: List[PredictiveScalingMetricSpecificationOutputTypeDef]
    Mode: NotRequired[PredictiveScalingModeType]
    SchedulingBufferTime: NotRequired[int]
    MaxCapacityBreachBehavior: NotRequired[PredictiveScalingMaxCapacityBreachBehaviorType]
    MaxCapacityBuffer: NotRequired[int]

class PredictiveScalingConfigurationTypeDef(TypedDict):
    MetricSpecifications: Sequence[PredictiveScalingMetricSpecificationTypeDef]
    Mode: NotRequired[PredictiveScalingModeType]
    SchedulingBufferTime: NotRequired[int]
    MaxCapacityBreachBehavior: NotRequired[PredictiveScalingMaxCapacityBreachBehaviorType]
    MaxCapacityBuffer: NotRequired[int]

TargetTrackingConfigurationUnionTypeDef = Union[
    TargetTrackingConfigurationTypeDef, TargetTrackingConfigurationOutputTypeDef
]

class AutoScalingGroupTypeDef(TypedDict):
    AutoScalingGroupName: str
    MinSize: int
    MaxSize: int
    DesiredCapacity: int
    DefaultCooldown: int
    AvailabilityZones: List[str]
    HealthCheckType: str
    CreatedTime: datetime
    AutoScalingGroupARN: NotRequired[str]
    LaunchConfigurationName: NotRequired[str]
    LaunchTemplate: NotRequired[LaunchTemplateSpecificationTypeDef]
    MixedInstancesPolicy: NotRequired[MixedInstancesPolicyOutputTypeDef]
    PredictedCapacity: NotRequired[int]
    LoadBalancerNames: NotRequired[List[str]]
    TargetGroupARNs: NotRequired[List[str]]
    HealthCheckGracePeriod: NotRequired[int]
    Instances: NotRequired[List[InstanceTypeDef]]
    SuspendedProcesses: NotRequired[List[SuspendedProcessTypeDef]]
    PlacementGroup: NotRequired[str]
    VPCZoneIdentifier: NotRequired[str]
    EnabledMetrics: NotRequired[List[EnabledMetricTypeDef]]
    Status: NotRequired[str]
    Tags: NotRequired[List[TagDescriptionTypeDef]]
    TerminationPolicies: NotRequired[List[str]]
    NewInstancesProtectedFromScaleIn: NotRequired[bool]
    ServiceLinkedRoleARN: NotRequired[str]
    MaxInstanceLifetime: NotRequired[int]
    CapacityRebalance: NotRequired[bool]
    WarmPoolConfiguration: NotRequired[WarmPoolConfigurationTypeDef]
    WarmPoolSize: NotRequired[int]
    Context: NotRequired[str]
    DesiredCapacityType: NotRequired[str]
    DefaultInstanceWarmup: NotRequired[int]
    TrafficSources: NotRequired[List[TrafficSourceIdentifierTypeDef]]
    InstanceMaintenancePolicy: NotRequired[InstanceMaintenancePolicyTypeDef]
    AvailabilityZoneDistribution: NotRequired[AvailabilityZoneDistributionTypeDef]
    AvailabilityZoneImpairmentPolicy: NotRequired[AvailabilityZoneImpairmentPolicyTypeDef]
    CapacityReservationSpecification: NotRequired[CapacityReservationSpecificationOutputTypeDef]

class DesiredConfigurationOutputTypeDef(TypedDict):
    LaunchTemplate: NotRequired[LaunchTemplateSpecificationTypeDef]
    MixedInstancesPolicy: NotRequired[MixedInstancesPolicyOutputTypeDef]

class DesiredConfigurationTypeDef(TypedDict):
    LaunchTemplate: NotRequired[LaunchTemplateSpecificationTypeDef]
    MixedInstancesPolicy: NotRequired[MixedInstancesPolicyTypeDef]

MixedInstancesPolicyUnionTypeDef = Union[
    MixedInstancesPolicyTypeDef, MixedInstancesPolicyOutputTypeDef
]

class GetPredictiveScalingForecastAnswerTypeDef(TypedDict):
    LoadForecast: List[LoadForecastTypeDef]
    CapacityForecast: CapacityForecastTypeDef
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ScalingPolicyTypeDef(TypedDict):
    AutoScalingGroupName: NotRequired[str]
    PolicyName: NotRequired[str]
    PolicyARN: NotRequired[str]
    PolicyType: NotRequired[str]
    AdjustmentType: NotRequired[str]
    MinAdjustmentStep: NotRequired[int]
    MinAdjustmentMagnitude: NotRequired[int]
    ScalingAdjustment: NotRequired[int]
    Cooldown: NotRequired[int]
    StepAdjustments: NotRequired[List[StepAdjustmentTypeDef]]
    MetricAggregationType: NotRequired[str]
    EstimatedInstanceWarmup: NotRequired[int]
    Alarms: NotRequired[List[AlarmTypeDef]]
    TargetTrackingConfiguration: NotRequired[TargetTrackingConfigurationOutputTypeDef]
    Enabled: NotRequired[bool]
    PredictiveScalingConfiguration: NotRequired[PredictiveScalingConfigurationOutputTypeDef]

PredictiveScalingConfigurationUnionTypeDef = Union[
    PredictiveScalingConfigurationTypeDef, PredictiveScalingConfigurationOutputTypeDef
]

class AutoScalingGroupsTypeTypeDef(TypedDict):
    AutoScalingGroups: List[AutoScalingGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class InstanceRefreshTypeDef(TypedDict):
    InstanceRefreshId: NotRequired[str]
    AutoScalingGroupName: NotRequired[str]
    Status: NotRequired[InstanceRefreshStatusType]
    StatusReason: NotRequired[str]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    PercentageComplete: NotRequired[int]
    InstancesToUpdate: NotRequired[int]
    ProgressDetails: NotRequired[InstanceRefreshProgressDetailsTypeDef]
    Preferences: NotRequired[RefreshPreferencesOutputTypeDef]
    DesiredConfiguration: NotRequired[DesiredConfigurationOutputTypeDef]
    RollbackDetails: NotRequired[RollbackDetailsTypeDef]

DesiredConfigurationUnionTypeDef = Union[
    DesiredConfigurationTypeDef, DesiredConfigurationOutputTypeDef
]

class CreateAutoScalingGroupTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    MinSize: int
    MaxSize: int
    LaunchConfigurationName: NotRequired[str]
    LaunchTemplate: NotRequired[LaunchTemplateSpecificationTypeDef]
    MixedInstancesPolicy: NotRequired[MixedInstancesPolicyUnionTypeDef]
    InstanceId: NotRequired[str]
    DesiredCapacity: NotRequired[int]
    DefaultCooldown: NotRequired[int]
    AvailabilityZones: NotRequired[Sequence[str]]
    LoadBalancerNames: NotRequired[Sequence[str]]
    TargetGroupARNs: NotRequired[Sequence[str]]
    HealthCheckType: NotRequired[str]
    HealthCheckGracePeriod: NotRequired[int]
    PlacementGroup: NotRequired[str]
    VPCZoneIdentifier: NotRequired[str]
    TerminationPolicies: NotRequired[Sequence[str]]
    NewInstancesProtectedFromScaleIn: NotRequired[bool]
    CapacityRebalance: NotRequired[bool]
    LifecycleHookSpecificationList: NotRequired[Sequence[LifecycleHookSpecificationTypeDef]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ServiceLinkedRoleARN: NotRequired[str]
    MaxInstanceLifetime: NotRequired[int]
    Context: NotRequired[str]
    DesiredCapacityType: NotRequired[str]
    DefaultInstanceWarmup: NotRequired[int]
    TrafficSources: NotRequired[Sequence[TrafficSourceIdentifierTypeDef]]
    InstanceMaintenancePolicy: NotRequired[InstanceMaintenancePolicyTypeDef]
    AvailabilityZoneDistribution: NotRequired[AvailabilityZoneDistributionTypeDef]
    AvailabilityZoneImpairmentPolicy: NotRequired[AvailabilityZoneImpairmentPolicyTypeDef]
    SkipZonalShiftValidation: NotRequired[bool]
    CapacityReservationSpecification: NotRequired[CapacityReservationSpecificationUnionTypeDef]

class UpdateAutoScalingGroupTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    LaunchConfigurationName: NotRequired[str]
    LaunchTemplate: NotRequired[LaunchTemplateSpecificationTypeDef]
    MixedInstancesPolicy: NotRequired[MixedInstancesPolicyUnionTypeDef]
    MinSize: NotRequired[int]
    MaxSize: NotRequired[int]
    DesiredCapacity: NotRequired[int]
    DefaultCooldown: NotRequired[int]
    AvailabilityZones: NotRequired[Sequence[str]]
    HealthCheckType: NotRequired[str]
    HealthCheckGracePeriod: NotRequired[int]
    PlacementGroup: NotRequired[str]
    VPCZoneIdentifier: NotRequired[str]
    TerminationPolicies: NotRequired[Sequence[str]]
    NewInstancesProtectedFromScaleIn: NotRequired[bool]
    ServiceLinkedRoleARN: NotRequired[str]
    MaxInstanceLifetime: NotRequired[int]
    CapacityRebalance: NotRequired[bool]
    Context: NotRequired[str]
    DesiredCapacityType: NotRequired[str]
    DefaultInstanceWarmup: NotRequired[int]
    InstanceMaintenancePolicy: NotRequired[InstanceMaintenancePolicyTypeDef]
    AvailabilityZoneDistribution: NotRequired[AvailabilityZoneDistributionTypeDef]
    AvailabilityZoneImpairmentPolicy: NotRequired[AvailabilityZoneImpairmentPolicyTypeDef]
    SkipZonalShiftValidation: NotRequired[bool]
    CapacityReservationSpecification: NotRequired[CapacityReservationSpecificationUnionTypeDef]

class PoliciesTypeTypeDef(TypedDict):
    ScalingPolicies: List[ScalingPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutScalingPolicyTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    PolicyName: str
    PolicyType: NotRequired[str]
    AdjustmentType: NotRequired[str]
    MinAdjustmentStep: NotRequired[int]
    MinAdjustmentMagnitude: NotRequired[int]
    ScalingAdjustment: NotRequired[int]
    Cooldown: NotRequired[int]
    MetricAggregationType: NotRequired[str]
    StepAdjustments: NotRequired[Sequence[StepAdjustmentTypeDef]]
    EstimatedInstanceWarmup: NotRequired[int]
    TargetTrackingConfiguration: NotRequired[TargetTrackingConfigurationUnionTypeDef]
    Enabled: NotRequired[bool]
    PredictiveScalingConfiguration: NotRequired[PredictiveScalingConfigurationUnionTypeDef]

class DescribeInstanceRefreshesAnswerTypeDef(TypedDict):
    InstanceRefreshes: List[InstanceRefreshTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class StartInstanceRefreshTypeTypeDef(TypedDict):
    AutoScalingGroupName: str
    Strategy: NotRequired[Literal["Rolling"]]
    DesiredConfiguration: NotRequired[DesiredConfigurationUnionTypeDef]
    Preferences: NotRequired[RefreshPreferencesUnionTypeDef]
