"""
Main interface for robomaker service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_robomaker import (
        Client,
        ListDeploymentJobsPaginator,
        ListFleetsPaginator,
        ListRobotApplicationsPaginator,
        ListRobotsPaginator,
        ListSimulationApplicationsPaginator,
        ListSimulationJobBatchesPaginator,
        ListSimulationJobsPaginator,
        ListWorldExportJobsPaginator,
        ListWorldGenerationJobsPaginator,
        ListWorldTemplatesPaginator,
        ListWorldsPaginator,
        RoboMakerClient,
    )

    session = Session()
    client: RoboMakerClient = session.client("robomaker")

    list_deployment_jobs_paginator: ListDeploymentJobsPaginator = client.get_paginator("list_deployment_jobs")
    list_fleets_paginator: ListFleetsPaginator = client.get_paginator("list_fleets")
    list_robot_applications_paginator: ListRobotApplicationsPaginator = client.get_paginator("list_robot_applications")
    list_robots_paginator: ListRobotsPaginator = client.get_paginator("list_robots")
    list_simulation_applications_paginator: ListSimulationApplicationsPaginator = client.get_paginator("list_simulation_applications")
    list_simulation_job_batches_paginator: ListSimulationJobBatchesPaginator = client.get_paginator("list_simulation_job_batches")
    list_simulation_jobs_paginator: ListSimulationJobsPaginator = client.get_paginator("list_simulation_jobs")
    list_world_export_jobs_paginator: ListWorldExportJobsPaginator = client.get_paginator("list_world_export_jobs")
    list_world_generation_jobs_paginator: ListWorldGenerationJobsPaginator = client.get_paginator("list_world_generation_jobs")
    list_world_templates_paginator: ListWorldTemplatesPaginator = client.get_paginator("list_world_templates")
    list_worlds_paginator: ListWorldsPaginator = client.get_paginator("list_worlds")
    ```
"""

from .client import RoboMakerClient
from .paginator import (
    ListDeploymentJobsPaginator,
    ListFleetsPaginator,
    ListRobotApplicationsPaginator,
    ListRobotsPaginator,
    ListSimulationApplicationsPaginator,
    ListSimulationJobBatchesPaginator,
    ListSimulationJobsPaginator,
    ListWorldExportJobsPaginator,
    ListWorldGenerationJobsPaginator,
    ListWorldsPaginator,
    ListWorldTemplatesPaginator,
)

Client = RoboMakerClient

__all__ = (
    "Client",
    "ListDeploymentJobsPaginator",
    "ListFleetsPaginator",
    "ListRobotApplicationsPaginator",
    "ListRobotsPaginator",
    "ListSimulationApplicationsPaginator",
    "ListSimulationJobBatchesPaginator",
    "ListSimulationJobsPaginator",
    "ListWorldExportJobsPaginator",
    "ListWorldGenerationJobsPaginator",
    "ListWorldTemplatesPaginator",
    "ListWorldsPaginator",
    "RoboMakerClient",
)
