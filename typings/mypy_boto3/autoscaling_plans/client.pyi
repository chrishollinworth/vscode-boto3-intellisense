"""
Type annotations for autoscaling-plans service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_autoscaling_plans import AutoScalingPlansClient

    client: AutoScalingPlansClient = boto3.client("autoscaling-plans")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import ForecastDataTypeType, ScalableDimensionType, ServiceNamespaceType
from .paginator import DescribeScalingPlanResourcesPaginator, DescribeScalingPlansPaginator
from .type_defs import (
    ApplicationSourceTypeDef,
    CreateScalingPlanResponseTypeDef,
    DescribeScalingPlanResourcesResponseTypeDef,
    DescribeScalingPlansResponseTypeDef,
    GetScalingPlanResourceForecastDataResponseTypeDef,
    ScalingInstructionTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AutoScalingPlansClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentUpdateException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ObjectNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class AutoScalingPlansClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/autoscaling-plans.html#AutoScalingPlans.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        AutoScalingPlansClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client.html#can_paginate)
        """
    def create_scaling_plan(
        self,
        *,
        ScalingPlanName: str,
        ApplicationSource: "ApplicationSourceTypeDef",
        ScalingInstructions: List["ScalingInstructionTypeDef"]
    ) -> CreateScalingPlanResponseTypeDef:
        """
        Creates a scaling plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.create_scaling_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client.html#create_scaling_plan)
        """
    def delete_scaling_plan(
        self, *, ScalingPlanName: str, ScalingPlanVersion: int
    ) -> Dict[str, Any]:
        """
        Deletes the specified scaling plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.delete_scaling_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client.html#delete_scaling_plan)
        """
    def describe_scaling_plan_resources(
        self,
        *,
        ScalingPlanName: str,
        ScalingPlanVersion: int,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeScalingPlanResourcesResponseTypeDef:
        """
        Describes the scalable resources in the specified scaling plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.describe_scaling_plan_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client.html#describe_scaling_plan_resources)
        """
    def describe_scaling_plans(
        self,
        *,
        ScalingPlanNames: List[str] = None,
        ScalingPlanVersion: int = None,
        ApplicationSources: List["ApplicationSourceTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeScalingPlansResponseTypeDef:
        """
        Describes one or more of your scaling plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.describe_scaling_plans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client.html#describe_scaling_plans)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client.html#generate_presigned_url)
        """
    def get_scaling_plan_resource_forecast_data(
        self,
        *,
        ScalingPlanName: str,
        ScalingPlanVersion: int,
        ServiceNamespace: ServiceNamespaceType,
        ResourceId: str,
        ScalableDimension: ScalableDimensionType,
        ForecastDataType: ForecastDataTypeType,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str]
    ) -> GetScalingPlanResourceForecastDataResponseTypeDef:
        """
        Retrieves the forecast data for a scalable resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.get_scaling_plan_resource_forecast_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client.html#get_scaling_plan_resource_forecast_data)
        """
    def update_scaling_plan(
        self,
        *,
        ScalingPlanName: str,
        ScalingPlanVersion: int,
        ApplicationSource: "ApplicationSourceTypeDef" = None,
        ScalingInstructions: List["ScalingInstructionTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Updates the specified scaling plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.update_scaling_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/client.html#update_scaling_plan)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scaling_plan_resources"]
    ) -> DescribeScalingPlanResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlanResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/paginators.html#describescalingplanresourcespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scaling_plans"]
    ) -> DescribeScalingPlansPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/paginators.html#describescalingplanspaginator)
        """
