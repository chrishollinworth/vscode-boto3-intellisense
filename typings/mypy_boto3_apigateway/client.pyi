# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for apigateway service client

Usage::

    ```python
    import boto3
    from mypy_boto3_apigateway import APIGatewayClient

    client: APIGatewayClient = boto3.client("apigateway")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_apigateway.paginator import (
    GetApiKeysPaginator,
    GetAuthorizersPaginator,
    GetBasePathMappingsPaginator,
    GetClientCertificatesPaginator,
    GetDeploymentsPaginator,
    GetDocumentationPartsPaginator,
    GetDocumentationVersionsPaginator,
    GetDomainNamesPaginator,
    GetGatewayResponsesPaginator,
    GetModelsPaginator,
    GetRequestValidatorsPaginator,
    GetResourcesPaginator,
    GetRestApisPaginator,
    GetSdkTypesPaginator,
    GetUsagePaginator,
    GetUsagePlanKeysPaginator,
    GetUsagePlansPaginator,
    GetVpcLinksPaginator,
)
from mypy_boto3_apigateway.type_defs import (
    AccountTypeDef,
    ApiKeyIdsTypeDef,
    ApiKeysTypeDef,
    ApiKeyTypeDef,
    ApiStageTypeDef,
    AuthorizersTypeDef,
    AuthorizerTypeDef,
    BasePathMappingsTypeDef,
    BasePathMappingTypeDef,
    CanarySettingsTypeDef,
    ClientCertificatesTypeDef,
    ClientCertificateTypeDef,
    DeploymentCanarySettingsTypeDef,
    DeploymentsTypeDef,
    DeploymentTypeDef,
    DocumentationPartIdsTypeDef,
    DocumentationPartLocationTypeDef,
    DocumentationPartsTypeDef,
    DocumentationPartTypeDef,
    DocumentationVersionsTypeDef,
    DocumentationVersionTypeDef,
    DomainNamesTypeDef,
    DomainNameTypeDef,
    EndpointConfigurationTypeDef,
    ExportResponseTypeDef,
    GatewayResponsesTypeDef,
    GatewayResponseTypeDef,
    IntegrationResponseTypeDef,
    IntegrationTypeDef,
    MethodResponseTypeDef,
    MethodTypeDef,
    ModelsTypeDef,
    ModelTypeDef,
    PatchOperationTypeDef,
    QuotaSettingsTypeDef,
    RequestValidatorsTypeDef,
    RequestValidatorTypeDef,
    ResourcesTypeDef,
    ResourceTypeDef,
    RestApisTypeDef,
    RestApiTypeDef,
    SdkResponseTypeDef,
    SdkTypesTypeDef,
    SdkTypeTypeDef,
    StageKeyTypeDef,
    StagesTypeDef,
    StageTypeDef,
    TagsTypeDef,
    TemplateTypeDef,
    TestInvokeAuthorizerResponseTypeDef,
    TestInvokeMethodResponseTypeDef,
    ThrottleSettingsTypeDef,
    TlsConfigTypeDef,
    UsagePlanKeysTypeDef,
    UsagePlanKeyTypeDef,
    UsagePlansTypeDef,
    UsagePlanTypeDef,
    UsageTypeDef,
    VpcLinksTypeDef,
    VpcLinkTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("APIGatewayClient",)


class Exceptions:
    BadRequestException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    ConflictException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    NotFoundException: Type[Boto3ClientError]
    ServiceUnavailableException: Type[Boto3ClientError]
    TooManyRequestsException: Type[Boto3ClientError]
    UnauthorizedException: Type[Boto3ClientError]


class APIGatewayClient:
    """
    [APIGateway.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.can_paginate)
        """

    def create_api_key(
        self,
        name: str = None,
        description: str = None,
        enabled: bool = None,
        generateDistinctId: bool = None,
        value: str = None,
        stageKeys: List[StageKeyTypeDef] = None,
        customerId: str = None,
        tags: Dict[str, str] = None,
    ) -> "ApiKeyTypeDef":
        """
        [Client.create_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.create_api_key)
        """

    def create_authorizer(
        self,
        restApiId: str,
        name: str,
        type: Literal["TOKEN", "REQUEST", "COGNITO_USER_POOLS"],
        providerARNs: List[str] = None,
        authType: str = None,
        authorizerUri: str = None,
        authorizerCredentials: str = None,
        identitySource: str = None,
        identityValidationExpression: str = None,
        authorizerResultTtlInSeconds: int = None,
    ) -> "AuthorizerTypeDef":
        """
        [Client.create_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.create_authorizer)
        """

    def create_base_path_mapping(
        self, domainName: str, restApiId: str, basePath: str = None, stage: str = None
    ) -> "BasePathMappingTypeDef":
        """
        [Client.create_base_path_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.create_base_path_mapping)
        """

    def create_deployment(
        self,
        restApiId: str,
        stageName: str = None,
        stageDescription: str = None,
        description: str = None,
        cacheClusterEnabled: bool = None,
        cacheClusterSize: Literal["0.5", "1.6", "6.1", "13.5", "28.4", "58.2", "118", "237"] = None,
        variables: Dict[str, str] = None,
        canarySettings: DeploymentCanarySettingsTypeDef = None,
        tracingEnabled: bool = None,
    ) -> "DeploymentTypeDef":
        """
        [Client.create_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.create_deployment)
        """

    def create_documentation_part(
        self, restApiId: str, location: "DocumentationPartLocationTypeDef", properties: str
    ) -> "DocumentationPartTypeDef":
        """
        [Client.create_documentation_part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.create_documentation_part)
        """

    def create_documentation_version(
        self,
        restApiId: str,
        documentationVersion: str,
        stageName: str = None,
        description: str = None,
    ) -> "DocumentationVersionTypeDef":
        """
        [Client.create_documentation_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.create_documentation_version)
        """

    def create_domain_name(
        self,
        domainName: str,
        certificateName: str = None,
        certificateBody: str = None,
        certificatePrivateKey: str = None,
        certificateChain: str = None,
        certificateArn: str = None,
        regionalCertificateName: str = None,
        regionalCertificateArn: str = None,
        endpointConfiguration: "EndpointConfigurationTypeDef" = None,
        tags: Dict[str, str] = None,
        securityPolicy: Literal["TLS_1_0", "TLS_1_2"] = None,
    ) -> "DomainNameTypeDef":
        """
        [Client.create_domain_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.create_domain_name)
        """

    def create_model(
        self,
        restApiId: str,
        name: str,
        contentType: str,
        description: str = None,
        schema: str = None,
    ) -> "ModelTypeDef":
        """
        [Client.create_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.create_model)
        """

    def create_request_validator(
        self,
        restApiId: str,
        name: str = None,
        validateRequestBody: bool = None,
        validateRequestParameters: bool = None,
    ) -> "RequestValidatorTypeDef":
        """
        [Client.create_request_validator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.create_request_validator)
        """

    def create_resource(self, restApiId: str, parentId: str, pathPart: str) -> "ResourceTypeDef":
        """
        [Client.create_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.create_resource)
        """

    def create_rest_api(
        self,
        name: str,
        description: str = None,
        version: str = None,
        cloneFrom: str = None,
        binaryMediaTypes: List[str] = None,
        minimumCompressionSize: int = None,
        apiKeySource: Literal["HEADER", "AUTHORIZER"] = None,
        endpointConfiguration: "EndpointConfigurationTypeDef" = None,
        policy: str = None,
        tags: Dict[str, str] = None,
    ) -> "RestApiTypeDef":
        """
        [Client.create_rest_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.create_rest_api)
        """

    def create_stage(
        self,
        restApiId: str,
        stageName: str,
        deploymentId: str,
        description: str = None,
        cacheClusterEnabled: bool = None,
        cacheClusterSize: Literal["0.5", "1.6", "6.1", "13.5", "28.4", "58.2", "118", "237"] = None,
        variables: Dict[str, str] = None,
        documentationVersion: str = None,
        canarySettings: "CanarySettingsTypeDef" = None,
        tracingEnabled: bool = None,
        tags: Dict[str, str] = None,
    ) -> "StageTypeDef":
        """
        [Client.create_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.create_stage)
        """

    def create_usage_plan(
        self,
        name: str,
        description: str = None,
        apiStages: List["ApiStageTypeDef"] = None,
        throttle: "ThrottleSettingsTypeDef" = None,
        quota: "QuotaSettingsTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> "UsagePlanTypeDef":
        """
        [Client.create_usage_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.create_usage_plan)
        """

    def create_usage_plan_key(
        self, usagePlanId: str, keyId: str, keyType: str
    ) -> "UsagePlanKeyTypeDef":
        """
        [Client.create_usage_plan_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.create_usage_plan_key)
        """

    def create_vpc_link(
        self, name: str, targetArns: List[str], description: str = None, tags: Dict[str, str] = None
    ) -> "VpcLinkTypeDef":
        """
        [Client.create_vpc_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.create_vpc_link)
        """

    def delete_api_key(self, apiKey: str) -> None:
        """
        [Client.delete_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_api_key)
        """

    def delete_authorizer(self, restApiId: str, authorizerId: str) -> None:
        """
        [Client.delete_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_authorizer)
        """

    def delete_base_path_mapping(self, domainName: str, basePath: str) -> None:
        """
        [Client.delete_base_path_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_base_path_mapping)
        """

    def delete_client_certificate(self, clientCertificateId: str) -> None:
        """
        [Client.delete_client_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_client_certificate)
        """

    def delete_deployment(self, restApiId: str, deploymentId: str) -> None:
        """
        [Client.delete_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_deployment)
        """

    def delete_documentation_part(self, restApiId: str, documentationPartId: str) -> None:
        """
        [Client.delete_documentation_part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_documentation_part)
        """

    def delete_documentation_version(self, restApiId: str, documentationVersion: str) -> None:
        """
        [Client.delete_documentation_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_documentation_version)
        """

    def delete_domain_name(self, domainName: str) -> None:
        """
        [Client.delete_domain_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_domain_name)
        """

    def delete_gateway_response(
        self,
        restApiId: str,
        responseType: Literal[
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
    ) -> None:
        """
        [Client.delete_gateway_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_gateway_response)
        """

    def delete_integration(self, restApiId: str, resourceId: str, httpMethod: str) -> None:
        """
        [Client.delete_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_integration)
        """

    def delete_integration_response(
        self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str
    ) -> None:
        """
        [Client.delete_integration_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_integration_response)
        """

    def delete_method(self, restApiId: str, resourceId: str, httpMethod: str) -> None:
        """
        [Client.delete_method documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_method)
        """

    def delete_method_response(
        self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str
    ) -> None:
        """
        [Client.delete_method_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_method_response)
        """

    def delete_model(self, restApiId: str, modelName: str) -> None:
        """
        [Client.delete_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_model)
        """

    def delete_request_validator(self, restApiId: str, requestValidatorId: str) -> None:
        """
        [Client.delete_request_validator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_request_validator)
        """

    def delete_resource(self, restApiId: str, resourceId: str) -> None:
        """
        [Client.delete_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_resource)
        """

    def delete_rest_api(self, restApiId: str) -> None:
        """
        [Client.delete_rest_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_rest_api)
        """

    def delete_stage(self, restApiId: str, stageName: str) -> None:
        """
        [Client.delete_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_stage)
        """

    def delete_usage_plan(self, usagePlanId: str) -> None:
        """
        [Client.delete_usage_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_usage_plan)
        """

    def delete_usage_plan_key(self, usagePlanId: str, keyId: str) -> None:
        """
        [Client.delete_usage_plan_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_usage_plan_key)
        """

    def delete_vpc_link(self, vpcLinkId: str) -> None:
        """
        [Client.delete_vpc_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.delete_vpc_link)
        """

    def flush_stage_authorizers_cache(self, restApiId: str, stageName: str) -> None:
        """
        [Client.flush_stage_authorizers_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.flush_stage_authorizers_cache)
        """

    def flush_stage_cache(self, restApiId: str, stageName: str) -> None:
        """
        [Client.flush_stage_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.flush_stage_cache)
        """

    def generate_client_certificate(
        self, description: str = None, tags: Dict[str, str] = None
    ) -> "ClientCertificateTypeDef":
        """
        [Client.generate_client_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.generate_client_certificate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.generate_presigned_url)
        """

    def get_account(self) -> AccountTypeDef:
        """
        [Client.get_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_account)
        """

    def get_api_key(self, apiKey: str, includeValue: bool = None) -> "ApiKeyTypeDef":
        """
        [Client.get_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_api_key)
        """

    def get_api_keys(
        self,
        position: str = None,
        limit: int = None,
        nameQuery: str = None,
        customerId: str = None,
        includeValues: bool = None,
    ) -> ApiKeysTypeDef:
        """
        [Client.get_api_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_api_keys)
        """

    def get_authorizer(self, restApiId: str, authorizerId: str) -> "AuthorizerTypeDef":
        """
        [Client.get_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_authorizer)
        """

    def get_authorizers(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> AuthorizersTypeDef:
        """
        [Client.get_authorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_authorizers)
        """

    def get_base_path_mapping(self, domainName: str, basePath: str) -> "BasePathMappingTypeDef":
        """
        [Client.get_base_path_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_base_path_mapping)
        """

    def get_base_path_mappings(
        self, domainName: str, position: str = None, limit: int = None
    ) -> BasePathMappingsTypeDef:
        """
        [Client.get_base_path_mappings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_base_path_mappings)
        """

    def get_client_certificate(self, clientCertificateId: str) -> "ClientCertificateTypeDef":
        """
        [Client.get_client_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_client_certificate)
        """

    def get_client_certificates(
        self, position: str = None, limit: int = None
    ) -> ClientCertificatesTypeDef:
        """
        [Client.get_client_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_client_certificates)
        """

    def get_deployment(
        self, restApiId: str, deploymentId: str, embed: List[str] = None
    ) -> "DeploymentTypeDef":
        """
        [Client.get_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_deployment)
        """

    def get_deployments(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> DeploymentsTypeDef:
        """
        [Client.get_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_deployments)
        """

    def get_documentation_part(
        self, restApiId: str, documentationPartId: str
    ) -> "DocumentationPartTypeDef":
        """
        [Client.get_documentation_part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_documentation_part)
        """

    def get_documentation_parts(
        self,
        restApiId: str,
        type: Literal[
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
        ] = None,
        nameQuery: str = None,
        path: str = None,
        position: str = None,
        limit: int = None,
        locationStatus: Literal["DOCUMENTED", "UNDOCUMENTED"] = None,
    ) -> DocumentationPartsTypeDef:
        """
        [Client.get_documentation_parts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_documentation_parts)
        """

    def get_documentation_version(
        self, restApiId: str, documentationVersion: str
    ) -> "DocumentationVersionTypeDef":
        """
        [Client.get_documentation_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_documentation_version)
        """

    def get_documentation_versions(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> DocumentationVersionsTypeDef:
        """
        [Client.get_documentation_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_documentation_versions)
        """

    def get_domain_name(self, domainName: str) -> "DomainNameTypeDef":
        """
        [Client.get_domain_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_domain_name)
        """

    def get_domain_names(self, position: str = None, limit: int = None) -> DomainNamesTypeDef:
        """
        [Client.get_domain_names documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_domain_names)
        """

    def get_export(
        self,
        restApiId: str,
        stageName: str,
        exportType: str,
        parameters: Dict[str, str] = None,
        accepts: str = None,
    ) -> ExportResponseTypeDef:
        """
        [Client.get_export documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_export)
        """

    def get_gateway_response(
        self,
        restApiId: str,
        responseType: Literal[
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
    ) -> "GatewayResponseTypeDef":
        """
        [Client.get_gateway_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_gateway_response)
        """

    def get_gateway_responses(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> GatewayResponsesTypeDef:
        """
        [Client.get_gateway_responses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_gateway_responses)
        """

    def get_integration(
        self, restApiId: str, resourceId: str, httpMethod: str
    ) -> "IntegrationTypeDef":
        """
        [Client.get_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_integration)
        """

    def get_integration_response(
        self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str
    ) -> "IntegrationResponseTypeDef":
        """
        [Client.get_integration_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_integration_response)
        """

    def get_method(self, restApiId: str, resourceId: str, httpMethod: str) -> "MethodTypeDef":
        """
        [Client.get_method documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_method)
        """

    def get_method_response(
        self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str
    ) -> "MethodResponseTypeDef":
        """
        [Client.get_method_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_method_response)
        """

    def get_model(self, restApiId: str, modelName: str, flatten: bool = None) -> "ModelTypeDef":
        """
        [Client.get_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_model)
        """

    def get_model_template(self, restApiId: str, modelName: str) -> TemplateTypeDef:
        """
        [Client.get_model_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_model_template)
        """

    def get_models(self, restApiId: str, position: str = None, limit: int = None) -> ModelsTypeDef:
        """
        [Client.get_models documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_models)
        """

    def get_request_validator(
        self, restApiId: str, requestValidatorId: str
    ) -> "RequestValidatorTypeDef":
        """
        [Client.get_request_validator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_request_validator)
        """

    def get_request_validators(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> RequestValidatorsTypeDef:
        """
        [Client.get_request_validators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_request_validators)
        """

    def get_resource(
        self, restApiId: str, resourceId: str, embed: List[str] = None
    ) -> "ResourceTypeDef":
        """
        [Client.get_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_resource)
        """

    def get_resources(
        self, restApiId: str, position: str = None, limit: int = None, embed: List[str] = None
    ) -> ResourcesTypeDef:
        """
        [Client.get_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_resources)
        """

    def get_rest_api(self, restApiId: str) -> "RestApiTypeDef":
        """
        [Client.get_rest_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_rest_api)
        """

    def get_rest_apis(self, position: str = None, limit: int = None) -> RestApisTypeDef:
        """
        [Client.get_rest_apis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_rest_apis)
        """

    def get_sdk(
        self, restApiId: str, stageName: str, sdkType: str, parameters: Dict[str, str] = None
    ) -> SdkResponseTypeDef:
        """
        [Client.get_sdk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_sdk)
        """

    def get_sdk_type(self, id: str) -> "SdkTypeTypeDef":
        """
        [Client.get_sdk_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_sdk_type)
        """

    def get_sdk_types(self, position: str = None, limit: int = None) -> SdkTypesTypeDef:
        """
        [Client.get_sdk_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_sdk_types)
        """

    def get_stage(self, restApiId: str, stageName: str) -> "StageTypeDef":
        """
        [Client.get_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_stage)
        """

    def get_stages(self, restApiId: str, deploymentId: str = None) -> StagesTypeDef:
        """
        [Client.get_stages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_stages)
        """

    def get_tags(self, resourceArn: str, position: str = None, limit: int = None) -> TagsTypeDef:
        """
        [Client.get_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_tags)
        """

    def get_usage(
        self,
        usagePlanId: str,
        startDate: str,
        endDate: str,
        keyId: str = None,
        position: str = None,
        limit: int = None,
    ) -> UsageTypeDef:
        """
        [Client.get_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_usage)
        """

    def get_usage_plan(self, usagePlanId: str) -> "UsagePlanTypeDef":
        """
        [Client.get_usage_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_usage_plan)
        """

    def get_usage_plan_key(self, usagePlanId: str, keyId: str) -> "UsagePlanKeyTypeDef":
        """
        [Client.get_usage_plan_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_usage_plan_key)
        """

    def get_usage_plan_keys(
        self, usagePlanId: str, position: str = None, limit: int = None, nameQuery: str = None
    ) -> UsagePlanKeysTypeDef:
        """
        [Client.get_usage_plan_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_usage_plan_keys)
        """

    def get_usage_plans(
        self, position: str = None, keyId: str = None, limit: int = None
    ) -> UsagePlansTypeDef:
        """
        [Client.get_usage_plans documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_usage_plans)
        """

    def get_vpc_link(self, vpcLinkId: str) -> "VpcLinkTypeDef":
        """
        [Client.get_vpc_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_vpc_link)
        """

    def get_vpc_links(self, position: str = None, limit: int = None) -> VpcLinksTypeDef:
        """
        [Client.get_vpc_links documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.get_vpc_links)
        """

    def import_api_keys(
        self, body: Union[bytes, IO[bytes]], format: Literal["csv"], failOnWarnings: bool = None
    ) -> ApiKeyIdsTypeDef:
        """
        [Client.import_api_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.import_api_keys)
        """

    def import_documentation_parts(
        self,
        restApiId: str,
        body: Union[bytes, IO[bytes]],
        mode: Literal["merge", "overwrite"] = None,
        failOnWarnings: bool = None,
    ) -> DocumentationPartIdsTypeDef:
        """
        [Client.import_documentation_parts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.import_documentation_parts)
        """

    def import_rest_api(
        self,
        body: Union[bytes, IO[bytes]],
        failOnWarnings: bool = None,
        parameters: Dict[str, str] = None,
    ) -> "RestApiTypeDef":
        """
        [Client.import_rest_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.import_rest_api)
        """

    def put_gateway_response(
        self,
        restApiId: str,
        responseType: Literal[
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
        statusCode: str = None,
        responseParameters: Dict[str, str] = None,
        responseTemplates: Dict[str, str] = None,
    ) -> "GatewayResponseTypeDef":
        """
        [Client.put_gateway_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.put_gateway_response)
        """

    def put_integration(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        type: Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        integrationHttpMethod: str = None,
        uri: str = None,
        connectionType: Literal["INTERNET", "VPC_LINK"] = None,
        connectionId: str = None,
        credentials: str = None,
        requestParameters: Dict[str, str] = None,
        requestTemplates: Dict[str, str] = None,
        passthroughBehavior: str = None,
        cacheNamespace: str = None,
        cacheKeyParameters: List[str] = None,
        contentHandling: Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"] = None,
        timeoutInMillis: int = None,
        tlsConfig: "TlsConfigTypeDef" = None,
    ) -> "IntegrationTypeDef":
        """
        [Client.put_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.put_integration)
        """

    def put_integration_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        selectionPattern: str = None,
        responseParameters: Dict[str, str] = None,
        responseTemplates: Dict[str, str] = None,
        contentHandling: Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"] = None,
    ) -> "IntegrationResponseTypeDef":
        """
        [Client.put_integration_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.put_integration_response)
        """

    def put_method(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        authorizationType: str,
        authorizerId: str = None,
        apiKeyRequired: bool = None,
        operationName: str = None,
        requestParameters: Dict[str, bool] = None,
        requestModels: Dict[str, str] = None,
        requestValidatorId: str = None,
        authorizationScopes: List[str] = None,
    ) -> "MethodTypeDef":
        """
        [Client.put_method documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.put_method)
        """

    def put_method_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        responseParameters: Dict[str, bool] = None,
        responseModels: Dict[str, str] = None,
    ) -> "MethodResponseTypeDef":
        """
        [Client.put_method_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.put_method_response)
        """

    def put_rest_api(
        self,
        restApiId: str,
        body: Union[bytes, IO[bytes]],
        mode: Literal["merge", "overwrite"] = None,
        failOnWarnings: bool = None,
        parameters: Dict[str, str] = None,
    ) -> "RestApiTypeDef":
        """
        [Client.put_rest_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.put_rest_api)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.tag_resource)
        """

    def test_invoke_authorizer(
        self,
        restApiId: str,
        authorizerId: str,
        headers: Dict[str, str] = None,
        multiValueHeaders: Dict[str, List[str]] = None,
        pathWithQueryString: str = None,
        body: str = None,
        stageVariables: Dict[str, str] = None,
        additionalContext: Dict[str, str] = None,
    ) -> TestInvokeAuthorizerResponseTypeDef:
        """
        [Client.test_invoke_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.test_invoke_authorizer)
        """

    def test_invoke_method(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        pathWithQueryString: str = None,
        body: str = None,
        headers: Dict[str, str] = None,
        multiValueHeaders: Dict[str, List[str]] = None,
        clientCertificateId: str = None,
        stageVariables: Dict[str, str] = None,
    ) -> TestInvokeMethodResponseTypeDef:
        """
        [Client.test_invoke_method documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.test_invoke_method)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.untag_resource)
        """

    def update_account(self, patchOperations: List[PatchOperationTypeDef] = None) -> AccountTypeDef:
        """
        [Client.update_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_account)
        """

    def update_api_key(
        self, apiKey: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "ApiKeyTypeDef":
        """
        [Client.update_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_api_key)
        """

    def update_authorizer(
        self, restApiId: str, authorizerId: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "AuthorizerTypeDef":
        """
        [Client.update_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_authorizer)
        """

    def update_base_path_mapping(
        self, domainName: str, basePath: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "BasePathMappingTypeDef":
        """
        [Client.update_base_path_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_base_path_mapping)
        """

    def update_client_certificate(
        self, clientCertificateId: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "ClientCertificateTypeDef":
        """
        [Client.update_client_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_client_certificate)
        """

    def update_deployment(
        self, restApiId: str, deploymentId: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "DeploymentTypeDef":
        """
        [Client.update_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_deployment)
        """

    def update_documentation_part(
        self,
        restApiId: str,
        documentationPartId: str,
        patchOperations: List[PatchOperationTypeDef] = None,
    ) -> "DocumentationPartTypeDef":
        """
        [Client.update_documentation_part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_documentation_part)
        """

    def update_documentation_version(
        self,
        restApiId: str,
        documentationVersion: str,
        patchOperations: List[PatchOperationTypeDef] = None,
    ) -> "DocumentationVersionTypeDef":
        """
        [Client.update_documentation_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_documentation_version)
        """

    def update_domain_name(
        self, domainName: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "DomainNameTypeDef":
        """
        [Client.update_domain_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_domain_name)
        """

    def update_gateway_response(
        self,
        restApiId: str,
        responseType: Literal[
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
        patchOperations: List[PatchOperationTypeDef] = None,
    ) -> "GatewayResponseTypeDef":
        """
        [Client.update_gateway_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_gateway_response)
        """

    def update_integration(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        patchOperations: List[PatchOperationTypeDef] = None,
    ) -> "IntegrationTypeDef":
        """
        [Client.update_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_integration)
        """

    def update_integration_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        patchOperations: List[PatchOperationTypeDef] = None,
    ) -> "IntegrationResponseTypeDef":
        """
        [Client.update_integration_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_integration_response)
        """

    def update_method(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        patchOperations: List[PatchOperationTypeDef] = None,
    ) -> "MethodTypeDef":
        """
        [Client.update_method documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_method)
        """

    def update_method_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        patchOperations: List[PatchOperationTypeDef] = None,
    ) -> "MethodResponseTypeDef":
        """
        [Client.update_method_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_method_response)
        """

    def update_model(
        self, restApiId: str, modelName: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "ModelTypeDef":
        """
        [Client.update_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_model)
        """

    def update_request_validator(
        self,
        restApiId: str,
        requestValidatorId: str,
        patchOperations: List[PatchOperationTypeDef] = None,
    ) -> "RequestValidatorTypeDef":
        """
        [Client.update_request_validator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_request_validator)
        """

    def update_resource(
        self, restApiId: str, resourceId: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "ResourceTypeDef":
        """
        [Client.update_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_resource)
        """

    def update_rest_api(
        self, restApiId: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "RestApiTypeDef":
        """
        [Client.update_rest_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_rest_api)
        """

    def update_stage(
        self, restApiId: str, stageName: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "StageTypeDef":
        """
        [Client.update_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_stage)
        """

    def update_usage(
        self, usagePlanId: str, keyId: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> UsageTypeDef:
        """
        [Client.update_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_usage)
        """

    def update_usage_plan(
        self, usagePlanId: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "UsagePlanTypeDef":
        """
        [Client.update_usage_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_usage_plan)
        """

    def update_vpc_link(
        self, vpcLinkId: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "VpcLinkTypeDef":
        """
        [Client.update_vpc_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Client.update_vpc_link)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_api_keys"]) -> GetApiKeysPaginator:
        """
        [Paginator.GetApiKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Paginator.GetApiKeys)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_authorizers"]) -> GetAuthorizersPaginator:
        """
        [Paginator.GetAuthorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Paginator.GetAuthorizers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_base_path_mappings"]
    ) -> GetBasePathMappingsPaginator:
        """
        [Paginator.GetBasePathMappings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Paginator.GetBasePathMappings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_client_certificates"]
    ) -> GetClientCertificatesPaginator:
        """
        [Paginator.GetClientCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Paginator.GetClientCertificates)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_deployments"]) -> GetDeploymentsPaginator:
        """
        [Paginator.GetDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Paginator.GetDeployments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_documentation_parts"]
    ) -> GetDocumentationPartsPaginator:
        """
        [Paginator.GetDocumentationParts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationParts)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_documentation_versions"]
    ) -> GetDocumentationVersionsPaginator:
        """
        [Paginator.GetDocumentationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationVersions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_domain_names"]) -> GetDomainNamesPaginator:
        """
        [Paginator.GetDomainNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Paginator.GetDomainNames)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_gateway_responses"]
    ) -> GetGatewayResponsesPaginator:
        """
        [Paginator.GetGatewayResponses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Paginator.GetGatewayResponses)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_models"]) -> GetModelsPaginator:
        """
        [Paginator.GetModels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Paginator.GetModels)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_request_validators"]
    ) -> GetRequestValidatorsPaginator:
        """
        [Paginator.GetRequestValidators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Paginator.GetRequestValidators)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_resources"]) -> GetResourcesPaginator:
        """
        [Paginator.GetResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Paginator.GetResources)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_rest_apis"]) -> GetRestApisPaginator:
        """
        [Paginator.GetRestApis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Paginator.GetRestApis)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_sdk_types"]) -> GetSdkTypesPaginator:
        """
        [Paginator.GetSdkTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Paginator.GetSdkTypes)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_usage"]) -> GetUsagePaginator:
        """
        [Paginator.GetUsage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Paginator.GetUsage)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_usage_plan_keys"]
    ) -> GetUsagePlanKeysPaginator:
        """
        [Paginator.GetUsagePlanKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlanKeys)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_usage_plans"]) -> GetUsagePlansPaginator:
        """
        [Paginator.GetUsagePlans documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlans)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_vpc_links"]) -> GetVpcLinksPaginator:
        """
        [Paginator.GetVpcLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/apigateway.html#APIGateway.Paginator.GetVpcLinks)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
