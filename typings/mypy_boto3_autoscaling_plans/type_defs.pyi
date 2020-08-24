"""
Main interface for autoscaling-plans service type definitions.

Usage::

    ```python
    from mypy_boto3_autoscaling_plans.type_defs import ApplicationSourceTypeDef

    data: ApplicationSourceTypeDef = {...}
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
    "ApplicationSourceTypeDef",
    "CustomizedLoadMetricSpecificationTypeDef",
    "CustomizedScalingMetricSpecificationTypeDef",
    "DatapointTypeDef",
    "MetricDimensionTypeDef",
    "PredefinedLoadMetricSpecificationTypeDef",
    "PredefinedScalingMetricSpecificationTypeDef",
    "ScalingInstructionTypeDef",
    "ScalingPlanResourceTypeDef",
    "ScalingPlanTypeDef",
    "ScalingPolicyTypeDef",
    "TagFilterTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "CreateScalingPlanResponseTypeDef",
    "DescribeScalingPlanResourcesResponseTypeDef",
    "DescribeScalingPlansResponseTypeDef",
    "GetScalingPlanResourceForecastDataResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ApplicationSourceTypeDef = TypedDict(
    "ApplicationSourceTypeDef",
    {"CloudFormationStackARN": str, "TagFilters": List["TagFilterTypeDef"]},
    total=False,
)

_RequiredCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "_RequiredCustomizedLoadMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
    },
)
_OptionalCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "_OptionalCustomizedLoadMetricSpecificationTypeDef",
    {"Dimensions": List["MetricDimensionTypeDef"], "Unit": str},
    total=False,
)


class CustomizedLoadMetricSpecificationTypeDef(
    _RequiredCustomizedLoadMetricSpecificationTypeDef,
    _OptionalCustomizedLoadMetricSpecificationTypeDef,
):
    pass


_RequiredCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_RequiredCustomizedScalingMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
    },
)
_OptionalCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_OptionalCustomizedScalingMetricSpecificationTypeDef",
    {"Dimensions": List["MetricDimensionTypeDef"], "Unit": str},
    total=False,
)


class CustomizedScalingMetricSpecificationTypeDef(
    _RequiredCustomizedScalingMetricSpecificationTypeDef,
    _OptionalCustomizedScalingMetricSpecificationTypeDef,
):
    pass


DatapointTypeDef = TypedDict(
    "DatapointTypeDef", {"Timestamp": datetime, "Value": float}, total=False
)

MetricDimensionTypeDef = TypedDict("MetricDimensionTypeDef", {"Name": str, "Value": str})

_RequiredPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "_RequiredPredefinedLoadMetricSpecificationTypeDef",
    {
        "PredefinedLoadMetricType": Literal[
            "ASGTotalCPUUtilization",
            "ASGTotalNetworkIn",
            "ASGTotalNetworkOut",
            "ALBTargetGroupRequestCount",
        ]
    },
)
_OptionalPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "_OptionalPredefinedLoadMetricSpecificationTypeDef", {"ResourceLabel": str}, total=False
)


class PredefinedLoadMetricSpecificationTypeDef(
    _RequiredPredefinedLoadMetricSpecificationTypeDef,
    _OptionalPredefinedLoadMetricSpecificationTypeDef,
):
    pass


_RequiredPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_RequiredPredefinedScalingMetricSpecificationTypeDef",
    {
        "PredefinedScalingMetricType": Literal[
            "ASGAverageCPUUtilization",
            "ASGAverageNetworkIn",
            "ASGAverageNetworkOut",
            "DynamoDBReadCapacityUtilization",
            "DynamoDBWriteCapacityUtilization",
            "ECSServiceAverageCPUUtilization",
            "ECSServiceAverageMemoryUtilization",
            "ALBRequestCountPerTarget",
            "RDSReaderAverageCPUUtilization",
            "RDSReaderAverageDatabaseConnections",
            "EC2SpotFleetRequestAverageCPUUtilization",
            "EC2SpotFleetRequestAverageNetworkIn",
            "EC2SpotFleetRequestAverageNetworkOut",
        ]
    },
)
_OptionalPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_OptionalPredefinedScalingMetricSpecificationTypeDef", {"ResourceLabel": str}, total=False
)


class PredefinedScalingMetricSpecificationTypeDef(
    _RequiredPredefinedScalingMetricSpecificationTypeDef,
    _OptionalPredefinedScalingMetricSpecificationTypeDef,
):
    pass


_RequiredScalingInstructionTypeDef = TypedDict(
    "_RequiredScalingInstructionTypeDef",
    {
        "ServiceNamespace": Literal["autoscaling", "ecs", "ec2", "rds", "dynamodb"],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "autoscaling:autoScalingGroup:DesiredCapacity",
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "rds:cluster:ReadReplicaCount",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
        ],
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": List["TargetTrackingConfigurationTypeDef"],
    },
)
_OptionalScalingInstructionTypeDef = TypedDict(
    "_OptionalScalingInstructionTypeDef",
    {
        "PredefinedLoadMetricSpecification": "PredefinedLoadMetricSpecificationTypeDef",
        "CustomizedLoadMetricSpecification": "CustomizedLoadMetricSpecificationTypeDef",
        "ScheduledActionBufferTime": int,
        "PredictiveScalingMaxCapacityBehavior": Literal[
            "SetForecastCapacityToMaxCapacity",
            "SetMaxCapacityToForecastCapacity",
            "SetMaxCapacityAboveForecastCapacity",
        ],
        "PredictiveScalingMaxCapacityBuffer": int,
        "PredictiveScalingMode": Literal["ForecastAndScale", "ForecastOnly"],
        "ScalingPolicyUpdateBehavior": Literal["KeepExternalPolicies", "ReplaceExternalPolicies"],
        "DisableDynamicScaling": bool,
    },
    total=False,
)


class ScalingInstructionTypeDef(
    _RequiredScalingInstructionTypeDef, _OptionalScalingInstructionTypeDef
):
    pass


_RequiredScalingPlanResourceTypeDef = TypedDict(
    "_RequiredScalingPlanResourceTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ServiceNamespace": Literal["autoscaling", "ecs", "ec2", "rds", "dynamodb"],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "autoscaling:autoScalingGroup:DesiredCapacity",
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "rds:cluster:ReadReplicaCount",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
        ],
        "ScalingStatusCode": Literal["Inactive", "PartiallyActive", "Active"],
    },
)
_OptionalScalingPlanResourceTypeDef = TypedDict(
    "_OptionalScalingPlanResourceTypeDef",
    {"ScalingPolicies": List["ScalingPolicyTypeDef"], "ScalingStatusMessage": str},
    total=False,
)


class ScalingPlanResourceTypeDef(
    _RequiredScalingPlanResourceTypeDef, _OptionalScalingPlanResourceTypeDef
):
    pass


_RequiredScalingPlanTypeDef = TypedDict(
    "_RequiredScalingPlanTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ApplicationSource": "ApplicationSourceTypeDef",
        "ScalingInstructions": List["ScalingInstructionTypeDef"],
        "StatusCode": Literal[
            "Active",
            "ActiveWithProblems",
            "CreationInProgress",
            "CreationFailed",
            "DeletionInProgress",
            "DeletionFailed",
            "UpdateInProgress",
            "UpdateFailed",
        ],
    },
)
_OptionalScalingPlanTypeDef = TypedDict(
    "_OptionalScalingPlanTypeDef",
    {"StatusMessage": str, "StatusStartTime": datetime, "CreationTime": datetime},
    total=False,
)


class ScalingPlanTypeDef(_RequiredScalingPlanTypeDef, _OptionalScalingPlanTypeDef):
    pass


_RequiredScalingPolicyTypeDef = TypedDict(
    "_RequiredScalingPolicyTypeDef",
    {"PolicyName": str, "PolicyType": Literal["TargetTrackingScaling"]},
)
_OptionalScalingPolicyTypeDef = TypedDict(
    "_OptionalScalingPolicyTypeDef",
    {"TargetTrackingConfiguration": "TargetTrackingConfigurationTypeDef"},
    total=False,
)


class ScalingPolicyTypeDef(_RequiredScalingPolicyTypeDef, _OptionalScalingPolicyTypeDef):
    pass


TagFilterTypeDef = TypedDict("TagFilterTypeDef", {"Key": str, "Values": List[str]}, total=False)

_RequiredTargetTrackingConfigurationTypeDef = TypedDict(
    "_RequiredTargetTrackingConfigurationTypeDef", {"TargetValue": float}
)
_OptionalTargetTrackingConfigurationTypeDef = TypedDict(
    "_OptionalTargetTrackingConfigurationTypeDef",
    {
        "PredefinedScalingMetricSpecification": "PredefinedScalingMetricSpecificationTypeDef",
        "CustomizedScalingMetricSpecification": "CustomizedScalingMetricSpecificationTypeDef",
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)


class TargetTrackingConfigurationTypeDef(
    _RequiredTargetTrackingConfigurationTypeDef, _OptionalTargetTrackingConfigurationTypeDef
):
    pass


CreateScalingPlanResponseTypeDef = TypedDict(
    "CreateScalingPlanResponseTypeDef", {"ScalingPlanVersion": int}
)

DescribeScalingPlanResourcesResponseTypeDef = TypedDict(
    "DescribeScalingPlanResourcesResponseTypeDef",
    {"ScalingPlanResources": List["ScalingPlanResourceTypeDef"], "NextToken": str},
    total=False,
)

DescribeScalingPlansResponseTypeDef = TypedDict(
    "DescribeScalingPlansResponseTypeDef",
    {"ScalingPlans": List["ScalingPlanTypeDef"], "NextToken": str},
    total=False,
)

GetScalingPlanResourceForecastDataResponseTypeDef = TypedDict(
    "GetScalingPlanResourceForecastDataResponseTypeDef", {"Datapoints": List["DatapointTypeDef"]}
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
