"""
Type annotations for odb service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_odb.client import OdbClient
    from mypy_boto3_odb.paginator import (
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

    session = Session()
    client: OdbClient = session.client("odb")

    list_autonomous_virtual_machines_paginator: ListAutonomousVirtualMachinesPaginator = client.get_paginator("list_autonomous_virtual_machines")
    list_cloud_autonomous_vm_clusters_paginator: ListCloudAutonomousVmClustersPaginator = client.get_paginator("list_cloud_autonomous_vm_clusters")
    list_cloud_exadata_infrastructures_paginator: ListCloudExadataInfrastructuresPaginator = client.get_paginator("list_cloud_exadata_infrastructures")
    list_cloud_vm_clusters_paginator: ListCloudVmClustersPaginator = client.get_paginator("list_cloud_vm_clusters")
    list_db_nodes_paginator: ListDbNodesPaginator = client.get_paginator("list_db_nodes")
    list_db_servers_paginator: ListDbServersPaginator = client.get_paginator("list_db_servers")
    list_db_system_shapes_paginator: ListDbSystemShapesPaginator = client.get_paginator("list_db_system_shapes")
    list_gi_versions_paginator: ListGiVersionsPaginator = client.get_paginator("list_gi_versions")
    list_odb_networks_paginator: ListOdbNetworksPaginator = client.get_paginator("list_odb_networks")
    list_odb_peering_connections_paginator: ListOdbPeeringConnectionsPaginator = client.get_paginator("list_odb_peering_connections")
    list_system_versions_paginator: ListSystemVersionsPaginator = client.get_paginator("list_system_versions")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAutonomousVirtualMachinesInputPaginateTypeDef,
    ListAutonomousVirtualMachinesOutputTypeDef,
    ListCloudAutonomousVmClustersInputPaginateTypeDef,
    ListCloudAutonomousVmClustersOutputTypeDef,
    ListCloudExadataInfrastructuresInputPaginateTypeDef,
    ListCloudExadataInfrastructuresOutputTypeDef,
    ListCloudVmClustersInputPaginateTypeDef,
    ListCloudVmClustersOutputTypeDef,
    ListDbNodesInputPaginateTypeDef,
    ListDbNodesOutputTypeDef,
    ListDbServersInputPaginateTypeDef,
    ListDbServersOutputTypeDef,
    ListDbSystemShapesInputPaginateTypeDef,
    ListDbSystemShapesOutputTypeDef,
    ListGiVersionsInputPaginateTypeDef,
    ListGiVersionsOutputTypeDef,
    ListOdbNetworksInputPaginateTypeDef,
    ListOdbNetworksOutputTypeDef,
    ListOdbPeeringConnectionsInputPaginateTypeDef,
    ListOdbPeeringConnectionsOutputTypeDef,
    ListSystemVersionsInputPaginateTypeDef,
    ListSystemVersionsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAutonomousVirtualMachinesPaginator",
    "ListCloudAutonomousVmClustersPaginator",
    "ListCloudExadataInfrastructuresPaginator",
    "ListCloudVmClustersPaginator",
    "ListDbNodesPaginator",
    "ListDbServersPaginator",
    "ListDbSystemShapesPaginator",
    "ListGiVersionsPaginator",
    "ListOdbNetworksPaginator",
    "ListOdbPeeringConnectionsPaginator",
    "ListSystemVersionsPaginator",
)

if TYPE_CHECKING:
    _ListAutonomousVirtualMachinesPaginatorBase = Paginator[
        ListAutonomousVirtualMachinesOutputTypeDef
    ]
else:
    _ListAutonomousVirtualMachinesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAutonomousVirtualMachinesPaginator(_ListAutonomousVirtualMachinesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListAutonomousVirtualMachines.html#Odb.Paginator.ListAutonomousVirtualMachines)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listautonomousvirtualmachinespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAutonomousVirtualMachinesInputPaginateTypeDef]
    ) -> PageIterator[ListAutonomousVirtualMachinesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListAutonomousVirtualMachines.html#Odb.Paginator.ListAutonomousVirtualMachines.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listautonomousvirtualmachinespaginator)
        """

if TYPE_CHECKING:
    _ListCloudAutonomousVmClustersPaginatorBase = Paginator[
        ListCloudAutonomousVmClustersOutputTypeDef
    ]
else:
    _ListCloudAutonomousVmClustersPaginatorBase = Paginator  # type: ignore[assignment]

