"""
Type annotations for mgh service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mgh.client import MigrationHubClient

    session = Session()
    client: MigrationHubClient = session.client("mgh")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListApplicationStatesPaginator,
    ListCreatedArtifactsPaginator,
    ListDiscoveredResourcesPaginator,
    ListMigrationTasksPaginator,
    ListMigrationTaskUpdatesPaginator,
    ListProgressUpdateStreamsPaginator,
    ListSourceResourcesPaginator,
)
from .type_defs import (
    AssociateCreatedArtifactRequestTypeDef,
    AssociateDiscoveredResourceRequestTypeDef,
    AssociateSourceResourceRequestTypeDef,
    CreateProgressUpdateStreamRequestTypeDef,
    DeleteProgressUpdateStreamRequestTypeDef,
    DescribeApplicationStateRequestTypeDef,
    DescribeApplicationStateResultTypeDef,
    DescribeMigrationTaskRequestTypeDef,
    DescribeMigrationTaskResultTypeDef,
    DisassociateCreatedArtifactRequestTypeDef,
    DisassociateDiscoveredResourceRequestTypeDef,
    DisassociateSourceResourceRequestTypeDef,
    ImportMigrationTaskRequestTypeDef,
    ListApplicationStatesRequestTypeDef,
    ListApplicationStatesResultTypeDef,
    ListCreatedArtifactsRequestTypeDef,
    ListCreatedArtifactsResultTypeDef,
    ListDiscoveredResourcesRequestTypeDef,
    ListDiscoveredResourcesResultTypeDef,
    ListMigrationTasksRequestTypeDef,
    ListMigrationTasksResultTypeDef,
    ListMigrationTaskUpdatesRequestTypeDef,
    ListMigrationTaskUpdatesResultTypeDef,
    ListProgressUpdateStreamsRequestTypeDef,
    ListProgressUpdateStreamsResultTypeDef,
    ListSourceResourcesRequestTypeDef,
    ListSourceResourcesResultTypeDef,
    NotifyApplicationStateRequestTypeDef,
    NotifyMigrationTaskStateRequestTypeDef,
    PutResourceAttributesRequestTypeDef,
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

__all__ = ("MigrationHubClient",)

class Exceptions(BaseClientExceptions):
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

class MigrationHubClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MigrationHubClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#generate_presigned_url)
        """

    def associate_created_artifact(
        self, **kwargs: Unpack[AssociateCreatedArtifactRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates a created artifact of an AWS cloud resource, the target receiving
        the migration, with the migration task performed by a migration tool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/associate_created_artifact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#associate_created_artifact)
        """

    def associate_discovered_resource(
        self, **kwargs: Unpack[AssociateDiscoveredResourceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates a discovered resource ID from Application Discovery Service with a
        migration task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/associate_discovered_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#associate_discovered_resource)
        """

    def associate_source_resource(
        self, **kwargs: Unpack[AssociateSourceResourceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates a source resource with a migration task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/associate_source_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#associate_source_resource)
        """

    def create_progress_update_stream(
        self, **kwargs: Unpack[CreateProgressUpdateStreamRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates a progress update stream which is an AWS resource used for access
        control as well as a namespace for migration task names that is implicitly
        linked to your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/create_progress_update_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#create_progress_update_stream)
        """

    def delete_progress_update_stream(
        self, **kwargs: Unpack[DeleteProgressUpdateStreamRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a progress update stream, including all of its tasks, which was
        previously created as an AWS resource used for access control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/delete_progress_update_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#delete_progress_update_stream)
        """

    def describe_application_state(
        self, **kwargs: Unpack[DescribeApplicationStateRequestTypeDef]
    ) -> DescribeApplicationStateResultTypeDef:
        """
        Gets the migration status of an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/describe_application_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#describe_application_state)
        """

    def describe_migration_task(
        self, **kwargs: Unpack[DescribeMigrationTaskRequestTypeDef]
    ) -> DescribeMigrationTaskResultTypeDef:
        """
        Retrieves a list of all attributes associated with a specific migration task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/describe_migration_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#describe_migration_task)
        """

    def disassociate_created_artifact(
        self, **kwargs: Unpack[DisassociateCreatedArtifactRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates a created artifact of an AWS resource with a migration task
        performed by a migration tool that was previously associated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/disassociate_created_artifact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#disassociate_created_artifact)
        """

    def disassociate_discovered_resource(
        self, **kwargs: Unpack[DisassociateDiscoveredResourceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociate an Application Discovery Service discovered resource from a
        migration task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/disassociate_discovered_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#disassociate_discovered_resource)
        """

    def disassociate_source_resource(
        self, **kwargs: Unpack[DisassociateSourceResourceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the association between a source resource and a migration task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/disassociate_source_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#disassociate_source_resource)
        """

    def import_migration_task(
        self, **kwargs: Unpack[ImportMigrationTaskRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Registers a new migration task which represents a server, database, etc., being
        migrated to AWS by a migration tool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/import_migration_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#import_migration_task)
        """

    def list_application_states(
        self, **kwargs: Unpack[ListApplicationStatesRequestTypeDef]
    ) -> ListApplicationStatesResultTypeDef:
        """
        Lists all the migration statuses for your applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/list_application_states.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#list_application_states)
        """

    def list_created_artifacts(
        self, **kwargs: Unpack[ListCreatedArtifactsRequestTypeDef]
    ) -> ListCreatedArtifactsResultTypeDef:
        """
        Lists the created artifacts attached to a given migration task in an update
        stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/list_created_artifacts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#list_created_artifacts)
        """

    def list_discovered_resources(
        self, **kwargs: Unpack[ListDiscoveredResourcesRequestTypeDef]
    ) -> ListDiscoveredResourcesResultTypeDef:
        """
        Lists discovered resources associated with the given <code>MigrationTask</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/list_discovered_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#list_discovered_resources)
        """

    def list_migration_task_updates(
        self, **kwargs: Unpack[ListMigrationTaskUpdatesRequestTypeDef]
    ) -> ListMigrationTaskUpdatesResultTypeDef:
        """
        This is a paginated API that returns all the migration-task states for the
        specified <code>MigrationTaskName</code> and <code>ProgressUpdateStream</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/list_migration_task_updates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#list_migration_task_updates)
        """

    def list_migration_tasks(
        self, **kwargs: Unpack[ListMigrationTasksRequestTypeDef]
    ) -> ListMigrationTasksResultTypeDef:
        """
        Lists all, or filtered by resource name, migration tasks associated with the
        user account making this call.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/list_migration_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#list_migration_tasks)
        """

    def list_progress_update_streams(
        self, **kwargs: Unpack[ListProgressUpdateStreamsRequestTypeDef]
    ) -> ListProgressUpdateStreamsResultTypeDef:
        """
        Lists progress update streams associated with the user account making this call.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/list_progress_update_streams.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#list_progress_update_streams)
        """

    def list_source_resources(
        self, **kwargs: Unpack[ListSourceResourcesRequestTypeDef]
    ) -> ListSourceResourcesResultTypeDef:
        """
        Lists all the source resource that are associated with the specified
        <code>MigrationTaskName</code> and <code>ProgressUpdateStream</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/list_source_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#list_source_resources)
        """

    def notify_application_state(
        self, **kwargs: Unpack[NotifyApplicationStateRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sets the migration state of an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/notify_application_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#notify_application_state)
        """

    def notify_migration_task_state(
        self, **kwargs: Unpack[NotifyMigrationTaskStateRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Notifies Migration Hub of the current status, progress, or other detail
        regarding a migration task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/notify_migration_task_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#notify_migration_task_state)
        """

    def put_resource_attributes(
        self, **kwargs: Unpack[PutResourceAttributesRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Provides identifying details of the resource being migrated so that it can be
        associated in the Application Discovery Service repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/put_resource_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#put_resource_attributes)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_application_states"]
    ) -> ListApplicationStatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_created_artifacts"]
    ) -> ListCreatedArtifactsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_discovered_resources"]
    ) -> ListDiscoveredResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_migration_task_updates"]
    ) -> ListMigrationTaskUpdatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_migration_tasks"]
    ) -> ListMigrationTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_progress_update_streams"]
    ) -> ListProgressUpdateStreamsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_source_resources"]
    ) -> ListSourceResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/client/#get_paginator)
        """
