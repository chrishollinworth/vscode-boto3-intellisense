"""
Type annotations for codecatalyst service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_codecatalyst.client import CodeCatalystClient
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAccessTokensRequestPaginateTypeDef,
    ListAccessTokensResponseTypeDef,
    ListDevEnvironmentSessionsRequestPaginateTypeDef,
    ListDevEnvironmentSessionsResponseTypeDef,
    ListDevEnvironmentsRequestPaginateTypeDef,
    ListDevEnvironmentsResponseTypeDef,
    ListEventLogsRequestPaginateTypeDef,
    ListEventLogsResponseTypeDef,
    ListProjectsRequestPaginateTypeDef,
    ListProjectsResponseTypeDef,
    ListSourceRepositoriesRequestPaginateTypeDef,
    ListSourceRepositoriesResponseTypeDef,
    ListSourceRepositoryBranchesRequestPaginateTypeDef,
    ListSourceRepositoryBranchesResponseTypeDef,
    ListSpacesRequestPaginateTypeDef,
    ListSpacesResponseTypeDef,
    ListWorkflowRunsRequestPaginateTypeDef,
    ListWorkflowRunsResponseTypeDef,
    ListWorkflowsRequestPaginateTypeDef,
    ListWorkflowsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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

if TYPE_CHECKING:
    _ListAccessTokensPaginatorBase = Paginator[ListAccessTokensResponseTypeDef]
else:
    _ListAccessTokensPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccessTokensPaginator(_ListAccessTokensPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/paginator/ListAccessTokens.html#CodeCatalyst.Paginator.ListAccessTokens)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/#listaccesstokenspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccessTokensRequestPaginateTypeDef]
    ) -> PageIterator[ListAccessTokensResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/paginator/ListAccessTokens.html#CodeCatalyst.Paginator.ListAccessTokens.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/#listaccesstokenspaginator)
        """

if TYPE_CHECKING:
    _ListDevEnvironmentSessionsPaginatorBase = Paginator[ListDevEnvironmentSessionsResponseTypeDef]
else:
    _ListDevEnvironmentSessionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDevEnvironmentSessionsPaginator(_ListDevEnvironmentSessionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/paginator/ListDevEnvironmentSessions.html#CodeCatalyst.Paginator.ListDevEnvironmentSessions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/#listdevenvironmentsessionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDevEnvironmentSessionsRequestPaginateTypeDef]
    ) -> PageIterator[ListDevEnvironmentSessionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/paginator/ListDevEnvironmentSessions.html#CodeCatalyst.Paginator.ListDevEnvironmentSessions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/#listdevenvironmentsessionspaginator)
        """

if TYPE_CHECKING:
    _ListDevEnvironmentsPaginatorBase = Paginator[ListDevEnvironmentsResponseTypeDef]
else:
    _ListDevEnvironmentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDevEnvironmentsPaginator(_ListDevEnvironmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/paginator/ListDevEnvironments.html#CodeCatalyst.Paginator.ListDevEnvironments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/#listdevenvironmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDevEnvironmentsRequestPaginateTypeDef]
    ) -> PageIterator[ListDevEnvironmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/paginator/ListDevEnvironments.html#CodeCatalyst.Paginator.ListDevEnvironments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/#listdevenvironmentspaginator)
        """

if TYPE_CHECKING:
    _ListEventLogsPaginatorBase = Paginator[ListEventLogsResponseTypeDef]
else:
    _ListEventLogsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEventLogsPaginator(_ListEventLogsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/paginator/ListEventLogs.html#CodeCatalyst.Paginator.ListEventLogs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/#listeventlogspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEventLogsRequestPaginateTypeDef]
    ) -> PageIterator[ListEventLogsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/paginator/ListEventLogs.html#CodeCatalyst.Paginator.ListEventLogs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/#listeventlogspaginator)
        """

if TYPE_CHECKING:
    _ListProjectsPaginatorBase = Paginator[ListProjectsResponseTypeDef]
else:
    _ListProjectsPaginatorBase = Paginator  # type: ignore[assignment]

class ListProjectsPaginator(_ListProjectsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/paginator/ListProjects.html#CodeCatalyst.Paginator.ListProjects)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/#listprojectspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProjectsRequestPaginateTypeDef]
    ) -> PageIterator[ListProjectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/paginator/ListProjects.html#CodeCatalyst.Paginator.ListProjects.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/#listprojectspaginator)
        """

if TYPE_CHECKING:
    _ListSourceRepositoriesPaginatorBase = Paginator[ListSourceRepositoriesResponseTypeDef]
else:
    _ListSourceRepositoriesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSourceRepositoriesPaginator(_ListSourceRepositoriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/paginator/ListSourceRepositories.html#CodeCatalyst.Paginator.ListSourceRepositories)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/#listsourcerepositoriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSourceRepositoriesRequestPaginateTypeDef]
    ) -> PageIterator[ListSourceRepositoriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/paginator/ListSourceRepositories.html#CodeCatalyst.Paginator.ListSourceRepositories.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/#listsourcerepositoriespaginator)
        """

if TYPE_CHECKING:
    _ListSourceRepositoryBranchesPaginatorBase = Paginator[
        ListSourceRepositoryBranchesResponseTypeDef
    ]
else:
    _ListSourceRepositoryBranchesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSourceRepositoryBranchesPaginator(_ListSourceRepositoryBranchesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/paginator/ListSourceRepositoryBranches.html#CodeCatalyst.Paginator.ListSourceRepositoryBranches)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/#listsourcerepositorybranchespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSourceRepositoryBranchesRequestPaginateTypeDef]
    ) -> PageIterator[ListSourceRepositoryBranchesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/paginator/ListSourceRepositoryBranches.html#CodeCatalyst.Paginator.ListSourceRepositoryBranches.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/#listsourcerepositorybranchespaginator)
        """

if TYPE_CHECKING:
    _ListSpacesPaginatorBase = Paginator[ListSpacesResponseTypeDef]
else:
    _ListSpacesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSpacesPaginator(_ListSpacesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/paginator/ListSpaces.html#CodeCatalyst.Paginator.ListSpaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/#listspacespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSpacesRequestPaginateTypeDef]
    ) -> PageIterator[ListSpacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/paginator/ListSpaces.html#CodeCatalyst.Paginator.ListSpaces.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/#listspacespaginator)
        """

if TYPE_CHECKING:
    _ListWorkflowRunsPaginatorBase = Paginator[ListWorkflowRunsResponseTypeDef]
else:
    _ListWorkflowRunsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkflowRunsPaginator(_ListWorkflowRunsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/paginator/ListWorkflowRuns.html#CodeCatalyst.Paginator.ListWorkflowRuns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/#listworkflowrunspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkflowRunsRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkflowRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/paginator/ListWorkflowRuns.html#CodeCatalyst.Paginator.ListWorkflowRuns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/#listworkflowrunspaginator)
        """

if TYPE_CHECKING:
    _ListWorkflowsPaginatorBase = Paginator[ListWorkflowsResponseTypeDef]
else:
    _ListWorkflowsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkflowsPaginator(_ListWorkflowsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/paginator/ListWorkflows.html#CodeCatalyst.Paginator.ListWorkflows)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/#listworkflowspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkflowsRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkflowsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/paginator/ListWorkflows.html#CodeCatalyst.Paginator.ListWorkflows.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators/#listworkflowspaginator)
        """
