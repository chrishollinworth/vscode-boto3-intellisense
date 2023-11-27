"""
Type annotations for autoscaling service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_autoscaling import AutoScalingClient

    client: AutoScalingClient = boto3.client("autoscaling")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import WarmPoolStateType
from .paginator import (
    DescribeAutoScalingGroupsPaginator,
    DescribeAutoScalingInstancesPaginator,
    DescribeLaunchConfigurationsPaginator,
    DescribeLoadBalancersPaginator,
    DescribeLoadBalancerTargetGroupsPaginator,
    DescribeNotificationConfigurationsPaginator,
    DescribePoliciesPaginator,
    DescribeScalingActivitiesPaginator,
    DescribeScheduledActionsPaginator,
    DescribeTagsPaginator,
    DescribeWarmPoolPaginator,
)
from .type_defs import (
    ActivitiesTypeTypeDef,
    ActivityTypeTypeDef,
    AutoScalingGroupsTypeTypeDef,
    AutoScalingInstancesTypeTypeDef,
    BatchDeleteScheduledActionAnswerTypeDef,
    BatchPutScheduledUpdateGroupActionAnswerTypeDef,
    BlockDeviceMappingTypeDef,
    CancelInstanceRefreshAnswerTypeDef,
    DescribeAccountLimitsAnswerTypeDef,
    DescribeAdjustmentTypesAnswerTypeDef,
    DescribeAutoScalingNotificationTypesAnswerTypeDef,
    DescribeInstanceRefreshesAnswerTypeDef,
    DescribeLifecycleHooksAnswerTypeDef,
    DescribeLifecycleHookTypesAnswerTypeDef,
    DescribeLoadBalancersResponseTypeDef,
    DescribeLoadBalancerTargetGroupsResponseTypeDef,
    DescribeMetricCollectionTypesAnswerTypeDef,
    DescribeNotificationConfigurationsAnswerTypeDef,
    DescribeTerminationPolicyTypesAnswerTypeDef,
    DescribeTrafficSourcesResponseTypeDef,
    DescribeWarmPoolAnswerTypeDef,
    DesiredConfigurationTypeDef,
    DetachInstancesAnswerTypeDef,
    EnterStandbyAnswerTypeDef,
    ExitStandbyAnswerTypeDef,
    FilterTypeDef,
    GetPredictiveScalingForecastAnswerTypeDef,
    InstanceMaintenancePolicyTypeDef,
    InstanceMetadataOptionsTypeDef,
    InstanceMonitoringTypeDef,
    InstanceReusePolicyTypeDef,
    LaunchConfigurationsTypeTypeDef,
    LaunchTemplateSpecificationTypeDef,
    LifecycleHookSpecificationTypeDef,
    MixedInstancesPolicyTypeDef,
    PoliciesTypeTypeDef,
    PolicyARNTypeTypeDef,
    PredictiveScalingConfigurationTypeDef,
    ProcessesTypeTypeDef,
    RefreshPreferencesTypeDef,
    RollbackInstanceRefreshAnswerTypeDef,
    ScheduledActionsTypeTypeDef,
    ScheduledUpdateGroupActionRequestTypeDef,
    StartInstanceRefreshAnswerTypeDef,
    StepAdjustmentTypeDef,
    TagsTypeTypeDef,
    TagTypeDef,
    TargetTrackingConfigurationTypeDef,
    TrafficSourceIdentifierTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AutoScalingClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ActiveInstanceRefreshNotFoundFault: Type[BotocoreClientError]
    AlreadyExistsFault: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InstanceRefreshInProgressFault: Type[BotocoreClientError]
    InvalidNextToken: Type[BotocoreClientError]
    IrreversibleInstanceRefreshFault: Type[BotocoreClientError]
    LimitExceededFault: Type[BotocoreClientError]
    ResourceContentionFault: Type[BotocoreClientError]
    ResourceInUseFault: Type[BotocoreClientError]
    ScalingActivityInProgressFault: Type[BotocoreClientError]
    ServiceLinkedRoleFailure: Type[BotocoreClientError]

class AutoScalingClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AutoScalingClient exceptions.
        """
    def attach_instances(self, *, AutoScalingGroupName: str, InstanceIds: List[str] = None) -> None:
        """
        Attaches one or more EC2 instances to the specified Auto Scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.attach_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#attach_instances)
        """
    def attach_load_balancer_target_groups(
        self, *, AutoScalingGroupName: str, TargetGroupARNs: List[str]
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.attach_load_balancer_target_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#attach_load_balancer_target_groups)
        """
    def attach_load_balancers(
        self, *, AutoScalingGroupName: str, LoadBalancerNames: List[str]
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.attach_load_balancers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#attach_load_balancers)
        """
    def attach_traffic_sources(
        self, *, AutoScalingGroupName: str, TrafficSources: List["TrafficSourceIdentifierTypeDef"]
    ) -> Dict[str, Any]:
        """
        Attaches one or more traffic sources to the specified Auto Scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.attach_traffic_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#attach_traffic_sources)
        """
    def batch_delete_scheduled_action(
        self, *, AutoScalingGroupName: str, ScheduledActionNames: List[str]
    ) -> BatchDeleteScheduledActionAnswerTypeDef:
        """
        Deletes one or more scheduled actions for the specified Auto Scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.batch_delete_scheduled_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#batch_delete_scheduled_action)
        """
    def batch_put_scheduled_update_group_action(
        self,
        *,
        AutoScalingGroupName: str,
        ScheduledUpdateGroupActions: List["ScheduledUpdateGroupActionRequestTypeDef"]
    ) -> BatchPutScheduledUpdateGroupActionAnswerTypeDef:
        """
        Creates or updates one or more scheduled scaling actions for an Auto Scaling
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.batch_put_scheduled_update_group_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#batch_put_scheduled_update_group_action)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#can_paginate)
        """
    def cancel_instance_refresh(
        self, *, AutoScalingGroupName: str
    ) -> CancelInstanceRefreshAnswerTypeDef:
        """
        Cancels an instance refresh or rollback that is in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.cancel_instance_refresh)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#cancel_instance_refresh)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#close)
        """
    def complete_lifecycle_action(
        self,
        *,
        LifecycleHookName: str,
        AutoScalingGroupName: str,
        LifecycleActionResult: str,
        LifecycleActionToken: str = None,
        InstanceId: str = None
    ) -> Dict[str, Any]:
        """
        Completes the lifecycle action for the specified token or instance with the
        specified result.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.complete_lifecycle_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#complete_lifecycle_action)
        """
    def create_auto_scaling_group(
        self,
        *,
        AutoScalingGroupName: str,
        MinSize: int,
        MaxSize: int,
        LaunchConfigurationName: str = None,
        LaunchTemplate: "LaunchTemplateSpecificationTypeDef" = None,
        MixedInstancesPolicy: "MixedInstancesPolicyTypeDef" = None,
        InstanceId: str = None,
        DesiredCapacity: int = None,
        DefaultCooldown: int = None,
        AvailabilityZones: List[str] = None,
        LoadBalancerNames: List[str] = None,
        TargetGroupARNs: List[str] = None,
        HealthCheckType: str = None,
        HealthCheckGracePeriod: int = None,
        PlacementGroup: str = None,
        VPCZoneIdentifier: str = None,
        TerminationPolicies: List[str] = None,
        NewInstancesProtectedFromScaleIn: bool = None,
        CapacityRebalance: bool = None,
        LifecycleHookSpecificationList: List["LifecycleHookSpecificationTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        ServiceLinkedRoleARN: str = None,
        MaxInstanceLifetime: int = None,
        Context: str = None,
        DesiredCapacityType: str = None,
        DefaultInstanceWarmup: int = None,
        TrafficSources: List["TrafficSourceIdentifierTypeDef"] = None,
        InstanceMaintenancePolicy: "InstanceMaintenancePolicyTypeDef" = None
    ) -> None:
        """
        **We strongly recommend using a launch template when calling this operation to
        ensure full functionality for Amazon EC2 Auto Scaling and Amazon EC2.** Creates
        an Auto Scaling group with the specified name and attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.create_auto_scaling_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#create_auto_scaling_group)
        """
    def create_launch_configuration(
        self,
        *,
        LaunchConfigurationName: str,
        ImageId: str = None,
        KeyName: str = None,
        SecurityGroups: List[str] = None,
        ClassicLinkVPCId: str = None,
        ClassicLinkVPCSecurityGroups: List[str] = None,
        UserData: str = None,
        InstanceId: str = None,
        InstanceType: str = None,
        KernelId: str = None,
        RamdiskId: str = None,
        BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
        InstanceMonitoring: "InstanceMonitoringTypeDef" = None,
        SpotPrice: str = None,
        IamInstanceProfile: str = None,
        EbsOptimized: bool = None,
        AssociatePublicIpAddress: bool = None,
        PlacementTenancy: str = None,
        MetadataOptions: "InstanceMetadataOptionsTypeDef" = None
    ) -> None:
        """
        Creates a launch configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.create_launch_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#create_launch_configuration)
        """
    def create_or_update_tags(self, *, Tags: List["TagTypeDef"]) -> None:
        """
        Creates or updates tags for the specified Auto Scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.create_or_update_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#create_or_update_tags)
        """
    def delete_auto_scaling_group(
        self, *, AutoScalingGroupName: str, ForceDelete: bool = None
    ) -> None:
        """
        Deletes the specified Auto Scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.delete_auto_scaling_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#delete_auto_scaling_group)
        """
    def delete_launch_configuration(self, *, LaunchConfigurationName: str) -> None:
        """
        Deletes the specified launch configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.delete_launch_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#delete_launch_configuration)
        """
    def delete_lifecycle_hook(
        self, *, LifecycleHookName: str, AutoScalingGroupName: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified lifecycle hook.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.delete_lifecycle_hook)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#delete_lifecycle_hook)
        """
    def delete_notification_configuration(
        self, *, AutoScalingGroupName: str, TopicARN: str
    ) -> None:
        """
        Deletes the specified notification.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.delete_notification_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#delete_notification_configuration)
        """
    def delete_policy(self, *, PolicyName: str, AutoScalingGroupName: str = None) -> None:
        """
        Deletes the specified scaling policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.delete_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#delete_policy)
        """
    def delete_scheduled_action(
        self, *, AutoScalingGroupName: str, ScheduledActionName: str
    ) -> None:
        """
        Deletes the specified scheduled action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.delete_scheduled_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#delete_scheduled_action)
        """
    def delete_tags(self, *, Tags: List["TagTypeDef"]) -> None:
        """
        Deletes the specified tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.delete_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#delete_tags)
        """
    def delete_warm_pool(
        self, *, AutoScalingGroupName: str, ForceDelete: bool = None
    ) -> Dict[str, Any]:
        """
        Deletes the warm pool for the specified Auto Scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.delete_warm_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#delete_warm_pool)
        """
    def describe_account_limits(self) -> DescribeAccountLimitsAnswerTypeDef:
        """
        Describes the current Amazon EC2 Auto Scaling resource quotas for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_account_limits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_account_limits)
        """
    def describe_adjustment_types(self) -> DescribeAdjustmentTypesAnswerTypeDef:
        """
        Describes the available adjustment types for step scaling and simple scaling
        policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_adjustment_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_adjustment_types)
        """
    def describe_auto_scaling_groups(
        self,
        *,
        AutoScalingGroupNames: List[str] = None,
        NextToken: str = None,
        MaxRecords: int = None,
        Filters: List["FilterTypeDef"] = None
    ) -> AutoScalingGroupsTypeTypeDef:
        """
        Gets information about the Auto Scaling groups in the account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_auto_scaling_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_auto_scaling_groups)
        """
    def describe_auto_scaling_instances(
        self, *, InstanceIds: List[str] = None, MaxRecords: int = None, NextToken: str = None
    ) -> AutoScalingInstancesTypeTypeDef:
        """
        Gets information about the Auto Scaling instances in the account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_auto_scaling_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_auto_scaling_instances)
        """
    def describe_auto_scaling_notification_types(
        self,
    ) -> DescribeAutoScalingNotificationTypesAnswerTypeDef:
        """
        Describes the notification types that are supported by Amazon EC2 Auto Scaling.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_auto_scaling_notification_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_auto_scaling_notification_types)
        """
    def describe_instance_refreshes(
        self,
        *,
        AutoScalingGroupName: str,
        InstanceRefreshIds: List[str] = None,
        NextToken: str = None,
        MaxRecords: int = None
    ) -> DescribeInstanceRefreshesAnswerTypeDef:
        """
        Gets information about the instance refreshes for the specified Auto Scaling
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_instance_refreshes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_instance_refreshes)
        """
    def describe_launch_configurations(
        self,
        *,
        LaunchConfigurationNames: List[str] = None,
        NextToken: str = None,
        MaxRecords: int = None
    ) -> LaunchConfigurationsTypeTypeDef:
        """
        Gets information about the launch configurations in the account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_launch_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_launch_configurations)
        """
    def describe_lifecycle_hook_types(self) -> DescribeLifecycleHookTypesAnswerTypeDef:
        """
        Describes the available types of lifecycle hooks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_lifecycle_hook_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_lifecycle_hook_types)
        """
    def describe_lifecycle_hooks(
        self, *, AutoScalingGroupName: str, LifecycleHookNames: List[str] = None
    ) -> DescribeLifecycleHooksAnswerTypeDef:
        """
        Gets information about the lifecycle hooks for the specified Auto Scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_lifecycle_hooks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_lifecycle_hooks)
        """
    def describe_load_balancer_target_groups(
        self, *, AutoScalingGroupName: str, NextToken: str = None, MaxRecords: int = None
    ) -> DescribeLoadBalancerTargetGroupsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_load_balancer_target_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_load_balancer_target_groups)
        """
    def describe_load_balancers(
        self, *, AutoScalingGroupName: str, NextToken: str = None, MaxRecords: int = None
    ) -> DescribeLoadBalancersResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_load_balancers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_load_balancers)
        """
    def describe_metric_collection_types(self) -> DescribeMetricCollectionTypesAnswerTypeDef:
        """
        Describes the available CloudWatch metrics for Amazon EC2 Auto Scaling.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_metric_collection_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_metric_collection_types)
        """
    def describe_notification_configurations(
        self,
        *,
        AutoScalingGroupNames: List[str] = None,
        NextToken: str = None,
        MaxRecords: int = None
    ) -> DescribeNotificationConfigurationsAnswerTypeDef:
        """
        Gets information about the Amazon SNS notifications that are configured for one
        or more Auto Scaling groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_notification_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_notification_configurations)
        """
    def describe_policies(
        self,
        *,
        AutoScalingGroupName: str = None,
        PolicyNames: List[str] = None,
        PolicyTypes: List[str] = None,
        NextToken: str = None,
        MaxRecords: int = None
    ) -> PoliciesTypeTypeDef:
        """
        Gets information about the scaling policies in the account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_policies)
        """
    def describe_scaling_activities(
        self,
        *,
        ActivityIds: List[str] = None,
        AutoScalingGroupName: str = None,
        IncludeDeletedGroups: bool = None,
        MaxRecords: int = None,
        NextToken: str = None
    ) -> ActivitiesTypeTypeDef:
        """
        Gets information about the scaling activities in the account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_scaling_activities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_scaling_activities)
        """
    def describe_scaling_process_types(self) -> ProcessesTypeTypeDef:
        """
        Describes the scaling process types for use with the  ResumeProcesses and
        SuspendProcesses APIs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_scaling_process_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_scaling_process_types)
        """
    def describe_scheduled_actions(
        self,
        *,
        AutoScalingGroupName: str = None,
        ScheduledActionNames: List[str] = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        NextToken: str = None,
        MaxRecords: int = None
    ) -> ScheduledActionsTypeTypeDef:
        """
        Gets information about the scheduled actions that haven't run or that have not
        reached their end time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_scheduled_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_scheduled_actions)
        """
    def describe_tags(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        NextToken: str = None,
        MaxRecords: int = None
    ) -> TagsTypeTypeDef:
        """
        Describes the specified tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_tags)
        """
    def describe_termination_policy_types(self) -> DescribeTerminationPolicyTypesAnswerTypeDef:
        """
        Describes the termination policies supported by Amazon EC2 Auto Scaling.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_termination_policy_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_termination_policy_types)
        """
    def describe_traffic_sources(
        self,
        *,
        AutoScalingGroupName: str,
        TrafficSourceType: str = None,
        NextToken: str = None,
        MaxRecords: int = None
    ) -> DescribeTrafficSourcesResponseTypeDef:
        """
        Gets information about the traffic sources for the specified Auto Scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_traffic_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_traffic_sources)
        """
    def describe_warm_pool(
        self, *, AutoScalingGroupName: str, MaxRecords: int = None, NextToken: str = None
    ) -> DescribeWarmPoolAnswerTypeDef:
        """
        Gets information about a warm pool and its instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.describe_warm_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#describe_warm_pool)
        """
    def detach_instances(
        self,
        *,
        AutoScalingGroupName: str,
        ShouldDecrementDesiredCapacity: bool,
        InstanceIds: List[str] = None
    ) -> DetachInstancesAnswerTypeDef:
        """
        Removes one or more instances from the specified Auto Scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.detach_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#detach_instances)
        """
    def detach_load_balancer_target_groups(
        self, *, AutoScalingGroupName: str, TargetGroupARNs: List[str]
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.detach_load_balancer_target_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#detach_load_balancer_target_groups)
        """
    def detach_load_balancers(
        self, *, AutoScalingGroupName: str, LoadBalancerNames: List[str]
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.detach_load_balancers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#detach_load_balancers)
        """
    def detach_traffic_sources(
        self, *, AutoScalingGroupName: str, TrafficSources: List["TrafficSourceIdentifierTypeDef"]
    ) -> Dict[str, Any]:
        """
        Detaches one or more traffic sources from the specified Auto Scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.detach_traffic_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#detach_traffic_sources)
        """
    def disable_metrics_collection(
        self, *, AutoScalingGroupName: str, Metrics: List[str] = None
    ) -> None:
        """
        Disables group metrics collection for the specified Auto Scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.disable_metrics_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#disable_metrics_collection)
        """
    def enable_metrics_collection(
        self, *, AutoScalingGroupName: str, Granularity: str, Metrics: List[str] = None
    ) -> None:
        """
        Enables group metrics collection for the specified Auto Scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.enable_metrics_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#enable_metrics_collection)
        """
    def enter_standby(
        self,
        *,
        AutoScalingGroupName: str,
        ShouldDecrementDesiredCapacity: bool,
        InstanceIds: List[str] = None
    ) -> EnterStandbyAnswerTypeDef:
        """
        Moves the specified instances into the standby state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.enter_standby)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#enter_standby)
        """
    def execute_policy(
        self,
        *,
        PolicyName: str,
        AutoScalingGroupName: str = None,
        HonorCooldown: bool = None,
        MetricValue: float = None,
        BreachThreshold: float = None
    ) -> None:
        """
        Executes the specified policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.execute_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#execute_policy)
        """
    def exit_standby(
        self, *, AutoScalingGroupName: str, InstanceIds: List[str] = None
    ) -> ExitStandbyAnswerTypeDef:
        """
        Moves the specified instances out of the standby state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.exit_standby)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#exit_standby)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#generate_presigned_url)
        """
    def get_predictive_scaling_forecast(
        self,
        *,
        AutoScalingGroupName: str,
        PolicyName: str,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str]
    ) -> GetPredictiveScalingForecastAnswerTypeDef:
        """
        Retrieves the forecast data for a predictive scaling policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.get_predictive_scaling_forecast)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#get_predictive_scaling_forecast)
        """
    def put_lifecycle_hook(
        self,
        *,
        LifecycleHookName: str,
        AutoScalingGroupName: str,
        LifecycleTransition: str = None,
        RoleARN: str = None,
        NotificationTargetARN: str = None,
        NotificationMetadata: str = None,
        HeartbeatTimeout: int = None,
        DefaultResult: str = None
    ) -> Dict[str, Any]:
        """
        Creates or updates a lifecycle hook for the specified Auto Scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.put_lifecycle_hook)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#put_lifecycle_hook)
        """
    def put_notification_configuration(
        self, *, AutoScalingGroupName: str, TopicARN: str, NotificationTypes: List[str]
    ) -> None:
        """
        Configures an Auto Scaling group to send notifications when specified events
        take place.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.put_notification_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#put_notification_configuration)
        """
    def put_scaling_policy(
        self,
        *,
        AutoScalingGroupName: str,
        PolicyName: str,
        PolicyType: str = None,
        AdjustmentType: str = None,
        MinAdjustmentStep: int = None,
        MinAdjustmentMagnitude: int = None,
        ScalingAdjustment: int = None,
        Cooldown: int = None,
        MetricAggregationType: str = None,
        StepAdjustments: List["StepAdjustmentTypeDef"] = None,
        EstimatedInstanceWarmup: int = None,
        TargetTrackingConfiguration: "TargetTrackingConfigurationTypeDef" = None,
        Enabled: bool = None,
        PredictiveScalingConfiguration: "PredictiveScalingConfigurationTypeDef" = None
    ) -> PolicyARNTypeTypeDef:
        """
        Creates or updates a scaling policy for an Auto Scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.put_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#put_scaling_policy)
        """
    def put_scheduled_update_group_action(
        self,
        *,
        AutoScalingGroupName: str,
        ScheduledActionName: str,
        Time: Union[datetime, str] = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        Recurrence: str = None,
        MinSize: int = None,
        MaxSize: int = None,
        DesiredCapacity: int = None,
        TimeZone: str = None
    ) -> None:
        """
        Creates or updates a scheduled scaling action for an Auto Scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.put_scheduled_update_group_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#put_scheduled_update_group_action)
        """
    def put_warm_pool(
        self,
        *,
        AutoScalingGroupName: str,
        MaxGroupPreparedCapacity: int = None,
        MinSize: int = None,
        PoolState: WarmPoolStateType = None,
        InstanceReusePolicy: "InstanceReusePolicyTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Creates or updates a warm pool for the specified Auto Scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.put_warm_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#put_warm_pool)
        """
    def record_lifecycle_action_heartbeat(
        self,
        *,
        LifecycleHookName: str,
        AutoScalingGroupName: str,
        LifecycleActionToken: str = None,
        InstanceId: str = None
    ) -> Dict[str, Any]:
        """
        Records a heartbeat for the lifecycle action associated with the specified token
        or instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.record_lifecycle_action_heartbeat)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#record_lifecycle_action_heartbeat)
        """
    def resume_processes(
        self, *, AutoScalingGroupName: str, ScalingProcesses: List[str] = None
    ) -> None:
        """
        Resumes the specified suspended auto scaling processes, or all suspended
        process, for the specified Auto Scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.resume_processes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#resume_processes)
        """
    def rollback_instance_refresh(
        self, *, AutoScalingGroupName: str
    ) -> RollbackInstanceRefreshAnswerTypeDef:
        """
        Cancels an instance refresh that is in progress and rolls back any changes that
        it made.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.rollback_instance_refresh)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#rollback_instance_refresh)
        """
    def set_desired_capacity(
        self, *, AutoScalingGroupName: str, DesiredCapacity: int, HonorCooldown: bool = None
    ) -> None:
        """
        Sets the size of the specified Auto Scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.set_desired_capacity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#set_desired_capacity)
        """
    def set_instance_health(
        self, *, InstanceId: str, HealthStatus: str, ShouldRespectGracePeriod: bool = None
    ) -> None:
        """
        Sets the health status of the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.set_instance_health)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#set_instance_health)
        """
    def set_instance_protection(
        self, *, InstanceIds: List[str], AutoScalingGroupName: str, ProtectedFromScaleIn: bool
    ) -> Dict[str, Any]:
        """
        Updates the instance protection settings of the specified instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.set_instance_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#set_instance_protection)
        """
    def start_instance_refresh(
        self,
        *,
        AutoScalingGroupName: str,
        Strategy: Literal["Rolling"] = None,
        DesiredConfiguration: "DesiredConfigurationTypeDef" = None,
        Preferences: "RefreshPreferencesTypeDef" = None
    ) -> StartInstanceRefreshAnswerTypeDef:
        """
        Starts an instance refresh.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.start_instance_refresh)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#start_instance_refresh)
        """
    def suspend_processes(
        self, *, AutoScalingGroupName: str, ScalingProcesses: List[str] = None
    ) -> None:
        """
        Suspends the specified auto scaling processes, or all processes, for the
        specified Auto Scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.suspend_processes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#suspend_processes)
        """
    def terminate_instance_in_auto_scaling_group(
        self, *, InstanceId: str, ShouldDecrementDesiredCapacity: bool
    ) -> ActivityTypeTypeDef:
        """
        Terminates the specified instance and optionally adjusts the desired group size.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.terminate_instance_in_auto_scaling_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#terminate_instance_in_auto_scaling_group)
        """
    def update_auto_scaling_group(
        self,
        *,
        AutoScalingGroupName: str,
        LaunchConfigurationName: str = None,
        LaunchTemplate: "LaunchTemplateSpecificationTypeDef" = None,
        MixedInstancesPolicy: "MixedInstancesPolicyTypeDef" = None,
        MinSize: int = None,
        MaxSize: int = None,
        DesiredCapacity: int = None,
        DefaultCooldown: int = None,
        AvailabilityZones: List[str] = None,
        HealthCheckType: str = None,
        HealthCheckGracePeriod: int = None,
        PlacementGroup: str = None,
        VPCZoneIdentifier: str = None,
        TerminationPolicies: List[str] = None,
        NewInstancesProtectedFromScaleIn: bool = None,
        ServiceLinkedRoleARN: str = None,
        MaxInstanceLifetime: int = None,
        CapacityRebalance: bool = None,
        Context: str = None,
        DesiredCapacityType: str = None,
        DefaultInstanceWarmup: int = None,
        InstanceMaintenancePolicy: "InstanceMaintenancePolicyTypeDef" = None
    ) -> None:
        """
        **We strongly recommend that all Auto Scaling groups use launch templates to
        ensure full functionality for Amazon EC2 Auto Scaling and Amazon EC2.** Updates
        the configuration for the specified Auto Scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Client.update_auto_scaling_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/client.html#update_auto_scaling_group)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_auto_scaling_groups"]
    ) -> DescribeAutoScalingGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeAutoScalingGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators.html#describeautoscalinggroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_auto_scaling_instances"]
    ) -> DescribeAutoScalingInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeAutoScalingInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators.html#describeautoscalinginstancespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_launch_configurations"]
    ) -> DescribeLaunchConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLaunchConfigurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators.html#describelaunchconfigurationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_load_balancer_target_groups"]
    ) -> DescribeLoadBalancerTargetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLoadBalancerTargetGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators.html#describeloadbalancertargetgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_load_balancers"]
    ) -> DescribeLoadBalancersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLoadBalancers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators.html#describeloadbalancerspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_notification_configurations"]
    ) -> DescribeNotificationConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeNotificationConfigurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators.html#describenotificationconfigurationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_policies"]
    ) -> DescribePoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Paginator.DescribePolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators.html#describepoliciespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scaling_activities"]
    ) -> DescribeScalingActivitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeScalingActivities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators.html#describescalingactivitiespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_actions"]
    ) -> DescribeScheduledActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeScheduledActions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators.html#describescheduledactionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_tags"]) -> DescribeTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeTags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators.html#describetagspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_warm_pool"]
    ) -> DescribeWarmPoolPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeWarmPool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators.html#describewarmpoolpaginator)
        """
