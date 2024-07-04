"""
Type annotations for deadline service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_deadline import DeadlineCloudClient
    from mypy_boto3_deadline.paginator import (
        GetSessionsStatisticsAggregationPaginator,
        ListAvailableMeteredProductsPaginator,
        ListBudgetsPaginator,
        ListFarmMembersPaginator,
        ListFarmsPaginator,
        ListFleetMembersPaginator,
        ListFleetsPaginator,
        ListJobMembersPaginator,
        ListJobsPaginator,
        ListLicenseEndpointsPaginator,
        ListMeteredProductsPaginator,
        ListMonitorsPaginator,
        ListQueueEnvironmentsPaginator,
        ListQueueFleetAssociationsPaginator,
        ListQueueMembersPaginator,
        ListQueuesPaginator,
        ListSessionActionsPaginator,
        ListSessionsPaginator,
        ListSessionsForWorkerPaginator,
        ListStepConsumersPaginator,
        ListStepDependenciesPaginator,
        ListStepsPaginator,
        ListStorageProfilesPaginator,
        ListStorageProfilesForQueuePaginator,
        ListTasksPaginator,
        ListWorkersPaginator,
    )

    client: DeadlineCloudClient = boto3.client("deadline")

    get_sessions_statistics_aggregation_paginator: GetSessionsStatisticsAggregationPaginator = client.get_paginator("get_sessions_statistics_aggregation")
    list_available_metered_products_paginator: ListAvailableMeteredProductsPaginator = client.get_paginator("list_available_metered_products")
    list_budgets_paginator: ListBudgetsPaginator = client.get_paginator("list_budgets")
    list_farm_members_paginator: ListFarmMembersPaginator = client.get_paginator("list_farm_members")
    list_farms_paginator: ListFarmsPaginator = client.get_paginator("list_farms")
    list_fleet_members_paginator: ListFleetMembersPaginator = client.get_paginator("list_fleet_members")
    list_fleets_paginator: ListFleetsPaginator = client.get_paginator("list_fleets")
    list_job_members_paginator: ListJobMembersPaginator = client.get_paginator("list_job_members")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    list_license_endpoints_paginator: ListLicenseEndpointsPaginator = client.get_paginator("list_license_endpoints")
    list_metered_products_paginator: ListMeteredProductsPaginator = client.get_paginator("list_metered_products")
    list_monitors_paginator: ListMonitorsPaginator = client.get_paginator("list_monitors")
    list_queue_environments_paginator: ListQueueEnvironmentsPaginator = client.get_paginator("list_queue_environments")
    list_queue_fleet_associations_paginator: ListQueueFleetAssociationsPaginator = client.get_paginator("list_queue_fleet_associations")
    list_queue_members_paginator: ListQueueMembersPaginator = client.get_paginator("list_queue_members")
    list_queues_paginator: ListQueuesPaginator = client.get_paginator("list_queues")
    list_session_actions_paginator: ListSessionActionsPaginator = client.get_paginator("list_session_actions")
    list_sessions_paginator: ListSessionsPaginator = client.get_paginator("list_sessions")
    list_sessions_for_worker_paginator: ListSessionsForWorkerPaginator = client.get_paginator("list_sessions_for_worker")
    list_step_consumers_paginator: ListStepConsumersPaginator = client.get_paginator("list_step_consumers")
    list_step_dependencies_paginator: ListStepDependenciesPaginator = client.get_paginator("list_step_dependencies")
    list_steps_paginator: ListStepsPaginator = client.get_paginator("list_steps")
    list_storage_profiles_paginator: ListStorageProfilesPaginator = client.get_paginator("list_storage_profiles")
    list_storage_profiles_for_queue_paginator: ListStorageProfilesForQueuePaginator = client.get_paginator("list_storage_profiles_for_queue")
    list_tasks_paginator: ListTasksPaginator = client.get_paginator("list_tasks")
    list_workers_paginator: ListWorkersPaginator = client.get_paginator("list_workers")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import BudgetStatusType, FleetStatusType, QueueStatusType
from .type_defs import (
    GetSessionsStatisticsAggregationResponseTypeDef,
    ListAvailableMeteredProductsResponseTypeDef,
    ListBudgetsResponseTypeDef,
    ListFarmMembersResponseTypeDef,
    ListFarmsResponseTypeDef,
    ListFleetMembersResponseTypeDef,
    ListFleetsResponseTypeDef,
    ListJobMembersResponseTypeDef,
    ListJobsResponseTypeDef,
    ListLicenseEndpointsResponseTypeDef,
    ListMeteredProductsResponseTypeDef,
    ListMonitorsResponseTypeDef,
    ListQueueEnvironmentsResponseTypeDef,
    ListQueueFleetAssociationsResponseTypeDef,
    ListQueueMembersResponseTypeDef,
    ListQueuesResponseTypeDef,
    ListSessionActionsResponseTypeDef,
    ListSessionsForWorkerResponseTypeDef,
    ListSessionsResponseTypeDef,
    ListStepConsumersResponseTypeDef,
    ListStepDependenciesResponseTypeDef,
    ListStepsResponseTypeDef,
    ListStorageProfilesForQueueResponseTypeDef,
    ListStorageProfilesResponseTypeDef,
    ListTasksResponseTypeDef,
    ListWorkersResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "GetSessionsStatisticsAggregationPaginator",
    "ListAvailableMeteredProductsPaginator",
    "ListBudgetsPaginator",
    "ListFarmMembersPaginator",
    "ListFarmsPaginator",
    "ListFleetMembersPaginator",
    "ListFleetsPaginator",
    "ListJobMembersPaginator",
    "ListJobsPaginator",
    "ListLicenseEndpointsPaginator",
    "ListMeteredProductsPaginator",
    "ListMonitorsPaginator",
    "ListQueueEnvironmentsPaginator",
    "ListQueueFleetAssociationsPaginator",
    "ListQueueMembersPaginator",
    "ListQueuesPaginator",
    "ListSessionActionsPaginator",
    "ListSessionsPaginator",
    "ListSessionsForWorkerPaginator",
    "ListStepConsumersPaginator",
    "ListStepDependenciesPaginator",
    "ListStepsPaginator",
    "ListStorageProfilesPaginator",
    "ListStorageProfilesForQueuePaginator",
    "ListTasksPaginator",
    "ListWorkersPaginator",
)

class GetSessionsStatisticsAggregationPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.GetSessionsStatisticsAggregation)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#getsessionsstatisticsaggregationpaginator)
    """

    def paginate(
        self, *, aggregationId: str, farmId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetSessionsStatisticsAggregationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.GetSessionsStatisticsAggregation.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#getsessionsstatisticsaggregationpaginator)
        """

class ListAvailableMeteredProductsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListAvailableMeteredProducts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listavailablemeteredproductspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAvailableMeteredProductsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListAvailableMeteredProducts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listavailablemeteredproductspaginator)
        """

class ListBudgetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListBudgets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listbudgetspaginator)
    """

    def paginate(
        self,
        *,
        farmId: str,
        status: BudgetStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBudgetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListBudgets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listbudgetspaginator)
        """

class ListFarmMembersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListFarmMembers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listfarmmemberspaginator)
    """

    def paginate(
        self, *, farmId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFarmMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListFarmMembers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listfarmmemberspaginator)
        """

class ListFarmsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListFarms)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listfarmspaginator)
    """

    def paginate(
        self, *, principalId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFarmsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListFarms.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listfarmspaginator)
        """

class ListFleetMembersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListFleetMembers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listfleetmemberspaginator)
    """

    def paginate(
        self, *, farmId: str, fleetId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFleetMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListFleetMembers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listfleetmemberspaginator)
        """

class ListFleetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListFleets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listfleetspaginator)
    """

    def paginate(
        self,
        *,
        farmId: str,
        displayName: str = None,
        principalId: str = None,
        status: FleetStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFleetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListFleets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listfleetspaginator)
        """

class ListJobMembersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListJobMembers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listjobmemberspaginator)
    """

    def paginate(
        self,
        *,
        farmId: str,
        jobId: str,
        queueId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListJobMembers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listjobmemberspaginator)
        """

class ListJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listjobspaginator)
    """

    def paginate(
        self,
        *,
        farmId: str,
        queueId: str,
        principalId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listjobspaginator)
        """

class ListLicenseEndpointsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListLicenseEndpoints)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listlicenseendpointspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLicenseEndpointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListLicenseEndpoints.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listlicenseendpointspaginator)
        """

class ListMeteredProductsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListMeteredProducts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listmeteredproductspaginator)
    """

    def paginate(
        self, *, licenseEndpointId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMeteredProductsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListMeteredProducts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listmeteredproductspaginator)
        """

class ListMonitorsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListMonitors)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listmonitorspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMonitorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListMonitors.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listmonitorspaginator)
        """

class ListQueueEnvironmentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListQueueEnvironments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listqueueenvironmentspaginator)
    """

    def paginate(
        self, *, farmId: str, queueId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQueueEnvironmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListQueueEnvironments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listqueueenvironmentspaginator)
        """

class ListQueueFleetAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListQueueFleetAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listqueuefleetassociationspaginator)
    """

    def paginate(
        self,
        *,
        farmId: str,
        fleetId: str = None,
        queueId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQueueFleetAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListQueueFleetAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listqueuefleetassociationspaginator)
        """

class ListQueueMembersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListQueueMembers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listqueuememberspaginator)
    """

    def paginate(
        self, *, farmId: str, queueId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQueueMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListQueueMembers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listqueuememberspaginator)
        """

class ListQueuesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListQueues)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listqueuespaginator)
    """

    def paginate(
        self,
        *,
        farmId: str,
        principalId: str = None,
        status: QueueStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQueuesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListQueues.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listqueuespaginator)
        """

class ListSessionActionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListSessionActions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listsessionactionspaginator)
    """

    def paginate(
        self,
        *,
        farmId: str,
        jobId: str,
        queueId: str,
        sessionId: str = None,
        taskId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSessionActionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListSessionActions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listsessionactionspaginator)
        """

class ListSessionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListSessions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listsessionspaginator)
    """

    def paginate(
        self,
        *,
        farmId: str,
        jobId: str,
        queueId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSessionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListSessions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listsessionspaginator)
        """

class ListSessionsForWorkerPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListSessionsForWorker)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listsessionsforworkerpaginator)
    """

    def paginate(
        self,
        *,
        farmId: str,
        fleetId: str,
        workerId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSessionsForWorkerResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListSessionsForWorker.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listsessionsforworkerpaginator)
        """

class ListStepConsumersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListStepConsumers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#liststepconsumerspaginator)
    """

    def paginate(
        self,
        *,
        farmId: str,
        jobId: str,
        queueId: str,
        stepId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStepConsumersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListStepConsumers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#liststepconsumerspaginator)
        """

class ListStepDependenciesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListStepDependencies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#liststepdependenciespaginator)
    """

    def paginate(
        self,
        *,
        farmId: str,
        jobId: str,
        queueId: str,
        stepId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStepDependenciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListStepDependencies.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#liststepdependenciespaginator)
        """

class ListStepsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListSteps)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#liststepspaginator)
    """

    def paginate(
        self,
        *,
        farmId: str,
        jobId: str,
        queueId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStepsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListSteps.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#liststepspaginator)
        """

class ListStorageProfilesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListStorageProfiles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#liststorageprofilespaginator)
    """

    def paginate(
        self, *, farmId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStorageProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListStorageProfiles.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#liststorageprofilespaginator)
        """

class ListStorageProfilesForQueuePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListStorageProfilesForQueue)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#liststorageprofilesforqueuepaginator)
    """

    def paginate(
        self, *, farmId: str, queueId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStorageProfilesForQueueResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListStorageProfilesForQueue.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#liststorageprofilesforqueuepaginator)
        """

class ListTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listtaskspaginator)
    """

    def paginate(
        self,
        *,
        farmId: str,
        jobId: str,
        queueId: str,
        stepId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listtaskspaginator)
        """

class ListWorkersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListWorkers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listworkerspaginator)
    """

    def paginate(
        self, *, farmId: str, fleetId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListWorkers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listworkerspaginator)
        """
