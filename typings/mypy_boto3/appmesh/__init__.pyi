"""
Main interface for appmesh service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_appmesh import (
        AppMeshClient,
        Client,
        ListGatewayRoutesPaginator,
        ListMeshesPaginator,
        ListRoutesPaginator,
        ListTagsForResourcePaginator,
        ListVirtualGatewaysPaginator,
        ListVirtualNodesPaginator,
        ListVirtualRoutersPaginator,
        ListVirtualServicesPaginator,
    )

    session = Session()
    client: AppMeshClient = session.client("appmesh")

    list_gateway_routes_paginator: ListGatewayRoutesPaginator = client.get_paginator("list_gateway_routes")
    list_meshes_paginator: ListMeshesPaginator = client.get_paginator("list_meshes")
    list_routes_paginator: ListRoutesPaginator = client.get_paginator("list_routes")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_virtual_gateways_paginator: ListVirtualGatewaysPaginator = client.get_paginator("list_virtual_gateways")
    list_virtual_nodes_paginator: ListVirtualNodesPaginator = client.get_paginator("list_virtual_nodes")
    list_virtual_routers_paginator: ListVirtualRoutersPaginator = client.get_paginator("list_virtual_routers")
    list_virtual_services_paginator: ListVirtualServicesPaginator = client.get_paginator("list_virtual_services")
    ```
"""

from .client import AppMeshClient
from .paginator import (
    ListGatewayRoutesPaginator,
    ListMeshesPaginator,
    ListRoutesPaginator,
    ListTagsForResourcePaginator,
    ListVirtualGatewaysPaginator,
    ListVirtualNodesPaginator,
    ListVirtualRoutersPaginator,
    ListVirtualServicesPaginator,
)

Client = AppMeshClient

__all__ = (
    "AppMeshClient",
    "Client",
    "ListGatewayRoutesPaginator",
    "ListMeshesPaginator",
    "ListRoutesPaginator",
    "ListTagsForResourcePaginator",
    "ListVirtualGatewaysPaginator",
    "ListVirtualNodesPaginator",
    "ListVirtualRoutersPaginator",
    "ListVirtualServicesPaginator",
)
