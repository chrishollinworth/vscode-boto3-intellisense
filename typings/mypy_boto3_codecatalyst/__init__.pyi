"""
Main interface for codecatalyst service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_codecatalyst import (
        Client,
        CodeCatalystClient,
        ListAccessTokensPaginator,
        ListDevEnvironmentSessionsPaginator,
        ListDevEnvironmentsPaginator,
        ListEventLogsPaginator,
        ListProjectsPaginator,
        ListSourceRepositoriesPaginator,
        ListSourceRepositoryBranchesPaginator,
        ListSpacesPaginator,
        ListWorkflowRunsPaginator,
        ListWorkflowsPaginator,
    )

    session = Session()
    client: CodeCatalystClient = session.client("codecatalyst")

    list_access_tokens_paginator: ListAccessTokensPaginator = client.get_paginator("list_access_tokens")
    list_dev_environment_sessions_paginator: ListDevEnvironmentSessionsPaginator = client.get_paginator("list_dev_environment_sessions")
    list_dev_environments_paginator: ListDevEnvironmentsPaginator = client.get_paginator("list_dev_environments")
    list_event_logs_paginator: ListEventLogsPaginator = client.get_paginator("list_event_logs")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    list_source_repositories_paginator: ListSourceRepositoriesPaginator = client.get_paginator("list_source_repositories")
    list_source_repository_branches_paginator: ListSourceRepositoryBranchesPaginator = client.get_paginator("list_source_repository_branches")
    list_spaces_paginator: ListSpacesPaginator = client.get_paginator("list_spaces")
    list_workflow_runs_paginator: ListWorkflowRunsPaginator = client.get_paginator("list_workflow_runs")
    list_workflows_paginator: ListWorkflowsPaginator = client.get_paginator("list_workflows")
    ```
"""

from .client import CodeCatalystClient
from .paginator import (
    ListAccessTokensPaginator,
    ListDevEnvironmentSessionsPaginator,
    ListDevEnvironmentsPaginator,
    ListEventLogsPaginator,
    ListProjectsPaginator,
    ListSourceRepositoriesPaginator,
    ListSourceRepositoryBranchesPaginator,
    ListSpacesPaginator,
    ListWorkflowRunsPaginator,
    ListWorkflowsPaginator,
)

Client = CodeCatalystClient

__all__ = (
    "Client",
    "CodeCatalystClient",
    "ListAccessTokensPaginator",
    "ListDevEnvironmentSessionsPaginator",
    "ListDevEnvironmentsPaginator",
    "ListEventLogsPaginator",
    "ListProjectsPaginator",
    "ListSourceRepositoriesPaginator",
    "ListSourceRepositoryBranchesPaginator",
    "ListSpacesPaginator",
    "ListWorkflowRunsPaginator",
    "ListWorkflowsPaginator",
)
