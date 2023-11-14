"""
Type annotations for ssm-sap service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/literals.html)

Usage::

    ```python
    from mypy_boto3_ssm_sap.literals import AllocationTypeType

    data: AllocationTypeType = "ELASTIC_IP"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AllocationTypeType",
    "ApplicationDiscoveryStatusType",
    "ApplicationStatusType",
    "ApplicationTypeType",
    "BackintModeType",
    "ClusterStatusType",
    "ComponentStatusType",
    "ComponentTypeType",
    "CredentialTypeType",
    "DatabaseConnectionMethodType",
    "DatabaseStatusType",
    "DatabaseTypeType",
    "FilterOperatorType",
    "HostRoleType",
    "ListApplicationsPaginatorName",
    "ListComponentsPaginatorName",
    "ListDatabasesPaginatorName",
    "ListOperationsPaginatorName",
    "OperationModeType",
    "OperationStatusType",
    "PermissionActionTypeType",
    "ReplicationModeType",
)

AllocationTypeType = Literal["ELASTIC_IP", "OVERLAY", "UNKNOWN", "VPC_SUBNET"]
ApplicationDiscoveryStatusType = Literal[
    "DELETING", "REFRESH_FAILED", "REGISTERING", "REGISTRATION_FAILED", "SUCCESS"
]
ApplicationStatusType = Literal[
    "ACTIVATED", "DELETING", "FAILED", "REGISTERING", "STARTING", "STOPPED", "STOPPING", "UNKNOWN"
]
ApplicationTypeType = Literal["HANA", "SAP_ABAP"]
BackintModeType = Literal["AWSBackup"]
ClusterStatusType = Literal["MAINTENANCE", "NONE", "OFFLINE", "ONLINE", "STANDBY"]
ComponentStatusType = Literal[
    "ACTIVATED", "RUNNING", "RUNNING_WITH_ERROR", "STARTING", "STOPPED", "STOPPING", "UNDEFINED"
]
ComponentTypeType = Literal["ABAP", "ASCS", "DIALOG", "ERS", "HANA", "HANA_NODE", "WD", "WEBDISP"]
CredentialTypeType = Literal["ADMIN"]
DatabaseConnectionMethodType = Literal["DIRECT", "OVERLAY"]
DatabaseStatusType = Literal["ERROR", "RUNNING", "STARTING", "STOPPED", "UNKNOWN", "WARNING"]
DatabaseTypeType = Literal["SYSTEM", "TENANT"]
FilterOperatorType = Literal["Equals", "GreaterThanOrEquals", "LessThanOrEquals"]
HostRoleType = Literal["LEADER", "STANDBY", "UNKNOWN", "WORKER"]
ListApplicationsPaginatorName = Literal["list_applications"]
ListComponentsPaginatorName = Literal["list_components"]
ListDatabasesPaginatorName = Literal["list_databases"]
ListOperationsPaginatorName = Literal["list_operations"]
OperationModeType = Literal[
    "DELTA_DATASHIPPING", "LOGREPLAY", "LOGREPLAY_READACCESS", "NONE", "PRIMARY"
]
OperationStatusType = Literal["ERROR", "INPROGRESS", "SUCCESS"]
PermissionActionTypeType = Literal["RESTORE"]
ReplicationModeType = Literal["ASYNC", "NONE", "PRIMARY", "SYNC", "SYNCMEM"]
