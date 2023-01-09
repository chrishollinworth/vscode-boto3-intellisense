"""
Type annotations for gamesparks service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_gamesparks import GameSparksClient
    from mypy_boto3_gamesparks.paginator import (
        ListExtensionVersionsPaginator,
        ListExtensionsPaginator,
        ListGamesPaginator,
        ListGeneratedCodeJobsPaginator,
        ListSnapshotsPaginator,
        ListStageDeploymentsPaginator,
        ListStagesPaginator,
    )

    client: GameSparksClient = boto3.client("gamesparks")

    list_extension_versions_paginator: ListExtensionVersionsPaginator = client.get_paginator("list_extension_versions")
    list_extensions_paginator: ListExtensionsPaginator = client.get_paginator("list_extensions")
    list_games_paginator: ListGamesPaginator = client.get_paginator("list_games")
    list_generated_code_jobs_paginator: ListGeneratedCodeJobsPaginator = client.get_paginator("list_generated_code_jobs")
    list_snapshots_paginator: ListSnapshotsPaginator = client.get_paginator("list_snapshots")
    list_stage_deployments_paginator: ListStageDeploymentsPaginator = client.get_paginator("list_stage_deployments")
    list_stages_paginator: ListStagesPaginator = client.get_paginator("list_stages")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListExtensionsResultTypeDef,
    ListExtensionVersionsResultTypeDef,
    ListGamesResultTypeDef,
    ListGeneratedCodeJobsResultTypeDef,
    ListSnapshotsResultTypeDef,
    ListStageDeploymentsResultTypeDef,
    ListStagesResultTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListExtensionVersionsPaginator",
    "ListExtensionsPaginator",
    "ListGamesPaginator",
    "ListGeneratedCodeJobsPaginator",
    "ListSnapshotsPaginator",
    "ListStageDeploymentsPaginator",
    "ListStagesPaginator",
)

class ListExtensionVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/gamesparks.html#GameSparks.Paginator.ListExtensionVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#listextensionversionspaginator)
    """

    def paginate(
        self, *, Name: str, Namespace: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListExtensionVersionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/gamesparks.html#GameSparks.Paginator.ListExtensionVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#listextensionversionspaginator)
        """

class ListExtensionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/gamesparks.html#GameSparks.Paginator.ListExtensions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#listextensionspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListExtensionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/gamesparks.html#GameSparks.Paginator.ListExtensions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#listextensionspaginator)
        """

class ListGamesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/gamesparks.html#GameSparks.Paginator.ListGames)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#listgamespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGamesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/gamesparks.html#GameSparks.Paginator.ListGames.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#listgamespaginator)
        """

class ListGeneratedCodeJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/gamesparks.html#GameSparks.Paginator.ListGeneratedCodeJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#listgeneratedcodejobspaginator)
    """

    def paginate(
        self, *, GameName: str, SnapshotId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGeneratedCodeJobsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/gamesparks.html#GameSparks.Paginator.ListGeneratedCodeJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#listgeneratedcodejobspaginator)
        """

class ListSnapshotsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/gamesparks.html#GameSparks.Paginator.ListSnapshots)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#listsnapshotspaginator)
    """

    def paginate(
        self, *, GameName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSnapshotsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/gamesparks.html#GameSparks.Paginator.ListSnapshots.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#listsnapshotspaginator)
        """

class ListStageDeploymentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/gamesparks.html#GameSparks.Paginator.ListStageDeployments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#liststagedeploymentspaginator)
    """

    def paginate(
        self, *, GameName: str, StageName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStageDeploymentsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/gamesparks.html#GameSparks.Paginator.ListStageDeployments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#liststagedeploymentspaginator)
        """

class ListStagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/gamesparks.html#GameSparks.Paginator.ListStages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#liststagespaginator)
    """

    def paginate(
        self, *, GameName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStagesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/gamesparks.html#GameSparks.Paginator.ListStages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#liststagespaginator)
        """
