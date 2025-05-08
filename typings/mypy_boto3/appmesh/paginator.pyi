"""
Type annotations for appmesh service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_appmesh.client import AppMeshClient
    from mypy_boto3_appmesh.paginator import (
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListGatewayRoutesInputPaginateTypeDef,
    ListGatewayRoutesOutputTypeDef,
    ListMeshesInputPaginateTypeDef,
    ListMeshesOutputTypeDef,
    ListRoutesInputPaginateTypeDef,
    ListRoutesOutputTypeDef,
    ListTagsForResourceInputPaginateTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListVirtualGatewaysInputPaginateTypeDef,
    ListVirtualGatewaysOutputTypeDef,
    ListVirtualNodesInputPaginateTypeDef,
    ListVirtualNodesOutputTypeDef,
    ListVirtualRoutersInputPaginateTypeDef,
    ListVirtualRoutersOutputTypeDef,
    ListVirtualServicesInputPaginateTypeDef,
    ListVirtualServicesOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListGatewayRoutesPaginator",
    "ListMeshesPaginator",
    "ListRoutesPaginator",
    "ListTagsForResourcePaginator",
    "ListVirtualGatewaysPaginator",
    "ListVirtualNodesPaginator",
    "ListVirtualRoutersPaginator",
    "ListVirtualServicesPaginator",
)

if TYPE_CHECKING:
    _ListGatewayRoutesPaginatorBase = Paginator[ListGatewayRoutesOutputTypeDef]
else:
    _ListGatewayRoutesPaginatorBase = Paginator  # type: ignore[assignment]

class ListGatewayRoutesPaginator(_ListGatewayRoutesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh/paginator/ListGatewayRoutes.html#AppMesh.Paginator.ListGatewayRoutes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators/#listgatewayroutespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGatewayRoutesInputPaginateTypeDef]
    ) -> PageIterator[ListGatewayRoutesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh/paginator/ListGatewayRoutes.html#AppMesh.Paginator.ListGatewayRoutes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators/#listgatewayroutespaginator)
        """

if TYPE_CHECKING:
    _ListMeshesPaginatorBase = Paginator[ListMeshesOutputTypeDef]
else:
    _ListMeshesPaginatorBase = Paginator  # type: ignore[assignment]

class ListMeshesPaginator(_ListMeshesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh/paginator/ListMeshes.html#AppMesh.Paginator.ListMeshes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators/#listmeshespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMeshesInputPaginateTypeDef]
    ) -> PageIterator[ListMeshesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh/paginator/ListMeshes.html#AppMesh.Paginator.ListMeshes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators/#listmeshespaginator)
        """

if TYPE_CHECKING:
    _ListRoutesPaginatorBase = Paginator[ListRoutesOutputTypeDef]
else:
    _ListRoutesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRoutesPaginator(_ListRoutesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh/paginator/ListRoutes.html#AppMesh.Paginator.ListRoutes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators/#listroutespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRoutesInputPaginateTypeDef]
    ) -> PageIterator[ListRoutesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh/paginator/ListRoutes.html#AppMesh.Paginator.ListRoutes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators/#listroutespaginator)
        """

if TYPE_CHECKING:
    _ListTagsForResourcePaginatorBase = Paginator[ListTagsForResourceOutputTypeDef]
else:
    _ListTagsForResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsForResourcePaginator(_ListTagsForResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh/paginator/ListTagsForResource.html#AppMesh.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators/#listtagsforresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsForResourceInputPaginateTypeDef]
    ) -> PageIterator[ListTagsForResourceOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh/paginator/ListTagsForResource.html#AppMesh.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators/#listtagsforresourcepaginator)
        """

if TYPE_CHECKING:
    _ListVirtualGatewaysPaginatorBase = Paginator[ListVirtualGatewaysOutputTypeDef]
else:
    _ListVirtualGatewaysPaginatorBase = Paginator  # type: ignore[assignment]

class ListVirtualGatewaysPaginator(_ListVirtualGatewaysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh/paginator/ListVirtualGateways.html#AppMesh.Paginator.ListVirtualGateways)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators/#listvirtualgatewayspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListVirtualGatewaysInputPaginateTypeDef]
    ) -> PageIterator[ListVirtualGatewaysOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh/paginator/ListVirtualGateways.html#AppMesh.Paginator.ListVirtualGateways.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators/#listvirtualgatewayspaginator)
        """

if TYPE_CHECKING:
    _ListVirtualNodesPaginatorBase = Paginator[ListVirtualNodesOutputTypeDef]
else:
    _ListVirtualNodesPaginatorBase = Paginator  # type: ignore[assignment]

class ListVirtualNodesPaginator(_ListVirtualNodesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh/paginator/ListVirtualNodes.html#AppMesh.Paginator.ListVirtualNodes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators/#listvirtualnodespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListVirtualNodesInputPaginateTypeDef]
    ) -> PageIterator[ListVirtualNodesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh/paginator/ListVirtualNodes.html#AppMesh.Paginator.ListVirtualNodes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators/#listvirtualnodespaginator)
        """

if TYPE_CHECKING:
    _ListVirtualRoutersPaginatorBase = Paginator[ListVirtualRoutersOutputTypeDef]
else:
    _ListVirtualRoutersPaginatorBase = Paginator  # type: ignore[assignment]

class ListVirtualRoutersPaginator(_ListVirtualRoutersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh/paginator/ListVirtualRouters.html#AppMesh.Paginator.ListVirtualRouters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators/#listvirtualrouterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListVirtualRoutersInputPaginateTypeDef]
    ) -> PageIterator[ListVirtualRoutersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh/paginator/ListVirtualRouters.html#AppMesh.Paginator.ListVirtualRouters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators/#listvirtualrouterspaginator)
        """

if TYPE_CHECKING:
    _ListVirtualServicesPaginatorBase = Paginator[ListVirtualServicesOutputTypeDef]
else:
    _ListVirtualServicesPaginatorBase = Paginator  # type: ignore[assignment]

class ListVirtualServicesPaginator(_ListVirtualServicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh/paginator/ListVirtualServices.html#AppMesh.Paginator.ListVirtualServices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators/#listvirtualservicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListVirtualServicesInputPaginateTypeDef]
    ) -> PageIterator[ListVirtualServicesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh/paginator/ListVirtualServices.html#AppMesh.Paginator.ListVirtualServices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators/#listvirtualservicespaginator)
        """
