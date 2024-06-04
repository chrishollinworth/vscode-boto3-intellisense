"""
Type annotations for omics service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_omics import OmicsClient
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
        ListRunGroupsPaginator,
        ListRunTasksPaginator,
        ListRunsPaginator,
        ListSequenceStoresPaginator,
        ListSharesPaginator,
        ListVariantImportJobsPaginator,
        ListVariantStoresPaginator,
        ListWorkflowsPaginator,
    )

    client: OmicsClient = boto3.client("omics")

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
    list_run_groups_paginator: ListRunGroupsPaginator = client.get_paginator("list_run_groups")
    list_run_tasks_paginator: ListRunTasksPaginator = client.get_paginator("list_run_tasks")
    list_runs_paginator: ListRunsPaginator = client.get_paginator("list_runs")
    list_sequence_stores_paginator: ListSequenceStoresPaginator = client.get_paginator("list_sequence_stores")
    list_shares_paginator: ListSharesPaginator = client.get_paginator("list_shares")
    list_variant_import_jobs_paginator: ListVariantImportJobsPaginator = client.get_paginator("list_variant_import_jobs")
    list_variant_stores_paginator: ListVariantStoresPaginator = client.get_paginator("list_variant_stores")
    list_workflows_paginator: ListWorkflowsPaginator = client.get_paginator("list_workflows")
    ```
"""

from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    ReadSetPartSourceType,
    ResourceOwnerType,
    RunStatusType,
    TaskStatusType,
    WorkflowTypeType,
)
from .type_defs import (
    ActivateReadSetFilterTypeDef,
    ExportReadSetFilterTypeDef,
    FilterTypeDef,
    ImportReadSetFilterTypeDef,
    ImportReferenceFilterTypeDef,
    ListAnnotationImportJobsFilterTypeDef,
    ListAnnotationImportJobsResponseTypeDef,
    ListAnnotationStoresFilterTypeDef,
    ListAnnotationStoresResponseTypeDef,
    ListAnnotationStoreVersionsFilterTypeDef,
    ListAnnotationStoreVersionsResponseTypeDef,
    ListMultipartReadSetUploadsResponseTypeDef,
    ListReadSetActivationJobsResponseTypeDef,
    ListReadSetExportJobsResponseTypeDef,
    ListReadSetImportJobsResponseTypeDef,
    ListReadSetsResponseTypeDef,
    ListReadSetUploadPartsResponseTypeDef,
    ListReferenceImportJobsResponseTypeDef,
    ListReferencesResponseTypeDef,
    ListReferenceStoresResponseTypeDef,
    ListRunGroupsResponseTypeDef,
    ListRunsResponseTypeDef,
    ListRunTasksResponseTypeDef,
    ListSequenceStoresResponseTypeDef,
    ListSharesResponseTypeDef,
    ListVariantImportJobsFilterTypeDef,
    ListVariantImportJobsResponseTypeDef,
    ListVariantStoresFilterTypeDef,
    ListVariantStoresResponseTypeDef,
    ListWorkflowsResponseTypeDef,
    PaginatorConfigTypeDef,
    ReadSetFilterTypeDef,
    ReadSetUploadPartListFilterTypeDef,
    ReferenceFilterTypeDef,
    ReferenceStoreFilterTypeDef,
    SequenceStoreFilterTypeDef,
)

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
    "ListRunGroupsPaginator",
    "ListRunTasksPaginator",
    "ListRunsPaginator",
    "ListSequenceStoresPaginator",
    "ListSharesPaginator",
    "ListVariantImportJobsPaginator",
    "ListVariantStoresPaginator",
    "ListWorkflowsPaginator",
)

class ListAnnotationImportJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListAnnotationImportJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listannotationimportjobspaginator)
    """

    def paginate(
        self,
        *,
        ids: List[str] = None,
        filter: "ListAnnotationImportJobsFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAnnotationImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListAnnotationImportJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listannotationimportjobspaginator)
        """

class ListAnnotationStoreVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListAnnotationStoreVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listannotationstoreversionspaginator)
    """

    def paginate(
        self,
        *,
        name: str,
        filter: "ListAnnotationStoreVersionsFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAnnotationStoreVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListAnnotationStoreVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listannotationstoreversionspaginator)
        """

class ListAnnotationStoresPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListAnnotationStores)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listannotationstorespaginator)
    """

    def paginate(
        self,
        *,
        ids: List[str] = None,
        filter: "ListAnnotationStoresFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAnnotationStoresResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListAnnotationStores.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listannotationstorespaginator)
        """

class ListMultipartReadSetUploadsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListMultipartReadSetUploads)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listmultipartreadsetuploadspaginator)
    """

    def paginate(
        self, *, sequenceStoreId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMultipartReadSetUploadsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListMultipartReadSetUploads.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listmultipartreadsetuploadspaginator)
        """

class ListReadSetActivationJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListReadSetActivationJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreadsetactivationjobspaginator)
    """

    def paginate(
        self,
        *,
        sequenceStoreId: str,
        filter: "ActivateReadSetFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListReadSetActivationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListReadSetActivationJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreadsetactivationjobspaginator)
        """

class ListReadSetExportJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListReadSetExportJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreadsetexportjobspaginator)
    """

    def paginate(
        self,
        *,
        sequenceStoreId: str,
        filter: "ExportReadSetFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListReadSetExportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListReadSetExportJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreadsetexportjobspaginator)
        """

class ListReadSetImportJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListReadSetImportJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreadsetimportjobspaginator)
    """

    def paginate(
        self,
        *,
        sequenceStoreId: str,
        filter: "ImportReadSetFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListReadSetImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListReadSetImportJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreadsetimportjobspaginator)
        """

class ListReadSetUploadPartsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListReadSetUploadParts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreadsetuploadpartspaginator)
    """

    def paginate(
        self,
        *,
        sequenceStoreId: str,
        uploadId: str,
        partSource: ReadSetPartSourceType,
        filter: "ReadSetUploadPartListFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListReadSetUploadPartsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListReadSetUploadParts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreadsetuploadpartspaginator)
        """

class ListReadSetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListReadSets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreadsetspaginator)
    """

    def paginate(
        self,
        *,
        sequenceStoreId: str,
        filter: "ReadSetFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListReadSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListReadSets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreadsetspaginator)
        """

class ListReferenceImportJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListReferenceImportJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreferenceimportjobspaginator)
    """

    def paginate(
        self,
        *,
        referenceStoreId: str,
        filter: "ImportReferenceFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListReferenceImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListReferenceImportJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreferenceimportjobspaginator)
        """

class ListReferenceStoresPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListReferenceStores)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreferencestorespaginator)
    """

    def paginate(
        self,
        *,
        filter: "ReferenceStoreFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListReferenceStoresResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListReferenceStores.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreferencestorespaginator)
        """

class ListReferencesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListReferences)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreferencespaginator)
    """

    def paginate(
        self,
        *,
        referenceStoreId: str,
        filter: "ReferenceFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListReferencesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListReferences.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreferencespaginator)
        """

class ListRunGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListRunGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listrungroupspaginator)
    """

    def paginate(
        self, *, name: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRunGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListRunGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listrungroupspaginator)
        """

class ListRunTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListRunTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listruntaskspaginator)
    """

    def paginate(
        self,
        *,
        id: str,
        status: TaskStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRunTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListRunTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listruntaskspaginator)
        """

class ListRunsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListRuns)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listrunspaginator)
    """

    def paginate(
        self,
        *,
        name: str = None,
        runGroupId: str = None,
        status: RunStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListRuns.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listrunspaginator)
        """

class ListSequenceStoresPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListSequenceStores)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listsequencestorespaginator)
    """

    def paginate(
        self,
        *,
        filter: "SequenceStoreFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSequenceStoresResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListSequenceStores.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listsequencestorespaginator)
        """

class ListSharesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListShares)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listsharespaginator)
    """

    def paginate(
        self,
        *,
        resourceOwner: ResourceOwnerType,
        filter: "FilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSharesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListShares.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listsharespaginator)
        """

class ListVariantImportJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListVariantImportJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listvariantimportjobspaginator)
    """

    def paginate(
        self,
        *,
        ids: List[str] = None,
        filter: "ListVariantImportJobsFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVariantImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListVariantImportJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listvariantimportjobspaginator)
        """

class ListVariantStoresPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListVariantStores)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listvariantstorespaginator)
    """

    def paginate(
        self,
        *,
        ids: List[str] = None,
        filter: "ListVariantStoresFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVariantStoresResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListVariantStores.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listvariantstorespaginator)
        """

class ListWorkflowsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListWorkflows)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listworkflowspaginator)
    """

    def paginate(
        self,
        *,
        type: WorkflowTypeType = None,
        name: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkflowsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/omics.html#Omics.Paginator.ListWorkflows.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listworkflowspaginator)
        """
