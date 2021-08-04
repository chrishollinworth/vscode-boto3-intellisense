"""
Type annotations for datasync service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/type_defs.html)

Usage::

    ```python
    from mypy_boto3_datasync.type_defs import AgentListEntryTypeDef

    data: AgentListEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AgentStatusType,
    AtimeType,
    EndpointTypeType,
    GidType,
    LocationFilterNameType,
    LogLevelType,
    MtimeType,
    NfsVersionType,
    ObjectStorageServerProtocolType,
    OperatorType,
    OverwriteModeType,
    PhaseStatusType,
    PosixPermissionsType,
    PreserveDeletedFilesType,
    PreserveDevicesType,
    S3StorageClassType,
    SmbSecurityDescriptorCopyFlagsType,
    SmbVersionType,
    TaskExecutionStatusType,
    TaskFilterNameType,
    TaskQueueingType,
    TaskStatusType,
    TransferModeType,
    UidType,
    VerifyModeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AgentListEntryTypeDef",
    "CancelTaskExecutionRequestRequestTypeDef",
    "CreateAgentRequestRequestTypeDef",
    "CreateAgentResponseTypeDef",
    "CreateLocationEfsRequestRequestTypeDef",
    "CreateLocationEfsResponseTypeDef",
    "CreateLocationFsxWindowsRequestRequestTypeDef",
    "CreateLocationFsxWindowsResponseTypeDef",
    "CreateLocationNfsRequestRequestTypeDef",
    "CreateLocationNfsResponseTypeDef",
    "CreateLocationObjectStorageRequestRequestTypeDef",
    "CreateLocationObjectStorageResponseTypeDef",
    "CreateLocationS3RequestRequestTypeDef",
    "CreateLocationS3ResponseTypeDef",
    "CreateLocationSmbRequestRequestTypeDef",
    "CreateLocationSmbResponseTypeDef",
    "CreateTaskRequestRequestTypeDef",
    "CreateTaskResponseTypeDef",
    "DeleteAgentRequestRequestTypeDef",
    "DeleteLocationRequestRequestTypeDef",
    "DeleteTaskRequestRequestTypeDef",
    "DescribeAgentRequestRequestTypeDef",
    "DescribeAgentResponseTypeDef",
    "DescribeLocationEfsRequestRequestTypeDef",
    "DescribeLocationEfsResponseTypeDef",
    "DescribeLocationFsxWindowsRequestRequestTypeDef",
    "DescribeLocationFsxWindowsResponseTypeDef",
    "DescribeLocationNfsRequestRequestTypeDef",
    "DescribeLocationNfsResponseTypeDef",
    "DescribeLocationObjectStorageRequestRequestTypeDef",
    "DescribeLocationObjectStorageResponseTypeDef",
    "DescribeLocationS3RequestRequestTypeDef",
    "DescribeLocationS3ResponseTypeDef",
    "DescribeLocationSmbRequestRequestTypeDef",
    "DescribeLocationSmbResponseTypeDef",
    "DescribeTaskExecutionRequestRequestTypeDef",
    "DescribeTaskExecutionResponseTypeDef",
    "DescribeTaskRequestRequestTypeDef",
    "DescribeTaskResponseTypeDef",
    "Ec2ConfigTypeDef",
    "FilterRuleTypeDef",
    "ListAgentsRequestRequestTypeDef",
    "ListAgentsResponseTypeDef",
    "ListLocationsRequestRequestTypeDef",
    "ListLocationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTaskExecutionsRequestRequestTypeDef",
    "ListTaskExecutionsResponseTypeDef",
    "ListTasksRequestRequestTypeDef",
    "ListTasksResponseTypeDef",
    "LocationFilterTypeDef",
    "LocationListEntryTypeDef",
    "NfsMountOptionsTypeDef",
    "OnPremConfigTypeDef",
    "OptionsTypeDef",
    "PaginatorConfigTypeDef",
    "PrivateLinkConfigTypeDef",
    "ResponseMetadataTypeDef",
    "S3ConfigTypeDef",
    "SmbMountOptionsTypeDef",
    "StartTaskExecutionRequestRequestTypeDef",
    "StartTaskExecutionResponseTypeDef",
    "TagListEntryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TaskExecutionListEntryTypeDef",
    "TaskExecutionResultDetailTypeDef",
    "TaskFilterTypeDef",
    "TaskListEntryTypeDef",
    "TaskScheduleTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAgentRequestRequestTypeDef",
    "UpdateLocationNfsRequestRequestTypeDef",
    "UpdateLocationObjectStorageRequestRequestTypeDef",
    "UpdateLocationSmbRequestRequestTypeDef",
    "UpdateTaskExecutionRequestRequestTypeDef",
    "UpdateTaskRequestRequestTypeDef",
)

AgentListEntryTypeDef = TypedDict(
    "AgentListEntryTypeDef",
    {
        "AgentArn": str,
        "Name": str,
        "Status": AgentStatusType,
    },
    total=False,
)

CancelTaskExecutionRequestRequestTypeDef = TypedDict(
    "CancelTaskExecutionRequestRequestTypeDef",
    {
        "TaskExecutionArn": str,
    },
)

_RequiredCreateAgentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAgentRequestRequestTypeDef",
    {
        "ActivationKey": str,
    },
)
_OptionalCreateAgentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAgentRequestRequestTypeDef",
    {
        "AgentName": str,
        "Tags": List["TagListEntryTypeDef"],
        "VpcEndpointId": str,
        "SubnetArns": List[str],
        "SecurityGroupArns": List[str],
    },
    total=False,
)

class CreateAgentRequestRequestTypeDef(
    _RequiredCreateAgentRequestRequestTypeDef, _OptionalCreateAgentRequestRequestTypeDef
):
    pass

CreateAgentResponseTypeDef = TypedDict(
    "CreateAgentResponseTypeDef",
    {
        "AgentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLocationEfsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationEfsRequestRequestTypeDef",
    {
        "EfsFilesystemArn": str,
        "Ec2Config": "Ec2ConfigTypeDef",
    },
)
_OptionalCreateLocationEfsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationEfsRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "Tags": List["TagListEntryTypeDef"],
    },
    total=False,
)

class CreateLocationEfsRequestRequestTypeDef(
    _RequiredCreateLocationEfsRequestRequestTypeDef, _OptionalCreateLocationEfsRequestRequestTypeDef
):
    pass

CreateLocationEfsResponseTypeDef = TypedDict(
    "CreateLocationEfsResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLocationFsxWindowsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationFsxWindowsRequestRequestTypeDef",
    {
        "FsxFilesystemArn": str,
        "SecurityGroupArns": List[str],
        "User": str,
        "Password": str,
    },
)
_OptionalCreateLocationFsxWindowsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationFsxWindowsRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "Tags": List["TagListEntryTypeDef"],
        "Domain": str,
    },
    total=False,
)

class CreateLocationFsxWindowsRequestRequestTypeDef(
    _RequiredCreateLocationFsxWindowsRequestRequestTypeDef,
    _OptionalCreateLocationFsxWindowsRequestRequestTypeDef,
):
    pass

CreateLocationFsxWindowsResponseTypeDef = TypedDict(
    "CreateLocationFsxWindowsResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLocationNfsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationNfsRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "ServerHostname": str,
        "OnPremConfig": "OnPremConfigTypeDef",
    },
)
_OptionalCreateLocationNfsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationNfsRequestRequestTypeDef",
    {
        "MountOptions": "NfsMountOptionsTypeDef",
        "Tags": List["TagListEntryTypeDef"],
    },
    total=False,
)

class CreateLocationNfsRequestRequestTypeDef(
    _RequiredCreateLocationNfsRequestRequestTypeDef, _OptionalCreateLocationNfsRequestRequestTypeDef
):
    pass

CreateLocationNfsResponseTypeDef = TypedDict(
    "CreateLocationNfsResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLocationObjectStorageRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationObjectStorageRequestRequestTypeDef",
    {
        "ServerHostname": str,
        "BucketName": str,
        "AgentArns": List[str],
    },
)
_OptionalCreateLocationObjectStorageRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationObjectStorageRequestRequestTypeDef",
    {
        "ServerPort": int,
        "ServerProtocol": ObjectStorageServerProtocolType,
        "Subdirectory": str,
        "AccessKey": str,
        "SecretKey": str,
        "Tags": List["TagListEntryTypeDef"],
    },
    total=False,
)

class CreateLocationObjectStorageRequestRequestTypeDef(
    _RequiredCreateLocationObjectStorageRequestRequestTypeDef,
    _OptionalCreateLocationObjectStorageRequestRequestTypeDef,
):
    pass

CreateLocationObjectStorageResponseTypeDef = TypedDict(
    "CreateLocationObjectStorageResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLocationS3RequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationS3RequestRequestTypeDef",
    {
        "S3BucketArn": str,
        "S3Config": "S3ConfigTypeDef",
    },
)
_OptionalCreateLocationS3RequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationS3RequestRequestTypeDef",
    {
        "Subdirectory": str,
        "S3StorageClass": S3StorageClassType,
        "AgentArns": List[str],
        "Tags": List["TagListEntryTypeDef"],
    },
    total=False,
)

class CreateLocationS3RequestRequestTypeDef(
    _RequiredCreateLocationS3RequestRequestTypeDef, _OptionalCreateLocationS3RequestRequestTypeDef
):
    pass

CreateLocationS3ResponseTypeDef = TypedDict(
    "CreateLocationS3ResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLocationSmbRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationSmbRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "ServerHostname": str,
        "User": str,
        "Password": str,
        "AgentArns": List[str],
    },
)
_OptionalCreateLocationSmbRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationSmbRequestRequestTypeDef",
    {
        "Domain": str,
        "MountOptions": "SmbMountOptionsTypeDef",
        "Tags": List["TagListEntryTypeDef"],
    },
    total=False,
)

class CreateLocationSmbRequestRequestTypeDef(
    _RequiredCreateLocationSmbRequestRequestTypeDef, _OptionalCreateLocationSmbRequestRequestTypeDef
):
    pass

CreateLocationSmbResponseTypeDef = TypedDict(
    "CreateLocationSmbResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTaskRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTaskRequestRequestTypeDef",
    {
        "SourceLocationArn": str,
        "DestinationLocationArn": str,
    },
)
_OptionalCreateTaskRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTaskRequestRequestTypeDef",
    {
        "CloudWatchLogGroupArn": str,
        "Name": str,
        "Options": "OptionsTypeDef",
        "Excludes": List["FilterRuleTypeDef"],
        "Schedule": "TaskScheduleTypeDef",
        "Tags": List["TagListEntryTypeDef"],
    },
    total=False,
)

class CreateTaskRequestRequestTypeDef(
    _RequiredCreateTaskRequestRequestTypeDef, _OptionalCreateTaskRequestRequestTypeDef
):
    pass

CreateTaskResponseTypeDef = TypedDict(
    "CreateTaskResponseTypeDef",
    {
        "TaskArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAgentRequestRequestTypeDef = TypedDict(
    "DeleteAgentRequestRequestTypeDef",
    {
        "AgentArn": str,
    },
)

DeleteLocationRequestRequestTypeDef = TypedDict(
    "DeleteLocationRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DeleteTaskRequestRequestTypeDef = TypedDict(
    "DeleteTaskRequestRequestTypeDef",
    {
        "TaskArn": str,
    },
)

DescribeAgentRequestRequestTypeDef = TypedDict(
    "DescribeAgentRequestRequestTypeDef",
    {
        "AgentArn": str,
    },
)

DescribeAgentResponseTypeDef = TypedDict(
    "DescribeAgentResponseTypeDef",
    {
        "AgentArn": str,
        "Name": str,
        "Status": AgentStatusType,
        "LastConnectionTime": datetime,
        "CreationTime": datetime,
        "EndpointType": EndpointTypeType,
        "PrivateLinkConfig": "PrivateLinkConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationEfsRequestRequestTypeDef = TypedDict(
    "DescribeLocationEfsRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationEfsResponseTypeDef = TypedDict(
    "DescribeLocationEfsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "Ec2Config": "Ec2ConfigTypeDef",
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationFsxWindowsRequestRequestTypeDef = TypedDict(
    "DescribeLocationFsxWindowsRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationFsxWindowsResponseTypeDef = TypedDict(
    "DescribeLocationFsxWindowsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "SecurityGroupArns": List[str],
        "CreationTime": datetime,
        "User": str,
        "Domain": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationNfsRequestRequestTypeDef = TypedDict(
    "DescribeLocationNfsRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationNfsResponseTypeDef = TypedDict(
    "DescribeLocationNfsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "OnPremConfig": "OnPremConfigTypeDef",
        "MountOptions": "NfsMountOptionsTypeDef",
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationObjectStorageRequestRequestTypeDef = TypedDict(
    "DescribeLocationObjectStorageRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationObjectStorageResponseTypeDef = TypedDict(
    "DescribeLocationObjectStorageResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "AccessKey": str,
        "ServerPort": int,
        "ServerProtocol": ObjectStorageServerProtocolType,
        "AgentArns": List[str],
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationS3RequestRequestTypeDef = TypedDict(
    "DescribeLocationS3RequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationS3ResponseTypeDef = TypedDict(
    "DescribeLocationS3ResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "S3StorageClass": S3StorageClassType,
        "S3Config": "S3ConfigTypeDef",
        "AgentArns": List[str],
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationSmbRequestRequestTypeDef = TypedDict(
    "DescribeLocationSmbRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationSmbResponseTypeDef = TypedDict(
    "DescribeLocationSmbResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "AgentArns": List[str],
        "User": str,
        "Domain": str,
        "MountOptions": "SmbMountOptionsTypeDef",
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTaskExecutionRequestRequestTypeDef = TypedDict(
    "DescribeTaskExecutionRequestRequestTypeDef",
    {
        "TaskExecutionArn": str,
    },
)

DescribeTaskExecutionResponseTypeDef = TypedDict(
    "DescribeTaskExecutionResponseTypeDef",
    {
        "TaskExecutionArn": str,
        "Status": TaskExecutionStatusType,
        "Options": "OptionsTypeDef",
        "Excludes": List["FilterRuleTypeDef"],
        "Includes": List["FilterRuleTypeDef"],
        "StartTime": datetime,
        "EstimatedFilesToTransfer": int,
        "EstimatedBytesToTransfer": int,
        "FilesTransferred": int,
        "BytesWritten": int,
        "BytesTransferred": int,
        "Result": "TaskExecutionResultDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTaskRequestRequestTypeDef = TypedDict(
    "DescribeTaskRequestRequestTypeDef",
    {
        "TaskArn": str,
    },
)

DescribeTaskResponseTypeDef = TypedDict(
    "DescribeTaskResponseTypeDef",
    {
        "TaskArn": str,
        "Status": TaskStatusType,
        "Name": str,
        "CurrentTaskExecutionArn": str,
        "SourceLocationArn": str,
        "DestinationLocationArn": str,
        "CloudWatchLogGroupArn": str,
        "SourceNetworkInterfaceArns": List[str],
        "DestinationNetworkInterfaceArns": List[str],
        "Options": "OptionsTypeDef",
        "Excludes": List["FilterRuleTypeDef"],
        "Schedule": "TaskScheduleTypeDef",
        "ErrorCode": str,
        "ErrorDetail": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

Ec2ConfigTypeDef = TypedDict(
    "Ec2ConfigTypeDef",
    {
        "SubnetArn": str,
        "SecurityGroupArns": List[str],
    },
)

FilterRuleTypeDef = TypedDict(
    "FilterRuleTypeDef",
    {
        "FilterType": Literal["SIMPLE_PATTERN"],
        "Value": str,
    },
    total=False,
)

ListAgentsRequestRequestTypeDef = TypedDict(
    "ListAgentsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListAgentsResponseTypeDef = TypedDict(
    "ListAgentsResponseTypeDef",
    {
        "Agents": List["AgentListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLocationsRequestRequestTypeDef = TypedDict(
    "ListLocationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["LocationFilterTypeDef"],
    },
    total=False,
)

ListLocationsResponseTypeDef = TypedDict(
    "ListLocationsResponseTypeDef",
    {
        "Locations": List["LocationListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTaskExecutionsRequestRequestTypeDef = TypedDict(
    "ListTaskExecutionsRequestRequestTypeDef",
    {
        "TaskArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListTaskExecutionsResponseTypeDef = TypedDict(
    "ListTaskExecutionsResponseTypeDef",
    {
        "TaskExecutions": List["TaskExecutionListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTasksRequestRequestTypeDef = TypedDict(
    "ListTasksRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["TaskFilterTypeDef"],
    },
    total=False,
)

ListTasksResponseTypeDef = TypedDict(
    "ListTasksResponseTypeDef",
    {
        "Tasks": List["TaskListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocationFilterTypeDef = TypedDict(
    "LocationFilterTypeDef",
    {
        "Name": LocationFilterNameType,
        "Values": List[str],
        "Operator": OperatorType,
    },
)

LocationListEntryTypeDef = TypedDict(
    "LocationListEntryTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
    },
    total=False,
)

NfsMountOptionsTypeDef = TypedDict(
    "NfsMountOptionsTypeDef",
    {
        "Version": NfsVersionType,
    },
    total=False,
)

OnPremConfigTypeDef = TypedDict(
    "OnPremConfigTypeDef",
    {
        "AgentArns": List[str],
    },
)

OptionsTypeDef = TypedDict(
    "OptionsTypeDef",
    {
        "VerifyMode": VerifyModeType,
        "OverwriteMode": OverwriteModeType,
        "Atime": AtimeType,
        "Mtime": MtimeType,
        "Uid": UidType,
        "Gid": GidType,
        "PreserveDeletedFiles": PreserveDeletedFilesType,
        "PreserveDevices": PreserveDevicesType,
        "PosixPermissions": PosixPermissionsType,
        "BytesPerSecond": int,
        "TaskQueueing": TaskQueueingType,
        "LogLevel": LogLevelType,
        "TransferMode": TransferModeType,
        "SecurityDescriptorCopyFlags": SmbSecurityDescriptorCopyFlagsType,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PrivateLinkConfigTypeDef = TypedDict(
    "PrivateLinkConfigTypeDef",
    {
        "VpcEndpointId": str,
        "PrivateLinkEndpoint": str,
        "SubnetArns": List[str],
        "SecurityGroupArns": List[str],
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

S3ConfigTypeDef = TypedDict(
    "S3ConfigTypeDef",
    {
        "BucketAccessRoleArn": str,
    },
)

SmbMountOptionsTypeDef = TypedDict(
    "SmbMountOptionsTypeDef",
    {
        "Version": SmbVersionType,
    },
    total=False,
)

_RequiredStartTaskExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredStartTaskExecutionRequestRequestTypeDef",
    {
        "TaskArn": str,
    },
)
_OptionalStartTaskExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalStartTaskExecutionRequestRequestTypeDef",
    {
        "OverrideOptions": "OptionsTypeDef",
        "Includes": List["FilterRuleTypeDef"],
    },
    total=False,
)

class StartTaskExecutionRequestRequestTypeDef(
    _RequiredStartTaskExecutionRequestRequestTypeDef,
    _OptionalStartTaskExecutionRequestRequestTypeDef,
):
    pass

StartTaskExecutionResponseTypeDef = TypedDict(
    "StartTaskExecutionResponseTypeDef",
    {
        "TaskExecutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTagListEntryTypeDef = TypedDict(
    "_RequiredTagListEntryTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagListEntryTypeDef = TypedDict(
    "_OptionalTagListEntryTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class TagListEntryTypeDef(_RequiredTagListEntryTypeDef, _OptionalTagListEntryTypeDef):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagListEntryTypeDef"],
    },
)

TaskExecutionListEntryTypeDef = TypedDict(
    "TaskExecutionListEntryTypeDef",
    {
        "TaskExecutionArn": str,
        "Status": TaskExecutionStatusType,
    },
    total=False,
)

TaskExecutionResultDetailTypeDef = TypedDict(
    "TaskExecutionResultDetailTypeDef",
    {
        "PrepareDuration": int,
        "PrepareStatus": PhaseStatusType,
        "TotalDuration": int,
        "TransferDuration": int,
        "TransferStatus": PhaseStatusType,
        "VerifyDuration": int,
        "VerifyStatus": PhaseStatusType,
        "ErrorCode": str,
        "ErrorDetail": str,
    },
    total=False,
)

TaskFilterTypeDef = TypedDict(
    "TaskFilterTypeDef",
    {
        "Name": TaskFilterNameType,
        "Values": List[str],
        "Operator": OperatorType,
    },
)

TaskListEntryTypeDef = TypedDict(
    "TaskListEntryTypeDef",
    {
        "TaskArn": str,
        "Status": TaskStatusType,
        "Name": str,
    },
    total=False,
)

TaskScheduleTypeDef = TypedDict(
    "TaskScheduleTypeDef",
    {
        "ScheduleExpression": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Keys": List[str],
    },
)

_RequiredUpdateAgentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAgentRequestRequestTypeDef",
    {
        "AgentArn": str,
    },
)
_OptionalUpdateAgentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAgentRequestRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class UpdateAgentRequestRequestTypeDef(
    _RequiredUpdateAgentRequestRequestTypeDef, _OptionalUpdateAgentRequestRequestTypeDef
):
    pass

_RequiredUpdateLocationNfsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLocationNfsRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)
_OptionalUpdateLocationNfsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLocationNfsRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "OnPremConfig": "OnPremConfigTypeDef",
        "MountOptions": "NfsMountOptionsTypeDef",
    },
    total=False,
)

class UpdateLocationNfsRequestRequestTypeDef(
    _RequiredUpdateLocationNfsRequestRequestTypeDef, _OptionalUpdateLocationNfsRequestRequestTypeDef
):
    pass

_RequiredUpdateLocationObjectStorageRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLocationObjectStorageRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)
_OptionalUpdateLocationObjectStorageRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLocationObjectStorageRequestRequestTypeDef",
    {
        "ServerPort": int,
        "ServerProtocol": ObjectStorageServerProtocolType,
        "Subdirectory": str,
        "AccessKey": str,
        "SecretKey": str,
        "AgentArns": List[str],
    },
    total=False,
)

class UpdateLocationObjectStorageRequestRequestTypeDef(
    _RequiredUpdateLocationObjectStorageRequestRequestTypeDef,
    _OptionalUpdateLocationObjectStorageRequestRequestTypeDef,
):
    pass

_RequiredUpdateLocationSmbRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLocationSmbRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)
_OptionalUpdateLocationSmbRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLocationSmbRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "User": str,
        "Domain": str,
        "Password": str,
        "AgentArns": List[str],
        "MountOptions": "SmbMountOptionsTypeDef",
    },
    total=False,
)

class UpdateLocationSmbRequestRequestTypeDef(
    _RequiredUpdateLocationSmbRequestRequestTypeDef, _OptionalUpdateLocationSmbRequestRequestTypeDef
):
    pass

UpdateTaskExecutionRequestRequestTypeDef = TypedDict(
    "UpdateTaskExecutionRequestRequestTypeDef",
    {
        "TaskExecutionArn": str,
        "Options": "OptionsTypeDef",
    },
)

_RequiredUpdateTaskRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTaskRequestRequestTypeDef",
    {
        "TaskArn": str,
    },
)
_OptionalUpdateTaskRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTaskRequestRequestTypeDef",
    {
        "Options": "OptionsTypeDef",
        "Excludes": List["FilterRuleTypeDef"],
        "Schedule": "TaskScheduleTypeDef",
        "Name": str,
        "CloudWatchLogGroupArn": str,
    },
    total=False,
)

class UpdateTaskRequestRequestTypeDef(
    _RequiredUpdateTaskRequestRequestTypeDef, _OptionalUpdateTaskRequestRequestTypeDef
):
    pass
