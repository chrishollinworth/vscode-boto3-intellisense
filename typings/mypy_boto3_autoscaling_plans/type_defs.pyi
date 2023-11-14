"""
Type annotations for autoscaling-plans service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/type_defs.html)

Usage::

    ```python
    from mypy_boto3_autoscaling_plans.type_defs import ApplicationSourceTypeDef

    data: ApplicationSourceTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ForecastDataTypeType,
    LoadMetricTypeType,
    MetricStatisticType,
    PredictiveScalingMaxCapacityBehaviorType,
    PredictiveScalingModeType,
    ScalableDimensionType,
    ScalingMetricTypeType,
    ScalingPlanStatusCodeType,
    ScalingPolicyUpdateBehaviorType,
    ScalingStatusCodeType,
    ServiceNamespaceType,
)

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
    "CreateScalingPlanRequestRequestTypeDef",
    "CreateScalingPlanResponseTypeDef",
    "CustomizedLoadMetricSpecificationTypeDef",
    "CustomizedScalingMetricSpecificationTypeDef",
    "DatapointTypeDef",
    "DeleteScalingPlanRequestRequestTypeDef",
    "DescribeScalingPlanResourcesRequestRequestTypeDef",
    "DescribeScalingPlanResourcesResponseTypeDef",
    "DescribeScalingPlansRequestRequestTypeDef",
    "DescribeScalingPlansResponseTypeDef",
    "GetScalingPlanResourceForecastDataRequestRequestTypeDef",
    "GetScalingPlanResourceForecastDataResponseTypeDef",
    "MetricDimensionTypeDef",
    "PaginatorConfigTypeDef",
    "PredefinedLoadMetricSpecificationTypeDef",
    "PredefinedScalingMetricSpecificationTypeDef",
    "ResponseMetadataTypeDef",
    "ScalingInstructionTypeDef",
    "ScalingPlanResourceTypeDef",
    "ScalingPlanTypeDef",
    "ScalingPolicyTypeDef",
    "TagFilterTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "UpdateScalingPlanRequestRequestTypeDef",
)

ApplicationSourceTypeDef = TypedDict(
    "ApplicationSourceTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List["TagFilterTypeDef"],
    },
    total=False,
)

CreateScalingPlanRequestRequestTypeDef = TypedDict(
    "CreateScalingPlanRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ApplicationSource": "ApplicationSourceTypeDef",
        "ScalingInstructions": List["ScalingInstructionTypeDef"],
    },
)

CreateScalingPlanResponseTypeDef = TypedDict(
    "CreateScalingPlanResponseTypeDef",
    {
        "ScalingPlanVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "_RequiredCustomizedLoadMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": MetricStatisticType,
    },
)
_OptionalCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "_OptionalCustomizedLoadMetricSpecificationTypeDef",
    {
        "Dimensions": List["MetricDimensionTypeDef"],
        "Unit": str,
    },
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
        "Statistic": MetricStatisticType,
    },
)
_OptionalCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_OptionalCustomizedScalingMetricSpecificationTypeDef",
    {
        "Dimensions": List["MetricDimensionTypeDef"],
        "Unit": str,
    },
    total=False,
)

class CustomizedScalingMetricSpecificationTypeDef(
    _RequiredCustomizedScalingMetricSpecificationTypeDef,
    _OptionalCustomizedScalingMetricSpecificationTypeDef,
):
    pass

DatapointTypeDef = TypedDict(
    "DatapointTypeDef",
    {
        "Timestamp": datetime,
        "Value": float,
    },
    total=False,
)

DeleteScalingPlanRequestRequestTypeDef = TypedDict(
    "DeleteScalingPlanRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
    },
)

_RequiredDescribeScalingPlanResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeScalingPlanResourcesRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
    },
)
_OptionalDescribeScalingPlanResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeScalingPlanResourcesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeScalingPlanResourcesRequestRequestTypeDef(
    _RequiredDescribeScalingPlanResourcesRequestRequestTypeDef,
    _OptionalDescribeScalingPlanResourcesRequestRequestTypeDef,
):
    pass

DescribeScalingPlanResourcesResponseTypeDef = TypedDict(
    "DescribeScalingPlanResourcesResponseTypeDef",
    {
        "ScalingPlanResources": List["ScalingPlanResourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScalingPlansRequestRequestTypeDef = TypedDict(
    "DescribeScalingPlansRequestRequestTypeDef",
    {
        "ScalingPlanNames": List[str],
        "ScalingPlanVersion": int,
        "ApplicationSources": List["ApplicationSourceTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeScalingPlansResponseTypeDef = TypedDict(
    "DescribeScalingPlansResponseTypeDef",
    {
        "ScalingPlans": List["ScalingPlanTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetScalingPlanResourceForecastDataRequestRequestTypeDef = TypedDict(
    "GetScalingPlanResourceForecastDataRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "ForecastDataType": ForecastDataTypeType,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)

GetScalingPlanResourceForecastDataResponseTypeDef = TypedDict(
    "GetScalingPlanResourceForecastDataResponseTypeDef",
    {
        "Datapoints": List["DatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "_RequiredPredefinedLoadMetricSpecificationTypeDef",
    {
        "PredefinedLoadMetricType": LoadMetricTypeType,
    },
)
_OptionalPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "_OptionalPredefinedLoadMetricSpecificationTypeDef",
    {
        "ResourceLabel": str,
    },
    total=False,
)

class PredefinedLoadMetricSpecificationTypeDef(
    _RequiredPredefinedLoadMetricSpecificationTypeDef,
    _OptionalPredefinedLoadMetricSpecificationTypeDef,
):
    pass

_RequiredPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_RequiredPredefinedScalingMetricSpecificationTypeDef",
    {
        "PredefinedScalingMetricType": ScalingMetricTypeType,
    },
)
_OptionalPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_OptionalPredefinedScalingMetricSpecificationTypeDef",
    {
        "ResourceLabel": str,
    },
    total=False,
)

class PredefinedScalingMetricSpecificationTypeDef(
    _RequiredPredefinedScalingMetricSpecificationTypeDef,
    _OptionalPredefinedScalingMetricSpecificationTypeDef,
):
    pass

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

_RequiredScalingInstructionTypeDef = TypedDict(
    "_RequiredScalingInstructionTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
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
        "PredictiveScalingMaxCapacityBehavior": PredictiveScalingMaxCapacityBehaviorType,
        "PredictiveScalingMaxCapacityBuffer": int,
        "PredictiveScalingMode": PredictiveScalingModeType,
        "ScalingPolicyUpdateBehavior": ScalingPolicyUpdateBehaviorType,
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
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "ScalingStatusCode": ScalingStatusCodeType,
    },
)
_OptionalScalingPlanResourceTypeDef = TypedDict(
    "_OptionalScalingPlanResourceTypeDef",
    {
        "ScalingPolicies": List["ScalingPolicyTypeDef"],
        "ScalingStatusMessage": str,
    },
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
        "StatusCode": ScalingPlanStatusCodeType,
    },
)
_OptionalScalingPlanTypeDef = TypedDict(
    "_OptionalScalingPlanTypeDef",
    {
        "StatusMessage": str,
        "StatusStartTime": datetime,
        "CreationTime": datetime,
    },
    total=False,
)

class ScalingPlanTypeDef(_RequiredScalingPlanTypeDef, _OptionalScalingPlanTypeDef):
    pass

_RequiredScalingPolicyTypeDef = TypedDict(
    "_RequiredScalingPolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyType": Literal["TargetTrackingScaling"],
    },
)
_OptionalScalingPolicyTypeDef = TypedDict(
    "_OptionalScalingPolicyTypeDef",
    {
        "TargetTrackingConfiguration": "TargetTrackingConfigurationTypeDef",
    },
    total=False,
)

class ScalingPolicyTypeDef(_RequiredScalingPolicyTypeDef, _OptionalScalingPolicyTypeDef):
    pass

TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
    total=False,
)

_RequiredTargetTrackingConfigurationTypeDef = TypedDict(
    "_RequiredTargetTrackingConfigurationTypeDef",
    {
        "TargetValue": float,
    },
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

_RequiredUpdateScalingPlanRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateScalingPlanRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
    },
)
_OptionalUpdateScalingPlanRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateScalingPlanRequestRequestTypeDef",
    {
        "ApplicationSource": "ApplicationSourceTypeDef",
        "ScalingInstructions": List["ScalingInstructionTypeDef"],
    },
    total=False,
)

class UpdateScalingPlanRequestRequestTypeDef(
    _RequiredUpdateScalingPlanRequestRequestTypeDef, _OptionalUpdateScalingPlanRequestRequestTypeDef
):
    pass
