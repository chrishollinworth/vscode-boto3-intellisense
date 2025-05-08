"""
Main interface for servicediscovery service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_servicediscovery import (
        Client,
        ListInstancesPaginator,
        ListNamespacesPaginator,
        ListOperationsPaginator,
        ListServicesPaginator,
        ServiceDiscoveryClient,
    )

    session = Session()
    client: ServiceDiscoveryClient = session.client("servicediscovery")

    list_instances_paginator: ListInstancesPaginator = client.get_paginator("list_instances")
    list_namespaces_paginator: ListNamespacesPaginator = client.get_paginator("list_namespaces")
    list_operations_paginator: ListOperationsPaginator = client.get_paginator("list_operations")
    list_services_paginator: ListServicesPaginator = client.get_paginator("list_services")
    ```
"""

from .client import ServiceDiscoveryClient
from .paginator import (
    ListInstancesPaginator,
    ListNamespacesPaginator,
    ListOperationsPaginator,
    ListServicesPaginator,
)

Client = ServiceDiscoveryClient

__all__ = (
    "Client",
    "ListInstancesPaginator",
    "ListNamespacesPaginator",
    "ListOperationsPaginator",
    "ListServicesPaginator",
    "ServiceDiscoveryClient",
)
