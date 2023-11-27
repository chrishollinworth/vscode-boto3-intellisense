"""
Type annotations for migrationhubstrategy service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_migrationhubstrategy import MigrationHubStrategyRecommendationsClient
    from mypy_boto3_migrationhubstrategy.paginator import (
        GetServerDetailsPaginator,
        ListAnalyzableServersPaginator,
        ListApplicationComponentsPaginator,
        ListCollectorsPaginator,
        ListImportFileTaskPaginator,
        ListServersPaginator,
    )

    client: MigrationHubStrategyRecommendationsClient = boto3.client("migrationhubstrategy")

    get_server_details_paginator: GetServerDetailsPaginator = client.get_paginator("get_server_details")
    list_analyzable_servers_paginator: ListAnalyzableServersPaginator = client.get_paginator("list_analyzable_servers")
    list_application_components_paginator: ListApplicationComponentsPaginator = client.get_paginator("list_application_components")
    list_collectors_paginator: ListCollectorsPaginator = client.get_paginator("list_collectors")
    list_import_file_task_paginator: ListImportFileTaskPaginator = client.get_paginator("list_import_file_task")
    list_servers_paginator: ListServersPaginator = client.get_paginator("list_servers")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ApplicationComponentCriteriaType, ServerCriteriaType, SortOrderType
from .type_defs import (
    GetServerDetailsResponseTypeDef,
    GroupTypeDef,
    ListAnalyzableServersResponseTypeDef,
    ListApplicationComponentsResponseTypeDef,
    ListCollectorsResponseTypeDef,
    ListImportFileTaskResponseTypeDef,
    ListServersResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "GetServerDetailsPaginator",
    "ListAnalyzableServersPaginator",
    "ListApplicationComponentsPaginator",
    "ListCollectorsPaginator",
    "ListImportFileTaskPaginator",
    "ListServersPaginator",
)

class GetServerDetailsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Paginator.GetServerDetails)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators.html#getserverdetailspaginator)
    """

    def paginate(
        self, *, serverId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetServerDetailsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Paginator.GetServerDetails.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators.html#getserverdetailspaginator)
        """

class ListAnalyzableServersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Paginator.ListAnalyzableServers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators.html#listanalyzableserverspaginator)
    """

    def paginate(
        self, *, sort: SortOrderType = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAnalyzableServersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Paginator.ListAnalyzableServers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators.html#listanalyzableserverspaginator)
        """

class ListApplicationComponentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Paginator.ListApplicationComponents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators.html#listapplicationcomponentspaginator)
    """

    def paginate(
        self,
        *,
        applicationComponentCriteria: ApplicationComponentCriteriaType = None,
        filterValue: str = None,
        groupIdFilter: List["GroupTypeDef"] = None,
        sort: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationComponentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Paginator.ListApplicationComponents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators.html#listapplicationcomponentspaginator)
        """

class ListCollectorsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Paginator.ListCollectors)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators.html#listcollectorspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCollectorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Paginator.ListCollectors.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators.html#listcollectorspaginator)
        """

class ListImportFileTaskPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Paginator.ListImportFileTask)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators.html#listimportfiletaskpaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListImportFileTaskResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Paginator.ListImportFileTask.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators.html#listimportfiletaskpaginator)
        """

class ListServersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Paginator.ListServers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators.html#listserverspaginator)
    """

    def paginate(
        self,
        *,
        filterValue: str = None,
        groupIdFilter: List["GroupTypeDef"] = None,
        serverCriteria: ServerCriteriaType = None,
        sort: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Paginator.ListServers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators.html#listserverspaginator)
        """