class ListCloudAutonomousVmClustersPaginator(_ListCloudAutonomousVmClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListCloudAutonomousVmClusters.html#Odb.Paginator.ListCloudAutonomousVmClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listcloudautonomousvmclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCloudAutonomousVmClustersInputPaginateTypeDef]
    ) -> PageIterator[ListCloudAutonomousVmClustersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListCloudAutonomousVmClusters.html#Odb.Paginator.ListCloudAutonomousVmClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listcloudautonomousvmclusterspaginator)
        """

if TYPE_CHECKING:
    _ListCloudExadataInfrastructuresPaginatorBase = Paginator[
        ListCloudExadataInfrastructuresOutputTypeDef
    ]
else:
    _ListCloudExadataInfrastructuresPaginatorBase = Paginator  # type: ignore[assignment]

class ListCloudExadataInfrastructuresPaginator(_ListCloudExadataInfrastructuresPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListCloudExadataInfrastructures.html#Odb.Paginator.ListCloudExadataInfrastructures)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listcloudexadatainfrastructurespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCloudExadataInfrastructuresInputPaginateTypeDef]
    ) -> PageIterator[ListCloudExadataInfrastructuresOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListCloudExadataInfrastructures.html#Odb.Paginator.ListCloudExadataInfrastructures.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listcloudexadatainfrastructurespaginator)
        """

if TYPE_CHECKING:
    _ListCloudVmClustersPaginatorBase = Paginator[ListCloudVmClustersOutputTypeDef]
else:
    _ListCloudVmClustersPaginatorBase = Paginator  # type: ignore[assignment]

class ListCloudVmClustersPaginator(_ListCloudVmClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListCloudVmClusters.html#Odb.Paginator.ListCloudVmClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listcloudvmclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCloudVmClustersInputPaginateTypeDef]
    ) -> PageIterator[ListCloudVmClustersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListCloudVmClusters.html#Odb.Paginator.ListCloudVmClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listcloudvmclusterspaginator)
        """

if TYPE_CHECKING:
    _ListDbNodesPaginatorBase = Paginator[ListDbNodesOutputTypeDef]
else:
    _ListDbNodesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDbNodesPaginator(_ListDbNodesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListDbNodes.html#Odb.Paginator.ListDbNodes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listdbnodespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDbNodesInputPaginateTypeDef]
    ) -> PageIterator[ListDbNodesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListDbNodes.html#Odb.Paginator.ListDbNodes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listdbnodespaginator)
        """

if TYPE_CHECKING:
    _ListDbServersPaginatorBase = Paginator[ListDbServersOutputTypeDef]
else:
    _ListDbServersPaginatorBase = Paginator  # type: ignore[assignment]

class ListDbServersPaginator(_ListDbServersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListDbServers.html#Odb.Paginator.ListDbServers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listdbserverspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDbServersInputPaginateTypeDef]
    ) -> PageIterator[ListDbServersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListDbServers.html#Odb.Paginator.ListDbServers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listdbserverspaginator)
        """

if TYPE_CHECKING:
    _ListDbSystemShapesPaginatorBase = Paginator[ListDbSystemShapesOutputTypeDef]
else:
    _ListDbSystemShapesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDbSystemShapesPaginator(_ListDbSystemShapesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListDbSystemShapes.html#Odb.Paginator.ListDbSystemShapes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listdbsystemshapespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDbSystemShapesInputPaginateTypeDef]
    ) -> PageIterator[ListDbSystemShapesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListDbSystemShapes.html#Odb.Paginator.ListDbSystemShapes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listdbsystemshapespaginator)
        """

if TYPE_CHECKING:
    _ListGiVersionsPaginatorBase = Paginator[ListGiVersionsOutputTypeDef]
else:
    _ListGiVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListGiVersionsPaginator(_ListGiVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListGiVersions.html#Odb.Paginator.ListGiVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listgiversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGiVersionsInputPaginateTypeDef]
    ) -> PageIterator[ListGiVersionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListGiVersions.html#Odb.Paginator.ListGiVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listgiversionspaginator)
        """

if TYPE_CHECKING:
    _ListOdbNetworksPaginatorBase = Paginator[ListOdbNetworksOutputTypeDef]
else:
    _ListOdbNetworksPaginatorBase = Paginator  # type: ignore[assignment]

class ListOdbNetworksPaginator(_ListOdbNetworksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListOdbNetworks.html#Odb.Paginator.ListOdbNetworks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listodbnetworkspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOdbNetworksInputPaginateTypeDef]
    ) -> PageIterator[ListOdbNetworksOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListOdbNetworks.html#Odb.Paginator.ListOdbNetworks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listodbnetworkspaginator)
        """

if TYPE_CHECKING:
    _ListOdbPeeringConnectionsPaginatorBase = Paginator[ListOdbPeeringConnectionsOutputTypeDef]
else:
    _ListOdbPeeringConnectionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOdbPeeringConnectionsPaginator(_ListOdbPeeringConnectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListOdbPeeringConnections.html#Odb.Paginator.ListOdbPeeringConnections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listodbpeeringconnectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOdbPeeringConnectionsInputPaginateTypeDef]
    ) -> PageIterator[ListOdbPeeringConnectionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListOdbPeeringConnections.html#Odb.Paginator.ListOdbPeeringConnections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listodbpeeringconnectionspaginator)
        """

if TYPE_CHECKING:
    _ListSystemVersionsPaginatorBase = Paginator[ListSystemVersionsOutputTypeDef]
else:
    _ListSystemVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSystemVersionsPaginator(_ListSystemVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListSystemVersions.html#Odb.Paginator.ListSystemVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listsystemversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSystemVersionsInputPaginateTypeDef]
    ) -> PageIterator[ListSystemVersionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/odb/paginator/ListSystemVersions.html#Odb.Paginator.ListSystemVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/paginators/#listsystemversionspaginator)
        """
