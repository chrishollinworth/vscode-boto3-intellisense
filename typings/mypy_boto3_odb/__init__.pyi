"""
Main interface for odb service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_odb import (
        Client,
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
        OdbClient,
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

from .client import OdbClient
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

Client = OdbClient

__all__ = (
    "Client",
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
    "OdbClient",
)
