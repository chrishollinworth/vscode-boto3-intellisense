"""
Main interface for mgh service.

Usage::

    ```python
    import boto3
    from mypy_boto3_mgh import (
        Client,
        ListApplicationStatesPaginator,
        ListCreatedArtifactsPaginator,
        ListDiscoveredResourcesPaginator,
        ListMigrationTasksPaginator,
        ListProgressUpdateStreamsPaginator,
        MigrationHubClient,
    )

    session = boto3.Session()

    client: MigrationHubClient = boto3.client("mgh")
    session_client: MigrationHubClient = session.client("mgh")

    list_application_states_paginator: ListApplicationStatesPaginator = client.get_paginator("list_application_states")
    list_created_artifacts_paginator: ListCreatedArtifactsPaginator = client.get_paginator("list_created_artifacts")
    list_discovered_resources_paginator: ListDiscoveredResourcesPaginator = client.get_paginator("list_discovered_resources")
    list_migration_tasks_paginator: ListMigrationTasksPaginator = client.get_paginator("list_migration_tasks")
    list_progress_update_streams_paginator: ListProgressUpdateStreamsPaginator = client.get_paginator("list_progress_update_streams")
    ```
"""
from mypy_boto3_mgh.client import MigrationHubClient
from mypy_boto3_mgh.paginator import (
    ListApplicationStatesPaginator,
    ListCreatedArtifactsPaginator,
    ListDiscoveredResourcesPaginator,
    ListMigrationTasksPaginator,
    ListProgressUpdateStreamsPaginator,
)

Client = MigrationHubClient


__all__ = (
    "Client",
    "ListApplicationStatesPaginator",
    "ListCreatedArtifactsPaginator",
    "ListDiscoveredResourcesPaginator",
    "ListMigrationTasksPaginator",
    "ListProgressUpdateStreamsPaginator",
    "MigrationHubClient",
)
