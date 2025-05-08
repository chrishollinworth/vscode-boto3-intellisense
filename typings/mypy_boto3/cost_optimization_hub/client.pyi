"""
Type annotations for cost-optimization-hub service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cost_optimization_hub.client import CostOptimizationHubClient

    session = Session()
    client: CostOptimizationHubClient = session.client("cost-optimization-hub")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListEnrollmentStatusesPaginator,
    ListRecommendationsPaginator,
    ListRecommendationSummariesPaginator,
)
from .type_defs import (
    GetPreferencesResponseTypeDef,
    GetRecommendationRequestTypeDef,
    GetRecommendationResponseTypeDef,
    ListEnrollmentStatusesRequestTypeDef,
    ListEnrollmentStatusesResponseTypeDef,
    ListRecommendationsRequestTypeDef,
    ListRecommendationsResponseTypeDef,
    ListRecommendationSummariesRequestTypeDef,
    ListRecommendationSummariesResponseTypeDef,
    UpdateEnrollmentStatusRequestTypeDef,
    UpdateEnrollmentStatusResponseTypeDef,
    UpdatePreferencesRequestTypeDef,
    UpdatePreferencesResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("CostOptimizationHubClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CostOptimizationHubClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cost-optimization-hub.html#CostOptimizationHub.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CostOptimizationHubClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cost-optimization-hub.html#CostOptimizationHub.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cost-optimization-hub/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cost-optimization-hub/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client/#generate_presigned_url)
        """

    def get_preferences(self) -> GetPreferencesResponseTypeDef:
        """
        Returns a set of preferences for an account in order to add account-specific
        preferences into the service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cost-optimization-hub/client/get_preferences.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client/#get_preferences)
        """

    def get_recommendation(
        self, **kwargs: Unpack[GetRecommendationRequestTypeDef]
    ) -> GetRecommendationResponseTypeDef:
        """
        Returns both the current and recommended resource configuration and the
        estimated cost impact for a recommendation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cost-optimization-hub/client/get_recommendation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client/#get_recommendation)
        """

    def list_enrollment_statuses(
        self, **kwargs: Unpack[ListEnrollmentStatusesRequestTypeDef]
    ) -> ListEnrollmentStatusesResponseTypeDef:
        """
        Retrieves the enrollment status for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cost-optimization-hub/client/list_enrollment_statuses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client/#list_enrollment_statuses)
        """

    def list_recommendation_summaries(
        self, **kwargs: Unpack[ListRecommendationSummariesRequestTypeDef]
    ) -> ListRecommendationSummariesResponseTypeDef:
        """
        Returns a concise representation of savings estimates for resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cost-optimization-hub/client/list_recommendation_summaries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client/#list_recommendation_summaries)
        """

    def list_recommendations(
        self, **kwargs: Unpack[ListRecommendationsRequestTypeDef]
    ) -> ListRecommendationsResponseTypeDef:
        """
        Returns a list of recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cost-optimization-hub/client/list_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client/#list_recommendations)
        """

    def update_enrollment_status(
        self, **kwargs: Unpack[UpdateEnrollmentStatusRequestTypeDef]
    ) -> UpdateEnrollmentStatusResponseTypeDef:
        """
        Updates the enrollment (opt in and opt out) status of an account to the Cost
        Optimization Hub service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cost-optimization-hub/client/update_enrollment_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client/#update_enrollment_status)
        """

    def update_preferences(
        self, **kwargs: Unpack[UpdatePreferencesRequestTypeDef]
    ) -> UpdatePreferencesResponseTypeDef:
        """
        Updates a set of preferences for an account in order to add account-specific
        preferences into the service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cost-optimization-hub/client/update_preferences.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client/#update_preferences)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_enrollment_statuses"]
    ) -> ListEnrollmentStatusesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cost-optimization-hub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_recommendation_summaries"]
    ) -> ListRecommendationSummariesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cost-optimization-hub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_recommendations"]
    ) -> ListRecommendationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cost-optimization-hub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client/#get_paginator)
        """
