"""
Main interface for apigateway service type definitions.

Usage::

    ```python
    from mypy_boto3_apigateway.type_defs import AccessLogSettingsTypeDef

    data: AccessLogSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

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
    "ApiKeyTypeDef",
    "ApiStageTypeDef",
    "AuthorizerTypeDef",
    "BasePathMappingTypeDef",
    "CanarySettingsTypeDef",
    "ClientCertificateTypeDef",
    "DeploymentTypeDef",
    "DocumentationPartLocationTypeDef",
    "DocumentationPartTypeDef",
    "DocumentationVersionTypeDef",
    "DomainNameTypeDef",
    "EndpointConfigurationTypeDef",
    "GatewayResponseTypeDef",
    "IntegrationResponseTypeDef",
    "IntegrationTypeDef",
    "MethodResponseTypeDef",
    "MethodSettingTypeDef",
    "MethodSnapshotTypeDef",
    "MethodTypeDef",
    "ModelTypeDef",
    "MutualTlsAuthenticationTypeDef",
    "QuotaSettingsTypeDef",
    "RequestValidatorTypeDef",
    "ResourceTypeDef",
    "RestApiTypeDef",
    "SdkConfigurationPropertyTypeDef",
    "SdkTypeTypeDef",
    "StageTypeDef",
    "ThrottleSettingsTypeDef",
    "TlsConfigTypeDef",
    "UsagePlanKeyTypeDef",
    "UsagePlanTypeDef",
    "VpcLinkTypeDef",
    "AccountTypeDef",
    "ApiKeyIdsTypeDef",
    "ApiKeysTypeDef",
    "AuthorizersTypeDef",
    "BasePathMappingsTypeDef",
    "ClientCertificatesTypeDef",
    "DeploymentCanarySettingsTypeDef",
    "DeploymentsTypeDef",
    "DocumentationPartIdsTypeDef",
    "DocumentationPartsTypeDef",
    "DocumentationVersionsTypeDef",
    "DomainNamesTypeDef",
    "ExportResponseTypeDef",
    "GatewayResponsesTypeDef",
    "ModelsTypeDef",
    "MutualTlsAuthenticationInputTypeDef",
    "PaginatorConfigTypeDef",
    "PatchOperationTypeDef",
    "RequestValidatorsTypeDef",
    "ResourcesTypeDef",
    "RestApisTypeDef",
    "SdkResponseTypeDef",
    "SdkTypesTypeDef",
    "StageKeyTypeDef",
    "StagesTypeDef",
    "TagsTypeDef",
    "TemplateTypeDef",
    "TestInvokeAuthorizerResponseTypeDef",
    "TestInvokeMethodResponseTypeDef",
    "UsagePlanKeysTypeDef",
    "UsagePlansTypeDef",
    "UsageTypeDef",
    "VpcLinksTypeDef",
)

AccessLogSettingsTypeDef = TypedDict(
    "AccessLogSettingsTypeDef", {"format": str, "destinationArn": str}, total=False
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

ApiStageTypeDef = TypedDict(
    "ApiStageTypeDef",
    {"apiId": str, "stage": str, "throttle": Dict[str, "ThrottleSettingsTypeDef"]},
    total=False,
)

AuthorizerTypeDef = TypedDict(
    "AuthorizerTypeDef",
    {
        "id": str,
        "name": str,
        "type": Literal["TOKEN", "REQUEST", "COGNITO_USER_POOLS"],
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

BasePathMappingTypeDef = TypedDict(
    "BasePathMappingTypeDef", {"basePath": str, "restApiId": str, "stage": str}, total=False
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

_RequiredDocumentationPartLocationTypeDef = TypedDict(
    "_RequiredDocumentationPartLocationTypeDef",
    {
        "type": Literal[
            "API",
            "AUTHORIZER",
            "MODEL",
            "RESOURCE",
            "METHOD",
            "PATH_PARAMETER",
            "QUERY_PARAMETER",
            "REQUEST_HEADER",
            "REQUEST_BODY",
            "RESPONSE",
            "RESPONSE_HEADER",
            "RESPONSE_BODY",
        ]
    },
)
_OptionalDocumentationPartLocationTypeDef = TypedDict(
    "_OptionalDocumentationPartLocationTypeDef",
    {"path": str, "method": str, "statusCode": str, "name": str},
    total=False,
)


class DocumentationPartLocationTypeDef(
    _RequiredDocumentationPartLocationTypeDef, _OptionalDocumentationPartLocationTypeDef
):
    pass


DocumentationPartTypeDef = TypedDict(
    "DocumentationPartTypeDef",
    {"id": str, "location": "DocumentationPartLocationTypeDef", "properties": str},
    total=False,
)

DocumentationVersionTypeDef = TypedDict(
    "DocumentationVersionTypeDef",
    {"version": str, "createdDate": datetime, "description": str},
    total=False,
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
        "domainNameStatus": Literal["AVAILABLE", "UPDATING", "PENDING"],
        "domainNameStatusMessage": str,
        "securityPolicy": Literal["TLS_1_0", "TLS_1_2"],
        "tags": Dict[str, str],
        "mutualTlsAuthentication": "MutualTlsAuthenticationTypeDef",
    },
    total=False,
)

EndpointConfigurationTypeDef = TypedDict(
    "EndpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)

GatewayResponseTypeDef = TypedDict(
    "GatewayResponseTypeDef",
    {
        "responseType": Literal[
            "DEFAULT_4XX",
            "DEFAULT_5XX",
            "RESOURCE_NOT_FOUND",
            "UNAUTHORIZED",
            "INVALID_API_KEY",
            "ACCESS_DENIED",
            "AUTHORIZER_FAILURE",
            "AUTHORIZER_CONFIGURATION_ERROR",
            "INVALID_SIGNATURE",
            "EXPIRED_TOKEN",
            "MISSING_AUTHENTICATION_TOKEN",
            "INTEGRATION_FAILURE",
            "INTEGRATION_TIMEOUT",
            "API_CONFIGURATION_ERROR",
            "UNSUPPORTED_MEDIA_TYPE",
            "BAD_REQUEST_PARAMETERS",
            "BAD_REQUEST_BODY",
            "REQUEST_TOO_LARGE",
            "THROTTLED",
            "QUOTA_EXCEEDED",
        ],
        "statusCode": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "defaultResponse": bool,
    },
    total=False,
)

IntegrationResponseTypeDef = TypedDict(
    "IntegrationResponseTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)

IntegrationTypeDef = TypedDict(
    "IntegrationTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[str, "IntegrationResponseTypeDef"],
        "tlsConfig": "TlsConfigTypeDef",
    },
    total=False,
)

MethodResponseTypeDef = TypedDict(
    "MethodResponseTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
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
        "unauthorizedCacheControlHeaderStrategy": Literal[
            "FAIL_WITH_403", "SUCCEED_WITH_RESPONSE_HEADER", "SUCCEED_WITHOUT_RESPONSE_HEADER"
        ],
    },
    total=False,
)

MethodSnapshotTypeDef = TypedDict(
    "MethodSnapshotTypeDef", {"authorizationType": str, "apiKeyRequired": bool}, total=False
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

ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {"id": str, "name": str, "description": str, "schema": str, "contentType": str},
    total=False,
)

MutualTlsAuthenticationTypeDef = TypedDict(
    "MutualTlsAuthenticationTypeDef",
    {"truststoreUri": str, "truststoreVersion": str, "truststoreWarnings": List[str]},
    total=False,
)

QuotaSettingsTypeDef = TypedDict(
    "QuotaSettingsTypeDef",
    {"limit": int, "offset": int, "period": Literal["DAY", "WEEK", "MONTH"]},
    total=False,
)

RequestValidatorTypeDef = TypedDict(
    "RequestValidatorTypeDef",
    {"id": str, "name": str, "validateRequestBody": bool, "validateRequestParameters": bool},
    total=False,
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
        "apiKeySource": Literal["HEADER", "AUTHORIZER"],
        "endpointConfiguration": "EndpointConfigurationTypeDef",
        "policy": str,
        "tags": Dict[str, str],
        "disableExecuteApiEndpoint": bool,
    },
    total=False,
)

SdkConfigurationPropertyTypeDef = TypedDict(
    "SdkConfigurationPropertyTypeDef",
    {"name": str, "friendlyName": str, "description": str, "required": bool, "defaultValue": str},
    total=False,
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

StageTypeDef = TypedDict(
    "StageTypeDef",
    {
        "deploymentId": str,
        "clientCertificateId": str,
        "stageName": str,
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": Literal["0.5", "1.6", "6.1", "13.5", "28.4", "58.2", "118", "237"],
        "cacheClusterStatus": Literal[
            "CREATE_IN_PROGRESS",
            "AVAILABLE",
            "DELETE_IN_PROGRESS",
            "NOT_AVAILABLE",
            "FLUSH_IN_PROGRESS",
        ],
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

ThrottleSettingsTypeDef = TypedDict(
    "ThrottleSettingsTypeDef", {"burstLimit": int, "rateLimit": float}, total=False
)

TlsConfigTypeDef = TypedDict("TlsConfigTypeDef", {"insecureSkipVerification": bool}, total=False)

UsagePlanKeyTypeDef = TypedDict(
    "UsagePlanKeyTypeDef", {"id": str, "type": str, "value": str, "name": str}, total=False
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

VpcLinkTypeDef = TypedDict(
    "VpcLinkTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "targetArns": List[str],
        "status": Literal["AVAILABLE", "PENDING", "DELETING", "FAILED"],
        "statusMessage": str,
        "tags": Dict[str, str],
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
    },
    total=False,
)

ApiKeyIdsTypeDef = TypedDict(
    "ApiKeyIdsTypeDef", {"ids": List[str], "warnings": List[str]}, total=False
)

ApiKeysTypeDef = TypedDict(
    "ApiKeysTypeDef",
    {"warnings": List[str], "position": str, "items": List["ApiKeyTypeDef"]},
    total=False,
)

AuthorizersTypeDef = TypedDict(
    "AuthorizersTypeDef", {"position": str, "items": List["AuthorizerTypeDef"]}, total=False
)

BasePathMappingsTypeDef = TypedDict(
    "BasePathMappingsTypeDef",
    {"position": str, "items": List["BasePathMappingTypeDef"]},
    total=False,
)

ClientCertificatesTypeDef = TypedDict(
    "ClientCertificatesTypeDef",
    {"position": str, "items": List["ClientCertificateTypeDef"]},
    total=False,
)

DeploymentCanarySettingsTypeDef = TypedDict(
    "DeploymentCanarySettingsTypeDef",
    {"percentTraffic": float, "stageVariableOverrides": Dict[str, str], "useStageCache": bool},
    total=False,
)

DeploymentsTypeDef = TypedDict(
    "DeploymentsTypeDef", {"position": str, "items": List["DeploymentTypeDef"]}, total=False
)

DocumentationPartIdsTypeDef = TypedDict(
    "DocumentationPartIdsTypeDef", {"ids": List[str], "warnings": List[str]}, total=False
)

DocumentationPartsTypeDef = TypedDict(
    "DocumentationPartsTypeDef",
    {"position": str, "items": List["DocumentationPartTypeDef"]},
    total=False,
)

DocumentationVersionsTypeDef = TypedDict(
    "DocumentationVersionsTypeDef",
    {"position": str, "items": List["DocumentationVersionTypeDef"]},
    total=False,
)

DomainNamesTypeDef = TypedDict(
    "DomainNamesTypeDef", {"position": str, "items": List["DomainNameTypeDef"]}, total=False
)

ExportResponseTypeDef = TypedDict(
    "ExportResponseTypeDef",
    {"contentType": str, "contentDisposition": str, "body": Union[bytes, IO[bytes]]},
    total=False,
)

GatewayResponsesTypeDef = TypedDict(
    "GatewayResponsesTypeDef",
    {"position": str, "items": List["GatewayResponseTypeDef"]},
    total=False,
)

ModelsTypeDef = TypedDict(
    "ModelsTypeDef", {"position": str, "items": List["ModelTypeDef"]}, total=False
)

MutualTlsAuthenticationInputTypeDef = TypedDict(
    "MutualTlsAuthenticationInputTypeDef",
    {"truststoreUri": str, "truststoreVersion": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PatchOperationTypeDef = TypedDict(
    "PatchOperationTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

RequestValidatorsTypeDef = TypedDict(
    "RequestValidatorsTypeDef",
    {"position": str, "items": List["RequestValidatorTypeDef"]},
    total=False,
)

ResourcesTypeDef = TypedDict(
    "ResourcesTypeDef", {"position": str, "items": List["ResourceTypeDef"]}, total=False
)

RestApisTypeDef = TypedDict(
    "RestApisTypeDef", {"position": str, "items": List["RestApiTypeDef"]}, total=False
)

SdkResponseTypeDef = TypedDict(
    "SdkResponseTypeDef",
    {"contentType": str, "contentDisposition": str, "body": Union[bytes, IO[bytes]]},
    total=False,
)

SdkTypesTypeDef = TypedDict(
    "SdkTypesTypeDef", {"position": str, "items": List["SdkTypeTypeDef"]}, total=False
)

StageKeyTypeDef = TypedDict("StageKeyTypeDef", {"restApiId": str, "stageName": str}, total=False)

StagesTypeDef = TypedDict("StagesTypeDef", {"item": List["StageTypeDef"]}, total=False)

TagsTypeDef = TypedDict("TagsTypeDef", {"tags": Dict[str, str]}, total=False)

TemplateTypeDef = TypedDict("TemplateTypeDef", {"value": str}, total=False)

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
    },
    total=False,
)

TestInvokeMethodResponseTypeDef = TypedDict(
    "TestInvokeMethodResponseTypeDef",
    {
        "status": int,
        "body": str,
        "headers": Dict[str, str],
        "multiValueHeaders": Dict[str, List[str]],
        "log": str,
        "latency": int,
    },
    total=False,
)

UsagePlanKeysTypeDef = TypedDict(
    "UsagePlanKeysTypeDef", {"position": str, "items": List["UsagePlanKeyTypeDef"]}, total=False
)

UsagePlansTypeDef = TypedDict(
    "UsagePlansTypeDef", {"position": str, "items": List["UsagePlanTypeDef"]}, total=False
)

UsageTypeDef = TypedDict(
    "UsageTypeDef",
    {
        "usagePlanId": str,
        "startDate": str,
        "endDate": str,
        "position": str,
        "items": Dict[str, List[List[int]]],
    },
    total=False,
)

VpcLinksTypeDef = TypedDict(
    "VpcLinksTypeDef", {"position": str, "items": List["VpcLinkTypeDef"]}, total=False
)
