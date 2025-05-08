"""
Type annotations for drs service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_drs.client import DrsClient

    session = Session()
    client: DrsClient = session.client("drs")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeJobLogItemsPaginator,
    DescribeJobsPaginator,
    DescribeLaunchConfigurationTemplatesPaginator,
    DescribeRecoveryInstancesPaginator,
    DescribeRecoverySnapshotsPaginator,
    DescribeReplicationConfigurationTemplatesPaginator,
    DescribeSourceNetworksPaginator,
    DescribeSourceServersPaginator,
    ListExtensibleSourceServersPaginator,
    ListLaunchActionsPaginator,
    ListStagingAccountsPaginator,
)
from .type_defs import (
    AssociateSourceNetworkStackRequestTypeDef,
    AssociateSourceNetworkStackResponseTypeDef,
    CreateExtendedSourceServerRequestTypeDef,
    CreateExtendedSourceServerResponseTypeDef,
    CreateLaunchConfigurationTemplateRequestTypeDef,
    CreateLaunchConfigurationTemplateResponseTypeDef,
    CreateReplicationConfigurationTemplateRequestTypeDef,
    CreateSourceNetworkRequestTypeDef,
    CreateSourceNetworkResponseTypeDef,
    DeleteJobRequestTypeDef,
    DeleteLaunchActionRequestTypeDef,
    DeleteLaunchConfigurationTemplateRequestTypeDef,
    DeleteRecoveryInstanceRequestTypeDef,
    DeleteReplicationConfigurationTemplateRequestTypeDef,
    DeleteSourceNetworkRequestTypeDef,
    DeleteSourceServerRequestTypeDef,
    DescribeJobLogItemsRequestTypeDef,
    DescribeJobLogItemsResponseTypeDef,
    DescribeJobsRequestTypeDef,
    DescribeJobsResponseTypeDef,
    DescribeLaunchConfigurationTemplatesRequestTypeDef,
    DescribeLaunchConfigurationTemplatesResponseTypeDef,
    DescribeRecoveryInstancesRequestTypeDef,
    DescribeRecoveryInstancesResponseTypeDef,
    DescribeRecoverySnapshotsRequestTypeDef,
    DescribeRecoverySnapshotsResponseTypeDef,
    DescribeReplicationConfigurationTemplatesRequestTypeDef,
    DescribeReplicationConfigurationTemplatesResponseTypeDef,
    DescribeSourceNetworksRequestTypeDef,
    DescribeSourceNetworksResponseTypeDef,
    DescribeSourceServersRequestTypeDef,
    DescribeSourceServersResponseTypeDef,
    DisconnectRecoveryInstanceRequestTypeDef,
    DisconnectSourceServerRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    ExportSourceNetworkCfnTemplateRequestTypeDef,
    ExportSourceNetworkCfnTemplateResponseTypeDef,
    GetFailbackReplicationConfigurationRequestTypeDef,
    GetFailbackReplicationConfigurationResponseTypeDef,
    GetLaunchConfigurationRequestTypeDef,
    GetReplicationConfigurationRequestTypeDef,
    LaunchConfigurationTypeDef,
    ListExtensibleSourceServersRequestTypeDef,
    ListExtensibleSourceServersResponseTypeDef,
    ListLaunchActionsRequestTypeDef,
    ListLaunchActionsResponseTypeDef,
    ListStagingAccountsRequestTypeDef,
    ListStagingAccountsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutLaunchActionRequestTypeDef,
    PutLaunchActionResponseTypeDef,
    ReplicationConfigurationTemplateResponseTypeDef,
    ReplicationConfigurationTypeDef,
    RetryDataReplicationRequestTypeDef,
    ReverseReplicationRequestTypeDef,
    ReverseReplicationResponseTypeDef,
    SourceServerResponseTypeDef,
    StartFailbackLaunchRequestTypeDef,
    StartFailbackLaunchResponseTypeDef,
    StartRecoveryRequestTypeDef,
    StartRecoveryResponseTypeDef,
    StartReplicationRequestTypeDef,
    StartReplicationResponseTypeDef,
    StartSourceNetworkRecoveryRequestTypeDef,
    StartSourceNetworkRecoveryResponseTypeDef,
    StartSourceNetworkReplicationRequestTypeDef,
    StartSourceNetworkReplicationResponseTypeDef,
    StopFailbackRequestTypeDef,
    StopReplicationRequestTypeDef,
    StopReplicationResponseTypeDef,
    StopSourceNetworkReplicationRequestTypeDef,
    StopSourceNetworkReplicationResponseTypeDef,
    TagResourceRequestTypeDef,
    TerminateRecoveryInstancesRequestTypeDef,
    TerminateRecoveryInstancesResponseTypeDef,
    UntagResourceRequestTypeDef,
    UpdateFailbackReplicationConfigurationRequestTypeDef,
    UpdateLaunchConfigurationRequestTypeDef,
    UpdateLaunchConfigurationTemplateRequestTypeDef,
    UpdateLaunchConfigurationTemplateResponseTypeDef,
    UpdateReplicationConfigurationRequestTypeDef,
    UpdateReplicationConfigurationTemplateRequestTypeDef,
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

__all__ = ("DrsClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UninitializedAccountException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class DrsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs.html#Drs.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DrsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs.html#Drs.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#generate_presigned_url)
        """

    def associate_source_network_stack(
        self, **kwargs: Unpack[AssociateSourceNetworkStackRequestTypeDef]
    ) -> AssociateSourceNetworkStackResponseTypeDef:
        """
        Associate a Source Network to an existing CloudFormation Stack and modify
        launch templates to use this network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/associate_source_network_stack.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#associate_source_network_stack)
        """

    def create_extended_source_server(
        self, **kwargs: Unpack[CreateExtendedSourceServerRequestTypeDef]
    ) -> CreateExtendedSourceServerResponseTypeDef:
        """
        Create an extended source server in the target Account based on the source
        server in staging account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/create_extended_source_server.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#create_extended_source_server)
        """

    def create_launch_configuration_template(
        self, **kwargs: Unpack[CreateLaunchConfigurationTemplateRequestTypeDef]
    ) -> CreateLaunchConfigurationTemplateResponseTypeDef:
        """
        Creates a new Launch Configuration Template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/create_launch_configuration_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#create_launch_configuration_template)
        """

    def create_replication_configuration_template(
        self, **kwargs: Unpack[CreateReplicationConfigurationTemplateRequestTypeDef]
    ) -> ReplicationConfigurationTemplateResponseTypeDef:
        """
        Creates a new ReplicationConfigurationTemplate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/create_replication_configuration_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#create_replication_configuration_template)
        """

    def create_source_network(
        self, **kwargs: Unpack[CreateSourceNetworkRequestTypeDef]
    ) -> CreateSourceNetworkResponseTypeDef:
        """
        Create a new Source Network resource for a provided VPC ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/create_source_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#create_source_network)
        """

    def delete_job(self, **kwargs: Unpack[DeleteJobRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a single Job by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/delete_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#delete_job)
        """

    def delete_launch_action(
        self, **kwargs: Unpack[DeleteLaunchActionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a resource launch action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/delete_launch_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#delete_launch_action)
        """

    def delete_launch_configuration_template(
        self, **kwargs: Unpack[DeleteLaunchConfigurationTemplateRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a single Launch Configuration Template by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/delete_launch_configuration_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#delete_launch_configuration_template)
        """

    def delete_recovery_instance(
        self, **kwargs: Unpack[DeleteRecoveryInstanceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a single Recovery Instance by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/delete_recovery_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#delete_recovery_instance)
        """

    def delete_replication_configuration_template(
        self, **kwargs: Unpack[DeleteReplicationConfigurationTemplateRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a single Replication Configuration Template by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/delete_replication_configuration_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#delete_replication_configuration_template)
        """

    def delete_source_network(
        self, **kwargs: Unpack[DeleteSourceNetworkRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete Source Network resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/delete_source_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#delete_source_network)
        """

    def delete_source_server(
        self, **kwargs: Unpack[DeleteSourceServerRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a single Source Server by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/delete_source_server.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#delete_source_server)
        """

    def describe_job_log_items(
        self, **kwargs: Unpack[DescribeJobLogItemsRequestTypeDef]
    ) -> DescribeJobLogItemsResponseTypeDef:
        """
        Retrieves a detailed Job log with pagination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/describe_job_log_items.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#describe_job_log_items)
        """

    def describe_jobs(
        self, **kwargs: Unpack[DescribeJobsRequestTypeDef]
    ) -> DescribeJobsResponseTypeDef:
        """
        Returns a list of Jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/describe_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#describe_jobs)
        """

    def describe_launch_configuration_templates(
        self, **kwargs: Unpack[DescribeLaunchConfigurationTemplatesRequestTypeDef]
    ) -> DescribeLaunchConfigurationTemplatesResponseTypeDef:
        """
        Lists all Launch Configuration Templates, filtered by Launch Configuration
        Template IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/describe_launch_configuration_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#describe_launch_configuration_templates)
        """

    def describe_recovery_instances(
        self, **kwargs: Unpack[DescribeRecoveryInstancesRequestTypeDef]
    ) -> DescribeRecoveryInstancesResponseTypeDef:
        """
        Lists all Recovery Instances or multiple Recovery Instances by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/describe_recovery_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#describe_recovery_instances)
        """

    def describe_recovery_snapshots(
        self, **kwargs: Unpack[DescribeRecoverySnapshotsRequestTypeDef]
    ) -> DescribeRecoverySnapshotsResponseTypeDef:
        """
        Lists all Recovery Snapshots for a single Source Server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/describe_recovery_snapshots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#describe_recovery_snapshots)
        """

    def describe_replication_configuration_templates(
        self, **kwargs: Unpack[DescribeReplicationConfigurationTemplatesRequestTypeDef]
    ) -> DescribeReplicationConfigurationTemplatesResponseTypeDef:
        """
        Lists all ReplicationConfigurationTemplates, filtered by Source Server IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/describe_replication_configuration_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#describe_replication_configuration_templates)
        """

    def describe_source_networks(
        self, **kwargs: Unpack[DescribeSourceNetworksRequestTypeDef]
    ) -> DescribeSourceNetworksResponseTypeDef:
        """
        Lists all Source Networks or multiple Source Networks filtered by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/describe_source_networks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#describe_source_networks)
        """

    def describe_source_servers(
        self, **kwargs: Unpack[DescribeSourceServersRequestTypeDef]
    ) -> DescribeSourceServersResponseTypeDef:
        """
        Lists all Source Servers or multiple Source Servers filtered by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/describe_source_servers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#describe_source_servers)
        """

    def disconnect_recovery_instance(
        self, **kwargs: Unpack[DisconnectRecoveryInstanceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disconnect a Recovery Instance from Elastic Disaster Recovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/disconnect_recovery_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#disconnect_recovery_instance)
        """

    def disconnect_source_server(
        self, **kwargs: Unpack[DisconnectSourceServerRequestTypeDef]
    ) -> SourceServerResponseTypeDef:
        """
        Disconnects a specific Source Server from Elastic Disaster Recovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/disconnect_source_server.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#disconnect_source_server)
        """

    def export_source_network_cfn_template(
        self, **kwargs: Unpack[ExportSourceNetworkCfnTemplateRequestTypeDef]
    ) -> ExportSourceNetworkCfnTemplateResponseTypeDef:
        """
        Export the Source Network CloudFormation template to an S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/export_source_network_cfn_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#export_source_network_cfn_template)
        """

    def get_failback_replication_configuration(
        self, **kwargs: Unpack[GetFailbackReplicationConfigurationRequestTypeDef]
    ) -> GetFailbackReplicationConfigurationResponseTypeDef:
        """
        Lists all Failback ReplicationConfigurations, filtered by Recovery Instance ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/get_failback_replication_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#get_failback_replication_configuration)
        """

    def get_launch_configuration(
        self, **kwargs: Unpack[GetLaunchConfigurationRequestTypeDef]
    ) -> LaunchConfigurationTypeDef:
        """
        Gets a LaunchConfiguration, filtered by Source Server IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/get_launch_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#get_launch_configuration)
        """

    def get_replication_configuration(
        self, **kwargs: Unpack[GetReplicationConfigurationRequestTypeDef]
    ) -> ReplicationConfigurationTypeDef:
        """
        Gets a ReplicationConfiguration, filtered by Source Server ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/get_replication_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#get_replication_configuration)
        """

    def initialize_service(self) -> Dict[str, Any]:
        """
        Initialize Elastic Disaster Recovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/initialize_service.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#initialize_service)
        """

    def list_extensible_source_servers(
        self, **kwargs: Unpack[ListExtensibleSourceServersRequestTypeDef]
    ) -> ListExtensibleSourceServersResponseTypeDef:
        """
        Returns a list of source servers on a staging account that are extensible,
        which means that: a.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/list_extensible_source_servers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#list_extensible_source_servers)
        """

    def list_launch_actions(
        self, **kwargs: Unpack[ListLaunchActionsRequestTypeDef]
    ) -> ListLaunchActionsResponseTypeDef:
        """
        Lists resource launch actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/list_launch_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#list_launch_actions)
        """

    def list_staging_accounts(
        self, **kwargs: Unpack[ListStagingAccountsRequestTypeDef]
    ) -> ListStagingAccountsResponseTypeDef:
        """
        Returns an array of staging accounts for existing extended source servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/list_staging_accounts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#list_staging_accounts)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List all tags for your Elastic Disaster Recovery resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#list_tags_for_resource)
        """

    def put_launch_action(
        self, **kwargs: Unpack[PutLaunchActionRequestTypeDef]
    ) -> PutLaunchActionResponseTypeDef:
        """
        Puts a resource launch action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/put_launch_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#put_launch_action)
        """

    def retry_data_replication(
        self, **kwargs: Unpack[RetryDataReplicationRequestTypeDef]
    ) -> SourceServerResponseTypeDef:
        """
        WARNING: RetryDataReplication is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/retry_data_replication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#retry_data_replication)
        """

    def reverse_replication(
        self, **kwargs: Unpack[ReverseReplicationRequestTypeDef]
    ) -> ReverseReplicationResponseTypeDef:
        """
        Start replication to origin / target region - applies only to protected
        instances that originated in EC2.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/reverse_replication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#reverse_replication)
        """

    def start_failback_launch(
        self, **kwargs: Unpack[StartFailbackLaunchRequestTypeDef]
    ) -> StartFailbackLaunchResponseTypeDef:
        """
        Initiates a Job for launching the machine that is being failed back to from the
        specified Recovery Instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/start_failback_launch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#start_failback_launch)
        """

    def start_recovery(
        self, **kwargs: Unpack[StartRecoveryRequestTypeDef]
    ) -> StartRecoveryResponseTypeDef:
        """
        Launches Recovery Instances for the specified Source Servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/start_recovery.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#start_recovery)
        """

    def start_replication(
        self, **kwargs: Unpack[StartReplicationRequestTypeDef]
    ) -> StartReplicationResponseTypeDef:
        """
        Starts replication for a stopped Source Server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/start_replication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#start_replication)
        """

    def start_source_network_recovery(
        self, **kwargs: Unpack[StartSourceNetworkRecoveryRequestTypeDef]
    ) -> StartSourceNetworkRecoveryResponseTypeDef:
        """
        Deploy VPC for the specified Source Network and modify launch templates to use
        this network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/start_source_network_recovery.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#start_source_network_recovery)
        """

    def start_source_network_replication(
        self, **kwargs: Unpack[StartSourceNetworkReplicationRequestTypeDef]
    ) -> StartSourceNetworkReplicationResponseTypeDef:
        """
        Starts replication for a Source Network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/start_source_network_replication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#start_source_network_replication)
        """

    def stop_failback(
        self, **kwargs: Unpack[StopFailbackRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops the failback process for a specified Recovery Instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/stop_failback.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#stop_failback)
        """

    def stop_replication(
        self, **kwargs: Unpack[StopReplicationRequestTypeDef]
    ) -> StopReplicationResponseTypeDef:
        """
        Stops replication for a Source Server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/stop_replication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#stop_replication)
        """

    def stop_source_network_replication(
        self, **kwargs: Unpack[StopSourceNetworkReplicationRequestTypeDef]
    ) -> StopSourceNetworkReplicationResponseTypeDef:
        """
        Stops replication for a Source Network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/stop_source_network_replication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#stop_source_network_replication)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds or overwrites only the specified tags for the specified Elastic Disaster
        Recovery resource or resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#tag_resource)
        """

    def terminate_recovery_instances(
        self, **kwargs: Unpack[TerminateRecoveryInstancesRequestTypeDef]
    ) -> TerminateRecoveryInstancesResponseTypeDef:
        """
        Initiates a Job for terminating the EC2 resources associated with the specified
        Recovery Instances, and then will delete the Recovery Instances from the
        Elastic Disaster Recovery service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/terminate_recovery_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#terminate_recovery_instances)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified set of tags from the specified set of Elastic Disaster
        Recovery resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#untag_resource)
        """

    def update_failback_replication_configuration(
        self, **kwargs: Unpack[UpdateFailbackReplicationConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Allows you to update the failback replication configuration of a Recovery
        Instance by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/update_failback_replication_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#update_failback_replication_configuration)
        """

    def update_launch_configuration(
        self, **kwargs: Unpack[UpdateLaunchConfigurationRequestTypeDef]
    ) -> LaunchConfigurationTypeDef:
        """
        Updates a LaunchConfiguration by Source Server ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/update_launch_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#update_launch_configuration)
        """

    def update_launch_configuration_template(
        self, **kwargs: Unpack[UpdateLaunchConfigurationTemplateRequestTypeDef]
    ) -> UpdateLaunchConfigurationTemplateResponseTypeDef:
        """
        Updates an existing Launch Configuration Template by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/update_launch_configuration_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#update_launch_configuration_template)
        """

    def update_replication_configuration(
        self, **kwargs: Unpack[UpdateReplicationConfigurationRequestTypeDef]
    ) -> ReplicationConfigurationTypeDef:
        """
        Allows you to update a ReplicationConfiguration by Source Server ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/update_replication_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#update_replication_configuration)
        """

    def update_replication_configuration_template(
        self, **kwargs: Unpack[UpdateReplicationConfigurationTemplateRequestTypeDef]
    ) -> ReplicationConfigurationTemplateResponseTypeDef:
        """
        Updates a ReplicationConfigurationTemplate by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/update_replication_configuration_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#update_replication_configuration_template)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_job_log_items"]
    ) -> DescribeJobLogItemsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_jobs"]
    ) -> DescribeJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_launch_configuration_templates"]
    ) -> DescribeLaunchConfigurationTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_recovery_instances"]
    ) -> DescribeRecoveryInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_recovery_snapshots"]
    ) -> DescribeRecoverySnapshotsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_replication_configuration_templates"]
    ) -> DescribeReplicationConfigurationTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_source_networks"]
    ) -> DescribeSourceNetworksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_source_servers"]
    ) -> DescribeSourceServersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_extensible_source_servers"]
    ) -> ListExtensibleSourceServersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_launch_actions"]
    ) -> ListLaunchActionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_staging_accounts"]
    ) -> ListStagingAccountsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/client/#get_paginator)
        """
