"""
Main interface for omics service.

Usage::

    ```python
    import boto3
    from mypy_boto3_omics import (
        AnnotationImportJobCreatedWaiter,
        AnnotationStoreCreatedWaiter,
        AnnotationStoreDeletedWaiter,
        Client,
        ListAnnotationImportJobsPaginator,
        ListAnnotationStoresPaginator,
        ListReadSetActivationJobsPaginator,
        ListReadSetExportJobsPaginator,
        ListReadSetImportJobsPaginator,
        ListReadSetsPaginator,
        ListReferenceImportJobsPaginator,
        ListReferenceStoresPaginator,
        ListReferencesPaginator,
        ListRunGroupsPaginator,
        ListRunTasksPaginator,
        ListRunsPaginator,
        ListSequenceStoresPaginator,
        ListVariantImportJobsPaginator,
        ListVariantStoresPaginator,
        ListWorkflowsPaginator,
        OmicsClient,
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

    session = boto3.Session()

    client: OmicsClient = boto3.client("omics")
    session_client: OmicsClient = session.client("omics")

    annotation_import_job_created_waiter: AnnotationImportJobCreatedWaiter = client.get_waiter("annotation_import_job_created")
    annotation_store_created_waiter: AnnotationStoreCreatedWaiter = client.get_waiter("annotation_store_created")
    annotation_store_deleted_waiter: AnnotationStoreDeletedWaiter = client.get_waiter("annotation_store_deleted")
    read_set_activation_job_completed_waiter: ReadSetActivationJobCompletedWaiter = client.get_waiter("read_set_activation_job_completed")
    read_set_export_job_completed_waiter: ReadSetExportJobCompletedWaiter = client.get_waiter("read_set_export_job_completed")
    read_set_import_job_completed_waiter: ReadSetImportJobCompletedWaiter = client.get_waiter("read_set_import_job_completed")
    reference_import_job_completed_waiter: ReferenceImportJobCompletedWaiter = client.get_waiter("reference_import_job_completed")
    run_completed_waiter: RunCompletedWaiter = client.get_waiter("run_completed")
    run_running_waiter: RunRunningWaiter = client.get_waiter("run_running")
    task_completed_waiter: TaskCompletedWaiter = client.get_waiter("task_completed")
    task_running_waiter: TaskRunningWaiter = client.get_waiter("task_running")
    variant_import_job_created_waiter: VariantImportJobCreatedWaiter = client.get_waiter("variant_import_job_created")
    variant_store_created_waiter: VariantStoreCreatedWaiter = client.get_waiter("variant_store_created")
    variant_store_deleted_waiter: VariantStoreDeletedWaiter = client.get_waiter("variant_store_deleted")
    workflow_active_waiter: WorkflowActiveWaiter = client.get_waiter("workflow_active")

    list_annotation_import_jobs_paginator: ListAnnotationImportJobsPaginator = client.get_paginator("list_annotation_import_jobs")
    list_annotation_stores_paginator: ListAnnotationStoresPaginator = client.get_paginator("list_annotation_stores")
    list_read_set_activation_jobs_paginator: ListReadSetActivationJobsPaginator = client.get_paginator("list_read_set_activation_jobs")
    list_read_set_export_jobs_paginator: ListReadSetExportJobsPaginator = client.get_paginator("list_read_set_export_jobs")
    list_read_set_import_jobs_paginator: ListReadSetImportJobsPaginator = client.get_paginator("list_read_set_import_jobs")
    list_read_sets_paginator: ListReadSetsPaginator = client.get_paginator("list_read_sets")
    list_reference_import_jobs_paginator: ListReferenceImportJobsPaginator = client.get_paginator("list_reference_import_jobs")
    list_reference_stores_paginator: ListReferenceStoresPaginator = client.get_paginator("list_reference_stores")
    list_references_paginator: ListReferencesPaginator = client.get_paginator("list_references")
    list_run_groups_paginator: ListRunGroupsPaginator = client.get_paginator("list_run_groups")
    list_run_tasks_paginator: ListRunTasksPaginator = client.get_paginator("list_run_tasks")
    list_runs_paginator: ListRunsPaginator = client.get_paginator("list_runs")
    list_sequence_stores_paginator: ListSequenceStoresPaginator = client.get_paginator("list_sequence_stores")
    list_variant_import_jobs_paginator: ListVariantImportJobsPaginator = client.get_paginator("list_variant_import_jobs")
    list_variant_stores_paginator: ListVariantStoresPaginator = client.get_paginator("list_variant_stores")
    list_workflows_paginator: ListWorkflowsPaginator = client.get_paginator("list_workflows")
    ```
"""
from .client import OmicsClient
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

Client = OmicsClient

__all__ = (
    "AnnotationImportJobCreatedWaiter",
    "AnnotationStoreCreatedWaiter",
    "AnnotationStoreDeletedWaiter",
    "Client",
    "ListAnnotationImportJobsPaginator",
    "ListAnnotationStoresPaginator",
    "ListReadSetActivationJobsPaginator",
    "ListReadSetExportJobsPaginator",
    "ListReadSetImportJobsPaginator",
    "ListReadSetsPaginator",
    "ListReferenceImportJobsPaginator",
    "ListReferenceStoresPaginator",
    "ListReferencesPaginator",
    "ListRunGroupsPaginator",
    "ListRunTasksPaginator",
    "ListRunsPaginator",
    "ListSequenceStoresPaginator",
    "ListVariantImportJobsPaginator",
    "ListVariantStoresPaginator",
    "ListWorkflowsPaginator",
    "OmicsClient",
    "ReadSetActivationJobCompletedWaiter",
    "ReadSetExportJobCompletedWaiter",
    "ReadSetImportJobCompletedWaiter",
    "ReferenceImportJobCompletedWaiter",
    "RunCompletedWaiter",
    "RunRunningWaiter",
    "TaskCompletedWaiter",
    "TaskRunningWaiter",
    "VariantImportJobCreatedWaiter",
    "VariantStoreCreatedWaiter",
    "VariantStoreDeletedWaiter",
    "WorkflowActiveWaiter",
)
