"""
Type annotations for application-autoscaling service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/type_defs.html)

Usage::

    ```python
    from mypy_boto3_application_autoscaling.type_defs import AlarmTypeDef

    data: AlarmTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AdjustmentTypeType,
    MetricAggregationTypeType,
    MetricStatisticType,
    MetricTypeType,
    PolicyTypeType,
    ScalableDimensionType,
    ScalingActivityStatusCodeType,
    ServiceNamespaceType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AlarmTypeDef",
    "CustomizedMetricSpecificationTypeDef",
    "DeleteScalingPolicyRequestRequestTypeDef",
    "DeleteScheduledActionRequestRequestTypeDef",
    "DeregisterScalableTargetRequestRequestTypeDef",
    "DescribeScalableTargetsRequestRequestTypeDef",
    "DescribeScalableTargetsResponseTypeDef",
    "DescribeScalingActivitiesRequestRequestTypeDef",
    "DescribeScalingActivitiesResponseTypeDef",
    "DescribeScalingPoliciesRequestRequestTypeDef",
    "DescribeScalingPoliciesResponseTypeDef",
    "DescribeScheduledActionsRequestRequestTypeDef",
    "DescribeScheduledActionsResponseTypeDef",
    "MetricDimensionTypeDef",
    "PaginatorConfigTypeDef",
    "PredefinedMetricSpecificationTypeDef",
    "PutScalingPolicyRequestRequestTypeDef",
    "PutScalingPolicyResponseTypeDef",
    "PutScheduledActionRequestRequestTypeDef",
    "RegisterScalableTargetRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ScalableTargetActionTypeDef",
    "ScalableTargetTypeDef",
    "ScalingActivityTypeDef",
    "ScalingPolicyTypeDef",
    "ScheduledActionTypeDef",
    "StepAdjustmentTypeDef",
    "StepScalingPolicyConfigurationTypeDef",
    "SuspendedStateTypeDef",
    "TargetTrackingScalingPolicyConfigurationTypeDef",
)

AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "AlarmName": str,
        "AlarmARN": str,
    },
)

_RequiredCustomizedMetricSpecificationTypeDef = TypedDict(
    "_RequiredCustomizedMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": MetricStatisticType,
    },
)
_OptionalCustomizedMetricSpecificationTypeDef = TypedDict(
    "_OptionalCustomizedMetricSpecificationTypeDef",
    {
        "Dimensions": List["MetricDimensionTypeDef"],
        "Unit": str,
    },
    total=False,
)

class CustomizedMetricSpecificationTypeDef(
    _RequiredCustomizedMetricSpecificationTypeDef, _OptionalCustomizedMetricSpecificationTypeDef
):
    pass

DeleteScalingPolicyRequestRequestTypeDef = TypedDict(
    "DeleteScalingPolicyRequestRequestTypeDef",
    {
        "PolicyName": str,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
    },
)

DeleteScheduledActionRequestRequestTypeDef = TypedDict(
    "DeleteScheduledActionRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ScheduledActionName": str,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
    },
)

DeregisterScalableTargetRequestRequestTypeDef = TypedDict(
    "DeregisterScalableTargetRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
    },
)

_RequiredDescribeScalableTargetsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeScalableTargetsRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
    },
)
_OptionalDescribeScalableTargetsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeScalableTargetsRequestRequestTypeDef",
    {
        "ResourceIds": List[str],
        "ScalableDimension": ScalableDimensionType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeScalableTargetsRequestRequestTypeDef(
    _RequiredDescribeScalableTargetsRequestRequestTypeDef,
    _OptionalDescribeScalableTargetsRequestRequestTypeDef,
):
    pass

DescribeScalableTargetsResponseTypeDef = TypedDict(
    "DescribeScalableTargetsResponseTypeDef",
    {
        "ScalableTargets": List["ScalableTargetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeScalingActivitiesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeScalingActivitiesRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
    },
)
_OptionalDescribeScalingActivitiesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeScalingActivitiesRequestRequestTypeDef",
    {
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeScalingActivitiesRequestRequestTypeDef(
    _RequiredDescribeScalingActivitiesRequestRequestTypeDef,
    _OptionalDescribeScalingActivitiesRequestRequestTypeDef,
):
    pass

DescribeScalingActivitiesResponseTypeDef = TypedDict(
    "DescribeScalingActivitiesResponseTypeDef",
    {
        "ScalingActivities": List["ScalingActivityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeScalingPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeScalingPoliciesRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
    },
)
_OptionalDescribeScalingPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeScalingPoliciesRequestRequestTypeDef",
    {
        "PolicyNames": List[str],
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeScalingPoliciesRequestRequestTypeDef(
    _RequiredDescribeScalingPoliciesRequestRequestTypeDef,
    _OptionalDescribeScalingPoliciesRequestRequestTypeDef,
):
    pass

DescribeScalingPoliciesResponseTypeDef = TypedDict(
    "DescribeScalingPoliciesResponseTypeDef",
    {
        "ScalingPolicies": List["ScalingPolicyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeScheduledActionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeScheduledActionsRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
    },
)
_OptionalDescribeScheduledActionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeScheduledActionsRequestRequestTypeDef",
    {
        "ScheduledActionNames": List[str],
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeScheduledActionsRequestRequestTypeDef(
    _RequiredDescribeScheduledActionsRequestRequestTypeDef,
    _OptionalDescribeScheduledActionsRequestRequestTypeDef,
):
    pass

DescribeScheduledActionsResponseTypeDef = TypedDict(
    "DescribeScheduledActionsResponseTypeDef",
    {
        "ScheduledActions": List["ScheduledActionTypeDef"],
        "NextToken": str,
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

_RequiredPredefinedMetricSpecificationTypeDef = TypedDict(
    "_RequiredPredefinedMetricSpecificationTypeDef",
    {
        "PredefinedMetricType": MetricTypeType,
    },
)
_OptionalPredefinedMetricSpecificationTypeDef = TypedDict(
    "_OptionalPredefinedMetricSpecificationTypeDef",
    {
        "ResourceLabel": str,
    },
    total=False,
)

class PredefinedMetricSpecificationTypeDef(
    _RequiredPredefinedMetricSpecificationTypeDef, _OptionalPredefinedMetricSpecificationTypeDef
):
    pass

_RequiredPutScalingPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutScalingPolicyRequestRequestTypeDef",
    {
        "PolicyName": str,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
    },
)
_OptionalPutScalingPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutScalingPolicyRequestRequestTypeDef",
    {
        "PolicyType": PolicyTypeType,
        "StepScalingPolicyConfiguration": "StepScalingPolicyConfigurationTypeDef",
        "TargetTrackingScalingPolicyConfiguration": "TargetTrackingScalingPolicyConfigurationTypeDef",
    },
    total=False,
)

class PutScalingPolicyRequestRequestTypeDef(
    _RequiredPutScalingPolicyRequestRequestTypeDef, _OptionalPutScalingPolicyRequestRequestTypeDef
):
    pass

PutScalingPolicyResponseTypeDef = TypedDict(
    "PutScalingPolicyResponseTypeDef",
    {
        "PolicyARN": str,
        "Alarms": List["AlarmTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutScheduledActionRequestRequestTypeDef = TypedDict(
    "_RequiredPutScheduledActionRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ScheduledActionName": str,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
    },
)
_OptionalPutScheduledActionRequestRequestTypeDef = TypedDict(
    "_OptionalPutScheduledActionRequestRequestTypeDef",
    {
        "Schedule": str,
        "Timezone": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "ScalableTargetAction": "ScalableTargetActionTypeDef",
    },
    total=False,
)

class PutScheduledActionRequestRequestTypeDef(
    _RequiredPutScheduledActionRequestRequestTypeDef,
    _OptionalPutScheduledActionRequestRequestTypeDef,
):
    pass

_RequiredRegisterScalableTargetRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterScalableTargetRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
    },
)
_OptionalRegisterScalableTargetRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterScalableTargetRequestRequestTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "RoleARN": str,
        "SuspendedState": "SuspendedStateTypeDef",
    },
    total=False,
)

class RegisterScalableTargetRequestRequestTypeDef(
    _RequiredRegisterScalableTargetRequestRequestTypeDef,
    _OptionalRegisterScalableTargetRequestRequestTypeDef,
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

ScalableTargetActionTypeDef = TypedDict(
    "ScalableTargetActionTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
    },
    total=False,
)

_RequiredScalableTargetTypeDef = TypedDict(
    "_RequiredScalableTargetTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "MinCapacity": int,
        "MaxCapacity": int,
        "RoleARN": str,
        "CreationTime": datetime,
    },
)
_OptionalScalableTargetTypeDef = TypedDict(
    "_OptionalScalableTargetTypeDef",
    {
        "SuspendedState": "SuspendedStateTypeDef",
    },
    total=False,
)

class ScalableTargetTypeDef(_RequiredScalableTargetTypeDef, _OptionalScalableTargetTypeDef):
    pass

_RequiredScalingActivityTypeDef = TypedDict(
    "_RequiredScalingActivityTypeDef",
    {
        "ActivityId": str,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "StatusCode": ScalingActivityStatusCodeType,
    },
)
_OptionalScalingActivityTypeDef = TypedDict(
    "_OptionalScalingActivityTypeDef",
    {
        "EndTime": datetime,
        "StatusMessage": str,
        "Details": str,
    },
    total=False,
)

class ScalingActivityTypeDef(_RequiredScalingActivityTypeDef, _OptionalScalingActivityTypeDef):
    pass

_RequiredScalingPolicyTypeDef = TypedDict(
    "_RequiredScalingPolicyTypeDef",
    {
        "PolicyARN": str,
        "PolicyName": str,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "PolicyType": PolicyTypeType,
        "CreationTime": datetime,
    },
)
_OptionalScalingPolicyTypeDef = TypedDict(
    "_OptionalScalingPolicyTypeDef",
    {
        "StepScalingPolicyConfiguration": "StepScalingPolicyConfigurationTypeDef",
        "TargetTrackingScalingPolicyConfiguration": "TargetTrackingScalingPolicyConfigurationTypeDef",
        "Alarms": List["AlarmTypeDef"],
    },
    total=False,
)

class ScalingPolicyTypeDef(_RequiredScalingPolicyTypeDef, _OptionalScalingPolicyTypeDef):
    pass

_RequiredScheduledActionTypeDef = TypedDict(
    "_RequiredScheduledActionTypeDef",
    {
        "ScheduledActionName": str,
        "ScheduledActionARN": str,
        "ServiceNamespace": ServiceNamespaceType,
        "Schedule": str,
        "ResourceId": str,
        "CreationTime": datetime,
    },
)
_OptionalScheduledActionTypeDef = TypedDict(
    "_OptionalScheduledActionTypeDef",
    {
        "Timezone": str,
        "ScalableDimension": ScalableDimensionType,
        "StartTime": datetime,
        "EndTime": datetime,
        "ScalableTargetAction": "ScalableTargetActionTypeDef",
    },
    total=False,
)

class ScheduledActionTypeDef(_RequiredScheduledActionTypeDef, _OptionalScheduledActionTypeDef):
    pass

_RequiredStepAdjustmentTypeDef = TypedDict(
    "_RequiredStepAdjustmentTypeDef",
    {
        "ScalingAdjustment": int,
    },
)
_OptionalStepAdjustmentTypeDef = TypedDict(
    "_OptionalStepAdjustmentTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
    },
    total=False,
)

class StepAdjustmentTypeDef(_RequiredStepAdjustmentTypeDef, _OptionalStepAdjustmentTypeDef):
    pass

StepScalingPolicyConfigurationTypeDef = TypedDict(
    "StepScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": AdjustmentTypeType,
        "StepAdjustments": List["StepAdjustmentTypeDef"],
        "MinAdjustmentMagnitude": int,
        "Cooldown": int,
        "MetricAggregationType": MetricAggregationTypeType,
    },
    total=False,
)

SuspendedStateTypeDef = TypedDict(
    "SuspendedStateTypeDef",
    {
        "DynamicScalingInSuspended": bool,
        "DynamicScalingOutSuspended": bool,
        "ScheduledScalingSuspended": bool,
    },
    total=False,
)

_RequiredTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "_RequiredTargetTrackingScalingPolicyConfigurationTypeDef",
    {
        "TargetValue": float,
    },
)
_OptionalTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "_OptionalTargetTrackingScalingPolicyConfigurationTypeDef",
    {
        "PredefinedMetricSpecification": "PredefinedMetricSpecificationTypeDef",
        "CustomizedMetricSpecification": "CustomizedMetricSpecificationTypeDef",
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "DisableScaleIn": bool,
    },
    total=False,
)

class TargetTrackingScalingPolicyConfigurationTypeDef(
    _RequiredTargetTrackingScalingPolicyConfigurationTypeDef,
    _OptionalTargetTrackingScalingPolicyConfigurationTypeDef,
):
    pass
