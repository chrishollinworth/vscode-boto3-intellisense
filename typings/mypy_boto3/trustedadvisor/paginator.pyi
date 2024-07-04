"""
Type annotations for trustedadvisor service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_trustedadvisor import TrustedAdvisorPublicAPIClient
    from mypy_boto3_trustedadvisor.paginator import (
        ListChecksPaginator,
        ListOrganizationRecommendationAccountsPaginator,
        ListOrganizationRecommendationResourcesPaginator,
        ListOrganizationRecommendationsPaginator,
        ListRecommendationResourcesPaginator,
        ListRecommendationsPaginator,
    )

    client: TrustedAdvisorPublicAPIClient = boto3.client("trustedadvisor")

    list_checks_paginator: ListChecksPaginator = client.get_paginator("list_checks")
    list_organization_recommendation_accounts_paginator: ListOrganizationRecommendationAccountsPaginator = client.get_paginator("list_organization_recommendation_accounts")
    list_organization_recommendation_resources_paginator: ListOrganizationRecommendationResourcesPaginator = client.get_paginator("list_organization_recommendation_resources")
    list_organization_recommendations_paginator: ListOrganizationRecommendationsPaginator = client.get_paginator("list_organization_recommendations")
    list_recommendation_resources_paginator: ListRecommendationResourcesPaginator = client.get_paginator("list_recommendation_resources")
    list_recommendations_paginator: ListRecommendationsPaginator = client.get_paginator("list_recommendations")
    ```
"""

from datetime import datetime
from typing import Iterator, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    ExclusionStatusType,
    RecommendationLanguageType,
    RecommendationPillarType,
    RecommendationSourceType,
    RecommendationStatusType,
    RecommendationTypeType,
    ResourceStatusType,
)
from .type_defs import (
    ListChecksResponseTypeDef,
    ListOrganizationRecommendationAccountsResponseTypeDef,
    ListOrganizationRecommendationResourcesResponseTypeDef,
    ListOrganizationRecommendationsResponseTypeDef,
    ListRecommendationResourcesResponseTypeDef,
    ListRecommendationsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListChecksPaginator",
    "ListOrganizationRecommendationAccountsPaginator",
    "ListOrganizationRecommendationResourcesPaginator",
    "ListOrganizationRecommendationsPaginator",
    "ListRecommendationResourcesPaginator",
    "ListRecommendationsPaginator",
)

class ListChecksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListChecks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators.html#listcheckspaginator)
    """

    def paginate(
        self,
        *,
        awsService: str = None,
        language: RecommendationLanguageType = None,
        pillar: RecommendationPillarType = None,
        source: RecommendationSourceType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListChecksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListChecks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators.html#listcheckspaginator)
        """

class ListOrganizationRecommendationAccountsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendationAccounts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators.html#listorganizationrecommendationaccountspaginator)
    """

    def paginate(
        self,
        *,
        organizationRecommendationIdentifier: str,
        affectedAccountId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOrganizationRecommendationAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendationAccounts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators.html#listorganizationrecommendationaccountspaginator)
        """

class ListOrganizationRecommendationResourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendationResources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators.html#listorganizationrecommendationresourcespaginator)
    """

    def paginate(
        self,
        *,
        organizationRecommendationIdentifier: str,
        affectedAccountId: str = None,
        exclusionStatus: ExclusionStatusType = None,
        regionCode: str = None,
        status: ResourceStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOrganizationRecommendationResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendationResources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators.html#listorganizationrecommendationresourcespaginator)
        """

class ListOrganizationRecommendationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators.html#listorganizationrecommendationspaginator)
    """

    def paginate(
        self,
        *,
        afterLastUpdatedAt: Union[datetime, str] = None,
        awsService: str = None,
        beforeLastUpdatedAt: Union[datetime, str] = None,
        checkIdentifier: str = None,
        pillar: RecommendationPillarType = None,
        source: RecommendationSourceType = None,
        status: RecommendationStatusType = None,
        type: RecommendationTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOrganizationRecommendationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators.html#listorganizationrecommendationspaginator)
        """

class ListRecommendationResourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListRecommendationResources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators.html#listrecommendationresourcespaginator)
    """

    def paginate(
        self,
        *,
        recommendationIdentifier: str,
        exclusionStatus: ExclusionStatusType = None,
        regionCode: str = None,
        status: ResourceStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecommendationResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListRecommendationResources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators.html#listrecommendationresourcespaginator)
        """

class ListRecommendationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListRecommendations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators.html#listrecommendationspaginator)
    """

    def paginate(
        self,
        *,
        afterLastUpdatedAt: Union[datetime, str] = None,
        awsService: str = None,
        beforeLastUpdatedAt: Union[datetime, str] = None,
        checkIdentifier: str = None,
        pillar: RecommendationPillarType = None,
        source: RecommendationSourceType = None,
        status: RecommendationStatusType = None,
        type: RecommendationTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecommendationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListRecommendations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators.html#listrecommendationspaginator)
        """
