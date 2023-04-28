"""
Type annotations for codecatalyst service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_codecatalyst import CodeCatalystClient

    client: CodeCatalystClient = boto3.client("codecatalyst")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import InstanceTypeType
from .paginator import (
    ListAccessTokensPaginator,
    ListDevEnvironmentsPaginator,
    ListEventLogsPaginator,
    ListProjectsPaginator,
    ListSourceRepositoriesPaginator,
    ListSourceRepositoryBranchesPaginator,
    ListSpacesPaginator,
)
from .type_defs import (
    CreateAccessTokenResponseTypeDef,
    CreateDevEnvironmentResponseTypeDef,
    CreateProjectResponseTypeDef,
    CreateSourceRepositoryBranchResponseTypeDef,
    DeleteDevEnvironmentResponseTypeDef,
    DevEnvironmentSessionConfigurationTypeDef,
    FilterTypeDef,
    GetDevEnvironmentResponseTypeDef,
    GetProjectResponseTypeDef,
    GetSourceRepositoryCloneUrlsResponseTypeDef,
    GetSpaceResponseTypeDef,
    GetSubscriptionResponseTypeDef,
    GetUserDetailsResponseTypeDef,
    IdeConfigurationTypeDef,
    ListAccessTokensResponseTypeDef,
    ListDevEnvironmentsResponseTypeDef,
    ListEventLogsResponseTypeDef,
    ListProjectsResponseTypeDef,
    ListSourceRepositoriesResponseTypeDef,
    ListSourceRepositoryBranchesResponseTypeDef,
    ListSpacesResponseTypeDef,
    PersistentStorageConfigurationTypeDef,
    ProjectListFilterTypeDef,
    RepositoryInputTypeDef,
    StartDevEnvironmentResponseTypeDef,
    StartDevEnvironmentSessionResponseTypeDef,
    StopDevEnvironmentResponseTypeDef,
    StopDevEnvironmentSessionResponseTypeDef,
    UpdateDevEnvironmentResponseTypeDef,
    VerifySessionResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CodeCatalystClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CodeCatalystClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CodeCatalystClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#close)
        """
    def create_access_token(
        self, *, name: str, expiresTime: Union[datetime, str] = None
    ) -> CreateAccessTokenResponseTypeDef:
        """
        Creates a personal access token (PAT) for the current user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.create_access_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#create_access_token)
        """
    def create_dev_environment(
        self,
        *,
        spaceName: str,
        projectName: str,
        instanceType: InstanceTypeType,
        persistentStorage: "PersistentStorageConfigurationTypeDef",
        repositories: List["RepositoryInputTypeDef"] = None,
        clientToken: str = None,
        alias: str = None,
        ides: List["IdeConfigurationTypeDef"] = None,
        inactivityTimeoutMinutes: int = None
    ) -> CreateDevEnvironmentResponseTypeDef:
        """
        Creates a Dev Environment in Amazon CodeCatalyst, a cloud-based development
        environment that you can use to quickly work on the code stored in the source
        repositories of your project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.create_dev_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#create_dev_environment)
        """
    def create_project(
        self, *, spaceName: str, displayName: str, description: str = None
    ) -> CreateProjectResponseTypeDef:
        """
        Creates a project in a specified space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.create_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#create_project)
        """
    def create_source_repository_branch(
        self,
        *,
        spaceName: str,
        projectName: str,
        sourceRepositoryName: str,
        name: str,
        headCommitId: str = None
    ) -> CreateSourceRepositoryBranchResponseTypeDef:
        """
        Creates a branch in a specified source repository in Amazon CodeCatalyst.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.create_source_repository_branch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#create_source_repository_branch)
        """
    def delete_access_token(self, *, id: str) -> Dict[str, Any]:
        """
        Deletes a specified personal access token (PAT).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.delete_access_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#delete_access_token)
        """
    def delete_dev_environment(
        self, *, spaceName: str, projectName: str, id: str
    ) -> DeleteDevEnvironmentResponseTypeDef:
        """
        Deletes a Dev Environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.delete_dev_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#delete_dev_environment)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#generate_presigned_url)
        """
    def get_dev_environment(
        self, *, spaceName: str, projectName: str, id: str
    ) -> GetDevEnvironmentResponseTypeDef:
        """
        Returns information about a Dev Environment for a source repository in a
        project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.get_dev_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#get_dev_environment)
        """
    def get_project(self, *, spaceName: str, name: str) -> GetProjectResponseTypeDef:
        """
        Returns information about a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.get_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#get_project)
        """
    def get_source_repository_clone_urls(
        self, *, spaceName: str, projectName: str, sourceRepositoryName: str
    ) -> GetSourceRepositoryCloneUrlsResponseTypeDef:
        """
        Returns information about the URLs that can be used with a Git client to clone a
        source repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.get_source_repository_clone_urls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#get_source_repository_clone_urls)
        """
    def get_space(self, *, name: str) -> GetSpaceResponseTypeDef:
        """
        Returns information about an space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.get_space)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#get_space)
        """
    def get_subscription(self, *, spaceName: str) -> GetSubscriptionResponseTypeDef:
        """
        Returns information about the Amazon Web Services account used for billing
        purposes and the billing plan for the space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.get_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#get_subscription)
        """
    def get_user_details(
        self, *, id: str = None, userName: str = None
    ) -> GetUserDetailsResponseTypeDef:
        """
        Returns information about a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.get_user_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#get_user_details)
        """
    def list_access_tokens(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListAccessTokensResponseTypeDef:
        """
        Lists all personal access tokens (PATs) associated with the user who calls the
        API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.list_access_tokens)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#list_access_tokens)
        """
    def list_dev_environments(
        self,
        *,
        spaceName: str,
        projectName: str,
        filters: List["FilterTypeDef"] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListDevEnvironmentsResponseTypeDef:
        """
        Retrieves a list of Dev Environments in a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.list_dev_environments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#list_dev_environments)
        """
    def list_event_logs(
        self,
        *,
        spaceName: str,
        startTime: Union[datetime, str],
        endTime: Union[datetime, str],
        eventName: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListEventLogsResponseTypeDef:
        """
        Retrieves a list of events that occurred during a specified time period in a
        space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.list_event_logs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#list_event_logs)
        """
    def list_projects(
        self,
        *,
        spaceName: str,
        nextToken: str = None,
        maxResults: int = None,
        filters: List["ProjectListFilterTypeDef"] = None
    ) -> ListProjectsResponseTypeDef:
        """
        Retrieves a list of projects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.list_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#list_projects)
        """
    def list_source_repositories(
        self, *, spaceName: str, projectName: str, nextToken: str = None, maxResults: int = None
    ) -> ListSourceRepositoriesResponseTypeDef:
        """
        Retrieves a list of source repositories in a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.list_source_repositories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#list_source_repositories)
        """
    def list_source_repository_branches(
        self,
        *,
        spaceName: str,
        projectName: str,
        sourceRepositoryName: str,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListSourceRepositoryBranchesResponseTypeDef:
        """
        Retrieves a list of branches in a specified source repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.list_source_repository_branches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#list_source_repository_branches)
        """
    def list_spaces(self, *, nextToken: str = None) -> ListSpacesResponseTypeDef:
        """
        Retrieves a list of spaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.list_spaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#list_spaces)
        """
    def start_dev_environment(
        self,
        *,
        spaceName: str,
        projectName: str,
        id: str,
        ides: List["IdeConfigurationTypeDef"] = None,
        instanceType: InstanceTypeType = None,
        inactivityTimeoutMinutes: int = None
    ) -> StartDevEnvironmentResponseTypeDef:
        """
        Starts a specified Dev Environment and puts it into an active state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.start_dev_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#start_dev_environment)
        """
    def start_dev_environment_session(
        self,
        *,
        spaceName: str,
        projectName: str,
        id: str,
        sessionConfiguration: "DevEnvironmentSessionConfigurationTypeDef"
    ) -> StartDevEnvironmentSessionResponseTypeDef:
        """
        Starts a session for a specified Dev Environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.start_dev_environment_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#start_dev_environment_session)
        """
    def stop_dev_environment(
        self, *, spaceName: str, projectName: str, id: str
    ) -> StopDevEnvironmentResponseTypeDef:
        """
        Pauses a specified Dev Environment and places it in a non-running state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.stop_dev_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#stop_dev_environment)
        """
    def stop_dev_environment_session(
        self, *, spaceName: str, projectName: str, id: str, sessionId: str
    ) -> StopDevEnvironmentSessionResponseTypeDef:
        """
        Stops a session for a specified Dev Environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.stop_dev_environment_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#stop_dev_environment_session)
        """
    def update_dev_environment(
        self,
        *,
        spaceName: str,
        projectName: str,
        id: str,
        alias: str = None,
        ides: List["IdeConfigurationTypeDef"] = None,
        instanceType: InstanceTypeType = None,
        inactivityTimeoutMinutes: int = None,
        clientToken: str = None
    ) -> UpdateDevEnvironmentResponseTypeDef:
        """
        Changes one or more values for a Dev Environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.update_dev_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#update_dev_environment)
        """
    def verify_session(self) -> VerifySessionResponseTypeDef:
        """
        Verifies whether the calling user has a valid Amazon CodeCatalyst login and
        session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Client.verify_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/client.html#verify_session)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_access_tokens"]
    ) -> ListAccessTokensPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListAccessTokens)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listaccesstokenspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_dev_environments"]
    ) -> ListDevEnvironmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListDevEnvironments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listdevenvironmentspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_event_logs"]) -> ListEventLogsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListEventLogs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listeventlogspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListProjects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listprojectspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_source_repositories"]
    ) -> ListSourceRepositoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListSourceRepositories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listsourcerepositoriespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_source_repository_branches"]
    ) -> ListSourceRepositoryBranchesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListSourceRepositoryBranches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listsourcerepositorybranchespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_spaces"]) -> ListSpacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/codecatalyst.html#CodeCatalyst.Paginator.ListSpaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/paginators.html#listspacespaginator)
        """
