"""
Type annotations for codecatalyst service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_codecatalyst.client import CodeCatalystClient

    session = Session()
    client: CodeCatalystClient = session.client("codecatalyst")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

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
from .type_defs import (
    CreateAccessTokenRequestTypeDef,
    CreateAccessTokenResponseTypeDef,
    CreateDevEnvironmentRequestTypeDef,
    CreateDevEnvironmentResponseTypeDef,
    CreateProjectRequestTypeDef,
    CreateProjectResponseTypeDef,
    CreateSourceRepositoryBranchRequestTypeDef,
    CreateSourceRepositoryBranchResponseTypeDef,
    CreateSourceRepositoryRequestTypeDef,
    CreateSourceRepositoryResponseTypeDef,
    DeleteAccessTokenRequestTypeDef,
    DeleteDevEnvironmentRequestTypeDef,
    DeleteDevEnvironmentResponseTypeDef,
    DeleteProjectRequestTypeDef,
    DeleteProjectResponseTypeDef,
    DeleteSourceRepositoryRequestTypeDef,
    DeleteSourceRepositoryResponseTypeDef,
    DeleteSpaceRequestTypeDef,
    DeleteSpaceResponseTypeDef,
    GetDevEnvironmentRequestTypeDef,
    GetDevEnvironmentResponseTypeDef,
    GetProjectRequestTypeDef,
    GetProjectResponseTypeDef,
    GetSourceRepositoryCloneUrlsRequestTypeDef,
    GetSourceRepositoryCloneUrlsResponseTypeDef,
    GetSourceRepositoryRequestTypeDef,
    GetSourceRepositoryResponseTypeDef,
    GetSpaceRequestTypeDef,
    GetSpaceResponseTypeDef,
    GetSubscriptionRequestTypeDef,
    GetSubscriptionResponseTypeDef,
    GetUserDetailsRequestTypeDef,
    GetUserDetailsResponseTypeDef,
    GetWorkflowRequestTypeDef,
    GetWorkflowResponseTypeDef,
    GetWorkflowRunRequestTypeDef,
    GetWorkflowRunResponseTypeDef,
    ListAccessTokensRequestTypeDef,
    ListAccessTokensResponseTypeDef,
    ListDevEnvironmentSessionsRequestTypeDef,
    ListDevEnvironmentSessionsResponseTypeDef,
    ListDevEnvironmentsRequestTypeDef,
    ListDevEnvironmentsResponseTypeDef,
    ListEventLogsRequestTypeDef,
    ListEventLogsResponseTypeDef,
    ListProjectsRequestTypeDef,
    ListProjectsResponseTypeDef,
    ListSourceRepositoriesRequestTypeDef,
    ListSourceRepositoriesResponseTypeDef,
    ListSourceRepositoryBranchesRequestTypeDef,
    ListSourceRepositoryBranchesResponseTypeDef,
    ListSpacesRequestTypeDef,
    ListSpacesResponseTypeDef,
    ListWorkflowRunsRequestTypeDef,
    ListWorkflowRunsResponseTypeDef,
    ListWorkflowsRequestTypeDef,
    ListWorkflowsResponseTypeDef,
    StartDevEnvironmentRequestTypeDef,
    StartDevEnvironmentResponseTypeDef,
    StartDevEnvironmentSessionRequestTypeDef,
    StartDevEnvironmentSessionResponseTypeDef,
    StartWorkflowRunRequestTypeDef,
    StartWorkflowRunResponseTypeDef,
    StopDevEnvironmentRequestTypeDef,
    StopDevEnvironmentResponseTypeDef,
    StopDevEnvironmentSessionRequestTypeDef,
    StopDevEnvironmentSessionResponseTypeDef,
    UpdateDevEnvironmentRequestTypeDef,
    UpdateDevEnvironmentResponseTypeDef,
    UpdateProjectRequestTypeDef,
    UpdateProjectResponseTypeDef,
    UpdateSpaceRequestTypeDef,
    UpdateSpaceResponseTypeDef,
    VerifySessionResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("CodeCatalystClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CodeCatalystClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CodeCatalystClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#generate_presigned_url)
        """

    def create_access_token(
        self, **kwargs: Unpack[CreateAccessTokenRequestTypeDef]
    ) -> CreateAccessTokenResponseTypeDef:
        """
        Creates a personal access token (PAT) for the current user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/create_access_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#create_access_token)
        """

    def create_dev_environment(
        self, **kwargs: Unpack[CreateDevEnvironmentRequestTypeDef]
    ) -> CreateDevEnvironmentResponseTypeDef:
        """
        Creates a Dev Environment in Amazon CodeCatalyst, a cloud-based development
        environment that you can use to quickly work on the code stored in the source
        repositories of your project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/create_dev_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#create_dev_environment)
        """

    def create_project(
        self, **kwargs: Unpack[CreateProjectRequestTypeDef]
    ) -> CreateProjectResponseTypeDef:
        """
        Creates a project in a specified space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/create_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#create_project)
        """

    def create_source_repository(
        self, **kwargs: Unpack[CreateSourceRepositoryRequestTypeDef]
    ) -> CreateSourceRepositoryResponseTypeDef:
        """
        Creates an empty Git-based source repository in a specified project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/create_source_repository.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#create_source_repository)
        """

    def create_source_repository_branch(
        self, **kwargs: Unpack[CreateSourceRepositoryBranchRequestTypeDef]
    ) -> CreateSourceRepositoryBranchResponseTypeDef:
        """
        Creates a branch in a specified source repository in Amazon CodeCatalyst.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/create_source_repository_branch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#create_source_repository_branch)
        """

    def delete_access_token(
        self, **kwargs: Unpack[DeleteAccessTokenRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a specified personal access token (PAT).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/delete_access_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#delete_access_token)
        """

    def delete_dev_environment(
        self, **kwargs: Unpack[DeleteDevEnvironmentRequestTypeDef]
    ) -> DeleteDevEnvironmentResponseTypeDef:
        """
        Deletes a Dev Environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/delete_dev_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#delete_dev_environment)
        """

    def delete_project(
        self, **kwargs: Unpack[DeleteProjectRequestTypeDef]
    ) -> DeleteProjectResponseTypeDef:
        """
        Deletes a project in a space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/delete_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#delete_project)
        """

    def delete_source_repository(
        self, **kwargs: Unpack[DeleteSourceRepositoryRequestTypeDef]
    ) -> DeleteSourceRepositoryResponseTypeDef:
        """
        Deletes a source repository in Amazon CodeCatalyst.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/delete_source_repository.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#delete_source_repository)
        """

    def delete_space(
        self, **kwargs: Unpack[DeleteSpaceRequestTypeDef]
    ) -> DeleteSpaceResponseTypeDef:
        """
        Deletes a space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/delete_space.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#delete_space)
        """

    def get_dev_environment(
        self, **kwargs: Unpack[GetDevEnvironmentRequestTypeDef]
    ) -> GetDevEnvironmentResponseTypeDef:
        """
        Returns information about a Dev Environment for a source repository in a
        project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/get_dev_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#get_dev_environment)
        """

    def get_project(self, **kwargs: Unpack[GetProjectRequestTypeDef]) -> GetProjectResponseTypeDef:
        """
        Returns information about a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/get_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#get_project)
        """

    def get_source_repository(
        self, **kwargs: Unpack[GetSourceRepositoryRequestTypeDef]
    ) -> GetSourceRepositoryResponseTypeDef:
        """
        Returns information about a source repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/get_source_repository.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#get_source_repository)
        """

    def get_source_repository_clone_urls(
        self, **kwargs: Unpack[GetSourceRepositoryCloneUrlsRequestTypeDef]
    ) -> GetSourceRepositoryCloneUrlsResponseTypeDef:
        """
        Returns information about the URLs that can be used with a Git client to clone
        a source repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/get_source_repository_clone_urls.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#get_source_repository_clone_urls)
        """

    def get_space(self, **kwargs: Unpack[GetSpaceRequestTypeDef]) -> GetSpaceResponseTypeDef:
        """
        Returns information about an space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/get_space.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#get_space)
        """

    def get_subscription(
        self, **kwargs: Unpack[GetSubscriptionRequestTypeDef]
    ) -> GetSubscriptionResponseTypeDef:
        """
        Returns information about the Amazon Web Services account used for billing
        purposes and the billing plan for the space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/get_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#get_subscription)
        """

    def get_user_details(
        self, **kwargs: Unpack[GetUserDetailsRequestTypeDef]
    ) -> GetUserDetailsResponseTypeDef:
        """
        Returns information about a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/get_user_details.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#get_user_details)
        """

    def get_workflow(
        self, **kwargs: Unpack[GetWorkflowRequestTypeDef]
    ) -> GetWorkflowResponseTypeDef:
        """
        Returns information about a workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/get_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#get_workflow)
        """

    def get_workflow_run(
        self, **kwargs: Unpack[GetWorkflowRunRequestTypeDef]
    ) -> GetWorkflowRunResponseTypeDef:
        """
        Returns information about a specified run of a workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/get_workflow_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#get_workflow_run)
        """

    def list_access_tokens(
        self, **kwargs: Unpack[ListAccessTokensRequestTypeDef]
    ) -> ListAccessTokensResponseTypeDef:
        """
        Lists all personal access tokens (PATs) associated with the user who calls the
        API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/list_access_tokens.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#list_access_tokens)
        """

    def list_dev_environment_sessions(
        self, **kwargs: Unpack[ListDevEnvironmentSessionsRequestTypeDef]
    ) -> ListDevEnvironmentSessionsResponseTypeDef:
        """
        Retrieves a list of active sessions for a Dev Environment in a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/list_dev_environment_sessions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#list_dev_environment_sessions)
        """

    def list_dev_environments(
        self, **kwargs: Unpack[ListDevEnvironmentsRequestTypeDef]
    ) -> ListDevEnvironmentsResponseTypeDef:
        """
        Retrieves a list of Dev Environments in a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/list_dev_environments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#list_dev_environments)
        """

    def list_event_logs(
        self, **kwargs: Unpack[ListEventLogsRequestTypeDef]
    ) -> ListEventLogsResponseTypeDef:
        """
        Retrieves a list of events that occurred during a specific time in a space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/list_event_logs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#list_event_logs)
        """

    def list_projects(
        self, **kwargs: Unpack[ListProjectsRequestTypeDef]
    ) -> ListProjectsResponseTypeDef:
        """
        Retrieves a list of projects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/list_projects.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#list_projects)
        """

    def list_source_repositories(
        self, **kwargs: Unpack[ListSourceRepositoriesRequestTypeDef]
    ) -> ListSourceRepositoriesResponseTypeDef:
        """
        Retrieves a list of source repositories in a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/list_source_repositories.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#list_source_repositories)
        """

    def list_source_repository_branches(
        self, **kwargs: Unpack[ListSourceRepositoryBranchesRequestTypeDef]
    ) -> ListSourceRepositoryBranchesResponseTypeDef:
        """
        Retrieves a list of branches in a specified source repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/list_source_repository_branches.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#list_source_repository_branches)
        """

    def list_spaces(self, **kwargs: Unpack[ListSpacesRequestTypeDef]) -> ListSpacesResponseTypeDef:
        """
        Retrieves a list of spaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/list_spaces.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#list_spaces)
        """

    def list_workflow_runs(
        self, **kwargs: Unpack[ListWorkflowRunsRequestTypeDef]
    ) -> ListWorkflowRunsResponseTypeDef:
        """
        Retrieves a list of workflow runs of a specified workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/list_workflow_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#list_workflow_runs)
        """

    def list_workflows(
        self, **kwargs: Unpack[ListWorkflowsRequestTypeDef]
    ) -> ListWorkflowsResponseTypeDef:
        """
        Retrieves a list of workflows in a specified project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/list_workflows.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#list_workflows)
        """

    def start_dev_environment(
        self, **kwargs: Unpack[StartDevEnvironmentRequestTypeDef]
    ) -> StartDevEnvironmentResponseTypeDef:
        """
        Starts a specified Dev Environment and puts it into an active state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/start_dev_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#start_dev_environment)
        """

    def start_dev_environment_session(
        self, **kwargs: Unpack[StartDevEnvironmentSessionRequestTypeDef]
    ) -> StartDevEnvironmentSessionResponseTypeDef:
        """
        Starts a session for a specified Dev Environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/start_dev_environment_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#start_dev_environment_session)
        """

    def start_workflow_run(
        self, **kwargs: Unpack[StartWorkflowRunRequestTypeDef]
    ) -> StartWorkflowRunResponseTypeDef:
        """
        Begins a run of a specified workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/start_workflow_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#start_workflow_run)
        """

    def stop_dev_environment(
        self, **kwargs: Unpack[StopDevEnvironmentRequestTypeDef]
    ) -> StopDevEnvironmentResponseTypeDef:
        """
        Pauses a specified Dev Environment and places it in a non-running state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/stop_dev_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#stop_dev_environment)
        """

    def stop_dev_environment_session(
        self, **kwargs: Unpack[StopDevEnvironmentSessionRequestTypeDef]
    ) -> StopDevEnvironmentSessionResponseTypeDef:
        """
        Stops a session for a specified Dev Environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/stop_dev_environment_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#stop_dev_environment_session)
        """

    def update_dev_environment(
        self, **kwargs: Unpack[UpdateDevEnvironmentRequestTypeDef]
    ) -> UpdateDevEnvironmentResponseTypeDef:
        """
        Changes one or more values for a Dev Environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/update_dev_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#update_dev_environment)
        """

    def update_project(
        self, **kwargs: Unpack[UpdateProjectRequestTypeDef]
    ) -> UpdateProjectResponseTypeDef:
        """
        Changes one or more values for a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/update_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#update_project)
        """

    def update_space(
        self, **kwargs: Unpack[UpdateSpaceRequestTypeDef]
    ) -> UpdateSpaceResponseTypeDef:
        """
        Changes one or more values for a space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/update_space.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#update_space)
        """

    def verify_session(self) -> VerifySessionResponseTypeDef:
        """
        Verifies whether the calling user has a valid Amazon CodeCatalyst login and
        session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/verify_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#verify_session)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_access_tokens"]
    ) -> ListAccessTokensPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_dev_environment_sessions"]
    ) -> ListDevEnvironmentSessionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_dev_environments"]
    ) -> ListDevEnvironmentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_event_logs"]
    ) -> ListEventLogsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_projects"]
    ) -> ListProjectsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_source_repositories"]
    ) -> ListSourceRepositoriesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_source_repository_branches"]
    ) -> ListSourceRepositoryBranchesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_spaces"]
    ) -> ListSpacesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workflow_runs"]
    ) -> ListWorkflowRunsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workflows"]
    ) -> ListWorkflowsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client/#get_paginator)
        """
