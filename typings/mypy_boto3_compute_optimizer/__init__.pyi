"""
Main interface for compute-optimizer service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_compute_optimizer import (
        Client,
        ComputeOptimizerClient,
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

from .client import ComputeOptimizerClient
from .paginator import (
    DescribeRecommendationExportJobsPaginator,
    GetEnrollmentStatusesForOrganizationPaginator,
    GetLambdaFunctionRecommendationsPaginator,
    GetRecommendationPreferencesPaginator,
    GetRecommendationSummariesPaginator,
)

Client = ComputeOptimizerClient

__all__ = (
    "Client",
    "ComputeOptimizerClient",
    "DescribeRecommendationExportJobsPaginator",
    "GetEnrollmentStatusesForOrganizationPaginator",
    "GetLambdaFunctionRecommendationsPaginator",
    "GetRecommendationPreferencesPaginator",
    "GetRecommendationSummariesPaginator",
)
