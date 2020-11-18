# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for schemas service client

Usage::

    ```python
    import boto3
    from mypy_boto3_schemas import SchemasClient

    client: SchemasClient = boto3.client("schemas")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_schemas.paginator import (
    ListDiscoverersPaginator,
    ListRegistriesPaginator,
    ListSchemasPaginator,
    ListSchemaVersionsPaginator,
    SearchSchemasPaginator,
)
from mypy_boto3_schemas.type_defs import (
    CreateDiscovererResponseTypeDef,
    CreateRegistryResponseTypeDef,
    CreateSchemaResponseTypeDef,
    DescribeCodeBindingResponseTypeDef,
    DescribeDiscovererResponseTypeDef,
    DescribeRegistryResponseTypeDef,
    DescribeSchemaResponseTypeDef,
    ExportSchemaResponseTypeDef,
    GetCodeBindingSourceResponseTypeDef,
    GetDiscoveredSchemaResponseTypeDef,
    GetResourcePolicyResponseTypeDef,
    ListDiscoverersResponseTypeDef,
    ListRegistriesResponseTypeDef,
    ListSchemasResponseTypeDef,
    ListSchemaVersionsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutCodeBindingResponseTypeDef,
    PutResourcePolicyResponseTypeDef,
    SearchSchemasResponseTypeDef,
    StartDiscovererResponseTypeDef,
    StopDiscovererResponseTypeDef,
    UpdateDiscovererResponseTypeDef,
    UpdateRegistryResponseTypeDef,
    UpdateSchemaResponseTypeDef,
)
from mypy_boto3_schemas.waiter import CodeBindingExistsWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SchemasClient",)


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
    GoneException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    PreconditionFailedException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]


class SchemasClient:
    """
    [Schemas.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.can_paginate)
        """

    def create_discoverer(
        self, SourceArn: str, Description: str = None, Tags: Dict[str, str] = None
    ) -> CreateDiscovererResponseTypeDef:
        """
        [Client.create_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.create_discoverer)
        """

    def create_registry(
        self, RegistryName: str, Description: str = None, Tags: Dict[str, str] = None
    ) -> CreateRegistryResponseTypeDef:
        """
        [Client.create_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.create_registry)
        """

    def create_schema(
        self,
        Content: str,
        RegistryName: str,
        SchemaName: str,
        Type: Literal["OpenApi3", "JSONSchemaDraft4"],
        Description: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateSchemaResponseTypeDef:
        """
        [Client.create_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.create_schema)
        """

    def delete_discoverer(self, DiscovererId: str) -> None:
        """
        [Client.delete_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.delete_discoverer)
        """

    def delete_registry(self, RegistryName: str) -> None:
        """
        [Client.delete_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.delete_registry)
        """

    def delete_resource_policy(self, RegistryName: str = None) -> None:
        """
        [Client.delete_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.delete_resource_policy)
        """

    def delete_schema(self, RegistryName: str, SchemaName: str) -> None:
        """
        [Client.delete_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.delete_schema)
        """

    def delete_schema_version(self, RegistryName: str, SchemaName: str, SchemaVersion: str) -> None:
        """
        [Client.delete_schema_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.delete_schema_version)
        """

    def describe_code_binding(
        self, Language: str, RegistryName: str, SchemaName: str, SchemaVersion: str = None
    ) -> DescribeCodeBindingResponseTypeDef:
        """
        [Client.describe_code_binding documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.describe_code_binding)
        """

    def describe_discoverer(self, DiscovererId: str) -> DescribeDiscovererResponseTypeDef:
        """
        [Client.describe_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.describe_discoverer)
        """

    def describe_registry(self, RegistryName: str) -> DescribeRegistryResponseTypeDef:
        """
        [Client.describe_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.describe_registry)
        """

    def describe_schema(
        self, RegistryName: str, SchemaName: str, SchemaVersion: str = None
    ) -> DescribeSchemaResponseTypeDef:
        """
        [Client.describe_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.describe_schema)
        """

    def export_schema(
        self, RegistryName: str, SchemaName: str, Type: str, SchemaVersion: str = None
    ) -> ExportSchemaResponseTypeDef:
        """
        [Client.export_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.export_schema)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.generate_presigned_url)
        """

    def get_code_binding_source(
        self, Language: str, RegistryName: str, SchemaName: str, SchemaVersion: str = None
    ) -> GetCodeBindingSourceResponseTypeDef:
        """
        [Client.get_code_binding_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.get_code_binding_source)
        """

    def get_discovered_schema(
        self, Events: List[str], Type: Literal["OpenApi3", "JSONSchemaDraft4"]
    ) -> GetDiscoveredSchemaResponseTypeDef:
        """
        [Client.get_discovered_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.get_discovered_schema)
        """

    def get_resource_policy(self, RegistryName: str = None) -> GetResourcePolicyResponseTypeDef:
        """
        [Client.get_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.get_resource_policy)
        """

    def list_discoverers(
        self,
        DiscovererIdPrefix: str = None,
        Limit: int = None,
        NextToken: str = None,
        SourceArnPrefix: str = None,
    ) -> ListDiscoverersResponseTypeDef:
        """
        [Client.list_discoverers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.list_discoverers)
        """

    def list_registries(
        self,
        Limit: int = None,
        NextToken: str = None,
        RegistryNamePrefix: str = None,
        Scope: str = None,
    ) -> ListRegistriesResponseTypeDef:
        """
        [Client.list_registries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.list_registries)
        """

    def list_schema_versions(
        self, RegistryName: str, SchemaName: str, Limit: int = None, NextToken: str = None
    ) -> ListSchemaVersionsResponseTypeDef:
        """
        [Client.list_schema_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.list_schema_versions)
        """

    def list_schemas(
        self,
        RegistryName: str,
        Limit: int = None,
        NextToken: str = None,
        SchemaNamePrefix: str = None,
    ) -> ListSchemasResponseTypeDef:
        """
        [Client.list_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.list_schemas)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.list_tags_for_resource)
        """

    def put_code_binding(
        self, Language: str, RegistryName: str, SchemaName: str, SchemaVersion: str = None
    ) -> PutCodeBindingResponseTypeDef:
        """
        [Client.put_code_binding documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.put_code_binding)
        """

    def put_resource_policy(
        self, Policy: str, RegistryName: str = None, RevisionId: str = None
    ) -> PutResourcePolicyResponseTypeDef:
        """
        [Client.put_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.put_resource_policy)
        """

    def search_schemas(
        self, Keywords: str, RegistryName: str, Limit: int = None, NextToken: str = None
    ) -> SearchSchemasResponseTypeDef:
        """
        [Client.search_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.search_schemas)
        """

    def start_discoverer(self, DiscovererId: str) -> StartDiscovererResponseTypeDef:
        """
        [Client.start_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.start_discoverer)
        """

    def stop_discoverer(self, DiscovererId: str) -> StopDiscovererResponseTypeDef:
        """
        [Client.stop_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.stop_discoverer)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.untag_resource)
        """

    def update_discoverer(
        self, DiscovererId: str, Description: str = None
    ) -> UpdateDiscovererResponseTypeDef:
        """
        [Client.update_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.update_discoverer)
        """

    def update_registry(
        self, RegistryName: str, Description: str = None
    ) -> UpdateRegistryResponseTypeDef:
        """
        [Client.update_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.update_registry)
        """

    def update_schema(
        self,
        RegistryName: str,
        SchemaName: str,
        ClientTokenId: str = None,
        Content: str = None,
        Description: str = None,
        Type: Literal["OpenApi3", "JSONSchemaDraft4"] = None,
    ) -> UpdateSchemaResponseTypeDef:
        """
        [Client.update_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Client.update_schema)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_discoverers"]
    ) -> ListDiscoverersPaginator:
        """
        [Paginator.ListDiscoverers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Paginator.ListDiscoverers)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_registries"]) -> ListRegistriesPaginator:
        """
        [Paginator.ListRegistries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Paginator.ListRegistries)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_schema_versions"]
    ) -> ListSchemaVersionsPaginator:
        """
        [Paginator.ListSchemaVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Paginator.ListSchemaVersions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_schemas"]) -> ListSchemasPaginator:
        """
        [Paginator.ListSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Paginator.ListSchemas)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_schemas"]) -> SearchSchemasPaginator:
        """
        [Paginator.SearchSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Paginator.SearchSchemas)
        """

    def get_waiter(self, waiter_name: Literal["code_binding_exists"]) -> CodeBindingExistsWaiter:
        """
        [Waiter.CodeBindingExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/schemas.html#Schemas.Waiter.CodeBindingExists)
        """
