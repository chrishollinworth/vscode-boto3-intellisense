"""
Type annotations for apigatewayv2 service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_apigatewayv2.type_defs import AccessLogSettingsTypeDef

    data: AccessLogSettingsTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from botocore.response import StreamingBody

from .literals import (
    AuthorizationTypeType,
    AuthorizerTypeType,
    ConnectionTypeType,
    ContentHandlingStrategyType,
    DeploymentStatusType,
    DomainNameStatusType,
    EndpointTypeType,
    IntegrationTypeType,
    IpAddressTypeType,
    JSONYAMLType,
    LoggingLevelType,
    PassthroughBehaviorType,
    ProtocolTypeType,
    SecurityPolicyType,
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
    "ApiMappingTypeDef",
    "ApiTypeDef",
    "AuthorizerTypeDef",
    "CorsOutputTypeDef",
    "CorsTypeDef",
    "CorsUnionTypeDef",
    "CreateApiMappingRequestTypeDef",
    "CreateApiMappingResponseTypeDef",
    "CreateApiRequestTypeDef",
    "CreateApiResponseTypeDef",
    "CreateAuthorizerRequestTypeDef",
    "CreateAuthorizerResponseTypeDef",
    "CreateDeploymentRequestTypeDef",
    "CreateDeploymentResponseTypeDef",
    "CreateDomainNameRequestTypeDef",
    "CreateDomainNameResponseTypeDef",
    "CreateIntegrationRequestTypeDef",
    "CreateIntegrationResponseRequestTypeDef",
    "CreateIntegrationResponseResponseTypeDef",
    "CreateIntegrationResultTypeDef",
    "CreateModelRequestTypeDef",
    "CreateModelResponseTypeDef",
    "CreateRouteRequestTypeDef",
    "CreateRouteResponseRequestTypeDef",
    "CreateRouteResponseResponseTypeDef",
    "CreateRouteResultTypeDef",
    "CreateStageRequestTypeDef",
    "CreateStageResponseTypeDef",
    "CreateVpcLinkRequestTypeDef",
    "CreateVpcLinkResponseTypeDef",
    "DeleteAccessLogSettingsRequestTypeDef",
    "DeleteApiMappingRequestTypeDef",
    "DeleteApiRequestTypeDef",
    "DeleteAuthorizerRequestTypeDef",
    "DeleteCorsConfigurationRequestTypeDef",
    "DeleteDeploymentRequestTypeDef",
    "DeleteDomainNameRequestTypeDef",
    "DeleteIntegrationRequestTypeDef",
    "DeleteIntegrationResponseRequestTypeDef",
    "DeleteModelRequestTypeDef",
    "DeleteRouteRequestParameterRequestTypeDef",
    "DeleteRouteRequestTypeDef",
    "DeleteRouteResponseRequestTypeDef",
    "DeleteRouteSettingsRequestTypeDef",
    "DeleteStageRequestTypeDef",
    "DeleteVpcLinkRequestTypeDef",
    "DeploymentTypeDef",
    "DomainNameConfigurationOutputTypeDef",
    "DomainNameConfigurationTypeDef",
    "DomainNameConfigurationUnionTypeDef",
    "DomainNameTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExportApiRequestTypeDef",
    "ExportApiResponseTypeDef",
    "GetApiMappingRequestTypeDef",
    "GetApiMappingResponseTypeDef",
    "GetApiMappingsRequestTypeDef",
    "GetApiMappingsResponseTypeDef",
    "GetApiRequestTypeDef",
    "GetApiResponseTypeDef",
    "GetApisRequestPaginateTypeDef",
    "GetApisRequestTypeDef",
    "GetApisResponseTypeDef",
    "GetAuthorizerRequestTypeDef",
    "GetAuthorizerResponseTypeDef",
    "GetAuthorizersRequestPaginateTypeDef",
    "GetAuthorizersRequestTypeDef",
    "GetAuthorizersResponseTypeDef",
    "GetDeploymentRequestTypeDef",
    "GetDeploymentResponseTypeDef",
    "GetDeploymentsRequestPaginateTypeDef",
    "GetDeploymentsRequestTypeDef",
    "GetDeploymentsResponseTypeDef",
    "GetDomainNameRequestTypeDef",
    "GetDomainNameResponseTypeDef",
    "GetDomainNamesRequestPaginateTypeDef",
    "GetDomainNamesRequestTypeDef",
    "GetDomainNamesResponseTypeDef",
    "GetIntegrationRequestTypeDef",
    "GetIntegrationResponseRequestTypeDef",
    "GetIntegrationResponseResponseTypeDef",
    "GetIntegrationResponsesRequestPaginateTypeDef",
    "GetIntegrationResponsesRequestTypeDef",
    "GetIntegrationResponsesResponseTypeDef",
    "GetIntegrationResultTypeDef",
    "GetIntegrationsRequestPaginateTypeDef",
    "GetIntegrationsRequestTypeDef",
    "GetIntegrationsResponseTypeDef",
    "GetModelRequestTypeDef",
    "GetModelResponseTypeDef",
    "GetModelTemplateRequestTypeDef",
    "GetModelTemplateResponseTypeDef",
    "GetModelsRequestPaginateTypeDef",
    "GetModelsRequestTypeDef",
    "GetModelsResponseTypeDef",
    "GetRouteRequestTypeDef",
    "GetRouteResponseRequestTypeDef",
    "GetRouteResponseResponseTypeDef",
    "GetRouteResponsesRequestPaginateTypeDef",
    "GetRouteResponsesRequestTypeDef",
    "GetRouteResponsesResponseTypeDef",
    "GetRouteResultTypeDef",
    "GetRoutesRequestPaginateTypeDef",
    "GetRoutesRequestTypeDef",
    "GetRoutesResponseTypeDef",
    "GetStageRequestTypeDef",
    "GetStageResponseTypeDef",
    "GetStagesRequestPaginateTypeDef",
    "GetStagesRequestTypeDef",
    "GetStagesResponseTypeDef",
    "GetTagsRequestTypeDef",
    "GetTagsResponseTypeDef",
    "GetVpcLinkRequestTypeDef",
    "GetVpcLinkResponseTypeDef",
    "GetVpcLinksRequestTypeDef",
    "GetVpcLinksResponseTypeDef",
    "ImportApiRequestTypeDef",
    "ImportApiResponseTypeDef",
    "IntegrationResponseTypeDef",
    "IntegrationTypeDef",
    "JWTConfigurationOutputTypeDef",
    "JWTConfigurationTypeDef",
    "JWTConfigurationUnionTypeDef",
    "ModelTypeDef",
    "MutualTlsAuthenticationInputTypeDef",
    "MutualTlsAuthenticationTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterConstraintsTypeDef",
    "ReimportApiRequestTypeDef",
    "ReimportApiResponseTypeDef",
    "ResetAuthorizersCacheRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RouteResponseTypeDef",
    "RouteSettingsTypeDef",
    "RouteTypeDef",
    "StageTypeDef",
    "TagResourceRequestTypeDef",
    "TimestampTypeDef",
    "TlsConfigInputTypeDef",
    "TlsConfigTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateApiMappingRequestTypeDef",
    "UpdateApiMappingResponseTypeDef",
    "UpdateApiRequestTypeDef",
    "UpdateApiResponseTypeDef",
    "UpdateAuthorizerRequestTypeDef",
    "UpdateAuthorizerResponseTypeDef",
    "UpdateDeploymentRequestTypeDef",
    "UpdateDeploymentResponseTypeDef",
    "UpdateDomainNameRequestTypeDef",
    "UpdateDomainNameResponseTypeDef",
    "UpdateIntegrationRequestTypeDef",
    "UpdateIntegrationResponseRequestTypeDef",
    "UpdateIntegrationResponseResponseTypeDef",
    "UpdateIntegrationResultTypeDef",
    "UpdateModelRequestTypeDef",
    "UpdateModelResponseTypeDef",
    "UpdateRouteRequestTypeDef",
    "UpdateRouteResponseRequestTypeDef",
    "UpdateRouteResponseResponseTypeDef",
    "UpdateRouteResultTypeDef",
    "UpdateStageRequestTypeDef",
    "UpdateStageResponseTypeDef",
    "UpdateVpcLinkRequestTypeDef",
    "UpdateVpcLinkResponseTypeDef",
    "VpcLinkTypeDef",
)

class AccessLogSettingsTypeDef(TypedDict):
    DestinationArn: NotRequired[str]
    Format: NotRequired[str]

class ApiMappingTypeDef(TypedDict):
    ApiId: str
    Stage: str
    ApiMappingId: NotRequired[str]
    ApiMappingKey: NotRequired[str]

class CorsOutputTypeDef(TypedDict):
    AllowCredentials: NotRequired[bool]
    AllowHeaders: NotRequired[List[str]]
    AllowMethods: NotRequired[List[str]]
    AllowOrigins: NotRequired[List[str]]
    ExposeHeaders: NotRequired[List[str]]
    MaxAge: NotRequired[int]

class JWTConfigurationOutputTypeDef(TypedDict):
    Audience: NotRequired[List[str]]
    Issuer: NotRequired[str]

class CorsTypeDef(TypedDict):
    AllowCredentials: NotRequired[bool]
    AllowHeaders: NotRequired[Sequence[str]]
    AllowMethods: NotRequired[Sequence[str]]
    AllowOrigins: NotRequired[Sequence[str]]
    ExposeHeaders: NotRequired[Sequence[str]]
    MaxAge: NotRequired[int]

class CreateApiMappingRequestTypeDef(TypedDict):
    ApiId: str
    DomainName: str
    Stage: str
    ApiMappingKey: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateDeploymentRequestTypeDef(TypedDict):
    ApiId: str
    Description: NotRequired[str]
    StageName: NotRequired[str]

class MutualTlsAuthenticationInputTypeDef(TypedDict):
    TruststoreUri: NotRequired[str]
    TruststoreVersion: NotRequired[str]

class DomainNameConfigurationOutputTypeDef(TypedDict):
    ApiGatewayDomainName: NotRequired[str]
    CertificateArn: NotRequired[str]
    CertificateName: NotRequired[str]
    CertificateUploadDate: NotRequired[datetime]
    DomainNameStatus: NotRequired[DomainNameStatusType]
    DomainNameStatusMessage: NotRequired[str]
    EndpointType: NotRequired[EndpointTypeType]
    HostedZoneId: NotRequired[str]
    IpAddressType: NotRequired[IpAddressTypeType]
    SecurityPolicy: NotRequired[SecurityPolicyType]
    OwnershipVerificationCertificateArn: NotRequired[str]

class MutualTlsAuthenticationTypeDef(TypedDict):
    TruststoreUri: NotRequired[str]
    TruststoreVersion: NotRequired[str]
    TruststoreWarnings: NotRequired[List[str]]

class TlsConfigInputTypeDef(TypedDict):
    ServerNameToVerify: NotRequired[str]

class CreateIntegrationResponseRequestTypeDef(TypedDict):
    ApiId: str
    IntegrationId: str
    IntegrationResponseKey: str
    ContentHandlingStrategy: NotRequired[ContentHandlingStrategyType]
    ResponseParameters: NotRequired[Mapping[str, str]]
    ResponseTemplates: NotRequired[Mapping[str, str]]
    TemplateSelectionExpression: NotRequired[str]

class TlsConfigTypeDef(TypedDict):
    ServerNameToVerify: NotRequired[str]

class CreateModelRequestTypeDef(TypedDict):
    ApiId: str
    Name: str
    Schema: str
    ContentType: NotRequired[str]
    Description: NotRequired[str]

ParameterConstraintsTypeDef = TypedDict(
    "ParameterConstraintsTypeDef",
    {
        "Required": NotRequired[bool],
    },
)

class RouteSettingsTypeDef(TypedDict):
    DataTraceEnabled: NotRequired[bool]
    DetailedMetricsEnabled: NotRequired[bool]
    LoggingLevel: NotRequired[LoggingLevelType]
    ThrottlingBurstLimit: NotRequired[int]
    ThrottlingRateLimit: NotRequired[float]

class CreateVpcLinkRequestTypeDef(TypedDict):
    Name: str
    SubnetIds: Sequence[str]
    SecurityGroupIds: NotRequired[Sequence[str]]
    Tags: NotRequired[Mapping[str, str]]

class DeleteAccessLogSettingsRequestTypeDef(TypedDict):
    ApiId: str
    StageName: str

class DeleteApiMappingRequestTypeDef(TypedDict):
    ApiMappingId: str
    DomainName: str

class DeleteApiRequestTypeDef(TypedDict):
    ApiId: str

class DeleteAuthorizerRequestTypeDef(TypedDict):
    ApiId: str
    AuthorizerId: str

class DeleteCorsConfigurationRequestTypeDef(TypedDict):
    ApiId: str

class DeleteDeploymentRequestTypeDef(TypedDict):
    ApiId: str
    DeploymentId: str

class DeleteDomainNameRequestTypeDef(TypedDict):
    DomainName: str

class DeleteIntegrationRequestTypeDef(TypedDict):
    ApiId: str
    IntegrationId: str

class DeleteIntegrationResponseRequestTypeDef(TypedDict):
    ApiId: str
    IntegrationId: str
    IntegrationResponseId: str

class DeleteModelRequestTypeDef(TypedDict):
    ApiId: str
    ModelId: str

class DeleteRouteRequestParameterRequestTypeDef(TypedDict):
    ApiId: str
    RequestParameterKey: str
    RouteId: str

class DeleteRouteRequestTypeDef(TypedDict):
    ApiId: str
    RouteId: str

class DeleteRouteResponseRequestTypeDef(TypedDict):
    ApiId: str
    RouteId: str
    RouteResponseId: str

class DeleteRouteSettingsRequestTypeDef(TypedDict):
    ApiId: str
    RouteKey: str
    StageName: str

class DeleteStageRequestTypeDef(TypedDict):
    ApiId: str
    StageName: str

class DeleteVpcLinkRequestTypeDef(TypedDict):
    VpcLinkId: str

class DeploymentTypeDef(TypedDict):
    AutoDeployed: NotRequired[bool]
    CreatedDate: NotRequired[datetime]
    DeploymentId: NotRequired[str]
    DeploymentStatus: NotRequired[DeploymentStatusType]
    DeploymentStatusMessage: NotRequired[str]
    Description: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class ExportApiRequestTypeDef(TypedDict):
    ApiId: str
    OutputType: JSONYAMLType
    Specification: Literal["OAS30"]
    ExportVersion: NotRequired[str]
    IncludeExtensions: NotRequired[bool]
    StageName: NotRequired[str]

class GetApiMappingRequestTypeDef(TypedDict):
    ApiMappingId: str
    DomainName: str

class GetApiMappingsRequestTypeDef(TypedDict):
    DomainName: str
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class GetApiRequestTypeDef(TypedDict):
    ApiId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetApisRequestTypeDef(TypedDict):
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class GetAuthorizerRequestTypeDef(TypedDict):
    ApiId: str
    AuthorizerId: str

class GetAuthorizersRequestTypeDef(TypedDict):
    ApiId: str
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class GetDeploymentRequestTypeDef(TypedDict):
    ApiId: str
    DeploymentId: str

class GetDeploymentsRequestTypeDef(TypedDict):
    ApiId: str
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class GetDomainNameRequestTypeDef(TypedDict):
    DomainName: str

class GetDomainNamesRequestTypeDef(TypedDict):
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class GetIntegrationRequestTypeDef(TypedDict):
    ApiId: str
    IntegrationId: str

class GetIntegrationResponseRequestTypeDef(TypedDict):
    ApiId: str
    IntegrationId: str
    IntegrationResponseId: str

class GetIntegrationResponsesRequestTypeDef(TypedDict):
    ApiId: str
    IntegrationId: str
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class IntegrationResponseTypeDef(TypedDict):
    IntegrationResponseKey: str
    ContentHandlingStrategy: NotRequired[ContentHandlingStrategyType]
    IntegrationResponseId: NotRequired[str]
    ResponseParameters: NotRequired[Dict[str, str]]
    ResponseTemplates: NotRequired[Dict[str, str]]
    TemplateSelectionExpression: NotRequired[str]

class GetIntegrationsRequestTypeDef(TypedDict):
    ApiId: str
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class GetModelRequestTypeDef(TypedDict):
    ApiId: str
    ModelId: str

class GetModelTemplateRequestTypeDef(TypedDict):
    ApiId: str
    ModelId: str

class GetModelsRequestTypeDef(TypedDict):
    ApiId: str
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class ModelTypeDef(TypedDict):
    Name: str
    ContentType: NotRequired[str]
    Description: NotRequired[str]
    ModelId: NotRequired[str]
    Schema: NotRequired[str]

class GetRouteRequestTypeDef(TypedDict):
    ApiId: str
    RouteId: str

class GetRouteResponseRequestTypeDef(TypedDict):
    ApiId: str
    RouteId: str
    RouteResponseId: str

class GetRouteResponsesRequestTypeDef(TypedDict):
    ApiId: str
    RouteId: str
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class GetRoutesRequestTypeDef(TypedDict):
    ApiId: str
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class GetStageRequestTypeDef(TypedDict):
    ApiId: str
    StageName: str

class GetStagesRequestTypeDef(TypedDict):
    ApiId: str
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class GetTagsRequestTypeDef(TypedDict):
    ResourceArn: str

class GetVpcLinkRequestTypeDef(TypedDict):
    VpcLinkId: str

class GetVpcLinksRequestTypeDef(TypedDict):
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class VpcLinkTypeDef(TypedDict):
    Name: str
    SecurityGroupIds: List[str]
    SubnetIds: List[str]
    VpcLinkId: str
    CreatedDate: NotRequired[datetime]
    Tags: NotRequired[Dict[str, str]]
    VpcLinkStatus: NotRequired[VpcLinkStatusType]
    VpcLinkStatusMessage: NotRequired[str]
    VpcLinkVersion: NotRequired[Literal["V2"]]

class ImportApiRequestTypeDef(TypedDict):
    Body: str
    Basepath: NotRequired[str]
    FailOnWarnings: NotRequired[bool]

class JWTConfigurationTypeDef(TypedDict):
    Audience: NotRequired[Sequence[str]]
    Issuer: NotRequired[str]

class ReimportApiRequestTypeDef(TypedDict):
    ApiId: str
    Body: str
    Basepath: NotRequired[str]
    FailOnWarnings: NotRequired[bool]

class ResetAuthorizersCacheRequestTypeDef(TypedDict):
    ApiId: str
    StageName: str

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: NotRequired[Mapping[str, str]]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateApiMappingRequestTypeDef(TypedDict):
    ApiId: str
    ApiMappingId: str
    DomainName: str
    ApiMappingKey: NotRequired[str]
    Stage: NotRequired[str]

class UpdateDeploymentRequestTypeDef(TypedDict):
    ApiId: str
    DeploymentId: str
    Description: NotRequired[str]

class UpdateIntegrationResponseRequestTypeDef(TypedDict):
    ApiId: str
    IntegrationId: str
    IntegrationResponseId: str
    ContentHandlingStrategy: NotRequired[ContentHandlingStrategyType]
    IntegrationResponseKey: NotRequired[str]
    ResponseParameters: NotRequired[Mapping[str, str]]
    ResponseTemplates: NotRequired[Mapping[str, str]]
    TemplateSelectionExpression: NotRequired[str]

class UpdateModelRequestTypeDef(TypedDict):
    ApiId: str
    ModelId: str
    ContentType: NotRequired[str]
    Description: NotRequired[str]
    Name: NotRequired[str]
    Schema: NotRequired[str]

class UpdateVpcLinkRequestTypeDef(TypedDict):
    VpcLinkId: str
    Name: NotRequired[str]

class ApiTypeDef(TypedDict):
    Name: str
    ProtocolType: ProtocolTypeType
    RouteSelectionExpression: str
    ApiEndpoint: NotRequired[str]
    ApiGatewayManaged: NotRequired[bool]
    ApiId: NotRequired[str]
    ApiKeySelectionExpression: NotRequired[str]
    CorsConfiguration: NotRequired[CorsOutputTypeDef]
    CreatedDate: NotRequired[datetime]
    Description: NotRequired[str]
    DisableSchemaValidation: NotRequired[bool]
    DisableExecuteApiEndpoint: NotRequired[bool]
    ImportInfo: NotRequired[List[str]]
    IpAddressType: NotRequired[IpAddressTypeType]
    Tags: NotRequired[Dict[str, str]]
    Version: NotRequired[str]
    Warnings: NotRequired[List[str]]

class AuthorizerTypeDef(TypedDict):
    Name: str
    AuthorizerCredentialsArn: NotRequired[str]
    AuthorizerId: NotRequired[str]
    AuthorizerPayloadFormatVersion: NotRequired[str]
    AuthorizerResultTtlInSeconds: NotRequired[int]
    AuthorizerType: NotRequired[AuthorizerTypeType]
    AuthorizerUri: NotRequired[str]
    EnableSimpleResponses: NotRequired[bool]
    IdentitySource: NotRequired[List[str]]
    IdentityValidationExpression: NotRequired[str]
    JwtConfiguration: NotRequired[JWTConfigurationOutputTypeDef]

CorsUnionTypeDef = Union[CorsTypeDef, CorsOutputTypeDef]

class CreateApiMappingResponseTypeDef(TypedDict):
    ApiId: str
    ApiMappingId: str
    ApiMappingKey: str
    Stage: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApiResponseTypeDef(TypedDict):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: CorsOutputTypeDef
    CreatedDate: datetime
    Description: str
    DisableSchemaValidation: bool
    DisableExecuteApiEndpoint: bool
    ImportInfo: List[str]
    IpAddressType: IpAddressTypeType
    Name: str
    ProtocolType: ProtocolTypeType
    RouteSelectionExpression: str
    Tags: Dict[str, str]
    Version: str
    Warnings: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAuthorizerResponseTypeDef(TypedDict):
    AuthorizerCredentialsArn: str
    AuthorizerId: str
    AuthorizerPayloadFormatVersion: str
    AuthorizerResultTtlInSeconds: int
    AuthorizerType: AuthorizerTypeType
    AuthorizerUri: str
    EnableSimpleResponses: bool
    IdentitySource: List[str]
    IdentityValidationExpression: str
    JwtConfiguration: JWTConfigurationOutputTypeDef
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentResponseTypeDef(TypedDict):
    AutoDeployed: bool
    CreatedDate: datetime
    DeploymentId: str
    DeploymentStatus: DeploymentStatusType
    DeploymentStatusMessage: str
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIntegrationResponseResponseTypeDef(TypedDict):
    ContentHandlingStrategy: ContentHandlingStrategyType
    IntegrationResponseId: str
    IntegrationResponseKey: str
    ResponseParameters: Dict[str, str]
    ResponseTemplates: Dict[str, str]
    TemplateSelectionExpression: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelResponseTypeDef(TypedDict):
    ContentType: str
    Description: str
    ModelId: str
    Name: str
    Schema: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpcLinkResponseTypeDef(TypedDict):
    CreatedDate: datetime
    Name: str
    SecurityGroupIds: List[str]
    SubnetIds: List[str]
    Tags: Dict[str, str]
    VpcLinkId: str
    VpcLinkStatus: VpcLinkStatusType
    VpcLinkStatusMessage: str
    VpcLinkVersion: Literal["V2"]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ExportApiResponseTypeDef(TypedDict):
    body: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetApiMappingResponseTypeDef(TypedDict):
    ApiId: str
    ApiMappingId: str
    ApiMappingKey: str
    Stage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetApiMappingsResponseTypeDef(TypedDict):
    Items: List[ApiMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetApiResponseTypeDef(TypedDict):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: CorsOutputTypeDef
    CreatedDate: datetime
    Description: str
    DisableSchemaValidation: bool
    DisableExecuteApiEndpoint: bool
    ImportInfo: List[str]
    IpAddressType: IpAddressTypeType
    Name: str
    ProtocolType: ProtocolTypeType
    RouteSelectionExpression: str
    Tags: Dict[str, str]
    Version: str
    Warnings: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetAuthorizerResponseTypeDef(TypedDict):
    AuthorizerCredentialsArn: str
    AuthorizerId: str
    AuthorizerPayloadFormatVersion: str
    AuthorizerResultTtlInSeconds: int
    AuthorizerType: AuthorizerTypeType
    AuthorizerUri: str
    EnableSimpleResponses: bool
    IdentitySource: List[str]
    IdentityValidationExpression: str
    JwtConfiguration: JWTConfigurationOutputTypeDef
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentResponseTypeDef(TypedDict):
    AutoDeployed: bool
    CreatedDate: datetime
    DeploymentId: str
    DeploymentStatus: DeploymentStatusType
    DeploymentStatusMessage: str
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIntegrationResponseResponseTypeDef(TypedDict):
    ContentHandlingStrategy: ContentHandlingStrategyType
    IntegrationResponseId: str
    IntegrationResponseKey: str
    ResponseParameters: Dict[str, str]
    ResponseTemplates: Dict[str, str]
    TemplateSelectionExpression: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetModelResponseTypeDef(TypedDict):
    ContentType: str
    Description: str
    ModelId: str
    Name: str
    Schema: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetModelTemplateResponseTypeDef(TypedDict):
    Value: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTagsResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetVpcLinkResponseTypeDef(TypedDict):
    CreatedDate: datetime
    Name: str
    SecurityGroupIds: List[str]
    SubnetIds: List[str]
    Tags: Dict[str, str]
    VpcLinkId: str
    VpcLinkStatus: VpcLinkStatusType
    VpcLinkStatusMessage: str
    VpcLinkVersion: Literal["V2"]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportApiResponseTypeDef(TypedDict):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: CorsOutputTypeDef
    CreatedDate: datetime
    Description: str
    DisableSchemaValidation: bool
    DisableExecuteApiEndpoint: bool
    ImportInfo: List[str]
    IpAddressType: IpAddressTypeType
    Name: str
    ProtocolType: ProtocolTypeType
    RouteSelectionExpression: str
    Tags: Dict[str, str]
    Version: str
    Warnings: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ReimportApiResponseTypeDef(TypedDict):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: CorsOutputTypeDef
    CreatedDate: datetime
    Description: str
    DisableSchemaValidation: bool
    DisableExecuteApiEndpoint: bool
    ImportInfo: List[str]
    IpAddressType: IpAddressTypeType
    Name: str
    ProtocolType: ProtocolTypeType
    RouteSelectionExpression: str
    Tags: Dict[str, str]
    Version: str
    Warnings: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApiMappingResponseTypeDef(TypedDict):
    ApiId: str
    ApiMappingId: str
    ApiMappingKey: str
    Stage: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApiResponseTypeDef(TypedDict):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: CorsOutputTypeDef
    CreatedDate: datetime
    Description: str
    DisableSchemaValidation: bool
    DisableExecuteApiEndpoint: bool
    ImportInfo: List[str]
    IpAddressType: IpAddressTypeType
    Name: str
    ProtocolType: ProtocolTypeType
    RouteSelectionExpression: str
    Tags: Dict[str, str]
    Version: str
    Warnings: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAuthorizerResponseTypeDef(TypedDict):
    AuthorizerCredentialsArn: str
    AuthorizerId: str
    AuthorizerPayloadFormatVersion: str
    AuthorizerResultTtlInSeconds: int
    AuthorizerType: AuthorizerTypeType
    AuthorizerUri: str
    EnableSimpleResponses: bool
    IdentitySource: List[str]
    IdentityValidationExpression: str
    JwtConfiguration: JWTConfigurationOutputTypeDef
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDeploymentResponseTypeDef(TypedDict):
    AutoDeployed: bool
    CreatedDate: datetime
    DeploymentId: str
    DeploymentStatus: DeploymentStatusType
    DeploymentStatusMessage: str
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIntegrationResponseResponseTypeDef(TypedDict):
    ContentHandlingStrategy: ContentHandlingStrategyType
    IntegrationResponseId: str
    IntegrationResponseKey: str
    ResponseParameters: Dict[str, str]
    ResponseTemplates: Dict[str, str]
    TemplateSelectionExpression: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateModelResponseTypeDef(TypedDict):
    ContentType: str
    Description: str
    ModelId: str
    Name: str
    Schema: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVpcLinkResponseTypeDef(TypedDict):
    CreatedDate: datetime
    Name: str
    SecurityGroupIds: List[str]
    SubnetIds: List[str]
    Tags: Dict[str, str]
    VpcLinkId: str
    VpcLinkStatus: VpcLinkStatusType
    VpcLinkStatusMessage: str
    VpcLinkVersion: Literal["V2"]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainNameResponseTypeDef(TypedDict):
    ApiMappingSelectionExpression: str
    DomainName: str
    DomainNameConfigurations: List[DomainNameConfigurationOutputTypeDef]
    MutualTlsAuthentication: MutualTlsAuthenticationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DomainNameTypeDef(TypedDict):
    DomainName: str
    ApiMappingSelectionExpression: NotRequired[str]
    DomainNameConfigurations: NotRequired[List[DomainNameConfigurationOutputTypeDef]]
    MutualTlsAuthentication: NotRequired[MutualTlsAuthenticationTypeDef]
    Tags: NotRequired[Dict[str, str]]

class GetDomainNameResponseTypeDef(TypedDict):
    ApiMappingSelectionExpression: str
    DomainName: str
    DomainNameConfigurations: List[DomainNameConfigurationOutputTypeDef]
    MutualTlsAuthentication: MutualTlsAuthenticationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainNameResponseTypeDef(TypedDict):
    ApiMappingSelectionExpression: str
    DomainName: str
    DomainNameConfigurations: List[DomainNameConfigurationOutputTypeDef]
    MutualTlsAuthentication: MutualTlsAuthenticationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIntegrationRequestTypeDef(TypedDict):
    ApiId: str
    IntegrationType: IntegrationTypeType
    ConnectionId: NotRequired[str]
    ConnectionType: NotRequired[ConnectionTypeType]
    ContentHandlingStrategy: NotRequired[ContentHandlingStrategyType]
    CredentialsArn: NotRequired[str]
    Description: NotRequired[str]
    IntegrationMethod: NotRequired[str]
    IntegrationSubtype: NotRequired[str]
    IntegrationUri: NotRequired[str]
    PassthroughBehavior: NotRequired[PassthroughBehaviorType]
    PayloadFormatVersion: NotRequired[str]
    RequestParameters: NotRequired[Mapping[str, str]]
    RequestTemplates: NotRequired[Mapping[str, str]]
    ResponseParameters: NotRequired[Mapping[str, Mapping[str, str]]]
    TemplateSelectionExpression: NotRequired[str]
    TimeoutInMillis: NotRequired[int]
    TlsConfig: NotRequired[TlsConfigInputTypeDef]

class UpdateIntegrationRequestTypeDef(TypedDict):
    ApiId: str
    IntegrationId: str
    ConnectionId: NotRequired[str]
    ConnectionType: NotRequired[ConnectionTypeType]
    ContentHandlingStrategy: NotRequired[ContentHandlingStrategyType]
    CredentialsArn: NotRequired[str]
    Description: NotRequired[str]
    IntegrationMethod: NotRequired[str]
    IntegrationSubtype: NotRequired[str]
    IntegrationType: NotRequired[IntegrationTypeType]
    IntegrationUri: NotRequired[str]
    PassthroughBehavior: NotRequired[PassthroughBehaviorType]
    PayloadFormatVersion: NotRequired[str]
    RequestParameters: NotRequired[Mapping[str, str]]
    RequestTemplates: NotRequired[Mapping[str, str]]
    ResponseParameters: NotRequired[Mapping[str, Mapping[str, str]]]
    TemplateSelectionExpression: NotRequired[str]
    TimeoutInMillis: NotRequired[int]
    TlsConfig: NotRequired[TlsConfigInputTypeDef]

class CreateIntegrationResultTypeDef(TypedDict):
    ApiGatewayManaged: bool
    ConnectionId: str
    ConnectionType: ConnectionTypeType
    ContentHandlingStrategy: ContentHandlingStrategyType
    CredentialsArn: str
    Description: str
    IntegrationId: str
    IntegrationMethod: str
    IntegrationResponseSelectionExpression: str
    IntegrationSubtype: str
    IntegrationType: IntegrationTypeType
    IntegrationUri: str
    PassthroughBehavior: PassthroughBehaviorType
    PayloadFormatVersion: str
    RequestParameters: Dict[str, str]
    RequestTemplates: Dict[str, str]
    ResponseParameters: Dict[str, Dict[str, str]]
    TemplateSelectionExpression: str
    TimeoutInMillis: int
    TlsConfig: TlsConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIntegrationResultTypeDef(TypedDict):
    ApiGatewayManaged: bool
    ConnectionId: str
    ConnectionType: ConnectionTypeType
    ContentHandlingStrategy: ContentHandlingStrategyType
    CredentialsArn: str
    Description: str
    IntegrationId: str
    IntegrationMethod: str
    IntegrationResponseSelectionExpression: str
    IntegrationSubtype: str
    IntegrationType: IntegrationTypeType
    IntegrationUri: str
    PassthroughBehavior: PassthroughBehaviorType
    PayloadFormatVersion: str
    RequestParameters: Dict[str, str]
    RequestTemplates: Dict[str, str]
    ResponseParameters: Dict[str, Dict[str, str]]
    TemplateSelectionExpression: str
    TimeoutInMillis: int
    TlsConfig: TlsConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IntegrationTypeDef(TypedDict):
    ApiGatewayManaged: NotRequired[bool]
    ConnectionId: NotRequired[str]
    ConnectionType: NotRequired[ConnectionTypeType]
    ContentHandlingStrategy: NotRequired[ContentHandlingStrategyType]
    CredentialsArn: NotRequired[str]
    Description: NotRequired[str]
    IntegrationId: NotRequired[str]
    IntegrationMethod: NotRequired[str]
    IntegrationResponseSelectionExpression: NotRequired[str]
    IntegrationSubtype: NotRequired[str]
    IntegrationType: NotRequired[IntegrationTypeType]
    IntegrationUri: NotRequired[str]
    PassthroughBehavior: NotRequired[PassthroughBehaviorType]
    PayloadFormatVersion: NotRequired[str]
    RequestParameters: NotRequired[Dict[str, str]]
    RequestTemplates: NotRequired[Dict[str, str]]
    ResponseParameters: NotRequired[Dict[str, Dict[str, str]]]
    TemplateSelectionExpression: NotRequired[str]
    TimeoutInMillis: NotRequired[int]
    TlsConfig: NotRequired[TlsConfigTypeDef]

class UpdateIntegrationResultTypeDef(TypedDict):
    ApiGatewayManaged: bool
    ConnectionId: str
    ConnectionType: ConnectionTypeType
    ContentHandlingStrategy: ContentHandlingStrategyType
    CredentialsArn: str
    Description: str
    IntegrationId: str
    IntegrationMethod: str
    IntegrationResponseSelectionExpression: str
    IntegrationSubtype: str
    IntegrationType: IntegrationTypeType
    IntegrationUri: str
    PassthroughBehavior: PassthroughBehaviorType
    PayloadFormatVersion: str
    RequestParameters: Dict[str, str]
    RequestTemplates: Dict[str, str]
    ResponseParameters: Dict[str, Dict[str, str]]
    TemplateSelectionExpression: str
    TimeoutInMillis: int
    TlsConfig: TlsConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRouteRequestTypeDef(TypedDict):
    ApiId: str
    RouteKey: str
    ApiKeyRequired: NotRequired[bool]
    AuthorizationScopes: NotRequired[Sequence[str]]
    AuthorizationType: NotRequired[AuthorizationTypeType]
    AuthorizerId: NotRequired[str]
    ModelSelectionExpression: NotRequired[str]
    OperationName: NotRequired[str]
    RequestModels: NotRequired[Mapping[str, str]]
    RequestParameters: NotRequired[Mapping[str, ParameterConstraintsTypeDef]]
    RouteResponseSelectionExpression: NotRequired[str]
    Target: NotRequired[str]

class CreateRouteResponseRequestTypeDef(TypedDict):
    ApiId: str
    RouteId: str
    RouteResponseKey: str
    ModelSelectionExpression: NotRequired[str]
    ResponseModels: NotRequired[Mapping[str, str]]
    ResponseParameters: NotRequired[Mapping[str, ParameterConstraintsTypeDef]]

class CreateRouteResponseResponseTypeDef(TypedDict):
    ModelSelectionExpression: str
    ResponseModels: Dict[str, str]
    ResponseParameters: Dict[str, ParameterConstraintsTypeDef]
    RouteResponseId: str
    RouteResponseKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRouteResultTypeDef(TypedDict):
    ApiGatewayManaged: bool
    ApiKeyRequired: bool
    AuthorizationScopes: List[str]
    AuthorizationType: AuthorizationTypeType
    AuthorizerId: str
    ModelSelectionExpression: str
    OperationName: str
    RequestModels: Dict[str, str]
    RequestParameters: Dict[str, ParameterConstraintsTypeDef]
    RouteId: str
    RouteKey: str
    RouteResponseSelectionExpression: str
    Target: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRouteResponseResponseTypeDef(TypedDict):
    ModelSelectionExpression: str
    ResponseModels: Dict[str, str]
    ResponseParameters: Dict[str, ParameterConstraintsTypeDef]
    RouteResponseId: str
    RouteResponseKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRouteResultTypeDef(TypedDict):
    ApiGatewayManaged: bool
    ApiKeyRequired: bool
    AuthorizationScopes: List[str]
    AuthorizationType: AuthorizationTypeType
    AuthorizerId: str
    ModelSelectionExpression: str
    OperationName: str
    RequestModels: Dict[str, str]
    RequestParameters: Dict[str, ParameterConstraintsTypeDef]
    RouteId: str
    RouteKey: str
    RouteResponseSelectionExpression: str
    Target: str
    ResponseMetadata: ResponseMetadataTypeDef

class RouteResponseTypeDef(TypedDict):
    RouteResponseKey: str
    ModelSelectionExpression: NotRequired[str]
    ResponseModels: NotRequired[Dict[str, str]]
    ResponseParameters: NotRequired[Dict[str, ParameterConstraintsTypeDef]]
    RouteResponseId: NotRequired[str]

class RouteTypeDef(TypedDict):
    RouteKey: str
    ApiGatewayManaged: NotRequired[bool]
    ApiKeyRequired: NotRequired[bool]
    AuthorizationScopes: NotRequired[List[str]]
    AuthorizationType: NotRequired[AuthorizationTypeType]
    AuthorizerId: NotRequired[str]
    ModelSelectionExpression: NotRequired[str]
    OperationName: NotRequired[str]
    RequestModels: NotRequired[Dict[str, str]]
    RequestParameters: NotRequired[Dict[str, ParameterConstraintsTypeDef]]
    RouteId: NotRequired[str]
    RouteResponseSelectionExpression: NotRequired[str]
    Target: NotRequired[str]

class UpdateRouteRequestTypeDef(TypedDict):
    ApiId: str
    RouteId: str
    ApiKeyRequired: NotRequired[bool]
    AuthorizationScopes: NotRequired[Sequence[str]]
    AuthorizationType: NotRequired[AuthorizationTypeType]
    AuthorizerId: NotRequired[str]
    ModelSelectionExpression: NotRequired[str]
    OperationName: NotRequired[str]
    RequestModels: NotRequired[Mapping[str, str]]
    RequestParameters: NotRequired[Mapping[str, ParameterConstraintsTypeDef]]
    RouteKey: NotRequired[str]
    RouteResponseSelectionExpression: NotRequired[str]
    Target: NotRequired[str]

class UpdateRouteResponseRequestTypeDef(TypedDict):
    ApiId: str
    RouteId: str
    RouteResponseId: str
    ModelSelectionExpression: NotRequired[str]
    ResponseModels: NotRequired[Mapping[str, str]]
    ResponseParameters: NotRequired[Mapping[str, ParameterConstraintsTypeDef]]
    RouteResponseKey: NotRequired[str]

class UpdateRouteResponseResponseTypeDef(TypedDict):
    ModelSelectionExpression: str
    ResponseModels: Dict[str, str]
    ResponseParameters: Dict[str, ParameterConstraintsTypeDef]
    RouteResponseId: str
    RouteResponseKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRouteResultTypeDef(TypedDict):
    ApiGatewayManaged: bool
    ApiKeyRequired: bool
    AuthorizationScopes: List[str]
    AuthorizationType: AuthorizationTypeType
    AuthorizerId: str
    ModelSelectionExpression: str
    OperationName: str
    RequestModels: Dict[str, str]
    RequestParameters: Dict[str, ParameterConstraintsTypeDef]
    RouteId: str
    RouteKey: str
    RouteResponseSelectionExpression: str
    Target: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStageRequestTypeDef(TypedDict):
    ApiId: str
    StageName: str
    AccessLogSettings: NotRequired[AccessLogSettingsTypeDef]
    AutoDeploy: NotRequired[bool]
    ClientCertificateId: NotRequired[str]
    DefaultRouteSettings: NotRequired[RouteSettingsTypeDef]
    DeploymentId: NotRequired[str]
    Description: NotRequired[str]
    RouteSettings: NotRequired[Mapping[str, RouteSettingsTypeDef]]
    StageVariables: NotRequired[Mapping[str, str]]
    Tags: NotRequired[Mapping[str, str]]

class CreateStageResponseTypeDef(TypedDict):
    AccessLogSettings: AccessLogSettingsTypeDef
    ApiGatewayManaged: bool
    AutoDeploy: bool
    ClientCertificateId: str
    CreatedDate: datetime
    DefaultRouteSettings: RouteSettingsTypeDef
    DeploymentId: str
    Description: str
    LastDeploymentStatusMessage: str
    LastUpdatedDate: datetime
    RouteSettings: Dict[str, RouteSettingsTypeDef]
    StageName: str
    StageVariables: Dict[str, str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetStageResponseTypeDef(TypedDict):
    AccessLogSettings: AccessLogSettingsTypeDef
    ApiGatewayManaged: bool
    AutoDeploy: bool
    ClientCertificateId: str
    CreatedDate: datetime
    DefaultRouteSettings: RouteSettingsTypeDef
    DeploymentId: str
    Description: str
    LastDeploymentStatusMessage: str
    LastUpdatedDate: datetime
    RouteSettings: Dict[str, RouteSettingsTypeDef]
    StageName: str
    StageVariables: Dict[str, str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StageTypeDef(TypedDict):
    StageName: str
    AccessLogSettings: NotRequired[AccessLogSettingsTypeDef]
    ApiGatewayManaged: NotRequired[bool]
    AutoDeploy: NotRequired[bool]
    ClientCertificateId: NotRequired[str]
    CreatedDate: NotRequired[datetime]
    DefaultRouteSettings: NotRequired[RouteSettingsTypeDef]
    DeploymentId: NotRequired[str]
    Description: NotRequired[str]
    LastDeploymentStatusMessage: NotRequired[str]
    LastUpdatedDate: NotRequired[datetime]
    RouteSettings: NotRequired[Dict[str, RouteSettingsTypeDef]]
    StageVariables: NotRequired[Dict[str, str]]
    Tags: NotRequired[Dict[str, str]]

class UpdateStageRequestTypeDef(TypedDict):
    ApiId: str
    StageName: str
    AccessLogSettings: NotRequired[AccessLogSettingsTypeDef]
    AutoDeploy: NotRequired[bool]
    ClientCertificateId: NotRequired[str]
    DefaultRouteSettings: NotRequired[RouteSettingsTypeDef]
    DeploymentId: NotRequired[str]
    Description: NotRequired[str]
    RouteSettings: NotRequired[Mapping[str, RouteSettingsTypeDef]]
    StageVariables: NotRequired[Mapping[str, str]]

class UpdateStageResponseTypeDef(TypedDict):
    AccessLogSettings: AccessLogSettingsTypeDef
    ApiGatewayManaged: bool
    AutoDeploy: bool
    ClientCertificateId: str
    CreatedDate: datetime
    DefaultRouteSettings: RouteSettingsTypeDef
    DeploymentId: str
    Description: str
    LastDeploymentStatusMessage: str
    LastUpdatedDate: datetime
    RouteSettings: Dict[str, RouteSettingsTypeDef]
    StageName: str
    StageVariables: Dict[str, str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentsResponseTypeDef(TypedDict):
    Items: List[DeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DomainNameConfigurationTypeDef(TypedDict):
    ApiGatewayDomainName: NotRequired[str]
    CertificateArn: NotRequired[str]
    CertificateName: NotRequired[str]
    CertificateUploadDate: NotRequired[TimestampTypeDef]
    DomainNameStatus: NotRequired[DomainNameStatusType]
    DomainNameStatusMessage: NotRequired[str]
    EndpointType: NotRequired[EndpointTypeType]
    HostedZoneId: NotRequired[str]
    IpAddressType: NotRequired[IpAddressTypeType]
    SecurityPolicy: NotRequired[SecurityPolicyType]
    OwnershipVerificationCertificateArn: NotRequired[str]

class GetApisRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetAuthorizersRequestPaginateTypeDef(TypedDict):
    ApiId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetDeploymentsRequestPaginateTypeDef(TypedDict):
    ApiId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetDomainNamesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetIntegrationResponsesRequestPaginateTypeDef(TypedDict):
    ApiId: str
    IntegrationId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetIntegrationsRequestPaginateTypeDef(TypedDict):
    ApiId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetModelsRequestPaginateTypeDef(TypedDict):
    ApiId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetRouteResponsesRequestPaginateTypeDef(TypedDict):
    ApiId: str
    RouteId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetRoutesRequestPaginateTypeDef(TypedDict):
    ApiId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetStagesRequestPaginateTypeDef(TypedDict):
    ApiId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetIntegrationResponsesResponseTypeDef(TypedDict):
    Items: List[IntegrationResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetModelsResponseTypeDef(TypedDict):
    Items: List[ModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetVpcLinksResponseTypeDef(TypedDict):
    Items: List[VpcLinkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

JWTConfigurationUnionTypeDef = Union[JWTConfigurationTypeDef, JWTConfigurationOutputTypeDef]

class GetApisResponseTypeDef(TypedDict):
    Items: List[ApiTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetAuthorizersResponseTypeDef(TypedDict):
    Items: List[AuthorizerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateApiRequestTypeDef(TypedDict):
    Name: str
    ProtocolType: ProtocolTypeType
    ApiKeySelectionExpression: NotRequired[str]
    CorsConfiguration: NotRequired[CorsUnionTypeDef]
    CredentialsArn: NotRequired[str]
    Description: NotRequired[str]
    DisableSchemaValidation: NotRequired[bool]
    DisableExecuteApiEndpoint: NotRequired[bool]
    IpAddressType: NotRequired[IpAddressTypeType]
    RouteKey: NotRequired[str]
    RouteSelectionExpression: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    Target: NotRequired[str]
    Version: NotRequired[str]

class UpdateApiRequestTypeDef(TypedDict):
    ApiId: str
    ApiKeySelectionExpression: NotRequired[str]
    CorsConfiguration: NotRequired[CorsUnionTypeDef]
    CredentialsArn: NotRequired[str]
    Description: NotRequired[str]
    DisableSchemaValidation: NotRequired[bool]
    DisableExecuteApiEndpoint: NotRequired[bool]
    IpAddressType: NotRequired[IpAddressTypeType]
    Name: NotRequired[str]
    RouteKey: NotRequired[str]
    RouteSelectionExpression: NotRequired[str]
    Target: NotRequired[str]
    Version: NotRequired[str]

class GetDomainNamesResponseTypeDef(TypedDict):
    Items: List[DomainNameTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetIntegrationsResponseTypeDef(TypedDict):
    Items: List[IntegrationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetRouteResponsesResponseTypeDef(TypedDict):
    Items: List[RouteResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetRoutesResponseTypeDef(TypedDict):
    Items: List[RouteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetStagesResponseTypeDef(TypedDict):
    Items: List[StageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

DomainNameConfigurationUnionTypeDef = Union[
    DomainNameConfigurationTypeDef, DomainNameConfigurationOutputTypeDef
]

class CreateAuthorizerRequestTypeDef(TypedDict):
    ApiId: str
    AuthorizerType: AuthorizerTypeType
    IdentitySource: Sequence[str]
    Name: str
    AuthorizerCredentialsArn: NotRequired[str]
    AuthorizerPayloadFormatVersion: NotRequired[str]
    AuthorizerResultTtlInSeconds: NotRequired[int]
    AuthorizerUri: NotRequired[str]
    EnableSimpleResponses: NotRequired[bool]
    IdentityValidationExpression: NotRequired[str]
    JwtConfiguration: NotRequired[JWTConfigurationUnionTypeDef]

class UpdateAuthorizerRequestTypeDef(TypedDict):
    ApiId: str
    AuthorizerId: str
    AuthorizerCredentialsArn: NotRequired[str]
    AuthorizerPayloadFormatVersion: NotRequired[str]
    AuthorizerResultTtlInSeconds: NotRequired[int]
    AuthorizerType: NotRequired[AuthorizerTypeType]
    AuthorizerUri: NotRequired[str]
    EnableSimpleResponses: NotRequired[bool]
    IdentitySource: NotRequired[Sequence[str]]
    IdentityValidationExpression: NotRequired[str]
    JwtConfiguration: NotRequired[JWTConfigurationUnionTypeDef]
    Name: NotRequired[str]

class CreateDomainNameRequestTypeDef(TypedDict):
    DomainName: str
    DomainNameConfigurations: NotRequired[Sequence[DomainNameConfigurationUnionTypeDef]]
    MutualTlsAuthentication: NotRequired[MutualTlsAuthenticationInputTypeDef]
    Tags: NotRequired[Mapping[str, str]]

class UpdateDomainNameRequestTypeDef(TypedDict):
    DomainName: str
    DomainNameConfigurations: NotRequired[Sequence[DomainNameConfigurationUnionTypeDef]]
    MutualTlsAuthentication: NotRequired[MutualTlsAuthenticationInputTypeDef]
