"""
Type annotations for arc-region-switch service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_arc_region_switch.client import ARCRegionswitchClient
    from mypy_boto3_arc_region_switch.paginator import (
        GetPlanEvaluationStatusPaginator,
        GetPlanExecutionPaginator,
        ListPlanExecutionEventsPaginator,
        ListPlanExecutionsPaginator,
        ListPlansInRegionPaginator,
        ListPlansPaginator,
        ListRoute53HealthChecksInRegionPaginator,
        ListRoute53HealthChecksPaginator,
    )

    session = Session()
    client: ARCRegionswitchClient = session.client("arc-region-switch")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetPlanEvaluationStatusRequestPaginateTypeDef,
    GetPlanEvaluationStatusResponseTypeDef,
    GetPlanExecutionRequestPaginateTypeDef,
    GetPlanExecutionResponsePaginatorTypeDef,
    ListPlanExecutionEventsRequestPaginateTypeDef,
    ListPlanExecutionEventsResponseTypeDef,
    ListPlanExecutionsRequestPaginateTypeDef,
    ListPlanExecutionsResponseTypeDef,
    ListPlansInRegionRequestPaginateTypeDef,
    ListPlansInRegionResponseTypeDef,
    ListPlansRequestPaginateTypeDef,
    ListPlansResponseTypeDef,
    ListRoute53HealthChecksInRegionRequestPaginateTypeDef,
    ListRoute53HealthChecksInRegionResponseTypeDef,
    ListRoute53HealthChecksRequestPaginateTypeDef,
    ListRoute53HealthChecksResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetPlanEvaluationStatusPaginator",
    "GetPlanExecutionPaginator",
    "ListPlanExecutionEventsPaginator",
    "ListPlanExecutionsPaginator",
    "ListPlansInRegionPaginator",
    "ListPlansPaginator",
    "ListRoute53HealthChecksInRegionPaginator",
    "ListRoute53HealthChecksPaginator",
)

if TYPE_CHECKING:
    _GetPlanEvaluationStatusPaginatorBase = Paginator[GetPlanEvaluationStatusResponseTypeDef]
else:
    _GetPlanEvaluationStatusPaginatorBase = Paginator  # type: ignore[assignment]

class GetPlanEvaluationStatusPaginator(_GetPlanEvaluationStatusPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/paginator/GetPlanEvaluationStatus.html#ARCRegionswitch.Paginator.GetPlanEvaluationStatus)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/paginators/#getplanevaluationstatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetPlanEvaluationStatusRequestPaginateTypeDef]
    ) -> PageIterator[GetPlanEvaluationStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/paginator/GetPlanEvaluationStatus.html#ARCRegionswitch.Paginator.GetPlanEvaluationStatus.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/paginators/#getplanevaluationstatuspaginator)
        """

if TYPE_CHECKING:
    _GetPlanExecutionPaginatorBase = Paginator[GetPlanExecutionResponsePaginatorTypeDef]
else:
    _GetPlanExecutionPaginatorBase = Paginator  # type: ignore[assignment]

