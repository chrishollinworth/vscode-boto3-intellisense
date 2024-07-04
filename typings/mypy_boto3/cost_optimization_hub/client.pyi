"""
Type annotations for cost-optimization-hub service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cost_optimization_hub import CostOptimizationHubClient

    client: CostOptimizationHubClient = boto3.client("cost-optimization-hub")
    ```
"""

import sys
from typing import Any, Dict, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    EnrollmentStatusType,
    MemberAccountDiscountVisibilityType,
    SavingsEstimationModeType,
)
from .paginator import (
    ListEnrollmentStatusesPaginator,
    ListRecommendationsPaginator,
    ListRecommendationSummariesPaginator,
)
from .type_defs import (
    FilterTypeDef,
    GetPreferencesResponseTypeDef,
    GetRecommendationResponseTypeDef,
    ListEnrollmentStatusesResponseTypeDef,
    ListRecommendationsResponseTypeDef,
    ListRecommendationSummariesResponseTypeDef,
    OrderByTypeDef,
    UpdateEnrollmentStatusResponseTypeDef,
    UpdatePreferencesResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CostOptimizationHubClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CostOptimizationHubClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cost-optimization-hub.html#CostOptimizationHub.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CostOptimizationHubClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cost-optimization-hub.html#CostOptimizationHub.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cost-optimization-hub.html#CostOptimizationHub.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client.html#close)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cost-optimization-hub.html#CostOptimizationHub.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client.html#generate_presigned_url)
        """

    def get_preferences(self) -> GetPreferencesResponseTypeDef:
        """
        Returns a set of preferences for an account in order to add account-specific
        preferences into the service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cost-optimization-hub.html#CostOptimizationHub.Client.get_preferences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client.html#get_preferences)
        """

    def get_recommendation(self, *, recommendationId: str) -> GetRecommendationResponseTypeDef:
        """
        Returns both the current and recommended resource configuration and the
        estimated cost impact for a recommendation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cost-optimization-hub.html#CostOptimizationHub.Client.get_recommendation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client.html#get_recommendation)
        """

    def list_enrollment_statuses(
        self,
        *,
        includeOrganizationInfo: bool = None,
        accountId: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListEnrollmentStatusesResponseTypeDef:
        """
        Retrieves the enrollment status for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cost-optimization-hub.html#CostOptimizationHub.Client.list_enrollment_statuses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client.html#list_enrollment_statuses)
        """

    def list_recommendation_summaries(
        self,
        *,
        groupBy: str,
        filter: "FilterTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListRecommendationSummariesResponseTypeDef:
        """
        Returns a concise representation of savings estimates for resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cost-optimization-hub.html#CostOptimizationHub.Client.list_recommendation_summaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client.html#list_recommendation_summaries)
        """

    def list_recommendations(
        self,
        *,
        filter: "FilterTypeDef" = None,
        orderBy: "OrderByTypeDef" = None,
        includeAllRecommendations: bool = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListRecommendationsResponseTypeDef:
        """
        Returns a list of recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cost-optimization-hub.html#CostOptimizationHub.Client.list_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client.html#list_recommendations)
        """

    def update_enrollment_status(
        self, *, status: EnrollmentStatusType, includeMemberAccounts: bool = None
    ) -> UpdateEnrollmentStatusResponseTypeDef:
        """
        Updates the enrollment (opt in and opt out) status of an account to the Cost
        Optimization Hub service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cost-optimization-hub.html#CostOptimizationHub.Client.update_enrollment_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client.html#update_enrollment_status)
        """

    def update_preferences(
        self,
        *,
        savingsEstimationMode: SavingsEstimationModeType = None,
        memberAccountDiscountVisibility: MemberAccountDiscountVisibilityType = None
    ) -> UpdatePreferencesResponseTypeDef:
        """
        Updates a set of preferences for an account in order to add account-specific
        preferences into the service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cost-optimization-hub.html#CostOptimizationHub.Client.update_preferences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/client.html#update_preferences)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_enrollment_statuses"]
    ) -> ListEnrollmentStatusesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cost-optimization-hub.html#CostOptimizationHub.Paginator.ListEnrollmentStatuses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/paginators.html#listenrollmentstatusespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_recommendation_summaries"]
    ) -> ListRecommendationSummariesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cost-optimization-hub.html#CostOptimizationHub.Paginator.ListRecommendationSummaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/paginators.html#listrecommendationsummariespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_recommendations"]
    ) -> ListRecommendationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cost-optimization-hub.html#CostOptimizationHub.Paginator.ListRecommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/paginators.html#listrecommendationspaginator)
        """
