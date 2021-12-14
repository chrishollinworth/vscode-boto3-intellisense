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
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import (
    HdfsAuthenticationTypeType,
    ObjectStorageServerProtocolType,
    S3StorageClassType,
)
from .paginator import (
    ListAgentsPaginator,
    ListLocationsPaginator,
    ListTagsForResourcePaginator,
    ListTaskExecutionsPaginator,
    ListTasksPaginator,
)
from .type_defs import (
    CreateAgentResponseTypeDef,
    CreateLocationEfsResponseTypeDef,
    CreateLocationFsxWindowsResponseTypeDef,
    CreateLocationHdfsResponseTypeDef,
    CreateLocationNfsResponseTypeDef,
    CreateLocationObjectStorageResponseTypeDef,
    CreateLocationS3ResponseTypeDef,
    CreateLocationSmbResponseTypeDef,
    CreateTaskResponseTypeDef,
    DescribeAgentResponseTypeDef,
    DescribeLocationEfsResponseTypeDef,
    DescribeLocationFsxWindowsResponseTypeDef,
    DescribeLocationHdfsResponseTypeDef,
    DescribeLocationNfsResponseTypeDef,
    DescribeLocationObjectStorageResponseTypeDef,
    DescribeLocationS3ResponseTypeDef,
    DescribeLocationSmbResponseTypeDef,
    DescribeTaskExecutionResponseTypeDef,
    DescribeTaskResponseTypeDef,
    Ec2ConfigTypeDef,
    FilterRuleTypeDef,
    HdfsNameNodeTypeDef,
    ListAgentsResponseTypeDef,
    ListLocationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTaskExecutionsResponseTypeDef,
    ListTasksResponseTypeDef,
    LocationFilterTypeDef,
    NfsMountOptionsTypeDef,
    OnPremConfigTypeDef,
    OptionsTypeDef,
    QopConfigurationTypeDef,
    S3ConfigTypeDef,
    SmbMountOptionsTypeDef,
    StartTaskExecutionResponseTypeDef,
    TagListEntryTypeDef,
    TaskFilterTypeDef,
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        DataSyncClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#can_paginate)
        """
    def cancel_task_execution(self, *, TaskExecutionArn: str) -> Dict[str, Any]:
        """
        Cancels execution of a task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.cancel_task_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#cancel_task_execution)
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
        Activates an DataSync agent that you have deployed on your host.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.create_agent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#create_agent)
        """
    def create_location_efs(
        self,
        *,
        EfsFilesystemArn: str,
        Ec2Config: "Ec2ConfigTypeDef",
        Subdirectory: str = None,
        Tags: List["TagListEntryTypeDef"] = None
    ) -> CreateLocationEfsResponseTypeDef:
        """
        Creates an endpoint for an Amazon EFS file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.create_location_efs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#create_location_efs)
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
        Creates an endpoint for an Amazon FSx for Windows File Server file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.create_location_fsx_windows)
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
        Creates an endpoint for a Hadoop Distributed File System (HDFS).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.create_location_hdfs)
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
        Defines a file system on a Network File System (NFS) server that can be read
        from or written to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.create_location_nfs)
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
        Tags: List["TagListEntryTypeDef"] = None
    ) -> CreateLocationObjectStorageResponseTypeDef:
        """
        Creates an endpoint for a self-managed object storage bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.create_location_object_storage)
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
        Creates an endpoint for an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.create_location_s3)
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
        Defines a file system on a Server Message Block (SMB) server that can be read
        from or written to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.create_location_smb)
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
        Includes: List["FilterRuleTypeDef"] = None
    ) -> CreateTaskResponseTypeDef:
        """
        Creates a task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.create_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#create_task)
        """
    def delete_agent(self, *, AgentArn: str) -> Dict[str, Any]:
        """
        Deletes an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.delete_agent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#delete_agent)
        """
    def delete_location(self, *, LocationArn: str) -> Dict[str, Any]:
        """
        Deletes the configuration of a location used by DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.delete_location)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#delete_location)
        """
    def delete_task(self, *, TaskArn: str) -> Dict[str, Any]:
        """
        Deletes a task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.delete_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#delete_task)
        """
    def describe_agent(self, *, AgentArn: str) -> DescribeAgentResponseTypeDef:
        """
        Returns metadata such as the name, the network interfaces, and the status (that
        is, whether the agent is running or not) for an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.describe_agent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_agent)
        """
    def describe_location_efs(self, *, LocationArn: str) -> DescribeLocationEfsResponseTypeDef:
        """
        Returns metadata, such as the path information about an Amazon EFS location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.describe_location_efs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_location_efs)
        """
    def describe_location_fsx_windows(
        self, *, LocationArn: str
    ) -> DescribeLocationFsxWindowsResponseTypeDef:
        """
        Returns metadata, such as the path information about an Amazon FSx for Windows
        File Server location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.describe_location_fsx_windows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_location_fsx_windows)
        """
    def describe_location_hdfs(self, *, LocationArn: str) -> DescribeLocationHdfsResponseTypeDef:
        """
        Returns metadata, such as the authentication information about the Hadoop
        Distributed File System (HDFS) location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.describe_location_hdfs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_location_hdfs)
        """
    def describe_location_nfs(self, *, LocationArn: str) -> DescribeLocationNfsResponseTypeDef:
        """
        Returns metadata, such as the path information, about an NFS location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.describe_location_nfs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_location_nfs)
        """
    def describe_location_object_storage(
        self, *, LocationArn: str
    ) -> DescribeLocationObjectStorageResponseTypeDef:
        """
        Returns metadata about a self-managed object storage server location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.describe_location_object_storage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_location_object_storage)
        """
    def describe_location_s3(self, *, LocationArn: str) -> DescribeLocationS3ResponseTypeDef:
        """
        Returns metadata, such as bucket name, about an Amazon S3 bucket location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.describe_location_s3)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_location_s3)
        """
    def describe_location_smb(self, *, LocationArn: str) -> DescribeLocationSmbResponseTypeDef:
        """
        Returns metadata, such as the path and user information about an SMB location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.describe_location_smb)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_location_smb)
        """
    def describe_task(self, *, TaskArn: str) -> DescribeTaskResponseTypeDef:
        """
        Returns metadata about a task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.describe_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#describe_task)
        """
    def describe_task_execution(
        self, *, TaskExecutionArn: str
    ) -> DescribeTaskExecutionResponseTypeDef:
        """
        Returns detailed metadata about a task that is being executed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.describe_task_execution)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#generate_presigned_url)
        """
    def list_agents(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListAgentsResponseTypeDef:
        """
        Returns a list of agents owned by an Amazon Web Services account in the Amazon
        Web Services Region specified in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.list_agents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#list_agents)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.list_locations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#list_locations)
        """
    def list_tags_for_resource(
        self, *, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns all the tags associated with a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#list_tags_for_resource)
        """
    def list_task_executions(
        self, *, TaskArn: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListTaskExecutionsResponseTypeDef:
        """
        Returns a list of executed tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.list_task_executions)
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
        Returns a list of all the tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.list_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#list_tasks)
        """
    def start_task_execution(
        self,
        *,
        TaskArn: str,
        OverrideOptions: "OptionsTypeDef" = None,
        Includes: List["FilterRuleTypeDef"] = None,
        Excludes: List["FilterRuleTypeDef"] = None
    ) -> StartTaskExecutionResponseTypeDef:
        """
        Starts a specific invocation of a task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.start_task_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#start_task_execution)
        """
    def tag_resource(
        self, *, ResourceArn: str, Tags: List["TagListEntryTypeDef"]
    ) -> Dict[str, Any]:
        """
        Applies a key-value pair to an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, Keys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag from an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#untag_resource)
        """
    def update_agent(self, *, AgentArn: str, Name: str = None) -> Dict[str, Any]:
        """
        Updates the name of an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.update_agent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#update_agent)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.update_location_hdfs)
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
        Updates some of the parameters of a previously created location for Network File
        System (NFS) access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.update_location_nfs)
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
        AgentArns: List[str] = None
    ) -> Dict[str, Any]:
        """
        Updates some of the parameters of a previously created location for self-managed
        object storage server access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.update_location_object_storage)
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
        Updates some of the parameters of a previously created location for Server
        Message Block (SMB) file system access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.update_location_smb)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#update_location_smb)
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
        Includes: List["FilterRuleTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Updates the metadata associated with a task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.update_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#update_task)
        """
    def update_task_execution(
        self, *, TaskExecutionArn: str, Options: "OptionsTypeDef"
    ) -> Dict[str, Any]:
        """
        Updates execution of a task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Client.update_task_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/client.html#update_task_execution)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_agents"]) -> ListAgentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Paginator.ListAgents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listagentspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_locations"]) -> ListLocationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Paginator.ListLocations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listlocationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Paginator.ListTagsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listtagsforresourcepaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_task_executions"]
    ) -> ListTaskExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Paginator.ListTaskExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listtaskexecutionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_tasks"]) -> ListTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/datasync.html#DataSync.Paginator.ListTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/paginators.html#listtaskspaginator)
        """
