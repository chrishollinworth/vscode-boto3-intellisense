"""
Type annotations for ce service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ce import CostExplorerClient

    client: CostExplorerClient = boto3.client("ce")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AccountScopeType,
    AnomalyFeedbackTypeType,
    AnomalySubscriptionFrequencyType,
    ContextType,
    CostAllocationTagStatusType,
    CostAllocationTagTypeType,
    DimensionType,
    GenerationStatusType,
    GranularityType,
    LookbackPeriodInDaysType,
    MetricType,
    PaymentOptionType,
    SavingsPlansDataTypeType,
    SupportedSavingsPlansTypeType,
    TermInYearsType,
)
from .type_defs import (
    AnomalyDateIntervalTypeDef,
    AnomalyMonitorTypeDef,
    AnomalySubscriptionTypeDef,
    CostAllocationTagStatusEntryTypeDef,
    CostCategoryRuleTypeDef,
    CostCategorySplitChargeRuleTypeDef,
    CreateAnomalyMonitorResponseTypeDef,
    CreateAnomalySubscriptionResponseTypeDef,
    CreateCostCategoryDefinitionResponseTypeDef,
    DateIntervalTypeDef,
    DeleteCostCategoryDefinitionResponseTypeDef,
    DescribeCostCategoryDefinitionResponseTypeDef,
    ExpressionTypeDef,
    GetAnomaliesResponseTypeDef,
    GetAnomalyMonitorsResponseTypeDef,
    GetAnomalySubscriptionsResponseTypeDef,
    GetCostAndUsageResponseTypeDef,
    GetCostAndUsageWithResourcesResponseTypeDef,
    GetCostCategoriesResponseTypeDef,
    GetCostForecastResponseTypeDef,
    GetDimensionValuesResponseTypeDef,
    GetReservationCoverageResponseTypeDef,
    GetReservationPurchaseRecommendationResponseTypeDef,
    GetReservationUtilizationResponseTypeDef,
    GetRightsizingRecommendationResponseTypeDef,
    GetSavingsPlansCoverageResponseTypeDef,
    GetSavingsPlansPurchaseRecommendationResponseTypeDef,
    GetSavingsPlansUtilizationDetailsResponseTypeDef,
    GetSavingsPlansUtilizationResponseTypeDef,
    GetTagsResponseTypeDef,
    GetUsageForecastResponseTypeDef,
    GroupDefinitionTypeDef,
    ListCostAllocationTagsResponseTypeDef,
    ListCostCategoryDefinitionsResponseTypeDef,
    ListSavingsPlansPurchaseRecommendationGenerationResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ProvideAnomalyFeedbackResponseTypeDef,
    ResourceTagTypeDef,
    RightsizingRecommendationConfigurationTypeDef,
    ServiceSpecificationTypeDef,
    SortDefinitionTypeDef,
    StartSavingsPlansPurchaseRecommendationGenerationResponseTypeDef,
    SubscriberTypeDef,
    TotalImpactFilterTypeDef,
    UpdateAnomalyMonitorResponseTypeDef,
    UpdateAnomalySubscriptionResponseTypeDef,
    UpdateCostAllocationTagsStatusResponseTypeDef,
    UpdateCostCategoryDefinitionResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CostExplorerClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CostExplorerClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#close)
        """
    def create_anomaly_monitor(
        self,
        *,
        AnomalyMonitor: "AnomalyMonitorTypeDef",
        ResourceTags: List["ResourceTagTypeDef"] = None
    ) -> CreateAnomalyMonitorResponseTypeDef:
        """
        Creates a new cost anomaly detection monitor with the requested type and monitor
        specification.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.create_anomaly_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#create_anomaly_monitor)
        """
    def create_anomaly_subscription(
        self,
        *,
        AnomalySubscription: "AnomalySubscriptionTypeDef",
        ResourceTags: List["ResourceTagTypeDef"] = None
    ) -> CreateAnomalySubscriptionResponseTypeDef:
        """
        Adds an alert subscription to a cost anomaly detection monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.create_anomaly_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#create_anomaly_subscription)
        """
    def create_cost_category_definition(
        self,
        *,
        Name: str,
        RuleVersion: Literal["CostCategoryExpression.v1"],
        Rules: List["CostCategoryRuleTypeDef"],
        EffectiveStart: str = None,
        DefaultValue: str = None,
        SplitChargeRules: List["CostCategorySplitChargeRuleTypeDef"] = None,
        ResourceTags: List["ResourceTagTypeDef"] = None
    ) -> CreateCostCategoryDefinitionResponseTypeDef:
        """
        Creates a new Cost Category with the requested name and rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.create_cost_category_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#create_cost_category_definition)
        """
    def delete_anomaly_monitor(self, *, MonitorArn: str) -> Dict[str, Any]:
        """
        Deletes a cost anomaly monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.delete_anomaly_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#delete_anomaly_monitor)
        """
    def delete_anomaly_subscription(self, *, SubscriptionArn: str) -> Dict[str, Any]:
        """
        Deletes a cost anomaly subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.delete_anomaly_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#delete_anomaly_subscription)
        """
    def delete_cost_category_definition(
        self, *, CostCategoryArn: str
    ) -> DeleteCostCategoryDefinitionResponseTypeDef:
        """
        Deletes a Cost Category.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.delete_cost_category_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#delete_cost_category_definition)
        """
    def describe_cost_category_definition(
        self, *, CostCategoryArn: str, EffectiveOn: str = None
    ) -> DescribeCostCategoryDefinitionResponseTypeDef:
        """
        Returns the name, Amazon Resource Name (ARN), rules, definition, and effective
        dates of a Cost Category that's defined in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.describe_cost_category_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#describe_cost_category_definition)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#generate_presigned_url)
        """
    def get_anomalies(
        self,
        *,
        DateInterval: "AnomalyDateIntervalTypeDef",
        MonitorArn: str = None,
        Feedback: AnomalyFeedbackTypeType = None,
        TotalImpact: "TotalImpactFilterTypeDef" = None,
        NextPageToken: str = None,
        MaxResults: int = None
    ) -> GetAnomaliesResponseTypeDef:
        """
        Retrieves all of the cost anomalies detected on your account during the time
        period that's specified by the `DateInterval` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.get_anomalies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#get_anomalies)
        """
    def get_anomaly_monitors(
        self, *, MonitorArnList: List[str] = None, NextPageToken: str = None, MaxResults: int = None
    ) -> GetAnomalyMonitorsResponseTypeDef:
        """
        Retrieves the cost anomaly monitor definitions for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.get_anomaly_monitors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#get_anomaly_monitors)
        """
    def get_anomaly_subscriptions(
        self,
        *,
        SubscriptionArnList: List[str] = None,
        MonitorArn: str = None,
        NextPageToken: str = None,
        MaxResults: int = None
    ) -> GetAnomalySubscriptionsResponseTypeDef:
        """
        Retrieves the cost anomaly subscription objects for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.get_anomaly_subscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#get_anomaly_subscriptions)
        """
    def get_cost_and_usage(
        self,
        *,
        TimePeriod: "DateIntervalTypeDef",
        Granularity: GranularityType,
        Metrics: List[str],
        Filter: "ExpressionTypeDef" = None,
        GroupBy: List["GroupDefinitionTypeDef"] = None,
        NextPageToken: str = None
    ) -> GetCostAndUsageResponseTypeDef:
        """
        Retrieves cost and usage metrics for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.get_cost_and_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#get_cost_and_usage)
        """
    def get_cost_and_usage_with_resources(
        self,
        *,
        TimePeriod: "DateIntervalTypeDef",
        Granularity: GranularityType,
        Filter: "ExpressionTypeDef",
        Metrics: List[str] = None,
        GroupBy: List["GroupDefinitionTypeDef"] = None,
        NextPageToken: str = None
    ) -> GetCostAndUsageWithResourcesResponseTypeDef:
        """
        Retrieves cost and usage metrics with resources for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.get_cost_and_usage_with_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#get_cost_and_usage_with_resources)
        """
    def get_cost_categories(
        self,
        *,
        TimePeriod: "DateIntervalTypeDef",
        SearchString: str = None,
        CostCategoryName: str = None,
        Filter: "ExpressionTypeDef" = None,
        SortBy: List["SortDefinitionTypeDef"] = None,
        MaxResults: int = None,
        NextPageToken: str = None
    ) -> GetCostCategoriesResponseTypeDef:
        """
        Retrieves an array of Cost Category names and values incurred cost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.get_cost_categories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#get_cost_categories)
        """
    def get_cost_forecast(
        self,
        *,
        TimePeriod: "DateIntervalTypeDef",
        Metric: MetricType,
        Granularity: GranularityType,
        Filter: "ExpressionTypeDef" = None,
        PredictionIntervalLevel: int = None
    ) -> GetCostForecastResponseTypeDef:
        """
        Retrieves a forecast for how much Amazon Web Services predicts that you will
        spend over the forecast time period that you select, based on your past costs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.get_cost_forecast)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#get_cost_forecast)
        """
    def get_dimension_values(
        self,
        *,
        TimePeriod: "DateIntervalTypeDef",
        Dimension: DimensionType,
        SearchString: str = None,
        Context: ContextType = None,
        Filter: "ExpressionTypeDef" = None,
        SortBy: List["SortDefinitionTypeDef"] = None,
        MaxResults: int = None,
        NextPageToken: str = None
    ) -> GetDimensionValuesResponseTypeDef:
        """
        Retrieves all available filter values for a specified filter over a period of
        time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.get_dimension_values)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#get_dimension_values)
        """
    def get_reservation_coverage(
        self,
        *,
        TimePeriod: "DateIntervalTypeDef",
        GroupBy: List["GroupDefinitionTypeDef"] = None,
        Granularity: GranularityType = None,
        Filter: "ExpressionTypeDef" = None,
        Metrics: List[str] = None,
        NextPageToken: str = None,
        SortBy: "SortDefinitionTypeDef" = None,
        MaxResults: int = None
    ) -> GetReservationCoverageResponseTypeDef:
        """
        Retrieves the reservation coverage for your account, which you can use to see
        how much of your Amazon Elastic Compute Cloud, Amazon ElastiCache, Amazon
        Relational Database Service, or Amazon Redshift usage is covered by a
        reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.get_reservation_coverage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#get_reservation_coverage)
        """
    def get_reservation_purchase_recommendation(
        self,
        *,
        Service: str,
        AccountId: str = None,
        Filter: "ExpressionTypeDef" = None,
        AccountScope: AccountScopeType = None,
        LookbackPeriodInDays: LookbackPeriodInDaysType = None,
        TermInYears: TermInYearsType = None,
        PaymentOption: PaymentOptionType = None,
        ServiceSpecification: "ServiceSpecificationTypeDef" = None,
        PageSize: int = None,
        NextPageToken: str = None
    ) -> GetReservationPurchaseRecommendationResponseTypeDef:
        """
        Gets recommendations for reservation purchases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.get_reservation_purchase_recommendation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#get_reservation_purchase_recommendation)
        """
    def get_reservation_utilization(
        self,
        *,
        TimePeriod: "DateIntervalTypeDef",
        GroupBy: List["GroupDefinitionTypeDef"] = None,
        Granularity: GranularityType = None,
        Filter: "ExpressionTypeDef" = None,
        SortBy: "SortDefinitionTypeDef" = None,
        NextPageToken: str = None,
        MaxResults: int = None
    ) -> GetReservationUtilizationResponseTypeDef:
        """
        Retrieves the reservation utilization for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.get_reservation_utilization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#get_reservation_utilization)
        """
    def get_rightsizing_recommendation(
        self,
        *,
        Service: str,
        Filter: "ExpressionTypeDef" = None,
        Configuration: "RightsizingRecommendationConfigurationTypeDef" = None,
        PageSize: int = None,
        NextPageToken: str = None
    ) -> GetRightsizingRecommendationResponseTypeDef:
        """
        Creates recommendations that help you save cost by identifying idle and
        underutilized Amazon EC2 instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.get_rightsizing_recommendation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#get_rightsizing_recommendation)
        """
    def get_savings_plans_coverage(
        self,
        *,
        TimePeriod: "DateIntervalTypeDef",
        GroupBy: List["GroupDefinitionTypeDef"] = None,
        Granularity: GranularityType = None,
        Filter: "ExpressionTypeDef" = None,
        Metrics: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        SortBy: "SortDefinitionTypeDef" = None
    ) -> GetSavingsPlansCoverageResponseTypeDef:
        """
        Retrieves the Savings Plans covered for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.get_savings_plans_coverage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#get_savings_plans_coverage)
        """
    def get_savings_plans_purchase_recommendation(
        self,
        *,
        SavingsPlansType: SupportedSavingsPlansTypeType,
        TermInYears: TermInYearsType,
        PaymentOption: PaymentOptionType,
        LookbackPeriodInDays: LookbackPeriodInDaysType,
        AccountScope: AccountScopeType = None,
        NextPageToken: str = None,
        PageSize: int = None,
        Filter: "ExpressionTypeDef" = None
    ) -> GetSavingsPlansPurchaseRecommendationResponseTypeDef:
        """
        Retrieves the Savings Plans recommendations for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.get_savings_plans_purchase_recommendation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#get_savings_plans_purchase_recommendation)
        """
    def get_savings_plans_utilization(
        self,
        *,
        TimePeriod: "DateIntervalTypeDef",
        Granularity: GranularityType = None,
        Filter: "ExpressionTypeDef" = None,
        SortBy: "SortDefinitionTypeDef" = None
    ) -> GetSavingsPlansUtilizationResponseTypeDef:
        """
        Retrieves the Savings Plans utilization for your account across date ranges with
        daily or monthly granularity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.get_savings_plans_utilization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#get_savings_plans_utilization)
        """
    def get_savings_plans_utilization_details(
        self,
        *,
        TimePeriod: "DateIntervalTypeDef",
        Filter: "ExpressionTypeDef" = None,
        DataType: List[SavingsPlansDataTypeType] = None,
        NextToken: str = None,
        MaxResults: int = None,
        SortBy: "SortDefinitionTypeDef" = None
    ) -> GetSavingsPlansUtilizationDetailsResponseTypeDef:
        """
        Retrieves attribute data along with aggregate utilization and savings data for a
        given time period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.get_savings_plans_utilization_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#get_savings_plans_utilization_details)
        """
    def get_tags(
        self,
        *,
        TimePeriod: "DateIntervalTypeDef",
        SearchString: str = None,
        TagKey: str = None,
        Filter: "ExpressionTypeDef" = None,
        SortBy: List["SortDefinitionTypeDef"] = None,
        MaxResults: int = None,
        NextPageToken: str = None
    ) -> GetTagsResponseTypeDef:
        """
        Queries for available tag keys and tag values for a specified period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.get_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#get_tags)
        """
    def get_usage_forecast(
        self,
        *,
        TimePeriod: "DateIntervalTypeDef",
        Metric: MetricType,
        Granularity: GranularityType,
        Filter: "ExpressionTypeDef" = None,
        PredictionIntervalLevel: int = None
    ) -> GetUsageForecastResponseTypeDef:
        """
        Retrieves a forecast for how much Amazon Web Services predicts that you will use
        over the forecast time period that you select, based on your past usage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.get_usage_forecast)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#get_usage_forecast)
        """
    def list_cost_allocation_tags(
        self,
        *,
        Status: CostAllocationTagStatusType = None,
        TagKeys: List[str] = None,
        Type: CostAllocationTagTypeType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListCostAllocationTagsResponseTypeDef:
        """
        Get a list of cost allocation tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.list_cost_allocation_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#list_cost_allocation_tags)
        """
    def list_cost_category_definitions(
        self, *, EffectiveOn: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListCostCategoryDefinitionsResponseTypeDef:
        """
        Returns the name, Amazon Resource Name (ARN), `NumberOfRules` and effective
        dates of all Cost Categories defined in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.list_cost_category_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#list_cost_category_definitions)
        """
    def list_savings_plans_purchase_recommendation_generation(
        self,
        *,
        GenerationStatus: GenerationStatusType = None,
        RecommendationIds: List[str] = None,
        PageSize: int = None,
        NextPageToken: str = None
    ) -> ListSavingsPlansPurchaseRecommendationGenerationResponseTypeDef:
        """
        Retrieves a list of your historical recommendation generations within the past
        30 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.list_savings_plans_purchase_recommendation_generation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#list_savings_plans_purchase_recommendation_generation)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of resource tags associated with the resource specified by the
        Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#list_tags_for_resource)
        """
    def provide_anomaly_feedback(
        self, *, AnomalyId: str, Feedback: AnomalyFeedbackTypeType
    ) -> ProvideAnomalyFeedbackResponseTypeDef:
        """
        Modifies the feedback property of a given cost anomaly.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.provide_anomaly_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#provide_anomaly_feedback)
        """
    def start_savings_plans_purchase_recommendation_generation(
        self,
    ) -> StartSavingsPlansPurchaseRecommendationGenerationResponseTypeDef:
        """
        Requests a Savings Plans recommendation generation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.start_savings_plans_purchase_recommendation_generation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#start_savings_plans_purchase_recommendation_generation)
        """
    def tag_resource(
        self, *, ResourceArn: str, ResourceTags: List["ResourceTagTypeDef"]
    ) -> Dict[str, Any]:
        """
        An API operation for adding one or more tags (key-value pairs) to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, ResourceTagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#untag_resource)
        """
    def update_anomaly_monitor(
        self, *, MonitorArn: str, MonitorName: str = None
    ) -> UpdateAnomalyMonitorResponseTypeDef:
        """
        Updates an existing cost anomaly monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.update_anomaly_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#update_anomaly_monitor)
        """
    def update_anomaly_subscription(
        self,
        *,
        SubscriptionArn: str,
        Threshold: float = None,
        Frequency: AnomalySubscriptionFrequencyType = None,
        MonitorArnList: List[str] = None,
        Subscribers: List["SubscriberTypeDef"] = None,
        SubscriptionName: str = None,
        ThresholdExpression: "ExpressionTypeDef" = None
    ) -> UpdateAnomalySubscriptionResponseTypeDef:
        """
        Updates an existing cost anomaly monitor subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.update_anomaly_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#update_anomaly_subscription)
        """
    def update_cost_allocation_tags_status(
        self, *, CostAllocationTagsStatus: List["CostAllocationTagStatusEntryTypeDef"]
    ) -> UpdateCostAllocationTagsStatusResponseTypeDef:
        """
        Updates status for cost allocation tags in bulk, with maximum batch size of 20.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.update_cost_allocation_tags_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#update_cost_allocation_tags_status)
        """
    def update_cost_category_definition(
        self,
        *,
        CostCategoryArn: str,
        RuleVersion: Literal["CostCategoryExpression.v1"],
        Rules: List["CostCategoryRuleTypeDef"],
        EffectiveStart: str = None,
        DefaultValue: str = None,
        SplitChargeRules: List["CostCategorySplitChargeRuleTypeDef"] = None
    ) -> UpdateCostCategoryDefinitionResponseTypeDef:
        """
        Updates an existing Cost Category.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ce.html#CostExplorer.Client.update_cost_category_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/client.html#update_cost_category_definition)
        """
