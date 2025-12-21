"""
Type annotations for arc-region-switch service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_arc_region_switch.client import ARCRegionswitchClient

    session = Session()
    client: ARCRegionswitchClient = session.client("arc-region-switch")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    GetPlanEvaluationStatusPaginator,
    GetPlanExecutionPaginator,
    ListPlanExecutionEventsPaginator,
    ListPlanExecutionsPaginator,
    ListPlansInRegionPaginator,
    ListPlansPaginator,
    ListRoute53HealthChecksInRegionPaginator,
    ListRoute53HealthChecksPaginator,
)
from .type_defs import (
    ApprovePlanExecutionStepRequestTypeDef,
    CancelPlanExecutionRequestTypeDef,
    CreatePlanRequestTypeDef,
    CreatePlanResponseTypeDef,
    DeletePlanRequestTypeDef,
    GetPlanEvaluationStatusRequestTypeDef,
    GetPlanEvaluationStatusResponseTypeDef,
    GetPlanExecutionRequestTypeDef,
    GetPlanExecutionResponseTypeDef,
    GetPlanInRegionRequestTypeDef,
    GetPlanInRegionResponseTypeDef,
    GetPlanRequestTypeDef,
    GetPlanResponseTypeDef,
    ListPlanExecutionEventsRequestTypeDef,
    ListPlanExecutionEventsResponseTypeDef,
    ListPlanExecutionsRequestTypeDef,
    ListPlanExecutionsResponseTypeDef,
    ListPlansInRegionRequestTypeDef,
    ListPlansInRegionResponseTypeDef,
    ListPlansRequestTypeDef,
    ListPlansResponseTypeDef,
    ListRoute53HealthChecksInRegionRequestTypeDef,
    ListRoute53HealthChecksInRegionResponseTypeDef,
    ListRoute53HealthChecksRequestTypeDef,
    ListRoute53HealthChecksResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartPlanExecutionRequestTypeDef,
    StartPlanExecutionResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdatePlanExecutionRequestTypeDef,
    UpdatePlanExecutionStepRequestTypeDef,
    UpdatePlanRequestTypeDef,
    UpdatePlanResponseTypeDef,
)
from .waiter import PlanEvaluationStatusPassedWaiter, PlanExecutionCompletedWaiter

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

__all__ = ("ARCRegionswitchClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    IllegalArgumentException: Type[BotocoreClientError]
    IllegalStateException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class ARCRegionswitchClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch.html#ARCRegionswitch.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ARCRegionswitchClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch.html#ARCRegionswitch.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#generate_presigned_url)
        """

    def approve_plan_execution_step(
        self, **kwargs: Unpack[ApprovePlanExecutionStepRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Approves a step in a plan execution that requires manual approval.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/approve_plan_execution_step.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#approve_plan_execution_step)
        """

    def cancel_plan_execution(
        self, **kwargs: Unpack[CancelPlanExecutionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Cancels an in-progress plan execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/cancel_plan_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#cancel_plan_execution)
        """

    def create_plan(self, **kwargs: Unpack[CreatePlanRequestTypeDef]) -> CreatePlanResponseTypeDef:
        """
        Creates a new Region switch plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/create_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#create_plan)
        """

    def delete_plan(self, **kwargs: Unpack[DeletePlanRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a Region switch plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/delete_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#delete_plan)
        """

    def get_plan(self, **kwargs: Unpack[GetPlanRequestTypeDef]) -> GetPlanResponseTypeDef:
        """
        Retrieves detailed information about a Region switch plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/get_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#get_plan)
        """

    def get_plan_evaluation_status(
        self, **kwargs: Unpack[GetPlanEvaluationStatusRequestTypeDef]
    ) -> GetPlanEvaluationStatusResponseTypeDef:
        """
        Retrieves the evaluation status of a Region switch plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/get_plan_evaluation_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#get_plan_evaluation_status)
        """

    def get_plan_execution(
        self, **kwargs: Unpack[GetPlanExecutionRequestTypeDef]
    ) -> GetPlanExecutionResponseTypeDef:
        """
        Retrieves detailed information about a specific plan execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/get_plan_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#get_plan_execution)
        """

    def get_plan_in_region(
        self, **kwargs: Unpack[GetPlanInRegionRequestTypeDef]
    ) -> GetPlanInRegionResponseTypeDef:
        """
        Retrieves information about a Region switch plan in a specific Amazon Web
        Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/get_plan_in_region.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#get_plan_in_region)
        """

    def list_plan_execution_events(
        self, **kwargs: Unpack[ListPlanExecutionEventsRequestTypeDef]
    ) -> ListPlanExecutionEventsResponseTypeDef:
        """
        Lists the events that occurred during a plan execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/list_plan_execution_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#list_plan_execution_events)
        """

    def list_plan_executions(
        self, **kwargs: Unpack[ListPlanExecutionsRequestTypeDef]
    ) -> ListPlanExecutionsResponseTypeDef:
        """
        Lists the executions of a Region switch plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/list_plan_executions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#list_plan_executions)
        """

    def list_plans(self, **kwargs: Unpack[ListPlansRequestTypeDef]) -> ListPlansResponseTypeDef:
        """
        Lists all Region switch plans in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/list_plans.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#list_plans)
        """

    def list_plans_in_region(
        self, **kwargs: Unpack[ListPlansInRegionRequestTypeDef]
    ) -> ListPlansInRegionResponseTypeDef:
        """
        Lists all Region switch plans in your Amazon Web Services account that are
        available in the current Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/list_plans_in_region.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#list_plans_in_region)
        """

    def list_route53_health_checks(
        self, **kwargs: Unpack[ListRoute53HealthChecksRequestTypeDef]
    ) -> ListRoute53HealthChecksResponseTypeDef:
        """
        List the Amazon Route 53 health checks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/list_route53_health_checks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#list_route53_health_checks)
        """

    def list_route53_health_checks_in_region(
        self, **kwargs: Unpack[ListRoute53HealthChecksInRegionRequestTypeDef]
    ) -> ListRoute53HealthChecksInRegionResponseTypeDef:
        """
        List the Amazon Route 53 health checks in a specific Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/list_route53_health_checks_in_region.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#list_route53_health_checks_in_region)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags attached to a Region switch resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#list_tags_for_resource)
        """

    def start_plan_execution(
        self, **kwargs: Unpack[StartPlanExecutionRequestTypeDef]
    ) -> StartPlanExecutionResponseTypeDef:
        """
        Starts the execution of a Region switch plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/start_plan_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#start_plan_execution)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds or updates tags for a Region switch resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from a Region switch resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#untag_resource)
        """

    def update_plan(self, **kwargs: Unpack[UpdatePlanRequestTypeDef]) -> UpdatePlanResponseTypeDef:
        """
        Updates an existing Region switch plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/update_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#update_plan)
        """

    def update_plan_execution(
        self, **kwargs: Unpack[UpdatePlanExecutionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates an in-progress plan execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/update_plan_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#update_plan_execution)
        """

    def update_plan_execution_step(
        self, **kwargs: Unpack[UpdatePlanExecutionStepRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a specific step in an in-progress plan execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/update_plan_execution_step.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#update_plan_execution_step)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_plan_evaluation_status"]
    ) -> GetPlanEvaluationStatusPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_plan_execution"]
    ) -> GetPlanExecutionPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_plan_execution_events"]
    ) -> ListPlanExecutionEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_plan_executions"]
    ) -> ListPlanExecutionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_plans_in_region"]
    ) -> ListPlansInRegionPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_plans"]
    ) -> ListPlansPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_route53_health_checks_in_region"]
    ) -> ListRoute53HealthChecksInRegionPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_route53_health_checks"]
    ) -> ListRoute53HealthChecksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["plan_evaluation_status_passed"]
    ) -> PlanEvaluationStatusPassedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["plan_execution_completed"]
    ) -> PlanExecutionCompletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/client/#get_waiter)
        """
