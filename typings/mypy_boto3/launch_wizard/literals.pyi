"""
Type annotations for launch-wizard service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/literals.html)

Usage::

    ```python
    from mypy_boto3_launch_wizard.literals import DeploymentFilterKeyType

    data: DeploymentFilterKeyType = "DEPLOYMENT_STATUS"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DeploymentFilterKeyType",
    "DeploymentStatusType",
    "EventStatusType",
    "ListDeploymentEventsPaginatorName",
    "ListDeploymentsPaginatorName",
    "ListWorkloadDeploymentPatternsPaginatorName",
    "ListWorkloadsPaginatorName",
    "WorkloadDeploymentPatternStatusType",
    "WorkloadStatusType",
)

DeploymentFilterKeyType = Literal["DEPLOYMENT_STATUS", "WORKLOAD_NAME"]
DeploymentStatusType = Literal[
    "COMPLETED",
    "CREATING",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_INITIATING",
    "DELETE_IN_PROGRESS",
    "FAILED",
    "IN_PROGRESS",
    "VALIDATING",
]
EventStatusType = Literal[
    "CANCELED", "CANCELING", "COMPLETED", "CREATED", "FAILED", "IN_PROGRESS", "PENDING", "TIMED_OUT"
]
ListDeploymentEventsPaginatorName = Literal["list_deployment_events"]
ListDeploymentsPaginatorName = Literal["list_deployments"]
ListWorkloadDeploymentPatternsPaginatorName = Literal["list_workload_deployment_patterns"]
ListWorkloadsPaginatorName = Literal["list_workloads"]
WorkloadDeploymentPatternStatusType = Literal["ACTIVE", "DELETED", "DISABLED", "INACTIVE"]
WorkloadStatusType = Literal["ACTIVE", "DELETED", "DISABLED", "INACTIVE"]
