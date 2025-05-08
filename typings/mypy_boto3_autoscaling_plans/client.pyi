"""
Type annotations for autoscaling-plans service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_autoscaling_plans.client import AutoScalingPlansClient

    session = Session()
    client: AutoScalingPlansClient = session.client("autoscaling-plans")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import DescribeScalingPlanResourcesPaginator, DescribeScalingPlansPaginator
from .type_defs import (
    CreateScalingPlanRequestTypeDef,
    CreateScalingPlanResponseTypeDef,
    DeleteScalingPlanRequestTypeDef,
    DescribeScalingPlanResourcesRequestTypeDef,
    DescribeScalingPlanResourcesResponseTypeDef,
    DescribeScalingPlansRequestTypeDef,
    DescribeScalingPlansResponseTypeDef,
    GetScalingPlanResourceForecastDataRequestTypeDef,
    GetScalingPlanResourceForecastDataResponseTypeDef,
    UpdateScalingPlanRequestTypeDef,
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

__all__ = ("AutoScalingPlansClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ConcurrentUpdateException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ObjectNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class AutoScalingPlansClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html#AutoScalingPlans.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AutoScalingPlansClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html#AutoScalingPlans.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client/#generate_presigned_url)
        """

    def create_scaling_plan(
        self, **kwargs: Unpack[CreateScalingPlanRequestTypeDef]
    ) -> CreateScalingPlanResponseTypeDef:
        """
        Creates a scaling plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans/client/create_scaling_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client/#create_scaling_plan)
        """

    def delete_scaling_plan(
        self, **kwargs: Unpack[DeleteScalingPlanRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified scaling plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans/client/delete_scaling_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client/#delete_scaling_plan)
        """

    def describe_scaling_plan_resources(
        self, **kwargs: Unpack[DescribeScalingPlanResourcesRequestTypeDef]
    ) -> DescribeScalingPlanResourcesResponseTypeDef:
        """
        Describes the scalable resources in the specified scaling plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans/client/describe_scaling_plan_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client/#describe_scaling_plan_resources)
        """

    def describe_scaling_plans(
        self, **kwargs: Unpack[DescribeScalingPlansRequestTypeDef]
    ) -> DescribeScalingPlansResponseTypeDef:
        """
        Describes one or more of your scaling plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans/client/describe_scaling_plans.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client/#describe_scaling_plans)
        """

    def get_scaling_plan_resource_forecast_data(
        self, **kwargs: Unpack[GetScalingPlanResourceForecastDataRequestTypeDef]
    ) -> GetScalingPlanResourceForecastDataResponseTypeDef:
        """
        Retrieves the forecast data for a scalable resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans/client/get_scaling_plan_resource_forecast_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client/#get_scaling_plan_resource_forecast_data)
        """

    def update_scaling_plan(
        self, **kwargs: Unpack[UpdateScalingPlanRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the specified scaling plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans/client/update_scaling_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client/#update_scaling_plan)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_scaling_plan_resources"]
    ) -> DescribeScalingPlanResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_scaling_plans"]
    ) -> DescribeScalingPlansPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client/#get_paginator)
        """
