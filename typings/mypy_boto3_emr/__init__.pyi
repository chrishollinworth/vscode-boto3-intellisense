"""
Main interface for emr service.

Usage::

    ```python
    import boto3
    from mypy_boto3_emr import (
        Client,
        ClusterRunningWaiter,
        ClusterTerminatedWaiter,
        EMRClient,
        ListBootstrapActionsPaginator,
        ListClustersPaginator,
        ListInstanceFleetsPaginator,
        ListInstanceGroupsPaginator,
        ListInstancesPaginator,
        ListNotebookExecutionsPaginator,
        ListSecurityConfigurationsPaginator,
        ListStepsPaginator,
        StepCompleteWaiter,
    )

    session = boto3.Session()

    client: EMRClient = boto3.client("emr")
    session_client: EMRClient = session.client("emr")

    cluster_running_waiter: ClusterRunningWaiter = client.get_waiter("cluster_running")
    cluster_terminated_waiter: ClusterTerminatedWaiter = client.get_waiter("cluster_terminated")
    step_complete_waiter: StepCompleteWaiter = client.get_waiter("step_complete")

    list_bootstrap_actions_paginator: ListBootstrapActionsPaginator = client.get_paginator("list_bootstrap_actions")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_instance_fleets_paginator: ListInstanceFleetsPaginator = client.get_paginator("list_instance_fleets")
    list_instance_groups_paginator: ListInstanceGroupsPaginator = client.get_paginator("list_instance_groups")
    list_instances_paginator: ListInstancesPaginator = client.get_paginator("list_instances")
    list_notebook_executions_paginator: ListNotebookExecutionsPaginator = client.get_paginator("list_notebook_executions")
    list_security_configurations_paginator: ListSecurityConfigurationsPaginator = client.get_paginator("list_security_configurations")
    list_steps_paginator: ListStepsPaginator = client.get_paginator("list_steps")
    ```
"""
from mypy_boto3_emr.client import EMRClient
from mypy_boto3_emr.paginator import (
    ListBootstrapActionsPaginator,
    ListClustersPaginator,
    ListInstanceFleetsPaginator,
    ListInstanceGroupsPaginator,
    ListInstancesPaginator,
    ListNotebookExecutionsPaginator,
    ListSecurityConfigurationsPaginator,
    ListStepsPaginator,
)
from mypy_boto3_emr.waiter import ClusterRunningWaiter, ClusterTerminatedWaiter, StepCompleteWaiter

Client = EMRClient


__all__ = (
    "Client",
    "ClusterRunningWaiter",
    "ClusterTerminatedWaiter",
    "EMRClient",
    "ListBootstrapActionsPaginator",
    "ListClustersPaginator",
    "ListInstanceFleetsPaginator",
    "ListInstanceGroupsPaginator",
    "ListInstancesPaginator",
    "ListNotebookExecutionsPaginator",
    "ListSecurityConfigurationsPaginator",
    "ListStepsPaginator",
    "StepCompleteWaiter",
)
