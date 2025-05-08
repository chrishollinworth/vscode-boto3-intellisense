"""
Type annotations for mgh service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_mgh.client import MigrationHubClient
    from mypy_boto3_mgh.paginator import (
        ListApplicationStatesPaginator,
        ListCreatedArtifactsPaginator,
        ListDiscoveredResourcesPaginator,
        ListMigrationTaskUpdatesPaginator,
        ListMigrationTasksPaginator,
        ListProgressUpdateStreamsPaginator,
        ListSourceResourcesPaginator,
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListApplicationStatesRequestPaginateTypeDef,
    ListApplicationStatesResultTypeDef,
    ListCreatedArtifactsRequestPaginateTypeDef,
    ListCreatedArtifactsResultTypeDef,
    ListDiscoveredResourcesRequestPaginateTypeDef,
    ListDiscoveredResourcesResultTypeDef,
    ListMigrationTasksRequestPaginateTypeDef,
    ListMigrationTasksResultTypeDef,
    ListMigrationTaskUpdatesRequestPaginateTypeDef,
    ListMigrationTaskUpdatesResultTypeDef,
    ListProgressUpdateStreamsRequestPaginateTypeDef,
    ListProgressUpdateStreamsResultTypeDef,
    ListSourceResourcesRequestPaginateTypeDef,
    ListSourceResourcesResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListApplicationStatesPaginator",
    "ListCreatedArtifactsPaginator",
    "ListDiscoveredResourcesPaginator",
    "ListMigrationTaskUpdatesPaginator",
    "ListMigrationTasksPaginator",
    "ListProgressUpdateStreamsPaginator",
    "ListSourceResourcesPaginator",
)

if TYPE_CHECKING:
    _ListApplicationStatesPaginatorBase = Paginator[ListApplicationStatesResultTypeDef]
else:
    _ListApplicationStatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationStatesPaginator(_ListApplicationStatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/paginator/ListApplicationStates.html#MigrationHub.Paginator.ListApplicationStates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators/#listapplicationstatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationStatesRequestPaginateTypeDef]
    ) -> PageIterator[ListApplicationStatesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/paginator/ListApplicationStates.html#MigrationHub.Paginator.ListApplicationStates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators/#listapplicationstatespaginator)
        """

if TYPE_CHECKING:
    _ListCreatedArtifactsPaginatorBase = Paginator[ListCreatedArtifactsResultTypeDef]
else:
    _ListCreatedArtifactsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCreatedArtifactsPaginator(_ListCreatedArtifactsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/paginator/ListCreatedArtifacts.html#MigrationHub.Paginator.ListCreatedArtifacts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators/#listcreatedartifactspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCreatedArtifactsRequestPaginateTypeDef]
    ) -> PageIterator[ListCreatedArtifactsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/paginator/ListCreatedArtifacts.html#MigrationHub.Paginator.ListCreatedArtifacts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators/#listcreatedartifactspaginator)
        """

if TYPE_CHECKING:
    _ListDiscoveredResourcesPaginatorBase = Paginator[ListDiscoveredResourcesResultTypeDef]
else:
    _ListDiscoveredResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDiscoveredResourcesPaginator(_ListDiscoveredResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/paginator/ListDiscoveredResources.html#MigrationHub.Paginator.ListDiscoveredResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators/#listdiscoveredresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDiscoveredResourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListDiscoveredResourcesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/paginator/ListDiscoveredResources.html#MigrationHub.Paginator.ListDiscoveredResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators/#listdiscoveredresourcespaginator)
        """

if TYPE_CHECKING:
    _ListMigrationTaskUpdatesPaginatorBase = Paginator[ListMigrationTaskUpdatesResultTypeDef]
else:
    _ListMigrationTaskUpdatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListMigrationTaskUpdatesPaginator(_ListMigrationTaskUpdatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/paginator/ListMigrationTaskUpdates.html#MigrationHub.Paginator.ListMigrationTaskUpdates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators/#listmigrationtaskupdatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMigrationTaskUpdatesRequestPaginateTypeDef]
    ) -> PageIterator[ListMigrationTaskUpdatesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/paginator/ListMigrationTaskUpdates.html#MigrationHub.Paginator.ListMigrationTaskUpdates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators/#listmigrationtaskupdatespaginator)
        """

if TYPE_CHECKING:
    _ListMigrationTasksPaginatorBase = Paginator[ListMigrationTasksResultTypeDef]
else:
    _ListMigrationTasksPaginatorBase = Paginator  # type: ignore[assignment]

class ListMigrationTasksPaginator(_ListMigrationTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/paginator/ListMigrationTasks.html#MigrationHub.Paginator.ListMigrationTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators/#listmigrationtaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMigrationTasksRequestPaginateTypeDef]
    ) -> PageIterator[ListMigrationTasksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/paginator/ListMigrationTasks.html#MigrationHub.Paginator.ListMigrationTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators/#listmigrationtaskspaginator)
        """

if TYPE_CHECKING:
    _ListProgressUpdateStreamsPaginatorBase = Paginator[ListProgressUpdateStreamsResultTypeDef]
else:
    _ListProgressUpdateStreamsPaginatorBase = Paginator  # type: ignore[assignment]

class ListProgressUpdateStreamsPaginator(_ListProgressUpdateStreamsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/paginator/ListProgressUpdateStreams.html#MigrationHub.Paginator.ListProgressUpdateStreams)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators/#listprogressupdatestreamspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProgressUpdateStreamsRequestPaginateTypeDef]
    ) -> PageIterator[ListProgressUpdateStreamsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/paginator/ListProgressUpdateStreams.html#MigrationHub.Paginator.ListProgressUpdateStreams.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators/#listprogressupdatestreamspaginator)
        """

if TYPE_CHECKING:
    _ListSourceResourcesPaginatorBase = Paginator[ListSourceResourcesResultTypeDef]
else:
    _ListSourceResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSourceResourcesPaginator(_ListSourceResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/paginator/ListSourceResources.html#MigrationHub.Paginator.ListSourceResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators/#listsourceresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSourceResourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListSourceResourcesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh/paginator/ListSourceResources.html#MigrationHub.Paginator.ListSourceResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators/#listsourceresourcespaginator)
        """
