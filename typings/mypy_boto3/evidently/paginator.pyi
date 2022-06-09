"""
Type annotations for evidently service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_evidently import CloudWatchEvidentlyClient
    from mypy_boto3_evidently.paginator import (
        ListExperimentsPaginator,
        ListFeaturesPaginator,
        ListLaunchesPaginator,
        ListProjectsPaginator,
    )

    client: CloudWatchEvidentlyClient = boto3.client("evidently")

    list_experiments_paginator: ListExperimentsPaginator = client.get_paginator("list_experiments")
    list_features_paginator: ListFeaturesPaginator = client.get_paginator("list_features")
    list_launches_paginator: ListLaunchesPaginator = client.get_paginator("list_launches")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ExperimentStatusType, LaunchStatusType
from .type_defs import (
    ListExperimentsResponseTypeDef,
    ListFeaturesResponseTypeDef,
    ListLaunchesResponseTypeDef,
    ListProjectsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListExperimentsPaginator",
    "ListFeaturesPaginator",
    "ListLaunchesPaginator",
    "ListProjectsPaginator",
)

class ListExperimentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/evidently.html#CloudWatchEvidently.Paginator.ListExperiments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators.html#listexperimentspaginator)
    """

    def paginate(
        self,
        *,
        project: str,
        status: ExperimentStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListExperimentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/evidently.html#CloudWatchEvidently.Paginator.ListExperiments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators.html#listexperimentspaginator)
        """

class ListFeaturesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/evidently.html#CloudWatchEvidently.Paginator.ListFeatures)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators.html#listfeaturespaginator)
    """

    def paginate(
        self, *, project: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFeaturesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/evidently.html#CloudWatchEvidently.Paginator.ListFeatures.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators.html#listfeaturespaginator)
        """

class ListLaunchesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/evidently.html#CloudWatchEvidently.Paginator.ListLaunches)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators.html#listlaunchespaginator)
    """

    def paginate(
        self,
        *,
        project: str,
        status: LaunchStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLaunchesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/evidently.html#CloudWatchEvidently.Paginator.ListLaunches.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators.html#listlaunchespaginator)
        """

class ListProjectsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/evidently.html#CloudWatchEvidently.Paginator.ListProjects)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators.html#listprojectspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/evidently.html#CloudWatchEvidently.Paginator.ListProjects.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators.html#listprojectspaginator)
        """
