"""
Type annotations for apigateway service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/type_defs.html)

Usage::

    ```python
    from mypy_boto3_apigateway.type_defs import AccessLogSettingsTypeDef

    data: AccessLogSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

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
    LocationStatusTypeType,
    OpType,
    PutModeType,
    QuotaPeriodTypeType,
    SecurityPolicyType,
    UnauthorizedCacheControlHeaderStrategyType,
    VpcLinkStatusType,
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
    "AccessLogSettingsTypeDef",
    "AccountTypeDef",
    "ApiKeyIdsTypeDef",
    "ApiKeyResponseMetadataTypeDef",
    "ApiKeyTypeDef",
    "ApiKeysTypeDef",
    "ApiStageTypeDef",
    "AuthorizerResponseMetadataTypeDef",
    "AuthorizerTypeDef",
    "AuthorizersTypeDef",
    "BasePathMappingResponseMetadataTypeDef",
    "BasePathMappingTypeDef",
    "BasePathMappingsTypeDef",
    "CanarySettingsTypeDef",
    "ClientCertificateResponseMetadataTypeDef",
    "ClientCertificateTypeDef",
    "ClientCertificatesTypeDef",
    "CreateApiKeyRequestRequestTypeDef",
    "CreateAuthorizerRequestRequestTypeDef",
    "CreateBasePathMappingRequestRequestTypeDef",
    "CreateDeploymentRequestRequestTypeDef",
    "CreateDocumentationPartRequestRequestTypeDef",
    "CreateDocumentationVersionRequestRequestTypeDef",
    "CreateDomainNameRequestRequestTypeDef",
    "CreateModelRequestRequestTypeDef",
    "CreateRequestValidatorRequestRequestTypeDef",
    "CreateResourceRequestRequestTypeDef",
    "CreateRestApiRequestRequestTypeDef",
    "CreateStageRequestRequestTypeDef",
    "CreateUsagePlanKeyRequestRequestTypeDef",
    "CreateUsagePlanRequestRequestTypeDef",
    "CreateVpcLinkRequestRequestTypeDef",
    "DeleteApiKeyRequestRequestTypeDef",
    "DeleteAuthorizerRequestRequestTypeDef",
    "DeleteBasePathMappingRequestRequestTypeDef",
    "DeleteClientCertificateRequestRequestTypeDef",
    "DeleteDeploymentRequestRequestTypeDef",
    "DeleteDocumentationPartRequestRequestTypeDef",
    "DeleteDocumentationVersionRequestRequestTypeDef",
    "DeleteDomainNameRequestRequestTypeDef",
    "DeleteGatewayResponseRequestRequestTypeDef",
    "DeleteIntegrationRequestRequestTypeDef",
    "DeleteIntegrationResponseRequestRequestTypeDef",
    "DeleteMethodRequestRequestTypeDef",
    "DeleteMethodResponseRequestRequestTypeDef",
    "DeleteModelRequestRequestTypeDef",
    "DeleteRequestValidatorRequestRequestTypeDef",
    "DeleteResourceRequestRequestTypeDef",
    "DeleteRestApiRequestRequestTypeDef",
    "DeleteStageRequestRequestTypeDef",
    "DeleteUsagePlanKeyRequestRequestTypeDef",
    "DeleteUsagePlanRequestRequestTypeDef",
    "DeleteVpcLinkRequestRequestTypeDef",
    "DeploymentCanarySettingsTypeDef",
    "DeploymentResponseMetadataTypeDef",
    "DeploymentTypeDef",
    "DeploymentsTypeDef",
    "DocumentationPartIdsTypeDef",
    "DocumentationPartLocationTypeDef",
    "DocumentationPartResponseMetadataTypeDef",
    "DocumentationPartTypeDef",
    "DocumentationPartsTypeDef",
    "DocumentationVersionResponseMetadataTypeDef",
    "DocumentationVersionTypeDef",
    "DocumentationVersionsTypeDef",
    "DomainNameResponseMetadataTypeDef",
    "DomainNameTypeDef",
    "DomainNamesTypeDef",
    "EndpointConfigurationTypeDef",
    "ExportResponseTypeDef",
    "FlushStageAuthorizersCacheRequestRequestTypeDef",
    "FlushStageCacheRequestRequestTypeDef",
    "GatewayResponseResponseMetadataTypeDef",
    "GatewayResponseTypeDef",
    "GatewayResponsesTypeDef",
    "GenerateClientCertificateRequestRequestTypeDef",
    "GetApiKeyRequestRequestTypeDef",
    "GetApiKeysRequestRequestTypeDef",
    "GetAuthorizerRequestRequestTypeDef",
    "GetAuthorizersRequestRequestTypeDef",
    "GetBasePathMappingRequestRequestTypeDef",
    "GetBasePathMappingsRequestRequestTypeDef",
    "GetClientCertificateRequestRequestTypeDef",
    "GetClientCertificatesRequestRequestTypeDef",
    "GetDeploymentRequestRequestTypeDef",
    "GetDeploymentsRequestRequestTypeDef",
    "GetDocumentationPartRequestRequestTypeDef",
    "GetDocumentationPartsRequestRequestTypeDef",
    "GetDocumentationVersionRequestRequestTypeDef",
    "GetDocumentationVersionsRequestRequestTypeDef",
    "GetDomainNameRequestRequestTypeDef",
    "GetDomainNamesRequestRequestTypeDef",
    "GetExportRequestRequestTypeDef",
    "GetGatewayResponseRequestRequestTypeDef",
    "GetGatewayResponsesRequestRequestTypeDef",
    "GetIntegrationRequestRequestTypeDef",
    "GetIntegrationResponseRequestRequestTypeDef",
    "GetMethodRequestRequestTypeDef",
    "GetMethodResponseRequestRequestTypeDef",
    "GetModelRequestRequestTypeDef",
    "GetModelTemplateRequestRequestTypeDef",
    "GetModelsRequestRequestTypeDef",
    "GetRequestValidatorRequestRequestTypeDef",
    "GetRequestValidatorsRequestRequestTypeDef",
    "GetResourceRequestRequestTypeDef",
    "GetResourcesRequestRequestTypeDef",
    "GetRestApiRequestRequestTypeDef",
    "GetRestApisRequestRequestTypeDef",
    "GetSdkRequestRequestTypeDef",
    "GetSdkTypeRequestRequestTypeDef",
    "GetSdkTypesRequestRequestTypeDef",
    "GetStageRequestRequestTypeDef",
    "GetStagesRequestRequestTypeDef",
    "GetTagsRequestRequestTypeDef",
    "GetUsagePlanKeyRequestRequestTypeDef",
    "GetUsagePlanKeysRequestRequestTypeDef",
    "GetUsagePlanRequestRequestTypeDef",
    "GetUsagePlansRequestRequestTypeDef",
    "GetUsageRequestRequestTypeDef",
    "GetVpcLinkRequestRequestTypeDef",
    "GetVpcLinksRequestRequestTypeDef",
    "ImportApiKeysRequestRequestTypeDef",
    "ImportDocumentationPartsRequestRequestTypeDef",
    "ImportRestApiRequestRequestTypeDef",
    "IntegrationResponseMetadataTypeDef",
    "IntegrationResponseResponseMetadataTypeDef",
    "IntegrationResponseTypeDef",
    "IntegrationTypeDef",
    "MethodResponseMetadataTypeDef",
    "MethodResponseResponseMetadataTypeDef",
    "MethodResponseTypeDef",
    "MethodSettingTypeDef",
    "MethodSnapshotTypeDef",
    "MethodTypeDef",
    "ModelResponseMetadataTypeDef",
    "ModelTypeDef",
    "ModelsTypeDef",
    "MutualTlsAuthenticationInputTypeDef",
    "MutualTlsAuthenticationTypeDef",
    "PaginatorConfigTypeDef",
    "PatchOperationTypeDef",
    "PutGatewayResponseRequestRequestTypeDef",
    "PutIntegrationRequestRequestTypeDef",
    "PutIntegrationResponseRequestRequestTypeDef",
    "PutMethodRequestRequestTypeDef",
    "PutMethodResponseRequestRequestTypeDef",
    "PutRestApiRequestRequestTypeDef",
    "QuotaSettingsTypeDef",
    "RequestValidatorResponseMetadataTypeDef",
    "RequestValidatorTypeDef",
    "RequestValidatorsTypeDef",
    "ResourceResponseMetadataTypeDef",
    "ResourceTypeDef",
    "ResourcesTypeDef",
    "ResponseMetadataTypeDef",
    "RestApiResponseMetadataTypeDef",
    "RestApiTypeDef",
    "RestApisTypeDef",
    "SdkConfigurationPropertyTypeDef",
    "SdkResponseTypeDef",
    "SdkTypeResponseMetadataTypeDef",
    "SdkTypeTypeDef",
    "SdkTypesTypeDef",
    "StageKeyTypeDef",
    "StageResponseMetadataTypeDef",
    "StageTypeDef",
    "StagesTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagsTypeDef",
    "TemplateTypeDef",
    "TestInvokeAuthorizerRequestRequestTypeDef",
    "TestInvokeAuthorizerResponseTypeDef",
    "TestInvokeMethodRequestRequestTypeDef",
    "TestInvokeMethodResponseTypeDef",
    "ThrottleSettingsTypeDef",
    "TlsConfigTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccountRequestRequestTypeDef",
    "UpdateApiKeyRequestRequestTypeDef",
    "UpdateAuthorizerRequestRequestTypeDef",
    "UpdateBasePathMappingRequestRequestTypeDef",
    "UpdateClientCertificateRequestRequestTypeDef",
    "UpdateDeploymentRequestRequestTypeDef",
    "UpdateDocumentationPartRequestRequestTypeDef",
    "UpdateDocumentationVersionRequestRequestTypeDef",
    "UpdateDomainNameRequestRequestTypeDef",
    "UpdateGatewayResponseRequestRequestTypeDef",
    "UpdateIntegrationRequestRequestTypeDef",
    "UpdateIntegrationResponseRequestRequestTypeDef",
    "UpdateMethodRequestRequestTypeDef",
    "UpdateMethodResponseRequestRequestTypeDef",
    "UpdateModelRequestRequestTypeDef",
    "UpdateRequestValidatorRequestRequestTypeDef",
    "UpdateResourceRequestRequestTypeDef",
    "UpdateRestApiRequestRequestTypeDef",
    "UpdateStageRequestRequestTypeDef",
    "UpdateUsagePlanRequestRequestTypeDef",
    "UpdateUsageRequestRequestTypeDef",
    "UpdateVpcLinkRequestRequestTypeDef",
    "UsagePlanKeyResponseMetadataTypeDef",
    "UsagePlanKeyTypeDef",
    "UsagePlanKeysTypeDef",
    "UsagePlanResponseMetadataTypeDef",
    "UsagePlanTypeDef",
    "UsagePlansTypeDef",
    "UsageTypeDef",
    "VpcLinkResponseMetadataTypeDef",
    "VpcLinkTypeDef",
    "VpcLinksTypeDef",
)

AccessLogSettingsTypeDef = TypedDict(
    "AccessLogSettingsTypeDef",
    {
        "format": str,
        "destinationArn": str,
    },
    total=False,
)

AccountTypeDef = TypedDict(
    "AccountTypeDef",
    {
        "cloudwatchRoleArn": str,
        "throttleSettings": "ThrottleSettingsTypeDef",
        "features": List[str],
        "apiKeyVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApiKeyIdsTypeDef = TypedDict(
    "ApiKeyIdsTypeDef",
    {
        "ids": List[str],
        "warnings": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApiKeyResponseMetadataTypeDef = TypedDict(
    "ApiKeyResponseMetadataTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApiKeyTypeDef = TypedDict(
    "ApiKeyTypeDef",
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
    },
    total=False,
)

ApiKeysTypeDef = TypedDict(
    "ApiKeysTypeDef",
    {
        "warnings": List[str],
        "position": str,
        "items": List["ApiKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApiStageTypeDef = TypedDict(
    "ApiStageTypeDef",
    {
        "apiId": str,
        "stage": str,
        "throttle": Dict[str, "ThrottleSettingsTypeDef"],
    },
    total=False,
)

AuthorizerResponseMetadataTypeDef = TypedDict(
    "AuthorizerResponseMetadataTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuthorizerTypeDef = TypedDict(
    "AuthorizerTypeDef",
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
    },
    total=False,
)

AuthorizersTypeDef = TypedDict(
    "AuthorizersTypeDef",
    {
        "position": str,
        "items": List["AuthorizerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BasePathMappingResponseMetadataTypeDef = TypedDict(
    "BasePathMappingResponseMetadataTypeDef",
    {
        "basePath": str,
        "restApiId": str,
        "stage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BasePathMappingTypeDef = TypedDict(
    "BasePathMappingTypeDef",
    {
        "basePath": str,
        "restApiId": str,
        "stage": str,
    },
    total=False,
)

BasePathMappingsTypeDef = TypedDict(
    "BasePathMappingsTypeDef",
    {
        "position": str,
        "items": List["BasePathMappingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CanarySettingsTypeDef = TypedDict(
    "CanarySettingsTypeDef",
    {
        "percentTraffic": float,
        "deploymentId": str,
        "stageVariableOverrides": Dict[str, str],
        "useStageCache": bool,
    },
    total=False,
)

ClientCertificateResponseMetadataTypeDef = TypedDict(
    "ClientCertificateResponseMetadataTypeDef",
    {
        "clientCertificateId": str,
        "description": str,
        "pemEncodedCertificate": str,
        "createdDate": datetime,
        "expirationDate": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClientCertificateTypeDef = TypedDict(
    "ClientCertificateTypeDef",
    {
        "clientCertificateId": str,
        "description": str,
        "pemEncodedCertificate": str,
        "createdDate": datetime,
        "expirationDate": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientCertificatesTypeDef = TypedDict(
    "ClientCertificatesTypeDef",
    {
        "position": str,
        "items": List["ClientCertificateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateApiKeyRequestRequestTypeDef = TypedDict(
    "CreateApiKeyRequestRequestTypeDef",
    {
        "name": str,
        "description": str,
        "enabled": bool,
        "generateDistinctId": bool,
        "value": str,
        "stageKeys": List["StageKeyTypeDef"],
        "customerId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredCreateAuthorizerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAuthorizerRequestRequestTypeDef",
    {
        "restApiId": str,
        "name": str,
        "type": AuthorizerTypeType,
    },
)
_OptionalCreateAuthorizerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAuthorizerRequestRequestTypeDef",
    {
        "providerARNs": List[str],
        "authType": str,
        "authorizerUri": str,
        "authorizerCredentials": str,
        "identitySource": str,
        "identityValidationExpression": str,
        "authorizerResultTtlInSeconds": int,
    },
    total=False,
)

class CreateAuthorizerRequestRequestTypeDef(
    _RequiredCreateAuthorizerRequestRequestTypeDef, _OptionalCreateAuthorizerRequestRequestTypeDef
):
    pass

_RequiredCreateBasePathMappingRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBasePathMappingRequestRequestTypeDef",
    {
        "domainName": str,
        "restApiId": str,
    },
)
_OptionalCreateBasePathMappingRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBasePathMappingRequestRequestTypeDef",
    {
        "basePath": str,
        "stage": str,
    },
    total=False,
)

class CreateBasePathMappingRequestRequestTypeDef(
    _RequiredCreateBasePathMappingRequestRequestTypeDef,
    _OptionalCreateBasePathMappingRequestRequestTypeDef,
):
    pass

_RequiredCreateDeploymentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDeploymentRequestRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalCreateDeploymentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDeploymentRequestRequestTypeDef",
    {
        "stageName": str,
        "stageDescription": str,
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": CacheClusterSizeType,
        "variables": Dict[str, str],
        "canarySettings": "DeploymentCanarySettingsTypeDef",
        "tracingEnabled": bool,
    },
    total=False,
)

class CreateDeploymentRequestRequestTypeDef(
    _RequiredCreateDeploymentRequestRequestTypeDef, _OptionalCreateDeploymentRequestRequestTypeDef
):
    pass

CreateDocumentationPartRequestRequestTypeDef = TypedDict(
    "CreateDocumentationPartRequestRequestTypeDef",
    {
        "restApiId": str,
        "location": "DocumentationPartLocationTypeDef",
        "properties": str,
    },
)

_RequiredCreateDocumentationVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDocumentationVersionRequestRequestTypeDef",
    {
        "restApiId": str,
        "documentationVersion": str,
    },
)
_OptionalCreateDocumentationVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDocumentationVersionRequestRequestTypeDef",
    {
        "stageName": str,
        "description": str,
    },
    total=False,
)

class CreateDocumentationVersionRequestRequestTypeDef(
    _RequiredCreateDocumentationVersionRequestRequestTypeDef,
    _OptionalCreateDocumentationVersionRequestRequestTypeDef,
):
    pass

_RequiredCreateDomainNameRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDomainNameRequestRequestTypeDef",
    {
        "domainName": str,
    },
)
_OptionalCreateDomainNameRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDomainNameRequestRequestTypeDef",
    {
        "certificateName": str,
        "certificateBody": str,
        "certificatePrivateKey": str,
        "certificateChain": str,
        "certificateArn": str,
        "regionalCertificateName": str,
        "regionalCertificateArn": str,
        "endpointConfiguration": "EndpointConfigurationTypeDef",
        "tags": Dict[str, str],
        "securityPolicy": SecurityPolicyType,
        "mutualTlsAuthentication": "MutualTlsAuthenticationInputTypeDef",
    },
    total=False,
)

class CreateDomainNameRequestRequestTypeDef(
    _RequiredCreateDomainNameRequestRequestTypeDef, _OptionalCreateDomainNameRequestRequestTypeDef
):
    pass

_RequiredCreateModelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelRequestRequestTypeDef",
    {
        "restApiId": str,
        "name": str,
        "contentType": str,
    },
)
_OptionalCreateModelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelRequestRequestTypeDef",
    {
        "description": str,
        "schema": str,
    },
    total=False,
)

class CreateModelRequestRequestTypeDef(
    _RequiredCreateModelRequestRequestTypeDef, _OptionalCreateModelRequestRequestTypeDef
):
    pass

_RequiredCreateRequestValidatorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRequestValidatorRequestRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalCreateRequestValidatorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRequestValidatorRequestRequestTypeDef",
    {
        "name": str,
        "validateRequestBody": bool,
        "validateRequestParameters": bool,
    },
    total=False,
)

class CreateRequestValidatorRequestRequestTypeDef(
    _RequiredCreateRequestValidatorRequestRequestTypeDef,
    _OptionalCreateRequestValidatorRequestRequestTypeDef,
):
    pass

CreateResourceRequestRequestTypeDef = TypedDict(
    "CreateResourceRequestRequestTypeDef",
    {
        "restApiId": str,
        "parentId": str,
        "pathPart": str,
    },
)

_RequiredCreateRestApiRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRestApiRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateRestApiRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRestApiRequestRequestTypeDef",
    {
        "description": str,
        "version": str,
        "cloneFrom": str,
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": ApiKeySourceTypeType,
        "endpointConfiguration": "EndpointConfigurationTypeDef",
        "policy": str,
        "tags": Dict[str, str],
        "disableExecuteApiEndpoint": bool,
    },
    total=False,
)

class CreateRestApiRequestRequestTypeDef(
    _RequiredCreateRestApiRequestRequestTypeDef, _OptionalCreateRestApiRequestRequestTypeDef
):
    pass

_RequiredCreateStageRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStageRequestRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
        "deploymentId": str,
    },
)
_OptionalCreateStageRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStageRequestRequestTypeDef",
    {
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": CacheClusterSizeType,
        "variables": Dict[str, str],
        "documentationVersion": str,
        "canarySettings": "CanarySettingsTypeDef",
        "tracingEnabled": bool,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateStageRequestRequestTypeDef(
    _RequiredCreateStageRequestRequestTypeDef, _OptionalCreateStageRequestRequestTypeDef
):
    pass

CreateUsagePlanKeyRequestRequestTypeDef = TypedDict(
    "CreateUsagePlanKeyRequestRequestTypeDef",
    {
        "usagePlanId": str,
        "keyId": str,
        "keyType": str,
    },
)

_RequiredCreateUsagePlanRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUsagePlanRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateUsagePlanRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUsagePlanRequestRequestTypeDef",
    {
        "description": str,
        "apiStages": List["ApiStageTypeDef"],
        "throttle": "ThrottleSettingsTypeDef",
        "quota": "QuotaSettingsTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateUsagePlanRequestRequestTypeDef(
    _RequiredCreateUsagePlanRequestRequestTypeDef, _OptionalCreateUsagePlanRequestRequestTypeDef
):
    pass

_RequiredCreateVpcLinkRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVpcLinkRequestRequestTypeDef",
    {
        "name": str,
        "targetArns": List[str],
    },
)
_OptionalCreateVpcLinkRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVpcLinkRequestRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateVpcLinkRequestRequestTypeDef(
    _RequiredCreateVpcLinkRequestRequestTypeDef, _OptionalCreateVpcLinkRequestRequestTypeDef
):
    pass

DeleteApiKeyRequestRequestTypeDef = TypedDict(
    "DeleteApiKeyRequestRequestTypeDef",
    {
        "apiKey": str,
    },
)

DeleteAuthorizerRequestRequestTypeDef = TypedDict(
    "DeleteAuthorizerRequestRequestTypeDef",
    {
        "restApiId": str,
        "authorizerId": str,
    },
)

DeleteBasePathMappingRequestRequestTypeDef = TypedDict(
    "DeleteBasePathMappingRequestRequestTypeDef",
    {
        "domainName": str,
        "basePath": str,
    },
)

DeleteClientCertificateRequestRequestTypeDef = TypedDict(
    "DeleteClientCertificateRequestRequestTypeDef",
    {
        "clientCertificateId": str,
    },
)

DeleteDeploymentRequestRequestTypeDef = TypedDict(
    "DeleteDeploymentRequestRequestTypeDef",
    {
        "restApiId": str,
        "deploymentId": str,
    },
)

DeleteDocumentationPartRequestRequestTypeDef = TypedDict(
    "DeleteDocumentationPartRequestRequestTypeDef",
    {
        "restApiId": str,
        "documentationPartId": str,
    },
)

DeleteDocumentationVersionRequestRequestTypeDef = TypedDict(
    "DeleteDocumentationVersionRequestRequestTypeDef",
    {
        "restApiId": str,
        "documentationVersion": str,
    },
)

DeleteDomainNameRequestRequestTypeDef = TypedDict(
    "DeleteDomainNameRequestRequestTypeDef",
    {
        "domainName": str,
    },
)

DeleteGatewayResponseRequestRequestTypeDef = TypedDict(
    "DeleteGatewayResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "responseType": GatewayResponseTypeType,
    },
)

DeleteIntegrationRequestRequestTypeDef = TypedDict(
    "DeleteIntegrationRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
    },
)

DeleteIntegrationResponseRequestRequestTypeDef = TypedDict(
    "DeleteIntegrationResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
    },
)

DeleteMethodRequestRequestTypeDef = TypedDict(
    "DeleteMethodRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
    },
)

DeleteMethodResponseRequestRequestTypeDef = TypedDict(
    "DeleteMethodResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
    },
)

DeleteModelRequestRequestTypeDef = TypedDict(
    "DeleteModelRequestRequestTypeDef",
    {
        "restApiId": str,
        "modelName": str,
    },
)

DeleteRequestValidatorRequestRequestTypeDef = TypedDict(
    "DeleteRequestValidatorRequestRequestTypeDef",
    {
        "restApiId": str,
        "requestValidatorId": str,
    },
)

DeleteResourceRequestRequestTypeDef = TypedDict(
    "DeleteResourceRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
    },
)

DeleteRestApiRequestRequestTypeDef = TypedDict(
    "DeleteRestApiRequestRequestTypeDef",
    {
        "restApiId": str,
    },
)

DeleteStageRequestRequestTypeDef = TypedDict(
    "DeleteStageRequestRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
    },
)

DeleteUsagePlanKeyRequestRequestTypeDef = TypedDict(
    "DeleteUsagePlanKeyRequestRequestTypeDef",
    {
        "usagePlanId": str,
        "keyId": str,
    },
)

DeleteUsagePlanRequestRequestTypeDef = TypedDict(
    "DeleteUsagePlanRequestRequestTypeDef",
    {
        "usagePlanId": str,
    },
)

DeleteVpcLinkRequestRequestTypeDef = TypedDict(
    "DeleteVpcLinkRequestRequestTypeDef",
    {
        "vpcLinkId": str,
    },
)

DeploymentCanarySettingsTypeDef = TypedDict(
    "DeploymentCanarySettingsTypeDef",
    {
        "percentTraffic": float,
        "stageVariableOverrides": Dict[str, str],
        "useStageCache": bool,
    },
    total=False,
)

DeploymentResponseMetadataTypeDef = TypedDict(
    "DeploymentResponseMetadataTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[str, Dict[str, "MethodSnapshotTypeDef"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[str, Dict[str, "MethodSnapshotTypeDef"]],
    },
    total=False,
)

DeploymentsTypeDef = TypedDict(
    "DeploymentsTypeDef",
    {
        "position": str,
        "items": List["DeploymentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DocumentationPartIdsTypeDef = TypedDict(
    "DocumentationPartIdsTypeDef",
    {
        "ids": List[str],
        "warnings": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDocumentationPartLocationTypeDef = TypedDict(
    "_RequiredDocumentationPartLocationTypeDef",
    {
        "type": DocumentationPartTypeType,
    },
)
_OptionalDocumentationPartLocationTypeDef = TypedDict(
    "_OptionalDocumentationPartLocationTypeDef",
    {
        "path": str,
        "method": str,
        "statusCode": str,
        "name": str,
    },
    total=False,
)

class DocumentationPartLocationTypeDef(
    _RequiredDocumentationPartLocationTypeDef, _OptionalDocumentationPartLocationTypeDef
):
    pass

DocumentationPartResponseMetadataTypeDef = TypedDict(
    "DocumentationPartResponseMetadataTypeDef",
    {
        "id": str,
        "location": "DocumentationPartLocationTypeDef",
        "properties": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DocumentationPartTypeDef = TypedDict(
    "DocumentationPartTypeDef",
    {
        "id": str,
        "location": "DocumentationPartLocationTypeDef",
        "properties": str,
    },
    total=False,
)

DocumentationPartsTypeDef = TypedDict(
    "DocumentationPartsTypeDef",
    {
        "position": str,
        "items": List["DocumentationPartTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DocumentationVersionResponseMetadataTypeDef = TypedDict(
    "DocumentationVersionResponseMetadataTypeDef",
    {
        "version": str,
        "createdDate": datetime,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DocumentationVersionTypeDef = TypedDict(
    "DocumentationVersionTypeDef",
    {
        "version": str,
        "createdDate": datetime,
        "description": str,
    },
    total=False,
)

DocumentationVersionsTypeDef = TypedDict(
    "DocumentationVersionsTypeDef",
    {
        "position": str,
        "items": List["DocumentationVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainNameResponseMetadataTypeDef = TypedDict(
    "DomainNameResponseMetadataTypeDef",
    {
        "domainName": str,
        "certificateName": str,
        "certificateArn": str,
        "certificateUploadDate": datetime,
        "regionalDomainName": str,
        "regionalHostedZoneId": str,
        "regionalCertificateName": str,
        "regionalCertificateArn": str,
        "distributionDomainName": str,
        "distributionHostedZoneId": str,
        "endpointConfiguration": "EndpointConfigurationTypeDef",
        "domainNameStatus": DomainNameStatusType,
        "domainNameStatusMessage": str,
        "securityPolicy": SecurityPolicyType,
        "tags": Dict[str, str],
        "mutualTlsAuthentication": "MutualTlsAuthenticationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainNameTypeDef = TypedDict(
    "DomainNameTypeDef",
    {
        "domainName": str,
        "certificateName": str,
        "certificateArn": str,
        "certificateUploadDate": datetime,
        "regionalDomainName": str,
        "regionalHostedZoneId": str,
        "regionalCertificateName": str,
        "regionalCertificateArn": str,
        "distributionDomainName": str,
        "distributionHostedZoneId": str,
        "endpointConfiguration": "EndpointConfigurationTypeDef",
        "domainNameStatus": DomainNameStatusType,
        "domainNameStatusMessage": str,
        "securityPolicy": SecurityPolicyType,
        "tags": Dict[str, str],
        "mutualTlsAuthentication": "MutualTlsAuthenticationTypeDef",
    },
    total=False,
)

DomainNamesTypeDef = TypedDict(
    "DomainNamesTypeDef",
    {
        "position": str,
        "items": List["DomainNameTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointConfigurationTypeDef = TypedDict(
    "EndpointConfigurationTypeDef",
    {
        "types": List[EndpointTypeType],
        "vpcEndpointIds": List[str],
    },
    total=False,
)

ExportResponseTypeDef = TypedDict(
    "ExportResponseTypeDef",
    {
        "contentType": str,
        "contentDisposition": str,
        "body": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FlushStageAuthorizersCacheRequestRequestTypeDef = TypedDict(
    "FlushStageAuthorizersCacheRequestRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
    },
)

FlushStageCacheRequestRequestTypeDef = TypedDict(
    "FlushStageCacheRequestRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
    },
)

GatewayResponseResponseMetadataTypeDef = TypedDict(
    "GatewayResponseResponseMetadataTypeDef",
    {
        "responseType": GatewayResponseTypeType,
        "statusCode": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "defaultResponse": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GatewayResponseTypeDef = TypedDict(
    "GatewayResponseTypeDef",
    {
        "responseType": GatewayResponseTypeType,
        "statusCode": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "defaultResponse": bool,
    },
    total=False,
)

GatewayResponsesTypeDef = TypedDict(
    "GatewayResponsesTypeDef",
    {
        "position": str,
        "items": List["GatewayResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GenerateClientCertificateRequestRequestTypeDef = TypedDict(
    "GenerateClientCertificateRequestRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredGetApiKeyRequestRequestTypeDef = TypedDict(
    "_RequiredGetApiKeyRequestRequestTypeDef",
    {
        "apiKey": str,
    },
)
_OptionalGetApiKeyRequestRequestTypeDef = TypedDict(
    "_OptionalGetApiKeyRequestRequestTypeDef",
    {
        "includeValue": bool,
    },
    total=False,
)

class GetApiKeyRequestRequestTypeDef(
    _RequiredGetApiKeyRequestRequestTypeDef, _OptionalGetApiKeyRequestRequestTypeDef
):
    pass

GetApiKeysRequestRequestTypeDef = TypedDict(
    "GetApiKeysRequestRequestTypeDef",
    {
        "position": str,
        "limit": int,
        "nameQuery": str,
        "customerId": str,
        "includeValues": bool,
    },
    total=False,
)

GetAuthorizerRequestRequestTypeDef = TypedDict(
    "GetAuthorizerRequestRequestTypeDef",
    {
        "restApiId": str,
        "authorizerId": str,
    },
)

_RequiredGetAuthorizersRequestRequestTypeDef = TypedDict(
    "_RequiredGetAuthorizersRequestRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalGetAuthorizersRequestRequestTypeDef = TypedDict(
    "_OptionalGetAuthorizersRequestRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)

class GetAuthorizersRequestRequestTypeDef(
    _RequiredGetAuthorizersRequestRequestTypeDef, _OptionalGetAuthorizersRequestRequestTypeDef
):
    pass

GetBasePathMappingRequestRequestTypeDef = TypedDict(
    "GetBasePathMappingRequestRequestTypeDef",
    {
        "domainName": str,
        "basePath": str,
    },
)

_RequiredGetBasePathMappingsRequestRequestTypeDef = TypedDict(
    "_RequiredGetBasePathMappingsRequestRequestTypeDef",
    {
        "domainName": str,
    },
)
_OptionalGetBasePathMappingsRequestRequestTypeDef = TypedDict(
    "_OptionalGetBasePathMappingsRequestRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)

class GetBasePathMappingsRequestRequestTypeDef(
    _RequiredGetBasePathMappingsRequestRequestTypeDef,
    _OptionalGetBasePathMappingsRequestRequestTypeDef,
):
    pass

GetClientCertificateRequestRequestTypeDef = TypedDict(
    "GetClientCertificateRequestRequestTypeDef",
    {
        "clientCertificateId": str,
    },
)

GetClientCertificatesRequestRequestTypeDef = TypedDict(
    "GetClientCertificatesRequestRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)

_RequiredGetDeploymentRequestRequestTypeDef = TypedDict(
    "_RequiredGetDeploymentRequestRequestTypeDef",
    {
        "restApiId": str,
        "deploymentId": str,
    },
)
_OptionalGetDeploymentRequestRequestTypeDef = TypedDict(
    "_OptionalGetDeploymentRequestRequestTypeDef",
    {
        "embed": List[str],
    },
    total=False,
)

class GetDeploymentRequestRequestTypeDef(
    _RequiredGetDeploymentRequestRequestTypeDef, _OptionalGetDeploymentRequestRequestTypeDef
):
    pass

_RequiredGetDeploymentsRequestRequestTypeDef = TypedDict(
    "_RequiredGetDeploymentsRequestRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalGetDeploymentsRequestRequestTypeDef = TypedDict(
    "_OptionalGetDeploymentsRequestRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)

class GetDeploymentsRequestRequestTypeDef(
    _RequiredGetDeploymentsRequestRequestTypeDef, _OptionalGetDeploymentsRequestRequestTypeDef
):
    pass

GetDocumentationPartRequestRequestTypeDef = TypedDict(
    "GetDocumentationPartRequestRequestTypeDef",
    {
        "restApiId": str,
        "documentationPartId": str,
    },
)

_RequiredGetDocumentationPartsRequestRequestTypeDef = TypedDict(
    "_RequiredGetDocumentationPartsRequestRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalGetDocumentationPartsRequestRequestTypeDef = TypedDict(
    "_OptionalGetDocumentationPartsRequestRequestTypeDef",
    {
        "type": DocumentationPartTypeType,
        "nameQuery": str,
        "path": str,
        "position": str,
        "limit": int,
        "locationStatus": LocationStatusTypeType,
    },
    total=False,
)

class GetDocumentationPartsRequestRequestTypeDef(
    _RequiredGetDocumentationPartsRequestRequestTypeDef,
    _OptionalGetDocumentationPartsRequestRequestTypeDef,
):
    pass

GetDocumentationVersionRequestRequestTypeDef = TypedDict(
    "GetDocumentationVersionRequestRequestTypeDef",
    {
        "restApiId": str,
        "documentationVersion": str,
    },
)

_RequiredGetDocumentationVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredGetDocumentationVersionsRequestRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalGetDocumentationVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalGetDocumentationVersionsRequestRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)

class GetDocumentationVersionsRequestRequestTypeDef(
    _RequiredGetDocumentationVersionsRequestRequestTypeDef,
    _OptionalGetDocumentationVersionsRequestRequestTypeDef,
):
    pass

GetDomainNameRequestRequestTypeDef = TypedDict(
    "GetDomainNameRequestRequestTypeDef",
    {
        "domainName": str,
    },
)

GetDomainNamesRequestRequestTypeDef = TypedDict(
    "GetDomainNamesRequestRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)

_RequiredGetExportRequestRequestTypeDef = TypedDict(
    "_RequiredGetExportRequestRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
        "exportType": str,
    },
)
_OptionalGetExportRequestRequestTypeDef = TypedDict(
    "_OptionalGetExportRequestRequestTypeDef",
    {
        "parameters": Dict[str, str],
        "accepts": str,
    },
    total=False,
)

class GetExportRequestRequestTypeDef(
    _RequiredGetExportRequestRequestTypeDef, _OptionalGetExportRequestRequestTypeDef
):
    pass

GetGatewayResponseRequestRequestTypeDef = TypedDict(
    "GetGatewayResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "responseType": GatewayResponseTypeType,
    },
)

_RequiredGetGatewayResponsesRequestRequestTypeDef = TypedDict(
    "_RequiredGetGatewayResponsesRequestRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalGetGatewayResponsesRequestRequestTypeDef = TypedDict(
    "_OptionalGetGatewayResponsesRequestRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)

class GetGatewayResponsesRequestRequestTypeDef(
    _RequiredGetGatewayResponsesRequestRequestTypeDef,
    _OptionalGetGatewayResponsesRequestRequestTypeDef,
):
    pass

GetIntegrationRequestRequestTypeDef = TypedDict(
    "GetIntegrationRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
    },
)

GetIntegrationResponseRequestRequestTypeDef = TypedDict(
    "GetIntegrationResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
    },
)

GetMethodRequestRequestTypeDef = TypedDict(
    "GetMethodRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
    },
)

GetMethodResponseRequestRequestTypeDef = TypedDict(
    "GetMethodResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
    },
)

_RequiredGetModelRequestRequestTypeDef = TypedDict(
    "_RequiredGetModelRequestRequestTypeDef",
    {
        "restApiId": str,
        "modelName": str,
    },
)
_OptionalGetModelRequestRequestTypeDef = TypedDict(
    "_OptionalGetModelRequestRequestTypeDef",
    {
        "flatten": bool,
    },
    total=False,
)

class GetModelRequestRequestTypeDef(
    _RequiredGetModelRequestRequestTypeDef, _OptionalGetModelRequestRequestTypeDef
):
    pass

GetModelTemplateRequestRequestTypeDef = TypedDict(
    "GetModelTemplateRequestRequestTypeDef",
    {
        "restApiId": str,
        "modelName": str,
    },
)

_RequiredGetModelsRequestRequestTypeDef = TypedDict(
    "_RequiredGetModelsRequestRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalGetModelsRequestRequestTypeDef = TypedDict(
    "_OptionalGetModelsRequestRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)

class GetModelsRequestRequestTypeDef(
    _RequiredGetModelsRequestRequestTypeDef, _OptionalGetModelsRequestRequestTypeDef
):
    pass

GetRequestValidatorRequestRequestTypeDef = TypedDict(
    "GetRequestValidatorRequestRequestTypeDef",
    {
        "restApiId": str,
        "requestValidatorId": str,
    },
)

_RequiredGetRequestValidatorsRequestRequestTypeDef = TypedDict(
    "_RequiredGetRequestValidatorsRequestRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalGetRequestValidatorsRequestRequestTypeDef = TypedDict(
    "_OptionalGetRequestValidatorsRequestRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)

class GetRequestValidatorsRequestRequestTypeDef(
    _RequiredGetRequestValidatorsRequestRequestTypeDef,
    _OptionalGetRequestValidatorsRequestRequestTypeDef,
):
    pass

_RequiredGetResourceRequestRequestTypeDef = TypedDict(
    "_RequiredGetResourceRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
    },
)
_OptionalGetResourceRequestRequestTypeDef = TypedDict(
    "_OptionalGetResourceRequestRequestTypeDef",
    {
        "embed": List[str],
    },
    total=False,
)

class GetResourceRequestRequestTypeDef(
    _RequiredGetResourceRequestRequestTypeDef, _OptionalGetResourceRequestRequestTypeDef
):
    pass

_RequiredGetResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredGetResourcesRequestRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalGetResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalGetResourcesRequestRequestTypeDef",
    {
        "position": str,
        "limit": int,
        "embed": List[str],
    },
    total=False,
)

class GetResourcesRequestRequestTypeDef(
    _RequiredGetResourcesRequestRequestTypeDef, _OptionalGetResourcesRequestRequestTypeDef
):
    pass

GetRestApiRequestRequestTypeDef = TypedDict(
    "GetRestApiRequestRequestTypeDef",
    {
        "restApiId": str,
    },
)

GetRestApisRequestRequestTypeDef = TypedDict(
    "GetRestApisRequestRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)

_RequiredGetSdkRequestRequestTypeDef = TypedDict(
    "_RequiredGetSdkRequestRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
        "sdkType": str,
    },
)
_OptionalGetSdkRequestRequestTypeDef = TypedDict(
    "_OptionalGetSdkRequestRequestTypeDef",
    {
        "parameters": Dict[str, str],
    },
    total=False,
)

class GetSdkRequestRequestTypeDef(
    _RequiredGetSdkRequestRequestTypeDef, _OptionalGetSdkRequestRequestTypeDef
):
    pass

GetSdkTypeRequestRequestTypeDef = TypedDict(
    "GetSdkTypeRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetSdkTypesRequestRequestTypeDef = TypedDict(
    "GetSdkTypesRequestRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)

GetStageRequestRequestTypeDef = TypedDict(
    "GetStageRequestRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
    },
)

_RequiredGetStagesRequestRequestTypeDef = TypedDict(
    "_RequiredGetStagesRequestRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalGetStagesRequestRequestTypeDef = TypedDict(
    "_OptionalGetStagesRequestRequestTypeDef",
    {
        "deploymentId": str,
    },
    total=False,
)

class GetStagesRequestRequestTypeDef(
    _RequiredGetStagesRequestRequestTypeDef, _OptionalGetStagesRequestRequestTypeDef
):
    pass

_RequiredGetTagsRequestRequestTypeDef = TypedDict(
    "_RequiredGetTagsRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalGetTagsRequestRequestTypeDef = TypedDict(
    "_OptionalGetTagsRequestRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)

class GetTagsRequestRequestTypeDef(
    _RequiredGetTagsRequestRequestTypeDef, _OptionalGetTagsRequestRequestTypeDef
):
    pass

GetUsagePlanKeyRequestRequestTypeDef = TypedDict(
    "GetUsagePlanKeyRequestRequestTypeDef",
    {
        "usagePlanId": str,
        "keyId": str,
    },
)

_RequiredGetUsagePlanKeysRequestRequestTypeDef = TypedDict(
    "_RequiredGetUsagePlanKeysRequestRequestTypeDef",
    {
        "usagePlanId": str,
    },
)
_OptionalGetUsagePlanKeysRequestRequestTypeDef = TypedDict(
    "_OptionalGetUsagePlanKeysRequestRequestTypeDef",
    {
        "position": str,
        "limit": int,
        "nameQuery": str,
    },
    total=False,
)

class GetUsagePlanKeysRequestRequestTypeDef(
    _RequiredGetUsagePlanKeysRequestRequestTypeDef, _OptionalGetUsagePlanKeysRequestRequestTypeDef
):
    pass

GetUsagePlanRequestRequestTypeDef = TypedDict(
    "GetUsagePlanRequestRequestTypeDef",
    {
        "usagePlanId": str,
    },
)

GetUsagePlansRequestRequestTypeDef = TypedDict(
    "GetUsagePlansRequestRequestTypeDef",
    {
        "position": str,
        "keyId": str,
        "limit": int,
    },
    total=False,
)

_RequiredGetUsageRequestRequestTypeDef = TypedDict(
    "_RequiredGetUsageRequestRequestTypeDef",
    {
        "usagePlanId": str,
        "startDate": str,
        "endDate": str,
    },
)
_OptionalGetUsageRequestRequestTypeDef = TypedDict(
    "_OptionalGetUsageRequestRequestTypeDef",
    {
        "keyId": str,
        "position": str,
        "limit": int,
    },
    total=False,
)

class GetUsageRequestRequestTypeDef(
    _RequiredGetUsageRequestRequestTypeDef, _OptionalGetUsageRequestRequestTypeDef
):
    pass

GetVpcLinkRequestRequestTypeDef = TypedDict(
    "GetVpcLinkRequestRequestTypeDef",
    {
        "vpcLinkId": str,
    },
)

GetVpcLinksRequestRequestTypeDef = TypedDict(
    "GetVpcLinksRequestRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)

_RequiredImportApiKeysRequestRequestTypeDef = TypedDict(
    "_RequiredImportApiKeysRequestRequestTypeDef",
    {
        "body": Union[bytes, IO[bytes], StreamingBody],
        "format": Literal["csv"],
    },
)
_OptionalImportApiKeysRequestRequestTypeDef = TypedDict(
    "_OptionalImportApiKeysRequestRequestTypeDef",
    {
        "failOnWarnings": bool,
    },
    total=False,
)

class ImportApiKeysRequestRequestTypeDef(
    _RequiredImportApiKeysRequestRequestTypeDef, _OptionalImportApiKeysRequestRequestTypeDef
):
    pass

_RequiredImportDocumentationPartsRequestRequestTypeDef = TypedDict(
    "_RequiredImportDocumentationPartsRequestRequestTypeDef",
    {
        "restApiId": str,
        "body": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalImportDocumentationPartsRequestRequestTypeDef = TypedDict(
    "_OptionalImportDocumentationPartsRequestRequestTypeDef",
    {
        "mode": PutModeType,
        "failOnWarnings": bool,
    },
    total=False,
)

class ImportDocumentationPartsRequestRequestTypeDef(
    _RequiredImportDocumentationPartsRequestRequestTypeDef,
    _OptionalImportDocumentationPartsRequestRequestTypeDef,
):
    pass

_RequiredImportRestApiRequestRequestTypeDef = TypedDict(
    "_RequiredImportRestApiRequestRequestTypeDef",
    {
        "body": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalImportRestApiRequestRequestTypeDef = TypedDict(
    "_OptionalImportRestApiRequestRequestTypeDef",
    {
        "failOnWarnings": bool,
        "parameters": Dict[str, str],
    },
    total=False,
)

class ImportRestApiRequestRequestTypeDef(
    _RequiredImportRestApiRequestRequestTypeDef, _OptionalImportRestApiRequestRequestTypeDef
):
    pass

IntegrationResponseMetadataTypeDef = TypedDict(
    "IntegrationResponseMetadataTypeDef",
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
        "integrationResponses": Dict[str, "IntegrationResponseTypeDef"],
        "tlsConfig": "TlsConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IntegrationResponseResponseMetadataTypeDef = TypedDict(
    "IntegrationResponseResponseMetadataTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": ContentHandlingStrategyType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IntegrationResponseTypeDef = TypedDict(
    "IntegrationResponseTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": ContentHandlingStrategyType,
    },
    total=False,
)

IntegrationTypeDef = TypedDict(
    "IntegrationTypeDef",
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
        "integrationResponses": Dict[str, "IntegrationResponseTypeDef"],
        "tlsConfig": "TlsConfigTypeDef",
    },
    total=False,
)

MethodResponseMetadataTypeDef = TypedDict(
    "MethodResponseMetadataTypeDef",
    {
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": str,
        "apiKeyRequired": bool,
        "requestValidatorId": str,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "methodResponses": Dict[str, "MethodResponseTypeDef"],
        "methodIntegration": "IntegrationTypeDef",
        "authorizationScopes": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MethodResponseResponseMetadataTypeDef = TypedDict(
    "MethodResponseResponseMetadataTypeDef",
    {
        "statusCode": str,
        "responseParameters": Dict[str, bool],
        "responseModels": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MethodResponseTypeDef = TypedDict(
    "MethodResponseTypeDef",
    {
        "statusCode": str,
        "responseParameters": Dict[str, bool],
        "responseModels": Dict[str, str],
    },
    total=False,
)

MethodSettingTypeDef = TypedDict(
    "MethodSettingTypeDef",
    {
        "metricsEnabled": bool,
        "loggingLevel": str,
        "dataTraceEnabled": bool,
        "throttlingBurstLimit": int,
        "throttlingRateLimit": float,
        "cachingEnabled": bool,
        "cacheTtlInSeconds": int,
        "cacheDataEncrypted": bool,
        "requireAuthorizationForCacheControl": bool,
        "unauthorizedCacheControlHeaderStrategy": UnauthorizedCacheControlHeaderStrategyType,
    },
    total=False,
)

MethodSnapshotTypeDef = TypedDict(
    "MethodSnapshotTypeDef",
    {
        "authorizationType": str,
        "apiKeyRequired": bool,
    },
    total=False,
)

MethodTypeDef = TypedDict(
    "MethodTypeDef",
    {
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": str,
        "apiKeyRequired": bool,
        "requestValidatorId": str,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "methodResponses": Dict[str, "MethodResponseTypeDef"],
        "methodIntegration": "IntegrationTypeDef",
        "authorizationScopes": List[str],
    },
    total=False,
)

ModelResponseMetadataTypeDef = TypedDict(
    "ModelResponseMetadataTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "schema": str,
        "contentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "schema": str,
        "contentType": str,
    },
    total=False,
)

ModelsTypeDef = TypedDict(
    "ModelsTypeDef",
    {
        "position": str,
        "items": List["ModelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MutualTlsAuthenticationInputTypeDef = TypedDict(
    "MutualTlsAuthenticationInputTypeDef",
    {
        "truststoreUri": str,
        "truststoreVersion": str,
    },
    total=False,
)

MutualTlsAuthenticationTypeDef = TypedDict(
    "MutualTlsAuthenticationTypeDef",
    {
        "truststoreUri": str,
        "truststoreVersion": str,
        "truststoreWarnings": List[str],
    },
    total=False,
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

PatchOperationTypeDef = TypedDict(
    "PatchOperationTypeDef",
    {
        "op": OpType,
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

_RequiredPutGatewayResponseRequestRequestTypeDef = TypedDict(
    "_RequiredPutGatewayResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "responseType": GatewayResponseTypeType,
    },
)
_OptionalPutGatewayResponseRequestRequestTypeDef = TypedDict(
    "_OptionalPutGatewayResponseRequestRequestTypeDef",
    {
        "statusCode": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
    },
    total=False,
)

class PutGatewayResponseRequestRequestTypeDef(
    _RequiredPutGatewayResponseRequestRequestTypeDef,
    _OptionalPutGatewayResponseRequestRequestTypeDef,
):
    pass

_RequiredPutIntegrationRequestRequestTypeDef = TypedDict(
    "_RequiredPutIntegrationRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "type": IntegrationTypeType,
    },
)
_OptionalPutIntegrationRequestRequestTypeDef = TypedDict(
    "_OptionalPutIntegrationRequestRequestTypeDef",
    {
        "integrationHttpMethod": str,
        "uri": str,
        "connectionType": ConnectionTypeType,
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "contentHandling": ContentHandlingStrategyType,
        "timeoutInMillis": int,
        "tlsConfig": "TlsConfigTypeDef",
    },
    total=False,
)

class PutIntegrationRequestRequestTypeDef(
    _RequiredPutIntegrationRequestRequestTypeDef, _OptionalPutIntegrationRequestRequestTypeDef
):
    pass

_RequiredPutIntegrationResponseRequestRequestTypeDef = TypedDict(
    "_RequiredPutIntegrationResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
    },
)
_OptionalPutIntegrationResponseRequestRequestTypeDef = TypedDict(
    "_OptionalPutIntegrationResponseRequestRequestTypeDef",
    {
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": ContentHandlingStrategyType,
    },
    total=False,
)

class PutIntegrationResponseRequestRequestTypeDef(
    _RequiredPutIntegrationResponseRequestRequestTypeDef,
    _OptionalPutIntegrationResponseRequestRequestTypeDef,
):
    pass

_RequiredPutMethodRequestRequestTypeDef = TypedDict(
    "_RequiredPutMethodRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "authorizationType": str,
    },
)
_OptionalPutMethodRequestRequestTypeDef = TypedDict(
    "_OptionalPutMethodRequestRequestTypeDef",
    {
        "authorizerId": str,
        "apiKeyRequired": bool,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "requestValidatorId": str,
        "authorizationScopes": List[str],
    },
    total=False,
)

class PutMethodRequestRequestTypeDef(
    _RequiredPutMethodRequestRequestTypeDef, _OptionalPutMethodRequestRequestTypeDef
):
    pass

_RequiredPutMethodResponseRequestRequestTypeDef = TypedDict(
    "_RequiredPutMethodResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
    },
)
_OptionalPutMethodResponseRequestRequestTypeDef = TypedDict(
    "_OptionalPutMethodResponseRequestRequestTypeDef",
    {
        "responseParameters": Dict[str, bool],
        "responseModels": Dict[str, str],
    },
    total=False,
)

class PutMethodResponseRequestRequestTypeDef(
    _RequiredPutMethodResponseRequestRequestTypeDef, _OptionalPutMethodResponseRequestRequestTypeDef
):
    pass

_RequiredPutRestApiRequestRequestTypeDef = TypedDict(
    "_RequiredPutRestApiRequestRequestTypeDef",
    {
        "restApiId": str,
        "body": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalPutRestApiRequestRequestTypeDef = TypedDict(
    "_OptionalPutRestApiRequestRequestTypeDef",
    {
        "mode": PutModeType,
        "failOnWarnings": bool,
        "parameters": Dict[str, str],
    },
    total=False,
)

class PutRestApiRequestRequestTypeDef(
    _RequiredPutRestApiRequestRequestTypeDef, _OptionalPutRestApiRequestRequestTypeDef
):
    pass

QuotaSettingsTypeDef = TypedDict(
    "QuotaSettingsTypeDef",
    {
        "limit": int,
        "offset": int,
        "period": QuotaPeriodTypeType,
    },
    total=False,
)

RequestValidatorResponseMetadataTypeDef = TypedDict(
    "RequestValidatorResponseMetadataTypeDef",
    {
        "id": str,
        "name": str,
        "validateRequestBody": bool,
        "validateRequestParameters": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequestValidatorTypeDef = TypedDict(
    "RequestValidatorTypeDef",
    {
        "id": str,
        "name": str,
        "validateRequestBody": bool,
        "validateRequestParameters": bool,
    },
    total=False,
)

RequestValidatorsTypeDef = TypedDict(
    "RequestValidatorsTypeDef",
    {
        "position": str,
        "items": List["RequestValidatorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceResponseMetadataTypeDef = TypedDict(
    "ResourceResponseMetadataTypeDef",
    {
        "id": str,
        "parentId": str,
        "pathPart": str,
        "path": str,
        "resourceMethods": Dict[str, "MethodTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "id": str,
        "parentId": str,
        "pathPart": str,
        "path": str,
        "resourceMethods": Dict[str, "MethodTypeDef"],
    },
    total=False,
)

ResourcesTypeDef = TypedDict(
    "ResourcesTypeDef",
    {
        "position": str,
        "items": List["ResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

RestApiResponseMetadataTypeDef = TypedDict(
    "RestApiResponseMetadataTypeDef",
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
        "endpointConfiguration": "EndpointConfigurationTypeDef",
        "policy": str,
        "tags": Dict[str, str],
        "disableExecuteApiEndpoint": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestApiTypeDef = TypedDict(
    "RestApiTypeDef",
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
        "endpointConfiguration": "EndpointConfigurationTypeDef",
        "policy": str,
        "tags": Dict[str, str],
        "disableExecuteApiEndpoint": bool,
    },
    total=False,
)

RestApisTypeDef = TypedDict(
    "RestApisTypeDef",
    {
        "position": str,
        "items": List["RestApiTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SdkConfigurationPropertyTypeDef = TypedDict(
    "SdkConfigurationPropertyTypeDef",
    {
        "name": str,
        "friendlyName": str,
        "description": str,
        "required": bool,
        "defaultValue": str,
    },
    total=False,
)

SdkResponseTypeDef = TypedDict(
    "SdkResponseTypeDef",
    {
        "contentType": str,
        "contentDisposition": str,
        "body": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SdkTypeResponseMetadataTypeDef = TypedDict(
    "SdkTypeResponseMetadataTypeDef",
    {
        "id": str,
        "friendlyName": str,
        "description": str,
        "configurationProperties": List["SdkConfigurationPropertyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SdkTypeTypeDef = TypedDict(
    "SdkTypeTypeDef",
    {
        "id": str,
        "friendlyName": str,
        "description": str,
        "configurationProperties": List["SdkConfigurationPropertyTypeDef"],
    },
    total=False,
)

SdkTypesTypeDef = TypedDict(
    "SdkTypesTypeDef",
    {
        "position": str,
        "items": List["SdkTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StageKeyTypeDef = TypedDict(
    "StageKeyTypeDef",
    {
        "restApiId": str,
        "stageName": str,
    },
    total=False,
)

StageResponseMetadataTypeDef = TypedDict(
    "StageResponseMetadataTypeDef",
    {
        "deploymentId": str,
        "clientCertificateId": str,
        "stageName": str,
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": CacheClusterSizeType,
        "cacheClusterStatus": CacheClusterStatusType,
        "methodSettings": Dict[str, "MethodSettingTypeDef"],
        "variables": Dict[str, str],
        "documentationVersion": str,
        "accessLogSettings": "AccessLogSettingsTypeDef",
        "canarySettings": "CanarySettingsTypeDef",
        "tracingEnabled": bool,
        "webAclArn": str,
        "tags": Dict[str, str],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StageTypeDef = TypedDict(
    "StageTypeDef",
    {
        "deploymentId": str,
        "clientCertificateId": str,
        "stageName": str,
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": CacheClusterSizeType,
        "cacheClusterStatus": CacheClusterStatusType,
        "methodSettings": Dict[str, "MethodSettingTypeDef"],
        "variables": Dict[str, str],
        "documentationVersion": str,
        "accessLogSettings": "AccessLogSettingsTypeDef",
        "canarySettings": "CanarySettingsTypeDef",
        "tracingEnabled": bool,
        "webAclArn": str,
        "tags": Dict[str, str],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
    },
    total=False,
)

StagesTypeDef = TypedDict(
    "StagesTypeDef",
    {
        "item": List["StageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TagsTypeDef = TypedDict(
    "TagsTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "value": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTestInvokeAuthorizerRequestRequestTypeDef = TypedDict(
    "_RequiredTestInvokeAuthorizerRequestRequestTypeDef",
    {
        "restApiId": str,
        "authorizerId": str,
    },
)
_OptionalTestInvokeAuthorizerRequestRequestTypeDef = TypedDict(
    "_OptionalTestInvokeAuthorizerRequestRequestTypeDef",
    {
        "headers": Dict[str, str],
        "multiValueHeaders": Dict[str, List[str]],
        "pathWithQueryString": str,
        "body": str,
        "stageVariables": Dict[str, str],
        "additionalContext": Dict[str, str],
    },
    total=False,
)

class TestInvokeAuthorizerRequestRequestTypeDef(
    _RequiredTestInvokeAuthorizerRequestRequestTypeDef,
    _OptionalTestInvokeAuthorizerRequestRequestTypeDef,
):
    pass

TestInvokeAuthorizerResponseTypeDef = TypedDict(
    "TestInvokeAuthorizerResponseTypeDef",
    {
        "clientStatus": int,
        "log": str,
        "latency": int,
        "principalId": str,
        "policy": str,
        "authorization": Dict[str, List[str]],
        "claims": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTestInvokeMethodRequestRequestTypeDef = TypedDict(
    "_RequiredTestInvokeMethodRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
    },
)
_OptionalTestInvokeMethodRequestRequestTypeDef = TypedDict(
    "_OptionalTestInvokeMethodRequestRequestTypeDef",
    {
        "pathWithQueryString": str,
        "body": str,
        "headers": Dict[str, str],
        "multiValueHeaders": Dict[str, List[str]],
        "clientCertificateId": str,
        "stageVariables": Dict[str, str],
    },
    total=False,
)

class TestInvokeMethodRequestRequestTypeDef(
    _RequiredTestInvokeMethodRequestRequestTypeDef, _OptionalTestInvokeMethodRequestRequestTypeDef
):
    pass

TestInvokeMethodResponseTypeDef = TypedDict(
    "TestInvokeMethodResponseTypeDef",
    {
        "status": int,
        "body": str,
        "headers": Dict[str, str],
        "multiValueHeaders": Dict[str, List[str]],
        "log": str,
        "latency": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ThrottleSettingsTypeDef = TypedDict(
    "ThrottleSettingsTypeDef",
    {
        "burstLimit": int,
        "rateLimit": float,
    },
    total=False,
)

TlsConfigTypeDef = TypedDict(
    "TlsConfigTypeDef",
    {
        "insecureSkipVerification": bool,
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

UpdateAccountRequestRequestTypeDef = TypedDict(
    "UpdateAccountRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

_RequiredUpdateApiKeyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApiKeyRequestRequestTypeDef",
    {
        "apiKey": str,
    },
)
_OptionalUpdateApiKeyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApiKeyRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateApiKeyRequestRequestTypeDef(
    _RequiredUpdateApiKeyRequestRequestTypeDef, _OptionalUpdateApiKeyRequestRequestTypeDef
):
    pass

_RequiredUpdateAuthorizerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAuthorizerRequestRequestTypeDef",
    {
        "restApiId": str,
        "authorizerId": str,
    },
)
_OptionalUpdateAuthorizerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAuthorizerRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateAuthorizerRequestRequestTypeDef(
    _RequiredUpdateAuthorizerRequestRequestTypeDef, _OptionalUpdateAuthorizerRequestRequestTypeDef
):
    pass

_RequiredUpdateBasePathMappingRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBasePathMappingRequestRequestTypeDef",
    {
        "domainName": str,
        "basePath": str,
    },
)
_OptionalUpdateBasePathMappingRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBasePathMappingRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateBasePathMappingRequestRequestTypeDef(
    _RequiredUpdateBasePathMappingRequestRequestTypeDef,
    _OptionalUpdateBasePathMappingRequestRequestTypeDef,
):
    pass

_RequiredUpdateClientCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateClientCertificateRequestRequestTypeDef",
    {
        "clientCertificateId": str,
    },
)
_OptionalUpdateClientCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateClientCertificateRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateClientCertificateRequestRequestTypeDef(
    _RequiredUpdateClientCertificateRequestRequestTypeDef,
    _OptionalUpdateClientCertificateRequestRequestTypeDef,
):
    pass

_RequiredUpdateDeploymentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDeploymentRequestRequestTypeDef",
    {
        "restApiId": str,
        "deploymentId": str,
    },
)
_OptionalUpdateDeploymentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDeploymentRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateDeploymentRequestRequestTypeDef(
    _RequiredUpdateDeploymentRequestRequestTypeDef, _OptionalUpdateDeploymentRequestRequestTypeDef
):
    pass

_RequiredUpdateDocumentationPartRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDocumentationPartRequestRequestTypeDef",
    {
        "restApiId": str,
        "documentationPartId": str,
    },
)
_OptionalUpdateDocumentationPartRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDocumentationPartRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateDocumentationPartRequestRequestTypeDef(
    _RequiredUpdateDocumentationPartRequestRequestTypeDef,
    _OptionalUpdateDocumentationPartRequestRequestTypeDef,
):
    pass

_RequiredUpdateDocumentationVersionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDocumentationVersionRequestRequestTypeDef",
    {
        "restApiId": str,
        "documentationVersion": str,
    },
)
_OptionalUpdateDocumentationVersionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDocumentationVersionRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateDocumentationVersionRequestRequestTypeDef(
    _RequiredUpdateDocumentationVersionRequestRequestTypeDef,
    _OptionalUpdateDocumentationVersionRequestRequestTypeDef,
):
    pass

_RequiredUpdateDomainNameRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainNameRequestRequestTypeDef",
    {
        "domainName": str,
    },
)
_OptionalUpdateDomainNameRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainNameRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateDomainNameRequestRequestTypeDef(
    _RequiredUpdateDomainNameRequestRequestTypeDef, _OptionalUpdateDomainNameRequestRequestTypeDef
):
    pass

_RequiredUpdateGatewayResponseRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateGatewayResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "responseType": GatewayResponseTypeType,
    },
)
_OptionalUpdateGatewayResponseRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateGatewayResponseRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateGatewayResponseRequestRequestTypeDef(
    _RequiredUpdateGatewayResponseRequestRequestTypeDef,
    _OptionalUpdateGatewayResponseRequestRequestTypeDef,
):
    pass

_RequiredUpdateIntegrationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIntegrationRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
    },
)
_OptionalUpdateIntegrationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIntegrationRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateIntegrationRequestRequestTypeDef(
    _RequiredUpdateIntegrationRequestRequestTypeDef, _OptionalUpdateIntegrationRequestRequestTypeDef
):
    pass

_RequiredUpdateIntegrationResponseRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIntegrationResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
    },
)
_OptionalUpdateIntegrationResponseRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIntegrationResponseRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateIntegrationResponseRequestRequestTypeDef(
    _RequiredUpdateIntegrationResponseRequestRequestTypeDef,
    _OptionalUpdateIntegrationResponseRequestRequestTypeDef,
):
    pass

_RequiredUpdateMethodRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMethodRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
    },
)
_OptionalUpdateMethodRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMethodRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateMethodRequestRequestTypeDef(
    _RequiredUpdateMethodRequestRequestTypeDef, _OptionalUpdateMethodRequestRequestTypeDef
):
    pass

_RequiredUpdateMethodResponseRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMethodResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
    },
)
_OptionalUpdateMethodResponseRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMethodResponseRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateMethodResponseRequestRequestTypeDef(
    _RequiredUpdateMethodResponseRequestRequestTypeDef,
    _OptionalUpdateMethodResponseRequestRequestTypeDef,
):
    pass

_RequiredUpdateModelRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateModelRequestRequestTypeDef",
    {
        "restApiId": str,
        "modelName": str,
    },
)
_OptionalUpdateModelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateModelRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateModelRequestRequestTypeDef(
    _RequiredUpdateModelRequestRequestTypeDef, _OptionalUpdateModelRequestRequestTypeDef
):
    pass

_RequiredUpdateRequestValidatorRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRequestValidatorRequestRequestTypeDef",
    {
        "restApiId": str,
        "requestValidatorId": str,
    },
)
_OptionalUpdateRequestValidatorRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRequestValidatorRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateRequestValidatorRequestRequestTypeDef(
    _RequiredUpdateRequestValidatorRequestRequestTypeDef,
    _OptionalUpdateRequestValidatorRequestRequestTypeDef,
):
    pass

_RequiredUpdateResourceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateResourceRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
    },
)
_OptionalUpdateResourceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateResourceRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateResourceRequestRequestTypeDef(
    _RequiredUpdateResourceRequestRequestTypeDef, _OptionalUpdateResourceRequestRequestTypeDef
):
    pass

_RequiredUpdateRestApiRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRestApiRequestRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalUpdateRestApiRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRestApiRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateRestApiRequestRequestTypeDef(
    _RequiredUpdateRestApiRequestRequestTypeDef, _OptionalUpdateRestApiRequestRequestTypeDef
):
    pass

_RequiredUpdateStageRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStageRequestRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
    },
)
_OptionalUpdateStageRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStageRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateStageRequestRequestTypeDef(
    _RequiredUpdateStageRequestRequestTypeDef, _OptionalUpdateStageRequestRequestTypeDef
):
    pass

_RequiredUpdateUsagePlanRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUsagePlanRequestRequestTypeDef",
    {
        "usagePlanId": str,
    },
)
_OptionalUpdateUsagePlanRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUsagePlanRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateUsagePlanRequestRequestTypeDef(
    _RequiredUpdateUsagePlanRequestRequestTypeDef, _OptionalUpdateUsagePlanRequestRequestTypeDef
):
    pass

_RequiredUpdateUsageRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUsageRequestRequestTypeDef",
    {
        "usagePlanId": str,
        "keyId": str,
    },
)
_OptionalUpdateUsageRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUsageRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateUsageRequestRequestTypeDef(
    _RequiredUpdateUsageRequestRequestTypeDef, _OptionalUpdateUsageRequestRequestTypeDef
):
    pass

_RequiredUpdateVpcLinkRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateVpcLinkRequestRequestTypeDef",
    {
        "vpcLinkId": str,
    },
)
_OptionalUpdateVpcLinkRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateVpcLinkRequestRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

class UpdateVpcLinkRequestRequestTypeDef(
    _RequiredUpdateVpcLinkRequestRequestTypeDef, _OptionalUpdateVpcLinkRequestRequestTypeDef
):
    pass

UsagePlanKeyResponseMetadataTypeDef = TypedDict(
    "UsagePlanKeyResponseMetadataTypeDef",
    {
        "id": str,
        "type": str,
        "value": str,
        "name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsagePlanKeyTypeDef = TypedDict(
    "UsagePlanKeyTypeDef",
    {
        "id": str,
        "type": str,
        "value": str,
        "name": str,
    },
    total=False,
)

UsagePlanKeysTypeDef = TypedDict(
    "UsagePlanKeysTypeDef",
    {
        "position": str,
        "items": List["UsagePlanKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsagePlanResponseMetadataTypeDef = TypedDict(
    "UsagePlanResponseMetadataTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "apiStages": List["ApiStageTypeDef"],
        "throttle": "ThrottleSettingsTypeDef",
        "quota": "QuotaSettingsTypeDef",
        "productCode": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsagePlanTypeDef = TypedDict(
    "UsagePlanTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "apiStages": List["ApiStageTypeDef"],
        "throttle": "ThrottleSettingsTypeDef",
        "quota": "QuotaSettingsTypeDef",
        "productCode": str,
        "tags": Dict[str, str],
    },
    total=False,
)

UsagePlansTypeDef = TypedDict(
    "UsagePlansTypeDef",
    {
        "position": str,
        "items": List["UsagePlanTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsageTypeDef = TypedDict(
    "UsageTypeDef",
    {
        "usagePlanId": str,
        "startDate": str,
        "endDate": str,
        "position": str,
        "items": Dict[str, List[List[int]]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcLinkResponseMetadataTypeDef = TypedDict(
    "VpcLinkResponseMetadataTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "targetArns": List[str],
        "status": VpcLinkStatusType,
        "statusMessage": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcLinkTypeDef = TypedDict(
    "VpcLinkTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "targetArns": List[str],
        "status": VpcLinkStatusType,
        "statusMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)

VpcLinksTypeDef = TypedDict(
    "VpcLinksTypeDef",
    {
        "position": str,
        "items": List["VpcLinkTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
