"""
Type annotations for evidently service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_evidently.client import CloudWatchEvidentlyClient
    from mypy_boto3_evidently.paginator import (
        ListExperimentsPaginator,
        ListFeaturesPaginator,
        ListLaunchesPaginator,
        ListProjectsPaginator,
        ListSegmentReferencesPaginator,
        ListSegmentsPaginator,
    )

    session = Session()
    client: CloudWatchEvidentlyClient = session.client("evidently")

    list_experiments_paginator: ListExperimentsPaginator = client.get_paginator("list_experiments")
    list_features_paginator: ListFeaturesPaginator = client.get_paginator("list_features")
    list_launches_paginator: ListLaunchesPaginator = client.get_paginator("list_launches")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    list_segment_references_paginator: ListSegmentReferencesPaginator = client.get_paginator("list_segment_references")
    list_segments_paginator: ListSegmentsPaginator = client.get_paginator("list_segments")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListExperimentsRequestPaginateTypeDef,
    ListExperimentsResponseTypeDef,
    ListFeaturesRequestPaginateTypeDef,
    ListFeaturesResponseTypeDef,
    ListLaunchesRequestPaginateTypeDef,
    ListLaunchesResponseTypeDef,
    ListProjectsRequestPaginateTypeDef,
    ListProjectsResponseTypeDef,
    ListSegmentReferencesRequestPaginateTypeDef,
    ListSegmentReferencesResponseTypeDef,
    ListSegmentsRequestPaginateTypeDef,
    ListSegmentsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListExperimentsPaginator",
    "ListFeaturesPaginator",
    "ListLaunchesPaginator",
    "ListProjectsPaginator",
    "ListSegmentReferencesPaginator",
    "ListSegmentsPaginator",
)

if TYPE_CHECKING:
    _ListExperimentsPaginatorBase = Paginator[ListExperimentsResponseTypeDef]
else:
    _ListExperimentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListExperimentsPaginator(_ListExperimentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/paginator/ListExperiments.html#CloudWatchEvidently.Paginator.ListExperiments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators/#listexperimentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListExperimentsRequestPaginateTypeDef]
    ) -> PageIterator[ListExperimentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/paginator/ListExperiments.html#CloudWatchEvidently.Paginator.ListExperiments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators/#listexperimentspaginator)
        """

if TYPE_CHECKING:
    _ListFeaturesPaginatorBase = Paginator[ListFeaturesResponseTypeDef]
else:
    _ListFeaturesPaginatorBase = Paginator  # type: ignore[assignment]

class ListFeaturesPaginator(_ListFeaturesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/paginator/ListFeatures.html#CloudWatchEvidently.Paginator.ListFeatures)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators/#listfeaturespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFeaturesRequestPaginateTypeDef]
    ) -> PageIterator[ListFeaturesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/paginator/ListFeatures.html#CloudWatchEvidently.Paginator.ListFeatures.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators/#listfeaturespaginator)
        """

if TYPE_CHECKING:
    _ListLaunchesPaginatorBase = Paginator[ListLaunchesResponseTypeDef]
else:
    _ListLaunchesPaginatorBase = Paginator  # type: ignore[assignment]

class ListLaunchesPaginator(_ListLaunchesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/paginator/ListLaunches.html#CloudWatchEvidently.Paginator.ListLaunches)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators/#listlaunchespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLaunchesRequestPaginateTypeDef]
    ) -> PageIterator[ListLaunchesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/paginator/ListLaunches.html#CloudWatchEvidently.Paginator.ListLaunches.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators/#listlaunchespaginator)
        """

if TYPE_CHECKING:
    _ListProjectsPaginatorBase = Paginator[ListProjectsResponseTypeDef]
else:
    _ListProjectsPaginatorBase = Paginator  # type: ignore[assignment]

class ListProjectsPaginator(_ListProjectsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/paginator/ListProjects.html#CloudWatchEvidently.Paginator.ListProjects)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators/#listprojectspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProjectsRequestPaginateTypeDef]
    ) -> PageIterator[ListProjectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/paginator/ListProjects.html#CloudWatchEvidently.Paginator.ListProjects.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators/#listprojectspaginator)
        """

if TYPE_CHECKING:
    _ListSegmentReferencesPaginatorBase = Paginator[ListSegmentReferencesResponseTypeDef]
else:
    _ListSegmentReferencesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSegmentReferencesPaginator(_ListSegmentReferencesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/paginator/ListSegmentReferences.html#CloudWatchEvidently.Paginator.ListSegmentReferences)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators/#listsegmentreferencespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSegmentReferencesRequestPaginateTypeDef]
    ) -> PageIterator[ListSegmentReferencesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/paginator/ListSegmentReferences.html#CloudWatchEvidently.Paginator.ListSegmentReferences.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators/#listsegmentreferencespaginator)
        """

if TYPE_CHECKING:
    _ListSegmentsPaginatorBase = Paginator[ListSegmentsResponseTypeDef]
else:
    _ListSegmentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSegmentsPaginator(_ListSegmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/paginator/ListSegments.html#CloudWatchEvidently.Paginator.ListSegments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators/#listsegmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSegmentsRequestPaginateTypeDef]
    ) -> PageIterator[ListSegmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/paginator/ListSegments.html#CloudWatchEvidently.Paginator.ListSegments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/paginators/#listsegmentspaginator)
        """
