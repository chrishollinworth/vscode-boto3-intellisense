# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for ce service client

Usage::

    ```python
    import boto3
    from mypy_boto3_ce import CostExplorerClient

    client: CostExplorerClient = boto3.client("ce")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_ce.type_defs import (
    CostCategoryRuleTypeDef,
    CreateCostCategoryDefinitionResponseTypeDef,
    DateIntervalTypeDef,
    DeleteCostCategoryDefinitionResponseTypeDef,
    DescribeCostCategoryDefinitionResponseTypeDef,
    GetCostAndUsageResponseTypeDef,
    GetCostAndUsageWithResourcesResponseTypeDef,
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
    ListCostCategoryDefinitionsResponseTypeDef,
    RightsizingRecommendationConfigurationTypeDef,
    ServiceSpecificationTypeDef,
    UpdateCostCategoryDefinitionResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CostExplorerClient",)


class Exceptions:
    BillExpirationException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    DataUnavailableException: Type[Boto3ClientError]
    InvalidNextTokenException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    RequestChangedException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    ServiceQuotaExceededException: Type[Boto3ClientError]
    UnresolvableUsageUnitException: Type[Boto3ClientError]


class CostExplorerClient:
    """
    [CostExplorer.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.can_paginate)
        """

    def create_cost_category_definition(
        self,
        Name: str,
        RuleVersion: Literal["CostCategoryExpression.v1"],
        Rules: List["CostCategoryRuleTypeDef"],
    ) -> CreateCostCategoryDefinitionResponseTypeDef:
        """
        [Client.create_cost_category_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.create_cost_category_definition)
        """

    def delete_cost_category_definition(
        self, CostCategoryArn: str
    ) -> DeleteCostCategoryDefinitionResponseTypeDef:
        """
        [Client.delete_cost_category_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.delete_cost_category_definition)
        """

    def describe_cost_category_definition(
        self, CostCategoryArn: str, EffectiveOn: str = None
    ) -> DescribeCostCategoryDefinitionResponseTypeDef:
        """
        [Client.describe_cost_category_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.describe_cost_category_definition)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.generate_presigned_url)
        """

    def get_cost_and_usage(
        self,
        TimePeriod: "DateIntervalTypeDef",
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"] = None,
        Filter: Dict[str, Any] = None,
        Metrics: List[str] = None,
        GroupBy: List["GroupDefinitionTypeDef"] = None,
        NextPageToken: str = None,
    ) -> GetCostAndUsageResponseTypeDef:
        """
        [Client.get_cost_and_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.get_cost_and_usage)
        """

    def get_cost_and_usage_with_resources(
        self,
        TimePeriod: "DateIntervalTypeDef",
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"] = None,
        Filter: Dict[str, Any] = None,
        Metrics: List[str] = None,
        GroupBy: List["GroupDefinitionTypeDef"] = None,
        NextPageToken: str = None,
    ) -> GetCostAndUsageWithResourcesResponseTypeDef:
        """
        [Client.get_cost_and_usage_with_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.get_cost_and_usage_with_resources)
        """

    def get_cost_forecast(
        self,
        TimePeriod: "DateIntervalTypeDef",
        Metric: Literal[
            "BLENDED_COST",
            "UNBLENDED_COST",
            "AMORTIZED_COST",
            "NET_UNBLENDED_COST",
            "NET_AMORTIZED_COST",
            "USAGE_QUANTITY",
            "NORMALIZED_USAGE_AMOUNT",
        ],
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"],
        Filter: Dict[str, Any] = None,
        PredictionIntervalLevel: int = None,
    ) -> GetCostForecastResponseTypeDef:
        """
        [Client.get_cost_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.get_cost_forecast)
        """

    def get_dimension_values(
        self,
        TimePeriod: "DateIntervalTypeDef",
        Dimension: Literal[
            "AZ",
            "INSTANCE_TYPE",
            "LINKED_ACCOUNT",
            "LINKED_ACCOUNT_NAME",
            "OPERATION",
            "PURCHASE_TYPE",
            "REGION",
            "SERVICE",
            "SERVICE_CODE",
            "USAGE_TYPE",
            "USAGE_TYPE_GROUP",
            "RECORD_TYPE",
            "OPERATING_SYSTEM",
            "TENANCY",
            "SCOPE",
            "PLATFORM",
            "SUBSCRIPTION_ID",
            "LEGAL_ENTITY_NAME",
            "DEPLOYMENT_OPTION",
            "DATABASE_ENGINE",
            "CACHE_ENGINE",
            "INSTANCE_TYPE_FAMILY",
            "BILLING_ENTITY",
            "RESERVATION_ID",
            "RESOURCE_ID",
            "RIGHTSIZING_TYPE",
            "SAVINGS_PLANS_TYPE",
            "SAVINGS_PLAN_ARN",
            "PAYMENT_OPTION",
        ],
        SearchString: str = None,
        Context: Literal["COST_AND_USAGE", "RESERVATIONS", "SAVINGS_PLANS"] = None,
        NextPageToken: str = None,
    ) -> GetDimensionValuesResponseTypeDef:
        """
        [Client.get_dimension_values documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.get_dimension_values)
        """

    def get_reservation_coverage(
        self,
        TimePeriod: "DateIntervalTypeDef",
        GroupBy: List["GroupDefinitionTypeDef"] = None,
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"] = None,
        Filter: Dict[str, Any] = None,
        Metrics: List[str] = None,
        NextPageToken: str = None,
    ) -> GetReservationCoverageResponseTypeDef:
        """
        [Client.get_reservation_coverage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.get_reservation_coverage)
        """

    def get_reservation_purchase_recommendation(
        self,
        Service: str,
        AccountId: str = None,
        AccountScope: Literal["PAYER", "LINKED"] = None,
        LookbackPeriodInDays: Literal["SEVEN_DAYS", "THIRTY_DAYS", "SIXTY_DAYS"] = None,
        TermInYears: Literal["ONE_YEAR", "THREE_YEARS"] = None,
        PaymentOption: Literal[
            "NO_UPFRONT",
            "PARTIAL_UPFRONT",
            "ALL_UPFRONT",
            "LIGHT_UTILIZATION",
            "MEDIUM_UTILIZATION",
            "HEAVY_UTILIZATION",
        ] = None,
        ServiceSpecification: "ServiceSpecificationTypeDef" = None,
        PageSize: int = None,
        NextPageToken: str = None,
    ) -> GetReservationPurchaseRecommendationResponseTypeDef:
        """
        [Client.get_reservation_purchase_recommendation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.get_reservation_purchase_recommendation)
        """

    def get_reservation_utilization(
        self,
        TimePeriod: "DateIntervalTypeDef",
        GroupBy: List["GroupDefinitionTypeDef"] = None,
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"] = None,
        Filter: Dict[str, Any] = None,
        NextPageToken: str = None,
    ) -> GetReservationUtilizationResponseTypeDef:
        """
        [Client.get_reservation_utilization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.get_reservation_utilization)
        """

    def get_rightsizing_recommendation(
        self,
        Service: str,
        Filter: Dict[str, Any] = None,
        Configuration: "RightsizingRecommendationConfigurationTypeDef" = None,
        PageSize: int = None,
        NextPageToken: str = None,
    ) -> GetRightsizingRecommendationResponseTypeDef:
        """
        [Client.get_rightsizing_recommendation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.get_rightsizing_recommendation)
        """

    def get_savings_plans_coverage(
        self,
        TimePeriod: "DateIntervalTypeDef",
        GroupBy: List["GroupDefinitionTypeDef"] = None,
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"] = None,
        Filter: Dict[str, Any] = None,
        Metrics: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetSavingsPlansCoverageResponseTypeDef:
        """
        [Client.get_savings_plans_coverage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.get_savings_plans_coverage)
        """

    def get_savings_plans_purchase_recommendation(
        self,
        SavingsPlansType: Literal["COMPUTE_SP", "EC2_INSTANCE_SP"],
        TermInYears: Literal["ONE_YEAR", "THREE_YEARS"],
        PaymentOption: Literal[
            "NO_UPFRONT",
            "PARTIAL_UPFRONT",
            "ALL_UPFRONT",
            "LIGHT_UTILIZATION",
            "MEDIUM_UTILIZATION",
            "HEAVY_UTILIZATION",
        ],
        LookbackPeriodInDays: Literal["SEVEN_DAYS", "THIRTY_DAYS", "SIXTY_DAYS"],
        AccountScope: Literal["PAYER", "LINKED"] = None,
        NextPageToken: str = None,
        PageSize: int = None,
        Filter: Dict[str, Any] = None,
    ) -> GetSavingsPlansPurchaseRecommendationResponseTypeDef:
        """
        [Client.get_savings_plans_purchase_recommendation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.get_savings_plans_purchase_recommendation)
        """

    def get_savings_plans_utilization(
        self,
        TimePeriod: "DateIntervalTypeDef",
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"] = None,
        Filter: Dict[str, Any] = None,
    ) -> GetSavingsPlansUtilizationResponseTypeDef:
        """
        [Client.get_savings_plans_utilization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.get_savings_plans_utilization)
        """

    def get_savings_plans_utilization_details(
        self,
        TimePeriod: "DateIntervalTypeDef",
        Filter: Dict[str, Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetSavingsPlansUtilizationDetailsResponseTypeDef:
        """
        [Client.get_savings_plans_utilization_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.get_savings_plans_utilization_details)
        """

    def get_tags(
        self,
        TimePeriod: "DateIntervalTypeDef",
        SearchString: str = None,
        TagKey: str = None,
        NextPageToken: str = None,
    ) -> GetTagsResponseTypeDef:
        """
        [Client.get_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.get_tags)
        """

    def get_usage_forecast(
        self,
        TimePeriod: "DateIntervalTypeDef",
        Metric: Literal[
            "BLENDED_COST",
            "UNBLENDED_COST",
            "AMORTIZED_COST",
            "NET_UNBLENDED_COST",
            "NET_AMORTIZED_COST",
            "USAGE_QUANTITY",
            "NORMALIZED_USAGE_AMOUNT",
        ],
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"],
        Filter: Dict[str, Any] = None,
        PredictionIntervalLevel: int = None,
    ) -> GetUsageForecastResponseTypeDef:
        """
        [Client.get_usage_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.get_usage_forecast)
        """

    def list_cost_category_definitions(
        self, EffectiveOn: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListCostCategoryDefinitionsResponseTypeDef:
        """
        [Client.list_cost_category_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.list_cost_category_definitions)
        """

    def update_cost_category_definition(
        self,
        CostCategoryArn: str,
        RuleVersion: Literal["CostCategoryExpression.v1"],
        Rules: List["CostCategoryRuleTypeDef"],
    ) -> UpdateCostCategoryDefinitionResponseTypeDef:
        """
        [Client.update_cost_category_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ce.html#CostExplorer.Client.update_cost_category_definition)
        """
