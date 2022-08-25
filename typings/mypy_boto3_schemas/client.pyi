"""
Type annotations for schemas service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_schemas import SchemasClient

    client: SchemasClient = boto3.client("schemas")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import TypeType
from .paginator import (
    ListDiscoverersPaginator,
    ListRegistriesPaginator,
    ListSchemasPaginator,
    ListSchemaVersionsPaginator,
    SearchSchemasPaginator,
)
from .type_defs import (
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
from .waiter import CodeBindingExistsWaiter

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

class SchemasClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SchemasClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#close)
        """
    def create_discoverer(
        self,
        *,
        SourceArn: str,
        Description: str = None,
        CrossAccount: bool = None,
        Tags: Dict[str, str] = None
    ) -> CreateDiscovererResponseTypeDef:
        """
        Creates a discoverer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.create_discoverer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#create_discoverer)
        """
    def create_registry(
        self, *, RegistryName: str, Description: str = None, Tags: Dict[str, str] = None
    ) -> CreateRegistryResponseTypeDef:
        """
        Creates a registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.create_registry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#create_registry)
        """
    def create_schema(
        self,
        *,
        Content: str,
        RegistryName: str,
        SchemaName: str,
        Type: TypeType,
        Description: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateSchemaResponseTypeDef:
        """
        Creates a schema definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.create_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#create_schema)
        """
    def delete_discoverer(self, *, DiscovererId: str) -> None:
        """
        Deletes a discoverer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.delete_discoverer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#delete_discoverer)
        """
    def delete_registry(self, *, RegistryName: str) -> None:
        """
        Deletes a Registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.delete_registry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#delete_registry)
        """
    def delete_resource_policy(self, *, RegistryName: str = None) -> None:
        """
        Delete the resource-based policy attached to the specified registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#delete_resource_policy)
        """
    def delete_schema(self, *, RegistryName: str, SchemaName: str) -> None:
        """
        Delete a schema definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.delete_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#delete_schema)
        """
    def delete_schema_version(
        self, *, RegistryName: str, SchemaName: str, SchemaVersion: str
    ) -> None:
        """
        Delete the schema version definition See also: `AWS API Documentation <https://d
        ocs.aws.amazon.com/goto/WebAPI/schemas-2019-12-02/DeleteSchemaVersion>`_
        **Request Syntax** response = client.delete_schema_version(
        RegistryName='string', SchemaName='string', SchemaVers...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.delete_schema_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#delete_schema_version)
        """
    def describe_code_binding(
        self, *, Language: str, RegistryName: str, SchemaName: str, SchemaVersion: str = None
    ) -> DescribeCodeBindingResponseTypeDef:
        """
        Describe the code binding URI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.describe_code_binding)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#describe_code_binding)
        """
    def describe_discoverer(self, *, DiscovererId: str) -> DescribeDiscovererResponseTypeDef:
        """
        Describes the discoverer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.describe_discoverer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#describe_discoverer)
        """
    def describe_registry(self, *, RegistryName: str) -> DescribeRegistryResponseTypeDef:
        """
        Describes the registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.describe_registry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#describe_registry)
        """
    def describe_schema(
        self, *, RegistryName: str, SchemaName: str, SchemaVersion: str = None
    ) -> DescribeSchemaResponseTypeDef:
        """
        Retrieve the schema definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.describe_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#describe_schema)
        """
    def export_schema(
        self, *, RegistryName: str, SchemaName: str, Type: str, SchemaVersion: str = None
    ) -> ExportSchemaResponseTypeDef:
        """
        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/schemas-2019-12-02/ExportSchema>`_
        **Request Syntax** response = client.export_schema( RegistryName='string',
        SchemaName='string', SchemaVersion='string', Type='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.export_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#export_schema)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#generate_presigned_url)
        """
    def get_code_binding_source(
        self, *, Language: str, RegistryName: str, SchemaName: str, SchemaVersion: str = None
    ) -> GetCodeBindingSourceResponseTypeDef:
        """
        Get the code binding source URI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.get_code_binding_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#get_code_binding_source)
        """
    def get_discovered_schema(
        self, *, Events: List[str], Type: TypeType
    ) -> GetDiscoveredSchemaResponseTypeDef:
        """
        Get the discovered schema that was generated based on sampled events.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.get_discovered_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#get_discovered_schema)
        """
    def get_resource_policy(self, *, RegistryName: str = None) -> GetResourcePolicyResponseTypeDef:
        """
        Retrieves the resource-based policy attached to a given registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.get_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#get_resource_policy)
        """
    def list_discoverers(
        self,
        *,
        DiscovererIdPrefix: str = None,
        Limit: int = None,
        NextToken: str = None,
        SourceArnPrefix: str = None
    ) -> ListDiscoverersResponseTypeDef:
        """
        List the discoverers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.list_discoverers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#list_discoverers)
        """
    def list_registries(
        self,
        *,
        Limit: int = None,
        NextToken: str = None,
        RegistryNamePrefix: str = None,
        Scope: str = None
    ) -> ListRegistriesResponseTypeDef:
        """
        List the registries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.list_registries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#list_registries)
        """
    def list_schema_versions(
        self, *, RegistryName: str, SchemaName: str, Limit: int = None, NextToken: str = None
    ) -> ListSchemaVersionsResponseTypeDef:
        """
        Provides a list of the schema versions and related information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.list_schema_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#list_schema_versions)
        """
    def list_schemas(
        self,
        *,
        RegistryName: str,
        Limit: int = None,
        NextToken: str = None,
        SchemaNamePrefix: str = None
    ) -> ListSchemasResponseTypeDef:
        """
        List the schemas.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.list_schemas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#list_schemas)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Get tags for resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#list_tags_for_resource)
        """
    def put_code_binding(
        self, *, Language: str, RegistryName: str, SchemaName: str, SchemaVersion: str = None
    ) -> PutCodeBindingResponseTypeDef:
        """
        Put code binding URI See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/schemas-2019-12-02/PutCodeBinding>`_
        **Request Syntax** response = client.put_code_binding( Language='string',
        RegistryName='string', SchemaName='string', SchemaVersi...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.put_code_binding)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#put_code_binding)
        """
    def put_resource_policy(
        self, *, Policy: str, RegistryName: str = None, RevisionId: str = None
    ) -> PutResourcePolicyResponseTypeDef:
        """
        The name of the policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#put_resource_policy)
        """
    def search_schemas(
        self, *, Keywords: str, RegistryName: str, Limit: int = None, NextToken: str = None
    ) -> SearchSchemasResponseTypeDef:
        """
        Search the schemas See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/schemas-2019-12-02/SearchSchemas>`_
        **Request Syntax** response = client.search_schemas( Keywords='string',
        Limit=123, NextToken='string', RegistryName='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.search_schemas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#search_schemas)
        """
    def start_discoverer(self, *, DiscovererId: str) -> StartDiscovererResponseTypeDef:
        """
        Starts the discoverer See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/schemas-2019-12-02/StartDiscoverer>`_
        **Request Syntax** response = client.start_discoverer( DiscovererId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.start_discoverer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#start_discoverer)
        """
    def stop_discoverer(self, *, DiscovererId: str) -> StopDiscovererResponseTypeDef:
        """
        Stops the discoverer See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/schemas-2019-12-02/StopDiscoverer>`_
        **Request Syntax** response = client.stop_discoverer( DiscovererId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.stop_discoverer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#stop_discoverer)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        Add tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#untag_resource)
        """
    def update_discoverer(
        self, *, DiscovererId: str, Description: str = None, CrossAccount: bool = None
    ) -> UpdateDiscovererResponseTypeDef:
        """
        Updates the discoverer See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/schemas-2019-12-02/UpdateDiscoverer>`_
        **Request Syntax** response = client.update_discoverer( Description='string',
        DiscovererId='string', CrossAccount=True|False ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.update_discoverer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#update_discoverer)
        """
    def update_registry(
        self, *, RegistryName: str, Description: str = None
    ) -> UpdateRegistryResponseTypeDef:
        """
        Updates a registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.update_registry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#update_registry)
        """
    def update_schema(
        self,
        *,
        RegistryName: str,
        SchemaName: str,
        ClientTokenId: str = None,
        Content: str = None,
        Description: str = None,
        Type: TypeType = None
    ) -> UpdateSchemaResponseTypeDef:
        """
        Updates the schema definition .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Client.update_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#update_schema)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_discoverers"]
    ) -> ListDiscoverersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Paginator.ListDiscoverers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators.html#listdiscovererspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_registries"]) -> ListRegistriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Paginator.ListRegistries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators.html#listregistriespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_schema_versions"]
    ) -> ListSchemaVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Paginator.ListSchemaVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators.html#listschemaversionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_schemas"]) -> ListSchemasPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Paginator.ListSchemas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators.html#listschemaspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["search_schemas"]) -> SearchSchemasPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Paginator.SearchSchemas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators.html#searchschemaspaginator)
        """
    def get_waiter(self, waiter_name: Literal["code_binding_exists"]) -> CodeBindingExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/schemas.html#Schemas.Waiter.CodeBindingExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/waiters.html#codebindingexistswaiter)
        """
