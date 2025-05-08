"""
Type annotations for apigateway service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_apigateway.client import APIGatewayClient

    session = Session()
    client: APIGatewayClient = session.client("apigateway")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

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
    ApiKeyResponseTypeDef,
    ApiKeysTypeDef,
    AuthorizerResponseTypeDef,
    AuthorizersTypeDef,
    BasePathMappingResponseTypeDef,
    BasePathMappingsTypeDef,
    ClientCertificateResponseTypeDef,
    ClientCertificatesTypeDef,
    CreateApiKeyRequestTypeDef,
    CreateAuthorizerRequestTypeDef,
    CreateBasePathMappingRequestTypeDef,
    CreateDeploymentRequestTypeDef,
    CreateDocumentationPartRequestTypeDef,
    CreateDocumentationVersionRequestTypeDef,
    CreateDomainNameAccessAssociationRequestTypeDef,
    CreateDomainNameRequestTypeDef,
    CreateModelRequestTypeDef,
    CreateRequestValidatorRequestTypeDef,
    CreateResourceRequestTypeDef,
    CreateRestApiRequestTypeDef,
    CreateStageRequestTypeDef,
    CreateUsagePlanKeyRequestTypeDef,
    CreateUsagePlanRequestTypeDef,
    CreateVpcLinkRequestTypeDef,
    DeleteApiKeyRequestTypeDef,
    DeleteAuthorizerRequestTypeDef,
    DeleteBasePathMappingRequestTypeDef,
    DeleteClientCertificateRequestTypeDef,
    DeleteDeploymentRequestTypeDef,
    DeleteDocumentationPartRequestTypeDef,
    DeleteDocumentationVersionRequestTypeDef,
    DeleteDomainNameAccessAssociationRequestTypeDef,
    DeleteDomainNameRequestTypeDef,
    DeleteGatewayResponseRequestTypeDef,
    DeleteIntegrationRequestTypeDef,
    DeleteIntegrationResponseRequestTypeDef,
    DeleteMethodRequestTypeDef,
    DeleteMethodResponseRequestTypeDef,
    DeleteModelRequestTypeDef,
    DeleteRequestValidatorRequestTypeDef,
    DeleteResourceRequestTypeDef,
    DeleteRestApiRequestTypeDef,
    DeleteStageRequestTypeDef,
    DeleteUsagePlanKeyRequestTypeDef,
    DeleteUsagePlanRequestTypeDef,
    DeleteVpcLinkRequestTypeDef,
    DeploymentResponseTypeDef,
    DeploymentsTypeDef,
    DocumentationPartIdsTypeDef,
    DocumentationPartResponseTypeDef,
    DocumentationPartsTypeDef,
    DocumentationVersionResponseTypeDef,
    DocumentationVersionsTypeDef,
    DomainNameAccessAssociationResponseTypeDef,
    DomainNameAccessAssociationsTypeDef,
    DomainNameResponseTypeDef,
    DomainNamesTypeDef,
    EmptyResponseMetadataTypeDef,
    ExportResponseTypeDef,
    FlushStageAuthorizersCacheRequestTypeDef,
    FlushStageCacheRequestTypeDef,
    GatewayResponseResponseTypeDef,
    GatewayResponsesTypeDef,
    GenerateClientCertificateRequestTypeDef,
    GetApiKeyRequestTypeDef,
    GetApiKeysRequestTypeDef,
    GetAuthorizerRequestTypeDef,
    GetAuthorizersRequestTypeDef,
    GetBasePathMappingRequestTypeDef,
    GetBasePathMappingsRequestTypeDef,
    GetClientCertificateRequestTypeDef,
    GetClientCertificatesRequestTypeDef,
    GetDeploymentRequestTypeDef,
    GetDeploymentsRequestTypeDef,
    GetDocumentationPartRequestTypeDef,
    GetDocumentationPartsRequestTypeDef,
    GetDocumentationVersionRequestTypeDef,
    GetDocumentationVersionsRequestTypeDef,
    GetDomainNameAccessAssociationsRequestTypeDef,
    GetDomainNameRequestTypeDef,
    GetDomainNamesRequestTypeDef,
    GetExportRequestTypeDef,
    GetGatewayResponseRequestTypeDef,
    GetGatewayResponsesRequestTypeDef,
    GetIntegrationRequestTypeDef,
    GetIntegrationResponseRequestTypeDef,
    GetMethodRequestTypeDef,
    GetMethodResponseRequestTypeDef,
    GetModelRequestTypeDef,
    GetModelsRequestTypeDef,
    GetModelTemplateRequestTypeDef,
    GetRequestValidatorRequestTypeDef,
    GetRequestValidatorsRequestTypeDef,
    GetResourceRequestTypeDef,
    GetResourcesRequestTypeDef,
    GetRestApiRequestTypeDef,
    GetRestApisRequestTypeDef,
    GetSdkRequestTypeDef,
    GetSdkTypeRequestTypeDef,
    GetSdkTypesRequestTypeDef,
    GetStageRequestTypeDef,
    GetStagesRequestTypeDef,
    GetTagsRequestTypeDef,
    GetUsagePlanKeyRequestTypeDef,
    GetUsagePlanKeysRequestTypeDef,
    GetUsagePlanRequestTypeDef,
    GetUsagePlansRequestTypeDef,
    GetUsageRequestTypeDef,
    GetVpcLinkRequestTypeDef,
    GetVpcLinksRequestTypeDef,
    ImportApiKeysRequestTypeDef,
    ImportDocumentationPartsRequestTypeDef,
    ImportRestApiRequestTypeDef,
    IntegrationResponseExtraTypeDef,
    IntegrationResponseResponseTypeDef,
    MethodResponseExtraTypeDef,
    MethodResponseResponseTypeDef,
    ModelResponseTypeDef,
    ModelsTypeDef,
    PutGatewayResponseRequestTypeDef,
    PutIntegrationRequestTypeDef,
    PutIntegrationResponseRequestTypeDef,
    PutMethodRequestTypeDef,
    PutMethodResponseRequestTypeDef,
    PutRestApiRequestTypeDef,
    RejectDomainNameAccessAssociationRequestTypeDef,
    RequestValidatorResponseTypeDef,
    RequestValidatorsTypeDef,
    ResourceResponseTypeDef,
    ResourcesTypeDef,
    RestApiResponseTypeDef,
    RestApisTypeDef,
    SdkResponseTypeDef,
    SdkTypeResponseTypeDef,
    SdkTypesTypeDef,
    StageResponseTypeDef,
    StagesTypeDef,
    TagResourceRequestTypeDef,
    TagsTypeDef,
    TemplateTypeDef,
    TestInvokeAuthorizerRequestTypeDef,
    TestInvokeAuthorizerResponseTypeDef,
    TestInvokeMethodRequestTypeDef,
    TestInvokeMethodResponseTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAccountRequestTypeDef,
    UpdateApiKeyRequestTypeDef,
    UpdateAuthorizerRequestTypeDef,
    UpdateBasePathMappingRequestTypeDef,
    UpdateClientCertificateRequestTypeDef,
    UpdateDeploymentRequestTypeDef,
    UpdateDocumentationPartRequestTypeDef,
    UpdateDocumentationVersionRequestTypeDef,
    UpdateDomainNameRequestTypeDef,
    UpdateGatewayResponseRequestTypeDef,
    UpdateIntegrationRequestTypeDef,
    UpdateIntegrationResponseRequestTypeDef,
    UpdateMethodRequestTypeDef,
    UpdateMethodResponseRequestTypeDef,
    UpdateModelRequestTypeDef,
    UpdateRequestValidatorRequestTypeDef,
    UpdateResourceRequestTypeDef,
    UpdateRestApiRequestTypeDef,
    UpdateStageRequestTypeDef,
    UpdateUsagePlanRequestTypeDef,
    UpdateUsageRequestTypeDef,
    UpdateVpcLinkRequestTypeDef,
    UsagePlanKeyResponseTypeDef,
    UsagePlanKeysTypeDef,
    UsagePlanResponseTypeDef,
    UsagePlansTypeDef,
    UsageTypeDef,
    VpcLinkResponseTypeDef,
    VpcLinksTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("APIGatewayClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        APIGatewayClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#generate_presigned_url)
        """

    def create_api_key(self, **kwargs: Unpack[CreateApiKeyRequestTypeDef]) -> ApiKeyResponseTypeDef:
        """
        Create an ApiKey resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/create_api_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#create_api_key)
        """

    def create_authorizer(
        self, **kwargs: Unpack[CreateAuthorizerRequestTypeDef]
    ) -> AuthorizerResponseTypeDef:
        """
        Adds a new Authorizer resource to an existing RestApi resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/create_authorizer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#create_authorizer)
        """

    def create_base_path_mapping(
        self, **kwargs: Unpack[CreateBasePathMappingRequestTypeDef]
    ) -> BasePathMappingResponseTypeDef:
        """
        Creates a new BasePathMapping resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/create_base_path_mapping.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#create_base_path_mapping)
        """

    def create_deployment(
        self, **kwargs: Unpack[CreateDeploymentRequestTypeDef]
    ) -> DeploymentResponseTypeDef:
        """
        Creates a Deployment resource, which makes a specified RestApi callable over
        the internet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/create_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#create_deployment)
        """

    def create_documentation_part(
        self, **kwargs: Unpack[CreateDocumentationPartRequestTypeDef]
    ) -> DocumentationPartResponseTypeDef:
        """
        Creates a documentation part.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/create_documentation_part.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#create_documentation_part)
        """

    def create_documentation_version(
        self, **kwargs: Unpack[CreateDocumentationVersionRequestTypeDef]
    ) -> DocumentationVersionResponseTypeDef:
        """
        Creates a documentation version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/create_documentation_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#create_documentation_version)
        """

    def create_domain_name(
        self, **kwargs: Unpack[CreateDomainNameRequestTypeDef]
    ) -> DomainNameResponseTypeDef:
        """
        Creates a new domain name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/create_domain_name.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#create_domain_name)
        """

    def create_domain_name_access_association(
        self, **kwargs: Unpack[CreateDomainNameAccessAssociationRequestTypeDef]
    ) -> DomainNameAccessAssociationResponseTypeDef:
        """
        Creates a domain name access association resource between an access association
        source and a private custom domain name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/create_domain_name_access_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#create_domain_name_access_association)
        """

    def create_model(self, **kwargs: Unpack[CreateModelRequestTypeDef]) -> ModelResponseTypeDef:
        """
        Adds a new Model resource to an existing RestApi resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/create_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#create_model)
        """

    def create_request_validator(
        self, **kwargs: Unpack[CreateRequestValidatorRequestTypeDef]
    ) -> RequestValidatorResponseTypeDef:
        """
        Creates a RequestValidator of a given RestApi.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/create_request_validator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#create_request_validator)
        """

    def create_resource(
        self, **kwargs: Unpack[CreateResourceRequestTypeDef]
    ) -> ResourceResponseTypeDef:
        """
        Creates a Resource resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/create_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#create_resource)
        """

    def create_rest_api(
        self, **kwargs: Unpack[CreateRestApiRequestTypeDef]
    ) -> RestApiResponseTypeDef:
        """
        Creates a new RestApi resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/create_rest_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#create_rest_api)
        """

    def create_stage(self, **kwargs: Unpack[CreateStageRequestTypeDef]) -> StageResponseTypeDef:
        """
        Creates a new Stage resource that references a pre-existing Deployment for the
        API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/create_stage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#create_stage)
        """

    def create_usage_plan(
        self, **kwargs: Unpack[CreateUsagePlanRequestTypeDef]
    ) -> UsagePlanResponseTypeDef:
        """
        Creates a usage plan with the throttle and quota limits, as well as the
        associated API stages, specified in the payload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/create_usage_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#create_usage_plan)
        """

    def create_usage_plan_key(
        self, **kwargs: Unpack[CreateUsagePlanKeyRequestTypeDef]
    ) -> UsagePlanKeyResponseTypeDef:
        """
        Creates a usage plan key for adding an existing API key to a usage plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/create_usage_plan_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#create_usage_plan_key)
        """

    def create_vpc_link(
        self, **kwargs: Unpack[CreateVpcLinkRequestTypeDef]
    ) -> VpcLinkResponseTypeDef:
        """
        Creates a VPC link, under the caller's account in a selected region, in an
        asynchronous operation that typically takes 2-4 minutes to complete and become
        operational.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/create_vpc_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#create_vpc_link)
        """

    def delete_api_key(
        self, **kwargs: Unpack[DeleteApiKeyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the ApiKey resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_api_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_api_key)
        """

    def delete_authorizer(
        self, **kwargs: Unpack[DeleteAuthorizerRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an existing Authorizer resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_authorizer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_authorizer)
        """

    def delete_base_path_mapping(
        self, **kwargs: Unpack[DeleteBasePathMappingRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the BasePathMapping resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_base_path_mapping.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_base_path_mapping)
        """

    def delete_client_certificate(
        self, **kwargs: Unpack[DeleteClientCertificateRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the ClientCertificate resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_client_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_client_certificate)
        """

    def delete_deployment(
        self, **kwargs: Unpack[DeleteDeploymentRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a Deployment resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_deployment)
        """

    def delete_documentation_part(
        self, **kwargs: Unpack[DeleteDocumentationPartRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a documentation part.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_documentation_part.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_documentation_part)
        """

    def delete_documentation_version(
        self, **kwargs: Unpack[DeleteDocumentationVersionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a documentation version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_documentation_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_documentation_version)
        """

    def delete_domain_name(
        self, **kwargs: Unpack[DeleteDomainNameRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the DomainName resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_domain_name.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_domain_name)
        """

    def delete_domain_name_access_association(
        self, **kwargs: Unpack[DeleteDomainNameAccessAssociationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the DomainNameAccessAssociation resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_domain_name_access_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_domain_name_access_association)
        """

    def delete_gateway_response(
        self, **kwargs: Unpack[DeleteGatewayResponseRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Clears any customization of a GatewayResponse of a specified response type on
        the given RestApi and resets it with the default settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_gateway_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_gateway_response)
        """

    def delete_integration(
        self, **kwargs: Unpack[DeleteIntegrationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Represents a delete integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_integration)
        """

    def delete_integration_response(
        self, **kwargs: Unpack[DeleteIntegrationResponseRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Represents a delete integration response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_integration_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_integration_response)
        """

    def delete_method(
        self, **kwargs: Unpack[DeleteMethodRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an existing Method resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_method.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_method)
        """

    def delete_method_response(
        self, **kwargs: Unpack[DeleteMethodResponseRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an existing MethodResponse resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_method_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_method_response)
        """

    def delete_model(
        self, **kwargs: Unpack[DeleteModelRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_model)
        """

    def delete_request_validator(
        self, **kwargs: Unpack[DeleteRequestValidatorRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a RequestValidator of a given RestApi.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_request_validator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_request_validator)
        """

    def delete_resource(
        self, **kwargs: Unpack[DeleteResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a Resource resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_resource)
        """

    def delete_rest_api(
        self, **kwargs: Unpack[DeleteRestApiRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_rest_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_rest_api)
        """

    def delete_stage(
        self, **kwargs: Unpack[DeleteStageRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a Stage resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_stage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_stage)
        """

    def delete_usage_plan(
        self, **kwargs: Unpack[DeleteUsagePlanRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a usage plan of a given plan Id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_usage_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_usage_plan)
        """

    def delete_usage_plan_key(
        self, **kwargs: Unpack[DeleteUsagePlanKeyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a usage plan key and remove the underlying API key from the associated
        usage plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_usage_plan_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_usage_plan_key)
        """

    def delete_vpc_link(
        self, **kwargs: Unpack[DeleteVpcLinkRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an existing VpcLink of a specified identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/delete_vpc_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#delete_vpc_link)
        """

    def flush_stage_authorizers_cache(
        self, **kwargs: Unpack[FlushStageAuthorizersCacheRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Flushes all authorizer cache entries on a stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/flush_stage_authorizers_cache.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#flush_stage_authorizers_cache)
        """

    def flush_stage_cache(
        self, **kwargs: Unpack[FlushStageCacheRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Flushes a stage's cache.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/flush_stage_cache.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#flush_stage_cache)
        """

    def generate_client_certificate(
        self, **kwargs: Unpack[GenerateClientCertificateRequestTypeDef]
    ) -> ClientCertificateResponseTypeDef:
        """
        Generates a ClientCertificate resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/generate_client_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#generate_client_certificate)
        """

    def get_account(self) -> AccountTypeDef:
        """
        Gets information about the current Account resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_account)
        """

    def get_api_key(self, **kwargs: Unpack[GetApiKeyRequestTypeDef]) -> ApiKeyResponseTypeDef:
        """
        Gets information about the current ApiKey resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_api_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_api_key)
        """

    def get_api_keys(self, **kwargs: Unpack[GetApiKeysRequestTypeDef]) -> ApiKeysTypeDef:
        """
        Gets information about the current ApiKeys resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_api_keys.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_api_keys)
        """

    def get_authorizer(
        self, **kwargs: Unpack[GetAuthorizerRequestTypeDef]
    ) -> AuthorizerResponseTypeDef:
        """
        Describe an existing Authorizer resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_authorizer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_authorizer)
        """

    def get_authorizers(self, **kwargs: Unpack[GetAuthorizersRequestTypeDef]) -> AuthorizersTypeDef:
        """
        Describe an existing Authorizers resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_authorizers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_authorizers)
        """

    def get_base_path_mapping(
        self, **kwargs: Unpack[GetBasePathMappingRequestTypeDef]
    ) -> BasePathMappingResponseTypeDef:
        """
        Describe a BasePathMapping resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_base_path_mapping.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_base_path_mapping)
        """

    def get_base_path_mappings(
        self, **kwargs: Unpack[GetBasePathMappingsRequestTypeDef]
    ) -> BasePathMappingsTypeDef:
        """
        Represents a collection of BasePathMapping resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_base_path_mappings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_base_path_mappings)
        """

    def get_client_certificate(
        self, **kwargs: Unpack[GetClientCertificateRequestTypeDef]
    ) -> ClientCertificateResponseTypeDef:
        """
        Gets information about the current ClientCertificate resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_client_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_client_certificate)
        """

    def get_client_certificates(
        self, **kwargs: Unpack[GetClientCertificatesRequestTypeDef]
    ) -> ClientCertificatesTypeDef:
        """
        Gets a collection of ClientCertificate resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_client_certificates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_client_certificates)
        """

    def get_deployment(
        self, **kwargs: Unpack[GetDeploymentRequestTypeDef]
    ) -> DeploymentResponseTypeDef:
        """
        Gets information about a Deployment resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_deployment)
        """

    def get_deployments(self, **kwargs: Unpack[GetDeploymentsRequestTypeDef]) -> DeploymentsTypeDef:
        """
        Gets information about a Deployments collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_deployments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_deployments)
        """

    def get_documentation_part(
        self, **kwargs: Unpack[GetDocumentationPartRequestTypeDef]
    ) -> DocumentationPartResponseTypeDef:
        """
        Gets a documentation part.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_documentation_part.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_documentation_part)
        """

    def get_documentation_parts(
        self, **kwargs: Unpack[GetDocumentationPartsRequestTypeDef]
    ) -> DocumentationPartsTypeDef:
        """
        Gets documentation parts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_documentation_parts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_documentation_parts)
        """

    def get_documentation_version(
        self, **kwargs: Unpack[GetDocumentationVersionRequestTypeDef]
    ) -> DocumentationVersionResponseTypeDef:
        """
        Gets a documentation version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_documentation_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_documentation_version)
        """

    def get_documentation_versions(
        self, **kwargs: Unpack[GetDocumentationVersionsRequestTypeDef]
    ) -> DocumentationVersionsTypeDef:
        """
        Gets documentation versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_documentation_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_documentation_versions)
        """

    def get_domain_name(
        self, **kwargs: Unpack[GetDomainNameRequestTypeDef]
    ) -> DomainNameResponseTypeDef:
        """
        Represents a domain name that is contained in a simpler, more intuitive URL
        that can be called.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_domain_name.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_domain_name)
        """

    def get_domain_name_access_associations(
        self, **kwargs: Unpack[GetDomainNameAccessAssociationsRequestTypeDef]
    ) -> DomainNameAccessAssociationsTypeDef:
        """
        Represents a collection on DomainNameAccessAssociations resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_domain_name_access_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_domain_name_access_associations)
        """

    def get_domain_names(
        self, **kwargs: Unpack[GetDomainNamesRequestTypeDef]
    ) -> DomainNamesTypeDef:
        """
        Represents a collection of DomainName resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_domain_names.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_domain_names)
        """

    def get_export(self, **kwargs: Unpack[GetExportRequestTypeDef]) -> ExportResponseTypeDef:
        """
        Exports a deployed version of a RestApi in a specified format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_export.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_export)
        """

    def get_gateway_response(
        self, **kwargs: Unpack[GetGatewayResponseRequestTypeDef]
    ) -> GatewayResponseResponseTypeDef:
        """
        Gets a GatewayResponse of a specified response type on the given RestApi.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_gateway_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_gateway_response)
        """

    def get_gateway_responses(
        self, **kwargs: Unpack[GetGatewayResponsesRequestTypeDef]
    ) -> GatewayResponsesTypeDef:
        """
        Gets the GatewayResponses collection on the given RestApi.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_gateway_responses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_gateway_responses)
        """

    def get_integration(
        self, **kwargs: Unpack[GetIntegrationRequestTypeDef]
    ) -> IntegrationResponseExtraTypeDef:
        """
        Get the integration settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_integration)
        """

    def get_integration_response(
        self, **kwargs: Unpack[GetIntegrationResponseRequestTypeDef]
    ) -> IntegrationResponseResponseTypeDef:
        """
        Represents a get integration response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_integration_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_integration_response)
        """

    def get_method(self, **kwargs: Unpack[GetMethodRequestTypeDef]) -> MethodResponseExtraTypeDef:
        """
        Describe an existing Method resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_method.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_method)
        """

    def get_method_response(
        self, **kwargs: Unpack[GetMethodResponseRequestTypeDef]
    ) -> MethodResponseResponseTypeDef:
        """
        Describes a MethodResponse resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_method_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_method_response)
        """

    def get_model(self, **kwargs: Unpack[GetModelRequestTypeDef]) -> ModelResponseTypeDef:
        """
        Describes an existing model defined for a RestApi resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_model)
        """

    def get_model_template(
        self, **kwargs: Unpack[GetModelTemplateRequestTypeDef]
    ) -> TemplateTypeDef:
        """
        Generates a sample mapping template that can be used to transform a payload
        into the structure of a model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_model_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_model_template)
        """

    def get_models(self, **kwargs: Unpack[GetModelsRequestTypeDef]) -> ModelsTypeDef:
        """
        Describes existing Models defined for a RestApi resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_models.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_models)
        """

    def get_request_validator(
        self, **kwargs: Unpack[GetRequestValidatorRequestTypeDef]
    ) -> RequestValidatorResponseTypeDef:
        """
        Gets a RequestValidator of a given RestApi.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_request_validator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_request_validator)
        """

    def get_request_validators(
        self, **kwargs: Unpack[GetRequestValidatorsRequestTypeDef]
    ) -> RequestValidatorsTypeDef:
        """
        Gets the RequestValidators collection of a given RestApi.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_request_validators.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_request_validators)
        """

    def get_resource(self, **kwargs: Unpack[GetResourceRequestTypeDef]) -> ResourceResponseTypeDef:
        """
        Lists information about a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_resource)
        """

    def get_resources(self, **kwargs: Unpack[GetResourcesRequestTypeDef]) -> ResourcesTypeDef:
        """
        Lists information about a collection of Resource resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_resources)
        """

    def get_rest_api(self, **kwargs: Unpack[GetRestApiRequestTypeDef]) -> RestApiResponseTypeDef:
        """
        Lists the RestApi resource in the collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_rest_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_rest_api)
        """

    def get_rest_apis(self, **kwargs: Unpack[GetRestApisRequestTypeDef]) -> RestApisTypeDef:
        """
        Lists the RestApis resources for your collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_rest_apis.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_rest_apis)
        """

    def get_sdk(self, **kwargs: Unpack[GetSdkRequestTypeDef]) -> SdkResponseTypeDef:
        """
        Generates a client SDK for a RestApi and Stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_sdk.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_sdk)
        """

    def get_sdk_type(self, **kwargs: Unpack[GetSdkTypeRequestTypeDef]) -> SdkTypeResponseTypeDef:
        """
        Gets an SDK type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_sdk_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_sdk_type)
        """

    def get_sdk_types(self, **kwargs: Unpack[GetSdkTypesRequestTypeDef]) -> SdkTypesTypeDef:
        """
        Gets SDK types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_sdk_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_sdk_types)
        """

    def get_stage(self, **kwargs: Unpack[GetStageRequestTypeDef]) -> StageResponseTypeDef:
        """
        Gets information about a Stage resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_stage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_stage)
        """

    def get_stages(self, **kwargs: Unpack[GetStagesRequestTypeDef]) -> StagesTypeDef:
        """
        Gets information about one or more Stage resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_stages.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_stages)
        """

    def get_tags(self, **kwargs: Unpack[GetTagsRequestTypeDef]) -> TagsTypeDef:
        """
        Gets the Tags collection for a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_tags)
        """

    def get_usage(self, **kwargs: Unpack[GetUsageRequestTypeDef]) -> UsageTypeDef:
        """
        Gets the usage data of a usage plan in a specified time interval.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_usage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_usage)
        """

    def get_usage_plan(
        self, **kwargs: Unpack[GetUsagePlanRequestTypeDef]
    ) -> UsagePlanResponseTypeDef:
        """
        Gets a usage plan of a given plan identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_usage_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_usage_plan)
        """

    def get_usage_plan_key(
        self, **kwargs: Unpack[GetUsagePlanKeyRequestTypeDef]
    ) -> UsagePlanKeyResponseTypeDef:
        """
        Gets a usage plan key of a given key identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_usage_plan_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_usage_plan_key)
        """

    def get_usage_plan_keys(
        self, **kwargs: Unpack[GetUsagePlanKeysRequestTypeDef]
    ) -> UsagePlanKeysTypeDef:
        """
        Gets all the usage plan keys representing the API keys added to a specified
        usage plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_usage_plan_keys.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_usage_plan_keys)
        """

    def get_usage_plans(self, **kwargs: Unpack[GetUsagePlansRequestTypeDef]) -> UsagePlansTypeDef:
        """
        Gets all the usage plans of the caller's account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_usage_plans.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_usage_plans)
        """

    def get_vpc_link(self, **kwargs: Unpack[GetVpcLinkRequestTypeDef]) -> VpcLinkResponseTypeDef:
        """
        Gets a specified VPC link under the caller's account in a region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_vpc_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_vpc_link)
        """

    def get_vpc_links(self, **kwargs: Unpack[GetVpcLinksRequestTypeDef]) -> VpcLinksTypeDef:
        """
        Gets the VpcLinks collection under the caller's account in a selected region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_vpc_links.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_vpc_links)
        """

    def import_api_keys(self, **kwargs: Unpack[ImportApiKeysRequestTypeDef]) -> ApiKeyIdsTypeDef:
        """
        Import API keys from an external source, such as a CSV-formatted file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/import_api_keys.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#import_api_keys)
        """

    def import_documentation_parts(
        self, **kwargs: Unpack[ImportDocumentationPartsRequestTypeDef]
    ) -> DocumentationPartIdsTypeDef:
        """
        Imports documentation parts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/import_documentation_parts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#import_documentation_parts)
        """

    def import_rest_api(
        self, **kwargs: Unpack[ImportRestApiRequestTypeDef]
    ) -> RestApiResponseTypeDef:
        """
        A feature of the API Gateway control service for creating a new API from an
        external API definition file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/import_rest_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#import_rest_api)
        """

    def put_gateway_response(
        self, **kwargs: Unpack[PutGatewayResponseRequestTypeDef]
    ) -> GatewayResponseResponseTypeDef:
        """
        Creates a customization of a GatewayResponse of a specified response type and
        status code on the given RestApi.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/put_gateway_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#put_gateway_response)
        """

    def put_integration(
        self, **kwargs: Unpack[PutIntegrationRequestTypeDef]
    ) -> IntegrationResponseExtraTypeDef:
        """
        Sets up a method's integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/put_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#put_integration)
        """

    def put_integration_response(
        self, **kwargs: Unpack[PutIntegrationResponseRequestTypeDef]
    ) -> IntegrationResponseResponseTypeDef:
        """
        Represents a put integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/put_integration_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#put_integration_response)
        """

    def put_method(self, **kwargs: Unpack[PutMethodRequestTypeDef]) -> MethodResponseExtraTypeDef:
        """
        Add a method to an existing Resource resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/put_method.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#put_method)
        """

    def put_method_response(
        self, **kwargs: Unpack[PutMethodResponseRequestTypeDef]
    ) -> MethodResponseResponseTypeDef:
        """
        Adds a MethodResponse to an existing Method resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/put_method_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#put_method_response)
        """

    def put_rest_api(self, **kwargs: Unpack[PutRestApiRequestTypeDef]) -> RestApiResponseTypeDef:
        """
        A feature of the API Gateway control service for updating an existing API with
        an input of external API definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/put_rest_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#put_rest_api)
        """

    def reject_domain_name_access_association(
        self, **kwargs: Unpack[RejectDomainNameAccessAssociationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Rejects a domain name access association with a private custom domain name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/reject_domain_name_access_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#reject_domain_name_access_association)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds or updates a tag on a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#tag_resource)
        """

    def test_invoke_authorizer(
        self, **kwargs: Unpack[TestInvokeAuthorizerRequestTypeDef]
    ) -> TestInvokeAuthorizerResponseTypeDef:
        """
        Simulate the execution of an Authorizer in your RestApi with headers,
        parameters, and an incoming request body.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/test_invoke_authorizer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#test_invoke_authorizer)
        """

    def test_invoke_method(
        self, **kwargs: Unpack[TestInvokeMethodRequestTypeDef]
    ) -> TestInvokeMethodResponseTypeDef:
        """
        Simulate the invocation of a Method in your RestApi with headers, parameters,
        and an incoming request body.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/test_invoke_method.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#test_invoke_method)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes a tag from a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#untag_resource)
        """

    def update_account(self, **kwargs: Unpack[UpdateAccountRequestTypeDef]) -> AccountTypeDef:
        """
        Changes information about the current Account resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_account)
        """

    def update_api_key(self, **kwargs: Unpack[UpdateApiKeyRequestTypeDef]) -> ApiKeyResponseTypeDef:
        """
        Changes information about an ApiKey resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_api_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_api_key)
        """

    def update_authorizer(
        self, **kwargs: Unpack[UpdateAuthorizerRequestTypeDef]
    ) -> AuthorizerResponseTypeDef:
        """
        Updates an existing Authorizer resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_authorizer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_authorizer)
        """

    def update_base_path_mapping(
        self, **kwargs: Unpack[UpdateBasePathMappingRequestTypeDef]
    ) -> BasePathMappingResponseTypeDef:
        """
        Changes information about the BasePathMapping resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_base_path_mapping.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_base_path_mapping)
        """

    def update_client_certificate(
        self, **kwargs: Unpack[UpdateClientCertificateRequestTypeDef]
    ) -> ClientCertificateResponseTypeDef:
        """
        Changes information about an ClientCertificate resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_client_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_client_certificate)
        """

    def update_deployment(
        self, **kwargs: Unpack[UpdateDeploymentRequestTypeDef]
    ) -> DeploymentResponseTypeDef:
        """
        Changes information about a Deployment resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_deployment)
        """

    def update_documentation_part(
        self, **kwargs: Unpack[UpdateDocumentationPartRequestTypeDef]
    ) -> DocumentationPartResponseTypeDef:
        """
        Updates a documentation part.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_documentation_part.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_documentation_part)
        """

    def update_documentation_version(
        self, **kwargs: Unpack[UpdateDocumentationVersionRequestTypeDef]
    ) -> DocumentationVersionResponseTypeDef:
        """
        Updates a documentation version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_documentation_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_documentation_version)
        """

    def update_domain_name(
        self, **kwargs: Unpack[UpdateDomainNameRequestTypeDef]
    ) -> DomainNameResponseTypeDef:
        """
        Changes information about the DomainName resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_domain_name.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_domain_name)
        """

    def update_gateway_response(
        self, **kwargs: Unpack[UpdateGatewayResponseRequestTypeDef]
    ) -> GatewayResponseResponseTypeDef:
        """
        Updates a GatewayResponse of a specified response type on the given RestApi.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_gateway_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_gateway_response)
        """

    def update_integration(
        self, **kwargs: Unpack[UpdateIntegrationRequestTypeDef]
    ) -> IntegrationResponseExtraTypeDef:
        """
        Represents an update integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_integration)
        """

    def update_integration_response(
        self, **kwargs: Unpack[UpdateIntegrationResponseRequestTypeDef]
    ) -> IntegrationResponseResponseTypeDef:
        """
        Represents an update integration response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_integration_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_integration_response)
        """

    def update_method(
        self, **kwargs: Unpack[UpdateMethodRequestTypeDef]
    ) -> MethodResponseExtraTypeDef:
        """
        Updates an existing Method resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_method.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_method)
        """

    def update_method_response(
        self, **kwargs: Unpack[UpdateMethodResponseRequestTypeDef]
    ) -> MethodResponseResponseTypeDef:
        """
        Updates an existing MethodResponse resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_method_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_method_response)
        """

    def update_model(self, **kwargs: Unpack[UpdateModelRequestTypeDef]) -> ModelResponseTypeDef:
        """
        Changes information about a model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_model)
        """

    def update_request_validator(
        self, **kwargs: Unpack[UpdateRequestValidatorRequestTypeDef]
    ) -> RequestValidatorResponseTypeDef:
        """
        Updates a RequestValidator of a given RestApi.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_request_validator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_request_validator)
        """

    def update_resource(
        self, **kwargs: Unpack[UpdateResourceRequestTypeDef]
    ) -> ResourceResponseTypeDef:
        """
        Changes information about a Resource resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_resource)
        """

    def update_rest_api(
        self, **kwargs: Unpack[UpdateRestApiRequestTypeDef]
    ) -> RestApiResponseTypeDef:
        """
        Changes information about the specified API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_rest_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_rest_api)
        """

    def update_stage(self, **kwargs: Unpack[UpdateStageRequestTypeDef]) -> StageResponseTypeDef:
        """
        Changes information about a Stage resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_stage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_stage)
        """

    def update_usage(self, **kwargs: Unpack[UpdateUsageRequestTypeDef]) -> UsageTypeDef:
        """
        Grants a temporary extension to the remaining quota of a usage plan associated
        with a specified API key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_usage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_usage)
        """

    def update_usage_plan(
        self, **kwargs: Unpack[UpdateUsagePlanRequestTypeDef]
    ) -> UsagePlanResponseTypeDef:
        """
        Updates a usage plan of a given plan Id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_usage_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_usage_plan)
        """

    def update_vpc_link(
        self, **kwargs: Unpack[UpdateVpcLinkRequestTypeDef]
    ) -> VpcLinkResponseTypeDef:
        """
        Updates an existing VpcLink of a specified identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/update_vpc_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#update_vpc_link)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_api_keys"]
    ) -> GetApiKeysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_authorizers"]
    ) -> GetAuthorizersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_base_path_mappings"]
    ) -> GetBasePathMappingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_client_certificates"]
    ) -> GetClientCertificatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_deployments"]
    ) -> GetDeploymentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_documentation_parts"]
    ) -> GetDocumentationPartsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_documentation_versions"]
    ) -> GetDocumentationVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_domain_names"]
    ) -> GetDomainNamesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_gateway_responses"]
    ) -> GetGatewayResponsesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_models"]
    ) -> GetModelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_request_validators"]
    ) -> GetRequestValidatorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_resources"]
    ) -> GetResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_rest_apis"]
    ) -> GetRestApisPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_sdk_types"]
    ) -> GetSdkTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_usage"]
    ) -> GetUsagePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_usage_plan_keys"]
    ) -> GetUsagePlanKeysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_usage_plans"]
    ) -> GetUsagePlansPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_vpc_links"]
    ) -> GetVpcLinksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client/#get_paginator)
        """
