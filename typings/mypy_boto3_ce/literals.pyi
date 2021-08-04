"""
Type annotations for ce service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/literals.html)

Usage::

    ```python
    from mypy_boto3_ce.literals import AccountScopeType

    data: AccountScopeType = "LINKED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccountScopeType",
    "AnomalyFeedbackTypeType",
    "AnomalySubscriptionFrequencyType",
    "ContextType",
    "CostCategoryInheritedValueDimensionNameType",
    "CostCategoryRuleTypeType",
    "CostCategoryRuleVersionType",
    "CostCategoryStatusComponentType",
    "CostCategoryStatusType",
    "DimensionType",
    "FindingReasonCodeType",
    "GranularityType",
    "GroupDefinitionTypeType",
    "LookbackPeriodInDaysType",
    "MatchOptionType",
    "MetricType",
    "MonitorDimensionType",
    "MonitorTypeType",
    "NumericOperatorType",
    "OfferingClassType",
    "PaymentOptionType",
    "PlatformDifferenceType",
    "RecommendationTargetType",
    "RightsizingTypeType",
    "SavingsPlansDataTypeType",
    "SortOrderType",
    "SubscriberStatusType",
    "SubscriberTypeType",
    "SupportedSavingsPlansTypeType",
    "TermInYearsType",
)

AccountScopeType = Literal["LINKED", "PAYER"]
AnomalyFeedbackTypeType = Literal["NO", "PLANNED_ACTIVITY", "YES"]
AnomalySubscriptionFrequencyType = Literal["DAILY", "IMMEDIATE", "WEEKLY"]
ContextType = Literal["COST_AND_USAGE", "RESERVATIONS", "SAVINGS_PLANS"]
CostCategoryInheritedValueDimensionNameType = Literal["LINKED_ACCOUNT_NAME", "TAG"]
CostCategoryRuleTypeType = Literal["INHERITED_VALUE", "REGULAR"]
CostCategoryRuleVersionType = Literal["CostCategoryExpression.v1"]
CostCategoryStatusComponentType = Literal["COST_EXPLORER"]
CostCategoryStatusType = Literal["APPLIED", "PROCESSING"]
DimensionType = Literal[
    "AGREEMENT_END_DATE_TIME_AFTER",
    "AGREEMENT_END_DATE_TIME_BEFORE",
    "AZ",
    "BILLING_ENTITY",
    "CACHE_ENGINE",
    "DATABASE_ENGINE",
    "DEPLOYMENT_OPTION",
    "INSTANCE_TYPE",
    "INSTANCE_TYPE_FAMILY",
    "LEGAL_ENTITY_NAME",
    "LINKED_ACCOUNT",
    "LINKED_ACCOUNT_NAME",
    "OPERATING_SYSTEM",
    "OPERATION",
    "PAYMENT_OPTION",
    "PLATFORM",
    "PURCHASE_TYPE",
    "RECORD_TYPE",
    "REGION",
    "RESERVATION_ID",
    "RESOURCE_ID",
    "RIGHTSIZING_TYPE",
    "SAVINGS_PLANS_TYPE",
    "SAVINGS_PLAN_ARN",
    "SCOPE",
    "SERVICE",
    "SERVICE_CODE",
    "SUBSCRIPTION_ID",
    "TENANCY",
    "USAGE_TYPE",
    "USAGE_TYPE_GROUP",
]
FindingReasonCodeType = Literal[
    "CPU_OVER_PROVISIONED",
    "CPU_UNDER_PROVISIONED",
    "DISK_IOPS_OVER_PROVISIONED",
    "DISK_IOPS_UNDER_PROVISIONED",
    "DISK_THROUGHPUT_OVER_PROVISIONED",
    "DISK_THROUGHPUT_UNDER_PROVISIONED",
    "EBS_IOPS_OVER_PROVISIONED",
    "EBS_IOPS_UNDER_PROVISIONED",
    "EBS_THROUGHPUT_OVER_PROVISIONED",
    "EBS_THROUGHPUT_UNDER_PROVISIONED",
    "MEMORY_OVER_PROVISIONED",
    "MEMORY_UNDER_PROVISIONED",
    "NETWORK_BANDWIDTH_OVER_PROVISIONED",
    "NETWORK_BANDWIDTH_UNDER_PROVISIONED",
    "NETWORK_PPS_OVER_PROVISIONED",
    "NETWORK_PPS_UNDER_PROVISIONED",
]
GranularityType = Literal["DAILY", "HOURLY", "MONTHLY"]
GroupDefinitionTypeType = Literal["COST_CATEGORY", "DIMENSION", "TAG"]
LookbackPeriodInDaysType = Literal["SEVEN_DAYS", "SIXTY_DAYS", "THIRTY_DAYS"]
MatchOptionType = Literal[
    "ABSENT", "CASE_INSENSITIVE", "CASE_SENSITIVE", "CONTAINS", "ENDS_WITH", "EQUALS", "STARTS_WITH"
]
MetricType = Literal[
    "AMORTIZED_COST",
    "BLENDED_COST",
    "NET_AMORTIZED_COST",
    "NET_UNBLENDED_COST",
    "NORMALIZED_USAGE_AMOUNT",
    "UNBLENDED_COST",
    "USAGE_QUANTITY",
]
MonitorDimensionType = Literal["SERVICE"]
MonitorTypeType = Literal["CUSTOM", "DIMENSIONAL"]
NumericOperatorType = Literal[
    "BETWEEN", "EQUAL", "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL"
]
OfferingClassType = Literal["CONVERTIBLE", "STANDARD"]
PaymentOptionType = Literal[
    "ALL_UPFRONT",
    "HEAVY_UTILIZATION",
    "LIGHT_UTILIZATION",
    "MEDIUM_UTILIZATION",
    "NO_UPFRONT",
    "PARTIAL_UPFRONT",
]
PlatformDifferenceType = Literal[
    "HYPERVISOR",
    "INSTANCE_STORE_AVAILABILITY",
    "NETWORK_INTERFACE",
    "STORAGE_INTERFACE",
    "VIRTUALIZATION_TYPE",
]
RecommendationTargetType = Literal["CROSS_INSTANCE_FAMILY", "SAME_INSTANCE_FAMILY"]
RightsizingTypeType = Literal["MODIFY", "TERMINATE"]
SavingsPlansDataTypeType = Literal["AMORTIZED_COMMITMENT", "ATTRIBUTES", "SAVINGS", "UTILIZATION"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
SubscriberStatusType = Literal["CONFIRMED", "DECLINED"]
SubscriberTypeType = Literal["EMAIL", "SNS"]
SupportedSavingsPlansTypeType = Literal["COMPUTE_SP", "EC2_INSTANCE_SP", "SAGEMAKER_SP"]
TermInYearsType = Literal["ONE_YEAR", "THREE_YEARS"]
