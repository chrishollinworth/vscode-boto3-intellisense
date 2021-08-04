"""
Type annotations for autoscaling service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/type_defs.html)

Usage::

    ```python
    from mypy_boto3_autoscaling.type_defs import ActivitiesTypeTypeDef

    data: ActivitiesTypeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    InstanceMetadataEndpointStateType,
    InstanceMetadataHttpTokensStateType,
    InstanceRefreshStatusType,
    LifecycleStateType,
    MetricStatisticType,
    MetricTypeType,
    PredefinedLoadMetricTypeType,
    PredefinedMetricPairTypeType,
    PredefinedScalingMetricTypeType,
    PredictiveScalingMaxCapacityBreachBehaviorType,
    PredictiveScalingModeType,
    ScalingActivityStatusCodeType,
    WarmPoolStateType,
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
    "ActivitiesTypeTypeDef",
    "ActivityTypeDef",
    "ActivityTypeTypeDef",
    "AdjustmentTypeTypeDef",
    "AlarmTypeDef",
    "AttachInstancesQueryRequestTypeDef",
    "AttachLoadBalancerTargetGroupsTypeRequestTypeDef",
    "AttachLoadBalancersTypeRequestTypeDef",
    "AutoScalingGroupNamesTypeRequestTypeDef",
    "AutoScalingGroupTypeDef",
    "AutoScalingGroupsTypeTypeDef",
    "AutoScalingInstanceDetailsTypeDef",
    "AutoScalingInstancesTypeTypeDef",
    "BatchDeleteScheduledActionAnswerTypeDef",
    "BatchDeleteScheduledActionTypeRequestTypeDef",
    "BatchPutScheduledUpdateGroupActionAnswerTypeDef",
    "BatchPutScheduledUpdateGroupActionTypeRequestTypeDef",
    "BlockDeviceMappingTypeDef",
    "CancelInstanceRefreshAnswerTypeDef",
    "CancelInstanceRefreshTypeRequestTypeDef",
    "CapacityForecastTypeDef",
    "CompleteLifecycleActionTypeRequestTypeDef",
    "CreateAutoScalingGroupTypeRequestTypeDef",
    "CreateLaunchConfigurationTypeRequestTypeDef",
    "CreateOrUpdateTagsTypeRequestTypeDef",
    "CustomizedMetricSpecificationTypeDef",
    "DeleteAutoScalingGroupTypeRequestTypeDef",
    "DeleteLifecycleHookTypeRequestTypeDef",
    "DeleteNotificationConfigurationTypeRequestTypeDef",
    "DeletePolicyTypeRequestTypeDef",
    "DeleteScheduledActionTypeRequestTypeDef",
    "DeleteTagsTypeRequestTypeDef",
    "DeleteWarmPoolTypeRequestTypeDef",
    "DescribeAccountLimitsAnswerTypeDef",
    "DescribeAdjustmentTypesAnswerTypeDef",
    "DescribeAutoScalingInstancesTypeRequestTypeDef",
    "DescribeAutoScalingNotificationTypesAnswerTypeDef",
    "DescribeInstanceRefreshesAnswerTypeDef",
    "DescribeInstanceRefreshesTypeRequestTypeDef",
    "DescribeLifecycleHookTypesAnswerTypeDef",
    "DescribeLifecycleHooksAnswerTypeDef",
    "DescribeLifecycleHooksTypeRequestTypeDef",
    "DescribeLoadBalancerTargetGroupsRequestRequestTypeDef",
    "DescribeLoadBalancerTargetGroupsResponseTypeDef",
    "DescribeLoadBalancersRequestRequestTypeDef",
    "DescribeLoadBalancersResponseTypeDef",
    "DescribeMetricCollectionTypesAnswerTypeDef",
    "DescribeNotificationConfigurationsAnswerTypeDef",
    "DescribeNotificationConfigurationsTypeRequestTypeDef",
    "DescribePoliciesTypeRequestTypeDef",
    "DescribeScalingActivitiesTypeRequestTypeDef",
    "DescribeScheduledActionsTypeRequestTypeDef",
    "DescribeTagsTypeRequestTypeDef",
    "DescribeTerminationPolicyTypesAnswerTypeDef",
    "DescribeWarmPoolAnswerTypeDef",
    "DescribeWarmPoolTypeRequestTypeDef",
    "DetachInstancesAnswerTypeDef",
    "DetachInstancesQueryRequestTypeDef",
    "DetachLoadBalancerTargetGroupsTypeRequestTypeDef",
    "DetachLoadBalancersTypeRequestTypeDef",
    "DisableMetricsCollectionQueryRequestTypeDef",
    "EbsTypeDef",
    "EnableMetricsCollectionQueryRequestTypeDef",
    "EnabledMetricTypeDef",
    "EnterStandbyAnswerTypeDef",
    "EnterStandbyQueryRequestTypeDef",
    "ExecutePolicyTypeRequestTypeDef",
    "ExitStandbyAnswerTypeDef",
    "ExitStandbyQueryRequestTypeDef",
    "FailedScheduledUpdateGroupActionRequestTypeDef",
    "FilterTypeDef",
    "GetPredictiveScalingForecastAnswerTypeDef",
    "GetPredictiveScalingForecastTypeRequestTypeDef",
    "InstanceMetadataOptionsTypeDef",
    "InstanceMonitoringTypeDef",
    "InstanceRefreshLivePoolProgressTypeDef",
    "InstanceRefreshProgressDetailsTypeDef",
    "InstanceRefreshTypeDef",
    "InstanceRefreshWarmPoolProgressTypeDef",
    "InstanceTypeDef",
    "InstancesDistributionTypeDef",
    "LaunchConfigurationNameTypeRequestTypeDef",
    "LaunchConfigurationNamesTypeRequestTypeDef",
    "LaunchConfigurationTypeDef",
    "LaunchConfigurationsTypeTypeDef",
    "LaunchTemplateOverridesTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "LaunchTemplateTypeDef",
    "LifecycleHookSpecificationTypeDef",
    "LifecycleHookTypeDef",
    "LoadBalancerStateTypeDef",
    "LoadBalancerTargetGroupStateTypeDef",
    "LoadForecastTypeDef",
    "MetricCollectionTypeTypeDef",
    "MetricDimensionTypeDef",
    "MetricGranularityTypeTypeDef",
    "MixedInstancesPolicyTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PoliciesTypeTypeDef",
    "PolicyARNTypeTypeDef",
    "PredefinedMetricSpecificationTypeDef",
    "PredictiveScalingConfigurationTypeDef",
    "PredictiveScalingMetricSpecificationTypeDef",
    "PredictiveScalingPredefinedLoadMetricTypeDef",
    "PredictiveScalingPredefinedMetricPairTypeDef",
    "PredictiveScalingPredefinedScalingMetricTypeDef",
    "ProcessTypeTypeDef",
    "ProcessesTypeTypeDef",
    "PutLifecycleHookTypeRequestTypeDef",
    "PutNotificationConfigurationTypeRequestTypeDef",
    "PutScalingPolicyTypeRequestTypeDef",
    "PutScheduledUpdateGroupActionTypeRequestTypeDef",
    "PutWarmPoolTypeRequestTypeDef",
    "RecordLifecycleActionHeartbeatTypeRequestTypeDef",
    "RefreshPreferencesTypeDef",
    "ResponseMetadataTypeDef",
    "ScalingPolicyTypeDef",
    "ScalingProcessQueryRequestTypeDef",
    "ScheduledActionsTypeTypeDef",
    "ScheduledUpdateGroupActionRequestTypeDef",
    "ScheduledUpdateGroupActionTypeDef",
    "SetDesiredCapacityTypeRequestTypeDef",
    "SetInstanceHealthQueryRequestTypeDef",
    "SetInstanceProtectionQueryRequestTypeDef",
    "StartInstanceRefreshAnswerTypeDef",
    "StartInstanceRefreshTypeRequestTypeDef",
    "StepAdjustmentTypeDef",
    "SuspendedProcessTypeDef",
    "TagDescriptionTypeDef",
    "TagTypeDef",
    "TagsTypeTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "TerminateInstanceInAutoScalingGroupTypeRequestTypeDef",
    "UpdateAutoScalingGroupTypeRequestTypeDef",
    "WarmPoolConfigurationTypeDef",
)

ActivitiesTypeTypeDef = TypedDict(
    "ActivitiesTypeTypeDef",
    {
        "Activities": List["ActivityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredActivityTypeDef = TypedDict(
    "_RequiredActivityTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Cause": str,
        "StartTime": datetime,
        "StatusCode": ScalingActivityStatusCodeType,
    },
)
_OptionalActivityTypeDef = TypedDict(
    "_OptionalActivityTypeDef",
    {
        "Description": str,
        "EndTime": datetime,
        "StatusMessage": str,
        "Progress": int,
        "Details": str,
        "AutoScalingGroupState": str,
        "AutoScalingGroupARN": str,
    },
    total=False,
)

class ActivityTypeDef(_RequiredActivityTypeDef, _OptionalActivityTypeDef):
    pass

ActivityTypeTypeDef = TypedDict(
    "ActivityTypeTypeDef",
    {
        "Activity": "ActivityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdjustmentTypeTypeDef = TypedDict(
    "AdjustmentTypeTypeDef",
    {
        "AdjustmentType": str,
    },
    total=False,
)

AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "AlarmName": str,
        "AlarmARN": str,
    },
    total=False,
)

_RequiredAttachInstancesQueryRequestTypeDef = TypedDict(
    "_RequiredAttachInstancesQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalAttachInstancesQueryRequestTypeDef = TypedDict(
    "_OptionalAttachInstancesQueryRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
    total=False,
)

class AttachInstancesQueryRequestTypeDef(
    _RequiredAttachInstancesQueryRequestTypeDef, _OptionalAttachInstancesQueryRequestTypeDef
):
    pass

AttachLoadBalancerTargetGroupsTypeRequestTypeDef = TypedDict(
    "AttachLoadBalancerTargetGroupsTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "TargetGroupARNs": List[str],
    },
)

AttachLoadBalancersTypeRequestTypeDef = TypedDict(
    "AttachLoadBalancersTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "LoadBalancerNames": List[str],
    },
)

AutoScalingGroupNamesTypeRequestTypeDef = TypedDict(
    "AutoScalingGroupNamesTypeRequestTypeDef",
    {
        "AutoScalingGroupNames": List[str],
        "NextToken": str,
        "MaxRecords": int,
    },
    total=False,
)

_RequiredAutoScalingGroupTypeDef = TypedDict(
    "_RequiredAutoScalingGroupTypeDef",
    {
        "AutoScalingGroupName": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
        "DefaultCooldown": int,
        "AvailabilityZones": List[str],
        "HealthCheckType": str,
        "CreatedTime": datetime,
    },
)
_OptionalAutoScalingGroupTypeDef = TypedDict(
    "_OptionalAutoScalingGroupTypeDef",
    {
        "AutoScalingGroupARN": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": "LaunchTemplateSpecificationTypeDef",
        "MixedInstancesPolicy": "MixedInstancesPolicyTypeDef",
        "PredictedCapacity": int,
        "LoadBalancerNames": List[str],
        "TargetGroupARNs": List[str],
        "HealthCheckGracePeriod": int,
        "Instances": List["InstanceTypeDef"],
        "SuspendedProcesses": List["SuspendedProcessTypeDef"],
        "PlacementGroup": str,
        "VPCZoneIdentifier": str,
        "EnabledMetrics": List["EnabledMetricTypeDef"],
        "Status": str,
        "Tags": List["TagDescriptionTypeDef"],
        "TerminationPolicies": List[str],
        "NewInstancesProtectedFromScaleIn": bool,
        "ServiceLinkedRoleARN": str,
        "MaxInstanceLifetime": int,
        "CapacityRebalance": bool,
        "WarmPoolConfiguration": "WarmPoolConfigurationTypeDef",
        "WarmPoolSize": int,
        "Context": str,
    },
    total=False,
)

class AutoScalingGroupTypeDef(_RequiredAutoScalingGroupTypeDef, _OptionalAutoScalingGroupTypeDef):
    pass

AutoScalingGroupsTypeTypeDef = TypedDict(
    "AutoScalingGroupsTypeTypeDef",
    {
        "AutoScalingGroups": List["AutoScalingGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAutoScalingInstanceDetailsTypeDef = TypedDict(
    "_RequiredAutoScalingInstanceDetailsTypeDef",
    {
        "InstanceId": str,
        "AutoScalingGroupName": str,
        "AvailabilityZone": str,
        "LifecycleState": str,
        "HealthStatus": str,
        "ProtectedFromScaleIn": bool,
    },
)
_OptionalAutoScalingInstanceDetailsTypeDef = TypedDict(
    "_OptionalAutoScalingInstanceDetailsTypeDef",
    {
        "InstanceType": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": "LaunchTemplateSpecificationTypeDef",
        "WeightedCapacity": str,
    },
    total=False,
)

class AutoScalingInstanceDetailsTypeDef(
    _RequiredAutoScalingInstanceDetailsTypeDef, _OptionalAutoScalingInstanceDetailsTypeDef
):
    pass

AutoScalingInstancesTypeTypeDef = TypedDict(
    "AutoScalingInstancesTypeTypeDef",
    {
        "AutoScalingInstances": List["AutoScalingInstanceDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteScheduledActionAnswerTypeDef = TypedDict(
    "BatchDeleteScheduledActionAnswerTypeDef",
    {
        "FailedScheduledActions": List["FailedScheduledUpdateGroupActionRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteScheduledActionTypeRequestTypeDef = TypedDict(
    "BatchDeleteScheduledActionTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionNames": List[str],
    },
)

BatchPutScheduledUpdateGroupActionAnswerTypeDef = TypedDict(
    "BatchPutScheduledUpdateGroupActionAnswerTypeDef",
    {
        "FailedScheduledUpdateGroupActions": List["FailedScheduledUpdateGroupActionRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPutScheduledUpdateGroupActionTypeRequestTypeDef = TypedDict(
    "BatchPutScheduledUpdateGroupActionTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledUpdateGroupActions": List["ScheduledUpdateGroupActionRequestTypeDef"],
    },
)

_RequiredBlockDeviceMappingTypeDef = TypedDict(
    "_RequiredBlockDeviceMappingTypeDef",
    {
        "DeviceName": str,
    },
)
_OptionalBlockDeviceMappingTypeDef = TypedDict(
    "_OptionalBlockDeviceMappingTypeDef",
    {
        "VirtualName": str,
        "Ebs": "EbsTypeDef",
        "NoDevice": bool,
    },
    total=False,
)

class BlockDeviceMappingTypeDef(
    _RequiredBlockDeviceMappingTypeDef, _OptionalBlockDeviceMappingTypeDef
):
    pass

CancelInstanceRefreshAnswerTypeDef = TypedDict(
    "CancelInstanceRefreshAnswerTypeDef",
    {
        "InstanceRefreshId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelInstanceRefreshTypeRequestTypeDef = TypedDict(
    "CancelInstanceRefreshTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)

CapacityForecastTypeDef = TypedDict(
    "CapacityForecastTypeDef",
    {
        "Timestamps": List[datetime],
        "Values": List[float],
    },
)

_RequiredCompleteLifecycleActionTypeRequestTypeDef = TypedDict(
    "_RequiredCompleteLifecycleActionTypeRequestTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
        "LifecycleActionResult": str,
    },
)
_OptionalCompleteLifecycleActionTypeRequestTypeDef = TypedDict(
    "_OptionalCompleteLifecycleActionTypeRequestTypeDef",
    {
        "LifecycleActionToken": str,
        "InstanceId": str,
    },
    total=False,
)

class CompleteLifecycleActionTypeRequestTypeDef(
    _RequiredCompleteLifecycleActionTypeRequestTypeDef,
    _OptionalCompleteLifecycleActionTypeRequestTypeDef,
):
    pass

_RequiredCreateAutoScalingGroupTypeRequestTypeDef = TypedDict(
    "_RequiredCreateAutoScalingGroupTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "MinSize": int,
        "MaxSize": int,
    },
)
_OptionalCreateAutoScalingGroupTypeRequestTypeDef = TypedDict(
    "_OptionalCreateAutoScalingGroupTypeRequestTypeDef",
    {
        "LaunchConfigurationName": str,
        "LaunchTemplate": "LaunchTemplateSpecificationTypeDef",
        "MixedInstancesPolicy": "MixedInstancesPolicyTypeDef",
        "InstanceId": str,
        "DesiredCapacity": int,
        "DefaultCooldown": int,
        "AvailabilityZones": List[str],
        "LoadBalancerNames": List[str],
        "TargetGroupARNs": List[str],
        "HealthCheckType": str,
        "HealthCheckGracePeriod": int,
        "PlacementGroup": str,
        "VPCZoneIdentifier": str,
        "TerminationPolicies": List[str],
        "NewInstancesProtectedFromScaleIn": bool,
        "CapacityRebalance": bool,
        "LifecycleHookSpecificationList": List["LifecycleHookSpecificationTypeDef"],
        "Tags": List["TagTypeDef"],
        "ServiceLinkedRoleARN": str,
        "MaxInstanceLifetime": int,
        "Context": str,
    },
    total=False,
)

class CreateAutoScalingGroupTypeRequestTypeDef(
    _RequiredCreateAutoScalingGroupTypeRequestTypeDef,
    _OptionalCreateAutoScalingGroupTypeRequestTypeDef,
):
    pass

_RequiredCreateLaunchConfigurationTypeRequestTypeDef = TypedDict(
    "_RequiredCreateLaunchConfigurationTypeRequestTypeDef",
    {
        "LaunchConfigurationName": str,
    },
)
_OptionalCreateLaunchConfigurationTypeRequestTypeDef = TypedDict(
    "_OptionalCreateLaunchConfigurationTypeRequestTypeDef",
    {
        "ImageId": str,
        "KeyName": str,
        "SecurityGroups": List[str],
        "ClassicLinkVPCId": str,
        "ClassicLinkVPCSecurityGroups": List[str],
        "UserData": str,
        "InstanceId": str,
        "InstanceType": str,
        "KernelId": str,
        "RamdiskId": str,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "InstanceMonitoring": "InstanceMonitoringTypeDef",
        "SpotPrice": str,
        "IamInstanceProfile": str,
        "EbsOptimized": bool,
        "AssociatePublicIpAddress": bool,
        "PlacementTenancy": str,
        "MetadataOptions": "InstanceMetadataOptionsTypeDef",
    },
    total=False,
)

class CreateLaunchConfigurationTypeRequestTypeDef(
    _RequiredCreateLaunchConfigurationTypeRequestTypeDef,
    _OptionalCreateLaunchConfigurationTypeRequestTypeDef,
):
    pass

CreateOrUpdateTagsTypeRequestTypeDef = TypedDict(
    "CreateOrUpdateTagsTypeRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
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

_RequiredDeleteAutoScalingGroupTypeRequestTypeDef = TypedDict(
    "_RequiredDeleteAutoScalingGroupTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalDeleteAutoScalingGroupTypeRequestTypeDef = TypedDict(
    "_OptionalDeleteAutoScalingGroupTypeRequestTypeDef",
    {
        "ForceDelete": bool,
    },
    total=False,
)

class DeleteAutoScalingGroupTypeRequestTypeDef(
    _RequiredDeleteAutoScalingGroupTypeRequestTypeDef,
    _OptionalDeleteAutoScalingGroupTypeRequestTypeDef,
):
    pass

DeleteLifecycleHookTypeRequestTypeDef = TypedDict(
    "DeleteLifecycleHookTypeRequestTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
    },
)

DeleteNotificationConfigurationTypeRequestTypeDef = TypedDict(
    "DeleteNotificationConfigurationTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "TopicARN": str,
    },
)

_RequiredDeletePolicyTypeRequestTypeDef = TypedDict(
    "_RequiredDeletePolicyTypeRequestTypeDef",
    {
        "PolicyName": str,
    },
)
_OptionalDeletePolicyTypeRequestTypeDef = TypedDict(
    "_OptionalDeletePolicyTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
    total=False,
)

class DeletePolicyTypeRequestTypeDef(
    _RequiredDeletePolicyTypeRequestTypeDef, _OptionalDeletePolicyTypeRequestTypeDef
):
    pass

DeleteScheduledActionTypeRequestTypeDef = TypedDict(
    "DeleteScheduledActionTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionName": str,
    },
)

DeleteTagsTypeRequestTypeDef = TypedDict(
    "DeleteTagsTypeRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
)

_RequiredDeleteWarmPoolTypeRequestTypeDef = TypedDict(
    "_RequiredDeleteWarmPoolTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalDeleteWarmPoolTypeRequestTypeDef = TypedDict(
    "_OptionalDeleteWarmPoolTypeRequestTypeDef",
    {
        "ForceDelete": bool,
    },
    total=False,
)

class DeleteWarmPoolTypeRequestTypeDef(
    _RequiredDeleteWarmPoolTypeRequestTypeDef, _OptionalDeleteWarmPoolTypeRequestTypeDef
):
    pass

DescribeAccountLimitsAnswerTypeDef = TypedDict(
    "DescribeAccountLimitsAnswerTypeDef",
    {
        "MaxNumberOfAutoScalingGroups": int,
        "MaxNumberOfLaunchConfigurations": int,
        "NumberOfAutoScalingGroups": int,
        "NumberOfLaunchConfigurations": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAdjustmentTypesAnswerTypeDef = TypedDict(
    "DescribeAdjustmentTypesAnswerTypeDef",
    {
        "AdjustmentTypes": List["AdjustmentTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAutoScalingInstancesTypeRequestTypeDef = TypedDict(
    "DescribeAutoScalingInstancesTypeRequestTypeDef",
    {
        "InstanceIds": List[str],
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

DescribeAutoScalingNotificationTypesAnswerTypeDef = TypedDict(
    "DescribeAutoScalingNotificationTypesAnswerTypeDef",
    {
        "AutoScalingNotificationTypes": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceRefreshesAnswerTypeDef = TypedDict(
    "DescribeInstanceRefreshesAnswerTypeDef",
    {
        "InstanceRefreshes": List["InstanceRefreshTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeInstanceRefreshesTypeRequestTypeDef = TypedDict(
    "_RequiredDescribeInstanceRefreshesTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalDescribeInstanceRefreshesTypeRequestTypeDef = TypedDict(
    "_OptionalDescribeInstanceRefreshesTypeRequestTypeDef",
    {
        "InstanceRefreshIds": List[str],
        "NextToken": str,
        "MaxRecords": int,
    },
    total=False,
)

class DescribeInstanceRefreshesTypeRequestTypeDef(
    _RequiredDescribeInstanceRefreshesTypeRequestTypeDef,
    _OptionalDescribeInstanceRefreshesTypeRequestTypeDef,
):
    pass

DescribeLifecycleHookTypesAnswerTypeDef = TypedDict(
    "DescribeLifecycleHookTypesAnswerTypeDef",
    {
        "LifecycleHookTypes": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLifecycleHooksAnswerTypeDef = TypedDict(
    "DescribeLifecycleHooksAnswerTypeDef",
    {
        "LifecycleHooks": List["LifecycleHookTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeLifecycleHooksTypeRequestTypeDef = TypedDict(
    "_RequiredDescribeLifecycleHooksTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalDescribeLifecycleHooksTypeRequestTypeDef = TypedDict(
    "_OptionalDescribeLifecycleHooksTypeRequestTypeDef",
    {
        "LifecycleHookNames": List[str],
    },
    total=False,
)

class DescribeLifecycleHooksTypeRequestTypeDef(
    _RequiredDescribeLifecycleHooksTypeRequestTypeDef,
    _OptionalDescribeLifecycleHooksTypeRequestTypeDef,
):
    pass

_RequiredDescribeLoadBalancerTargetGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeLoadBalancerTargetGroupsRequestRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalDescribeLoadBalancerTargetGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeLoadBalancerTargetGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxRecords": int,
    },
    total=False,
)

class DescribeLoadBalancerTargetGroupsRequestRequestTypeDef(
    _RequiredDescribeLoadBalancerTargetGroupsRequestRequestTypeDef,
    _OptionalDescribeLoadBalancerTargetGroupsRequestRequestTypeDef,
):
    pass

DescribeLoadBalancerTargetGroupsResponseTypeDef = TypedDict(
    "DescribeLoadBalancerTargetGroupsResponseTypeDef",
    {
        "LoadBalancerTargetGroups": List["LoadBalancerTargetGroupStateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeLoadBalancersRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeLoadBalancersRequestRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalDescribeLoadBalancersRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeLoadBalancersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxRecords": int,
    },
    total=False,
)

class DescribeLoadBalancersRequestRequestTypeDef(
    _RequiredDescribeLoadBalancersRequestRequestTypeDef,
    _OptionalDescribeLoadBalancersRequestRequestTypeDef,
):
    pass

DescribeLoadBalancersResponseTypeDef = TypedDict(
    "DescribeLoadBalancersResponseTypeDef",
    {
        "LoadBalancers": List["LoadBalancerStateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMetricCollectionTypesAnswerTypeDef = TypedDict(
    "DescribeMetricCollectionTypesAnswerTypeDef",
    {
        "Metrics": List["MetricCollectionTypeTypeDef"],
        "Granularities": List["MetricGranularityTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNotificationConfigurationsAnswerTypeDef = TypedDict(
    "DescribeNotificationConfigurationsAnswerTypeDef",
    {
        "NotificationConfigurations": List["NotificationConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNotificationConfigurationsTypeRequestTypeDef = TypedDict(
    "DescribeNotificationConfigurationsTypeRequestTypeDef",
    {
        "AutoScalingGroupNames": List[str],
        "NextToken": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribePoliciesTypeRequestTypeDef = TypedDict(
    "DescribePoliciesTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "PolicyNames": List[str],
        "PolicyTypes": List[str],
        "NextToken": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribeScalingActivitiesTypeRequestTypeDef = TypedDict(
    "DescribeScalingActivitiesTypeRequestTypeDef",
    {
        "ActivityIds": List[str],
        "AutoScalingGroupName": str,
        "IncludeDeletedGroups": bool,
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

DescribeScheduledActionsTypeRequestTypeDef = TypedDict(
    "DescribeScheduledActionsTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionNames": List[str],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "NextToken": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribeTagsTypeRequestTypeDef = TypedDict(
    "DescribeTagsTypeRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribeTerminationPolicyTypesAnswerTypeDef = TypedDict(
    "DescribeTerminationPolicyTypesAnswerTypeDef",
    {
        "TerminationPolicyTypes": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWarmPoolAnswerTypeDef = TypedDict(
    "DescribeWarmPoolAnswerTypeDef",
    {
        "WarmPoolConfiguration": "WarmPoolConfigurationTypeDef",
        "Instances": List["InstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeWarmPoolTypeRequestTypeDef = TypedDict(
    "_RequiredDescribeWarmPoolTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalDescribeWarmPoolTypeRequestTypeDef = TypedDict(
    "_OptionalDescribeWarmPoolTypeRequestTypeDef",
    {
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeWarmPoolTypeRequestTypeDef(
    _RequiredDescribeWarmPoolTypeRequestTypeDef, _OptionalDescribeWarmPoolTypeRequestTypeDef
):
    pass

DetachInstancesAnswerTypeDef = TypedDict(
    "DetachInstancesAnswerTypeDef",
    {
        "Activities": List["ActivityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetachInstancesQueryRequestTypeDef = TypedDict(
    "_RequiredDetachInstancesQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ShouldDecrementDesiredCapacity": bool,
    },
)
_OptionalDetachInstancesQueryRequestTypeDef = TypedDict(
    "_OptionalDetachInstancesQueryRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
    total=False,
)

class DetachInstancesQueryRequestTypeDef(
    _RequiredDetachInstancesQueryRequestTypeDef, _OptionalDetachInstancesQueryRequestTypeDef
):
    pass

DetachLoadBalancerTargetGroupsTypeRequestTypeDef = TypedDict(
    "DetachLoadBalancerTargetGroupsTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "TargetGroupARNs": List[str],
    },
)

DetachLoadBalancersTypeRequestTypeDef = TypedDict(
    "DetachLoadBalancersTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "LoadBalancerNames": List[str],
    },
)

_RequiredDisableMetricsCollectionQueryRequestTypeDef = TypedDict(
    "_RequiredDisableMetricsCollectionQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalDisableMetricsCollectionQueryRequestTypeDef = TypedDict(
    "_OptionalDisableMetricsCollectionQueryRequestTypeDef",
    {
        "Metrics": List[str],
    },
    total=False,
)

class DisableMetricsCollectionQueryRequestTypeDef(
    _RequiredDisableMetricsCollectionQueryRequestTypeDef,
    _OptionalDisableMetricsCollectionQueryRequestTypeDef,
):
    pass

EbsTypeDef = TypedDict(
    "EbsTypeDef",
    {
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": str,
        "DeleteOnTermination": bool,
        "Iops": int,
        "Encrypted": bool,
        "Throughput": int,
    },
    total=False,
)

_RequiredEnableMetricsCollectionQueryRequestTypeDef = TypedDict(
    "_RequiredEnableMetricsCollectionQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "Granularity": str,
    },
)
_OptionalEnableMetricsCollectionQueryRequestTypeDef = TypedDict(
    "_OptionalEnableMetricsCollectionQueryRequestTypeDef",
    {
        "Metrics": List[str],
    },
    total=False,
)

class EnableMetricsCollectionQueryRequestTypeDef(
    _RequiredEnableMetricsCollectionQueryRequestTypeDef,
    _OptionalEnableMetricsCollectionQueryRequestTypeDef,
):
    pass

EnabledMetricTypeDef = TypedDict(
    "EnabledMetricTypeDef",
    {
        "Metric": str,
        "Granularity": str,
    },
    total=False,
)

EnterStandbyAnswerTypeDef = TypedDict(
    "EnterStandbyAnswerTypeDef",
    {
        "Activities": List["ActivityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnterStandbyQueryRequestTypeDef = TypedDict(
    "_RequiredEnterStandbyQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ShouldDecrementDesiredCapacity": bool,
    },
)
_OptionalEnterStandbyQueryRequestTypeDef = TypedDict(
    "_OptionalEnterStandbyQueryRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
    total=False,
)

class EnterStandbyQueryRequestTypeDef(
    _RequiredEnterStandbyQueryRequestTypeDef, _OptionalEnterStandbyQueryRequestTypeDef
):
    pass

_RequiredExecutePolicyTypeRequestTypeDef = TypedDict(
    "_RequiredExecutePolicyTypeRequestTypeDef",
    {
        "PolicyName": str,
    },
)
_OptionalExecutePolicyTypeRequestTypeDef = TypedDict(
    "_OptionalExecutePolicyTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "HonorCooldown": bool,
        "MetricValue": float,
        "BreachThreshold": float,
    },
    total=False,
)

class ExecutePolicyTypeRequestTypeDef(
    _RequiredExecutePolicyTypeRequestTypeDef, _OptionalExecutePolicyTypeRequestTypeDef
):
    pass

ExitStandbyAnswerTypeDef = TypedDict(
    "ExitStandbyAnswerTypeDef",
    {
        "Activities": List["ActivityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExitStandbyQueryRequestTypeDef = TypedDict(
    "_RequiredExitStandbyQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalExitStandbyQueryRequestTypeDef = TypedDict(
    "_OptionalExitStandbyQueryRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
    total=False,
)

class ExitStandbyQueryRequestTypeDef(
    _RequiredExitStandbyQueryRequestTypeDef, _OptionalExitStandbyQueryRequestTypeDef
):
    pass

_RequiredFailedScheduledUpdateGroupActionRequestTypeDef = TypedDict(
    "_RequiredFailedScheduledUpdateGroupActionRequestTypeDef",
    {
        "ScheduledActionName": str,
    },
)
_OptionalFailedScheduledUpdateGroupActionRequestTypeDef = TypedDict(
    "_OptionalFailedScheduledUpdateGroupActionRequestTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

class FailedScheduledUpdateGroupActionRequestTypeDef(
    _RequiredFailedScheduledUpdateGroupActionRequestTypeDef,
    _OptionalFailedScheduledUpdateGroupActionRequestTypeDef,
):
    pass

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
    total=False,
)

GetPredictiveScalingForecastAnswerTypeDef = TypedDict(
    "GetPredictiveScalingForecastAnswerTypeDef",
    {
        "LoadForecast": List["LoadForecastTypeDef"],
        "CapacityForecast": "CapacityForecastTypeDef",
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPredictiveScalingForecastTypeRequestTypeDef = TypedDict(
    "GetPredictiveScalingForecastTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "PolicyName": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)

InstanceMetadataOptionsTypeDef = TypedDict(
    "InstanceMetadataOptionsTypeDef",
    {
        "HttpTokens": InstanceMetadataHttpTokensStateType,
        "HttpPutResponseHopLimit": int,
        "HttpEndpoint": InstanceMetadataEndpointStateType,
    },
    total=False,
)

InstanceMonitoringTypeDef = TypedDict(
    "InstanceMonitoringTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

InstanceRefreshLivePoolProgressTypeDef = TypedDict(
    "InstanceRefreshLivePoolProgressTypeDef",
    {
        "PercentageComplete": int,
        "InstancesToUpdate": int,
    },
    total=False,
)

InstanceRefreshProgressDetailsTypeDef = TypedDict(
    "InstanceRefreshProgressDetailsTypeDef",
    {
        "LivePoolProgress": "InstanceRefreshLivePoolProgressTypeDef",
        "WarmPoolProgress": "InstanceRefreshWarmPoolProgressTypeDef",
    },
    total=False,
)

InstanceRefreshTypeDef = TypedDict(
    "InstanceRefreshTypeDef",
    {
        "InstanceRefreshId": str,
        "AutoScalingGroupName": str,
        "Status": InstanceRefreshStatusType,
        "StatusReason": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "PercentageComplete": int,
        "InstancesToUpdate": int,
        "ProgressDetails": "InstanceRefreshProgressDetailsTypeDef",
    },
    total=False,
)

InstanceRefreshWarmPoolProgressTypeDef = TypedDict(
    "InstanceRefreshWarmPoolProgressTypeDef",
    {
        "PercentageComplete": int,
        "InstancesToUpdate": int,
    },
    total=False,
)

_RequiredInstanceTypeDef = TypedDict(
    "_RequiredInstanceTypeDef",
    {
        "InstanceId": str,
        "AvailabilityZone": str,
        "LifecycleState": LifecycleStateType,
        "HealthStatus": str,
        "ProtectedFromScaleIn": bool,
    },
)
_OptionalInstanceTypeDef = TypedDict(
    "_OptionalInstanceTypeDef",
    {
        "InstanceType": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": "LaunchTemplateSpecificationTypeDef",
        "WeightedCapacity": str,
    },
    total=False,
)

class InstanceTypeDef(_RequiredInstanceTypeDef, _OptionalInstanceTypeDef):
    pass

InstancesDistributionTypeDef = TypedDict(
    "InstancesDistributionTypeDef",
    {
        "OnDemandAllocationStrategy": str,
        "OnDemandBaseCapacity": int,
        "OnDemandPercentageAboveBaseCapacity": int,
        "SpotAllocationStrategy": str,
        "SpotInstancePools": int,
        "SpotMaxPrice": str,
    },
    total=False,
)

LaunchConfigurationNameTypeRequestTypeDef = TypedDict(
    "LaunchConfigurationNameTypeRequestTypeDef",
    {
        "LaunchConfigurationName": str,
    },
)

LaunchConfigurationNamesTypeRequestTypeDef = TypedDict(
    "LaunchConfigurationNamesTypeRequestTypeDef",
    {
        "LaunchConfigurationNames": List[str],
        "NextToken": str,
        "MaxRecords": int,
    },
    total=False,
)

_RequiredLaunchConfigurationTypeDef = TypedDict(
    "_RequiredLaunchConfigurationTypeDef",
    {
        "LaunchConfigurationName": str,
        "ImageId": str,
        "InstanceType": str,
        "CreatedTime": datetime,
    },
)
_OptionalLaunchConfigurationTypeDef = TypedDict(
    "_OptionalLaunchConfigurationTypeDef",
    {
        "LaunchConfigurationARN": str,
        "KeyName": str,
        "SecurityGroups": List[str],
        "ClassicLinkVPCId": str,
        "ClassicLinkVPCSecurityGroups": List[str],
        "UserData": str,
        "KernelId": str,
        "RamdiskId": str,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "InstanceMonitoring": "InstanceMonitoringTypeDef",
        "SpotPrice": str,
        "IamInstanceProfile": str,
        "EbsOptimized": bool,
        "AssociatePublicIpAddress": bool,
        "PlacementTenancy": str,
        "MetadataOptions": "InstanceMetadataOptionsTypeDef",
    },
    total=False,
)

class LaunchConfigurationTypeDef(
    _RequiredLaunchConfigurationTypeDef, _OptionalLaunchConfigurationTypeDef
):
    pass

LaunchConfigurationsTypeTypeDef = TypedDict(
    "LaunchConfigurationsTypeTypeDef",
    {
        "LaunchConfigurations": List["LaunchConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LaunchTemplateOverridesTypeDef = TypedDict(
    "LaunchTemplateOverridesTypeDef",
    {
        "InstanceType": str,
        "WeightedCapacity": str,
        "LaunchTemplateSpecification": "LaunchTemplateSpecificationTypeDef",
    },
    total=False,
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "Version": str,
    },
    total=False,
)

LaunchTemplateTypeDef = TypedDict(
    "LaunchTemplateTypeDef",
    {
        "LaunchTemplateSpecification": "LaunchTemplateSpecificationTypeDef",
        "Overrides": List["LaunchTemplateOverridesTypeDef"],
    },
    total=False,
)

_RequiredLifecycleHookSpecificationTypeDef = TypedDict(
    "_RequiredLifecycleHookSpecificationTypeDef",
    {
        "LifecycleHookName": str,
        "LifecycleTransition": str,
    },
)
_OptionalLifecycleHookSpecificationTypeDef = TypedDict(
    "_OptionalLifecycleHookSpecificationTypeDef",
    {
        "NotificationMetadata": str,
        "HeartbeatTimeout": int,
        "DefaultResult": str,
        "NotificationTargetARN": str,
        "RoleARN": str,
    },
    total=False,
)

class LifecycleHookSpecificationTypeDef(
    _RequiredLifecycleHookSpecificationTypeDef, _OptionalLifecycleHookSpecificationTypeDef
):
    pass

LifecycleHookTypeDef = TypedDict(
    "LifecycleHookTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
        "LifecycleTransition": str,
        "NotificationTargetARN": str,
        "RoleARN": str,
        "NotificationMetadata": str,
        "HeartbeatTimeout": int,
        "GlobalTimeout": int,
        "DefaultResult": str,
    },
    total=False,
)

LoadBalancerStateTypeDef = TypedDict(
    "LoadBalancerStateTypeDef",
    {
        "LoadBalancerName": str,
        "State": str,
    },
    total=False,
)

LoadBalancerTargetGroupStateTypeDef = TypedDict(
    "LoadBalancerTargetGroupStateTypeDef",
    {
        "LoadBalancerTargetGroupARN": str,
        "State": str,
    },
    total=False,
)

LoadForecastTypeDef = TypedDict(
    "LoadForecastTypeDef",
    {
        "Timestamps": List[datetime],
        "Values": List[float],
        "MetricSpecification": "PredictiveScalingMetricSpecificationTypeDef",
    },
)

MetricCollectionTypeTypeDef = TypedDict(
    "MetricCollectionTypeTypeDef",
    {
        "Metric": str,
    },
    total=False,
)

MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

MetricGranularityTypeTypeDef = TypedDict(
    "MetricGranularityTypeTypeDef",
    {
        "Granularity": str,
    },
    total=False,
)

MixedInstancesPolicyTypeDef = TypedDict(
    "MixedInstancesPolicyTypeDef",
    {
        "LaunchTemplate": "LaunchTemplateTypeDef",
        "InstancesDistribution": "InstancesDistributionTypeDef",
    },
    total=False,
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "AutoScalingGroupName": str,
        "TopicARN": str,
        "NotificationType": str,
    },
    total=False,
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

PoliciesTypeTypeDef = TypedDict(
    "PoliciesTypeTypeDef",
    {
        "ScalingPolicies": List["ScalingPolicyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PolicyARNTypeTypeDef = TypedDict(
    "PolicyARNTypeTypeDef",
    {
        "PolicyARN": str,
        "Alarms": List["AlarmTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredPredictiveScalingConfigurationTypeDef = TypedDict(
    "_RequiredPredictiveScalingConfigurationTypeDef",
    {
        "MetricSpecifications": List["PredictiveScalingMetricSpecificationTypeDef"],
    },
)
_OptionalPredictiveScalingConfigurationTypeDef = TypedDict(
    "_OptionalPredictiveScalingConfigurationTypeDef",
    {
        "Mode": PredictiveScalingModeType,
        "SchedulingBufferTime": int,
        "MaxCapacityBreachBehavior": PredictiveScalingMaxCapacityBreachBehaviorType,
        "MaxCapacityBuffer": int,
    },
    total=False,
)

class PredictiveScalingConfigurationTypeDef(
    _RequiredPredictiveScalingConfigurationTypeDef, _OptionalPredictiveScalingConfigurationTypeDef
):
    pass

_RequiredPredictiveScalingMetricSpecificationTypeDef = TypedDict(
    "_RequiredPredictiveScalingMetricSpecificationTypeDef",
    {
        "TargetValue": float,
    },
)
_OptionalPredictiveScalingMetricSpecificationTypeDef = TypedDict(
    "_OptionalPredictiveScalingMetricSpecificationTypeDef",
    {
        "PredefinedMetricPairSpecification": "PredictiveScalingPredefinedMetricPairTypeDef",
        "PredefinedScalingMetricSpecification": "PredictiveScalingPredefinedScalingMetricTypeDef",
        "PredefinedLoadMetricSpecification": "PredictiveScalingPredefinedLoadMetricTypeDef",
    },
    total=False,
)

class PredictiveScalingMetricSpecificationTypeDef(
    _RequiredPredictiveScalingMetricSpecificationTypeDef,
    _OptionalPredictiveScalingMetricSpecificationTypeDef,
):
    pass

_RequiredPredictiveScalingPredefinedLoadMetricTypeDef = TypedDict(
    "_RequiredPredictiveScalingPredefinedLoadMetricTypeDef",
    {
        "PredefinedMetricType": PredefinedLoadMetricTypeType,
    },
)
_OptionalPredictiveScalingPredefinedLoadMetricTypeDef = TypedDict(
    "_OptionalPredictiveScalingPredefinedLoadMetricTypeDef",
    {
        "ResourceLabel": str,
    },
    total=False,
)

class PredictiveScalingPredefinedLoadMetricTypeDef(
    _RequiredPredictiveScalingPredefinedLoadMetricTypeDef,
    _OptionalPredictiveScalingPredefinedLoadMetricTypeDef,
):
    pass

_RequiredPredictiveScalingPredefinedMetricPairTypeDef = TypedDict(
    "_RequiredPredictiveScalingPredefinedMetricPairTypeDef",
    {
        "PredefinedMetricType": PredefinedMetricPairTypeType,
    },
)
_OptionalPredictiveScalingPredefinedMetricPairTypeDef = TypedDict(
    "_OptionalPredictiveScalingPredefinedMetricPairTypeDef",
    {
        "ResourceLabel": str,
    },
    total=False,
)

class PredictiveScalingPredefinedMetricPairTypeDef(
    _RequiredPredictiveScalingPredefinedMetricPairTypeDef,
    _OptionalPredictiveScalingPredefinedMetricPairTypeDef,
):
    pass

_RequiredPredictiveScalingPredefinedScalingMetricTypeDef = TypedDict(
    "_RequiredPredictiveScalingPredefinedScalingMetricTypeDef",
    {
        "PredefinedMetricType": PredefinedScalingMetricTypeType,
    },
)
_OptionalPredictiveScalingPredefinedScalingMetricTypeDef = TypedDict(
    "_OptionalPredictiveScalingPredefinedScalingMetricTypeDef",
    {
        "ResourceLabel": str,
    },
    total=False,
)

class PredictiveScalingPredefinedScalingMetricTypeDef(
    _RequiredPredictiveScalingPredefinedScalingMetricTypeDef,
    _OptionalPredictiveScalingPredefinedScalingMetricTypeDef,
):
    pass

ProcessTypeTypeDef = TypedDict(
    "ProcessTypeTypeDef",
    {
        "ProcessName": str,
    },
)

ProcessesTypeTypeDef = TypedDict(
    "ProcessesTypeTypeDef",
    {
        "Processes": List["ProcessTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutLifecycleHookTypeRequestTypeDef = TypedDict(
    "_RequiredPutLifecycleHookTypeRequestTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
    },
)
_OptionalPutLifecycleHookTypeRequestTypeDef = TypedDict(
    "_OptionalPutLifecycleHookTypeRequestTypeDef",
    {
        "LifecycleTransition": str,
        "RoleARN": str,
        "NotificationTargetARN": str,
        "NotificationMetadata": str,
        "HeartbeatTimeout": int,
        "DefaultResult": str,
    },
    total=False,
)

class PutLifecycleHookTypeRequestTypeDef(
    _RequiredPutLifecycleHookTypeRequestTypeDef, _OptionalPutLifecycleHookTypeRequestTypeDef
):
    pass

PutNotificationConfigurationTypeRequestTypeDef = TypedDict(
    "PutNotificationConfigurationTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "TopicARN": str,
        "NotificationTypes": List[str],
    },
)

_RequiredPutScalingPolicyTypeRequestTypeDef = TypedDict(
    "_RequiredPutScalingPolicyTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "PolicyName": str,
    },
)
_OptionalPutScalingPolicyTypeRequestTypeDef = TypedDict(
    "_OptionalPutScalingPolicyTypeRequestTypeDef",
    {
        "PolicyType": str,
        "AdjustmentType": str,
        "MinAdjustmentStep": int,
        "MinAdjustmentMagnitude": int,
        "ScalingAdjustment": int,
        "Cooldown": int,
        "MetricAggregationType": str,
        "StepAdjustments": List["StepAdjustmentTypeDef"],
        "EstimatedInstanceWarmup": int,
        "TargetTrackingConfiguration": "TargetTrackingConfigurationTypeDef",
        "Enabled": bool,
        "PredictiveScalingConfiguration": "PredictiveScalingConfigurationTypeDef",
    },
    total=False,
)

class PutScalingPolicyTypeRequestTypeDef(
    _RequiredPutScalingPolicyTypeRequestTypeDef, _OptionalPutScalingPolicyTypeRequestTypeDef
):
    pass

_RequiredPutScheduledUpdateGroupActionTypeRequestTypeDef = TypedDict(
    "_RequiredPutScheduledUpdateGroupActionTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionName": str,
    },
)
_OptionalPutScheduledUpdateGroupActionTypeRequestTypeDef = TypedDict(
    "_OptionalPutScheduledUpdateGroupActionTypeRequestTypeDef",
    {
        "Time": Union[datetime, str],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Recurrence": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
        "TimeZone": str,
    },
    total=False,
)

class PutScheduledUpdateGroupActionTypeRequestTypeDef(
    _RequiredPutScheduledUpdateGroupActionTypeRequestTypeDef,
    _OptionalPutScheduledUpdateGroupActionTypeRequestTypeDef,
):
    pass

_RequiredPutWarmPoolTypeRequestTypeDef = TypedDict(
    "_RequiredPutWarmPoolTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalPutWarmPoolTypeRequestTypeDef = TypedDict(
    "_OptionalPutWarmPoolTypeRequestTypeDef",
    {
        "MaxGroupPreparedCapacity": int,
        "MinSize": int,
        "PoolState": WarmPoolStateType,
    },
    total=False,
)

class PutWarmPoolTypeRequestTypeDef(
    _RequiredPutWarmPoolTypeRequestTypeDef, _OptionalPutWarmPoolTypeRequestTypeDef
):
    pass

_RequiredRecordLifecycleActionHeartbeatTypeRequestTypeDef = TypedDict(
    "_RequiredRecordLifecycleActionHeartbeatTypeRequestTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
    },
)
_OptionalRecordLifecycleActionHeartbeatTypeRequestTypeDef = TypedDict(
    "_OptionalRecordLifecycleActionHeartbeatTypeRequestTypeDef",
    {
        "LifecycleActionToken": str,
        "InstanceId": str,
    },
    total=False,
)

class RecordLifecycleActionHeartbeatTypeRequestTypeDef(
    _RequiredRecordLifecycleActionHeartbeatTypeRequestTypeDef,
    _OptionalRecordLifecycleActionHeartbeatTypeRequestTypeDef,
):
    pass

RefreshPreferencesTypeDef = TypedDict(
    "RefreshPreferencesTypeDef",
    {
        "MinHealthyPercentage": int,
        "InstanceWarmup": int,
        "CheckpointPercentages": List[int],
        "CheckpointDelay": int,
    },
    total=False,
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

ScalingPolicyTypeDef = TypedDict(
    "ScalingPolicyTypeDef",
    {
        "AutoScalingGroupName": str,
        "PolicyName": str,
        "PolicyARN": str,
        "PolicyType": str,
        "AdjustmentType": str,
        "MinAdjustmentStep": int,
        "MinAdjustmentMagnitude": int,
        "ScalingAdjustment": int,
        "Cooldown": int,
        "StepAdjustments": List["StepAdjustmentTypeDef"],
        "MetricAggregationType": str,
        "EstimatedInstanceWarmup": int,
        "Alarms": List["AlarmTypeDef"],
        "TargetTrackingConfiguration": "TargetTrackingConfigurationTypeDef",
        "Enabled": bool,
        "PredictiveScalingConfiguration": "PredictiveScalingConfigurationTypeDef",
    },
    total=False,
)

_RequiredScalingProcessQueryRequestTypeDef = TypedDict(
    "_RequiredScalingProcessQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalScalingProcessQueryRequestTypeDef = TypedDict(
    "_OptionalScalingProcessQueryRequestTypeDef",
    {
        "ScalingProcesses": List[str],
    },
    total=False,
)

class ScalingProcessQueryRequestTypeDef(
    _RequiredScalingProcessQueryRequestTypeDef, _OptionalScalingProcessQueryRequestTypeDef
):
    pass

ScheduledActionsTypeTypeDef = TypedDict(
    "ScheduledActionsTypeTypeDef",
    {
        "ScheduledUpdateGroupActions": List["ScheduledUpdateGroupActionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredScheduledUpdateGroupActionRequestTypeDef = TypedDict(
    "_RequiredScheduledUpdateGroupActionRequestTypeDef",
    {
        "ScheduledActionName": str,
    },
)
_OptionalScheduledUpdateGroupActionRequestTypeDef = TypedDict(
    "_OptionalScheduledUpdateGroupActionRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Recurrence": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
        "TimeZone": str,
    },
    total=False,
)

class ScheduledUpdateGroupActionRequestTypeDef(
    _RequiredScheduledUpdateGroupActionRequestTypeDef,
    _OptionalScheduledUpdateGroupActionRequestTypeDef,
):
    pass

ScheduledUpdateGroupActionTypeDef = TypedDict(
    "ScheduledUpdateGroupActionTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionName": str,
        "ScheduledActionARN": str,
        "Time": datetime,
        "StartTime": datetime,
        "EndTime": datetime,
        "Recurrence": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
        "TimeZone": str,
    },
    total=False,
)

_RequiredSetDesiredCapacityTypeRequestTypeDef = TypedDict(
    "_RequiredSetDesiredCapacityTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "DesiredCapacity": int,
    },
)
_OptionalSetDesiredCapacityTypeRequestTypeDef = TypedDict(
    "_OptionalSetDesiredCapacityTypeRequestTypeDef",
    {
        "HonorCooldown": bool,
    },
    total=False,
)

class SetDesiredCapacityTypeRequestTypeDef(
    _RequiredSetDesiredCapacityTypeRequestTypeDef, _OptionalSetDesiredCapacityTypeRequestTypeDef
):
    pass

_RequiredSetInstanceHealthQueryRequestTypeDef = TypedDict(
    "_RequiredSetInstanceHealthQueryRequestTypeDef",
    {
        "InstanceId": str,
        "HealthStatus": str,
    },
)
_OptionalSetInstanceHealthQueryRequestTypeDef = TypedDict(
    "_OptionalSetInstanceHealthQueryRequestTypeDef",
    {
        "ShouldRespectGracePeriod": bool,
    },
    total=False,
)

class SetInstanceHealthQueryRequestTypeDef(
    _RequiredSetInstanceHealthQueryRequestTypeDef, _OptionalSetInstanceHealthQueryRequestTypeDef
):
    pass

SetInstanceProtectionQueryRequestTypeDef = TypedDict(
    "SetInstanceProtectionQueryRequestTypeDef",
    {
        "InstanceIds": List[str],
        "AutoScalingGroupName": str,
        "ProtectedFromScaleIn": bool,
    },
)

StartInstanceRefreshAnswerTypeDef = TypedDict(
    "StartInstanceRefreshAnswerTypeDef",
    {
        "InstanceRefreshId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartInstanceRefreshTypeRequestTypeDef = TypedDict(
    "_RequiredStartInstanceRefreshTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalStartInstanceRefreshTypeRequestTypeDef = TypedDict(
    "_OptionalStartInstanceRefreshTypeRequestTypeDef",
    {
        "Strategy": Literal["Rolling"],
        "Preferences": "RefreshPreferencesTypeDef",
    },
    total=False,
)

class StartInstanceRefreshTypeRequestTypeDef(
    _RequiredStartInstanceRefreshTypeRequestTypeDef, _OptionalStartInstanceRefreshTypeRequestTypeDef
):
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

SuspendedProcessTypeDef = TypedDict(
    "SuspendedProcessTypeDef",
    {
        "ProcessName": str,
        "SuspensionReason": str,
    },
    total=False,
)

TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef",
    {
        "ResourceId": str,
        "ResourceType": str,
        "Key": str,
        "Value": str,
        "PropagateAtLaunch": bool,
    },
    total=False,
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
        "ResourceId": str,
        "ResourceType": str,
        "Value": str,
        "PropagateAtLaunch": bool,
    },
    total=False,
)

class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass

TagsTypeTypeDef = TypedDict(
    "TagsTypeTypeDef",
    {
        "Tags": List["TagDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "PredefinedMetricSpecification": "PredefinedMetricSpecificationTypeDef",
        "CustomizedMetricSpecification": "CustomizedMetricSpecificationTypeDef",
        "DisableScaleIn": bool,
    },
    total=False,
)

class TargetTrackingConfigurationTypeDef(
    _RequiredTargetTrackingConfigurationTypeDef, _OptionalTargetTrackingConfigurationTypeDef
):
    pass

TerminateInstanceInAutoScalingGroupTypeRequestTypeDef = TypedDict(
    "TerminateInstanceInAutoScalingGroupTypeRequestTypeDef",
    {
        "InstanceId": str,
        "ShouldDecrementDesiredCapacity": bool,
    },
)

_RequiredUpdateAutoScalingGroupTypeRequestTypeDef = TypedDict(
    "_RequiredUpdateAutoScalingGroupTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalUpdateAutoScalingGroupTypeRequestTypeDef = TypedDict(
    "_OptionalUpdateAutoScalingGroupTypeRequestTypeDef",
    {
        "LaunchConfigurationName": str,
        "LaunchTemplate": "LaunchTemplateSpecificationTypeDef",
        "MixedInstancesPolicy": "MixedInstancesPolicyTypeDef",
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
        "DefaultCooldown": int,
        "AvailabilityZones": List[str],
        "HealthCheckType": str,
        "HealthCheckGracePeriod": int,
        "PlacementGroup": str,
        "VPCZoneIdentifier": str,
        "TerminationPolicies": List[str],
        "NewInstancesProtectedFromScaleIn": bool,
        "ServiceLinkedRoleARN": str,
        "MaxInstanceLifetime": int,
        "CapacityRebalance": bool,
        "Context": str,
    },
    total=False,
)

class UpdateAutoScalingGroupTypeRequestTypeDef(
    _RequiredUpdateAutoScalingGroupTypeRequestTypeDef,
    _OptionalUpdateAutoScalingGroupTypeRequestTypeDef,
):
    pass

WarmPoolConfigurationTypeDef = TypedDict(
    "WarmPoolConfigurationTypeDef",
    {
        "MaxGroupPreparedCapacity": int,
        "MinSize": int,
        "PoolState": WarmPoolStateType,
        "Status": Literal["PendingDelete"],
    },
    total=False,
)
