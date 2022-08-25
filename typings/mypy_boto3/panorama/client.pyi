"""
Type annotations for panorama service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_panorama import PanoramaClient

    client: PanoramaClient = boto3.client("panorama")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import NodeCategoryType, PackageImportJobTypeType, StatusFilterType
from .type_defs import (
    CreateApplicationInstanceResponseTypeDef,
    CreateJobForDevicesResponseTypeDef,
    CreateNodeFromTemplateJobResponseTypeDef,
    CreatePackageImportJobResponseTypeDef,
    CreatePackageResponseTypeDef,
    DeleteDeviceResponseTypeDef,
    DescribeApplicationInstanceDetailsResponseTypeDef,
    DescribeApplicationInstanceResponseTypeDef,
    DescribeDeviceJobResponseTypeDef,
    DescribeDeviceResponseTypeDef,
    DescribeNodeFromTemplateJobResponseTypeDef,
    DescribeNodeResponseTypeDef,
    DescribePackageImportJobResponseTypeDef,
    DescribePackageResponseTypeDef,
    DescribePackageVersionResponseTypeDef,
    DeviceJobConfigTypeDef,
    JobResourceTagsTypeDef,
    ListApplicationInstanceDependenciesResponseTypeDef,
    ListApplicationInstanceNodeInstancesResponseTypeDef,
    ListApplicationInstancesResponseTypeDef,
    ListDevicesJobsResponseTypeDef,
    ListDevicesResponseTypeDef,
    ListNodeFromTemplateJobsResponseTypeDef,
    ListNodesResponseTypeDef,
    ListPackageImportJobsResponseTypeDef,
    ListPackagesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ManifestOverridesPayloadTypeDef,
    ManifestPayloadTypeDef,
    NetworkPayloadTypeDef,
    PackageImportJobInputConfigTypeDef,
    PackageImportJobOutputConfigTypeDef,
    ProvisionDeviceResponseTypeDef,
    UpdateDeviceMetadataResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("PanoramaClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class PanoramaClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PanoramaClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#close)
        """
    def create_application_instance(
        self,
        *,
        DefaultRuntimeContextDevice: str,
        ManifestPayload: "ManifestPayloadTypeDef",
        ApplicationInstanceIdToReplace: str = None,
        Description: str = None,
        ManifestOverridesPayload: "ManifestOverridesPayloadTypeDef" = None,
        Name: str = None,
        RuntimeRoleArn: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateApplicationInstanceResponseTypeDef:
        """
        Creates an application instance and deploys it to a device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.create_application_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#create_application_instance)
        """
    def create_job_for_devices(
        self,
        *,
        DeviceIds: List[str],
        DeviceJobConfig: "DeviceJobConfigTypeDef",
        JobType: Literal["OTA"]
    ) -> CreateJobForDevicesResponseTypeDef:
        """
        Creates a job to run on one or more devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.create_job_for_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#create_job_for_devices)
        """
    def create_node_from_template_job(
        self,
        *,
        NodeName: str,
        OutputPackageName: str,
        OutputPackageVersion: str,
        TemplateParameters: Dict[str, str],
        TemplateType: Literal["RTSP_CAMERA_STREAM"],
        JobTags: List["JobResourceTagsTypeDef"] = None,
        NodeDescription: str = None
    ) -> CreateNodeFromTemplateJobResponseTypeDef:
        """
        Creates a camera stream node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.create_node_from_template_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#create_node_from_template_job)
        """
    def create_package(
        self, *, PackageName: str, Tags: Dict[str, str] = None
    ) -> CreatePackageResponseTypeDef:
        """
        Creates a package and storage location in an Amazon S3 access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.create_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#create_package)
        """
    def create_package_import_job(
        self,
        *,
        ClientToken: str,
        InputConfig: "PackageImportJobInputConfigTypeDef",
        JobType: PackageImportJobTypeType,
        OutputConfig: "PackageImportJobOutputConfigTypeDef",
        JobTags: List["JobResourceTagsTypeDef"] = None
    ) -> CreatePackageImportJobResponseTypeDef:
        """
        Imports a node package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.create_package_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#create_package_import_job)
        """
    def delete_device(self, *, DeviceId: str) -> DeleteDeviceResponseTypeDef:
        """
        Deletes a device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.delete_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#delete_device)
        """
    def delete_package(self, *, PackageId: str, ForceDelete: bool = None) -> Dict[str, Any]:
        """
        Deletes a package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.delete_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#delete_package)
        """
    def deregister_package_version(
        self,
        *,
        PackageId: str,
        PackageVersion: str,
        PatchVersion: str,
        OwnerAccount: str = None,
        UpdatedLatestPatchVersion: str = None
    ) -> Dict[str, Any]:
        """
        Deregisters a package version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.deregister_package_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#deregister_package_version)
        """
    def describe_application_instance(
        self, *, ApplicationInstanceId: str
    ) -> DescribeApplicationInstanceResponseTypeDef:
        """
        Returns information about an application instance on a device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.describe_application_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#describe_application_instance)
        """
    def describe_application_instance_details(
        self, *, ApplicationInstanceId: str
    ) -> DescribeApplicationInstanceDetailsResponseTypeDef:
        """
        Returns information about an application instance's configuration manifest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.describe_application_instance_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#describe_application_instance_details)
        """
    def describe_device(self, *, DeviceId: str) -> DescribeDeviceResponseTypeDef:
        """
        Returns information about a device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.describe_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#describe_device)
        """
    def describe_device_job(self, *, JobId: str) -> DescribeDeviceJobResponseTypeDef:
        """
        Returns information about a device job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.describe_device_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#describe_device_job)
        """
    def describe_node(
        self, *, NodeId: str, OwnerAccount: str = None
    ) -> DescribeNodeResponseTypeDef:
        """
        Returns information about a node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.describe_node)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#describe_node)
        """
    def describe_node_from_template_job(
        self, *, JobId: str
    ) -> DescribeNodeFromTemplateJobResponseTypeDef:
        """
        Returns information about a job to create a camera stream node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.describe_node_from_template_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#describe_node_from_template_job)
        """
    def describe_package(self, *, PackageId: str) -> DescribePackageResponseTypeDef:
        """
        Returns information about a package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.describe_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#describe_package)
        """
    def describe_package_import_job(self, *, JobId: str) -> DescribePackageImportJobResponseTypeDef:
        """
        Returns information about a package import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.describe_package_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#describe_package_import_job)
        """
    def describe_package_version(
        self,
        *,
        PackageId: str,
        PackageVersion: str,
        OwnerAccount: str = None,
        PatchVersion: str = None
    ) -> DescribePackageVersionResponseTypeDef:
        """
        Returns information about a package version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.describe_package_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#describe_package_version)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#generate_presigned_url)
        """
    def list_application_instance_dependencies(
        self, *, ApplicationInstanceId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListApplicationInstanceDependenciesResponseTypeDef:
        """
        Returns a list of application instance dependencies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.list_application_instance_dependencies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#list_application_instance_dependencies)
        """
    def list_application_instance_node_instances(
        self, *, ApplicationInstanceId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListApplicationInstanceNodeInstancesResponseTypeDef:
        """
        Returns a list of application node instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.list_application_instance_node_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#list_application_instance_node_instances)
        """
    def list_application_instances(
        self,
        *,
        DeviceId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        StatusFilter: StatusFilterType = None
    ) -> ListApplicationInstancesResponseTypeDef:
        """
        Returns a list of application instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.list_application_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#list_application_instances)
        """
    def list_devices(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListDevicesResponseTypeDef:
        """
        Returns a list of devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.list_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#list_devices)
        """
    def list_devices_jobs(
        self, *, DeviceId: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListDevicesJobsResponseTypeDef:
        """
        Returns a list of jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.list_devices_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#list_devices_jobs)
        """
    def list_node_from_template_jobs(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListNodeFromTemplateJobsResponseTypeDef:
        """
        Returns a list of camera stream node jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.list_node_from_template_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#list_node_from_template_jobs)
        """
    def list_nodes(
        self,
        *,
        Category: NodeCategoryType = None,
        MaxResults: int = None,
        NextToken: str = None,
        OwnerAccount: str = None,
        PackageName: str = None,
        PackageVersion: str = None,
        PatchVersion: str = None
    ) -> ListNodesResponseTypeDef:
        """
        Returns a list of nodes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.list_nodes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#list_nodes)
        """
    def list_package_import_jobs(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListPackageImportJobsResponseTypeDef:
        """
        Returns a list of package import jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.list_package_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#list_package_import_jobs)
        """
    def list_packages(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListPackagesResponseTypeDef:
        """
        Returns a list of packages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.list_packages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#list_packages)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#list_tags_for_resource)
        """
    def provision_device(
        self,
        *,
        Name: str,
        Description: str = None,
        NetworkingConfiguration: "NetworkPayloadTypeDef" = None,
        Tags: Dict[str, str] = None
    ) -> ProvisionDeviceResponseTypeDef:
        """
        Creates a device and returns a configuration archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.provision_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#provision_device)
        """
    def register_package_version(
        self,
        *,
        PackageId: str,
        PackageVersion: str,
        PatchVersion: str,
        MarkLatest: bool = None,
        OwnerAccount: str = None
    ) -> Dict[str, Any]:
        """
        Registers a package version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.register_package_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#register_package_version)
        """
    def remove_application_instance(self, *, ApplicationInstanceId: str) -> Dict[str, Any]:
        """
        Removes an application instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.remove_application_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#remove_application_instance)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Tags a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#untag_resource)
        """
    def update_device_metadata(
        self, *, DeviceId: str, Description: str = None
    ) -> UpdateDeviceMetadataResponseTypeDef:
        """
        Updates a device's metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/panorama.html#Panorama.Client.update_device_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/client.html#update_device_metadata)
        """
