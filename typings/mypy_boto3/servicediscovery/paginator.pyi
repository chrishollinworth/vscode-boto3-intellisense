"""
Type annotations for servicediscovery service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_servicediscovery.client import ServiceDiscoveryClient
    from mypy_boto3_servicediscovery.paginator import (
        ListInstancesPaginator,
        ListNamespacesPaginator,
        ListOperationsPaginator,
        ListServicesPaginator,
    )

    session = Session()
    client: ServiceDiscoveryClient = session.client("servicediscovery")

    list_instances_paginator: ListInstancesPaginator = client.get_paginator("list_instances")
    list_namespaces_paginator: ListNamespacesPaginator = client.get_paginator("list_namespaces")
    list_operations_paginator: ListOperationsPaginator = client.get_paginator("list_operations")
    list_services_paginator: ListServicesPaginator = client.get_paginator("list_services")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListInstancesRequestPaginateTypeDef,
    ListInstancesResponseTypeDef,
    ListNamespacesRequestPaginateTypeDef,
    ListNamespacesResponseTypeDef,
    ListOperationsRequestPaginateTypeDef,
    ListOperationsResponseTypeDef,
    ListServicesRequestPaginateTypeDef,
    ListServicesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListInstancesPaginator",
    "ListNamespacesPaginator",
    "ListOperationsPaginator",
    "ListServicesPaginator",
)

if TYPE_CHECKING:
    _ListInstancesPaginatorBase = Paginator[ListInstancesResponseTypeDef]
else:
    _ListInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class ListInstancesPaginator(_ListInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery/paginator/ListInstances.html#ServiceDiscovery.Paginator.ListInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators/#listinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInstancesRequestPaginateTypeDef]
    ) -> PageIterator[ListInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery/paginator/ListInstances.html#ServiceDiscovery.Paginator.ListInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators/#listinstancespaginator)
        """

if TYPE_CHECKING:
    _ListNamespacesPaginatorBase = Paginator[ListNamespacesResponseTypeDef]
else:
    _ListNamespacesPaginatorBase = Paginator  # type: ignore[assignment]

class ListNamespacesPaginator(_ListNamespacesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery/paginator/ListNamespaces.html#ServiceDiscovery.Paginator.ListNamespaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators/#listnamespacespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListNamespacesRequestPaginateTypeDef]
    ) -> PageIterator[ListNamespacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery/paginator/ListNamespaces.html#ServiceDiscovery.Paginator.ListNamespaces.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators/#listnamespacespaginator)
        """

if TYPE_CHECKING:
    _ListOperationsPaginatorBase = Paginator[ListOperationsResponseTypeDef]
else:
    _ListOperationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOperationsPaginator(_ListOperationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery/paginator/ListOperations.html#ServiceDiscovery.Paginator.ListOperations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators/#listoperationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOperationsRequestPaginateTypeDef]
    ) -> PageIterator[ListOperationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery/paginator/ListOperations.html#ServiceDiscovery.Paginator.ListOperations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators/#listoperationspaginator)
        """

if TYPE_CHECKING:
    _ListServicesPaginatorBase = Paginator[ListServicesResponseTypeDef]
else:
    _ListServicesPaginatorBase = Paginator  # type: ignore[assignment]

class ListServicesPaginator(_ListServicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery/paginator/ListServices.html#ServiceDiscovery.Paginator.ListServices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators/#listservicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServicesRequestPaginateTypeDef]
    ) -> PageIterator[ListServicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery/paginator/ListServices.html#ServiceDiscovery.Paginator.ListServices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators/#listservicespaginator)
        """
