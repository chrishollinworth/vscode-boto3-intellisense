"""
Type annotations for omics service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/literals.html)

Usage::

    ```python
    from mypy_boto3_omics.literals import AnnotationImportJobCreatedWaiterName

    data: AnnotationImportJobCreatedWaiterName = "annotation_import_job_created"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AnnotationImportJobCreatedWaiterName",
    "AnnotationStoreCreatedWaiterName",
    "AnnotationStoreDeletedWaiterName",
    "AnnotationTypeType",
    "EncryptionTypeType",
    "FileTypeType",
    "FormatToHeaderKeyType",
    "JobStatusType",
    "ListAnnotationImportJobsPaginatorName",
    "ListAnnotationStoresPaginatorName",
    "ListReadSetActivationJobsPaginatorName",
    "ListReadSetExportJobsPaginatorName",
    "ListReadSetImportJobsPaginatorName",
    "ListReadSetsPaginatorName",
    "ListReferenceImportJobsPaginatorName",
    "ListReferenceStoresPaginatorName",
    "ListReferencesPaginatorName",
    "ListRunGroupsPaginatorName",
    "ListRunTasksPaginatorName",
    "ListRunsPaginatorName",
    "ListSequenceStoresPaginatorName",
    "ListVariantImportJobsPaginatorName",
    "ListVariantStoresPaginatorName",
    "ListWorkflowsPaginatorName",
    "ReadSetActivationJobCompletedWaiterName",
    "ReadSetActivationJobItemStatusType",
    "ReadSetActivationJobStatusType",
    "ReadSetExportJobCompletedWaiterName",
    "ReadSetExportJobItemStatusType",
    "ReadSetExportJobStatusType",
    "ReadSetFileType",
    "ReadSetImportJobCompletedWaiterName",
    "ReadSetImportJobItemStatusType",
    "ReadSetImportJobStatusType",
    "ReadSetStatusType",
    "ReferenceFileType",
    "ReferenceImportJobCompletedWaiterName",
    "ReferenceImportJobItemStatusType",
    "ReferenceImportJobStatusType",
    "ReferenceStatusType",
    "RunCompletedWaiterName",
    "RunExportType",
    "RunLogLevelType",
    "RunRunningWaiterName",
    "RunStatusType",
    "SchemaValueTypeType",
    "StoreFormatType",
    "StoreStatusType",
    "TaskCompletedWaiterName",
    "TaskRunningWaiterName",
    "TaskStatusType",
    "VariantImportJobCreatedWaiterName",
    "VariantStoreCreatedWaiterName",
    "VariantStoreDeletedWaiterName",
    "WorkflowActiveWaiterName",
    "WorkflowEngineType",
    "WorkflowExportType",
    "WorkflowStatusType",
    "WorkflowTypeType",
)

AnnotationImportJobCreatedWaiterName = Literal["annotation_import_job_created"]
AnnotationStoreCreatedWaiterName = Literal["annotation_store_created"]
AnnotationStoreDeletedWaiterName = Literal["annotation_store_deleted"]
AnnotationTypeType = Literal[
    "CHR_POS",
    "CHR_POS_REF_ALT",
    "CHR_START_END_ONE_BASE",
    "CHR_START_END_REF_ALT_ONE_BASE",
    "CHR_START_END_REF_ALT_ZERO_BASE",
    "CHR_START_END_ZERO_BASE",
    "GENERIC",
]
EncryptionTypeType = Literal["KMS"]
FileTypeType = Literal["BAM", "CRAM", "FASTQ"]
FormatToHeaderKeyType = Literal["ALT", "CHR", "END", "POS", "REF", "START"]
JobStatusType = Literal["CANCELLED", "COMPLETED", "FAILED", "IN_PROGRESS", "SUBMITTED"]
ListAnnotationImportJobsPaginatorName = Literal["list_annotation_import_jobs"]
ListAnnotationStoresPaginatorName = Literal["list_annotation_stores"]
ListReadSetActivationJobsPaginatorName = Literal["list_read_set_activation_jobs"]
ListReadSetExportJobsPaginatorName = Literal["list_read_set_export_jobs"]
ListReadSetImportJobsPaginatorName = Literal["list_read_set_import_jobs"]
ListReadSetsPaginatorName = Literal["list_read_sets"]
ListReferenceImportJobsPaginatorName = Literal["list_reference_import_jobs"]
ListReferenceStoresPaginatorName = Literal["list_reference_stores"]
ListReferencesPaginatorName = Literal["list_references"]
ListRunGroupsPaginatorName = Literal["list_run_groups"]
ListRunTasksPaginatorName = Literal["list_run_tasks"]
ListRunsPaginatorName = Literal["list_runs"]
ListSequenceStoresPaginatorName = Literal["list_sequence_stores"]
ListVariantImportJobsPaginatorName = Literal["list_variant_import_jobs"]
ListVariantStoresPaginatorName = Literal["list_variant_stores"]
ListWorkflowsPaginatorName = Literal["list_workflows"]
ReadSetActivationJobCompletedWaiterName = Literal["read_set_activation_job_completed"]
ReadSetActivationJobItemStatusType = Literal["FAILED", "FINISHED", "IN_PROGRESS", "NOT_STARTED"]
ReadSetActivationJobStatusType = Literal[
    "CANCELLED",
    "CANCELLING",
    "COMPLETED",
    "COMPLETED_WITH_FAILURES",
    "FAILED",
    "IN_PROGRESS",
    "SUBMITTED",
]
ReadSetExportJobCompletedWaiterName = Literal["read_set_export_job_completed"]
ReadSetExportJobItemStatusType = Literal["FAILED", "FINISHED", "IN_PROGRESS", "NOT_STARTED"]
ReadSetExportJobStatusType = Literal[
    "CANCELLED",
    "CANCELLING",
    "COMPLETED",
    "COMPLETED_WITH_FAILURES",
    "FAILED",
    "IN_PROGRESS",
    "SUBMITTED",
]
ReadSetFileType = Literal["INDEX", "SOURCE1", "SOURCE2"]
ReadSetImportJobCompletedWaiterName = Literal["read_set_import_job_completed"]
ReadSetImportJobItemStatusType = Literal["FAILED", "FINISHED", "IN_PROGRESS", "NOT_STARTED"]
ReadSetImportJobStatusType = Literal[
    "CANCELLED",
    "CANCELLING",
    "COMPLETED",
    "COMPLETED_WITH_FAILURES",
    "FAILED",
    "IN_PROGRESS",
    "SUBMITTED",
]
ReadSetStatusType = Literal["ACTIVATING", "ACTIVE", "ARCHIVED", "DELETED", "DELETING"]
ReferenceFileType = Literal["INDEX", "SOURCE"]
ReferenceImportJobCompletedWaiterName = Literal["reference_import_job_completed"]
ReferenceImportJobItemStatusType = Literal["FAILED", "FINISHED", "IN_PROGRESS", "NOT_STARTED"]
ReferenceImportJobStatusType = Literal[
    "CANCELLED",
    "CANCELLING",
    "COMPLETED",
    "COMPLETED_WITH_FAILURES",
    "FAILED",
    "IN_PROGRESS",
    "SUBMITTED",
]
ReferenceStatusType = Literal["ACTIVE", "DELETED", "DELETING"]
RunCompletedWaiterName = Literal["run_completed"]
RunExportType = Literal["DEFINITION"]
RunLogLevelType = Literal["ALL", "ERROR", "FATAL", "OFF"]
RunRunningWaiterName = Literal["run_running"]
RunStatusType = Literal[
    "CANCELLED", "COMPLETED", "DELETED", "FAILED", "PENDING", "RUNNING", "STARTING", "STOPPING"
]
SchemaValueTypeType = Literal["BOOLEAN", "DOUBLE", "FLOAT", "INT", "LONG", "STRING"]
StoreFormatType = Literal["GFF", "TSV", "VCF"]
StoreStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
TaskCompletedWaiterName = Literal["task_completed"]
TaskRunningWaiterName = Literal["task_running"]
TaskStatusType = Literal[
    "CANCELLED", "COMPLETED", "FAILED", "PENDING", "RUNNING", "STARTING", "STOPPING"
]
VariantImportJobCreatedWaiterName = Literal["variant_import_job_created"]
VariantStoreCreatedWaiterName = Literal["variant_store_created"]
VariantStoreDeletedWaiterName = Literal["variant_store_deleted"]
WorkflowActiveWaiterName = Literal["workflow_active"]
WorkflowEngineType = Literal["NEXTFLOW", "WDL"]
WorkflowExportType = Literal["DEFINITION"]
WorkflowStatusType = Literal["ACTIVE", "CREATING", "DELETED", "FAILED", "UPDATING"]
WorkflowTypeType = Literal["PRIVATE"]
