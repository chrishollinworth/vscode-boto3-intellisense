"""
Type annotations for apigatewayv2 service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_apigatewayv2 import ApiGatewayV2Client
    from mypy_boto3_apigatewayv2.paginator import (
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

    client: ApiGatewayV2Client = boto3.client("apigatewayv2")

    get_apis_paginator: GetApisPaginator = client.get_paginator("get_apis")
    get_authorizers_paginator: GetAuthorizersPaginator = client.get_paginator("get_authorizers")
    get_deployments_paginator: GetDeploymentsPaginator = client.get_paginator("get_deployments")
    get_domain_names_paginator: GetDomainNamesPaginator = client.get_paginator("get_domain_names")
    get_integration_responses_paginator: GetIntegrationResponsesPaginator = client.get_paginator("get_integration_responses")
    get_integrations_paginator: GetIntegrationsPaginator = client.get_paginator("get_integrations")
    get_models_paginator: GetModelsPaginator = client.get_paginator("get_models")
    get_route_responses_paginator: GetRouteResponsesPaginator = client.get_paginator("get_route_responses")
    get_routes_paginator: GetRoutesPaginator = client.get_paginator("get_routes")
    get_stages_paginator: GetStagesPaginator = client.get_paginator("get_stages")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    GetApisResponseTypeDef,
    GetAuthorizersResponseTypeDef,
    GetDeploymentsResponseTypeDef,
    GetDomainNamesResponseTypeDef,
    GetIntegrationResponsesResponseTypeDef,
    GetIntegrationsResponseTypeDef,
    GetModelsResponseTypeDef,
    GetRouteResponsesResponseTypeDef,
    GetRoutesResponseTypeDef,
    GetStagesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "GetApisPaginator",
    "GetAuthorizersPaginator",
    "GetDeploymentsPaginator",
    "GetDomainNamesPaginator",
    "GetIntegrationResponsesPaginator",
    "GetIntegrationsPaginator",
    "GetModelsPaginator",
    "GetRouteResponsesPaginator",
    "GetRoutesPaginator",
    "GetStagesPaginator",
)

class GetApisPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetApis)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getapispaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetApisResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetApis.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getapispaginator)
        """

class GetAuthorizersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetAuthorizers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getauthorizerspaginator)
    """

    def paginate(
        self, *, ApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetAuthorizersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetAuthorizers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getauthorizerspaginator)
        """

class GetDeploymentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetDeployments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getdeploymentspaginator)
    """

    def paginate(
        self, *, ApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDeploymentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetDeployments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getdeploymentspaginator)
        """

class GetDomainNamesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetDomainNames)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getdomainnamespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDomainNamesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetDomainNames.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getdomainnamespaginator)
        """

class GetIntegrationResponsesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetIntegrationResponses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getintegrationresponsespaginator)
    """

    def paginate(
        self, *, ApiId: str, IntegrationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetIntegrationResponsesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetIntegrationResponses.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getintegrationresponsespaginator)
        """

class GetIntegrationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetIntegrations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getintegrationspaginator)
    """

    def paginate(
        self, *, ApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetIntegrationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetIntegrations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getintegrationspaginator)
        """

class GetModelsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetModels)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getmodelspaginator)
    """

    def paginate(
        self, *, ApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetModelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetModels.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getmodelspaginator)
        """

class GetRouteResponsesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetRouteResponses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getrouteresponsespaginator)
    """

    def paginate(
        self, *, ApiId: str, RouteId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetRouteResponsesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetRouteResponses.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getrouteresponsespaginator)
        """

class GetRoutesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetRoutes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getroutespaginator)
    """

    def paginate(
        self, *, ApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetRoutesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetRoutes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getroutespaginator)
        """

class GetStagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetStages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getstagespaginator)
    """

    def paginate(
        self, *, ApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetStagesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetStages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getstagespaginator)
        """
