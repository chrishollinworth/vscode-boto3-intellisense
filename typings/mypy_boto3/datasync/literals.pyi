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
    "AzureAccessTierType",
    "AzureBlobAuthenticationTypeType",
    "AzureBlobTypeType",
    "DescribeStorageSystemResourceMetricsPaginatorName",
    "DiscoveryJobStatusType",
    "DiscoveryResourceFilterType",
    "DiscoveryResourceTypeType",
    "DiscoverySystemTypeType",
    "EfsInTransitEncryptionType",
    "EndpointTypeType",
    "FilterTypeType",
    "GidType",
    "HdfsAuthenticationTypeType",
    "HdfsDataTransferProtectionType",
    "HdfsRpcProtectionType",
    "ListAgentsPaginatorName",
    "ListDiscoveryJobsPaginatorName",
    "ListLocationsPaginatorName",
    "ListStorageSystemsPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ListTaskExecutionsPaginatorName",
    "ListTasksPaginatorName",
    "LocationFilterNameType",
    "LogLevelType",
    "MtimeType",
    "NfsVersionType",
    "ObjectStorageServerProtocolType",
    "ObjectTagsType",
    "ObjectVersionIdsType",
    "OperatorType",
    "OverwriteModeType",
    "PhaseStatusType",
    "PosixPermissionsType",
    "PreserveDeletedFilesType",
    "PreserveDevicesType",
    "RecommendationStatusType",
    "ReportLevelType",
    "ReportOutputTypeType",
    "S3StorageClassType",
    "SmbSecurityDescriptorCopyFlagsType",
    "SmbVersionType",
    "StorageSystemConnectivityStatusType",
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
AzureAccessTierType = Literal["ARCHIVE", "COOL", "HOT"]
AzureBlobAuthenticationTypeType = Literal["SAS"]
AzureBlobTypeType = Literal["BLOCK"]
DescribeStorageSystemResourceMetricsPaginatorName = Literal[
    "describe_storage_system_resource_metrics"
]
DiscoveryJobStatusType = Literal[
    "COMPLETED", "COMPLETED_WITH_ISSUES", "FAILED", "RUNNING", "STOPPED", "TERMINATED", "WARNING"
]
DiscoveryResourceFilterType = Literal["SVM"]
DiscoveryResourceTypeType = Literal["CLUSTER", "SVM", "VOLUME"]
DiscoverySystemTypeType = Literal["NetAppONTAP"]
EfsInTransitEncryptionType = Literal["NONE", "TLS1_2"]
EndpointTypeType = Literal["FIPS", "PRIVATE_LINK", "PUBLIC"]
FilterTypeType = Literal["SIMPLE_PATTERN"]
GidType = Literal["BOTH", "INT_VALUE", "NAME", "NONE"]
HdfsAuthenticationTypeType = Literal["KERBEROS", "SIMPLE"]
HdfsDataTransferProtectionType = Literal["AUTHENTICATION", "DISABLED", "INTEGRITY", "PRIVACY"]
HdfsRpcProtectionType = Literal["AUTHENTICATION", "DISABLED", "INTEGRITY", "PRIVACY"]
ListAgentsPaginatorName = Literal["list_agents"]
ListDiscoveryJobsPaginatorName = Literal["list_discovery_jobs"]
ListLocationsPaginatorName = Literal["list_locations"]
ListStorageSystemsPaginatorName = Literal["list_storage_systems"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ListTaskExecutionsPaginatorName = Literal["list_task_executions"]
ListTasksPaginatorName = Literal["list_tasks"]
LocationFilterNameType = Literal["CreationTime", "LocationType", "LocationUri"]
LogLevelType = Literal["BASIC", "OFF", "TRANSFER"]
MtimeType = Literal["NONE", "PRESERVE"]
NfsVersionType = Literal["AUTOMATIC", "NFS3", "NFS4_0", "NFS4_1"]
ObjectStorageServerProtocolType = Literal["HTTP", "HTTPS"]
ObjectTagsType = Literal["NONE", "PRESERVE"]
ObjectVersionIdsType = Literal["INCLUDE", "NONE"]
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
RecommendationStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "NONE"]
ReportLevelType = Literal["ERRORS_ONLY", "SUCCESSES_AND_ERRORS"]
ReportOutputTypeType = Literal["STANDARD", "SUMMARY_ONLY"]
S3StorageClassType = Literal[
    "DEEP_ARCHIVE",
    "GLACIER",
    "GLACIER_INSTANT_RETRIEVAL",
    "INTELLIGENT_TIERING",
    "ONEZONE_IA",
    "OUTPOSTS",
    "STANDARD",
    "STANDARD_IA",
]
SmbSecurityDescriptorCopyFlagsType = Literal["NONE", "OWNER_DACL", "OWNER_DACL_SACL"]
SmbVersionType = Literal["AUTOMATIC", "SMB1", "SMB2", "SMB2_0", "SMB3"]
StorageSystemConnectivityStatusType = Literal["FAIL", "PASS", "UNKNOWN"]
TaskExecutionStatusType = Literal[
    "ERROR", "LAUNCHING", "PREPARING", "QUEUED", "SUCCESS", "TRANSFERRING", "VERIFYING"
]
TaskFilterNameType = Literal["CreationTime", "LocationId"]
TaskQueueingType = Literal["DISABLED", "ENABLED"]
TaskStatusType = Literal["AVAILABLE", "CREATING", "QUEUED", "RUNNING", "UNAVAILABLE"]
TransferModeType = Literal["ALL", "CHANGED"]
UidType = Literal["BOTH", "INT_VALUE", "NAME", "NONE"]
VerifyModeType = Literal["NONE", "ONLY_FILES_TRANSFERRED", "POINT_IN_TIME_CONSISTENT"]
