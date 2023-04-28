"""
Type annotations for servicediscovery service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_servicediscovery import ServiceDiscoveryClient
    from mypy_boto3_servicediscovery.paginator import (
        ListInstancesPaginator,
        ListNamespacesPaginator,
        ListOperationsPaginator,
        ListServicesPaginator,
    )

    client: ServiceDiscoveryClient = boto3.client("servicediscovery")

    list_instances_paginator: ListInstancesPaginator = client.get_paginator("list_instances")
    list_namespaces_paginator: ListNamespacesPaginator = client.get_paginator("list_namespaces")
    list_operations_paginator: ListOperationsPaginator = client.get_paginator("list_operations")
    list_services_paginator: ListServicesPaginator = client.get_paginator("list_services")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListInstancesResponseTypeDef,
    ListNamespacesResponseTypeDef,
    ListOperationsResponseTypeDef,
    ListServicesResponseTypeDef,
    NamespaceFilterTypeDef,
    OperationFilterTypeDef,
    PaginatorConfigTypeDef,
    ServiceFilterTypeDef,
)

__all__ = (
    "ListInstancesPaginator",
    "ListNamespacesPaginator",
    "ListOperationsPaginator",
    "ListServicesPaginator",
)

class ListInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListInstances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators.html#listinstancespaginator)
    """

    def paginate(
        self, *, ServiceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListInstances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators.html#listinstancespaginator)
        """

class ListNamespacesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListNamespaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators.html#listnamespacespaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["NamespaceFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNamespacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListNamespaces.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators.html#listnamespacespaginator)
        """

class ListOperationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListOperations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators.html#listoperationspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["OperationFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOperationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListOperations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators.html#listoperationspaginator)
        """

class ListServicesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListServices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators.html#listservicespaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["ServiceFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListServices.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators.html#listservicespaginator)
        """
