"""
Type annotations for resiliencehub service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_resiliencehub.client import ResilienceHubClient
    from mypy_boto3_resiliencehub.paginator import (
        ListAppAssessmentResourceDriftsPaginator,
        ListMetricsPaginator,
        ListResourceGroupingRecommendationsPaginator,
    )

    session = Session()
    client: ResilienceHubClient = session.client("resiliencehub")

    list_app_assessment_resource_drifts_paginator: ListAppAssessmentResourceDriftsPaginator = client.get_paginator("list_app_assessment_resource_drifts")
    list_metrics_paginator: ListMetricsPaginator = client.get_paginator("list_metrics")
    list_resource_grouping_recommendations_paginator: ListResourceGroupingRecommendationsPaginator = client.get_paginator("list_resource_grouping_recommendations")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAppAssessmentResourceDriftsRequestPaginateTypeDef,
    ListAppAssessmentResourceDriftsResponseTypeDef,
    ListMetricsRequestPaginateTypeDef,
    ListMetricsResponseTypeDef,
    ListResourceGroupingRecommendationsRequestPaginateTypeDef,
    ListResourceGroupingRecommendationsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAppAssessmentResourceDriftsPaginator",
    "ListMetricsPaginator",
    "ListResourceGroupingRecommendationsPaginator",
)

if TYPE_CHECKING:
    _ListAppAssessmentResourceDriftsPaginatorBase = Paginator[
        ListAppAssessmentResourceDriftsResponseTypeDef
    ]
else:
    _ListAppAssessmentResourceDriftsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAppAssessmentResourceDriftsPaginator(_ListAppAssessmentResourceDriftsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/paginator/ListAppAssessmentResourceDrifts.html#ResilienceHub.Paginator.ListAppAssessmentResourceDrifts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/paginators/#listappassessmentresourcedriftspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAppAssessmentResourceDriftsRequestPaginateTypeDef]
    ) -> PageIterator[ListAppAssessmentResourceDriftsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/paginator/ListAppAssessmentResourceDrifts.html#ResilienceHub.Paginator.ListAppAssessmentResourceDrifts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/paginators/#listappassessmentresourcedriftspaginator)
        """

if TYPE_CHECKING:
    _ListMetricsPaginatorBase = Paginator[ListMetricsResponseTypeDef]
else:
    _ListMetricsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMetricsPaginator(_ListMetricsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/paginator/ListMetrics.html#ResilienceHub.Paginator.ListMetrics)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/paginators/#listmetricspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMetricsRequestPaginateTypeDef]
    ) -> PageIterator[ListMetricsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/paginator/ListMetrics.html#ResilienceHub.Paginator.ListMetrics.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/paginators/#listmetricspaginator)
        """

if TYPE_CHECKING:
    _ListResourceGroupingRecommendationsPaginatorBase = Paginator[
        ListResourceGroupingRecommendationsResponseTypeDef
    ]
else:
    _ListResourceGroupingRecommendationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceGroupingRecommendationsPaginator(
    _ListResourceGroupingRecommendationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/paginator/ListResourceGroupingRecommendations.html#ResilienceHub.Paginator.ListResourceGroupingRecommendations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/paginators/#listresourcegroupingrecommendationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceGroupingRecommendationsRequestPaginateTypeDef]
    ) -> PageIterator[ListResourceGroupingRecommendationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/paginator/ListResourceGroupingRecommendations.html#ResilienceHub.Paginator.ListResourceGroupingRecommendations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/paginators/#listresourcegroupingrecommendationspaginator)
        """
