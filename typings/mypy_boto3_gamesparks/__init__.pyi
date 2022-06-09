"""
Main interface for gamesparks service.

Usage::

    ```python
    import boto3
    from mypy_boto3_gamesparks import (
        Client,
        GameSparksClient,
        ListExtensionVersionsPaginator,
        ListExtensionsPaginator,
        ListGamesPaginator,
        ListGeneratedCodeJobsPaginator,
        ListSnapshotsPaginator,
        ListStageDeploymentsPaginator,
        ListStagesPaginator,
    )

    session = boto3.Session()

    client: GameSparksClient = boto3.client("gamesparks")
    session_client: GameSparksClient = session.client("gamesparks")

    list_extension_versions_paginator: ListExtensionVersionsPaginator = client.get_paginator("list_extension_versions")
    list_extensions_paginator: ListExtensionsPaginator = client.get_paginator("list_extensions")
    list_games_paginator: ListGamesPaginator = client.get_paginator("list_games")
    list_generated_code_jobs_paginator: ListGeneratedCodeJobsPaginator = client.get_paginator("list_generated_code_jobs")
    list_snapshots_paginator: ListSnapshotsPaginator = client.get_paginator("list_snapshots")
    list_stage_deployments_paginator: ListStageDeploymentsPaginator = client.get_paginator("list_stage_deployments")
    list_stages_paginator: ListStagesPaginator = client.get_paginator("list_stages")
    ```
"""
from .client import GameSparksClient
from .paginator import (
    ListExtensionsPaginator,
    ListExtensionVersionsPaginator,
    ListGamesPaginator,
    ListGeneratedCodeJobsPaginator,
    ListSnapshotsPaginator,
    ListStageDeploymentsPaginator,
    ListStagesPaginator,
)

Client = GameSparksClient

__all__ = (
    "Client",
    "GameSparksClient",
    "ListExtensionVersionsPaginator",
    "ListExtensionsPaginator",
    "ListGamesPaginator",
    "ListGeneratedCodeJobsPaginator",
    "ListSnapshotsPaginator",
    "ListStageDeploymentsPaginator",
    "ListStagesPaginator",
)
