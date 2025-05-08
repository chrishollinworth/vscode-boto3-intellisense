"""
Type annotations for tnb service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_tnb.client import TelcoNetworkBuilderClient
    from mypy_boto3_tnb.paginator import (
        ListSolFunctionInstancesPaginator,
        ListSolFunctionPackagesPaginator,
        ListSolNetworkInstancesPaginator,
        ListSolNetworkOperationsPaginator,
        ListSolNetworkPackagesPaginator,
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListSolFunctionInstancesInputPaginateTypeDef,
    ListSolFunctionInstancesOutputTypeDef,
    ListSolFunctionPackagesInputPaginateTypeDef,
    ListSolFunctionPackagesOutputTypeDef,
    ListSolNetworkInstancesInputPaginateTypeDef,
    ListSolNetworkInstancesOutputTypeDef,
    ListSolNetworkOperationsInputPaginateTypeDef,
    ListSolNetworkOperationsOutputTypeDef,
    ListSolNetworkPackagesInputPaginateTypeDef,
    ListSolNetworkPackagesOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListSolFunctionInstancesPaginator",
    "ListSolFunctionPackagesPaginator",
    "ListSolNetworkInstancesPaginator",
    "ListSolNetworkOperationsPaginator",
    "ListSolNetworkPackagesPaginator",
)

if TYPE_CHECKING:
    _ListSolFunctionInstancesPaginatorBase = Paginator[ListSolFunctionInstancesOutputTypeDef]
else:
    _ListSolFunctionInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSolFunctionInstancesPaginator(_ListSolFunctionInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/paginator/ListSolFunctionInstances.html#TelcoNetworkBuilder.Paginator.ListSolFunctionInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators/#listsolfunctioninstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSolFunctionInstancesInputPaginateTypeDef]
    ) -> PageIterator[ListSolFunctionInstancesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/paginator/ListSolFunctionInstances.html#TelcoNetworkBuilder.Paginator.ListSolFunctionInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators/#listsolfunctioninstancespaginator)
        """

if TYPE_CHECKING:
    _ListSolFunctionPackagesPaginatorBase = Paginator[ListSolFunctionPackagesOutputTypeDef]
else:
    _ListSolFunctionPackagesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSolFunctionPackagesPaginator(_ListSolFunctionPackagesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/paginator/ListSolFunctionPackages.html#TelcoNetworkBuilder.Paginator.ListSolFunctionPackages)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators/#listsolfunctionpackagespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSolFunctionPackagesInputPaginateTypeDef]
    ) -> PageIterator[ListSolFunctionPackagesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/paginator/ListSolFunctionPackages.html#TelcoNetworkBuilder.Paginator.ListSolFunctionPackages.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators/#listsolfunctionpackagespaginator)
        """

if TYPE_CHECKING:
    _ListSolNetworkInstancesPaginatorBase = Paginator[ListSolNetworkInstancesOutputTypeDef]
else:
    _ListSolNetworkInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSolNetworkInstancesPaginator(_ListSolNetworkInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/paginator/ListSolNetworkInstances.html#TelcoNetworkBuilder.Paginator.ListSolNetworkInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators/#listsolnetworkinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSolNetworkInstancesInputPaginateTypeDef]
    ) -> PageIterator[ListSolNetworkInstancesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/paginator/ListSolNetworkInstances.html#TelcoNetworkBuilder.Paginator.ListSolNetworkInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators/#listsolnetworkinstancespaginator)
        """

if TYPE_CHECKING:
    _ListSolNetworkOperationsPaginatorBase = Paginator[ListSolNetworkOperationsOutputTypeDef]
else:
    _ListSolNetworkOperationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSolNetworkOperationsPaginator(_ListSolNetworkOperationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/paginator/ListSolNetworkOperations.html#TelcoNetworkBuilder.Paginator.ListSolNetworkOperations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators/#listsolnetworkoperationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSolNetworkOperationsInputPaginateTypeDef]
    ) -> PageIterator[ListSolNetworkOperationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/paginator/ListSolNetworkOperations.html#TelcoNetworkBuilder.Paginator.ListSolNetworkOperations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators/#listsolnetworkoperationspaginator)
        """

if TYPE_CHECKING:
    _ListSolNetworkPackagesPaginatorBase = Paginator[ListSolNetworkPackagesOutputTypeDef]
else:
    _ListSolNetworkPackagesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSolNetworkPackagesPaginator(_ListSolNetworkPackagesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/paginator/ListSolNetworkPackages.html#TelcoNetworkBuilder.Paginator.ListSolNetworkPackages)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators/#listsolnetworkpackagespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSolNetworkPackagesInputPaginateTypeDef]
    ) -> PageIterator[ListSolNetworkPackagesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/paginator/ListSolNetworkPackages.html#TelcoNetworkBuilder.Paginator.ListSolNetworkPackages.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators/#listsolnetworkpackagespaginator)
        """
