"""
Main interface for backup-gateway service.

Usage::

    ```python
    import boto3
    from mypy_boto3_backup_gateway import (
        BackupGatewayClient,
        Client,
        ListGatewaysPaginator,
        ListHypervisorsPaginator,
        ListVirtualMachinesPaginator,
    )

    session = boto3.Session()

    client: BackupGatewayClient = boto3.client("backup-gateway")
    session_client: BackupGatewayClient = session.client("backup-gateway")

    list_gateways_paginator: ListGatewaysPaginator = client.get_paginator("list_gateways")
    list_hypervisors_paginator: ListHypervisorsPaginator = client.get_paginator("list_hypervisors")
    list_virtual_machines_paginator: ListVirtualMachinesPaginator = client.get_paginator("list_virtual_machines")
    ```
"""
from .client import BackupGatewayClient
from .paginator import ListGatewaysPaginator, ListHypervisorsPaginator, ListVirtualMachinesPaginator

Client = BackupGatewayClient

__all__ = (
    "BackupGatewayClient",
    "Client",
    "ListGatewaysPaginator",
    "ListHypervisorsPaginator",
    "ListVirtualMachinesPaginator",
)
