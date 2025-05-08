"""
Main interface for tnb service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_tnb import (
        Client,
        ListSolFunctionInstancesPaginator,
        ListSolFunctionPackagesPaginator,
        ListSolNetworkInstancesPaginator,
        ListSolNetworkOperationsPaginator,
        ListSolNetworkPackagesPaginator,
        TelcoNetworkBuilderClient,
    )

    session = Session()
    client: TelcoNetworkBuilderClient = session.client("tnb")

    list_sol_function_instances_paginator: ListSolFunctionInstancesPaginator = client.get_paginator("list_sol_function_instances")
    list_sol_function_packages_paginator: ListSolFunctionPackagesPaginator = client.get_paginator("list_sol_function_packages")
    list_sol_network_instances_paginator: ListSolNetworkInstancesPaginator = client.get_paginator("list_sol_network_instances")
    list_sol_network_operations_paginator: ListSolNetworkOperationsPaginator = client.get_paginator("list_sol_network_operations")
    list_sol_network_packages_paginator: ListSolNetworkPackagesPaginator = client.get_paginator("list_sol_network_packages")
    ```
"""

from .client import TelcoNetworkBuilderClient
from .paginator import (
    ListSolFunctionInstancesPaginator,
    ListSolFunctionPackagesPaginator,
    ListSolNetworkInstancesPaginator,
    ListSolNetworkOperationsPaginator,
    ListSolNetworkPackagesPaginator,
)

Client = TelcoNetworkBuilderClient

__all__ = (
    "Client",
    "ListSolFunctionInstancesPaginator",
    "ListSolFunctionPackagesPaginator",
    "ListSolNetworkInstancesPaginator",
    "ListSolNetworkOperationsPaginator",
    "ListSolNetworkPackagesPaginator",
    "TelcoNetworkBuilderClient",
)
