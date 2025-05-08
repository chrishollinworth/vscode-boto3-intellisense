"""
Type annotations for deadline service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_deadline.client import DeadlineCloudClient
    from mypy_boto3_deadline.paginator import (
        GetSessionsStatisticsAggregationPaginator,
        ListAvailableMeteredProductsPaginator,
        ListBudgetsPaginator,
        ListFarmMembersPaginator,
        ListFarmsPaginator,
        ListFleetMembersPaginator,
        ListFleetsPaginator,
        ListJobMembersPaginator,
        ListJobParameterDefinitionsPaginator,
        ListJobsPaginator,
        ListLicenseEndpointsPaginator,
        ListLimitsPaginator,
        ListMeteredProductsPaginator,
        ListMonitorsPaginator,
        ListQueueEnvironmentsPaginator,
        ListQueueFleetAssociationsPaginator,
        ListQueueLimitAssociationsPaginator,
        ListQueueMembersPaginator,
        ListQueuesPaginator,
        ListSessionActionsPaginator,
        ListSessionsForWorkerPaginator,
        ListSessionsPaginator,
        ListStepConsumersPaginator,
        ListStepDependenciesPaginator,
        ListStepsPaginator,
        ListStorageProfilesForQueuePaginator,
        ListStorageProfilesPaginator,
        ListTasksPaginator,
        ListWorkersPaginator,
    )

    session = Session()
    client: DeadlineCloudClient = session.client("deadline")

    get_sessions_statistics_aggregation_paginator: GetSessionsStatisticsAggregationPaginator = client.get_paginator("get_sessions_statistics_aggregation")
    list_available_metered_products_paginator: ListAvailableMeteredProductsPaginator = client.get_paginator("list_available_metered_products")
    list_budgets_paginator: ListBudgetsPaginator = client.get_paginator("list_budgets")
    list_farm_members_paginator: ListFarmMembersPaginator = client.get_paginator("list_farm_members")
    list_farms_paginator: ListFarmsPaginator = client.get_paginator("list_farms")
    list_fleet_members_paginator: ListFleetMembersPaginator = client.get_paginator("list_fleet_members")
    list_fleets_paginator: ListFleetsPaginator = client.get_paginator("list_fleets")
    list_job_members_paginator: ListJobMembersPaginator = client.get_paginator("list_job_members")
    list_job_parameter_definitions_paginator: ListJobParameterDefinitionsPaginator = client.get_paginator("list_job_parameter_definitions")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    list_license_endpoints_paginator: ListLicenseEndpointsPaginator = client.get_paginator("list_license_endpoints")
    list_limits_paginator: ListLimitsPaginator = client.get_paginator("list_limits")
    list_metered_products_paginator: ListMeteredProductsPaginator = client.get_paginator("list_metered_products")
    list_monitors_paginator: ListMonitorsPaginator = client.get_paginator("list_monitors")
    list_queue_environments_paginator: ListQueueEnvironmentsPaginator = client.get_paginator("list_queue_environments")
    list_queue_fleet_associations_paginator: ListQueueFleetAssociationsPaginator = client.get_paginator("list_queue_fleet_associations")
    list_queue_limit_associations_paginator: ListQueueLimitAssociationsPaginator = client.get_paginator("list_queue_limit_associations")
    list_queue_members_paginator: ListQueueMembersPaginator = client.get_paginator("list_queue_members")
    list_queues_paginator: ListQueuesPaginator = client.get_paginator("list_queues")
    list_session_actions_paginator: ListSessionActionsPaginator = client.get_paginator("list_session_actions")
    list_sessions_for_worker_paginator: ListSessionsForWorkerPaginator = client.get_paginator("list_sessions_for_worker")
    list_sessions_paginator: ListSessionsPaginator = client.get_paginator("list_sessions")
    list_step_consumers_paginator: ListStepConsumersPaginator = client.get_paginator("list_step_consumers")
    list_step_dependencies_paginator: ListStepDependenciesPaginator = client.get_paginator("list_step_dependencies")
    list_steps_paginator: ListStepsPaginator = client.get_paginator("list_steps")
    list_storage_profiles_for_queue_paginator: ListStorageProfilesForQueuePaginator = client.get_paginator("list_storage_profiles_for_queue")
    list_storage_profiles_paginator: ListStorageProfilesPaginator = client.get_paginator("list_storage_profiles")
    list_tasks_paginator: ListTasksPaginator = client.get_paginator("list_tasks")
    list_workers_paginator: ListWorkersPaginator = client.get_paginator("list_workers")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetSessionsStatisticsAggregationRequestPaginateTypeDef,
    GetSessionsStatisticsAggregationResponseTypeDef,
    ListAvailableMeteredProductsRequestPaginateTypeDef,
    ListAvailableMeteredProductsResponseTypeDef,
    ListBudgetsRequestPaginateTypeDef,
    ListBudgetsResponseTypeDef,
    ListFarmMembersRequestPaginateTypeDef,
    ListFarmMembersResponseTypeDef,
    ListFarmsRequestPaginateTypeDef,
    ListFarmsResponseTypeDef,
    ListFleetMembersRequestPaginateTypeDef,
    ListFleetMembersResponseTypeDef,
    ListFleetsRequestPaginateTypeDef,
    ListFleetsResponseTypeDef,
    ListJobMembersRequestPaginateTypeDef,
    ListJobMembersResponseTypeDef,
    ListJobParameterDefinitionsRequestPaginateTypeDef,
    ListJobParameterDefinitionsResponseTypeDef,
    ListJobsRequestPaginateTypeDef,
    ListJobsResponseTypeDef,
    ListLicenseEndpointsRequestPaginateTypeDef,
    ListLicenseEndpointsResponseTypeDef,
    ListLimitsRequestPaginateTypeDef,
    ListLimitsResponseTypeDef,
    ListMeteredProductsRequestPaginateTypeDef,
    ListMeteredProductsResponseTypeDef,
    ListMonitorsRequestPaginateTypeDef,
    ListMonitorsResponseTypeDef,
    ListQueueEnvironmentsRequestPaginateTypeDef,
    ListQueueEnvironmentsResponseTypeDef,
    ListQueueFleetAssociationsRequestPaginateTypeDef,
    ListQueueFleetAssociationsResponseTypeDef,
    ListQueueLimitAssociationsRequestPaginateTypeDef,
    ListQueueLimitAssociationsResponseTypeDef,
    ListQueueMembersRequestPaginateTypeDef,
    ListQueueMembersResponseTypeDef,
    ListQueuesRequestPaginateTypeDef,
    ListQueuesResponseTypeDef,
    ListSessionActionsRequestPaginateTypeDef,
    ListSessionActionsResponseTypeDef,
    ListSessionsForWorkerRequestPaginateTypeDef,
    ListSessionsForWorkerResponseTypeDef,
    ListSessionsRequestPaginateTypeDef,
    ListSessionsResponseTypeDef,
    ListStepConsumersRequestPaginateTypeDef,
    ListStepConsumersResponseTypeDef,
    ListStepDependenciesRequestPaginateTypeDef,
    ListStepDependenciesResponseTypeDef,
    ListStepsRequestPaginateTypeDef,
    ListStepsResponseTypeDef,
    ListStorageProfilesForQueueRequestPaginateTypeDef,
    ListStorageProfilesForQueueResponseTypeDef,
    ListStorageProfilesRequestPaginateTypeDef,
    ListStorageProfilesResponseTypeDef,
    ListTasksRequestPaginateTypeDef,
    ListTasksResponseTypeDef,
    ListWorkersRequestPaginateTypeDef,
    ListWorkersResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetSessionsStatisticsAggregationPaginator",
    "ListAvailableMeteredProductsPaginator",
    "ListBudgetsPaginator",
    "ListFarmMembersPaginator",
    "ListFarmsPaginator",
    "ListFleetMembersPaginator",
    "ListFleetsPaginator",
    "ListJobMembersPaginator",
    "ListJobParameterDefinitionsPaginator",
    "ListJobsPaginator",
    "ListLicenseEndpointsPaginator",
    "ListLimitsPaginator",
    "ListMeteredProductsPaginator",
    "ListMonitorsPaginator",
    "ListQueueEnvironmentsPaginator",
    "ListQueueFleetAssociationsPaginator",
    "ListQueueLimitAssociationsPaginator",
    "ListQueueMembersPaginator",
    "ListQueuesPaginator",
    "ListSessionActionsPaginator",
    "ListSessionsForWorkerPaginator",
    "ListSessionsPaginator",
    "ListStepConsumersPaginator",
    "ListStepDependenciesPaginator",
    "ListStepsPaginator",
    "ListStorageProfilesForQueuePaginator",
    "ListStorageProfilesPaginator",
    "ListTasksPaginator",
    "ListWorkersPaginator",
)

if TYPE_CHECKING:
    _GetSessionsStatisticsAggregationPaginatorBase = Paginator[
        GetSessionsStatisticsAggregationResponseTypeDef
    ]
else:
    _GetSessionsStatisticsAggregationPaginatorBase = Paginator  # type: ignore[assignment]

class GetSessionsStatisticsAggregationPaginator(_GetSessionsStatisticsAggregationPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/GetSessionsStatisticsAggregation.html#DeadlineCloud.Paginator.GetSessionsStatisticsAggregation)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#getsessionsstatisticsaggregationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetSessionsStatisticsAggregationRequestPaginateTypeDef]
    ) -> PageIterator[GetSessionsStatisticsAggregationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/GetSessionsStatisticsAggregation.html#DeadlineCloud.Paginator.GetSessionsStatisticsAggregation.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#getsessionsstatisticsaggregationpaginator)
        """

