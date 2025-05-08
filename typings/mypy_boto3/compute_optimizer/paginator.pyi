"""
Type annotations for compute-optimizer service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_compute_optimizer.client import ComputeOptimizerClient
    from mypy_boto3_compute_optimizer.paginator import (
        DescribeRecommendationExportJobsPaginator,
        GetEnrollmentStatusesForOrganizationPaginator,
        GetLambdaFunctionRecommendationsPaginator,
        GetRecommendationPreferencesPaginator,
        GetRecommendationSummariesPaginator,
    )

    session = Session()
    client: ComputeOptimizerClient = session.client("compute-optimizer")

    describe_recommendation_export_jobs_paginator: DescribeRecommendationExportJobsPaginator = client.get_paginator("describe_recommendation_export_jobs")
    get_enrollment_statuses_for_organization_paginator: GetEnrollmentStatusesForOrganizationPaginator = client.get_paginator("get_enrollment_statuses_for_organization")
    get_lambda_function_recommendations_paginator: GetLambdaFunctionRecommendationsPaginator = client.get_paginator("get_lambda_function_recommendations")
    get_recommendation_preferences_paginator: GetRecommendationPreferencesPaginator = client.get_paginator("get_recommendation_preferences")
    get_recommendation_summaries_paginator: GetRecommendationSummariesPaginator = client.get_paginator("get_recommendation_summaries")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeRecommendationExportJobsRequestPaginateTypeDef,
    DescribeRecommendationExportJobsResponseTypeDef,
    GetEnrollmentStatusesForOrganizationRequestPaginateTypeDef,
    GetEnrollmentStatusesForOrganizationResponseTypeDef,
    GetLambdaFunctionRecommendationsRequestPaginateTypeDef,
    GetLambdaFunctionRecommendationsResponseTypeDef,
    GetRecommendationPreferencesRequestPaginateTypeDef,
    GetRecommendationPreferencesResponseTypeDef,
    GetRecommendationSummariesRequestPaginateTypeDef,
    GetRecommendationSummariesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeRecommendationExportJobsPaginator",
    "GetEnrollmentStatusesForOrganizationPaginator",
    "GetLambdaFunctionRecommendationsPaginator",
    "GetRecommendationPreferencesPaginator",
    "GetRecommendationSummariesPaginator",
)

if TYPE_CHECKING:
    _DescribeRecommendationExportJobsPaginatorBase = Paginator[
        DescribeRecommendationExportJobsResponseTypeDef
    ]
else:
    _DescribeRecommendationExportJobsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeRecommendationExportJobsPaginator(_DescribeRecommendationExportJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/paginator/DescribeRecommendationExportJobs.html#ComputeOptimizer.Paginator.DescribeRecommendationExportJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators/#describerecommendationexportjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeRecommendationExportJobsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeRecommendationExportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/paginator/DescribeRecommendationExportJobs.html#ComputeOptimizer.Paginator.DescribeRecommendationExportJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators/#describerecommendationexportjobspaginator)
        """

if TYPE_CHECKING:
    _GetEnrollmentStatusesForOrganizationPaginatorBase = Paginator[
        GetEnrollmentStatusesForOrganizationResponseTypeDef
    ]
else:
    _GetEnrollmentStatusesForOrganizationPaginatorBase = Paginator  # type: ignore[assignment]

class GetEnrollmentStatusesForOrganizationPaginator(
    _GetEnrollmentStatusesForOrganizationPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/paginator/GetEnrollmentStatusesForOrganization.html#ComputeOptimizer.Paginator.GetEnrollmentStatusesForOrganization)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators/#getenrollmentstatusesfororganizationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetEnrollmentStatusesForOrganizationRequestPaginateTypeDef]
    ) -> PageIterator[GetEnrollmentStatusesForOrganizationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/paginator/GetEnrollmentStatusesForOrganization.html#ComputeOptimizer.Paginator.GetEnrollmentStatusesForOrganization.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators/#getenrollmentstatusesfororganizationpaginator)
        """

if TYPE_CHECKING:
    _GetLambdaFunctionRecommendationsPaginatorBase = Paginator[
        GetLambdaFunctionRecommendationsResponseTypeDef
    ]
else:
    _GetLambdaFunctionRecommendationsPaginatorBase = Paginator  # type: ignore[assignment]

class GetLambdaFunctionRecommendationsPaginator(_GetLambdaFunctionRecommendationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/paginator/GetLambdaFunctionRecommendations.html#ComputeOptimizer.Paginator.GetLambdaFunctionRecommendations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators/#getlambdafunctionrecommendationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetLambdaFunctionRecommendationsRequestPaginateTypeDef]
    ) -> PageIterator[GetLambdaFunctionRecommendationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/paginator/GetLambdaFunctionRecommendations.html#ComputeOptimizer.Paginator.GetLambdaFunctionRecommendations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators/#getlambdafunctionrecommendationspaginator)
        """

if TYPE_CHECKING:
    _GetRecommendationPreferencesPaginatorBase = Paginator[
        GetRecommendationPreferencesResponseTypeDef
    ]
else:
    _GetRecommendationPreferencesPaginatorBase = Paginator  # type: ignore[assignment]

class GetRecommendationPreferencesPaginator(_GetRecommendationPreferencesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/paginator/GetRecommendationPreferences.html#ComputeOptimizer.Paginator.GetRecommendationPreferences)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators/#getrecommendationpreferencespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetRecommendationPreferencesRequestPaginateTypeDef]
    ) -> PageIterator[GetRecommendationPreferencesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/paginator/GetRecommendationPreferences.html#ComputeOptimizer.Paginator.GetRecommendationPreferences.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators/#getrecommendationpreferencespaginator)
        """

if TYPE_CHECKING:
    _GetRecommendationSummariesPaginatorBase = Paginator[GetRecommendationSummariesResponseTypeDef]
else:
    _GetRecommendationSummariesPaginatorBase = Paginator  # type: ignore[assignment]

class GetRecommendationSummariesPaginator(_GetRecommendationSummariesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/paginator/GetRecommendationSummaries.html#ComputeOptimizer.Paginator.GetRecommendationSummaries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators/#getrecommendationsummariespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetRecommendationSummariesRequestPaginateTypeDef]
    ) -> PageIterator[GetRecommendationSummariesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/paginator/GetRecommendationSummaries.html#ComputeOptimizer.Paginator.GetRecommendationSummaries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators/#getrecommendationsummariespaginator)
        """
