"""
Type annotations for apigateway service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_apigateway import APIGatewayClient

    client: APIGatewayClient = boto3.client("apigateway")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import (
    ApiKeySourceTypeType,
    AuthorizerTypeType,
    CacheClusterSizeType,
    ConnectionTypeType,
    ContentHandlingStrategyType,
    DocumentationPartTypeType,
    GatewayResponseTypeType,
    IntegrationTypeType,
    LocationStatusTypeType,
    PutModeType,
    SecurityPolicyType,
)
from .paginator import (
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
from .type_defs import (
    AccountTypeDef,
    ApiKeyIdsTypeDef,
    ApiKeyResponseMetadataTypeDef,
    ApiKeysTypeDef,
    ApiStageTypeDef,
    AuthorizerResponseMetadataTypeDef,
    AuthorizersTypeDef,
    BasePathMappingResponseMetadataTypeDef,
    BasePathMappingsTypeDef,
    CanarySettingsTypeDef,
    ClientCertificateResponseMetadataTypeDef,
    ClientCertificatesTypeDef,
    DeploymentCanarySettingsTypeDef,
    DeploymentResponseMetadataTypeDef,
    DeploymentsTypeDef,
    DocumentationPartIdsTypeDef,
    DocumentationPartLocationTypeDef,
    DocumentationPartResponseMetadataTypeDef,
    DocumentationPartsTypeDef,
    DocumentationVersionResponseMetadataTypeDef,
    DocumentationVersionsTypeDef,
    DomainNameResponseMetadataTypeDef,
    DomainNamesTypeDef,
    EndpointConfigurationTypeDef,
    ExportResponseTypeDef,
    GatewayResponseResponseMetadataTypeDef,
    GatewayResponsesTypeDef,
    IntegrationResponseMetadataTypeDef,
    IntegrationResponseResponseMetadataTypeDef,
    MethodResponseMetadataTypeDef,
    MethodResponseResponseMetadataTypeDef,
    ModelResponseMetadataTypeDef,
    ModelsTypeDef,
    MutualTlsAuthenticationInputTypeDef,
    PatchOperationTypeDef,
    QuotaSettingsTypeDef,
    RequestValidatorResponseMetadataTypeDef,
    RequestValidatorsTypeDef,
    ResourceResponseMetadataTypeDef,
    ResourcesTypeDef,
    RestApiResponseMetadataTypeDef,
    RestApisTypeDef,
    SdkResponseTypeDef,
    SdkTypeResponseMetadataTypeDef,
    SdkTypesTypeDef,
    StageKeyTypeDef,
    StageResponseMetadataTypeDef,
    StagesTypeDef,
    TagsTypeDef,
    TemplateTypeDef,
    TestInvokeAuthorizerResponseTypeDef,
    TestInvokeMethodResponseTypeDef,
    ThrottleSettingsTypeDef,
    TlsConfigTypeDef,
    UsagePlanKeyResponseMetadataTypeDef,
    UsagePlanKeysTypeDef,
    UsagePlanResponseMetadataTypeDef,
    UsagePlansTypeDef,
    UsageTypeDef,
    VpcLinkResponseMetadataTypeDef,
    VpcLinksTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("APIGatewayClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]

class APIGatewayClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        APIGatewayClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#can_paginate)
        """
    def create_api_key(
        self,
        *,
        name: str = None,
        description: str = None,
        enabled: bool = None,
        generateDistinctId: bool = None,
        value: str = None,
        stageKeys: List["StageKeyTypeDef"] = None,
        customerId: str = None,
        tags: Dict[str, str] = None
    ) -> ApiKeyResponseMetadataTypeDef:
        """
        Create an ApiKey resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.create_api_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create_api_key)
        """
    def create_authorizer(
        self,
        *,
        restApiId: str,
        name: str,
        type: AuthorizerTypeType,
        providerARNs: List[str] = None,
        authType: str = None,
        authorizerUri: str = None,
        authorizerCredentials: str = None,
        identitySource: str = None,
        identityValidationExpression: str = None,
        authorizerResultTtlInSeconds: int = None
    ) -> AuthorizerResponseMetadataTypeDef:
        """
        Adds a new Authorizer resource to an existing RestApi resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.create_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create_authorizer)
        """
    def create_base_path_mapping(
        self, *, domainName: str, restApiId: str, basePath: str = None, stage: str = None
    ) -> BasePathMappingResponseMetadataTypeDef:
        """
        Creates a new BasePathMapping resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.create_base_path_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create_base_path_mapping)
        """
    def create_deployment(
        self,
        *,
        restApiId: str,
        stageName: str = None,
        stageDescription: str = None,
        description: str = None,
        cacheClusterEnabled: bool = None,
        cacheClusterSize: CacheClusterSizeType = None,
        variables: Dict[str, str] = None,
        canarySettings: "DeploymentCanarySettingsTypeDef" = None,
        tracingEnabled: bool = None
    ) -> DeploymentResponseMetadataTypeDef:
        """
        Creates a Deployment resource, which makes a specified RestApi callable over the
        internet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.create_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create_deployment)
        """
    def create_documentation_part(
        self, *, restApiId: str, location: "DocumentationPartLocationTypeDef", properties: str
    ) -> DocumentationPartResponseMetadataTypeDef:
        """
        Creates a documentation part.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.create_documentation_part)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create_documentation_part)
        """
    def create_documentation_version(
        self,
        *,
        restApiId: str,
        documentationVersion: str,
        stageName: str = None,
        description: str = None
    ) -> DocumentationVersionResponseMetadataTypeDef:
        """
        Creates a documentation version See also: `AWS API Documentation <https://docs.a
        ws.amazon.com/goto/WebAPI/apigateway-2015-07-09/CreateDocumentationVersion>`_
        **Request Syntax** response = client.create_documentation_version(
        restApiId='string', documentationVersion='string...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.create_documentation_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create_documentation_version)
        """
    def create_domain_name(
        self,
        *,
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
        securityPolicy: SecurityPolicyType = None,
        mutualTlsAuthentication: "MutualTlsAuthenticationInputTypeDef" = None,
        ownershipVerificationCertificateArn: str = None
    ) -> DomainNameResponseMetadataTypeDef:
        """
        Creates a new domain name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.create_domain_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create_domain_name)
        """
    def create_model(
        self,
        *,
        restApiId: str,
        name: str,
        contentType: str,
        description: str = None,
        schema: str = None
    ) -> ModelResponseMetadataTypeDef:
        """
        Adds a new Model resource to an existing RestApi resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.create_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create_model)
        """
    def create_request_validator(
        self,
        *,
        restApiId: str,
        name: str = None,
        validateRequestBody: bool = None,
        validateRequestParameters: bool = None
    ) -> RequestValidatorResponseMetadataTypeDef:
        """
        Creates a RequestValidator of a given RestApi.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.create_request_validator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create_request_validator)
        """
    def create_resource(
        self, *, restApiId: str, parentId: str, pathPart: str
    ) -> ResourceResponseMetadataTypeDef:
        """
        Creates a Resource resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.create_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create_resource)
        """
    def create_rest_api(
        self,
        *,
        name: str,
        description: str = None,
        version: str = None,
        cloneFrom: str = None,
        binaryMediaTypes: List[str] = None,
        minimumCompressionSize: int = None,
        apiKeySource: ApiKeySourceTypeType = None,
        endpointConfiguration: "EndpointConfigurationTypeDef" = None,
        policy: str = None,
        tags: Dict[str, str] = None,
        disableExecuteApiEndpoint: bool = None
    ) -> RestApiResponseMetadataTypeDef:
        """
        Creates a new RestApi resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.create_rest_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create_rest_api)
        """
    def create_stage(
        self,
        *,
        restApiId: str,
        stageName: str,
        deploymentId: str,
        description: str = None,
        cacheClusterEnabled: bool = None,
        cacheClusterSize: CacheClusterSizeType = None,
        variables: Dict[str, str] = None,
        documentationVersion: str = None,
        canarySettings: "CanarySettingsTypeDef" = None,
        tracingEnabled: bool = None,
        tags: Dict[str, str] = None
    ) -> StageResponseMetadataTypeDef:
        """
        Creates a new Stage resource that references a pre-existing Deployment for the
        API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.create_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create_stage)
        """
    def create_usage_plan(
        self,
        *,
        name: str,
        description: str = None,
        apiStages: List["ApiStageTypeDef"] = None,
        throttle: "ThrottleSettingsTypeDef" = None,
        quota: "QuotaSettingsTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> UsagePlanResponseMetadataTypeDef:
        """
        Creates a usage plan with the throttle and quota limits, as well as the
        associated API stages, specified in the payload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.create_usage_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create_usage_plan)
        """
    def create_usage_plan_key(
        self, *, usagePlanId: str, keyId: str, keyType: str
    ) -> UsagePlanKeyResponseMetadataTypeDef:
        """
        Creates a usage plan key for adding an existing API key to a usage plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.create_usage_plan_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create_usage_plan_key)
        """
    def create_vpc_link(
        self,
        *,
        name: str,
        targetArns: List[str],
        description: str = None,
        tags: Dict[str, str] = None
    ) -> VpcLinkResponseMetadataTypeDef:
        """
        Creates a VPC link, under the caller's account in a selected region, in an
        asynchronous operation that typically takes 2-4 minutes to complete and become
        operational.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.create_vpc_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create_vpc_link)
        """
    def delete_api_key(self, *, apiKey: str) -> None:
        """
        Deletes the ApiKey resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_api_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_api_key)
        """
    def delete_authorizer(self, *, restApiId: str, authorizerId: str) -> None:
        """
        Deletes an existing Authorizer resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_authorizer)
        """
    def delete_base_path_mapping(self, *, domainName: str, basePath: str) -> None:
        """
        Deletes the BasePathMapping resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_base_path_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_base_path_mapping)
        """
    def delete_client_certificate(self, *, clientCertificateId: str) -> None:
        """
        Deletes the ClientCertificate resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_client_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_client_certificate)
        """
    def delete_deployment(self, *, restApiId: str, deploymentId: str) -> None:
        """
        Deletes a Deployment resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_deployment)
        """
    def delete_documentation_part(self, *, restApiId: str, documentationPartId: str) -> None:
        """
        Deletes a documentation part See also: `AWS API Documentation <https://docs.aws.
        amazon.com/goto/WebAPI/apigateway-2015-07-09/DeleteDocumentationPart>`_
        **Request Syntax** response = client.delete_documentation_part(
        restApiId='string', documentationPartId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_documentation_part)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_documentation_part)
        """
    def delete_documentation_version(self, *, restApiId: str, documentationVersion: str) -> None:
        """
        Deletes a documentation version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_documentation_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_documentation_version)
        """
    def delete_domain_name(self, *, domainName: str) -> None:
        """
        Deletes the DomainName resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_domain_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_domain_name)
        """
    def delete_gateway_response(
        self, *, restApiId: str, responseType: GatewayResponseTypeType
    ) -> None:
        """
        Clears any customization of a GatewayResponse of a specified response type on
        the given RestApi and resets it with the default settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_gateway_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_gateway_response)
        """
    def delete_integration(self, *, restApiId: str, resourceId: str, httpMethod: str) -> None:
        """
        Represents a delete integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_integration)
        """
    def delete_integration_response(
        self, *, restApiId: str, resourceId: str, httpMethod: str, statusCode: str
    ) -> None:
        """
        Represents a delete integration response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_integration_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_integration_response)
        """
    def delete_method(self, *, restApiId: str, resourceId: str, httpMethod: str) -> None:
        """
        Deletes an existing Method resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_method)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_method)
        """
    def delete_method_response(
        self, *, restApiId: str, resourceId: str, httpMethod: str, statusCode: str
    ) -> None:
        """
        Deletes an existing MethodResponse resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_method_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_method_response)
        """
    def delete_model(self, *, restApiId: str, modelName: str) -> None:
        """
        Deletes a model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_model)
        """
    def delete_request_validator(self, *, restApiId: str, requestValidatorId: str) -> None:
        """
        Deletes a RequestValidator of a given RestApi.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_request_validator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_request_validator)
        """
    def delete_resource(self, *, restApiId: str, resourceId: str) -> None:
        """
        Deletes a Resource resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_resource)
        """
    def delete_rest_api(self, *, restApiId: str) -> None:
        """
        Deletes the specified API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_rest_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_rest_api)
        """
    def delete_stage(self, *, restApiId: str, stageName: str) -> None:
        """
        Deletes a Stage resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_stage)
        """
    def delete_usage_plan(self, *, usagePlanId: str) -> None:
        """
        Deletes a usage plan of a given plan Id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_usage_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_usage_plan)
        """
    def delete_usage_plan_key(self, *, usagePlanId: str, keyId: str) -> None:
        """
        Deletes a usage plan key and remove the underlying API key from the associated
        usage plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_usage_plan_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_usage_plan_key)
        """
    def delete_vpc_link(self, *, vpcLinkId: str) -> None:
        """
        Deletes an existing VpcLink of a specified identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.delete_vpc_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete_vpc_link)
        """
    def flush_stage_authorizers_cache(self, *, restApiId: str, stageName: str) -> None:
        """
        Flushes all authorizer cache entries on a stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.flush_stage_authorizers_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#flush_stage_authorizers_cache)
        """
    def flush_stage_cache(self, *, restApiId: str, stageName: str) -> None:
        """
        Flushes a stage's cache.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.flush_stage_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#flush_stage_cache)
        """
    def generate_client_certificate(
        self, *, description: str = None, tags: Dict[str, str] = None
    ) -> ClientCertificateResponseMetadataTypeDef:
        """
        Generates a ClientCertificate resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.generate_client_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#generate_client_certificate)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#generate_presigned_url)
        """
    def get_account(self) -> AccountTypeDef:
        """
        Gets information about the current Account resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_account)
        """
    def get_api_key(
        self, *, apiKey: str, includeValue: bool = None
    ) -> ApiKeyResponseMetadataTypeDef:
        """
        Gets information about the current ApiKey resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_api_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_api_key)
        """
    def get_api_keys(
        self,
        *,
        position: str = None,
        limit: int = None,
        nameQuery: str = None,
        customerId: str = None,
        includeValues: bool = None
    ) -> ApiKeysTypeDef:
        """
        Gets information about the current ApiKeys resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_api_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_api_keys)
        """
    def get_authorizer(
        self, *, restApiId: str, authorizerId: str
    ) -> AuthorizerResponseMetadataTypeDef:
        """
        Describe an existing Authorizer resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_authorizer)
        """
    def get_authorizers(
        self, *, restApiId: str, position: str = None, limit: int = None
    ) -> AuthorizersTypeDef:
        """
        Describe an existing Authorizers resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_authorizers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_authorizers)
        """
    def get_base_path_mapping(
        self, *, domainName: str, basePath: str
    ) -> BasePathMappingResponseMetadataTypeDef:
        """
        Describe a BasePathMapping resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_base_path_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_base_path_mapping)
        """
    def get_base_path_mappings(
        self, *, domainName: str, position: str = None, limit: int = None
    ) -> BasePathMappingsTypeDef:
        """
        Represents a collection of BasePathMapping resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_base_path_mappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_base_path_mappings)
        """
    def get_client_certificate(
        self, *, clientCertificateId: str
    ) -> ClientCertificateResponseMetadataTypeDef:
        """
        Gets information about the current ClientCertificate resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_client_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_client_certificate)
        """
    def get_client_certificates(
        self, *, position: str = None, limit: int = None
    ) -> ClientCertificatesTypeDef:
        """
        Gets a collection of ClientCertificate resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_client_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_client_certificates)
        """
    def get_deployment(
        self, *, restApiId: str, deploymentId: str, embed: List[str] = None
    ) -> DeploymentResponseMetadataTypeDef:
        """
        Gets information about a Deployment resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_deployment)
        """
    def get_deployments(
        self, *, restApiId: str, position: str = None, limit: int = None
    ) -> DeploymentsTypeDef:
        """
        Gets information about a Deployments collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_deployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_deployments)
        """
    def get_documentation_part(
        self, *, restApiId: str, documentationPartId: str
    ) -> DocumentationPartResponseMetadataTypeDef:
        """
        Gets a documentation part.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_documentation_part)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_documentation_part)
        """
    def get_documentation_parts(
        self,
        *,
        restApiId: str,
        type: DocumentationPartTypeType = None,
        nameQuery: str = None,
        path: str = None,
        position: str = None,
        limit: int = None,
        locationStatus: LocationStatusTypeType = None
    ) -> DocumentationPartsTypeDef:
        """
        Gets documentation parts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_documentation_parts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_documentation_parts)
        """
    def get_documentation_version(
        self, *, restApiId: str, documentationVersion: str
    ) -> DocumentationVersionResponseMetadataTypeDef:
        """
        Gets a documentation version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_documentation_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_documentation_version)
        """
    def get_documentation_versions(
        self, *, restApiId: str, position: str = None, limit: int = None
    ) -> DocumentationVersionsTypeDef:
        """
        Gets documentation versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_documentation_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_documentation_versions)
        """
    def get_domain_name(self, *, domainName: str) -> DomainNameResponseMetadataTypeDef:
        """
        Represents a domain name that is contained in a simpler, more intuitive URL that
        can be called.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_domain_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_domain_name)
        """
    def get_domain_names(self, *, position: str = None, limit: int = None) -> DomainNamesTypeDef:
        """
        Represents a collection of DomainName resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_domain_names)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_domain_names)
        """
    def get_export(
        self,
        *,
        restApiId: str,
        stageName: str,
        exportType: str,
        parameters: Dict[str, str] = None,
        accepts: str = None
    ) -> ExportResponseTypeDef:
        """
        Exports a deployed version of a RestApi in a specified format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_export)
        """
    def get_gateway_response(
        self, *, restApiId: str, responseType: GatewayResponseTypeType
    ) -> GatewayResponseResponseMetadataTypeDef:
        """
        Gets a GatewayResponse of a specified response type on the given RestApi.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_gateway_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_gateway_response)
        """
    def get_gateway_responses(
        self, *, restApiId: str, position: str = None, limit: int = None
    ) -> GatewayResponsesTypeDef:
        """
        Gets the GatewayResponses collection on the given RestApi.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_gateway_responses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_gateway_responses)
        """
    def get_integration(
        self, *, restApiId: str, resourceId: str, httpMethod: str
    ) -> IntegrationResponseMetadataTypeDef:
        """
        Get the integration settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_integration)
        """
    def get_integration_response(
        self, *, restApiId: str, resourceId: str, httpMethod: str, statusCode: str
    ) -> IntegrationResponseResponseMetadataTypeDef:
        """
        Represents a get integration response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_integration_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_integration_response)
        """
    def get_method(
        self, *, restApiId: str, resourceId: str, httpMethod: str
    ) -> MethodResponseMetadataTypeDef:
        """
        Describe an existing Method resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_method)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_method)
        """
    def get_method_response(
        self, *, restApiId: str, resourceId: str, httpMethod: str, statusCode: str
    ) -> MethodResponseResponseMetadataTypeDef:
        """
        Describes a MethodResponse resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_method_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_method_response)
        """
    def get_model(
        self, *, restApiId: str, modelName: str, flatten: bool = None
    ) -> ModelResponseMetadataTypeDef:
        """
        Describes an existing model defined for a RestApi resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_model)
        """
    def get_model_template(self, *, restApiId: str, modelName: str) -> TemplateTypeDef:
        """
        Generates a sample mapping template that can be used to transform a payload into
        the structure of a model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_model_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_model_template)
        """
    def get_models(
        self, *, restApiId: str, position: str = None, limit: int = None
    ) -> ModelsTypeDef:
        """
        Describes existing Models defined for a RestApi resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_models)
        """
    def get_request_validator(
        self, *, restApiId: str, requestValidatorId: str
    ) -> RequestValidatorResponseMetadataTypeDef:
        """
        Gets a RequestValidator of a given RestApi.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_request_validator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_request_validator)
        """
    def get_request_validators(
        self, *, restApiId: str, position: str = None, limit: int = None
    ) -> RequestValidatorsTypeDef:
        """
        Gets the RequestValidators collection of a given RestApi.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_request_validators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_request_validators)
        """
    def get_resource(
        self, *, restApiId: str, resourceId: str, embed: List[str] = None
    ) -> ResourceResponseMetadataTypeDef:
        """
        Lists information about a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_resource)
        """
    def get_resources(
        self, *, restApiId: str, position: str = None, limit: int = None, embed: List[str] = None
    ) -> ResourcesTypeDef:
        """
        Lists information about a collection of Resource resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_resources)
        """
    def get_rest_api(self, *, restApiId: str) -> RestApiResponseMetadataTypeDef:
        """
        Lists the RestApi resource in the collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_rest_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_rest_api)
        """
    def get_rest_apis(self, *, position: str = None, limit: int = None) -> RestApisTypeDef:
        """
        Lists the RestApis resources for your collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_rest_apis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_rest_apis)
        """
    def get_sdk(
        self, *, restApiId: str, stageName: str, sdkType: str, parameters: Dict[str, str] = None
    ) -> SdkResponseTypeDef:
        """
        Generates a client SDK for a RestApi and Stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_sdk)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_sdk)
        """
    def get_sdk_type(self, *, id: str) -> SdkTypeResponseMetadataTypeDef:
        """
        Gets an SDK type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_sdk_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_sdk_type)
        """
    def get_sdk_types(self, *, position: str = None, limit: int = None) -> SdkTypesTypeDef:
        """
        Gets SDK types See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetSdkTypes>`_
        **Request Syntax** response = client.get_sdk_types( position='string', limit=123
        ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_sdk_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_sdk_types)
        """
    def get_stage(self, *, restApiId: str, stageName: str) -> StageResponseMetadataTypeDef:
        """
        Gets information about a Stage resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_stage)
        """
    def get_stages(self, *, restApiId: str, deploymentId: str = None) -> StagesTypeDef:
        """
        Gets information about one or more Stage resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_stages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_stages)
        """
    def get_tags(self, *, resourceArn: str, position: str = None, limit: int = None) -> TagsTypeDef:
        """
        Gets the Tags collection for a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_tags)
        """
    def get_usage(
        self,
        *,
        usagePlanId: str,
        startDate: str,
        endDate: str,
        keyId: str = None,
        position: str = None,
        limit: int = None
    ) -> UsageTypeDef:
        """
        Gets the usage data of a usage plan in a specified time interval.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_usage)
        """
    def get_usage_plan(self, *, usagePlanId: str) -> UsagePlanResponseMetadataTypeDef:
        """
        Gets a usage plan of a given plan identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_usage_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_usage_plan)
        """
    def get_usage_plan_key(
        self, *, usagePlanId: str, keyId: str
    ) -> UsagePlanKeyResponseMetadataTypeDef:
        """
        Gets a usage plan key of a given key identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_usage_plan_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_usage_plan_key)
        """
    def get_usage_plan_keys(
        self, *, usagePlanId: str, position: str = None, limit: int = None, nameQuery: str = None
    ) -> UsagePlanKeysTypeDef:
        """
        Gets all the usage plan keys representing the API keys added to a specified
        usage plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_usage_plan_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_usage_plan_keys)
        """
    def get_usage_plans(
        self, *, position: str = None, keyId: str = None, limit: int = None
    ) -> UsagePlansTypeDef:
        """
        Gets all the usage plans of the caller's account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_usage_plans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_usage_plans)
        """
    def get_vpc_link(self, *, vpcLinkId: str) -> VpcLinkResponseMetadataTypeDef:
        """
        Gets a specified VPC link under the caller's account in a region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_vpc_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_vpc_link)
        """
    def get_vpc_links(self, *, position: str = None, limit: int = None) -> VpcLinksTypeDef:
        """
        Gets the VpcLinks collection under the caller's account in a selected region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.get_vpc_links)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get_vpc_links)
        """
    def import_api_keys(
        self,
        *,
        body: Union[bytes, IO[bytes], StreamingBody],
        format: Literal["csv"],
        failOnWarnings: bool = None
    ) -> ApiKeyIdsTypeDef:
        """
        Import API keys from an external source, such as a CSV-formatted file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.import_api_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#import_api_keys)
        """
    def import_documentation_parts(
        self,
        *,
        restApiId: str,
        body: Union[bytes, IO[bytes], StreamingBody],
        mode: PutModeType = None,
        failOnWarnings: bool = None
    ) -> DocumentationPartIdsTypeDef:
        """
        Imports documentation parts See also: `AWS API Documentation <https://docs.aws.a
        mazon.com/goto/WebAPI/apigateway-2015-07-09/ImportDocumentationParts>`_
        **Request Syntax** response = client.import_documentation_parts(
        restApiId='string', mode='merge'|'overwrite', fail...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.import_documentation_parts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#import_documentation_parts)
        """
    def import_rest_api(
        self,
        *,
        body: Union[bytes, IO[bytes], StreamingBody],
        failOnWarnings: bool = None,
        parameters: Dict[str, str] = None
    ) -> RestApiResponseMetadataTypeDef:
        """
        A feature of the API Gateway control service for creating a new API from an
        external API definition file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.import_rest_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#import_rest_api)
        """
    def put_gateway_response(
        self,
        *,
        restApiId: str,
        responseType: GatewayResponseTypeType,
        statusCode: str = None,
        responseParameters: Dict[str, str] = None,
        responseTemplates: Dict[str, str] = None
    ) -> GatewayResponseResponseMetadataTypeDef:
        """
        Creates a customization of a GatewayResponse of a specified response type and
        status code on the given RestApi.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.put_gateway_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#put_gateway_response)
        """
    def put_integration(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        type: IntegrationTypeType,
        integrationHttpMethod: str = None,
        uri: str = None,
        connectionType: ConnectionTypeType = None,
        connectionId: str = None,
        credentials: str = None,
        requestParameters: Dict[str, str] = None,
        requestTemplates: Dict[str, str] = None,
        passthroughBehavior: str = None,
        cacheNamespace: str = None,
        cacheKeyParameters: List[str] = None,
        contentHandling: ContentHandlingStrategyType = None,
        timeoutInMillis: int = None,
        tlsConfig: "TlsConfigTypeDef" = None
    ) -> IntegrationResponseMetadataTypeDef:
        """
        Sets up a method's integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.put_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#put_integration)
        """
    def put_integration_response(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        selectionPattern: str = None,
        responseParameters: Dict[str, str] = None,
        responseTemplates: Dict[str, str] = None,
        contentHandling: ContentHandlingStrategyType = None
    ) -> IntegrationResponseResponseMetadataTypeDef:
        """
        Represents a put integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.put_integration_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#put_integration_response)
        """
    def put_method(
        self,
        *,
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
        authorizationScopes: List[str] = None
    ) -> MethodResponseMetadataTypeDef:
        """
        Add a method to an existing Resource resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.put_method)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#put_method)
        """
    def put_method_response(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        responseParameters: Dict[str, bool] = None,
        responseModels: Dict[str, str] = None
    ) -> MethodResponseResponseMetadataTypeDef:
        """
        Adds a MethodResponse to an existing Method resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.put_method_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#put_method_response)
        """
    def put_rest_api(
        self,
        *,
        restApiId: str,
        body: Union[bytes, IO[bytes], StreamingBody],
        mode: PutModeType = None,
        failOnWarnings: bool = None,
        parameters: Dict[str, str] = None
    ) -> RestApiResponseMetadataTypeDef:
        """
        A feature of the API Gateway control service for updating an existing API with
        an input of external API definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.put_rest_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#put_rest_api)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> None:
        """
        Adds or updates a tag on a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#tag_resource)
        """
    def test_invoke_authorizer(
        self,
        *,
        restApiId: str,
        authorizerId: str,
        headers: Dict[str, str] = None,
        multiValueHeaders: Dict[str, List[str]] = None,
        pathWithQueryString: str = None,
        body: str = None,
        stageVariables: Dict[str, str] = None,
        additionalContext: Dict[str, str] = None
    ) -> TestInvokeAuthorizerResponseTypeDef:
        """
        Simulate the execution of an Authorizer in your RestApi with headers,
        parameters, and an incoming request body.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.test_invoke_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#test_invoke_authorizer)
        """
    def test_invoke_method(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        pathWithQueryString: str = None,
        body: str = None,
        headers: Dict[str, str] = None,
        multiValueHeaders: Dict[str, List[str]] = None,
        clientCertificateId: str = None,
        stageVariables: Dict[str, str] = None
    ) -> TestInvokeMethodResponseTypeDef:
        """
        Simulate the invocation of a Method in your RestApi with headers, parameters,
        and an incoming request body.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.test_invoke_method)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#test_invoke_method)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> None:
        """
        Removes a tag from a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#untag_resource)
        """
    def update_account(
        self, *, patchOperations: List["PatchOperationTypeDef"] = None
    ) -> AccountTypeDef:
        """
        Changes information about the current Account resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_account)
        """
    def update_api_key(
        self, *, apiKey: str, patchOperations: List["PatchOperationTypeDef"] = None
    ) -> ApiKeyResponseMetadataTypeDef:
        """
        Changes information about an ApiKey resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_api_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_api_key)
        """
    def update_authorizer(
        self,
        *,
        restApiId: str,
        authorizerId: str,
        patchOperations: List["PatchOperationTypeDef"] = None
    ) -> AuthorizerResponseMetadataTypeDef:
        """
        Updates an existing Authorizer resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_authorizer)
        """
    def update_base_path_mapping(
        self,
        *,
        domainName: str,
        basePath: str,
        patchOperations: List["PatchOperationTypeDef"] = None
    ) -> BasePathMappingResponseMetadataTypeDef:
        """
        Changes information about the BasePathMapping resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_base_path_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_base_path_mapping)
        """
    def update_client_certificate(
        self, *, clientCertificateId: str, patchOperations: List["PatchOperationTypeDef"] = None
    ) -> ClientCertificateResponseMetadataTypeDef:
        """
        Changes information about an ClientCertificate resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_client_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_client_certificate)
        """
    def update_deployment(
        self,
        *,
        restApiId: str,
        deploymentId: str,
        patchOperations: List["PatchOperationTypeDef"] = None
    ) -> DeploymentResponseMetadataTypeDef:
        """
        Changes information about a Deployment resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_deployment)
        """
    def update_documentation_part(
        self,
        *,
        restApiId: str,
        documentationPartId: str,
        patchOperations: List["PatchOperationTypeDef"] = None
    ) -> DocumentationPartResponseMetadataTypeDef:
        """
        Updates a documentation part.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_documentation_part)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_documentation_part)
        """
    def update_documentation_version(
        self,
        *,
        restApiId: str,
        documentationVersion: str,
        patchOperations: List["PatchOperationTypeDef"] = None
    ) -> DocumentationVersionResponseMetadataTypeDef:
        """
        Updates a documentation version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_documentation_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_documentation_version)
        """
    def update_domain_name(
        self, *, domainName: str, patchOperations: List["PatchOperationTypeDef"] = None
    ) -> DomainNameResponseMetadataTypeDef:
        """
        Changes information about the DomainName resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_domain_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_domain_name)
        """
    def update_gateway_response(
        self,
        *,
        restApiId: str,
        responseType: GatewayResponseTypeType,
        patchOperations: List["PatchOperationTypeDef"] = None
    ) -> GatewayResponseResponseMetadataTypeDef:
        """
        Updates a GatewayResponse of a specified response type on the given RestApi.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_gateway_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_gateway_response)
        """
    def update_integration(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        patchOperations: List["PatchOperationTypeDef"] = None
    ) -> IntegrationResponseMetadataTypeDef:
        """
        Represents an update integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_integration)
        """
    def update_integration_response(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        patchOperations: List["PatchOperationTypeDef"] = None
    ) -> IntegrationResponseResponseMetadataTypeDef:
        """
        Represents an update integration response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_integration_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_integration_response)
        """
    def update_method(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        patchOperations: List["PatchOperationTypeDef"] = None
    ) -> MethodResponseMetadataTypeDef:
        """
        Updates an existing Method resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_method)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_method)
        """
    def update_method_response(
        self,
        *,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        patchOperations: List["PatchOperationTypeDef"] = None
    ) -> MethodResponseResponseMetadataTypeDef:
        """
        Updates an existing MethodResponse resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_method_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_method_response)
        """
    def update_model(
        self,
        *,
        restApiId: str,
        modelName: str,
        patchOperations: List["PatchOperationTypeDef"] = None
    ) -> ModelResponseMetadataTypeDef:
        """
        Changes information about a model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_model)
        """
    def update_request_validator(
        self,
        *,
        restApiId: str,
        requestValidatorId: str,
        patchOperations: List["PatchOperationTypeDef"] = None
    ) -> RequestValidatorResponseMetadataTypeDef:
        """
        Updates a RequestValidator of a given RestApi.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_request_validator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_request_validator)
        """
    def update_resource(
        self,
        *,
        restApiId: str,
        resourceId: str,
        patchOperations: List["PatchOperationTypeDef"] = None
    ) -> ResourceResponseMetadataTypeDef:
        """
        Changes information about a Resource resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_resource)
        """
    def update_rest_api(
        self, *, restApiId: str, patchOperations: List["PatchOperationTypeDef"] = None
    ) -> RestApiResponseMetadataTypeDef:
        """
        Changes information about the specified API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_rest_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_rest_api)
        """
    def update_stage(
        self,
        *,
        restApiId: str,
        stageName: str,
        patchOperations: List["PatchOperationTypeDef"] = None
    ) -> StageResponseMetadataTypeDef:
        """
        Changes information about a Stage resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_stage)
        """
    def update_usage(
        self, *, usagePlanId: str, keyId: str, patchOperations: List["PatchOperationTypeDef"] = None
    ) -> UsageTypeDef:
        """
        Grants a temporary extension to the remaining quota of a usage plan associated
        with a specified API key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_usage)
        """
    def update_usage_plan(
        self, *, usagePlanId: str, patchOperations: List["PatchOperationTypeDef"] = None
    ) -> UsagePlanResponseMetadataTypeDef:
        """
        Updates a usage plan of a given plan Id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_usage_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_usage_plan)
        """
    def update_vpc_link(
        self, *, vpcLinkId: str, patchOperations: List["PatchOperationTypeDef"] = None
    ) -> VpcLinkResponseMetadataTypeDef:
        """
        Updates an existing VpcLink of a specified identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Client.update_vpc_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update_vpc_link)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_api_keys"]) -> GetApiKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Paginator.GetApiKeys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getapikeyspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_authorizers"]) -> GetAuthorizersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Paginator.GetAuthorizers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getauthorizerspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_base_path_mappings"]
    ) -> GetBasePathMappingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Paginator.GetBasePathMappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getbasepathmappingspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_client_certificates"]
    ) -> GetClientCertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Paginator.GetClientCertificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getclientcertificatespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_deployments"]) -> GetDeploymentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Paginator.GetDeployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getdeploymentspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_documentation_parts"]
    ) -> GetDocumentationPartsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationParts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getdocumentationpartspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_documentation_versions"]
    ) -> GetDocumentationVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getdocumentationversionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_domain_names"]) -> GetDomainNamesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Paginator.GetDomainNames)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getdomainnamespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_gateway_responses"]
    ) -> GetGatewayResponsesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Paginator.GetGatewayResponses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getgatewayresponsespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_models"]) -> GetModelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Paginator.GetModels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getmodelspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_request_validators"]
    ) -> GetRequestValidatorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Paginator.GetRequestValidators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getrequestvalidatorspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_resources"]) -> GetResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Paginator.GetResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getresourcespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_rest_apis"]) -> GetRestApisPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Paginator.GetRestApis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getrestapispaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_sdk_types"]) -> GetSdkTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Paginator.GetSdkTypes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getsdktypespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_usage"]) -> GetUsagePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Paginator.GetUsage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getusagepaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_usage_plan_keys"]
    ) -> GetUsagePlanKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlanKeys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getusageplankeyspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_usage_plans"]) -> GetUsagePlansPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getusageplanspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_vpc_links"]) -> GetVpcLinksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/apigateway.html#APIGateway.Paginator.GetVpcLinks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getvpclinkspaginator)
        """
