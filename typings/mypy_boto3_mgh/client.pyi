# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for mgh service client

Usage::

    ```python
    import boto3
    from mypy_boto3_mgh import MigrationHubClient

    client: MigrationHubClient = boto3.client("mgh")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_mgh.paginator import (
    ListApplicationStatesPaginator,
    ListCreatedArtifactsPaginator,
    ListDiscoveredResourcesPaginator,
    ListMigrationTasksPaginator,
    ListProgressUpdateStreamsPaginator,
)
from mypy_boto3_mgh.type_defs import (
    CreatedArtifactTypeDef,
    DescribeApplicationStateResultTypeDef,
    DescribeMigrationTaskResultTypeDef,
    DiscoveredResourceTypeDef,
    ListApplicationStatesResultTypeDef,
    ListCreatedArtifactsResultTypeDef,
    ListDiscoveredResourcesResultTypeDef,
    ListMigrationTasksResultTypeDef,
    ListProgressUpdateStreamsResultTypeDef,
    ResourceAttributeTypeDef,
    TaskTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MigrationHubClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DryRunOperation: Type[BotocoreClientError]
    HomeRegionNotSetException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    PolicyErrorException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnauthorizedOperation: Type[BotocoreClientError]


class MigrationHubClient:
    """
    [MigrationHub.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_created_artifact(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        CreatedArtifact: "CreatedArtifactTypeDef",
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.associate_created_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Client.associate_created_artifact)
        """

    def associate_discovered_resource(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        DiscoveredResource: "DiscoveredResourceTypeDef",
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.associate_discovered_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Client.associate_discovered_resource)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Client.can_paginate)
        """

    def create_progress_update_stream(
        self, ProgressUpdateStreamName: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.create_progress_update_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Client.create_progress_update_stream)
        """

    def delete_progress_update_stream(
        self, ProgressUpdateStreamName: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_progress_update_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Client.delete_progress_update_stream)
        """

    def describe_application_state(
        self, ApplicationId: str
    ) -> DescribeApplicationStateResultTypeDef:
        """
        [Client.describe_application_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Client.describe_application_state)
        """

    def describe_migration_task(
        self, ProgressUpdateStream: str, MigrationTaskName: str
    ) -> DescribeMigrationTaskResultTypeDef:
        """
        [Client.describe_migration_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Client.describe_migration_task)
        """

    def disassociate_created_artifact(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        CreatedArtifactName: str,
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_created_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Client.disassociate_created_artifact)
        """

    def disassociate_discovered_resource(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        ConfigurationId: str,
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_discovered_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Client.disassociate_discovered_resource)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Client.generate_presigned_url)
        """

    def import_migration_task(
        self, ProgressUpdateStream: str, MigrationTaskName: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.import_migration_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Client.import_migration_task)
        """

    def list_application_states(
        self, ApplicationIds: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> ListApplicationStatesResultTypeDef:
        """
        [Client.list_application_states documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Client.list_application_states)
        """

    def list_created_artifacts(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListCreatedArtifactsResultTypeDef:
        """
        [Client.list_created_artifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Client.list_created_artifacts)
        """

    def list_discovered_resources(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListDiscoveredResourcesResultTypeDef:
        """
        [Client.list_discovered_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Client.list_discovered_resources)
        """

    def list_migration_tasks(
        self, NextToken: str = None, MaxResults: int = None, ResourceName: str = None
    ) -> ListMigrationTasksResultTypeDef:
        """
        [Client.list_migration_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Client.list_migration_tasks)
        """

    def list_progress_update_streams(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListProgressUpdateStreamsResultTypeDef:
        """
        [Client.list_progress_update_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Client.list_progress_update_streams)
        """

    def notify_application_state(
        self,
        ApplicationId: str,
        Status: Literal["NOT_STARTED", "IN_PROGRESS", "COMPLETED"],
        UpdateDateTime: datetime = None,
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.notify_application_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Client.notify_application_state)
        """

    def notify_migration_task_state(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        Task: "TaskTypeDef",
        UpdateDateTime: datetime,
        NextUpdateSeconds: int,
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.notify_migration_task_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Client.notify_migration_task_state)
        """

    def put_resource_attributes(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        ResourceAttributeList: List["ResourceAttributeTypeDef"],
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_resource_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Client.put_resource_attributes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_states"]
    ) -> ListApplicationStatesPaginator:
        """
        [Paginator.ListApplicationStates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Paginator.ListApplicationStates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_created_artifacts"]
    ) -> ListCreatedArtifactsPaginator:
        """
        [Paginator.ListCreatedArtifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Paginator.ListCreatedArtifacts)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_discovered_resources"]
    ) -> ListDiscoveredResourcesPaginator:
        """
        [Paginator.ListDiscoveredResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Paginator.ListDiscoveredResources)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_migration_tasks"]
    ) -> ListMigrationTasksPaginator:
        """
        [Paginator.ListMigrationTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Paginator.ListMigrationTasks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_progress_update_streams"]
    ) -> ListProgressUpdateStreamsPaginator:
        """
        [Paginator.ListProgressUpdateStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mgh.html#MigrationHub.Paginator.ListProgressUpdateStreams)
        """
