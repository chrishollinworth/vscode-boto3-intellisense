"""
Main interface for ecs service.

Usage::

    ```python
    import boto3
    from mypy_boto3_ecs import (
        Client,
        ECSClient,
        ListAccountSettingsPaginator,
        ListAttributesPaginator,
        ListClustersPaginator,
        ListContainerInstancesPaginator,
        ListServicesPaginator,
        ListTaskDefinitionFamiliesPaginator,
        ListTaskDefinitionsPaginator,
        ListTasksPaginator,
        ServicesInactiveWaiter,
        ServicesStableWaiter,
        TasksRunningWaiter,
        TasksStoppedWaiter,
    )

    session = boto3.Session()

    client: ECSClient = boto3.client("ecs")
    session_client: ECSClient = session.client("ecs")

    services_inactive_waiter: ServicesInactiveWaiter = client.get_waiter("services_inactive")
    services_stable_waiter: ServicesStableWaiter = client.get_waiter("services_stable")
    tasks_running_waiter: TasksRunningWaiter = client.get_waiter("tasks_running")
    tasks_stopped_waiter: TasksStoppedWaiter = client.get_waiter("tasks_stopped")

    list_account_settings_paginator: ListAccountSettingsPaginator = client.get_paginator("list_account_settings")
    list_attributes_paginator: ListAttributesPaginator = client.get_paginator("list_attributes")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_container_instances_paginator: ListContainerInstancesPaginator = client.get_paginator("list_container_instances")
    list_services_paginator: ListServicesPaginator = client.get_paginator("list_services")
    list_task_definition_families_paginator: ListTaskDefinitionFamiliesPaginator = client.get_paginator("list_task_definition_families")
    list_task_definitions_paginator: ListTaskDefinitionsPaginator = client.get_paginator("list_task_definitions")
    list_tasks_paginator: ListTasksPaginator = client.get_paginator("list_tasks")
    ```
"""
from mypy_boto3_ecs.client import ECSClient
from mypy_boto3_ecs.paginator import (
    ListAccountSettingsPaginator,
    ListAttributesPaginator,
    ListClustersPaginator,
    ListContainerInstancesPaginator,
    ListServicesPaginator,
    ListTaskDefinitionFamiliesPaginator,
    ListTaskDefinitionsPaginator,
    ListTasksPaginator,
)
from mypy_boto3_ecs.waiter import (
    ServicesInactiveWaiter,
    ServicesStableWaiter,
    TasksRunningWaiter,
    TasksStoppedWaiter,
)

Client = ECSClient


__all__ = (
    "Client",
    "ECSClient",
    "ListAccountSettingsPaginator",
    "ListAttributesPaginator",
    "ListClustersPaginator",
    "ListContainerInstancesPaginator",
    "ListServicesPaginator",
    "ListTaskDefinitionFamiliesPaginator",
    "ListTaskDefinitionsPaginator",
    "ListTasksPaginator",
    "ServicesInactiveWaiter",
    "ServicesStableWaiter",
    "TasksRunningWaiter",
    "TasksStoppedWaiter",
)
