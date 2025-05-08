"""
Type annotations for application-autoscaling service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_application_autoscaling.client import ApplicationAutoScalingClient

    session = Session()
    client: ApplicationAutoScalingClient = session.client("application-autoscaling")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeScalableTargetsPaginator,
    DescribeScalingActivitiesPaginator,
    DescribeScalingPoliciesPaginator,
    DescribeScheduledActionsPaginator,
)
from .type_defs import (
    DeleteScalingPolicyRequestTypeDef,
    DeleteScheduledActionRequestTypeDef,
    DeregisterScalableTargetRequestTypeDef,
    DescribeScalableTargetsRequestTypeDef,
    DescribeScalableTargetsResponseTypeDef,
    DescribeScalingActivitiesRequestTypeDef,
    DescribeScalingActivitiesResponseTypeDef,
    DescribeScalingPoliciesRequestTypeDef,
    DescribeScalingPoliciesResponseTypeDef,
    DescribeScheduledActionsRequestTypeDef,
    DescribeScheduledActionsResponseTypeDef,
    GetPredictiveScalingForecastRequestTypeDef,
    GetPredictiveScalingForecastResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutScalingPolicyRequestTypeDef,
    PutScalingPolicyResponseTypeDef,
    PutScheduledActionRequestTypeDef,
    RegisterScalableTargetRequestTypeDef,
    RegisterScalableTargetResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("ApplicationAutoScalingClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ConcurrentUpdateException: Type[BotocoreClientError]
    FailedResourceAccessException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ObjectNotFoundException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ApplicationAutoScalingClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ApplicationAutoScalingClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#generate_presigned_url)
        """

    def delete_scaling_policy(
        self, **kwargs: Unpack[DeleteScalingPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified scaling policy for an Application Auto Scaling scalable
        target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/client/delete_scaling_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#delete_scaling_policy)
        """

    def delete_scheduled_action(
        self, **kwargs: Unpack[DeleteScheduledActionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified scheduled action for an Application Auto Scaling scalable
        target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/client/delete_scheduled_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#delete_scheduled_action)
        """

    def deregister_scalable_target(
        self, **kwargs: Unpack[DeregisterScalableTargetRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deregisters an Application Auto Scaling scalable target when you have finished
        using it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/client/deregister_scalable_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#deregister_scalable_target)
        """

    def describe_scalable_targets(
        self, **kwargs: Unpack[DescribeScalableTargetsRequestTypeDef]
    ) -> DescribeScalableTargetsResponseTypeDef:
        """
        Gets information about the scalable targets in the specified namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/client/describe_scalable_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#describe_scalable_targets)
        """

    def describe_scaling_activities(
        self, **kwargs: Unpack[DescribeScalingActivitiesRequestTypeDef]
    ) -> DescribeScalingActivitiesResponseTypeDef:
        """
        Provides descriptive information about the scaling activities in the specified
        namespace from the previous six weeks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/client/describe_scaling_activities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#describe_scaling_activities)
        """

    def describe_scaling_policies(
        self, **kwargs: Unpack[DescribeScalingPoliciesRequestTypeDef]
    ) -> DescribeScalingPoliciesResponseTypeDef:
        """
        Describes the Application Auto Scaling scaling policies for the specified
        service namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/client/describe_scaling_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#describe_scaling_policies)
        """

    def describe_scheduled_actions(
        self, **kwargs: Unpack[DescribeScheduledActionsRequestTypeDef]
    ) -> DescribeScheduledActionsResponseTypeDef:
        """
        Describes the Application Auto Scaling scheduled actions for the specified
        service namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/client/describe_scheduled_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#describe_scheduled_actions)
        """

    def get_predictive_scaling_forecast(
        self, **kwargs: Unpack[GetPredictiveScalingForecastRequestTypeDef]
    ) -> GetPredictiveScalingForecastResponseTypeDef:
        """
        Retrieves the forecast data for a predictive scaling policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/client/get_predictive_scaling_forecast.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#get_predictive_scaling_forecast)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns all the tags on the specified Application Auto Scaling scalable target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#list_tags_for_resource)
        """

    def put_scaling_policy(
        self, **kwargs: Unpack[PutScalingPolicyRequestTypeDef]
    ) -> PutScalingPolicyResponseTypeDef:
        """
        Creates or updates a scaling policy for an Application Auto Scaling scalable
        target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/client/put_scaling_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#put_scaling_policy)
        """

    def put_scheduled_action(
        self, **kwargs: Unpack[PutScheduledActionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates or updates a scheduled action for an Application Auto Scaling scalable
        target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/client/put_scheduled_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#put_scheduled_action)
        """

    def register_scalable_target(
        self, **kwargs: Unpack[RegisterScalableTargetRequestTypeDef]
    ) -> RegisterScalableTargetResponseTypeDef:
        """
        Registers or updates a scalable target, which is the resource that you want to
        scale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/client/register_scalable_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#register_scalable_target)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds or edits tags on an Application Auto Scaling scalable target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes tags from an Application Auto Scaling scalable target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#untag_resource)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_scalable_targets"]
    ) -> DescribeScalableTargetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_scaling_activities"]
    ) -> DescribeScalingActivitiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_scaling_policies"]
    ) -> DescribeScalingPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_scheduled_actions"]
    ) -> DescribeScheduledActionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client/#get_paginator)
        """
