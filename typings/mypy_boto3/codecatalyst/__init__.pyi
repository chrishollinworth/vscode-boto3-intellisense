"""
Main interface for codecatalyst service.

Usage::

    ```python
    import boto3
    from mypy_boto3_codecatalyst import (
        Client,
        CodeCatalystClient,
        ListAccessTokensPaginator,
        ListDevEnvironmentsPaginator,
        ListEventLogsPaginator,
        ListProjectsPaginator,
        ListSourceRepositoriesPaginator,
        ListSourceRepositoryBranchesPaginator,
        ListSpacesPaginator,
    )

    session = boto3.Session()

    client: CodeCatalystClient = boto3.client("codecatalyst")
    session_client: CodeCatalystClient = session.client("codecatalyst")

    list_access_tokens_paginator: ListAccessTokensPaginator = client.get_paginator("list_access_tokens")
    list_dev_environments_paginator: ListDevEnvironmentsPaginator = client.get_paginator("list_dev_environments")
    list_event_logs_paginator: ListEventLogsPaginator = client.get_paginator("list_event_logs")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    list_source_repositories_paginator: ListSourceRepositoriesPaginator = client.get_paginator("list_source_repositories")
    list_source_repository_branches_paginator: ListSourceRepositoryBranchesPaginator = client.get_paginator("list_source_repository_branches")
    list_spaces_paginator: ListSpacesPaginator = client.get_paginator("list_spaces")
    ```
"""
from .client import CodeCatalystClient
from .paginator import (
    ListAccessTokensPaginator,
    ListDevEnvironmentsPaginator,
    ListEventLogsPaginator,
    ListProjectsPaginator,
    ListSourceRepositoriesPaginator,
    ListSourceRepositoryBranchesPaginator,
    ListSpacesPaginator,
)

Client = CodeCatalystClient

__all__ = (
    "Client",
    "CodeCatalystClient",
    "ListAccessTokensPaginator",
    "ListDevEnvironmentsPaginator",
    "ListEventLogsPaginator",
    "ListProjectsPaginator",
    "ListSourceRepositoriesPaginator",
    "ListSourceRepositoryBranchesPaginator",
    "ListSpacesPaginator",
)
