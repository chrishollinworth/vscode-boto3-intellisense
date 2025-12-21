"""
Main interface for arc-region-switch service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_arc_region_switch import (
        ARCRegionswitchClient,
        Client,
        GetPlanEvaluationStatusPaginator,
        GetPlanExecutionPaginator,
        ListPlanExecutionEventsPaginator,
        ListPlanExecutionsPaginator,
        ListPlansInRegionPaginator,
        ListPlansPaginator,
        ListRoute53HealthChecksInRegionPaginator,
        ListRoute53HealthChecksPaginator,
        PlanEvaluationStatusPassedWaiter,
        PlanExecutionCompletedWaiter,
    )

    session = Session()
    client: ARCRegionswitchClient = session.client("arc-region-switch")

    plan_evaluation_status_passed_waiter: PlanEvaluationStatusPassedWaiter = client.get_waiter("plan_evaluation_status_passed")
    plan_execution_completed_waiter: PlanExecutionCompletedWaiter = client.get_waiter("plan_execution_completed")

    get_plan_evaluation_status_paginator: GetPlanEvaluationStatusPaginator = client.get_paginator("get_plan_evaluation_status")
    get_plan_execution_paginator: GetPlanExecutionPaginator = client.get_paginator("get_plan_execution")
    list_plan_execution_events_paginator: ListPlanExecutionEventsPaginator = client.get_paginator("list_plan_execution_events")
    list_plan_executions_paginator: ListPlanExecutionsPaginator = client.get_paginator("list_plan_executions")
    list_plans_in_region_paginator: ListPlansInRegionPaginator = client.get_paginator("list_plans_in_region")
    list_plans_paginator: ListPlansPaginator = client.get_paginator("list_plans")
    list_route53_health_checks_in_region_paginator: ListRoute53HealthChecksInRegionPaginator = client.get_paginator("list_route53_health_checks_in_region")
    list_route53_health_checks_paginator: ListRoute53HealthChecksPaginator = client.get_paginator("list_route53_health_checks")
    ```
"""

from .client import ARCRegionswitchClient
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
from .waiter import PlanEvaluationStatusPassedWaiter, PlanExecutionCompletedWaiter

Client = ARCRegionswitchClient

__all__ = (
    "ARCRegionswitchClient",
    "Client",
    "GetPlanEvaluationStatusPaginator",
    "GetPlanExecutionPaginator",
    "ListPlanExecutionEventsPaginator",
    "ListPlanExecutionsPaginator",
    "ListPlansInRegionPaginator",
    "ListPlansPaginator",
    "ListRoute53HealthChecksInRegionPaginator",
    "ListRoute53HealthChecksPaginator",
    "PlanEvaluationStatusPassedWaiter",
    "PlanExecutionCompletedWaiter",
)
