"""
Type annotations for apigatewayv2 service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_apigatewayv2.client import ApiGatewayV2Client

    session = Session()
    client: ApiGatewayV2Client = session.client("apigatewayv2")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    GetApisPaginator,
    GetAuthorizersPaginator,
    GetDeploymentsPaginator,
    GetDomainNamesPaginator,
    GetIntegrationResponsesPaginator,
    GetIntegrationsPaginator,
    GetModelsPaginator,
    GetRouteResponsesPaginator,
    GetRoutesPaginator,
    GetStagesPaginator,
)
from .type_defs import (
    CreateApiMappingRequestTypeDef,
    CreateApiMappingResponseTypeDef,
    CreateApiRequestTypeDef,
    CreateApiResponseTypeDef,
    CreateAuthorizerRequestTypeDef,
    CreateAuthorizerResponseTypeDef,
    CreateDeploymentRequestTypeDef,
    CreateDeploymentResponseTypeDef,
    CreateDomainNameRequestTypeDef,
    CreateDomainNameResponseTypeDef,
    CreateIntegrationRequestTypeDef,
    CreateIntegrationResponseRequestTypeDef,
    CreateIntegrationResponseResponseTypeDef,
    CreateIntegrationResultTypeDef,
    CreateModelRequestTypeDef,
    CreateModelResponseTypeDef,
    CreateRouteRequestTypeDef,
    CreateRouteResponseRequestTypeDef,
    CreateRouteResponseResponseTypeDef,
    CreateRouteResultTypeDef,
    CreateStageRequestTypeDef,
    CreateStageResponseTypeDef,
    CreateVpcLinkRequestTypeDef,
    CreateVpcLinkResponseTypeDef,
    DeleteAccessLogSettingsRequestTypeDef,
    DeleteApiMappingRequestTypeDef,
    DeleteApiRequestTypeDef,
    DeleteAuthorizerRequestTypeDef,
    DeleteCorsConfigurationRequestTypeDef,
    DeleteDeploymentRequestTypeDef,
    DeleteDomainNameRequestTypeDef,
    DeleteIntegrationRequestTypeDef,
    DeleteIntegrationResponseRequestTypeDef,
    DeleteModelRequestTypeDef,
    DeleteRouteRequestParameterRequestTypeDef,
    DeleteRouteRequestTypeDef,
    DeleteRouteResponseRequestTypeDef,
    DeleteRouteSettingsRequestTypeDef,
    DeleteStageRequestTypeDef,
    DeleteVpcLinkRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    ExportApiRequestTypeDef,
    ExportApiResponseTypeDef,
    GetApiMappingRequestTypeDef,
    GetApiMappingResponseTypeDef,
    GetApiMappingsRequestTypeDef,
    GetApiMappingsResponseTypeDef,
    GetApiRequestTypeDef,
    GetApiResponseTypeDef,
    GetApisRequestTypeDef,
    GetApisResponseTypeDef,
    GetAuthorizerRequestTypeDef,
    GetAuthorizerResponseTypeDef,
    GetAuthorizersRequestTypeDef,
    GetAuthorizersResponseTypeDef,
    GetDeploymentRequestTypeDef,
    GetDeploymentResponseTypeDef,
    GetDeploymentsRequestTypeDef,
    GetDeploymentsResponseTypeDef,
    GetDomainNameRequestTypeDef,
    GetDomainNameResponseTypeDef,
    GetDomainNamesRequestTypeDef,
    GetDomainNamesResponseTypeDef,
    GetIntegrationRequestTypeDef,
    GetIntegrationResponseRequestTypeDef,
    GetIntegrationResponseResponseTypeDef,
    GetIntegrationResponsesRequestTypeDef,
    GetIntegrationResponsesResponseTypeDef,
    GetIntegrationResultTypeDef,
    GetIntegrationsRequestTypeDef,
    GetIntegrationsResponseTypeDef,
    GetModelRequestTypeDef,
    GetModelResponseTypeDef,
    GetModelsRequestTypeDef,
    GetModelsResponseTypeDef,
    GetModelTemplateRequestTypeDef,
    GetModelTemplateResponseTypeDef,
    GetRouteRequestTypeDef,
    GetRouteResponseRequestTypeDef,
    GetRouteResponseResponseTypeDef,
    GetRouteResponsesRequestTypeDef,
    GetRouteResponsesResponseTypeDef,
    GetRouteResultTypeDef,
    GetRoutesRequestTypeDef,
    GetRoutesResponseTypeDef,
    GetStageRequestTypeDef,
    GetStageResponseTypeDef,
    GetStagesRequestTypeDef,
    GetStagesResponseTypeDef,
    GetTagsRequestTypeDef,
    GetTagsResponseTypeDef,
    GetVpcLinkRequestTypeDef,
    GetVpcLinkResponseTypeDef,
    GetVpcLinksRequestTypeDef,
    GetVpcLinksResponseTypeDef,
    ImportApiRequestTypeDef,
    ImportApiResponseTypeDef,
    ReimportApiRequestTypeDef,
    ReimportApiResponseTypeDef,
    ResetAuthorizersCacheRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateApiMappingRequestTypeDef,
    UpdateApiMappingResponseTypeDef,
    UpdateApiRequestTypeDef,
    UpdateApiResponseTypeDef,
    UpdateAuthorizerRequestTypeDef,
    UpdateAuthorizerResponseTypeDef,
    UpdateDeploymentRequestTypeDef,
    UpdateDeploymentResponseTypeDef,
    UpdateDomainNameRequestTypeDef,
    UpdateDomainNameResponseTypeDef,
    UpdateIntegrationRequestTypeDef,
    UpdateIntegrationResponseRequestTypeDef,
    UpdateIntegrationResponseResponseTypeDef,
    UpdateIntegrationResultTypeDef,
    UpdateModelRequestTypeDef,
    UpdateModelResponseTypeDef,
    UpdateRouteRequestTypeDef,
    UpdateRouteResponseRequestTypeDef,
    UpdateRouteResponseResponseTypeDef,
    UpdateRouteResultTypeDef,
    UpdateStageRequestTypeDef,
    UpdateStageResponseTypeDef,
    UpdateVpcLinkRequestTypeDef,
    UpdateVpcLinkResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("ApiGatewayV2Client",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]

class ApiGatewayV2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ApiGatewayV2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#generate_presigned_url)
        """

    def create_api(self, **kwargs: Unpack[CreateApiRequestTypeDef]) -> CreateApiResponseTypeDef:
        """
        Creates an Api resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/create_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#create_api)
        """

    def create_api_mapping(
        self, **kwargs: Unpack[CreateApiMappingRequestTypeDef]
    ) -> CreateApiMappingResponseTypeDef:
        """
        Creates an API mapping.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/create_api_mapping.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#create_api_mapping)
        """

    def create_authorizer(
        self, **kwargs: Unpack[CreateAuthorizerRequestTypeDef]
    ) -> CreateAuthorizerResponseTypeDef:
        """
        Creates an Authorizer for an API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/create_authorizer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#create_authorizer)
        """

    def create_deployment(
        self, **kwargs: Unpack[CreateDeploymentRequestTypeDef]
    ) -> CreateDeploymentResponseTypeDef:
        """
        Creates a Deployment for an API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/create_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#create_deployment)
        """

    def create_domain_name(
        self, **kwargs: Unpack[CreateDomainNameRequestTypeDef]
    ) -> CreateDomainNameResponseTypeDef:
        """
        Creates a domain name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/create_domain_name.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#create_domain_name)
        """

    def create_integration(
        self, **kwargs: Unpack[CreateIntegrationRequestTypeDef]
    ) -> CreateIntegrationResultTypeDef:
        """
        Creates an Integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/create_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#create_integration)
        """

    def create_integration_response(
        self, **kwargs: Unpack[CreateIntegrationResponseRequestTypeDef]
    ) -> CreateIntegrationResponseResponseTypeDef:
        """
        Creates an IntegrationResponses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/create_integration_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#create_integration_response)
        """

    def create_model(
        self, **kwargs: Unpack[CreateModelRequestTypeDef]
    ) -> CreateModelResponseTypeDef:
        """
        Creates a Model for an API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/create_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#create_model)
        """

    def create_route(self, **kwargs: Unpack[CreateRouteRequestTypeDef]) -> CreateRouteResultTypeDef:
        """
        Creates a Route for an API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/create_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#create_route)
        """

    def create_route_response(
        self, **kwargs: Unpack[CreateRouteResponseRequestTypeDef]
    ) -> CreateRouteResponseResponseTypeDef:
        """
        Creates a RouteResponse for a Route.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/create_route_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#create_route_response)
        """

    def create_stage(
        self, **kwargs: Unpack[CreateStageRequestTypeDef]
    ) -> CreateStageResponseTypeDef:
        """
        Creates a Stage for an API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/create_stage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#create_stage)
        """

    def create_vpc_link(
        self, **kwargs: Unpack[CreateVpcLinkRequestTypeDef]
    ) -> CreateVpcLinkResponseTypeDef:
        """
        Creates a VPC link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/create_vpc_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#create_vpc_link)
        """

    def delete_access_log_settings(
        self, **kwargs: Unpack[DeleteAccessLogSettingsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the AccessLogSettings for a Stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/delete_access_log_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#delete_access_log_settings)
        """

    def delete_api(self, **kwargs: Unpack[DeleteApiRequestTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Api resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/delete_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#delete_api)
        """

    def delete_api_mapping(
        self, **kwargs: Unpack[DeleteApiMappingRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an API mapping.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/delete_api_mapping.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#delete_api_mapping)
        """

    def delete_authorizer(
        self, **kwargs: Unpack[DeleteAuthorizerRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Authorizer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/delete_authorizer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#delete_authorizer)
        """

    def delete_cors_configuration(
        self, **kwargs: Unpack[DeleteCorsConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a CORS configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/delete_cors_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#delete_cors_configuration)
        """

    def delete_deployment(
        self, **kwargs: Unpack[DeleteDeploymentRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a Deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/delete_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#delete_deployment)
        """

    def delete_domain_name(
        self, **kwargs: Unpack[DeleteDomainNameRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a domain name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/delete_domain_name.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#delete_domain_name)
        """

    def delete_integration(
        self, **kwargs: Unpack[DeleteIntegrationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/delete_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#delete_integration)
        """

    def delete_integration_response(
        self, **kwargs: Unpack[DeleteIntegrationResponseRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an IntegrationResponses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/delete_integration_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#delete_integration_response)
        """

    def delete_model(
        self, **kwargs: Unpack[DeleteModelRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a Model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/delete_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#delete_model)
        """

    def delete_route(
        self, **kwargs: Unpack[DeleteRouteRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a Route.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/delete_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#delete_route)
        """

    def delete_route_request_parameter(
        self, **kwargs: Unpack[DeleteRouteRequestParameterRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a route request parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/delete_route_request_parameter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#delete_route_request_parameter)
        """

    def delete_route_response(
        self, **kwargs: Unpack[DeleteRouteResponseRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a RouteResponse.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/delete_route_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#delete_route_response)
        """

    def delete_route_settings(
        self, **kwargs: Unpack[DeleteRouteSettingsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the RouteSettings for a stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/delete_route_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#delete_route_settings)
        """

    def delete_stage(
        self, **kwargs: Unpack[DeleteStageRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a Stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/delete_stage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#delete_stage)
        """

    def delete_vpc_link(self, **kwargs: Unpack[DeleteVpcLinkRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a VPC link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/delete_vpc_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#delete_vpc_link)
        """

    def export_api(self, **kwargs: Unpack[ExportApiRequestTypeDef]) -> ExportApiResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/export_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#export_api)
        """

    def reset_authorizers_cache(
        self, **kwargs: Unpack[ResetAuthorizersCacheRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Resets all authorizer cache entries on a stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/reset_authorizers_cache.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#reset_authorizers_cache)
        """

    def get_api(self, **kwargs: Unpack[GetApiRequestTypeDef]) -> GetApiResponseTypeDef:
        """
        Gets an Api resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_api)
        """

    def get_api_mapping(
        self, **kwargs: Unpack[GetApiMappingRequestTypeDef]
    ) -> GetApiMappingResponseTypeDef:
        """
        Gets an API mapping.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_api_mapping.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_api_mapping)
        """

    def get_api_mappings(
        self, **kwargs: Unpack[GetApiMappingsRequestTypeDef]
    ) -> GetApiMappingsResponseTypeDef:
        """
        Gets API mappings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_api_mappings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_api_mappings)
        """

    def get_apis(self, **kwargs: Unpack[GetApisRequestTypeDef]) -> GetApisResponseTypeDef:
        """
        Gets a collection of Api resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_apis.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_apis)
        """

    def get_authorizer(
        self, **kwargs: Unpack[GetAuthorizerRequestTypeDef]
    ) -> GetAuthorizerResponseTypeDef:
        """
        Gets an Authorizer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_authorizer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_authorizer)
        """

    def get_authorizers(
        self, **kwargs: Unpack[GetAuthorizersRequestTypeDef]
    ) -> GetAuthorizersResponseTypeDef:
        """
        Gets the Authorizers for an API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_authorizers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_authorizers)
        """

    def get_deployment(
        self, **kwargs: Unpack[GetDeploymentRequestTypeDef]
    ) -> GetDeploymentResponseTypeDef:
        """
        Gets a Deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_deployment)
        """

    def get_deployments(
        self, **kwargs: Unpack[GetDeploymentsRequestTypeDef]
    ) -> GetDeploymentsResponseTypeDef:
        """
        Gets the Deployments for an API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_deployments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_deployments)
        """

    def get_domain_name(
        self, **kwargs: Unpack[GetDomainNameRequestTypeDef]
    ) -> GetDomainNameResponseTypeDef:
        """
        Gets a domain name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_domain_name.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_domain_name)
        """

    def get_domain_names(
        self, **kwargs: Unpack[GetDomainNamesRequestTypeDef]
    ) -> GetDomainNamesResponseTypeDef:
        """
        Gets the domain names for an AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_domain_names.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_domain_names)
        """

    def get_integration(
        self, **kwargs: Unpack[GetIntegrationRequestTypeDef]
    ) -> GetIntegrationResultTypeDef:
        """
        Gets an Integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_integration)
        """

    def get_integration_response(
        self, **kwargs: Unpack[GetIntegrationResponseRequestTypeDef]
    ) -> GetIntegrationResponseResponseTypeDef:
        """
        Gets an IntegrationResponses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_integration_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_integration_response)
        """

    def get_integration_responses(
        self, **kwargs: Unpack[GetIntegrationResponsesRequestTypeDef]
    ) -> GetIntegrationResponsesResponseTypeDef:
        """
        Gets the IntegrationResponses for an Integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_integration_responses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_integration_responses)
        """

    def get_integrations(
        self, **kwargs: Unpack[GetIntegrationsRequestTypeDef]
    ) -> GetIntegrationsResponseTypeDef:
        """
        Gets the Integrations for an API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_integrations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_integrations)
        """

    def get_model(self, **kwargs: Unpack[GetModelRequestTypeDef]) -> GetModelResponseTypeDef:
        """
        Gets a Model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_model)
        """

    def get_model_template(
        self, **kwargs: Unpack[GetModelTemplateRequestTypeDef]
    ) -> GetModelTemplateResponseTypeDef:
        """
        Gets a model template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_model_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_model_template)
        """

    def get_models(self, **kwargs: Unpack[GetModelsRequestTypeDef]) -> GetModelsResponseTypeDef:
        """
        Gets the Models for an API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_models.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_models)
        """

    def get_route(self, **kwargs: Unpack[GetRouteRequestTypeDef]) -> GetRouteResultTypeDef:
        """
        Gets a Route.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_route)
        """

    def get_route_response(
        self, **kwargs: Unpack[GetRouteResponseRequestTypeDef]
    ) -> GetRouteResponseResponseTypeDef:
        """
        Gets a RouteResponse.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_route_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_route_response)
        """

    def get_route_responses(
        self, **kwargs: Unpack[GetRouteResponsesRequestTypeDef]
    ) -> GetRouteResponsesResponseTypeDef:
        """
        Gets the RouteResponses for a Route.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_route_responses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_route_responses)
        """

    def get_routes(self, **kwargs: Unpack[GetRoutesRequestTypeDef]) -> GetRoutesResponseTypeDef:
        """
        Gets the Routes for an API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_routes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_routes)
        """

    def get_stage(self, **kwargs: Unpack[GetStageRequestTypeDef]) -> GetStageResponseTypeDef:
        """
        Gets a Stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_stage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_stage)
        """

    def get_stages(self, **kwargs: Unpack[GetStagesRequestTypeDef]) -> GetStagesResponseTypeDef:
        """
        Gets the Stages for an API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_stages.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_stages)
        """

    def get_tags(self, **kwargs: Unpack[GetTagsRequestTypeDef]) -> GetTagsResponseTypeDef:
        """
        Gets a collection of Tag resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_tags)
        """

    def get_vpc_link(self, **kwargs: Unpack[GetVpcLinkRequestTypeDef]) -> GetVpcLinkResponseTypeDef:
        """
        Gets a VPC link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_vpc_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_vpc_link)
        """

    def get_vpc_links(
        self, **kwargs: Unpack[GetVpcLinksRequestTypeDef]
    ) -> GetVpcLinksResponseTypeDef:
        """
        Gets a collection of VPC links.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_vpc_links.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_vpc_links)
        """

    def import_api(self, **kwargs: Unpack[ImportApiRequestTypeDef]) -> ImportApiResponseTypeDef:
        """
        Imports an API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/import_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#import_api)
        """

    def reimport_api(
        self, **kwargs: Unpack[ReimportApiRequestTypeDef]
    ) -> ReimportApiResponseTypeDef:
        """
        Puts an Api resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/reimport_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#reimport_api)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates a new Tag resource to represent a tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a Tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#untag_resource)
        """

    def update_api(self, **kwargs: Unpack[UpdateApiRequestTypeDef]) -> UpdateApiResponseTypeDef:
        """
        Updates an Api resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/update_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#update_api)
        """

    def update_api_mapping(
        self, **kwargs: Unpack[UpdateApiMappingRequestTypeDef]
    ) -> UpdateApiMappingResponseTypeDef:
        """
        The API mapping.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/update_api_mapping.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#update_api_mapping)
        """

    def update_authorizer(
        self, **kwargs: Unpack[UpdateAuthorizerRequestTypeDef]
    ) -> UpdateAuthorizerResponseTypeDef:
        """
        Updates an Authorizer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/update_authorizer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#update_authorizer)
        """

    def update_deployment(
        self, **kwargs: Unpack[UpdateDeploymentRequestTypeDef]
    ) -> UpdateDeploymentResponseTypeDef:
        """
        Updates a Deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/update_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#update_deployment)
        """

    def update_domain_name(
        self, **kwargs: Unpack[UpdateDomainNameRequestTypeDef]
    ) -> UpdateDomainNameResponseTypeDef:
        """
        Updates a domain name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/update_domain_name.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#update_domain_name)
        """

    def update_integration(
        self, **kwargs: Unpack[UpdateIntegrationRequestTypeDef]
    ) -> UpdateIntegrationResultTypeDef:
        """
        Updates an Integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/update_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#update_integration)
        """

    def update_integration_response(
        self, **kwargs: Unpack[UpdateIntegrationResponseRequestTypeDef]
    ) -> UpdateIntegrationResponseResponseTypeDef:
        """
        Updates an IntegrationResponses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/update_integration_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#update_integration_response)
        """

    def update_model(
        self, **kwargs: Unpack[UpdateModelRequestTypeDef]
    ) -> UpdateModelResponseTypeDef:
        """
        Updates a Model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/update_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#update_model)
        """

    def update_route(self, **kwargs: Unpack[UpdateRouteRequestTypeDef]) -> UpdateRouteResultTypeDef:
        """
        Updates a Route.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/update_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#update_route)
        """

    def update_route_response(
        self, **kwargs: Unpack[UpdateRouteResponseRequestTypeDef]
    ) -> UpdateRouteResponseResponseTypeDef:
        """
        Updates a RouteResponse.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/update_route_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#update_route_response)
        """

    def update_stage(
        self, **kwargs: Unpack[UpdateStageRequestTypeDef]
    ) -> UpdateStageResponseTypeDef:
        """
        Updates a Stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/update_stage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#update_stage)
        """

    def update_vpc_link(
        self, **kwargs: Unpack[UpdateVpcLinkRequestTypeDef]
    ) -> UpdateVpcLinkResponseTypeDef:
        """
        Updates a VPC link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/update_vpc_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#update_vpc_link)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_apis"]
    ) -> GetApisPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_authorizers"]
    ) -> GetAuthorizersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_deployments"]
    ) -> GetDeploymentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_domain_names"]
    ) -> GetDomainNamesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_integration_responses"]
    ) -> GetIntegrationResponsesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_integrations"]
    ) -> GetIntegrationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_models"]
    ) -> GetModelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_route_responses"]
    ) -> GetRouteResponsesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_routes"]
    ) -> GetRoutesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_stages"]
    ) -> GetStagesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client/#get_paginator)
        """
