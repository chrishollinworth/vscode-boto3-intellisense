"""
Main interface for iot1click-projects service.

Usage::

    ```python
    import boto3
    from mypy_boto3_iot1click_projects import (
        Client,
        IoT1ClickProjectsClient,
        ListPlacementsPaginator,
        ListProjectsPaginator,
    )

    session = boto3.Session()

    client: IoT1ClickProjectsClient = boto3.client("iot1click-projects")
    session_client: IoT1ClickProjectsClient = session.client("iot1click-projects")

    list_placements_paginator: ListPlacementsPaginator = client.get_paginator("list_placements")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    ```
"""
from .client import IoT1ClickProjectsClient
from .paginator import ListPlacementsPaginator, ListProjectsPaginator

Client = IoT1ClickProjectsClient

__all__ = ("Client", "IoT1ClickProjectsClient", "ListPlacementsPaginator", "ListProjectsPaginator")
