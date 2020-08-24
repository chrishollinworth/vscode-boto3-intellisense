# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for application-autoscaling service client

Usage::

    ```python
    import boto3
    from mypy_boto3_application_autoscaling import ApplicationAutoScalingClient

    client: ApplicationAutoScalingClient = boto3.client("application-autoscaling")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_application_autoscaling.paginator import (
    DescribeScalableTargetsPaginator,
    DescribeScalingActivitiesPaginator,
    DescribeScalingPoliciesPaginator,
    DescribeScheduledActionsPaginator,
)
from mypy_boto3_application_autoscaling.type_defs import (
    DescribeScalableTargetsResponseTypeDef,
    DescribeScalingActivitiesResponseTypeDef,
    DescribeScalingPoliciesResponseTypeDef,
    DescribeScheduledActionsResponseTypeDef,
    PutScalingPolicyResponseTypeDef,
    ScalableTargetActionTypeDef,
    StepScalingPolicyConfigurationTypeDef,
    SuspendedStateTypeDef,
    TargetTrackingScalingPolicyConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ApplicationAutoScalingClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    ConcurrentUpdateException: Type[Boto3ClientError]
    FailedResourceAccessException: Type[Boto3ClientError]
    InternalServiceException: Type[Boto3ClientError]
    InvalidNextTokenException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    ObjectNotFoundException: Type[Boto3ClientError]
    ValidationException: Type[Boto3ClientError]


class ApplicationAutoScalingClient:
    """
    [ApplicationAutoScaling.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.can_paginate)
        """

    def delete_scaling_policy(
        self,
        PolicyName: str,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
            "cassandra",
        ],
        ResourceId: str,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
            "cassandra:table:ReadCapacityUnits",
            "cassandra:table:WriteCapacityUnits",
        ],
    ) -> Dict[str, Any]:
        """
        [Client.delete_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.delete_scaling_policy)
        """

    def delete_scheduled_action(
        self,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
            "cassandra",
        ],
        ScheduledActionName: str,
        ResourceId: str,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
            "cassandra:table:ReadCapacityUnits",
            "cassandra:table:WriteCapacityUnits",
        ],
    ) -> Dict[str, Any]:
        """
        [Client.delete_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.delete_scheduled_action)
        """

    def deregister_scalable_target(
        self,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
            "cassandra",
        ],
        ResourceId: str,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
            "cassandra:table:ReadCapacityUnits",
            "cassandra:table:WriteCapacityUnits",
        ],
    ) -> Dict[str, Any]:
        """
        [Client.deregister_scalable_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.deregister_scalable_target)
        """

    def describe_scalable_targets(
        self,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
            "cassandra",
        ],
        ResourceIds: List[str] = None,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
            "cassandra:table:ReadCapacityUnits",
            "cassandra:table:WriteCapacityUnits",
        ] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeScalableTargetsResponseTypeDef:
        """
        [Client.describe_scalable_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scalable_targets)
        """

    def describe_scaling_activities(
        self,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
            "cassandra",
        ],
        ResourceId: str = None,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
            "cassandra:table:ReadCapacityUnits",
            "cassandra:table:WriteCapacityUnits",
        ] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeScalingActivitiesResponseTypeDef:
        """
        [Client.describe_scaling_activities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scaling_activities)
        """

    def describe_scaling_policies(
        self,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
            "cassandra",
        ],
        PolicyNames: List[str] = None,
        ResourceId: str = None,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
            "cassandra:table:ReadCapacityUnits",
            "cassandra:table:WriteCapacityUnits",
        ] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeScalingPoliciesResponseTypeDef:
        """
        [Client.describe_scaling_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scaling_policies)
        """

    def describe_scheduled_actions(
        self,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
            "cassandra",
        ],
        ScheduledActionNames: List[str] = None,
        ResourceId: str = None,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
            "cassandra:table:ReadCapacityUnits",
            "cassandra:table:WriteCapacityUnits",
        ] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeScheduledActionsResponseTypeDef:
        """
        [Client.describe_scheduled_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scheduled_actions)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.generate_presigned_url)
        """

    def put_scaling_policy(
        self,
        PolicyName: str,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
            "cassandra",
        ],
        ResourceId: str,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
            "cassandra:table:ReadCapacityUnits",
            "cassandra:table:WriteCapacityUnits",
        ],
        PolicyType: Literal["StepScaling", "TargetTrackingScaling"] = None,
        StepScalingPolicyConfiguration: "StepScalingPolicyConfigurationTypeDef" = None,
        TargetTrackingScalingPolicyConfiguration: "TargetTrackingScalingPolicyConfigurationTypeDef" = None,
    ) -> PutScalingPolicyResponseTypeDef:
        """
        [Client.put_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.put_scaling_policy)
        """

    def put_scheduled_action(
        self,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
            "cassandra",
        ],
        ScheduledActionName: str,
        ResourceId: str,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
            "cassandra:table:ReadCapacityUnits",
            "cassandra:table:WriteCapacityUnits",
        ],
        Schedule: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        ScalableTargetAction: "ScalableTargetActionTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.put_scheduled_action)
        """

    def register_scalable_target(
        self,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
            "cassandra",
        ],
        ResourceId: str,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
            "cassandra:table:ReadCapacityUnits",
            "cassandra:table:WriteCapacityUnits",
        ],
        MinCapacity: int = None,
        MaxCapacity: int = None,
        RoleARN: str = None,
        SuspendedState: "SuspendedStateTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Client.register_scalable_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.register_scalable_target)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scalable_targets"]
    ) -> DescribeScalableTargetsPaginator:
        """
        [Paginator.DescribeScalableTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalableTargets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scaling_activities"]
    ) -> DescribeScalingActivitiesPaginator:
        """
        [Paginator.DescribeScalingActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalingActivities)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scaling_policies"]
    ) -> DescribeScalingPoliciesPaginator:
        """
        [Paginator.DescribeScalingPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalingPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_actions"]
    ) -> DescribeScheduledActionsPaginator:
        """
        [Paginator.DescribeScheduledActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScheduledActions)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
