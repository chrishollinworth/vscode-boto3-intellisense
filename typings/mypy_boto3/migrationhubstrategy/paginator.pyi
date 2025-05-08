"""
Type annotations for migrationhubstrategy service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_migrationhubstrategy.client import MigrationHubStrategyRecommendationsClient
    from mypy_boto3_migrationhubstrategy.paginator import (
        GetServerDetailsPaginator,
        ListAnalyzableServersPaginator,
        ListApplicationComponentsPaginator,
        ListCollectorsPaginator,
        ListImportFileTaskPaginator,
        ListServersPaginator,
    )

    session = Session()
    client: MigrationHubStrategyRecommendationsClient = session.client("migrationhubstrategy")

    get_server_details_paginator: GetServerDetailsPaginator = client.get_paginator("get_server_details")
    list_analyzable_servers_paginator: ListAnalyzableServersPaginator = client.get_paginator("list_analyzable_servers")
    list_application_components_paginator: ListApplicationComponentsPaginator = client.get_paginator("list_application_components")
    list_collectors_paginator: ListCollectorsPaginator = client.get_paginator("list_collectors")
    list_import_file_task_paginator: ListImportFileTaskPaginator = client.get_paginator("list_import_file_task")
    list_servers_paginator: ListServersPaginator = client.get_paginator("list_servers")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetServerDetailsRequestPaginateTypeDef,
    GetServerDetailsResponseTypeDef,
    ListAnalyzableServersRequestPaginateTypeDef,
    ListAnalyzableServersResponseTypeDef,
    ListApplicationComponentsRequestPaginateTypeDef,
    ListApplicationComponentsResponseTypeDef,
    ListCollectorsRequestPaginateTypeDef,
    ListCollectorsResponseTypeDef,
    ListImportFileTaskRequestPaginateTypeDef,
    ListImportFileTaskResponseTypeDef,
    ListServersRequestPaginateTypeDef,
    ListServersResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetServerDetailsPaginator",
    "ListAnalyzableServersPaginator",
    "ListApplicationComponentsPaginator",
    "ListCollectorsPaginator",
    "ListImportFileTaskPaginator",
    "ListServersPaginator",
)

if TYPE_CHECKING:
    _GetServerDetailsPaginatorBase = Paginator[GetServerDetailsResponseTypeDef]
else:
    _GetServerDetailsPaginatorBase = Paginator  # type: ignore[assignment]

class GetServerDetailsPaginator(_GetServerDetailsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhubstrategy/paginator/GetServerDetails.html#MigrationHubStrategyRecommendations.Paginator.GetServerDetails)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators/#getserverdetailspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetServerDetailsRequestPaginateTypeDef]
    ) -> PageIterator[GetServerDetailsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhubstrategy/paginator/GetServerDetails.html#MigrationHubStrategyRecommendations.Paginator.GetServerDetails.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators/#getserverdetailspaginator)
        """

if TYPE_CHECKING:
    _ListAnalyzableServersPaginatorBase = Paginator[ListAnalyzableServersResponseTypeDef]
else:
    _ListAnalyzableServersPaginatorBase = Paginator  # type: ignore[assignment]

class ListAnalyzableServersPaginator(_ListAnalyzableServersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhubstrategy/paginator/ListAnalyzableServers.html#MigrationHubStrategyRecommendations.Paginator.ListAnalyzableServers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators/#listanalyzableserverspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAnalyzableServersRequestPaginateTypeDef]
    ) -> PageIterator[ListAnalyzableServersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhubstrategy/paginator/ListAnalyzableServers.html#MigrationHubStrategyRecommendations.Paginator.ListAnalyzableServers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators/#listanalyzableserverspaginator)
        """

if TYPE_CHECKING:
    _ListApplicationComponentsPaginatorBase = Paginator[ListApplicationComponentsResponseTypeDef]
else:
    _ListApplicationComponentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationComponentsPaginator(_ListApplicationComponentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhubstrategy/paginator/ListApplicationComponents.html#MigrationHubStrategyRecommendations.Paginator.ListApplicationComponents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators/#listapplicationcomponentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationComponentsRequestPaginateTypeDef]
    ) -> PageIterator[ListApplicationComponentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhubstrategy/paginator/ListApplicationComponents.html#MigrationHubStrategyRecommendations.Paginator.ListApplicationComponents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators/#listapplicationcomponentspaginator)
        """

if TYPE_CHECKING:
    _ListCollectorsPaginatorBase = Paginator[ListCollectorsResponseTypeDef]
else:
    _ListCollectorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCollectorsPaginator(_ListCollectorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhubstrategy/paginator/ListCollectors.html#MigrationHubStrategyRecommendations.Paginator.ListCollectors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators/#listcollectorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCollectorsRequestPaginateTypeDef]
    ) -> PageIterator[ListCollectorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhubstrategy/paginator/ListCollectors.html#MigrationHubStrategyRecommendations.Paginator.ListCollectors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators/#listcollectorspaginator)
        """

if TYPE_CHECKING:
    _ListImportFileTaskPaginatorBase = Paginator[ListImportFileTaskResponseTypeDef]
else:
    _ListImportFileTaskPaginatorBase = Paginator  # type: ignore[assignment]

class ListImportFileTaskPaginator(_ListImportFileTaskPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhubstrategy/paginator/ListImportFileTask.html#MigrationHubStrategyRecommendations.Paginator.ListImportFileTask)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators/#listimportfiletaskpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListImportFileTaskRequestPaginateTypeDef]
    ) -> PageIterator[ListImportFileTaskResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhubstrategy/paginator/ListImportFileTask.html#MigrationHubStrategyRecommendations.Paginator.ListImportFileTask.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators/#listimportfiletaskpaginator)
        """

if TYPE_CHECKING:
    _ListServersPaginatorBase = Paginator[ListServersResponseTypeDef]
else:
    _ListServersPaginatorBase = Paginator  # type: ignore[assignment]

class ListServersPaginator(_ListServersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhubstrategy/paginator/ListServers.html#MigrationHubStrategyRecommendations.Paginator.ListServers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators/#listserverspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServersRequestPaginateTypeDef]
    ) -> PageIterator[ListServersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhubstrategy/paginator/ListServers.html#MigrationHubStrategyRecommendations.Paginator.ListServers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators/#listserverspaginator)
        """
