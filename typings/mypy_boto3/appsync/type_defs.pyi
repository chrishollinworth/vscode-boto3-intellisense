"""
Type annotations for appsync service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_appsync.type_defs import CognitoUserPoolConfigTypeDef

    data: CognitoUserPoolConfigTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

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
    EventLogLevelType,
    FieldLogLevelType,
    GraphQLApiIntrospectionConfigType,
    GraphQLApiTypeType,
    GraphQLApiVisibilityType,
    HandlerBehaviorType,
    InvokeTypeType,
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

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AdditionalAuthenticationProviderTypeDef",
    "ApiAssociationTypeDef",
    "ApiCacheTypeDef",
    "ApiKeyTypeDef",
    "ApiTypeDef",
    "AppSyncRuntimeTypeDef",
    "AssociateApiRequestTypeDef",
    "AssociateApiResponseTypeDef",
    "AssociateMergedGraphqlApiRequestTypeDef",
    "AssociateMergedGraphqlApiResponseTypeDef",
    "AssociateSourceGraphqlApiRequestTypeDef",
    "AssociateSourceGraphqlApiResponseTypeDef",
    "AuthModeTypeDef",
    "AuthProviderTypeDef",
    "AuthorizationConfigTypeDef",
    "AwsIamConfigTypeDef",
    "BlobTypeDef",
    "CachingConfigOutputTypeDef",
    "CachingConfigTypeDef",
    "CachingConfigUnionTypeDef",
    "ChannelNamespaceTypeDef",
    "CodeErrorLocationTypeDef",
    "CodeErrorTypeDef",
    "CognitoConfigTypeDef",
    "CognitoUserPoolConfigTypeDef",
    "CreateApiCacheRequestTypeDef",
    "CreateApiCacheResponseTypeDef",
    "CreateApiKeyRequestTypeDef",
    "CreateApiKeyResponseTypeDef",
    "CreateApiRequestTypeDef",
    "CreateApiResponseTypeDef",
    "CreateChannelNamespaceRequestTypeDef",
    "CreateChannelNamespaceResponseTypeDef",
    "CreateDataSourceRequestTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateDomainNameRequestTypeDef",
    "CreateDomainNameResponseTypeDef",
    "CreateFunctionRequestTypeDef",
    "CreateFunctionResponseTypeDef",
    "CreateGraphqlApiRequestTypeDef",
    "CreateGraphqlApiResponseTypeDef",
    "CreateResolverRequestTypeDef",
    "CreateResolverResponseTypeDef",
    "CreateTypeRequestTypeDef",
    "CreateTypeResponseTypeDef",
    "DataSourceIntrospectionModelFieldTypeDef",
    "DataSourceIntrospectionModelFieldTypeTypeDef",
    "DataSourceIntrospectionModelIndexTypeDef",
    "DataSourceIntrospectionModelTypeDef",
    "DataSourceIntrospectionResultTypeDef",
    "DataSourceTypeDef",
    "DeleteApiCacheRequestTypeDef",
    "DeleteApiKeyRequestTypeDef",
    "DeleteApiRequestTypeDef",
    "DeleteChannelNamespaceRequestTypeDef",
    "DeleteDataSourceRequestTypeDef",
    "DeleteDomainNameRequestTypeDef",
    "DeleteFunctionRequestTypeDef",
    "DeleteGraphqlApiRequestTypeDef",
    "DeleteResolverRequestTypeDef",
    "DeleteTypeRequestTypeDef",
    "DeltaSyncConfigTypeDef",
    "DisassociateApiRequestTypeDef",
    "DisassociateMergedGraphqlApiRequestTypeDef",
    "DisassociateMergedGraphqlApiResponseTypeDef",
    "DisassociateSourceGraphqlApiRequestTypeDef",
    "DisassociateSourceGraphqlApiResponseTypeDef",
    "DomainNameConfigTypeDef",
    "DynamodbDataSourceConfigTypeDef",
    "ElasticsearchDataSourceConfigTypeDef",
    "EnhancedMetricsConfigTypeDef",
    "ErrorDetailTypeDef",
    "EvaluateCodeErrorDetailTypeDef",
    "EvaluateCodeRequestTypeDef",
    "EvaluateCodeResponseTypeDef",
    "EvaluateMappingTemplateRequestTypeDef",
    "EvaluateMappingTemplateResponseTypeDef",
    "EventBridgeDataSourceConfigTypeDef",
    "EventConfigOutputTypeDef",
    "EventConfigTypeDef",
    "EventConfigUnionTypeDef",
    "EventLogConfigTypeDef",
    "FlushApiCacheRequestTypeDef",
    "FunctionConfigurationTypeDef",
    "GetApiAssociationRequestTypeDef",
    "GetApiAssociationResponseTypeDef",
    "GetApiCacheRequestTypeDef",
    "GetApiCacheResponseTypeDef",
    "GetApiRequestTypeDef",
    "GetApiResponseTypeDef",
    "GetChannelNamespaceRequestTypeDef",
    "GetChannelNamespaceResponseTypeDef",
    "GetDataSourceIntrospectionRequestTypeDef",
    "GetDataSourceIntrospectionResponseTypeDef",
    "GetDataSourceRequestTypeDef",
    "GetDataSourceResponseTypeDef",
    "GetDomainNameRequestTypeDef",
    "GetDomainNameResponseTypeDef",
    "GetFunctionRequestTypeDef",
    "GetFunctionResponseTypeDef",
    "GetGraphqlApiEnvironmentVariablesRequestTypeDef",
    "GetGraphqlApiEnvironmentVariablesResponseTypeDef",
    "GetGraphqlApiRequestTypeDef",
    "GetGraphqlApiResponseTypeDef",
    "GetIntrospectionSchemaRequestTypeDef",
    "GetIntrospectionSchemaResponseTypeDef",
    "GetResolverRequestTypeDef",
    "GetResolverResponseTypeDef",
    "GetSchemaCreationStatusRequestTypeDef",
    "GetSchemaCreationStatusResponseTypeDef",
    "GetSourceApiAssociationRequestTypeDef",
    "GetSourceApiAssociationResponseTypeDef",
    "GetTypeRequestTypeDef",
    "GetTypeResponseTypeDef",
    "GraphqlApiTypeDef",
    "HandlerConfigTypeDef",
    "HandlerConfigsTypeDef",
    "HttpDataSourceConfigTypeDef",
    "IntegrationTypeDef",
    "LambdaAuthorizerConfigTypeDef",
    "LambdaConfigTypeDef",
    "LambdaConflictHandlerConfigTypeDef",
    "LambdaDataSourceConfigTypeDef",
    "ListApiKeysRequestPaginateTypeDef",
    "ListApiKeysRequestTypeDef",
    "ListApiKeysResponseTypeDef",
    "ListApisRequestPaginateTypeDef",
    "ListApisRequestTypeDef",
    "ListApisResponseTypeDef",
    "ListChannelNamespacesRequestPaginateTypeDef",
    "ListChannelNamespacesRequestTypeDef",
    "ListChannelNamespacesResponseTypeDef",
    "ListDataSourcesRequestPaginateTypeDef",
    "ListDataSourcesRequestTypeDef",
    "ListDataSourcesResponseTypeDef",
    "ListDomainNamesRequestPaginateTypeDef",
    "ListDomainNamesRequestTypeDef",
    "ListDomainNamesResponseTypeDef",
    "ListFunctionsRequestPaginateTypeDef",
    "ListFunctionsRequestTypeDef",
    "ListFunctionsResponseTypeDef",
    "ListGraphqlApisRequestPaginateTypeDef",
    "ListGraphqlApisRequestTypeDef",
    "ListGraphqlApisResponseTypeDef",
    "ListResolversByFunctionRequestPaginateTypeDef",
    "ListResolversByFunctionRequestTypeDef",
    "ListResolversByFunctionResponseTypeDef",
    "ListResolversRequestPaginateTypeDef",
    "ListResolversRequestTypeDef",
    "ListResolversResponseTypeDef",
    "ListSourceApiAssociationsRequestPaginateTypeDef",
    "ListSourceApiAssociationsRequestTypeDef",
    "ListSourceApiAssociationsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTypesByAssociationRequestPaginateTypeDef",
    "ListTypesByAssociationRequestTypeDef",
    "ListTypesByAssociationResponseTypeDef",
    "ListTypesRequestPaginateTypeDef",
    "ListTypesRequestTypeDef",
    "ListTypesResponseTypeDef",
    "LogConfigTypeDef",
    "OpenIDConnectConfigTypeDef",
    "OpenSearchServiceDataSourceConfigTypeDef",
    "PaginatorConfigTypeDef",
    "PipelineConfigOutputTypeDef",
    "PipelineConfigTypeDef",
    "PipelineConfigUnionTypeDef",
    "PutGraphqlApiEnvironmentVariablesRequestTypeDef",
    "PutGraphqlApiEnvironmentVariablesResponseTypeDef",
    "RdsDataApiConfigTypeDef",
    "RdsHttpEndpointConfigTypeDef",
    "RelationalDatabaseDataSourceConfigTypeDef",
    "ResolverTypeDef",
    "ResponseMetadataTypeDef",
    "SourceApiAssociationConfigTypeDef",
    "SourceApiAssociationSummaryTypeDef",
    "SourceApiAssociationTypeDef",
    "StartDataSourceIntrospectionRequestTypeDef",
    "StartDataSourceIntrospectionResponseTypeDef",
    "StartSchemaCreationRequestTypeDef",
    "StartSchemaCreationResponseTypeDef",
    "StartSchemaMergeRequestTypeDef",
    "StartSchemaMergeResponseTypeDef",
    "SyncConfigTypeDef",
    "TagResourceRequestTypeDef",
    "TypeTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateApiCacheRequestTypeDef",
    "UpdateApiCacheResponseTypeDef",
    "UpdateApiKeyRequestTypeDef",
    "UpdateApiKeyResponseTypeDef",
    "UpdateApiRequestTypeDef",
    "UpdateApiResponseTypeDef",
    "UpdateChannelNamespaceRequestTypeDef",
    "UpdateChannelNamespaceResponseTypeDef",
    "UpdateDataSourceRequestTypeDef",
    "UpdateDataSourceResponseTypeDef",
    "UpdateDomainNameRequestTypeDef",
    "UpdateDomainNameResponseTypeDef",
    "UpdateFunctionRequestTypeDef",
    "UpdateFunctionResponseTypeDef",
    "UpdateGraphqlApiRequestTypeDef",
    "UpdateGraphqlApiResponseTypeDef",
    "UpdateResolverRequestTypeDef",
    "UpdateResolverResponseTypeDef",
    "UpdateSourceApiAssociationRequestTypeDef",
    "UpdateSourceApiAssociationResponseTypeDef",
    "UpdateTypeRequestTypeDef",
    "UpdateTypeResponseTypeDef",
    "UserPoolConfigTypeDef",
)

class CognitoUserPoolConfigTypeDef(TypedDict):
    userPoolId: str
    awsRegion: str
    appIdClientRegex: NotRequired[str]

class LambdaAuthorizerConfigTypeDef(TypedDict):
    authorizerUri: str
    authorizerResultTtlInSeconds: NotRequired[int]
    identityValidationExpression: NotRequired[str]

class OpenIDConnectConfigTypeDef(TypedDict):
    issuer: str
    clientId: NotRequired[str]
    iatTTL: NotRequired[int]
    authTTL: NotRequired[int]

class ApiAssociationTypeDef(TypedDict):
    domainName: NotRequired[str]
    apiId: NotRequired[str]
    associationStatus: NotRequired[AssociationStatusType]
    deploymentDetail: NotRequired[str]

ApiCacheTypeDef = TypedDict(
    "ApiCacheTypeDef",
    {
        "ttl": NotRequired[int],
        "apiCachingBehavior": NotRequired[ApiCachingBehaviorType],
        "transitEncryptionEnabled": NotRequired[bool],
        "atRestEncryptionEnabled": NotRequired[bool],
        "type": NotRequired[ApiCacheTypeType],
        "status": NotRequired[ApiCacheStatusType],
        "healthMetricsConfig": NotRequired[CacheHealthMetricsConfigType],
    },
)
ApiKeyTypeDef = TypedDict(
    "ApiKeyTypeDef",
    {
        "id": NotRequired[str],
        "description": NotRequired[str],
        "expires": NotRequired[int],
        "deletes": NotRequired[int],
    },
)

class AppSyncRuntimeTypeDef(TypedDict):
    name: Literal["APPSYNC_JS"]
    runtimeVersion: str

class AssociateApiRequestTypeDef(TypedDict):
    domainName: str
    apiId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class SourceApiAssociationConfigTypeDef(TypedDict):
    mergeType: NotRequired[MergeTypeType]

class AuthModeTypeDef(TypedDict):
    authType: AuthenticationTypeType

class CognitoConfigTypeDef(TypedDict):
    userPoolId: str
    awsRegion: str
    appIdClientRegex: NotRequired[str]

class AwsIamConfigTypeDef(TypedDict):
    signingRegion: NotRequired[str]
    signingServiceName: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CachingConfigOutputTypeDef(TypedDict):
    ttl: int
    cachingKeys: NotRequired[List[str]]

class CachingConfigTypeDef(TypedDict):
    ttl: int
    cachingKeys: NotRequired[Sequence[str]]

class CodeErrorLocationTypeDef(TypedDict):
    line: NotRequired[int]
    column: NotRequired[int]
    span: NotRequired[int]

CreateApiCacheRequestTypeDef = TypedDict(
    "CreateApiCacheRequestTypeDef",
    {
        "apiId": str,
        "ttl": int,
        "apiCachingBehavior": ApiCachingBehaviorType,
        "type": ApiCacheTypeType,
        "transitEncryptionEnabled": NotRequired[bool],
        "atRestEncryptionEnabled": NotRequired[bool],
        "healthMetricsConfig": NotRequired[CacheHealthMetricsConfigType],
    },
)

class CreateApiKeyRequestTypeDef(TypedDict):
    apiId: str
    description: NotRequired[str]
    expires: NotRequired[int]

class ElasticsearchDataSourceConfigTypeDef(TypedDict):
    endpoint: str
    awsRegion: str

class EventBridgeDataSourceConfigTypeDef(TypedDict):
    eventBusArn: str

class LambdaDataSourceConfigTypeDef(TypedDict):
    lambdaFunctionArn: str

class OpenSearchServiceDataSourceConfigTypeDef(TypedDict):
    endpoint: str
    awsRegion: str

class CreateDomainNameRequestTypeDef(TypedDict):
    domainName: str
    certificateArn: str
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class DomainNameConfigTypeDef(TypedDict):
    domainName: NotRequired[str]
    description: NotRequired[str]
    certificateArn: NotRequired[str]
    appsyncDomainName: NotRequired[str]
    hostedZoneId: NotRequired[str]
    tags: NotRequired[Dict[str, str]]
    domainNameArn: NotRequired[str]

class EnhancedMetricsConfigTypeDef(TypedDict):
    resolverLevelMetricsBehavior: ResolverLevelMetricsBehaviorType
    dataSourceLevelMetricsBehavior: DataSourceLevelMetricsBehaviorType
    operationLevelMetricsConfig: OperationLevelMetricsConfigType

class LogConfigTypeDef(TypedDict):
    fieldLogLevel: FieldLogLevelType
    cloudWatchLogsRoleArn: str
    excludeVerboseContent: NotRequired[bool]

class UserPoolConfigTypeDef(TypedDict):
    userPoolId: str
    awsRegion: str
    defaultAction: DefaultActionType
    appIdClientRegex: NotRequired[str]

CreateTypeRequestTypeDef = TypedDict(
    "CreateTypeRequestTypeDef",
    {
        "apiId": str,
        "definition": str,
        "format": TypeDefinitionFormatType,
    },
)
TypeTypeDef = TypedDict(
    "TypeTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "arn": NotRequired[str],
        "definition": NotRequired[str],
        "format": NotRequired[TypeDefinitionFormatType],
    },
)
DataSourceIntrospectionModelFieldTypeTypeDef = TypedDict(
    "DataSourceIntrospectionModelFieldTypeTypeDef",
    {
        "kind": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[Dict[str, Any]],
        "values": NotRequired[List[str]],
    },
)

class DataSourceIntrospectionModelIndexTypeDef(TypedDict):
    name: NotRequired[str]
    fields: NotRequired[List[str]]

class DeleteApiCacheRequestTypeDef(TypedDict):
    apiId: str

DeleteApiKeyRequestTypeDef = TypedDict(
    "DeleteApiKeyRequestTypeDef",
    {
        "apiId": str,
        "id": str,
    },
)

class DeleteApiRequestTypeDef(TypedDict):
    apiId: str

class DeleteChannelNamespaceRequestTypeDef(TypedDict):
    apiId: str
    name: str

class DeleteDataSourceRequestTypeDef(TypedDict):
    apiId: str
    name: str

class DeleteDomainNameRequestTypeDef(TypedDict):
    domainName: str

class DeleteFunctionRequestTypeDef(TypedDict):
    apiId: str
    functionId: str

class DeleteGraphqlApiRequestTypeDef(TypedDict):
    apiId: str

class DeleteResolverRequestTypeDef(TypedDict):
    apiId: str
    typeName: str
    fieldName: str

class DeleteTypeRequestTypeDef(TypedDict):
    apiId: str
    typeName: str

class DeltaSyncConfigTypeDef(TypedDict):
    baseTableTTL: NotRequired[int]
    deltaSyncTableName: NotRequired[str]
    deltaSyncTableTTL: NotRequired[int]

class DisassociateApiRequestTypeDef(TypedDict):
    domainName: str

class DisassociateMergedGraphqlApiRequestTypeDef(TypedDict):
    sourceApiIdentifier: str
    associationId: str

class DisassociateSourceGraphqlApiRequestTypeDef(TypedDict):
    mergedApiIdentifier: str
    associationId: str

class ErrorDetailTypeDef(TypedDict):
    message: NotRequired[str]

class EvaluateMappingTemplateRequestTypeDef(TypedDict):
    template: str
    context: str

class EventLogConfigTypeDef(TypedDict):
    logLevel: EventLogLevelType
    cloudWatchLogsRoleArn: str

class FlushApiCacheRequestTypeDef(TypedDict):
    apiId: str

class GetApiAssociationRequestTypeDef(TypedDict):
    domainName: str

class GetApiCacheRequestTypeDef(TypedDict):
    apiId: str

class GetApiRequestTypeDef(TypedDict):
    apiId: str

class GetChannelNamespaceRequestTypeDef(TypedDict):
    apiId: str
    name: str

class GetDataSourceIntrospectionRequestTypeDef(TypedDict):
    introspectionId: str
    includeModelsSDL: NotRequired[bool]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class GetDataSourceRequestTypeDef(TypedDict):
    apiId: str
    name: str

class GetDomainNameRequestTypeDef(TypedDict):
    domainName: str

class GetFunctionRequestTypeDef(TypedDict):
    apiId: str
    functionId: str

class GetGraphqlApiEnvironmentVariablesRequestTypeDef(TypedDict):
    apiId: str

class GetGraphqlApiRequestTypeDef(TypedDict):
    apiId: str

GetIntrospectionSchemaRequestTypeDef = TypedDict(
    "GetIntrospectionSchemaRequestTypeDef",
    {
        "apiId": str,
        "format": OutputTypeType,
        "includeDirectives": NotRequired[bool],
    },
)

class GetResolverRequestTypeDef(TypedDict):
    apiId: str
    typeName: str
    fieldName: str

class GetSchemaCreationStatusRequestTypeDef(TypedDict):
    apiId: str

class GetSourceApiAssociationRequestTypeDef(TypedDict):
    mergedApiIdentifier: str
    associationId: str

GetTypeRequestTypeDef = TypedDict(
    "GetTypeRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "format": TypeDefinitionFormatType,
    },
)

class LambdaConfigTypeDef(TypedDict):
    invokeType: NotRequired[InvokeTypeType]

class LambdaConflictHandlerConfigTypeDef(TypedDict):
    lambdaConflictHandlerArn: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListApiKeysRequestTypeDef(TypedDict):
    apiId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListApisRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListChannelNamespacesRequestTypeDef(TypedDict):
    apiId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListDataSourcesRequestTypeDef(TypedDict):
    apiId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListDomainNamesRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListFunctionsRequestTypeDef(TypedDict):
    apiId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListGraphqlApisRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    apiType: NotRequired[GraphQLApiTypeType]
    owner: NotRequired[OwnershipType]

class ListResolversByFunctionRequestTypeDef(TypedDict):
    apiId: str
    functionId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListResolversRequestTypeDef(TypedDict):
    apiId: str
    typeName: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListSourceApiAssociationsRequestTypeDef(TypedDict):
    apiId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class SourceApiAssociationSummaryTypeDef(TypedDict):
    associationId: NotRequired[str]
    associationArn: NotRequired[str]
    sourceApiId: NotRequired[str]
    sourceApiArn: NotRequired[str]
    mergedApiId: NotRequired[str]
    mergedApiArn: NotRequired[str]
    description: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

ListTypesByAssociationRequestTypeDef = TypedDict(
    "ListTypesByAssociationRequestTypeDef",
    {
        "mergedApiIdentifier": str,
        "associationId": str,
        "format": TypeDefinitionFormatType,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListTypesRequestTypeDef = TypedDict(
    "ListTypesRequestTypeDef",
    {
        "apiId": str,
        "format": TypeDefinitionFormatType,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

class PipelineConfigOutputTypeDef(TypedDict):
    functions: NotRequired[List[str]]

class PipelineConfigTypeDef(TypedDict):
    functions: NotRequired[Sequence[str]]

class PutGraphqlApiEnvironmentVariablesRequestTypeDef(TypedDict):
    apiId: str
    environmentVariables: Mapping[str, str]

class RdsDataApiConfigTypeDef(TypedDict):
    resourceArn: str
    secretArn: str
    databaseName: str

class RdsHttpEndpointConfigTypeDef(TypedDict):
    awsRegion: NotRequired[str]
    dbClusterIdentifier: NotRequired[str]
    databaseName: NotRequired[str]
    schema: NotRequired[str]
    awsSecretStoreArn: NotRequired[str]

class StartSchemaMergeRequestTypeDef(TypedDict):
    associationId: str
    mergedApiIdentifier: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

UpdateApiCacheRequestTypeDef = TypedDict(
    "UpdateApiCacheRequestTypeDef",
    {
        "apiId": str,
        "ttl": int,
        "apiCachingBehavior": ApiCachingBehaviorType,
        "type": ApiCacheTypeType,
        "healthMetricsConfig": NotRequired[CacheHealthMetricsConfigType],
    },
)
UpdateApiKeyRequestTypeDef = TypedDict(
    "UpdateApiKeyRequestTypeDef",
    {
        "apiId": str,
        "id": str,
        "description": NotRequired[str],
        "expires": NotRequired[int],
    },
)

class UpdateDomainNameRequestTypeDef(TypedDict):
    domainName: str
    description: NotRequired[str]

UpdateTypeRequestTypeDef = TypedDict(
    "UpdateTypeRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "format": TypeDefinitionFormatType,
        "definition": NotRequired[str],
    },
)

class AdditionalAuthenticationProviderTypeDef(TypedDict):
    authenticationType: NotRequired[AuthenticationTypeType]
    openIDConnectConfig: NotRequired[OpenIDConnectConfigTypeDef]
    userPoolConfig: NotRequired[CognitoUserPoolConfigTypeDef]
    lambdaAuthorizerConfig: NotRequired[LambdaAuthorizerConfigTypeDef]

class EvaluateCodeRequestTypeDef(TypedDict):
    runtime: AppSyncRuntimeTypeDef
    code: str
    context: str
    function: NotRequired[str]

class AssociateApiResponseTypeDef(TypedDict):
    apiAssociation: ApiAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApiCacheResponseTypeDef(TypedDict):
    apiCache: ApiCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApiKeyResponseTypeDef(TypedDict):
    apiKey: ApiKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateMergedGraphqlApiResponseTypeDef(TypedDict):
    sourceApiAssociationStatus: SourceApiAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateSourceGraphqlApiResponseTypeDef(TypedDict):
    sourceApiAssociationStatus: SourceApiAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetApiAssociationResponseTypeDef(TypedDict):
    apiAssociation: ApiAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetApiCacheResponseTypeDef(TypedDict):
    apiCache: ApiCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGraphqlApiEnvironmentVariablesResponseTypeDef(TypedDict):
    environmentVariables: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetIntrospectionSchemaResponseTypeDef(TypedDict):
    schema: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaCreationStatusResponseTypeDef(TypedDict):
    status: SchemaStatusType
    details: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApiKeysResponseTypeDef(TypedDict):
    apiKeys: List[ApiKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutGraphqlApiEnvironmentVariablesResponseTypeDef(TypedDict):
    environmentVariables: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartDataSourceIntrospectionResponseTypeDef(TypedDict):
    introspectionId: str
    introspectionStatus: DataSourceIntrospectionStatusType
    introspectionStatusDetail: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSchemaCreationResponseTypeDef(TypedDict):
    status: SchemaStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartSchemaMergeResponseTypeDef(TypedDict):
    sourceApiAssociationStatus: SourceApiAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApiCacheResponseTypeDef(TypedDict):
    apiCache: ApiCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApiKeyResponseTypeDef(TypedDict):
    apiKey: ApiKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateMergedGraphqlApiRequestTypeDef(TypedDict):
    sourceApiIdentifier: str
    mergedApiIdentifier: str
    description: NotRequired[str]
    sourceApiAssociationConfig: NotRequired[SourceApiAssociationConfigTypeDef]

class AssociateSourceGraphqlApiRequestTypeDef(TypedDict):
    mergedApiIdentifier: str
    sourceApiIdentifier: str
    description: NotRequired[str]
    sourceApiAssociationConfig: NotRequired[SourceApiAssociationConfigTypeDef]

class SourceApiAssociationTypeDef(TypedDict):
    associationId: NotRequired[str]
    associationArn: NotRequired[str]
    sourceApiId: NotRequired[str]
    sourceApiArn: NotRequired[str]
    mergedApiArn: NotRequired[str]
    mergedApiId: NotRequired[str]
    description: NotRequired[str]
    sourceApiAssociationConfig: NotRequired[SourceApiAssociationConfigTypeDef]
    sourceApiAssociationStatus: NotRequired[SourceApiAssociationStatusType]
    sourceApiAssociationStatusDetail: NotRequired[str]
    lastSuccessfulMergeDate: NotRequired[datetime]

class UpdateSourceApiAssociationRequestTypeDef(TypedDict):
    associationId: str
    mergedApiIdentifier: str
    description: NotRequired[str]
    sourceApiAssociationConfig: NotRequired[SourceApiAssociationConfigTypeDef]

class AuthProviderTypeDef(TypedDict):
    authType: AuthenticationTypeType
    cognitoConfig: NotRequired[CognitoConfigTypeDef]
    openIDConnectConfig: NotRequired[OpenIDConnectConfigTypeDef]
    lambdaAuthorizerConfig: NotRequired[LambdaAuthorizerConfigTypeDef]

class AuthorizationConfigTypeDef(TypedDict):
    authorizationType: Literal["AWS_IAM"]
    awsIamConfig: NotRequired[AwsIamConfigTypeDef]

class StartSchemaCreationRequestTypeDef(TypedDict):
    apiId: str
    definition: BlobTypeDef

CachingConfigUnionTypeDef = Union[CachingConfigTypeDef, CachingConfigOutputTypeDef]

class CodeErrorTypeDef(TypedDict):
    errorType: NotRequired[str]
    value: NotRequired[str]
    location: NotRequired[CodeErrorLocationTypeDef]

class CreateDomainNameResponseTypeDef(TypedDict):
    domainNameConfig: DomainNameConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainNameResponseTypeDef(TypedDict):
    domainNameConfig: DomainNameConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainNamesResponseTypeDef(TypedDict):
    domainNameConfigs: List[DomainNameConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateDomainNameResponseTypeDef(TypedDict):
    domainNameConfig: DomainNameConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CreateTypeResponseTypeDef = TypedDict(
    "CreateTypeResponseTypeDef",
    {
        "type": TypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTypeResponseTypeDef = TypedDict(
    "GetTypeResponseTypeDef",
    {
        "type": TypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTypesByAssociationResponseTypeDef = TypedDict(
    "ListTypesByAssociationResponseTypeDef",
    {
        "types": List[TypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "nextToken": NotRequired[str],
    },
)
ListTypesResponseTypeDef = TypedDict(
    "ListTypesResponseTypeDef",
    {
        "types": List[TypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "nextToken": NotRequired[str],
    },
)
UpdateTypeResponseTypeDef = TypedDict(
    "UpdateTypeResponseTypeDef",
    {
        "type": TypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataSourceIntrospectionModelFieldTypeDef = TypedDict(
    "DataSourceIntrospectionModelFieldTypeDef",
    {
        "name": NotRequired[str],
        "type": NotRequired[DataSourceIntrospectionModelFieldTypeTypeDef],
        "length": NotRequired[int],
    },
)

class DynamodbDataSourceConfigTypeDef(TypedDict):
    tableName: str
    awsRegion: str
    useCallerCredentials: NotRequired[bool]
    deltaSyncConfig: NotRequired[DeltaSyncConfigTypeDef]
    versioned: NotRequired[bool]

class EvaluateMappingTemplateResponseTypeDef(TypedDict):
    evaluationResult: str
    error: ErrorDetailTypeDef
    logs: List[str]
    stash: str
    outErrors: str
    ResponseMetadata: ResponseMetadataTypeDef

class IntegrationTypeDef(TypedDict):
    dataSourceName: str
    lambdaConfig: NotRequired[LambdaConfigTypeDef]

class SyncConfigTypeDef(TypedDict):
    conflictHandler: NotRequired[ConflictHandlerTypeType]
    conflictDetection: NotRequired[ConflictDetectionTypeType]
    lambdaConflictHandlerConfig: NotRequired[LambdaConflictHandlerConfigTypeDef]

class ListApiKeysRequestPaginateTypeDef(TypedDict):
    apiId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListApisRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListChannelNamespacesRequestPaginateTypeDef(TypedDict):
    apiId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataSourcesRequestPaginateTypeDef(TypedDict):
    apiId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDomainNamesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFunctionsRequestPaginateTypeDef(TypedDict):
    apiId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGraphqlApisRequestPaginateTypeDef(TypedDict):
    apiType: NotRequired[GraphQLApiTypeType]
    owner: NotRequired[OwnershipType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResolversByFunctionRequestPaginateTypeDef(TypedDict):
    apiId: str
    functionId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResolversRequestPaginateTypeDef(TypedDict):
    apiId: str
    typeName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSourceApiAssociationsRequestPaginateTypeDef(TypedDict):
    apiId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListTypesByAssociationRequestPaginateTypeDef = TypedDict(
    "ListTypesByAssociationRequestPaginateTypeDef",
    {
        "mergedApiIdentifier": str,
        "associationId": str,
        "format": TypeDefinitionFormatType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTypesRequestPaginateTypeDef = TypedDict(
    "ListTypesRequestPaginateTypeDef",
    {
        "apiId": str,
        "format": TypeDefinitionFormatType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListSourceApiAssociationsResponseTypeDef(TypedDict):
    sourceApiAssociationSummaries: List[SourceApiAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

PipelineConfigUnionTypeDef = Union[PipelineConfigTypeDef, PipelineConfigOutputTypeDef]

class StartDataSourceIntrospectionRequestTypeDef(TypedDict):
    rdsDataApiConfig: NotRequired[RdsDataApiConfigTypeDef]

class RelationalDatabaseDataSourceConfigTypeDef(TypedDict):
    relationalDatabaseSourceType: NotRequired[Literal["RDS_HTTP_ENDPOINT"]]
    rdsHttpEndpointConfig: NotRequired[RdsHttpEndpointConfigTypeDef]

class CreateGraphqlApiRequestTypeDef(TypedDict):
    name: str
    authenticationType: AuthenticationTypeType
    logConfig: NotRequired[LogConfigTypeDef]
    userPoolConfig: NotRequired[UserPoolConfigTypeDef]
    openIDConnectConfig: NotRequired[OpenIDConnectConfigTypeDef]
    tags: NotRequired[Mapping[str, str]]
    additionalAuthenticationProviders: NotRequired[
        Sequence[AdditionalAuthenticationProviderTypeDef]
    ]
    xrayEnabled: NotRequired[bool]
    lambdaAuthorizerConfig: NotRequired[LambdaAuthorizerConfigTypeDef]
    apiType: NotRequired[GraphQLApiTypeType]
    mergedApiExecutionRoleArn: NotRequired[str]
    visibility: NotRequired[GraphQLApiVisibilityType]
    ownerContact: NotRequired[str]
    introspectionConfig: NotRequired[GraphQLApiIntrospectionConfigType]
    queryDepthLimit: NotRequired[int]
    resolverCountLimit: NotRequired[int]
    enhancedMetricsConfig: NotRequired[EnhancedMetricsConfigTypeDef]

class GraphqlApiTypeDef(TypedDict):
    name: NotRequired[str]
    apiId: NotRequired[str]
    authenticationType: NotRequired[AuthenticationTypeType]
    logConfig: NotRequired[LogConfigTypeDef]
    userPoolConfig: NotRequired[UserPoolConfigTypeDef]
    openIDConnectConfig: NotRequired[OpenIDConnectConfigTypeDef]
    arn: NotRequired[str]
    uris: NotRequired[Dict[str, str]]
    tags: NotRequired[Dict[str, str]]
    additionalAuthenticationProviders: NotRequired[List[AdditionalAuthenticationProviderTypeDef]]
    xrayEnabled: NotRequired[bool]
    wafWebAclArn: NotRequired[str]
    lambdaAuthorizerConfig: NotRequired[LambdaAuthorizerConfigTypeDef]
    dns: NotRequired[Dict[str, str]]
    visibility: NotRequired[GraphQLApiVisibilityType]
    apiType: NotRequired[GraphQLApiTypeType]
    mergedApiExecutionRoleArn: NotRequired[str]
    owner: NotRequired[str]
    ownerContact: NotRequired[str]
    introspectionConfig: NotRequired[GraphQLApiIntrospectionConfigType]
    queryDepthLimit: NotRequired[int]
    resolverCountLimit: NotRequired[int]
    enhancedMetricsConfig: NotRequired[EnhancedMetricsConfigTypeDef]

class UpdateGraphqlApiRequestTypeDef(TypedDict):
    apiId: str
    name: str
    authenticationType: AuthenticationTypeType
    logConfig: NotRequired[LogConfigTypeDef]
    userPoolConfig: NotRequired[UserPoolConfigTypeDef]
    openIDConnectConfig: NotRequired[OpenIDConnectConfigTypeDef]
    additionalAuthenticationProviders: NotRequired[
        Sequence[AdditionalAuthenticationProviderTypeDef]
    ]
    xrayEnabled: NotRequired[bool]
    lambdaAuthorizerConfig: NotRequired[LambdaAuthorizerConfigTypeDef]
    mergedApiExecutionRoleArn: NotRequired[str]
    ownerContact: NotRequired[str]
    introspectionConfig: NotRequired[GraphQLApiIntrospectionConfigType]
    queryDepthLimit: NotRequired[int]
    resolverCountLimit: NotRequired[int]
    enhancedMetricsConfig: NotRequired[EnhancedMetricsConfigTypeDef]

class AssociateMergedGraphqlApiResponseTypeDef(TypedDict):
    sourceApiAssociation: SourceApiAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateSourceGraphqlApiResponseTypeDef(TypedDict):
    sourceApiAssociation: SourceApiAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSourceApiAssociationResponseTypeDef(TypedDict):
    sourceApiAssociation: SourceApiAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSourceApiAssociationResponseTypeDef(TypedDict):
    sourceApiAssociation: SourceApiAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EventConfigOutputTypeDef(TypedDict):
    authProviders: List[AuthProviderTypeDef]
    connectionAuthModes: List[AuthModeTypeDef]
    defaultPublishAuthModes: List[AuthModeTypeDef]
    defaultSubscribeAuthModes: List[AuthModeTypeDef]
    logConfig: NotRequired[EventLogConfigTypeDef]

class EventConfigTypeDef(TypedDict):
    authProviders: Sequence[AuthProviderTypeDef]
    connectionAuthModes: Sequence[AuthModeTypeDef]
    defaultPublishAuthModes: Sequence[AuthModeTypeDef]
    defaultSubscribeAuthModes: Sequence[AuthModeTypeDef]
    logConfig: NotRequired[EventLogConfigTypeDef]

class HttpDataSourceConfigTypeDef(TypedDict):
    endpoint: NotRequired[str]
    authorizationConfig: NotRequired[AuthorizationConfigTypeDef]

class EvaluateCodeErrorDetailTypeDef(TypedDict):
    message: NotRequired[str]
    codeErrors: NotRequired[List[CodeErrorTypeDef]]

class DataSourceIntrospectionModelTypeDef(TypedDict):
    name: NotRequired[str]
    fields: NotRequired[List[DataSourceIntrospectionModelFieldTypeDef]]
    primaryKey: NotRequired[DataSourceIntrospectionModelIndexTypeDef]
    indexes: NotRequired[List[DataSourceIntrospectionModelIndexTypeDef]]
    sdl: NotRequired[str]

class HandlerConfigTypeDef(TypedDict):
    behavior: HandlerBehaviorType
    integration: IntegrationTypeDef

class CreateFunctionRequestTypeDef(TypedDict):
    apiId: str
    name: str
    dataSourceName: str
    description: NotRequired[str]
    requestMappingTemplate: NotRequired[str]
    responseMappingTemplate: NotRequired[str]
    functionVersion: NotRequired[str]
    syncConfig: NotRequired[SyncConfigTypeDef]
    maxBatchSize: NotRequired[int]
    runtime: NotRequired[AppSyncRuntimeTypeDef]
    code: NotRequired[str]

class FunctionConfigurationTypeDef(TypedDict):
    functionId: NotRequired[str]
    functionArn: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    dataSourceName: NotRequired[str]
    requestMappingTemplate: NotRequired[str]
    responseMappingTemplate: NotRequired[str]
    functionVersion: NotRequired[str]
    syncConfig: NotRequired[SyncConfigTypeDef]
    maxBatchSize: NotRequired[int]
    runtime: NotRequired[AppSyncRuntimeTypeDef]
    code: NotRequired[str]

class ResolverTypeDef(TypedDict):
    typeName: NotRequired[str]
    fieldName: NotRequired[str]
    dataSourceName: NotRequired[str]
    resolverArn: NotRequired[str]
    requestMappingTemplate: NotRequired[str]
    responseMappingTemplate: NotRequired[str]
    kind: NotRequired[ResolverKindType]
    pipelineConfig: NotRequired[PipelineConfigOutputTypeDef]
    syncConfig: NotRequired[SyncConfigTypeDef]
    cachingConfig: NotRequired[CachingConfigOutputTypeDef]
    maxBatchSize: NotRequired[int]
    runtime: NotRequired[AppSyncRuntimeTypeDef]
    code: NotRequired[str]
    metricsConfig: NotRequired[ResolverLevelMetricsConfigType]

class UpdateFunctionRequestTypeDef(TypedDict):
    apiId: str
    name: str
    functionId: str
    dataSourceName: str
    description: NotRequired[str]
    requestMappingTemplate: NotRequired[str]
    responseMappingTemplate: NotRequired[str]
    functionVersion: NotRequired[str]
    syncConfig: NotRequired[SyncConfigTypeDef]
    maxBatchSize: NotRequired[int]
    runtime: NotRequired[AppSyncRuntimeTypeDef]
    code: NotRequired[str]

class CreateResolverRequestTypeDef(TypedDict):
    apiId: str
    typeName: str
    fieldName: str
    dataSourceName: NotRequired[str]
    requestMappingTemplate: NotRequired[str]
    responseMappingTemplate: NotRequired[str]
    kind: NotRequired[ResolverKindType]
    pipelineConfig: NotRequired[PipelineConfigUnionTypeDef]
    syncConfig: NotRequired[SyncConfigTypeDef]
    cachingConfig: NotRequired[CachingConfigUnionTypeDef]
    maxBatchSize: NotRequired[int]
    runtime: NotRequired[AppSyncRuntimeTypeDef]
    code: NotRequired[str]
    metricsConfig: NotRequired[ResolverLevelMetricsConfigType]

class UpdateResolverRequestTypeDef(TypedDict):
    apiId: str
    typeName: str
    fieldName: str
    dataSourceName: NotRequired[str]
    requestMappingTemplate: NotRequired[str]
    responseMappingTemplate: NotRequired[str]
    kind: NotRequired[ResolverKindType]
    pipelineConfig: NotRequired[PipelineConfigUnionTypeDef]
    syncConfig: NotRequired[SyncConfigTypeDef]
    cachingConfig: NotRequired[CachingConfigUnionTypeDef]
    maxBatchSize: NotRequired[int]
    runtime: NotRequired[AppSyncRuntimeTypeDef]
    code: NotRequired[str]
    metricsConfig: NotRequired[ResolverLevelMetricsConfigType]

class CreateGraphqlApiResponseTypeDef(TypedDict):
    graphqlApi: GraphqlApiTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGraphqlApiResponseTypeDef(TypedDict):
    graphqlApi: GraphqlApiTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListGraphqlApisResponseTypeDef(TypedDict):
    graphqlApis: List[GraphqlApiTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateGraphqlApiResponseTypeDef(TypedDict):
    graphqlApi: GraphqlApiTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ApiTypeDef(TypedDict):
    apiId: NotRequired[str]
    name: NotRequired[str]
    ownerContact: NotRequired[str]
    tags: NotRequired[Dict[str, str]]
    dns: NotRequired[Dict[str, str]]
    apiArn: NotRequired[str]
    created: NotRequired[datetime]
    xrayEnabled: NotRequired[bool]
    wafWebAclArn: NotRequired[str]
    eventConfig: NotRequired[EventConfigOutputTypeDef]

EventConfigUnionTypeDef = Union[EventConfigTypeDef, EventConfigOutputTypeDef]
CreateDataSourceRequestTypeDef = TypedDict(
    "CreateDataSourceRequestTypeDef",
    {
        "apiId": str,
        "name": str,
        "type": DataSourceTypeType,
        "description": NotRequired[str],
        "serviceRoleArn": NotRequired[str],
        "dynamodbConfig": NotRequired[DynamodbDataSourceConfigTypeDef],
        "lambdaConfig": NotRequired[LambdaDataSourceConfigTypeDef],
        "elasticsearchConfig": NotRequired[ElasticsearchDataSourceConfigTypeDef],
        "openSearchServiceConfig": NotRequired[OpenSearchServiceDataSourceConfigTypeDef],
        "httpConfig": NotRequired[HttpDataSourceConfigTypeDef],
        "relationalDatabaseConfig": NotRequired[RelationalDatabaseDataSourceConfigTypeDef],
        "eventBridgeConfig": NotRequired[EventBridgeDataSourceConfigTypeDef],
        "metricsConfig": NotRequired[DataSourceLevelMetricsConfigType],
    },
)
DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "dataSourceArn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "type": NotRequired[DataSourceTypeType],
        "serviceRoleArn": NotRequired[str],
        "dynamodbConfig": NotRequired[DynamodbDataSourceConfigTypeDef],
        "lambdaConfig": NotRequired[LambdaDataSourceConfigTypeDef],
        "elasticsearchConfig": NotRequired[ElasticsearchDataSourceConfigTypeDef],
        "openSearchServiceConfig": NotRequired[OpenSearchServiceDataSourceConfigTypeDef],
        "httpConfig": NotRequired[HttpDataSourceConfigTypeDef],
        "relationalDatabaseConfig": NotRequired[RelationalDatabaseDataSourceConfigTypeDef],
        "eventBridgeConfig": NotRequired[EventBridgeDataSourceConfigTypeDef],
        "metricsConfig": NotRequired[DataSourceLevelMetricsConfigType],
    },
)
UpdateDataSourceRequestTypeDef = TypedDict(
    "UpdateDataSourceRequestTypeDef",
    {
        "apiId": str,
        "name": str,
        "type": DataSourceTypeType,
        "description": NotRequired[str],
        "serviceRoleArn": NotRequired[str],
        "dynamodbConfig": NotRequired[DynamodbDataSourceConfigTypeDef],
        "lambdaConfig": NotRequired[LambdaDataSourceConfigTypeDef],
        "elasticsearchConfig": NotRequired[ElasticsearchDataSourceConfigTypeDef],
        "openSearchServiceConfig": NotRequired[OpenSearchServiceDataSourceConfigTypeDef],
        "httpConfig": NotRequired[HttpDataSourceConfigTypeDef],
        "relationalDatabaseConfig": NotRequired[RelationalDatabaseDataSourceConfigTypeDef],
        "eventBridgeConfig": NotRequired[EventBridgeDataSourceConfigTypeDef],
        "metricsConfig": NotRequired[DataSourceLevelMetricsConfigType],
    },
)

class EvaluateCodeResponseTypeDef(TypedDict):
    evaluationResult: str
    error: EvaluateCodeErrorDetailTypeDef
    logs: List[str]
    stash: str
    outErrors: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataSourceIntrospectionResultTypeDef(TypedDict):
    models: NotRequired[List[DataSourceIntrospectionModelTypeDef]]
    nextToken: NotRequired[str]

class HandlerConfigsTypeDef(TypedDict):
    onPublish: NotRequired[HandlerConfigTypeDef]
    onSubscribe: NotRequired[HandlerConfigTypeDef]

class CreateFunctionResponseTypeDef(TypedDict):
    functionConfiguration: FunctionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFunctionResponseTypeDef(TypedDict):
    functionConfiguration: FunctionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFunctionsResponseTypeDef(TypedDict):
    functions: List[FunctionConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateFunctionResponseTypeDef(TypedDict):
    functionConfiguration: FunctionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResolverResponseTypeDef(TypedDict):
    resolver: ResolverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResolverResponseTypeDef(TypedDict):
    resolver: ResolverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResolversByFunctionResponseTypeDef(TypedDict):
    resolvers: List[ResolverTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListResolversResponseTypeDef(TypedDict):
    resolvers: List[ResolverTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateResolverResponseTypeDef(TypedDict):
    resolver: ResolverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApiResponseTypeDef(TypedDict):
    api: ApiTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetApiResponseTypeDef(TypedDict):
    api: ApiTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListApisResponseTypeDef(TypedDict):
    apis: List[ApiTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateApiResponseTypeDef(TypedDict):
    api: ApiTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApiRequestTypeDef(TypedDict):
    name: str
    ownerContact: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    eventConfig: NotRequired[EventConfigUnionTypeDef]

class UpdateApiRequestTypeDef(TypedDict):
    apiId: str
    name: str
    ownerContact: NotRequired[str]
    eventConfig: NotRequired[EventConfigUnionTypeDef]

class CreateDataSourceResponseTypeDef(TypedDict):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataSourceResponseTypeDef(TypedDict):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataSourcesResponseTypeDef(TypedDict):
    dataSources: List[DataSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateDataSourceResponseTypeDef(TypedDict):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataSourceIntrospectionResponseTypeDef(TypedDict):
    introspectionId: str
    introspectionStatus: DataSourceIntrospectionStatusType
    introspectionStatusDetail: str
    introspectionResult: DataSourceIntrospectionResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ChannelNamespaceTypeDef(TypedDict):
    apiId: NotRequired[str]
    name: NotRequired[str]
    subscribeAuthModes: NotRequired[List[AuthModeTypeDef]]
    publishAuthModes: NotRequired[List[AuthModeTypeDef]]
    codeHandlers: NotRequired[str]
    tags: NotRequired[Dict[str, str]]
    channelNamespaceArn: NotRequired[str]
    created: NotRequired[datetime]
    lastModified: NotRequired[datetime]
    handlerConfigs: NotRequired[HandlerConfigsTypeDef]

class CreateChannelNamespaceRequestTypeDef(TypedDict):
    apiId: str
    name: str
    subscribeAuthModes: NotRequired[Sequence[AuthModeTypeDef]]
    publishAuthModes: NotRequired[Sequence[AuthModeTypeDef]]
    codeHandlers: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    handlerConfigs: NotRequired[HandlerConfigsTypeDef]

class UpdateChannelNamespaceRequestTypeDef(TypedDict):
    apiId: str
    name: str
    subscribeAuthModes: NotRequired[Sequence[AuthModeTypeDef]]
    publishAuthModes: NotRequired[Sequence[AuthModeTypeDef]]
    codeHandlers: NotRequired[str]
    handlerConfigs: NotRequired[HandlerConfigsTypeDef]

class CreateChannelNamespaceResponseTypeDef(TypedDict):
    channelNamespace: ChannelNamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelNamespaceResponseTypeDef(TypedDict):
    channelNamespace: ChannelNamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelNamespacesResponseTypeDef(TypedDict):
    channelNamespaces: List[ChannelNamespaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateChannelNamespaceResponseTypeDef(TypedDict):
    channelNamespace: ChannelNamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
