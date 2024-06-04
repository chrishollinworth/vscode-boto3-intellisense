"""
Type annotations for datasync service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/type_defs.html)

Usage::

    ```python
    from mypy_boto3_datasync.type_defs import AddStorageSystemRequestRequestTypeDef

    data: AddStorageSystemRequestRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AgentStatusType,
    AtimeType,
    AzureAccessTierType,
    DiscoveryJobStatusType,
    DiscoveryResourceTypeType,
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
    RecommendationStatusType,
    ReportLevelType,
    ReportOutputTypeType,
    S3StorageClassType,
    ScheduleDisabledByType,
    ScheduleStatusType,
    SmbSecurityDescriptorCopyFlagsType,
    SmbVersionType,
    StorageSystemConnectivityStatusType,
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
    "AddStorageSystemRequestRequestTypeDef",
    "AddStorageSystemResponseTypeDef",
    "AgentListEntryTypeDef",
    "AzureBlobSasConfigurationTypeDef",
    "CancelTaskExecutionRequestRequestTypeDef",
    "CapacityTypeDef",
    "CreateAgentRequestRequestTypeDef",
    "CreateAgentResponseTypeDef",
    "CreateLocationAzureBlobRequestRequestTypeDef",
    "CreateLocationAzureBlobResponseTypeDef",
    "CreateLocationEfsRequestRequestTypeDef",
    "CreateLocationEfsResponseTypeDef",
    "CreateLocationFsxLustreRequestRequestTypeDef",
    "CreateLocationFsxLustreResponseTypeDef",
    "CreateLocationFsxOntapRequestRequestTypeDef",
    "CreateLocationFsxOntapResponseTypeDef",
    "CreateLocationFsxOpenZfsRequestRequestTypeDef",
    "CreateLocationFsxOpenZfsResponseTypeDef",
    "CreateLocationFsxWindowsRequestRequestTypeDef",
    "CreateLocationFsxWindowsResponseTypeDef",
    "CreateLocationHdfsRequestRequestTypeDef",
    "CreateLocationHdfsResponseTypeDef",
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
    "CredentialsTypeDef",
    "DeleteAgentRequestRequestTypeDef",
    "DeleteLocationRequestRequestTypeDef",
    "DeleteTaskRequestRequestTypeDef",
    "DescribeAgentRequestRequestTypeDef",
    "DescribeAgentResponseTypeDef",
    "DescribeDiscoveryJobRequestRequestTypeDef",
    "DescribeDiscoveryJobResponseTypeDef",
    "DescribeLocationAzureBlobRequestRequestTypeDef",
    "DescribeLocationAzureBlobResponseTypeDef",
    "DescribeLocationEfsRequestRequestTypeDef",
    "DescribeLocationEfsResponseTypeDef",
    "DescribeLocationFsxLustreRequestRequestTypeDef",
    "DescribeLocationFsxLustreResponseTypeDef",
    "DescribeLocationFsxOntapRequestRequestTypeDef",
    "DescribeLocationFsxOntapResponseTypeDef",
    "DescribeLocationFsxOpenZfsRequestRequestTypeDef",
    "DescribeLocationFsxOpenZfsResponseTypeDef",
    "DescribeLocationFsxWindowsRequestRequestTypeDef",
    "DescribeLocationFsxWindowsResponseTypeDef",
    "DescribeLocationHdfsRequestRequestTypeDef",
    "DescribeLocationHdfsResponseTypeDef",
    "DescribeLocationNfsRequestRequestTypeDef",
    "DescribeLocationNfsResponseTypeDef",
    "DescribeLocationObjectStorageRequestRequestTypeDef",
    "DescribeLocationObjectStorageResponseTypeDef",
    "DescribeLocationS3RequestRequestTypeDef",
    "DescribeLocationS3ResponseTypeDef",
    "DescribeLocationSmbRequestRequestTypeDef",
    "DescribeLocationSmbResponseTypeDef",
    "DescribeStorageSystemRequestRequestTypeDef",
    "DescribeStorageSystemResourceMetricsRequestRequestTypeDef",
    "DescribeStorageSystemResourceMetricsResponseTypeDef",
    "DescribeStorageSystemResourcesRequestRequestTypeDef",
    "DescribeStorageSystemResourcesResponseTypeDef",
    "DescribeStorageSystemResponseTypeDef",
    "DescribeTaskExecutionRequestRequestTypeDef",
    "DescribeTaskExecutionResponseTypeDef",
    "DescribeTaskRequestRequestTypeDef",
    "DescribeTaskResponseTypeDef",
    "DiscoveryJobListEntryTypeDef",
    "DiscoveryServerConfigurationTypeDef",
    "Ec2ConfigTypeDef",
    "FilterRuleTypeDef",
    "FsxProtocolNfsTypeDef",
    "FsxProtocolSmbTypeDef",
    "FsxProtocolTypeDef",
    "GenerateRecommendationsRequestRequestTypeDef",
    "HdfsNameNodeTypeDef",
    "IOPSTypeDef",
    "LatencyTypeDef",
    "ListAgentsRequestRequestTypeDef",
    "ListAgentsResponseTypeDef",
    "ListDiscoveryJobsRequestRequestTypeDef",
    "ListDiscoveryJobsResponseTypeDef",
    "ListLocationsRequestRequestTypeDef",
    "ListLocationsResponseTypeDef",
    "ListStorageSystemsRequestRequestTypeDef",
    "ListStorageSystemsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTaskExecutionsRequestRequestTypeDef",
    "ListTaskExecutionsResponseTypeDef",
    "ListTasksRequestRequestTypeDef",
    "ListTasksResponseTypeDef",
    "LocationFilterTypeDef",
    "LocationListEntryTypeDef",
    "ManifestConfigTypeDef",
    "MaxP95PerformanceTypeDef",
    "NetAppONTAPClusterTypeDef",
    "NetAppONTAPSVMTypeDef",
    "NetAppONTAPVolumeTypeDef",
    "NfsMountOptionsTypeDef",
    "OnPremConfigTypeDef",
    "OptionsTypeDef",
    "P95MetricsTypeDef",
    "PaginatorConfigTypeDef",
    "PlatformTypeDef",
    "PrivateLinkConfigTypeDef",
    "QopConfigurationTypeDef",
    "RecommendationTypeDef",
    "RemoveStorageSystemRequestRequestTypeDef",
    "ReportDestinationS3TypeDef",
    "ReportDestinationTypeDef",
    "ReportOverrideTypeDef",
    "ReportOverridesTypeDef",
    "ReportResultTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceMetricsTypeDef",
    "ResponseMetadataTypeDef",
    "S3ConfigTypeDef",
    "S3ManifestConfigTypeDef",
    "SmbMountOptionsTypeDef",
    "SourceManifestConfigTypeDef",
    "StartDiscoveryJobRequestRequestTypeDef",
    "StartDiscoveryJobResponseTypeDef",
    "StartTaskExecutionRequestRequestTypeDef",
    "StartTaskExecutionResponseTypeDef",
    "StopDiscoveryJobRequestRequestTypeDef",
    "StorageSystemListEntryTypeDef",
    "TagListEntryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TaskExecutionListEntryTypeDef",
    "TaskExecutionResultDetailTypeDef",
    "TaskFilterTypeDef",
    "TaskListEntryTypeDef",
    "TaskReportConfigTypeDef",
    "TaskScheduleDetailsTypeDef",
    "TaskScheduleTypeDef",
    "ThroughputTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAgentRequestRequestTypeDef",
    "UpdateDiscoveryJobRequestRequestTypeDef",
    "UpdateLocationAzureBlobRequestRequestTypeDef",
    "UpdateLocationHdfsRequestRequestTypeDef",
    "UpdateLocationNfsRequestRequestTypeDef",
    "UpdateLocationObjectStorageRequestRequestTypeDef",
    "UpdateLocationSmbRequestRequestTypeDef",
    "UpdateStorageSystemRequestRequestTypeDef",
    "UpdateTaskExecutionRequestRequestTypeDef",
    "UpdateTaskRequestRequestTypeDef",
)

_RequiredAddStorageSystemRequestRequestTypeDef = TypedDict(
    "_RequiredAddStorageSystemRequestRequestTypeDef",
    {
        "ServerConfiguration": "DiscoveryServerConfigurationTypeDef",
        "SystemType": Literal["NetAppONTAP"],
        "AgentArns": List[str],
        "ClientToken": str,
        "Credentials": "CredentialsTypeDef",
    },
)
_OptionalAddStorageSystemRequestRequestTypeDef = TypedDict(
    "_OptionalAddStorageSystemRequestRequestTypeDef",
    {
        "CloudWatchLogGroupArn": str,
        "Tags": List["TagListEntryTypeDef"],
        "Name": str,
    },
    total=False,
)

class AddStorageSystemRequestRequestTypeDef(
    _RequiredAddStorageSystemRequestRequestTypeDef, _OptionalAddStorageSystemRequestRequestTypeDef
):
    pass

AddStorageSystemResponseTypeDef = TypedDict(
    "AddStorageSystemResponseTypeDef",
    {
        "StorageSystemArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AgentListEntryTypeDef = TypedDict(
    "AgentListEntryTypeDef",
    {
        "AgentArn": str,
        "Name": str,
        "Status": AgentStatusType,
        "Platform": "PlatformTypeDef",
    },
    total=False,
)

AzureBlobSasConfigurationTypeDef = TypedDict(
    "AzureBlobSasConfigurationTypeDef",
    {
        "Token": str,
    },
)

CancelTaskExecutionRequestRequestTypeDef = TypedDict(
    "CancelTaskExecutionRequestRequestTypeDef",
    {
        "TaskExecutionArn": str,
    },
)

CapacityTypeDef = TypedDict(
    "CapacityTypeDef",
    {
        "Used": int,
        "Provisioned": int,
        "LogicalUsed": int,
        "ClusterCloudStorageUsed": int,
    },
    total=False,
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

_RequiredCreateLocationAzureBlobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationAzureBlobRequestRequestTypeDef",
    {
        "ContainerUrl": str,
        "AuthenticationType": Literal["SAS"],
        "AgentArns": List[str],
    },
)
_OptionalCreateLocationAzureBlobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationAzureBlobRequestRequestTypeDef",
    {
        "SasConfiguration": "AzureBlobSasConfigurationTypeDef",
        "BlobType": Literal["BLOCK"],
        "AccessTier": AzureAccessTierType,
        "Subdirectory": str,
        "Tags": List["TagListEntryTypeDef"],
    },
    total=False,
)

class CreateLocationAzureBlobRequestRequestTypeDef(
    _RequiredCreateLocationAzureBlobRequestRequestTypeDef,
    _OptionalCreateLocationAzureBlobRequestRequestTypeDef,
):
    pass

CreateLocationAzureBlobResponseTypeDef = TypedDict(
    "CreateLocationAzureBlobResponseTypeDef",
    {
        "LocationArn": str,
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
        "AccessPointArn": str,
        "FileSystemAccessRoleArn": str,
        "InTransitEncryption": EfsInTransitEncryptionType,
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

_RequiredCreateLocationFsxLustreRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationFsxLustreRequestRequestTypeDef",
    {
        "FsxFilesystemArn": str,
        "SecurityGroupArns": List[str],
    },
)
_OptionalCreateLocationFsxLustreRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationFsxLustreRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "Tags": List["TagListEntryTypeDef"],
    },
    total=False,
)

class CreateLocationFsxLustreRequestRequestTypeDef(
    _RequiredCreateLocationFsxLustreRequestRequestTypeDef,
    _OptionalCreateLocationFsxLustreRequestRequestTypeDef,
):
    pass

CreateLocationFsxLustreResponseTypeDef = TypedDict(
    "CreateLocationFsxLustreResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLocationFsxOntapRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationFsxOntapRequestRequestTypeDef",
    {
        "Protocol": "FsxProtocolTypeDef",
        "SecurityGroupArns": List[str],
        "StorageVirtualMachineArn": str,
    },
)
_OptionalCreateLocationFsxOntapRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationFsxOntapRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "Tags": List["TagListEntryTypeDef"],
    },
    total=False,
)

class CreateLocationFsxOntapRequestRequestTypeDef(
    _RequiredCreateLocationFsxOntapRequestRequestTypeDef,
    _OptionalCreateLocationFsxOntapRequestRequestTypeDef,
):
    pass

CreateLocationFsxOntapResponseTypeDef = TypedDict(
    "CreateLocationFsxOntapResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLocationFsxOpenZfsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationFsxOpenZfsRequestRequestTypeDef",
    {
        "FsxFilesystemArn": str,
        "Protocol": "FsxProtocolTypeDef",
        "SecurityGroupArns": List[str],
    },
)
_OptionalCreateLocationFsxOpenZfsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationFsxOpenZfsRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "Tags": List["TagListEntryTypeDef"],
    },
    total=False,
)

class CreateLocationFsxOpenZfsRequestRequestTypeDef(
    _RequiredCreateLocationFsxOpenZfsRequestRequestTypeDef,
    _OptionalCreateLocationFsxOpenZfsRequestRequestTypeDef,
):
    pass

CreateLocationFsxOpenZfsResponseTypeDef = TypedDict(
    "CreateLocationFsxOpenZfsResponseTypeDef",
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

_RequiredCreateLocationHdfsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationHdfsRequestRequestTypeDef",
    {
        "NameNodes": List["HdfsNameNodeTypeDef"],
        "AuthenticationType": HdfsAuthenticationTypeType,
        "AgentArns": List[str],
    },
)
_OptionalCreateLocationHdfsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationHdfsRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "BlockSize": int,
        "ReplicationFactor": int,
        "KmsKeyProviderUri": str,
        "QopConfiguration": "QopConfigurationTypeDef",
        "SimpleUser": str,
        "KerberosPrincipal": str,
        "KerberosKeytab": Union[bytes, IO[bytes], StreamingBody],
        "KerberosKrb5Conf": Union[bytes, IO[bytes], StreamingBody],
        "Tags": List["TagListEntryTypeDef"],
    },
    total=False,
)

class CreateLocationHdfsRequestRequestTypeDef(
    _RequiredCreateLocationHdfsRequestRequestTypeDef,
    _OptionalCreateLocationHdfsRequestRequestTypeDef,
):
    pass

CreateLocationHdfsResponseTypeDef = TypedDict(
    "CreateLocationHdfsResponseTypeDef",
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
        "ServerCertificate": Union[bytes, IO[bytes], StreamingBody],
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
        "Includes": List["FilterRuleTypeDef"],
        "ManifestConfig": "ManifestConfigTypeDef",
        "TaskReportConfig": "TaskReportConfigTypeDef",
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

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "Username": str,
        "Password": str,
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
        "Platform": "PlatformTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDiscoveryJobRequestRequestTypeDef = TypedDict(
    "DescribeDiscoveryJobRequestRequestTypeDef",
    {
        "DiscoveryJobArn": str,
    },
)

DescribeDiscoveryJobResponseTypeDef = TypedDict(
    "DescribeDiscoveryJobResponseTypeDef",
    {
        "StorageSystemArn": str,
        "DiscoveryJobArn": str,
        "CollectionDurationMinutes": int,
        "Status": DiscoveryJobStatusType,
        "JobStartTime": datetime,
        "JobEndTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationAzureBlobRequestRequestTypeDef = TypedDict(
    "DescribeLocationAzureBlobRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationAzureBlobResponseTypeDef = TypedDict(
    "DescribeLocationAzureBlobResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "AuthenticationType": Literal["SAS"],
        "BlobType": Literal["BLOCK"],
        "AccessTier": AzureAccessTierType,
        "AgentArns": List[str],
        "CreationTime": datetime,
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
        "AccessPointArn": str,
        "FileSystemAccessRoleArn": str,
        "InTransitEncryption": EfsInTransitEncryptionType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationFsxLustreRequestRequestTypeDef = TypedDict(
    "DescribeLocationFsxLustreRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationFsxLustreResponseTypeDef = TypedDict(
    "DescribeLocationFsxLustreResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "SecurityGroupArns": List[str],
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationFsxOntapRequestRequestTypeDef = TypedDict(
    "DescribeLocationFsxOntapRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationFsxOntapResponseTypeDef = TypedDict(
    "DescribeLocationFsxOntapResponseTypeDef",
    {
        "CreationTime": datetime,
        "LocationArn": str,
        "LocationUri": str,
        "Protocol": "FsxProtocolTypeDef",
        "SecurityGroupArns": List[str],
        "StorageVirtualMachineArn": str,
        "FsxFilesystemArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationFsxOpenZfsRequestRequestTypeDef = TypedDict(
    "DescribeLocationFsxOpenZfsRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationFsxOpenZfsResponseTypeDef = TypedDict(
    "DescribeLocationFsxOpenZfsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "SecurityGroupArns": List[str],
        "Protocol": "FsxProtocolTypeDef",
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

DescribeLocationHdfsRequestRequestTypeDef = TypedDict(
    "DescribeLocationHdfsRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationHdfsResponseTypeDef = TypedDict(
    "DescribeLocationHdfsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "NameNodes": List["HdfsNameNodeTypeDef"],
        "BlockSize": int,
        "ReplicationFactor": int,
        "KmsKeyProviderUri": str,
        "QopConfiguration": "QopConfigurationTypeDef",
        "AuthenticationType": HdfsAuthenticationTypeType,
        "SimpleUser": str,
        "KerberosPrincipal": str,
        "AgentArns": List[str],
        "CreationTime": datetime,
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
        "ServerCertificate": bytes,
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

DescribeStorageSystemRequestRequestTypeDef = TypedDict(
    "DescribeStorageSystemRequestRequestTypeDef",
    {
        "StorageSystemArn": str,
    },
)

_RequiredDescribeStorageSystemResourceMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeStorageSystemResourceMetricsRequestRequestTypeDef",
    {
        "DiscoveryJobArn": str,
        "ResourceType": DiscoveryResourceTypeType,
        "ResourceId": str,
    },
)
_OptionalDescribeStorageSystemResourceMetricsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeStorageSystemResourceMetricsRequestRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeStorageSystemResourceMetricsRequestRequestTypeDef(
    _RequiredDescribeStorageSystemResourceMetricsRequestRequestTypeDef,
    _OptionalDescribeStorageSystemResourceMetricsRequestRequestTypeDef,
):
    pass

DescribeStorageSystemResourceMetricsResponseTypeDef = TypedDict(
    "DescribeStorageSystemResourceMetricsResponseTypeDef",
    {
        "Metrics": List["ResourceMetricsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeStorageSystemResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeStorageSystemResourcesRequestRequestTypeDef",
    {
        "DiscoveryJobArn": str,
        "ResourceType": DiscoveryResourceTypeType,
    },
)
_OptionalDescribeStorageSystemResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeStorageSystemResourcesRequestRequestTypeDef",
    {
        "ResourceIds": List[str],
        "Filter": Dict[Literal["SVM"], List[str]],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeStorageSystemResourcesRequestRequestTypeDef(
    _RequiredDescribeStorageSystemResourcesRequestRequestTypeDef,
    _OptionalDescribeStorageSystemResourcesRequestRequestTypeDef,
):
    pass

DescribeStorageSystemResourcesResponseTypeDef = TypedDict(
    "DescribeStorageSystemResourcesResponseTypeDef",
    {
        "ResourceDetails": "ResourceDetailsTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStorageSystemResponseTypeDef = TypedDict(
    "DescribeStorageSystemResponseTypeDef",
    {
        "StorageSystemArn": str,
        "ServerConfiguration": "DiscoveryServerConfigurationTypeDef",
        "SystemType": Literal["NetAppONTAP"],
        "AgentArns": List[str],
        "Name": str,
        "ErrorMessage": str,
        "ConnectivityStatus": StorageSystemConnectivityStatusType,
        "CloudWatchLogGroupArn": str,
        "CreationTime": datetime,
        "SecretsManagerArn": str,
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
        "ManifestConfig": "ManifestConfigTypeDef",
        "StartTime": datetime,
        "EstimatedFilesToTransfer": int,
        "EstimatedBytesToTransfer": int,
        "FilesTransferred": int,
        "BytesWritten": int,
        "BytesTransferred": int,
        "BytesCompressed": int,
        "Result": "TaskExecutionResultDetailTypeDef",
        "TaskReportConfig": "TaskReportConfigTypeDef",
        "FilesDeleted": int,
        "FilesSkipped": int,
        "FilesVerified": int,
        "ReportResult": "ReportResultTypeDef",
        "EstimatedFilesToDelete": int,
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
        "Includes": List["FilterRuleTypeDef"],
        "ManifestConfig": "ManifestConfigTypeDef",
        "TaskReportConfig": "TaskReportConfigTypeDef",
        "ScheduleDetails": "TaskScheduleDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DiscoveryJobListEntryTypeDef = TypedDict(
    "DiscoveryJobListEntryTypeDef",
    {
        "DiscoveryJobArn": str,
        "Status": DiscoveryJobStatusType,
    },
    total=False,
)

_RequiredDiscoveryServerConfigurationTypeDef = TypedDict(
    "_RequiredDiscoveryServerConfigurationTypeDef",
    {
        "ServerHostname": str,
    },
)
_OptionalDiscoveryServerConfigurationTypeDef = TypedDict(
    "_OptionalDiscoveryServerConfigurationTypeDef",
    {
        "ServerPort": int,
    },
    total=False,
)

class DiscoveryServerConfigurationTypeDef(
    _RequiredDiscoveryServerConfigurationTypeDef, _OptionalDiscoveryServerConfigurationTypeDef
):
    pass

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

FsxProtocolNfsTypeDef = TypedDict(
    "FsxProtocolNfsTypeDef",
    {
        "MountOptions": "NfsMountOptionsTypeDef",
    },
    total=False,
)

_RequiredFsxProtocolSmbTypeDef = TypedDict(
    "_RequiredFsxProtocolSmbTypeDef",
    {
        "Password": str,
        "User": str,
    },
)
_OptionalFsxProtocolSmbTypeDef = TypedDict(
    "_OptionalFsxProtocolSmbTypeDef",
    {
        "Domain": str,
        "MountOptions": "SmbMountOptionsTypeDef",
    },
    total=False,
)

class FsxProtocolSmbTypeDef(_RequiredFsxProtocolSmbTypeDef, _OptionalFsxProtocolSmbTypeDef):
    pass

FsxProtocolTypeDef = TypedDict(
    "FsxProtocolTypeDef",
    {
        "NFS": "FsxProtocolNfsTypeDef",
        "SMB": "FsxProtocolSmbTypeDef",
    },
    total=False,
)

GenerateRecommendationsRequestRequestTypeDef = TypedDict(
    "GenerateRecommendationsRequestRequestTypeDef",
    {
        "DiscoveryJobArn": str,
        "ResourceIds": List[str],
        "ResourceType": DiscoveryResourceTypeType,
    },
)

HdfsNameNodeTypeDef = TypedDict(
    "HdfsNameNodeTypeDef",
    {
        "Hostname": str,
        "Port": int,
    },
)

IOPSTypeDef = TypedDict(
    "IOPSTypeDef",
    {
        "Read": float,
        "Write": float,
        "Other": float,
        "Total": float,
    },
    total=False,
)

LatencyTypeDef = TypedDict(
    "LatencyTypeDef",
    {
        "Read": float,
        "Write": float,
        "Other": float,
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

ListDiscoveryJobsRequestRequestTypeDef = TypedDict(
    "ListDiscoveryJobsRequestRequestTypeDef",
    {
        "StorageSystemArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListDiscoveryJobsResponseTypeDef = TypedDict(
    "ListDiscoveryJobsResponseTypeDef",
    {
        "DiscoveryJobs": List["DiscoveryJobListEntryTypeDef"],
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

ListStorageSystemsRequestRequestTypeDef = TypedDict(
    "ListStorageSystemsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListStorageSystemsResponseTypeDef = TypedDict(
    "ListStorageSystemsResponseTypeDef",
    {
        "StorageSystems": List["StorageSystemListEntryTypeDef"],
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

ManifestConfigTypeDef = TypedDict(
    "ManifestConfigTypeDef",
    {
        "Action": Literal["TRANSFER"],
        "Format": Literal["CSV"],
        "Source": "SourceManifestConfigTypeDef",
    },
    total=False,
)

MaxP95PerformanceTypeDef = TypedDict(
    "MaxP95PerformanceTypeDef",
    {
        "IopsRead": float,
        "IopsWrite": float,
        "IopsOther": float,
        "IopsTotal": float,
        "ThroughputRead": float,
        "ThroughputWrite": float,
        "ThroughputOther": float,
        "ThroughputTotal": float,
        "LatencyRead": float,
        "LatencyWrite": float,
        "LatencyOther": float,
    },
    total=False,
)

NetAppONTAPClusterTypeDef = TypedDict(
    "NetAppONTAPClusterTypeDef",
    {
        "CifsShareCount": int,
        "NfsExportedVolumes": int,
        "ResourceId": str,
        "ClusterName": str,
        "MaxP95Performance": "MaxP95PerformanceTypeDef",
        "ClusterBlockStorageSize": int,
        "ClusterBlockStorageUsed": int,
        "ClusterBlockStorageLogicalUsed": int,
        "Recommendations": List["RecommendationTypeDef"],
        "RecommendationStatus": RecommendationStatusType,
        "LunCount": int,
        "ClusterCloudStorageUsed": int,
    },
    total=False,
)

NetAppONTAPSVMTypeDef = TypedDict(
    "NetAppONTAPSVMTypeDef",
    {
        "ClusterUuid": str,
        "ResourceId": str,
        "SvmName": str,
        "CifsShareCount": int,
        "EnabledProtocols": List[str],
        "TotalCapacityUsed": int,
        "TotalCapacityProvisioned": int,
        "TotalLogicalCapacityUsed": int,
        "MaxP95Performance": "MaxP95PerformanceTypeDef",
        "Recommendations": List["RecommendationTypeDef"],
        "NfsExportedVolumes": int,
        "RecommendationStatus": RecommendationStatusType,
        "TotalSnapshotCapacityUsed": int,
        "LunCount": int,
    },
    total=False,
)

NetAppONTAPVolumeTypeDef = TypedDict(
    "NetAppONTAPVolumeTypeDef",
    {
        "VolumeName": str,
        "ResourceId": str,
        "CifsShareCount": int,
        "SecurityStyle": str,
        "SvmUuid": str,
        "SvmName": str,
        "CapacityUsed": int,
        "CapacityProvisioned": int,
        "LogicalCapacityUsed": int,
        "NfsExported": bool,
        "SnapshotCapacityUsed": int,
        "MaxP95Performance": "MaxP95PerformanceTypeDef",
        "Recommendations": List["RecommendationTypeDef"],
        "RecommendationStatus": RecommendationStatusType,
        "LunCount": int,
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
        "ObjectTags": ObjectTagsType,
    },
    total=False,
)

P95MetricsTypeDef = TypedDict(
    "P95MetricsTypeDef",
    {
        "IOPS": "IOPSTypeDef",
        "Throughput": "ThroughputTypeDef",
        "Latency": "LatencyTypeDef",
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

PlatformTypeDef = TypedDict(
    "PlatformTypeDef",
    {
        "Version": str,
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

QopConfigurationTypeDef = TypedDict(
    "QopConfigurationTypeDef",
    {
        "RpcProtection": HdfsRpcProtectionType,
        "DataTransferProtection": HdfsDataTransferProtectionType,
    },
    total=False,
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "StorageType": str,
        "StorageConfiguration": Dict[str, str],
        "EstimatedMonthlyStorageCost": str,
    },
    total=False,
)

RemoveStorageSystemRequestRequestTypeDef = TypedDict(
    "RemoveStorageSystemRequestRequestTypeDef",
    {
        "StorageSystemArn": str,
    },
)

_RequiredReportDestinationS3TypeDef = TypedDict(
    "_RequiredReportDestinationS3TypeDef",
    {
        "S3BucketArn": str,
        "BucketAccessRoleArn": str,
    },
)
_OptionalReportDestinationS3TypeDef = TypedDict(
    "_OptionalReportDestinationS3TypeDef",
    {
        "Subdirectory": str,
    },
    total=False,
)

class ReportDestinationS3TypeDef(
    _RequiredReportDestinationS3TypeDef, _OptionalReportDestinationS3TypeDef
):
    pass

ReportDestinationTypeDef = TypedDict(
    "ReportDestinationTypeDef",
    {
        "S3": "ReportDestinationS3TypeDef",
    },
    total=False,
)

ReportOverrideTypeDef = TypedDict(
    "ReportOverrideTypeDef",
    {
        "ReportLevel": ReportLevelType,
    },
    total=False,
)

ReportOverridesTypeDef = TypedDict(
    "ReportOverridesTypeDef",
    {
        "Transferred": "ReportOverrideTypeDef",
        "Verified": "ReportOverrideTypeDef",
        "Deleted": "ReportOverrideTypeDef",
        "Skipped": "ReportOverrideTypeDef",
    },
    total=False,
)

ReportResultTypeDef = TypedDict(
    "ReportResultTypeDef",
    {
        "Status": PhaseStatusType,
        "ErrorCode": str,
        "ErrorDetail": str,
    },
    total=False,
)

ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "NetAppONTAPSVMs": List["NetAppONTAPSVMTypeDef"],
        "NetAppONTAPVolumes": List["NetAppONTAPVolumeTypeDef"],
        "NetAppONTAPClusters": List["NetAppONTAPClusterTypeDef"],
    },
    total=False,
)

ResourceMetricsTypeDef = TypedDict(
    "ResourceMetricsTypeDef",
    {
        "Timestamp": datetime,
        "P95Metrics": "P95MetricsTypeDef",
        "Capacity": "CapacityTypeDef",
        "ResourceId": str,
        "ResourceType": DiscoveryResourceTypeType,
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

_RequiredS3ManifestConfigTypeDef = TypedDict(
    "_RequiredS3ManifestConfigTypeDef",
    {
        "ManifestObjectPath": str,
        "BucketAccessRoleArn": str,
        "S3BucketArn": str,
    },
)
_OptionalS3ManifestConfigTypeDef = TypedDict(
    "_OptionalS3ManifestConfigTypeDef",
    {
        "ManifestObjectVersionId": str,
    },
    total=False,
)

class S3ManifestConfigTypeDef(_RequiredS3ManifestConfigTypeDef, _OptionalS3ManifestConfigTypeDef):
    pass

SmbMountOptionsTypeDef = TypedDict(
    "SmbMountOptionsTypeDef",
    {
        "Version": SmbVersionType,
    },
    total=False,
)

SourceManifestConfigTypeDef = TypedDict(
    "SourceManifestConfigTypeDef",
    {
        "S3": "S3ManifestConfigTypeDef",
    },
)

_RequiredStartDiscoveryJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartDiscoveryJobRequestRequestTypeDef",
    {
        "StorageSystemArn": str,
        "CollectionDurationMinutes": int,
        "ClientToken": str,
    },
)
_OptionalStartDiscoveryJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartDiscoveryJobRequestRequestTypeDef",
    {
        "Tags": List["TagListEntryTypeDef"],
    },
    total=False,
)

class StartDiscoveryJobRequestRequestTypeDef(
    _RequiredStartDiscoveryJobRequestRequestTypeDef, _OptionalStartDiscoveryJobRequestRequestTypeDef
):
    pass

StartDiscoveryJobResponseTypeDef = TypedDict(
    "StartDiscoveryJobResponseTypeDef",
    {
        "DiscoveryJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "Excludes": List["FilterRuleTypeDef"],
        "ManifestConfig": "ManifestConfigTypeDef",
        "TaskReportConfig": "TaskReportConfigTypeDef",
        "Tags": List["TagListEntryTypeDef"],
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

StopDiscoveryJobRequestRequestTypeDef = TypedDict(
    "StopDiscoveryJobRequestRequestTypeDef",
    {
        "DiscoveryJobArn": str,
    },
)

StorageSystemListEntryTypeDef = TypedDict(
    "StorageSystemListEntryTypeDef",
    {
        "StorageSystemArn": str,
        "Name": str,
    },
    total=False,
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

TaskReportConfigTypeDef = TypedDict(
    "TaskReportConfigTypeDef",
    {
        "Destination": "ReportDestinationTypeDef",
        "OutputType": ReportOutputTypeType,
        "ReportLevel": ReportLevelType,
        "ObjectVersionIds": ObjectVersionIdsType,
        "Overrides": "ReportOverridesTypeDef",
    },
    total=False,
)

TaskScheduleDetailsTypeDef = TypedDict(
    "TaskScheduleDetailsTypeDef",
    {
        "StatusUpdateTime": datetime,
        "DisabledReason": str,
        "DisabledBy": ScheduleDisabledByType,
    },
    total=False,
)

_RequiredTaskScheduleTypeDef = TypedDict(
    "_RequiredTaskScheduleTypeDef",
    {
        "ScheduleExpression": str,
    },
)
_OptionalTaskScheduleTypeDef = TypedDict(
    "_OptionalTaskScheduleTypeDef",
    {
        "Status": ScheduleStatusType,
    },
    total=False,
)

class TaskScheduleTypeDef(_RequiredTaskScheduleTypeDef, _OptionalTaskScheduleTypeDef):
    pass

ThroughputTypeDef = TypedDict(
    "ThroughputTypeDef",
    {
        "Read": float,
        "Write": float,
        "Other": float,
        "Total": float,
    },
    total=False,
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

UpdateDiscoveryJobRequestRequestTypeDef = TypedDict(
    "UpdateDiscoveryJobRequestRequestTypeDef",
    {
        "DiscoveryJobArn": str,
        "CollectionDurationMinutes": int,
    },
)

_RequiredUpdateLocationAzureBlobRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLocationAzureBlobRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)
_OptionalUpdateLocationAzureBlobRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLocationAzureBlobRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "AuthenticationType": Literal["SAS"],
        "SasConfiguration": "AzureBlobSasConfigurationTypeDef",
        "BlobType": Literal["BLOCK"],
        "AccessTier": AzureAccessTierType,
        "AgentArns": List[str],
    },
    total=False,
)

class UpdateLocationAzureBlobRequestRequestTypeDef(
    _RequiredUpdateLocationAzureBlobRequestRequestTypeDef,
    _OptionalUpdateLocationAzureBlobRequestRequestTypeDef,
):
    pass

_RequiredUpdateLocationHdfsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLocationHdfsRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)
_OptionalUpdateLocationHdfsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLocationHdfsRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "NameNodes": List["HdfsNameNodeTypeDef"],
        "BlockSize": int,
        "ReplicationFactor": int,
        "KmsKeyProviderUri": str,
        "QopConfiguration": "QopConfigurationTypeDef",
        "AuthenticationType": HdfsAuthenticationTypeType,
        "SimpleUser": str,
        "KerberosPrincipal": str,
        "KerberosKeytab": Union[bytes, IO[bytes], StreamingBody],
        "KerberosKrb5Conf": Union[bytes, IO[bytes], StreamingBody],
        "AgentArns": List[str],
    },
    total=False,
)

class UpdateLocationHdfsRequestRequestTypeDef(
    _RequiredUpdateLocationHdfsRequestRequestTypeDef,
    _OptionalUpdateLocationHdfsRequestRequestTypeDef,
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
        "ServerCertificate": Union[bytes, IO[bytes], StreamingBody],
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

_RequiredUpdateStorageSystemRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStorageSystemRequestRequestTypeDef",
    {
        "StorageSystemArn": str,
    },
)
_OptionalUpdateStorageSystemRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStorageSystemRequestRequestTypeDef",
    {
        "ServerConfiguration": "DiscoveryServerConfigurationTypeDef",
        "AgentArns": List[str],
        "Name": str,
        "CloudWatchLogGroupArn": str,
        "Credentials": "CredentialsTypeDef",
    },
    total=False,
)

class UpdateStorageSystemRequestRequestTypeDef(
    _RequiredUpdateStorageSystemRequestRequestTypeDef,
    _OptionalUpdateStorageSystemRequestRequestTypeDef,
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
        "Includes": List["FilterRuleTypeDef"],
        "ManifestConfig": "ManifestConfigTypeDef",
        "TaskReportConfig": "TaskReportConfigTypeDef",
    },
    total=False,
)

class UpdateTaskRequestRequestTypeDef(
    _RequiredUpdateTaskRequestRequestTypeDef, _OptionalUpdateTaskRequestRequestTypeDef
):
    pass
