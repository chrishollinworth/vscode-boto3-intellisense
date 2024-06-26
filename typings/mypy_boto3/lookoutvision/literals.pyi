"""
Type annotations for lookoutvision service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/literals.html)

Usage::

    ```python
    from mypy_boto3_lookoutvision.literals import DatasetStatusType

    data: DatasetStatusType = "CREATE_COMPLETE"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DatasetStatusType",
    "ListDatasetEntriesPaginatorName",
    "ListModelPackagingJobsPaginatorName",
    "ListModelsPaginatorName",
    "ListProjectsPaginatorName",
    "ModelHostingStatusType",
    "ModelPackagingJobStatusType",
    "ModelStatusType",
    "TargetDeviceType",
    "TargetPlatformAcceleratorType",
    "TargetPlatformArchType",
    "TargetPlatformOsType",
)

DatasetStatusType = Literal[
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETE_COMPLETE",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "UPDATE_COMPLETE",
    "UPDATE_FAILED_ROLLBACK_COMPLETE",
    "UPDATE_FAILED_ROLLBACK_IN_PROGRESS",
    "UPDATE_IN_PROGRESS",
]
ListDatasetEntriesPaginatorName = Literal["list_dataset_entries"]
ListModelPackagingJobsPaginatorName = Literal["list_model_packaging_jobs"]
ListModelsPaginatorName = Literal["list_models"]
ListProjectsPaginatorName = Literal["list_projects"]
ModelHostingStatusType = Literal[
    "HOSTED", "HOSTING_FAILED", "STARTING_HOSTING", "STOPPING_HOSTING", "SYSTEM_UPDATING"
]
ModelPackagingJobStatusType = Literal["CREATED", "FAILED", "RUNNING", "SUCCEEDED"]
ModelStatusType = Literal[
    "DELETING",
    "HOSTED",
    "HOSTING_FAILED",
    "STARTING_HOSTING",
    "STOPPING_HOSTING",
    "SYSTEM_UPDATING",
    "TRAINED",
    "TRAINING",
    "TRAINING_FAILED",
]
TargetDeviceType = Literal["jetson_xavier"]
TargetPlatformAcceleratorType = Literal["NVIDIA"]
TargetPlatformArchType = Literal["ARM64", "X86_64"]
TargetPlatformOsType = Literal["LINUX"]
