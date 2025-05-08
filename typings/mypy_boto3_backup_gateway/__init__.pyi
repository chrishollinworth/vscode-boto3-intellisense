"""
Main interface for backup-gateway service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_backup_gateway import (
        BackupGatewayClient,
        Client,
        ListGatewaysPaginator,
        ListHypervisorsPaginator,
        ListVirtualMachinesPaginator,
    )

    session = Session()
    client: BackupGatewayClient = session.client("backup-gateway")

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
