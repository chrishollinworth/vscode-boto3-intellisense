"""
Type annotations for odb service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_odb.client import OdbClient

    session = Session()
    client: OdbClient = session.client("odb")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAutonomousVirtualMachinesPaginator,
    ListCloudAutonomousVmClustersPaginator,
    ListCloudExadataInfrastructuresPaginator,
    ListCloudVmClustersPaginator,
    ListDbNodesPaginator,
    ListDbServersPaginator,
    ListDbSystemShapesPaginator,
    ListGiVersionsPaginator,
    ListOdbNetworksPaginator,
    ListOdbPeeringConnectionsPaginator,
    ListSystemVersionsPaginator,
)
from .type_defs import (
    AcceptMarketplaceRegistrationInputTypeDef,
    AssociateIamRoleToResourceInputTypeDef,
    CreateCloudAutonomousVmClusterInputTypeDef,
    CreateCloudAutonomousVmClusterOutputTypeDef,
    CreateCloudExadataInfrastructureInputTypeDef,
    CreateCloudExadataInfrastructureOutputTypeDef,
    CreateCloudVmClusterInputTypeDef,
    CreateCloudVmClusterOutputTypeDef,
    CreateOdbNetworkInputTypeDef,
    CreateOdbNetworkOutputTypeDef,
    CreateOdbPeeringConnectionInputTypeDef,
    CreateOdbPeeringConnectionOutputTypeDef,
    DeleteCloudAutonomousVmClusterInputTypeDef,
    DeleteCloudExadataInfrastructureInputTypeDef,
    DeleteCloudVmClusterInputTypeDef,
    DeleteOdbNetworkInputTypeDef,
    DeleteOdbPeeringConnectionInputTypeDef,
    DisassociateIamRoleFromResourceInputTypeDef,
    GetCloudAutonomousVmClusterInputTypeDef,
    GetCloudAutonomousVmClusterOutputTypeDef,
    GetCloudExadataInfrastructureInputTypeDef,
    GetCloudExadataInfrastructureOutputTypeDef,
    GetCloudExadataInfrastructureUnallocatedResourcesInputTypeDef,
    GetCloudExadataInfrastructureUnallocatedResourcesOutputTypeDef,
    GetCloudVmClusterInputTypeDef,
    GetCloudVmClusterOutputTypeDef,
    GetDbNodeInputTypeDef,
    GetDbNodeOutputTypeDef,
    GetDbServerInputTypeDef,
    GetDbServerOutputTypeDef,
    GetOciOnboardingStatusOutputTypeDef,
    GetOdbNetworkInputTypeDef,
    GetOdbNetworkOutputTypeDef,
    GetOdbPeeringConnectionInputTypeDef,
    GetOdbPeeringConnectionOutputTypeDef,
    InitializeServiceInputTypeDef,
    ListAutonomousVirtualMachinesInputTypeDef,
    ListAutonomousVirtualMachinesOutputTypeDef,
    ListCloudAutonomousVmClustersInputTypeDef,
    ListCloudAutonomousVmClustersOutputTypeDef,
    ListCloudExadataInfrastructuresInputTypeDef,
    ListCloudExadataInfrastructuresOutputTypeDef,
    ListCloudVmClustersInputTypeDef,
    ListCloudVmClustersOutputTypeDef,
    ListDbNodesInputTypeDef,
    ListDbNodesOutputTypeDef,
    ListDbServersInputTypeDef,
    ListDbServersOutputTypeDef,
    ListDbSystemShapesInputTypeDef,
    ListDbSystemShapesOutputTypeDef,
    ListGiVersionsInputTypeDef,
    ListGiVersionsOutputTypeDef,
    ListOdbNetworksInputTypeDef,
    ListOdbNetworksOutputTypeDef,
    ListOdbPeeringConnectionsInputTypeDef,
    ListOdbPeeringConnectionsOutputTypeDef,
    ListSystemVersionsInputTypeDef,
    ListSystemVersionsOutputTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    RebootDbNodeInputTypeDef,
    RebootDbNodeOutputTypeDef,
    StartDbNodeInputTypeDef,
    StartDbNodeOutputTypeDef,
    StopDbNodeInputTypeDef,
    StopDbNodeOutputTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateCloudExadataInfrastructureInputTypeDef,
    UpdateCloudExadataInfrastructureOutputTypeDef,
    UpdateOdbNetworkInputTypeDef,
    UpdateOdbNetworkOutputTypeDef,
    UpdateOdbPeeringConnectionInputTypeDef,
    UpdateOdbPeeringConnectionOutputTypeDef,
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

__all__ = ("OdbClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class OdbClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb.html#Odb.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        OdbClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb.html#Odb.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#generate_presigned_url)
        """

    def accept_marketplace_registration(
        self, **kwargs: Unpack[AcceptMarketplaceRegistrationInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Registers the Amazon Web Services Marketplace token for your Amazon Web
        Services account to activate your Oracle Database@Amazon Web Services
        subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/accept_marketplace_registration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#accept_marketplace_registration)
        """

    def associate_iam_role_to_resource(
        self, **kwargs: Unpack[AssociateIamRoleToResourceInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates an Amazon Web Services Identity and Access Management (IAM) service
        role with a specified resource to enable Amazon Web Services service
        integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/associate_iam_role_to_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#associate_iam_role_to_resource)
        """

    def create_cloud_autonomous_vm_cluster(
        self, **kwargs: Unpack[CreateCloudAutonomousVmClusterInputTypeDef]
    ) -> CreateCloudAutonomousVmClusterOutputTypeDef:
        """
        Creates a new Autonomous VM cluster in the specified Exadata infrastructure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/create_cloud_autonomous_vm_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#create_cloud_autonomous_vm_cluster)
        """

    def create_cloud_exadata_infrastructure(
        self, **kwargs: Unpack[CreateCloudExadataInfrastructureInputTypeDef]
    ) -> CreateCloudExadataInfrastructureOutputTypeDef:
        """
        Creates an Exadata infrastructure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/create_cloud_exadata_infrastructure.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#create_cloud_exadata_infrastructure)
        """

    def create_cloud_vm_cluster(
        self, **kwargs: Unpack[CreateCloudVmClusterInputTypeDef]
    ) -> CreateCloudVmClusterOutputTypeDef:
        """
        Creates a VM cluster on the specified Exadata infrastructure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/create_cloud_vm_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#create_cloud_vm_cluster)
        """

    def create_odb_network(
        self, **kwargs: Unpack[CreateOdbNetworkInputTypeDef]
    ) -> CreateOdbNetworkOutputTypeDef:
        """
        Creates an ODB network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/create_odb_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#create_odb_network)
        """

    def create_odb_peering_connection(
        self, **kwargs: Unpack[CreateOdbPeeringConnectionInputTypeDef]
    ) -> CreateOdbPeeringConnectionOutputTypeDef:
        """
        Creates a peering connection between an ODB network and a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/create_odb_peering_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#create_odb_peering_connection)
        """

    def delete_cloud_autonomous_vm_cluster(
        self, **kwargs: Unpack[DeleteCloudAutonomousVmClusterInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an Autonomous VM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/delete_cloud_autonomous_vm_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#delete_cloud_autonomous_vm_cluster)
        """

    def delete_cloud_exadata_infrastructure(
        self, **kwargs: Unpack[DeleteCloudExadataInfrastructureInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified Exadata infrastructure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/delete_cloud_exadata_infrastructure.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#delete_cloud_exadata_infrastructure)
        """

    def delete_cloud_vm_cluster(
        self, **kwargs: Unpack[DeleteCloudVmClusterInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified VM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/delete_cloud_vm_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#delete_cloud_vm_cluster)
        """

    def delete_odb_network(self, **kwargs: Unpack[DeleteOdbNetworkInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified ODB network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/delete_odb_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#delete_odb_network)
        """

    def delete_odb_peering_connection(
        self, **kwargs: Unpack[DeleteOdbPeeringConnectionInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an ODB peering connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/delete_odb_peering_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#delete_odb_peering_connection)
        """

    def disassociate_iam_role_from_resource(
        self, **kwargs: Unpack[DisassociateIamRoleFromResourceInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates an Amazon Web Services Identity and Access Management (IAM)
        service role from a specified resource to disable Amazon Web Services service
        integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/disassociate_iam_role_from_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#disassociate_iam_role_from_resource)
        """

    def get_cloud_autonomous_vm_cluster(
        self, **kwargs: Unpack[GetCloudAutonomousVmClusterInputTypeDef]
    ) -> GetCloudAutonomousVmClusterOutputTypeDef:
        """
        Gets information about a specific Autonomous VM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/get_cloud_autonomous_vm_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#get_cloud_autonomous_vm_cluster)
        """

    def get_cloud_exadata_infrastructure(
        self, **kwargs: Unpack[GetCloudExadataInfrastructureInputTypeDef]
    ) -> GetCloudExadataInfrastructureOutputTypeDef:
        """
        Returns information about the specified Exadata infrastructure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/get_cloud_exadata_infrastructure.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#get_cloud_exadata_infrastructure)
        """

    def get_cloud_exadata_infrastructure_unallocated_resources(
        self, **kwargs: Unpack[GetCloudExadataInfrastructureUnallocatedResourcesInputTypeDef]
    ) -> GetCloudExadataInfrastructureUnallocatedResourcesOutputTypeDef:
        """
        Retrieves information about unallocated resources in a specified Cloud Exadata
        Infrastructure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/get_cloud_exadata_infrastructure_unallocated_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#get_cloud_exadata_infrastructure_unallocated_resources)
        """

    def get_cloud_vm_cluster(
        self, **kwargs: Unpack[GetCloudVmClusterInputTypeDef]
    ) -> GetCloudVmClusterOutputTypeDef:
        """
        Returns information about the specified VM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/get_cloud_vm_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#get_cloud_vm_cluster)
        """

    def get_db_node(self, **kwargs: Unpack[GetDbNodeInputTypeDef]) -> GetDbNodeOutputTypeDef:
        """
        Returns information about the specified DB node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/get_db_node.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#get_db_node)
        """

    def get_db_server(self, **kwargs: Unpack[GetDbServerInputTypeDef]) -> GetDbServerOutputTypeDef:
        """
        Returns information about the specified database server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/get_db_server.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#get_db_server)
        """

    def get_oci_onboarding_status(self) -> GetOciOnboardingStatusOutputTypeDef:
        """
        Returns the tenancy activation link and onboarding status for your Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/get_oci_onboarding_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#get_oci_onboarding_status)
        """

    def get_odb_network(
        self, **kwargs: Unpack[GetOdbNetworkInputTypeDef]
    ) -> GetOdbNetworkOutputTypeDef:
        """
        Returns information about the specified ODB network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/get_odb_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#get_odb_network)
        """

    def get_odb_peering_connection(
        self, **kwargs: Unpack[GetOdbPeeringConnectionInputTypeDef]
    ) -> GetOdbPeeringConnectionOutputTypeDef:
        """
        Retrieves information about an ODB peering connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/get_odb_peering_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#get_odb_peering_connection)
        """

    def initialize_service(self, **kwargs: Unpack[InitializeServiceInputTypeDef]) -> Dict[str, Any]:
        """
        Initializes the ODB service for the first time in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/initialize_service.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#initialize_service)
        """

    def list_autonomous_virtual_machines(
        self, **kwargs: Unpack[ListAutonomousVirtualMachinesInputTypeDef]
    ) -> ListAutonomousVirtualMachinesOutputTypeDef:
        """
        Lists all Autonomous VMs in an Autonomous VM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/list_autonomous_virtual_machines.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#list_autonomous_virtual_machines)
        """

    def list_cloud_autonomous_vm_clusters(
        self, **kwargs: Unpack[ListCloudAutonomousVmClustersInputTypeDef]
    ) -> ListCloudAutonomousVmClustersOutputTypeDef:
        """
        Lists all Autonomous VM clusters in a specified Cloud Exadata infrastructure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/list_cloud_autonomous_vm_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#list_cloud_autonomous_vm_clusters)
        """

    def list_cloud_exadata_infrastructures(
        self, **kwargs: Unpack[ListCloudExadataInfrastructuresInputTypeDef]
    ) -> ListCloudExadataInfrastructuresOutputTypeDef:
        """
        Returns information about the Exadata infrastructures owned by your Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/list_cloud_exadata_infrastructures.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#list_cloud_exadata_infrastructures)
        """

    def list_cloud_vm_clusters(
        self, **kwargs: Unpack[ListCloudVmClustersInputTypeDef]
    ) -> ListCloudVmClustersOutputTypeDef:
        """
        Returns information about the VM clusters owned by your Amazon Web Services
        account or only the ones on the specified Exadata infrastructure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/list_cloud_vm_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#list_cloud_vm_clusters)
        """

    def list_db_nodes(self, **kwargs: Unpack[ListDbNodesInputTypeDef]) -> ListDbNodesOutputTypeDef:
        """
        Returns information about the DB nodes for the specified VM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/list_db_nodes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#list_db_nodes)
        """

    def list_db_servers(
        self, **kwargs: Unpack[ListDbServersInputTypeDef]
    ) -> ListDbServersOutputTypeDef:
        """
        Returns information about the database servers that belong to the specified
        Exadata infrastructure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/list_db_servers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#list_db_servers)
        """

    def list_db_system_shapes(
        self, **kwargs: Unpack[ListDbSystemShapesInputTypeDef]
    ) -> ListDbSystemShapesOutputTypeDef:
        """
        Returns information about the shapes that are available for an Exadata
        infrastructure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/list_db_system_shapes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#list_db_system_shapes)
        """

    def list_gi_versions(
        self, **kwargs: Unpack[ListGiVersionsInputTypeDef]
    ) -> ListGiVersionsOutputTypeDef:
        """
        Returns information about Oracle Grid Infrastructure (GI) software versions
        that are available for a VM cluster for the specified shape.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/list_gi_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#list_gi_versions)
        """

    def list_odb_networks(
        self, **kwargs: Unpack[ListOdbNetworksInputTypeDef]
    ) -> ListOdbNetworksOutputTypeDef:
        """
        Returns information about the ODB networks owned by your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/list_odb_networks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#list_odb_networks)
        """

    def list_odb_peering_connections(
        self, **kwargs: Unpack[ListOdbPeeringConnectionsInputTypeDef]
    ) -> ListOdbPeeringConnectionsOutputTypeDef:
        """
        Lists all ODB peering connections or those associated with a specific ODB
        network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/list_odb_peering_connections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#list_odb_peering_connections)
        """

    def list_system_versions(
        self, **kwargs: Unpack[ListSystemVersionsInputTypeDef]
    ) -> ListSystemVersionsOutputTypeDef:
        """
        Returns information about the system versions that are available for a VM
        cluster for the specified <code>giVersion</code> and <code>shape</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/list_system_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#list_system_versions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns information about the tags applied to this resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#list_tags_for_resource)
        """

    def reboot_db_node(
        self, **kwargs: Unpack[RebootDbNodeInputTypeDef]
    ) -> RebootDbNodeOutputTypeDef:
        """
        Reboots the specified DB node in a VM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/reboot_db_node.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#reboot_db_node)
        """

    def start_db_node(self, **kwargs: Unpack[StartDbNodeInputTypeDef]) -> StartDbNodeOutputTypeDef:
        """
        Starts the specified DB node in a VM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/start_db_node.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#start_db_node)
        """

    def stop_db_node(self, **kwargs: Unpack[StopDbNodeInputTypeDef]) -> StopDbNodeOutputTypeDef:
        """
        Stops the specified DB node in a VM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/stop_db_node.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#stop_db_node)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Applies tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#untag_resource)
        """

    def update_cloud_exadata_infrastructure(
        self, **kwargs: Unpack[UpdateCloudExadataInfrastructureInputTypeDef]
    ) -> UpdateCloudExadataInfrastructureOutputTypeDef:
        """
        Updates the properties of an Exadata infrastructure resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/update_cloud_exadata_infrastructure.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#update_cloud_exadata_infrastructure)
        """

    def update_odb_network(
        self, **kwargs: Unpack[UpdateOdbNetworkInputTypeDef]
    ) -> UpdateOdbNetworkOutputTypeDef:
        """
        Updates properties of a specified ODB network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/update_odb_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#update_odb_network)
        """

    def update_odb_peering_connection(
        self, **kwargs: Unpack[UpdateOdbPeeringConnectionInputTypeDef]
    ) -> UpdateOdbPeeringConnectionOutputTypeDef:
        """
        Modifies the settings of an Oracle Database@Amazon Web Services peering
        connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/update_odb_peering_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#update_odb_peering_connection)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_autonomous_virtual_machines"]
    ) -> ListAutonomousVirtualMachinesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_cloud_autonomous_vm_clusters"]
    ) -> ListCloudAutonomousVmClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_cloud_exadata_infrastructures"]
    ) -> ListCloudExadataInfrastructuresPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_cloud_vm_clusters"]
    ) -> ListCloudVmClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_db_nodes"]
    ) -> ListDbNodesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_db_servers"]
    ) -> ListDbServersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_db_system_shapes"]
    ) -> ListDbSystemShapesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_gi_versions"]
    ) -> ListGiVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_odb_networks"]
    ) -> ListOdbNetworksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_odb_peering_connections"]
    ) -> ListOdbPeeringConnectionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_system_versions"]
    ) -> ListSystemVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/client/#get_paginator)
        """
