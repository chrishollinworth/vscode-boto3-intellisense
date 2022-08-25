"""
Type annotations for application-autoscaling service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_application_autoscaling import ApplicationAutoScalingClient

    client: ApplicationAutoScalingClient = boto3.client("application-autoscaling")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import PolicyTypeType, ScalableDimensionType, ServiceNamespaceType
from .paginator import (
    DescribeScalableTargetsPaginator,
    DescribeScalingActivitiesPaginator,
    DescribeScalingPoliciesPaginator,
    DescribeScheduledActionsPaginator,
)
from .type_defs import (
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

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentUpdateException: Type[BotocoreClientError]
    FailedResourceAccessException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ObjectNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ApplicationAutoScalingClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ApplicationAutoScalingClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#close)
        """
    def delete_scaling_policy(
        self,
        *,
        PolicyName: str,
        ServiceNamespace: ServiceNamespaceType,
        ResourceId: str,
        ScalableDimension: ScalableDimensionType
    ) -> Dict[str, Any]:
        """
        Deletes the specified scaling policy for an Application Auto Scaling scalable
        target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.delete_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#delete_scaling_policy)
        """
    def delete_scheduled_action(
        self,
        *,
        ServiceNamespace: ServiceNamespaceType,
        ScheduledActionName: str,
        ResourceId: str,
        ScalableDimension: ScalableDimensionType
    ) -> Dict[str, Any]:
        """
        Deletes the specified scheduled action for an Application Auto Scaling scalable
        target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.delete_scheduled_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#delete_scheduled_action)
        """
    def deregister_scalable_target(
        self,
        *,
        ServiceNamespace: ServiceNamespaceType,
        ResourceId: str,
        ScalableDimension: ScalableDimensionType
    ) -> Dict[str, Any]:
        """
        Deregisters an Application Auto Scaling scalable target when you have finished
        using it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.deregister_scalable_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#deregister_scalable_target)
        """
    def describe_scalable_targets(
        self,
        *,
        ServiceNamespace: ServiceNamespaceType,
        ResourceIds: List[str] = None,
        ScalableDimension: ScalableDimensionType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeScalableTargetsResponseTypeDef:
        """
        Gets information about the scalable targets in the specified namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scalable_targets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#describe_scalable_targets)
        """
    def describe_scaling_activities(
        self,
        *,
        ServiceNamespace: ServiceNamespaceType,
        ResourceId: str = None,
        ScalableDimension: ScalableDimensionType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeScalingActivitiesResponseTypeDef:
        """
        Provides descriptive information about the scaling activities in the specified
        namespace from the previous six weeks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scaling_activities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#describe_scaling_activities)
        """
    def describe_scaling_policies(
        self,
        *,
        ServiceNamespace: ServiceNamespaceType,
        PolicyNames: List[str] = None,
        ResourceId: str = None,
        ScalableDimension: ScalableDimensionType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeScalingPoliciesResponseTypeDef:
        """
        Describes the Application Auto Scaling scaling policies for the specified
        service namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scaling_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#describe_scaling_policies)
        """
    def describe_scheduled_actions(
        self,
        *,
        ServiceNamespace: ServiceNamespaceType,
        ScheduledActionNames: List[str] = None,
        ResourceId: str = None,
        ScalableDimension: ScalableDimensionType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeScheduledActionsResponseTypeDef:
        """
        Describes the Application Auto Scaling scheduled actions for the specified
        service namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scheduled_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#describe_scheduled_actions)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#generate_presigned_url)
        """
    def put_scaling_policy(
        self,
        *,
        PolicyName: str,
        ServiceNamespace: ServiceNamespaceType,
        ResourceId: str,
        ScalableDimension: ScalableDimensionType,
        PolicyType: PolicyTypeType = None,
        StepScalingPolicyConfiguration: "StepScalingPolicyConfigurationTypeDef" = None,
        TargetTrackingScalingPolicyConfiguration: "TargetTrackingScalingPolicyConfigurationTypeDef" = None
    ) -> PutScalingPolicyResponseTypeDef:
        """
        Creates or updates a scaling policy for an Application Auto Scaling scalable
        target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.put_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#put_scaling_policy)
        """
    def put_scheduled_action(
        self,
        *,
        ServiceNamespace: ServiceNamespaceType,
        ScheduledActionName: str,
        ResourceId: str,
        ScalableDimension: ScalableDimensionType,
        Schedule: str = None,
        Timezone: str = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        ScalableTargetAction: "ScalableTargetActionTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Creates or updates a scheduled action for an Application Auto Scaling scalable
        target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.put_scheduled_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#put_scheduled_action)
        """
    def register_scalable_target(
        self,
        *,
        ServiceNamespace: ServiceNamespaceType,
        ResourceId: str,
        ScalableDimension: ScalableDimensionType,
        MinCapacity: int = None,
        MaxCapacity: int = None,
        RoleARN: str = None,
        SuspendedState: "SuspendedStateTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Registers or updates a scalable target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.register_scalable_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#register_scalable_target)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scalable_targets"]
    ) -> DescribeScalableTargetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalableTargets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/paginators.html#describescalabletargetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scaling_activities"]
    ) -> DescribeScalingActivitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalingActivities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/paginators.html#describescalingactivitiespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scaling_policies"]
    ) -> DescribeScalingPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalingPolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/paginators.html#describescalingpoliciespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_actions"]
    ) -> DescribeScheduledActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScheduledActions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/paginators.html#describescheduledactionspaginator)
        """
