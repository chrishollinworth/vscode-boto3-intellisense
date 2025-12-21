"""
Type annotations for datasync service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_datasync.type_defs import PlatformTypeDef

    data: PlatformTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    AgentStatusType,
    AtimeType,
    AzureAccessTierType,
    AzureBlobAuthenticationTypeType,
    EfsInTransitEncryptionType,
    EndpointTypeType,
    GidType,
    HdfsAuthenticationTypeType,
    HdfsDataTransferProtectionType,
    HdfsRpcProtectionType,
    LocationFilterNameType,
    LogLevelType,
    MtimeType,
    NfsVersionType,
    ObjectStorageServerProtocolType,
    ObjectTagsType,
    ObjectVersionIdsType,
    OperatorType,
    OverwriteModeType,
    PhaseStatusType,
    PosixPermissionsType,
    PreserveDeletedFilesType,
    PreserveDevicesType,
    ReportLevelType,
    ReportOutputTypeType,
    S3StorageClassType,
    ScheduleDisabledByType,
    ScheduleStatusType,
    SmbAuthenticationTypeType,
    SmbSecurityDescriptorCopyFlagsType,
    SmbVersionType,
    TaskExecutionStatusType,
    TaskFilterNameType,
    TaskModeType,
    TaskQueueingType,
    TaskStatusType,
    TransferModeType,
    UidType,
    VerifyModeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AgentListEntryTypeDef",
    "AzureBlobSasConfigurationTypeDef",
    "BlobTypeDef",
    "CancelTaskExecutionRequestTypeDef",
    "CmkSecretConfigTypeDef",
    "CreateAgentRequestTypeDef",
    "CreateAgentResponseTypeDef",
    "CreateLocationAzureBlobRequestTypeDef",
    "CreateLocationAzureBlobResponseTypeDef",
    "CreateLocationEfsRequestTypeDef",
    "CreateLocationEfsResponseTypeDef",
    "CreateLocationFsxLustreRequestTypeDef",
    "CreateLocationFsxLustreResponseTypeDef",
    "CreateLocationFsxOntapRequestTypeDef",
    "CreateLocationFsxOntapResponseTypeDef",
    "CreateLocationFsxOpenZfsRequestTypeDef",
    "CreateLocationFsxOpenZfsResponseTypeDef",
    "CreateLocationFsxWindowsRequestTypeDef",
    "CreateLocationFsxWindowsResponseTypeDef",
    "CreateLocationHdfsRequestTypeDef",
    "CreateLocationHdfsResponseTypeDef",
    "CreateLocationNfsRequestTypeDef",
    "CreateLocationNfsResponseTypeDef",
    "CreateLocationObjectStorageRequestTypeDef",
    "CreateLocationObjectStorageResponseTypeDef",
    "CreateLocationS3RequestTypeDef",
    "CreateLocationS3ResponseTypeDef",
    "CreateLocationSmbRequestTypeDef",
    "CreateLocationSmbResponseTypeDef",
    "CreateTaskRequestTypeDef",
    "CreateTaskResponseTypeDef",
    "CustomSecretConfigTypeDef",
    "DeleteAgentRequestTypeDef",
    "DeleteLocationRequestTypeDef",
    "DeleteTaskRequestTypeDef",
    "DescribeAgentRequestTypeDef",
    "DescribeAgentResponseTypeDef",
    "DescribeLocationAzureBlobRequestTypeDef",
    "DescribeLocationAzureBlobResponseTypeDef",
    "DescribeLocationEfsRequestTypeDef",
    "DescribeLocationEfsResponseTypeDef",
    "DescribeLocationFsxLustreRequestTypeDef",
    "DescribeLocationFsxLustreResponseTypeDef",
    "DescribeLocationFsxOntapRequestTypeDef",
    "DescribeLocationFsxOntapResponseTypeDef",
    "DescribeLocationFsxOpenZfsRequestTypeDef",
    "DescribeLocationFsxOpenZfsResponseTypeDef",
    "DescribeLocationFsxWindowsRequestTypeDef",
    "DescribeLocationFsxWindowsResponseTypeDef",
    "DescribeLocationHdfsRequestTypeDef",
    "DescribeLocationHdfsResponseTypeDef",
    "DescribeLocationNfsRequestTypeDef",
    "DescribeLocationNfsResponseTypeDef",
    "DescribeLocationObjectStorageRequestTypeDef",
    "DescribeLocationObjectStorageResponseTypeDef",
    "DescribeLocationS3RequestTypeDef",
    "DescribeLocationS3ResponseTypeDef",
    "DescribeLocationSmbRequestTypeDef",
    "DescribeLocationSmbResponseTypeDef",
    "DescribeTaskExecutionRequestTypeDef",
    "DescribeTaskExecutionResponseTypeDef",
    "DescribeTaskRequestTypeDef",
    "DescribeTaskResponseTypeDef",
    "Ec2ConfigOutputTypeDef",
    "Ec2ConfigTypeDef",
    "Ec2ConfigUnionTypeDef",
    "FilterRuleTypeDef",
    "FsxProtocolNfsTypeDef",
    "FsxProtocolSmbTypeDef",
    "FsxProtocolTypeDef",
    "FsxUpdateProtocolSmbTypeDef",
    "FsxUpdateProtocolTypeDef",
    "HdfsNameNodeTypeDef",
    "ListAgentsRequestPaginateTypeDef",
    "ListAgentsRequestTypeDef",
    "ListAgentsResponseTypeDef",
    "ListLocationsRequestPaginateTypeDef",
    "ListLocationsRequestTypeDef",
    "ListLocationsResponseTypeDef",
    "ListTagsForResourceRequestPaginateTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTaskExecutionsRequestPaginateTypeDef",
    "ListTaskExecutionsRequestTypeDef",
    "ListTaskExecutionsResponseTypeDef",
    "ListTasksRequestPaginateTypeDef",
    "ListTasksRequestTypeDef",
    "ListTasksResponseTypeDef",
    "LocationFilterTypeDef",
    "LocationListEntryTypeDef",
    "ManagedSecretConfigTypeDef",
    "ManifestConfigTypeDef",
    "NfsMountOptionsTypeDef",
    "OnPremConfigOutputTypeDef",
    "OnPremConfigTypeDef",
    "OnPremConfigUnionTypeDef",
    "OptionsTypeDef",
    "PaginatorConfigTypeDef",
    "PlatformTypeDef",
    "PrivateLinkConfigTypeDef",
    "QopConfigurationTypeDef",
    "ReportDestinationS3TypeDef",
    "ReportDestinationTypeDef",
    "ReportOverrideTypeDef",
    "ReportOverridesTypeDef",
    "ReportResultTypeDef",
    "ResponseMetadataTypeDef",
    "S3ConfigTypeDef",
    "S3ManifestConfigTypeDef",
    "SmbMountOptionsTypeDef",
    "SourceManifestConfigTypeDef",
    "StartTaskExecutionRequestTypeDef",
    "StartTaskExecutionResponseTypeDef",
    "TagListEntryTypeDef",
    "TagResourceRequestTypeDef",
    "TaskExecutionFilesFailedDetailTypeDef",
    "TaskExecutionFilesListedDetailTypeDef",
    "TaskExecutionFoldersFailedDetailTypeDef",
    "TaskExecutionFoldersListedDetailTypeDef",
    "TaskExecutionListEntryTypeDef",
    "TaskExecutionResultDetailTypeDef",
    "TaskFilterTypeDef",
    "TaskListEntryTypeDef",
    "TaskReportConfigTypeDef",
    "TaskScheduleDetailsTypeDef",
    "TaskScheduleTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAgentRequestTypeDef",
    "UpdateLocationAzureBlobRequestTypeDef",
    "UpdateLocationEfsRequestTypeDef",
    "UpdateLocationFsxLustreRequestTypeDef",
    "UpdateLocationFsxOntapRequestTypeDef",
    "UpdateLocationFsxOpenZfsRequestTypeDef",
    "UpdateLocationFsxWindowsRequestTypeDef",
    "UpdateLocationHdfsRequestTypeDef",
    "UpdateLocationNfsRequestTypeDef",
    "UpdateLocationObjectStorageRequestTypeDef",
    "UpdateLocationS3RequestTypeDef",
    "UpdateLocationSmbRequestTypeDef",
    "UpdateTaskExecutionRequestTypeDef",
    "UpdateTaskRequestTypeDef",
)

class PlatformTypeDef(TypedDict):
    Version: NotRequired[str]

class AzureBlobSasConfigurationTypeDef(TypedDict):
    Token: str

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CancelTaskExecutionRequestTypeDef(TypedDict):
    TaskExecutionArn: str

class CmkSecretConfigTypeDef(TypedDict):
    SecretArn: NotRequired[str]
    KmsKeyArn: NotRequired[str]

class TagListEntryTypeDef(TypedDict):
    Key: str
    Value: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CustomSecretConfigTypeDef(TypedDict):
    SecretArn: NotRequired[str]
    SecretAccessRoleArn: NotRequired[str]

class HdfsNameNodeTypeDef(TypedDict):
    Hostname: str
    Port: int

class QopConfigurationTypeDef(TypedDict):
    RpcProtection: NotRequired[HdfsRpcProtectionType]
    DataTransferProtection: NotRequired[HdfsDataTransferProtectionType]

class NfsMountOptionsTypeDef(TypedDict):
    Version: NotRequired[NfsVersionType]

class S3ConfigTypeDef(TypedDict):
    BucketAccessRoleArn: str

class SmbMountOptionsTypeDef(TypedDict):
    Version: NotRequired[SmbVersionType]

class FilterRuleTypeDef(TypedDict):
    FilterType: NotRequired[Literal["SIMPLE_PATTERN"]]
    Value: NotRequired[str]

class OptionsTypeDef(TypedDict):
    VerifyMode: NotRequired[VerifyModeType]
    OverwriteMode: NotRequired[OverwriteModeType]
    Atime: NotRequired[AtimeType]
    Mtime: NotRequired[MtimeType]
    Uid: NotRequired[UidType]
    Gid: NotRequired[GidType]
    PreserveDeletedFiles: NotRequired[PreserveDeletedFilesType]
    PreserveDevices: NotRequired[PreserveDevicesType]
    PosixPermissions: NotRequired[PosixPermissionsType]
    BytesPerSecond: NotRequired[int]
    TaskQueueing: NotRequired[TaskQueueingType]
    LogLevel: NotRequired[LogLevelType]
    TransferMode: NotRequired[TransferModeType]
    SecurityDescriptorCopyFlags: NotRequired[SmbSecurityDescriptorCopyFlagsType]
    ObjectTags: NotRequired[ObjectTagsType]

class TaskScheduleTypeDef(TypedDict):
    ScheduleExpression: str
    Status: NotRequired[ScheduleStatusType]

class DeleteAgentRequestTypeDef(TypedDict):
    AgentArn: str

class DeleteLocationRequestTypeDef(TypedDict):
    LocationArn: str

class DeleteTaskRequestTypeDef(TypedDict):
    TaskArn: str

class DescribeAgentRequestTypeDef(TypedDict):
    AgentArn: str

class PrivateLinkConfigTypeDef(TypedDict):
    VpcEndpointId: NotRequired[str]
    PrivateLinkEndpoint: NotRequired[str]
    SubnetArns: NotRequired[List[str]]
    SecurityGroupArns: NotRequired[List[str]]

class DescribeLocationAzureBlobRequestTypeDef(TypedDict):
    LocationArn: str

class ManagedSecretConfigTypeDef(TypedDict):
    SecretArn: NotRequired[str]

class DescribeLocationEfsRequestTypeDef(TypedDict):
    LocationArn: str

class Ec2ConfigOutputTypeDef(TypedDict):
    SubnetArn: str
    SecurityGroupArns: List[str]

class DescribeLocationFsxLustreRequestTypeDef(TypedDict):
    LocationArn: str

class DescribeLocationFsxOntapRequestTypeDef(TypedDict):
    LocationArn: str

class DescribeLocationFsxOpenZfsRequestTypeDef(TypedDict):
    LocationArn: str

class DescribeLocationFsxWindowsRequestTypeDef(TypedDict):
    LocationArn: str

class DescribeLocationHdfsRequestTypeDef(TypedDict):
    LocationArn: str

class DescribeLocationNfsRequestTypeDef(TypedDict):
    LocationArn: str

class OnPremConfigOutputTypeDef(TypedDict):
    AgentArns: List[str]

class DescribeLocationObjectStorageRequestTypeDef(TypedDict):
    LocationArn: str

class DescribeLocationS3RequestTypeDef(TypedDict):
    LocationArn: str

class DescribeLocationSmbRequestTypeDef(TypedDict):
    LocationArn: str

class DescribeTaskExecutionRequestTypeDef(TypedDict):
    TaskExecutionArn: str

class ReportResultTypeDef(TypedDict):
    Status: NotRequired[PhaseStatusType]
    ErrorCode: NotRequired[str]
    ErrorDetail: NotRequired[str]

class TaskExecutionFilesFailedDetailTypeDef(TypedDict):
    Prepare: NotRequired[int]
    Transfer: NotRequired[int]
    Verify: NotRequired[int]
    Delete: NotRequired[int]

class TaskExecutionFilesListedDetailTypeDef(TypedDict):
    AtSource: NotRequired[int]
    AtDestinationForDelete: NotRequired[int]

TaskExecutionFoldersFailedDetailTypeDef = TypedDict(
    "TaskExecutionFoldersFailedDetailTypeDef",
    {
        "List": NotRequired[int],
        "Prepare": NotRequired[int],
        "Transfer": NotRequired[int],
        "Verify": NotRequired[int],
        "Delete": NotRequired[int],
    },
)

class TaskExecutionFoldersListedDetailTypeDef(TypedDict):
    AtSource: NotRequired[int]
    AtDestinationForDelete: NotRequired[int]

class TaskExecutionResultDetailTypeDef(TypedDict):
    PrepareDuration: NotRequired[int]
    PrepareStatus: NotRequired[PhaseStatusType]
    TotalDuration: NotRequired[int]
    TransferDuration: NotRequired[int]
    TransferStatus: NotRequired[PhaseStatusType]
    VerifyDuration: NotRequired[int]
    VerifyStatus: NotRequired[PhaseStatusType]
    ErrorCode: NotRequired[str]
    ErrorDetail: NotRequired[str]

class DescribeTaskRequestTypeDef(TypedDict):
    TaskArn: str

class TaskScheduleDetailsTypeDef(TypedDict):
    StatusUpdateTime: NotRequired[datetime]
    DisabledReason: NotRequired[str]
    DisabledBy: NotRequired[ScheduleDisabledByType]

class Ec2ConfigTypeDef(TypedDict):
    SubnetArn: str
    SecurityGroupArns: Sequence[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAgentsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class LocationFilterTypeDef(TypedDict):
    Name: LocationFilterNameType
    Values: Sequence[str]
    Operator: OperatorType

class LocationListEntryTypeDef(TypedDict):
    LocationArn: NotRequired[str]
    LocationUri: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTaskExecutionsRequestTypeDef(TypedDict):
    TaskArn: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class TaskExecutionListEntryTypeDef(TypedDict):
    TaskExecutionArn: NotRequired[str]
    Status: NotRequired[TaskExecutionStatusType]
    TaskMode: NotRequired[TaskModeType]

class TaskFilterTypeDef(TypedDict):
    Name: TaskFilterNameType
    Values: Sequence[str]
    Operator: OperatorType

class TaskListEntryTypeDef(TypedDict):
    TaskArn: NotRequired[str]
    Status: NotRequired[TaskStatusType]
    Name: NotRequired[str]
    TaskMode: NotRequired[TaskModeType]

class OnPremConfigTypeDef(TypedDict):
    AgentArns: Sequence[str]

class ReportDestinationS3TypeDef(TypedDict):
    S3BucketArn: str
    BucketAccessRoleArn: str
    Subdirectory: NotRequired[str]

class ReportOverrideTypeDef(TypedDict):
    ReportLevel: NotRequired[ReportLevelType]

class S3ManifestConfigTypeDef(TypedDict):
    ManifestObjectPath: str
    BucketAccessRoleArn: str
    S3BucketArn: str
    ManifestObjectVersionId: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Keys: Sequence[str]

class UpdateAgentRequestTypeDef(TypedDict):
    AgentArn: str
    Name: NotRequired[str]

class UpdateLocationEfsRequestTypeDef(TypedDict):
    LocationArn: str
    Subdirectory: NotRequired[str]
    AccessPointArn: NotRequired[str]
    FileSystemAccessRoleArn: NotRequired[str]
    InTransitEncryption: NotRequired[EfsInTransitEncryptionType]

class UpdateLocationFsxLustreRequestTypeDef(TypedDict):
    LocationArn: str
    Subdirectory: NotRequired[str]

class UpdateLocationFsxWindowsRequestTypeDef(TypedDict):
    LocationArn: str
    Subdirectory: NotRequired[str]
    Domain: NotRequired[str]
    User: NotRequired[str]
    Password: NotRequired[str]

class AgentListEntryTypeDef(TypedDict):
    AgentArn: NotRequired[str]
    Name: NotRequired[str]
    Status: NotRequired[AgentStatusType]
    Platform: NotRequired[PlatformTypeDef]

class CreateAgentRequestTypeDef(TypedDict):
    ActivationKey: str
    AgentName: NotRequired[str]
    Tags: NotRequired[Sequence[TagListEntryTypeDef]]
    VpcEndpointId: NotRequired[str]
    SubnetArns: NotRequired[Sequence[str]]
    SecurityGroupArns: NotRequired[Sequence[str]]

class CreateLocationFsxLustreRequestTypeDef(TypedDict):
    FsxFilesystemArn: str
    SecurityGroupArns: Sequence[str]
    Subdirectory: NotRequired[str]
    Tags: NotRequired[Sequence[TagListEntryTypeDef]]

class CreateLocationFsxWindowsRequestTypeDef(TypedDict):
    FsxFilesystemArn: str
    SecurityGroupArns: Sequence[str]
    User: str
    Password: str
    Subdirectory: NotRequired[str]
    Tags: NotRequired[Sequence[TagListEntryTypeDef]]
    Domain: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagListEntryTypeDef]

class CreateAgentResponseTypeDef(TypedDict):
    AgentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationAzureBlobResponseTypeDef(TypedDict):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationEfsResponseTypeDef(TypedDict):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationFsxLustreResponseTypeDef(TypedDict):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationFsxOntapResponseTypeDef(TypedDict):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationFsxOpenZfsResponseTypeDef(TypedDict):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationFsxWindowsResponseTypeDef(TypedDict):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationHdfsResponseTypeDef(TypedDict):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationNfsResponseTypeDef(TypedDict):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationObjectStorageResponseTypeDef(TypedDict):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationS3ResponseTypeDef(TypedDict):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationSmbResponseTypeDef(TypedDict):
    LocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTaskResponseTypeDef(TypedDict):
    TaskArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationFsxLustreResponseTypeDef(TypedDict):
    LocationArn: str
    LocationUri: str
    SecurityGroupArns: List[str]
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationFsxWindowsResponseTypeDef(TypedDict):
    LocationArn: str
    LocationUri: str
    SecurityGroupArns: List[str]
    CreationTime: datetime
    User: str
    Domain: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class StartTaskExecutionResponseTypeDef(TypedDict):
    TaskExecutionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocationAzureBlobRequestTypeDef(TypedDict):
    ContainerUrl: str
    AuthenticationType: AzureBlobAuthenticationTypeType
    SasConfiguration: NotRequired[AzureBlobSasConfigurationTypeDef]
    BlobType: NotRequired[Literal["BLOCK"]]
    AccessTier: NotRequired[AzureAccessTierType]
    Subdirectory: NotRequired[str]
    AgentArns: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagListEntryTypeDef]]
    CmkSecretConfig: NotRequired[CmkSecretConfigTypeDef]
    CustomSecretConfig: NotRequired[CustomSecretConfigTypeDef]

class CreateLocationObjectStorageRequestTypeDef(TypedDict):
    ServerHostname: str
    BucketName: str
    ServerPort: NotRequired[int]
    ServerProtocol: NotRequired[ObjectStorageServerProtocolType]
    Subdirectory: NotRequired[str]
    AccessKey: NotRequired[str]
    SecretKey: NotRequired[str]
    AgentArns: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagListEntryTypeDef]]
    ServerCertificate: NotRequired[BlobTypeDef]
    CmkSecretConfig: NotRequired[CmkSecretConfigTypeDef]
    CustomSecretConfig: NotRequired[CustomSecretConfigTypeDef]

class UpdateLocationAzureBlobRequestTypeDef(TypedDict):
    LocationArn: str
    Subdirectory: NotRequired[str]
    AuthenticationType: NotRequired[AzureBlobAuthenticationTypeType]
    SasConfiguration: NotRequired[AzureBlobSasConfigurationTypeDef]
    BlobType: NotRequired[Literal["BLOCK"]]
    AccessTier: NotRequired[AzureAccessTierType]
    AgentArns: NotRequired[Sequence[str]]
    CmkSecretConfig: NotRequired[CmkSecretConfigTypeDef]
    CustomSecretConfig: NotRequired[CustomSecretConfigTypeDef]

class UpdateLocationObjectStorageRequestTypeDef(TypedDict):
    LocationArn: str
    ServerPort: NotRequired[int]
    ServerProtocol: NotRequired[ObjectStorageServerProtocolType]
    Subdirectory: NotRequired[str]
    ServerHostname: NotRequired[str]
    AccessKey: NotRequired[str]
    SecretKey: NotRequired[str]
    AgentArns: NotRequired[Sequence[str]]
    ServerCertificate: NotRequired[BlobTypeDef]
    CmkSecretConfig: NotRequired[CmkSecretConfigTypeDef]
    CustomSecretConfig: NotRequired[CustomSecretConfigTypeDef]

class CreateLocationHdfsRequestTypeDef(TypedDict):
    NameNodes: Sequence[HdfsNameNodeTypeDef]
    AuthenticationType: HdfsAuthenticationTypeType
    AgentArns: Sequence[str]
    Subdirectory: NotRequired[str]
    BlockSize: NotRequired[int]
    ReplicationFactor: NotRequired[int]
    KmsKeyProviderUri: NotRequired[str]
    QopConfiguration: NotRequired[QopConfigurationTypeDef]
    SimpleUser: NotRequired[str]
    KerberosPrincipal: NotRequired[str]
    KerberosKeytab: NotRequired[BlobTypeDef]
    KerberosKrb5Conf: NotRequired[BlobTypeDef]
    Tags: NotRequired[Sequence[TagListEntryTypeDef]]

class DescribeLocationHdfsResponseTypeDef(TypedDict):
    LocationArn: str
    LocationUri: str
    NameNodes: List[HdfsNameNodeTypeDef]
    BlockSize: int
    ReplicationFactor: int
    KmsKeyProviderUri: str
    QopConfiguration: QopConfigurationTypeDef
    AuthenticationType: HdfsAuthenticationTypeType
    SimpleUser: str
    KerberosPrincipal: str
    AgentArns: List[str]
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLocationHdfsRequestTypeDef(TypedDict):
    LocationArn: str
    Subdirectory: NotRequired[str]
    NameNodes: NotRequired[Sequence[HdfsNameNodeTypeDef]]
    BlockSize: NotRequired[int]
    ReplicationFactor: NotRequired[int]
    KmsKeyProviderUri: NotRequired[str]
    QopConfiguration: NotRequired[QopConfigurationTypeDef]
    AuthenticationType: NotRequired[HdfsAuthenticationTypeType]
    SimpleUser: NotRequired[str]
    KerberosPrincipal: NotRequired[str]
    KerberosKeytab: NotRequired[BlobTypeDef]
    KerberosKrb5Conf: NotRequired[BlobTypeDef]
    AgentArns: NotRequired[Sequence[str]]

class FsxProtocolNfsTypeDef(TypedDict):
    MountOptions: NotRequired[NfsMountOptionsTypeDef]

class CreateLocationS3RequestTypeDef(TypedDict):
    S3BucketArn: str
    S3Config: S3ConfigTypeDef
    Subdirectory: NotRequired[str]
    S3StorageClass: NotRequired[S3StorageClassType]
    AgentArns: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagListEntryTypeDef]]

class DescribeLocationS3ResponseTypeDef(TypedDict):
    LocationArn: str
    LocationUri: str
    S3StorageClass: S3StorageClassType
    S3Config: S3ConfigTypeDef
    AgentArns: List[str]
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLocationS3RequestTypeDef(TypedDict):
    LocationArn: str
    Subdirectory: NotRequired[str]
    S3StorageClass: NotRequired[S3StorageClassType]
    S3Config: NotRequired[S3ConfigTypeDef]

class CreateLocationSmbRequestTypeDef(TypedDict):
    Subdirectory: str
    ServerHostname: str
    AgentArns: Sequence[str]
    User: NotRequired[str]
    Domain: NotRequired[str]
    Password: NotRequired[str]
    CmkSecretConfig: NotRequired[CmkSecretConfigTypeDef]
    CustomSecretConfig: NotRequired[CustomSecretConfigTypeDef]
    MountOptions: NotRequired[SmbMountOptionsTypeDef]
    Tags: NotRequired[Sequence[TagListEntryTypeDef]]
    AuthenticationType: NotRequired[SmbAuthenticationTypeType]
    DnsIpAddresses: NotRequired[Sequence[str]]
    KerberosPrincipal: NotRequired[str]
    KerberosKeytab: NotRequired[BlobTypeDef]
    KerberosKrb5Conf: NotRequired[BlobTypeDef]

class FsxProtocolSmbTypeDef(TypedDict):
    Password: str
    User: str
    Domain: NotRequired[str]
    MountOptions: NotRequired[SmbMountOptionsTypeDef]

class FsxUpdateProtocolSmbTypeDef(TypedDict):
    Domain: NotRequired[str]
    MountOptions: NotRequired[SmbMountOptionsTypeDef]
    Password: NotRequired[str]
    User: NotRequired[str]

class UpdateLocationSmbRequestTypeDef(TypedDict):
    LocationArn: str
    Subdirectory: NotRequired[str]
    ServerHostname: NotRequired[str]
    User: NotRequired[str]
    Domain: NotRequired[str]
    Password: NotRequired[str]
    CmkSecretConfig: NotRequired[CmkSecretConfigTypeDef]
    CustomSecretConfig: NotRequired[CustomSecretConfigTypeDef]
    AgentArns: NotRequired[Sequence[str]]
    MountOptions: NotRequired[SmbMountOptionsTypeDef]
    AuthenticationType: NotRequired[SmbAuthenticationTypeType]
    DnsIpAddresses: NotRequired[Sequence[str]]
    KerberosPrincipal: NotRequired[str]
    KerberosKeytab: NotRequired[BlobTypeDef]
    KerberosKrb5Conf: NotRequired[BlobTypeDef]

class UpdateTaskExecutionRequestTypeDef(TypedDict):
    TaskExecutionArn: str
    Options: OptionsTypeDef

class DescribeAgentResponseTypeDef(TypedDict):
    AgentArn: str
    Name: str
    Status: AgentStatusType
    LastConnectionTime: datetime
    CreationTime: datetime
    EndpointType: EndpointTypeType
    PrivateLinkConfig: PrivateLinkConfigTypeDef
    Platform: PlatformTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationAzureBlobResponseTypeDef(TypedDict):
    LocationArn: str
    LocationUri: str
    AuthenticationType: AzureBlobAuthenticationTypeType
    BlobType: Literal["BLOCK"]
    AccessTier: AzureAccessTierType
    AgentArns: List[str]
    CreationTime: datetime
    ManagedSecretConfig: ManagedSecretConfigTypeDef
    CmkSecretConfig: CmkSecretConfigTypeDef
    CustomSecretConfig: CustomSecretConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationObjectStorageResponseTypeDef(TypedDict):
    LocationArn: str
    LocationUri: str
    AccessKey: str
    ServerPort: int
    ServerProtocol: ObjectStorageServerProtocolType
    AgentArns: List[str]
    CreationTime: datetime
    ServerCertificate: bytes
    ManagedSecretConfig: ManagedSecretConfigTypeDef
    CmkSecretConfig: CmkSecretConfigTypeDef
    CustomSecretConfig: CustomSecretConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationSmbResponseTypeDef(TypedDict):
    LocationArn: str
    LocationUri: str
    AgentArns: List[str]
    User: str
    Domain: str
    MountOptions: SmbMountOptionsTypeDef
    CreationTime: datetime
    DnsIpAddresses: List[str]
    KerberosPrincipal: str
    AuthenticationType: SmbAuthenticationTypeType
    ManagedSecretConfig: ManagedSecretConfigTypeDef
    CmkSecretConfig: CmkSecretConfigTypeDef
    CustomSecretConfig: CustomSecretConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationEfsResponseTypeDef(TypedDict):
    LocationArn: str
    LocationUri: str
    Ec2Config: Ec2ConfigOutputTypeDef
    CreationTime: datetime
    AccessPointArn: str
    FileSystemAccessRoleArn: str
    InTransitEncryption: EfsInTransitEncryptionType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocationNfsResponseTypeDef(TypedDict):
    LocationArn: str
    LocationUri: str
    OnPremConfig: OnPremConfigOutputTypeDef
    MountOptions: NfsMountOptionsTypeDef
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

Ec2ConfigUnionTypeDef = Union[Ec2ConfigTypeDef, Ec2ConfigOutputTypeDef]

class ListAgentsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsForResourceRequestPaginateTypeDef(TypedDict):
    ResourceArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTaskExecutionsRequestPaginateTypeDef(TypedDict):
    TaskArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLocationsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[LocationFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLocationsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Filters: NotRequired[Sequence[LocationFilterTypeDef]]

class ListLocationsResponseTypeDef(TypedDict):
    Locations: List[LocationListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTaskExecutionsResponseTypeDef(TypedDict):
    TaskExecutions: List[TaskExecutionListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTasksRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[TaskFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTasksRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Filters: NotRequired[Sequence[TaskFilterTypeDef]]

class ListTasksResponseTypeDef(TypedDict):
    Tasks: List[TaskListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

OnPremConfigUnionTypeDef = Union[OnPremConfigTypeDef, OnPremConfigOutputTypeDef]

class ReportDestinationTypeDef(TypedDict):
    S3: NotRequired[ReportDestinationS3TypeDef]

class ReportOverridesTypeDef(TypedDict):
    Transferred: NotRequired[ReportOverrideTypeDef]
    Verified: NotRequired[ReportOverrideTypeDef]
    Deleted: NotRequired[ReportOverrideTypeDef]
    Skipped: NotRequired[ReportOverrideTypeDef]

class SourceManifestConfigTypeDef(TypedDict):
    S3: S3ManifestConfigTypeDef

class ListAgentsResponseTypeDef(TypedDict):
    Agents: List[AgentListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class FsxProtocolTypeDef(TypedDict):
    NFS: NotRequired[FsxProtocolNfsTypeDef]
    SMB: NotRequired[FsxProtocolSmbTypeDef]

class FsxUpdateProtocolTypeDef(TypedDict):
    NFS: NotRequired[FsxProtocolNfsTypeDef]
    SMB: NotRequired[FsxUpdateProtocolSmbTypeDef]

class CreateLocationEfsRequestTypeDef(TypedDict):
    EfsFilesystemArn: str
    Ec2Config: Ec2ConfigUnionTypeDef
    Subdirectory: NotRequired[str]
    Tags: NotRequired[Sequence[TagListEntryTypeDef]]
    AccessPointArn: NotRequired[str]
    FileSystemAccessRoleArn: NotRequired[str]
    InTransitEncryption: NotRequired[EfsInTransitEncryptionType]

class CreateLocationNfsRequestTypeDef(TypedDict):
    Subdirectory: str
    ServerHostname: str
    OnPremConfig: OnPremConfigUnionTypeDef
    MountOptions: NotRequired[NfsMountOptionsTypeDef]
    Tags: NotRequired[Sequence[TagListEntryTypeDef]]

class UpdateLocationNfsRequestTypeDef(TypedDict):
    LocationArn: str
    Subdirectory: NotRequired[str]
    ServerHostname: NotRequired[str]
    OnPremConfig: NotRequired[OnPremConfigUnionTypeDef]
    MountOptions: NotRequired[NfsMountOptionsTypeDef]

class TaskReportConfigTypeDef(TypedDict):
    Destination: NotRequired[ReportDestinationTypeDef]
    OutputType: NotRequired[ReportOutputTypeType]
    ReportLevel: NotRequired[ReportLevelType]
    ObjectVersionIds: NotRequired[ObjectVersionIdsType]
    Overrides: NotRequired[ReportOverridesTypeDef]

class ManifestConfigTypeDef(TypedDict):
    Action: NotRequired[Literal["TRANSFER"]]
    Format: NotRequired[Literal["CSV"]]
    Source: NotRequired[SourceManifestConfigTypeDef]

CreateLocationFsxOntapRequestTypeDef = TypedDict(
    "CreateLocationFsxOntapRequestTypeDef",
    {
        "Protocol": FsxProtocolTypeDef,
        "SecurityGroupArns": Sequence[str],
        "StorageVirtualMachineArn": str,
        "Subdirectory": NotRequired[str],
        "Tags": NotRequired[Sequence[TagListEntryTypeDef]],
    },
)
CreateLocationFsxOpenZfsRequestTypeDef = TypedDict(
    "CreateLocationFsxOpenZfsRequestTypeDef",
    {
        "FsxFilesystemArn": str,
        "Protocol": FsxProtocolTypeDef,
        "SecurityGroupArns": Sequence[str],
        "Subdirectory": NotRequired[str],
        "Tags": NotRequired[Sequence[TagListEntryTypeDef]],
    },
)
DescribeLocationFsxOntapResponseTypeDef = TypedDict(
    "DescribeLocationFsxOntapResponseTypeDef",
    {
        "CreationTime": datetime,
        "LocationArn": str,
        "LocationUri": str,
        "Protocol": FsxProtocolTypeDef,
        "SecurityGroupArns": List[str],
        "StorageVirtualMachineArn": str,
        "FsxFilesystemArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLocationFsxOpenZfsResponseTypeDef = TypedDict(
    "DescribeLocationFsxOpenZfsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "SecurityGroupArns": List[str],
        "Protocol": FsxProtocolTypeDef,
        "CreationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateLocationFsxOpenZfsRequestTypeDef = TypedDict(
    "UpdateLocationFsxOpenZfsRequestTypeDef",
    {
        "LocationArn": str,
        "Protocol": NotRequired[FsxProtocolTypeDef],
        "Subdirectory": NotRequired[str],
    },
)
UpdateLocationFsxOntapRequestTypeDef = TypedDict(
    "UpdateLocationFsxOntapRequestTypeDef",
    {
        "LocationArn": str,
        "Protocol": NotRequired[FsxUpdateProtocolTypeDef],
        "Subdirectory": NotRequired[str],
    },
)

class CreateTaskRequestTypeDef(TypedDict):
    SourceLocationArn: str
    DestinationLocationArn: str
    CloudWatchLogGroupArn: NotRequired[str]
    Name: NotRequired[str]
    Options: NotRequired[OptionsTypeDef]
    Excludes: NotRequired[Sequence[FilterRuleTypeDef]]
    Schedule: NotRequired[TaskScheduleTypeDef]
    Tags: NotRequired[Sequence[TagListEntryTypeDef]]
    Includes: NotRequired[Sequence[FilterRuleTypeDef]]
    ManifestConfig: NotRequired[ManifestConfigTypeDef]
    TaskReportConfig: NotRequired[TaskReportConfigTypeDef]
    TaskMode: NotRequired[TaskModeType]

class DescribeTaskExecutionResponseTypeDef(TypedDict):
    TaskExecutionArn: str
    Status: TaskExecutionStatusType
    Options: OptionsTypeDef
    Excludes: List[FilterRuleTypeDef]
    Includes: List[FilterRuleTypeDef]
    ManifestConfig: ManifestConfigTypeDef
    StartTime: datetime
    EstimatedFilesToTransfer: int
    EstimatedBytesToTransfer: int
    FilesTransferred: int
    BytesWritten: int
    BytesTransferred: int
    BytesCompressed: int
    Result: TaskExecutionResultDetailTypeDef
    TaskReportConfig: TaskReportConfigTypeDef
    FilesDeleted: int
    FilesSkipped: int
    FilesVerified: int
    ReportResult: ReportResultTypeDef
    EstimatedFilesToDelete: int
    TaskMode: TaskModeType
    FilesPrepared: int
    FilesListed: TaskExecutionFilesListedDetailTypeDef
    FilesFailed: TaskExecutionFilesFailedDetailTypeDef
    EstimatedFoldersToDelete: int
    EstimatedFoldersToTransfer: int
    FoldersSkipped: int
    FoldersPrepared: int
    FoldersTransferred: int
    FoldersVerified: int
    FoldersDeleted: int
    FoldersListed: TaskExecutionFoldersListedDetailTypeDef
    FoldersFailed: TaskExecutionFoldersFailedDetailTypeDef
    LaunchTime: datetime
    EndTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTaskResponseTypeDef(TypedDict):
    TaskArn: str
    Status: TaskStatusType
    Name: str
    CurrentTaskExecutionArn: str
    SourceLocationArn: str
    DestinationLocationArn: str
    CloudWatchLogGroupArn: str
    SourceNetworkInterfaceArns: List[str]
    DestinationNetworkInterfaceArns: List[str]
    Options: OptionsTypeDef
    Excludes: List[FilterRuleTypeDef]
    Schedule: TaskScheduleTypeDef
    ErrorCode: str
    ErrorDetail: str
    CreationTime: datetime
    Includes: List[FilterRuleTypeDef]
    ManifestConfig: ManifestConfigTypeDef
    TaskReportConfig: TaskReportConfigTypeDef
    ScheduleDetails: TaskScheduleDetailsTypeDef
    TaskMode: TaskModeType
    ResponseMetadata: ResponseMetadataTypeDef

class StartTaskExecutionRequestTypeDef(TypedDict):
    TaskArn: str
    OverrideOptions: NotRequired[OptionsTypeDef]
    Includes: NotRequired[Sequence[FilterRuleTypeDef]]
    Excludes: NotRequired[Sequence[FilterRuleTypeDef]]
    ManifestConfig: NotRequired[ManifestConfigTypeDef]
    TaskReportConfig: NotRequired[TaskReportConfigTypeDef]
    Tags: NotRequired[Sequence[TagListEntryTypeDef]]

class UpdateTaskRequestTypeDef(TypedDict):
    TaskArn: str
    Options: NotRequired[OptionsTypeDef]
    Excludes: NotRequired[Sequence[FilterRuleTypeDef]]
    Schedule: NotRequired[TaskScheduleTypeDef]
    Name: NotRequired[str]
    CloudWatchLogGroupArn: NotRequired[str]
    Includes: NotRequired[Sequence[FilterRuleTypeDef]]
    ManifestConfig: NotRequired[ManifestConfigTypeDef]
    TaskReportConfig: NotRequired[TaskReportConfigTypeDef]
