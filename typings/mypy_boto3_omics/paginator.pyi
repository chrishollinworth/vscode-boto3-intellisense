"""
Type annotations for omics service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_omics.client import OmicsClient
    from mypy_boto3_omics.paginator import (
        ListAnnotationImportJobsPaginator,
        ListAnnotationStoreVersionsPaginator,
        ListAnnotationStoresPaginator,
        ListMultipartReadSetUploadsPaginator,
        ListReadSetActivationJobsPaginator,
        ListReadSetExportJobsPaginator,
        ListReadSetImportJobsPaginator,
        ListReadSetUploadPartsPaginator,
        ListReadSetsPaginator,
        ListReferenceImportJobsPaginator,
        ListReferenceStoresPaginator,
        ListReferencesPaginator,
        ListRunCachesPaginator,
        ListRunGroupsPaginator,
        ListRunTasksPaginator,
        ListRunsPaginator,
        ListSequenceStoresPaginator,
        ListSharesPaginator,
        ListVariantImportJobsPaginator,
        ListVariantStoresPaginator,
        ListWorkflowVersionsPaginator,
        ListWorkflowsPaginator,
    )

    session = Session()
    client: OmicsClient = session.client("omics")

    list_annotation_import_jobs_paginator: ListAnnotationImportJobsPaginator = client.get_paginator("list_annotation_import_jobs")
    list_annotation_store_versions_paginator: ListAnnotationStoreVersionsPaginator = client.get_paginator("list_annotation_store_versions")
    list_annotation_stores_paginator: ListAnnotationStoresPaginator = client.get_paginator("list_annotation_stores")
    list_multipart_read_set_uploads_paginator: ListMultipartReadSetUploadsPaginator = client.get_paginator("list_multipart_read_set_uploads")
    list_read_set_activation_jobs_paginator: ListReadSetActivationJobsPaginator = client.get_paginator("list_read_set_activation_jobs")
    list_read_set_export_jobs_paginator: ListReadSetExportJobsPaginator = client.get_paginator("list_read_set_export_jobs")
    list_read_set_import_jobs_paginator: ListReadSetImportJobsPaginator = client.get_paginator("list_read_set_import_jobs")
    list_read_set_upload_parts_paginator: ListReadSetUploadPartsPaginator = client.get_paginator("list_read_set_upload_parts")
    list_read_sets_paginator: ListReadSetsPaginator = client.get_paginator("list_read_sets")
    list_reference_import_jobs_paginator: ListReferenceImportJobsPaginator = client.get_paginator("list_reference_import_jobs")
    list_reference_stores_paginator: ListReferenceStoresPaginator = client.get_paginator("list_reference_stores")
    list_references_paginator: ListReferencesPaginator = client.get_paginator("list_references")
    list_run_caches_paginator: ListRunCachesPaginator = client.get_paginator("list_run_caches")
    list_run_groups_paginator: ListRunGroupsPaginator = client.get_paginator("list_run_groups")
    list_run_tasks_paginator: ListRunTasksPaginator = client.get_paginator("list_run_tasks")
    list_runs_paginator: ListRunsPaginator = client.get_paginator("list_runs")
    list_sequence_stores_paginator: ListSequenceStoresPaginator = client.get_paginator("list_sequence_stores")
    list_shares_paginator: ListSharesPaginator = client.get_paginator("list_shares")
    list_variant_import_jobs_paginator: ListVariantImportJobsPaginator = client.get_paginator("list_variant_import_jobs")
    list_variant_stores_paginator: ListVariantStoresPaginator = client.get_paginator("list_variant_stores")
    list_workflow_versions_paginator: ListWorkflowVersionsPaginator = client.get_paginator("list_workflow_versions")
    list_workflows_paginator: ListWorkflowsPaginator = client.get_paginator("list_workflows")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAnnotationImportJobsRequestPaginateTypeDef,
    ListAnnotationImportJobsResponseTypeDef,
    ListAnnotationStoresRequestPaginateTypeDef,
    ListAnnotationStoresResponseTypeDef,
    ListAnnotationStoreVersionsRequestPaginateTypeDef,
    ListAnnotationStoreVersionsResponseTypeDef,
    ListMultipartReadSetUploadsRequestPaginateTypeDef,
    ListMultipartReadSetUploadsResponseTypeDef,
    ListReadSetActivationJobsRequestPaginateTypeDef,
    ListReadSetActivationJobsResponseTypeDef,
    ListReadSetExportJobsRequestPaginateTypeDef,
    ListReadSetExportJobsResponseTypeDef,
    ListReadSetImportJobsRequestPaginateTypeDef,
    ListReadSetImportJobsResponseTypeDef,
    ListReadSetsRequestPaginateTypeDef,
    ListReadSetsResponseTypeDef,
    ListReadSetUploadPartsRequestPaginateTypeDef,
    ListReadSetUploadPartsResponseTypeDef,
    ListReferenceImportJobsRequestPaginateTypeDef,
    ListReferenceImportJobsResponseTypeDef,
    ListReferencesRequestPaginateTypeDef,
    ListReferencesResponseTypeDef,
    ListReferenceStoresRequestPaginateTypeDef,
    ListReferenceStoresResponseTypeDef,
    ListRunCachesRequestPaginateTypeDef,
    ListRunCachesResponseTypeDef,
    ListRunGroupsRequestPaginateTypeDef,
    ListRunGroupsResponseTypeDef,
    ListRunsRequestPaginateTypeDef,
    ListRunsResponseTypeDef,
    ListRunTasksRequestPaginateTypeDef,
    ListRunTasksResponseTypeDef,
    ListSequenceStoresRequestPaginateTypeDef,
    ListSequenceStoresResponseTypeDef,
    ListSharesRequestPaginateTypeDef,
    ListSharesResponseTypeDef,
    ListVariantImportJobsRequestPaginateTypeDef,
    ListVariantImportJobsResponseTypeDef,
    ListVariantStoresRequestPaginateTypeDef,
    ListVariantStoresResponseTypeDef,
    ListWorkflowsRequestPaginateTypeDef,
    ListWorkflowsResponseTypeDef,
    ListWorkflowVersionsRequestPaginateTypeDef,
    ListWorkflowVersionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAnnotationImportJobsPaginator",
    "ListAnnotationStoreVersionsPaginator",
    "ListAnnotationStoresPaginator",
    "ListMultipartReadSetUploadsPaginator",
    "ListReadSetActivationJobsPaginator",
    "ListReadSetExportJobsPaginator",
    "ListReadSetImportJobsPaginator",
    "ListReadSetUploadPartsPaginator",
    "ListReadSetsPaginator",
    "ListReferenceImportJobsPaginator",
    "ListReferenceStoresPaginator",
    "ListReferencesPaginator",
    "ListRunCachesPaginator",
    "ListRunGroupsPaginator",
    "ListRunTasksPaginator",
    "ListRunsPaginator",
    "ListSequenceStoresPaginator",
    "ListSharesPaginator",
    "ListVariantImportJobsPaginator",
    "ListVariantStoresPaginator",
    "ListWorkflowVersionsPaginator",
    "ListWorkflowsPaginator",
)

if TYPE_CHECKING:
    _ListAnnotationImportJobsPaginatorBase = Paginator[ListAnnotationImportJobsResponseTypeDef]
else:
    _ListAnnotationImportJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAnnotationImportJobsPaginator(_ListAnnotationImportJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListAnnotationImportJobs.html#Omics.Paginator.ListAnnotationImportJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listannotationimportjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAnnotationImportJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListAnnotationImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListAnnotationImportJobs.html#Omics.Paginator.ListAnnotationImportJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listannotationimportjobspaginator)
        """

