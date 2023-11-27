"""
Type annotations for cost-optimization-hub service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/literals.html)

Usage::

    ```python
    from mypy_boto3_cost_optimization_hub.literals import ActionTypeType

    data: ActionTypeType = "MigrateToGraviton"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionTypeType",
    "EnrollmentStatusType",
    "ImplementationEffortType",
    "ListEnrollmentStatusesPaginatorName",
    "ListRecommendationSummariesPaginatorName",
    "ListRecommendationsPaginatorName",
    "MemberAccountDiscountVisibilityType",
    "OrderType",
    "ResourceTypeType",
    "SavingsEstimationModeType",
    "SourceType",
)

ActionTypeType = Literal[
    "MigrateToGraviton",
    "PurchaseReservedInstances",
    "PurchaseSavingsPlans",
    "Rightsize",
    "Stop",
    "Upgrade",
]
EnrollmentStatusType = Literal["Active", "Inactive"]
ImplementationEffortType = Literal["High", "Low", "Medium", "VeryHigh", "VeryLow"]
ListEnrollmentStatusesPaginatorName = Literal["list_enrollment_statuses"]
ListRecommendationSummariesPaginatorName = Literal["list_recommendation_summaries"]
ListRecommendationsPaginatorName = Literal["list_recommendations"]
MemberAccountDiscountVisibilityType = Literal["All", "None"]
OrderType = Literal["Asc", "Desc"]
ResourceTypeType = Literal[
    "ComputeSavingsPlans",
    "EbsVolume",
    "Ec2AutoScalingGroup",
    "Ec2Instance",
    "Ec2InstanceSavingsPlans",
    "Ec2ReservedInstances",
    "EcsService",
    "ElastiCacheReservedInstances",
    "LambdaFunction",
    "OpenSearchReservedInstances",
    "RdsReservedInstances",
    "RedshiftReservedInstances",
    "SageMakerSavingsPlans",
]
SavingsEstimationModeType = Literal["AfterDiscounts", "BeforeDiscounts"]
SourceType = Literal["ComputeOptimizer", "CostExplorer"]
