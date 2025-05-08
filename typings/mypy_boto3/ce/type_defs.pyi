"""
Type annotations for ce service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_ce.type_defs import AnomalyDateIntervalTypeDef

    data: AnomalyDateIntervalTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Any, Union

from .literals import (
    AccountScopeType,
    AnalysisStatusType,
    AnalysisTypeType,
    AnomalyFeedbackTypeType,
    AnomalySubscriptionFrequencyType,
    ApproximationDimensionType,
    ContextType,
    CostAllocationTagBackfillStatusType,
    CostAllocationTagStatusType,
    CostAllocationTagTypeType,
    CostCategoryInheritedValueDimensionNameType,
    CostCategoryRuleTypeType,
    CostCategorySplitChargeMethodType,
    CostCategoryStatusType,
    DimensionType,
    ErrorCodeType,
    FindingReasonCodeType,
    GenerationStatusType,
    GranularityType,
    GroupDefinitionTypeType,
    LookbackPeriodInDaysType,
    MatchOptionType,
    MetricType,
    MonitorTypeType,
    NumericOperatorType,
    OfferingClassType,
    PaymentOptionType,
    PlatformDifferenceType,
    RecommendationTargetType,
    RightsizingTypeType,
    SavingsPlansDataTypeType,
    SortOrderType,
    SubscriberStatusType,
    SubscriberTypeType,
    SupportedSavingsPlansTypeType,
    TermInYearsType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AnalysisDetailsTypeDef",
    "AnalysisSummaryTypeDef",
    "AnomalyDateIntervalTypeDef",
    "AnomalyMonitorOutputTypeDef",
    "AnomalyMonitorPaginatorTypeDef",
    "AnomalyMonitorTypeDef",
    "AnomalyMonitorUnionTypeDef",
    "AnomalyScoreTypeDef",
    "AnomalySubscriptionOutputTypeDef",
    "AnomalySubscriptionPaginatorTypeDef",
    "AnomalySubscriptionTypeDef",
    "AnomalySubscriptionUnionTypeDef",
    "AnomalyTypeDef",
    "CommitmentPurchaseAnalysisConfigurationOutputTypeDef",
    "CommitmentPurchaseAnalysisConfigurationTypeDef",
    "CommitmentPurchaseAnalysisConfigurationUnionTypeDef",
    "CostAllocationTagBackfillRequestTypeDef",
    "CostAllocationTagStatusEntryTypeDef",
    "CostAllocationTagTypeDef",
    "CostCategoryInheritedValueDimensionTypeDef",
    "CostCategoryProcessingStatusTypeDef",
    "CostCategoryReferenceTypeDef",
    "CostCategoryRuleOutputTypeDef",
    "CostCategoryRuleTypeDef",
    "CostCategoryRuleUnionTypeDef",
    "CostCategorySplitChargeRuleOutputTypeDef",
    "CostCategorySplitChargeRuleParameterOutputTypeDef",
    "CostCategorySplitChargeRuleParameterTypeDef",
    "CostCategorySplitChargeRuleParameterUnionTypeDef",
    "CostCategorySplitChargeRuleTypeDef",
    "CostCategorySplitChargeRuleUnionTypeDef",
    "CostCategoryTypeDef",
    "CostCategoryValuesOutputTypeDef",
    "CostCategoryValuesTypeDef",
    "CostCategoryValuesUnionTypeDef",
    "CoverageByTimeTypeDef",
    "CoverageCostTypeDef",
    "CoverageHoursTypeDef",
    "CoverageNormalizedUnitsTypeDef",
    "CoverageTypeDef",
    "CreateAnomalyMonitorRequestTypeDef",
    "CreateAnomalyMonitorResponseTypeDef",
    "CreateAnomalySubscriptionRequestTypeDef",
    "CreateAnomalySubscriptionResponseTypeDef",
    "CreateCostCategoryDefinitionRequestTypeDef",
    "CreateCostCategoryDefinitionResponseTypeDef",
    "CurrentInstanceTypeDef",
    "DateIntervalTypeDef",
    "DeleteAnomalyMonitorRequestTypeDef",
    "DeleteAnomalySubscriptionRequestTypeDef",
    "DeleteCostCategoryDefinitionRequestTypeDef",
    "DeleteCostCategoryDefinitionResponseTypeDef",
    "DescribeCostCategoryDefinitionRequestTypeDef",
    "DescribeCostCategoryDefinitionResponseTypeDef",
    "DimensionValuesOutputTypeDef",
    "DimensionValuesTypeDef",
    "DimensionValuesUnionTypeDef",
    "DimensionValuesWithAttributesTypeDef",
    "DiskResourceUtilizationTypeDef",
    "DynamoDBCapacityDetailsTypeDef",
    "EBSResourceUtilizationTypeDef",
    "EC2InstanceDetailsTypeDef",
    "EC2ResourceDetailsTypeDef",
    "EC2ResourceUtilizationTypeDef",
    "EC2SpecificationTypeDef",
    "ESInstanceDetailsTypeDef",
    "ElastiCacheInstanceDetailsTypeDef",
    "ExpressionOutputTypeDef",
    "ExpressionPaginatorTypeDef",
    "ExpressionTypeDef",
    "ExpressionUnionTypeDef",
    "ForecastResultTypeDef",
    "GenerationSummaryTypeDef",
    "GetAnomaliesRequestPaginateTypeDef",
    "GetAnomaliesRequestTypeDef",
    "GetAnomaliesResponseTypeDef",
    "GetAnomalyMonitorsRequestPaginateTypeDef",
    "GetAnomalyMonitorsRequestTypeDef",
    "GetAnomalyMonitorsResponsePaginatorTypeDef",
    "GetAnomalyMonitorsResponseTypeDef",
    "GetAnomalySubscriptionsRequestPaginateTypeDef",
    "GetAnomalySubscriptionsRequestTypeDef",
    "GetAnomalySubscriptionsResponsePaginatorTypeDef",
    "GetAnomalySubscriptionsResponseTypeDef",
    "GetApproximateUsageRecordsRequestTypeDef",
    "GetApproximateUsageRecordsResponseTypeDef",
    "GetCommitmentPurchaseAnalysisRequestTypeDef",
    "GetCommitmentPurchaseAnalysisResponseTypeDef",
    "GetCostAndUsageRequestTypeDef",
    "GetCostAndUsageResponseTypeDef",
    "GetCostAndUsageWithResourcesRequestTypeDef",
    "GetCostAndUsageWithResourcesResponseTypeDef",
    "GetCostCategoriesRequestTypeDef",
    "GetCostCategoriesResponseTypeDef",
    "GetCostForecastRequestTypeDef",
    "GetCostForecastResponseTypeDef",
    "GetDimensionValuesRequestTypeDef",
    "GetDimensionValuesResponseTypeDef",
    "GetReservationCoverageRequestTypeDef",
    "GetReservationCoverageResponseTypeDef",
    "GetReservationPurchaseRecommendationRequestTypeDef",
    "GetReservationPurchaseRecommendationResponseTypeDef",
    "GetReservationUtilizationRequestTypeDef",
    "GetReservationUtilizationResponseTypeDef",
    "GetRightsizingRecommendationRequestTypeDef",
    "GetRightsizingRecommendationResponseTypeDef",
    "GetSavingsPlanPurchaseRecommendationDetailsRequestTypeDef",
    "GetSavingsPlanPurchaseRecommendationDetailsResponseTypeDef",
    "GetSavingsPlansCoverageRequestTypeDef",
    "GetSavingsPlansCoverageResponseTypeDef",
    "GetSavingsPlansPurchaseRecommendationRequestTypeDef",
    "GetSavingsPlansPurchaseRecommendationResponseTypeDef",
    "GetSavingsPlansUtilizationDetailsRequestTypeDef",
    "GetSavingsPlansUtilizationDetailsResponseTypeDef",
    "GetSavingsPlansUtilizationRequestTypeDef",
    "GetSavingsPlansUtilizationResponseTypeDef",
    "GetTagsRequestTypeDef",
    "GetTagsResponseTypeDef",
    "GetUsageForecastRequestTypeDef",
    "GetUsageForecastResponseTypeDef",
    "GroupDefinitionTypeDef",
    "GroupTypeDef",
    "ImpactTypeDef",
    "InstanceDetailsTypeDef",
    "ListCommitmentPurchaseAnalysesRequestTypeDef",
    "ListCommitmentPurchaseAnalysesResponseTypeDef",
    "ListCostAllocationTagBackfillHistoryRequestTypeDef",
    "ListCostAllocationTagBackfillHistoryResponseTypeDef",
    "ListCostAllocationTagsRequestTypeDef",
    "ListCostAllocationTagsResponseTypeDef",
    "ListCostCategoryDefinitionsRequestTypeDef",
    "ListCostCategoryDefinitionsResponseTypeDef",
    "ListSavingsPlansPurchaseRecommendationGenerationRequestTypeDef",
    "ListSavingsPlansPurchaseRecommendationGenerationResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MemoryDBInstanceDetailsTypeDef",
    "MetricValueTypeDef",
    "ModifyRecommendationDetailTypeDef",
    "NetworkResourceUtilizationTypeDef",
    "PaginatorConfigTypeDef",
    "ProvideAnomalyFeedbackRequestTypeDef",
    "ProvideAnomalyFeedbackResponseTypeDef",
    "RDSInstanceDetailsTypeDef",
    "RecommendationDetailDataTypeDef",
    "RecommendationDetailHourlyMetricsTypeDef",
    "RedshiftInstanceDetailsTypeDef",
    "ReservationAggregatesTypeDef",
    "ReservationCoverageGroupTypeDef",
    "ReservationPurchaseRecommendationDetailTypeDef",
    "ReservationPurchaseRecommendationMetadataTypeDef",
    "ReservationPurchaseRecommendationSummaryTypeDef",
    "ReservationPurchaseRecommendationTypeDef",
    "ReservationUtilizationGroupTypeDef",
    "ReservedCapacityDetailsTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceTagTypeDef",
    "ResourceUtilizationTypeDef",
    "ResponseMetadataTypeDef",
    "ResultByTimeTypeDef",
    "RightsizingRecommendationConfigurationTypeDef",
    "RightsizingRecommendationMetadataTypeDef",
    "RightsizingRecommendationSummaryTypeDef",
    "RightsizingRecommendationTypeDef",
    "RootCauseImpactTypeDef",
    "RootCauseTypeDef",
    "SavingsPlansAmortizedCommitmentTypeDef",
    "SavingsPlansCoverageDataTypeDef",
    "SavingsPlansCoverageTypeDef",
    "SavingsPlansDetailsTypeDef",
    "SavingsPlansPurchaseAnalysisConfigurationOutputTypeDef",
    "SavingsPlansPurchaseAnalysisConfigurationTypeDef",
    "SavingsPlansPurchaseAnalysisDetailsTypeDef",
    "SavingsPlansPurchaseRecommendationDetailTypeDef",
    "SavingsPlansPurchaseRecommendationMetadataTypeDef",
    "SavingsPlansPurchaseRecommendationSummaryTypeDef",
    "SavingsPlansPurchaseRecommendationTypeDef",
    "SavingsPlansSavingsTypeDef",
    "SavingsPlansTypeDef",
    "SavingsPlansUtilizationAggregatesTypeDef",
    "SavingsPlansUtilizationByTimeTypeDef",
    "SavingsPlansUtilizationDetailTypeDef",
    "SavingsPlansUtilizationTypeDef",
    "ServiceSpecificationTypeDef",
    "SortDefinitionTypeDef",
    "StartCommitmentPurchaseAnalysisRequestTypeDef",
    "StartCommitmentPurchaseAnalysisResponseTypeDef",
    "StartCostAllocationTagBackfillRequestTypeDef",
    "StartCostAllocationTagBackfillResponseTypeDef",
    "StartSavingsPlansPurchaseRecommendationGenerationResponseTypeDef",
    "SubscriberTypeDef",
    "TagResourceRequestTypeDef",
    "TagValuesOutputTypeDef",
    "TagValuesTypeDef",
    "TagValuesUnionTypeDef",
    "TargetInstanceTypeDef",
    "TerminateRecommendationDetailTypeDef",
    "TotalImpactFilterTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAnomalyMonitorRequestTypeDef",
    "UpdateAnomalyMonitorResponseTypeDef",
    "UpdateAnomalySubscriptionRequestTypeDef",
    "UpdateAnomalySubscriptionResponseTypeDef",
    "UpdateCostAllocationTagsStatusErrorTypeDef",
    "UpdateCostAllocationTagsStatusRequestTypeDef",
    "UpdateCostAllocationTagsStatusResponseTypeDef",
    "UpdateCostCategoryDefinitionRequestTypeDef",
    "UpdateCostCategoryDefinitionResponseTypeDef",
    "UtilizationByTimeTypeDef",
)

class AnomalyDateIntervalTypeDef(TypedDict):
    StartDate: str
    EndDate: NotRequired[str]

class AnomalyScoreTypeDef(TypedDict):
    MaxScore: float
    CurrentScore: float

SubscriberTypeDef = TypedDict(
    "SubscriberTypeDef",
    {
        "Address": NotRequired[str],
        "Type": NotRequired[SubscriberTypeType],
        "Status": NotRequired[SubscriberStatusType],
    },
)

class ImpactTypeDef(TypedDict):
    MaxImpact: float
    TotalImpact: NotRequired[float]
    TotalActualSpend: NotRequired[float]
    TotalExpectedSpend: NotRequired[float]
    TotalImpactPercentage: NotRequired[float]

class CostAllocationTagBackfillRequestTypeDef(TypedDict):
    BackfillFrom: NotRequired[str]
    RequestedAt: NotRequired[str]
    CompletedAt: NotRequired[str]
    BackfillStatus: NotRequired[CostAllocationTagBackfillStatusType]
    LastUpdatedAt: NotRequired[str]

class CostAllocationTagStatusEntryTypeDef(TypedDict):
    TagKey: str
    Status: CostAllocationTagStatusType

CostAllocationTagTypeDef = TypedDict(
    "CostAllocationTagTypeDef",
    {
        "TagKey": str,
        "Type": CostAllocationTagTypeType,
        "Status": CostAllocationTagStatusType,
        "LastUpdatedDate": NotRequired[str],
        "LastUsedDate": NotRequired[str],
    },
)

class CostCategoryInheritedValueDimensionTypeDef(TypedDict):
    DimensionName: NotRequired[CostCategoryInheritedValueDimensionNameType]
    DimensionKey: NotRequired[str]

class CostCategoryProcessingStatusTypeDef(TypedDict):
    Component: NotRequired[Literal["COST_EXPLORER"]]
    Status: NotRequired[CostCategoryStatusType]

CostCategorySplitChargeRuleParameterOutputTypeDef = TypedDict(
    "CostCategorySplitChargeRuleParameterOutputTypeDef",
    {
        "Type": Literal["ALLOCATION_PERCENTAGES"],
        "Values": List[str],
    },
)
CostCategorySplitChargeRuleParameterTypeDef = TypedDict(
    "CostCategorySplitChargeRuleParameterTypeDef",
    {
        "Type": Literal["ALLOCATION_PERCENTAGES"],
        "Values": Sequence[str],
    },
)

class CostCategoryValuesOutputTypeDef(TypedDict):
    Key: NotRequired[str]
    Values: NotRequired[List[str]]
    MatchOptions: NotRequired[List[MatchOptionType]]

class CostCategoryValuesTypeDef(TypedDict):
    Key: NotRequired[str]
    Values: NotRequired[Sequence[str]]
    MatchOptions: NotRequired[Sequence[MatchOptionType]]

class DateIntervalTypeDef(TypedDict):
    Start: str
    End: str

class CoverageCostTypeDef(TypedDict):
    OnDemandCost: NotRequired[str]

class CoverageHoursTypeDef(TypedDict):
    OnDemandHours: NotRequired[str]
    ReservedHours: NotRequired[str]
    TotalRunningHours: NotRequired[str]
    CoverageHoursPercentage: NotRequired[str]

class CoverageNormalizedUnitsTypeDef(TypedDict):
    OnDemandNormalizedUnits: NotRequired[str]
    ReservedNormalizedUnits: NotRequired[str]
    TotalRunningNormalizedUnits: NotRequired[str]
    CoverageNormalizedUnitsPercentage: NotRequired[str]

class ResourceTagTypeDef(TypedDict):
    Key: str
    Value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class TagValuesOutputTypeDef(TypedDict):
    Key: NotRequired[str]
    Values: NotRequired[List[str]]
    MatchOptions: NotRequired[List[MatchOptionType]]

class DeleteAnomalyMonitorRequestTypeDef(TypedDict):
    MonitorArn: str

class DeleteAnomalySubscriptionRequestTypeDef(TypedDict):
    SubscriptionArn: str

class DeleteCostCategoryDefinitionRequestTypeDef(TypedDict):
    CostCategoryArn: str

class DescribeCostCategoryDefinitionRequestTypeDef(TypedDict):
    CostCategoryArn: str
    EffectiveOn: NotRequired[str]

class DimensionValuesOutputTypeDef(TypedDict):
    Key: NotRequired[DimensionType]
    Values: NotRequired[List[str]]
    MatchOptions: NotRequired[List[MatchOptionType]]

class DimensionValuesTypeDef(TypedDict):
    Key: NotRequired[DimensionType]
    Values: NotRequired[Sequence[str]]
    MatchOptions: NotRequired[Sequence[MatchOptionType]]

class DimensionValuesWithAttributesTypeDef(TypedDict):
    Value: NotRequired[str]
    Attributes: NotRequired[Dict[str, str]]

class DiskResourceUtilizationTypeDef(TypedDict):
    DiskReadOpsPerSecond: NotRequired[str]
    DiskWriteOpsPerSecond: NotRequired[str]
    DiskReadBytesPerSecond: NotRequired[str]
    DiskWriteBytesPerSecond: NotRequired[str]

class DynamoDBCapacityDetailsTypeDef(TypedDict):
    CapacityUnits: NotRequired[str]
    Region: NotRequired[str]

class EBSResourceUtilizationTypeDef(TypedDict):
    EbsReadOpsPerSecond: NotRequired[str]
    EbsWriteOpsPerSecond: NotRequired[str]
    EbsReadBytesPerSecond: NotRequired[str]
    EbsWriteBytesPerSecond: NotRequired[str]

class EC2InstanceDetailsTypeDef(TypedDict):
    Family: NotRequired[str]
    InstanceType: NotRequired[str]
    Region: NotRequired[str]
    AvailabilityZone: NotRequired[str]
    Platform: NotRequired[str]
    Tenancy: NotRequired[str]
    CurrentGeneration: NotRequired[bool]
    SizeFlexEligible: NotRequired[bool]

class EC2ResourceDetailsTypeDef(TypedDict):
    HourlyOnDemandRate: NotRequired[str]
    InstanceType: NotRequired[str]
    Platform: NotRequired[str]
    Region: NotRequired[str]
    Sku: NotRequired[str]
    Memory: NotRequired[str]
    NetworkPerformance: NotRequired[str]
    Storage: NotRequired[str]
    Vcpu: NotRequired[str]

class NetworkResourceUtilizationTypeDef(TypedDict):
    NetworkInBytesPerSecond: NotRequired[str]
    NetworkOutBytesPerSecond: NotRequired[str]
    NetworkPacketsInPerSecond: NotRequired[str]
    NetworkPacketsOutPerSecond: NotRequired[str]

class EC2SpecificationTypeDef(TypedDict):
    OfferingClass: NotRequired[OfferingClassType]

class ESInstanceDetailsTypeDef(TypedDict):
    InstanceClass: NotRequired[str]
    InstanceSize: NotRequired[str]
    Region: NotRequired[str]
    CurrentGeneration: NotRequired[bool]
    SizeFlexEligible: NotRequired[bool]

class ElastiCacheInstanceDetailsTypeDef(TypedDict):
    Family: NotRequired[str]
    NodeType: NotRequired[str]
    Region: NotRequired[str]
    ProductDescription: NotRequired[str]
    CurrentGeneration: NotRequired[bool]
    SizeFlexEligible: NotRequired[bool]

class GenerationSummaryTypeDef(TypedDict):
    RecommendationId: NotRequired[str]
    GenerationStatus: NotRequired[GenerationStatusType]
    GenerationStartedTime: NotRequired[str]
    GenerationCompletionTime: NotRequired[str]
    EstimatedCompletionTime: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class TotalImpactFilterTypeDef(TypedDict):
    NumericOperator: NumericOperatorType
    StartValue: float
    EndValue: NotRequired[float]

class GetAnomalyMonitorsRequestTypeDef(TypedDict):
    MonitorArnList: NotRequired[Sequence[str]]
    NextPageToken: NotRequired[str]
    MaxResults: NotRequired[int]

class GetAnomalySubscriptionsRequestTypeDef(TypedDict):
    SubscriptionArnList: NotRequired[Sequence[str]]
    MonitorArn: NotRequired[str]
    NextPageToken: NotRequired[str]
    MaxResults: NotRequired[int]

class GetApproximateUsageRecordsRequestTypeDef(TypedDict):
    Granularity: GranularityType
    ApproximationDimension: ApproximationDimensionType
    Services: NotRequired[Sequence[str]]

class GetCommitmentPurchaseAnalysisRequestTypeDef(TypedDict):
    AnalysisId: str

GroupDefinitionTypeDef = TypedDict(
    "GroupDefinitionTypeDef",
    {
        "Type": NotRequired[GroupDefinitionTypeType],
        "Key": NotRequired[str],
    },
)

class SortDefinitionTypeDef(TypedDict):
    Key: str
    SortOrder: NotRequired[SortOrderType]

class MetricValueTypeDef(TypedDict):
    Amount: NotRequired[str]
    Unit: NotRequired[str]

class ReservationPurchaseRecommendationMetadataTypeDef(TypedDict):
    RecommendationId: NotRequired[str]
    GenerationTimestamp: NotRequired[str]
    AdditionalMetadata: NotRequired[str]

class ReservationAggregatesTypeDef(TypedDict):
    UtilizationPercentage: NotRequired[str]
    UtilizationPercentageInUnits: NotRequired[str]
    PurchasedHours: NotRequired[str]
    PurchasedUnits: NotRequired[str]
    TotalActualHours: NotRequired[str]
    TotalActualUnits: NotRequired[str]
    UnusedHours: NotRequired[str]
    UnusedUnits: NotRequired[str]
    OnDemandCostOfRIHoursUsed: NotRequired[str]
    NetRISavings: NotRequired[str]
    TotalPotentialRISavings: NotRequired[str]
    AmortizedUpfrontFee: NotRequired[str]
    AmortizedRecurringFee: NotRequired[str]
    TotalAmortizedFee: NotRequired[str]
    RICostForUnusedHours: NotRequired[str]
    RealizedSavings: NotRequired[str]
    UnrealizedSavings: NotRequired[str]

class RightsizingRecommendationConfigurationTypeDef(TypedDict):
    RecommendationTarget: RecommendationTargetType
    BenefitsConsidered: bool

class RightsizingRecommendationMetadataTypeDef(TypedDict):
    RecommendationId: NotRequired[str]
    GenerationTimestamp: NotRequired[str]
    LookbackPeriodInDays: NotRequired[LookbackPeriodInDaysType]
    AdditionalMetadata: NotRequired[str]

class RightsizingRecommendationSummaryTypeDef(TypedDict):
    TotalRecommendationCount: NotRequired[str]
    EstimatedTotalMonthlySavingsAmount: NotRequired[str]
    SavingsCurrencyCode: NotRequired[str]
    SavingsPercentage: NotRequired[str]

class GetSavingsPlanPurchaseRecommendationDetailsRequestTypeDef(TypedDict):
    RecommendationDetailId: str

class SavingsPlansPurchaseRecommendationMetadataTypeDef(TypedDict):
    RecommendationId: NotRequired[str]
    GenerationTimestamp: NotRequired[str]
    AdditionalMetadata: NotRequired[str]

class MemoryDBInstanceDetailsTypeDef(TypedDict):
    Family: NotRequired[str]
    NodeType: NotRequired[str]
    Region: NotRequired[str]
    CurrentGeneration: NotRequired[bool]
    SizeFlexEligible: NotRequired[bool]

class RDSInstanceDetailsTypeDef(TypedDict):
    Family: NotRequired[str]
    InstanceType: NotRequired[str]
    Region: NotRequired[str]
    DatabaseEngine: NotRequired[str]
    DatabaseEdition: NotRequired[str]
    DeploymentOption: NotRequired[str]
    LicenseModel: NotRequired[str]
    CurrentGeneration: NotRequired[bool]
    SizeFlexEligible: NotRequired[bool]

class RedshiftInstanceDetailsTypeDef(TypedDict):
    Family: NotRequired[str]
    NodeType: NotRequired[str]
    Region: NotRequired[str]
    CurrentGeneration: NotRequired[bool]
    SizeFlexEligible: NotRequired[bool]

class ListCommitmentPurchaseAnalysesRequestTypeDef(TypedDict):
    AnalysisStatus: NotRequired[AnalysisStatusType]
    NextPageToken: NotRequired[str]
    PageSize: NotRequired[int]
    AnalysisIds: NotRequired[Sequence[str]]

class ListCostAllocationTagBackfillHistoryRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

ListCostAllocationTagsRequestTypeDef = TypedDict(
    "ListCostAllocationTagsRequestTypeDef",
    {
        "Status": NotRequired[CostAllocationTagStatusType],
        "TagKeys": NotRequired[Sequence[str]],
        "Type": NotRequired[CostAllocationTagTypeType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

class ListCostCategoryDefinitionsRequestTypeDef(TypedDict):
    EffectiveOn: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListSavingsPlansPurchaseRecommendationGenerationRequestTypeDef(TypedDict):
    GenerationStatus: NotRequired[GenerationStatusType]
    RecommendationIds: NotRequired[Sequence[str]]
    PageSize: NotRequired[int]
    NextPageToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class ProvideAnomalyFeedbackRequestTypeDef(TypedDict):
    AnomalyId: str
    Feedback: AnomalyFeedbackTypeType

class RecommendationDetailHourlyMetricsTypeDef(TypedDict):
    StartTime: NotRequired[str]
    EstimatedOnDemandCost: NotRequired[str]
    CurrentCoverage: NotRequired[str]
    EstimatedCoverage: NotRequired[str]
    EstimatedNewCommitmentUtilization: NotRequired[str]

class ReservationPurchaseRecommendationSummaryTypeDef(TypedDict):
    TotalEstimatedMonthlySavingsAmount: NotRequired[str]
    TotalEstimatedMonthlySavingsPercentage: NotRequired[str]
    CurrencyCode: NotRequired[str]

class TerminateRecommendationDetailTypeDef(TypedDict):
    EstimatedMonthlySavings: NotRequired[str]
    CurrencyCode: NotRequired[str]

class RootCauseImpactTypeDef(TypedDict):
    Contribution: float

class SavingsPlansAmortizedCommitmentTypeDef(TypedDict):
    AmortizedRecurringCommitment: NotRequired[str]
    AmortizedUpfrontCommitment: NotRequired[str]
    TotalAmortizedCommitment: NotRequired[str]

class SavingsPlansCoverageDataTypeDef(TypedDict):
    SpendCoveredBySavingsPlans: NotRequired[str]
    OnDemandCost: NotRequired[str]
    TotalCost: NotRequired[str]
    CoveragePercentage: NotRequired[str]

class SavingsPlansDetailsTypeDef(TypedDict):
    Region: NotRequired[str]
    InstanceFamily: NotRequired[str]
    OfferingId: NotRequired[str]

class SavingsPlansTypeDef(TypedDict):
    PaymentOption: NotRequired[PaymentOptionType]
    SavingsPlansType: NotRequired[SupportedSavingsPlansTypeType]
    Region: NotRequired[str]
    InstanceFamily: NotRequired[str]
    TermInYears: NotRequired[TermInYearsType]
    SavingsPlansCommitment: NotRequired[float]
    OfferingId: NotRequired[str]

class SavingsPlansPurchaseRecommendationSummaryTypeDef(TypedDict):
    EstimatedROI: NotRequired[str]
    CurrencyCode: NotRequired[str]
    EstimatedTotalCost: NotRequired[str]
    CurrentOnDemandSpend: NotRequired[str]
    EstimatedSavingsAmount: NotRequired[str]
    TotalRecommendationCount: NotRequired[str]
    DailyCommitmentToPurchase: NotRequired[str]
    HourlyCommitmentToPurchase: NotRequired[str]
    EstimatedSavingsPercentage: NotRequired[str]
    EstimatedMonthlySavingsAmount: NotRequired[str]
    EstimatedOnDemandCostWithCurrentCommitment: NotRequired[str]

class SavingsPlansSavingsTypeDef(TypedDict):
    NetSavings: NotRequired[str]
    OnDemandCostEquivalent: NotRequired[str]

class SavingsPlansUtilizationTypeDef(TypedDict):
    TotalCommitment: NotRequired[str]
    UsedCommitment: NotRequired[str]
    UnusedCommitment: NotRequired[str]
    UtilizationPercentage: NotRequired[str]

class StartCostAllocationTagBackfillRequestTypeDef(TypedDict):
    BackfillFrom: str

class TagValuesTypeDef(TypedDict):
    Key: NotRequired[str]
    Values: NotRequired[Sequence[str]]
    MatchOptions: NotRequired[Sequence[MatchOptionType]]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    ResourceTagKeys: Sequence[str]

class UpdateAnomalyMonitorRequestTypeDef(TypedDict):
    MonitorArn: str
    MonitorName: NotRequired[str]

class UpdateCostAllocationTagsStatusErrorTypeDef(TypedDict):
    TagKey: NotRequired[str]
    Code: NotRequired[str]
    Message: NotRequired[str]

class UpdateCostAllocationTagsStatusRequestTypeDef(TypedDict):
    CostAllocationTagsStatus: Sequence[CostAllocationTagStatusEntryTypeDef]

class CostCategoryReferenceTypeDef(TypedDict):
    CostCategoryArn: NotRequired[str]
    Name: NotRequired[str]
    EffectiveStart: NotRequired[str]
    EffectiveEnd: NotRequired[str]
    NumberOfRules: NotRequired[int]
    ProcessingStatus: NotRequired[List[CostCategoryProcessingStatusTypeDef]]
    Values: NotRequired[List[str]]
    DefaultValue: NotRequired[str]

class CostCategorySplitChargeRuleOutputTypeDef(TypedDict):
    Source: str
    Targets: List[str]
    Method: CostCategorySplitChargeMethodType
    Parameters: NotRequired[List[CostCategorySplitChargeRuleParameterOutputTypeDef]]

CostCategorySplitChargeRuleParameterUnionTypeDef = Union[
    CostCategorySplitChargeRuleParameterTypeDef, CostCategorySplitChargeRuleParameterOutputTypeDef
]
CostCategoryValuesUnionTypeDef = Union[CostCategoryValuesTypeDef, CostCategoryValuesOutputTypeDef]

class ForecastResultTypeDef(TypedDict):
    TimePeriod: NotRequired[DateIntervalTypeDef]
    MeanValue: NotRequired[str]
    PredictionIntervalLowerBound: NotRequired[str]
    PredictionIntervalUpperBound: NotRequired[str]

class CoverageTypeDef(TypedDict):
    CoverageHours: NotRequired[CoverageHoursTypeDef]
    CoverageNormalizedUnits: NotRequired[CoverageNormalizedUnitsTypeDef]
    CoverageCost: NotRequired[CoverageCostTypeDef]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    ResourceTags: Sequence[ResourceTagTypeDef]

class CreateAnomalyMonitorResponseTypeDef(TypedDict):
    MonitorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAnomalySubscriptionResponseTypeDef(TypedDict):
    SubscriptionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCostCategoryDefinitionResponseTypeDef(TypedDict):
    CostCategoryArn: str
    EffectiveStart: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCostCategoryDefinitionResponseTypeDef(TypedDict):
    CostCategoryArn: str
    EffectiveEnd: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetApproximateUsageRecordsResponseTypeDef(TypedDict):
    Services: Dict[str, int]
    TotalRecords: int
    LookbackPeriod: DateIntervalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCostCategoriesResponseTypeDef(TypedDict):
    NextPageToken: str
    CostCategoryNames: List[str]
    CostCategoryValues: List[str]
    ReturnSize: int
    TotalSize: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetTagsResponseTypeDef(TypedDict):
    NextPageToken: str
    Tags: List[str]
    ReturnSize: int
    TotalSize: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListCostAllocationTagBackfillHistoryResponseTypeDef(TypedDict):
    BackfillRequests: List[CostAllocationTagBackfillRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListCostAllocationTagsResponseTypeDef(TypedDict):
    CostAllocationTags: List[CostAllocationTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    ResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ProvideAnomalyFeedbackResponseTypeDef(TypedDict):
    AnomalyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartCommitmentPurchaseAnalysisResponseTypeDef(TypedDict):
    AnalysisId: str
    AnalysisStartedTime: str
    EstimatedCompletionTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartCostAllocationTagBackfillResponseTypeDef(TypedDict):
    BackfillRequest: CostAllocationTagBackfillRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartSavingsPlansPurchaseRecommendationGenerationResponseTypeDef(TypedDict):
    RecommendationId: str
    GenerationStartedTime: str
    EstimatedCompletionTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAnomalyMonitorResponseTypeDef(TypedDict):
    MonitorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAnomalySubscriptionResponseTypeDef(TypedDict):
    SubscriptionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCostCategoryDefinitionResponseTypeDef(TypedDict):
    CostCategoryArn: str
    EffectiveStart: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExpressionOutputTypeDef(TypedDict):
    Or: NotRequired[List[Dict[str, Any]]]
    And: NotRequired[List[Dict[str, Any]]]
    Not: NotRequired[Dict[str, Any]]
    Dimensions: NotRequired[DimensionValuesOutputTypeDef]
    Tags: NotRequired[TagValuesOutputTypeDef]
    CostCategories: NotRequired[CostCategoryValuesOutputTypeDef]

class ExpressionPaginatorTypeDef(TypedDict):
    Or: NotRequired[List[Dict[str, Any]]]
    And: NotRequired[List[Dict[str, Any]]]
    Not: NotRequired[Dict[str, Any]]
    Dimensions: NotRequired[DimensionValuesOutputTypeDef]
    Tags: NotRequired[TagValuesOutputTypeDef]
    CostCategories: NotRequired[CostCategoryValuesOutputTypeDef]

DimensionValuesUnionTypeDef = Union[DimensionValuesTypeDef, DimensionValuesOutputTypeDef]

class GetDimensionValuesResponseTypeDef(TypedDict):
    DimensionValues: List[DimensionValuesWithAttributesTypeDef]
    ReturnSize: int
    TotalSize: int
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReservedCapacityDetailsTypeDef(TypedDict):
    DynamoDBCapacityDetails: NotRequired[DynamoDBCapacityDetailsTypeDef]

class ResourceDetailsTypeDef(TypedDict):
    EC2ResourceDetails: NotRequired[EC2ResourceDetailsTypeDef]

class EC2ResourceUtilizationTypeDef(TypedDict):
    MaxCpuUtilizationPercentage: NotRequired[str]
    MaxMemoryUtilizationPercentage: NotRequired[str]
    MaxStorageUtilizationPercentage: NotRequired[str]
    EBSResourceUtilization: NotRequired[EBSResourceUtilizationTypeDef]
    DiskResourceUtilization: NotRequired[DiskResourceUtilizationTypeDef]
    NetworkResourceUtilization: NotRequired[NetworkResourceUtilizationTypeDef]

class ServiceSpecificationTypeDef(TypedDict):
    EC2Specification: NotRequired[EC2SpecificationTypeDef]

class ListSavingsPlansPurchaseRecommendationGenerationResponseTypeDef(TypedDict):
    GenerationSummaryList: List[GenerationSummaryTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnomalyMonitorsRequestPaginateTypeDef(TypedDict):
    MonitorArnList: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetAnomalySubscriptionsRequestPaginateTypeDef(TypedDict):
    SubscriptionArnList: NotRequired[Sequence[str]]
    MonitorArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetAnomaliesRequestPaginateTypeDef(TypedDict):
    DateInterval: AnomalyDateIntervalTypeDef
    MonitorArn: NotRequired[str]
    Feedback: NotRequired[AnomalyFeedbackTypeType]
    TotalImpact: NotRequired[TotalImpactFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetAnomaliesRequestTypeDef(TypedDict):
    DateInterval: AnomalyDateIntervalTypeDef
    MonitorArn: NotRequired[str]
    Feedback: NotRequired[AnomalyFeedbackTypeType]
    TotalImpact: NotRequired[TotalImpactFilterTypeDef]
    NextPageToken: NotRequired[str]
    MaxResults: NotRequired[int]

class GroupTypeDef(TypedDict):
    Keys: NotRequired[List[str]]
    Metrics: NotRequired[Dict[str, MetricValueTypeDef]]

class ReservationUtilizationGroupTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]
    Attributes: NotRequired[Dict[str, str]]
    Utilization: NotRequired[ReservationAggregatesTypeDef]

class InstanceDetailsTypeDef(TypedDict):
    EC2InstanceDetails: NotRequired[EC2InstanceDetailsTypeDef]
    RDSInstanceDetails: NotRequired[RDSInstanceDetailsTypeDef]
    RedshiftInstanceDetails: NotRequired[RedshiftInstanceDetailsTypeDef]
    ElastiCacheInstanceDetails: NotRequired[ElastiCacheInstanceDetailsTypeDef]
    ESInstanceDetails: NotRequired[ESInstanceDetailsTypeDef]
    MemoryDBInstanceDetails: NotRequired[MemoryDBInstanceDetailsTypeDef]

class RecommendationDetailDataTypeDef(TypedDict):
    AccountScope: NotRequired[AccountScopeType]
    LookbackPeriodInDays: NotRequired[LookbackPeriodInDaysType]
    SavingsPlansType: NotRequired[SupportedSavingsPlansTypeType]
    TermInYears: NotRequired[TermInYearsType]
    PaymentOption: NotRequired[PaymentOptionType]
    AccountId: NotRequired[str]
    CurrencyCode: NotRequired[str]
    InstanceFamily: NotRequired[str]
    Region: NotRequired[str]
    OfferingId: NotRequired[str]
    GenerationTimestamp: NotRequired[str]
    LatestUsageTimestamp: NotRequired[str]
    CurrentAverageHourlyOnDemandSpend: NotRequired[str]
    CurrentMaximumHourlyOnDemandSpend: NotRequired[str]
    CurrentMinimumHourlyOnDemandSpend: NotRequired[str]
    EstimatedAverageUtilization: NotRequired[str]
    EstimatedMonthlySavingsAmount: NotRequired[str]
    EstimatedOnDemandCost: NotRequired[str]
    EstimatedOnDemandCostWithCurrentCommitment: NotRequired[str]
    EstimatedROI: NotRequired[str]
    EstimatedSPCost: NotRequired[str]
    EstimatedSavingsAmount: NotRequired[str]
    EstimatedSavingsPercentage: NotRequired[str]
    ExistingHourlyCommitment: NotRequired[str]
    HourlyCommitmentToPurchase: NotRequired[str]
    UpfrontCost: NotRequired[str]
    CurrentAverageCoverage: NotRequired[str]
    EstimatedAverageCoverage: NotRequired[str]
    MetricsOverLookbackPeriod: NotRequired[List[RecommendationDetailHourlyMetricsTypeDef]]

class SavingsPlansPurchaseAnalysisDetailsTypeDef(TypedDict):
    CurrencyCode: NotRequired[str]
    LookbackPeriodInHours: NotRequired[str]
    CurrentAverageCoverage: NotRequired[str]
    CurrentAverageHourlyOnDemandSpend: NotRequired[str]
    CurrentMaximumHourlyOnDemandSpend: NotRequired[str]
    CurrentMinimumHourlyOnDemandSpend: NotRequired[str]
    CurrentOnDemandSpend: NotRequired[str]
    ExistingHourlyCommitment: NotRequired[str]
    HourlyCommitmentToPurchase: NotRequired[str]
    EstimatedAverageCoverage: NotRequired[str]
    EstimatedAverageUtilization: NotRequired[str]
    EstimatedMonthlySavingsAmount: NotRequired[str]
    EstimatedOnDemandCost: NotRequired[str]
    EstimatedOnDemandCostWithCurrentCommitment: NotRequired[str]
    EstimatedROI: NotRequired[str]
    EstimatedSavingsAmount: NotRequired[str]
    EstimatedSavingsPercentage: NotRequired[str]
    EstimatedCommitmentCost: NotRequired[str]
    LatestUsageTimestamp: NotRequired[str]
    UpfrontCost: NotRequired[str]
    AdditionalMetadata: NotRequired[str]
    MetricsOverLookbackPeriod: NotRequired[List[RecommendationDetailHourlyMetricsTypeDef]]

class RootCauseTypeDef(TypedDict):
    Service: NotRequired[str]
    Region: NotRequired[str]
    LinkedAccount: NotRequired[str]
    LinkedAccountName: NotRequired[str]
    UsageType: NotRequired[str]
    Impact: NotRequired[RootCauseImpactTypeDef]

class SavingsPlansCoverageTypeDef(TypedDict):
    Attributes: NotRequired[Dict[str, str]]
    Coverage: NotRequired[SavingsPlansCoverageDataTypeDef]
    TimePeriod: NotRequired[DateIntervalTypeDef]

class SavingsPlansPurchaseRecommendationDetailTypeDef(TypedDict):
    SavingsPlansDetails: NotRequired[SavingsPlansDetailsTypeDef]
    AccountId: NotRequired[str]
    UpfrontCost: NotRequired[str]
    EstimatedROI: NotRequired[str]
    CurrencyCode: NotRequired[str]
    EstimatedSPCost: NotRequired[str]
    EstimatedOnDemandCost: NotRequired[str]
    EstimatedOnDemandCostWithCurrentCommitment: NotRequired[str]
    EstimatedSavingsAmount: NotRequired[str]
    EstimatedSavingsPercentage: NotRequired[str]
    HourlyCommitmentToPurchase: NotRequired[str]
    EstimatedAverageUtilization: NotRequired[str]
    EstimatedMonthlySavingsAmount: NotRequired[str]
    CurrentMinimumHourlyOnDemandSpend: NotRequired[str]
    CurrentMaximumHourlyOnDemandSpend: NotRequired[str]
    CurrentAverageHourlyOnDemandSpend: NotRequired[str]
    RecommendationDetailId: NotRequired[str]

class SavingsPlansPurchaseAnalysisConfigurationOutputTypeDef(TypedDict):
    AnalysisType: AnalysisTypeType
    SavingsPlansToAdd: List[SavingsPlansTypeDef]
    LookBackTimePeriod: DateIntervalTypeDef
    AccountScope: NotRequired[AccountScopeType]
    AccountId: NotRequired[str]
    SavingsPlansToExclude: NotRequired[List[str]]

class SavingsPlansPurchaseAnalysisConfigurationTypeDef(TypedDict):
    AnalysisType: AnalysisTypeType
    SavingsPlansToAdd: Sequence[SavingsPlansTypeDef]
    LookBackTimePeriod: DateIntervalTypeDef
    AccountScope: NotRequired[AccountScopeType]
    AccountId: NotRequired[str]
    SavingsPlansToExclude: NotRequired[Sequence[str]]

class SavingsPlansUtilizationAggregatesTypeDef(TypedDict):
    Utilization: SavingsPlansUtilizationTypeDef
    Savings: NotRequired[SavingsPlansSavingsTypeDef]
    AmortizedCommitment: NotRequired[SavingsPlansAmortizedCommitmentTypeDef]

class SavingsPlansUtilizationByTimeTypeDef(TypedDict):
    TimePeriod: DateIntervalTypeDef
    Utilization: SavingsPlansUtilizationTypeDef
    Savings: NotRequired[SavingsPlansSavingsTypeDef]
    AmortizedCommitment: NotRequired[SavingsPlansAmortizedCommitmentTypeDef]

class SavingsPlansUtilizationDetailTypeDef(TypedDict):
    SavingsPlanArn: NotRequired[str]
    Attributes: NotRequired[Dict[str, str]]
    Utilization: NotRequired[SavingsPlansUtilizationTypeDef]
    Savings: NotRequired[SavingsPlansSavingsTypeDef]
    AmortizedCommitment: NotRequired[SavingsPlansAmortizedCommitmentTypeDef]

TagValuesUnionTypeDef = Union[TagValuesTypeDef, TagValuesOutputTypeDef]

class UpdateCostAllocationTagsStatusResponseTypeDef(TypedDict):
    Errors: List[UpdateCostAllocationTagsStatusErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCostCategoryDefinitionsResponseTypeDef(TypedDict):
    CostCategoryReferences: List[CostCategoryReferenceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CostCategorySplitChargeRuleTypeDef(TypedDict):
    Source: str
    Targets: Sequence[str]
    Method: CostCategorySplitChargeMethodType
    Parameters: NotRequired[Sequence[CostCategorySplitChargeRuleParameterUnionTypeDef]]

class GetCostForecastResponseTypeDef(TypedDict):
    Total: MetricValueTypeDef
    ForecastResultsByTime: List[ForecastResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetUsageForecastResponseTypeDef(TypedDict):
    Total: MetricValueTypeDef
    ForecastResultsByTime: List[ForecastResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReservationCoverageGroupTypeDef(TypedDict):
    Attributes: NotRequired[Dict[str, str]]
    Coverage: NotRequired[CoverageTypeDef]

class AnomalyMonitorOutputTypeDef(TypedDict):
    MonitorName: str
    MonitorType: MonitorTypeType
    MonitorArn: NotRequired[str]
    CreationDate: NotRequired[str]
    LastUpdatedDate: NotRequired[str]
    LastEvaluatedDate: NotRequired[str]
    MonitorDimension: NotRequired[Literal["SERVICE"]]
    MonitorSpecification: NotRequired[ExpressionOutputTypeDef]
    DimensionalValueCount: NotRequired[int]

class AnomalySubscriptionOutputTypeDef(TypedDict):
    MonitorArnList: List[str]
    Subscribers: List[SubscriberTypeDef]
    Frequency: AnomalySubscriptionFrequencyType
    SubscriptionName: str
    SubscriptionArn: NotRequired[str]
    AccountId: NotRequired[str]
    Threshold: NotRequired[float]
    ThresholdExpression: NotRequired[ExpressionOutputTypeDef]

CostCategoryRuleOutputTypeDef = TypedDict(
    "CostCategoryRuleOutputTypeDef",
    {
        "Value": NotRequired[str],
        "Rule": NotRequired[ExpressionOutputTypeDef],
        "InheritedValue": NotRequired[CostCategoryInheritedValueDimensionTypeDef],
        "Type": NotRequired[CostCategoryRuleTypeType],
    },
)

class AnomalyMonitorPaginatorTypeDef(TypedDict):
    MonitorName: str
    MonitorType: MonitorTypeType
    MonitorArn: NotRequired[str]
    CreationDate: NotRequired[str]
    LastUpdatedDate: NotRequired[str]
    LastEvaluatedDate: NotRequired[str]
    MonitorDimension: NotRequired[Literal["SERVICE"]]
    MonitorSpecification: NotRequired[ExpressionPaginatorTypeDef]
    DimensionalValueCount: NotRequired[int]

class AnomalySubscriptionPaginatorTypeDef(TypedDict):
    MonitorArnList: List[str]
    Subscribers: List[SubscriberTypeDef]
    Frequency: AnomalySubscriptionFrequencyType
    SubscriptionName: str
    SubscriptionArn: NotRequired[str]
    AccountId: NotRequired[str]
    Threshold: NotRequired[float]
    ThresholdExpression: NotRequired[ExpressionPaginatorTypeDef]

class ResourceUtilizationTypeDef(TypedDict):
    EC2ResourceUtilization: NotRequired[EC2ResourceUtilizationTypeDef]

class ResultByTimeTypeDef(TypedDict):
    TimePeriod: NotRequired[DateIntervalTypeDef]
    Total: NotRequired[Dict[str, MetricValueTypeDef]]
    Groups: NotRequired[List[GroupTypeDef]]
    Estimated: NotRequired[bool]

class UtilizationByTimeTypeDef(TypedDict):
    TimePeriod: NotRequired[DateIntervalTypeDef]
    Groups: NotRequired[List[ReservationUtilizationGroupTypeDef]]
    Total: NotRequired[ReservationAggregatesTypeDef]

class ReservationPurchaseRecommendationDetailTypeDef(TypedDict):
    AccountId: NotRequired[str]
    InstanceDetails: NotRequired[InstanceDetailsTypeDef]
    RecommendedNumberOfInstancesToPurchase: NotRequired[str]
    RecommendedNormalizedUnitsToPurchase: NotRequired[str]
    MinimumNumberOfInstancesUsedPerHour: NotRequired[str]
    MinimumNormalizedUnitsUsedPerHour: NotRequired[str]
    MaximumNumberOfInstancesUsedPerHour: NotRequired[str]
    MaximumNormalizedUnitsUsedPerHour: NotRequired[str]
    AverageNumberOfInstancesUsedPerHour: NotRequired[str]
    AverageNormalizedUnitsUsedPerHour: NotRequired[str]
    AverageUtilization: NotRequired[str]
    EstimatedBreakEvenInMonths: NotRequired[str]
    CurrencyCode: NotRequired[str]
    EstimatedMonthlySavingsAmount: NotRequired[str]
    EstimatedMonthlySavingsPercentage: NotRequired[str]
    EstimatedMonthlyOnDemandCost: NotRequired[str]
    EstimatedReservationCostForLookbackPeriod: NotRequired[str]
    UpfrontCost: NotRequired[str]
    RecurringStandardMonthlyCost: NotRequired[str]
    ReservedCapacityDetails: NotRequired[ReservedCapacityDetailsTypeDef]
    RecommendedNumberOfCapacityUnitsToPurchase: NotRequired[str]
    MinimumNumberOfCapacityUnitsUsedPerHour: NotRequired[str]
    MaximumNumberOfCapacityUnitsUsedPerHour: NotRequired[str]
    AverageNumberOfCapacityUnitsUsedPerHour: NotRequired[str]

class GetSavingsPlanPurchaseRecommendationDetailsResponseTypeDef(TypedDict):
    RecommendationDetailId: str
    RecommendationDetailData: RecommendationDetailDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AnalysisDetailsTypeDef(TypedDict):
    SavingsPlansPurchaseAnalysisDetails: NotRequired[SavingsPlansPurchaseAnalysisDetailsTypeDef]

class AnomalyTypeDef(TypedDict):
    AnomalyId: str
    AnomalyScore: AnomalyScoreTypeDef
    Impact: ImpactTypeDef
    MonitorArn: str
    AnomalyStartDate: NotRequired[str]
    AnomalyEndDate: NotRequired[str]
    DimensionValue: NotRequired[str]
    RootCauses: NotRequired[List[RootCauseTypeDef]]
    Feedback: NotRequired[AnomalyFeedbackTypeType]

class GetSavingsPlansCoverageResponseTypeDef(TypedDict):
    SavingsPlansCoverages: List[SavingsPlansCoverageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SavingsPlansPurchaseRecommendationTypeDef(TypedDict):
    AccountScope: NotRequired[AccountScopeType]
    SavingsPlansType: NotRequired[SupportedSavingsPlansTypeType]
    TermInYears: NotRequired[TermInYearsType]
    PaymentOption: NotRequired[PaymentOptionType]
    LookbackPeriodInDays: NotRequired[LookbackPeriodInDaysType]
    SavingsPlansPurchaseRecommendationDetails: NotRequired[
        List[SavingsPlansPurchaseRecommendationDetailTypeDef]
    ]
    SavingsPlansPurchaseRecommendationSummary: NotRequired[
        SavingsPlansPurchaseRecommendationSummaryTypeDef
    ]

class CommitmentPurchaseAnalysisConfigurationOutputTypeDef(TypedDict):
    SavingsPlansPurchaseAnalysisConfiguration: NotRequired[
        SavingsPlansPurchaseAnalysisConfigurationOutputTypeDef
    ]

class CommitmentPurchaseAnalysisConfigurationTypeDef(TypedDict):
    SavingsPlansPurchaseAnalysisConfiguration: NotRequired[
        SavingsPlansPurchaseAnalysisConfigurationTypeDef
    ]

class GetSavingsPlansUtilizationResponseTypeDef(TypedDict):
    SavingsPlansUtilizationsByTime: List[SavingsPlansUtilizationByTimeTypeDef]
    Total: SavingsPlansUtilizationAggregatesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSavingsPlansUtilizationDetailsResponseTypeDef(TypedDict):
    SavingsPlansUtilizationDetails: List[SavingsPlansUtilizationDetailTypeDef]
    Total: SavingsPlansUtilizationAggregatesTypeDef
    TimePeriod: DateIntervalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ExpressionTypeDef(TypedDict):
    Or: NotRequired[Sequence[Mapping[str, Any]]]
    And: NotRequired[Sequence[Mapping[str, Any]]]
    Not: NotRequired[Mapping[str, Any]]
    Dimensions: NotRequired[DimensionValuesUnionTypeDef]
    Tags: NotRequired[TagValuesUnionTypeDef]
    CostCategories: NotRequired[CostCategoryValuesUnionTypeDef]

CostCategorySplitChargeRuleUnionTypeDef = Union[
    CostCategorySplitChargeRuleTypeDef, CostCategorySplitChargeRuleOutputTypeDef
]

class CoverageByTimeTypeDef(TypedDict):
    TimePeriod: NotRequired[DateIntervalTypeDef]
    Groups: NotRequired[List[ReservationCoverageGroupTypeDef]]
    Total: NotRequired[CoverageTypeDef]

class GetAnomalyMonitorsResponseTypeDef(TypedDict):
    AnomalyMonitors: List[AnomalyMonitorOutputTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnomalySubscriptionsResponseTypeDef(TypedDict):
    AnomalySubscriptions: List[AnomalySubscriptionOutputTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CostCategoryTypeDef(TypedDict):
    CostCategoryArn: str
    EffectiveStart: str
    Name: str
    RuleVersion: Literal["CostCategoryExpression.v1"]
    Rules: List[CostCategoryRuleOutputTypeDef]
    EffectiveEnd: NotRequired[str]
    SplitChargeRules: NotRequired[List[CostCategorySplitChargeRuleOutputTypeDef]]
    ProcessingStatus: NotRequired[List[CostCategoryProcessingStatusTypeDef]]
    DefaultValue: NotRequired[str]

class GetAnomalyMonitorsResponsePaginatorTypeDef(TypedDict):
    AnomalyMonitors: List[AnomalyMonitorPaginatorTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnomalySubscriptionsResponsePaginatorTypeDef(TypedDict):
    AnomalySubscriptions: List[AnomalySubscriptionPaginatorTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CurrentInstanceTypeDef(TypedDict):
    ResourceId: NotRequired[str]
    InstanceName: NotRequired[str]
    Tags: NotRequired[List[TagValuesOutputTypeDef]]
    ResourceDetails: NotRequired[ResourceDetailsTypeDef]
    ResourceUtilization: NotRequired[ResourceUtilizationTypeDef]
    ReservationCoveredHoursInLookbackPeriod: NotRequired[str]
    SavingsPlansCoveredHoursInLookbackPeriod: NotRequired[str]
    OnDemandHoursInLookbackPeriod: NotRequired[str]
    TotalRunningHoursInLookbackPeriod: NotRequired[str]
    MonthlyCost: NotRequired[str]
    CurrencyCode: NotRequired[str]

class TargetInstanceTypeDef(TypedDict):
    EstimatedMonthlyCost: NotRequired[str]
    EstimatedMonthlySavings: NotRequired[str]
    CurrencyCode: NotRequired[str]
    DefaultTargetInstance: NotRequired[bool]
    ResourceDetails: NotRequired[ResourceDetailsTypeDef]
    ExpectedResourceUtilization: NotRequired[ResourceUtilizationTypeDef]
    PlatformDifferences: NotRequired[List[PlatformDifferenceType]]

class GetCostAndUsageResponseTypeDef(TypedDict):
    NextPageToken: str
    GroupDefinitions: List[GroupDefinitionTypeDef]
    ResultsByTime: List[ResultByTimeTypeDef]
    DimensionValueAttributes: List[DimensionValuesWithAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCostAndUsageWithResourcesResponseTypeDef(TypedDict):
    NextPageToken: str
    GroupDefinitions: List[GroupDefinitionTypeDef]
    ResultsByTime: List[ResultByTimeTypeDef]
    DimensionValueAttributes: List[DimensionValuesWithAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetReservationUtilizationResponseTypeDef(TypedDict):
    UtilizationsByTime: List[UtilizationByTimeTypeDef]
    Total: ReservationAggregatesTypeDef
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReservationPurchaseRecommendationTypeDef(TypedDict):
    AccountScope: NotRequired[AccountScopeType]
    LookbackPeriodInDays: NotRequired[LookbackPeriodInDaysType]
    TermInYears: NotRequired[TermInYearsType]
    PaymentOption: NotRequired[PaymentOptionType]
    ServiceSpecification: NotRequired[ServiceSpecificationTypeDef]
    RecommendationDetails: NotRequired[List[ReservationPurchaseRecommendationDetailTypeDef]]
    RecommendationSummary: NotRequired[ReservationPurchaseRecommendationSummaryTypeDef]

class GetAnomaliesResponseTypeDef(TypedDict):
    Anomalies: List[AnomalyTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSavingsPlansPurchaseRecommendationResponseTypeDef(TypedDict):
    Metadata: SavingsPlansPurchaseRecommendationMetadataTypeDef
    SavingsPlansPurchaseRecommendation: SavingsPlansPurchaseRecommendationTypeDef
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AnalysisSummaryTypeDef(TypedDict):
    EstimatedCompletionTime: NotRequired[str]
    AnalysisCompletionTime: NotRequired[str]
    AnalysisStartedTime: NotRequired[str]
    AnalysisStatus: NotRequired[AnalysisStatusType]
    ErrorCode: NotRequired[ErrorCodeType]
    AnalysisId: NotRequired[str]
    CommitmentPurchaseAnalysisConfiguration: NotRequired[
        CommitmentPurchaseAnalysisConfigurationOutputTypeDef
    ]

class GetCommitmentPurchaseAnalysisResponseTypeDef(TypedDict):
    EstimatedCompletionTime: str
    AnalysisCompletionTime: str
    AnalysisStartedTime: str
    AnalysisId: str
    AnalysisStatus: AnalysisStatusType
    ErrorCode: ErrorCodeType
    AnalysisDetails: AnalysisDetailsTypeDef
    CommitmentPurchaseAnalysisConfiguration: CommitmentPurchaseAnalysisConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CommitmentPurchaseAnalysisConfigurationUnionTypeDef = Union[
    CommitmentPurchaseAnalysisConfigurationTypeDef,
    CommitmentPurchaseAnalysisConfigurationOutputTypeDef,
]

class AnomalyMonitorTypeDef(TypedDict):
    MonitorName: str
    MonitorType: MonitorTypeType
    MonitorArn: NotRequired[str]
    CreationDate: NotRequired[str]
    LastUpdatedDate: NotRequired[str]
    LastEvaluatedDate: NotRequired[str]
    MonitorDimension: NotRequired[Literal["SERVICE"]]
    MonitorSpecification: NotRequired[ExpressionTypeDef]
    DimensionalValueCount: NotRequired[int]

class AnomalySubscriptionTypeDef(TypedDict):
    MonitorArnList: Sequence[str]
    Subscribers: Sequence[SubscriberTypeDef]
    Frequency: AnomalySubscriptionFrequencyType
    SubscriptionName: str
    SubscriptionArn: NotRequired[str]
    AccountId: NotRequired[str]
    Threshold: NotRequired[float]
    ThresholdExpression: NotRequired[ExpressionTypeDef]

ExpressionUnionTypeDef = Union[ExpressionTypeDef, ExpressionOutputTypeDef]

class GetReservationCoverageResponseTypeDef(TypedDict):
    CoveragesByTime: List[CoverageByTimeTypeDef]
    Total: CoverageTypeDef
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCostCategoryDefinitionResponseTypeDef(TypedDict):
    CostCategory: CostCategoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyRecommendationDetailTypeDef(TypedDict):
    TargetInstances: NotRequired[List[TargetInstanceTypeDef]]

class GetReservationPurchaseRecommendationResponseTypeDef(TypedDict):
    Metadata: ReservationPurchaseRecommendationMetadataTypeDef
    Recommendations: List[ReservationPurchaseRecommendationTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCommitmentPurchaseAnalysesResponseTypeDef(TypedDict):
    AnalysisSummaryList: List[AnalysisSummaryTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartCommitmentPurchaseAnalysisRequestTypeDef(TypedDict):
    CommitmentPurchaseAnalysisConfiguration: CommitmentPurchaseAnalysisConfigurationUnionTypeDef

AnomalyMonitorUnionTypeDef = Union[AnomalyMonitorTypeDef, AnomalyMonitorOutputTypeDef]
AnomalySubscriptionUnionTypeDef = Union[
    AnomalySubscriptionTypeDef, AnomalySubscriptionOutputTypeDef
]
CostCategoryRuleTypeDef = TypedDict(
    "CostCategoryRuleTypeDef",
    {
        "Value": NotRequired[str],
        "Rule": NotRequired[ExpressionUnionTypeDef],
        "InheritedValue": NotRequired[CostCategoryInheritedValueDimensionTypeDef],
        "Type": NotRequired[CostCategoryRuleTypeType],
    },
)

class GetCostAndUsageRequestTypeDef(TypedDict):
    TimePeriod: DateIntervalTypeDef
    Granularity: GranularityType
    Metrics: Sequence[str]
    Filter: NotRequired[ExpressionUnionTypeDef]
    GroupBy: NotRequired[Sequence[GroupDefinitionTypeDef]]
    BillingViewArn: NotRequired[str]
    NextPageToken: NotRequired[str]

class GetCostAndUsageWithResourcesRequestTypeDef(TypedDict):
    TimePeriod: DateIntervalTypeDef
    Granularity: GranularityType
    Filter: ExpressionUnionTypeDef
    Metrics: NotRequired[Sequence[str]]
    GroupBy: NotRequired[Sequence[GroupDefinitionTypeDef]]
    BillingViewArn: NotRequired[str]
    NextPageToken: NotRequired[str]

class GetCostCategoriesRequestTypeDef(TypedDict):
    TimePeriod: DateIntervalTypeDef
    SearchString: NotRequired[str]
    CostCategoryName: NotRequired[str]
    Filter: NotRequired[ExpressionUnionTypeDef]
    SortBy: NotRequired[Sequence[SortDefinitionTypeDef]]
    BillingViewArn: NotRequired[str]
    MaxResults: NotRequired[int]
    NextPageToken: NotRequired[str]

class GetCostForecastRequestTypeDef(TypedDict):
    TimePeriod: DateIntervalTypeDef
    Metric: MetricType
    Granularity: GranularityType
    Filter: NotRequired[ExpressionUnionTypeDef]
    BillingViewArn: NotRequired[str]
    PredictionIntervalLevel: NotRequired[int]

class GetDimensionValuesRequestTypeDef(TypedDict):
    TimePeriod: DateIntervalTypeDef
    Dimension: DimensionType
    SearchString: NotRequired[str]
    Context: NotRequired[ContextType]
    Filter: NotRequired[ExpressionUnionTypeDef]
    SortBy: NotRequired[Sequence[SortDefinitionTypeDef]]
    BillingViewArn: NotRequired[str]
    MaxResults: NotRequired[int]
    NextPageToken: NotRequired[str]

class GetReservationCoverageRequestTypeDef(TypedDict):
    TimePeriod: DateIntervalTypeDef
    GroupBy: NotRequired[Sequence[GroupDefinitionTypeDef]]
    Granularity: NotRequired[GranularityType]
    Filter: NotRequired[ExpressionUnionTypeDef]
    Metrics: NotRequired[Sequence[str]]
    NextPageToken: NotRequired[str]
    SortBy: NotRequired[SortDefinitionTypeDef]
    MaxResults: NotRequired[int]

class GetReservationPurchaseRecommendationRequestTypeDef(TypedDict):
    Service: str
    AccountId: NotRequired[str]
    Filter: NotRequired[ExpressionUnionTypeDef]
    AccountScope: NotRequired[AccountScopeType]
    LookbackPeriodInDays: NotRequired[LookbackPeriodInDaysType]
    TermInYears: NotRequired[TermInYearsType]
    PaymentOption: NotRequired[PaymentOptionType]
    ServiceSpecification: NotRequired[ServiceSpecificationTypeDef]
    PageSize: NotRequired[int]
    NextPageToken: NotRequired[str]

class GetReservationUtilizationRequestTypeDef(TypedDict):
    TimePeriod: DateIntervalTypeDef
    GroupBy: NotRequired[Sequence[GroupDefinitionTypeDef]]
    Granularity: NotRequired[GranularityType]
    Filter: NotRequired[ExpressionUnionTypeDef]
    SortBy: NotRequired[SortDefinitionTypeDef]
    NextPageToken: NotRequired[str]
    MaxResults: NotRequired[int]

class GetRightsizingRecommendationRequestTypeDef(TypedDict):
    Service: str
    Filter: NotRequired[ExpressionUnionTypeDef]
    Configuration: NotRequired[RightsizingRecommendationConfigurationTypeDef]
    PageSize: NotRequired[int]
    NextPageToken: NotRequired[str]

class GetSavingsPlansCoverageRequestTypeDef(TypedDict):
    TimePeriod: DateIntervalTypeDef
    GroupBy: NotRequired[Sequence[GroupDefinitionTypeDef]]
    Granularity: NotRequired[GranularityType]
    Filter: NotRequired[ExpressionUnionTypeDef]
    Metrics: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SortBy: NotRequired[SortDefinitionTypeDef]

class GetSavingsPlansPurchaseRecommendationRequestTypeDef(TypedDict):
    SavingsPlansType: SupportedSavingsPlansTypeType
    TermInYears: TermInYearsType
    PaymentOption: PaymentOptionType
    LookbackPeriodInDays: LookbackPeriodInDaysType
    AccountScope: NotRequired[AccountScopeType]
    NextPageToken: NotRequired[str]
    PageSize: NotRequired[int]
    Filter: NotRequired[ExpressionUnionTypeDef]

class GetSavingsPlansUtilizationDetailsRequestTypeDef(TypedDict):
    TimePeriod: DateIntervalTypeDef
    Filter: NotRequired[ExpressionUnionTypeDef]
    DataType: NotRequired[Sequence[SavingsPlansDataTypeType]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SortBy: NotRequired[SortDefinitionTypeDef]

class GetSavingsPlansUtilizationRequestTypeDef(TypedDict):
    TimePeriod: DateIntervalTypeDef
    Granularity: NotRequired[GranularityType]
    Filter: NotRequired[ExpressionUnionTypeDef]
    SortBy: NotRequired[SortDefinitionTypeDef]

class GetTagsRequestTypeDef(TypedDict):
    TimePeriod: DateIntervalTypeDef
    SearchString: NotRequired[str]
    TagKey: NotRequired[str]
    Filter: NotRequired[ExpressionUnionTypeDef]
    SortBy: NotRequired[Sequence[SortDefinitionTypeDef]]
    BillingViewArn: NotRequired[str]
    MaxResults: NotRequired[int]
    NextPageToken: NotRequired[str]

class GetUsageForecastRequestTypeDef(TypedDict):
    TimePeriod: DateIntervalTypeDef
    Metric: MetricType
    Granularity: GranularityType
    Filter: NotRequired[ExpressionUnionTypeDef]
    BillingViewArn: NotRequired[str]
    PredictionIntervalLevel: NotRequired[int]

class UpdateAnomalySubscriptionRequestTypeDef(TypedDict):
    SubscriptionArn: str
    Threshold: NotRequired[float]
    Frequency: NotRequired[AnomalySubscriptionFrequencyType]
    MonitorArnList: NotRequired[Sequence[str]]
    Subscribers: NotRequired[Sequence[SubscriberTypeDef]]
    SubscriptionName: NotRequired[str]
    ThresholdExpression: NotRequired[ExpressionUnionTypeDef]

class RightsizingRecommendationTypeDef(TypedDict):
    AccountId: NotRequired[str]
    CurrentInstance: NotRequired[CurrentInstanceTypeDef]
    RightsizingType: NotRequired[RightsizingTypeType]
    ModifyRecommendationDetail: NotRequired[ModifyRecommendationDetailTypeDef]
    TerminateRecommendationDetail: NotRequired[TerminateRecommendationDetailTypeDef]
    FindingReasonCodes: NotRequired[List[FindingReasonCodeType]]

class CreateAnomalyMonitorRequestTypeDef(TypedDict):
    AnomalyMonitor: AnomalyMonitorUnionTypeDef
    ResourceTags: NotRequired[Sequence[ResourceTagTypeDef]]

class CreateAnomalySubscriptionRequestTypeDef(TypedDict):
    AnomalySubscription: AnomalySubscriptionUnionTypeDef
    ResourceTags: NotRequired[Sequence[ResourceTagTypeDef]]

CostCategoryRuleUnionTypeDef = Union[CostCategoryRuleTypeDef, CostCategoryRuleOutputTypeDef]

class GetRightsizingRecommendationResponseTypeDef(TypedDict):
    Metadata: RightsizingRecommendationMetadataTypeDef
    Summary: RightsizingRecommendationSummaryTypeDef
    RightsizingRecommendations: List[RightsizingRecommendationTypeDef]
    NextPageToken: str
    Configuration: RightsizingRecommendationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCostCategoryDefinitionRequestTypeDef(TypedDict):
    Name: str
    RuleVersion: Literal["CostCategoryExpression.v1"]
    Rules: Sequence[CostCategoryRuleUnionTypeDef]
    EffectiveStart: NotRequired[str]
    DefaultValue: NotRequired[str]
    SplitChargeRules: NotRequired[Sequence[CostCategorySplitChargeRuleUnionTypeDef]]
    ResourceTags: NotRequired[Sequence[ResourceTagTypeDef]]

class UpdateCostCategoryDefinitionRequestTypeDef(TypedDict):
    CostCategoryArn: str
    RuleVersion: Literal["CostCategoryExpression.v1"]
    Rules: Sequence[CostCategoryRuleUnionTypeDef]
    EffectiveStart: NotRequired[str]
    DefaultValue: NotRequired[str]
    SplitChargeRules: NotRequired[Sequence[CostCategorySplitChargeRuleUnionTypeDef]]