if TYPE_CHECKING:
    _ListAnnotationStoreVersionsPaginatorBase = Paginator[
        ListAnnotationStoreVersionsResponseTypeDef
    ]
else:
    _ListAnnotationStoreVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAnnotationStoreVersionsPaginator(_ListAnnotationStoreVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListAnnotationStoreVersions.html#Omics.Paginator.ListAnnotationStoreVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listannotationstoreversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAnnotationStoreVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListAnnotationStoreVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListAnnotationStoreVersions.html#Omics.Paginator.ListAnnotationStoreVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listannotationstoreversionspaginator)
        """

if TYPE_CHECKING:
    _ListAnnotationStoresPaginatorBase = Paginator[ListAnnotationStoresResponseTypeDef]
else:
    _ListAnnotationStoresPaginatorBase = Paginator  # type: ignore[assignment]

class ListAnnotationStoresPaginator(_ListAnnotationStoresPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListAnnotationStores.html#Omics.Paginator.ListAnnotationStores)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listannotationstorespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAnnotationStoresRequestPaginateTypeDef]
    ) -> PageIterator[ListAnnotationStoresResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListAnnotationStores.html#Omics.Paginator.ListAnnotationStores.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listannotationstorespaginator)
        """

if TYPE_CHECKING:
    _ListMultipartReadSetUploadsPaginatorBase = Paginator[
        ListMultipartReadSetUploadsResponseTypeDef
    ]
else:
    _ListMultipartReadSetUploadsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMultipartReadSetUploadsPaginator(_ListMultipartReadSetUploadsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListMultipartReadSetUploads.html#Omics.Paginator.ListMultipartReadSetUploads)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listmultipartreadsetuploadspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMultipartReadSetUploadsRequestPaginateTypeDef]
    ) -> PageIterator[ListMultipartReadSetUploadsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListMultipartReadSetUploads.html#Omics.Paginator.ListMultipartReadSetUploads.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listmultipartreadsetuploadspaginator)
        """

if TYPE_CHECKING:
    _ListReadSetActivationJobsPaginatorBase = Paginator[ListReadSetActivationJobsResponseTypeDef]
else:
    _ListReadSetActivationJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListReadSetActivationJobsPaginator(_ListReadSetActivationJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListReadSetActivationJobs.html#Omics.Paginator.ListReadSetActivationJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listreadsetactivationjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReadSetActivationJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListReadSetActivationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListReadSetActivationJobs.html#Omics.Paginator.ListReadSetActivationJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listreadsetactivationjobspaginator)
        """

if TYPE_CHECKING:
    _ListReadSetExportJobsPaginatorBase = Paginator[ListReadSetExportJobsResponseTypeDef]
else:
    _ListReadSetExportJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListReadSetExportJobsPaginator(_ListReadSetExportJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListReadSetExportJobs.html#Omics.Paginator.ListReadSetExportJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listreadsetexportjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReadSetExportJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListReadSetExportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListReadSetExportJobs.html#Omics.Paginator.ListReadSetExportJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listreadsetexportjobspaginator)
        """

if TYPE_CHECKING:
    _ListReadSetImportJobsPaginatorBase = Paginator[ListReadSetImportJobsResponseTypeDef]
else:
    _ListReadSetImportJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListReadSetImportJobsPaginator(_ListReadSetImportJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListReadSetImportJobs.html#Omics.Paginator.ListReadSetImportJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listreadsetimportjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReadSetImportJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListReadSetImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListReadSetImportJobs.html#Omics.Paginator.ListReadSetImportJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listreadsetimportjobspaginator)
        """

if TYPE_CHECKING:
    _ListReadSetUploadPartsPaginatorBase = Paginator[ListReadSetUploadPartsResponseTypeDef]
else:
    _ListReadSetUploadPartsPaginatorBase = Paginator  # type: ignore[assignment]

class ListReadSetUploadPartsPaginator(_ListReadSetUploadPartsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListReadSetUploadParts.html#Omics.Paginator.ListReadSetUploadParts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listreadsetuploadpartspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReadSetUploadPartsRequestPaginateTypeDef]
    ) -> PageIterator[ListReadSetUploadPartsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListReadSetUploadParts.html#Omics.Paginator.ListReadSetUploadParts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listreadsetuploadpartspaginator)
        """

if TYPE_CHECKING:
    _ListReadSetsPaginatorBase = Paginator[ListReadSetsResponseTypeDef]
else:
    _ListReadSetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListReadSetsPaginator(_ListReadSetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListReadSets.html#Omics.Paginator.ListReadSets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listreadsetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReadSetsRequestPaginateTypeDef]
    ) -> PageIterator[ListReadSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListReadSets.html#Omics.Paginator.ListReadSets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listreadsetspaginator)
        """

if TYPE_CHECKING:
    _ListReferenceImportJobsPaginatorBase = Paginator[ListReferenceImportJobsResponseTypeDef]
else:
    _ListReferenceImportJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListReferenceImportJobsPaginator(_ListReferenceImportJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListReferenceImportJobs.html#Omics.Paginator.ListReferenceImportJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listreferenceimportjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReferenceImportJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListReferenceImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListReferenceImportJobs.html#Omics.Paginator.ListReferenceImportJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listreferenceimportjobspaginator)
        """

if TYPE_CHECKING:
    _ListReferenceStoresPaginatorBase = Paginator[ListReferenceStoresResponseTypeDef]
else:
    _ListReferenceStoresPaginatorBase = Paginator  # type: ignore[assignment]

class ListReferenceStoresPaginator(_ListReferenceStoresPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListReferenceStores.html#Omics.Paginator.ListReferenceStores)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listreferencestorespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReferenceStoresRequestPaginateTypeDef]
    ) -> PageIterator[ListReferenceStoresResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListReferenceStores.html#Omics.Paginator.ListReferenceStores.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listreferencestorespaginator)
        """

if TYPE_CHECKING:
    _ListReferencesPaginatorBase = Paginator[ListReferencesResponseTypeDef]
else:
    _ListReferencesPaginatorBase = Paginator  # type: ignore[assignment]

class ListReferencesPaginator(_ListReferencesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListReferences.html#Omics.Paginator.ListReferences)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listreferencespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReferencesRequestPaginateTypeDef]
    ) -> PageIterator[ListReferencesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListReferences.html#Omics.Paginator.ListReferences.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listreferencespaginator)
        """

if TYPE_CHECKING:
    _ListRunCachesPaginatorBase = Paginator[ListRunCachesResponseTypeDef]
else:
    _ListRunCachesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRunCachesPaginator(_ListRunCachesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListRunCaches.html#Omics.Paginator.ListRunCaches)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listruncachespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRunCachesRequestPaginateTypeDef]
    ) -> PageIterator[ListRunCachesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListRunCaches.html#Omics.Paginator.ListRunCaches.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listruncachespaginator)
        """

if TYPE_CHECKING:
    _ListRunGroupsPaginatorBase = Paginator[ListRunGroupsResponseTypeDef]
else:
    _ListRunGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRunGroupsPaginator(_ListRunGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListRunGroups.html#Omics.Paginator.ListRunGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listrungroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRunGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListRunGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListRunGroups.html#Omics.Paginator.ListRunGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listrungroupspaginator)
        """

if TYPE_CHECKING:
    _ListRunTasksPaginatorBase = Paginator[ListRunTasksResponseTypeDef]
else:
    _ListRunTasksPaginatorBase = Paginator  # type: ignore[assignment]

class ListRunTasksPaginator(_ListRunTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListRunTasks.html#Omics.Paginator.ListRunTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listruntaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRunTasksRequestPaginateTypeDef]
    ) -> PageIterator[ListRunTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListRunTasks.html#Omics.Paginator.ListRunTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listruntaskspaginator)
        """

if TYPE_CHECKING:
    _ListRunsPaginatorBase = Paginator[ListRunsResponseTypeDef]
else:
    _ListRunsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRunsPaginator(_ListRunsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListRuns.html#Omics.Paginator.ListRuns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listrunspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRunsRequestPaginateTypeDef]
    ) -> PageIterator[ListRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListRuns.html#Omics.Paginator.ListRuns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listrunspaginator)
        """

if TYPE_CHECKING:
    _ListSequenceStoresPaginatorBase = Paginator[ListSequenceStoresResponseTypeDef]
else:
    _ListSequenceStoresPaginatorBase = Paginator  # type: ignore[assignment]

class ListSequenceStoresPaginator(_ListSequenceStoresPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListSequenceStores.html#Omics.Paginator.ListSequenceStores)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listsequencestorespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSequenceStoresRequestPaginateTypeDef]
    ) -> PageIterator[ListSequenceStoresResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListSequenceStores.html#Omics.Paginator.ListSequenceStores.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listsequencestorespaginator)
        """

if TYPE_CHECKING:
    _ListSharesPaginatorBase = Paginator[ListSharesResponseTypeDef]
else:
    _ListSharesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSharesPaginator(_ListSharesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListShares.html#Omics.Paginator.ListShares)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listsharespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSharesRequestPaginateTypeDef]
    ) -> PageIterator[ListSharesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListShares.html#Omics.Paginator.ListShares.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listsharespaginator)
        """

if TYPE_CHECKING:
    _ListVariantImportJobsPaginatorBase = Paginator[ListVariantImportJobsResponseTypeDef]
else:
    _ListVariantImportJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListVariantImportJobsPaginator(_ListVariantImportJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListVariantImportJobs.html#Omics.Paginator.ListVariantImportJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listvariantimportjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListVariantImportJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListVariantImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListVariantImportJobs.html#Omics.Paginator.ListVariantImportJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listvariantimportjobspaginator)
        """

if TYPE_CHECKING:
    _ListVariantStoresPaginatorBase = Paginator[ListVariantStoresResponseTypeDef]
else:
    _ListVariantStoresPaginatorBase = Paginator  # type: ignore[assignment]

class ListVariantStoresPaginator(_ListVariantStoresPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListVariantStores.html#Omics.Paginator.ListVariantStores)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listvariantstorespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListVariantStoresRequestPaginateTypeDef]
    ) -> PageIterator[ListVariantStoresResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListVariantStores.html#Omics.Paginator.ListVariantStores.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listvariantstorespaginator)
        """

if TYPE_CHECKING:
    _ListWorkflowVersionsPaginatorBase = Paginator[ListWorkflowVersionsResponseTypeDef]
else:
    _ListWorkflowVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkflowVersionsPaginator(_ListWorkflowVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListWorkflowVersions.html#Omics.Paginator.ListWorkflowVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listworkflowversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkflowVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkflowVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListWorkflowVersions.html#Omics.Paginator.ListWorkflowVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listworkflowversionspaginator)
        """

if TYPE_CHECKING:
    _ListWorkflowsPaginatorBase = Paginator[ListWorkflowsResponseTypeDef]
else:
    _ListWorkflowsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkflowsPaginator(_ListWorkflowsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListWorkflows.html#Omics.Paginator.ListWorkflows)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listworkflowspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkflowsRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkflowsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/paginator/ListWorkflows.html#Omics.Paginator.ListWorkflows.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators/#listworkflowspaginator)
        """
