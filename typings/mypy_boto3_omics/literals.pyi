"""
Type annotations for omics service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/literals.html)

Usage::

    ```python
    from mypy_boto3_omics.literals import AcceleratorsType

    data: AcceleratorsType = "GPU"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AcceleratorsType",
    "AnnotationImportJobCreatedWaiterName",
    "AnnotationStoreCreatedWaiterName",
    "AnnotationStoreDeletedWaiterName",
    "AnnotationStoreVersionCreatedWaiterName",
    "AnnotationStoreVersionDeletedWaiterName",
    "AnnotationTypeType",
    "CreationTypeType",
    "ETagAlgorithmFamilyType",
    "ETagAlgorithmType",
    "EncryptionTypeType",
    "FileTypeType",
    "FormatToHeaderKeyType",
    "JobStatusType",
    "ListAnnotationImportJobsPaginatorName",
    "ListAnnotationStoreVersionsPaginatorName",
    "ListAnnotationStoresPaginatorName",
    "ListMultipartReadSetUploadsPaginatorName",
    "ListReadSetActivationJobsPaginatorName",
    "ListReadSetExportJobsPaginatorName",
    "ListReadSetImportJobsPaginatorName",
    "ListReadSetUploadPartsPaginatorName",
    "ListReadSetsPaginatorName",
    "ListReferenceImportJobsPaginatorName",
    "ListReferenceStoresPaginatorName",
    "ListReferencesPaginatorName",
    "ListRunGroupsPaginatorName",
    "ListRunTasksPaginatorName",
    "ListRunsPaginatorName",
    "ListSequenceStoresPaginatorName",
    "ListSharesPaginatorName",
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
    "ReadSetPartSourceType",
    "ReadSetStatusType",
    "ReferenceFileType",
    "ReferenceImportJobCompletedWaiterName",
    "ReferenceImportJobItemStatusType",
    "ReferenceImportJobStatusType",
    "ReferenceStatusType",
    "ResourceOwnerType",
    "RunCompletedWaiterName",
    "RunExportType",
    "RunLogLevelType",
    "RunRetentionModeType",
    "RunRunningWaiterName",
    "RunStatusType",
    "SchemaValueTypeType",
    "ShareResourceTypeType",
    "ShareStatusType",
    "StorageTypeType",
    "StoreFormatType",
    "StoreStatusType",
    "TaskCompletedWaiterName",
    "TaskRunningWaiterName",
    "TaskStatusType",
    "VariantImportJobCreatedWaiterName",
    "VariantStoreCreatedWaiterName",
    "VariantStoreDeletedWaiterName",
    "VersionStatusType",
    "WorkflowActiveWaiterName",
    "WorkflowEngineType",
    "WorkflowExportType",
    "WorkflowStatusType",
    "WorkflowTypeType",
)

AcceleratorsType = Literal["GPU"]
AnnotationImportJobCreatedWaiterName = Literal["annotation_import_job_created"]
AnnotationStoreCreatedWaiterName = Literal["annotation_store_created"]
AnnotationStoreDeletedWaiterName = Literal["annotation_store_deleted"]
AnnotationStoreVersionCreatedWaiterName = Literal["annotation_store_version_created"]
AnnotationStoreVersionDeletedWaiterName = Literal["annotation_store_version_deleted"]
AnnotationTypeType = Literal[
    "CHR_POS",
    "CHR_POS_REF_ALT",
    "CHR_START_END_ONE_BASE",
    "CHR_START_END_REF_ALT_ONE_BASE",
    "CHR_START_END_REF_ALT_ZERO_BASE",
    "CHR_START_END_ZERO_BASE",
    "GENERIC",
]
CreationTypeType = Literal["IMPORT", "UPLOAD"]
ETagAlgorithmFamilyType = Literal["MD5up", "SHA256up", "SHA512up"]
ETagAlgorithmType = Literal[
    "BAM_MD5up",
    "BAM_SHA256up",
    "BAM_SHA512up",
    "CRAM_MD5up",
    "CRAM_SHA256up",
    "CRAM_SHA512up",
    "FASTQ_MD5up",
    "FASTQ_SHA256up",
    "FASTQ_SHA512up",
]
EncryptionTypeType = Literal["KMS"]
FileTypeType = Literal["BAM", "CRAM", "FASTQ", "UBAM"]
FormatToHeaderKeyType = Literal["ALT", "CHR", "END", "POS", "REF", "START"]
JobStatusType = Literal[
    "CANCELLED", "COMPLETED", "COMPLETED_WITH_FAILURES", "FAILED", "IN_PROGRESS", "SUBMITTED"
]
ListAnnotationImportJobsPaginatorName = Literal["list_annotation_import_jobs"]
ListAnnotationStoreVersionsPaginatorName = Literal["list_annotation_store_versions"]
ListAnnotationStoresPaginatorName = Literal["list_annotation_stores"]
ListMultipartReadSetUploadsPaginatorName = Literal["list_multipart_read_set_uploads"]
ListReadSetActivationJobsPaginatorName = Literal["list_read_set_activation_jobs"]
ListReadSetExportJobsPaginatorName = Literal["list_read_set_export_jobs"]
ListReadSetImportJobsPaginatorName = Literal["list_read_set_import_jobs"]
ListReadSetUploadPartsPaginatorName = Literal["list_read_set_upload_parts"]
ListReadSetsPaginatorName = Literal["list_read_sets"]
ListReferenceImportJobsPaginatorName = Literal["list_reference_import_jobs"]
ListReferenceStoresPaginatorName = Literal["list_reference_stores"]
ListReferencesPaginatorName = Literal["list_references"]
ListRunGroupsPaginatorName = Literal["list_run_groups"]
ListRunTasksPaginatorName = Literal["list_run_tasks"]
ListRunsPaginatorName = Literal["list_runs"]
ListSequenceStoresPaginatorName = Literal["list_sequence_stores"]
ListSharesPaginatorName = Literal["list_shares"]
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
ReadSetPartSourceType = Literal["SOURCE1", "SOURCE2"]
ReadSetStatusType = Literal[
    "ACTIVATING", "ACTIVE", "ARCHIVED", "DELETED", "DELETING", "PROCESSING_UPLOAD", "UPLOAD_FAILED"
]
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
ResourceOwnerType = Literal["OTHER", "SELF"]
RunCompletedWaiterName = Literal["run_completed"]
RunExportType = Literal["DEFINITION"]
RunLogLevelType = Literal["ALL", "ERROR", "FATAL", "OFF"]
RunRetentionModeType = Literal["REMOVE", "RETAIN"]
RunRunningWaiterName = Literal["run_running"]
RunStatusType = Literal[
    "CANCELLED", "COMPLETED", "DELETED", "FAILED", "PENDING", "RUNNING", "STARTING", "STOPPING"
]
SchemaValueTypeType = Literal["BOOLEAN", "DOUBLE", "FLOAT", "INT", "LONG", "STRING"]
ShareResourceTypeType = Literal["ANNOTATION_STORE", "VARIANT_STORE", "WORKFLOW"]
ShareStatusType = Literal["ACTIVATING", "ACTIVE", "DELETED", "DELETING", "FAILED", "PENDING"]
StorageTypeType = Literal["DYNAMIC", "STATIC"]
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
VersionStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
WorkflowActiveWaiterName = Literal["workflow_active"]
WorkflowEngineType = Literal["CWL", "NEXTFLOW", "WDL"]
WorkflowExportType = Literal["DEFINITION"]
WorkflowStatusType = Literal["ACTIVE", "CREATING", "DELETED", "FAILED", "INACTIVE", "UPDATING"]
WorkflowTypeType = Literal["PRIVATE", "READY2RUN"]
