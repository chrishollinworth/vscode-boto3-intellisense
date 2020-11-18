# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for apigateway service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_apigateway import APIGatewayClient
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

    client: APIGatewayClient = boto3.client("apigateway")

    get_api_keys_paginator: GetApiKeysPaginator = client.get_paginator("get_api_keys")
    get_authorizers_paginator: GetAuthorizersPaginator = client.get_paginator("get_authorizers")
    get_base_path_mappings_paginator: GetBasePathMappingsPaginator = client.get_paginator("get_base_path_mappings")
    get_client_certificates_paginator: GetClientCertificatesPaginator = client.get_paginator("get_client_certificates")
    get_deployments_paginator: GetDeploymentsPaginator = client.get_paginator("get_deployments")
    get_documentation_parts_paginator: GetDocumentationPartsPaginator = client.get_paginator("get_documentation_parts")
    get_documentation_versions_paginator: GetDocumentationVersionsPaginator = client.get_paginator("get_documentation_versions")
    get_domain_names_paginator: GetDomainNamesPaginator = client.get_paginator("get_domain_names")
    get_gateway_responses_paginator: GetGatewayResponsesPaginator = client.get_paginator("get_gateway_responses")
    get_models_paginator: GetModelsPaginator = client.get_paginator("get_models")
    get_request_validators_paginator: GetRequestValidatorsPaginator = client.get_paginator("get_request_validators")
    get_resources_paginator: GetResourcesPaginator = client.get_paginator("get_resources")
    get_rest_apis_paginator: GetRestApisPaginator = client.get_paginator("get_rest_apis")
    get_sdk_types_paginator: GetSdkTypesPaginator = client.get_paginator("get_sdk_types")
    get_usage_paginator: GetUsagePaginator = client.get_paginator("get_usage")
    get_usage_plan_keys_paginator: GetUsagePlanKeysPaginator = client.get_paginator("get_usage_plan_keys")
    get_usage_plans_paginator: GetUsagePlansPaginator = client.get_paginator("get_usage_plans")
    get_vpc_links_paginator: GetVpcLinksPaginator = client.get_paginator("get_vpc_links")
    ```
"""
import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_apigateway.type_defs import (
    ApiKeysTypeDef,
    AuthorizersTypeDef,
    BasePathMappingsTypeDef,
    ClientCertificatesTypeDef,
    DeploymentsTypeDef,
    DocumentationPartsTypeDef,
    DocumentationVersionsTypeDef,
    DomainNamesTypeDef,
    GatewayResponsesTypeDef,
    ModelsTypeDef,
    PaginatorConfigTypeDef,
    RequestValidatorsTypeDef,
    ResourcesTypeDef,
    RestApisTypeDef,
    SdkTypesTypeDef,
    UsagePlanKeysTypeDef,
    UsagePlansTypeDef,
    UsageTypeDef,
    VpcLinksTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetApiKeysPaginator",
    "GetAuthorizersPaginator",
    "GetBasePathMappingsPaginator",
    "GetClientCertificatesPaginator",
    "GetDeploymentsPaginator",
    "GetDocumentationPartsPaginator",
    "GetDocumentationVersionsPaginator",
    "GetDomainNamesPaginator",
    "GetGatewayResponsesPaginator",
    "GetModelsPaginator",
    "GetRequestValidatorsPaginator",
    "GetResourcesPaginator",
    "GetRestApisPaginator",
    "GetSdkTypesPaginator",
    "GetUsagePaginator",
    "GetUsagePlanKeysPaginator",
    "GetUsagePlansPaginator",
    "GetVpcLinksPaginator",
)


class GetApiKeysPaginator(Boto3Paginator):
    """
    [Paginator.GetApiKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetApiKeys)
    """

    def paginate(
        self,
        nameQuery: str = None,
        customerId: str = None,
        includeValues: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ApiKeysTypeDef]:
        """
        [GetApiKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetApiKeys.paginate)
        """


class GetAuthorizersPaginator(Boto3Paginator):
    """
    [Paginator.GetAuthorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetAuthorizers)
    """

    def paginate(
        self, restApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[AuthorizersTypeDef]:
        """
        [GetAuthorizers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetAuthorizers.paginate)
        """


class GetBasePathMappingsPaginator(Boto3Paginator):
    """
    [Paginator.GetBasePathMappings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetBasePathMappings)
    """

    def paginate(
        self, domainName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[BasePathMappingsTypeDef]:
        """
        [GetBasePathMappings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetBasePathMappings.paginate)
        """


class GetClientCertificatesPaginator(Boto3Paginator):
    """
    [Paginator.GetClientCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetClientCertificates)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ClientCertificatesTypeDef]:
        """
        [GetClientCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetClientCertificates.paginate)
        """


class GetDeploymentsPaginator(Boto3Paginator):
    """
    [Paginator.GetDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetDeployments)
    """

    def paginate(
        self, restApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DeploymentsTypeDef]:
        """
        [GetDeployments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetDeployments.paginate)
        """


class GetDocumentationPartsPaginator(Boto3Paginator):
    """
    [Paginator.GetDocumentationParts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationParts)
    """

    def paginate(
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
        locationStatus: Literal["DOCUMENTED", "UNDOCUMENTED"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DocumentationPartsTypeDef]:
        """
        [GetDocumentationParts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationParts.paginate)
        """


class GetDocumentationVersionsPaginator(Boto3Paginator):
    """
    [Paginator.GetDocumentationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationVersions)
    """

    def paginate(
        self, restApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DocumentationVersionsTypeDef]:
        """
        [GetDocumentationVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationVersions.paginate)
        """


class GetDomainNamesPaginator(Boto3Paginator):
    """
    [Paginator.GetDomainNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetDomainNames)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DomainNamesTypeDef]:
        """
        [GetDomainNames.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetDomainNames.paginate)
        """


class GetGatewayResponsesPaginator(Boto3Paginator):
    """
    [Paginator.GetGatewayResponses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetGatewayResponses)
    """

    def paginate(
        self, restApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GatewayResponsesTypeDef]:
        """
        [GetGatewayResponses.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetGatewayResponses.paginate)
        """


class GetModelsPaginator(Boto3Paginator):
    """
    [Paginator.GetModels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetModels)
    """

    def paginate(
        self, restApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ModelsTypeDef]:
        """
        [GetModels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetModels.paginate)
        """


class GetRequestValidatorsPaginator(Boto3Paginator):
    """
    [Paginator.GetRequestValidators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetRequestValidators)
    """

    def paginate(
        self, restApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[RequestValidatorsTypeDef]:
        """
        [GetRequestValidators.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetRequestValidators.paginate)
        """


class GetResourcesPaginator(Boto3Paginator):
    """
    [Paginator.GetResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetResources)
    """

    def paginate(
        self,
        restApiId: str,
        embed: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ResourcesTypeDef]:
        """
        [GetResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetResources.paginate)
        """


class GetRestApisPaginator(Boto3Paginator):
    """
    [Paginator.GetRestApis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetRestApis)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[RestApisTypeDef]:
        """
        [GetRestApis.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetRestApis.paginate)
        """


class GetSdkTypesPaginator(Boto3Paginator):
    """
    [Paginator.GetSdkTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetSdkTypes)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SdkTypesTypeDef]:
        """
        [GetSdkTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetSdkTypes.paginate)
        """


class GetUsagePaginator(Boto3Paginator):
    """
    [Paginator.GetUsage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetUsage)
    """

    def paginate(
        self,
        usagePlanId: str,
        startDate: str,
        endDate: str,
        keyId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[UsageTypeDef]:
        """
        [GetUsage.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetUsage.paginate)
        """


class GetUsagePlanKeysPaginator(Boto3Paginator):
    """
    [Paginator.GetUsagePlanKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlanKeys)
    """

    def paginate(
        self,
        usagePlanId: str,
        nameQuery: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[UsagePlanKeysTypeDef]:
        """
        [GetUsagePlanKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlanKeys.paginate)
        """


class GetUsagePlansPaginator(Boto3Paginator):
    """
    [Paginator.GetUsagePlans documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlans)
    """

    def paginate(
        self, keyId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[UsagePlansTypeDef]:
        """
        [GetUsagePlans.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlans.paginate)
        """


class GetVpcLinksPaginator(Boto3Paginator):
    """
    [Paginator.GetVpcLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetVpcLinks)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[VpcLinksTypeDef]:
        """
        [GetVpcLinks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigateway.html#APIGateway.Paginator.GetVpcLinks.paginate)
        """
