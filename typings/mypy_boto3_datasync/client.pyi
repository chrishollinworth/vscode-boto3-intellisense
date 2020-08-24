# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for datasync service client

Usage::

    ```python
    import boto3
    from mypy_boto3_datasync import DataSyncClient

    client: DataSyncClient = boto3.client("datasync")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_datasync.paginator import (
    ListAgentsPaginator,
    ListLocationsPaginator,
    ListTagsForResourcePaginator,
    ListTaskExecutionsPaginator,
    ListTasksPaginator,
)
from mypy_boto3_datasync.type_defs import (
    CreateAgentResponseTypeDef,
    CreateLocationEfsResponseTypeDef,
    CreateLocationFsxWindowsResponseTypeDef,
    CreateLocationNfsResponseTypeDef,
    CreateLocationObjectStorageResponseTypeDef,
    CreateLocationS3ResponseTypeDef,
    CreateLocationSmbResponseTypeDef,
    CreateTaskResponseTypeDef,
    DescribeAgentResponseTypeDef,
    DescribeLocationEfsResponseTypeDef,
    DescribeLocationFsxWindowsResponseTypeDef,
    DescribeLocationNfsResponseTypeDef,
    DescribeLocationObjectStorageResponseTypeDef,
    DescribeLocationS3ResponseTypeDef,
    DescribeLocationSmbResponseTypeDef,
    DescribeTaskExecutionResponseTypeDef,
    DescribeTaskResponseTypeDef,
    Ec2ConfigTypeDef,
    FilterRuleTypeDef,
    ListAgentsResponseTypeDef,
    ListLocationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTaskExecutionsResponseTypeDef,
    ListTasksResponseTypeDef,
    LocationFilterTypeDef,
    NfsMountOptionsTypeDef,
    OnPremConfigTypeDef,
    OptionsTypeDef,
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


class Exceptions:
    ClientError: Type[Boto3ClientError]
    InternalException: Type[Boto3ClientError]
    InvalidRequestException: Type[Boto3ClientError]


class DataSyncClient:
    """
    [DataSync.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.can_paginate)
        """

    def cancel_task_execution(self, TaskExecutionArn: str) -> Dict[str, Any]:
        """
        [Client.cancel_task_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.cancel_task_execution)
        """

    def create_agent(
        self,
        ActivationKey: str,
        AgentName: str = None,
        Tags: List["TagListEntryTypeDef"] = None,
        VpcEndpointId: str = None,
        SubnetArns: List[str] = None,
        SecurityGroupArns: List[str] = None,
    ) -> CreateAgentResponseTypeDef:
        """
        [Client.create_agent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.create_agent)
        """

    def create_location_efs(
        self,
        EfsFilesystemArn: str,
        Ec2Config: "Ec2ConfigTypeDef",
        Subdirectory: str = None,
        Tags: List["TagListEntryTypeDef"] = None,
    ) -> CreateLocationEfsResponseTypeDef:
        """
        [Client.create_location_efs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.create_location_efs)
        """

    def create_location_fsx_windows(
        self,
        FsxFilesystemArn: str,
        SecurityGroupArns: List[str],
        User: str,
        Password: str,
        Subdirectory: str = None,
        Tags: List["TagListEntryTypeDef"] = None,
        Domain: str = None,
    ) -> CreateLocationFsxWindowsResponseTypeDef:
        """
        [Client.create_location_fsx_windows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.create_location_fsx_windows)
        """

    def create_location_nfs(
        self,
        Subdirectory: str,
        ServerHostname: str,
        OnPremConfig: "OnPremConfigTypeDef",
        MountOptions: "NfsMountOptionsTypeDef" = None,
        Tags: List["TagListEntryTypeDef"] = None,
    ) -> CreateLocationNfsResponseTypeDef:
        """
        [Client.create_location_nfs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.create_location_nfs)
        """

    def create_location_object_storage(
        self,
        ServerHostname: str,
        BucketName: str,
        AgentArns: List[str],
        ServerPort: int = None,
        ServerProtocol: Literal["HTTPS", "HTTP"] = None,
        Subdirectory: str = None,
        AccessKey: str = None,
        SecretKey: str = None,
        Tags: List["TagListEntryTypeDef"] = None,
    ) -> CreateLocationObjectStorageResponseTypeDef:
        """
        [Client.create_location_object_storage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.create_location_object_storage)
        """

    def create_location_s3(
        self,
        S3BucketArn: str,
        S3Config: "S3ConfigTypeDef",
        Subdirectory: str = None,
        S3StorageClass: Literal[
            "STANDARD",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ] = None,
        Tags: List["TagListEntryTypeDef"] = None,
    ) -> CreateLocationS3ResponseTypeDef:
        """
        [Client.create_location_s3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.create_location_s3)
        """

    def create_location_smb(
        self,
        Subdirectory: str,
        ServerHostname: str,
        User: str,
        Password: str,
        AgentArns: List[str],
        Domain: str = None,
        MountOptions: "SmbMountOptionsTypeDef" = None,
        Tags: List["TagListEntryTypeDef"] = None,
    ) -> CreateLocationSmbResponseTypeDef:
        """
        [Client.create_location_smb documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.create_location_smb)
        """

    def create_task(
        self,
        SourceLocationArn: str,
        DestinationLocationArn: str,
        CloudWatchLogGroupArn: str = None,
        Name: str = None,
        Options: "OptionsTypeDef" = None,
        Excludes: List["FilterRuleTypeDef"] = None,
        Schedule: "TaskScheduleTypeDef" = None,
        Tags: List["TagListEntryTypeDef"] = None,
    ) -> CreateTaskResponseTypeDef:
        """
        [Client.create_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.create_task)
        """

    def delete_agent(self, AgentArn: str) -> Dict[str, Any]:
        """
        [Client.delete_agent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.delete_agent)
        """

    def delete_location(self, LocationArn: str) -> Dict[str, Any]:
        """
        [Client.delete_location documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.delete_location)
        """

    def delete_task(self, TaskArn: str) -> Dict[str, Any]:
        """
        [Client.delete_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.delete_task)
        """

    def describe_agent(self, AgentArn: str) -> DescribeAgentResponseTypeDef:
        """
        [Client.describe_agent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.describe_agent)
        """

    def describe_location_efs(self, LocationArn: str) -> DescribeLocationEfsResponseTypeDef:
        """
        [Client.describe_location_efs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.describe_location_efs)
        """

    def describe_location_fsx_windows(
        self, LocationArn: str
    ) -> DescribeLocationFsxWindowsResponseTypeDef:
        """
        [Client.describe_location_fsx_windows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.describe_location_fsx_windows)
        """

    def describe_location_nfs(self, LocationArn: str) -> DescribeLocationNfsResponseTypeDef:
        """
        [Client.describe_location_nfs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.describe_location_nfs)
        """

    def describe_location_object_storage(
        self, LocationArn: str
    ) -> DescribeLocationObjectStorageResponseTypeDef:
        """
        [Client.describe_location_object_storage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.describe_location_object_storage)
        """

    def describe_location_s3(self, LocationArn: str) -> DescribeLocationS3ResponseTypeDef:
        """
        [Client.describe_location_s3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.describe_location_s3)
        """

    def describe_location_smb(self, LocationArn: str) -> DescribeLocationSmbResponseTypeDef:
        """
        [Client.describe_location_smb documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.describe_location_smb)
        """

    def describe_task(self, TaskArn: str) -> DescribeTaskResponseTypeDef:
        """
        [Client.describe_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.describe_task)
        """

    def describe_task_execution(
        self, TaskExecutionArn: str
    ) -> DescribeTaskExecutionResponseTypeDef:
        """
        [Client.describe_task_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.describe_task_execution)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.generate_presigned_url)
        """

    def list_agents(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListAgentsResponseTypeDef:
        """
        [Client.list_agents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.list_agents)
        """

    def list_locations(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[LocationFilterTypeDef] = None,
    ) -> ListLocationsResponseTypeDef:
        """
        [Client.list_locations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.list_locations)
        """

    def list_tags_for_resource(
        self, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.list_tags_for_resource)
        """

    def list_task_executions(
        self, TaskArn: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListTaskExecutionsResponseTypeDef:
        """
        [Client.list_task_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.list_task_executions)
        """

    def list_tasks(
        self, MaxResults: int = None, NextToken: str = None, Filters: List[TaskFilterTypeDef] = None
    ) -> ListTasksResponseTypeDef:
        """
        [Client.list_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.list_tasks)
        """

    def start_task_execution(
        self,
        TaskArn: str,
        OverrideOptions: "OptionsTypeDef" = None,
        Includes: List["FilterRuleTypeDef"] = None,
    ) -> StartTaskExecutionResponseTypeDef:
        """
        [Client.start_task_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.start_task_execution)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagListEntryTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, Keys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.untag_resource)
        """

    def update_agent(self, AgentArn: str, Name: str = None) -> Dict[str, Any]:
        """
        [Client.update_agent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.update_agent)
        """

    def update_task(
        self,
        TaskArn: str,
        Options: "OptionsTypeDef" = None,
        Excludes: List["FilterRuleTypeDef"] = None,
        Schedule: "TaskScheduleTypeDef" = None,
        Name: str = None,
        CloudWatchLogGroupArn: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Client.update_task)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_agents"]) -> ListAgentsPaginator:
        """
        [Paginator.ListAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Paginator.ListAgents)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_locations"]) -> ListLocationsPaginator:
        """
        [Paginator.ListLocations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Paginator.ListLocations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Paginator.ListTagsForResource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_task_executions"]
    ) -> ListTaskExecutionsPaginator:
        """
        [Paginator.ListTaskExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Paginator.ListTaskExecutions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tasks"]) -> ListTasksPaginator:
        """
        [Paginator.ListTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/datasync.html#DataSync.Paginator.ListTasks)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
