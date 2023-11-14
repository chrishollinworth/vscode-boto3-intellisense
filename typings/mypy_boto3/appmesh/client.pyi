"""
Type annotations for appmesh service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_appmesh import AppMeshClient

    client: AppMeshClient = boto3.client("appmesh")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

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
from .type_defs import (
    CreateGatewayRouteOutputTypeDef,
    CreateMeshOutputTypeDef,
    CreateRouteOutputTypeDef,
    CreateVirtualGatewayOutputTypeDef,
    CreateVirtualNodeOutputTypeDef,
    CreateVirtualRouterOutputTypeDef,
    CreateVirtualServiceOutputTypeDef,
    DeleteGatewayRouteOutputTypeDef,
    DeleteMeshOutputTypeDef,
    DeleteRouteOutputTypeDef,
    DeleteVirtualGatewayOutputTypeDef,
    DeleteVirtualNodeOutputTypeDef,
    DeleteVirtualRouterOutputTypeDef,
    DeleteVirtualServiceOutputTypeDef,
    DescribeGatewayRouteOutputTypeDef,
    DescribeMeshOutputTypeDef,
    DescribeRouteOutputTypeDef,
    DescribeVirtualGatewayOutputTypeDef,
    DescribeVirtualNodeOutputTypeDef,
    DescribeVirtualRouterOutputTypeDef,
    DescribeVirtualServiceOutputTypeDef,
    GatewayRouteSpecTypeDef,
    ListGatewayRoutesOutputTypeDef,
    ListMeshesOutputTypeDef,
    ListRoutesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListVirtualGatewaysOutputTypeDef,
    ListVirtualNodesOutputTypeDef,
    ListVirtualRoutersOutputTypeDef,
    ListVirtualServicesOutputTypeDef,
    MeshSpecTypeDef,
    RouteSpecTypeDef,
    TagRefTypeDef,
    UpdateGatewayRouteOutputTypeDef,
    UpdateMeshOutputTypeDef,
    UpdateRouteOutputTypeDef,
    UpdateVirtualGatewayOutputTypeDef,
    UpdateVirtualNodeOutputTypeDef,
    UpdateVirtualRouterOutputTypeDef,
    UpdateVirtualServiceOutputTypeDef,
    VirtualGatewaySpecTypeDef,
    VirtualNodeSpecTypeDef,
    VirtualRouterSpecTypeDef,
    VirtualServiceSpecTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AppMeshClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]

class AppMeshClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppMeshClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#close)
        """
    def create_gateway_route(
        self,
        *,
        gatewayRouteName: str,
        meshName: str,
        spec: "GatewayRouteSpecTypeDef",
        virtualGatewayName: str,
        clientToken: str = None,
        meshOwner: str = None,
        tags: List["TagRefTypeDef"] = None
    ) -> CreateGatewayRouteOutputTypeDef:
        """
        Creates a gateway route.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.create_gateway_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#create_gateway_route)
        """
    def create_mesh(
        self,
        *,
        meshName: str,
        clientToken: str = None,
        spec: "MeshSpecTypeDef" = None,
        tags: List["TagRefTypeDef"] = None
    ) -> CreateMeshOutputTypeDef:
        """
        Creates a service mesh.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.create_mesh)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#create_mesh)
        """
    def create_route(
        self,
        *,
        meshName: str,
        routeName: str,
        spec: "RouteSpecTypeDef",
        virtualRouterName: str,
        clientToken: str = None,
        meshOwner: str = None,
        tags: List["TagRefTypeDef"] = None
    ) -> CreateRouteOutputTypeDef:
        """
        Creates a route that is associated with a virtual router.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.create_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#create_route)
        """
    def create_virtual_gateway(
        self,
        *,
        meshName: str,
        spec: "VirtualGatewaySpecTypeDef",
        virtualGatewayName: str,
        clientToken: str = None,
        meshOwner: str = None,
        tags: List["TagRefTypeDef"] = None
    ) -> CreateVirtualGatewayOutputTypeDef:
        """
        Creates a virtual gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.create_virtual_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#create_virtual_gateway)
        """
    def create_virtual_node(
        self,
        *,
        meshName: str,
        spec: "VirtualNodeSpecTypeDef",
        virtualNodeName: str,
        clientToken: str = None,
        meshOwner: str = None,
        tags: List["TagRefTypeDef"] = None
    ) -> CreateVirtualNodeOutputTypeDef:
        """
        Creates a virtual node within a service mesh.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.create_virtual_node)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#create_virtual_node)
        """
    def create_virtual_router(
        self,
        *,
        meshName: str,
        spec: "VirtualRouterSpecTypeDef",
        virtualRouterName: str,
        clientToken: str = None,
        meshOwner: str = None,
        tags: List["TagRefTypeDef"] = None
    ) -> CreateVirtualRouterOutputTypeDef:
        """
        Creates a virtual router within a service mesh.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.create_virtual_router)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#create_virtual_router)
        """
    def create_virtual_service(
        self,
        *,
        meshName: str,
        spec: "VirtualServiceSpecTypeDef",
        virtualServiceName: str,
        clientToken: str = None,
        meshOwner: str = None,
        tags: List["TagRefTypeDef"] = None
    ) -> CreateVirtualServiceOutputTypeDef:
        """
        Creates a virtual service within a service mesh.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.create_virtual_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#create_virtual_service)
        """
    def delete_gateway_route(
        self,
        *,
        gatewayRouteName: str,
        meshName: str,
        virtualGatewayName: str,
        meshOwner: str = None
    ) -> DeleteGatewayRouteOutputTypeDef:
        """
        Deletes an existing gateway route.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.delete_gateway_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#delete_gateway_route)
        """
    def delete_mesh(self, *, meshName: str) -> DeleteMeshOutputTypeDef:
        """
        Deletes an existing service mesh.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.delete_mesh)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#delete_mesh)
        """
    def delete_route(
        self, *, meshName: str, routeName: str, virtualRouterName: str, meshOwner: str = None
    ) -> DeleteRouteOutputTypeDef:
        """
        Deletes an existing route.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.delete_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#delete_route)
        """
    def delete_virtual_gateway(
        self, *, meshName: str, virtualGatewayName: str, meshOwner: str = None
    ) -> DeleteVirtualGatewayOutputTypeDef:
        """
        Deletes an existing virtual gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.delete_virtual_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#delete_virtual_gateway)
        """
    def delete_virtual_node(
        self, *, meshName: str, virtualNodeName: str, meshOwner: str = None
    ) -> DeleteVirtualNodeOutputTypeDef:
        """
        Deletes an existing virtual node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.delete_virtual_node)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#delete_virtual_node)
        """
    def delete_virtual_router(
        self, *, meshName: str, virtualRouterName: str, meshOwner: str = None
    ) -> DeleteVirtualRouterOutputTypeDef:
        """
        Deletes an existing virtual router.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.delete_virtual_router)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#delete_virtual_router)
        """
    def delete_virtual_service(
        self, *, meshName: str, virtualServiceName: str, meshOwner: str = None
    ) -> DeleteVirtualServiceOutputTypeDef:
        """
        Deletes an existing virtual service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.delete_virtual_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#delete_virtual_service)
        """
    def describe_gateway_route(
        self,
        *,
        gatewayRouteName: str,
        meshName: str,
        virtualGatewayName: str,
        meshOwner: str = None
    ) -> DescribeGatewayRouteOutputTypeDef:
        """
        Describes an existing gateway route.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.describe_gateway_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#describe_gateway_route)
        """
    def describe_mesh(self, *, meshName: str, meshOwner: str = None) -> DescribeMeshOutputTypeDef:
        """
        Describes an existing service mesh.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.describe_mesh)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#describe_mesh)
        """
    def describe_route(
        self, *, meshName: str, routeName: str, virtualRouterName: str, meshOwner: str = None
    ) -> DescribeRouteOutputTypeDef:
        """
        Describes an existing route.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.describe_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#describe_route)
        """
    def describe_virtual_gateway(
        self, *, meshName: str, virtualGatewayName: str, meshOwner: str = None
    ) -> DescribeVirtualGatewayOutputTypeDef:
        """
        Describes an existing virtual gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.describe_virtual_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#describe_virtual_gateway)
        """
    def describe_virtual_node(
        self, *, meshName: str, virtualNodeName: str, meshOwner: str = None
    ) -> DescribeVirtualNodeOutputTypeDef:
        """
        Describes an existing virtual node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.describe_virtual_node)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#describe_virtual_node)
        """
    def describe_virtual_router(
        self, *, meshName: str, virtualRouterName: str, meshOwner: str = None
    ) -> DescribeVirtualRouterOutputTypeDef:
        """
        Describes an existing virtual router.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.describe_virtual_router)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#describe_virtual_router)
        """
    def describe_virtual_service(
        self, *, meshName: str, virtualServiceName: str, meshOwner: str = None
    ) -> DescribeVirtualServiceOutputTypeDef:
        """
        Describes an existing virtual service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.describe_virtual_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#describe_virtual_service)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#generate_presigned_url)
        """
    def list_gateway_routes(
        self,
        *,
        meshName: str,
        virtualGatewayName: str,
        limit: int = None,
        meshOwner: str = None,
        nextToken: str = None
    ) -> ListGatewayRoutesOutputTypeDef:
        """
        Returns a list of existing gateway routes that are associated to a virtual
        gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.list_gateway_routes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#list_gateway_routes)
        """
    def list_meshes(self, *, limit: int = None, nextToken: str = None) -> ListMeshesOutputTypeDef:
        """
        Returns a list of existing service meshes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.list_meshes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#list_meshes)
        """
    def list_routes(
        self,
        *,
        meshName: str,
        virtualRouterName: str,
        limit: int = None,
        meshOwner: str = None,
        nextToken: str = None
    ) -> ListRoutesOutputTypeDef:
        """
        Returns a list of existing routes in a service mesh.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.list_routes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#list_routes)
        """
    def list_tags_for_resource(
        self, *, resourceArn: str, limit: int = None, nextToken: str = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        List the tags for an App Mesh resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#list_tags_for_resource)
        """
    def list_virtual_gateways(
        self, *, meshName: str, limit: int = None, meshOwner: str = None, nextToken: str = None
    ) -> ListVirtualGatewaysOutputTypeDef:
        """
        Returns a list of existing virtual gateways in a service mesh.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.list_virtual_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#list_virtual_gateways)
        """
    def list_virtual_nodes(
        self, *, meshName: str, limit: int = None, meshOwner: str = None, nextToken: str = None
    ) -> ListVirtualNodesOutputTypeDef:
        """
        Returns a list of existing virtual nodes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.list_virtual_nodes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#list_virtual_nodes)
        """
    def list_virtual_routers(
        self, *, meshName: str, limit: int = None, meshOwner: str = None, nextToken: str = None
    ) -> ListVirtualRoutersOutputTypeDef:
        """
        Returns a list of existing virtual routers in a service mesh.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.list_virtual_routers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#list_virtual_routers)
        """
    def list_virtual_services(
        self, *, meshName: str, limit: int = None, meshOwner: str = None, nextToken: str = None
    ) -> ListVirtualServicesOutputTypeDef:
        """
        Returns a list of existing virtual services in a service mesh.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.list_virtual_services)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#list_virtual_services)
        """
    def tag_resource(self, *, resourceArn: str, tags: List["TagRefTypeDef"]) -> Dict[str, Any]:
        """
        Associates the specified tags to a resource with the specified `resourceArn`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Deletes specified tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#untag_resource)
        """
    def update_gateway_route(
        self,
        *,
        gatewayRouteName: str,
        meshName: str,
        spec: "GatewayRouteSpecTypeDef",
        virtualGatewayName: str,
        clientToken: str = None,
        meshOwner: str = None
    ) -> UpdateGatewayRouteOutputTypeDef:
        """
        Updates an existing gateway route that is associated to a specified virtual
        gateway in a service mesh.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.update_gateway_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#update_gateway_route)
        """
    def update_mesh(
        self, *, meshName: str, clientToken: str = None, spec: "MeshSpecTypeDef" = None
    ) -> UpdateMeshOutputTypeDef:
        """
        Updates an existing service mesh.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.update_mesh)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#update_mesh)
        """
    def update_route(
        self,
        *,
        meshName: str,
        routeName: str,
        spec: "RouteSpecTypeDef",
        virtualRouterName: str,
        clientToken: str = None,
        meshOwner: str = None
    ) -> UpdateRouteOutputTypeDef:
        """
        Updates an existing route for a specified service mesh and virtual router.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.update_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#update_route)
        """
    def update_virtual_gateway(
        self,
        *,
        meshName: str,
        spec: "VirtualGatewaySpecTypeDef",
        virtualGatewayName: str,
        clientToken: str = None,
        meshOwner: str = None
    ) -> UpdateVirtualGatewayOutputTypeDef:
        """
        Updates an existing virtual gateway in a specified service mesh.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.update_virtual_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#update_virtual_gateway)
        """
    def update_virtual_node(
        self,
        *,
        meshName: str,
        spec: "VirtualNodeSpecTypeDef",
        virtualNodeName: str,
        clientToken: str = None,
        meshOwner: str = None
    ) -> UpdateVirtualNodeOutputTypeDef:
        """
        Updates an existing virtual node in a specified service mesh.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.update_virtual_node)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#update_virtual_node)
        """
    def update_virtual_router(
        self,
        *,
        meshName: str,
        spec: "VirtualRouterSpecTypeDef",
        virtualRouterName: str,
        clientToken: str = None,
        meshOwner: str = None
    ) -> UpdateVirtualRouterOutputTypeDef:
        """
        Updates an existing virtual router in a specified service mesh.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.update_virtual_router)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#update_virtual_router)
        """
    def update_virtual_service(
        self,
        *,
        meshName: str,
        spec: "VirtualServiceSpecTypeDef",
        virtualServiceName: str,
        clientToken: str = None,
        meshOwner: str = None
    ) -> UpdateVirtualServiceOutputTypeDef:
        """
        Updates an existing virtual service in a specified service mesh.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Client.update_virtual_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/client.html#update_virtual_service)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_gateway_routes"]
    ) -> ListGatewayRoutesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Paginator.ListGatewayRoutes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators.html#listgatewayroutespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_meshes"]) -> ListMeshesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Paginator.ListMeshes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators.html#listmeshespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_routes"]) -> ListRoutesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Paginator.ListRoutes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators.html#listroutespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Paginator.ListTagsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators.html#listtagsforresourcepaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_virtual_gateways"]
    ) -> ListVirtualGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualGateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators.html#listvirtualgatewayspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_virtual_nodes"]
    ) -> ListVirtualNodesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualNodes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators.html#listvirtualnodespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_virtual_routers"]
    ) -> ListVirtualRoutersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualRouters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators.html#listvirtualrouterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_virtual_services"]
    ) -> ListVirtualServicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualServices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/paginators.html#listvirtualservicespaginator)
        """
