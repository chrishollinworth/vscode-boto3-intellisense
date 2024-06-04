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
    ActionCategoryType,
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
    ListApplicationsPaginator,
    ListConnectorsPaginator,
    ListExportErrorsPaginator,
    ListExportsPaginator,
    ListImportErrorsPaginator,
    ListImportsPaginator,
    ListManagedAccountsPaginator,
    ListSourceServerActionsPaginator,
    ListTemplateActionsPaginator,
    ListWavesPaginator,
)
from .type_defs import (
    ApplicationResponseMetadataTypeDef,
    ChangeServerLifeCycleStateSourceServerLifecycleTypeDef,
    ConnectorResponseMetadataTypeDef,
    ConnectorSsmCommandConfigTypeDef,
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
    LaunchTemplateDiskConfTypeDef,
    LicensingTypeDef,
    ListApplicationsRequestFiltersTypeDef,
    ListApplicationsResponseTypeDef,
    ListConnectorsRequestFiltersTypeDef,
    ListConnectorsResponseTypeDef,
    ListExportErrorsResponseTypeDef,
    ListExportsRequestFiltersTypeDef,
    ListExportsResponseTypeDef,
    ListImportErrorsResponseTypeDef,
    ListImportsRequestFiltersTypeDef,
    ListImportsResponseTypeDef,
    ListManagedAccountsResponseTypeDef,
    ListSourceServerActionsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTemplateActionsResponseTypeDef,
    ListWavesRequestFiltersTypeDef,
    ListWavesResponseTypeDef,
    PostLaunchActionsTypeDef,
    ReplicationConfigurationReplicatedDiskTypeDef,
    ReplicationConfigurationTemplateResponseMetadataTypeDef,
    ReplicationConfigurationTypeDef,
    S3BucketSourceTypeDef,
    SourceServerActionDocumentResponseMetadataTypeDef,
    SourceServerActionsRequestFiltersTypeDef,
    SourceServerConnectorActionTypeDef,
    SourceServerResponseMetadataTypeDef,
    SsmExternalParameterTypeDef,
    SsmParameterStoreParameterTypeDef,
    StartCutoverResponseTypeDef,
    StartExportResponseTypeDef,
    StartImportResponseTypeDef,
    StartTestResponseTypeDef,
    TemplateActionDocumentResponseMetadataTypeDef,
    TemplateActionsRequestFiltersTypeDef,
    TerminateTargetInstancesResponseTypeDef,
    WaveResponseMetadataTypeDef,
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        mgnClient exceptions.
        """

    def archive_application(
        self, *, applicationID: str, accountID: str = None
    ) -> ApplicationResponseMetadataTypeDef:
        """
        Archive application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.archive_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#archive_application)
        """

    def archive_wave(self, *, waveID: str, accountID: str = None) -> WaveResponseMetadataTypeDef:
        """
        Archive wave.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.archive_wave)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#archive_wave)
        """

    def associate_applications(
        self, *, applicationIDs: List[str], waveID: str, accountID: str = None
    ) -> Dict[str, Any]:
        """
        Associate applications to wave.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.associate_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#associate_applications)
        """

    def associate_source_servers(
        self, *, applicationID: str, sourceServerIDs: List[str], accountID: str = None
    ) -> Dict[str, Any]:
        """
        Associate source servers to application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.associate_source_servers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#associate_source_servers)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#can_paginate)
        """

    def change_server_life_cycle_state(
        self,
        *,
        lifeCycle: "ChangeServerLifeCycleStateSourceServerLifecycleTypeDef",
        sourceServerID: str,
        accountID: str = None
    ) -> SourceServerResponseMetadataTypeDef:
        """
        Allows the user to set the SourceServer.LifeCycle.state property for specific
        Source Server IDs to one of the following: READY_FOR_TEST or READY_FOR_CUTOVER.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.change_server_life_cycle_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#change_server_life_cycle_state)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#close)
        """

    def create_application(
        self,
        *,
        name: str,
        accountID: str = None,
        description: str = None,
        tags: Dict[str, str] = None
    ) -> ApplicationResponseMetadataTypeDef:
        """
        Create application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.create_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#create_application)
        """

    def create_connector(
        self,
        *,
        name: str,
        ssmInstanceID: str,
        ssmCommandConfig: "ConnectorSsmCommandConfigTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> ConnectorResponseMetadataTypeDef:
        """
        Create Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.create_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#create_connector)
        """

    def create_launch_configuration_template(
        self,
        *,
        associatePublicIpAddress: bool = None,
        bootMode: BootModeType = None,
        copyPrivateIp: bool = None,
        copyTags: bool = None,
        enableMapAutoTagging: bool = None,
        largeVolumeConf: "LaunchTemplateDiskConfTypeDef" = None,
        launchDisposition: LaunchDispositionType = None,
        licensing: "LicensingTypeDef" = None,
        mapAutoTaggingMpeID: str = None,
        postLaunchActions: "PostLaunchActionsTypeDef" = None,
        smallVolumeConf: "LaunchTemplateDiskConfTypeDef" = None,
        smallVolumeMaxSize: int = None,
        tags: Dict[str, str] = None,
        targetInstanceTypeRightSizingMethod: TargetInstanceTypeRightSizingMethodType = None
    ) -> LaunchConfigurationTemplateResponseMetadataTypeDef:
        """
        Creates a new Launch Configuration Template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.create_launch_configuration_template)
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
        tags: Dict[str, str] = None,
        useFipsEndpoint: bool = None
    ) -> ReplicationConfigurationTemplateResponseMetadataTypeDef:
        """
        Creates a new ReplicationConfigurationTemplate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.create_replication_configuration_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#create_replication_configuration_template)
        """

    def create_wave(
        self,
        *,
        name: str,
        accountID: str = None,
        description: str = None,
        tags: Dict[str, str] = None
    ) -> WaveResponseMetadataTypeDef:
        """
        Create wave.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.create_wave)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#create_wave)
        """

    def delete_application(self, *, applicationID: str, accountID: str = None) -> Dict[str, Any]:
        """
        Delete application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.delete_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#delete_application)
        """

    def delete_connector(self, *, connectorID: str) -> None:
        """
        Delete Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.delete_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#delete_connector)
        """

    def delete_job(self, *, jobID: str, accountID: str = None) -> Dict[str, Any]:
        """
        Deletes a single Job by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.delete_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#delete_job)
        """

    def delete_launch_configuration_template(
        self, *, launchConfigurationTemplateID: str
    ) -> Dict[str, Any]:
        """
        Deletes a single Launch Configuration Template by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.delete_launch_configuration_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#delete_launch_configuration_template)
        """

    def delete_replication_configuration_template(
        self, *, replicationConfigurationTemplateID: str
    ) -> Dict[str, Any]:
        """
        Deletes a single Replication Configuration Template by ID See also: `AWS API
        Documentation <https://docs.aws.amazon.com/goto/WebAPI/mgn-2020-02-
        26/DeleteReplicationConfigurationTemplate>`_ **Request Syntax** response =
        client.delete_replication_configuration_template( replication...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.delete_replication_configuration_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#delete_replication_configuration_template)
        """

    def delete_source_server(self, *, sourceServerID: str, accountID: str = None) -> Dict[str, Any]:
        """
        Deletes a single source server by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.delete_source_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#delete_source_server)
        """

    def delete_vcenter_client(self, *, vcenterClientID: str) -> None:
        """
        Deletes a given vCenter client by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.delete_vcenter_client)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#delete_vcenter_client)
        """

    def delete_wave(self, *, waveID: str, accountID: str = None) -> Dict[str, Any]:
        """
        Delete wave.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.delete_wave)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#delete_wave)
        """

    def describe_job_log_items(
        self, *, jobID: str, accountID: str = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeJobLogItemsResponseTypeDef:
        """
        Retrieves detailed job log items with paging.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.describe_job_log_items)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#describe_job_log_items)
        """

    def describe_jobs(
        self,
        *,
        accountID: str = None,
        filters: "DescribeJobsRequestFiltersTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeJobsResponseTypeDef:
        """
        Returns a list of Jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.describe_jobs)
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
        Lists all Launch Configuration Templates, filtered by Launch Configuration
        Template IDs See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/
        WebAPI/mgn-2020-02-26/DescribeLaunchConfigurationTemplates>`_ **Request Syntax**
        response = client.describe_launch_configuration_te...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.describe_launch_configuration_templates)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.describe_replication_configuration_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#describe_replication_configuration_templates)
        """

    def describe_source_servers(
        self,
        *,
        accountID: str = None,
        filters: "DescribeSourceServersRequestFiltersTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeSourceServersResponseTypeDef:
        """
        Retrieves all SourceServers or multiple SourceServers by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.describe_source_servers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#describe_source_servers)
        """

    def describe_vcenter_clients(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> DescribeVcenterClientsResponseTypeDef:
        """
        Returns a list of the installed vCenter clients.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.describe_vcenter_clients)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#describe_vcenter_clients)
        """

    def disassociate_applications(
        self, *, applicationIDs: List[str], waveID: str, accountID: str = None
    ) -> Dict[str, Any]:
        """
        Disassociate applications from wave.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.disassociate_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#disassociate_applications)
        """

    def disassociate_source_servers(
        self, *, applicationID: str, sourceServerIDs: List[str], accountID: str = None
    ) -> Dict[str, Any]:
        """
        Disassociate source servers from application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.disassociate_source_servers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#disassociate_source_servers)
        """

    def disconnect_from_service(
        self, *, sourceServerID: str, accountID: str = None
    ) -> SourceServerResponseMetadataTypeDef:
        """
        Disconnects specific Source Servers from Application Migration Service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.disconnect_from_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#disconnect_from_service)
        """

    def finalize_cutover(
        self, *, sourceServerID: str, accountID: str = None
    ) -> SourceServerResponseMetadataTypeDef:
        """
        Finalizes the cutover immediately for specific Source Servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.finalize_cutover)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#generate_presigned_url)
        """

    def get_launch_configuration(
        self, *, sourceServerID: str, accountID: str = None
    ) -> LaunchConfigurationTypeDef:
        """
        Lists all LaunchConfigurations available, filtered by Source Server IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.get_launch_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#get_launch_configuration)
        """

    def get_replication_configuration(
        self, *, sourceServerID: str, accountID: str = None
    ) -> ReplicationConfigurationTypeDef:
        """
        Lists all ReplicationConfigurations, filtered by Source Server ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.get_replication_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#get_replication_configuration)
        """

    def initialize_service(self) -> Dict[str, Any]:
        """
        Initialize Application Migration Service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.initialize_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#initialize_service)
        """

    def list_applications(
        self,
        *,
        accountID: str = None,
        filters: "ListApplicationsRequestFiltersTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListApplicationsResponseTypeDef:
        """
        Retrieves all applications or multiple applications by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.list_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#list_applications)
        """

    def list_connectors(
        self,
        *,
        filters: "ListConnectorsRequestFiltersTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListConnectorsResponseTypeDef:
        """
        List Connectors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.list_connectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#list_connectors)
        """

    def list_export_errors(
        self, *, exportID: str, maxResults: int = None, nextToken: str = None
    ) -> ListExportErrorsResponseTypeDef:
        """
        List export errors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.list_export_errors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#list_export_errors)
        """

    def list_exports(
        self,
        *,
        filters: "ListExportsRequestFiltersTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListExportsResponseTypeDef:
        """
        List exports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.list_exports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#list_exports)
        """

    def list_import_errors(
        self, *, importID: str, maxResults: int = None, nextToken: str = None
    ) -> ListImportErrorsResponseTypeDef:
        """
        List import errors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.list_import_errors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#list_import_errors)
        """

    def list_imports(
        self,
        *,
        filters: "ListImportsRequestFiltersTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListImportsResponseTypeDef:
        """
        List imports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.list_imports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#list_imports)
        """

    def list_managed_accounts(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListManagedAccountsResponseTypeDef:
        """
        List Managed Accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.list_managed_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#list_managed_accounts)
        """

    def list_source_server_actions(
        self,
        *,
        sourceServerID: str,
        accountID: str = None,
        filters: "SourceServerActionsRequestFiltersTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListSourceServerActionsResponseTypeDef:
        """
        List source server post migration custom actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.list_source_server_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#list_source_server_actions)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        List all tags for your Application Migration Service resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#list_tags_for_resource)
        """

    def list_template_actions(
        self,
        *,
        launchConfigurationTemplateID: str,
        filters: "TemplateActionsRequestFiltersTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListTemplateActionsResponseTypeDef:
        """
        List template post migration custom actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.list_template_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#list_template_actions)
        """

    def list_waves(
        self,
        *,
        accountID: str = None,
        filters: "ListWavesRequestFiltersTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListWavesResponseTypeDef:
        """
        Retrieves all waves or multiple waves by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.list_waves)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#list_waves)
        """

    def mark_as_archived(
        self, *, sourceServerID: str, accountID: str = None
    ) -> SourceServerResponseMetadataTypeDef:
        """
        Archives specific Source Servers by setting the SourceServer.isArchived property
        to true for specified SourceServers by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.mark_as_archived)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#mark_as_archived)
        """

    def pause_replication(
        self, *, sourceServerID: str, accountID: str = None
    ) -> SourceServerResponseMetadataTypeDef:
        """
        Pause Replication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.pause_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#pause_replication)
        """

    def put_source_server_action(
        self,
        *,
        actionID: str,
        actionName: str,
        documentIdentifier: str,
        order: int,
        sourceServerID: str,
        accountID: str = None,
        active: bool = None,
        category: ActionCategoryType = None,
        description: str = None,
        documentVersion: str = None,
        externalParameters: Dict[str, "SsmExternalParameterTypeDef"] = None,
        mustSucceedForCutover: bool = None,
        parameters: Dict[str, List["SsmParameterStoreParameterTypeDef"]] = None,
        timeoutSeconds: int = None
    ) -> SourceServerActionDocumentResponseMetadataTypeDef:
        """
        Put source server post migration custom action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.put_source_server_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#put_source_server_action)
        """

    def put_template_action(
        self,
        *,
        actionID: str,
        actionName: str,
        documentIdentifier: str,
        launchConfigurationTemplateID: str,
        order: int,
        active: bool = None,
        category: ActionCategoryType = None,
        description: str = None,
        documentVersion: str = None,
        externalParameters: Dict[str, "SsmExternalParameterTypeDef"] = None,
        mustSucceedForCutover: bool = None,
        operatingSystem: str = None,
        parameters: Dict[str, List["SsmParameterStoreParameterTypeDef"]] = None,
        timeoutSeconds: int = None
    ) -> TemplateActionDocumentResponseMetadataTypeDef:
        """
        Put template post migration custom action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.put_template_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#put_template_action)
        """

    def remove_source_server_action(
        self, *, actionID: str, sourceServerID: str, accountID: str = None
    ) -> Dict[str, Any]:
        """
        Remove source server post migration custom action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.remove_source_server_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#remove_source_server_action)
        """

    def remove_template_action(
        self, *, actionID: str, launchConfigurationTemplateID: str
    ) -> Dict[str, Any]:
        """
        Remove template post migration custom action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.remove_template_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#remove_template_action)
        """

    def resume_replication(
        self, *, sourceServerID: str, accountID: str = None
    ) -> SourceServerResponseMetadataTypeDef:
        """
        Resume Replication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.resume_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#resume_replication)
        """

    def retry_data_replication(
        self, *, sourceServerID: str, accountID: str = None
    ) -> SourceServerResponseMetadataTypeDef:
        """
        Causes the data replication initiation sequence to begin immediately upon next
        Handshake for specified SourceServer IDs, regardless of when the previous
        initiation started.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.retry_data_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#retry_data_replication)
        """

    def start_cutover(
        self, *, sourceServerIDs: List[str], accountID: str = None, tags: Dict[str, str] = None
    ) -> StartCutoverResponseTypeDef:
        """
        Launches a Cutover Instance for specific Source Servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.start_cutover)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#start_cutover)
        """

    def start_export(
        self, *, s3Bucket: str, s3Key: str, s3BucketOwner: str = None
    ) -> StartExportResponseTypeDef:
        """
        Start export.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.start_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#start_export)
        """

    def start_import(
        self, *, s3BucketSource: "S3BucketSourceTypeDef", clientToken: str = None
    ) -> StartImportResponseTypeDef:
        """
        Start import.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.start_import)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#start_import)
        """

    def start_replication(
        self, *, sourceServerID: str, accountID: str = None
    ) -> SourceServerResponseMetadataTypeDef:
        """
        Starts replication for SNAPSHOT_SHIPPING agents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.start_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#start_replication)
        """

    def start_test(
        self, *, sourceServerIDs: List[str], accountID: str = None, tags: Dict[str, str] = None
    ) -> StartTestResponseTypeDef:
        """
        Launches a Test Instance for specific Source Servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.start_test)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#start_test)
        """

    def stop_replication(
        self, *, sourceServerID: str, accountID: str = None
    ) -> SourceServerResponseMetadataTypeDef:
        """
        Stop Replication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.stop_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#stop_replication)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> None:
        """
        Adds or overwrites only the specified tags for the specified Application
        Migration Service resource or resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#tag_resource)
        """

    def terminate_target_instances(
        self, *, sourceServerIDs: List[str], accountID: str = None, tags: Dict[str, str] = None
    ) -> TerminateTargetInstancesResponseTypeDef:
        """
        Starts a job that terminates specific launched EC2 Test and Cutover instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.terminate_target_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#terminate_target_instances)
        """

    def unarchive_application(
        self, *, applicationID: str, accountID: str = None
    ) -> ApplicationResponseMetadataTypeDef:
        """
        Unarchive application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.unarchive_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#unarchive_application)
        """

    def unarchive_wave(self, *, waveID: str, accountID: str = None) -> WaveResponseMetadataTypeDef:
        """
        Unarchive wave.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.unarchive_wave)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#unarchive_wave)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> None:
        """
        Deletes the specified set of tags from the specified set of Application
        Migration Service resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#untag_resource)
        """

    def update_application(
        self,
        *,
        applicationID: str,
        accountID: str = None,
        description: str = None,
        name: str = None
    ) -> ApplicationResponseMetadataTypeDef:
        """
        Update application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.update_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#update_application)
        """

    def update_connector(
        self,
        *,
        connectorID: str,
        name: str = None,
        ssmCommandConfig: "ConnectorSsmCommandConfigTypeDef" = None
    ) -> ConnectorResponseMetadataTypeDef:
        """
        Update Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.update_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#update_connector)
        """

    def update_launch_configuration(
        self,
        *,
        sourceServerID: str,
        accountID: str = None,
        bootMode: BootModeType = None,
        copyPrivateIp: bool = None,
        copyTags: bool = None,
        enableMapAutoTagging: bool = None,
        launchDisposition: LaunchDispositionType = None,
        licensing: "LicensingTypeDef" = None,
        mapAutoTaggingMpeID: str = None,
        name: str = None,
        postLaunchActions: "PostLaunchActionsTypeDef" = None,
        targetInstanceTypeRightSizingMethod: TargetInstanceTypeRightSizingMethodType = None
    ) -> LaunchConfigurationTypeDef:
        """
        Updates multiple LaunchConfigurations by Source Server ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.update_launch_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#update_launch_configuration)
        """

    def update_launch_configuration_template(
        self,
        *,
        launchConfigurationTemplateID: str,
        associatePublicIpAddress: bool = None,
        bootMode: BootModeType = None,
        copyPrivateIp: bool = None,
        copyTags: bool = None,
        enableMapAutoTagging: bool = None,
        largeVolumeConf: "LaunchTemplateDiskConfTypeDef" = None,
        launchDisposition: LaunchDispositionType = None,
        licensing: "LicensingTypeDef" = None,
        mapAutoTaggingMpeID: str = None,
        postLaunchActions: "PostLaunchActionsTypeDef" = None,
        smallVolumeConf: "LaunchTemplateDiskConfTypeDef" = None,
        smallVolumeMaxSize: int = None,
        targetInstanceTypeRightSizingMethod: TargetInstanceTypeRightSizingMethodType = None
    ) -> LaunchConfigurationTemplateResponseMetadataTypeDef:
        """
        Updates an existing Launch Configuration Template by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.update_launch_configuration_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#update_launch_configuration_template)
        """

    def update_replication_configuration(
        self,
        *,
        sourceServerID: str,
        accountID: str = None,
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
        useDedicatedReplicationServer: bool = None,
        useFipsEndpoint: bool = None
    ) -> ReplicationConfigurationTypeDef:
        """
        Allows you to update multiple ReplicationConfigurations by Source Server ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.update_replication_configuration)
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
        useDedicatedReplicationServer: bool = None,
        useFipsEndpoint: bool = None
    ) -> ReplicationConfigurationTemplateResponseMetadataTypeDef:
        """
        Updates multiple ReplicationConfigurationTemplates by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.update_replication_configuration_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#update_replication_configuration_template)
        """

    def update_source_server(
        self,
        *,
        sourceServerID: str,
        accountID: str = None,
        connectorAction: "SourceServerConnectorActionTypeDef" = None
    ) -> SourceServerResponseMetadataTypeDef:
        """
        Update Source Server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.update_source_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#update_source_server)
        """

    def update_source_server_replication_type(
        self, *, replicationType: ReplicationTypeType, sourceServerID: str, accountID: str = None
    ) -> SourceServerResponseMetadataTypeDef:
        """
        Allows you to change between the AGENT_BASED replication type and the
        SNAPSHOT_SHIPPING replication type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.update_source_server_replication_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#update_source_server_replication_type)
        """

    def update_wave(
        self, *, waveID: str, accountID: str = None, description: str = None, name: str = None
    ) -> WaveResponseMetadataTypeDef:
        """
        Update wave.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Client.update_wave)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#update_wave)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_job_log_items"]
    ) -> DescribeJobLogItemsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Paginator.DescribeJobLogItems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describejoblogitemspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_jobs"]) -> DescribeJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Paginator.DescribeJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describejobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_launch_configuration_templates"]
    ) -> DescribeLaunchConfigurationTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Paginator.DescribeLaunchConfigurationTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describelaunchconfigurationtemplatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_configuration_templates"]
    ) -> DescribeReplicationConfigurationTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Paginator.DescribeReplicationConfigurationTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describereplicationconfigurationtemplatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_source_servers"]
    ) -> DescribeSourceServersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Paginator.DescribeSourceServers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describesourceserverspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vcenter_clients"]
    ) -> DescribeVcenterClientsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Paginator.DescribeVcenterClients)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describevcenterclientspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Paginator.ListApplications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#listapplicationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_connectors"]) -> ListConnectorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Paginator.ListConnectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#listconnectorspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_export_errors"]
    ) -> ListExportErrorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Paginator.ListExportErrors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#listexporterrorspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_exports"]) -> ListExportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Paginator.ListExports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#listexportspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_import_errors"]
    ) -> ListImportErrorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Paginator.ListImportErrors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#listimporterrorspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_imports"]) -> ListImportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Paginator.ListImports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#listimportspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_managed_accounts"]
    ) -> ListManagedAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Paginator.ListManagedAccounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#listmanagedaccountspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_source_server_actions"]
    ) -> ListSourceServerActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Paginator.ListSourceServerActions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#listsourceserveractionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_template_actions"]
    ) -> ListTemplateActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Paginator.ListTemplateActions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#listtemplateactionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_waves"]) -> ListWavesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mgn.html#mgn.Paginator.ListWaves)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#listwavespaginator)
        """
