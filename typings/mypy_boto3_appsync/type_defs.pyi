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
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ApiCacheStatusType,
    ApiCacheTypeType,
    ApiCachingBehaviorType,
    AssociationStatusType,
    AuthenticationTypeType,
    CacheHealthMetricsConfigType,
    ConflictDetectionTypeType,
    ConflictHandlerTypeType,
    DataSourceIntrospectionStatusType,
    DataSourceLevelMetricsBehaviorType,
    DataSourceLevelMetricsConfigType,
    DataSourceTypeType,
    DefaultActionType,
    FieldLogLevelType,
    GraphQLApiIntrospectionConfigType,
    GraphQLApiTypeType,
    GraphQLApiVisibilityType,
    MergeTypeType,
    OperationLevelMetricsConfigType,
    OutputTypeType,
    OwnershipType,
    ResolverKindType,
    ResolverLevelMetricsBehaviorType,
    ResolverLevelMetricsConfigType,
    SchemaStatusType,
    SourceApiAssociationStatusType,
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
    "ApiAssociationTypeDef",
    "ApiCacheTypeDef",
    "ApiKeyTypeDef",
    "AppSyncRuntimeTypeDef",
    "AssociateApiRequestRequestTypeDef",
    "AssociateApiResponseTypeDef",
    "AssociateMergedGraphqlApiRequestRequestTypeDef",
    "AssociateMergedGraphqlApiResponseTypeDef",
    "AssociateSourceGraphqlApiRequestRequestTypeDef",
    "AssociateSourceGraphqlApiResponseTypeDef",
    "AuthorizationConfigTypeDef",
    "AwsIamConfigTypeDef",
    "CachingConfigTypeDef",
    "CodeErrorLocationTypeDef",
    "CodeErrorTypeDef",
    "CognitoUserPoolConfigTypeDef",
    "CreateApiCacheRequestRequestTypeDef",
    "CreateApiCacheResponseTypeDef",
    "CreateApiKeyRequestRequestTypeDef",
    "CreateApiKeyResponseTypeDef",
    "CreateDataSourceRequestRequestTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateDomainNameRequestRequestTypeDef",
    "CreateDomainNameResponseTypeDef",
    "CreateFunctionRequestRequestTypeDef",
    "CreateFunctionResponseTypeDef",
    "CreateGraphqlApiRequestRequestTypeDef",
    "CreateGraphqlApiResponseTypeDef",
    "CreateResolverRequestRequestTypeDef",
    "CreateResolverResponseTypeDef",
    "CreateTypeRequestRequestTypeDef",
    "CreateTypeResponseTypeDef",
    "DataSourceIntrospectionModelFieldTypeDef",
    "DataSourceIntrospectionModelFieldTypeTypeDef",
    "DataSourceIntrospectionModelIndexTypeDef",
    "DataSourceIntrospectionModelTypeDef",
    "DataSourceIntrospectionResultTypeDef",
    "DataSourceTypeDef",
    "DeleteApiCacheRequestRequestTypeDef",
    "DeleteApiKeyRequestRequestTypeDef",
    "DeleteDataSourceRequestRequestTypeDef",
    "DeleteDomainNameRequestRequestTypeDef",
    "DeleteFunctionRequestRequestTypeDef",
    "DeleteGraphqlApiRequestRequestTypeDef",
    "DeleteResolverRequestRequestTypeDef",
    "DeleteTypeRequestRequestTypeDef",
    "DeltaSyncConfigTypeDef",
    "DisassociateApiRequestRequestTypeDef",
    "DisassociateMergedGraphqlApiRequestRequestTypeDef",
    "DisassociateMergedGraphqlApiResponseTypeDef",
    "DisassociateSourceGraphqlApiRequestRequestTypeDef",
    "DisassociateSourceGraphqlApiResponseTypeDef",
    "DomainNameConfigTypeDef",
    "DynamodbDataSourceConfigTypeDef",
    "ElasticsearchDataSourceConfigTypeDef",
    "EnhancedMetricsConfigTypeDef",
    "ErrorDetailTypeDef",
    "EvaluateCodeErrorDetailTypeDef",
    "EvaluateCodeRequestRequestTypeDef",
    "EvaluateCodeResponseTypeDef",
    "EvaluateMappingTemplateRequestRequestTypeDef",
    "EvaluateMappingTemplateResponseTypeDef",
    "EventBridgeDataSourceConfigTypeDef",
    "FlushApiCacheRequestRequestTypeDef",
    "FunctionConfigurationTypeDef",
    "GetApiAssociationRequestRequestTypeDef",
    "GetApiAssociationResponseTypeDef",
    "GetApiCacheRequestRequestTypeDef",
    "GetApiCacheResponseTypeDef",
    "GetDataSourceIntrospectionRequestRequestTypeDef",
    "GetDataSourceIntrospectionResponseTypeDef",
    "GetDataSourceRequestRequestTypeDef",
    "GetDataSourceResponseTypeDef",
    "GetDomainNameRequestRequestTypeDef",
    "GetDomainNameResponseTypeDef",
    "GetFunctionRequestRequestTypeDef",
    "GetFunctionResponseTypeDef",
    "GetGraphqlApiEnvironmentVariablesRequestRequestTypeDef",
    "GetGraphqlApiEnvironmentVariablesResponseTypeDef",
    "GetGraphqlApiRequestRequestTypeDef",
    "GetGraphqlApiResponseTypeDef",
    "GetIntrospectionSchemaRequestRequestTypeDef",
    "GetIntrospectionSchemaResponseTypeDef",
    "GetResolverRequestRequestTypeDef",
    "GetResolverResponseTypeDef",
    "GetSchemaCreationStatusRequestRequestTypeDef",
    "GetSchemaCreationStatusResponseTypeDef",
    "GetSourceApiAssociationRequestRequestTypeDef",
    "GetSourceApiAssociationResponseTypeDef",
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
    "ListDomainNamesRequestRequestTypeDef",
    "ListDomainNamesResponseTypeDef",
    "ListFunctionsRequestRequestTypeDef",
    "ListFunctionsResponseTypeDef",
    "ListGraphqlApisRequestRequestTypeDef",
    "ListGraphqlApisResponseTypeDef",
    "ListResolversByFunctionRequestRequestTypeDef",
    "ListResolversByFunctionResponseTypeDef",
    "ListResolversRequestRequestTypeDef",
    "ListResolversResponseTypeDef",
    "ListSourceApiAssociationsRequestRequestTypeDef",
    "ListSourceApiAssociationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTypesByAssociationRequestRequestTypeDef",
    "ListTypesByAssociationResponseTypeDef",
    "ListTypesRequestRequestTypeDef",
    "ListTypesResponseTypeDef",
    "LogConfigTypeDef",
    "OpenIDConnectConfigTypeDef",
    "OpenSearchServiceDataSourceConfigTypeDef",
    "PaginatorConfigTypeDef",
    "PipelineConfigTypeDef",
    "PutGraphqlApiEnvironmentVariablesRequestRequestTypeDef",
    "PutGraphqlApiEnvironmentVariablesResponseTypeDef",
    "RdsDataApiConfigTypeDef",
    "RdsHttpEndpointConfigTypeDef",
    "RelationalDatabaseDataSourceConfigTypeDef",
    "ResolverTypeDef",
    "ResponseMetadataTypeDef",
    "SourceApiAssociationConfigTypeDef",
    "SourceApiAssociationSummaryTypeDef",
    "SourceApiAssociationTypeDef",
    "StartDataSourceIntrospectionRequestRequestTypeDef",
    "StartDataSourceIntrospectionResponseTypeDef",
    "StartSchemaCreationRequestRequestTypeDef",
    "StartSchemaCreationResponseTypeDef",
    "StartSchemaMergeRequestRequestTypeDef",
    "StartSchemaMergeResponseTypeDef",
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
    "UpdateDomainNameRequestRequestTypeDef",
    "UpdateDomainNameResponseTypeDef",
    "UpdateFunctionRequestRequestTypeDef",
    "UpdateFunctionResponseTypeDef",
    "UpdateGraphqlApiRequestRequestTypeDef",
    "UpdateGraphqlApiResponseTypeDef",
    "UpdateResolverRequestRequestTypeDef",
    "UpdateResolverResponseTypeDef",
    "UpdateSourceApiAssociationRequestRequestTypeDef",
    "UpdateSourceApiAssociationResponseTypeDef",
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

