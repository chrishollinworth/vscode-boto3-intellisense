"""
Type annotations for datasync service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_datasync.client import DataSyncClient

    session = Session()
    client: DataSyncClient = session.client("datasync")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

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
    AddStorageSystemRequestTypeDef,
    AddStorageSystemResponseTypeDef,
    CancelTaskExecutionRequestTypeDef,
    CreateAgentRequestTypeDef,
    CreateAgentResponseTypeDef,
    CreateLocationAzureBlobRequestTypeDef,
    CreateLocationAzureBlobResponseTypeDef,
    CreateLocationEfsRequestTypeDef,
    CreateLocationEfsResponseTypeDef,
    CreateLocationFsxLustreRequestTypeDef,
    CreateLocationFsxLustreResponseTypeDef,
    CreateLocationFsxOntapRequestTypeDef,
    CreateLocationFsxOntapResponseTypeDef,
    CreateLocationFsxOpenZfsRequestTypeDef,
    CreateLocationFsxOpenZfsResponseTypeDef,
    CreateLocationFsxWindowsRequestTypeDef,
    CreateLocationFsxWindowsResponseTypeDef,
    CreateLocationHdfsRequestTypeDef,
    CreateLocationHdfsResponseTypeDef,
    CreateLocationNfsRequestTypeDef,
    CreateLocationNfsResponseTypeDef,
    CreateLocationObjectStorageRequestTypeDef,
    CreateLocationObjectStorageResponseTypeDef,
    CreateLocationS3RequestTypeDef,
    CreateLocationS3ResponseTypeDef,
    CreateLocationSmbRequestTypeDef,
    CreateLocationSmbResponseTypeDef,
    CreateTaskRequestTypeDef,
    CreateTaskResponseTypeDef,
    DeleteAgentRequestTypeDef,
    DeleteLocationRequestTypeDef,
    DeleteTaskRequestTypeDef,
    DescribeAgentRequestTypeDef,
    DescribeAgentResponseTypeDef,
    DescribeDiscoveryJobRequestTypeDef,
    DescribeDiscoveryJobResponseTypeDef,
    DescribeLocationAzureBlobRequestTypeDef,
    DescribeLocationAzureBlobResponseTypeDef,
    DescribeLocationEfsRequestTypeDef,
    DescribeLocationEfsResponseTypeDef,
    DescribeLocationFsxLustreRequestTypeDef,
    DescribeLocationFsxLustreResponseTypeDef,
    DescribeLocationFsxOntapRequestTypeDef,
    DescribeLocationFsxOntapResponseTypeDef,
    DescribeLocationFsxOpenZfsRequestTypeDef,
    DescribeLocationFsxOpenZfsResponseTypeDef,
    DescribeLocationFsxWindowsRequestTypeDef,
    DescribeLocationFsxWindowsResponseTypeDef,
    DescribeLocationHdfsRequestTypeDef,
    DescribeLocationHdfsResponseTypeDef,
    DescribeLocationNfsRequestTypeDef,
    DescribeLocationNfsResponseTypeDef,
    DescribeLocationObjectStorageRequestTypeDef,
    DescribeLocationObjectStorageResponseTypeDef,
    DescribeLocationS3RequestTypeDef,
    DescribeLocationS3ResponseTypeDef,
    DescribeLocationSmbRequestTypeDef,
    DescribeLocationSmbResponseTypeDef,
    DescribeStorageSystemRequestTypeDef,
    DescribeStorageSystemResourceMetricsRequestTypeDef,
    DescribeStorageSystemResourceMetricsResponseTypeDef,
    DescribeStorageSystemResourcesRequestTypeDef,
    DescribeStorageSystemResourcesResponseTypeDef,
    DescribeStorageSystemResponseTypeDef,
    DescribeTaskExecutionRequestTypeDef,
    DescribeTaskExecutionResponseTypeDef,
    DescribeTaskRequestTypeDef,
    DescribeTaskResponseTypeDef,
    GenerateRecommendationsRequestTypeDef,
    ListAgentsRequestTypeDef,
    ListAgentsResponseTypeDef,
    ListDiscoveryJobsRequestTypeDef,
    ListDiscoveryJobsResponseTypeDef,
    ListLocationsRequestTypeDef,
    ListLocationsResponseTypeDef,
    ListStorageSystemsRequestTypeDef,
    ListStorageSystemsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTaskExecutionsRequestTypeDef,
    ListTaskExecutionsResponseTypeDef,
    ListTasksRequestTypeDef,
    ListTasksResponseTypeDef,
    RemoveStorageSystemRequestTypeDef,
    StartDiscoveryJobRequestTypeDef,
    StartDiscoveryJobResponseTypeDef,
    StartTaskExecutionRequestTypeDef,
    StartTaskExecutionResponseTypeDef,
    StopDiscoveryJobRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAgentRequestTypeDef,
    UpdateDiscoveryJobRequestTypeDef,
    UpdateLocationAzureBlobRequestTypeDef,
    UpdateLocationEfsRequestTypeDef,
    UpdateLocationFsxLustreRequestTypeDef,
    UpdateLocationFsxOntapRequestTypeDef,
    UpdateLocationFsxOpenZfsRequestTypeDef,
    UpdateLocationFsxWindowsRequestTypeDef,
    UpdateLocationHdfsRequestTypeDef,
    UpdateLocationNfsRequestTypeDef,
    UpdateLocationObjectStorageRequestTypeDef,
    UpdateLocationS3RequestTypeDef,
    UpdateLocationSmbRequestTypeDef,
    UpdateStorageSystemRequestTypeDef,
    UpdateTaskExecutionRequestTypeDef,
    UpdateTaskRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("DataSyncClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]

class DataSyncClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DataSyncClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#generate_presigned_url)
        """

    def add_storage_system(
        self, **kwargs: Unpack[AddStorageSystemRequestTypeDef]
    ) -> AddStorageSystemResponseTypeDef:
        """
        Creates an Amazon Web Services resource for an on-premises storage system that
        you want DataSync Discovery to collect information about.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/add_storage_system.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#add_storage_system)
        """

    def cancel_task_execution(
        self, **kwargs: Unpack[CancelTaskExecutionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops an DataSync task execution that's in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/cancel_task_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#cancel_task_execution)
        """

    def create_agent(
        self, **kwargs: Unpack[CreateAgentRequestTypeDef]
    ) -> CreateAgentResponseTypeDef:
        """
        Activates an DataSync agent that you deploy in your storage environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_agent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#create_agent)
        """

    def create_location_azure_blob(
        self, **kwargs: Unpack[CreateLocationAzureBlobRequestTypeDef]
    ) -> CreateLocationAzureBlobResponseTypeDef:
        """
        Creates a transfer <i>location</i> for a Microsoft Azure Blob Storage container.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_azure_blob.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#create_location_azure_blob)
        """

    def create_location_efs(
        self, **kwargs: Unpack[CreateLocationEfsRequestTypeDef]
    ) -> CreateLocationEfsResponseTypeDef:
        """
        Creates a transfer <i>location</i> for an Amazon EFS file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_efs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#create_location_efs)
        """

    def create_location_fsx_lustre(
        self, **kwargs: Unpack[CreateLocationFsxLustreRequestTypeDef]
    ) -> CreateLocationFsxLustreResponseTypeDef:
        """
        Creates a transfer <i>location</i> for an Amazon FSx for Lustre file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_fsx_lustre.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#create_location_fsx_lustre)
        """

    def create_location_fsx_ontap(
        self, **kwargs: Unpack[CreateLocationFsxOntapRequestTypeDef]
    ) -> CreateLocationFsxOntapResponseTypeDef:
        """
        Creates a transfer <i>location</i> for an Amazon FSx for NetApp ONTAP file
        system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_fsx_ontap.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#create_location_fsx_ontap)
        """

    def create_location_fsx_open_zfs(
        self, **kwargs: Unpack[CreateLocationFsxOpenZfsRequestTypeDef]
    ) -> CreateLocationFsxOpenZfsResponseTypeDef:
        """
        Creates a transfer <i>location</i> for an Amazon FSx for OpenZFS file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_fsx_open_zfs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#create_location_fsx_open_zfs)
        """

    def create_location_fsx_windows(
        self, **kwargs: Unpack[CreateLocationFsxWindowsRequestTypeDef]
    ) -> CreateLocationFsxWindowsResponseTypeDef:
        """
        Creates a transfer <i>location</i> for an Amazon FSx for Windows File Server
        file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_fsx_windows.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#create_location_fsx_windows)
        """

    def create_location_hdfs(
        self, **kwargs: Unpack[CreateLocationHdfsRequestTypeDef]
    ) -> CreateLocationHdfsResponseTypeDef:
        """
        Creates a transfer <i>location</i> for a Hadoop Distributed File System (HDFS).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_hdfs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#create_location_hdfs)
        """

    def create_location_nfs(
        self, **kwargs: Unpack[CreateLocationNfsRequestTypeDef]
    ) -> CreateLocationNfsResponseTypeDef:
        """
        Creates a transfer <i>location</i> for a Network File System (NFS) file server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_nfs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#create_location_nfs)
        """

    def create_location_object_storage(
        self, **kwargs: Unpack[CreateLocationObjectStorageRequestTypeDef]
    ) -> CreateLocationObjectStorageResponseTypeDef:
        """
        Creates a transfer <i>location</i> for an object storage system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_object_storage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#create_location_object_storage)
        """

    def create_location_s3(
        self, **kwargs: Unpack[CreateLocationS3RequestTypeDef]
    ) -> CreateLocationS3ResponseTypeDef:
        """
        Creates a transfer <i>location</i> for an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_s3.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#create_location_s3)
        """

    def create_location_smb(
        self, **kwargs: Unpack[CreateLocationSmbRequestTypeDef]
    ) -> CreateLocationSmbResponseTypeDef:
        """
        Creates a transfer <i>location</i> for a Server Message Block (SMB) file server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_smb.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#create_location_smb)
        """

    def create_task(self, **kwargs: Unpack[CreateTaskRequestTypeDef]) -> CreateTaskResponseTypeDef:
        """
        Configures a <i>task</i>, which defines where and how DataSync transfers your
        data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#create_task)
        """

    def delete_agent(self, **kwargs: Unpack[DeleteAgentRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes an DataSync agent resource from your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/delete_agent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#delete_agent)
        """

    def delete_location(self, **kwargs: Unpack[DeleteLocationRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a transfer location resource from DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/delete_location.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#delete_location)
        """

    def delete_task(self, **kwargs: Unpack[DeleteTaskRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a transfer task resource from DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/delete_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#delete_task)
        """

    def describe_agent(
        self, **kwargs: Unpack[DescribeAgentRequestTypeDef]
    ) -> DescribeAgentResponseTypeDef:
        """
        Returns information about an DataSync agent, such as its name, service endpoint
        type, and status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_agent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#describe_agent)
        """

    def describe_discovery_job(
        self, **kwargs: Unpack[DescribeDiscoveryJobRequestTypeDef]
    ) -> DescribeDiscoveryJobResponseTypeDef:
        """
        Returns information about a DataSync discovery job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_discovery_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#describe_discovery_job)
        """

    def describe_location_azure_blob(
        self, **kwargs: Unpack[DescribeLocationAzureBlobRequestTypeDef]
    ) -> DescribeLocationAzureBlobResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for Microsoft Azure
        Blob Storage is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_azure_blob.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#describe_location_azure_blob)
        """

    def describe_location_efs(
        self, **kwargs: Unpack[DescribeLocationEfsRequestTypeDef]
    ) -> DescribeLocationEfsResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an Amazon EFS file
        system is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_efs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#describe_location_efs)
        """

    def describe_location_fsx_lustre(
        self, **kwargs: Unpack[DescribeLocationFsxLustreRequestTypeDef]
    ) -> DescribeLocationFsxLustreResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an Amazon FSx for
        Lustre file system is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_fsx_lustre.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#describe_location_fsx_lustre)
        """

    def describe_location_fsx_ontap(
        self, **kwargs: Unpack[DescribeLocationFsxOntapRequestTypeDef]
    ) -> DescribeLocationFsxOntapResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an Amazon FSx for
        NetApp ONTAP file system is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_fsx_ontap.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#describe_location_fsx_ontap)
        """

    def describe_location_fsx_open_zfs(
        self, **kwargs: Unpack[DescribeLocationFsxOpenZfsRequestTypeDef]
    ) -> DescribeLocationFsxOpenZfsResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an Amazon FSx for
        OpenZFS file system is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_fsx_open_zfs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#describe_location_fsx_open_zfs)
        """

    def describe_location_fsx_windows(
        self, **kwargs: Unpack[DescribeLocationFsxWindowsRequestTypeDef]
    ) -> DescribeLocationFsxWindowsResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an Amazon FSx for
        Windows File Server file system is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_fsx_windows.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#describe_location_fsx_windows)
        """

    def describe_location_hdfs(
        self, **kwargs: Unpack[DescribeLocationHdfsRequestTypeDef]
    ) -> DescribeLocationHdfsResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for a Hadoop
        Distributed File System (HDFS) is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_hdfs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#describe_location_hdfs)
        """

    def describe_location_nfs(
        self, **kwargs: Unpack[DescribeLocationNfsRequestTypeDef]
    ) -> DescribeLocationNfsResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for a Network File
        System (NFS) file server is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_nfs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#describe_location_nfs)
        """

    def describe_location_object_storage(
        self, **kwargs: Unpack[DescribeLocationObjectStorageRequestTypeDef]
    ) -> DescribeLocationObjectStorageResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an object storage
        system is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_object_storage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#describe_location_object_storage)
        """

    def describe_location_s3(
        self, **kwargs: Unpack[DescribeLocationS3RequestTypeDef]
    ) -> DescribeLocationS3ResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an S3 bucket is
        configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_s3.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#describe_location_s3)
        """

    def describe_location_smb(
        self, **kwargs: Unpack[DescribeLocationSmbRequestTypeDef]
    ) -> DescribeLocationSmbResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for a Server Message
        Block (SMB) file server is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_smb.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#describe_location_smb)
        """

    def describe_storage_system(
        self, **kwargs: Unpack[DescribeStorageSystemRequestTypeDef]
    ) -> DescribeStorageSystemResponseTypeDef:
        """
        Returns information about an on-premises storage system that you're using with
        DataSync Discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_storage_system.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#describe_storage_system)
        """

    def describe_storage_system_resource_metrics(
        self, **kwargs: Unpack[DescribeStorageSystemResourceMetricsRequestTypeDef]
    ) -> DescribeStorageSystemResourceMetricsResponseTypeDef:
        """
        Returns information, including performance data and capacity usage, which
        DataSync Discovery collects about a specific resource in your-premises storage
        system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_storage_system_resource_metrics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#describe_storage_system_resource_metrics)
        """

    def describe_storage_system_resources(
        self, **kwargs: Unpack[DescribeStorageSystemResourcesRequestTypeDef]
    ) -> DescribeStorageSystemResourcesResponseTypeDef:
        """
        Returns information that DataSync Discovery collects about resources in your
        on-premises storage system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_storage_system_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#describe_storage_system_resources)
        """

    def describe_task(
        self, **kwargs: Unpack[DescribeTaskRequestTypeDef]
    ) -> DescribeTaskResponseTypeDef:
        """
        Provides information about a <i>task</i>, which defines where and how DataSync
        transfers your data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#describe_task)
        """

    def describe_task_execution(
        self, **kwargs: Unpack[DescribeTaskExecutionRequestTypeDef]
    ) -> DescribeTaskExecutionResponseTypeDef:
        """
        Provides information about an execution of your DataSync task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_task_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#describe_task_execution)
        """

    def generate_recommendations(
        self, **kwargs: Unpack[GenerateRecommendationsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates recommendations about where to migrate your data to in Amazon Web
        Services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/generate_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#generate_recommendations)
        """

    def list_agents(self, **kwargs: Unpack[ListAgentsRequestTypeDef]) -> ListAgentsResponseTypeDef:
        """
        Returns a list of DataSync agents that belong to an Amazon Web Services account
        in the Amazon Web Services Region specified in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/list_agents.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#list_agents)
        """

    def list_discovery_jobs(
        self, **kwargs: Unpack[ListDiscoveryJobsRequestTypeDef]
    ) -> ListDiscoveryJobsResponseTypeDef:
        """
        Provides a list of the existing discovery jobs in the Amazon Web Services
        Region and Amazon Web Services account where you're using DataSync Discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/list_discovery_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#list_discovery_jobs)
        """

    def list_locations(
        self, **kwargs: Unpack[ListLocationsRequestTypeDef]
    ) -> ListLocationsResponseTypeDef:
        """
        Returns a list of source and destination locations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/list_locations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#list_locations)
        """

    def list_storage_systems(
        self, **kwargs: Unpack[ListStorageSystemsRequestTypeDef]
    ) -> ListStorageSystemsResponseTypeDef:
        """
        Lists the on-premises storage systems that you're using with DataSync Discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/list_storage_systems.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#list_storage_systems)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns all the tags associated with an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#list_tags_for_resource)
        """

    def list_task_executions(
        self, **kwargs: Unpack[ListTaskExecutionsRequestTypeDef]
    ) -> ListTaskExecutionsResponseTypeDef:
        """
        Returns a list of executions for an DataSync transfer task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/list_task_executions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#list_task_executions)
        """

    def list_tasks(self, **kwargs: Unpack[ListTasksRequestTypeDef]) -> ListTasksResponseTypeDef:
        """
        Returns a list of the DataSync tasks you created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/list_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#list_tasks)
        """

    def remove_storage_system(
        self, **kwargs: Unpack[RemoveStorageSystemRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Permanently removes a storage system resource from DataSync Discovery,
        including the associated discovery jobs, collected data, and recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/remove_storage_system.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#remove_storage_system)
        """

    def start_discovery_job(
        self, **kwargs: Unpack[StartDiscoveryJobRequestTypeDef]
    ) -> StartDiscoveryJobResponseTypeDef:
        """
        Runs a DataSync discovery job on your on-premises storage system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/start_discovery_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#start_discovery_job)
        """

    def start_task_execution(
        self, **kwargs: Unpack[StartTaskExecutionRequestTypeDef]
    ) -> StartTaskExecutionResponseTypeDef:
        """
        Starts an DataSync transfer task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/start_task_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#start_task_execution)
        """

    def stop_discovery_job(
        self, **kwargs: Unpack[StopDiscoveryJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops a running DataSync discovery job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/stop_discovery_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#stop_discovery_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Applies a <i>tag</i> to an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#untag_resource)
        """

    def update_agent(self, **kwargs: Unpack[UpdateAgentRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates the name of an DataSync agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_agent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#update_agent)
        """

    def update_discovery_job(
        self, **kwargs: Unpack[UpdateDiscoveryJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Edits a DataSync discovery job configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_discovery_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#update_discovery_job)
        """

    def update_location_azure_blob(
        self, **kwargs: Unpack[UpdateLocationAzureBlobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configurations of the Microsoft Azure Blob Storage
        transfer location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_azure_blob.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#update_location_azure_blob)
        """

    def update_location_efs(
        self, **kwargs: Unpack[UpdateLocationEfsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configuration parameters of the Amazon EFS transfer
        location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_efs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#update_location_efs)
        """

    def update_location_fsx_lustre(
        self, **kwargs: Unpack[UpdateLocationFsxLustreRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configuration parameters of the Amazon FSx for Lustre
        transfer location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_fsx_lustre.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#update_location_fsx_lustre)
        """

    def update_location_fsx_ontap(
        self, **kwargs: Unpack[UpdateLocationFsxOntapRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configuration parameters of the Amazon FSx for NetApp
        ONTAP transfer location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_fsx_ontap.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#update_location_fsx_ontap)
        """

    def update_location_fsx_open_zfs(
        self, **kwargs: Unpack[UpdateLocationFsxOpenZfsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configuration parameters of the Amazon FSx for OpenZFS
        transfer location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_fsx_open_zfs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#update_location_fsx_open_zfs)
        """

    def update_location_fsx_windows(
        self, **kwargs: Unpack[UpdateLocationFsxWindowsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configuration parameters of the Amazon FSx for Windows
        File Server transfer location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_fsx_windows.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#update_location_fsx_windows)
        """

    def update_location_hdfs(
        self, **kwargs: Unpack[UpdateLocationHdfsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configuration parameters of the Hadoop Distributed File
        System (HDFS) transfer location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_hdfs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#update_location_hdfs)
        """

    def update_location_nfs(
        self, **kwargs: Unpack[UpdateLocationNfsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configuration parameters of the Network File System
        (NFS) transfer location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_nfs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#update_location_nfs)
        """

    def update_location_object_storage(
        self, **kwargs: Unpack[UpdateLocationObjectStorageRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configuration parameters of the object storage transfer
        location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_object_storage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#update_location_object_storage)
        """

    def update_location_s3(
        self, **kwargs: Unpack[UpdateLocationS3RequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configuration parameters of the Amazon S3 transfer
        location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_s3.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#update_location_s3)
        """

    def update_location_smb(
        self, **kwargs: Unpack[UpdateLocationSmbRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configuration parameters of the Server Message Block
        (SMB) transfer location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_smb.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#update_location_smb)
        """

    def update_storage_system(
        self, **kwargs: Unpack[UpdateStorageSystemRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies some configurations of an on-premises storage system resource that
        you're using with DataSync Discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_storage_system.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#update_storage_system)
        """

    def update_task(self, **kwargs: Unpack[UpdateTaskRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates the configuration of a <i>task</i>, which defines where and how
        DataSync transfers your data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#update_task)
        """

    def update_task_execution(
        self, **kwargs: Unpack[UpdateTaskExecutionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the configuration of a running DataSync task execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_task_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#update_task_execution)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_storage_system_resource_metrics"]
    ) -> DescribeStorageSystemResourceMetricsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_agents"]
    ) -> ListAgentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_discovery_jobs"]
    ) -> ListDiscoveryJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_locations"]
    ) -> ListLocationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_storage_systems"]
    ) -> ListStorageSystemsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_task_executions"]
    ) -> ListTaskExecutionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tasks"]
    ) -> ListTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/client/#get_paginator)
        """
