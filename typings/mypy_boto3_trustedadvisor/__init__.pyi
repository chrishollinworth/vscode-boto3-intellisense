"""
Main interface for trustedadvisor service.

Usage::

    ```python
    import boto3
    from mypy_boto3_trustedadvisor import (
        Client,
        ListChecksPaginator,
        ListOrganizationRecommendationAccountsPaginator,
        ListOrganizationRecommendationResourcesPaginator,
        ListOrganizationRecommendationsPaginator,
        ListRecommendationResourcesPaginator,
        ListRecommendationsPaginator,
        TrustedAdvisorPublicAPIClient,
    )

    session = boto3.Session()

    client: TrustedAdvisorPublicAPIClient = boto3.client("trustedadvisor")
    session_client: TrustedAdvisorPublicAPIClient = session.client("trustedadvisor")

    list_checks_paginator: ListChecksPaginator = client.get_paginator("list_checks")
    list_organization_recommendation_accounts_paginator: ListOrganizationRecommendationAccountsPaginator = client.get_paginator("list_organization_recommendation_accounts")
    list_organization_recommendation_resources_paginator: ListOrganizationRecommendationResourcesPaginator = client.get_paginator("list_organization_recommendation_resources")
    list_organization_recommendations_paginator: ListOrganizationRecommendationsPaginator = client.get_paginator("list_organization_recommendations")
    list_recommendation_resources_paginator: ListRecommendationResourcesPaginator = client.get_paginator("list_recommendation_resources")
    list_recommendations_paginator: ListRecommendationsPaginator = client.get_paginator("list_recommendations")
    ```
"""

from .client import TrustedAdvisorPublicAPIClient
from .paginator import (
    ListChecksPaginator,
    ListOrganizationRecommendationAccountsPaginator,
    ListOrganizationRecommendationResourcesPaginator,
    ListOrganizationRecommendationsPaginator,
    ListRecommendationResourcesPaginator,
    ListRecommendationsPaginator,
)

Client = TrustedAdvisorPublicAPIClient

__all__ = (
    "Client",
    "ListChecksPaginator",
    "ListOrganizationRecommendationAccountsPaginator",
    "ListOrganizationRecommendationResourcesPaginator",
    "ListOrganizationRecommendationsPaginator",
    "ListRecommendationResourcesPaginator",
    "ListRecommendationsPaginator",
    "TrustedAdvisorPublicAPIClient",
)
