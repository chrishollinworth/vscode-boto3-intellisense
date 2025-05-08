"""
Type annotations for medical-imaging service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_medical_imaging.client import HealthImagingClient
    from mypy_boto3_medical_imaging.paginator import (
        ListDICOMImportJobsPaginator,
        ListDatastoresPaginator,
        ListImageSetVersionsPaginator,
        SearchImageSetsPaginator,
    )

    session = Session()
    client: HealthImagingClient = session.client("medical-imaging")

    list_dicom_import_jobs_paginator: ListDICOMImportJobsPaginator = client.get_paginator("list_dicom_import_jobs")
    list_datastores_paginator: ListDatastoresPaginator = client.get_paginator("list_datastores")
    list_image_set_versions_paginator: ListImageSetVersionsPaginator = client.get_paginator("list_image_set_versions")
    search_image_sets_paginator: SearchImageSetsPaginator = client.get_paginator("search_image_sets")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListDatastoresRequestPaginateTypeDef,
    ListDatastoresResponseTypeDef,
    ListDICOMImportJobsRequestPaginateTypeDef,
    ListDICOMImportJobsResponseTypeDef,
    ListImageSetVersionsRequestPaginateTypeDef,
    ListImageSetVersionsResponseTypeDef,
    SearchImageSetsRequestPaginateTypeDef,
    SearchImageSetsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListDICOMImportJobsPaginator",
    "ListDatastoresPaginator",
    "ListImageSetVersionsPaginator",
    "SearchImageSetsPaginator",
)

if TYPE_CHECKING:
    _ListDICOMImportJobsPaginatorBase = Paginator[ListDICOMImportJobsResponseTypeDef]
else:
    _ListDICOMImportJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDICOMImportJobsPaginator(_ListDICOMImportJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/paginator/ListDICOMImportJobs.html#HealthImaging.Paginator.ListDICOMImportJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators/#listdicomimportjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDICOMImportJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListDICOMImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/paginator/ListDICOMImportJobs.html#HealthImaging.Paginator.ListDICOMImportJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators/#listdicomimportjobspaginator)
        """

if TYPE_CHECKING:
    _ListDatastoresPaginatorBase = Paginator[ListDatastoresResponseTypeDef]
else:
    _ListDatastoresPaginatorBase = Paginator  # type: ignore[assignment]

class ListDatastoresPaginator(_ListDatastoresPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/paginator/ListDatastores.html#HealthImaging.Paginator.ListDatastores)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators/#listdatastorespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDatastoresRequestPaginateTypeDef]
    ) -> PageIterator[ListDatastoresResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/paginator/ListDatastores.html#HealthImaging.Paginator.ListDatastores.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators/#listdatastorespaginator)
        """

if TYPE_CHECKING:
    _ListImageSetVersionsPaginatorBase = Paginator[ListImageSetVersionsResponseTypeDef]
else:
    _ListImageSetVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListImageSetVersionsPaginator(_ListImageSetVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/paginator/ListImageSetVersions.html#HealthImaging.Paginator.ListImageSetVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators/#listimagesetversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListImageSetVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListImageSetVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/paginator/ListImageSetVersions.html#HealthImaging.Paginator.ListImageSetVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators/#listimagesetversionspaginator)
        """

if TYPE_CHECKING:
    _SearchImageSetsPaginatorBase = Paginator[SearchImageSetsResponseTypeDef]
else:
    _SearchImageSetsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchImageSetsPaginator(_SearchImageSetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/paginator/SearchImageSets.html#HealthImaging.Paginator.SearchImageSets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators/#searchimagesetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchImageSetsRequestPaginateTypeDef]
    ) -> PageIterator[SearchImageSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/paginator/SearchImageSets.html#HealthImaging.Paginator.SearchImageSets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators/#searchimagesetspaginator)
        """
