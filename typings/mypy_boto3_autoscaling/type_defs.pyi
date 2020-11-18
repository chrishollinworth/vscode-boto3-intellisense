"""
Main interface for autoscaling service type definitions.

Usage::

    ```python
    from mypy_boto3_autoscaling.type_defs import ActivityTypeDef

    data: ActivityTypeDef = {...}
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
    "ActivityTypeDef",
    "AdjustmentTypeTypeDef",
    "AlarmTypeDef",
    "AutoScalingGroupTypeDef",
    "AutoScalingInstanceDetailsTypeDef",
    "BlockDeviceMappingTypeDef",
    "CustomizedMetricSpecificationTypeDef",
    "EbsTypeDef",
    "EnabledMetricTypeDef",
    "FailedScheduledUpdateGroupActionRequestTypeDef",
    "InstanceMetadataOptionsTypeDef",
    "InstanceMonitoringTypeDef",
    "InstanceRefreshTypeDef",
    "InstanceTypeDef",
    "InstancesDistributionTypeDef",
    "LaunchConfigurationTypeDef",
    "LaunchTemplateOverridesTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "LaunchTemplateTypeDef",
    "LifecycleHookTypeDef",
    "LoadBalancerStateTypeDef",
    "LoadBalancerTargetGroupStateTypeDef",
    "MetricCollectionTypeTypeDef",
    "MetricDimensionTypeDef",
    "MetricGranularityTypeTypeDef",
    "MixedInstancesPolicyTypeDef",
    "NotificationConfigurationTypeDef",
    "PredefinedMetricSpecificationTypeDef",
    "ProcessTypeTypeDef",
    "ScalingPolicyTypeDef",
    "ScheduledUpdateGroupActionTypeDef",
    "StepAdjustmentTypeDef",
    "SuspendedProcessTypeDef",
    "TagDescriptionTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "ActivitiesTypeTypeDef",
    "ActivityTypeTypeDef",
    "AutoScalingGroupsTypeTypeDef",
    "AutoScalingInstancesTypeTypeDef",
    "BatchDeleteScheduledActionAnswerTypeDef",
    "BatchPutScheduledUpdateGroupActionAnswerTypeDef",
    "CancelInstanceRefreshAnswerTypeDef",
    "DescribeAccountLimitsAnswerTypeDef",
    "DescribeAdjustmentTypesAnswerTypeDef",
    "DescribeAutoScalingNotificationTypesAnswerTypeDef",
    "DescribeInstanceRefreshesAnswerTypeDef",
    "DescribeLifecycleHookTypesAnswerTypeDef",
    "DescribeLifecycleHooksAnswerTypeDef",
    "DescribeLoadBalancerTargetGroupsResponseTypeDef",
    "DescribeLoadBalancersResponseTypeDef",
    "DescribeMetricCollectionTypesAnswerTypeDef",
    "DescribeNotificationConfigurationsAnswerTypeDef",
    "DescribeTerminationPolicyTypesAnswerTypeDef",
    "DetachInstancesAnswerTypeDef",
    "EnterStandbyAnswerTypeDef",
    "ExitStandbyAnswerTypeDef",
    "FilterTypeDef",
    "LaunchConfigurationsTypeTypeDef",
    "LifecycleHookSpecificationTypeDef",
    "PaginatorConfigTypeDef",
    "PoliciesTypeTypeDef",
    "PolicyARNTypeTypeDef",
    "ProcessesTypeTypeDef",
    "RefreshPreferencesTypeDef",
    "ScheduledActionsTypeTypeDef",
    "ScheduledUpdateGroupActionRequestTypeDef",
    "StartInstanceRefreshAnswerTypeDef",
    "TagTypeDef",
    "TagsTypeTypeDef",
)

_RequiredActivityTypeDef = TypedDict(
    "_RequiredActivityTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Cause": str,
        "StartTime": datetime,
        "StatusCode": Literal[
            "PendingSpotBidPlacement",
            "WaitingForSpotInstanceRequestId",
            "WaitingForSpotInstanceId",
            "WaitingForInstanceId",
            "PreInService",
            "InProgress",
            "WaitingForELBConnectionDraining",
            "MidLifecycleAction",
            "WaitingForInstanceWarmup",
            "Successful",
            "Failed",
            "Cancelled",
        ],
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
    },
    total=False,
)


class ActivityTypeDef(_RequiredActivityTypeDef, _OptionalActivityTypeDef):
    pass


AdjustmentTypeTypeDef = TypedDict("AdjustmentTypeTypeDef", {"AdjustmentType": str}, total=False)

AlarmTypeDef = TypedDict("AlarmTypeDef", {"AlarmName": str, "AlarmARN": str}, total=False)

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
    },
    total=False,
)


class AutoScalingGroupTypeDef(_RequiredAutoScalingGroupTypeDef, _OptionalAutoScalingGroupTypeDef):
    pass


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


_RequiredBlockDeviceMappingTypeDef = TypedDict(
    "_RequiredBlockDeviceMappingTypeDef", {"DeviceName": str}
)
_OptionalBlockDeviceMappingTypeDef = TypedDict(
    "_OptionalBlockDeviceMappingTypeDef",
    {"VirtualName": str, "Ebs": "EbsTypeDef", "NoDevice": bool},
    total=False,
)


class BlockDeviceMappingTypeDef(
    _RequiredBlockDeviceMappingTypeDef, _OptionalBlockDeviceMappingTypeDef
):
    pass


_RequiredCustomizedMetricSpecificationTypeDef = TypedDict(
    "_RequiredCustomizedMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
    },
)
_OptionalCustomizedMetricSpecificationTypeDef = TypedDict(
    "_OptionalCustomizedMetricSpecificationTypeDef",
    {"Dimensions": List["MetricDimensionTypeDef"], "Unit": str},
    total=False,
)


class CustomizedMetricSpecificationTypeDef(
    _RequiredCustomizedMetricSpecificationTypeDef, _OptionalCustomizedMetricSpecificationTypeDef
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
    },
    total=False,
)

EnabledMetricTypeDef = TypedDict(
    "EnabledMetricTypeDef", {"Metric": str, "Granularity": str}, total=False
)

_RequiredFailedScheduledUpdateGroupActionRequestTypeDef = TypedDict(
    "_RequiredFailedScheduledUpdateGroupActionRequestTypeDef", {"ScheduledActionName": str}
)
_OptionalFailedScheduledUpdateGroupActionRequestTypeDef = TypedDict(
    "_OptionalFailedScheduledUpdateGroupActionRequestTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class FailedScheduledUpdateGroupActionRequestTypeDef(
    _RequiredFailedScheduledUpdateGroupActionRequestTypeDef,
    _OptionalFailedScheduledUpdateGroupActionRequestTypeDef,
):
    pass


InstanceMetadataOptionsTypeDef = TypedDict(
    "InstanceMetadataOptionsTypeDef",
    {
        "HttpTokens": Literal["optional", "required"],
        "HttpPutResponseHopLimit": int,
        "HttpEndpoint": Literal["disabled", "enabled"],
    },
    total=False,
)

InstanceMonitoringTypeDef = TypedDict("InstanceMonitoringTypeDef", {"Enabled": bool}, total=False)

InstanceRefreshTypeDef = TypedDict(
    "InstanceRefreshTypeDef",
    {
        "InstanceRefreshId": str,
        "AutoScalingGroupName": str,
        "Status": Literal[
            "Pending", "InProgress", "Successful", "Failed", "Cancelling", "Cancelled"
        ],
        "StatusReason": str,
        "StartTime": datetime,
        "EndTime": datetime,
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
        "LifecycleState": Literal[
            "Pending",
            "Pending:Wait",
            "Pending:Proceed",
            "Quarantined",
            "InService",
            "Terminating",
            "Terminating:Wait",
            "Terminating:Proceed",
            "Terminated",
            "Detaching",
            "Detached",
            "EnteringStandby",
            "Standby",
        ],
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

_RequiredLaunchConfigurationTypeDef = TypedDict(
    "_RequiredLaunchConfigurationTypeDef",
    {"LaunchConfigurationName": str, "ImageId": str, "InstanceType": str, "CreatedTime": datetime},
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


LaunchTemplateOverridesTypeDef = TypedDict(
    "LaunchTemplateOverridesTypeDef", {"InstanceType": str, "WeightedCapacity": str}, total=False
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
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
    "LoadBalancerStateTypeDef", {"LoadBalancerName": str, "State": str}, total=False
)

LoadBalancerTargetGroupStateTypeDef = TypedDict(
    "LoadBalancerTargetGroupStateTypeDef",
    {"LoadBalancerTargetGroupARN": str, "State": str},
    total=False,
)

MetricCollectionTypeTypeDef = TypedDict("MetricCollectionTypeTypeDef", {"Metric": str}, total=False)

MetricDimensionTypeDef = TypedDict("MetricDimensionTypeDef", {"Name": str, "Value": str})

MetricGranularityTypeTypeDef = TypedDict(
    "MetricGranularityTypeTypeDef", {"Granularity": str}, total=False
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
    {"AutoScalingGroupName": str, "TopicARN": str, "NotificationType": str},
    total=False,
)

_RequiredPredefinedMetricSpecificationTypeDef = TypedDict(
    "_RequiredPredefinedMetricSpecificationTypeDef",
    {
        "PredefinedMetricType": Literal[
            "ASGAverageCPUUtilization",
            "ASGAverageNetworkIn",
            "ASGAverageNetworkOut",
            "ALBRequestCountPerTarget",
        ]
    },
)
_OptionalPredefinedMetricSpecificationTypeDef = TypedDict(
    "_OptionalPredefinedMetricSpecificationTypeDef", {"ResourceLabel": str}, total=False
)


class PredefinedMetricSpecificationTypeDef(
    _RequiredPredefinedMetricSpecificationTypeDef, _OptionalPredefinedMetricSpecificationTypeDef
):
    pass


ProcessTypeTypeDef = TypedDict("ProcessTypeTypeDef", {"ProcessName": str})

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
    },
    total=False,
)

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
    },
    total=False,
)

_RequiredStepAdjustmentTypeDef = TypedDict(
    "_RequiredStepAdjustmentTypeDef", {"ScalingAdjustment": int}
)
_OptionalStepAdjustmentTypeDef = TypedDict(
    "_OptionalStepAdjustmentTypeDef",
    {"MetricIntervalLowerBound": float, "MetricIntervalUpperBound": float},
    total=False,
)


class StepAdjustmentTypeDef(_RequiredStepAdjustmentTypeDef, _OptionalStepAdjustmentTypeDef):
    pass


SuspendedProcessTypeDef = TypedDict(
    "SuspendedProcessTypeDef", {"ProcessName": str, "SuspensionReason": str}, total=False
)

TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)

_RequiredTargetTrackingConfigurationTypeDef = TypedDict(
    "_RequiredTargetTrackingConfigurationTypeDef", {"TargetValue": float}
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


_RequiredActivitiesTypeTypeDef = TypedDict(
    "_RequiredActivitiesTypeTypeDef", {"Activities": List["ActivityTypeDef"]}
)
_OptionalActivitiesTypeTypeDef = TypedDict(
    "_OptionalActivitiesTypeTypeDef", {"NextToken": str}, total=False
)


class ActivitiesTypeTypeDef(_RequiredActivitiesTypeTypeDef, _OptionalActivitiesTypeTypeDef):
    pass


ActivityTypeTypeDef = TypedDict("ActivityTypeTypeDef", {"Activity": "ActivityTypeDef"}, total=False)

_RequiredAutoScalingGroupsTypeTypeDef = TypedDict(
    "_RequiredAutoScalingGroupsTypeTypeDef", {"AutoScalingGroups": List["AutoScalingGroupTypeDef"]}
)
_OptionalAutoScalingGroupsTypeTypeDef = TypedDict(
    "_OptionalAutoScalingGroupsTypeTypeDef", {"NextToken": str}, total=False
)


class AutoScalingGroupsTypeTypeDef(
    _RequiredAutoScalingGroupsTypeTypeDef, _OptionalAutoScalingGroupsTypeTypeDef
):
    pass


AutoScalingInstancesTypeTypeDef = TypedDict(
    "AutoScalingInstancesTypeTypeDef",
    {"AutoScalingInstances": List["AutoScalingInstanceDetailsTypeDef"], "NextToken": str},
    total=False,
)

BatchDeleteScheduledActionAnswerTypeDef = TypedDict(
    "BatchDeleteScheduledActionAnswerTypeDef",
    {"FailedScheduledActions": List["FailedScheduledUpdateGroupActionRequestTypeDef"]},
    total=False,
)

BatchPutScheduledUpdateGroupActionAnswerTypeDef = TypedDict(
    "BatchPutScheduledUpdateGroupActionAnswerTypeDef",
    {"FailedScheduledUpdateGroupActions": List["FailedScheduledUpdateGroupActionRequestTypeDef"]},
    total=False,
)

CancelInstanceRefreshAnswerTypeDef = TypedDict(
    "CancelInstanceRefreshAnswerTypeDef", {"InstanceRefreshId": str}, total=False
)

DescribeAccountLimitsAnswerTypeDef = TypedDict(
    "DescribeAccountLimitsAnswerTypeDef",
    {
        "MaxNumberOfAutoScalingGroups": int,
        "MaxNumberOfLaunchConfigurations": int,
        "NumberOfAutoScalingGroups": int,
        "NumberOfLaunchConfigurations": int,
    },
    total=False,
)

DescribeAdjustmentTypesAnswerTypeDef = TypedDict(
    "DescribeAdjustmentTypesAnswerTypeDef",
    {"AdjustmentTypes": List["AdjustmentTypeTypeDef"]},
    total=False,
)

DescribeAutoScalingNotificationTypesAnswerTypeDef = TypedDict(
    "DescribeAutoScalingNotificationTypesAnswerTypeDef",
    {"AutoScalingNotificationTypes": List[str]},
    total=False,
)

DescribeInstanceRefreshesAnswerTypeDef = TypedDict(
    "DescribeInstanceRefreshesAnswerTypeDef",
    {"InstanceRefreshes": List["InstanceRefreshTypeDef"], "NextToken": str},
    total=False,
)

DescribeLifecycleHookTypesAnswerTypeDef = TypedDict(
    "DescribeLifecycleHookTypesAnswerTypeDef", {"LifecycleHookTypes": List[str]}, total=False
)

DescribeLifecycleHooksAnswerTypeDef = TypedDict(
    "DescribeLifecycleHooksAnswerTypeDef",
    {"LifecycleHooks": List["LifecycleHookTypeDef"]},
    total=False,
)

DescribeLoadBalancerTargetGroupsResponseTypeDef = TypedDict(
    "DescribeLoadBalancerTargetGroupsResponseTypeDef",
    {"LoadBalancerTargetGroups": List["LoadBalancerTargetGroupStateTypeDef"], "NextToken": str},
    total=False,
)

DescribeLoadBalancersResponseTypeDef = TypedDict(
    "DescribeLoadBalancersResponseTypeDef",
    {"LoadBalancers": List["LoadBalancerStateTypeDef"], "NextToken": str},
    total=False,
)

DescribeMetricCollectionTypesAnswerTypeDef = TypedDict(
    "DescribeMetricCollectionTypesAnswerTypeDef",
    {
        "Metrics": List["MetricCollectionTypeTypeDef"],
        "Granularities": List["MetricGranularityTypeTypeDef"],
    },
    total=False,
)

_RequiredDescribeNotificationConfigurationsAnswerTypeDef = TypedDict(
    "_RequiredDescribeNotificationConfigurationsAnswerTypeDef",
    {"NotificationConfigurations": List["NotificationConfigurationTypeDef"]},
)
_OptionalDescribeNotificationConfigurationsAnswerTypeDef = TypedDict(
    "_OptionalDescribeNotificationConfigurationsAnswerTypeDef", {"NextToken": str}, total=False
)


class DescribeNotificationConfigurationsAnswerTypeDef(
    _RequiredDescribeNotificationConfigurationsAnswerTypeDef,
    _OptionalDescribeNotificationConfigurationsAnswerTypeDef,
):
    pass


DescribeTerminationPolicyTypesAnswerTypeDef = TypedDict(
    "DescribeTerminationPolicyTypesAnswerTypeDef",
    {"TerminationPolicyTypes": List[str]},
    total=False,
)

DetachInstancesAnswerTypeDef = TypedDict(
    "DetachInstancesAnswerTypeDef", {"Activities": List["ActivityTypeDef"]}, total=False
)

EnterStandbyAnswerTypeDef = TypedDict(
    "EnterStandbyAnswerTypeDef", {"Activities": List["ActivityTypeDef"]}, total=False
)

ExitStandbyAnswerTypeDef = TypedDict(
    "ExitStandbyAnswerTypeDef", {"Activities": List["ActivityTypeDef"]}, total=False
)

FilterTypeDef = TypedDict("FilterTypeDef", {"Name": str, "Values": List[str]}, total=False)

_RequiredLaunchConfigurationsTypeTypeDef = TypedDict(
    "_RequiredLaunchConfigurationsTypeTypeDef",
    {"LaunchConfigurations": List["LaunchConfigurationTypeDef"]},
)
_OptionalLaunchConfigurationsTypeTypeDef = TypedDict(
    "_OptionalLaunchConfigurationsTypeTypeDef", {"NextToken": str}, total=False
)


class LaunchConfigurationsTypeTypeDef(
    _RequiredLaunchConfigurationsTypeTypeDef, _OptionalLaunchConfigurationsTypeTypeDef
):
    pass


_RequiredLifecycleHookSpecificationTypeDef = TypedDict(
    "_RequiredLifecycleHookSpecificationTypeDef",
    {"LifecycleHookName": str, "LifecycleTransition": str},
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


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PoliciesTypeTypeDef = TypedDict(
    "PoliciesTypeTypeDef",
    {"ScalingPolicies": List["ScalingPolicyTypeDef"], "NextToken": str},
    total=False,
)

PolicyARNTypeTypeDef = TypedDict(
    "PolicyARNTypeTypeDef", {"PolicyARN": str, "Alarms": List["AlarmTypeDef"]}, total=False
)

ProcessesTypeTypeDef = TypedDict(
    "ProcessesTypeTypeDef", {"Processes": List["ProcessTypeTypeDef"]}, total=False
)

RefreshPreferencesTypeDef = TypedDict(
    "RefreshPreferencesTypeDef", {"MinHealthyPercentage": int, "InstanceWarmup": int}, total=False
)

ScheduledActionsTypeTypeDef = TypedDict(
    "ScheduledActionsTypeTypeDef",
    {"ScheduledUpdateGroupActions": List["ScheduledUpdateGroupActionTypeDef"], "NextToken": str},
    total=False,
)

_RequiredScheduledUpdateGroupActionRequestTypeDef = TypedDict(
    "_RequiredScheduledUpdateGroupActionRequestTypeDef", {"ScheduledActionName": str}
)
_OptionalScheduledUpdateGroupActionRequestTypeDef = TypedDict(
    "_OptionalScheduledUpdateGroupActionRequestTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "Recurrence": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
    },
    total=False,
)


class ScheduledUpdateGroupActionRequestTypeDef(
    _RequiredScheduledUpdateGroupActionRequestTypeDef,
    _OptionalScheduledUpdateGroupActionRequestTypeDef,
):
    pass


StartInstanceRefreshAnswerTypeDef = TypedDict(
    "StartInstanceRefreshAnswerTypeDef", {"InstanceRefreshId": str}, total=False
)

_RequiredTagTypeDef = TypedDict("_RequiredTagTypeDef", {"Key": str})
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {"ResourceId": str, "ResourceType": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


TagsTypeTypeDef = TypedDict(
    "TagsTypeTypeDef", {"Tags": List["TagDescriptionTypeDef"], "NextToken": str}, total=False
)
