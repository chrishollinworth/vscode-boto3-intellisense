"""
Type annotations for cost-optimization-hub service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cost_optimization_hub.type_defs import AccountEnrollmentStatusTypeDef

    data: AccountEnrollmentStatusTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ActionTypeType,
    EnrollmentStatusType,
    ImplementationEffortType,
    MemberAccountDiscountVisibilityType,
    OrderType,
    ResourceTypeType,
    SavingsEstimationModeType,
    SourceType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountEnrollmentStatusTypeDef",
    "BlockStoragePerformanceConfigurationTypeDef",
    "ComputeConfigurationTypeDef",
    "ComputeSavingsPlansConfigurationTypeDef",
    "ComputeSavingsPlansTypeDef",
    "EbsVolumeConfigurationTypeDef",
    "EbsVolumeTypeDef",
    "Ec2AutoScalingGroupConfigurationTypeDef",
    "Ec2AutoScalingGroupTypeDef",
    "Ec2InstanceConfigurationTypeDef",
    "Ec2InstanceSavingsPlansConfigurationTypeDef",
    "Ec2InstanceSavingsPlansTypeDef",
    "Ec2InstanceTypeDef",
    "Ec2ReservedInstancesConfigurationTypeDef",
    "Ec2ReservedInstancesTypeDef",
    "EcsServiceConfigurationTypeDef",
    "EcsServiceTypeDef",
    "ElastiCacheReservedInstancesConfigurationTypeDef",
    "ElastiCacheReservedInstancesTypeDef",
    "EstimatedDiscountsTypeDef",
    "FilterTypeDef",
    "GetPreferencesResponseTypeDef",
    "GetRecommendationRequestRequestTypeDef",
    "GetRecommendationResponseTypeDef",
    "InstanceConfigurationTypeDef",
    "LambdaFunctionConfigurationTypeDef",
    "LambdaFunctionTypeDef",
    "ListEnrollmentStatusesRequestRequestTypeDef",
    "ListEnrollmentStatusesResponseTypeDef",
    "ListRecommendationSummariesRequestRequestTypeDef",
    "ListRecommendationSummariesResponseTypeDef",
    "ListRecommendationsRequestRequestTypeDef",
    "ListRecommendationsResponseTypeDef",
    "OpenSearchReservedInstancesConfigurationTypeDef",
    "OpenSearchReservedInstancesTypeDef",
    "OrderByTypeDef",
    "PaginatorConfigTypeDef",
    "RdsReservedInstancesConfigurationTypeDef",
    "RdsReservedInstancesTypeDef",
    "RecommendationSummaryTypeDef",
    "RecommendationTypeDef",
    "RedshiftReservedInstancesConfigurationTypeDef",
    "RedshiftReservedInstancesTypeDef",
    "ReservedInstancesCostCalculationTypeDef",
    "ReservedInstancesPricingTypeDef",
    "ResourceCostCalculationTypeDef",
    "ResourceDetailsTypeDef",
    "ResourcePricingTypeDef",
    "ResponseMetadataTypeDef",
    "SageMakerSavingsPlansConfigurationTypeDef",
    "SageMakerSavingsPlansTypeDef",
    "SavingsPlansCostCalculationTypeDef",
    "SavingsPlansPricingTypeDef",
    "StorageConfigurationTypeDef",
    "TagTypeDef",
    "UpdateEnrollmentStatusRequestRequestTypeDef",
    "UpdateEnrollmentStatusResponseTypeDef",
    "UpdatePreferencesRequestRequestTypeDef",
    "UpdatePreferencesResponseTypeDef",
    "UsageTypeDef",
)

AccountEnrollmentStatusTypeDef = TypedDict(
    "AccountEnrollmentStatusTypeDef",
    {
        "accountId": str,
        "createdTimestamp": datetime,
        "lastUpdatedTimestamp": datetime,
        "status": EnrollmentStatusType,
    },
    total=False,
)

BlockStoragePerformanceConfigurationTypeDef = TypedDict(
    "BlockStoragePerformanceConfigurationTypeDef",
    {
        "iops": float,
        "throughput": float,
    },
    total=False,
)

ComputeConfigurationTypeDef = TypedDict(
    "ComputeConfigurationTypeDef",
    {
        "architecture": str,
        "memorySizeInMB": int,
        "platform": str,
        "vCpu": float,
    },
    total=False,
)

ComputeSavingsPlansConfigurationTypeDef = TypedDict(
    "ComputeSavingsPlansConfigurationTypeDef",
    {
        "accountScope": str,
        "hourlyCommitment": str,
        "paymentOption": str,
        "term": str,
    },
    total=False,
)

ComputeSavingsPlansTypeDef = TypedDict(
    "ComputeSavingsPlansTypeDef",
    {
        "configuration": "ComputeSavingsPlansConfigurationTypeDef",
        "costCalculation": "SavingsPlansCostCalculationTypeDef",
    },
    total=False,
)

EbsVolumeConfigurationTypeDef = TypedDict(
    "EbsVolumeConfigurationTypeDef",
    {
        "attachmentState": str,
        "performance": "BlockStoragePerformanceConfigurationTypeDef",
        "storage": "StorageConfigurationTypeDef",
    },
    total=False,
)

EbsVolumeTypeDef = TypedDict(
    "EbsVolumeTypeDef",
    {
        "configuration": "EbsVolumeConfigurationTypeDef",
        "costCalculation": "ResourceCostCalculationTypeDef",
    },
    total=False,
)

Ec2AutoScalingGroupConfigurationTypeDef = TypedDict(
    "Ec2AutoScalingGroupConfigurationTypeDef",
    {
        "instance": "InstanceConfigurationTypeDef",
    },
    total=False,
)

Ec2AutoScalingGroupTypeDef = TypedDict(
    "Ec2AutoScalingGroupTypeDef",
    {
        "configuration": "Ec2AutoScalingGroupConfigurationTypeDef",
        "costCalculation": "ResourceCostCalculationTypeDef",
    },
    total=False,
)

Ec2InstanceConfigurationTypeDef = TypedDict(
    "Ec2InstanceConfigurationTypeDef",
    {
        "instance": "InstanceConfigurationTypeDef",
    },
    total=False,
)

Ec2InstanceSavingsPlansConfigurationTypeDef = TypedDict(
    "Ec2InstanceSavingsPlansConfigurationTypeDef",
    {
        "accountScope": str,
        "hourlyCommitment": str,
        "instanceFamily": str,
        "paymentOption": str,
        "savingsPlansRegion": str,
        "term": str,
    },
    total=False,
)

Ec2InstanceSavingsPlansTypeDef = TypedDict(
    "Ec2InstanceSavingsPlansTypeDef",
    {
        "configuration": "Ec2InstanceSavingsPlansConfigurationTypeDef",
        "costCalculation": "SavingsPlansCostCalculationTypeDef",
    },
    total=False,
)

Ec2InstanceTypeDef = TypedDict(
    "Ec2InstanceTypeDef",
    {
        "configuration": "Ec2InstanceConfigurationTypeDef",
        "costCalculation": "ResourceCostCalculationTypeDef",
    },
    total=False,
)

Ec2ReservedInstancesConfigurationTypeDef = TypedDict(
    "Ec2ReservedInstancesConfigurationTypeDef",
    {
        "accountScope": str,
        "currentGeneration": str,
        "instanceFamily": str,
        "instanceType": str,
        "monthlyRecurringCost": str,
        "normalizedUnitsToPurchase": str,
        "numberOfInstancesToPurchase": str,
        "offeringClass": str,
        "paymentOption": str,
        "platform": str,
        "reservedInstancesRegion": str,
        "service": str,
        "sizeFlexEligible": bool,
        "tenancy": str,
        "term": str,
        "upfrontCost": str,
    },
    total=False,
)

Ec2ReservedInstancesTypeDef = TypedDict(
    "Ec2ReservedInstancesTypeDef",
    {
        "configuration": "Ec2ReservedInstancesConfigurationTypeDef",
        "costCalculation": "ReservedInstancesCostCalculationTypeDef",
    },
    total=False,
)

EcsServiceConfigurationTypeDef = TypedDict(
    "EcsServiceConfigurationTypeDef",
    {
        "compute": "ComputeConfigurationTypeDef",
    },
    total=False,
)

EcsServiceTypeDef = TypedDict(
    "EcsServiceTypeDef",
    {
        "configuration": "EcsServiceConfigurationTypeDef",
        "costCalculation": "ResourceCostCalculationTypeDef",
    },
    total=False,
)

ElastiCacheReservedInstancesConfigurationTypeDef = TypedDict(
    "ElastiCacheReservedInstancesConfigurationTypeDef",
    {
        "accountScope": str,
        "currentGeneration": str,
        "instanceFamily": str,
        "instanceType": str,
        "monthlyRecurringCost": str,
        "normalizedUnitsToPurchase": str,
        "numberOfInstancesToPurchase": str,
        "paymentOption": str,
        "reservedInstancesRegion": str,
        "service": str,
        "sizeFlexEligible": bool,
        "term": str,
        "upfrontCost": str,
    },
    total=False,
)

ElastiCacheReservedInstancesTypeDef = TypedDict(
    "ElastiCacheReservedInstancesTypeDef",
    {
        "configuration": "ElastiCacheReservedInstancesConfigurationTypeDef",
        "costCalculation": "ReservedInstancesCostCalculationTypeDef",
    },
    total=False,
)

EstimatedDiscountsTypeDef = TypedDict(
    "EstimatedDiscountsTypeDef",
    {
        "otherDiscount": float,
        "reservedInstancesDiscount": float,
        "savingsPlansDiscount": float,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "accountIds": List[str],
        "actionTypes": List[ActionTypeType],
        "implementationEfforts": List[ImplementationEffortType],
        "recommendationIds": List[str],
        "regions": List[str],
        "resourceArns": List[str],
        "resourceIds": List[str],
        "resourceTypes": List[ResourceTypeType],
        "restartNeeded": bool,
        "rollbackPossible": bool,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

GetPreferencesResponseTypeDef = TypedDict(
    "GetPreferencesResponseTypeDef",
    {
        "memberAccountDiscountVisibility": MemberAccountDiscountVisibilityType,
        "savingsEstimationMode": SavingsEstimationModeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecommendationRequestRequestTypeDef = TypedDict(
    "GetRecommendationRequestRequestTypeDef",
    {
        "recommendationId": str,
    },
)

GetRecommendationResponseTypeDef = TypedDict(
    "GetRecommendationResponseTypeDef",
    {
        "accountId": str,
        "actionType": ActionTypeType,
        "costCalculationLookbackPeriodInDays": int,
        "currencyCode": str,
        "currentResourceDetails": "ResourceDetailsTypeDef",
        "currentResourceType": ResourceTypeType,
        "estimatedMonthlyCost": float,
        "estimatedMonthlySavings": float,
        "estimatedSavingsOverCostCalculationLookbackPeriod": float,
        "estimatedSavingsPercentage": float,
        "implementationEffort": ImplementationEffortType,
        "lastRefreshTimestamp": datetime,
        "recommendationId": str,
        "recommendationLookbackPeriodInDays": int,
        "recommendedResourceDetails": "ResourceDetailsTypeDef",
        "recommendedResourceType": ResourceTypeType,
        "region": str,
        "resourceArn": str,
        "resourceId": str,
        "restartNeeded": bool,
        "rollbackPossible": bool,
        "source": SourceType,
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceConfigurationTypeDef = TypedDict(
    "InstanceConfigurationTypeDef",
    {
        "type": str,
    },
    total=False,
)

LambdaFunctionConfigurationTypeDef = TypedDict(
    "LambdaFunctionConfigurationTypeDef",
    {
        "compute": "ComputeConfigurationTypeDef",
    },
    total=False,
)

LambdaFunctionTypeDef = TypedDict(
    "LambdaFunctionTypeDef",
    {
        "configuration": "LambdaFunctionConfigurationTypeDef",
        "costCalculation": "ResourceCostCalculationTypeDef",
    },
    total=False,
)

ListEnrollmentStatusesRequestRequestTypeDef = TypedDict(
    "ListEnrollmentStatusesRequestRequestTypeDef",
    {
        "accountId": str,
        "includeOrganizationInfo": bool,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListEnrollmentStatusesResponseTypeDef = TypedDict(
    "ListEnrollmentStatusesResponseTypeDef",
    {
        "items": List["AccountEnrollmentStatusTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRecommendationSummariesRequestRequestTypeDef = TypedDict(
    "_RequiredListRecommendationSummariesRequestRequestTypeDef",
    {
        "groupBy": str,
    },
)
_OptionalListRecommendationSummariesRequestRequestTypeDef = TypedDict(
    "_OptionalListRecommendationSummariesRequestRequestTypeDef",
    {
        "filter": "FilterTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListRecommendationSummariesRequestRequestTypeDef(
    _RequiredListRecommendationSummariesRequestRequestTypeDef,
    _OptionalListRecommendationSummariesRequestRequestTypeDef,
):
    pass

ListRecommendationSummariesResponseTypeDef = TypedDict(
    "ListRecommendationSummariesResponseTypeDef",
    {
        "currencyCode": str,
        "estimatedTotalDedupedSavings": float,
        "groupBy": str,
        "items": List["RecommendationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecommendationsRequestRequestTypeDef = TypedDict(
    "ListRecommendationsRequestRequestTypeDef",
    {
        "filter": "FilterTypeDef",
        "includeAllRecommendations": bool,
        "maxResults": int,
        "nextToken": str,
        "orderBy": "OrderByTypeDef",
    },
    total=False,
)

ListRecommendationsResponseTypeDef = TypedDict(
    "ListRecommendationsResponseTypeDef",
    {
        "items": List["RecommendationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OpenSearchReservedInstancesConfigurationTypeDef = TypedDict(
    "OpenSearchReservedInstancesConfigurationTypeDef",
    {
        "accountScope": str,
        "currentGeneration": str,
        "instanceType": str,
        "monthlyRecurringCost": str,
        "normalizedUnitsToPurchase": str,
        "numberOfInstancesToPurchase": str,
        "paymentOption": str,
        "reservedInstancesRegion": str,
        "service": str,
        "sizeFlexEligible": bool,
        "term": str,
        "upfrontCost": str,
    },
    total=False,
)

OpenSearchReservedInstancesTypeDef = TypedDict(
    "OpenSearchReservedInstancesTypeDef",
    {
        "configuration": "OpenSearchReservedInstancesConfigurationTypeDef",
        "costCalculation": "ReservedInstancesCostCalculationTypeDef",
    },
    total=False,
)

OrderByTypeDef = TypedDict(
    "OrderByTypeDef",
    {
        "dimension": str,
        "order": OrderType,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

RdsReservedInstancesConfigurationTypeDef = TypedDict(
    "RdsReservedInstancesConfigurationTypeDef",
    {
        "accountScope": str,
        "currentGeneration": str,
        "databaseEdition": str,
        "databaseEngine": str,
        "deploymentOption": str,
        "instanceFamily": str,
        "instanceType": str,
        "licenseModel": str,
        "monthlyRecurringCost": str,
        "normalizedUnitsToPurchase": str,
        "numberOfInstancesToPurchase": str,
        "paymentOption": str,
        "reservedInstancesRegion": str,
        "service": str,
        "sizeFlexEligible": bool,
        "term": str,
        "upfrontCost": str,
    },
    total=False,
)

RdsReservedInstancesTypeDef = TypedDict(
    "RdsReservedInstancesTypeDef",
    {
        "configuration": "RdsReservedInstancesConfigurationTypeDef",
        "costCalculation": "ReservedInstancesCostCalculationTypeDef",
    },
    total=False,
)

RecommendationSummaryTypeDef = TypedDict(
    "RecommendationSummaryTypeDef",
    {
        "estimatedMonthlySavings": float,
        "group": str,
        "recommendationCount": int,
    },
    total=False,
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "accountId": str,
        "actionType": str,
        "currencyCode": str,
        "currentResourceSummary": str,
        "currentResourceType": str,
        "estimatedMonthlyCost": float,
        "estimatedMonthlySavings": float,
        "estimatedSavingsPercentage": float,
        "implementationEffort": str,
        "lastRefreshTimestamp": datetime,
        "recommendationId": str,
        "recommendationLookbackPeriodInDays": int,
        "recommendedResourceSummary": str,
        "recommendedResourceType": str,
        "region": str,
        "resourceArn": str,
        "resourceId": str,
        "restartNeeded": bool,
        "rollbackPossible": bool,
        "source": SourceType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

RedshiftReservedInstancesConfigurationTypeDef = TypedDict(
    "RedshiftReservedInstancesConfigurationTypeDef",
    {
        "accountScope": str,
        "currentGeneration": str,
        "instanceFamily": str,
        "instanceType": str,
        "monthlyRecurringCost": str,
        "normalizedUnitsToPurchase": str,
        "numberOfInstancesToPurchase": str,
        "paymentOption": str,
        "reservedInstancesRegion": str,
        "service": str,
        "sizeFlexEligible": bool,
        "term": str,
        "upfrontCost": str,
    },
    total=False,
)

RedshiftReservedInstancesTypeDef = TypedDict(
    "RedshiftReservedInstancesTypeDef",
    {
        "configuration": "RedshiftReservedInstancesConfigurationTypeDef",
        "costCalculation": "ReservedInstancesCostCalculationTypeDef",
    },
    total=False,
)

ReservedInstancesCostCalculationTypeDef = TypedDict(
    "ReservedInstancesCostCalculationTypeDef",
    {
        "pricing": "ReservedInstancesPricingTypeDef",
    },
    total=False,
)

ReservedInstancesPricingTypeDef = TypedDict(
    "ReservedInstancesPricingTypeDef",
    {
        "estimatedMonthlyAmortizedReservationCost": float,
        "estimatedOnDemandCost": float,
        "monthlyReservationEligibleCost": float,
        "savingsPercentage": float,
    },
    total=False,
)

ResourceCostCalculationTypeDef = TypedDict(
    "ResourceCostCalculationTypeDef",
    {
        "pricing": "ResourcePricingTypeDef",
        "usages": List["UsageTypeDef"],
    },
    total=False,
)

ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "computeSavingsPlans": "ComputeSavingsPlansTypeDef",
        "ebsVolume": "EbsVolumeTypeDef",
        "ec2AutoScalingGroup": "Ec2AutoScalingGroupTypeDef",
        "ec2Instance": "Ec2InstanceTypeDef",
        "ec2InstanceSavingsPlans": "Ec2InstanceSavingsPlansTypeDef",
        "ec2ReservedInstances": "Ec2ReservedInstancesTypeDef",
        "ecsService": "EcsServiceTypeDef",
        "elastiCacheReservedInstances": "ElastiCacheReservedInstancesTypeDef",
        "lambdaFunction": "LambdaFunctionTypeDef",
        "openSearchReservedInstances": "OpenSearchReservedInstancesTypeDef",
        "rdsReservedInstances": "RdsReservedInstancesTypeDef",
        "redshiftReservedInstances": "RedshiftReservedInstancesTypeDef",
        "sageMakerSavingsPlans": "SageMakerSavingsPlansTypeDef",
    },
    total=False,
)

ResourcePricingTypeDef = TypedDict(
    "ResourcePricingTypeDef",
    {
        "estimatedCostAfterDiscounts": float,
        "estimatedCostBeforeDiscounts": float,
        "estimatedDiscounts": "EstimatedDiscountsTypeDef",
        "estimatedNetUnusedAmortizedCommitments": float,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

SageMakerSavingsPlansConfigurationTypeDef = TypedDict(
    "SageMakerSavingsPlansConfigurationTypeDef",
    {
        "accountScope": str,
        "hourlyCommitment": str,
        "paymentOption": str,
        "term": str,
    },
    total=False,
)

SageMakerSavingsPlansTypeDef = TypedDict(
    "SageMakerSavingsPlansTypeDef",
    {
        "configuration": "SageMakerSavingsPlansConfigurationTypeDef",
        "costCalculation": "SavingsPlansCostCalculationTypeDef",
    },
    total=False,
)

SavingsPlansCostCalculationTypeDef = TypedDict(
    "SavingsPlansCostCalculationTypeDef",
    {
        "pricing": "SavingsPlansPricingTypeDef",
    },
    total=False,
)

SavingsPlansPricingTypeDef = TypedDict(
    "SavingsPlansPricingTypeDef",
    {
        "estimatedMonthlyCommitment": float,
        "estimatedOnDemandCost": float,
        "monthlySavingsPlansEligibleCost": float,
        "savingsPercentage": float,
    },
    total=False,
)

StorageConfigurationTypeDef = TypedDict(
    "StorageConfigurationTypeDef",
    {
        "sizeInGb": float,
        "type": str,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

_RequiredUpdateEnrollmentStatusRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEnrollmentStatusRequestRequestTypeDef",
    {
        "status": EnrollmentStatusType,
    },
)
_OptionalUpdateEnrollmentStatusRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEnrollmentStatusRequestRequestTypeDef",
    {
        "includeMemberAccounts": bool,
    },
    total=False,
)

class UpdateEnrollmentStatusRequestRequestTypeDef(
    _RequiredUpdateEnrollmentStatusRequestRequestTypeDef,
    _OptionalUpdateEnrollmentStatusRequestRequestTypeDef,
):
    pass

UpdateEnrollmentStatusResponseTypeDef = TypedDict(
    "UpdateEnrollmentStatusResponseTypeDef",
    {
        "status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePreferencesRequestRequestTypeDef = TypedDict(
    "UpdatePreferencesRequestRequestTypeDef",
    {
        "memberAccountDiscountVisibility": MemberAccountDiscountVisibilityType,
        "savingsEstimationMode": SavingsEstimationModeType,
    },
    total=False,
)

UpdatePreferencesResponseTypeDef = TypedDict(
    "UpdatePreferencesResponseTypeDef",
    {
        "memberAccountDiscountVisibility": MemberAccountDiscountVisibilityType,
        "savingsEstimationMode": SavingsEstimationModeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsageTypeDef = TypedDict(
    "UsageTypeDef",
    {
        "operation": str,
        "productCode": str,
        "unit": str,
        "usageAmount": float,
        "usageType": str,
    },
    total=False,
)
