"""
Type annotations for cost-optimization-hub service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_cost_optimization_hub.type_defs import AccountEnrollmentStatusTypeDef

    data: AccountEnrollmentStatusTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    ActionTypeType,
    AllocationStrategyType,
    Ec2AutoScalingGroupTypeType,
    EnrollmentStatusType,
    ImplementationEffortType,
    MemberAccountDiscountVisibilityType,
    OrderType,
    ResourceTypeType,
    SavingsEstimationModeType,
    SourceType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccountEnrollmentStatusTypeDef",
    "BlockStoragePerformanceConfigurationTypeDef",
    "ComputeConfigurationTypeDef",
    "ComputeSavingsPlansConfigurationTypeDef",
    "ComputeSavingsPlansTypeDef",
    "DbInstanceConfigurationTypeDef",
    "DynamoDbReservedCapacityConfigurationTypeDef",
    "DynamoDbReservedCapacityTypeDef",
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
    "GetRecommendationRequestTypeDef",
    "GetRecommendationResponseTypeDef",
    "InstanceConfigurationTypeDef",
    "LambdaFunctionConfigurationTypeDef",
    "LambdaFunctionTypeDef",
    "ListEnrollmentStatusesRequestPaginateTypeDef",
    "ListEnrollmentStatusesRequestTypeDef",
    "ListEnrollmentStatusesResponseTypeDef",
    "ListRecommendationSummariesRequestPaginateTypeDef",
    "ListRecommendationSummariesRequestTypeDef",
    "ListRecommendationSummariesResponseTypeDef",
    "ListRecommendationsRequestPaginateTypeDef",
    "ListRecommendationsRequestTypeDef",
    "ListRecommendationsResponseTypeDef",
    "MemoryDbReservedInstancesConfigurationTypeDef",
    "MemoryDbReservedInstancesTypeDef",
    "MixedInstanceConfigurationTypeDef",
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
    "SummaryMetricsResultTypeDef",
    "TagTypeDef",
    "UpdateEnrollmentStatusRequestTypeDef",
    "UpdateEnrollmentStatusResponseTypeDef",
    "UpdatePreferencesRequestTypeDef",
    "UpdatePreferencesResponseTypeDef",
    "UsageTypeDef",
)

class AccountEnrollmentStatusTypeDef(TypedDict):
    accountId: NotRequired[str]
    status: NotRequired[EnrollmentStatusType]
    lastUpdatedTimestamp: NotRequired[datetime]
    createdTimestamp: NotRequired[datetime]

class BlockStoragePerformanceConfigurationTypeDef(TypedDict):
    iops: NotRequired[float]
    throughput: NotRequired[float]

class ComputeConfigurationTypeDef(TypedDict):
    vCpu: NotRequired[float]
    memorySizeInMB: NotRequired[int]
    architecture: NotRequired[str]
    platform: NotRequired[str]

class ComputeSavingsPlansConfigurationTypeDef(TypedDict):
    accountScope: NotRequired[str]
    term: NotRequired[str]
    paymentOption: NotRequired[str]
    hourlyCommitment: NotRequired[str]

class DbInstanceConfigurationTypeDef(TypedDict):
    dbInstanceClass: NotRequired[str]

class DynamoDbReservedCapacityConfigurationTypeDef(TypedDict):
    accountScope: NotRequired[str]
    service: NotRequired[str]
    term: NotRequired[str]
    paymentOption: NotRequired[str]
    reservedInstancesRegion: NotRequired[str]
    upfrontCost: NotRequired[str]
    monthlyRecurringCost: NotRequired[str]
    numberOfCapacityUnitsToPurchase: NotRequired[str]
    capacityUnits: NotRequired[str]

StorageConfigurationTypeDef = TypedDict(
    "StorageConfigurationTypeDef",
    {
        "type": NotRequired[str],
        "sizeInGb": NotRequired[float],
    },
)
InstanceConfigurationTypeDef = TypedDict(
    "InstanceConfigurationTypeDef",
    {
        "type": NotRequired[str],
    },
)
MixedInstanceConfigurationTypeDef = TypedDict(
    "MixedInstanceConfigurationTypeDef",
    {
        "type": NotRequired[str],
    },
)

class Ec2InstanceSavingsPlansConfigurationTypeDef(TypedDict):
    accountScope: NotRequired[str]
    term: NotRequired[str]
    paymentOption: NotRequired[str]
    hourlyCommitment: NotRequired[str]
    instanceFamily: NotRequired[str]
    savingsPlansRegion: NotRequired[str]

class Ec2ReservedInstancesConfigurationTypeDef(TypedDict):
    accountScope: NotRequired[str]
    service: NotRequired[str]
    term: NotRequired[str]
    paymentOption: NotRequired[str]
    reservedInstancesRegion: NotRequired[str]
    upfrontCost: NotRequired[str]
    monthlyRecurringCost: NotRequired[str]
    normalizedUnitsToPurchase: NotRequired[str]
    numberOfInstancesToPurchase: NotRequired[str]
    offeringClass: NotRequired[str]
    instanceFamily: NotRequired[str]
    instanceType: NotRequired[str]
    currentGeneration: NotRequired[str]
    platform: NotRequired[str]
    tenancy: NotRequired[str]
    sizeFlexEligible: NotRequired[bool]

class ElastiCacheReservedInstancesConfigurationTypeDef(TypedDict):
    accountScope: NotRequired[str]
    service: NotRequired[str]
    term: NotRequired[str]
    paymentOption: NotRequired[str]
    reservedInstancesRegion: NotRequired[str]
    upfrontCost: NotRequired[str]
    monthlyRecurringCost: NotRequired[str]
    normalizedUnitsToPurchase: NotRequired[str]
    numberOfInstancesToPurchase: NotRequired[str]
    instanceFamily: NotRequired[str]
    instanceType: NotRequired[str]
    currentGeneration: NotRequired[str]
    sizeFlexEligible: NotRequired[bool]

class EstimatedDiscountsTypeDef(TypedDict):
    savingsPlansDiscount: NotRequired[float]
    reservedInstancesDiscount: NotRequired[float]
    otherDiscount: NotRequired[float]

class TagTypeDef(TypedDict):
    key: NotRequired[str]
    value: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GetRecommendationRequestTypeDef(TypedDict):
    recommendationId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListEnrollmentStatusesRequestTypeDef(TypedDict):
    includeOrganizationInfo: NotRequired[bool]
    accountId: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class RecommendationSummaryTypeDef(TypedDict):
    group: NotRequired[str]
    estimatedMonthlySavings: NotRequired[float]
    recommendationCount: NotRequired[int]

class SummaryMetricsResultTypeDef(TypedDict):
    savingsPercentage: NotRequired[str]

class OrderByTypeDef(TypedDict):
    dimension: NotRequired[str]
    order: NotRequired[OrderType]

class MemoryDbReservedInstancesConfigurationTypeDef(TypedDict):
    accountScope: NotRequired[str]
    service: NotRequired[str]
    term: NotRequired[str]
    paymentOption: NotRequired[str]
    reservedInstancesRegion: NotRequired[str]
    upfrontCost: NotRequired[str]
    monthlyRecurringCost: NotRequired[str]
    normalizedUnitsToPurchase: NotRequired[str]
    numberOfInstancesToPurchase: NotRequired[str]
    instanceType: NotRequired[str]
    instanceFamily: NotRequired[str]
    sizeFlexEligible: NotRequired[bool]
    currentGeneration: NotRequired[str]

class OpenSearchReservedInstancesConfigurationTypeDef(TypedDict):
    accountScope: NotRequired[str]
    service: NotRequired[str]
    term: NotRequired[str]
    paymentOption: NotRequired[str]
    reservedInstancesRegion: NotRequired[str]
    upfrontCost: NotRequired[str]
    monthlyRecurringCost: NotRequired[str]
    normalizedUnitsToPurchase: NotRequired[str]
    numberOfInstancesToPurchase: NotRequired[str]
    instanceType: NotRequired[str]
    currentGeneration: NotRequired[str]
    sizeFlexEligible: NotRequired[bool]

class RdsDbInstanceStorageConfigurationTypeDef(TypedDict):
    storageType: NotRequired[str]
    allocatedStorageInGb: NotRequired[float]
    iops: NotRequired[float]
    storageThroughput: NotRequired[float]

class RdsReservedInstancesConfigurationTypeDef(TypedDict):
    accountScope: NotRequired[str]
    service: NotRequired[str]
    term: NotRequired[str]
    paymentOption: NotRequired[str]
    reservedInstancesRegion: NotRequired[str]
    upfrontCost: NotRequired[str]
    monthlyRecurringCost: NotRequired[str]
    normalizedUnitsToPurchase: NotRequired[str]
    numberOfInstancesToPurchase: NotRequired[str]
    instanceFamily: NotRequired[str]
    instanceType: NotRequired[str]
    sizeFlexEligible: NotRequired[bool]
    currentGeneration: NotRequired[str]
    licenseModel: NotRequired[str]
    databaseEdition: NotRequired[str]
    databaseEngine: NotRequired[str]
    deploymentOption: NotRequired[str]

class RedshiftReservedInstancesConfigurationTypeDef(TypedDict):
    accountScope: NotRequired[str]
    service: NotRequired[str]
    term: NotRequired[str]
    paymentOption: NotRequired[str]
    reservedInstancesRegion: NotRequired[str]
    upfrontCost: NotRequired[str]
    monthlyRecurringCost: NotRequired[str]
    normalizedUnitsToPurchase: NotRequired[str]
    numberOfInstancesToPurchase: NotRequired[str]
    instanceFamily: NotRequired[str]
    instanceType: NotRequired[str]
    sizeFlexEligible: NotRequired[bool]
    currentGeneration: NotRequired[str]

class ReservedInstancesPricingTypeDef(TypedDict):
    estimatedOnDemandCost: NotRequired[float]
    monthlyReservationEligibleCost: NotRequired[float]
    savingsPercentage: NotRequired[float]
    estimatedMonthlyAmortizedReservationCost: NotRequired[float]

class UsageTypeDef(TypedDict):
    usageType: NotRequired[str]
    usageAmount: NotRequired[float]
    operation: NotRequired[str]
    productCode: NotRequired[str]
    unit: NotRequired[str]

class SageMakerSavingsPlansConfigurationTypeDef(TypedDict):
    accountScope: NotRequired[str]
    term: NotRequired[str]
    paymentOption: NotRequired[str]
    hourlyCommitment: NotRequired[str]

class SavingsPlansPricingTypeDef(TypedDict):
    monthlySavingsPlansEligibleCost: NotRequired[float]
    estimatedMonthlyCommitment: NotRequired[float]
    savingsPercentage: NotRequired[float]
    estimatedOnDemandCost: NotRequired[float]

class UpdateEnrollmentStatusRequestTypeDef(TypedDict):
    status: EnrollmentStatusType
    includeMemberAccounts: NotRequired[bool]

class UpdatePreferencesRequestTypeDef(TypedDict):
    savingsEstimationMode: NotRequired[SavingsEstimationModeType]
    memberAccountDiscountVisibility: NotRequired[MemberAccountDiscountVisibilityType]

class EcsServiceConfigurationTypeDef(TypedDict):
    compute: NotRequired[ComputeConfigurationTypeDef]

class LambdaFunctionConfigurationTypeDef(TypedDict):
    compute: NotRequired[ComputeConfigurationTypeDef]

class RdsDbInstanceConfigurationTypeDef(TypedDict):
    instance: NotRequired[DbInstanceConfigurationTypeDef]

class EbsVolumeConfigurationTypeDef(TypedDict):
    storage: NotRequired[StorageConfigurationTypeDef]
    performance: NotRequired[BlockStoragePerformanceConfigurationTypeDef]
    attachmentState: NotRequired[str]

class Ec2InstanceConfigurationTypeDef(TypedDict):
    instance: NotRequired[InstanceConfigurationTypeDef]

Ec2AutoScalingGroupConfigurationTypeDef = TypedDict(
    "Ec2AutoScalingGroupConfigurationTypeDef",
    {
        "instance": NotRequired[InstanceConfigurationTypeDef],
        "mixedInstances": NotRequired[List[MixedInstanceConfigurationTypeDef]],
        "type": NotRequired[Ec2AutoScalingGroupTypeType],
        "allocationStrategy": NotRequired[AllocationStrategyType],
    },
)

class ResourcePricingTypeDef(TypedDict):
    estimatedCostBeforeDiscounts: NotRequired[float]
    estimatedNetUnusedAmortizedCommitments: NotRequired[float]
    estimatedDiscounts: NotRequired[EstimatedDiscountsTypeDef]
    estimatedCostAfterDiscounts: NotRequired[float]

class FilterTypeDef(TypedDict):
    restartNeeded: NotRequired[bool]
    rollbackPossible: NotRequired[bool]
    implementationEfforts: NotRequired[Sequence[ImplementationEffortType]]
    accountIds: NotRequired[Sequence[str]]
    regions: NotRequired[Sequence[str]]
    resourceTypes: NotRequired[Sequence[ResourceTypeType]]
    actionTypes: NotRequired[Sequence[ActionTypeType]]
    tags: NotRequired[Sequence[TagTypeDef]]
    resourceIds: NotRequired[Sequence[str]]
    resourceArns: NotRequired[Sequence[str]]
    recommendationIds: NotRequired[Sequence[str]]

class RecommendationTypeDef(TypedDict):
    recommendationId: NotRequired[str]
    accountId: NotRequired[str]
    region: NotRequired[str]
    resourceId: NotRequired[str]
    resourceArn: NotRequired[str]
    currentResourceType: NotRequired[str]
    recommendedResourceType: NotRequired[str]
    estimatedMonthlySavings: NotRequired[float]
    estimatedSavingsPercentage: NotRequired[float]
    estimatedMonthlyCost: NotRequired[float]
    currencyCode: NotRequired[str]
    implementationEffort: NotRequired[str]
    restartNeeded: NotRequired[bool]
    actionType: NotRequired[str]
    rollbackPossible: NotRequired[bool]
    currentResourceSummary: NotRequired[str]
    recommendedResourceSummary: NotRequired[str]
    lastRefreshTimestamp: NotRequired[datetime]
    recommendationLookbackPeriodInDays: NotRequired[int]
    source: NotRequired[SourceType]
    tags: NotRequired[List[TagTypeDef]]

class GetPreferencesResponseTypeDef(TypedDict):
    savingsEstimationMode: SavingsEstimationModeType
    memberAccountDiscountVisibility: MemberAccountDiscountVisibilityType
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnrollmentStatusesResponseTypeDef(TypedDict):
    items: List[AccountEnrollmentStatusTypeDef]
    includeMemberAccounts: bool
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateEnrollmentStatusResponseTypeDef(TypedDict):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePreferencesResponseTypeDef(TypedDict):
    savingsEstimationMode: SavingsEstimationModeType
    memberAccountDiscountVisibility: MemberAccountDiscountVisibilityType
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnrollmentStatusesRequestPaginateTypeDef(TypedDict):
    includeOrganizationInfo: NotRequired[bool]
    accountId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRecommendationSummariesResponseTypeDef(TypedDict):
    estimatedTotalDedupedSavings: float
    items: List[RecommendationSummaryTypeDef]
    groupBy: str
    currencyCode: str
    metrics: SummaryMetricsResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ReservedInstancesCostCalculationTypeDef(TypedDict):
    pricing: NotRequired[ReservedInstancesPricingTypeDef]

class SavingsPlansCostCalculationTypeDef(TypedDict):
    pricing: NotRequired[SavingsPlansPricingTypeDef]

class ResourceCostCalculationTypeDef(TypedDict):
    usages: NotRequired[List[UsageTypeDef]]
    pricing: NotRequired[ResourcePricingTypeDef]

ListRecommendationSummariesRequestPaginateTypeDef = TypedDict(
    "ListRecommendationSummariesRequestPaginateTypeDef",
    {
        "groupBy": str,
        "filter": NotRequired[FilterTypeDef],
        "metrics": NotRequired[Sequence[Literal["SavingsPercentage"]]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecommendationSummariesRequestTypeDef = TypedDict(
    "ListRecommendationSummariesRequestTypeDef",
    {
        "groupBy": str,
        "filter": NotRequired[FilterTypeDef],
        "maxResults": NotRequired[int],
        "metrics": NotRequired[Sequence[Literal["SavingsPercentage"]]],
        "nextToken": NotRequired[str],
    },
)
ListRecommendationsRequestPaginateTypeDef = TypedDict(
    "ListRecommendationsRequestPaginateTypeDef",
    {
        "filter": NotRequired[FilterTypeDef],
        "orderBy": NotRequired[OrderByTypeDef],
        "includeAllRecommendations": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecommendationsRequestTypeDef = TypedDict(
    "ListRecommendationsRequestTypeDef",
    {
        "filter": NotRequired[FilterTypeDef],
        "orderBy": NotRequired[OrderByTypeDef],
        "includeAllRecommendations": NotRequired[bool],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

class ListRecommendationsResponseTypeDef(TypedDict):
    items: List[RecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DynamoDbReservedCapacityTypeDef(TypedDict):
    configuration: NotRequired[DynamoDbReservedCapacityConfigurationTypeDef]
    costCalculation: NotRequired[ReservedInstancesCostCalculationTypeDef]

class Ec2ReservedInstancesTypeDef(TypedDict):
    configuration: NotRequired[Ec2ReservedInstancesConfigurationTypeDef]
    costCalculation: NotRequired[ReservedInstancesCostCalculationTypeDef]

class ElastiCacheReservedInstancesTypeDef(TypedDict):
    configuration: NotRequired[ElastiCacheReservedInstancesConfigurationTypeDef]
    costCalculation: NotRequired[ReservedInstancesCostCalculationTypeDef]

class MemoryDbReservedInstancesTypeDef(TypedDict):
    configuration: NotRequired[MemoryDbReservedInstancesConfigurationTypeDef]
    costCalculation: NotRequired[ReservedInstancesCostCalculationTypeDef]

class OpenSearchReservedInstancesTypeDef(TypedDict):
    configuration: NotRequired[OpenSearchReservedInstancesConfigurationTypeDef]
    costCalculation: NotRequired[ReservedInstancesCostCalculationTypeDef]

class RdsReservedInstancesTypeDef(TypedDict):
    configuration: NotRequired[RdsReservedInstancesConfigurationTypeDef]
    costCalculation: NotRequired[ReservedInstancesCostCalculationTypeDef]

class RedshiftReservedInstancesTypeDef(TypedDict):
    configuration: NotRequired[RedshiftReservedInstancesConfigurationTypeDef]
    costCalculation: NotRequired[ReservedInstancesCostCalculationTypeDef]

class ComputeSavingsPlansTypeDef(TypedDict):
    configuration: NotRequired[ComputeSavingsPlansConfigurationTypeDef]
    costCalculation: NotRequired[SavingsPlansCostCalculationTypeDef]

class Ec2InstanceSavingsPlansTypeDef(TypedDict):
    configuration: NotRequired[Ec2InstanceSavingsPlansConfigurationTypeDef]
    costCalculation: NotRequired[SavingsPlansCostCalculationTypeDef]

class SageMakerSavingsPlansTypeDef(TypedDict):
    configuration: NotRequired[SageMakerSavingsPlansConfigurationTypeDef]
    costCalculation: NotRequired[SavingsPlansCostCalculationTypeDef]

class EbsVolumeTypeDef(TypedDict):
    configuration: NotRequired[EbsVolumeConfigurationTypeDef]
    costCalculation: NotRequired[ResourceCostCalculationTypeDef]

class Ec2AutoScalingGroupTypeDef(TypedDict):
    configuration: NotRequired[Ec2AutoScalingGroupConfigurationTypeDef]
    costCalculation: NotRequired[ResourceCostCalculationTypeDef]

class Ec2InstanceTypeDef(TypedDict):
    configuration: NotRequired[Ec2InstanceConfigurationTypeDef]
    costCalculation: NotRequired[ResourceCostCalculationTypeDef]

class EcsServiceTypeDef(TypedDict):
    configuration: NotRequired[EcsServiceConfigurationTypeDef]
    costCalculation: NotRequired[ResourceCostCalculationTypeDef]

class LambdaFunctionTypeDef(TypedDict):
    configuration: NotRequired[LambdaFunctionConfigurationTypeDef]
    costCalculation: NotRequired[ResourceCostCalculationTypeDef]

class RdsDbInstanceStorageTypeDef(TypedDict):
    configuration: NotRequired[RdsDbInstanceStorageConfigurationTypeDef]
    costCalculation: NotRequired[ResourceCostCalculationTypeDef]

class RdsDbInstanceTypeDef(TypedDict):
    configuration: NotRequired[RdsDbInstanceConfigurationTypeDef]
    costCalculation: NotRequired[ResourceCostCalculationTypeDef]

class ResourceDetailsTypeDef(TypedDict):
    lambdaFunction: NotRequired[LambdaFunctionTypeDef]
    ecsService: NotRequired[EcsServiceTypeDef]
    ec2Instance: NotRequired[Ec2InstanceTypeDef]
    ebsVolume: NotRequired[EbsVolumeTypeDef]
    ec2AutoScalingGroup: NotRequired[Ec2AutoScalingGroupTypeDef]
    ec2ReservedInstances: NotRequired[Ec2ReservedInstancesTypeDef]
    rdsReservedInstances: NotRequired[RdsReservedInstancesTypeDef]
    elastiCacheReservedInstances: NotRequired[ElastiCacheReservedInstancesTypeDef]
    openSearchReservedInstances: NotRequired[OpenSearchReservedInstancesTypeDef]
    redshiftReservedInstances: NotRequired[RedshiftReservedInstancesTypeDef]
    ec2InstanceSavingsPlans: NotRequired[Ec2InstanceSavingsPlansTypeDef]
    computeSavingsPlans: NotRequired[ComputeSavingsPlansTypeDef]
    sageMakerSavingsPlans: NotRequired[SageMakerSavingsPlansTypeDef]
    rdsDbInstance: NotRequired[RdsDbInstanceTypeDef]
    rdsDbInstanceStorage: NotRequired[RdsDbInstanceStorageTypeDef]
    dynamoDbReservedCapacity: NotRequired[DynamoDbReservedCapacityTypeDef]
    memoryDbReservedInstances: NotRequired[MemoryDbReservedInstancesTypeDef]

class GetRecommendationResponseTypeDef(TypedDict):
    recommendationId: str
    resourceId: str
    resourceArn: str
    accountId: str
    currencyCode: str
    recommendationLookbackPeriodInDays: int
    costCalculationLookbackPeriodInDays: int
    estimatedSavingsPercentage: float
    estimatedSavingsOverCostCalculationLookbackPeriod: float
    currentResourceType: ResourceTypeType
    recommendedResourceType: ResourceTypeType
    region: str
    source: SourceType
    lastRefreshTimestamp: datetime
    estimatedMonthlySavings: float
    estimatedMonthlyCost: float
    implementationEffort: ImplementationEffortType
    restartNeeded: bool
    actionType: ActionTypeType
    rollbackPossible: bool
    currentResourceDetails: ResourceDetailsTypeDef
    recommendedResourceDetails: ResourceDetailsTypeDef
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
