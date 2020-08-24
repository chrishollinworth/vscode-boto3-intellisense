# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for appsync service client

Usage::

    ```python
    import boto3
    from mypy_boto3_appsync import AppSyncClient

    client: AppSyncClient = boto3.client("appsync")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_appsync.paginator import (
    ListApiKeysPaginator,
    ListDataSourcesPaginator,
    ListFunctionsPaginator,
    ListGraphqlApisPaginator,
    ListResolversByFunctionPaginator,
    ListResolversPaginator,
    ListTypesPaginator,
)
from mypy_boto3_appsync.type_defs import (
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


class Exceptions:
    AccessDeniedException: Type[Boto3ClientError]
    ApiKeyLimitExceededException: Type[Boto3ClientError]
    ApiKeyValidityOutOfBoundsException: Type[Boto3ClientError]
    ApiLimitExceededException: Type[Boto3ClientError]
    BadRequestException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    ConcurrentModificationException: Type[Boto3ClientError]
    GraphQLSchemaException: Type[Boto3ClientError]
    InternalFailureException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    NotFoundException: Type[Boto3ClientError]
    UnauthorizedException: Type[Boto3ClientError]


class AppSyncClient:
    """
    [AppSync.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.can_paginate)
        """

    def create_api_cache(
        self,
        apiId: str,
        ttl: int,
        apiCachingBehavior: Literal["FULL_REQUEST_CACHING", "PER_RESOLVER_CACHING"],
        type: Literal[
            "T2_SMALL",
            "T2_MEDIUM",
            "R4_LARGE",
            "R4_XLARGE",
            "R4_2XLARGE",
            "R4_4XLARGE",
            "R4_8XLARGE",
            "SMALL",
            "MEDIUM",
            "LARGE",
            "XLARGE",
            "LARGE_2X",
            "LARGE_4X",
            "LARGE_8X",
            "LARGE_12X",
        ],
        transitEncryptionEnabled: bool = None,
        atRestEncryptionEnabled: bool = None,
    ) -> CreateApiCacheResponseTypeDef:
        """
        [Client.create_api_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.create_api_cache)
        """

    def create_api_key(
        self, apiId: str, description: str = None, expires: int = None
    ) -> CreateApiKeyResponseTypeDef:
        """
        [Client.create_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.create_api_key)
        """

    def create_data_source(
        self,
        apiId: str,
        name: str,
        type: Literal[
            "AWS_LAMBDA",
            "AMAZON_DYNAMODB",
            "AMAZON_ELASTICSEARCH",
            "NONE",
            "HTTP",
            "RELATIONAL_DATABASE",
        ],
        description: str = None,
        serviceRoleArn: str = None,
        dynamodbConfig: "DynamodbDataSourceConfigTypeDef" = None,
        lambdaConfig: "LambdaDataSourceConfigTypeDef" = None,
        elasticsearchConfig: "ElasticsearchDataSourceConfigTypeDef" = None,
        httpConfig: "HttpDataSourceConfigTypeDef" = None,
        relationalDatabaseConfig: "RelationalDatabaseDataSourceConfigTypeDef" = None,
    ) -> CreateDataSourceResponseTypeDef:
        """
        [Client.create_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.create_data_source)
        """

    def create_function(
        self,
        apiId: str,
        name: str,
        dataSourceName: str,
        functionVersion: str,
        description: str = None,
        requestMappingTemplate: str = None,
        responseMappingTemplate: str = None,
    ) -> CreateFunctionResponseTypeDef:
        """
        [Client.create_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.create_function)
        """

    def create_graphql_api(
        self,
        name: str,
        authenticationType: Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        logConfig: "LogConfigTypeDef" = None,
        userPoolConfig: "UserPoolConfigTypeDef" = None,
        openIDConnectConfig: "OpenIDConnectConfigTypeDef" = None,
        tags: Dict[str, str] = None,
        additionalAuthenticationProviders: List["AdditionalAuthenticationProviderTypeDef"] = None,
        xrayEnabled: bool = None,
    ) -> CreateGraphqlApiResponseTypeDef:
        """
        [Client.create_graphql_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.create_graphql_api)
        """

    def create_resolver(
        self,
        apiId: str,
        typeName: str,
        fieldName: str,
        dataSourceName: str = None,
        requestMappingTemplate: str = None,
        responseMappingTemplate: str = None,
        kind: Literal["UNIT", "PIPELINE"] = None,
        pipelineConfig: "PipelineConfigTypeDef" = None,
        syncConfig: "SyncConfigTypeDef" = None,
        cachingConfig: "CachingConfigTypeDef" = None,
    ) -> CreateResolverResponseTypeDef:
        """
        [Client.create_resolver documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.create_resolver)
        """

    def create_type(
        self, apiId: str, definition: str, format: Literal["SDL", "JSON"]
    ) -> CreateTypeResponseTypeDef:
        """
        [Client.create_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.create_type)
        """

    def delete_api_cache(self, apiId: str) -> Dict[str, Any]:
        """
        [Client.delete_api_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.delete_api_cache)
        """

    def delete_api_key(self, apiId: str, id: str) -> Dict[str, Any]:
        """
        [Client.delete_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.delete_api_key)
        """

    def delete_data_source(self, apiId: str, name: str) -> Dict[str, Any]:
        """
        [Client.delete_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.delete_data_source)
        """

    def delete_function(self, apiId: str, functionId: str) -> Dict[str, Any]:
        """
        [Client.delete_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.delete_function)
        """

    def delete_graphql_api(self, apiId: str) -> Dict[str, Any]:
        """
        [Client.delete_graphql_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.delete_graphql_api)
        """

    def delete_resolver(self, apiId: str, typeName: str, fieldName: str) -> Dict[str, Any]:
        """
        [Client.delete_resolver documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.delete_resolver)
        """

    def delete_type(self, apiId: str, typeName: str) -> Dict[str, Any]:
        """
        [Client.delete_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.delete_type)
        """

    def flush_api_cache(self, apiId: str) -> Dict[str, Any]:
        """
        [Client.flush_api_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.flush_api_cache)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.generate_presigned_url)
        """

    def get_api_cache(self, apiId: str) -> GetApiCacheResponseTypeDef:
        """
        [Client.get_api_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.get_api_cache)
        """

    def get_data_source(self, apiId: str, name: str) -> GetDataSourceResponseTypeDef:
        """
        [Client.get_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.get_data_source)
        """

    def get_function(self, apiId: str, functionId: str) -> GetFunctionResponseTypeDef:
        """
        [Client.get_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.get_function)
        """

    def get_graphql_api(self, apiId: str) -> GetGraphqlApiResponseTypeDef:
        """
        [Client.get_graphql_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.get_graphql_api)
        """

    def get_introspection_schema(
        self, apiId: str, format: Literal["SDL", "JSON"], includeDirectives: bool = None
    ) -> GetIntrospectionSchemaResponseTypeDef:
        """
        [Client.get_introspection_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.get_introspection_schema)
        """

    def get_resolver(self, apiId: str, typeName: str, fieldName: str) -> GetResolverResponseTypeDef:
        """
        [Client.get_resolver documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.get_resolver)
        """

    def get_schema_creation_status(self, apiId: str) -> GetSchemaCreationStatusResponseTypeDef:
        """
        [Client.get_schema_creation_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.get_schema_creation_status)
        """

    def get_type(
        self, apiId: str, typeName: str, format: Literal["SDL", "JSON"]
    ) -> GetTypeResponseTypeDef:
        """
        [Client.get_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.get_type)
        """

    def list_api_keys(
        self, apiId: str, nextToken: str = None, maxResults: int = None
    ) -> ListApiKeysResponseTypeDef:
        """
        [Client.list_api_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.list_api_keys)
        """

    def list_data_sources(
        self, apiId: str, nextToken: str = None, maxResults: int = None
    ) -> ListDataSourcesResponseTypeDef:
        """
        [Client.list_data_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.list_data_sources)
        """

    def list_functions(
        self, apiId: str, nextToken: str = None, maxResults: int = None
    ) -> ListFunctionsResponseTypeDef:
        """
        [Client.list_functions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.list_functions)
        """

    def list_graphql_apis(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListGraphqlApisResponseTypeDef:
        """
        [Client.list_graphql_apis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.list_graphql_apis)
        """

    def list_resolvers(
        self, apiId: str, typeName: str, nextToken: str = None, maxResults: int = None
    ) -> ListResolversResponseTypeDef:
        """
        [Client.list_resolvers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.list_resolvers)
        """

    def list_resolvers_by_function(
        self, apiId: str, functionId: str, nextToken: str = None, maxResults: int = None
    ) -> ListResolversByFunctionResponseTypeDef:
        """
        [Client.list_resolvers_by_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.list_resolvers_by_function)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.list_tags_for_resource)
        """

    def list_types(
        self,
        apiId: str,
        format: Literal["SDL", "JSON"],
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListTypesResponseTypeDef:
        """
        [Client.list_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.list_types)
        """

    def start_schema_creation(
        self, apiId: str, definition: Union[bytes, IO[bytes]]
    ) -> StartSchemaCreationResponseTypeDef:
        """
        [Client.start_schema_creation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.start_schema_creation)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.untag_resource)
        """

    def update_api_cache(
        self,
        apiId: str,
        ttl: int,
        apiCachingBehavior: Literal["FULL_REQUEST_CACHING", "PER_RESOLVER_CACHING"],
        type: Literal[
            "T2_SMALL",
            "T2_MEDIUM",
            "R4_LARGE",
            "R4_XLARGE",
            "R4_2XLARGE",
            "R4_4XLARGE",
            "R4_8XLARGE",
            "SMALL",
            "MEDIUM",
            "LARGE",
            "XLARGE",
            "LARGE_2X",
            "LARGE_4X",
            "LARGE_8X",
            "LARGE_12X",
        ],
    ) -> UpdateApiCacheResponseTypeDef:
        """
        [Client.update_api_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.update_api_cache)
        """

    def update_api_key(
        self, apiId: str, id: str, description: str = None, expires: int = None
    ) -> UpdateApiKeyResponseTypeDef:
        """
        [Client.update_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.update_api_key)
        """

    def update_data_source(
        self,
        apiId: str,
        name: str,
        type: Literal[
            "AWS_LAMBDA",
            "AMAZON_DYNAMODB",
            "AMAZON_ELASTICSEARCH",
            "NONE",
            "HTTP",
            "RELATIONAL_DATABASE",
        ],
        description: str = None,
        serviceRoleArn: str = None,
        dynamodbConfig: "DynamodbDataSourceConfigTypeDef" = None,
        lambdaConfig: "LambdaDataSourceConfigTypeDef" = None,
        elasticsearchConfig: "ElasticsearchDataSourceConfigTypeDef" = None,
        httpConfig: "HttpDataSourceConfigTypeDef" = None,
        relationalDatabaseConfig: "RelationalDatabaseDataSourceConfigTypeDef" = None,
    ) -> UpdateDataSourceResponseTypeDef:
        """
        [Client.update_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.update_data_source)
        """

    def update_function(
        self,
        apiId: str,
        name: str,
        functionId: str,
        dataSourceName: str,
        functionVersion: str,
        description: str = None,
        requestMappingTemplate: str = None,
        responseMappingTemplate: str = None,
    ) -> UpdateFunctionResponseTypeDef:
        """
        [Client.update_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.update_function)
        """

    def update_graphql_api(
        self,
        apiId: str,
        name: str,
        logConfig: "LogConfigTypeDef" = None,
        authenticationType: Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ] = None,
        userPoolConfig: "UserPoolConfigTypeDef" = None,
        openIDConnectConfig: "OpenIDConnectConfigTypeDef" = None,
        additionalAuthenticationProviders: List["AdditionalAuthenticationProviderTypeDef"] = None,
        xrayEnabled: bool = None,
    ) -> UpdateGraphqlApiResponseTypeDef:
        """
        [Client.update_graphql_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.update_graphql_api)
        """

    def update_resolver(
        self,
        apiId: str,
        typeName: str,
        fieldName: str,
        dataSourceName: str = None,
        requestMappingTemplate: str = None,
        responseMappingTemplate: str = None,
        kind: Literal["UNIT", "PIPELINE"] = None,
        pipelineConfig: "PipelineConfigTypeDef" = None,
        syncConfig: "SyncConfigTypeDef" = None,
        cachingConfig: "CachingConfigTypeDef" = None,
    ) -> UpdateResolverResponseTypeDef:
        """
        [Client.update_resolver documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.update_resolver)
        """

    def update_type(
        self, apiId: str, typeName: str, format: Literal["SDL", "JSON"], definition: str = None
    ) -> UpdateTypeResponseTypeDef:
        """
        [Client.update_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Client.update_type)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_api_keys"]) -> ListApiKeysPaginator:
        """
        [Paginator.ListApiKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Paginator.ListApiKeys)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_sources"]
    ) -> ListDataSourcesPaginator:
        """
        [Paginator.ListDataSources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Paginator.ListDataSources)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_functions"]) -> ListFunctionsPaginator:
        """
        [Paginator.ListFunctions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Paginator.ListFunctions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_graphql_apis"]
    ) -> ListGraphqlApisPaginator:
        """
        [Paginator.ListGraphqlApis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Paginator.ListGraphqlApis)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_resolvers"]) -> ListResolversPaginator:
        """
        [Paginator.ListResolvers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Paginator.ListResolvers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resolvers_by_function"]
    ) -> ListResolversByFunctionPaginator:
        """
        [Paginator.ListResolversByFunction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Paginator.ListResolversByFunction)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_types"]) -> ListTypesPaginator:
        """
        [Paginator.ListTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appsync.html#AppSync.Paginator.ListTypes)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
