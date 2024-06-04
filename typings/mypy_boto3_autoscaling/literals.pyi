"""
Type annotations for autoscaling service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/literals.html)

Usage::

    ```python
    from mypy_boto3_autoscaling.literals import AcceleratorManufacturerType

    data: AcceleratorManufacturerType = "amazon-web-services"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AcceleratorManufacturerType",
    "AcceleratorNameType",
    "AcceleratorTypeType",
    "BareMetalType",
    "BurstablePerformanceType",
    "CpuManufacturerType",
    "DescribeAutoScalingGroupsPaginatorName",
    "DescribeAutoScalingInstancesPaginatorName",
    "DescribeLaunchConfigurationsPaginatorName",
    "DescribeLoadBalancerTargetGroupsPaginatorName",
    "DescribeLoadBalancersPaginatorName",
    "DescribeNotificationConfigurationsPaginatorName",
    "DescribePoliciesPaginatorName",
    "DescribeScalingActivitiesPaginatorName",
    "DescribeScheduledActionsPaginatorName",
    "DescribeTagsPaginatorName",
    "DescribeWarmPoolPaginatorName",
    "InstanceGenerationType",
    "InstanceMetadataEndpointStateType",
    "InstanceMetadataHttpTokensStateType",
    "InstanceRefreshStatusType",
    "LifecycleStateType",
    "LocalStorageType",
    "LocalStorageTypeType",
    "MetricStatisticType",
    "MetricTypeType",
    "PredefinedLoadMetricTypeType",
    "PredefinedMetricPairTypeType",
    "PredefinedScalingMetricTypeType",
    "PredictiveScalingMaxCapacityBreachBehaviorType",
    "PredictiveScalingModeType",
    "RefreshStrategyType",
    "ScaleInProtectedInstancesType",
    "ScalingActivityStatusCodeType",
    "StandbyInstancesType",
    "WarmPoolStateType",
    "WarmPoolStatusType",
)

AcceleratorManufacturerType = Literal["amazon-web-services", "amd", "nvidia", "xilinx"]
AcceleratorNameType = Literal["a100", "k80", "m60", "radeon-pro-v520", "t4", "v100", "vu9p"]
AcceleratorTypeType = Literal["fpga", "gpu", "inference"]
BareMetalType = Literal["excluded", "included", "required"]
BurstablePerformanceType = Literal["excluded", "included", "required"]
CpuManufacturerType = Literal["amazon-web-services", "amd", "intel"]
DescribeAutoScalingGroupsPaginatorName = Literal["describe_auto_scaling_groups"]
DescribeAutoScalingInstancesPaginatorName = Literal["describe_auto_scaling_instances"]
DescribeLaunchConfigurationsPaginatorName = Literal["describe_launch_configurations"]
DescribeLoadBalancerTargetGroupsPaginatorName = Literal["describe_load_balancer_target_groups"]
DescribeLoadBalancersPaginatorName = Literal["describe_load_balancers"]
DescribeNotificationConfigurationsPaginatorName = Literal["describe_notification_configurations"]
DescribePoliciesPaginatorName = Literal["describe_policies"]
DescribeScalingActivitiesPaginatorName = Literal["describe_scaling_activities"]
DescribeScheduledActionsPaginatorName = Literal["describe_scheduled_actions"]
DescribeTagsPaginatorName = Literal["describe_tags"]
DescribeWarmPoolPaginatorName = Literal["describe_warm_pool"]
InstanceGenerationType = Literal["current", "previous"]
InstanceMetadataEndpointStateType = Literal["disabled", "enabled"]
InstanceMetadataHttpTokensStateType = Literal["optional", "required"]
InstanceRefreshStatusType = Literal[
    "Cancelled",
    "Cancelling",
    "Failed",
    "InProgress",
    "Pending",
    "RollbackFailed",
    "RollbackInProgress",
    "RollbackSuccessful",
    "Successful",
]
LifecycleStateType = Literal[
    "Detached",
    "Detaching",
    "EnteringStandby",
    "InService",
    "Pending",
    "Pending:Proceed",
    "Pending:Wait",
    "Quarantined",
    "Standby",
    "Terminated",
    "Terminating",
    "Terminating:Proceed",
    "Terminating:Wait",
    "Warmed:Hibernated",
    "Warmed:Pending",
    "Warmed:Pending:Proceed",
    "Warmed:Pending:Wait",
    "Warmed:Running",
    "Warmed:Stopped",
    "Warmed:Terminated",
    "Warmed:Terminating",
    "Warmed:Terminating:Proceed",
    "Warmed:Terminating:Wait",
]
LocalStorageType = Literal["excluded", "included", "required"]
LocalStorageTypeType = Literal["hdd", "ssd"]
MetricStatisticType = Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
MetricTypeType = Literal[
    "ALBRequestCountPerTarget",
    "ASGAverageCPUUtilization",
    "ASGAverageNetworkIn",
    "ASGAverageNetworkOut",
]
PredefinedLoadMetricTypeType = Literal[
    "ALBTargetGroupRequestCount",
    "ASGTotalCPUUtilization",
    "ASGTotalNetworkIn",
    "ASGTotalNetworkOut",
]
PredefinedMetricPairTypeType = Literal[
    "ALBRequestCount", "ASGCPUUtilization", "ASGNetworkIn", "ASGNetworkOut"
]
PredefinedScalingMetricTypeType = Literal[
    "ALBRequestCountPerTarget",
    "ASGAverageCPUUtilization",
    "ASGAverageNetworkIn",
    "ASGAverageNetworkOut",
]
PredictiveScalingMaxCapacityBreachBehaviorType = Literal["HonorMaxCapacity", "IncreaseMaxCapacity"]
PredictiveScalingModeType = Literal["ForecastAndScale", "ForecastOnly"]
RefreshStrategyType = Literal["Rolling"]
ScaleInProtectedInstancesType = Literal["Ignore", "Refresh", "Wait"]
ScalingActivityStatusCodeType = Literal[
    "Cancelled",
    "Failed",
    "InProgress",
    "MidLifecycleAction",
    "PendingSpotBidPlacement",
    "PreInService",
    "Successful",
    "WaitingForConnectionDraining",
    "WaitingForELBConnectionDraining",
    "WaitingForInstanceId",
    "WaitingForInstanceWarmup",
    "WaitingForSpotInstanceId",
    "WaitingForSpotInstanceRequestId",
]
StandbyInstancesType = Literal["Ignore", "Terminate", "Wait"]
WarmPoolStateType = Literal["Hibernated", "Running", "Stopped"]
WarmPoolStatusType = Literal["PendingDelete"]
