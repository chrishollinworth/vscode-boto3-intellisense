"""
Type annotations for medical-imaging service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_medical_imaging import HealthImagingClient
    from mypy_boto3_medical_imaging.paginator import (
        ListDICOMImportJobsPaginator,
        ListDatastoresPaginator,
        ListImageSetVersionsPaginator,
        SearchImageSetsPaginator,
    )

    client: HealthImagingClient = boto3.client("medical-imaging")

    list_dicom_import_jobs_paginator: ListDICOMImportJobsPaginator = client.get_paginator("list_dicom_import_jobs")
    list_datastores_paginator: ListDatastoresPaginator = client.get_paginator("list_datastores")
    list_image_set_versions_paginator: ListImageSetVersionsPaginator = client.get_paginator("list_image_set_versions")
    search_image_sets_paginator: SearchImageSetsPaginator = client.get_paginator("search_image_sets")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import DatastoreStatusType, JobStatusType
from .type_defs import (
    ListDatastoresResponseTypeDef,
    ListDICOMImportJobsResponseTypeDef,
    ListImageSetVersionsResponseTypeDef,
    PaginatorConfigTypeDef,
    SearchCriteriaTypeDef,
    SearchImageSetsResponseTypeDef,
)

__all__ = (
    "ListDICOMImportJobsPaginator",
    "ListDatastoresPaginator",
    "ListImageSetVersionsPaginator",
    "SearchImageSetsPaginator",
)

class ListDICOMImportJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/medical-imaging.html#HealthImaging.Paginator.ListDICOMImportJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators.html#listdicomimportjobspaginator)
    """

    def paginate(
        self,
        *,
        datastoreId: str,
        jobStatus: JobStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDICOMImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/medical-imaging.html#HealthImaging.Paginator.ListDICOMImportJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators.html#listdicomimportjobspaginator)
        """

class ListDatastoresPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/medical-imaging.html#HealthImaging.Paginator.ListDatastores)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators.html#listdatastorespaginator)
    """

    def paginate(
        self,
        *,
        datastoreStatus: DatastoreStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatastoresResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/medical-imaging.html#HealthImaging.Paginator.ListDatastores.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators.html#listdatastorespaginator)
        """

class ListImageSetVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/medical-imaging.html#HealthImaging.Paginator.ListImageSetVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators.html#listimagesetversionspaginator)
    """

    def paginate(
        self, *, datastoreId: str, imageSetId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListImageSetVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/medical-imaging.html#HealthImaging.Paginator.ListImageSetVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators.html#listimagesetversionspaginator)
        """

class SearchImageSetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/medical-imaging.html#HealthImaging.Paginator.SearchImageSets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators.html#searchimagesetspaginator)
    """

    def paginate(
        self,
        *,
        datastoreId: str,
        searchCriteria: "SearchCriteriaTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchImageSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/medical-imaging.html#HealthImaging.Paginator.SearchImageSets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators.html#searchimagesetspaginator)
        """
