"""
Type annotations for ce service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ce.client import CostExplorerClient

    session = Session()
    client: CostExplorerClient = session.client("ce")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    GetAnomaliesPaginator,
    GetAnomalyMonitorsPaginator,
    GetAnomalySubscriptionsPaginator,
)
from .type_defs import (
    CreateAnomalyMonitorRequestTypeDef,
    CreateAnomalyMonitorResponseTypeDef,
    CreateAnomalySubscriptionRequestTypeDef,
    CreateAnomalySubscriptionResponseTypeDef,
    CreateCostCategoryDefinitionRequestTypeDef,
    CreateCostCategoryDefinitionResponseTypeDef,
    DeleteAnomalyMonitorRequestTypeDef,
    DeleteAnomalySubscriptionRequestTypeDef,
    DeleteCostCategoryDefinitionRequestTypeDef,
    DeleteCostCategoryDefinitionResponseTypeDef,
    DescribeCostCategoryDefinitionRequestTypeDef,
    DescribeCostCategoryDefinitionResponseTypeDef,
    GetAnomaliesRequestTypeDef,
    GetAnomaliesResponseTypeDef,
    GetAnomalyMonitorsRequestTypeDef,
    GetAnomalyMonitorsResponseTypeDef,
    GetAnomalySubscriptionsRequestTypeDef,
    GetAnomalySubscriptionsResponseTypeDef,
    GetApproximateUsageRecordsRequestTypeDef,
    GetApproximateUsageRecordsResponseTypeDef,
    GetCommitmentPurchaseAnalysisRequestTypeDef,
    GetCommitmentPurchaseAnalysisResponseTypeDef,
    GetCostAndUsageRequestTypeDef,
    GetCostAndUsageResponseTypeDef,
    GetCostAndUsageWithResourcesRequestTypeDef,
    GetCostAndUsageWithResourcesResponseTypeDef,
    GetCostCategoriesRequestTypeDef,
    GetCostCategoriesResponseTypeDef,
    GetCostForecastRequestTypeDef,
    GetCostForecastResponseTypeDef,
    GetDimensionValuesRequestTypeDef,
    GetDimensionValuesResponseTypeDef,
    GetReservationCoverageRequestTypeDef,
    GetReservationCoverageResponseTypeDef,
    GetReservationPurchaseRecommendationRequestTypeDef,
    GetReservationPurchaseRecommendationResponseTypeDef,
    GetReservationUtilizationRequestTypeDef,
    GetReservationUtilizationResponseTypeDef,
    GetRightsizingRecommendationRequestTypeDef,
    GetRightsizingRecommendationResponseTypeDef,
    GetSavingsPlanPurchaseRecommendationDetailsRequestTypeDef,
    GetSavingsPlanPurchaseRecommendationDetailsResponseTypeDef,
    GetSavingsPlansCoverageRequestTypeDef,
    GetSavingsPlansCoverageResponseTypeDef,
    GetSavingsPlansPurchaseRecommendationRequestTypeDef,
    GetSavingsPlansPurchaseRecommendationResponseTypeDef,
    GetSavingsPlansUtilizationDetailsRequestTypeDef,
    GetSavingsPlansUtilizationDetailsResponseTypeDef,
    GetSavingsPlansUtilizationRequestTypeDef,
    GetSavingsPlansUtilizationResponseTypeDef,
    GetTagsRequestTypeDef,
    GetTagsResponseTypeDef,
    GetUsageForecastRequestTypeDef,
    GetUsageForecastResponseTypeDef,
    ListCommitmentPurchaseAnalysesRequestTypeDef,
    ListCommitmentPurchaseAnalysesResponseTypeDef,
    ListCostAllocationTagBackfillHistoryRequestTypeDef,
    ListCostAllocationTagBackfillHistoryResponseTypeDef,
    ListCostAllocationTagsRequestTypeDef,
    ListCostAllocationTagsResponseTypeDef,
    ListCostCategoryDefinitionsRequestTypeDef,
    ListCostCategoryDefinitionsResponseTypeDef,
    ListSavingsPlansPurchaseRecommendationGenerationRequestTypeDef,
    ListSavingsPlansPurchaseRecommendationGenerationResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ProvideAnomalyFeedbackRequestTypeDef,
    ProvideAnomalyFeedbackResponseTypeDef,
    StartCommitmentPurchaseAnalysisRequestTypeDef,
    StartCommitmentPurchaseAnalysisResponseTypeDef,
    StartCostAllocationTagBackfillRequestTypeDef,
    StartCostAllocationTagBackfillResponseTypeDef,
    StartSavingsPlansPurchaseRecommendationGenerationResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAnomalyMonitorRequestTypeDef,
    UpdateAnomalyMonitorResponseTypeDef,
    UpdateAnomalySubscriptionRequestTypeDef,
    UpdateAnomalySubscriptionResponseTypeDef,
    UpdateCostAllocationTagsStatusRequestTypeDef,
    UpdateCostAllocationTagsStatusResponseTypeDef,
    UpdateCostCategoryDefinitionRequestTypeDef,
    UpdateCostCategoryDefinitionResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("CostExplorerClient",)

class Exceptions(BaseClientExceptions):
    AnalysisNotFoundException: Type[BotocoreClientError]
    BackfillLimitExceededException: Type[BotocoreClientError]
    BillExpirationException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DataUnavailableException: Type[BotocoreClientError]
    GenerationExistsException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    RequestChangedException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    UnknownMonitorException: Type[BotocoreClientError]
    UnknownSubscriptionException: Type[BotocoreClientError]
    UnresolvableUsageUnitException: Type[BotocoreClientError]

class CostExplorerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CostExplorerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#generate_presigned_url)
        """

    def create_anomaly_monitor(
        self, **kwargs: Unpack[CreateAnomalyMonitorRequestTypeDef]
    ) -> CreateAnomalyMonitorResponseTypeDef:
        """
        Creates a new cost anomaly detection monitor with the requested type and
        monitor specification.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/create_anomaly_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#create_anomaly_monitor)
        """

    def create_anomaly_subscription(
        self, **kwargs: Unpack[CreateAnomalySubscriptionRequestTypeDef]
    ) -> CreateAnomalySubscriptionResponseTypeDef:
        """
        Adds an alert subscription to a cost anomaly detection monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/create_anomaly_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#create_anomaly_subscription)
        """

    def create_cost_category_definition(
        self, **kwargs: Unpack[CreateCostCategoryDefinitionRequestTypeDef]
    ) -> CreateCostCategoryDefinitionResponseTypeDef:
        """
        Creates a new Cost Category with the requested name and rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/create_cost_category_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#create_cost_category_definition)
        """

    def delete_anomaly_monitor(
        self, **kwargs: Unpack[DeleteAnomalyMonitorRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a cost anomaly monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/delete_anomaly_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#delete_anomaly_monitor)
        """

    def delete_anomaly_subscription(
        self, **kwargs: Unpack[DeleteAnomalySubscriptionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a cost anomaly subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/delete_anomaly_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#delete_anomaly_subscription)
        """

    def delete_cost_category_definition(
        self, **kwargs: Unpack[DeleteCostCategoryDefinitionRequestTypeDef]
    ) -> DeleteCostCategoryDefinitionResponseTypeDef:
        """
        Deletes a Cost Category.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/delete_cost_category_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#delete_cost_category_definition)
        """

    def describe_cost_category_definition(
        self, **kwargs: Unpack[DescribeCostCategoryDefinitionRequestTypeDef]
    ) -> DescribeCostCategoryDefinitionResponseTypeDef:
        """
        Returns the name, Amazon Resource Name (ARN), rules, definition, and effective
        dates of a Cost Category that's defined in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/describe_cost_category_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#describe_cost_category_definition)
        """

    def get_anomalies(
        self, **kwargs: Unpack[GetAnomaliesRequestTypeDef]
    ) -> GetAnomaliesResponseTypeDef:
        """
        Retrieves all of the cost anomalies detected on your account during the time
        period that's specified by the <code>DateInterval</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_anomalies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_anomalies)
        """

    def get_anomaly_monitors(
        self, **kwargs: Unpack[GetAnomalyMonitorsRequestTypeDef]
    ) -> GetAnomalyMonitorsResponseTypeDef:
        """
        Retrieves the cost anomaly monitor definitions for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_anomaly_monitors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_anomaly_monitors)
        """

    def get_anomaly_subscriptions(
        self, **kwargs: Unpack[GetAnomalySubscriptionsRequestTypeDef]
    ) -> GetAnomalySubscriptionsResponseTypeDef:
        """
        Retrieves the cost anomaly subscription objects for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_anomaly_subscriptions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_anomaly_subscriptions)
        """

    def get_approximate_usage_records(
        self, **kwargs: Unpack[GetApproximateUsageRecordsRequestTypeDef]
    ) -> GetApproximateUsageRecordsResponseTypeDef:
        """
        Retrieves estimated usage records for hourly granularity or resource-level data
        at daily granularity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_approximate_usage_records.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_approximate_usage_records)
        """

    def get_commitment_purchase_analysis(
        self, **kwargs: Unpack[GetCommitmentPurchaseAnalysisRequestTypeDef]
    ) -> GetCommitmentPurchaseAnalysisResponseTypeDef:
        """
        Retrieves a commitment purchase analysis result based on the
        <code>AnalysisId</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_commitment_purchase_analysis.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_commitment_purchase_analysis)
        """

    def get_cost_and_usage(
        self, **kwargs: Unpack[GetCostAndUsageRequestTypeDef]
    ) -> GetCostAndUsageResponseTypeDef:
        """
        Retrieves cost and usage metrics for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_cost_and_usage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_cost_and_usage)
        """

    def get_cost_and_usage_with_resources(
        self, **kwargs: Unpack[GetCostAndUsageWithResourcesRequestTypeDef]
    ) -> GetCostAndUsageWithResourcesResponseTypeDef:
        """
        Retrieves cost and usage metrics with resources for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_cost_and_usage_with_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_cost_and_usage_with_resources)
        """

    def get_cost_categories(
        self, **kwargs: Unpack[GetCostCategoriesRequestTypeDef]
    ) -> GetCostCategoriesResponseTypeDef:
        """
        Retrieves an array of Cost Category names and values incurred cost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_cost_categories.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_cost_categories)
        """

    def get_cost_forecast(
        self, **kwargs: Unpack[GetCostForecastRequestTypeDef]
    ) -> GetCostForecastResponseTypeDef:
        """
        Retrieves a forecast for how much Amazon Web Services predicts that you will
        spend over the forecast time period that you select, based on your past costs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_cost_forecast.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_cost_forecast)
        """

    def get_dimension_values(
        self, **kwargs: Unpack[GetDimensionValuesRequestTypeDef]
    ) -> GetDimensionValuesResponseTypeDef:
        """
        Retrieves all available filter values for a specified filter over a period of
        time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_dimension_values.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_dimension_values)
        """

    def get_reservation_coverage(
        self, **kwargs: Unpack[GetReservationCoverageRequestTypeDef]
    ) -> GetReservationCoverageResponseTypeDef:
        """
        Retrieves the reservation coverage for your account, which you can use to see
        how much of your Amazon Elastic Compute Cloud, Amazon ElastiCache, Amazon
        Relational Database Service, or Amazon Redshift usage is covered by a
        reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_reservation_coverage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_reservation_coverage)
        """

    def get_reservation_purchase_recommendation(
        self, **kwargs: Unpack[GetReservationPurchaseRecommendationRequestTypeDef]
    ) -> GetReservationPurchaseRecommendationResponseTypeDef:
        """
        Gets recommendations for reservation purchases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_reservation_purchase_recommendation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_reservation_purchase_recommendation)
        """

    def get_reservation_utilization(
        self, **kwargs: Unpack[GetReservationUtilizationRequestTypeDef]
    ) -> GetReservationUtilizationResponseTypeDef:
        """
        Retrieves the reservation utilization for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_reservation_utilization.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_reservation_utilization)
        """

    def get_rightsizing_recommendation(
        self, **kwargs: Unpack[GetRightsizingRecommendationRequestTypeDef]
    ) -> GetRightsizingRecommendationResponseTypeDef:
        """
        Creates recommendations that help you save cost by identifying idle and
        underutilized Amazon EC2 instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_rightsizing_recommendation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_rightsizing_recommendation)
        """

    def get_savings_plan_purchase_recommendation_details(
        self, **kwargs: Unpack[GetSavingsPlanPurchaseRecommendationDetailsRequestTypeDef]
    ) -> GetSavingsPlanPurchaseRecommendationDetailsResponseTypeDef:
        """
        Retrieves the details for a Savings Plan recommendation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_savings_plan_purchase_recommendation_details.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_savings_plan_purchase_recommendation_details)
        """

    def get_savings_plans_coverage(
        self, **kwargs: Unpack[GetSavingsPlansCoverageRequestTypeDef]
    ) -> GetSavingsPlansCoverageResponseTypeDef:
        """
        Retrieves the Savings Plans covered for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_savings_plans_coverage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_savings_plans_coverage)
        """

    def get_savings_plans_purchase_recommendation(
        self, **kwargs: Unpack[GetSavingsPlansPurchaseRecommendationRequestTypeDef]
    ) -> GetSavingsPlansPurchaseRecommendationResponseTypeDef:
        """
        Retrieves the Savings Plans recommendations for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_savings_plans_purchase_recommendation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_savings_plans_purchase_recommendation)
        """

    def get_savings_plans_utilization(
        self, **kwargs: Unpack[GetSavingsPlansUtilizationRequestTypeDef]
    ) -> GetSavingsPlansUtilizationResponseTypeDef:
        """
        Retrieves the Savings Plans utilization for your account across date ranges
        with daily or monthly granularity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_savings_plans_utilization.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_savings_plans_utilization)
        """

    def get_savings_plans_utilization_details(
        self, **kwargs: Unpack[GetSavingsPlansUtilizationDetailsRequestTypeDef]
    ) -> GetSavingsPlansUtilizationDetailsResponseTypeDef:
        """
        Retrieves attribute data along with aggregate utilization and savings data for
        a given time period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_savings_plans_utilization_details.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_savings_plans_utilization_details)
        """

    def get_tags(self, **kwargs: Unpack[GetTagsRequestTypeDef]) -> GetTagsResponseTypeDef:
        """
        Queries for available tag keys and tag values for a specified period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_tags)
        """

    def get_usage_forecast(
        self, **kwargs: Unpack[GetUsageForecastRequestTypeDef]
    ) -> GetUsageForecastResponseTypeDef:
        """
        Retrieves a forecast for how much Amazon Web Services predicts that you will
        use over the forecast time period that you select, based on your past usage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_usage_forecast.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_usage_forecast)
        """

    def list_commitment_purchase_analyses(
        self, **kwargs: Unpack[ListCommitmentPurchaseAnalysesRequestTypeDef]
    ) -> ListCommitmentPurchaseAnalysesResponseTypeDef:
        """
        Lists the commitment purchase analyses for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/list_commitment_purchase_analyses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#list_commitment_purchase_analyses)
        """

    def list_cost_allocation_tag_backfill_history(
        self, **kwargs: Unpack[ListCostAllocationTagBackfillHistoryRequestTypeDef]
    ) -> ListCostAllocationTagBackfillHistoryResponseTypeDef:
        """
        Retrieves a list of your historical cost allocation tag backfill requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/list_cost_allocation_tag_backfill_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#list_cost_allocation_tag_backfill_history)
        """

    def list_cost_allocation_tags(
        self, **kwargs: Unpack[ListCostAllocationTagsRequestTypeDef]
    ) -> ListCostAllocationTagsResponseTypeDef:
        """
        Get a list of cost allocation tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/list_cost_allocation_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#list_cost_allocation_tags)
        """

    def list_cost_category_definitions(
        self, **kwargs: Unpack[ListCostCategoryDefinitionsRequestTypeDef]
    ) -> ListCostCategoryDefinitionsResponseTypeDef:
        """
        Returns the name, Amazon Resource Name (ARN), <code>NumberOfRules</code> and
        effective dates of all Cost Categories defined in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/list_cost_category_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#list_cost_category_definitions)
        """

    def list_savings_plans_purchase_recommendation_generation(
        self, **kwargs: Unpack[ListSavingsPlansPurchaseRecommendationGenerationRequestTypeDef]
    ) -> ListSavingsPlansPurchaseRecommendationGenerationResponseTypeDef:
        """
        Retrieves a list of your historical recommendation generations within the past
        30 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/list_savings_plans_purchase_recommendation_generation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#list_savings_plans_purchase_recommendation_generation)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of resource tags associated with the resource specified by the
        Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#list_tags_for_resource)
        """

    def provide_anomaly_feedback(
        self, **kwargs: Unpack[ProvideAnomalyFeedbackRequestTypeDef]
    ) -> ProvideAnomalyFeedbackResponseTypeDef:
        """
        Modifies the feedback property of a given cost anomaly.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/provide_anomaly_feedback.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#provide_anomaly_feedback)
        """

    def start_commitment_purchase_analysis(
        self, **kwargs: Unpack[StartCommitmentPurchaseAnalysisRequestTypeDef]
    ) -> StartCommitmentPurchaseAnalysisResponseTypeDef:
        """
        Specifies the parameters of a planned commitment purchase and starts the
        generation of the analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/start_commitment_purchase_analysis.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#start_commitment_purchase_analysis)
        """

    def start_cost_allocation_tag_backfill(
        self, **kwargs: Unpack[StartCostAllocationTagBackfillRequestTypeDef]
    ) -> StartCostAllocationTagBackfillResponseTypeDef:
        """
        Request a cost allocation tag backfill.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/start_cost_allocation_tag_backfill.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#start_cost_allocation_tag_backfill)
        """

    def start_savings_plans_purchase_recommendation_generation(
        self,
    ) -> StartSavingsPlansPurchaseRecommendationGenerationResponseTypeDef:
        """
        Requests a Savings Plans recommendation generation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/start_savings_plans_purchase_recommendation_generation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#start_savings_plans_purchase_recommendation_generation)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        An API operation for adding one or more tags (key-value pairs) to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#untag_resource)
        """

    def update_anomaly_monitor(
        self, **kwargs: Unpack[UpdateAnomalyMonitorRequestTypeDef]
    ) -> UpdateAnomalyMonitorResponseTypeDef:
        """
        Updates an existing cost anomaly monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/update_anomaly_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#update_anomaly_monitor)
        """

    def update_anomaly_subscription(
        self, **kwargs: Unpack[UpdateAnomalySubscriptionRequestTypeDef]
    ) -> UpdateAnomalySubscriptionResponseTypeDef:
        """
        Updates an existing cost anomaly subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/update_anomaly_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#update_anomaly_subscription)
        """

    def update_cost_allocation_tags_status(
        self, **kwargs: Unpack[UpdateCostAllocationTagsStatusRequestTypeDef]
    ) -> UpdateCostAllocationTagsStatusResponseTypeDef:
        """
        Updates status for cost allocation tags in bulk, with maximum batch size of 20.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/update_cost_allocation_tags_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#update_cost_allocation_tags_status)
        """

    def update_cost_category_definition(
        self, **kwargs: Unpack[UpdateCostCategoryDefinitionRequestTypeDef]
    ) -> UpdateCostCategoryDefinitionResponseTypeDef:
        """
        Updates an existing Cost Category.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/update_cost_category_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#update_cost_category_definition)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_anomalies"]
    ) -> GetAnomaliesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_anomaly_monitors"]
    ) -> GetAnomalyMonitorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_anomaly_subscriptions"]
    ) -> GetAnomalySubscriptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_paginator)
        """
