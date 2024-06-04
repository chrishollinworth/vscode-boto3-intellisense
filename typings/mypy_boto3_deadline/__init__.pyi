"""
Main interface for deadline service.

Usage::

    ```python
    import boto3
    from mypy_boto3_deadline import (
        Client,
        DeadlineCloudClient,
        FleetActiveWaiter,
        GetSessionsStatisticsAggregationPaginator,
        JobCreateCompleteWaiter,
        LicenseEndpointDeletedWaiter,
        LicenseEndpointValidWaiter,
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
        ListSessionsForWorkerPaginator,
        ListSessionsPaginator,
        ListStepConsumersPaginator,
        ListStepDependenciesPaginator,
        ListStepsPaginator,
        ListStorageProfilesForQueuePaginator,
        ListStorageProfilesPaginator,
        ListTasksPaginator,
        ListWorkersPaginator,
        QueueFleetAssociationStoppedWaiter,
        QueueSchedulingBlockedWaiter,
        QueueSchedulingWaiter,
    )

    session = boto3.Session()

    client: DeadlineCloudClient = boto3.client("deadline")
    session_client: DeadlineCloudClient = session.client("deadline")

    fleet_active_waiter: FleetActiveWaiter = client.get_waiter("fleet_active")
    job_create_complete_waiter: JobCreateCompleteWaiter = client.get_waiter("job_create_complete")
    license_endpoint_deleted_waiter: LicenseEndpointDeletedWaiter = client.get_waiter("license_endpoint_deleted")
    license_endpoint_valid_waiter: LicenseEndpointValidWaiter = client.get_waiter("license_endpoint_valid")
    queue_fleet_association_stopped_waiter: QueueFleetAssociationStoppedWaiter = client.get_waiter("queue_fleet_association_stopped")
    queue_scheduling_waiter: QueueSchedulingWaiter = client.get_waiter("queue_scheduling")
    queue_scheduling_blocked_waiter: QueueSchedulingBlockedWaiter = client.get_waiter("queue_scheduling_blocked")

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

from .client import DeadlineCloudClient
from .paginator import (
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
from .waiter import (
    FleetActiveWaiter,
    JobCreateCompleteWaiter,
    LicenseEndpointDeletedWaiter,
    LicenseEndpointValidWaiter,
    QueueFleetAssociationStoppedWaiter,
    QueueSchedulingBlockedWaiter,
    QueueSchedulingWaiter,
)

Client = DeadlineCloudClient

__all__ = (
    "Client",
    "DeadlineCloudClient",
    "FleetActiveWaiter",
    "GetSessionsStatisticsAggregationPaginator",
    "JobCreateCompleteWaiter",
    "LicenseEndpointDeletedWaiter",
    "LicenseEndpointValidWaiter",
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
    "ListSessionsForWorkerPaginator",
    "ListSessionsPaginator",
    "ListStepConsumersPaginator",
    "ListStepDependenciesPaginator",
    "ListStepsPaginator",
    "ListStorageProfilesForQueuePaginator",
    "ListStorageProfilesPaginator",
    "ListTasksPaginator",
    "ListWorkersPaginator",
    "QueueFleetAssociationStoppedWaiter",
    "QueueSchedulingBlockedWaiter",
    "QueueSchedulingWaiter",
)
