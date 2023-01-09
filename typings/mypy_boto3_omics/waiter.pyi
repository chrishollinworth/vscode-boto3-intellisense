"""
Type annotations for omics service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_omics import OmicsClient
    from mypy_boto3_omics.waiter import (
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

    client: OmicsClient = boto3.client("omics")

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
    ```
"""
import sys
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AnnotationImportJobCreatedWaiter",
    "AnnotationStoreCreatedWaiter",
    "AnnotationStoreDeletedWaiter",
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

class AnnotationImportJobCreatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.AnnotationImportJobCreated)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#annotationimportjobcreatedwaiter)
    """

    def wait(self, *, jobId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.AnnotationImportJobCreated.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#annotationimportjobcreatedwaiter)
        """

class AnnotationStoreCreatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.AnnotationStoreCreated)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#annotationstorecreatedwaiter)
    """

    def wait(self, *, name: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.AnnotationStoreCreated.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#annotationstorecreatedwaiter)
        """

class AnnotationStoreDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.AnnotationStoreDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#annotationstoredeletedwaiter)
    """

    def wait(self, *, name: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.AnnotationStoreDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#annotationstoredeletedwaiter)
        """

class ReadSetActivationJobCompletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.ReadSetActivationJobCompleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#readsetactivationjobcompletedwaiter)
    """

    def wait(
        self, *, id: str, sequenceStoreId: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.ReadSetActivationJobCompleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#readsetactivationjobcompletedwaiter)
        """

class ReadSetExportJobCompletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.ReadSetExportJobCompleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#readsetexportjobcompletedwaiter)
    """

    def wait(
        self, *, id: str, sequenceStoreId: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.ReadSetExportJobCompleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#readsetexportjobcompletedwaiter)
        """

class ReadSetImportJobCompletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.ReadSetImportJobCompleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#readsetimportjobcompletedwaiter)
    """

    def wait(
        self, *, id: str, sequenceStoreId: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.ReadSetImportJobCompleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#readsetimportjobcompletedwaiter)
        """

class ReferenceImportJobCompletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.ReferenceImportJobCompleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#referenceimportjobcompletedwaiter)
    """

    def wait(
        self, *, id: str, referenceStoreId: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.ReferenceImportJobCompleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#referenceimportjobcompletedwaiter)
        """

class RunCompletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.RunCompleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#runcompletedwaiter)
    """

    def wait(
        self,
        *,
        id: str,
        export: List[Literal["DEFINITION"]] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.RunCompleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#runcompletedwaiter)
        """

class RunRunningWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.RunRunning)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#runrunningwaiter)
    """

    def wait(
        self,
        *,
        id: str,
        export: List[Literal["DEFINITION"]] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.RunRunning.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#runrunningwaiter)
        """

class TaskCompletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.TaskCompleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#taskcompletedwaiter)
    """

    def wait(self, *, id: str, taskId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.TaskCompleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#taskcompletedwaiter)
        """

class TaskRunningWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.TaskRunning)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#taskrunningwaiter)
    """

    def wait(self, *, id: str, taskId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.TaskRunning.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#taskrunningwaiter)
        """

class VariantImportJobCreatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.VariantImportJobCreated)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#variantimportjobcreatedwaiter)
    """

    def wait(self, *, jobId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.VariantImportJobCreated.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#variantimportjobcreatedwaiter)
        """

class VariantStoreCreatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.VariantStoreCreated)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#variantstorecreatedwaiter)
    """

    def wait(self, *, name: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.VariantStoreCreated.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#variantstorecreatedwaiter)
        """

class VariantStoreDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.VariantStoreDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#variantstoredeletedwaiter)
    """

    def wait(self, *, name: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.VariantStoreDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#variantstoredeletedwaiter)
        """

class WorkflowActiveWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.WorkflowActive)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#workflowactivewaiter)
    """

    def wait(
        self,
        *,
        id: str,
        export: List[Literal["DEFINITION"]] = None,
        type: Literal["PRIVATE"] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/omics.html#Omics.Waiter.WorkflowActive.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/waiters.html#workflowactivewaiter)
        """
