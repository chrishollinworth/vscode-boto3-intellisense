"""
Type annotations for codecatalyst service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_codecatalyst import CodeCatalystClient
    from mypy_boto3_codecatalyst.paginator import (
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

    client: CodeCatalystClient = boto3.client("codecatalyst")

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
from datetime import datetime
from typing import Any, Dict, Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    FilterTypeDef,
    ListAccessTokensResponseTypeDef,
    ListDevEnvironmentSessionsResponseTypeDef,
    ListDevEnvironmentsResponseTypeDef,
    ListEventLogsResponseTypeDef,
    ListProjectsResponseTypeDef,
    ListSourceRepositoriesResponseTypeDef,
    ListSourceRepositoryBranchesResponseTypeDef,
    ListSpacesResponseTypeDef,
    ListWorkflowRunsResponseTypeDef,
    ListWorkflowsResponseTypeDef,
    PaginatorConfigTypeDef,
    ProjectListFilterTypeDef,
)

__all__ = (
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

class ListAccessTokensPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListAccessTokens)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listaccesstokenspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccessTokensResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListAccessTokens.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listaccesstokenspaginator)
        """

class ListDevEnvironmentSessionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListDevEnvironmentSessions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listdevenvironmentsessionspaginator)
    """

    def paginate(
        self,
        *,
        spaceName: str,
        projectName: str,
        devEnvironmentId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDevEnvironmentSessionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListDevEnvironmentSessions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listdevenvironmentsessionspaginator)
        """

class ListDevEnvironmentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListDevEnvironments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listdevenvironmentspaginator)
    """

    def paginate(
        self,
        *,
        spaceName: str,
        projectName: str = None,
        filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDevEnvironmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListDevEnvironments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listdevenvironmentspaginator)
        """

class ListEventLogsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListEventLogs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listeventlogspaginator)
    """

    def paginate(
        self,
        *,
        spaceName: str,
        startTime: Union[datetime, str],
        endTime: Union[datetime, str],
        eventName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEventLogsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListEventLogs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listeventlogspaginator)
        """

class ListProjectsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListProjects)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listprojectspaginator)
    """

    def paginate(
        self,
        *,
        spaceName: str,
        filters: List["ProjectListFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListProjects.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listprojectspaginator)
        """

class ListSourceRepositoriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListSourceRepositories)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listsourcerepositoriespaginator)
    """

    def paginate(
        self, *, spaceName: str, projectName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSourceRepositoriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListSourceRepositories.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listsourcerepositoriespaginator)
        """

class ListSourceRepositoryBranchesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListSourceRepositoryBranches)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listsourcerepositorybranchespaginator)
    """

    def paginate(
        self,
        *,
        spaceName: str,
        projectName: str,
        sourceRepositoryName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSourceRepositoryBranchesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListSourceRepositoryBranches.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listsourcerepositorybranchespaginator)
        """

class ListSpacesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListSpaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listspacespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSpacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListSpaces.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listspacespaginator)
        """

class ListWorkflowRunsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListWorkflowRuns)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listworkflowrunspaginator)
    """

    def paginate(
        self,
        *,
        spaceName: str,
        projectName: str,
        workflowId: str = None,
        sortBy: List[Dict[str, Any]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkflowRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListWorkflowRuns.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listworkflowrunspaginator)
        """

class ListWorkflowsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListWorkflows)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listworkflowspaginator)
    """

    def paginate(
        self,
        *,
        spaceName: str,
        projectName: str,
        sortBy: List[Dict[str, Any]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkflowsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListWorkflows.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listworkflowspaginator)
        """