class GetPlanExecutionPaginator(_GetPlanExecutionPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/paginator/GetPlanExecution.html#ARCRegionswitch.Paginator.GetPlanExecution)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/paginators/#getplanexecutionpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetPlanExecutionRequestPaginateTypeDef]
    ) -> PageIterator[GetPlanExecutionResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/paginator/GetPlanExecution.html#ARCRegionswitch.Paginator.GetPlanExecution.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/paginators/#getplanexecutionpaginator)
        """

if TYPE_CHECKING:
    _ListPlanExecutionEventsPaginatorBase = Paginator[ListPlanExecutionEventsResponseTypeDef]
else:
    _ListPlanExecutionEventsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPlanExecutionEventsPaginator(_ListPlanExecutionEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/paginator/ListPlanExecutionEvents.html#ARCRegionswitch.Paginator.ListPlanExecutionEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/paginators/#listplanexecutioneventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPlanExecutionEventsRequestPaginateTypeDef]
    ) -> PageIterator[ListPlanExecutionEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/paginator/ListPlanExecutionEvents.html#ARCRegionswitch.Paginator.ListPlanExecutionEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/paginators/#listplanexecutioneventspaginator)
        """

if TYPE_CHECKING:
    _ListPlanExecutionsPaginatorBase = Paginator[ListPlanExecutionsResponseTypeDef]
else:
    _ListPlanExecutionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPlanExecutionsPaginator(_ListPlanExecutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/paginator/ListPlanExecutions.html#ARCRegionswitch.Paginator.ListPlanExecutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/paginators/#listplanexecutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPlanExecutionsRequestPaginateTypeDef]
    ) -> PageIterator[ListPlanExecutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/paginator/ListPlanExecutions.html#ARCRegionswitch.Paginator.ListPlanExecutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/paginators/#listplanexecutionspaginator)
        """

if TYPE_CHECKING:
    _ListPlansInRegionPaginatorBase = Paginator[ListPlansInRegionResponseTypeDef]
else:
    _ListPlansInRegionPaginatorBase = Paginator  # type: ignore[assignment]

class ListPlansInRegionPaginator(_ListPlansInRegionPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/paginator/ListPlansInRegion.html#ARCRegionswitch.Paginator.ListPlansInRegion)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/paginators/#listplansinregionpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPlansInRegionRequestPaginateTypeDef]
    ) -> PageIterator[ListPlansInRegionResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/paginator/ListPlansInRegion.html#ARCRegionswitch.Paginator.ListPlansInRegion.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/paginators/#listplansinregionpaginator)
        """

if TYPE_CHECKING:
    _ListPlansPaginatorBase = Paginator[ListPlansResponseTypeDef]
else:
    _ListPlansPaginatorBase = Paginator  # type: ignore[assignment]

class ListPlansPaginator(_ListPlansPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/paginator/ListPlans.html#ARCRegionswitch.Paginator.ListPlans)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/paginators/#listplanspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPlansRequestPaginateTypeDef]
    ) -> PageIterator[ListPlansResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/paginator/ListPlans.html#ARCRegionswitch.Paginator.ListPlans.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/paginators/#listplanspaginator)
        """

if TYPE_CHECKING:
    _ListRoute53HealthChecksInRegionPaginatorBase = Paginator[
        ListRoute53HealthChecksInRegionResponseTypeDef
    ]
else:
    _ListRoute53HealthChecksInRegionPaginatorBase = Paginator  # type: ignore[assignment]

class ListRoute53HealthChecksInRegionPaginator(_ListRoute53HealthChecksInRegionPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/paginator/ListRoute53HealthChecksInRegion.html#ARCRegionswitch.Paginator.ListRoute53HealthChecksInRegion)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/paginators/#listroute53healthchecksinregionpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRoute53HealthChecksInRegionRequestPaginateTypeDef]
    ) -> PageIterator[ListRoute53HealthChecksInRegionResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/paginator/ListRoute53HealthChecksInRegion.html#ARCRegionswitch.Paginator.ListRoute53HealthChecksInRegion.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/paginators/#listroute53healthchecksinregionpaginator)
        """

if TYPE_CHECKING:
    _ListRoute53HealthChecksPaginatorBase = Paginator[ListRoute53HealthChecksResponseTypeDef]
else:
    _ListRoute53HealthChecksPaginatorBase = Paginator  # type: ignore[assignment]

class ListRoute53HealthChecksPaginator(_ListRoute53HealthChecksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/paginator/ListRoute53HealthChecks.html#ARCRegionswitch.Paginator.ListRoute53HealthChecks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/paginators/#listroute53healthcheckspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRoute53HealthChecksRequestPaginateTypeDef]
    ) -> PageIterator[ListRoute53HealthChecksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/paginator/ListRoute53HealthChecks.html#ARCRegionswitch.Paginator.ListRoute53HealthChecks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/paginators/#listroute53healthcheckspaginator)
        """
