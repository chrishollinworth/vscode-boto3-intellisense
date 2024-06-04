"""
Type annotations for m2 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/literals.html)

Usage::

    ```python
    from mypy_boto3_m2.literals import ApplicationDeploymentLifecycleType

    data: ApplicationDeploymentLifecycleType = "Deployed"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ApplicationDeploymentLifecycleType",
    "ApplicationLifecycleType",
    "ApplicationVersionLifecycleType",
    "BatchJobExecutionStatusType",
    "BatchJobTypeType",
    "DataSetTaskLifecycleType",
    "DeploymentLifecycleType",
    "EngineTypeType",
    "EnvironmentLifecycleType",
    "ListApplicationVersionsPaginatorName",
    "ListApplicationsPaginatorName",
    "ListBatchJobDefinitionsPaginatorName",
    "ListBatchJobExecutionsPaginatorName",
    "ListDataSetImportHistoryPaginatorName",
    "ListDataSetsPaginatorName",
    "ListDeploymentsPaginatorName",
    "ListEngineVersionsPaginatorName",
    "ListEnvironmentsPaginatorName",
)

ApplicationDeploymentLifecycleType = Literal["Deployed", "Deploying"]
ApplicationLifecycleType = Literal[
    "Available",
    "Created",
    "Creating",
    "Deleting",
    "Deleting From Environment",
    "Failed",
    "Ready",
    "Running",
    "Starting",
    "Stopped",
    "Stopping",
]
ApplicationVersionLifecycleType = Literal["Available", "Creating", "Failed"]
BatchJobExecutionStatusType = Literal[
    "Cancelled",
    "Cancelling",
    "Dispatching",
    "Failed",
    "Holding",
    "Purged",
    "Running",
    "Submitting",
    "Succeeded",
    "Succeeded With Warning",
]
BatchJobTypeType = Literal["JES2", "JES3", "VSE"]
DataSetTaskLifecycleType = Literal["Completed", "Creating", "Failed", "Running"]
DeploymentLifecycleType = Literal["Deploying", "Failed", "Succeeded", "Updating Deployment"]
EngineTypeType = Literal["bluage", "microfocus"]
EnvironmentLifecycleType = Literal["Available", "Creating", "Deleting", "Failed", "Updating"]
ListApplicationVersionsPaginatorName = Literal["list_application_versions"]
ListApplicationsPaginatorName = Literal["list_applications"]
ListBatchJobDefinitionsPaginatorName = Literal["list_batch_job_definitions"]
ListBatchJobExecutionsPaginatorName = Literal["list_batch_job_executions"]
ListDataSetImportHistoryPaginatorName = Literal["list_data_set_import_history"]
ListDataSetsPaginatorName = Literal["list_data_sets"]
ListDeploymentsPaginatorName = Literal["list_deployments"]
ListEngineVersionsPaginatorName = Literal["list_engine_versions"]
ListEnvironmentsPaginatorName = Literal["list_environments"]
