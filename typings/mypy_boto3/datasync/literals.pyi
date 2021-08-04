"""
Type annotations for datasync service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/literals.html)

Usage::

    ```python
    from mypy_boto3_datasync.literals import AgentStatusType

    data: AgentStatusType = "OFFLINE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AgentStatusType",
    "AtimeType",
    "EndpointTypeType",
    "FilterTypeType",
    "GidType",
    "ListAgentsPaginatorName",
    "ListLocationsPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ListTaskExecutionsPaginatorName",
    "ListTasksPaginatorName",
    "LocationFilterNameType",
    "LogLevelType",
    "MtimeType",
    "NfsVersionType",
    "ObjectStorageServerProtocolType",
    "OperatorType",
    "OverwriteModeType",
    "PhaseStatusType",
    "PosixPermissionsType",
    "PreserveDeletedFilesType",
    "PreserveDevicesType",
    "S3StorageClassType",
    "SmbSecurityDescriptorCopyFlagsType",
    "SmbVersionType",
    "TaskExecutionStatusType",
    "TaskFilterNameType",
    "TaskQueueingType",
    "TaskStatusType",
    "TransferModeType",
    "UidType",
    "VerifyModeType",
)

AgentStatusType = Literal["OFFLINE", "ONLINE"]
AtimeType = Literal["BEST_EFFORT", "NONE"]
EndpointTypeType = Literal["FIPS", "PRIVATE_LINK", "PUBLIC"]
FilterTypeType = Literal["SIMPLE_PATTERN"]
GidType = Literal["BOTH", "INT_VALUE", "NAME", "NONE"]
ListAgentsPaginatorName = Literal["list_agents"]
ListLocationsPaginatorName = Literal["list_locations"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ListTaskExecutionsPaginatorName = Literal["list_task_executions"]
ListTasksPaginatorName = Literal["list_tasks"]
LocationFilterNameType = Literal["CreationTime", "LocationType", "LocationUri"]
LogLevelType = Literal["BASIC", "OFF", "TRANSFER"]
MtimeType = Literal["NONE", "PRESERVE"]
NfsVersionType = Literal["AUTOMATIC", "NFS3", "NFS4_0", "NFS4_1"]
ObjectStorageServerProtocolType = Literal["HTTP", "HTTPS"]
OperatorType = Literal[
    "BeginsWith",
    "Contains",
    "Equals",
    "GreaterThan",
    "GreaterThanOrEqual",
    "In",
    "LessThan",
    "LessThanOrEqual",
    "NotContains",
    "NotEquals",
]
OverwriteModeType = Literal["ALWAYS", "NEVER"]
PhaseStatusType = Literal["ERROR", "PENDING", "SUCCESS"]
PosixPermissionsType = Literal["NONE", "PRESERVE"]
PreserveDeletedFilesType = Literal["PRESERVE", "REMOVE"]
PreserveDevicesType = Literal["NONE", "PRESERVE"]
S3StorageClassType = Literal[
    "DEEP_ARCHIVE",
    "GLACIER",
    "INTELLIGENT_TIERING",
    "ONEZONE_IA",
    "OUTPOSTS",
    "STANDARD",
    "STANDARD_IA",
]
SmbSecurityDescriptorCopyFlagsType = Literal["NONE", "OWNER_DACL", "OWNER_DACL_SACL"]
SmbVersionType = Literal["AUTOMATIC", "SMB2", "SMB3"]
TaskExecutionStatusType = Literal[
    "ERROR", "LAUNCHING", "PREPARING", "QUEUED", "SUCCESS", "TRANSFERRING", "VERIFYING"
]
TaskFilterNameType = Literal["CreationTime", "LocationId"]
TaskQueueingType = Literal["DISABLED", "ENABLED"]
TaskStatusType = Literal["AVAILABLE", "CREATING", "QUEUED", "RUNNING", "UNAVAILABLE"]
TransferModeType = Literal["ALL", "CHANGED"]
UidType = Literal["BOTH", "INT_VALUE", "NAME", "NONE"]
VerifyModeType = Literal["NONE", "ONLY_FILES_TRANSFERRED", "POINT_IN_TIME_CONSISTENT"]
