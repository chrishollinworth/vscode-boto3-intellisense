"""
Main interface for mgh service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mgh import (
        Client,
        ListApplicationStatesPaginator,
        ListCreatedArtifactsPaginator,
        ListDiscoveredResourcesPaginator,
        ListMigrationTaskUpdatesPaginator,
        ListMigrationTasksPaginator,
        ListProgressUpdateStreamsPaginator,
        ListSourceResourcesPaginator,
        MigrationHubClient,
    )

    session = Session()
    client: MigrationHubClient = session.client("mgh")

    list_application_states_paginator: ListApplicationStatesPaginator = client.get_paginator("list_application_states")
    list_created_artifacts_paginator: ListCreatedArtifactsPaginator = client.get_paginator("list_created_artifacts")
    list_discovered_resources_paginator: ListDiscoveredResourcesPaginator = client.get_paginator("list_discovered_resources")
    list_migration_task_updates_paginator: ListMigrationTaskUpdatesPaginator = client.get_paginator("list_migration_task_updates")
    list_migration_tasks_paginator: ListMigrationTasksPaginator = client.get_paginator("list_migration_tasks")
    list_progress_update_streams_paginator: ListProgressUpdateStreamsPaginator = client.get_paginator("list_progress_update_streams")
    list_source_resources_paginator: ListSourceResourcesPaginator = client.get_paginator("list_source_resources")
    ```
"""

from .client import MigrationHubClient
from .paginator import (
    ListApplicationStatesPaginator,
    ListCreatedArtifactsPaginator,
    ListDiscoveredResourcesPaginator,
    ListMigrationTasksPaginator,
    ListMigrationTaskUpdatesPaginator,
    ListProgressUpdateStreamsPaginator,
    ListSourceResourcesPaginator,
)

Client = MigrationHubClient

__all__ = (
    "Client",
    "ListApplicationStatesPaginator",
    "ListCreatedArtifactsPaginator",
    "ListDiscoveredResourcesPaginator",
    "ListMigrationTaskUpdatesPaginator",
    "ListMigrationTasksPaginator",
    "ListProgressUpdateStreamsPaginator",
    "ListSourceResourcesPaginator",
    "MigrationHubClient",
)
