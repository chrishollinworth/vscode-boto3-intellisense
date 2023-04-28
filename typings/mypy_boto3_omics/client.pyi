"""
Type annotations for omics service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_omics import OmicsClient

    client: OmicsClient = boto3.client("omics")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import (
    ReadSetFileType,
    ReferenceFileType,
    RunLogLevelType,
    StoreFormatType,
    TaskStatusType,
    WorkflowEngineType,
)
from .paginator import (
    ListAnnotationImportJobsPaginator,
    ListAnnotationStoresPaginator,
    ListReadSetActivationJobsPaginator,
    ListReadSetExportJobsPaginator,
    ListReadSetImportJobsPaginator,
    ListReadSetsPaginator,
    ListReferenceImportJobsPaginator,
    ListReferencesPaginator,
    ListReferenceStoresPaginator,
    ListRunGroupsPaginator,
    ListRunsPaginator,
    ListRunTasksPaginator,
    ListSequenceStoresPaginator,
    ListVariantImportJobsPaginator,
    ListVariantStoresPaginator,
    ListWorkflowsPaginator,
)
from .type_defs import (
    ActivateReadSetFilterTypeDef,
    AnnotationImportItemSourceTypeDef,
    BatchDeleteReadSetResponseTypeDef,
    CreateAnnotationStoreResponseTypeDef,
    CreateReferenceStoreResponseTypeDef,
    CreateRunGroupResponseTypeDef,
    CreateSequenceStoreResponseTypeDef,
    CreateVariantStoreResponseTypeDef,
    CreateWorkflowResponseTypeDef,
    DeleteAnnotationStoreResponseTypeDef,
    DeleteVariantStoreResponseTypeDef,
    ExportReadSetFilterTypeDef,
    ExportReadSetTypeDef,
    FormatOptionsTypeDef,
    GetAnnotationImportResponseTypeDef,
    GetAnnotationStoreResponseTypeDef,
    GetReadSetActivationJobResponseTypeDef,
    GetReadSetExportJobResponseTypeDef,
    GetReadSetImportJobResponseTypeDef,
    GetReadSetMetadataResponseTypeDef,
    GetReadSetResponseTypeDef,
    GetReferenceImportJobResponseTypeDef,
    GetReferenceMetadataResponseTypeDef,
    GetReferenceResponseTypeDef,
    GetReferenceStoreResponseTypeDef,
    GetRunGroupResponseTypeDef,
    GetRunResponseTypeDef,
    GetRunTaskResponseTypeDef,
    GetSequenceStoreResponseTypeDef,
    GetVariantImportResponseTypeDef,
    GetVariantStoreResponseTypeDef,
    GetWorkflowResponseTypeDef,
    ImportReadSetFilterTypeDef,
    ImportReferenceFilterTypeDef,
    ListAnnotationImportJobsFilterTypeDef,
    ListAnnotationImportJobsResponseTypeDef,
    ListAnnotationStoresFilterTypeDef,
    ListAnnotationStoresResponseTypeDef,
    ListReadSetActivationJobsResponseTypeDef,
    ListReadSetExportJobsResponseTypeDef,
    ListReadSetImportJobsResponseTypeDef,
    ListReadSetsResponseTypeDef,
    ListReferenceImportJobsResponseTypeDef,
    ListReferencesResponseTypeDef,
    ListReferenceStoresResponseTypeDef,
    ListRunGroupsResponseTypeDef,
    ListRunsResponseTypeDef,
    ListRunTasksResponseTypeDef,
    ListSequenceStoresResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVariantImportJobsFilterTypeDef,
    ListVariantImportJobsResponseTypeDef,
    ListVariantStoresFilterTypeDef,
    ListVariantStoresResponseTypeDef,
    ListWorkflowsResponseTypeDef,
    ReadSetFilterTypeDef,
    ReferenceFilterTypeDef,
    ReferenceItemTypeDef,
    ReferenceStoreFilterTypeDef,
    SequenceStoreFilterTypeDef,
    SseConfigTypeDef,
    StartAnnotationImportResponseTypeDef,
    StartReadSetActivationJobResponseTypeDef,
    StartReadSetActivationJobSourceItemTypeDef,
    StartReadSetExportJobResponseTypeDef,
    StartReadSetImportJobResponseTypeDef,
    StartReadSetImportJobSourceItemTypeDef,
    StartReferenceImportJobResponseTypeDef,
    StartReferenceImportJobSourceItemTypeDef,
    StartRunResponseTypeDef,
    StartVariantImportResponseTypeDef,
    StoreOptionsTypeDef,
    UpdateAnnotationStoreResponseTypeDef,
    UpdateVariantStoreResponseTypeDef,
    VariantImportItemSourceTypeDef,
    WorkflowParameterTypeDef,
)
from .waiter import (
    AnnotationImportJobCreatedWaiter,
    AnnotationStoreCreatedWaiter,
    AnnotationStoreDeletedWaiter,
    ReadSetActivationJobCompletedWaiter,
    ReadSetExportJobCompletedWaiter,
    ReadSetImportJobCompletedWaiter,
    ReferenceImportJobCompletedWaiter,
    RunCompletedWaiter,
    RunRunningWaiter,
    TaskCompletedWaiter,
    TaskRunningWaiter,
    VariantImportJobCreatedWaiter,
    VariantStoreCreatedWaiter,
    VariantStoreDeletedWaiter,
    WorkflowActiveWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("OmicsClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    RangeNotSatisfiableException: Type[BotocoreClientError]
    RequestTimeoutException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class OmicsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        OmicsClient exceptions.
        """
    def batch_delete_read_set(
        self, *, ids: List[str], sequenceStoreId: str
    ) -> BatchDeleteReadSetResponseTypeDef:
        """
        Deletes one or more read sets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.batch_delete_read_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#batch_delete_read_set)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#can_paginate)
        """
    def cancel_annotation_import_job(self, *, jobId: str) -> Dict[str, Any]:
        """
        Cancels an annotation import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.cancel_annotation_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#cancel_annotation_import_job)
        """
    def cancel_run(self, *, id: str) -> None:
        """
        Cancels a run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.cancel_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#cancel_run)
        """
    def cancel_variant_import_job(self, *, jobId: str) -> Dict[str, Any]:
        """
        Cancels a variant import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.cancel_variant_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#cancel_variant_import_job)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#close)
        """
    def create_annotation_store(
        self,
        *,
        storeFormat: StoreFormatType,
        description: str = None,
        name: str = None,
        reference: "ReferenceItemTypeDef" = None,
        sseConfig: "SseConfigTypeDef" = None,
        storeOptions: "StoreOptionsTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateAnnotationStoreResponseTypeDef:
        """
        Creates an annotation store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.create_annotation_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#create_annotation_store)
        """
    def create_reference_store(
        self,
        *,
        name: str,
        clientToken: str = None,
        description: str = None,
        sseConfig: "SseConfigTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateReferenceStoreResponseTypeDef:
        """
        Creates a reference store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.create_reference_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#create_reference_store)
        """
    def create_run_group(
        self,
        *,
        requestId: str,
        maxCpus: int = None,
        maxDuration: int = None,
        maxRuns: int = None,
        name: str = None,
        tags: Dict[str, str] = None
    ) -> CreateRunGroupResponseTypeDef:
        """
        Creates a run group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.create_run_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#create_run_group)
        """
    def create_sequence_store(
        self,
        *,
        name: str,
        clientToken: str = None,
        description: str = None,
        sseConfig: "SseConfigTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateSequenceStoreResponseTypeDef:
        """
        Creates a sequence store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.create_sequence_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#create_sequence_store)
        """
    def create_variant_store(
        self,
        *,
        reference: "ReferenceItemTypeDef",
        description: str = None,
        name: str = None,
        sseConfig: "SseConfigTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateVariantStoreResponseTypeDef:
        """
        Creates a variant store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.create_variant_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#create_variant_store)
        """
    def create_workflow(
        self,
        *,
        requestId: str,
        definitionUri: str = None,
        definitionZip: Union[bytes, IO[bytes], StreamingBody] = None,
        description: str = None,
        engine: WorkflowEngineType = None,
        main: str = None,
        name: str = None,
        parameterTemplate: Dict[str, "WorkflowParameterTypeDef"] = None,
        storageCapacity: int = None,
        tags: Dict[str, str] = None
    ) -> CreateWorkflowResponseTypeDef:
        """
        Creates a workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.create_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#create_workflow)
        """
    def delete_annotation_store(
        self, *, name: str, force: bool = None
    ) -> DeleteAnnotationStoreResponseTypeDef:
        """
        Deletes an annotation store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.delete_annotation_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#delete_annotation_store)
        """
    def delete_reference(self, *, id: str, referenceStoreId: str) -> Dict[str, Any]:
        """
        Deletes a genome reference.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.delete_reference)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#delete_reference)
        """
    def delete_reference_store(self, *, id: str) -> Dict[str, Any]:
        """
        Deletes a genome reference store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.delete_reference_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#delete_reference_store)
        """
    def delete_run(self, *, id: str) -> None:
        """
        Deletes a workflow run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.delete_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#delete_run)
        """
    def delete_run_group(self, *, id: str) -> None:
        """
        Deletes a workflow run group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.delete_run_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#delete_run_group)
        """
    def delete_sequence_store(self, *, id: str) -> Dict[str, Any]:
        """
        Deletes a sequence store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.delete_sequence_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#delete_sequence_store)
        """
    def delete_variant_store(
        self, *, name: str, force: bool = None
    ) -> DeleteVariantStoreResponseTypeDef:
        """
        Deletes a variant store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.delete_variant_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#delete_variant_store)
        """
    def delete_workflow(self, *, id: str) -> None:
        """
        Deletes a workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.delete_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#delete_workflow)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#generate_presigned_url)
        """
    def get_annotation_import_job(self, *, jobId: str) -> GetAnnotationImportResponseTypeDef:
        """
        Gets information about an annotation import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.get_annotation_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#get_annotation_import_job)
        """
    def get_annotation_store(self, *, name: str) -> GetAnnotationStoreResponseTypeDef:
        """
        Gets information about an annotation store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.get_annotation_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#get_annotation_store)
        """
    def get_read_set(
        self, *, id: str, partNumber: int, sequenceStoreId: str, file: ReadSetFileType = None
    ) -> GetReadSetResponseTypeDef:
        """
        Gets a file from a read set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.get_read_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#get_read_set)
        """
    def get_read_set_activation_job(
        self, *, id: str, sequenceStoreId: str
    ) -> GetReadSetActivationJobResponseTypeDef:
        """
        Gets information about a read set activation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.get_read_set_activation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#get_read_set_activation_job)
        """
    def get_read_set_export_job(
        self, *, id: str, sequenceStoreId: str
    ) -> GetReadSetExportJobResponseTypeDef:
        """
        Gets information about a read set export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.get_read_set_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#get_read_set_export_job)
        """
    def get_read_set_import_job(
        self, *, id: str, sequenceStoreId: str
    ) -> GetReadSetImportJobResponseTypeDef:
        """
        Gets information about a read set import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.get_read_set_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#get_read_set_import_job)
        """
    def get_read_set_metadata(
        self, *, id: str, sequenceStoreId: str
    ) -> GetReadSetMetadataResponseTypeDef:
        """
        Gets details about a read set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.get_read_set_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#get_read_set_metadata)
        """
    def get_reference(
        self,
        *,
        id: str,
        partNumber: int,
        referenceStoreId: str,
        file: ReferenceFileType = None,
        range: str = None
    ) -> GetReferenceResponseTypeDef:
        """
        Gets a reference file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.get_reference)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#get_reference)
        """
    def get_reference_import_job(
        self, *, id: str, referenceStoreId: str
    ) -> GetReferenceImportJobResponseTypeDef:
        """
        Gets information about a reference import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.get_reference_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#get_reference_import_job)
        """
    def get_reference_metadata(
        self, *, id: str, referenceStoreId: str
    ) -> GetReferenceMetadataResponseTypeDef:
        """
        Gets information about a genome reference's metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.get_reference_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#get_reference_metadata)
        """
    def get_reference_store(self, *, id: str) -> GetReferenceStoreResponseTypeDef:
        """
        Gets information about a reference store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.get_reference_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#get_reference_store)
        """
    def get_run(
        self, *, id: str, export: List[Literal["DEFINITION"]] = None
    ) -> GetRunResponseTypeDef:
        """
        Gets information about a workflow run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.get_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#get_run)
        """
    def get_run_group(self, *, id: str) -> GetRunGroupResponseTypeDef:
        """
        Gets information about a workflow run group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.get_run_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#get_run_group)
        """
    def get_run_task(self, *, id: str, taskId: str) -> GetRunTaskResponseTypeDef:
        """
        Gets information about a workflow run task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.get_run_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#get_run_task)
        """
    def get_sequence_store(self, *, id: str) -> GetSequenceStoreResponseTypeDef:
        """
        Gets information about a sequence store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.get_sequence_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#get_sequence_store)
        """
    def get_variant_import_job(self, *, jobId: str) -> GetVariantImportResponseTypeDef:
        """
        Gets information about a variant import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.get_variant_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#get_variant_import_job)
        """
    def get_variant_store(self, *, name: str) -> GetVariantStoreResponseTypeDef:
        """
        Gets information about a variant store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.get_variant_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#get_variant_store)
        """
    def get_workflow(
        self,
        *,
        id: str,
        export: List[Literal["DEFINITION"]] = None,
        type: Literal["PRIVATE"] = None
    ) -> GetWorkflowResponseTypeDef:
        """
        Gets information about a workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.get_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#get_workflow)
        """
    def list_annotation_import_jobs(
        self,
        *,
        filter: "ListAnnotationImportJobsFilterTypeDef" = None,
        ids: List[str] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListAnnotationImportJobsResponseTypeDef:
        """
        Retrieves a list of annotation import jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.list_annotation_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#list_annotation_import_jobs)
        """
    def list_annotation_stores(
        self,
        *,
        filter: "ListAnnotationStoresFilterTypeDef" = None,
        ids: List[str] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListAnnotationStoresResponseTypeDef:
        """
        Retrieves a list of annotation stores.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.list_annotation_stores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#list_annotation_stores)
        """
    def list_read_set_activation_jobs(
        self,
        *,
        sequenceStoreId: str,
        filter: "ActivateReadSetFilterTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListReadSetActivationJobsResponseTypeDef:
        """
        Retrieves a list of read set activation jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.list_read_set_activation_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#list_read_set_activation_jobs)
        """
    def list_read_set_export_jobs(
        self,
        *,
        sequenceStoreId: str,
        filter: "ExportReadSetFilterTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListReadSetExportJobsResponseTypeDef:
        """
        Retrieves a list of read set export jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.list_read_set_export_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#list_read_set_export_jobs)
        """
    def list_read_set_import_jobs(
        self,
        *,
        sequenceStoreId: str,
        filter: "ImportReadSetFilterTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListReadSetImportJobsResponseTypeDef:
        """
        Retrieves a list of read set import jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.list_read_set_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#list_read_set_import_jobs)
        """
    def list_read_sets(
        self,
        *,
        sequenceStoreId: str,
        filter: "ReadSetFilterTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListReadSetsResponseTypeDef:
        """
        Retrieves a list of read sets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.list_read_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#list_read_sets)
        """
    def list_reference_import_jobs(
        self,
        *,
        referenceStoreId: str,
        filter: "ImportReferenceFilterTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListReferenceImportJobsResponseTypeDef:
        """
        Retrieves a list of reference import jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.list_reference_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#list_reference_import_jobs)
        """
    def list_reference_stores(
        self,
        *,
        filter: "ReferenceStoreFilterTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListReferenceStoresResponseTypeDef:
        """
        Retrieves a list of reference stores.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.list_reference_stores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#list_reference_stores)
        """
    def list_references(
        self,
        *,
        referenceStoreId: str,
        filter: "ReferenceFilterTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListReferencesResponseTypeDef:
        """
        Retrieves a list of references.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.list_references)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#list_references)
        """
    def list_run_groups(
        self, *, maxResults: int = None, name: str = None, startingToken: str = None
    ) -> ListRunGroupsResponseTypeDef:
        """
        Retrieves a list of run groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.list_run_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#list_run_groups)
        """
    def list_run_tasks(
        self,
        *,
        id: str,
        maxResults: int = None,
        startingToken: str = None,
        status: TaskStatusType = None
    ) -> ListRunTasksResponseTypeDef:
        """
        Retrieves a list of tasks for a run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.list_run_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#list_run_tasks)
        """
    def list_runs(
        self,
        *,
        maxResults: int = None,
        name: str = None,
        runGroupId: str = None,
        startingToken: str = None
    ) -> ListRunsResponseTypeDef:
        """
        Retrieves a list of runs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.list_runs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#list_runs)
        """
    def list_sequence_stores(
        self,
        *,
        filter: "SequenceStoreFilterTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListSequenceStoresResponseTypeDef:
        """
        Retrieves a list of sequence stores.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.list_sequence_stores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#list_sequence_stores)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves a list of tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#list_tags_for_resource)
        """
    def list_variant_import_jobs(
        self,
        *,
        filter: "ListVariantImportJobsFilterTypeDef" = None,
        ids: List[str] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListVariantImportJobsResponseTypeDef:
        """
        Retrieves a list of variant import jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.list_variant_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#list_variant_import_jobs)
        """
    def list_variant_stores(
        self,
        *,
        filter: "ListVariantStoresFilterTypeDef" = None,
        ids: List[str] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListVariantStoresResponseTypeDef:
        """
        Retrieves a list of variant stores.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.list_variant_stores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#list_variant_stores)
        """
    def list_workflows(
        self,
        *,
        maxResults: int = None,
        name: str = None,
        startingToken: str = None,
        type: Literal["PRIVATE"] = None
    ) -> ListWorkflowsResponseTypeDef:
        """
        Retrieves a list of workflows.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.list_workflows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#list_workflows)
        """
    def start_annotation_import_job(
        self,
        *,
        destinationName: str,
        items: List["AnnotationImportItemSourceTypeDef"],
        roleArn: str,
        formatOptions: "FormatOptionsTypeDef" = None,
        runLeftNormalization: bool = None
    ) -> StartAnnotationImportResponseTypeDef:
        """
        Starts an annotation import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.start_annotation_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#start_annotation_import_job)
        """
    def start_read_set_activation_job(
        self,
        *,
        sequenceStoreId: str,
        sources: List["StartReadSetActivationJobSourceItemTypeDef"],
        clientToken: str = None
    ) -> StartReadSetActivationJobResponseTypeDef:
        """
        Activates an archived read set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.start_read_set_activation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#start_read_set_activation_job)
        """
    def start_read_set_export_job(
        self,
        *,
        destination: str,
        roleArn: str,
        sequenceStoreId: str,
        sources: List["ExportReadSetTypeDef"],
        clientToken: str = None
    ) -> StartReadSetExportJobResponseTypeDef:
        """
        Exports a read set to Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.start_read_set_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#start_read_set_export_job)
        """
    def start_read_set_import_job(
        self,
        *,
        roleArn: str,
        sequenceStoreId: str,
        sources: List["StartReadSetImportJobSourceItemTypeDef"],
        clientToken: str = None
    ) -> StartReadSetImportJobResponseTypeDef:
        """
        Starts a read set import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.start_read_set_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#start_read_set_import_job)
        """
    def start_reference_import_job(
        self,
        *,
        referenceStoreId: str,
        roleArn: str,
        sources: List["StartReferenceImportJobSourceItemTypeDef"],
        clientToken: str = None
    ) -> StartReferenceImportJobResponseTypeDef:
        """
        Starts a reference import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.start_reference_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#start_reference_import_job)
        """
    def start_run(
        self,
        *,
        requestId: str,
        roleArn: str,
        logLevel: RunLogLevelType = None,
        name: str = None,
        outputUri: str = None,
        parameters: Dict[str, Any] = None,
        priority: int = None,
        runGroupId: str = None,
        runId: str = None,
        storageCapacity: int = None,
        tags: Dict[str, str] = None,
        workflowId: str = None,
        workflowType: Literal["PRIVATE"] = None
    ) -> StartRunResponseTypeDef:
        """
        Starts a run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.start_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#start_run)
        """
    def start_variant_import_job(
        self,
        *,
        destinationName: str,
        items: List["VariantImportItemSourceTypeDef"],
        roleArn: str,
        runLeftNormalization: bool = None
    ) -> StartVariantImportResponseTypeDef:
        """
        Starts a variant import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.start_variant_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#start_variant_import_job)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Tags a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#untag_resource)
        """
    def update_annotation_store(
        self, *, name: str, description: str = None
    ) -> UpdateAnnotationStoreResponseTypeDef:
        """
        Updates an annotation store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.update_annotation_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#update_annotation_store)
        """
    def update_run_group(
        self,
        *,
        id: str,
        maxCpus: int = None,
        maxDuration: int = None,
        maxRuns: int = None,
        name: str = None
    ) -> None:
        """
        Updates a run group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.update_run_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#update_run_group)
        """
    def update_variant_store(
        self, *, name: str, description: str = None
    ) -> UpdateVariantStoreResponseTypeDef:
        """
        Updates a variant store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.update_variant_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#update_variant_store)
        """
    def update_workflow(self, *, id: str, description: str = None, name: str = None) -> None:
        """
        Updates a workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Client.update_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/client.html#update_workflow)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_annotation_import_jobs"]
    ) -> ListAnnotationImportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Paginator.ListAnnotationImportJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listannotationimportjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_annotation_stores"]
    ) -> ListAnnotationStoresPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Paginator.ListAnnotationStores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listannotationstorespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_read_set_activation_jobs"]
    ) -> ListReadSetActivationJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Paginator.ListReadSetActivationJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreadsetactivationjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_read_set_export_jobs"]
    ) -> ListReadSetExportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Paginator.ListReadSetExportJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreadsetexportjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_read_set_import_jobs"]
    ) -> ListReadSetImportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Paginator.ListReadSetImportJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreadsetimportjobspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_read_sets"]) -> ListReadSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Paginator.ListReadSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreadsetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_reference_import_jobs"]
    ) -> ListReferenceImportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Paginator.ListReferenceImportJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreferenceimportjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_reference_stores"]
    ) -> ListReferenceStoresPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Paginator.ListReferenceStores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreferencestorespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_references"]) -> ListReferencesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Paginator.ListReferences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listreferencespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_run_groups"]) -> ListRunGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Paginator.ListRunGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listrungroupspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_run_tasks"]) -> ListRunTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Paginator.ListRunTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listruntaskspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_runs"]) -> ListRunsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Paginator.ListRuns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listrunspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_sequence_stores"]
    ) -> ListSequenceStoresPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Paginator.ListSequenceStores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listsequencestorespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_variant_import_jobs"]
    ) -> ListVariantImportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Paginator.ListVariantImportJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listvariantimportjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_variant_stores"]
    ) -> ListVariantStoresPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Paginator.ListVariantStores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listvariantstorespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_workflows"]) -> ListWorkflowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Paginator.ListWorkflows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/paginators.html#listworkflowspaginator)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["annotation_import_job_created"]
    ) -> AnnotationImportJobCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Waiter.AnnotationImportJobCreated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#annotationimportjobcreatedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["annotation_store_created"]
    ) -> AnnotationStoreCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Waiter.AnnotationStoreCreated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#annotationstorecreatedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["annotation_store_deleted"]
    ) -> AnnotationStoreDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Waiter.AnnotationStoreDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#annotationstoredeletedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["read_set_activation_job_completed"]
    ) -> ReadSetActivationJobCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Waiter.ReadSetActivationJobCompleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#readsetactivationjobcompletedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["read_set_export_job_completed"]
    ) -> ReadSetExportJobCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Waiter.ReadSetExportJobCompleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#readsetexportjobcompletedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["read_set_import_job_completed"]
    ) -> ReadSetImportJobCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Waiter.ReadSetImportJobCompleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#readsetimportjobcompletedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["reference_import_job_completed"]
    ) -> ReferenceImportJobCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Waiter.ReferenceImportJobCompleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#referenceimportjobcompletedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["run_completed"]) -> RunCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Waiter.RunCompleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#runcompletedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["run_running"]) -> RunRunningWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Waiter.RunRunning)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#runrunningwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["task_completed"]) -> TaskCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Waiter.TaskCompleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#taskcompletedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["task_running"]) -> TaskRunningWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Waiter.TaskRunning)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#taskrunningwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["variant_import_job_created"]
    ) -> VariantImportJobCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Waiter.VariantImportJobCreated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#variantimportjobcreatedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["variant_store_created"]
    ) -> VariantStoreCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Waiter.VariantStoreCreated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#variantstorecreatedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["variant_store_deleted"]
    ) -> VariantStoreDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Waiter.VariantStoreDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#variantstoredeletedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["workflow_active"]) -> WorkflowActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/omics.html#Omics.Waiter.WorkflowActive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#workflowactivewaiter)
        """
