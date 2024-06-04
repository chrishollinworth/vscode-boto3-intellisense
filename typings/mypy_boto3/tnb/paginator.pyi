"""
Type annotations for tnb service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_tnb import TelcoNetworkBuilderClient
    from mypy_boto3_tnb.paginator import (
        ListSolFunctionInstancesPaginator,
        ListSolFunctionPackagesPaginator,
        ListSolNetworkInstancesPaginator,
        ListSolNetworkOperationsPaginator,
        ListSolNetworkPackagesPaginator,
    )

    client: TelcoNetworkBuilderClient = boto3.client("tnb")

    list_sol_function_instances_paginator: ListSolFunctionInstancesPaginator = client.get_paginator("list_sol_function_instances")
    list_sol_function_packages_paginator: ListSolFunctionPackagesPaginator = client.get_paginator("list_sol_function_packages")
    list_sol_network_instances_paginator: ListSolNetworkInstancesPaginator = client.get_paginator("list_sol_network_instances")
    list_sol_network_operations_paginator: ListSolNetworkOperationsPaginator = client.get_paginator("list_sol_network_operations")
    list_sol_network_packages_paginator: ListSolNetworkPackagesPaginator = client.get_paginator("list_sol_network_packages")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListSolFunctionInstancesOutputTypeDef,
    ListSolFunctionPackagesOutputTypeDef,
    ListSolNetworkInstancesOutputTypeDef,
    ListSolNetworkOperationsOutputTypeDef,
    ListSolNetworkPackagesOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListSolFunctionInstancesPaginator",
    "ListSolFunctionPackagesPaginator",
    "ListSolNetworkInstancesPaginator",
    "ListSolNetworkOperationsPaginator",
    "ListSolNetworkPackagesPaginator",
)

class ListSolFunctionInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/tnb.html#TelcoNetworkBuilder.Paginator.ListSolFunctionInstances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators.html#listsolfunctioninstancespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSolFunctionInstancesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/tnb.html#TelcoNetworkBuilder.Paginator.ListSolFunctionInstances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators.html#listsolfunctioninstancespaginator)
        """

class ListSolFunctionPackagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/tnb.html#TelcoNetworkBuilder.Paginator.ListSolFunctionPackages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators.html#listsolfunctionpackagespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSolFunctionPackagesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/tnb.html#TelcoNetworkBuilder.Paginator.ListSolFunctionPackages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators.html#listsolfunctionpackagespaginator)
        """

class ListSolNetworkInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/tnb.html#TelcoNetworkBuilder.Paginator.ListSolNetworkInstances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators.html#listsolnetworkinstancespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSolNetworkInstancesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/tnb.html#TelcoNetworkBuilder.Paginator.ListSolNetworkInstances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators.html#listsolnetworkinstancespaginator)
        """

class ListSolNetworkOperationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/tnb.html#TelcoNetworkBuilder.Paginator.ListSolNetworkOperations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators.html#listsolnetworkoperationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSolNetworkOperationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/tnb.html#TelcoNetworkBuilder.Paginator.ListSolNetworkOperations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators.html#listsolnetworkoperationspaginator)
        """

class ListSolNetworkPackagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/tnb.html#TelcoNetworkBuilder.Paginator.ListSolNetworkPackages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators.html#listsolnetworkpackagespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSolNetworkPackagesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/tnb.html#TelcoNetworkBuilder.Paginator.ListSolNetworkPackages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators.html#listsolnetworkpackagespaginator)
        """
