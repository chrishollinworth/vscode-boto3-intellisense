"""
Main interface for launch-wizard service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_launch_wizard import (
        Client,
        LaunchWizardClient,
        ListDeploymentEventsPaginator,
        ListDeploymentsPaginator,
        ListWorkloadDeploymentPatternsPaginator,
        ListWorkloadsPaginator,
    )

    session = Session()
    client: LaunchWizardClient = session.client("launch-wizard")

    list_deployment_events_paginator: ListDeploymentEventsPaginator = client.get_paginator("list_deployment_events")
    list_deployments_paginator: ListDeploymentsPaginator = client.get_paginator("list_deployments")
    list_workload_deployment_patterns_paginator: ListWorkloadDeploymentPatternsPaginator = client.get_paginator("list_workload_deployment_patterns")
    list_workloads_paginator: ListWorkloadsPaginator = client.get_paginator("list_workloads")
    ```
"""

from .client import LaunchWizardClient
from .paginator import (
    ListDeploymentEventsPaginator,
    ListDeploymentsPaginator,
    ListWorkloadDeploymentPatternsPaginator,
    ListWorkloadsPaginator,
)

Client = LaunchWizardClient

__all__ = (
    "Client",
    "LaunchWizardClient",
    "ListDeploymentEventsPaginator",
    "ListDeploymentsPaginator",
    "ListWorkloadDeploymentPatternsPaginator",
    "ListWorkloadsPaginator",
)
