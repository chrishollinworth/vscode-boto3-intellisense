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
    "DbInstanceConfigurationTypeDef",
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
    "RdsDbInstanceConfigurationTypeDef",
    "RdsDbInstanceStorageConfigurationTypeDef",
    "RdsDbInstanceStorageTypeDef",
    "RdsDbInstanceTypeDef",
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
        "status": EnrollmentStatusType,
        "lastUpdatedTimestamp": datetime,
        "createdTimestamp": datetime,
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
        "vCpu": float,
        "memorySizeInMB": int,
        "architecture": str,
        "platform": str,
    },
    total=False,
)

ComputeSavingsPlansConfigurationTypeDef = TypedDict(
    "ComputeSavingsPlansConfigurationTypeDef",
    {
        "accountScope": str,
        "term": str,
        "paymentOption": str,
        "hourlyCommitment": str,
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

DbInstanceConfigurationTypeDef = TypedDict(
    "DbInstanceConfigurationTypeDef",
    {
        "dbInstanceClass": str,
    },
    total=False,
)

EbsVolumeConfigurationTypeDef = TypedDict(
    "EbsVolumeConfigurationTypeDef",
    {
        "storage": "StorageConfigurationTypeDef",
        "performance": "BlockStoragePerformanceConfigurationTypeDef",
        "attachmentState": str,
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
        "term": str,
        "paymentOption": str,
        "hourlyCommitment": str,
        "instanceFamily": str,
        "savingsPlansRegion": str,
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
        "service": str,
        "normalizedUnitsToPurchase": str,
        "term": str,
        "paymentOption": str,
        "numberOfInstancesToPurchase": str,
        "offeringClass": str,
        "instanceFamily": str,
        "instanceType": str,
        "reservedInstancesRegion": str,
        "currentGeneration": str,
        "platform": str,
        "tenancy": str,
        "sizeFlexEligible": bool,
        "upfrontCost": str,
        "monthlyRecurringCost": str,
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
        "service": str,
        "normalizedUnitsToPurchase": str,
        "term": str,
        "paymentOption": str,
        "numberOfInstancesToPurchase": str,
        "instanceFamily": str,
        "instanceType": str,
        "reservedInstancesRegion": str,
        "currentGeneration": str,
        "sizeFlexEligible": bool,
        "upfrontCost": str,
        "monthlyRecurringCost": str,
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
        "savingsPlansDiscount": float,
        "reservedInstancesDiscount": float,
        "otherDiscount": float,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "restartNeeded": bool,
        "rollbackPossible": bool,
        "implementationEfforts": List[ImplementationEffortType],
        "accountIds": List[str],
        "regions": List[str],
        "resourceTypes": List[ResourceTypeType],
        "actionTypes": List[ActionTypeType],
        "tags": List["TagTypeDef"],
        "resourceIds": List[str],
        "resourceArns": List[str],
        "recommendationIds": List[str],
    },
    total=False,
)

GetPreferencesResponseTypeDef = TypedDict(
    "GetPreferencesResponseTypeDef",
    {
        "savingsEstimationMode": SavingsEstimationModeType,
        "memberAccountDiscountVisibility": MemberAccountDiscountVisibilityType,
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
        "recommendationId": str,
        "resourceId": str,
        "resourceArn": str,
        "accountId": str,
        "currencyCode": str,
        "recommendationLookbackPeriodInDays": int,
        "costCalculationLookbackPeriodInDays": int,
        "estimatedSavingsPercentage": float,
        "estimatedSavingsOverCostCalculationLookbackPeriod": float,
        "currentResourceType": ResourceTypeType,
        "recommendedResourceType": ResourceTypeType,
        "region": str,
        "source": SourceType,
        "lastRefreshTimestamp": datetime,
        "estimatedMonthlySavings": float,
        "estimatedMonthlyCost": float,
        "implementationEffort": ImplementationEffortType,
        "restartNeeded": bool,
        "actionType": ActionTypeType,
        "rollbackPossible": bool,
        "currentResourceDetails": "ResourceDetailsTypeDef",
        "recommendedResourceDetails": "ResourceDetailsTypeDef",
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
        "includeOrganizationInfo": bool,
        "accountId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListEnrollmentStatusesResponseTypeDef = TypedDict(
    "ListEnrollmentStatusesResponseTypeDef",
    {
        "items": List["AccountEnrollmentStatusTypeDef"],
        "includeMemberAccounts": bool,
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
        "estimatedTotalDedupedSavings": float,
        "items": List["RecommendationSummaryTypeDef"],
        "groupBy": str,
        "currencyCode": str,
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecommendationsRequestRequestTypeDef = TypedDict(
    "ListRecommendationsRequestRequestTypeDef",
    {
        "filter": "FilterTypeDef",
        "orderBy": "OrderByTypeDef",
        "includeAllRecommendations": bool,
        "maxResults": int,
        "nextToken": str,
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
        "service": str,
        "normalizedUnitsToPurchase": str,
        "term": str,
        "paymentOption": str,
        "numberOfInstancesToPurchase": str,
        "instanceType": str,
        "reservedInstancesRegion": str,
        "currentGeneration": str,
        "sizeFlexEligible": bool,
        "upfrontCost": str,
        "monthlyRecurringCost": str,
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

RdsDbInstanceConfigurationTypeDef = TypedDict(
    "RdsDbInstanceConfigurationTypeDef",
    {
        "instance": "DbInstanceConfigurationTypeDef",
    },
    total=False,
)

RdsDbInstanceStorageConfigurationTypeDef = TypedDict(
    "RdsDbInstanceStorageConfigurationTypeDef",
    {
        "storageType": str,
        "allocatedStorageInGb": float,
        "iops": float,
        "storageThroughput": float,
    },
    total=False,
)

RdsDbInstanceStorageTypeDef = TypedDict(
    "RdsDbInstanceStorageTypeDef",
    {
        "configuration": "RdsDbInstanceStorageConfigurationTypeDef",
        "costCalculation": "ResourceCostCalculationTypeDef",
    },
    total=False,
)

RdsDbInstanceTypeDef = TypedDict(
    "RdsDbInstanceTypeDef",
    {
        "configuration": "RdsDbInstanceConfigurationTypeDef",
        "costCalculation": "ResourceCostCalculationTypeDef",
    },
    total=False,
)

RdsReservedInstancesConfigurationTypeDef = TypedDict(
    "RdsReservedInstancesConfigurationTypeDef",
    {
        "accountScope": str,
        "service": str,
        "normalizedUnitsToPurchase": str,
        "term": str,
        "paymentOption": str,
        "numberOfInstancesToPurchase": str,
        "instanceFamily": str,
        "instanceType": str,
        "reservedInstancesRegion": str,
        "sizeFlexEligible": bool,
        "currentGeneration": str,
        "upfrontCost": str,
        "monthlyRecurringCost": str,
        "licenseModel": str,
        "databaseEdition": str,
        "databaseEngine": str,
        "deploymentOption": str,
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
        "group": str,
        "estimatedMonthlySavings": float,
        "recommendationCount": int,
    },
    total=False,
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "recommendationId": str,
        "accountId": str,
        "region": str,
        "resourceId": str,
        "resourceArn": str,
        "currentResourceType": str,
        "recommendedResourceType": str,
        "estimatedMonthlySavings": float,
        "estimatedSavingsPercentage": float,
        "estimatedMonthlyCost": float,
        "currencyCode": str,
        "implementationEffort": str,
        "restartNeeded": bool,
        "actionType": str,
        "rollbackPossible": bool,
        "currentResourceSummary": str,
        "recommendedResourceSummary": str,
        "lastRefreshTimestamp": datetime,
        "recommendationLookbackPeriodInDays": int,
        "source": SourceType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

RedshiftReservedInstancesConfigurationTypeDef = TypedDict(
    "RedshiftReservedInstancesConfigurationTypeDef",
    {
        "accountScope": str,
        "service": str,
        "normalizedUnitsToPurchase": str,
        "term": str,
        "paymentOption": str,
        "numberOfInstancesToPurchase": str,
        "instanceFamily": str,
        "instanceType": str,
        "reservedInstancesRegion": str,
        "sizeFlexEligible": bool,
        "currentGeneration": str,
        "upfrontCost": str,
        "monthlyRecurringCost": str,
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
        "estimatedOnDemandCost": float,
        "monthlyReservationEligibleCost": float,
        "savingsPercentage": float,
        "estimatedMonthlyAmortizedReservationCost": float,
    },
    total=False,
)

ResourceCostCalculationTypeDef = TypedDict(
    "ResourceCostCalculationTypeDef",
    {
        "usages": List["UsageTypeDef"],
        "pricing": "ResourcePricingTypeDef",
    },
    total=False,
)

ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "lambdaFunction": "LambdaFunctionTypeDef",
        "ecsService": "EcsServiceTypeDef",
        "ec2Instance": "Ec2InstanceTypeDef",
        "ebsVolume": "EbsVolumeTypeDef",
        "ec2AutoScalingGroup": "Ec2AutoScalingGroupTypeDef",
        "ec2ReservedInstances": "Ec2ReservedInstancesTypeDef",
        "rdsReservedInstances": "RdsReservedInstancesTypeDef",
        "elastiCacheReservedInstances": "ElastiCacheReservedInstancesTypeDef",
        "openSearchReservedInstances": "OpenSearchReservedInstancesTypeDef",
        "redshiftReservedInstances": "RedshiftReservedInstancesTypeDef",
        "ec2InstanceSavingsPlans": "Ec2InstanceSavingsPlansTypeDef",
        "computeSavingsPlans": "ComputeSavingsPlansTypeDef",
        "sageMakerSavingsPlans": "SageMakerSavingsPlansTypeDef",
        "rdsDbInstance": "RdsDbInstanceTypeDef",
        "rdsDbInstanceStorage": "RdsDbInstanceStorageTypeDef",
    },
    total=False,
)

ResourcePricingTypeDef = TypedDict(
    "ResourcePricingTypeDef",
    {
        "estimatedCostBeforeDiscounts": float,
        "estimatedNetUnusedAmortizedCommitments": float,
        "estimatedDiscounts": "EstimatedDiscountsTypeDef",
        "estimatedCostAfterDiscounts": float,
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
        "term": str,
        "paymentOption": str,
        "hourlyCommitment": str,
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
        "monthlySavingsPlansEligibleCost": float,
        "estimatedMonthlyCommitment": float,
        "savingsPercentage": float,
        "estimatedOnDemandCost": float,
    },
    total=False,
)

StorageConfigurationTypeDef = TypedDict(
    "StorageConfigurationTypeDef",
    {
        "type": str,
        "sizeInGb": float,
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
        "savingsEstimationMode": SavingsEstimationModeType,
        "memberAccountDiscountVisibility": MemberAccountDiscountVisibilityType,
    },
    total=False,
)

UpdatePreferencesResponseTypeDef = TypedDict(
    "UpdatePreferencesResponseTypeDef",
    {
        "savingsEstimationMode": SavingsEstimationModeType,
        "memberAccountDiscountVisibility": MemberAccountDiscountVisibilityType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsageTypeDef = TypedDict(
    "UsageTypeDef",
    {
        "usageType": str,
        "usageAmount": float,
        "operation": str,
        "productCode": str,
        "unit": str,
    },
    total=False,
)
