"""
Type annotations for compute-optimizer service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_compute_optimizer import ComputeOptimizerClient
    from mypy_boto3_compute_optimizer.paginator import (
        DescribeRecommendationExportJobsPaginator,
        GetEnrollmentStatusesForOrganizationPaginator,
        GetLambdaFunctionRecommendationsPaginator,
        GetRecommendationPreferencesPaginator,
        GetRecommendationSummariesPaginator,
    )

    client: ComputeOptimizerClient = boto3.client("compute-optimizer")

    describe_recommendation_export_jobs_paginator: DescribeRecommendationExportJobsPaginator = client.get_paginator("describe_recommendation_export_jobs")
    get_enrollment_statuses_for_organization_paginator: GetEnrollmentStatusesForOrganizationPaginator = client.get_paginator("get_enrollment_statuses_for_organization")
    get_lambda_function_recommendations_paginator: GetLambdaFunctionRecommendationsPaginator = client.get_paginator("get_lambda_function_recommendations")
    get_recommendation_preferences_paginator: GetRecommendationPreferencesPaginator = client.get_paginator("get_recommendation_preferences")
    get_recommendation_summaries_paginator: GetRecommendationSummariesPaginator = client.get_paginator("get_recommendation_summaries")
    ```
"""

from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ResourceTypeType
from .type_defs import (
    DescribeRecommendationExportJobsResponseTypeDef,
    EnrollmentFilterTypeDef,
    GetEnrollmentStatusesForOrganizationResponseTypeDef,
    GetLambdaFunctionRecommendationsResponseTypeDef,
    GetRecommendationPreferencesResponseTypeDef,
    GetRecommendationSummariesResponseTypeDef,
    JobFilterTypeDef,
    LambdaFunctionRecommendationFilterTypeDef,
    PaginatorConfigTypeDef,
    ScopeTypeDef,
)

__all__ = (
    "DescribeRecommendationExportJobsPaginator",
    "GetEnrollmentStatusesForOrganizationPaginator",
    "GetLambdaFunctionRecommendationsPaginator",
    "GetRecommendationPreferencesPaginator",
    "GetRecommendationSummariesPaginator",
)

class DescribeRecommendationExportJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/compute-optimizer.html#ComputeOptimizer.Paginator.DescribeRecommendationExportJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators.html#describerecommendationexportjobspaginator)
    """

    def paginate(
        self,
        *,
        jobIds: List[str] = None,
        filters: List["JobFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeRecommendationExportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/compute-optimizer.html#ComputeOptimizer.Paginator.DescribeRecommendationExportJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators.html#describerecommendationexportjobspaginator)
        """

class GetEnrollmentStatusesForOrganizationPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/compute-optimizer.html#ComputeOptimizer.Paginator.GetEnrollmentStatusesForOrganization)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators.html#getenrollmentstatusesfororganizationpaginator)
    """

    def paginate(
        self,
        *,
        filters: List["EnrollmentFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetEnrollmentStatusesForOrganizationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/compute-optimizer.html#ComputeOptimizer.Paginator.GetEnrollmentStatusesForOrganization.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators.html#getenrollmentstatusesfororganizationpaginator)
        """

class GetLambdaFunctionRecommendationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/compute-optimizer.html#ComputeOptimizer.Paginator.GetLambdaFunctionRecommendations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators.html#getlambdafunctionrecommendationspaginator)
    """

    def paginate(
        self,
        *,
        functionArns: List[str] = None,
        accountIds: List[str] = None,
        filters: List["LambdaFunctionRecommendationFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetLambdaFunctionRecommendationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/compute-optimizer.html#ComputeOptimizer.Paginator.GetLambdaFunctionRecommendations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators.html#getlambdafunctionrecommendationspaginator)
        """

class GetRecommendationPreferencesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/compute-optimizer.html#ComputeOptimizer.Paginator.GetRecommendationPreferences)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators.html#getrecommendationpreferencespaginator)
    """

    def paginate(
        self,
        *,
        resourceType: ResourceTypeType,
        scope: "ScopeTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetRecommendationPreferencesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/compute-optimizer.html#ComputeOptimizer.Paginator.GetRecommendationPreferences.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators.html#getrecommendationpreferencespaginator)
        """

class GetRecommendationSummariesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/compute-optimizer.html#ComputeOptimizer.Paginator.GetRecommendationSummaries)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators.html#getrecommendationsummariespaginator)
    """

    def paginate(
        self, *, accountIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetRecommendationSummariesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/compute-optimizer.html#ComputeOptimizer.Paginator.GetRecommendationSummaries.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/paginators.html#getrecommendationsummariespaginator)
        """
