"""
Type annotations for sms service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/literals.html)

Usage::

    ```python
    from mypy_boto3_sms.literals import AppLaunchConfigurationStatusType

    data: AppLaunchConfigurationStatusType = "CONFIGURED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AppLaunchConfigurationStatusType",
    "AppLaunchStatusType",
    "AppReplicationConfigurationStatusType",
    "AppReplicationStatusType",
    "AppStatusType",
    "AppValidationStrategyType",
    "ConnectorCapabilityType",
    "ConnectorStatusType",
    "GetConnectorsPaginatorName",
    "GetReplicationJobsPaginatorName",
    "GetReplicationRunsPaginatorName",
    "GetServersPaginatorName",
    "LicenseTypeType",
    "ListAppsPaginatorName",
    "OutputFormatType",
    "ReplicationJobStateType",
    "ReplicationRunStateType",
    "ReplicationRunTypeType",
    "ScriptTypeType",
    "ServerCatalogStatusType",
    "ServerTypeType",
    "ServerValidationStrategyType",
    "ValidationStatusType",
    "VmManagerTypeType",
)

AppLaunchConfigurationStatusType = Literal["CONFIGURED", "NOT_CONFIGURED"]
AppLaunchStatusType = Literal[
    "CONFIGURATION_INVALID",
    "CONFIGURATION_IN_PROGRESS",
    "DELTA_LAUNCH_FAILED",
    "DELTA_LAUNCH_IN_PROGRESS",
    "LAUNCHED",
    "LAUNCH_FAILED",
    "LAUNCH_IN_PROGRESS",
    "LAUNCH_PENDING",
    "PARTIALLY_LAUNCHED",
    "READY_FOR_CONFIGURATION",
    "READY_FOR_LAUNCH",
    "TERMINATED",
    "TERMINATE_FAILED",
    "TERMINATE_IN_PROGRESS",
    "VALIDATION_IN_PROGRESS",
]
AppReplicationConfigurationStatusType = Literal["CONFIGURED", "NOT_CONFIGURED"]
AppReplicationStatusType = Literal[
    "CONFIGURATION_INVALID",
    "CONFIGURATION_IN_PROGRESS",
    "DELTA_REPLICATED",
    "DELTA_REPLICATION_FAILED",
    "DELTA_REPLICATION_IN_PROGRESS",
    "PARTIALLY_REPLICATED",
    "READY_FOR_CONFIGURATION",
    "READY_FOR_REPLICATION",
    "REPLICATED",
    "REPLICATION_FAILED",
    "REPLICATION_IN_PROGRESS",
    "REPLICATION_PENDING",
    "REPLICATION_STOPPED",
    "REPLICATION_STOPPING",
    "REPLICATION_STOP_FAILED",
    "VALIDATION_IN_PROGRESS",
]
AppStatusType = Literal["ACTIVE", "CREATING", "DELETED", "DELETE_FAILED", "DELETING", "UPDATING"]
AppValidationStrategyType = Literal["SSM"]
ConnectorCapabilityType = Literal[
    "HYPERV-MANAGER", "SCVMM", "SMS_OPTIMIZED", "SNAPSHOT_BATCHING", "VSPHERE"
]
ConnectorStatusType = Literal["HEALTHY", "UNHEALTHY"]
GetConnectorsPaginatorName = Literal["get_connectors"]
GetReplicationJobsPaginatorName = Literal["get_replication_jobs"]
GetReplicationRunsPaginatorName = Literal["get_replication_runs"]
GetServersPaginatorName = Literal["get_servers"]
LicenseTypeType = Literal["AWS", "BYOL"]
ListAppsPaginatorName = Literal["list_apps"]
OutputFormatType = Literal["JSON", "YAML"]
ReplicationJobStateType = Literal[
    "ACTIVE",
    "COMPLETED",
    "DELETED",
    "DELETING",
    "FAILED",
    "FAILING",
    "PAUSED_ON_FAILURE",
    "PENDING",
]
ReplicationRunStateType = Literal[
    "ACTIVE", "COMPLETED", "DELETED", "DELETING", "FAILED", "MISSED", "PENDING"
]
ReplicationRunTypeType = Literal["AUTOMATIC", "ON_DEMAND"]
ScriptTypeType = Literal["POWERSHELL_SCRIPT", "SHELL_SCRIPT"]
ServerCatalogStatusType = Literal["AVAILABLE", "DELETED", "EXPIRED", "IMPORTING", "NOT_IMPORTED"]
ServerTypeType = Literal["VIRTUAL_MACHINE"]
ServerValidationStrategyType = Literal["USERDATA"]
ValidationStatusType = Literal[
    "FAILED", "IN_PROGRESS", "PENDING", "READY_FOR_VALIDATION", "SUCCEEDED"
]
VmManagerTypeType = Literal["HYPERV-MANAGER", "SCVMM", "VSPHERE"]
