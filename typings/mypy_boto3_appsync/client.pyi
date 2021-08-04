"""
Type annotations for appsync service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_appsync import AppSyncClient

    client: AppSyncClient = boto3.client("appsync")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import (
    ApiCacheTypeType,
    ApiCachingBehaviorType,
    AuthenticationTypeType,
    DataSourceTypeType,
    OutputTypeType,
    ResolverKindType,
    TypeDefinitionFormatType,
)
from .paginator import (
    ListApiKeysPaginator,
    ListDataSourcesPaginator,
    ListFunctionsPaginator,
    ListGraphqlApisPaginator,
    ListResolversByFunctionPaginator,
    ListResolversPaginator,
    ListTypesPaginator,
)
from .type_defs import (
    AdditionalAuthenticationProviderTypeDef,
    CachingConfigTypeDef,
    CreateApiCacheResponseTypeDef,
    CreateApiKeyResponseTypeDef,
    CreateDataSourceResponseTypeDef,
    CreateFunctionResponseTypeDef,
    CreateGraphqlApiResponseTypeDef,
    CreateResolverResponseTypeDef,
    CreateTypeResponseTypeDef,
    DynamodbDataSourceConfigTypeDef,
    ElasticsearchDataSourceConfigTypeDef,
    GetApiCacheResponseTypeDef,
    GetDataSourceResponseTypeDef,
    GetFunctionResponseTypeDef,
    GetGraphqlApiResponseTypeDef,
    GetIntrospectionSchemaResponseTypeDef,
    GetResolverResponseTypeDef,
    GetSchemaCreationStatusResponseTypeDef,
    GetTypeResponseTypeDef,
    HttpDataSourceConfigTypeDef,
    LambdaAuthorizerConfigTypeDef,
    LambdaDataSourceConfigTypeDef,
    ListApiKeysResponseTypeDef,
    ListDataSourcesResponseTypeDef,
    ListFunctionsResponseTypeDef,
    ListGraphqlApisResponseTypeDef,
    ListResolversByFunctionResponseTypeDef,
    ListResolversResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTypesResponseTypeDef,
    LogConfigTypeDef,
    OpenIDConnectConfigTypeDef,
    PipelineConfigTypeDef,
    RelationalDatabaseDataSourceConfigTypeDef,
    StartSchemaCreationResponseTypeDef,
    SyncConfigTypeDef,
    UpdateApiCacheResponseTypeDef,
    UpdateApiKeyResponseTypeDef,
    UpdateDataSourceResponseTypeDef,
    UpdateFunctionResponseTypeDef,
    UpdateGraphqlApiResponseTypeDef,
    UpdateResolverResponseTypeDef,
    UpdateTypeResponseTypeDef,
    UserPoolConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AppSyncClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ApiKeyLimitExceededException: Type[BotocoreClientError]
    ApiKeyValidityOutOfBoundsException: Type[BotocoreClientError]
    ApiLimitExceededException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    GraphQLSchemaException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]

class AppSyncClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        AppSyncClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#can_paginate)
        """
    def create_api_cache(
        self,
        *,
        apiId: str,
        ttl: int,
        apiCachingBehavior: ApiCachingBehaviorType,
        type: ApiCacheTypeType,
        transitEncryptionEnabled: bool = None,
        atRestEncryptionEnabled: bool = None
    ) -> CreateApiCacheResponseTypeDef:
        """
        Creates a cache for the GraphQL API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.create_api_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#create_api_cache)
        """
    def create_api_key(
        self, *, apiId: str, description: str = None, expires: int = None
    ) -> CreateApiKeyResponseTypeDef:
        """
        Creates a unique key that you can distribute to clients who are executing your
        API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.create_api_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#create_api_key)
        """
    def create_data_source(
        self,
        *,
        apiId: str,
        name: str,
        type: DataSourceTypeType,
        description: str = None,
        serviceRoleArn: str = None,
        dynamodbConfig: "DynamodbDataSourceConfigTypeDef" = None,
        lambdaConfig: "LambdaDataSourceConfigTypeDef" = None,
        elasticsearchConfig: "ElasticsearchDataSourceConfigTypeDef" = None,
        httpConfig: "HttpDataSourceConfigTypeDef" = None,
        relationalDatabaseConfig: "RelationalDatabaseDataSourceConfigTypeDef" = None
    ) -> CreateDataSourceResponseTypeDef:
        """
        Creates a `DataSource` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.create_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#create_data_source)
        """
    def create_function(
        self,
        *,
        apiId: str,
        name: str,
        dataSourceName: str,
        functionVersion: str,
        description: str = None,
        requestMappingTemplate: str = None,
        responseMappingTemplate: str = None,
        syncConfig: "SyncConfigTypeDef" = None
    ) -> CreateFunctionResponseTypeDef:
        """
        Creates a `Function` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.create_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#create_function)
        """
    def create_graphql_api(
        self,
        *,
        name: str,
        authenticationType: AuthenticationTypeType,
        logConfig: "LogConfigTypeDef" = None,
        userPoolConfig: "UserPoolConfigTypeDef" = None,
        openIDConnectConfig: "OpenIDConnectConfigTypeDef" = None,
        tags: Dict[str, str] = None,
        additionalAuthenticationProviders: List["AdditionalAuthenticationProviderTypeDef"] = None,
        xrayEnabled: bool = None,
        lambdaAuthorizerConfig: "LambdaAuthorizerConfigTypeDef" = None
    ) -> CreateGraphqlApiResponseTypeDef:
        """
        Creates a `GraphqlApi` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.create_graphql_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#create_graphql_api)
        """
    def create_resolver(
        self,
        *,
        apiId: str,
        typeName: str,
        fieldName: str,
        dataSourceName: str = None,
        requestMappingTemplate: str = None,
        responseMappingTemplate: str = None,
        kind: ResolverKindType = None,
        pipelineConfig: "PipelineConfigTypeDef" = None,
        syncConfig: "SyncConfigTypeDef" = None,
        cachingConfig: "CachingConfigTypeDef" = None
    ) -> CreateResolverResponseTypeDef:
        """
        Creates a `Resolver` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.create_resolver)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#create_resolver)
        """
    def create_type(
        self, *, apiId: str, definition: str, format: TypeDefinitionFormatType
    ) -> CreateTypeResponseTypeDef:
        """
        Creates a `Type` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.create_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#create_type)
        """
    def delete_api_cache(self, *, apiId: str) -> Dict[str, Any]:
        """
        Deletes an `ApiCache` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.delete_api_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#delete_api_cache)
        """
    def delete_api_key(self, *, apiId: str, id: str) -> Dict[str, Any]:
        """
        Deletes an API key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.delete_api_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#delete_api_key)
        """
    def delete_data_source(self, *, apiId: str, name: str) -> Dict[str, Any]:
        """
        Deletes a `DataSource` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.delete_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#delete_data_source)
        """
    def delete_function(self, *, apiId: str, functionId: str) -> Dict[str, Any]:
        """
        Deletes a `Function` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.delete_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#delete_function)
        """
    def delete_graphql_api(self, *, apiId: str) -> Dict[str, Any]:
        """
        Deletes a `GraphqlApi` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.delete_graphql_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#delete_graphql_api)
        """
    def delete_resolver(self, *, apiId: str, typeName: str, fieldName: str) -> Dict[str, Any]:
        """
        Deletes a `Resolver` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.delete_resolver)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#delete_resolver)
        """
    def delete_type(self, *, apiId: str, typeName: str) -> Dict[str, Any]:
        """
        Deletes a `Type` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.delete_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#delete_type)
        """
    def flush_api_cache(self, *, apiId: str) -> Dict[str, Any]:
        """
        Flushes an `ApiCache` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.flush_api_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#flush_api_cache)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#generate_presigned_url)
        """
    def get_api_cache(self, *, apiId: str) -> GetApiCacheResponseTypeDef:
        """
        Retrieves an `ApiCache` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.get_api_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#get_api_cache)
        """
    def get_data_source(self, *, apiId: str, name: str) -> GetDataSourceResponseTypeDef:
        """
        Retrieves a `DataSource` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.get_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#get_data_source)
        """
    def get_function(self, *, apiId: str, functionId: str) -> GetFunctionResponseTypeDef:
        """
        Get a `Function` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.get_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#get_function)
        """
    def get_graphql_api(self, *, apiId: str) -> GetGraphqlApiResponseTypeDef:
        """
        Retrieves a `GraphqlApi` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.get_graphql_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#get_graphql_api)
        """
    def get_introspection_schema(
        self, *, apiId: str, format: OutputTypeType, includeDirectives: bool = None
    ) -> GetIntrospectionSchemaResponseTypeDef:
        """
        Retrieves the introspection schema for a GraphQL API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.get_introspection_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#get_introspection_schema)
        """
    def get_resolver(
        self, *, apiId: str, typeName: str, fieldName: str
    ) -> GetResolverResponseTypeDef:
        """
        Retrieves a `Resolver` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.get_resolver)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#get_resolver)
        """
    def get_schema_creation_status(self, *, apiId: str) -> GetSchemaCreationStatusResponseTypeDef:
        """
        Retrieves the current status of a schema creation operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.get_schema_creation_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#get_schema_creation_status)
        """
    def get_type(
        self, *, apiId: str, typeName: str, format: TypeDefinitionFormatType
    ) -> GetTypeResponseTypeDef:
        """
        Retrieves a `Type` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.get_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#get_type)
        """
    def list_api_keys(
        self, *, apiId: str, nextToken: str = None, maxResults: int = None
    ) -> ListApiKeysResponseTypeDef:
        """
        Lists the API keys for a given API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.list_api_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#list_api_keys)
        """
    def list_data_sources(
        self, *, apiId: str, nextToken: str = None, maxResults: int = None
    ) -> ListDataSourcesResponseTypeDef:
        """
        Lists the data sources for a given API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.list_data_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#list_data_sources)
        """
    def list_functions(
        self, *, apiId: str, nextToken: str = None, maxResults: int = None
    ) -> ListFunctionsResponseTypeDef:
        """
        List multiple functions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.list_functions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#list_functions)
        """
    def list_graphql_apis(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListGraphqlApisResponseTypeDef:
        """
        Lists your GraphQL APIs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.list_graphql_apis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#list_graphql_apis)
        """
    def list_resolvers(
        self, *, apiId: str, typeName: str, nextToken: str = None, maxResults: int = None
    ) -> ListResolversResponseTypeDef:
        """
        Lists the resolvers for a given API and type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.list_resolvers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#list_resolvers)
        """
    def list_resolvers_by_function(
        self, *, apiId: str, functionId: str, nextToken: str = None, maxResults: int = None
    ) -> ListResolversByFunctionResponseTypeDef:
        """
        List the resolvers that are associated with a specific function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.list_resolvers_by_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#list_resolvers_by_function)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#list_tags_for_resource)
        """
    def list_types(
        self,
        *,
        apiId: str,
        format: TypeDefinitionFormatType,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListTypesResponseTypeDef:
        """
        Lists the types for a given API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.list_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#list_types)
        """
    def start_schema_creation(
        self, *, apiId: str, definition: Union[bytes, IO[bytes], StreamingBody]
    ) -> StartSchemaCreationResponseTypeDef:
        """
        Adds a new schema to your GraphQL API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.start_schema_creation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#start_schema_creation)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Tags a resource with user-supplied tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Untags a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#untag_resource)
        """
    def update_api_cache(
        self,
        *,
        apiId: str,
        ttl: int,
        apiCachingBehavior: ApiCachingBehaviorType,
        type: ApiCacheTypeType
    ) -> UpdateApiCacheResponseTypeDef:
        """
        Updates the cache for the GraphQL API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.update_api_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#update_api_cache)
        """
    def update_api_key(
        self, *, apiId: str, id: str, description: str = None, expires: int = None
    ) -> UpdateApiKeyResponseTypeDef:
        """
        Updates an API key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.update_api_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#update_api_key)
        """
    def update_data_source(
        self,
        *,
        apiId: str,
        name: str,
        type: DataSourceTypeType,
        description: str = None,
        serviceRoleArn: str = None,
        dynamodbConfig: "DynamodbDataSourceConfigTypeDef" = None,
        lambdaConfig: "LambdaDataSourceConfigTypeDef" = None,
        elasticsearchConfig: "ElasticsearchDataSourceConfigTypeDef" = None,
        httpConfig: "HttpDataSourceConfigTypeDef" = None,
        relationalDatabaseConfig: "RelationalDatabaseDataSourceConfigTypeDef" = None
    ) -> UpdateDataSourceResponseTypeDef:
        """
        Updates a `DataSource` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.update_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#update_data_source)
        """
    def update_function(
        self,
        *,
        apiId: str,
        name: str,
        functionId: str,
        dataSourceName: str,
        functionVersion: str,
        description: str = None,
        requestMappingTemplate: str = None,
        responseMappingTemplate: str = None,
        syncConfig: "SyncConfigTypeDef" = None
    ) -> UpdateFunctionResponseTypeDef:
        """
        Updates a `Function` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.update_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#update_function)
        """
    def update_graphql_api(
        self,
        *,
        apiId: str,
        name: str,
        logConfig: "LogConfigTypeDef" = None,
        authenticationType: AuthenticationTypeType = None,
        userPoolConfig: "UserPoolConfigTypeDef" = None,
        openIDConnectConfig: "OpenIDConnectConfigTypeDef" = None,
        additionalAuthenticationProviders: List["AdditionalAuthenticationProviderTypeDef"] = None,
        xrayEnabled: bool = None,
        lambdaAuthorizerConfig: "LambdaAuthorizerConfigTypeDef" = None
    ) -> UpdateGraphqlApiResponseTypeDef:
        """
        Updates a `GraphqlApi` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.update_graphql_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#update_graphql_api)
        """
    def update_resolver(
        self,
        *,
        apiId: str,
        typeName: str,
        fieldName: str,
        dataSourceName: str = None,
        requestMappingTemplate: str = None,
        responseMappingTemplate: str = None,
        kind: ResolverKindType = None,
        pipelineConfig: "PipelineConfigTypeDef" = None,
        syncConfig: "SyncConfigTypeDef" = None,
        cachingConfig: "CachingConfigTypeDef" = None
    ) -> UpdateResolverResponseTypeDef:
        """
        Updates a `Resolver` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.update_resolver)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#update_resolver)
        """
    def update_type(
        self, *, apiId: str, typeName: str, format: TypeDefinitionFormatType, definition: str = None
    ) -> UpdateTypeResponseTypeDef:
        """
        Updates a `Type` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Client.update_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#update_type)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_api_keys"]) -> ListApiKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Paginator.ListApiKeys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators.html#listapikeyspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_sources"]
    ) -> ListDataSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Paginator.ListDataSources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators.html#listdatasourcespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_functions"]) -> ListFunctionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Paginator.ListFunctions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators.html#listfunctionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_graphql_apis"]
    ) -> ListGraphqlApisPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Paginator.ListGraphqlApis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators.html#listgraphqlapispaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_resolvers"]) -> ListResolversPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Paginator.ListResolvers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators.html#listresolverspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_resolvers_by_function"]
    ) -> ListResolversByFunctionPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Paginator.ListResolversByFunction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators.html#listresolversbyfunctionpaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_types"]) -> ListTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/appsync.html#AppSync.Paginator.ListTypes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators.html#listtypespaginator)
        """
