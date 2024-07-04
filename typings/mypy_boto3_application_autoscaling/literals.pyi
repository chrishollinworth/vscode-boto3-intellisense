"""
Type annotations for application-autoscaling service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/literals.html)

Usage::

    ```python
    from mypy_boto3_application_autoscaling.literals import AdjustmentTypeType

    data: AdjustmentTypeType = "ChangeInCapacity"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AdjustmentTypeType",
    "DescribeScalableTargetsPaginatorName",
    "DescribeScalingActivitiesPaginatorName",
    "DescribeScalingPoliciesPaginatorName",
    "DescribeScheduledActionsPaginatorName",
    "MetricAggregationTypeType",
    "MetricStatisticType",
    "MetricTypeType",
    "PolicyTypeType",
    "ScalableDimensionType",
    "ScalingActivityStatusCodeType",
    "ServiceNamespaceType",
)

AdjustmentTypeType = Literal["ChangeInCapacity", "ExactCapacity", "PercentChangeInCapacity"]
DescribeScalableTargetsPaginatorName = Literal["describe_scalable_targets"]
DescribeScalingActivitiesPaginatorName = Literal["describe_scaling_activities"]
DescribeScalingPoliciesPaginatorName = Literal["describe_scaling_policies"]
DescribeScheduledActionsPaginatorName = Literal["describe_scheduled_actions"]
MetricAggregationTypeType = Literal["Average", "Maximum", "Minimum"]
MetricStatisticType = Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
MetricTypeType = Literal[
    "ALBRequestCountPerTarget",
    "AppStreamAverageCapacityUtilization",
    "CassandraReadCapacityUtilization",
    "CassandraWriteCapacityUtilization",
    "ComprehendInferenceUtilization",
    "DynamoDBReadCapacityUtilization",
    "DynamoDBWriteCapacityUtilization",
    "EC2SpotFleetRequestAverageCPUUtilization",
    "EC2SpotFleetRequestAverageNetworkIn",
    "EC2SpotFleetRequestAverageNetworkOut",
    "ECSServiceAverageCPUUtilization",
    "ECSServiceAverageMemoryUtilization",
    "ElastiCacheDatabaseCapacityUsageCountedForEvictPercentage",
    "ElastiCacheDatabaseMemoryUsageCountedForEvictPercentage",
    "ElastiCachePrimaryEngineCPUUtilization",
    "ElastiCacheReplicaEngineCPUUtilization",
    "KafkaBrokerStorageUtilization",
    "LambdaProvisionedConcurrencyUtilization",
    "NeptuneReaderAverageCPUUtilization",
    "RDSReaderAverageCPUUtilization",
    "RDSReaderAverageDatabaseConnections",
    "SageMakerInferenceComponentInvocationsPerCopy",
    "SageMakerVariantInvocationsPerInstance",
    "SageMakerVariantProvisionedConcurrencyUtilization",
    "WorkSpacesAverageUserSessionsCapacityUtilization",
]
PolicyTypeType = Literal["StepScaling", "TargetTrackingScaling"]
ScalableDimensionType = Literal[
    "appstream:fleet:DesiredCapacity",
    "cassandra:table:ReadCapacityUnits",
    "cassandra:table:WriteCapacityUnits",
    "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
    "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
    "custom-resource:ResourceType:Property",
    "dynamodb:index:ReadCapacityUnits",
    "dynamodb:index:WriteCapacityUnits",
    "dynamodb:table:ReadCapacityUnits",
    "dynamodb:table:WriteCapacityUnits",
    "ec2:spot-fleet-request:TargetCapacity",
    "ecs:service:DesiredCount",
    "elasticache:replication-group:NodeGroups",
    "elasticache:replication-group:Replicas",
    "elasticmapreduce:instancegroup:InstanceCount",
    "kafka:broker-storage:VolumeSize",
    "lambda:function:ProvisionedConcurrency",
    "neptune:cluster:ReadReplicaCount",
    "rds:cluster:ReadReplicaCount",
    "sagemaker:inference-component:DesiredCopyCount",
    "sagemaker:variant:DesiredInstanceCount",
    "sagemaker:variant:DesiredProvisionedConcurrency",
    "workspaces:workspacespool:DesiredUserSessions",
]
ScalingActivityStatusCodeType = Literal[
    "Failed", "InProgress", "Overridden", "Pending", "Successful", "Unfulfilled"
]
ServiceNamespaceType = Literal[
    "appstream",
    "cassandra",
    "comprehend",
    "custom-resource",
    "dynamodb",
    "ec2",
    "ecs",
    "elasticache",
    "elasticmapreduce",
    "kafka",
    "lambda",
    "neptune",
    "rds",
    "sagemaker",
    "workspaces",
]
