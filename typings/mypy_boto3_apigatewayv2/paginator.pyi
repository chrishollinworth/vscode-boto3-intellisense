"""
Type annotations for apigatewayv2 service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_apigatewayv2.client import ApiGatewayV2Client
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

    session = Session()
    client: ApiGatewayV2Client = session.client("apigatewayv2")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetApisRequestPaginateTypeDef,
    GetApisResponseTypeDef,
    GetAuthorizersRequestPaginateTypeDef,
    GetAuthorizersResponseTypeDef,
    GetDeploymentsRequestPaginateTypeDef,
    GetDeploymentsResponseTypeDef,
    GetDomainNamesRequestPaginateTypeDef,
    GetDomainNamesResponseTypeDef,
    GetIntegrationResponsesRequestPaginateTypeDef,
    GetIntegrationResponsesResponseTypeDef,
    GetIntegrationsRequestPaginateTypeDef,
    GetIntegrationsResponseTypeDef,
    GetModelsRequestPaginateTypeDef,
    GetModelsResponseTypeDef,
    GetRouteResponsesRequestPaginateTypeDef,
    GetRouteResponsesResponseTypeDef,
    GetRoutesRequestPaginateTypeDef,
    GetRoutesResponseTypeDef,
    GetStagesRequestPaginateTypeDef,
    GetStagesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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

if TYPE_CHECKING:
    _GetApisPaginatorBase = Paginator[GetApisResponseTypeDef]
else:
    _GetApisPaginatorBase = Paginator  # type: ignore[assignment]

class GetApisPaginator(_GetApisPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/paginator/GetApis.html#ApiGatewayV2.Paginator.GetApis)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/#getapispaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetApisRequestPaginateTypeDef]
    ) -> PageIterator[GetApisResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/paginator/GetApis.html#ApiGatewayV2.Paginator.GetApis.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/#getapispaginator)
        """

if TYPE_CHECKING:
    _GetAuthorizersPaginatorBase = Paginator[GetAuthorizersResponseTypeDef]
else:
    _GetAuthorizersPaginatorBase = Paginator  # type: ignore[assignment]

class GetAuthorizersPaginator(_GetAuthorizersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/paginator/GetAuthorizers.html#ApiGatewayV2.Paginator.GetAuthorizers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/#getauthorizerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetAuthorizersRequestPaginateTypeDef]
    ) -> PageIterator[GetAuthorizersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/paginator/GetAuthorizers.html#ApiGatewayV2.Paginator.GetAuthorizers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/#getauthorizerspaginator)
        """

if TYPE_CHECKING:
    _GetDeploymentsPaginatorBase = Paginator[GetDeploymentsResponseTypeDef]
else:
    _GetDeploymentsPaginatorBase = Paginator  # type: ignore[assignment]

class GetDeploymentsPaginator(_GetDeploymentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/paginator/GetDeployments.html#ApiGatewayV2.Paginator.GetDeployments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/#getdeploymentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetDeploymentsRequestPaginateTypeDef]
    ) -> PageIterator[GetDeploymentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/paginator/GetDeployments.html#ApiGatewayV2.Paginator.GetDeployments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/#getdeploymentspaginator)
        """

if TYPE_CHECKING:
    _GetDomainNamesPaginatorBase = Paginator[GetDomainNamesResponseTypeDef]
else:
    _GetDomainNamesPaginatorBase = Paginator  # type: ignore[assignment]

class GetDomainNamesPaginator(_GetDomainNamesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/paginator/GetDomainNames.html#ApiGatewayV2.Paginator.GetDomainNames)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/#getdomainnamespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetDomainNamesRequestPaginateTypeDef]
    ) -> PageIterator[GetDomainNamesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/paginator/GetDomainNames.html#ApiGatewayV2.Paginator.GetDomainNames.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/#getdomainnamespaginator)
        """

if TYPE_CHECKING:
    _GetIntegrationResponsesPaginatorBase = Paginator[GetIntegrationResponsesResponseTypeDef]
else:
    _GetIntegrationResponsesPaginatorBase = Paginator  # type: ignore[assignment]

class GetIntegrationResponsesPaginator(_GetIntegrationResponsesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/paginator/GetIntegrationResponses.html#ApiGatewayV2.Paginator.GetIntegrationResponses)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/#getintegrationresponsespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetIntegrationResponsesRequestPaginateTypeDef]
    ) -> PageIterator[GetIntegrationResponsesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/paginator/GetIntegrationResponses.html#ApiGatewayV2.Paginator.GetIntegrationResponses.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/#getintegrationresponsespaginator)
        """

if TYPE_CHECKING:
    _GetIntegrationsPaginatorBase = Paginator[GetIntegrationsResponseTypeDef]
else:
    _GetIntegrationsPaginatorBase = Paginator  # type: ignore[assignment]

class GetIntegrationsPaginator(_GetIntegrationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/paginator/GetIntegrations.html#ApiGatewayV2.Paginator.GetIntegrations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/#getintegrationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetIntegrationsRequestPaginateTypeDef]
    ) -> PageIterator[GetIntegrationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/paginator/GetIntegrations.html#ApiGatewayV2.Paginator.GetIntegrations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/#getintegrationspaginator)
        """

if TYPE_CHECKING:
    _GetModelsPaginatorBase = Paginator[GetModelsResponseTypeDef]
else:
    _GetModelsPaginatorBase = Paginator  # type: ignore[assignment]

class GetModelsPaginator(_GetModelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/paginator/GetModels.html#ApiGatewayV2.Paginator.GetModels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/#getmodelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetModelsRequestPaginateTypeDef]
    ) -> PageIterator[GetModelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/paginator/GetModels.html#ApiGatewayV2.Paginator.GetModels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/#getmodelspaginator)
        """

if TYPE_CHECKING:
    _GetRouteResponsesPaginatorBase = Paginator[GetRouteResponsesResponseTypeDef]
else:
    _GetRouteResponsesPaginatorBase = Paginator  # type: ignore[assignment]

class GetRouteResponsesPaginator(_GetRouteResponsesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/paginator/GetRouteResponses.html#ApiGatewayV2.Paginator.GetRouteResponses)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/#getrouteresponsespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetRouteResponsesRequestPaginateTypeDef]
    ) -> PageIterator[GetRouteResponsesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/paginator/GetRouteResponses.html#ApiGatewayV2.Paginator.GetRouteResponses.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/#getrouteresponsespaginator)
        """

if TYPE_CHECKING:
    _GetRoutesPaginatorBase = Paginator[GetRoutesResponseTypeDef]
else:
    _GetRoutesPaginatorBase = Paginator  # type: ignore[assignment]

class GetRoutesPaginator(_GetRoutesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/paginator/GetRoutes.html#ApiGatewayV2.Paginator.GetRoutes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/#getroutespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetRoutesRequestPaginateTypeDef]
    ) -> PageIterator[GetRoutesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/paginator/GetRoutes.html#ApiGatewayV2.Paginator.GetRoutes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/#getroutespaginator)
        """

if TYPE_CHECKING:
    _GetStagesPaginatorBase = Paginator[GetStagesResponseTypeDef]
else:
    _GetStagesPaginatorBase = Paginator  # type: ignore[assignment]

class GetStagesPaginator(_GetStagesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/paginator/GetStages.html#ApiGatewayV2.Paginator.GetStages)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/#getstagespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetStagesRequestPaginateTypeDef]
    ) -> PageIterator[GetStagesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2/paginator/GetStages.html#ApiGatewayV2.Paginator.GetStages.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators/#getstagespaginator)
        """
