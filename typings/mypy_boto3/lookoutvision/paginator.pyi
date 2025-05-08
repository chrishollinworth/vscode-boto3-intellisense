"""
Type annotations for lookoutvision service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_lookoutvision.client import LookoutforVisionClient
    from mypy_boto3_lookoutvision.paginator import (
        ListDatasetEntriesPaginator,
        ListModelPackagingJobsPaginator,
        ListModelsPaginator,
        ListProjectsPaginator,
    )

    session = Session()
    client: LookoutforVisionClient = session.client("lookoutvision")

    list_dataset_entries_paginator: ListDatasetEntriesPaginator = client.get_paginator("list_dataset_entries")
    list_model_packaging_jobs_paginator: ListModelPackagingJobsPaginator = client.get_paginator("list_model_packaging_jobs")
    list_models_paginator: ListModelsPaginator = client.get_paginator("list_models")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListDatasetEntriesRequestPaginateTypeDef,
    ListDatasetEntriesResponseTypeDef,
    ListModelPackagingJobsRequestPaginateTypeDef,
    ListModelPackagingJobsResponseTypeDef,
    ListModelsRequestPaginateTypeDef,
    ListModelsResponseTypeDef,
    ListProjectsRequestPaginateTypeDef,
    ListProjectsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListDatasetEntriesPaginator",
    "ListModelPackagingJobsPaginator",
    "ListModelsPaginator",
    "ListProjectsPaginator",
)

if TYPE_CHECKING:
    _ListDatasetEntriesPaginatorBase = Paginator[ListDatasetEntriesResponseTypeDef]
else:
    _ListDatasetEntriesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDatasetEntriesPaginator(_ListDatasetEntriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/paginator/ListDatasetEntries.html#LookoutforVision.Paginator.ListDatasetEntries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/paginators/#listdatasetentriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDatasetEntriesRequestPaginateTypeDef]
    ) -> PageIterator[ListDatasetEntriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/paginator/ListDatasetEntries.html#LookoutforVision.Paginator.ListDatasetEntries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/paginators/#listdatasetentriespaginator)
        """

if TYPE_CHECKING:
    _ListModelPackagingJobsPaginatorBase = Paginator[ListModelPackagingJobsResponseTypeDef]
else:
    _ListModelPackagingJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListModelPackagingJobsPaginator(_ListModelPackagingJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/paginator/ListModelPackagingJobs.html#LookoutforVision.Paginator.ListModelPackagingJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/paginators/#listmodelpackagingjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListModelPackagingJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListModelPackagingJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/paginator/ListModelPackagingJobs.html#LookoutforVision.Paginator.ListModelPackagingJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/paginators/#listmodelpackagingjobspaginator)
        """

if TYPE_CHECKING:
    _ListModelsPaginatorBase = Paginator[ListModelsResponseTypeDef]
else:
    _ListModelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListModelsPaginator(_ListModelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/paginator/ListModels.html#LookoutforVision.Paginator.ListModels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/paginators/#listmodelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListModelsRequestPaginateTypeDef]
    ) -> PageIterator[ListModelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/paginator/ListModels.html#LookoutforVision.Paginator.ListModels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/paginators/#listmodelspaginator)
        """

if TYPE_CHECKING:
    _ListProjectsPaginatorBase = Paginator[ListProjectsResponseTypeDef]
else:
    _ListProjectsPaginatorBase = Paginator  # type: ignore[assignment]

class ListProjectsPaginator(_ListProjectsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/paginator/ListProjects.html#LookoutforVision.Paginator.ListProjects)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/paginators/#listprojectspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProjectsRequestPaginateTypeDef]
    ) -> PageIterator[ListProjectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/paginator/ListProjects.html#LookoutforVision.Paginator.ListProjects.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/paginators/#listprojectspaginator)
        """
