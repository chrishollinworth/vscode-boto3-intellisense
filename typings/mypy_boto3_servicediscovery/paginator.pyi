# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for servicediscovery service client paginators.

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

from mypy_boto3_servicediscovery.type_defs import (
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
    [Paginator.ListInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListInstances)
    """

    def paginate(
        self, ServiceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstancesResponseTypeDef]:
        """
        [ListInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListInstances.paginate)
        """


class ListNamespacesPaginator(Boto3Paginator):
    """
    [Paginator.ListNamespaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListNamespaces)
    """

    def paginate(
        self,
        Filters: List[NamespaceFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListNamespacesResponseTypeDef]:
        """
        [ListNamespaces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListNamespaces.paginate)
        """


class ListOperationsPaginator(Boto3Paginator):
    """
    [Paginator.ListOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListOperations)
    """

    def paginate(
        self,
        Filters: List[OperationFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListOperationsResponseTypeDef]:
        """
        [ListOperations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListOperations.paginate)
        """


class ListServicesPaginator(Boto3Paginator):
    """
    [Paginator.ListServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListServices)
    """

    def paginate(
        self,
        Filters: List[ServiceFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListServicesResponseTypeDef]:
        """
        [ListServices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListServices.paginate)
        """