if TYPE_CHECKING:
    _ListAvailableMeteredProductsPaginatorBase = Paginator[
        ListAvailableMeteredProductsResponseTypeDef
    ]
else:
    _ListAvailableMeteredProductsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAvailableMeteredProductsPaginator(_ListAvailableMeteredProductsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListAvailableMeteredProducts.html#DeadlineCloud.Paginator.ListAvailableMeteredProducts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listavailablemeteredproductspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAvailableMeteredProductsRequestPaginateTypeDef]
    ) -> PageIterator[ListAvailableMeteredProductsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListAvailableMeteredProducts.html#DeadlineCloud.Paginator.ListAvailableMeteredProducts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listavailablemeteredproductspaginator)
        """

if TYPE_CHECKING:
    _ListBudgetsPaginatorBase = Paginator[ListBudgetsResponseTypeDef]
else:
    _ListBudgetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBudgetsPaginator(_ListBudgetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListBudgets.html#DeadlineCloud.Paginator.ListBudgets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listbudgetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBudgetsRequestPaginateTypeDef]
    ) -> PageIterator[ListBudgetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListBudgets.html#DeadlineCloud.Paginator.ListBudgets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listbudgetspaginator)
        """

if TYPE_CHECKING:
    _ListFarmMembersPaginatorBase = Paginator[ListFarmMembersResponseTypeDef]
else:
    _ListFarmMembersPaginatorBase = Paginator  # type: ignore[assignment]

class ListFarmMembersPaginator(_ListFarmMembersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListFarmMembers.html#DeadlineCloud.Paginator.ListFarmMembers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listfarmmemberspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFarmMembersRequestPaginateTypeDef]
    ) -> PageIterator[ListFarmMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListFarmMembers.html#DeadlineCloud.Paginator.ListFarmMembers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listfarmmemberspaginator)
        """

if TYPE_CHECKING:
    _ListFarmsPaginatorBase = Paginator[ListFarmsResponseTypeDef]
else:
    _ListFarmsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFarmsPaginator(_ListFarmsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListFarms.html#DeadlineCloud.Paginator.ListFarms)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listfarmspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFarmsRequestPaginateTypeDef]
    ) -> PageIterator[ListFarmsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListFarms.html#DeadlineCloud.Paginator.ListFarms.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listfarmspaginator)
        """

if TYPE_CHECKING:
    _ListFleetMembersPaginatorBase = Paginator[ListFleetMembersResponseTypeDef]
else:
    _ListFleetMembersPaginatorBase = Paginator  # type: ignore[assignment]

class ListFleetMembersPaginator(_ListFleetMembersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListFleetMembers.html#DeadlineCloud.Paginator.ListFleetMembers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listfleetmemberspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFleetMembersRequestPaginateTypeDef]
    ) -> PageIterator[ListFleetMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListFleetMembers.html#DeadlineCloud.Paginator.ListFleetMembers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listfleetmemberspaginator)
        """

if TYPE_CHECKING:
    _ListFleetsPaginatorBase = Paginator[ListFleetsResponseTypeDef]
else:
    _ListFleetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFleetsPaginator(_ListFleetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListFleets.html#DeadlineCloud.Paginator.ListFleets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listfleetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFleetsRequestPaginateTypeDef]
    ) -> PageIterator[ListFleetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListFleets.html#DeadlineCloud.Paginator.ListFleets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listfleetspaginator)
        """

if TYPE_CHECKING:
    _ListJobMembersPaginatorBase = Paginator[ListJobMembersResponseTypeDef]
else:
    _ListJobMembersPaginatorBase = Paginator  # type: ignore[assignment]

class ListJobMembersPaginator(_ListJobMembersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListJobMembers.html#DeadlineCloud.Paginator.ListJobMembers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listjobmemberspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobMembersRequestPaginateTypeDef]
    ) -> PageIterator[ListJobMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListJobMembers.html#DeadlineCloud.Paginator.ListJobMembers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listjobmemberspaginator)
        """

if TYPE_CHECKING:
    _ListJobParameterDefinitionsPaginatorBase = Paginator[
        ListJobParameterDefinitionsResponseTypeDef
    ]
else:
    _ListJobParameterDefinitionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListJobParameterDefinitionsPaginator(_ListJobParameterDefinitionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListJobParameterDefinitions.html#DeadlineCloud.Paginator.ListJobParameterDefinitions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listjobparameterdefinitionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobParameterDefinitionsRequestPaginateTypeDef]
    ) -> PageIterator[ListJobParameterDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListJobParameterDefinitions.html#DeadlineCloud.Paginator.ListJobParameterDefinitions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listjobparameterdefinitionspaginator)
        """

if TYPE_CHECKING:
    _ListJobsPaginatorBase = Paginator[ListJobsResponseTypeDef]
else:
    _ListJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListJobsPaginator(_ListJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListJobs.html#DeadlineCloud.Paginator.ListJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListJobs.html#DeadlineCloud.Paginator.ListJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listjobspaginator)
        """

if TYPE_CHECKING:
    _ListLicenseEndpointsPaginatorBase = Paginator[ListLicenseEndpointsResponseTypeDef]
else:
    _ListLicenseEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class ListLicenseEndpointsPaginator(_ListLicenseEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListLicenseEndpoints.html#DeadlineCloud.Paginator.ListLicenseEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listlicenseendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLicenseEndpointsRequestPaginateTypeDef]
    ) -> PageIterator[ListLicenseEndpointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListLicenseEndpoints.html#DeadlineCloud.Paginator.ListLicenseEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listlicenseendpointspaginator)
        """

if TYPE_CHECKING:
    _ListLimitsPaginatorBase = Paginator[ListLimitsResponseTypeDef]
else:
    _ListLimitsPaginatorBase = Paginator  # type: ignore[assignment]

class ListLimitsPaginator(_ListLimitsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListLimits.html#DeadlineCloud.Paginator.ListLimits)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listlimitspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLimitsRequestPaginateTypeDef]
    ) -> PageIterator[ListLimitsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListLimits.html#DeadlineCloud.Paginator.ListLimits.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listlimitspaginator)
        """

if TYPE_CHECKING:
    _ListMeteredProductsPaginatorBase = Paginator[ListMeteredProductsResponseTypeDef]
else:
    _ListMeteredProductsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMeteredProductsPaginator(_ListMeteredProductsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListMeteredProducts.html#DeadlineCloud.Paginator.ListMeteredProducts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listmeteredproductspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMeteredProductsRequestPaginateTypeDef]
    ) -> PageIterator[ListMeteredProductsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListMeteredProducts.html#DeadlineCloud.Paginator.ListMeteredProducts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listmeteredproductspaginator)
        """

if TYPE_CHECKING:
    _ListMonitorsPaginatorBase = Paginator[ListMonitorsResponseTypeDef]
else:
    _ListMonitorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMonitorsPaginator(_ListMonitorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListMonitors.html#DeadlineCloud.Paginator.ListMonitors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listmonitorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMonitorsRequestPaginateTypeDef]
    ) -> PageIterator[ListMonitorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListMonitors.html#DeadlineCloud.Paginator.ListMonitors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listmonitorspaginator)
        """

if TYPE_CHECKING:
    _ListQueueEnvironmentsPaginatorBase = Paginator[ListQueueEnvironmentsResponseTypeDef]
else:
    _ListQueueEnvironmentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListQueueEnvironmentsPaginator(_ListQueueEnvironmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListQueueEnvironments.html#DeadlineCloud.Paginator.ListQueueEnvironments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listqueueenvironmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListQueueEnvironmentsRequestPaginateTypeDef]
    ) -> PageIterator[ListQueueEnvironmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListQueueEnvironments.html#DeadlineCloud.Paginator.ListQueueEnvironments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listqueueenvironmentspaginator)
        """

if TYPE_CHECKING:
    _ListQueueFleetAssociationsPaginatorBase = Paginator[ListQueueFleetAssociationsResponseTypeDef]
else:
    _ListQueueFleetAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListQueueFleetAssociationsPaginator(_ListQueueFleetAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListQueueFleetAssociations.html#DeadlineCloud.Paginator.ListQueueFleetAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listqueuefleetassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListQueueFleetAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListQueueFleetAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListQueueFleetAssociations.html#DeadlineCloud.Paginator.ListQueueFleetAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listqueuefleetassociationspaginator)
        """

if TYPE_CHECKING:
    _ListQueueLimitAssociationsPaginatorBase = Paginator[ListQueueLimitAssociationsResponseTypeDef]
else:
    _ListQueueLimitAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListQueueLimitAssociationsPaginator(_ListQueueLimitAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListQueueLimitAssociations.html#DeadlineCloud.Paginator.ListQueueLimitAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listqueuelimitassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListQueueLimitAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListQueueLimitAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListQueueLimitAssociations.html#DeadlineCloud.Paginator.ListQueueLimitAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listqueuelimitassociationspaginator)
        """

if TYPE_CHECKING:
    _ListQueueMembersPaginatorBase = Paginator[ListQueueMembersResponseTypeDef]
else:
    _ListQueueMembersPaginatorBase = Paginator  # type: ignore[assignment]

class ListQueueMembersPaginator(_ListQueueMembersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListQueueMembers.html#DeadlineCloud.Paginator.ListQueueMembers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listqueuememberspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListQueueMembersRequestPaginateTypeDef]
    ) -> PageIterator[ListQueueMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListQueueMembers.html#DeadlineCloud.Paginator.ListQueueMembers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listqueuememberspaginator)
        """

if TYPE_CHECKING:
    _ListQueuesPaginatorBase = Paginator[ListQueuesResponseTypeDef]
else:
    _ListQueuesPaginatorBase = Paginator  # type: ignore[assignment]

class ListQueuesPaginator(_ListQueuesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListQueues.html#DeadlineCloud.Paginator.ListQueues)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listqueuespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListQueuesRequestPaginateTypeDef]
    ) -> PageIterator[ListQueuesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListQueues.html#DeadlineCloud.Paginator.ListQueues.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listqueuespaginator)
        """

if TYPE_CHECKING:
    _ListSessionActionsPaginatorBase = Paginator[ListSessionActionsResponseTypeDef]
else:
    _ListSessionActionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSessionActionsPaginator(_ListSessionActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListSessionActions.html#DeadlineCloud.Paginator.ListSessionActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listsessionactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSessionActionsRequestPaginateTypeDef]
    ) -> PageIterator[ListSessionActionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListSessionActions.html#DeadlineCloud.Paginator.ListSessionActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listsessionactionspaginator)
        """

if TYPE_CHECKING:
    _ListSessionsForWorkerPaginatorBase = Paginator[ListSessionsForWorkerResponseTypeDef]
else:
    _ListSessionsForWorkerPaginatorBase = Paginator  # type: ignore[assignment]

class ListSessionsForWorkerPaginator(_ListSessionsForWorkerPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListSessionsForWorker.html#DeadlineCloud.Paginator.ListSessionsForWorker)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listsessionsforworkerpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSessionsForWorkerRequestPaginateTypeDef]
    ) -> PageIterator[ListSessionsForWorkerResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListSessionsForWorker.html#DeadlineCloud.Paginator.ListSessionsForWorker.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listsessionsforworkerpaginator)
        """

if TYPE_CHECKING:
    _ListSessionsPaginatorBase = Paginator[ListSessionsResponseTypeDef]
else:
    _ListSessionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSessionsPaginator(_ListSessionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListSessions.html#DeadlineCloud.Paginator.ListSessions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listsessionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSessionsRequestPaginateTypeDef]
    ) -> PageIterator[ListSessionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListSessions.html#DeadlineCloud.Paginator.ListSessions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listsessionspaginator)
        """

if TYPE_CHECKING:
    _ListStepConsumersPaginatorBase = Paginator[ListStepConsumersResponseTypeDef]
else:
    _ListStepConsumersPaginatorBase = Paginator  # type: ignore[assignment]

class ListStepConsumersPaginator(_ListStepConsumersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListStepConsumers.html#DeadlineCloud.Paginator.ListStepConsumers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#liststepconsumerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStepConsumersRequestPaginateTypeDef]
    ) -> PageIterator[ListStepConsumersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListStepConsumers.html#DeadlineCloud.Paginator.ListStepConsumers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#liststepconsumerspaginator)
        """

if TYPE_CHECKING:
    _ListStepDependenciesPaginatorBase = Paginator[ListStepDependenciesResponseTypeDef]
else:
    _ListStepDependenciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListStepDependenciesPaginator(_ListStepDependenciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListStepDependencies.html#DeadlineCloud.Paginator.ListStepDependencies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#liststepdependenciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStepDependenciesRequestPaginateTypeDef]
    ) -> PageIterator[ListStepDependenciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListStepDependencies.html#DeadlineCloud.Paginator.ListStepDependencies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#liststepdependenciespaginator)
        """

if TYPE_CHECKING:
    _ListStepsPaginatorBase = Paginator[ListStepsResponseTypeDef]
else:
    _ListStepsPaginatorBase = Paginator  # type: ignore[assignment]

class ListStepsPaginator(_ListStepsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListSteps.html#DeadlineCloud.Paginator.ListSteps)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#liststepspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStepsRequestPaginateTypeDef]
    ) -> PageIterator[ListStepsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListSteps.html#DeadlineCloud.Paginator.ListSteps.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#liststepspaginator)
        """

if TYPE_CHECKING:
    _ListStorageProfilesForQueuePaginatorBase = Paginator[
        ListStorageProfilesForQueueResponseTypeDef
    ]
else:
    _ListStorageProfilesForQueuePaginatorBase = Paginator  # type: ignore[assignment]

class ListStorageProfilesForQueuePaginator(_ListStorageProfilesForQueuePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListStorageProfilesForQueue.html#DeadlineCloud.Paginator.ListStorageProfilesForQueue)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#liststorageprofilesforqueuepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStorageProfilesForQueueRequestPaginateTypeDef]
    ) -> PageIterator[ListStorageProfilesForQueueResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListStorageProfilesForQueue.html#DeadlineCloud.Paginator.ListStorageProfilesForQueue.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#liststorageprofilesforqueuepaginator)
        """

if TYPE_CHECKING:
    _ListStorageProfilesPaginatorBase = Paginator[ListStorageProfilesResponseTypeDef]
else:
    _ListStorageProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class ListStorageProfilesPaginator(_ListStorageProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListStorageProfiles.html#DeadlineCloud.Paginator.ListStorageProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#liststorageprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStorageProfilesRequestPaginateTypeDef]
    ) -> PageIterator[ListStorageProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListStorageProfiles.html#DeadlineCloud.Paginator.ListStorageProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#liststorageprofilespaginator)
        """

if TYPE_CHECKING:
    _ListTasksPaginatorBase = Paginator[ListTasksResponseTypeDef]
else:
    _ListTasksPaginatorBase = Paginator  # type: ignore[assignment]

class ListTasksPaginator(_ListTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListTasks.html#DeadlineCloud.Paginator.ListTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listtaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTasksRequestPaginateTypeDef]
    ) -> PageIterator[ListTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListTasks.html#DeadlineCloud.Paginator.ListTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listtaskspaginator)
        """

if TYPE_CHECKING:
    _ListWorkersPaginatorBase = Paginator[ListWorkersResponseTypeDef]
else:
    _ListWorkersPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkersPaginator(_ListWorkersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListWorkers.html#DeadlineCloud.Paginator.ListWorkers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listworkerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkersRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/paginator/ListWorkers.html#DeadlineCloud.Paginator.ListWorkers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators/#listworkerspaginator)
        """
