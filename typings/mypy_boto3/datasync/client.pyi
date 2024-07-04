"""
Type annotations for datasync service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_datasync import DataSyncClient

    client: DataSyncClient = boto3.client("datasync")
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import (
    AzureAccessTierType,
    DiscoveryResourceTypeType,
    EfsInTransitEncryptionType,
    HdfsAuthenticationTypeType,
    ObjectStorageServerProtocolType,
    S3StorageClassType,
)
from .paginator import (
    DescribeStorageSystemResourceMetricsPaginator,
    ListAgentsPaginator,
    ListDiscoveryJobsPaginator,
    ListLocationsPaginator,
    ListStorageSystemsPaginator,
    ListTagsForResourcePaginator,
    ListTaskExecutionsPaginator,
    ListTasksPaginator,
)
from .type_defs import (
    AddStorageSystemResponseTypeDef,
    AzureBlobSasConfigurationTypeDef,
    CreateAgentResponseTypeDef,
    CreateLocationAzureBlobResponseTypeDef,
    CreateLocationEfsResponseTypeDef,
    CreateLocationFsxLustreResponseTypeDef,
    CreateLocationFsxOntapResponseTypeDef,
    CreateLocationFsxOpenZfsResponseTypeDef,
    CreateLocationFsxWindowsResponseTypeDef,
    CreateLocationHdfsResponseTypeDef,
    CreateLocationNfsResponseTypeDef,
    CreateLocationObjectStorageResponseTypeDef,
    CreateLocationS3ResponseTypeDef,
    CreateLocationSmbResponseTypeDef,
    CreateTaskResponseTypeDef,
    CredentialsTypeDef,
    DescribeAgentResponseTypeDef,
    DescribeDiscoveryJobResponseTypeDef,
    DescribeLocationAzureBlobResponseTypeDef,
    DescribeLocationEfsResponseTypeDef,
    DescribeLocationFsxLustreResponseTypeDef,
    DescribeLocationFsxOntapResponseTypeDef,
    DescribeLocationFsxOpenZfsResponseTypeDef,
    DescribeLocationFsxWindowsResponseTypeDef,
    DescribeLocationHdfsResponseTypeDef,
    DescribeLocationNfsResponseTypeDef,
    DescribeLocationObjectStorageResponseTypeDef,
    DescribeLocationS3ResponseTypeDef,
    DescribeLocationSmbResponseTypeDef,
    DescribeStorageSystemResourceMetricsResponseTypeDef,
    DescribeStorageSystemResourcesResponseTypeDef,
    DescribeStorageSystemResponseTypeDef,
    DescribeTaskExecutionResponseTypeDef,
    DescribeTaskResponseTypeDef,
    DiscoveryServerConfigurationTypeDef,
    Ec2ConfigTypeDef,
    FilterRuleTypeDef,
    FsxProtocolTypeDef,
    HdfsNameNodeTypeDef,
    ListAgentsResponseTypeDef,
    ListDiscoveryJobsResponseTypeDef,
    ListLocationsResponseTypeDef,
    ListStorageSystemsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTaskExecutionsResponseTypeDef,
    ListTasksResponseTypeDef,
    LocationFilterTypeDef,
    ManifestConfigTypeDef,
    NfsMountOptionsTypeDef,
    OnPremConfigTypeDef,
    OptionsTypeDef,
    QopConfigurationTypeDef,
    S3ConfigTypeDef,
    SmbMountOptionsTypeDef,
    StartDiscoveryJobResponseTypeDef,
    StartTaskExecutionResponseTypeDef,
    TagListEntryTypeDef,
    TaskFilterTypeDef,
    TaskReportConfigTypeDef,
    TaskScheduleTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("DataSyncClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]

class DataSyncClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DataSyncClient exceptions.
        """

    def add_storage_system(
        self,
        *,
        ServerConfiguration: "DiscoveryServerConfigurationTypeDef",
        SystemType: Literal["NetAppONTAP"],
        AgentArns: List[str],
        ClientToken: str,
        Credentials: "CredentialsTypeDef",
        CloudWatchLogGroupArn: str = None,
        Tags: List["TagListEntryTypeDef"] = None,
        Name: str = None
    ) -> AddStorageSystemResponseTypeDef:
        """
        Creates an Amazon Web Services resource for an on-premises storage system that
        you want DataSync Discovery to collect information about.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.add_storage_system)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#add_storage_system)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#can_paginate)
        """

    def cancel_task_execution(self, *, TaskExecutionArn: str) -> Dict[str, Any]:
        """
        Stops an DataSync task execution that's in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.cancel_task_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#cancel_task_execution)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#close)
        """

    def create_agent(
        self,
        *,
        ActivationKey: str,
        AgentName: str = None,
        Tags: List["TagListEntryTypeDef"] = None,
        VpcEndpointId: str = None,
        SubnetArns: List[str] = None,
        SecurityGroupArns: List[str] = None
    ) -> CreateAgentResponseTypeDef:
        """
        Activates an DataSync agent that you've deployed in your storage environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.create_agent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#create_agent)
        """

    def create_location_azure_blob(
        self,
        *,
        ContainerUrl: str,
        AuthenticationType: Literal["SAS"],
        AgentArns: List[str],
        SasConfiguration: "AzureBlobSasConfigurationTypeDef" = None,
        BlobType: Literal["BLOCK"] = None,
        AccessTier: AzureAccessTierType = None,
        Subdirectory: str = None,
        Tags: List["TagListEntryTypeDef"] = None
    ) -> CreateLocationAzureBlobResponseTypeDef:
        """
        Creates a transfer *location* for a Microsoft Azure Blob Storage container.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.create_location_azure_blob)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#create_location_azure_blob)
        """

    def create_location_efs(
        self,
        *,
        EfsFilesystemArn: str,
        Ec2Config: "Ec2ConfigTypeDef",
        Subdirectory: str = None,
        Tags: List["TagListEntryTypeDef"] = None,
        AccessPointArn: str = None,
        FileSystemAccessRoleArn: str = None,
        InTransitEncryption: EfsInTransitEncryptionType = None
    ) -> CreateLocationEfsResponseTypeDef:
        """
        Creates a transfer *location* for an Amazon EFS file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.create_location_efs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#create_location_efs)
        """

    def create_location_fsx_lustre(
        self,
        *,
        FsxFilesystemArn: str,
        SecurityGroupArns: List[str],
        Subdirectory: str = None,
        Tags: List["TagListEntryTypeDef"] = None
    ) -> CreateLocationFsxLustreResponseTypeDef:
        """
        Creates a transfer *location* for an Amazon FSx for Lustre file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.create_location_fsx_lustre)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#create_location_fsx_lustre)
        """

    def create_location_fsx_ontap(
        self,
        *,
        Protocol: "FsxProtocolTypeDef",
        SecurityGroupArns: List[str],
        StorageVirtualMachineArn: str,
        Subdirectory: str = None,
        Tags: List["TagListEntryTypeDef"] = None
    ) -> CreateLocationFsxOntapResponseTypeDef:
        """
        Creates a transfer *location* for an Amazon FSx for NetApp ONTAP file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.create_location_fsx_ontap)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#create_location_fsx_ontap)
        """

    def create_location_fsx_open_zfs(
        self,
        *,
        FsxFilesystemArn: str,
        Protocol: "FsxProtocolTypeDef",
        SecurityGroupArns: List[str],
        Subdirectory: str = None,
        Tags: List["TagListEntryTypeDef"] = None
    ) -> CreateLocationFsxOpenZfsResponseTypeDef:
        """
        Creates a transfer *location* for an Amazon FSx for OpenZFS file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.create_location_fsx_open_zfs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#create_location_fsx_open_zfs)
        """

    def create_location_fsx_windows(
        self,
        *,
        FsxFilesystemArn: str,
        SecurityGroupArns: List[str],
        User: str,
        Password: str,
        Subdirectory: str = None,
        Tags: List["TagListEntryTypeDef"] = None,
        Domain: str = None
    ) -> CreateLocationFsxWindowsResponseTypeDef:
        """
        Creates a transfer *location* for an Amazon FSx for Windows File Server file
        system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.create_location_fsx_windows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#create_location_fsx_windows)
        """

    def create_location_hdfs(
        self,
        *,
        NameNodes: List["HdfsNameNodeTypeDef"],
        AuthenticationType: HdfsAuthenticationTypeType,
        AgentArns: List[str],
        Subdirectory: str = None,
        BlockSize: int = None,
        ReplicationFactor: int = None,
        KmsKeyProviderUri: str = None,
        QopConfiguration: "QopConfigurationTypeDef" = None,
        SimpleUser: str = None,
        KerberosPrincipal: str = None,
        KerberosKeytab: Union[bytes, IO[bytes], StreamingBody] = None,
        KerberosKrb5Conf: Union[bytes, IO[bytes], StreamingBody] = None,
        Tags: List["TagListEntryTypeDef"] = None
    ) -> CreateLocationHdfsResponseTypeDef:
        """
        Creates a transfer *location* for a Hadoop Distributed File System (HDFS).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.create_location_hdfs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#create_location_hdfs)
        """

    def create_location_nfs(
        self,
        *,
        Subdirectory: str,
        ServerHostname: str,
        OnPremConfig: "OnPremConfigTypeDef",
        MountOptions: "NfsMountOptionsTypeDef" = None,
        Tags: List["TagListEntryTypeDef"] = None
    ) -> CreateLocationNfsResponseTypeDef:
        """
        Creates a transfer *location* for a Network File System (NFS) file server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.create_location_nfs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#create_location_nfs)
        """

    def create_location_object_storage(
        self,
        *,
        ServerHostname: str,
        BucketName: str,
        AgentArns: List[str],
        ServerPort: int = None,
        ServerProtocol: ObjectStorageServerProtocolType = None,
        Subdirectory: str = None,
        AccessKey: str = None,
        SecretKey: str = None,
        Tags: List["TagListEntryTypeDef"] = None,
        ServerCertificate: Union[bytes, IO[bytes], StreamingBody] = None
    ) -> CreateLocationObjectStorageResponseTypeDef:
        """
        Creates a transfer *location* for an object storage system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.create_location_object_storage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#create_location_object_storage)
        """

    def create_location_s3(
        self,
        *,
        S3BucketArn: str,
        S3Config: "S3ConfigTypeDef",
        Subdirectory: str = None,
        S3StorageClass: S3StorageClassType = None,
        AgentArns: List[str] = None,
        Tags: List["TagListEntryTypeDef"] = None
    ) -> CreateLocationS3ResponseTypeDef:
        """
        Creates a transfer *location* for an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.create_location_s3)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#create_location_s3)
        """

    def create_location_smb(
        self,
        *,
        Subdirectory: str,
        ServerHostname: str,
        User: str,
        Password: str,
        AgentArns: List[str],
        Domain: str = None,
        MountOptions: "SmbMountOptionsTypeDef" = None,
        Tags: List["TagListEntryTypeDef"] = None
    ) -> CreateLocationSmbResponseTypeDef:
        """
        Creates a transfer *location* for a Server Message Block (SMB) file server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.create_location_smb)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#create_location_smb)
        """

    def create_task(
        self,
        *,
        SourceLocationArn: str,
        DestinationLocationArn: str,
        CloudWatchLogGroupArn: str = None,
        Name: str = None,
        Options: "OptionsTypeDef" = None,
        Excludes: List["FilterRuleTypeDef"] = None,
        Schedule: "TaskScheduleTypeDef" = None,
        Tags: List["TagListEntryTypeDef"] = None,
        Includes: List["FilterRuleTypeDef"] = None,
        ManifestConfig: "ManifestConfigTypeDef" = None,
        TaskReportConfig: "TaskReportConfigTypeDef" = None
    ) -> CreateTaskResponseTypeDef:
        """
        Configures a *task*, which defines where and how DataSync transfers your data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.create_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#create_task)
        """

    def delete_agent(self, *, AgentArn: str) -> Dict[str, Any]:
        """
        Removes an DataSync agent resource from your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.delete_agent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#delete_agent)
        """

    def delete_location(self, *, LocationArn: str) -> Dict[str, Any]:
        """
        Deletes a transfer location resource from DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.delete_location)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#delete_location)
        """

    def delete_task(self, *, TaskArn: str) -> Dict[str, Any]:
        """
        Deletes a transfer task resource from DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.delete_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#delete_task)
        """

    def describe_agent(self, *, AgentArn: str) -> DescribeAgentResponseTypeDef:
        """
        Returns information about an DataSync agent, such as its name, service endpoint
        type, and status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.describe_agent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_agent)
        """

    def describe_discovery_job(
        self, *, DiscoveryJobArn: str
    ) -> DescribeDiscoveryJobResponseTypeDef:
        """
        Returns information about a DataSync discovery job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.describe_discovery_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_discovery_job)
        """

    def describe_location_azure_blob(
        self, *, LocationArn: str
    ) -> DescribeLocationAzureBlobResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for Microsoft Azure
        Blob Storage is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.describe_location_azure_blob)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_location_azure_blob)
        """

    def describe_location_efs(self, *, LocationArn: str) -> DescribeLocationEfsResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an Amazon EFS file
        system is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.describe_location_efs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_location_efs)
        """

    def describe_location_fsx_lustre(
        self, *, LocationArn: str
    ) -> DescribeLocationFsxLustreResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an Amazon FSx for
        Lustre file system is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.describe_location_fsx_lustre)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_location_fsx_lustre)
        """

    def describe_location_fsx_ontap(
        self, *, LocationArn: str
    ) -> DescribeLocationFsxOntapResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an Amazon FSx for
        NetApp ONTAP file system is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.describe_location_fsx_ontap)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_location_fsx_ontap)
        """

    def describe_location_fsx_open_zfs(
        self, *, LocationArn: str
    ) -> DescribeLocationFsxOpenZfsResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an Amazon FSx for
        OpenZFS file system is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.describe_location_fsx_open_zfs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_location_fsx_open_zfs)
        """

    def describe_location_fsx_windows(
        self, *, LocationArn: str
    ) -> DescribeLocationFsxWindowsResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an Amazon FSx for
        Windows File Server file system is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.describe_location_fsx_windows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_location_fsx_windows)
        """

    def describe_location_hdfs(self, *, LocationArn: str) -> DescribeLocationHdfsResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for a Hadoop
        Distributed File System (HDFS) is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.describe_location_hdfs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_location_hdfs)
        """

    def describe_location_nfs(self, *, LocationArn: str) -> DescribeLocationNfsResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for a Network File
        System (NFS) file server is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.describe_location_nfs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_location_nfs)
        """

    def describe_location_object_storage(
        self, *, LocationArn: str
    ) -> DescribeLocationObjectStorageResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an object storage
        system is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.describe_location_object_storage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_location_object_storage)
        """

    def describe_location_s3(self, *, LocationArn: str) -> DescribeLocationS3ResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an S3 bucket is
        configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.describe_location_s3)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_location_s3)
        """

    def describe_location_smb(self, *, LocationArn: str) -> DescribeLocationSmbResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for a Server Message
        Block (SMB) file server is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.describe_location_smb)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_location_smb)
        """

    def describe_storage_system(
        self, *, StorageSystemArn: str
    ) -> DescribeStorageSystemResponseTypeDef:
        """
        Returns information about an on-premises storage system that you're using with
        DataSync Discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.describe_storage_system)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_storage_system)
        """

    def describe_storage_system_resource_metrics(
        self,
        *,
        DiscoveryJobArn: str,
        ResourceType: DiscoveryResourceTypeType,
        ResourceId: str,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeStorageSystemResourceMetricsResponseTypeDef:
        """
        Returns information, including performance data and capacity usage, which
        DataSync Discovery collects about a specific resource in your-premises storage
        system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.describe_storage_system_resource_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_storage_system_resource_metrics)
        """

    def describe_storage_system_resources(
        self,
        *,
        DiscoveryJobArn: str,
        ResourceType: DiscoveryResourceTypeType,
        ResourceIds: List[str] = None,
        Filter: Dict[Literal["SVM"], List[str]] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeStorageSystemResourcesResponseTypeDef:
        """
        Returns information that DataSync Discovery collects about resources in your on-
        premises storage system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.describe_storage_system_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_storage_system_resources)
        """

    def describe_task(self, *, TaskArn: str) -> DescribeTaskResponseTypeDef:
        """
        Provides information about a *task*, which defines where and how DataSync
        transfers your data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.describe_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_task)
        """

    def describe_task_execution(
        self, *, TaskExecutionArn: str
    ) -> DescribeTaskExecutionResponseTypeDef:
        """
        Provides information about an execution of your DataSync task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.describe_task_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_task_execution)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#generate_presigned_url)
        """

    def generate_recommendations(
        self,
        *,
        DiscoveryJobArn: str,
        ResourceIds: List[str],
        ResourceType: DiscoveryResourceTypeType
    ) -> Dict[str, Any]:
        """
        Creates recommendations about where to migrate your data to in Amazon Web
        Services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.generate_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#generate_recommendations)
        """

    def list_agents(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListAgentsResponseTypeDef:
        """
        Returns a list of DataSync agents that belong to an Amazon Web Services account
        in the Amazon Web Services Region specified in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.list_agents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#list_agents)
        """

    def list_discovery_jobs(
        self, *, StorageSystemArn: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListDiscoveryJobsResponseTypeDef:
        """
        Provides a list of the existing discovery jobs in the Amazon Web Services Region
        and Amazon Web Services account where you're using DataSync Discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.list_discovery_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#list_discovery_jobs)
        """

    def list_locations(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["LocationFilterTypeDef"] = None
    ) -> ListLocationsResponseTypeDef:
        """
        Returns a list of source and destination locations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.list_locations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#list_locations)
        """

    def list_storage_systems(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListStorageSystemsResponseTypeDef:
        """
        Lists the on-premises storage systems that you're using with DataSync Discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.list_storage_systems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#list_storage_systems)
        """

    def list_tags_for_resource(
        self, *, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns all the tags associated with an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#list_tags_for_resource)
        """

    def list_task_executions(
        self, *, TaskArn: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListTaskExecutionsResponseTypeDef:
        """
        Returns a list of executions for an DataSync transfer task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.list_task_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#list_task_executions)
        """

    def list_tasks(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["TaskFilterTypeDef"] = None
    ) -> ListTasksResponseTypeDef:
        """
        Returns a list of the DataSync tasks you created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.list_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#list_tasks)
        """

    def remove_storage_system(self, *, StorageSystemArn: str) -> Dict[str, Any]:
        """
        Permanently removes a storage system resource from DataSync Discovery, including
        the associated discovery jobs, collected data, and recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.remove_storage_system)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#remove_storage_system)
        """

    def start_discovery_job(
        self,
        *,
        StorageSystemArn: str,
        CollectionDurationMinutes: int,
        ClientToken: str,
        Tags: List["TagListEntryTypeDef"] = None
    ) -> StartDiscoveryJobResponseTypeDef:
        """
        Runs a DataSync discovery job on your on-premises storage system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.start_discovery_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#start_discovery_job)
        """

    def start_task_execution(
        self,
        *,
        TaskArn: str,
        OverrideOptions: "OptionsTypeDef" = None,
        Includes: List["FilterRuleTypeDef"] = None,
        Excludes: List["FilterRuleTypeDef"] = None,
        ManifestConfig: "ManifestConfigTypeDef" = None,
        TaskReportConfig: "TaskReportConfigTypeDef" = None,
        Tags: List["TagListEntryTypeDef"] = None
    ) -> StartTaskExecutionResponseTypeDef:
        """
        Starts an DataSync transfer task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.start_task_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#start_task_execution)
        """

    def stop_discovery_job(self, *, DiscoveryJobArn: str) -> Dict[str, Any]:
        """
        Stops a running DataSync discovery job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.stop_discovery_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#stop_discovery_job)
        """

    def tag_resource(
        self, *, ResourceArn: str, Tags: List["TagListEntryTypeDef"]
    ) -> Dict[str, Any]:
        """
        Applies a *tag* to an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, Keys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#untag_resource)
        """

    def update_agent(self, *, AgentArn: str, Name: str = None) -> Dict[str, Any]:
        """
        Updates the name of an DataSync agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.update_agent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#update_agent)
        """

    def update_discovery_job(
        self, *, DiscoveryJobArn: str, CollectionDurationMinutes: int
    ) -> Dict[str, Any]:
        """
        Edits a DataSync discovery job configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.update_discovery_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#update_discovery_job)
        """

    def update_location_azure_blob(
        self,
        *,
        LocationArn: str,
        Subdirectory: str = None,
        AuthenticationType: Literal["SAS"] = None,
        SasConfiguration: "AzureBlobSasConfigurationTypeDef" = None,
        BlobType: Literal["BLOCK"] = None,
        AccessTier: AzureAccessTierType = None,
        AgentArns: List[str] = None
    ) -> Dict[str, Any]:
        """
        Modifies some configurations of the Microsoft Azure Blob Storage transfer
        location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.update_location_azure_blob)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#update_location_azure_blob)
        """

    def update_location_hdfs(
        self,
        *,
        LocationArn: str,
        Subdirectory: str = None,
        NameNodes: List["HdfsNameNodeTypeDef"] = None,
        BlockSize: int = None,
        ReplicationFactor: int = None,
        KmsKeyProviderUri: str = None,
        QopConfiguration: "QopConfigurationTypeDef" = None,
        AuthenticationType: HdfsAuthenticationTypeType = None,
        SimpleUser: str = None,
        KerberosPrincipal: str = None,
        KerberosKeytab: Union[bytes, IO[bytes], StreamingBody] = None,
        KerberosKrb5Conf: Union[bytes, IO[bytes], StreamingBody] = None,
        AgentArns: List[str] = None
    ) -> Dict[str, Any]:
        """
        Updates some parameters of a previously created location for a Hadoop
        Distributed File System cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.update_location_hdfs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#update_location_hdfs)
        """

    def update_location_nfs(
        self,
        *,
        LocationArn: str,
        Subdirectory: str = None,
        OnPremConfig: "OnPremConfigTypeDef" = None,
        MountOptions: "NfsMountOptionsTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Modifies some configurations of the Network File System (NFS) transfer location
        that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.update_location_nfs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#update_location_nfs)
        """

    def update_location_object_storage(
        self,
        *,
        LocationArn: str,
        ServerPort: int = None,
        ServerProtocol: ObjectStorageServerProtocolType = None,
        Subdirectory: str = None,
        AccessKey: str = None,
        SecretKey: str = None,
        AgentArns: List[str] = None,
        ServerCertificate: Union[bytes, IO[bytes], StreamingBody] = None
    ) -> Dict[str, Any]:
        """
        Updates some parameters of an existing DataSync location for an object storage
        system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.update_location_object_storage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#update_location_object_storage)
        """

    def update_location_smb(
        self,
        *,
        LocationArn: str,
        Subdirectory: str = None,
        User: str = None,
        Domain: str = None,
        Password: str = None,
        AgentArns: List[str] = None,
        MountOptions: "SmbMountOptionsTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates some of the parameters of a Server Message Block (SMB) file server
        location that you can use for DataSync transfers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.update_location_smb)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#update_location_smb)
        """

    def update_storage_system(
        self,
        *,
        StorageSystemArn: str,
        ServerConfiguration: "DiscoveryServerConfigurationTypeDef" = None,
        AgentArns: List[str] = None,
        Name: str = None,
        CloudWatchLogGroupArn: str = None,
        Credentials: "CredentialsTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Modifies some configurations of an on-premises storage system resource that
        you're using with DataSync Discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.update_storage_system)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#update_storage_system)
        """

    def update_task(
        self,
        *,
        TaskArn: str,
        Options: "OptionsTypeDef" = None,
        Excludes: List["FilterRuleTypeDef"] = None,
        Schedule: "TaskScheduleTypeDef" = None,
        Name: str = None,
        CloudWatchLogGroupArn: str = None,
        Includes: List["FilterRuleTypeDef"] = None,
        ManifestConfig: "ManifestConfigTypeDef" = None,
        TaskReportConfig: "TaskReportConfigTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates the configuration of a *task*, which defines where and how DataSync
        transfers your data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.update_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#update_task)
        """

    def update_task_execution(
        self, *, TaskExecutionArn: str, Options: "OptionsTypeDef"
    ) -> Dict[str, Any]:
        """
        Updates the configuration of a running DataSync task execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Client.update_task_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#update_task_execution)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_storage_system_resource_metrics"]
    ) -> DescribeStorageSystemResourceMetricsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Paginator.DescribeStorageSystemResourceMetrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#describestoragesystemresourcemetricspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_agents"]) -> ListAgentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Paginator.ListAgents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listagentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_discovery_jobs"]
    ) -> ListDiscoveryJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Paginator.ListDiscoveryJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listdiscoveryjobspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_locations"]) -> ListLocationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Paginator.ListLocations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listlocationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_storage_systems"]
    ) -> ListStorageSystemsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Paginator.ListStorageSystems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#liststoragesystemspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Paginator.ListTagsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listtagsforresourcepaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_task_executions"]
    ) -> ListTaskExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Paginator.ListTaskExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listtaskexecutionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tasks"]) -> ListTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/datasync.html#DataSync.Paginator.ListTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listtaskspaginator)
        """
