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
    GraphQLApiTypeType,
    GraphQLApiVisibilityType,
    OutputTypeType,
    OwnershipType,
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
    AppSyncRuntimeTypeDef,
    AssociateApiResponseTypeDef,
    AssociateMergedGraphqlApiResponseTypeDef,
    AssociateSourceGraphqlApiResponseTypeDef,
    CachingConfigTypeDef,
    CreateApiCacheResponseTypeDef,
    CreateApiKeyResponseTypeDef,
    CreateDataSourceResponseTypeDef,
    CreateDomainNameResponseTypeDef,
    CreateFunctionResponseTypeDef,
    CreateGraphqlApiResponseTypeDef,
    CreateResolverResponseTypeDef,
    CreateTypeResponseTypeDef,
    DisassociateMergedGraphqlApiResponseTypeDef,
    DisassociateSourceGraphqlApiResponseTypeDef,
    DynamodbDataSourceConfigTypeDef,
    ElasticsearchDataSourceConfigTypeDef,
    EvaluateCodeResponseTypeDef,
    EvaluateMappingTemplateResponseTypeDef,
    EventBridgeDataSourceConfigTypeDef,
    GetApiAssociationResponseTypeDef,
    GetApiCacheResponseTypeDef,
    GetDataSourceResponseTypeDef,
    GetDomainNameResponseTypeDef,
    GetFunctionResponseTypeDef,
    GetGraphqlApiResponseTypeDef,
    GetIntrospectionSchemaResponseTypeDef,
    GetResolverResponseTypeDef,
    GetSchemaCreationStatusResponseTypeDef,
    GetSourceApiAssociationResponseTypeDef,
    GetTypeResponseTypeDef,
    HttpDataSourceConfigTypeDef,
    LambdaAuthorizerConfigTypeDef,
    LambdaDataSourceConfigTypeDef,
    ListApiKeysResponseTypeDef,
    ListDataSourcesResponseTypeDef,
    ListDomainNamesResponseTypeDef,
    ListFunctionsResponseTypeDef,
    ListGraphqlApisResponseTypeDef,
    ListResolversByFunctionResponseTypeDef,
    ListResolversResponseTypeDef,
    ListSourceApiAssociationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTypesByAssociationResponseTypeDef,
    ListTypesResponseTypeDef,
    LogConfigTypeDef,
    OpenIDConnectConfigTypeDef,
    OpenSearchServiceDataSourceConfigTypeDef,
    PipelineConfigTypeDef,
    RelationalDatabaseDataSourceConfigTypeDef,
    SourceApiAssociationConfigTypeDef,
    StartSchemaCreationResponseTypeDef,
    StartSchemaMergeResponseTypeDef,
    SyncConfigTypeDef,
    UpdateApiCacheResponseTypeDef,
    UpdateApiKeyResponseTypeDef,
    UpdateDataSourceResponseTypeDef,
    UpdateDomainNameResponseTypeDef,
    UpdateFunctionResponseTypeDef,
    UpdateGraphqlApiResponseTypeDef,
    UpdateResolverResponseTypeDef,
    UpdateSourceApiAssociationResponseTypeDef,
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppSyncClient exceptions.
        """
    def associate_api(self, *, domainName: str, apiId: str) -> AssociateApiResponseTypeDef:
        """
        Maps an endpoint to your custom domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.associate_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#associate_api)
        """
    def associate_merged_graphql_api(
        self,
        *,
        sourceApiIdentifier: str,
        mergedApiIdentifier: str,
        description: str = None,
        sourceApiAssociationConfig: "SourceApiAssociationConfigTypeDef" = None
    ) -> AssociateMergedGraphqlApiResponseTypeDef:
        """
        Creates an association between a Merged API and source API using the source
        API's identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.associate_merged_graphql_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#associate_merged_graphql_api)
        """
    def associate_source_graphql_api(
        self,
        *,
        mergedApiIdentifier: str,
        sourceApiIdentifier: str,
        description: str = None,
        sourceApiAssociationConfig: "SourceApiAssociationConfigTypeDef" = None
    ) -> AssociateSourceGraphqlApiResponseTypeDef:
        """
        Creates an association between a Merged API and source API using the Merged
        API's identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.associate_source_graphql_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#associate_source_graphql_api)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.create_api_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#create_api_cache)
        """
    def create_api_key(
        self, *, apiId: str, description: str = None, expires: int = None
    ) -> CreateApiKeyResponseTypeDef:
        """
        Creates a unique key that you can distribute to clients who invoke your API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.create_api_key)
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
        openSearchServiceConfig: "OpenSearchServiceDataSourceConfigTypeDef" = None,
        httpConfig: "HttpDataSourceConfigTypeDef" = None,
        relationalDatabaseConfig: "RelationalDatabaseDataSourceConfigTypeDef" = None,
        eventBridgeConfig: "EventBridgeDataSourceConfigTypeDef" = None
    ) -> CreateDataSourceResponseTypeDef:
        """
        Creates a `DataSource` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.create_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#create_data_source)
        """
    def create_domain_name(
        self, *, domainName: str, certificateArn: str, description: str = None
    ) -> CreateDomainNameResponseTypeDef:
        """
        Creates a custom `DomainName` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.create_domain_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#create_domain_name)
        """
    def create_function(
        self,
        *,
        apiId: str,
        name: str,
        dataSourceName: str,
        description: str = None,
        requestMappingTemplate: str = None,
        responseMappingTemplate: str = None,
        functionVersion: str = None,
        syncConfig: "SyncConfigTypeDef" = None,
        maxBatchSize: int = None,
        runtime: "AppSyncRuntimeTypeDef" = None,
        code: str = None
    ) -> CreateFunctionResponseTypeDef:
        """
        Creates a `Function` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.create_function)
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
        lambdaAuthorizerConfig: "LambdaAuthorizerConfigTypeDef" = None,
        visibility: GraphQLApiVisibilityType = None,
        apiType: GraphQLApiTypeType = None,
        mergedApiExecutionRoleArn: str = None,
        ownerContact: str = None
    ) -> CreateGraphqlApiResponseTypeDef:
        """
        Creates a `GraphqlApi` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.create_graphql_api)
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
        cachingConfig: "CachingConfigTypeDef" = None,
        maxBatchSize: int = None,
        runtime: "AppSyncRuntimeTypeDef" = None,
        code: str = None
    ) -> CreateResolverResponseTypeDef:
        """
        Creates a `Resolver` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.create_resolver)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#create_resolver)
        """
    def create_type(
        self, *, apiId: str, definition: str, format: TypeDefinitionFormatType
    ) -> CreateTypeResponseTypeDef:
        """
        Creates a `Type` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.create_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#create_type)
        """
    def delete_api_cache(self, *, apiId: str) -> Dict[str, Any]:
        """
        Deletes an `ApiCache` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.delete_api_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#delete_api_cache)
        """
    def delete_api_key(self, *, apiId: str, id: str) -> Dict[str, Any]:
        """
        Deletes an API key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.delete_api_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#delete_api_key)
        """
    def delete_data_source(self, *, apiId: str, name: str) -> Dict[str, Any]:
        """
        Deletes a `DataSource` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.delete_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#delete_data_source)
        """
    def delete_domain_name(self, *, domainName: str) -> Dict[str, Any]:
        """
        Deletes a custom `DomainName` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.delete_domain_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#delete_domain_name)
        """
    def delete_function(self, *, apiId: str, functionId: str) -> Dict[str, Any]:
        """
        Deletes a `Function`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.delete_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#delete_function)
        """
    def delete_graphql_api(self, *, apiId: str) -> Dict[str, Any]:
        """
        Deletes a `GraphqlApi` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.delete_graphql_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#delete_graphql_api)
        """
    def delete_resolver(self, *, apiId: str, typeName: str, fieldName: str) -> Dict[str, Any]:
        """
        Deletes a `Resolver` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.delete_resolver)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#delete_resolver)
        """
    def delete_type(self, *, apiId: str, typeName: str) -> Dict[str, Any]:
        """
        Deletes a `Type` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.delete_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#delete_type)
        """
    def disassociate_api(self, *, domainName: str) -> Dict[str, Any]:
        """
        Removes an `ApiAssociation` object from a custom domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.disassociate_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#disassociate_api)
        """
    def disassociate_merged_graphql_api(
        self, *, sourceApiIdentifier: str, associationId: str
    ) -> DisassociateMergedGraphqlApiResponseTypeDef:
        """
        Deletes an association between a Merged API and source API using the source
        API's identifier and the association ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.disassociate_merged_graphql_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#disassociate_merged_graphql_api)
        """
    def disassociate_source_graphql_api(
        self, *, mergedApiIdentifier: str, associationId: str
    ) -> DisassociateSourceGraphqlApiResponseTypeDef:
        """
        Deletes an association between a Merged API and source API using the Merged
        API's identifier and the association ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.disassociate_source_graphql_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#disassociate_source_graphql_api)
        """
    def evaluate_code(
        self, *, runtime: "AppSyncRuntimeTypeDef", code: str, context: str, function: str = None
    ) -> EvaluateCodeResponseTypeDef:
        """
        Evaluates the given code and returns the response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.evaluate_code)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#evaluate_code)
        """
    def evaluate_mapping_template(
        self, *, template: str, context: str
    ) -> EvaluateMappingTemplateResponseTypeDef:
        """
        Evaluates a given template and returns the response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.evaluate_mapping_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#evaluate_mapping_template)
        """
    def flush_api_cache(self, *, apiId: str) -> Dict[str, Any]:
        """
        Flushes an `ApiCache` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.flush_api_cache)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#generate_presigned_url)
        """
    def get_api_association(self, *, domainName: str) -> GetApiAssociationResponseTypeDef:
        """
        Retrieves an `ApiAssociation` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.get_api_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#get_api_association)
        """
    def get_api_cache(self, *, apiId: str) -> GetApiCacheResponseTypeDef:
        """
        Retrieves an `ApiCache` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.get_api_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#get_api_cache)
        """
    def get_data_source(self, *, apiId: str, name: str) -> GetDataSourceResponseTypeDef:
        """
        Retrieves a `DataSource` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.get_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#get_data_source)
        """
    def get_domain_name(self, *, domainName: str) -> GetDomainNameResponseTypeDef:
        """
        Retrieves a custom `DomainName` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.get_domain_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#get_domain_name)
        """
    def get_function(self, *, apiId: str, functionId: str) -> GetFunctionResponseTypeDef:
        """
        Get a `Function`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.get_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#get_function)
        """
    def get_graphql_api(self, *, apiId: str) -> GetGraphqlApiResponseTypeDef:
        """
        Retrieves a `GraphqlApi` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.get_graphql_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#get_graphql_api)
        """
    def get_introspection_schema(
        self, *, apiId: str, format: OutputTypeType, includeDirectives: bool = None
    ) -> GetIntrospectionSchemaResponseTypeDef:
        """
        Retrieves the introspection schema for a GraphQL API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.get_introspection_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#get_introspection_schema)
        """
    def get_resolver(
        self, *, apiId: str, typeName: str, fieldName: str
    ) -> GetResolverResponseTypeDef:
        """
        Retrieves a `Resolver` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.get_resolver)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#get_resolver)
        """
    def get_schema_creation_status(self, *, apiId: str) -> GetSchemaCreationStatusResponseTypeDef:
        """
        Retrieves the current status of a schema creation operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.get_schema_creation_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#get_schema_creation_status)
        """
    def get_source_api_association(
        self, *, mergedApiIdentifier: str, associationId: str
    ) -> GetSourceApiAssociationResponseTypeDef:
        """
        Retrieves a `SourceApiAssociation` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.get_source_api_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#get_source_api_association)
        """
    def get_type(
        self, *, apiId: str, typeName: str, format: TypeDefinitionFormatType
    ) -> GetTypeResponseTypeDef:
        """
        Retrieves a `Type` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.get_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#get_type)
        """
    def list_api_keys(
        self, *, apiId: str, nextToken: str = None, maxResults: int = None
    ) -> ListApiKeysResponseTypeDef:
        """
        Lists the API keys for a given API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.list_api_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#list_api_keys)
        """
    def list_data_sources(
        self, *, apiId: str, nextToken: str = None, maxResults: int = None
    ) -> ListDataSourcesResponseTypeDef:
        """
        Lists the data sources for a given API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.list_data_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#list_data_sources)
        """
    def list_domain_names(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListDomainNamesResponseTypeDef:
        """
        Lists multiple custom domain names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.list_domain_names)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#list_domain_names)
        """
    def list_functions(
        self, *, apiId: str, nextToken: str = None, maxResults: int = None
    ) -> ListFunctionsResponseTypeDef:
        """
        List multiple functions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.list_functions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#list_functions)
        """
    def list_graphql_apis(
        self,
        *,
        nextToken: str = None,
        maxResults: int = None,
        apiType: GraphQLApiTypeType = None,
        owner: OwnershipType = None
    ) -> ListGraphqlApisResponseTypeDef:
        """
        Lists your GraphQL APIs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.list_graphql_apis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#list_graphql_apis)
        """
    def list_resolvers(
        self, *, apiId: str, typeName: str, nextToken: str = None, maxResults: int = None
    ) -> ListResolversResponseTypeDef:
        """
        Lists the resolvers for a given API and type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.list_resolvers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#list_resolvers)
        """
    def list_resolvers_by_function(
        self, *, apiId: str, functionId: str, nextToken: str = None, maxResults: int = None
    ) -> ListResolversByFunctionResponseTypeDef:
        """
        List the resolvers that are associated with a specific function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.list_resolvers_by_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#list_resolvers_by_function)
        """
    def list_source_api_associations(
        self, *, apiId: str, nextToken: str = None, maxResults: int = None
    ) -> ListSourceApiAssociationsResponseTypeDef:
        """
        Lists the `SourceApiAssociationSummary` data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.list_source_api_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#list_source_api_associations)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.list_tags_for_resource)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.list_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#list_types)
        """
    def list_types_by_association(
        self,
        *,
        mergedApiIdentifier: str,
        associationId: str,
        format: TypeDefinitionFormatType,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListTypesByAssociationResponseTypeDef:
        """
        Lists `Type` objects by the source API association ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.list_types_by_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#list_types_by_association)
        """
    def start_schema_creation(
        self, *, apiId: str, definition: Union[bytes, IO[bytes], StreamingBody]
    ) -> StartSchemaCreationResponseTypeDef:
        """
        Adds a new schema to your GraphQL API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.start_schema_creation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#start_schema_creation)
        """
    def start_schema_merge(
        self, *, associationId: str, mergedApiIdentifier: str
    ) -> StartSchemaMergeResponseTypeDef:
        """
        Initiates a merge operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.start_schema_merge)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#start_schema_merge)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Tags a resource with user-supplied tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Untags a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.untag_resource)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.update_api_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#update_api_cache)
        """
    def update_api_key(
        self, *, apiId: str, id: str, description: str = None, expires: int = None
    ) -> UpdateApiKeyResponseTypeDef:
        """
        Updates an API key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.update_api_key)
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
        openSearchServiceConfig: "OpenSearchServiceDataSourceConfigTypeDef" = None,
        httpConfig: "HttpDataSourceConfigTypeDef" = None,
        relationalDatabaseConfig: "RelationalDatabaseDataSourceConfigTypeDef" = None,
        eventBridgeConfig: "EventBridgeDataSourceConfigTypeDef" = None
    ) -> UpdateDataSourceResponseTypeDef:
        """
        Updates a `DataSource` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.update_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#update_data_source)
        """
    def update_domain_name(
        self, *, domainName: str, description: str = None
    ) -> UpdateDomainNameResponseTypeDef:
        """
        Updates a custom `DomainName` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.update_domain_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#update_domain_name)
        """
    def update_function(
        self,
        *,
        apiId: str,
        name: str,
        functionId: str,
        dataSourceName: str,
        description: str = None,
        requestMappingTemplate: str = None,
        responseMappingTemplate: str = None,
        functionVersion: str = None,
        syncConfig: "SyncConfigTypeDef" = None,
        maxBatchSize: int = None,
        runtime: "AppSyncRuntimeTypeDef" = None,
        code: str = None
    ) -> UpdateFunctionResponseTypeDef:
        """
        Updates a `Function` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.update_function)
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
        lambdaAuthorizerConfig: "LambdaAuthorizerConfigTypeDef" = None,
        mergedApiExecutionRoleArn: str = None,
        ownerContact: str = None
    ) -> UpdateGraphqlApiResponseTypeDef:
        """
        Updates a `GraphqlApi` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.update_graphql_api)
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
        cachingConfig: "CachingConfigTypeDef" = None,
        maxBatchSize: int = None,
        runtime: "AppSyncRuntimeTypeDef" = None,
        code: str = None
    ) -> UpdateResolverResponseTypeDef:
        """
        Updates a `Resolver` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.update_resolver)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#update_resolver)
        """
    def update_source_api_association(
        self,
        *,
        associationId: str,
        mergedApiIdentifier: str,
        description: str = None,
        sourceApiAssociationConfig: "SourceApiAssociationConfigTypeDef" = None
    ) -> UpdateSourceApiAssociationResponseTypeDef:
        """
        Updates some of the configuration choices of a particular source API
        association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.update_source_api_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#update_source_api_association)
        """
    def update_type(
        self, *, apiId: str, typeName: str, format: TypeDefinitionFormatType, definition: str = None
    ) -> UpdateTypeResponseTypeDef:
        """
        Updates a `Type` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Client.update_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/client.html#update_type)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_api_keys"]) -> ListApiKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Paginator.ListApiKeys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators.html#listapikeyspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_sources"]
    ) -> ListDataSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Paginator.ListDataSources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators.html#listdatasourcespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_functions"]) -> ListFunctionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Paginator.ListFunctions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators.html#listfunctionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_graphql_apis"]
    ) -> ListGraphqlApisPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Paginator.ListGraphqlApis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators.html#listgraphqlapispaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_resolvers"]) -> ListResolversPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Paginator.ListResolvers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators.html#listresolverspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_resolvers_by_function"]
    ) -> ListResolversByFunctionPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Paginator.ListResolversByFunction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators.html#listresolversbyfunctionpaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_types"]) -> ListTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appsync.html#AppSync.Paginator.ListTypes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/paginators.html#listtypespaginator)
        """
