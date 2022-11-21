"""
Type annotations for mgn service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_mgn import mgnClient

    client: mgnClient = boto3.client("mgn")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    BootModeType,
    LaunchDispositionType,
    ReplicationConfigurationDataPlaneRoutingType,
    ReplicationConfigurationDefaultLargeStagingDiskTypeType,
    ReplicationConfigurationEbsEncryptionType,
    ReplicationTypeType,
    TargetInstanceTypeRightSizingMethodType,
)
from .paginator import (
    DescribeJobLogItemsPaginator,
    DescribeJobsPaginator,
    DescribeLaunchConfigurationTemplatesPaginator,
    DescribeReplicationConfigurationTemplatesPaginator,
    DescribeSourceServersPaginator,
    DescribeVcenterClientsPaginator,
)
from .type_defs import (
    ChangeServerLifeCycleStateSourceServerLifecycleTypeDef,
    DescribeJobLogItemsResponseTypeDef,
    DescribeJobsRequestFiltersTypeDef,
    DescribeJobsResponseTypeDef,
    DescribeLaunchConfigurationTemplatesResponseTypeDef,
    DescribeReplicationConfigurationTemplatesResponseTypeDef,
    DescribeSourceServersRequestFiltersTypeDef,
    DescribeSourceServersResponseTypeDef,
    DescribeVcenterClientsResponseTypeDef,
    LaunchConfigurationTemplateResponseMetadataTypeDef,
    LaunchConfigurationTypeDef,
    LicensingTypeDef,
    ListTagsForResourceResponseTypeDef,
    PostLaunchActionsTypeDef,
    ReplicationConfigurationReplicatedDiskTypeDef,
    ReplicationConfigurationTemplateResponseMetadataTypeDef,
    ReplicationConfigurationTypeDef,
    SourceServerResponseMetadataTypeDef,
    StartCutoverResponseTypeDef,
    StartTestResponseTypeDef,
    TerminateTargetInstancesResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("mgnClient",)

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
    ThrottlingException: Type[BotocoreClientError]
    UninitializedAccountException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class mgnClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        mgnClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#can_paginate)
        """
    def change_server_life_cycle_state(
        self,
        *,
        lifeCycle: "ChangeServerLifeCycleStateSourceServerLifecycleTypeDef",
        sourceServerID: str
    ) -> SourceServerResponseMetadataTypeDef:
        """
        Allows the user to set the SourceServer.LifeCycle.state property for specific
        Source Server IDs to one of the following: READY_FOR_TEST or READY_FOR_CUTOVER.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.change_server_life_cycle_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#change_server_life_cycle_state)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#close)
        """
    def create_launch_configuration_template(
        self, *, postLaunchActions: "PostLaunchActionsTypeDef" = None, tags: Dict[str, str] = None
    ) -> LaunchConfigurationTemplateResponseMetadataTypeDef:
        """
        Creates a new ReplicationConfigurationTemplate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.create_launch_configuration_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#create_launch_configuration_template)
        """
    def create_replication_configuration_template(
        self,
        *,
        associateDefaultSecurityGroup: bool,
        bandwidthThrottling: int,
        createPublicIP: bool,
        dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType,
        defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        ebsEncryption: ReplicationConfigurationEbsEncryptionType,
        replicationServerInstanceType: str,
        replicationServersSecurityGroupsIDs: List[str],
        stagingAreaSubnetId: str,
        stagingAreaTags: Dict[str, str],
        useDedicatedReplicationServer: bool,
        ebsEncryptionKeyArn: str = None,
        tags: Dict[str, str] = None
    ) -> ReplicationConfigurationTemplateResponseMetadataTypeDef:
        """
        Creates a new ReplicationConfigurationTemplate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.create_replication_configuration_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#create_replication_configuration_template)
        """
    def delete_job(self, *, jobID: str) -> Dict[str, Any]:
        """
        Deletes a single Job by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.delete_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#delete_job)
        """
    def delete_launch_configuration_template(
        self, *, launchConfigurationTemplateID: str
    ) -> Dict[str, Any]:
        """
        Creates a new ReplicationConfigurationTemplate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.delete_launch_configuration_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#delete_launch_configuration_template)
        """
    def delete_replication_configuration_template(
        self, *, replicationConfigurationTemplateID: str
    ) -> Dict[str, Any]:
        """
        Deletes a single Replication Configuration Template by ID See also: `AWS API
        Documentation <https://docs.aws.amazon.com/goto/WebAPI/mgn-2020-02-
        26/DeleteReplicationConfigurationTemplate>`_ **Request Syntax** response =
        client.delete_replication_configuration_template( replicatio...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.delete_replication_configuration_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#delete_replication_configuration_template)
        """
    def delete_source_server(self, *, sourceServerID: str) -> Dict[str, Any]:
        """
        Deletes a single source server by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.delete_source_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#delete_source_server)
        """
    def delete_vcenter_client(self, *, vcenterClientID: str) -> None:
        """
        Deletes a given vCenter client by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.delete_vcenter_client)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#delete_vcenter_client)
        """
    def describe_job_log_items(
        self, *, jobID: str, maxResults: int = None, nextToken: str = None
    ) -> DescribeJobLogItemsResponseTypeDef:
        """
        Retrieves detailed job log items with paging.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.describe_job_log_items)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#describe_job_log_items)
        """
    def describe_jobs(
        self,
        *,
        filters: "DescribeJobsRequestFiltersTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeJobsResponseTypeDef:
        """
        Returns a list of Jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.describe_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#describe_jobs)
        """
    def describe_launch_configuration_templates(
        self,
        *,
        launchConfigurationTemplateIDs: List[str] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeLaunchConfigurationTemplatesResponseTypeDef:
        """
        Creates a new ReplicationConfigurationTemplate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.describe_launch_configuration_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#describe_launch_configuration_templates)
        """
    def describe_replication_configuration_templates(
        self,
        *,
        maxResults: int = None,
        nextToken: str = None,
        replicationConfigurationTemplateIDs: List[str] = None
    ) -> DescribeReplicationConfigurationTemplatesResponseTypeDef:
        """
        Lists all ReplicationConfigurationTemplates, filtered by Source Server IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.describe_replication_configuration_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#describe_replication_configuration_templates)
        """
    def describe_source_servers(
        self,
        *,
        filters: "DescribeSourceServersRequestFiltersTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeSourceServersResponseTypeDef:
        """
        Retrieves all SourceServers or multiple SourceServers by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.describe_source_servers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#describe_source_servers)
        """
    def describe_vcenter_clients(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> DescribeVcenterClientsResponseTypeDef:
        """
        Returns a list of the installed vCenter clients.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.describe_vcenter_clients)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#describe_vcenter_clients)
        """
    def disconnect_from_service(
        self, *, sourceServerID: str
    ) -> SourceServerResponseMetadataTypeDef:
        """
        Disconnects specific Source Servers from Application Migration Service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.disconnect_from_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#disconnect_from_service)
        """
    def finalize_cutover(self, *, sourceServerID: str) -> SourceServerResponseMetadataTypeDef:
        """
        Finalizes the cutover immediately for specific Source Servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.finalize_cutover)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#finalize_cutover)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#generate_presigned_url)
        """
    def get_launch_configuration(self, *, sourceServerID: str) -> LaunchConfigurationTypeDef:
        """
        Lists all LaunchConfigurations available, filtered by Source Server IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.get_launch_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#get_launch_configuration)
        """
    def get_replication_configuration(
        self, *, sourceServerID: str
    ) -> ReplicationConfigurationTypeDef:
        """
        Lists all ReplicationConfigurations, filtered by Source Server ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.get_replication_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#get_replication_configuration)
        """
    def initialize_service(self) -> Dict[str, Any]:
        """
        Initialize Application Migration Service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.initialize_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#initialize_service)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        List all tags for your Application Migration Service resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#list_tags_for_resource)
        """
    def mark_as_archived(self, *, sourceServerID: str) -> SourceServerResponseMetadataTypeDef:
        """
        Archives specific Source Servers by setting the SourceServer.isArchived property
        to true for specified SourceServers by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.mark_as_archived)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#mark_as_archived)
        """
    def retry_data_replication(self, *, sourceServerID: str) -> SourceServerResponseMetadataTypeDef:
        """
        Causes the data replication initiation sequence to begin immediately upon next
        Handshake for specified SourceServer IDs, regardless of when the previous
        initiation started.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.retry_data_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#retry_data_replication)
        """
    def start_cutover(
        self, *, sourceServerIDs: List[str], tags: Dict[str, str] = None
    ) -> StartCutoverResponseTypeDef:
        """
        Launches a Cutover Instance for specific Source Servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.start_cutover)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#start_cutover)
        """
    def start_replication(self, *, sourceServerID: str) -> SourceServerResponseMetadataTypeDef:
        """
        Starts replication for SNAPSHOT_SHIPPING agents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.start_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#start_replication)
        """
    def start_test(
        self, *, sourceServerIDs: List[str], tags: Dict[str, str] = None
    ) -> StartTestResponseTypeDef:
        """
        Launches a Test Instance for specific Source Servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.start_test)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#start_test)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> None:
        """
        Adds or overwrites only the specified tags for the specified Application
        Migration Service resource or resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#tag_resource)
        """
    def terminate_target_instances(
        self, *, sourceServerIDs: List[str], tags: Dict[str, str] = None
    ) -> TerminateTargetInstancesResponseTypeDef:
        """
        Starts a job that terminates specific launched EC2 Test and Cutover instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.terminate_target_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#terminate_target_instances)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> None:
        """
        Deletes the specified set of tags from the specified set of Application
        Migration Service resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#untag_resource)
        """
    def update_launch_configuration(
        self,
        *,
        sourceServerID: str,
        bootMode: BootModeType = None,
        copyPrivateIp: bool = None,
        copyTags: bool = None,
        launchDisposition: LaunchDispositionType = None,
        licensing: "LicensingTypeDef" = None,
        name: str = None,
        postLaunchActions: "PostLaunchActionsTypeDef" = None,
        targetInstanceTypeRightSizingMethod: TargetInstanceTypeRightSizingMethodType = None
    ) -> LaunchConfigurationTypeDef:
        """
        Updates multiple LaunchConfigurations by Source Server ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.update_launch_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#update_launch_configuration)
        """
    def update_launch_configuration_template(
        self,
        *,
        launchConfigurationTemplateID: str,
        postLaunchActions: "PostLaunchActionsTypeDef" = None
    ) -> LaunchConfigurationTemplateResponseMetadataTypeDef:
        """
        Creates a new ReplicationConfigurationTemplate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.update_launch_configuration_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#update_launch_configuration_template)
        """
    def update_replication_configuration(
        self,
        *,
        sourceServerID: str,
        associateDefaultSecurityGroup: bool = None,
        bandwidthThrottling: int = None,
        createPublicIP: bool = None,
        dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType = None,
        defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType = None,
        ebsEncryption: ReplicationConfigurationEbsEncryptionType = None,
        ebsEncryptionKeyArn: str = None,
        name: str = None,
        replicatedDisks: List["ReplicationConfigurationReplicatedDiskTypeDef"] = None,
        replicationServerInstanceType: str = None,
        replicationServersSecurityGroupsIDs: List[str] = None,
        stagingAreaSubnetId: str = None,
        stagingAreaTags: Dict[str, str] = None,
        useDedicatedReplicationServer: bool = None
    ) -> ReplicationConfigurationTypeDef:
        """
        Allows you to update multiple ReplicationConfigurations by Source Server ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.update_replication_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#update_replication_configuration)
        """
    def update_replication_configuration_template(
        self,
        *,
        replicationConfigurationTemplateID: str,
        arn: str = None,
        associateDefaultSecurityGroup: bool = None,
        bandwidthThrottling: int = None,
        createPublicIP: bool = None,
        dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType = None,
        defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType = None,
        ebsEncryption: ReplicationConfigurationEbsEncryptionType = None,
        ebsEncryptionKeyArn: str = None,
        replicationServerInstanceType: str = None,
        replicationServersSecurityGroupsIDs: List[str] = None,
        stagingAreaSubnetId: str = None,
        stagingAreaTags: Dict[str, str] = None,
        useDedicatedReplicationServer: bool = None
    ) -> ReplicationConfigurationTemplateResponseMetadataTypeDef:
        """
        Updates multiple ReplicationConfigurationTemplates by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.update_replication_configuration_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#update_replication_configuration_template)
        """
    def update_source_server_replication_type(
        self, *, replicationType: ReplicationTypeType, sourceServerID: str
    ) -> SourceServerResponseMetadataTypeDef:
        """
        Allows you to change between the AGENT_BASED replication type and the
        SNAPSHOT_SHIPPING replication type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Client.update_source_server_replication_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#update_source_server_replication_type)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_job_log_items"]
    ) -> DescribeJobLogItemsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Paginator.DescribeJobLogItems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describejoblogitemspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_jobs"]) -> DescribeJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Paginator.DescribeJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describejobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_launch_configuration_templates"]
    ) -> DescribeLaunchConfigurationTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Paginator.DescribeLaunchConfigurationTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describelaunchconfigurationtemplatespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_configuration_templates"]
    ) -> DescribeReplicationConfigurationTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Paginator.DescribeReplicationConfigurationTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describereplicationconfigurationtemplatespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_source_servers"]
    ) -> DescribeSourceServersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Paginator.DescribeSourceServers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describesourceserverspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vcenter_clients"]
    ) -> DescribeVcenterClientsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mgn.html#mgn.Paginator.DescribeVcenterClients)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describevcenterclientspaginator)
        """
