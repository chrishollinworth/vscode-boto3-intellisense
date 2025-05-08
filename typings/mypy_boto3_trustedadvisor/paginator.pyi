"""
Type annotations for trustedadvisor service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_trustedadvisor.client import TrustedAdvisorPublicAPIClient
    from mypy_boto3_trustedadvisor.paginator import (
        ListChecksPaginator,
        ListOrganizationRecommendationAccountsPaginator,
        ListOrganizationRecommendationResourcesPaginator,
        ListOrganizationRecommendationsPaginator,
        ListRecommendationResourcesPaginator,
        ListRecommendationsPaginator,
    )

    session = Session()
    client: TrustedAdvisorPublicAPIClient = session.client("trustedadvisor")

    list_checks_paginator: ListChecksPaginator = client.get_paginator("list_checks")
    list_organization_recommendation_accounts_paginator: ListOrganizationRecommendationAccountsPaginator = client.get_paginator("list_organization_recommendation_accounts")
    list_organization_recommendation_resources_paginator: ListOrganizationRecommendationResourcesPaginator = client.get_paginator("list_organization_recommendation_resources")
    list_organization_recommendations_paginator: ListOrganizationRecommendationsPaginator = client.get_paginator("list_organization_recommendations")
    list_recommendation_resources_paginator: ListRecommendationResourcesPaginator = client.get_paginator("list_recommendation_resources")
    list_recommendations_paginator: ListRecommendationsPaginator = client.get_paginator("list_recommendations")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListChecksRequestPaginateTypeDef,
    ListChecksResponseTypeDef,
    ListOrganizationRecommendationAccountsRequestPaginateTypeDef,
    ListOrganizationRecommendationAccountsResponseTypeDef,
    ListOrganizationRecommendationResourcesRequestPaginateTypeDef,
    ListOrganizationRecommendationResourcesResponseTypeDef,
    ListOrganizationRecommendationsRequestPaginateTypeDef,
    ListOrganizationRecommendationsResponseTypeDef,
    ListRecommendationResourcesRequestPaginateTypeDef,
    ListRecommendationResourcesResponseTypeDef,
    ListRecommendationsRequestPaginateTypeDef,
    ListRecommendationsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListChecksPaginator",
    "ListOrganizationRecommendationAccountsPaginator",
    "ListOrganizationRecommendationResourcesPaginator",
    "ListOrganizationRecommendationsPaginator",
    "ListRecommendationResourcesPaginator",
    "ListRecommendationsPaginator",
)

if TYPE_CHECKING:
    _ListChecksPaginatorBase = Paginator[ListChecksResponseTypeDef]
else:
    _ListChecksPaginatorBase = Paginator  # type: ignore[assignment]

class ListChecksPaginator(_ListChecksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/paginator/ListChecks.html#TrustedAdvisorPublicAPI.Paginator.ListChecks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators/#listcheckspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListChecksRequestPaginateTypeDef]
    ) -> PageIterator[ListChecksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/paginator/ListChecks.html#TrustedAdvisorPublicAPI.Paginator.ListChecks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators/#listcheckspaginator)
        """

if TYPE_CHECKING:
    _ListOrganizationRecommendationAccountsPaginatorBase = Paginator[
        ListOrganizationRecommendationAccountsResponseTypeDef
    ]
else:
    _ListOrganizationRecommendationAccountsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOrganizationRecommendationAccountsPaginator(
    _ListOrganizationRecommendationAccountsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/paginator/ListOrganizationRecommendationAccounts.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendationAccounts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators/#listorganizationrecommendationaccountspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOrganizationRecommendationAccountsRequestPaginateTypeDef]
    ) -> PageIterator[ListOrganizationRecommendationAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/paginator/ListOrganizationRecommendationAccounts.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendationAccounts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators/#listorganizationrecommendationaccountspaginator)
        """

if TYPE_CHECKING:
    _ListOrganizationRecommendationResourcesPaginatorBase = Paginator[
        ListOrganizationRecommendationResourcesResponseTypeDef
    ]
else:
    _ListOrganizationRecommendationResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListOrganizationRecommendationResourcesPaginator(
    _ListOrganizationRecommendationResourcesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/paginator/ListOrganizationRecommendationResources.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendationResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators/#listorganizationrecommendationresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOrganizationRecommendationResourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListOrganizationRecommendationResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/paginator/ListOrganizationRecommendationResources.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendationResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators/#listorganizationrecommendationresourcespaginator)
        """

if TYPE_CHECKING:
    _ListOrganizationRecommendationsPaginatorBase = Paginator[
        ListOrganizationRecommendationsResponseTypeDef
    ]
else:
    _ListOrganizationRecommendationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOrganizationRecommendationsPaginator(_ListOrganizationRecommendationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/paginator/ListOrganizationRecommendations.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators/#listorganizationrecommendationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOrganizationRecommendationsRequestPaginateTypeDef]
    ) -> PageIterator[ListOrganizationRecommendationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/paginator/ListOrganizationRecommendations.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators/#listorganizationrecommendationspaginator)
        """

if TYPE_CHECKING:
    _ListRecommendationResourcesPaginatorBase = Paginator[
        ListRecommendationResourcesResponseTypeDef
    ]
else:
    _ListRecommendationResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRecommendationResourcesPaginator(_ListRecommendationResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/paginator/ListRecommendationResources.html#TrustedAdvisorPublicAPI.Paginator.ListRecommendationResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators/#listrecommendationresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRecommendationResourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListRecommendationResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/paginator/ListRecommendationResources.html#TrustedAdvisorPublicAPI.Paginator.ListRecommendationResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators/#listrecommendationresourcespaginator)
        """

if TYPE_CHECKING:
    _ListRecommendationsPaginatorBase = Paginator[ListRecommendationsResponseTypeDef]
else:
    _ListRecommendationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRecommendationsPaginator(_ListRecommendationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/paginator/ListRecommendations.html#TrustedAdvisorPublicAPI.Paginator.ListRecommendations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators/#listrecommendationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRecommendationsRequestPaginateTypeDef]
    ) -> PageIterator[ListRecommendationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/paginator/ListRecommendations.html#TrustedAdvisorPublicAPI.Paginator.ListRecommendations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators/#listrecommendationspaginator)
        """
