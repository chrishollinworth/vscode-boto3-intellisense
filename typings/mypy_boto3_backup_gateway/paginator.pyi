"""
Type annotations for backup-gateway service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_backup_gateway import BackupGatewayClient
    from mypy_boto3_backup_gateway.paginator import (
        ListGatewaysPaginator,
        ListHypervisorsPaginator,
        ListVirtualMachinesPaginator,
    )

    client: BackupGatewayClient = boto3.client("backup-gateway")

    list_gateways_paginator: ListGatewaysPaginator = client.get_paginator("list_gateways")
    list_hypervisors_paginator: ListHypervisorsPaginator = client.get_paginator("list_hypervisors")
    list_virtual_machines_paginator: ListVirtualMachinesPaginator = client.get_paginator("list_virtual_machines")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListGatewaysOutputTypeDef,
    ListHypervisorsOutputTypeDef,
    ListVirtualMachinesOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListGatewaysPaginator", "ListHypervisorsPaginator", "ListVirtualMachinesPaginator")

class ListGatewaysPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/backup-gateway.html#BackupGateway.Paginator.ListGateways)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/paginators.html#listgatewayspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGatewaysOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/backup-gateway.html#BackupGateway.Paginator.ListGateways.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/paginators.html#listgatewayspaginator)
        """

class ListHypervisorsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/backup-gateway.html#BackupGateway.Paginator.ListHypervisors)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/paginators.html#listhypervisorspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHypervisorsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/backup-gateway.html#BackupGateway.Paginator.ListHypervisors.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/paginators.html#listhypervisorspaginator)
        """

class ListVirtualMachinesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/backup-gateway.html#BackupGateway.Paginator.ListVirtualMachines)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/paginators.html#listvirtualmachinespaginator)
    """

    def paginate(
        self, *, HypervisorArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVirtualMachinesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/backup-gateway.html#BackupGateway.Paginator.ListVirtualMachines.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/paginators.html#listvirtualmachinespaginator)
        """
