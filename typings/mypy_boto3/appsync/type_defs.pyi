"""
Type annotations for appsync service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appsync.type_defs import AdditionalAuthenticationProviderTypeDef

    data: AdditionalAuthenticationProviderTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ApiCacheStatusType,
    ApiCacheTypeType,
    ApiCachingBehaviorType,
    AuthenticationTypeType,
    ConflictDetectionTypeType,
    ConflictHandlerTypeType,
    DataSourceTypeType,
    DefaultActionType,
    FieldLogLevelType,
    OutputTypeType,
    ResolverKindType,
    SchemaStatusType,
    TypeDefinitionFormatType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AdditionalAuthenticationProviderTypeDef",
    "ApiCacheTypeDef",
    "ApiKeyTypeDef",
    "AuthorizationConfigTypeDef",
    "AwsIamConfigTypeDef",
    "CachingConfigTypeDef",
    "CognitoUserPoolConfigTypeDef",
    "CreateApiCacheRequestRequestTypeDef",
    "CreateApiCacheResponseTypeDef",
    "CreateApiKeyRequestRequestTypeDef",
    "CreateApiKeyResponseTypeDef",
    "CreateDataSourceRequestRequestTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateFunctionRequestRequestTypeDef",
    "CreateFunctionResponseTypeDef",
    "CreateGraphqlApiRequestRequestTypeDef",
    "CreateGraphqlApiResponseTypeDef",
    "CreateResolverRequestRequestTypeDef",
    "CreateResolverResponseTypeDef",
    "CreateTypeRequestRequestTypeDef",
    "CreateTypeResponseTypeDef",
    "DataSourceTypeDef",
    "DeleteApiCacheRequestRequestTypeDef",
    "DeleteApiKeyRequestRequestTypeDef",
    "DeleteDataSourceRequestRequestTypeDef",
    "DeleteFunctionRequestRequestTypeDef",
    "DeleteGraphqlApiRequestRequestTypeDef",
    "DeleteResolverRequestRequestTypeDef",
    "DeleteTypeRequestRequestTypeDef",
    "DeltaSyncConfigTypeDef",
    "DynamodbDataSourceConfigTypeDef",
    "ElasticsearchDataSourceConfigTypeDef",
    "FlushApiCacheRequestRequestTypeDef",
    "FunctionConfigurationTypeDef",
    "GetApiCacheRequestRequestTypeDef",
    "GetApiCacheResponseTypeDef",
    "GetDataSourceRequestRequestTypeDef",
    "GetDataSourceResponseTypeDef",
    "GetFunctionRequestRequestTypeDef",
    "GetFunctionResponseTypeDef",
    "GetGraphqlApiRequestRequestTypeDef",
    "GetGraphqlApiResponseTypeDef",
    "GetIntrospectionSchemaRequestRequestTypeDef",
    "GetIntrospectionSchemaResponseTypeDef",
    "GetResolverRequestRequestTypeDef",
    "GetResolverResponseTypeDef",
    "GetSchemaCreationStatusRequestRequestTypeDef",
    "GetSchemaCreationStatusResponseTypeDef",
    "GetTypeRequestRequestTypeDef",
    "GetTypeResponseTypeDef",
    "GraphqlApiTypeDef",
    "HttpDataSourceConfigTypeDef",
    "LambdaAuthorizerConfigTypeDef",
    "LambdaConflictHandlerConfigTypeDef",
    "LambdaDataSourceConfigTypeDef",
    "ListApiKeysRequestRequestTypeDef",
    "ListApiKeysResponseTypeDef",
    "ListDataSourcesRequestRequestTypeDef",
    "ListDataSourcesResponseTypeDef",
    "ListFunctionsRequestRequestTypeDef",
    "ListFunctionsResponseTypeDef",
    "ListGraphqlApisRequestRequestTypeDef",
    "ListGraphqlApisResponseTypeDef",
    "ListResolversByFunctionRequestRequestTypeDef",
    "ListResolversByFunctionResponseTypeDef",
    "ListResolversRequestRequestTypeDef",
    "ListResolversResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTypesRequestRequestTypeDef",
    "ListTypesResponseTypeDef",
    "LogConfigTypeDef",
    "OpenIDConnectConfigTypeDef",
    "PaginatorConfigTypeDef",
    "PipelineConfigTypeDef",
    "RdsHttpEndpointConfigTypeDef",
    "RelationalDatabaseDataSourceConfigTypeDef",
    "ResolverTypeDef",
    "ResponseMetadataTypeDef",
    "StartSchemaCreationRequestRequestTypeDef",
    "StartSchemaCreationResponseTypeDef",
    "SyncConfigTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TypeTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApiCacheRequestRequestTypeDef",
    "UpdateApiCacheResponseTypeDef",
    "UpdateApiKeyRequestRequestTypeDef",
    "UpdateApiKeyResponseTypeDef",
    "UpdateDataSourceRequestRequestTypeDef",
    "UpdateDataSourceResponseTypeDef",
    "UpdateFunctionRequestRequestTypeDef",
    "UpdateFunctionResponseTypeDef",
    "UpdateGraphqlApiRequestRequestTypeDef",
    "UpdateGraphqlApiResponseTypeDef",
    "UpdateResolverRequestRequestTypeDef",
    "UpdateResolverResponseTypeDef",
    "UpdateTypeRequestRequestTypeDef",
    "UpdateTypeResponseTypeDef",
    "UserPoolConfigTypeDef",
)

AdditionalAuthenticationProviderTypeDef = TypedDict(
    "AdditionalAuthenticationProviderTypeDef",
    {
        "authenticationType": AuthenticationTypeType,
        "openIDConnectConfig": "OpenIDConnectConfigTypeDef",
        "userPoolConfig": "CognitoUserPoolConfigTypeDef",
        "lambdaAuthorizerConfig": "LambdaAuthorizerConfigTypeDef",
    },
    total=False,
)

ApiCacheTypeDef = TypedDict(
    "ApiCacheTypeDef",
    {
        "ttl": int,
        "apiCachingBehavior": ApiCachingBehaviorType,
        "transitEncryptionEnabled": bool,
        "atRestEncryptionEnabled": bool,
        "type": ApiCacheTypeType,
        "status": ApiCacheStatusType,
    },
    total=False,
)

ApiKeyTypeDef = TypedDict(
    "ApiKeyTypeDef",
    {
        "id": str,
        "description": str,
        "expires": int,
        "deletes": int,
    },
    total=False,
)

_RequiredAuthorizationConfigTypeDef = TypedDict(
    "_RequiredAuthorizationConfigTypeDef",
    {
        "authorizationType": Literal["AWS_IAM"],
    },
)
_OptionalAuthorizationConfigTypeDef = TypedDict(
    "_OptionalAuthorizationConfigTypeDef",
    {
        "awsIamConfig": "AwsIamConfigTypeDef",
    },
    total=False,
)

class AuthorizationConfigTypeDef(
    _RequiredAuthorizationConfigTypeDef, _OptionalAuthorizationConfigTypeDef
):
    pass

AwsIamConfigTypeDef = TypedDict(
    "AwsIamConfigTypeDef",
    {
        "signingRegion": str,
        "signingServiceName": str,
    },
    total=False,
)

CachingConfigTypeDef = TypedDict(
    "CachingConfigTypeDef",
    {
        "ttl": int,
        "cachingKeys": List[str],
    },
    total=False,
)

_RequiredCognitoUserPoolConfigTypeDef = TypedDict(
    "_RequiredCognitoUserPoolConfigTypeDef",
    {
        "userPoolId": str,
        "awsRegion": str,
    },
)
_OptionalCognitoUserPoolConfigTypeDef = TypedDict(
    "_OptionalCognitoUserPoolConfigTypeDef",
    {
        "appIdClientRegex": str,
    },
    total=False,
)

class CognitoUserPoolConfigTypeDef(
    _RequiredCognitoUserPoolConfigTypeDef, _OptionalCognitoUserPoolConfigTypeDef
):
    pass

_RequiredCreateApiCacheRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApiCacheRequestRequestTypeDef",
    {
        "apiId": str,
        "ttl": int,
        "apiCachingBehavior": ApiCachingBehaviorType,
        "type": ApiCacheTypeType,
    },
)
_OptionalCreateApiCacheRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApiCacheRequestRequestTypeDef",
    {
        "transitEncryptionEnabled": bool,
        "atRestEncryptionEnabled": bool,
    },
    total=False,
)

class CreateApiCacheRequestRequestTypeDef(
    _RequiredCreateApiCacheRequestRequestTypeDef, _OptionalCreateApiCacheRequestRequestTypeDef
):
    pass

CreateApiCacheResponseTypeDef = TypedDict(
    "CreateApiCacheResponseTypeDef",
    {
        "apiCache": "ApiCacheTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateApiKeyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApiKeyRequestRequestTypeDef",
    {
        "apiId": str,
    },
)
_OptionalCreateApiKeyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApiKeyRequestRequestTypeDef",
    {
        "description": str,
        "expires": int,
    },
    total=False,
)

class CreateApiKeyRequestRequestTypeDef(
    _RequiredCreateApiKeyRequestRequestTypeDef, _OptionalCreateApiKeyRequestRequestTypeDef
):
    pass

CreateApiKeyResponseTypeDef = TypedDict(
    "CreateApiKeyResponseTypeDef",
    {
        "apiKey": "ApiKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataSourceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataSourceRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
        "type": DataSourceTypeType,
    },
)
_OptionalCreateDataSourceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataSourceRequestRequestTypeDef",
    {
        "description": str,
        "serviceRoleArn": str,
        "dynamodbConfig": "DynamodbDataSourceConfigTypeDef",
        "lambdaConfig": "LambdaDataSourceConfigTypeDef",
        "elasticsearchConfig": "ElasticsearchDataSourceConfigTypeDef",
        "httpConfig": "HttpDataSourceConfigTypeDef",
        "relationalDatabaseConfig": "RelationalDatabaseDataSourceConfigTypeDef",
    },
    total=False,
)

class CreateDataSourceRequestRequestTypeDef(
    _RequiredCreateDataSourceRequestRequestTypeDef, _OptionalCreateDataSourceRequestRequestTypeDef
):
    pass

CreateDataSourceResponseTypeDef = TypedDict(
    "CreateDataSourceResponseTypeDef",
    {
        "dataSource": "DataSourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFunctionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFunctionRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
        "dataSourceName": str,
        "functionVersion": str,
    },
)
_OptionalCreateFunctionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFunctionRequestRequestTypeDef",
    {
        "description": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "syncConfig": "SyncConfigTypeDef",
    },
    total=False,
)

class CreateFunctionRequestRequestTypeDef(
    _RequiredCreateFunctionRequestRequestTypeDef, _OptionalCreateFunctionRequestRequestTypeDef
):
    pass

CreateFunctionResponseTypeDef = TypedDict(
    "CreateFunctionResponseTypeDef",
    {
        "functionConfiguration": "FunctionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGraphqlApiRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGraphqlApiRequestRequestTypeDef",
    {
        "name": str,
        "authenticationType": AuthenticationTypeType,
    },
)
_OptionalCreateGraphqlApiRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGraphqlApiRequestRequestTypeDef",
    {
        "logConfig": "LogConfigTypeDef",
        "userPoolConfig": "UserPoolConfigTypeDef",
        "openIDConnectConfig": "OpenIDConnectConfigTypeDef",
        "tags": Dict[str, str],
        "additionalAuthenticationProviders": List["AdditionalAuthenticationProviderTypeDef"],
        "xrayEnabled": bool,
        "lambdaAuthorizerConfig": "LambdaAuthorizerConfigTypeDef",
    },
    total=False,
)

class CreateGraphqlApiRequestRequestTypeDef(
    _RequiredCreateGraphqlApiRequestRequestTypeDef, _OptionalCreateGraphqlApiRequestRequestTypeDef
):
    pass

CreateGraphqlApiResponseTypeDef = TypedDict(
    "CreateGraphqlApiResponseTypeDef",
    {
        "graphqlApi": "GraphqlApiTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateResolverRequestRequestTypeDef = TypedDict(
    "_RequiredCreateResolverRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "fieldName": str,
    },
)
_OptionalCreateResolverRequestRequestTypeDef = TypedDict(
    "_OptionalCreateResolverRequestRequestTypeDef",
    {
        "dataSourceName": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "kind": ResolverKindType,
        "pipelineConfig": "PipelineConfigTypeDef",
        "syncConfig": "SyncConfigTypeDef",
        "cachingConfig": "CachingConfigTypeDef",
    },
    total=False,
)

class CreateResolverRequestRequestTypeDef(
    _RequiredCreateResolverRequestRequestTypeDef, _OptionalCreateResolverRequestRequestTypeDef
):
    pass

CreateResolverResponseTypeDef = TypedDict(
    "CreateResolverResponseTypeDef",
    {
        "resolver": "ResolverTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTypeRequestRequestTypeDef = TypedDict(
    "CreateTypeRequestRequestTypeDef",
    {
        "apiId": str,
        "definition": str,
        "format": TypeDefinitionFormatType,
    },
)

CreateTypeResponseTypeDef = TypedDict(
    "CreateTypeResponseTypeDef",
    {
        "type": "TypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "dataSourceArn": str,
        "name": str,
        "description": str,
        "type": DataSourceTypeType,
        "serviceRoleArn": str,
        "dynamodbConfig": "DynamodbDataSourceConfigTypeDef",
        "lambdaConfig": "LambdaDataSourceConfigTypeDef",
        "elasticsearchConfig": "ElasticsearchDataSourceConfigTypeDef",
        "httpConfig": "HttpDataSourceConfigTypeDef",
        "relationalDatabaseConfig": "RelationalDatabaseDataSourceConfigTypeDef",
    },
    total=False,
)

DeleteApiCacheRequestRequestTypeDef = TypedDict(
    "DeleteApiCacheRequestRequestTypeDef",
    {
        "apiId": str,
    },
)

DeleteApiKeyRequestRequestTypeDef = TypedDict(
    "DeleteApiKeyRequestRequestTypeDef",
    {
        "apiId": str,
        "id": str,
    },
)

DeleteDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteDataSourceRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
    },
)

DeleteFunctionRequestRequestTypeDef = TypedDict(
    "DeleteFunctionRequestRequestTypeDef",
    {
        "apiId": str,
        "functionId": str,
    },
)

DeleteGraphqlApiRequestRequestTypeDef = TypedDict(
    "DeleteGraphqlApiRequestRequestTypeDef",
    {
        "apiId": str,
    },
)

DeleteResolverRequestRequestTypeDef = TypedDict(
    "DeleteResolverRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "fieldName": str,
    },
)

DeleteTypeRequestRequestTypeDef = TypedDict(
    "DeleteTypeRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
    },
)

DeltaSyncConfigTypeDef = TypedDict(
    "DeltaSyncConfigTypeDef",
    {
        "baseTableTTL": int,
        "deltaSyncTableName": str,
        "deltaSyncTableTTL": int,
    },
    total=False,
)

_RequiredDynamodbDataSourceConfigTypeDef = TypedDict(
    "_RequiredDynamodbDataSourceConfigTypeDef",
    {
        "tableName": str,
        "awsRegion": str,
    },
)
_OptionalDynamodbDataSourceConfigTypeDef = TypedDict(
    "_OptionalDynamodbDataSourceConfigTypeDef",
    {
        "useCallerCredentials": bool,
        "deltaSyncConfig": "DeltaSyncConfigTypeDef",
        "versioned": bool,
    },
    total=False,
)

class DynamodbDataSourceConfigTypeDef(
    _RequiredDynamodbDataSourceConfigTypeDef, _OptionalDynamodbDataSourceConfigTypeDef
):
    pass

ElasticsearchDataSourceConfigTypeDef = TypedDict(
    "ElasticsearchDataSourceConfigTypeDef",
    {
        "endpoint": str,
        "awsRegion": str,
    },
)

FlushApiCacheRequestRequestTypeDef = TypedDict(
    "FlushApiCacheRequestRequestTypeDef",
    {
        "apiId": str,
    },
)

FunctionConfigurationTypeDef = TypedDict(
    "FunctionConfigurationTypeDef",
    {
        "functionId": str,
        "functionArn": str,
        "name": str,
        "description": str,
        "dataSourceName": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "functionVersion": str,
        "syncConfig": "SyncConfigTypeDef",
    },
    total=False,
)

GetApiCacheRequestRequestTypeDef = TypedDict(
    "GetApiCacheRequestRequestTypeDef",
    {
        "apiId": str,
    },
)

GetApiCacheResponseTypeDef = TypedDict(
    "GetApiCacheResponseTypeDef",
    {
        "apiCache": "ApiCacheTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataSourceRequestRequestTypeDef = TypedDict(
    "GetDataSourceRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
    },
)

GetDataSourceResponseTypeDef = TypedDict(
    "GetDataSourceResponseTypeDef",
    {
        "dataSource": "DataSourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFunctionRequestRequestTypeDef = TypedDict(
    "GetFunctionRequestRequestTypeDef",
    {
        "apiId": str,
        "functionId": str,
    },
)

GetFunctionResponseTypeDef = TypedDict(
    "GetFunctionResponseTypeDef",
    {
        "functionConfiguration": "FunctionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGraphqlApiRequestRequestTypeDef = TypedDict(
    "GetGraphqlApiRequestRequestTypeDef",
    {
        "apiId": str,
    },
)

GetGraphqlApiResponseTypeDef = TypedDict(
    "GetGraphqlApiResponseTypeDef",
    {
        "graphqlApi": "GraphqlApiTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetIntrospectionSchemaRequestRequestTypeDef = TypedDict(
    "_RequiredGetIntrospectionSchemaRequestRequestTypeDef",
    {
        "apiId": str,
        "format": OutputTypeType,
    },
)
_OptionalGetIntrospectionSchemaRequestRequestTypeDef = TypedDict(
    "_OptionalGetIntrospectionSchemaRequestRequestTypeDef",
    {
        "includeDirectives": bool,
    },
    total=False,
)

class GetIntrospectionSchemaRequestRequestTypeDef(
    _RequiredGetIntrospectionSchemaRequestRequestTypeDef,
    _OptionalGetIntrospectionSchemaRequestRequestTypeDef,
):
    pass

GetIntrospectionSchemaResponseTypeDef = TypedDict(
    "GetIntrospectionSchemaResponseTypeDef",
    {
        "schema": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverRequestRequestTypeDef = TypedDict(
    "GetResolverRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "fieldName": str,
    },
)

GetResolverResponseTypeDef = TypedDict(
    "GetResolverResponseTypeDef",
    {
        "resolver": "ResolverTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaCreationStatusRequestRequestTypeDef = TypedDict(
    "GetSchemaCreationStatusRequestRequestTypeDef",
    {
        "apiId": str,
    },
)

GetSchemaCreationStatusResponseTypeDef = TypedDict(
    "GetSchemaCreationStatusResponseTypeDef",
    {
        "status": SchemaStatusType,
        "details": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTypeRequestRequestTypeDef = TypedDict(
    "GetTypeRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "format": TypeDefinitionFormatType,
    },
)

GetTypeResponseTypeDef = TypedDict(
    "GetTypeResponseTypeDef",
    {
        "type": "TypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GraphqlApiTypeDef = TypedDict(
    "GraphqlApiTypeDef",
    {
        "name": str,
        "apiId": str,
        "authenticationType": AuthenticationTypeType,
        "logConfig": "LogConfigTypeDef",
        "userPoolConfig": "UserPoolConfigTypeDef",
        "openIDConnectConfig": "OpenIDConnectConfigTypeDef",
        "arn": str,
        "uris": Dict[str, str],
        "tags": Dict[str, str],
        "additionalAuthenticationProviders": List["AdditionalAuthenticationProviderTypeDef"],
        "xrayEnabled": bool,
        "wafWebAclArn": str,
        "lambdaAuthorizerConfig": "LambdaAuthorizerConfigTypeDef",
    },
    total=False,
)

HttpDataSourceConfigTypeDef = TypedDict(
    "HttpDataSourceConfigTypeDef",
    {
        "endpoint": str,
        "authorizationConfig": "AuthorizationConfigTypeDef",
    },
    total=False,
)

_RequiredLambdaAuthorizerConfigTypeDef = TypedDict(
    "_RequiredLambdaAuthorizerConfigTypeDef",
    {
        "authorizerUri": str,
    },
)
_OptionalLambdaAuthorizerConfigTypeDef = TypedDict(
    "_OptionalLambdaAuthorizerConfigTypeDef",
    {
        "authorizerResultTtlInSeconds": int,
        "identityValidationExpression": str,
    },
    total=False,
)

class LambdaAuthorizerConfigTypeDef(
    _RequiredLambdaAuthorizerConfigTypeDef, _OptionalLambdaAuthorizerConfigTypeDef
):
    pass

LambdaConflictHandlerConfigTypeDef = TypedDict(
    "LambdaConflictHandlerConfigTypeDef",
    {
        "lambdaConflictHandlerArn": str,
    },
    total=False,
)

LambdaDataSourceConfigTypeDef = TypedDict(
    "LambdaDataSourceConfigTypeDef",
    {
        "lambdaFunctionArn": str,
    },
)

_RequiredListApiKeysRequestRequestTypeDef = TypedDict(
    "_RequiredListApiKeysRequestRequestTypeDef",
    {
        "apiId": str,
    },
)
_OptionalListApiKeysRequestRequestTypeDef = TypedDict(
    "_OptionalListApiKeysRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListApiKeysRequestRequestTypeDef(
    _RequiredListApiKeysRequestRequestTypeDef, _OptionalListApiKeysRequestRequestTypeDef
):
    pass

ListApiKeysResponseTypeDef = TypedDict(
    "ListApiKeysResponseTypeDef",
    {
        "apiKeys": List["ApiKeyTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDataSourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListDataSourcesRequestRequestTypeDef",
    {
        "apiId": str,
    },
)
_OptionalListDataSourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListDataSourcesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListDataSourcesRequestRequestTypeDef(
    _RequiredListDataSourcesRequestRequestTypeDef, _OptionalListDataSourcesRequestRequestTypeDef
):
    pass

ListDataSourcesResponseTypeDef = TypedDict(
    "ListDataSourcesResponseTypeDef",
    {
        "dataSources": List["DataSourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFunctionsRequestRequestTypeDef = TypedDict(
    "_RequiredListFunctionsRequestRequestTypeDef",
    {
        "apiId": str,
    },
)
_OptionalListFunctionsRequestRequestTypeDef = TypedDict(
    "_OptionalListFunctionsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListFunctionsRequestRequestTypeDef(
    _RequiredListFunctionsRequestRequestTypeDef, _OptionalListFunctionsRequestRequestTypeDef
):
    pass

ListFunctionsResponseTypeDef = TypedDict(
    "ListFunctionsResponseTypeDef",
    {
        "functions": List["FunctionConfigurationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGraphqlApisRequestRequestTypeDef = TypedDict(
    "ListGraphqlApisRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListGraphqlApisResponseTypeDef = TypedDict(
    "ListGraphqlApisResponseTypeDef",
    {
        "graphqlApis": List["GraphqlApiTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResolversByFunctionRequestRequestTypeDef = TypedDict(
    "_RequiredListResolversByFunctionRequestRequestTypeDef",
    {
        "apiId": str,
        "functionId": str,
    },
)
_OptionalListResolversByFunctionRequestRequestTypeDef = TypedDict(
    "_OptionalListResolversByFunctionRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListResolversByFunctionRequestRequestTypeDef(
    _RequiredListResolversByFunctionRequestRequestTypeDef,
    _OptionalListResolversByFunctionRequestRequestTypeDef,
):
    pass

ListResolversByFunctionResponseTypeDef = TypedDict(
    "ListResolversByFunctionResponseTypeDef",
    {
        "resolvers": List["ResolverTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResolversRequestRequestTypeDef = TypedDict(
    "_RequiredListResolversRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
    },
)
_OptionalListResolversRequestRequestTypeDef = TypedDict(
    "_OptionalListResolversRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListResolversRequestRequestTypeDef(
    _RequiredListResolversRequestRequestTypeDef, _OptionalListResolversRequestRequestTypeDef
):
    pass

ListResolversResponseTypeDef = TypedDict(
    "ListResolversResponseTypeDef",
    {
        "resolvers": List["ResolverTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTypesRequestRequestTypeDef = TypedDict(
    "_RequiredListTypesRequestRequestTypeDef",
    {
        "apiId": str,
        "format": TypeDefinitionFormatType,
    },
)
_OptionalListTypesRequestRequestTypeDef = TypedDict(
    "_OptionalListTypesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListTypesRequestRequestTypeDef(
    _RequiredListTypesRequestRequestTypeDef, _OptionalListTypesRequestRequestTypeDef
):
    pass

ListTypesResponseTypeDef = TypedDict(
    "ListTypesResponseTypeDef",
    {
        "types": List["TypeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLogConfigTypeDef = TypedDict(
    "_RequiredLogConfigTypeDef",
    {
        "fieldLogLevel": FieldLogLevelType,
        "cloudWatchLogsRoleArn": str,
    },
)
_OptionalLogConfigTypeDef = TypedDict(
    "_OptionalLogConfigTypeDef",
    {
        "excludeVerboseContent": bool,
    },
    total=False,
)

class LogConfigTypeDef(_RequiredLogConfigTypeDef, _OptionalLogConfigTypeDef):
    pass

_RequiredOpenIDConnectConfigTypeDef = TypedDict(
    "_RequiredOpenIDConnectConfigTypeDef",
    {
        "issuer": str,
    },
)
_OptionalOpenIDConnectConfigTypeDef = TypedDict(
    "_OptionalOpenIDConnectConfigTypeDef",
    {
        "clientId": str,
        "iatTTL": int,
        "authTTL": int,
    },
    total=False,
)

class OpenIDConnectConfigTypeDef(
    _RequiredOpenIDConnectConfigTypeDef, _OptionalOpenIDConnectConfigTypeDef
):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PipelineConfigTypeDef = TypedDict(
    "PipelineConfigTypeDef",
    {
        "functions": List[str],
    },
    total=False,
)

RdsHttpEndpointConfigTypeDef = TypedDict(
    "RdsHttpEndpointConfigTypeDef",
    {
        "awsRegion": str,
        "dbClusterIdentifier": str,
        "databaseName": str,
        "schema": str,
        "awsSecretStoreArn": str,
    },
    total=False,
)

RelationalDatabaseDataSourceConfigTypeDef = TypedDict(
    "RelationalDatabaseDataSourceConfigTypeDef",
    {
        "relationalDatabaseSourceType": Literal["RDS_HTTP_ENDPOINT"],
        "rdsHttpEndpointConfig": "RdsHttpEndpointConfigTypeDef",
    },
    total=False,
)

ResolverTypeDef = TypedDict(
    "ResolverTypeDef",
    {
        "typeName": str,
        "fieldName": str,
        "dataSourceName": str,
        "resolverArn": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "kind": ResolverKindType,
        "pipelineConfig": "PipelineConfigTypeDef",
        "syncConfig": "SyncConfigTypeDef",
        "cachingConfig": "CachingConfigTypeDef",
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

StartSchemaCreationRequestRequestTypeDef = TypedDict(
    "StartSchemaCreationRequestRequestTypeDef",
    {
        "apiId": str,
        "definition": Union[bytes, IO[bytes], StreamingBody],
    },
)

StartSchemaCreationResponseTypeDef = TypedDict(
    "StartSchemaCreationResponseTypeDef",
    {
        "status": SchemaStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SyncConfigTypeDef = TypedDict(
    "SyncConfigTypeDef",
    {
        "conflictHandler": ConflictHandlerTypeType,
        "conflictDetection": ConflictDetectionTypeType,
        "lambdaConflictHandlerConfig": "LambdaConflictHandlerConfigTypeDef",
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TypeTypeDef = TypedDict(
    "TypeTypeDef",
    {
        "name": str,
        "description": str,
        "arn": str,
        "definition": str,
        "format": TypeDefinitionFormatType,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateApiCacheRequestRequestTypeDef = TypedDict(
    "UpdateApiCacheRequestRequestTypeDef",
    {
        "apiId": str,
        "ttl": int,
        "apiCachingBehavior": ApiCachingBehaviorType,
        "type": ApiCacheTypeType,
    },
)

UpdateApiCacheResponseTypeDef = TypedDict(
    "UpdateApiCacheResponseTypeDef",
    {
        "apiCache": "ApiCacheTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateApiKeyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApiKeyRequestRequestTypeDef",
    {
        "apiId": str,
        "id": str,
    },
)
_OptionalUpdateApiKeyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApiKeyRequestRequestTypeDef",
    {
        "description": str,
        "expires": int,
    },
    total=False,
)

class UpdateApiKeyRequestRequestTypeDef(
    _RequiredUpdateApiKeyRequestRequestTypeDef, _OptionalUpdateApiKeyRequestRequestTypeDef
):
    pass

UpdateApiKeyResponseTypeDef = TypedDict(
    "UpdateApiKeyResponseTypeDef",
    {
        "apiKey": "ApiKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDataSourceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSourceRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
        "type": DataSourceTypeType,
    },
)
_OptionalUpdateDataSourceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSourceRequestRequestTypeDef",
    {
        "description": str,
        "serviceRoleArn": str,
        "dynamodbConfig": "DynamodbDataSourceConfigTypeDef",
        "lambdaConfig": "LambdaDataSourceConfigTypeDef",
        "elasticsearchConfig": "ElasticsearchDataSourceConfigTypeDef",
        "httpConfig": "HttpDataSourceConfigTypeDef",
        "relationalDatabaseConfig": "RelationalDatabaseDataSourceConfigTypeDef",
    },
    total=False,
)

class UpdateDataSourceRequestRequestTypeDef(
    _RequiredUpdateDataSourceRequestRequestTypeDef, _OptionalUpdateDataSourceRequestRequestTypeDef
):
    pass

UpdateDataSourceResponseTypeDef = TypedDict(
    "UpdateDataSourceResponseTypeDef",
    {
        "dataSource": "DataSourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFunctionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFunctionRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
        "functionId": str,
        "dataSourceName": str,
        "functionVersion": str,
    },
)
_OptionalUpdateFunctionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFunctionRequestRequestTypeDef",
    {
        "description": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "syncConfig": "SyncConfigTypeDef",
    },
    total=False,
)

class UpdateFunctionRequestRequestTypeDef(
    _RequiredUpdateFunctionRequestRequestTypeDef, _OptionalUpdateFunctionRequestRequestTypeDef
):
    pass

UpdateFunctionResponseTypeDef = TypedDict(
    "UpdateFunctionResponseTypeDef",
    {
        "functionConfiguration": "FunctionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGraphqlApiRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateGraphqlApiRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
    },
)
_OptionalUpdateGraphqlApiRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateGraphqlApiRequestRequestTypeDef",
    {
        "logConfig": "LogConfigTypeDef",
        "authenticationType": AuthenticationTypeType,
        "userPoolConfig": "UserPoolConfigTypeDef",
        "openIDConnectConfig": "OpenIDConnectConfigTypeDef",
        "additionalAuthenticationProviders": List["AdditionalAuthenticationProviderTypeDef"],
        "xrayEnabled": bool,
        "lambdaAuthorizerConfig": "LambdaAuthorizerConfigTypeDef",
    },
    total=False,
)

class UpdateGraphqlApiRequestRequestTypeDef(
    _RequiredUpdateGraphqlApiRequestRequestTypeDef, _OptionalUpdateGraphqlApiRequestRequestTypeDef
):
    pass

UpdateGraphqlApiResponseTypeDef = TypedDict(
    "UpdateGraphqlApiResponseTypeDef",
    {
        "graphqlApi": "GraphqlApiTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateResolverRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateResolverRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "fieldName": str,
    },
)
_OptionalUpdateResolverRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateResolverRequestRequestTypeDef",
    {
        "dataSourceName": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "kind": ResolverKindType,
        "pipelineConfig": "PipelineConfigTypeDef",
        "syncConfig": "SyncConfigTypeDef",
        "cachingConfig": "CachingConfigTypeDef",
    },
    total=False,
)

class UpdateResolverRequestRequestTypeDef(
    _RequiredUpdateResolverRequestRequestTypeDef, _OptionalUpdateResolverRequestRequestTypeDef
):
    pass

UpdateResolverResponseTypeDef = TypedDict(
    "UpdateResolverResponseTypeDef",
    {
        "resolver": "ResolverTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTypeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTypeRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "format": TypeDefinitionFormatType,
    },
)
_OptionalUpdateTypeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTypeRequestRequestTypeDef",
    {
        "definition": str,
    },
    total=False,
)

class UpdateTypeRequestRequestTypeDef(
    _RequiredUpdateTypeRequestRequestTypeDef, _OptionalUpdateTypeRequestRequestTypeDef
):
    pass

UpdateTypeResponseTypeDef = TypedDict(
    "UpdateTypeResponseTypeDef",
    {
        "type": "TypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUserPoolConfigTypeDef = TypedDict(
    "_RequiredUserPoolConfigTypeDef",
    {
        "userPoolId": str,
        "awsRegion": str,
        "defaultAction": DefaultActionType,
    },
)
_OptionalUserPoolConfigTypeDef = TypedDict(
    "_OptionalUserPoolConfigTypeDef",
    {
        "appIdClientRegex": str,
    },
    total=False,
)

class UserPoolConfigTypeDef(_RequiredUserPoolConfigTypeDef, _OptionalUserPoolConfigTypeDef):
    pass
