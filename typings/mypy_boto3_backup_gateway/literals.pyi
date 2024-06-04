"""
Type annotations for backup-gateway service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/literals.html)

Usage::

    ```python
    from mypy_boto3_backup_gateway.literals import GatewayTypeType

    data: GatewayTypeType = "BACKUP_VM"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "GatewayTypeType",
    "HypervisorStateType",
    "ListGatewaysPaginatorName",
    "ListHypervisorsPaginatorName",
    "ListVirtualMachinesPaginatorName",
    "SyncMetadataStatusType",
)

GatewayTypeType = Literal["BACKUP_VM"]
HypervisorStateType = Literal["ERROR", "OFFLINE", "ONLINE", "PENDING"]
ListGatewaysPaginatorName = Literal["list_gateways"]
ListHypervisorsPaginatorName = Literal["list_hypervisors"]
ListVirtualMachinesPaginatorName = Literal["list_virtual_machines"]
SyncMetadataStatusType = Literal["CREATED", "FAILED", "PARTIALLY_FAILED", "RUNNING", "SUCCEEDED"]
