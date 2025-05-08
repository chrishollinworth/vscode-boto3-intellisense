"""
Type annotations for apigateway service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_apigateway.type_defs import AccessLogSettingsTypeDef

    data: AccessLogSettingsTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    ApiKeySourceTypeType,
    AuthorizerTypeType,
    CacheClusterSizeType,
    CacheClusterStatusType,
    ConnectionTypeType,
    ContentHandlingStrategyType,
    DocumentationPartTypeType,
    DomainNameStatusType,
    EndpointTypeType,
    GatewayResponseTypeType,
    IntegrationTypeType,
    IpAddressTypeType,
    LocationStatusTypeType,
    OpType,
    PutModeType,
    QuotaPeriodTypeType,
    ResourceOwnerType,
    SecurityPolicyType,
    UnauthorizedCacheControlHeaderStrategyType,
    VpcLinkStatusType,
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
    "AccessLogSettingsTypeDef",
    "AccountTypeDef",
    "ApiKeyIdsTypeDef",
    "ApiKeyResponseTypeDef",
    "ApiKeyTypeDef",
    "ApiKeysTypeDef",
    "ApiStageOutputTypeDef",
    "ApiStageTypeDef",
    "ApiStageUnionTypeDef",
    "AuthorizerResponseTypeDef",
    "AuthorizerTypeDef",
    "AuthorizersTypeDef",
    "BasePathMappingResponseTypeDef",
    "BasePathMappingTypeDef",
    "BasePathMappingsTypeDef",
    "BlobTypeDef",
    "CanarySettingsOutputTypeDef",
    "CanarySettingsTypeDef",
    "CanarySettingsUnionTypeDef",
    "ClientCertificateResponseTypeDef",
    "ClientCertificateTypeDef",
    "ClientCertificatesTypeDef",
    "CreateApiKeyRequestTypeDef",
    "CreateAuthorizerRequestTypeDef",
    "CreateBasePathMappingRequestTypeDef",
    "CreateDeploymentRequestTypeDef",
    "CreateDocumentationPartRequestTypeDef",
    "CreateDocumentationVersionRequestTypeDef",
    "CreateDomainNameAccessAssociationRequestTypeDef",
    "CreateDomainNameRequestTypeDef",
    "CreateModelRequestTypeDef",
    "CreateRequestValidatorRequestTypeDef",
    "CreateResourceRequestTypeDef",
    "CreateRestApiRequestTypeDef",
    "CreateStageRequestTypeDef",
    "CreateUsagePlanKeyRequestTypeDef",
    "CreateUsagePlanRequestTypeDef",
    "CreateVpcLinkRequestTypeDef",
    "DeleteApiKeyRequestTypeDef",
    "DeleteAuthorizerRequestTypeDef",
    "DeleteBasePathMappingRequestTypeDef",
    "DeleteClientCertificateRequestTypeDef",
    "DeleteDeploymentRequestTypeDef",
    "DeleteDocumentationPartRequestTypeDef",
    "DeleteDocumentationVersionRequestTypeDef",
    "DeleteDomainNameAccessAssociationRequestTypeDef",
    "DeleteDomainNameRequestTypeDef",
    "DeleteGatewayResponseRequestTypeDef",
    "DeleteIntegrationRequestTypeDef",
    "DeleteIntegrationResponseRequestTypeDef",
    "DeleteMethodRequestTypeDef",
    "DeleteMethodResponseRequestTypeDef",
    "DeleteModelRequestTypeDef",
    "DeleteRequestValidatorRequestTypeDef",
    "DeleteResourceRequestTypeDef",
    "DeleteRestApiRequestTypeDef",
    "DeleteStageRequestTypeDef",
    "DeleteUsagePlanKeyRequestTypeDef",
    "DeleteUsagePlanRequestTypeDef",
    "DeleteVpcLinkRequestTypeDef",
    "DeploymentCanarySettingsTypeDef",
    "DeploymentResponseTypeDef",
    "DeploymentTypeDef",
    "DeploymentsTypeDef",
    "DocumentationPartIdsTypeDef",
    "DocumentationPartLocationTypeDef",
    "DocumentationPartResponseTypeDef",
    "DocumentationPartTypeDef",
    "DocumentationPartsTypeDef",
    "DocumentationVersionResponseTypeDef",
    "DocumentationVersionTypeDef",
    "DocumentationVersionsTypeDef",
    "DomainNameAccessAssociationResponseTypeDef",
    "DomainNameAccessAssociationTypeDef",
    "DomainNameAccessAssociationsTypeDef",
    "DomainNameResponseTypeDef",
    "DomainNameTypeDef",
    "DomainNamesTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EndpointConfigurationOutputTypeDef",
    "EndpointConfigurationTypeDef",
    "EndpointConfigurationUnionTypeDef",
    "ExportResponseTypeDef",
    "FlushStageAuthorizersCacheRequestTypeDef",
    "FlushStageCacheRequestTypeDef",
    "GatewayResponseResponseTypeDef",
    "GatewayResponseTypeDef",
    "GatewayResponsesTypeDef",
    "GenerateClientCertificateRequestTypeDef",
    "GetApiKeyRequestTypeDef",
    "GetApiKeysRequestPaginateTypeDef",
    "GetApiKeysRequestTypeDef",
    "GetAuthorizerRequestTypeDef",
    "GetAuthorizersRequestPaginateTypeDef",
    "GetAuthorizersRequestTypeDef",
    "GetBasePathMappingRequestTypeDef",
    "GetBasePathMappingsRequestPaginateTypeDef",
    "GetBasePathMappingsRequestTypeDef",
    "GetClientCertificateRequestTypeDef",
    "GetClientCertificatesRequestPaginateTypeDef",
    "GetClientCertificatesRequestTypeDef",
    "GetDeploymentRequestTypeDef",
    "GetDeploymentsRequestPaginateTypeDef",
    "GetDeploymentsRequestTypeDef",
    "GetDocumentationPartRequestTypeDef",
    "GetDocumentationPartsRequestPaginateTypeDef",
    "GetDocumentationPartsRequestTypeDef",
    "GetDocumentationVersionRequestTypeDef",
    "GetDocumentationVersionsRequestPaginateTypeDef",
    "GetDocumentationVersionsRequestTypeDef",
    "GetDomainNameAccessAssociationsRequestTypeDef",
    "GetDomainNameRequestTypeDef",
    "GetDomainNamesRequestPaginateTypeDef",
    "GetDomainNamesRequestTypeDef",
    "GetExportRequestTypeDef",
    "GetGatewayResponseRequestTypeDef",
    "GetGatewayResponsesRequestPaginateTypeDef",
    "GetGatewayResponsesRequestTypeDef",
    "GetIntegrationRequestTypeDef",
    "GetIntegrationResponseRequestTypeDef",
    "GetMethodRequestTypeDef",
    "GetMethodResponseRequestTypeDef",
    "GetModelRequestTypeDef",
    "GetModelTemplateRequestTypeDef",
    "GetModelsRequestPaginateTypeDef",
    "GetModelsRequestTypeDef",
    "GetRequestValidatorRequestTypeDef",
    "GetRequestValidatorsRequestPaginateTypeDef",
    "GetRequestValidatorsRequestTypeDef",
    "GetResourceRequestTypeDef",
    "GetResourcesRequestPaginateTypeDef",
    "GetResourcesRequestTypeDef",
    "GetRestApiRequestTypeDef",
    "GetRestApisRequestPaginateTypeDef",
    "GetRestApisRequestTypeDef",
    "GetSdkRequestTypeDef",
    "GetSdkTypeRequestTypeDef",
    "GetSdkTypesRequestPaginateTypeDef",
    "GetSdkTypesRequestTypeDef",
    "GetStageRequestTypeDef",
    "GetStagesRequestTypeDef",
    "GetTagsRequestTypeDef",
    "GetUsagePlanKeyRequestTypeDef",
    "GetUsagePlanKeysRequestPaginateTypeDef",
    "GetUsagePlanKeysRequestTypeDef",
    "GetUsagePlanRequestTypeDef",
    "GetUsagePlansRequestPaginateTypeDef",
    "GetUsagePlansRequestTypeDef",
    "GetUsageRequestPaginateTypeDef",
    "GetUsageRequestTypeDef",
    "GetVpcLinkRequestTypeDef",
    "GetVpcLinksRequestPaginateTypeDef",
    "GetVpcLinksRequestTypeDef",
    "ImportApiKeysRequestTypeDef",
    "ImportDocumentationPartsRequestTypeDef",
    "ImportRestApiRequestTypeDef",
    "IntegrationResponseExtraTypeDef",
    "IntegrationResponseResponseTypeDef",
    "IntegrationResponseTypeDef",
    "IntegrationTypeDef",
    "MethodResponseExtraTypeDef",
    "MethodResponseResponseTypeDef",
    "MethodResponseTypeDef",
    "MethodSettingTypeDef",
    "MethodSnapshotTypeDef",
    "MethodTypeDef",
    "ModelResponseTypeDef",
    "ModelTypeDef",
    "ModelsTypeDef",
    "MutualTlsAuthenticationInputTypeDef",
    "MutualTlsAuthenticationTypeDef",
    "PaginatorConfigTypeDef",
    "PatchOperationTypeDef",
    "PutGatewayResponseRequestTypeDef",
    "PutIntegrationRequestTypeDef",
    "PutIntegrationResponseRequestTypeDef",
    "PutMethodRequestTypeDef",
    "PutMethodResponseRequestTypeDef",
    "PutRestApiRequestTypeDef",
    "QuotaSettingsTypeDef",
    "RejectDomainNameAccessAssociationRequestTypeDef",
    "RequestValidatorResponseTypeDef",
    "RequestValidatorTypeDef",
    "RequestValidatorsTypeDef",
    "ResourceResponseTypeDef",
    "ResourceTypeDef",
    "ResourcesTypeDef",
    "ResponseMetadataTypeDef",
    "RestApiResponseTypeDef",
    "RestApiTypeDef",
    "RestApisTypeDef",
    "SdkConfigurationPropertyTypeDef",
    "SdkResponseTypeDef",
    "SdkTypeResponseTypeDef",
    "SdkTypeTypeDef",
    "SdkTypesTypeDef",
    "StageKeyTypeDef",
    "StageResponseTypeDef",
    "StageTypeDef",
    "StagesTypeDef",
    "TagResourceRequestTypeDef",
    "TagsTypeDef",
    "TemplateTypeDef",
    "TestInvokeAuthorizerRequestTypeDef",
    "TestInvokeAuthorizerResponseTypeDef",
    "TestInvokeMethodRequestTypeDef",
    "TestInvokeMethodResponseTypeDef",
    "ThrottleSettingsTypeDef",
    "TlsConfigTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAccountRequestTypeDef",
    "UpdateApiKeyRequestTypeDef",
    "UpdateAuthorizerRequestTypeDef",
    "UpdateBasePathMappingRequestTypeDef",
    "UpdateClientCertificateRequestTypeDef",
    "UpdateDeploymentRequestTypeDef",
    "UpdateDocumentationPartRequestTypeDef",
    "UpdateDocumentationVersionRequestTypeDef",
    "UpdateDomainNameRequestTypeDef",
    "UpdateGatewayResponseRequestTypeDef",
    "UpdateIntegrationRequestTypeDef",
    "UpdateIntegrationResponseRequestTypeDef",
    "UpdateMethodRequestTypeDef",
    "UpdateMethodResponseRequestTypeDef",
    "UpdateModelRequestTypeDef",
    "UpdateRequestValidatorRequestTypeDef",
    "UpdateResourceRequestTypeDef",
    "UpdateRestApiRequestTypeDef",
    "UpdateStageRequestTypeDef",
    "UpdateUsagePlanRequestTypeDef",
    "UpdateUsageRequestTypeDef",
    "UpdateVpcLinkRequestTypeDef",
    "UsagePlanKeyResponseTypeDef",
    "UsagePlanKeyTypeDef",
    "UsagePlanKeysTypeDef",
    "UsagePlanResponseTypeDef",
    "UsagePlanTypeDef",
    "UsagePlansTypeDef",
    "UsageTypeDef",
    "VpcLinkResponseTypeDef",
    "VpcLinkTypeDef",
    "VpcLinksTypeDef",
)

AccessLogSettingsTypeDef = TypedDict(
    "AccessLogSettingsTypeDef",
    {
        "format": NotRequired[str],
        "destinationArn": NotRequired[str],
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ThrottleSettingsTypeDef(TypedDict):
    burstLimit: NotRequired[int]
    rateLimit: NotRequired[float]

ApiKeyTypeDef = TypedDict(
    "ApiKeyTypeDef",
    {
        "id": NotRequired[str],
        "value": NotRequired[str],
        "name": NotRequired[str],
        "customerId": NotRequired[str],
        "description": NotRequired[str],
        "enabled": NotRequired[bool],
        "createdDate": NotRequired[datetime],
        "lastUpdatedDate": NotRequired[datetime],
        "stageKeys": NotRequired[List[str]],
        "tags": NotRequired[Dict[str, str]],
    },
)
AuthorizerTypeDef = TypedDict(
    "AuthorizerTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[AuthorizerTypeType],
        "providerARNs": NotRequired[List[str]],
        "authType": NotRequired[str],
        "authorizerUri": NotRequired[str],
        "authorizerCredentials": NotRequired[str],
        "identitySource": NotRequired[str],
        "identityValidationExpression": NotRequired[str],
        "authorizerResultTtlInSeconds": NotRequired[int],
    },
)

class BasePathMappingTypeDef(TypedDict):
    basePath: NotRequired[str]
    restApiId: NotRequired[str]
    stage: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CanarySettingsOutputTypeDef(TypedDict):
    percentTraffic: NotRequired[float]
    deploymentId: NotRequired[str]
    stageVariableOverrides: NotRequired[Dict[str, str]]
    useStageCache: NotRequired[bool]

class CanarySettingsTypeDef(TypedDict):
    percentTraffic: NotRequired[float]
    deploymentId: NotRequired[str]
    stageVariableOverrides: NotRequired[Mapping[str, str]]
    useStageCache: NotRequired[bool]

class ClientCertificateTypeDef(TypedDict):
    clientCertificateId: NotRequired[str]
    description: NotRequired[str]
    pemEncodedCertificate: NotRequired[str]
    createdDate: NotRequired[datetime]
    expirationDate: NotRequired[datetime]
    tags: NotRequired[Dict[str, str]]

class StageKeyTypeDef(TypedDict):
    restApiId: NotRequired[str]
    stageName: NotRequired[str]

CreateAuthorizerRequestTypeDef = TypedDict(
    "CreateAuthorizerRequestTypeDef",
    {
        "restApiId": str,
        "name": str,
        "type": AuthorizerTypeType,
        "providerARNs": NotRequired[Sequence[str]],
        "authType": NotRequired[str],
        "authorizerUri": NotRequired[str],
        "authorizerCredentials": NotRequired[str],
        "identitySource": NotRequired[str],
        "identityValidationExpression": NotRequired[str],
        "authorizerResultTtlInSeconds": NotRequired[int],
    },
)

class CreateBasePathMappingRequestTypeDef(TypedDict):
    domainName: str
    restApiId: str
    domainNameId: NotRequired[str]
    basePath: NotRequired[str]
    stage: NotRequired[str]

class DeploymentCanarySettingsTypeDef(TypedDict):
    percentTraffic: NotRequired[float]
    stageVariableOverrides: NotRequired[Mapping[str, str]]
    useStageCache: NotRequired[bool]

DocumentationPartLocationTypeDef = TypedDict(
    "DocumentationPartLocationTypeDef",
    {
        "type": DocumentationPartTypeType,
        "path": NotRequired[str],
        "method": NotRequired[str],
        "statusCode": NotRequired[str],
        "name": NotRequired[str],
    },
)

class CreateDocumentationVersionRequestTypeDef(TypedDict):
    restApiId: str
    documentationVersion: str
    stageName: NotRequired[str]
    description: NotRequired[str]

class CreateDomainNameAccessAssociationRequestTypeDef(TypedDict):
    domainNameArn: str
    accessAssociationSourceType: Literal["VPCE"]
    accessAssociationSource: str
    tags: NotRequired[Mapping[str, str]]

class MutualTlsAuthenticationInputTypeDef(TypedDict):
    truststoreUri: NotRequired[str]
    truststoreVersion: NotRequired[str]

class CreateModelRequestTypeDef(TypedDict):
    restApiId: str
    name: str
    contentType: str
    description: NotRequired[str]
    schema: NotRequired[str]

class CreateRequestValidatorRequestTypeDef(TypedDict):
    restApiId: str
    name: NotRequired[str]
    validateRequestBody: NotRequired[bool]
    validateRequestParameters: NotRequired[bool]

class CreateResourceRequestTypeDef(TypedDict):
    restApiId: str
    parentId: str
    pathPart: str

class CreateUsagePlanKeyRequestTypeDef(TypedDict):
    usagePlanId: str
    keyId: str
    keyType: str

class QuotaSettingsTypeDef(TypedDict):
    limit: NotRequired[int]
    offset: NotRequired[int]
    period: NotRequired[QuotaPeriodTypeType]

class CreateVpcLinkRequestTypeDef(TypedDict):
    name: str
    targetArns: Sequence[str]
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class DeleteApiKeyRequestTypeDef(TypedDict):
    apiKey: str

class DeleteAuthorizerRequestTypeDef(TypedDict):
    restApiId: str
    authorizerId: str

class DeleteBasePathMappingRequestTypeDef(TypedDict):
    domainName: str
    basePath: str
    domainNameId: NotRequired[str]

class DeleteClientCertificateRequestTypeDef(TypedDict):
    clientCertificateId: str

class DeleteDeploymentRequestTypeDef(TypedDict):
    restApiId: str
    deploymentId: str

class DeleteDocumentationPartRequestTypeDef(TypedDict):
    restApiId: str
    documentationPartId: str

class DeleteDocumentationVersionRequestTypeDef(TypedDict):
    restApiId: str
    documentationVersion: str

class DeleteDomainNameAccessAssociationRequestTypeDef(TypedDict):
    domainNameAccessAssociationArn: str

class DeleteDomainNameRequestTypeDef(TypedDict):
    domainName: str
    domainNameId: NotRequired[str]

class DeleteGatewayResponseRequestTypeDef(TypedDict):
    restApiId: str
    responseType: GatewayResponseTypeType

class DeleteIntegrationRequestTypeDef(TypedDict):
    restApiId: str
    resourceId: str
    httpMethod: str

class DeleteIntegrationResponseRequestTypeDef(TypedDict):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str

class DeleteMethodRequestTypeDef(TypedDict):
    restApiId: str
    resourceId: str
    httpMethod: str

class DeleteMethodResponseRequestTypeDef(TypedDict):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str

class DeleteModelRequestTypeDef(TypedDict):
    restApiId: str
    modelName: str

class DeleteRequestValidatorRequestTypeDef(TypedDict):
    restApiId: str
    requestValidatorId: str

class DeleteResourceRequestTypeDef(TypedDict):
    restApiId: str
    resourceId: str

class DeleteRestApiRequestTypeDef(TypedDict):
    restApiId: str

class DeleteStageRequestTypeDef(TypedDict):
    restApiId: str
    stageName: str

class DeleteUsagePlanKeyRequestTypeDef(TypedDict):
    usagePlanId: str
    keyId: str

class DeleteUsagePlanRequestTypeDef(TypedDict):
    usagePlanId: str

class DeleteVpcLinkRequestTypeDef(TypedDict):
    vpcLinkId: str

class MethodSnapshotTypeDef(TypedDict):
    authorizationType: NotRequired[str]
    apiKeyRequired: NotRequired[bool]

class DocumentationVersionTypeDef(TypedDict):
    version: NotRequired[str]
    createdDate: NotRequired[datetime]
    description: NotRequired[str]

class DomainNameAccessAssociationTypeDef(TypedDict):
    domainNameAccessAssociationArn: NotRequired[str]
    domainNameArn: NotRequired[str]
    accessAssociationSourceType: NotRequired[Literal["VPCE"]]
    accessAssociationSource: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

EndpointConfigurationOutputTypeDef = TypedDict(
    "EndpointConfigurationOutputTypeDef",
    {
        "types": NotRequired[List[EndpointTypeType]],
        "ipAddressType": NotRequired[IpAddressTypeType],
        "vpcEndpointIds": NotRequired[List[str]],
    },
)

class MutualTlsAuthenticationTypeDef(TypedDict):
    truststoreUri: NotRequired[str]
    truststoreVersion: NotRequired[str]
    truststoreWarnings: NotRequired[List[str]]

EndpointConfigurationTypeDef = TypedDict(
    "EndpointConfigurationTypeDef",
    {
        "types": NotRequired[Sequence[EndpointTypeType]],
        "ipAddressType": NotRequired[IpAddressTypeType],
        "vpcEndpointIds": NotRequired[Sequence[str]],
    },
)

class FlushStageAuthorizersCacheRequestTypeDef(TypedDict):
    restApiId: str
    stageName: str

class FlushStageCacheRequestTypeDef(TypedDict):
    restApiId: str
    stageName: str

class GatewayResponseTypeDef(TypedDict):
    responseType: NotRequired[GatewayResponseTypeType]
    statusCode: NotRequired[str]
    responseParameters: NotRequired[Dict[str, str]]
    responseTemplates: NotRequired[Dict[str, str]]
    defaultResponse: NotRequired[bool]

class GenerateClientCertificateRequestTypeDef(TypedDict):
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class GetApiKeyRequestTypeDef(TypedDict):
    apiKey: str
    includeValue: NotRequired[bool]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetApiKeysRequestTypeDef(TypedDict):
    position: NotRequired[str]
    limit: NotRequired[int]
    nameQuery: NotRequired[str]
    customerId: NotRequired[str]
    includeValues: NotRequired[bool]

class GetAuthorizerRequestTypeDef(TypedDict):
    restApiId: str
    authorizerId: str

class GetAuthorizersRequestTypeDef(TypedDict):
    restApiId: str
    position: NotRequired[str]
    limit: NotRequired[int]

class GetBasePathMappingRequestTypeDef(TypedDict):
    domainName: str
    basePath: str
    domainNameId: NotRequired[str]

class GetBasePathMappingsRequestTypeDef(TypedDict):
    domainName: str
    domainNameId: NotRequired[str]
    position: NotRequired[str]
    limit: NotRequired[int]

class GetClientCertificateRequestTypeDef(TypedDict):
    clientCertificateId: str

class GetClientCertificatesRequestTypeDef(TypedDict):
    position: NotRequired[str]
    limit: NotRequired[int]

class GetDeploymentRequestTypeDef(TypedDict):
    restApiId: str
    deploymentId: str
    embed: NotRequired[Sequence[str]]

class GetDeploymentsRequestTypeDef(TypedDict):
    restApiId: str
    position: NotRequired[str]
    limit: NotRequired[int]

class GetDocumentationPartRequestTypeDef(TypedDict):
    restApiId: str
    documentationPartId: str

GetDocumentationPartsRequestTypeDef = TypedDict(
    "GetDocumentationPartsRequestTypeDef",
    {
        "restApiId": str,
        "type": NotRequired[DocumentationPartTypeType],
        "nameQuery": NotRequired[str],
        "path": NotRequired[str],
        "position": NotRequired[str],
        "limit": NotRequired[int],
        "locationStatus": NotRequired[LocationStatusTypeType],
    },
)

class GetDocumentationVersionRequestTypeDef(TypedDict):
    restApiId: str
    documentationVersion: str

class GetDocumentationVersionsRequestTypeDef(TypedDict):
    restApiId: str
    position: NotRequired[str]
    limit: NotRequired[int]

class GetDomainNameAccessAssociationsRequestTypeDef(TypedDict):
    position: NotRequired[str]
    limit: NotRequired[int]
    resourceOwner: NotRequired[ResourceOwnerType]

class GetDomainNameRequestTypeDef(TypedDict):
    domainName: str
    domainNameId: NotRequired[str]

class GetDomainNamesRequestTypeDef(TypedDict):
    position: NotRequired[str]
    limit: NotRequired[int]
    resourceOwner: NotRequired[ResourceOwnerType]

class GetExportRequestTypeDef(TypedDict):
    restApiId: str
    stageName: str
    exportType: str
    parameters: NotRequired[Mapping[str, str]]
    accepts: NotRequired[str]

class GetGatewayResponseRequestTypeDef(TypedDict):
    restApiId: str
    responseType: GatewayResponseTypeType

class GetGatewayResponsesRequestTypeDef(TypedDict):
    restApiId: str
    position: NotRequired[str]
    limit: NotRequired[int]

class GetIntegrationRequestTypeDef(TypedDict):
    restApiId: str
    resourceId: str
    httpMethod: str

class GetIntegrationResponseRequestTypeDef(TypedDict):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str

class GetMethodRequestTypeDef(TypedDict):
    restApiId: str
    resourceId: str
    httpMethod: str

class GetMethodResponseRequestTypeDef(TypedDict):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str

class GetModelRequestTypeDef(TypedDict):
    restApiId: str
    modelName: str
    flatten: NotRequired[bool]

class GetModelTemplateRequestTypeDef(TypedDict):
    restApiId: str
    modelName: str

class GetModelsRequestTypeDef(TypedDict):
    restApiId: str
    position: NotRequired[str]
    limit: NotRequired[int]

class GetRequestValidatorRequestTypeDef(TypedDict):
    restApiId: str
    requestValidatorId: str

class GetRequestValidatorsRequestTypeDef(TypedDict):
    restApiId: str
    position: NotRequired[str]
    limit: NotRequired[int]

class GetResourceRequestTypeDef(TypedDict):
    restApiId: str
    resourceId: str
    embed: NotRequired[Sequence[str]]

class GetResourcesRequestTypeDef(TypedDict):
    restApiId: str
    position: NotRequired[str]
    limit: NotRequired[int]
    embed: NotRequired[Sequence[str]]

class GetRestApiRequestTypeDef(TypedDict):
    restApiId: str

class GetRestApisRequestTypeDef(TypedDict):
    position: NotRequired[str]
    limit: NotRequired[int]

class GetSdkRequestTypeDef(TypedDict):
    restApiId: str
    stageName: str
    sdkType: str
    parameters: NotRequired[Mapping[str, str]]

GetSdkTypeRequestTypeDef = TypedDict(
    "GetSdkTypeRequestTypeDef",
    {
        "id": str,
    },
)

class GetSdkTypesRequestTypeDef(TypedDict):
    position: NotRequired[str]
    limit: NotRequired[int]

class GetStageRequestTypeDef(TypedDict):
    restApiId: str
    stageName: str

class GetStagesRequestTypeDef(TypedDict):
    restApiId: str
    deploymentId: NotRequired[str]

class GetTagsRequestTypeDef(TypedDict):
    resourceArn: str
    position: NotRequired[str]
    limit: NotRequired[int]

class GetUsagePlanKeyRequestTypeDef(TypedDict):
    usagePlanId: str
    keyId: str

class GetUsagePlanKeysRequestTypeDef(TypedDict):
    usagePlanId: str
    position: NotRequired[str]
    limit: NotRequired[int]
    nameQuery: NotRequired[str]

class GetUsagePlanRequestTypeDef(TypedDict):
    usagePlanId: str

class GetUsagePlansRequestTypeDef(TypedDict):
    position: NotRequired[str]
    keyId: NotRequired[str]
    limit: NotRequired[int]

class GetUsageRequestTypeDef(TypedDict):
    usagePlanId: str
    startDate: str
    endDate: str
    keyId: NotRequired[str]
    position: NotRequired[str]
    limit: NotRequired[int]

class GetVpcLinkRequestTypeDef(TypedDict):
    vpcLinkId: str

class GetVpcLinksRequestTypeDef(TypedDict):
    position: NotRequired[str]
    limit: NotRequired[int]

class IntegrationResponseTypeDef(TypedDict):
    statusCode: NotRequired[str]
    selectionPattern: NotRequired[str]
    responseParameters: NotRequired[Dict[str, str]]
    responseTemplates: NotRequired[Dict[str, str]]
    contentHandling: NotRequired[ContentHandlingStrategyType]

class TlsConfigTypeDef(TypedDict):
    insecureSkipVerification: NotRequired[bool]

class MethodResponseTypeDef(TypedDict):
    statusCode: NotRequired[str]
    responseParameters: NotRequired[Dict[str, bool]]
    responseModels: NotRequired[Dict[str, str]]

class MethodSettingTypeDef(TypedDict):
    metricsEnabled: NotRequired[bool]
    loggingLevel: NotRequired[str]
    dataTraceEnabled: NotRequired[bool]
    throttlingBurstLimit: NotRequired[int]
    throttlingRateLimit: NotRequired[float]
    cachingEnabled: NotRequired[bool]
    cacheTtlInSeconds: NotRequired[int]
    cacheDataEncrypted: NotRequired[bool]
    requireAuthorizationForCacheControl: NotRequired[bool]
    unauthorizedCacheControlHeaderStrategy: NotRequired[UnauthorizedCacheControlHeaderStrategyType]

ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "schema": NotRequired[str],
        "contentType": NotRequired[str],
    },
)
PatchOperationTypeDef = TypedDict(
    "PatchOperationTypeDef",
    {
        "op": NotRequired[OpType],
        "path": NotRequired[str],
        "value": NotRequired[str],
        "from": NotRequired[str],
    },
)

class PutGatewayResponseRequestTypeDef(TypedDict):
    restApiId: str
    responseType: GatewayResponseTypeType
    statusCode: NotRequired[str]
    responseParameters: NotRequired[Mapping[str, str]]
    responseTemplates: NotRequired[Mapping[str, str]]

class PutIntegrationResponseRequestTypeDef(TypedDict):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str
    selectionPattern: NotRequired[str]
    responseParameters: NotRequired[Mapping[str, str]]
    responseTemplates: NotRequired[Mapping[str, str]]
    contentHandling: NotRequired[ContentHandlingStrategyType]

class PutMethodRequestTypeDef(TypedDict):
    restApiId: str
    resourceId: str
    httpMethod: str
    authorizationType: str
    authorizerId: NotRequired[str]
    apiKeyRequired: NotRequired[bool]
    operationName: NotRequired[str]
    requestParameters: NotRequired[Mapping[str, bool]]
    requestModels: NotRequired[Mapping[str, str]]
    requestValidatorId: NotRequired[str]
    authorizationScopes: NotRequired[Sequence[str]]

class PutMethodResponseRequestTypeDef(TypedDict):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str
    responseParameters: NotRequired[Mapping[str, bool]]
    responseModels: NotRequired[Mapping[str, str]]

class RejectDomainNameAccessAssociationRequestTypeDef(TypedDict):
    domainNameAccessAssociationArn: str
    domainNameArn: str

RequestValidatorTypeDef = TypedDict(
    "RequestValidatorTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "validateRequestBody": NotRequired[bool],
        "validateRequestParameters": NotRequired[bool],
    },
)

class SdkConfigurationPropertyTypeDef(TypedDict):
    name: NotRequired[str]
    friendlyName: NotRequired[str]
    description: NotRequired[str]
    required: NotRequired[bool]
    defaultValue: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class TestInvokeAuthorizerRequestTypeDef(TypedDict):
    restApiId: str
    authorizerId: str
    headers: NotRequired[Mapping[str, str]]
    multiValueHeaders: NotRequired[Mapping[str, Sequence[str]]]
    pathWithQueryString: NotRequired[str]
    body: NotRequired[str]
    stageVariables: NotRequired[Mapping[str, str]]
    additionalContext: NotRequired[Mapping[str, str]]

class TestInvokeMethodRequestTypeDef(TypedDict):
    restApiId: str
    resourceId: str
    httpMethod: str
    pathWithQueryString: NotRequired[str]
    body: NotRequired[str]
    headers: NotRequired[Mapping[str, str]]
    multiValueHeaders: NotRequired[Mapping[str, Sequence[str]]]
    clientCertificateId: NotRequired[str]
    stageVariables: NotRequired[Mapping[str, str]]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

UsagePlanKeyTypeDef = TypedDict(
    "UsagePlanKeyTypeDef",
    {
        "id": NotRequired[str],
        "type": NotRequired[str],
        "value": NotRequired[str],
        "name": NotRequired[str],
    },
)
VpcLinkTypeDef = TypedDict(
    "VpcLinkTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "targetArns": NotRequired[List[str]],
        "status": NotRequired[VpcLinkStatusType],
        "statusMessage": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

class ApiKeyIdsTypeDef(TypedDict):
    ids: List[str]
    warnings: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

ApiKeyResponseTypeDef = TypedDict(
    "ApiKeyResponseTypeDef",
    {
        "id": str,
        "value": str,
        "name": str,
        "customerId": str,
        "description": str,
        "enabled": bool,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "stageKeys": List[str],
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AuthorizerResponseTypeDef = TypedDict(
    "AuthorizerResponseTypeDef",
    {
        "id": str,
        "name": str,
        "type": AuthorizerTypeType,
        "providerARNs": List[str],
        "authType": str,
        "authorizerUri": str,
        "authorizerCredentials": str,
        "identitySource": str,
        "identityValidationExpression": str,
        "authorizerResultTtlInSeconds": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class BasePathMappingResponseTypeDef(TypedDict):
    basePath: str
    restApiId: str
    stage: str
    ResponseMetadata: ResponseMetadataTypeDef

class ClientCertificateResponseTypeDef(TypedDict):
    clientCertificateId: str
    description: str
    pemEncodedCertificate: str
    createdDate: datetime
    expirationDate: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentationPartIdsTypeDef(TypedDict):
    ids: List[str]
    warnings: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentationVersionResponseTypeDef(TypedDict):
    version: str
    createdDate: datetime
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class DomainNameAccessAssociationResponseTypeDef(TypedDict):
    domainNameAccessAssociationArn: str
    domainNameArn: str
    accessAssociationSourceType: Literal["VPCE"]
    accessAssociationSource: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ExportResponseTypeDef(TypedDict):
    contentType: str
    contentDisposition: str
    body: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GatewayResponseResponseTypeDef(TypedDict):
    responseType: GatewayResponseTypeType
    statusCode: str
    responseParameters: Dict[str, str]
    responseTemplates: Dict[str, str]
    defaultResponse: bool
    ResponseMetadata: ResponseMetadataTypeDef

class IntegrationResponseResponseTypeDef(TypedDict):
    statusCode: str
    selectionPattern: str
    responseParameters: Dict[str, str]
    responseTemplates: Dict[str, str]
    contentHandling: ContentHandlingStrategyType
    ResponseMetadata: ResponseMetadataTypeDef

class MethodResponseResponseTypeDef(TypedDict):
    statusCode: str
    responseParameters: Dict[str, bool]
    responseModels: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

ModelResponseTypeDef = TypedDict(
    "ModelResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "schema": str,
        "contentType": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RequestValidatorResponseTypeDef = TypedDict(
    "RequestValidatorResponseTypeDef",
    {
        "id": str,
        "name": str,
        "validateRequestBody": bool,
        "validateRequestParameters": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class SdkResponseTypeDef(TypedDict):
    contentType: str
    contentDisposition: str
    body: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class TagsTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class TemplateTypeDef(TypedDict):
    value: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestInvokeAuthorizerResponseTypeDef(TypedDict):
    clientStatus: int
    log: str
    latency: int
    principalId: str
    policy: str
    authorization: Dict[str, List[str]]
    claims: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class TestInvokeMethodResponseTypeDef(TypedDict):
    status: int
    body: str
    headers: Dict[str, str]
    multiValueHeaders: Dict[str, List[str]]
    log: str
    latency: int
    ResponseMetadata: ResponseMetadataTypeDef

UsagePlanKeyResponseTypeDef = TypedDict(
    "UsagePlanKeyResponseTypeDef",
    {
        "id": str,
        "type": str,
        "value": str,
        "name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class UsageTypeDef(TypedDict):
    usagePlanId: str
    startDate: str
    endDate: str
    position: str
    items: Dict[str, List[List[int]]]
    ResponseMetadata: ResponseMetadataTypeDef

VpcLinkResponseTypeDef = TypedDict(
    "VpcLinkResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "targetArns": List[str],
        "status": VpcLinkStatusType,
        "statusMessage": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class AccountTypeDef(TypedDict):
    cloudwatchRoleArn: str
    throttleSettings: ThrottleSettingsTypeDef
    features: List[str]
    apiKeyVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class ApiStageOutputTypeDef(TypedDict):
    apiId: NotRequired[str]
    stage: NotRequired[str]
    throttle: NotRequired[Dict[str, ThrottleSettingsTypeDef]]

class ApiStageTypeDef(TypedDict):
    apiId: NotRequired[str]
    stage: NotRequired[str]
    throttle: NotRequired[Mapping[str, ThrottleSettingsTypeDef]]

class ApiKeysTypeDef(TypedDict):
    warnings: List[str]
    position: str
    items: List[ApiKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AuthorizersTypeDef(TypedDict):
    position: str
    items: List[AuthorizerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BasePathMappingsTypeDef(TypedDict):
    position: str
    items: List[BasePathMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

ImportApiKeysRequestTypeDef = TypedDict(
    "ImportApiKeysRequestTypeDef",
    {
        "body": BlobTypeDef,
        "format": Literal["csv"],
        "failOnWarnings": NotRequired[bool],
    },
)

class ImportDocumentationPartsRequestTypeDef(TypedDict):
    restApiId: str
    body: BlobTypeDef
    mode: NotRequired[PutModeType]
    failOnWarnings: NotRequired[bool]

class ImportRestApiRequestTypeDef(TypedDict):
    body: BlobTypeDef
    failOnWarnings: NotRequired[bool]
    parameters: NotRequired[Mapping[str, str]]

class PutRestApiRequestTypeDef(TypedDict):
    restApiId: str
    body: BlobTypeDef
    mode: NotRequired[PutModeType]
    failOnWarnings: NotRequired[bool]
    parameters: NotRequired[Mapping[str, str]]

CanarySettingsUnionTypeDef = Union[CanarySettingsTypeDef, CanarySettingsOutputTypeDef]

class ClientCertificatesTypeDef(TypedDict):
    position: str
    items: List[ClientCertificateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApiKeyRequestTypeDef(TypedDict):
    name: NotRequired[str]
    description: NotRequired[str]
    enabled: NotRequired[bool]
    generateDistinctId: NotRequired[bool]
    value: NotRequired[str]
    stageKeys: NotRequired[Sequence[StageKeyTypeDef]]
    customerId: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateDeploymentRequestTypeDef(TypedDict):
    restApiId: str
    stageName: NotRequired[str]
    stageDescription: NotRequired[str]
    description: NotRequired[str]
    cacheClusterEnabled: NotRequired[bool]
    cacheClusterSize: NotRequired[CacheClusterSizeType]
    variables: NotRequired[Mapping[str, str]]
    canarySettings: NotRequired[DeploymentCanarySettingsTypeDef]
    tracingEnabled: NotRequired[bool]

class CreateDocumentationPartRequestTypeDef(TypedDict):
    restApiId: str
    location: DocumentationPartLocationTypeDef
    properties: str

DocumentationPartResponseTypeDef = TypedDict(
    "DocumentationPartResponseTypeDef",
    {
        "id": str,
        "location": DocumentationPartLocationTypeDef,
        "properties": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DocumentationPartTypeDef = TypedDict(
    "DocumentationPartTypeDef",
    {
        "id": NotRequired[str],
        "location": NotRequired[DocumentationPartLocationTypeDef],
        "properties": NotRequired[str],
    },
)
DeploymentResponseTypeDef = TypedDict(
    "DeploymentResponseTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[str, Dict[str, MethodSnapshotTypeDef]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "id": NotRequired[str],
        "description": NotRequired[str],
        "createdDate": NotRequired[datetime],
        "apiSummary": NotRequired[Dict[str, Dict[str, MethodSnapshotTypeDef]]],
    },
)

class DocumentationVersionsTypeDef(TypedDict):
    position: str
    items: List[DocumentationVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DomainNameAccessAssociationsTypeDef(TypedDict):
    position: str
    items: List[DomainNameAccessAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

RestApiResponseTypeDef = TypedDict(
    "RestApiResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": ApiKeySourceTypeType,
        "endpointConfiguration": EndpointConfigurationOutputTypeDef,
        "policy": str,
        "tags": Dict[str, str],
        "disableExecuteApiEndpoint": bool,
        "rootResourceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestApiTypeDef = TypedDict(
    "RestApiTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "createdDate": NotRequired[datetime],
        "version": NotRequired[str],
        "warnings": NotRequired[List[str]],
        "binaryMediaTypes": NotRequired[List[str]],
        "minimumCompressionSize": NotRequired[int],
        "apiKeySource": NotRequired[ApiKeySourceTypeType],
        "endpointConfiguration": NotRequired[EndpointConfigurationOutputTypeDef],
        "policy": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "disableExecuteApiEndpoint": NotRequired[bool],
        "rootResourceId": NotRequired[str],
    },
)

class DomainNameResponseTypeDef(TypedDict):
    domainName: str
    domainNameId: str
    domainNameArn: str
    certificateName: str
    certificateArn: str
    certificateUploadDate: datetime
    regionalDomainName: str
    regionalHostedZoneId: str
    regionalCertificateName: str
    regionalCertificateArn: str
    distributionDomainName: str
    distributionHostedZoneId: str
    endpointConfiguration: EndpointConfigurationOutputTypeDef
    domainNameStatus: DomainNameStatusType
    domainNameStatusMessage: str
    securityPolicy: SecurityPolicyType
    tags: Dict[str, str]
    mutualTlsAuthentication: MutualTlsAuthenticationTypeDef
    ownershipVerificationCertificateArn: str
    managementPolicy: str
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class DomainNameTypeDef(TypedDict):
    domainName: NotRequired[str]
    domainNameId: NotRequired[str]
    domainNameArn: NotRequired[str]
    certificateName: NotRequired[str]
    certificateArn: NotRequired[str]
    certificateUploadDate: NotRequired[datetime]
    regionalDomainName: NotRequired[str]
    regionalHostedZoneId: NotRequired[str]
    regionalCertificateName: NotRequired[str]
    regionalCertificateArn: NotRequired[str]
    distributionDomainName: NotRequired[str]
    distributionHostedZoneId: NotRequired[str]
    endpointConfiguration: NotRequired[EndpointConfigurationOutputTypeDef]
    domainNameStatus: NotRequired[DomainNameStatusType]
    domainNameStatusMessage: NotRequired[str]
    securityPolicy: NotRequired[SecurityPolicyType]
    tags: NotRequired[Dict[str, str]]
    mutualTlsAuthentication: NotRequired[MutualTlsAuthenticationTypeDef]
    ownershipVerificationCertificateArn: NotRequired[str]
    managementPolicy: NotRequired[str]
    policy: NotRequired[str]

EndpointConfigurationUnionTypeDef = Union[
    EndpointConfigurationTypeDef, EndpointConfigurationOutputTypeDef
]

class GatewayResponsesTypeDef(TypedDict):
    position: str
    items: List[GatewayResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetApiKeysRequestPaginateTypeDef(TypedDict):
    nameQuery: NotRequired[str]
    customerId: NotRequired[str]
    includeValues: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetAuthorizersRequestPaginateTypeDef(TypedDict):
    restApiId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetBasePathMappingsRequestPaginateTypeDef(TypedDict):
    domainName: str
    domainNameId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetClientCertificatesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetDeploymentsRequestPaginateTypeDef(TypedDict):
    restApiId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

GetDocumentationPartsRequestPaginateTypeDef = TypedDict(
    "GetDocumentationPartsRequestPaginateTypeDef",
    {
        "restApiId": str,
        "type": NotRequired[DocumentationPartTypeType],
        "nameQuery": NotRequired[str],
        "path": NotRequired[str],
        "locationStatus": NotRequired[LocationStatusTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class GetDocumentationVersionsRequestPaginateTypeDef(TypedDict):
    restApiId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetDomainNamesRequestPaginateTypeDef(TypedDict):
    resourceOwner: NotRequired[ResourceOwnerType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetGatewayResponsesRequestPaginateTypeDef(TypedDict):
    restApiId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetModelsRequestPaginateTypeDef(TypedDict):
    restApiId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetRequestValidatorsRequestPaginateTypeDef(TypedDict):
    restApiId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetResourcesRequestPaginateTypeDef(TypedDict):
    restApiId: str
    embed: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetRestApisRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetSdkTypesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetUsagePlanKeysRequestPaginateTypeDef(TypedDict):
    usagePlanId: str
    nameQuery: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetUsagePlansRequestPaginateTypeDef(TypedDict):
    keyId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetUsageRequestPaginateTypeDef(TypedDict):
    usagePlanId: str
    startDate: str
    endDate: str
    keyId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetVpcLinksRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

IntegrationResponseExtraTypeDef = TypedDict(
    "IntegrationResponseExtraTypeDef",
    {
        "type": IntegrationTypeType,
        "httpMethod": str,
        "uri": str,
        "connectionType": ConnectionTypeType,
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": ContentHandlingStrategyType,
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[str, IntegrationResponseTypeDef],
        "tlsConfig": TlsConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IntegrationTypeDef = TypedDict(
    "IntegrationTypeDef",
    {
        "type": NotRequired[IntegrationTypeType],
        "httpMethod": NotRequired[str],
        "uri": NotRequired[str],
        "connectionType": NotRequired[ConnectionTypeType],
        "connectionId": NotRequired[str],
        "credentials": NotRequired[str],
        "requestParameters": NotRequired[Dict[str, str]],
        "requestTemplates": NotRequired[Dict[str, str]],
        "passthroughBehavior": NotRequired[str],
        "contentHandling": NotRequired[ContentHandlingStrategyType],
        "timeoutInMillis": NotRequired[int],
        "cacheNamespace": NotRequired[str],
        "cacheKeyParameters": NotRequired[List[str]],
        "integrationResponses": NotRequired[Dict[str, IntegrationResponseTypeDef]],
        "tlsConfig": NotRequired[TlsConfigTypeDef],
    },
)
PutIntegrationRequestTypeDef = TypedDict(
    "PutIntegrationRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "type": IntegrationTypeType,
        "integrationHttpMethod": NotRequired[str],
        "uri": NotRequired[str],
        "connectionType": NotRequired[ConnectionTypeType],
        "connectionId": NotRequired[str],
        "credentials": NotRequired[str],
        "requestParameters": NotRequired[Mapping[str, str]],
        "requestTemplates": NotRequired[Mapping[str, str]],
        "passthroughBehavior": NotRequired[str],
        "cacheNamespace": NotRequired[str],
        "cacheKeyParameters": NotRequired[Sequence[str]],
        "contentHandling": NotRequired[ContentHandlingStrategyType],
        "timeoutInMillis": NotRequired[int],
        "tlsConfig": NotRequired[TlsConfigTypeDef],
    },
)

class StageResponseTypeDef(TypedDict):
    deploymentId: str
    clientCertificateId: str
    stageName: str
    description: str
    cacheClusterEnabled: bool
    cacheClusterSize: CacheClusterSizeType
    cacheClusterStatus: CacheClusterStatusType
    methodSettings: Dict[str, MethodSettingTypeDef]
    variables: Dict[str, str]
    documentationVersion: str
    accessLogSettings: AccessLogSettingsTypeDef
    canarySettings: CanarySettingsOutputTypeDef
    tracingEnabled: bool
    webAclArn: str
    tags: Dict[str, str]
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StageTypeDef(TypedDict):
    deploymentId: NotRequired[str]
    clientCertificateId: NotRequired[str]
    stageName: NotRequired[str]
    description: NotRequired[str]
    cacheClusterEnabled: NotRequired[bool]
    cacheClusterSize: NotRequired[CacheClusterSizeType]
    cacheClusterStatus: NotRequired[CacheClusterStatusType]
    methodSettings: NotRequired[Dict[str, MethodSettingTypeDef]]
    variables: NotRequired[Dict[str, str]]
    documentationVersion: NotRequired[str]
    accessLogSettings: NotRequired[AccessLogSettingsTypeDef]
    canarySettings: NotRequired[CanarySettingsOutputTypeDef]
    tracingEnabled: NotRequired[bool]
    webAclArn: NotRequired[str]
    tags: NotRequired[Dict[str, str]]
    createdDate: NotRequired[datetime]
    lastUpdatedDate: NotRequired[datetime]

class ModelsTypeDef(TypedDict):
    position: str
    items: List[ModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountRequestTypeDef(TypedDict):
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateApiKeyRequestTypeDef(TypedDict):
    apiKey: str
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateAuthorizerRequestTypeDef(TypedDict):
    restApiId: str
    authorizerId: str
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateBasePathMappingRequestTypeDef(TypedDict):
    domainName: str
    basePath: str
    domainNameId: NotRequired[str]
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateClientCertificateRequestTypeDef(TypedDict):
    clientCertificateId: str
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateDeploymentRequestTypeDef(TypedDict):
    restApiId: str
    deploymentId: str
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateDocumentationPartRequestTypeDef(TypedDict):
    restApiId: str
    documentationPartId: str
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateDocumentationVersionRequestTypeDef(TypedDict):
    restApiId: str
    documentationVersion: str
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateDomainNameRequestTypeDef(TypedDict):
    domainName: str
    domainNameId: NotRequired[str]
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateGatewayResponseRequestTypeDef(TypedDict):
    restApiId: str
    responseType: GatewayResponseTypeType
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateIntegrationRequestTypeDef(TypedDict):
    restApiId: str
    resourceId: str
    httpMethod: str
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateIntegrationResponseRequestTypeDef(TypedDict):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateMethodRequestTypeDef(TypedDict):
    restApiId: str
    resourceId: str
    httpMethod: str
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateMethodResponseRequestTypeDef(TypedDict):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateModelRequestTypeDef(TypedDict):
    restApiId: str
    modelName: str
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateRequestValidatorRequestTypeDef(TypedDict):
    restApiId: str
    requestValidatorId: str
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateResourceRequestTypeDef(TypedDict):
    restApiId: str
    resourceId: str
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateRestApiRequestTypeDef(TypedDict):
    restApiId: str
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateStageRequestTypeDef(TypedDict):
    restApiId: str
    stageName: str
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateUsagePlanRequestTypeDef(TypedDict):
    usagePlanId: str
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateUsageRequestTypeDef(TypedDict):
    usagePlanId: str
    keyId: str
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class UpdateVpcLinkRequestTypeDef(TypedDict):
    vpcLinkId: str
    patchOperations: NotRequired[Sequence[PatchOperationTypeDef]]

class RequestValidatorsTypeDef(TypedDict):
    position: str
    items: List[RequestValidatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

SdkTypeResponseTypeDef = TypedDict(
    "SdkTypeResponseTypeDef",
    {
        "id": str,
        "friendlyName": str,
        "description": str,
        "configurationProperties": List[SdkConfigurationPropertyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SdkTypeTypeDef = TypedDict(
    "SdkTypeTypeDef",
    {
        "id": NotRequired[str],
        "friendlyName": NotRequired[str],
        "description": NotRequired[str],
        "configurationProperties": NotRequired[List[SdkConfigurationPropertyTypeDef]],
    },
)

class UsagePlanKeysTypeDef(TypedDict):
    position: str
    items: List[UsagePlanKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class VpcLinksTypeDef(TypedDict):
    position: str
    items: List[VpcLinkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

UsagePlanResponseTypeDef = TypedDict(
    "UsagePlanResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "apiStages": List[ApiStageOutputTypeDef],
        "throttle": ThrottleSettingsTypeDef,
        "quota": QuotaSettingsTypeDef,
        "productCode": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UsagePlanTypeDef = TypedDict(
    "UsagePlanTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "apiStages": NotRequired[List[ApiStageOutputTypeDef]],
        "throttle": NotRequired[ThrottleSettingsTypeDef],
        "quota": NotRequired[QuotaSettingsTypeDef],
        "productCode": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
ApiStageUnionTypeDef = Union[ApiStageTypeDef, ApiStageOutputTypeDef]

class CreateStageRequestTypeDef(TypedDict):
    restApiId: str
    stageName: str
    deploymentId: str
    description: NotRequired[str]
    cacheClusterEnabled: NotRequired[bool]
    cacheClusterSize: NotRequired[CacheClusterSizeType]
    variables: NotRequired[Mapping[str, str]]
    documentationVersion: NotRequired[str]
    canarySettings: NotRequired[CanarySettingsUnionTypeDef]
    tracingEnabled: NotRequired[bool]
    tags: NotRequired[Mapping[str, str]]

class DocumentationPartsTypeDef(TypedDict):
    position: str
    items: List[DocumentationPartTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentsTypeDef(TypedDict):
    position: str
    items: List[DeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RestApisTypeDef(TypedDict):
    position: str
    items: List[RestApiTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DomainNamesTypeDef(TypedDict):
    position: str
    items: List[DomainNameTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainNameRequestTypeDef(TypedDict):
    domainName: str
    certificateName: NotRequired[str]
    certificateBody: NotRequired[str]
    certificatePrivateKey: NotRequired[str]
    certificateChain: NotRequired[str]
    certificateArn: NotRequired[str]
    regionalCertificateName: NotRequired[str]
    regionalCertificateArn: NotRequired[str]
    endpointConfiguration: NotRequired[EndpointConfigurationUnionTypeDef]
    tags: NotRequired[Mapping[str, str]]
    securityPolicy: NotRequired[SecurityPolicyType]
    mutualTlsAuthentication: NotRequired[MutualTlsAuthenticationInputTypeDef]
    ownershipVerificationCertificateArn: NotRequired[str]
    policy: NotRequired[str]

class CreateRestApiRequestTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    version: NotRequired[str]
    cloneFrom: NotRequired[str]
    binaryMediaTypes: NotRequired[Sequence[str]]
    minimumCompressionSize: NotRequired[int]
    apiKeySource: NotRequired[ApiKeySourceTypeType]
    endpointConfiguration: NotRequired[EndpointConfigurationUnionTypeDef]
    policy: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    disableExecuteApiEndpoint: NotRequired[bool]

class MethodResponseExtraTypeDef(TypedDict):
    httpMethod: str
    authorizationType: str
    authorizerId: str
    apiKeyRequired: bool
    requestValidatorId: str
    operationName: str
    requestParameters: Dict[str, bool]
    requestModels: Dict[str, str]
    methodResponses: Dict[str, MethodResponseTypeDef]
    methodIntegration: IntegrationTypeDef
    authorizationScopes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class MethodTypeDef(TypedDict):
    httpMethod: NotRequired[str]
    authorizationType: NotRequired[str]
    authorizerId: NotRequired[str]
    apiKeyRequired: NotRequired[bool]
    requestValidatorId: NotRequired[str]
    operationName: NotRequired[str]
    requestParameters: NotRequired[Dict[str, bool]]
    requestModels: NotRequired[Dict[str, str]]
    methodResponses: NotRequired[Dict[str, MethodResponseTypeDef]]
    methodIntegration: NotRequired[IntegrationTypeDef]
    authorizationScopes: NotRequired[List[str]]

class StagesTypeDef(TypedDict):
    item: List[StageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SdkTypesTypeDef(TypedDict):
    position: str
    items: List[SdkTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UsagePlansTypeDef(TypedDict):
    position: str
    items: List[UsagePlanTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUsagePlanRequestTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    apiStages: NotRequired[Sequence[ApiStageUnionTypeDef]]
    throttle: NotRequired[ThrottleSettingsTypeDef]
    quota: NotRequired[QuotaSettingsTypeDef]
    tags: NotRequired[Mapping[str, str]]

ResourceResponseTypeDef = TypedDict(
    "ResourceResponseTypeDef",
    {
        "id": str,
        "parentId": str,
        "pathPart": str,
        "path": str,
        "resourceMethods": Dict[str, MethodTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "id": NotRequired[str],
        "parentId": NotRequired[str],
        "pathPart": NotRequired[str],
        "path": NotRequired[str],
        "resourceMethods": NotRequired[Dict[str, MethodTypeDef]],
    },
)

class ResourcesTypeDef(TypedDict):
    position: str
    items: List[ResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
