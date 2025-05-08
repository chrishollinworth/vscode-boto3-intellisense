"""
Type annotations for backup-gateway service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_backup_gateway.client import BackupGatewayClient
    from mypy_boto3_backup_gateway.paginator import (
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListGatewaysInputPaginateTypeDef,
    ListGatewaysOutputTypeDef,
    ListHypervisorsInputPaginateTypeDef,
    ListHypervisorsOutputTypeDef,
    ListVirtualMachinesInputPaginateTypeDef,
    ListVirtualMachinesOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListGatewaysPaginator", "ListHypervisorsPaginator", "ListVirtualMachinesPaginator")

if TYPE_CHECKING:
    _ListGatewaysPaginatorBase = Paginator[ListGatewaysOutputTypeDef]
else:
    _ListGatewaysPaginatorBase = Paginator  # type: ignore[assignment]

class ListGatewaysPaginator(_ListGatewaysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/paginator/ListGateways.html#BackupGateway.Paginator.ListGateways)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/paginators/#listgatewayspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGatewaysInputPaginateTypeDef]
    ) -> PageIterator[ListGatewaysOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/paginator/ListGateways.html#BackupGateway.Paginator.ListGateways.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/paginators/#listgatewayspaginator)
        """

if TYPE_CHECKING:
    _ListHypervisorsPaginatorBase = Paginator[ListHypervisorsOutputTypeDef]
else:
    _ListHypervisorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListHypervisorsPaginator(_ListHypervisorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/paginator/ListHypervisors.html#BackupGateway.Paginator.ListHypervisors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/paginators/#listhypervisorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListHypervisorsInputPaginateTypeDef]
    ) -> PageIterator[ListHypervisorsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/paginator/ListHypervisors.html#BackupGateway.Paginator.ListHypervisors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/paginators/#listhypervisorspaginator)
        """

if TYPE_CHECKING:
    _ListVirtualMachinesPaginatorBase = Paginator[ListVirtualMachinesOutputTypeDef]
else:
    _ListVirtualMachinesPaginatorBase = Paginator  # type: ignore[assignment]

class ListVirtualMachinesPaginator(_ListVirtualMachinesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/paginator/ListVirtualMachines.html#BackupGateway.Paginator.ListVirtualMachines)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/paginators/#listvirtualmachinespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListVirtualMachinesInputPaginateTypeDef]
    ) -> PageIterator[ListVirtualMachinesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway/paginator/ListVirtualMachines.html#BackupGateway.Paginator.ListVirtualMachines.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/paginators/#listvirtualmachinespaginator)
        """