ApiAssociationTypeDef = TypedDict(
    "ApiAssociationTypeDef",
    {
        "domainName": str,
        "apiId": str,
        "associationStatus": AssociationStatusType,
        "deploymentDetail": str,
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
        "healthMetricsConfig": CacheHealthMetricsConfigType,
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

AppSyncRuntimeTypeDef = TypedDict(
    "AppSyncRuntimeTypeDef",
    {
        "name": Literal["APPSYNC_JS"],
        "runtimeVersion": str,
    },
)

AssociateApiRequestRequestTypeDef = TypedDict(
    "AssociateApiRequestRequestTypeDef",
    {
        "domainName": str,
        "apiId": str,
    },
)

AssociateApiResponseTypeDef = TypedDict(
    "AssociateApiResponseTypeDef",
    {
        "apiAssociation": "ApiAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateMergedGraphqlApiRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateMergedGraphqlApiRequestRequestTypeDef",
    {
        "sourceApiIdentifier": str,
        "mergedApiIdentifier": str,
    },
)
_OptionalAssociateMergedGraphqlApiRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateMergedGraphqlApiRequestRequestTypeDef",
    {
        "description": str,
        "sourceApiAssociationConfig": "SourceApiAssociationConfigTypeDef",
    },
    total=False,
)

class AssociateMergedGraphqlApiRequestRequestTypeDef(
    _RequiredAssociateMergedGraphqlApiRequestRequestTypeDef,
    _OptionalAssociateMergedGraphqlApiRequestRequestTypeDef,
):
    pass

AssociateMergedGraphqlApiResponseTypeDef = TypedDict(
    "AssociateMergedGraphqlApiResponseTypeDef",
    {
        "sourceApiAssociation": "SourceApiAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateSourceGraphqlApiRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateSourceGraphqlApiRequestRequestTypeDef",
    {
        "mergedApiIdentifier": str,
        "sourceApiIdentifier": str,
    },
)
_OptionalAssociateSourceGraphqlApiRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateSourceGraphqlApiRequestRequestTypeDef",
    {
        "description": str,
        "sourceApiAssociationConfig": "SourceApiAssociationConfigTypeDef",
    },
    total=False,
)

class AssociateSourceGraphqlApiRequestRequestTypeDef(
    _RequiredAssociateSourceGraphqlApiRequestRequestTypeDef,
    _OptionalAssociateSourceGraphqlApiRequestRequestTypeDef,
):
    pass

AssociateSourceGraphqlApiResponseTypeDef = TypedDict(
    "AssociateSourceGraphqlApiResponseTypeDef",
    {
        "sourceApiAssociation": "SourceApiAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredCachingConfigTypeDef = TypedDict(
    "_RequiredCachingConfigTypeDef",
    {
        "ttl": int,
    },
)
_OptionalCachingConfigTypeDef = TypedDict(
    "_OptionalCachingConfigTypeDef",
    {
        "cachingKeys": List[str],
    },
    total=False,
)

class CachingConfigTypeDef(_RequiredCachingConfigTypeDef, _OptionalCachingConfigTypeDef):
    pass

CodeErrorLocationTypeDef = TypedDict(
    "CodeErrorLocationTypeDef",
    {
        "line": int,
        "column": int,
        "span": int,
    },
    total=False,
)

CodeErrorTypeDef = TypedDict(
    "CodeErrorTypeDef",
    {
        "errorType": str,
        "value": str,
        "location": "CodeErrorLocationTypeDef",
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
        "healthMetricsConfig": CacheHealthMetricsConfigType,
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
        "openSearchServiceConfig": "OpenSearchServiceDataSourceConfigTypeDef",
        "httpConfig": "HttpDataSourceConfigTypeDef",
        "relationalDatabaseConfig": "RelationalDatabaseDataSourceConfigTypeDef",
        "eventBridgeConfig": "EventBridgeDataSourceConfigTypeDef",
        "metricsConfig": DataSourceLevelMetricsConfigType,
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

_RequiredCreateDomainNameRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDomainNameRequestRequestTypeDef",
    {
        "domainName": str,
        "certificateArn": str,
    },
)
_OptionalCreateDomainNameRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDomainNameRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class CreateDomainNameRequestRequestTypeDef(
    _RequiredCreateDomainNameRequestRequestTypeDef, _OptionalCreateDomainNameRequestRequestTypeDef
):
    pass

CreateDomainNameResponseTypeDef = TypedDict(
    "CreateDomainNameResponseTypeDef",
    {
        "domainNameConfig": "DomainNameConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFunctionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFunctionRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
        "dataSourceName": str,
    },
)
_OptionalCreateFunctionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFunctionRequestRequestTypeDef",
    {
        "description": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "functionVersion": str,
        "syncConfig": "SyncConfigTypeDef",
        "maxBatchSize": int,
        "runtime": "AppSyncRuntimeTypeDef",
        "code": str,
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
        "visibility": GraphQLApiVisibilityType,
        "apiType": GraphQLApiTypeType,
        "mergedApiExecutionRoleArn": str,
        "ownerContact": str,
        "introspectionConfig": GraphQLApiIntrospectionConfigType,
        "queryDepthLimit": int,
        "resolverCountLimit": int,
        "enhancedMetricsConfig": "EnhancedMetricsConfigTypeDef",
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
        "maxBatchSize": int,
        "runtime": "AppSyncRuntimeTypeDef",
        "code": str,
        "metricsConfig": ResolverLevelMetricsConfigType,
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

DataSourceIntrospectionModelFieldTypeDef = TypedDict(
    "DataSourceIntrospectionModelFieldTypeDef",
    {
        "name": str,
        "type": "DataSourceIntrospectionModelFieldTypeTypeDef",
        "length": int,
    },
    total=False,
)

DataSourceIntrospectionModelFieldTypeTypeDef = TypedDict(
    "DataSourceIntrospectionModelFieldTypeTypeDef",
    {
        "kind": str,
        "name": str,
        "type": Dict[str, Any],
        "values": List[str],
    },
    total=False,
)

DataSourceIntrospectionModelIndexTypeDef = TypedDict(
    "DataSourceIntrospectionModelIndexTypeDef",
    {
        "name": str,
        "fields": List[str],
    },
    total=False,
)

DataSourceIntrospectionModelTypeDef = TypedDict(
    "DataSourceIntrospectionModelTypeDef",
    {
        "name": str,
        "fields": List["DataSourceIntrospectionModelFieldTypeDef"],
        "primaryKey": "DataSourceIntrospectionModelIndexTypeDef",
        "indexes": List["DataSourceIntrospectionModelIndexTypeDef"],
        "sdl": str,
    },
    total=False,
)

DataSourceIntrospectionResultTypeDef = TypedDict(
    "DataSourceIntrospectionResultTypeDef",
    {
        "models": List["DataSourceIntrospectionModelTypeDef"],
        "nextToken": str,
    },
    total=False,
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
        "openSearchServiceConfig": "OpenSearchServiceDataSourceConfigTypeDef",
        "httpConfig": "HttpDataSourceConfigTypeDef",
        "relationalDatabaseConfig": "RelationalDatabaseDataSourceConfigTypeDef",
        "eventBridgeConfig": "EventBridgeDataSourceConfigTypeDef",
        "metricsConfig": DataSourceLevelMetricsConfigType,
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

DeleteDomainNameRequestRequestTypeDef = TypedDict(
    "DeleteDomainNameRequestRequestTypeDef",
    {
        "domainName": str,
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

DisassociateApiRequestRequestTypeDef = TypedDict(
    "DisassociateApiRequestRequestTypeDef",
    {
        "domainName": str,
    },
)

DisassociateMergedGraphqlApiRequestRequestTypeDef = TypedDict(
    "DisassociateMergedGraphqlApiRequestRequestTypeDef",
    {
        "sourceApiIdentifier": str,
        "associationId": str,
    },
)

DisassociateMergedGraphqlApiResponseTypeDef = TypedDict(
    "DisassociateMergedGraphqlApiResponseTypeDef",
    {
        "sourceApiAssociationStatus": SourceApiAssociationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateSourceGraphqlApiRequestRequestTypeDef = TypedDict(
    "DisassociateSourceGraphqlApiRequestRequestTypeDef",
    {
        "mergedApiIdentifier": str,
        "associationId": str,
    },
)

DisassociateSourceGraphqlApiResponseTypeDef = TypedDict(
    "DisassociateSourceGraphqlApiResponseTypeDef",
    {
        "sourceApiAssociationStatus": SourceApiAssociationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainNameConfigTypeDef = TypedDict(
    "DomainNameConfigTypeDef",
    {
        "domainName": str,
        "description": str,
        "certificateArn": str,
        "appsyncDomainName": str,
        "hostedZoneId": str,
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

EnhancedMetricsConfigTypeDef = TypedDict(
    "EnhancedMetricsConfigTypeDef",
    {
        "resolverLevelMetricsBehavior": ResolverLevelMetricsBehaviorType,
        "dataSourceLevelMetricsBehavior": DataSourceLevelMetricsBehaviorType,
        "operationLevelMetricsConfig": OperationLevelMetricsConfigType,
    },
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "message": str,
    },
    total=False,
)

EvaluateCodeErrorDetailTypeDef = TypedDict(
    "EvaluateCodeErrorDetailTypeDef",
    {
        "message": str,
        "codeErrors": List["CodeErrorTypeDef"],
    },
    total=False,
)

_RequiredEvaluateCodeRequestRequestTypeDef = TypedDict(
    "_RequiredEvaluateCodeRequestRequestTypeDef",
    {
        "runtime": "AppSyncRuntimeTypeDef",
        "code": str,
        "context": str,
    },
)
_OptionalEvaluateCodeRequestRequestTypeDef = TypedDict(
    "_OptionalEvaluateCodeRequestRequestTypeDef",
    {
        "function": str,
    },
    total=False,
)

class EvaluateCodeRequestRequestTypeDef(
    _RequiredEvaluateCodeRequestRequestTypeDef, _OptionalEvaluateCodeRequestRequestTypeDef
):
    pass

EvaluateCodeResponseTypeDef = TypedDict(
    "EvaluateCodeResponseTypeDef",
    {
        "evaluationResult": str,
        "error": "EvaluateCodeErrorDetailTypeDef",
        "logs": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EvaluateMappingTemplateRequestRequestTypeDef = TypedDict(
    "EvaluateMappingTemplateRequestRequestTypeDef",
    {
        "template": str,
        "context": str,
    },
)

EvaluateMappingTemplateResponseTypeDef = TypedDict(
    "EvaluateMappingTemplateResponseTypeDef",
    {
        "evaluationResult": str,
        "error": "ErrorDetailTypeDef",
        "logs": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventBridgeDataSourceConfigTypeDef = TypedDict(
    "EventBridgeDataSourceConfigTypeDef",
    {
        "eventBusArn": str,
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
        "maxBatchSize": int,
        "runtime": "AppSyncRuntimeTypeDef",
        "code": str,
    },
    total=False,
)

GetApiAssociationRequestRequestTypeDef = TypedDict(
    "GetApiAssociationRequestRequestTypeDef",
    {
        "domainName": str,
    },
)

GetApiAssociationResponseTypeDef = TypedDict(
    "GetApiAssociationResponseTypeDef",
    {
        "apiAssociation": "ApiAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredGetDataSourceIntrospectionRequestRequestTypeDef = TypedDict(
    "_RequiredGetDataSourceIntrospectionRequestRequestTypeDef",
    {
        "introspectionId": str,
    },
)
_OptionalGetDataSourceIntrospectionRequestRequestTypeDef = TypedDict(
    "_OptionalGetDataSourceIntrospectionRequestRequestTypeDef",
    {
        "includeModelsSDL": bool,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetDataSourceIntrospectionRequestRequestTypeDef(
    _RequiredGetDataSourceIntrospectionRequestRequestTypeDef,
    _OptionalGetDataSourceIntrospectionRequestRequestTypeDef,
):
    pass

GetDataSourceIntrospectionResponseTypeDef = TypedDict(
    "GetDataSourceIntrospectionResponseTypeDef",
    {
        "introspectionId": str,
        "introspectionStatus": DataSourceIntrospectionStatusType,
        "introspectionStatusDetail": str,
        "introspectionResult": "DataSourceIntrospectionResultTypeDef",
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

GetDomainNameRequestRequestTypeDef = TypedDict(
    "GetDomainNameRequestRequestTypeDef",
    {
        "domainName": str,
    },
)

GetDomainNameResponseTypeDef = TypedDict(
    "GetDomainNameResponseTypeDef",
    {
        "domainNameConfig": "DomainNameConfigTypeDef",
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

GetGraphqlApiEnvironmentVariablesRequestRequestTypeDef = TypedDict(
    "GetGraphqlApiEnvironmentVariablesRequestRequestTypeDef",
    {
        "apiId": str,
    },
)

GetGraphqlApiEnvironmentVariablesResponseTypeDef = TypedDict(
    "GetGraphqlApiEnvironmentVariablesResponseTypeDef",
    {
        "environmentVariables": Dict[str, str],
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

GetSourceApiAssociationRequestRequestTypeDef = TypedDict(
    "GetSourceApiAssociationRequestRequestTypeDef",
    {
        "mergedApiIdentifier": str,
        "associationId": str,
    },
)

GetSourceApiAssociationResponseTypeDef = TypedDict(
    "GetSourceApiAssociationResponseTypeDef",
    {
        "sourceApiAssociation": "SourceApiAssociationTypeDef",
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
        "dns": Dict[str, str],
        "visibility": GraphQLApiVisibilityType,
        "apiType": GraphQLApiTypeType,
        "mergedApiExecutionRoleArn": str,
        "owner": str,
        "ownerContact": str,
        "introspectionConfig": GraphQLApiIntrospectionConfigType,
        "queryDepthLimit": int,
        "resolverCountLimit": int,
        "enhancedMetricsConfig": "EnhancedMetricsConfigTypeDef",
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

ListDomainNamesRequestRequestTypeDef = TypedDict(
    "ListDomainNamesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDomainNamesResponseTypeDef = TypedDict(
    "ListDomainNamesResponseTypeDef",
    {
        "domainNameConfigs": List["DomainNameConfigTypeDef"],
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
        "apiType": GraphQLApiTypeType,
        "owner": OwnershipType,
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

_RequiredListSourceApiAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredListSourceApiAssociationsRequestRequestTypeDef",
    {
        "apiId": str,
    },
)
_OptionalListSourceApiAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalListSourceApiAssociationsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListSourceApiAssociationsRequestRequestTypeDef(
    _RequiredListSourceApiAssociationsRequestRequestTypeDef,
    _OptionalListSourceApiAssociationsRequestRequestTypeDef,
):
    pass

ListSourceApiAssociationsResponseTypeDef = TypedDict(
    "ListSourceApiAssociationsResponseTypeDef",
    {
        "sourceApiAssociationSummaries": List["SourceApiAssociationSummaryTypeDef"],
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

_RequiredListTypesByAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredListTypesByAssociationRequestRequestTypeDef",
    {
        "mergedApiIdentifier": str,
        "associationId": str,
        "format": TypeDefinitionFormatType,
    },
)
_OptionalListTypesByAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalListTypesByAssociationRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListTypesByAssociationRequestRequestTypeDef(
    _RequiredListTypesByAssociationRequestRequestTypeDef,
    _OptionalListTypesByAssociationRequestRequestTypeDef,
):
    pass

ListTypesByAssociationResponseTypeDef = TypedDict(
    "ListTypesByAssociationResponseTypeDef",
    {
        "types": List["TypeTypeDef"],
        "nextToken": str,
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

OpenSearchServiceDataSourceConfigTypeDef = TypedDict(
    "OpenSearchServiceDataSourceConfigTypeDef",
    {
        "endpoint": str,
        "awsRegion": str,
    },
)

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

PutGraphqlApiEnvironmentVariablesRequestRequestTypeDef = TypedDict(
    "PutGraphqlApiEnvironmentVariablesRequestRequestTypeDef",
    {
        "apiId": str,
        "environmentVariables": Dict[str, str],
    },
)

PutGraphqlApiEnvironmentVariablesResponseTypeDef = TypedDict(
    "PutGraphqlApiEnvironmentVariablesResponseTypeDef",
    {
        "environmentVariables": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RdsDataApiConfigTypeDef = TypedDict(
    "RdsDataApiConfigTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "databaseName": str,
    },
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
        "maxBatchSize": int,
        "runtime": "AppSyncRuntimeTypeDef",
        "code": str,
        "metricsConfig": ResolverLevelMetricsConfigType,
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

SourceApiAssociationConfigTypeDef = TypedDict(
    "SourceApiAssociationConfigTypeDef",
    {
        "mergeType": MergeTypeType,
    },
    total=False,
)

SourceApiAssociationSummaryTypeDef = TypedDict(
    "SourceApiAssociationSummaryTypeDef",
    {
        "associationId": str,
        "associationArn": str,
        "sourceApiId": str,
        "sourceApiArn": str,
        "mergedApiId": str,
        "mergedApiArn": str,
        "description": str,
    },
    total=False,
)

SourceApiAssociationTypeDef = TypedDict(
    "SourceApiAssociationTypeDef",
    {
        "associationId": str,
        "associationArn": str,
        "sourceApiId": str,
        "sourceApiArn": str,
        "mergedApiArn": str,
        "mergedApiId": str,
        "description": str,
        "sourceApiAssociationConfig": "SourceApiAssociationConfigTypeDef",
        "sourceApiAssociationStatus": SourceApiAssociationStatusType,
        "sourceApiAssociationStatusDetail": str,
        "lastSuccessfulMergeDate": datetime,
    },
    total=False,
)

StartDataSourceIntrospectionRequestRequestTypeDef = TypedDict(
    "StartDataSourceIntrospectionRequestRequestTypeDef",
    {
        "rdsDataApiConfig": "RdsDataApiConfigTypeDef",
    },
    total=False,
)

StartDataSourceIntrospectionResponseTypeDef = TypedDict(
    "StartDataSourceIntrospectionResponseTypeDef",
    {
        "introspectionId": str,
        "introspectionStatus": DataSourceIntrospectionStatusType,
        "introspectionStatusDetail": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

StartSchemaMergeRequestRequestTypeDef = TypedDict(
    "StartSchemaMergeRequestRequestTypeDef",
    {
        "associationId": str,
        "mergedApiIdentifier": str,
    },
)

StartSchemaMergeResponseTypeDef = TypedDict(
    "StartSchemaMergeResponseTypeDef",
    {
        "sourceApiAssociationStatus": SourceApiAssociationStatusType,
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

_RequiredUpdateApiCacheRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApiCacheRequestRequestTypeDef",
    {
        "apiId": str,
        "ttl": int,
        "apiCachingBehavior": ApiCachingBehaviorType,
        "type": ApiCacheTypeType,
    },
)
_OptionalUpdateApiCacheRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApiCacheRequestRequestTypeDef",
    {
        "healthMetricsConfig": CacheHealthMetricsConfigType,
    },
    total=False,
)

class UpdateApiCacheRequestRequestTypeDef(
    _RequiredUpdateApiCacheRequestRequestTypeDef, _OptionalUpdateApiCacheRequestRequestTypeDef
):
    pass

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
        "openSearchServiceConfig": "OpenSearchServiceDataSourceConfigTypeDef",
        "httpConfig": "HttpDataSourceConfigTypeDef",
        "relationalDatabaseConfig": "RelationalDatabaseDataSourceConfigTypeDef",
        "eventBridgeConfig": "EventBridgeDataSourceConfigTypeDef",
        "metricsConfig": DataSourceLevelMetricsConfigType,
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

_RequiredUpdateDomainNameRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainNameRequestRequestTypeDef",
    {
        "domainName": str,
    },
)
_OptionalUpdateDomainNameRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainNameRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateDomainNameRequestRequestTypeDef(
    _RequiredUpdateDomainNameRequestRequestTypeDef, _OptionalUpdateDomainNameRequestRequestTypeDef
):
    pass

UpdateDomainNameResponseTypeDef = TypedDict(
    "UpdateDomainNameResponseTypeDef",
    {
        "domainNameConfig": "DomainNameConfigTypeDef",
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
    },
)
_OptionalUpdateFunctionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFunctionRequestRequestTypeDef",
    {
        "description": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "functionVersion": str,
        "syncConfig": "SyncConfigTypeDef",
        "maxBatchSize": int,
        "runtime": "AppSyncRuntimeTypeDef",
        "code": str,
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
        "authenticationType": AuthenticationTypeType,
    },
)
_OptionalUpdateGraphqlApiRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateGraphqlApiRequestRequestTypeDef",
    {
        "logConfig": "LogConfigTypeDef",
        "userPoolConfig": "UserPoolConfigTypeDef",
        "openIDConnectConfig": "OpenIDConnectConfigTypeDef",
        "additionalAuthenticationProviders": List["AdditionalAuthenticationProviderTypeDef"],
        "xrayEnabled": bool,
        "lambdaAuthorizerConfig": "LambdaAuthorizerConfigTypeDef",
        "mergedApiExecutionRoleArn": str,
        "ownerContact": str,
        "introspectionConfig": GraphQLApiIntrospectionConfigType,
        "queryDepthLimit": int,
        "resolverCountLimit": int,
        "enhancedMetricsConfig": "EnhancedMetricsConfigTypeDef",
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
        "maxBatchSize": int,
        "runtime": "AppSyncRuntimeTypeDef",
        "code": str,
        "metricsConfig": ResolverLevelMetricsConfigType,
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

_RequiredUpdateSourceApiAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSourceApiAssociationRequestRequestTypeDef",
    {
        "associationId": str,
        "mergedApiIdentifier": str,
    },
)
_OptionalUpdateSourceApiAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSourceApiAssociationRequestRequestTypeDef",
    {
        "description": str,
        "sourceApiAssociationConfig": "SourceApiAssociationConfigTypeDef",
    },
    total=False,
)

class UpdateSourceApiAssociationRequestRequestTypeDef(
    _RequiredUpdateSourceApiAssociationRequestRequestTypeDef,
    _OptionalUpdateSourceApiAssociationRequestRequestTypeDef,
):
    pass

UpdateSourceApiAssociationResponseTypeDef = TypedDict(
    "UpdateSourceApiAssociationResponseTypeDef",
    {
        "sourceApiAssociation": "SourceApiAssociationTypeDef",
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
