"""
Type annotations for apigatewayv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_apigatewayv2.type_defs import AccessLogSettingsTypeDef

    data: AccessLogSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AuthorizationTypeType,
    AuthorizerTypeType,
    ConnectionTypeType,
    ContentHandlingStrategyType,
    DeploymentStatusType,
    DomainNameStatusType,
    EndpointTypeType,
    IntegrationTypeType,
    JSONYAMLType,
    LoggingLevelType,
    PassthroughBehaviorType,
    ProtocolTypeType,
    SecurityPolicyType,
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
    "ApiMappingTypeDef",
    "ApiTypeDef",
    "AuthorizerTypeDef",
    "CorsTypeDef",
    "CreateApiMappingRequestRequestTypeDef",
    "CreateApiMappingResponseTypeDef",
    "CreateApiRequestRequestTypeDef",
    "CreateApiResponseTypeDef",
    "CreateAuthorizerRequestRequestTypeDef",
    "CreateAuthorizerResponseTypeDef",
    "CreateDeploymentRequestRequestTypeDef",
    "CreateDeploymentResponseTypeDef",
    "CreateDomainNameRequestRequestTypeDef",
    "CreateDomainNameResponseTypeDef",
    "CreateIntegrationRequestRequestTypeDef",
    "CreateIntegrationResponseRequestRequestTypeDef",
    "CreateIntegrationResponseResponseTypeDef",
    "CreateIntegrationResultTypeDef",
    "CreateModelRequestRequestTypeDef",
    "CreateModelResponseTypeDef",
    "CreateRouteRequestRequestTypeDef",
    "CreateRouteResponseRequestRequestTypeDef",
    "CreateRouteResponseResponseTypeDef",
    "CreateRouteResultTypeDef",
    "CreateStageRequestRequestTypeDef",
    "CreateStageResponseTypeDef",
    "CreateVpcLinkRequestRequestTypeDef",
    "CreateVpcLinkResponseTypeDef",
    "DeleteAccessLogSettingsRequestRequestTypeDef",
    "DeleteApiMappingRequestRequestTypeDef",
    "DeleteApiRequestRequestTypeDef",
    "DeleteAuthorizerRequestRequestTypeDef",
    "DeleteCorsConfigurationRequestRequestTypeDef",
    "DeleteDeploymentRequestRequestTypeDef",
    "DeleteDomainNameRequestRequestTypeDef",
    "DeleteIntegrationRequestRequestTypeDef",
    "DeleteIntegrationResponseRequestRequestTypeDef",
    "DeleteModelRequestRequestTypeDef",
    "DeleteRouteRequestParameterRequestRequestTypeDef",
    "DeleteRouteRequestRequestTypeDef",
    "DeleteRouteResponseRequestRequestTypeDef",
    "DeleteRouteSettingsRequestRequestTypeDef",
    "DeleteStageRequestRequestTypeDef",
    "DeleteVpcLinkRequestRequestTypeDef",
    "DeploymentTypeDef",
    "DomainNameConfigurationTypeDef",
    "DomainNameTypeDef",
    "ExportApiRequestRequestTypeDef",
    "ExportApiResponseTypeDef",
    "GetApiMappingRequestRequestTypeDef",
    "GetApiMappingResponseTypeDef",
    "GetApiMappingsRequestRequestTypeDef",
    "GetApiMappingsResponseTypeDef",
    "GetApiRequestRequestTypeDef",
    "GetApiResponseTypeDef",
    "GetApisRequestRequestTypeDef",
    "GetApisResponseTypeDef",
    "GetAuthorizerRequestRequestTypeDef",
    "GetAuthorizerResponseTypeDef",
    "GetAuthorizersRequestRequestTypeDef",
    "GetAuthorizersResponseTypeDef",
    "GetDeploymentRequestRequestTypeDef",
    "GetDeploymentResponseTypeDef",
    "GetDeploymentsRequestRequestTypeDef",
    "GetDeploymentsResponseTypeDef",
    "GetDomainNameRequestRequestTypeDef",
    "GetDomainNameResponseTypeDef",
    "GetDomainNamesRequestRequestTypeDef",
    "GetDomainNamesResponseTypeDef",
    "GetIntegrationRequestRequestTypeDef",
    "GetIntegrationResponseRequestRequestTypeDef",
    "GetIntegrationResponseResponseTypeDef",
    "GetIntegrationResponsesRequestRequestTypeDef",
    "GetIntegrationResponsesResponseTypeDef",
    "GetIntegrationResultTypeDef",
    "GetIntegrationsRequestRequestTypeDef",
    "GetIntegrationsResponseTypeDef",
    "GetModelRequestRequestTypeDef",
    "GetModelResponseTypeDef",
    "GetModelTemplateRequestRequestTypeDef",
    "GetModelTemplateResponseTypeDef",
    "GetModelsRequestRequestTypeDef",
    "GetModelsResponseTypeDef",
    "GetRouteRequestRequestTypeDef",
    "GetRouteResponseRequestRequestTypeDef",
    "GetRouteResponseResponseTypeDef",
    "GetRouteResponsesRequestRequestTypeDef",
    "GetRouteResponsesResponseTypeDef",
    "GetRouteResultTypeDef",
    "GetRoutesRequestRequestTypeDef",
    "GetRoutesResponseTypeDef",
    "GetStageRequestRequestTypeDef",
    "GetStageResponseTypeDef",
    "GetStagesRequestRequestTypeDef",
    "GetStagesResponseTypeDef",
    "GetTagsRequestRequestTypeDef",
    "GetTagsResponseTypeDef",
    "GetVpcLinkRequestRequestTypeDef",
    "GetVpcLinkResponseTypeDef",
    "GetVpcLinksRequestRequestTypeDef",
    "GetVpcLinksResponseTypeDef",
    "ImportApiRequestRequestTypeDef",
    "ImportApiResponseTypeDef",
    "IntegrationResponseTypeDef",
    "IntegrationTypeDef",
    "JWTConfigurationTypeDef",
    "ModelTypeDef",
    "MutualTlsAuthenticationInputTypeDef",
    "MutualTlsAuthenticationTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterConstraintsTypeDef",
    "ReimportApiRequestRequestTypeDef",
    "ReimportApiResponseTypeDef",
    "ResetAuthorizersCacheRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RouteResponseTypeDef",
    "RouteSettingsTypeDef",
    "RouteTypeDef",
    "StageTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TlsConfigInputTypeDef",
    "TlsConfigTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApiMappingRequestRequestTypeDef",
    "UpdateApiMappingResponseTypeDef",
    "UpdateApiRequestRequestTypeDef",
    "UpdateApiResponseTypeDef",
    "UpdateAuthorizerRequestRequestTypeDef",
    "UpdateAuthorizerResponseTypeDef",
    "UpdateDeploymentRequestRequestTypeDef",
    "UpdateDeploymentResponseTypeDef",
    "UpdateDomainNameRequestRequestTypeDef",
    "UpdateDomainNameResponseTypeDef",
    "UpdateIntegrationRequestRequestTypeDef",
    "UpdateIntegrationResponseRequestRequestTypeDef",
    "UpdateIntegrationResponseResponseTypeDef",
    "UpdateIntegrationResultTypeDef",
    "UpdateModelRequestRequestTypeDef",
    "UpdateModelResponseTypeDef",
    "UpdateRouteRequestRequestTypeDef",
    "UpdateRouteResponseRequestRequestTypeDef",
    "UpdateRouteResponseResponseTypeDef",
    "UpdateRouteResultTypeDef",
    "UpdateStageRequestRequestTypeDef",
    "UpdateStageResponseTypeDef",
    "UpdateVpcLinkRequestRequestTypeDef",
    "UpdateVpcLinkResponseTypeDef",
    "VpcLinkTypeDef",
)

AccessLogSettingsTypeDef = TypedDict(
    "AccessLogSettingsTypeDef",
    {
        "DestinationArn": str,
        "Format": str,
    },
    total=False,
)

_RequiredApiMappingTypeDef = TypedDict(
    "_RequiredApiMappingTypeDef",
    {
        "ApiId": str,
        "Stage": str,
    },
)
_OptionalApiMappingTypeDef = TypedDict(
    "_OptionalApiMappingTypeDef",
    {
        "ApiMappingId": str,
        "ApiMappingKey": str,
    },
    total=False,
)

class ApiMappingTypeDef(_RequiredApiMappingTypeDef, _OptionalApiMappingTypeDef):
    pass

_RequiredApiTypeDef = TypedDict(
    "_RequiredApiTypeDef",
    {
        "Name": str,
        "ProtocolType": ProtocolTypeType,
        "RouteSelectionExpression": str,
    },
)
_OptionalApiTypeDef = TypedDict(
    "_OptionalApiTypeDef",
    {
        "ApiEndpoint": str,
        "ApiGatewayManaged": bool,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": "CorsTypeDef",
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "ImportInfo": List[str],
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
    },
    total=False,
)

class ApiTypeDef(_RequiredApiTypeDef, _OptionalApiTypeDef):
    pass

_RequiredAuthorizerTypeDef = TypedDict(
    "_RequiredAuthorizerTypeDef",
    {
        "Name": str,
    },
)
_OptionalAuthorizerTypeDef = TypedDict(
    "_OptionalAuthorizerTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerPayloadFormatVersion": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": AuthorizerTypeType,
        "AuthorizerUri": str,
        "EnableSimpleResponses": bool,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": "JWTConfigurationTypeDef",
    },
    total=False,
)

class AuthorizerTypeDef(_RequiredAuthorizerTypeDef, _OptionalAuthorizerTypeDef):
    pass

CorsTypeDef = TypedDict(
    "CorsTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

_RequiredCreateApiMappingRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApiMappingRequestRequestTypeDef",
    {
        "ApiId": str,
        "DomainName": str,
        "Stage": str,
    },
)
_OptionalCreateApiMappingRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApiMappingRequestRequestTypeDef",
    {
        "ApiMappingKey": str,
    },
    total=False,
)

class CreateApiMappingRequestRequestTypeDef(
    _RequiredCreateApiMappingRequestRequestTypeDef, _OptionalCreateApiMappingRequestRequestTypeDef
):
    pass

CreateApiMappingResponseTypeDef = TypedDict(
    "CreateApiMappingResponseTypeDef",
    {
        "ApiId": str,
        "ApiMappingId": str,
        "ApiMappingKey": str,
        "Stage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateApiRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApiRequestRequestTypeDef",
    {
        "Name": str,
        "ProtocolType": ProtocolTypeType,
    },
)
_OptionalCreateApiRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApiRequestRequestTypeDef",
    {
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": "CorsTypeDef",
        "CredentialsArn": str,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "RouteKey": str,
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Target": str,
        "Version": str,
    },
    total=False,
)

class CreateApiRequestRequestTypeDef(
    _RequiredCreateApiRequestRequestTypeDef, _OptionalCreateApiRequestRequestTypeDef
):
    pass

CreateApiResponseTypeDef = TypedDict(
    "CreateApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiGatewayManaged": bool,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": "CorsTypeDef",
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": ProtocolTypeType,
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAuthorizerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAuthorizerRequestRequestTypeDef",
    {
        "ApiId": str,
        "AuthorizerType": AuthorizerTypeType,
        "IdentitySource": List[str],
        "Name": str,
    },
)
_OptionalCreateAuthorizerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAuthorizerRequestRequestTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerPayloadFormatVersion": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerUri": str,
        "EnableSimpleResponses": bool,
        "IdentityValidationExpression": str,
        "JwtConfiguration": "JWTConfigurationTypeDef",
    },
    total=False,
)

class CreateAuthorizerRequestRequestTypeDef(
    _RequiredCreateAuthorizerRequestRequestTypeDef, _OptionalCreateAuthorizerRequestRequestTypeDef
):
    pass

CreateAuthorizerResponseTypeDef = TypedDict(
    "CreateAuthorizerResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerPayloadFormatVersion": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": AuthorizerTypeType,
        "AuthorizerUri": str,
        "EnableSimpleResponses": bool,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": "JWTConfigurationTypeDef",
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeploymentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDeploymentRequestRequestTypeDef",
    {
        "ApiId": str,
    },
)
_OptionalCreateDeploymentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDeploymentRequestRequestTypeDef",
    {
        "Description": str,
        "StageName": str,
    },
    total=False,
)

class CreateDeploymentRequestRequestTypeDef(
    _RequiredCreateDeploymentRequestRequestTypeDef, _OptionalCreateDeploymentRequestRequestTypeDef
):
    pass

CreateDeploymentResponseTypeDef = TypedDict(
    "CreateDeploymentResponseTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": DeploymentStatusType,
        "DeploymentStatusMessage": str,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDomainNameRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDomainNameRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalCreateDomainNameRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDomainNameRequestRequestTypeDef",
    {
        "DomainNameConfigurations": List["DomainNameConfigurationTypeDef"],
        "MutualTlsAuthentication": "MutualTlsAuthenticationInputTypeDef",
        "Tags": Dict[str, str],
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
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List["DomainNameConfigurationTypeDef"],
        "MutualTlsAuthentication": "MutualTlsAuthenticationTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIntegrationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIntegrationRequestRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationType": IntegrationTypeType,
    },
)
_OptionalCreateIntegrationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIntegrationRequestRequestTypeDef",
    {
        "ConnectionId": str,
        "ConnectionType": ConnectionTypeType,
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "CredentialsArn": str,
        "Description": str,
        "IntegrationMethod": str,
        "IntegrationSubtype": str,
        "IntegrationUri": str,
        "PassthroughBehavior": PassthroughBehaviorType,
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "ResponseParameters": Dict[str, Dict[str, str]],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
        "TlsConfig": "TlsConfigInputTypeDef",
    },
    total=False,
)

class CreateIntegrationRequestRequestTypeDef(
    _RequiredCreateIntegrationRequestRequestTypeDef, _OptionalCreateIntegrationRequestRequestTypeDef
):
    pass

_RequiredCreateIntegrationResponseRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIntegrationResponseRequestRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
        "IntegrationResponseKey": str,
    },
)
_OptionalCreateIntegrationResponseRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIntegrationResponseRequestRequestTypeDef",
    {
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)

class CreateIntegrationResponseRequestRequestTypeDef(
    _RequiredCreateIntegrationResponseRequestRequestTypeDef,
    _OptionalCreateIntegrationResponseRequestRequestTypeDef,
):
    pass

CreateIntegrationResponseResponseTypeDef = TypedDict(
    "CreateIntegrationResponseResponseTypeDef",
    {
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIntegrationResultTypeDef = TypedDict(
    "CreateIntegrationResultTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": ConnectionTypeType,
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationSubtype": str,
        "IntegrationType": IntegrationTypeType,
        "IntegrationUri": str,
        "PassthroughBehavior": PassthroughBehaviorType,
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "ResponseParameters": Dict[str, Dict[str, str]],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
        "TlsConfig": "TlsConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelRequestRequestTypeDef",
    {
        "ApiId": str,
        "Name": str,
        "Schema": str,
    },
)
_OptionalCreateModelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelRequestRequestTypeDef",
    {
        "ContentType": str,
        "Description": str,
    },
    total=False,
)

class CreateModelRequestRequestTypeDef(
    _RequiredCreateModelRequestRequestTypeDef, _OptionalCreateModelRequestRequestTypeDef
):
    pass

CreateModelResponseTypeDef = TypedDict(
    "CreateModelResponseTypeDef",
    {
        "ContentType": str,
        "Description": str,
        "ModelId": str,
        "Name": str,
        "Schema": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRouteRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRouteRequestRequestTypeDef",
    {
        "ApiId": str,
        "RouteKey": str,
    },
)
_OptionalCreateRouteRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRouteRequestRequestTypeDef",
    {
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": AuthorizationTypeType,
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)

class CreateRouteRequestRequestTypeDef(
    _RequiredCreateRouteRequestRequestTypeDef, _OptionalCreateRouteRequestRequestTypeDef
):
    pass

_RequiredCreateRouteResponseRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRouteResponseRequestRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
        "RouteResponseKey": str,
    },
)
_OptionalCreateRouteResponseRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRouteResponseRequestRequestTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, "ParameterConstraintsTypeDef"],
    },
    total=False,
)

class CreateRouteResponseRequestRequestTypeDef(
    _RequiredCreateRouteResponseRequestRequestTypeDef,
    _OptionalCreateRouteResponseRequestRequestTypeDef,
):
    pass

CreateRouteResponseResponseTypeDef = TypedDict(
    "CreateRouteResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteResponseId": str,
        "RouteResponseKey": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRouteResultTypeDef = TypedDict(
    "CreateRouteResultTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": AuthorizationTypeType,
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStageRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStageRequestRequestTypeDef",
    {
        "ApiId": str,
        "StageName": str,
    },
)
_OptionalCreateStageRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStageRequestRequestTypeDef",
    {
        "AccessLogSettings": "AccessLogSettingsTypeDef",
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "DefaultRouteSettings": "RouteSettingsTypeDef",
        "DeploymentId": str,
        "Description": str,
        "RouteSettings": Dict[str, "RouteSettingsTypeDef"],
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateStageRequestRequestTypeDef(
    _RequiredCreateStageRequestRequestTypeDef, _OptionalCreateStageRequestRequestTypeDef
):
    pass

CreateStageResponseTypeDef = TypedDict(
    "CreateStageResponseTypeDef",
    {
        "AccessLogSettings": "AccessLogSettingsTypeDef",
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": "RouteSettingsTypeDef",
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, "RouteSettingsTypeDef"],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVpcLinkRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVpcLinkRequestRequestTypeDef",
    {
        "Name": str,
        "SubnetIds": List[str],
    },
)
_OptionalCreateVpcLinkRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVpcLinkRequestRequestTypeDef",
    {
        "SecurityGroupIds": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateVpcLinkRequestRequestTypeDef(
    _RequiredCreateVpcLinkRequestRequestTypeDef, _OptionalCreateVpcLinkRequestRequestTypeDef
):
    pass

CreateVpcLinkResponseTypeDef = TypedDict(
    "CreateVpcLinkResponseTypeDef",
    {
        "CreatedDate": datetime,
        "Name": str,
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "Tags": Dict[str, str],
        "VpcLinkId": str,
        "VpcLinkStatus": VpcLinkStatusType,
        "VpcLinkStatusMessage": str,
        "VpcLinkVersion": Literal["V2"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAccessLogSettingsRequestRequestTypeDef = TypedDict(
    "DeleteAccessLogSettingsRequestRequestTypeDef",
    {
        "ApiId": str,
        "StageName": str,
    },
)

DeleteApiMappingRequestRequestTypeDef = TypedDict(
    "DeleteApiMappingRequestRequestTypeDef",
    {
        "ApiMappingId": str,
        "DomainName": str,
    },
)

DeleteApiRequestRequestTypeDef = TypedDict(
    "DeleteApiRequestRequestTypeDef",
    {
        "ApiId": str,
    },
)

DeleteAuthorizerRequestRequestTypeDef = TypedDict(
    "DeleteAuthorizerRequestRequestTypeDef",
    {
        "ApiId": str,
        "AuthorizerId": str,
    },
)

DeleteCorsConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteCorsConfigurationRequestRequestTypeDef",
    {
        "ApiId": str,
    },
)

DeleteDeploymentRequestRequestTypeDef = TypedDict(
    "DeleteDeploymentRequestRequestTypeDef",
    {
        "ApiId": str,
        "DeploymentId": str,
    },
)

DeleteDomainNameRequestRequestTypeDef = TypedDict(
    "DeleteDomainNameRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DeleteIntegrationRequestRequestTypeDef = TypedDict(
    "DeleteIntegrationRequestRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
    },
)

DeleteIntegrationResponseRequestRequestTypeDef = TypedDict(
    "DeleteIntegrationResponseRequestRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
        "IntegrationResponseId": str,
    },
)

DeleteModelRequestRequestTypeDef = TypedDict(
    "DeleteModelRequestRequestTypeDef",
    {
        "ApiId": str,
        "ModelId": str,
    },
)

DeleteRouteRequestParameterRequestRequestTypeDef = TypedDict(
    "DeleteRouteRequestParameterRequestRequestTypeDef",
    {
        "ApiId": str,
        "RequestParameterKey": str,
        "RouteId": str,
    },
)

DeleteRouteRequestRequestTypeDef = TypedDict(
    "DeleteRouteRequestRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
    },
)

DeleteRouteResponseRequestRequestTypeDef = TypedDict(
    "DeleteRouteResponseRequestRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
        "RouteResponseId": str,
    },
)

DeleteRouteSettingsRequestRequestTypeDef = TypedDict(
    "DeleteRouteSettingsRequestRequestTypeDef",
    {
        "ApiId": str,
        "RouteKey": str,
        "StageName": str,
    },
)

DeleteStageRequestRequestTypeDef = TypedDict(
    "DeleteStageRequestRequestTypeDef",
    {
        "ApiId": str,
        "StageName": str,
    },
)

DeleteVpcLinkRequestRequestTypeDef = TypedDict(
    "DeleteVpcLinkRequestRequestTypeDef",
    {
        "VpcLinkId": str,
    },
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": DeploymentStatusType,
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)

DomainNameConfigurationTypeDef = TypedDict(
    "DomainNameConfigurationTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": Union[datetime, str],
        "DomainNameStatus": DomainNameStatusType,
        "DomainNameStatusMessage": str,
        "EndpointType": EndpointTypeType,
        "HostedZoneId": str,
        "SecurityPolicy": SecurityPolicyType,
    },
    total=False,
)

_RequiredDomainNameTypeDef = TypedDict(
    "_RequiredDomainNameTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDomainNameTypeDef = TypedDict(
    "_OptionalDomainNameTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainNameConfigurations": List["DomainNameConfigurationTypeDef"],
        "MutualTlsAuthentication": "MutualTlsAuthenticationTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

class DomainNameTypeDef(_RequiredDomainNameTypeDef, _OptionalDomainNameTypeDef):
    pass

_RequiredExportApiRequestRequestTypeDef = TypedDict(
    "_RequiredExportApiRequestRequestTypeDef",
    {
        "ApiId": str,
        "OutputType": JSONYAMLType,
        "Specification": Literal["OAS30"],
    },
)
_OptionalExportApiRequestRequestTypeDef = TypedDict(
    "_OptionalExportApiRequestRequestTypeDef",
    {
        "ExportVersion": str,
        "IncludeExtensions": bool,
        "StageName": str,
    },
    total=False,
)

class ExportApiRequestRequestTypeDef(
    _RequiredExportApiRequestRequestTypeDef, _OptionalExportApiRequestRequestTypeDef
):
    pass

ExportApiResponseTypeDef = TypedDict(
    "ExportApiResponseTypeDef",
    {
        "body": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApiMappingRequestRequestTypeDef = TypedDict(
    "GetApiMappingRequestRequestTypeDef",
    {
        "ApiMappingId": str,
        "DomainName": str,
    },
)

GetApiMappingResponseTypeDef = TypedDict(
    "GetApiMappingResponseTypeDef",
    {
        "ApiId": str,
        "ApiMappingId": str,
        "ApiMappingKey": str,
        "Stage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetApiMappingsRequestRequestTypeDef = TypedDict(
    "_RequiredGetApiMappingsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalGetApiMappingsRequestRequestTypeDef = TypedDict(
    "_OptionalGetApiMappingsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

class GetApiMappingsRequestRequestTypeDef(
    _RequiredGetApiMappingsRequestRequestTypeDef, _OptionalGetApiMappingsRequestRequestTypeDef
):
    pass

GetApiMappingsResponseTypeDef = TypedDict(
    "GetApiMappingsResponseTypeDef",
    {
        "Items": List["ApiMappingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApiRequestRequestTypeDef = TypedDict(
    "GetApiRequestRequestTypeDef",
    {
        "ApiId": str,
    },
)

GetApiResponseTypeDef = TypedDict(
    "GetApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiGatewayManaged": bool,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": "CorsTypeDef",
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": ProtocolTypeType,
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApisRequestRequestTypeDef = TypedDict(
    "GetApisRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

GetApisResponseTypeDef = TypedDict(
    "GetApisResponseTypeDef",
    {
        "Items": List["ApiTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAuthorizerRequestRequestTypeDef = TypedDict(
    "GetAuthorizerRequestRequestTypeDef",
    {
        "ApiId": str,
        "AuthorizerId": str,
    },
)

GetAuthorizerResponseTypeDef = TypedDict(
    "GetAuthorizerResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerPayloadFormatVersion": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": AuthorizerTypeType,
        "AuthorizerUri": str,
        "EnableSimpleResponses": bool,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": "JWTConfigurationTypeDef",
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetAuthorizersRequestRequestTypeDef = TypedDict(
    "_RequiredGetAuthorizersRequestRequestTypeDef",
    {
        "ApiId": str,
    },
)
_OptionalGetAuthorizersRequestRequestTypeDef = TypedDict(
    "_OptionalGetAuthorizersRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

class GetAuthorizersRequestRequestTypeDef(
    _RequiredGetAuthorizersRequestRequestTypeDef, _OptionalGetAuthorizersRequestRequestTypeDef
):
    pass

GetAuthorizersResponseTypeDef = TypedDict(
    "GetAuthorizersResponseTypeDef",
    {
        "Items": List["AuthorizerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentRequestRequestTypeDef = TypedDict(
    "GetDeploymentRequestRequestTypeDef",
    {
        "ApiId": str,
        "DeploymentId": str,
    },
)

GetDeploymentResponseTypeDef = TypedDict(
    "GetDeploymentResponseTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": DeploymentStatusType,
        "DeploymentStatusMessage": str,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDeploymentsRequestRequestTypeDef = TypedDict(
    "_RequiredGetDeploymentsRequestRequestTypeDef",
    {
        "ApiId": str,
    },
)
_OptionalGetDeploymentsRequestRequestTypeDef = TypedDict(
    "_OptionalGetDeploymentsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

class GetDeploymentsRequestRequestTypeDef(
    _RequiredGetDeploymentsRequestRequestTypeDef, _OptionalGetDeploymentsRequestRequestTypeDef
):
    pass

GetDeploymentsResponseTypeDef = TypedDict(
    "GetDeploymentsResponseTypeDef",
    {
        "Items": List["DeploymentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainNameRequestRequestTypeDef = TypedDict(
    "GetDomainNameRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

GetDomainNameResponseTypeDef = TypedDict(
    "GetDomainNameResponseTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List["DomainNameConfigurationTypeDef"],
        "MutualTlsAuthentication": "MutualTlsAuthenticationTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainNamesRequestRequestTypeDef = TypedDict(
    "GetDomainNamesRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

GetDomainNamesResponseTypeDef = TypedDict(
    "GetDomainNamesResponseTypeDef",
    {
        "Items": List["DomainNameTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIntegrationRequestRequestTypeDef = TypedDict(
    "GetIntegrationRequestRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
    },
)

GetIntegrationResponseRequestRequestTypeDef = TypedDict(
    "GetIntegrationResponseRequestRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
        "IntegrationResponseId": str,
    },
)

GetIntegrationResponseResponseTypeDef = TypedDict(
    "GetIntegrationResponseResponseTypeDef",
    {
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetIntegrationResponsesRequestRequestTypeDef = TypedDict(
    "_RequiredGetIntegrationResponsesRequestRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
    },
)
_OptionalGetIntegrationResponsesRequestRequestTypeDef = TypedDict(
    "_OptionalGetIntegrationResponsesRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

class GetIntegrationResponsesRequestRequestTypeDef(
    _RequiredGetIntegrationResponsesRequestRequestTypeDef,
    _OptionalGetIntegrationResponsesRequestRequestTypeDef,
):
    pass

GetIntegrationResponsesResponseTypeDef = TypedDict(
    "GetIntegrationResponsesResponseTypeDef",
    {
        "Items": List["IntegrationResponseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIntegrationResultTypeDef = TypedDict(
    "GetIntegrationResultTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": ConnectionTypeType,
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationSubtype": str,
        "IntegrationType": IntegrationTypeType,
        "IntegrationUri": str,
        "PassthroughBehavior": PassthroughBehaviorType,
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "ResponseParameters": Dict[str, Dict[str, str]],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
        "TlsConfig": "TlsConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetIntegrationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetIntegrationsRequestRequestTypeDef",
    {
        "ApiId": str,
    },
)
_OptionalGetIntegrationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetIntegrationsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

class GetIntegrationsRequestRequestTypeDef(
    _RequiredGetIntegrationsRequestRequestTypeDef, _OptionalGetIntegrationsRequestRequestTypeDef
):
    pass

GetIntegrationsResponseTypeDef = TypedDict(
    "GetIntegrationsResponseTypeDef",
    {
        "Items": List["IntegrationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetModelRequestRequestTypeDef = TypedDict(
    "GetModelRequestRequestTypeDef",
    {
        "ApiId": str,
        "ModelId": str,
    },
)

GetModelResponseTypeDef = TypedDict(
    "GetModelResponseTypeDef",
    {
        "ContentType": str,
        "Description": str,
        "ModelId": str,
        "Name": str,
        "Schema": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetModelTemplateRequestRequestTypeDef = TypedDict(
    "GetModelTemplateRequestRequestTypeDef",
    {
        "ApiId": str,
        "ModelId": str,
    },
)

GetModelTemplateResponseTypeDef = TypedDict(
    "GetModelTemplateResponseTypeDef",
    {
        "Value": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetModelsRequestRequestTypeDef = TypedDict(
    "_RequiredGetModelsRequestRequestTypeDef",
    {
        "ApiId": str,
    },
)
_OptionalGetModelsRequestRequestTypeDef = TypedDict(
    "_OptionalGetModelsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

class GetModelsRequestRequestTypeDef(
    _RequiredGetModelsRequestRequestTypeDef, _OptionalGetModelsRequestRequestTypeDef
):
    pass

GetModelsResponseTypeDef = TypedDict(
    "GetModelsResponseTypeDef",
    {
        "Items": List["ModelTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRouteRequestRequestTypeDef = TypedDict(
    "GetRouteRequestRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
    },
)

GetRouteResponseRequestRequestTypeDef = TypedDict(
    "GetRouteResponseRequestRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
        "RouteResponseId": str,
    },
)

GetRouteResponseResponseTypeDef = TypedDict(
    "GetRouteResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteResponseId": str,
        "RouteResponseKey": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRouteResponsesRequestRequestTypeDef = TypedDict(
    "_RequiredGetRouteResponsesRequestRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
    },
)
_OptionalGetRouteResponsesRequestRequestTypeDef = TypedDict(
    "_OptionalGetRouteResponsesRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

class GetRouteResponsesRequestRequestTypeDef(
    _RequiredGetRouteResponsesRequestRequestTypeDef, _OptionalGetRouteResponsesRequestRequestTypeDef
):
    pass

GetRouteResponsesResponseTypeDef = TypedDict(
    "GetRouteResponsesResponseTypeDef",
    {
        "Items": List["RouteResponseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRouteResultTypeDef = TypedDict(
    "GetRouteResultTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": AuthorizationTypeType,
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRoutesRequestRequestTypeDef = TypedDict(
    "_RequiredGetRoutesRequestRequestTypeDef",
    {
        "ApiId": str,
    },
)
_OptionalGetRoutesRequestRequestTypeDef = TypedDict(
    "_OptionalGetRoutesRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

class GetRoutesRequestRequestTypeDef(
    _RequiredGetRoutesRequestRequestTypeDef, _OptionalGetRoutesRequestRequestTypeDef
):
    pass

GetRoutesResponseTypeDef = TypedDict(
    "GetRoutesResponseTypeDef",
    {
        "Items": List["RouteTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStageRequestRequestTypeDef = TypedDict(
    "GetStageRequestRequestTypeDef",
    {
        "ApiId": str,
        "StageName": str,
    },
)

GetStageResponseTypeDef = TypedDict(
    "GetStageResponseTypeDef",
    {
        "AccessLogSettings": "AccessLogSettingsTypeDef",
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": "RouteSettingsTypeDef",
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, "RouteSettingsTypeDef"],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetStagesRequestRequestTypeDef = TypedDict(
    "_RequiredGetStagesRequestRequestTypeDef",
    {
        "ApiId": str,
    },
)
_OptionalGetStagesRequestRequestTypeDef = TypedDict(
    "_OptionalGetStagesRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

class GetStagesRequestRequestTypeDef(
    _RequiredGetStagesRequestRequestTypeDef, _OptionalGetStagesRequestRequestTypeDef
):
    pass

GetStagesResponseTypeDef = TypedDict(
    "GetStagesResponseTypeDef",
    {
        "Items": List["StageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTagsRequestRequestTypeDef = TypedDict(
    "GetTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetTagsResponseTypeDef = TypedDict(
    "GetTagsResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVpcLinkRequestRequestTypeDef = TypedDict(
    "GetVpcLinkRequestRequestTypeDef",
    {
        "VpcLinkId": str,
    },
)

GetVpcLinkResponseTypeDef = TypedDict(
    "GetVpcLinkResponseTypeDef",
    {
        "CreatedDate": datetime,
        "Name": str,
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "Tags": Dict[str, str],
        "VpcLinkId": str,
        "VpcLinkStatus": VpcLinkStatusType,
        "VpcLinkStatusMessage": str,
        "VpcLinkVersion": Literal["V2"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVpcLinksRequestRequestTypeDef = TypedDict(
    "GetVpcLinksRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

GetVpcLinksResponseTypeDef = TypedDict(
    "GetVpcLinksResponseTypeDef",
    {
        "Items": List["VpcLinkTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImportApiRequestRequestTypeDef = TypedDict(
    "_RequiredImportApiRequestRequestTypeDef",
    {
        "Body": str,
    },
)
_OptionalImportApiRequestRequestTypeDef = TypedDict(
    "_OptionalImportApiRequestRequestTypeDef",
    {
        "Basepath": str,
        "FailOnWarnings": bool,
    },
    total=False,
)

class ImportApiRequestRequestTypeDef(
    _RequiredImportApiRequestRequestTypeDef, _OptionalImportApiRequestRequestTypeDef
):
    pass

ImportApiResponseTypeDef = TypedDict(
    "ImportApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiGatewayManaged": bool,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": "CorsTypeDef",
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": ProtocolTypeType,
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredIntegrationResponseTypeDef = TypedDict(
    "_RequiredIntegrationResponseTypeDef",
    {
        "IntegrationResponseKey": str,
    },
)
_OptionalIntegrationResponseTypeDef = TypedDict(
    "_OptionalIntegrationResponseTypeDef",
    {
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "IntegrationResponseId": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)

class IntegrationResponseTypeDef(
    _RequiredIntegrationResponseTypeDef, _OptionalIntegrationResponseTypeDef
):
    pass

IntegrationTypeDef = TypedDict(
    "IntegrationTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": ConnectionTypeType,
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationSubtype": str,
        "IntegrationType": IntegrationTypeType,
        "IntegrationUri": str,
        "PassthroughBehavior": PassthroughBehaviorType,
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "ResponseParameters": Dict[str, Dict[str, str]],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
        "TlsConfig": "TlsConfigTypeDef",
    },
    total=False,
)

JWTConfigurationTypeDef = TypedDict(
    "JWTConfigurationTypeDef",
    {
        "Audience": List[str],
        "Issuer": str,
    },
    total=False,
)

_RequiredModelTypeDef = TypedDict(
    "_RequiredModelTypeDef",
    {
        "Name": str,
    },
)
_OptionalModelTypeDef = TypedDict(
    "_OptionalModelTypeDef",
    {
        "ContentType": str,
        "Description": str,
        "ModelId": str,
        "Schema": str,
    },
    total=False,
)

class ModelTypeDef(_RequiredModelTypeDef, _OptionalModelTypeDef):
    pass

MutualTlsAuthenticationInputTypeDef = TypedDict(
    "MutualTlsAuthenticationInputTypeDef",
    {
        "TruststoreUri": str,
        "TruststoreVersion": str,
    },
    total=False,
)

MutualTlsAuthenticationTypeDef = TypedDict(
    "MutualTlsAuthenticationTypeDef",
    {
        "TruststoreUri": str,
        "TruststoreVersion": str,
        "TruststoreWarnings": List[str],
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

ParameterConstraintsTypeDef = TypedDict(
    "ParameterConstraintsTypeDef",
    {
        "Required": bool,
    },
    total=False,
)

_RequiredReimportApiRequestRequestTypeDef = TypedDict(
    "_RequiredReimportApiRequestRequestTypeDef",
    {
        "ApiId": str,
        "Body": str,
    },
)
_OptionalReimportApiRequestRequestTypeDef = TypedDict(
    "_OptionalReimportApiRequestRequestTypeDef",
    {
        "Basepath": str,
        "FailOnWarnings": bool,
    },
    total=False,
)

class ReimportApiRequestRequestTypeDef(
    _RequiredReimportApiRequestRequestTypeDef, _OptionalReimportApiRequestRequestTypeDef
):
    pass

ReimportApiResponseTypeDef = TypedDict(
    "ReimportApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiGatewayManaged": bool,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": "CorsTypeDef",
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": ProtocolTypeType,
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResetAuthorizersCacheRequestRequestTypeDef = TypedDict(
    "ResetAuthorizersCacheRequestRequestTypeDef",
    {
        "ApiId": str,
        "StageName": str,
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

_RequiredRouteResponseTypeDef = TypedDict(
    "_RequiredRouteResponseTypeDef",
    {
        "RouteResponseKey": str,
    },
)
_OptionalRouteResponseTypeDef = TypedDict(
    "_OptionalRouteResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteResponseId": str,
    },
    total=False,
)

class RouteResponseTypeDef(_RequiredRouteResponseTypeDef, _OptionalRouteResponseTypeDef):
    pass

RouteSettingsTypeDef = TypedDict(
    "RouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": LoggingLevelType,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

_RequiredRouteTypeDef = TypedDict(
    "_RequiredRouteTypeDef",
    {
        "RouteKey": str,
    },
)
_OptionalRouteTypeDef = TypedDict(
    "_OptionalRouteTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": AuthorizationTypeType,
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteId": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)

class RouteTypeDef(_RequiredRouteTypeDef, _OptionalRouteTypeDef):
    pass

_RequiredStageTypeDef = TypedDict(
    "_RequiredStageTypeDef",
    {
        "StageName": str,
    },
)
_OptionalStageTypeDef = TypedDict(
    "_OptionalStageTypeDef",
    {
        "AccessLogSettings": "AccessLogSettingsTypeDef",
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": "RouteSettingsTypeDef",
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, "RouteSettingsTypeDef"],
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)

class StageTypeDef(_RequiredStageTypeDef, _OptionalStageTypeDef):
    pass

_RequiredTagResourceRequestRequestTypeDef = TypedDict(
    "_RequiredTagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalTagResourceRequestRequestTypeDef = TypedDict(
    "_OptionalTagResourceRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class TagResourceRequestRequestTypeDef(
    _RequiredTagResourceRequestRequestTypeDef, _OptionalTagResourceRequestRequestTypeDef
):
    pass

TlsConfigInputTypeDef = TypedDict(
    "TlsConfigInputTypeDef",
    {
        "ServerNameToVerify": str,
    },
    total=False,
)

TlsConfigTypeDef = TypedDict(
    "TlsConfigTypeDef",
    {
        "ServerNameToVerify": str,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateApiMappingRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApiMappingRequestRequestTypeDef",
    {
        "ApiId": str,
        "ApiMappingId": str,
        "DomainName": str,
    },
)
_OptionalUpdateApiMappingRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApiMappingRequestRequestTypeDef",
    {
        "ApiMappingKey": str,
        "Stage": str,
    },
    total=False,
)

class UpdateApiMappingRequestRequestTypeDef(
    _RequiredUpdateApiMappingRequestRequestTypeDef, _OptionalUpdateApiMappingRequestRequestTypeDef
):
    pass

UpdateApiMappingResponseTypeDef = TypedDict(
    "UpdateApiMappingResponseTypeDef",
    {
        "ApiId": str,
        "ApiMappingId": str,
        "ApiMappingKey": str,
        "Stage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateApiRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApiRequestRequestTypeDef",
    {
        "ApiId": str,
    },
)
_OptionalUpdateApiRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApiRequestRequestTypeDef",
    {
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": "CorsTypeDef",
        "CredentialsArn": str,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "Name": str,
        "RouteKey": str,
        "RouteSelectionExpression": str,
        "Target": str,
        "Version": str,
    },
    total=False,
)

class UpdateApiRequestRequestTypeDef(
    _RequiredUpdateApiRequestRequestTypeDef, _OptionalUpdateApiRequestRequestTypeDef
):
    pass

UpdateApiResponseTypeDef = TypedDict(
    "UpdateApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiGatewayManaged": bool,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": "CorsTypeDef",
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": ProtocolTypeType,
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAuthorizerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAuthorizerRequestRequestTypeDef",
    {
        "ApiId": str,
        "AuthorizerId": str,
    },
)
_OptionalUpdateAuthorizerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAuthorizerRequestRequestTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerPayloadFormatVersion": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": AuthorizerTypeType,
        "AuthorizerUri": str,
        "EnableSimpleResponses": bool,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": "JWTConfigurationTypeDef",
        "Name": str,
    },
    total=False,
)

class UpdateAuthorizerRequestRequestTypeDef(
    _RequiredUpdateAuthorizerRequestRequestTypeDef, _OptionalUpdateAuthorizerRequestRequestTypeDef
):
    pass

UpdateAuthorizerResponseTypeDef = TypedDict(
    "UpdateAuthorizerResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerPayloadFormatVersion": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": AuthorizerTypeType,
        "AuthorizerUri": str,
        "EnableSimpleResponses": bool,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": "JWTConfigurationTypeDef",
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDeploymentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDeploymentRequestRequestTypeDef",
    {
        "ApiId": str,
        "DeploymentId": str,
    },
)
_OptionalUpdateDeploymentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDeploymentRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateDeploymentRequestRequestTypeDef(
    _RequiredUpdateDeploymentRequestRequestTypeDef, _OptionalUpdateDeploymentRequestRequestTypeDef
):
    pass

UpdateDeploymentResponseTypeDef = TypedDict(
    "UpdateDeploymentResponseTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": DeploymentStatusType,
        "DeploymentStatusMessage": str,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDomainNameRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainNameRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalUpdateDomainNameRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainNameRequestRequestTypeDef",
    {
        "DomainNameConfigurations": List["DomainNameConfigurationTypeDef"],
        "MutualTlsAuthentication": "MutualTlsAuthenticationInputTypeDef",
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
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List["DomainNameConfigurationTypeDef"],
        "MutualTlsAuthentication": "MutualTlsAuthenticationTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateIntegrationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIntegrationRequestRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
    },
)
_OptionalUpdateIntegrationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIntegrationRequestRequestTypeDef",
    {
        "ConnectionId": str,
        "ConnectionType": ConnectionTypeType,
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "CredentialsArn": str,
        "Description": str,
        "IntegrationMethod": str,
        "IntegrationSubtype": str,
        "IntegrationType": IntegrationTypeType,
        "IntegrationUri": str,
        "PassthroughBehavior": PassthroughBehaviorType,
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "ResponseParameters": Dict[str, Dict[str, str]],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
        "TlsConfig": "TlsConfigInputTypeDef",
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
        "ApiId": str,
        "IntegrationId": str,
        "IntegrationResponseId": str,
    },
)
_OptionalUpdateIntegrationResponseRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIntegrationResponseRequestRequestTypeDef",
    {
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)

class UpdateIntegrationResponseRequestRequestTypeDef(
    _RequiredUpdateIntegrationResponseRequestRequestTypeDef,
    _OptionalUpdateIntegrationResponseRequestRequestTypeDef,
):
    pass

UpdateIntegrationResponseResponseTypeDef = TypedDict(
    "UpdateIntegrationResponseResponseTypeDef",
    {
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateIntegrationResultTypeDef = TypedDict(
    "UpdateIntegrationResultTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": ConnectionTypeType,
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationSubtype": str,
        "IntegrationType": IntegrationTypeType,
        "IntegrationUri": str,
        "PassthroughBehavior": PassthroughBehaviorType,
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "ResponseParameters": Dict[str, Dict[str, str]],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
        "TlsConfig": "TlsConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateModelRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateModelRequestRequestTypeDef",
    {
        "ApiId": str,
        "ModelId": str,
    },
)
_OptionalUpdateModelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateModelRequestRequestTypeDef",
    {
        "ContentType": str,
        "Description": str,
        "Name": str,
        "Schema": str,
    },
    total=False,
)

class UpdateModelRequestRequestTypeDef(
    _RequiredUpdateModelRequestRequestTypeDef, _OptionalUpdateModelRequestRequestTypeDef
):
    pass

UpdateModelResponseTypeDef = TypedDict(
    "UpdateModelResponseTypeDef",
    {
        "ContentType": str,
        "Description": str,
        "ModelId": str,
        "Name": str,
        "Schema": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRouteRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRouteRequestRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
    },
)
_OptionalUpdateRouteRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRouteRequestRequestTypeDef",
    {
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": AuthorizationTypeType,
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)

class UpdateRouteRequestRequestTypeDef(
    _RequiredUpdateRouteRequestRequestTypeDef, _OptionalUpdateRouteRequestRequestTypeDef
):
    pass

_RequiredUpdateRouteResponseRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRouteResponseRequestRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
        "RouteResponseId": str,
    },
)
_OptionalUpdateRouteResponseRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRouteResponseRequestRequestTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteResponseKey": str,
    },
    total=False,
)

class UpdateRouteResponseRequestRequestTypeDef(
    _RequiredUpdateRouteResponseRequestRequestTypeDef,
    _OptionalUpdateRouteResponseRequestRequestTypeDef,
):
    pass

UpdateRouteResponseResponseTypeDef = TypedDict(
    "UpdateRouteResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteResponseId": str,
        "RouteResponseKey": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRouteResultTypeDef = TypedDict(
    "UpdateRouteResultTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": AuthorizationTypeType,
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateStageRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStageRequestRequestTypeDef",
    {
        "ApiId": str,
        "StageName": str,
    },
)
_OptionalUpdateStageRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStageRequestRequestTypeDef",
    {
        "AccessLogSettings": "AccessLogSettingsTypeDef",
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "DefaultRouteSettings": "RouteSettingsTypeDef",
        "DeploymentId": str,
        "Description": str,
        "RouteSettings": Dict[str, "RouteSettingsTypeDef"],
        "StageVariables": Dict[str, str],
    },
    total=False,
)

class UpdateStageRequestRequestTypeDef(
    _RequiredUpdateStageRequestRequestTypeDef, _OptionalUpdateStageRequestRequestTypeDef
):
    pass

UpdateStageResponseTypeDef = TypedDict(
    "UpdateStageResponseTypeDef",
    {
        "AccessLogSettings": "AccessLogSettingsTypeDef",
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": "RouteSettingsTypeDef",
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, "RouteSettingsTypeDef"],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVpcLinkRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateVpcLinkRequestRequestTypeDef",
    {
        "VpcLinkId": str,
    },
)
_OptionalUpdateVpcLinkRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateVpcLinkRequestRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class UpdateVpcLinkRequestRequestTypeDef(
    _RequiredUpdateVpcLinkRequestRequestTypeDef, _OptionalUpdateVpcLinkRequestRequestTypeDef
):
    pass

UpdateVpcLinkResponseTypeDef = TypedDict(
    "UpdateVpcLinkResponseTypeDef",
    {
        "CreatedDate": datetime,
        "Name": str,
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "Tags": Dict[str, str],
        "VpcLinkId": str,
        "VpcLinkStatus": VpcLinkStatusType,
        "VpcLinkStatusMessage": str,
        "VpcLinkVersion": Literal["V2"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredVpcLinkTypeDef = TypedDict(
    "_RequiredVpcLinkTypeDef",
    {
        "Name": str,
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "VpcLinkId": str,
    },
)
_OptionalVpcLinkTypeDef = TypedDict(
    "_OptionalVpcLinkTypeDef",
    {
        "CreatedDate": datetime,
        "Tags": Dict[str, str],
        "VpcLinkStatus": VpcLinkStatusType,
        "VpcLinkStatusMessage": str,
        "VpcLinkVersion": Literal["V2"],
    },
    total=False,
)

class VpcLinkTypeDef(_RequiredVpcLinkTypeDef, _OptionalVpcLinkTypeDef):
    pass
