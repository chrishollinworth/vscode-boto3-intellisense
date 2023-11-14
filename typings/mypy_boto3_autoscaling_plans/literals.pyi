"""
Type annotations for autoscaling-plans service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/literals.html)

Usage::

    ```python
    from mypy_boto3_autoscaling_plans.literals import DescribeScalingPlanResourcesPaginatorName

    data: DescribeScalingPlanResourcesPaginatorName = "describe_scaling_plan_resources"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DescribeScalingPlanResourcesPaginatorName",
    "DescribeScalingPlansPaginatorName",
    "ForecastDataTypeType",
    "LoadMetricTypeType",
    "MetricStatisticType",
    "PolicyTypeType",
    "PredictiveScalingMaxCapacityBehaviorType",
    "PredictiveScalingModeType",
    "ScalableDimensionType",
    "ScalingMetricTypeType",
    "ScalingPlanStatusCodeType",
    "ScalingPolicyUpdateBehaviorType",
    "ScalingStatusCodeType",
    "ServiceNamespaceType",
)

DescribeScalingPlanResourcesPaginatorName = Literal["describe_scaling_plan_resources"]
DescribeScalingPlansPaginatorName = Literal["describe_scaling_plans"]
ForecastDataTypeType = Literal[
    "CapacityForecast", "LoadForecast", "ScheduledActionMaxCapacity", "ScheduledActionMinCapacity"
]
LoadMetricTypeType = Literal[
    "ALBTargetGroupRequestCount",
    "ASGTotalCPUUtilization",
    "ASGTotalNetworkIn",
    "ASGTotalNetworkOut",
]
MetricStatisticType = Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
PolicyTypeType = Literal["TargetTrackingScaling"]
PredictiveScalingMaxCapacityBehaviorType = Literal[
    "SetForecastCapacityToMaxCapacity",
    "SetMaxCapacityAboveForecastCapacity",
    "SetMaxCapacityToForecastCapacity",
]
PredictiveScalingModeType = Literal["ForecastAndScale", "ForecastOnly"]
ScalableDimensionType = Literal[
    "autoscaling:autoScalingGroup:DesiredCapacity",
    "dynamodb:index:ReadCapacityUnits",
    "dynamodb:index:WriteCapacityUnits",
    "dynamodb:table:ReadCapacityUnits",
    "dynamodb:table:WriteCapacityUnits",
    "ec2:spot-fleet-request:TargetCapacity",
    "ecs:service:DesiredCount",
    "rds:cluster:ReadReplicaCount",
]
ScalingMetricTypeType = Literal[
    "ALBRequestCountPerTarget",
    "ASGAverageCPUUtilization",
    "ASGAverageNetworkIn",
    "ASGAverageNetworkOut",
    "DynamoDBReadCapacityUtilization",
    "DynamoDBWriteCapacityUtilization",
    "EC2SpotFleetRequestAverageCPUUtilization",
    "EC2SpotFleetRequestAverageNetworkIn",
    "EC2SpotFleetRequestAverageNetworkOut",
    "ECSServiceAverageCPUUtilization",
    "ECSServiceAverageMemoryUtilization",
    "RDSReaderAverageCPUUtilization",
    "RDSReaderAverageDatabaseConnections",
]
ScalingPlanStatusCodeType = Literal[
    "Active",
    "ActiveWithProblems",
    "CreationFailed",
    "CreationInProgress",
    "DeletionFailed",
    "DeletionInProgress",
    "UpdateFailed",
    "UpdateInProgress",
]
ScalingPolicyUpdateBehaviorType = Literal["KeepExternalPolicies", "ReplaceExternalPolicies"]
ScalingStatusCodeType = Literal["Active", "Inactive", "PartiallyActive"]
ServiceNamespaceType = Literal["autoscaling", "dynamodb", "ec2", "ecs", "rds"]
