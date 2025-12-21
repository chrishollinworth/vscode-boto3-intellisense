"""
Main interface for bcm-recommended-actions service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_recommended_actions/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_bcm_recommended_actions import (
        BillingandCostManagementRecommendedActionsClient,
        Client,
        ListRecommendedActionsPaginator,
    )

    session = Session()
    client: BillingandCostManagementRecommendedActionsClient = session.client("bcm-recommended-actions")

    list_recommended_actions_paginator: ListRecommendedActionsPaginator = client.get_paginator("list_recommended_actions")
    ```
"""

from .client import BillingandCostManagementRecommendedActionsClient
from .paginator import ListRecommendedActionsPaginator

Client = BillingandCostManagementRecommendedActionsClient

__all__ = (
    "BillingandCostManagementRecommendedActionsClient",
    "Client",
    "ListRecommendedActionsPaginator",
)
