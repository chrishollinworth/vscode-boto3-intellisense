"""
Type annotations for ce service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ce.type_defs import AnomalyDateIntervalTypeDef

    data: AnomalyDateIntervalTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    AccountScopeType,
    AnomalyFeedbackTypeType,
    AnomalySubscriptionFrequencyType,
    ContextType,
    CostCategoryInheritedValueDimensionNameType,
    CostCategoryRuleTypeType,
    CostCategoryStatusType,
    DimensionType,
    FindingReasonCodeType,
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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AnomalyDateIntervalTypeDef",
    "AnomalyMonitorTypeDef",
    "AnomalyScoreTypeDef",
    "AnomalySubscriptionTypeDef",
    "AnomalyTypeDef",
    "CostCategoryInheritedValueDimensionTypeDef",
    "CostCategoryProcessingStatusTypeDef",
    "CostCategoryReferenceTypeDef",
    "CostCategoryRuleTypeDef",
    "CostCategoryTypeDef",
    "CostCategoryValuesTypeDef",
    "CoverageByTimeTypeDef",
    "CoverageCostTypeDef",
    "CoverageHoursTypeDef",
    "CoverageNormalizedUnitsTypeDef",
    "CoverageTypeDef",
    "CreateAnomalyMonitorRequestRequestTypeDef",
    "CreateAnomalyMonitorResponseTypeDef",
    "CreateAnomalySubscriptionRequestRequestTypeDef",
    "CreateAnomalySubscriptionResponseTypeDef",
    "CreateCostCategoryDefinitionRequestRequestTypeDef",
    "CreateCostCategoryDefinitionResponseTypeDef",
    "CurrentInstanceTypeDef",
    "DateIntervalTypeDef",
    "DeleteAnomalyMonitorRequestRequestTypeDef",
    "DeleteAnomalySubscriptionRequestRequestTypeDef",
    "DeleteCostCategoryDefinitionRequestRequestTypeDef",
    "DeleteCostCategoryDefinitionResponseTypeDef",
    "DescribeCostCategoryDefinitionRequestRequestTypeDef",
    "DescribeCostCategoryDefinitionResponseTypeDef",
    "DimensionValuesTypeDef",
    "DimensionValuesWithAttributesTypeDef",
    "DiskResourceUtilizationTypeDef",
    "EBSResourceUtilizationTypeDef",
    "EC2InstanceDetailsTypeDef",
    "EC2ResourceDetailsTypeDef",
    "EC2ResourceUtilizationTypeDef",
    "EC2SpecificationTypeDef",
    "ESInstanceDetailsTypeDef",
    "ElastiCacheInstanceDetailsTypeDef",
    "ExpressionTypeDef",
    "ForecastResultTypeDef",
    "GetAnomaliesRequestRequestTypeDef",
    "GetAnomaliesResponseTypeDef",
    "GetAnomalyMonitorsRequestRequestTypeDef",
    "GetAnomalyMonitorsResponseTypeDef",
    "GetAnomalySubscriptionsRequestRequestTypeDef",
    "GetAnomalySubscriptionsResponseTypeDef",
    "GetCostAndUsageRequestRequestTypeDef",
    "GetCostAndUsageResponseTypeDef",
    "GetCostAndUsageWithResourcesRequestRequestTypeDef",
    "GetCostAndUsageWithResourcesResponseTypeDef",
    "GetCostCategoriesRequestRequestTypeDef",
    "GetCostCategoriesResponseTypeDef",
    "GetCostForecastRequestRequestTypeDef",
    "GetCostForecastResponseTypeDef",
    "GetDimensionValuesRequestRequestTypeDef",
    "GetDimensionValuesResponseTypeDef",
    "GetReservationCoverageRequestRequestTypeDef",
    "GetReservationCoverageResponseTypeDef",
    "GetReservationPurchaseRecommendationRequestRequestTypeDef",
    "GetReservationPurchaseRecommendationResponseTypeDef",
    "GetReservationUtilizationRequestRequestTypeDef",
    "GetReservationUtilizationResponseTypeDef",
    "GetRightsizingRecommendationRequestRequestTypeDef",
    "GetRightsizingRecommendationResponseTypeDef",
    "GetSavingsPlansCoverageRequestRequestTypeDef",
    "GetSavingsPlansCoverageResponseTypeDef",
    "GetSavingsPlansPurchaseRecommendationRequestRequestTypeDef",
    "GetSavingsPlansPurchaseRecommendationResponseTypeDef",
    "GetSavingsPlansUtilizationDetailsRequestRequestTypeDef",
    "GetSavingsPlansUtilizationDetailsResponseTypeDef",
    "GetSavingsPlansUtilizationRequestRequestTypeDef",
    "GetSavingsPlansUtilizationResponseTypeDef",
    "GetTagsRequestRequestTypeDef",
    "GetTagsResponseTypeDef",
    "GetUsageForecastRequestRequestTypeDef",
    "GetUsageForecastResponseTypeDef",
    "GroupDefinitionTypeDef",
    "GroupTypeDef",
    "ImpactTypeDef",
    "InstanceDetailsTypeDef",
    "ListCostCategoryDefinitionsRequestRequestTypeDef",
    "ListCostCategoryDefinitionsResponseTypeDef",
    "MetricValueTypeDef",
    "ModifyRecommendationDetailTypeDef",
    "NetworkResourceUtilizationTypeDef",
    "ProvideAnomalyFeedbackRequestRequestTypeDef",
    "ProvideAnomalyFeedbackResponseTypeDef",
    "RDSInstanceDetailsTypeDef",
    "RedshiftInstanceDetailsTypeDef",
    "ReservationAggregatesTypeDef",
    "ReservationCoverageGroupTypeDef",
    "ReservationPurchaseRecommendationDetailTypeDef",
    "ReservationPurchaseRecommendationMetadataTypeDef",
    "ReservationPurchaseRecommendationSummaryTypeDef",
    "ReservationPurchaseRecommendationTypeDef",
    "ReservationUtilizationGroupTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceUtilizationTypeDef",
    "ResponseMetadataTypeDef",
    "ResultByTimeTypeDef",
    "RightsizingRecommendationConfigurationTypeDef",
    "RightsizingRecommendationMetadataTypeDef",
    "RightsizingRecommendationSummaryTypeDef",
    "RightsizingRecommendationTypeDef",
    "RootCauseTypeDef",
    "SavingsPlansAmortizedCommitmentTypeDef",
    "SavingsPlansCoverageDataTypeDef",
    "SavingsPlansCoverageTypeDef",
    "SavingsPlansDetailsTypeDef",
    "SavingsPlansPurchaseRecommendationDetailTypeDef",
    "SavingsPlansPurchaseRecommendationMetadataTypeDef",
    "SavingsPlansPurchaseRecommendationSummaryTypeDef",
    "SavingsPlansPurchaseRecommendationTypeDef",
    "SavingsPlansSavingsTypeDef",
    "SavingsPlansUtilizationAggregatesTypeDef",
    "SavingsPlansUtilizationByTimeTypeDef",
    "SavingsPlansUtilizationDetailTypeDef",
    "SavingsPlansUtilizationTypeDef",
    "ServiceSpecificationTypeDef",
    "SortDefinitionTypeDef",
    "SubscriberTypeDef",
    "TagValuesTypeDef",
    "TargetInstanceTypeDef",
    "TerminateRecommendationDetailTypeDef",
    "TotalImpactFilterTypeDef",
    "UpdateAnomalyMonitorRequestRequestTypeDef",
    "UpdateAnomalyMonitorResponseTypeDef",
    "UpdateAnomalySubscriptionRequestRequestTypeDef",
    "UpdateAnomalySubscriptionResponseTypeDef",
    "UpdateCostCategoryDefinitionRequestRequestTypeDef",
    "UpdateCostCategoryDefinitionResponseTypeDef",
    "UtilizationByTimeTypeDef",
)

_RequiredAnomalyDateIntervalTypeDef = TypedDict(
    "_RequiredAnomalyDateIntervalTypeDef",
    {
        "StartDate": str,
    },
)
_OptionalAnomalyDateIntervalTypeDef = TypedDict(
    "_OptionalAnomalyDateIntervalTypeDef",
    {
        "EndDate": str,
    },
    total=False,
)

class AnomalyDateIntervalTypeDef(
    _RequiredAnomalyDateIntervalTypeDef, _OptionalAnomalyDateIntervalTypeDef
):
    pass

_RequiredAnomalyMonitorTypeDef = TypedDict(
    "_RequiredAnomalyMonitorTypeDef",
    {
        "MonitorName": str,
        "MonitorType": MonitorTypeType,
    },
)
_OptionalAnomalyMonitorTypeDef = TypedDict(
    "_OptionalAnomalyMonitorTypeDef",
    {
        "MonitorArn": str,
        "CreationDate": str,
        "LastUpdatedDate": str,
        "LastEvaluatedDate": str,
        "MonitorDimension": Literal["SERVICE"],
        "MonitorSpecification": "ExpressionTypeDef",
        "DimensionalValueCount": int,
    },
    total=False,
)

class AnomalyMonitorTypeDef(_RequiredAnomalyMonitorTypeDef, _OptionalAnomalyMonitorTypeDef):
    pass

AnomalyScoreTypeDef = TypedDict(
    "AnomalyScoreTypeDef",
    {
        "MaxScore": float,
        "CurrentScore": float,
    },
)

_RequiredAnomalySubscriptionTypeDef = TypedDict(
    "_RequiredAnomalySubscriptionTypeDef",
    {
        "MonitorArnList": List[str],
        "Subscribers": List["SubscriberTypeDef"],
        "Threshold": float,
        "Frequency": AnomalySubscriptionFrequencyType,
        "SubscriptionName": str,
    },
)
_OptionalAnomalySubscriptionTypeDef = TypedDict(
    "_OptionalAnomalySubscriptionTypeDef",
    {
        "SubscriptionArn": str,
        "AccountId": str,
    },
    total=False,
)

class AnomalySubscriptionTypeDef(
    _RequiredAnomalySubscriptionTypeDef, _OptionalAnomalySubscriptionTypeDef
):
    pass

_RequiredAnomalyTypeDef = TypedDict(
    "_RequiredAnomalyTypeDef",
    {
        "AnomalyId": str,
        "AnomalyScore": "AnomalyScoreTypeDef",
        "Impact": "ImpactTypeDef",
        "MonitorArn": str,
    },
)
_OptionalAnomalyTypeDef = TypedDict(
    "_OptionalAnomalyTypeDef",
    {
        "AnomalyStartDate": str,
        "AnomalyEndDate": str,
        "DimensionValue": str,
        "RootCauses": List["RootCauseTypeDef"],
        "Feedback": AnomalyFeedbackTypeType,
    },
    total=False,
)

class AnomalyTypeDef(_RequiredAnomalyTypeDef, _OptionalAnomalyTypeDef):
    pass

CostCategoryInheritedValueDimensionTypeDef = TypedDict(
    "CostCategoryInheritedValueDimensionTypeDef",
    {
        "DimensionName": CostCategoryInheritedValueDimensionNameType,
        "DimensionKey": str,
    },
    total=False,
)

CostCategoryProcessingStatusTypeDef = TypedDict(
    "CostCategoryProcessingStatusTypeDef",
    {
        "Component": Literal["COST_EXPLORER"],
        "Status": CostCategoryStatusType,
    },
    total=False,
)

CostCategoryReferenceTypeDef = TypedDict(
    "CostCategoryReferenceTypeDef",
    {
        "CostCategoryArn": str,
        "Name": str,
        "EffectiveStart": str,
        "EffectiveEnd": str,
        "NumberOfRules": int,
        "ProcessingStatus": List["CostCategoryProcessingStatusTypeDef"],
        "Values": List[str],
        "DefaultValue": str,
    },
    total=False,
)

CostCategoryRuleTypeDef = TypedDict(
    "CostCategoryRuleTypeDef",
    {
        "Value": str,
        "Rule": "ExpressionTypeDef",
        "InheritedValue": "CostCategoryInheritedValueDimensionTypeDef",
        "Type": CostCategoryRuleTypeType,
    },
    total=False,
)

_RequiredCostCategoryTypeDef = TypedDict(
    "_RequiredCostCategoryTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveStart": str,
        "Name": str,
        "RuleVersion": Literal["CostCategoryExpression.v1"],
        "Rules": List["CostCategoryRuleTypeDef"],
    },
)
_OptionalCostCategoryTypeDef = TypedDict(
    "_OptionalCostCategoryTypeDef",
    {
        "EffectiveEnd": str,
        "ProcessingStatus": List["CostCategoryProcessingStatusTypeDef"],
        "DefaultValue": str,
    },
    total=False,
)

class CostCategoryTypeDef(_RequiredCostCategoryTypeDef, _OptionalCostCategoryTypeDef):
    pass

CostCategoryValuesTypeDef = TypedDict(
    "CostCategoryValuesTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MatchOptions": List[MatchOptionType],
    },
    total=False,
)

CoverageByTimeTypeDef = TypedDict(
    "CoverageByTimeTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Groups": List["ReservationCoverageGroupTypeDef"],
        "Total": "CoverageTypeDef",
    },
    total=False,
)

CoverageCostTypeDef = TypedDict(
    "CoverageCostTypeDef",
    {
        "OnDemandCost": str,
    },
    total=False,
)

CoverageHoursTypeDef = TypedDict(
    "CoverageHoursTypeDef",
    {
        "OnDemandHours": str,
        "ReservedHours": str,
        "TotalRunningHours": str,
        "CoverageHoursPercentage": str,
    },
    total=False,
)

CoverageNormalizedUnitsTypeDef = TypedDict(
    "CoverageNormalizedUnitsTypeDef",
    {
        "OnDemandNormalizedUnits": str,
        "ReservedNormalizedUnits": str,
        "TotalRunningNormalizedUnits": str,
        "CoverageNormalizedUnitsPercentage": str,
    },
    total=False,
)

CoverageTypeDef = TypedDict(
    "CoverageTypeDef",
    {
        "CoverageHours": "CoverageHoursTypeDef",
        "CoverageNormalizedUnits": "CoverageNormalizedUnitsTypeDef",
        "CoverageCost": "CoverageCostTypeDef",
    },
    total=False,
)

CreateAnomalyMonitorRequestRequestTypeDef = TypedDict(
    "CreateAnomalyMonitorRequestRequestTypeDef",
    {
        "AnomalyMonitor": "AnomalyMonitorTypeDef",
    },
)

CreateAnomalyMonitorResponseTypeDef = TypedDict(
    "CreateAnomalyMonitorResponseTypeDef",
    {
        "MonitorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAnomalySubscriptionRequestRequestTypeDef = TypedDict(
    "CreateAnomalySubscriptionRequestRequestTypeDef",
    {
        "AnomalySubscription": "AnomalySubscriptionTypeDef",
    },
)

CreateAnomalySubscriptionResponseTypeDef = TypedDict(
    "CreateAnomalySubscriptionResponseTypeDef",
    {
        "SubscriptionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCostCategoryDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCostCategoryDefinitionRequestRequestTypeDef",
    {
        "Name": str,
        "RuleVersion": Literal["CostCategoryExpression.v1"],
        "Rules": List["CostCategoryRuleTypeDef"],
    },
)
_OptionalCreateCostCategoryDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCostCategoryDefinitionRequestRequestTypeDef",
    {
        "DefaultValue": str,
    },
    total=False,
)

class CreateCostCategoryDefinitionRequestRequestTypeDef(
    _RequiredCreateCostCategoryDefinitionRequestRequestTypeDef,
    _OptionalCreateCostCategoryDefinitionRequestRequestTypeDef,
):
    pass

CreateCostCategoryDefinitionResponseTypeDef = TypedDict(
    "CreateCostCategoryDefinitionResponseTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveStart": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CurrentInstanceTypeDef = TypedDict(
    "CurrentInstanceTypeDef",
    {
        "ResourceId": str,
        "InstanceName": str,
        "Tags": List["TagValuesTypeDef"],
        "ResourceDetails": "ResourceDetailsTypeDef",
        "ResourceUtilization": "ResourceUtilizationTypeDef",
        "ReservationCoveredHoursInLookbackPeriod": str,
        "SavingsPlansCoveredHoursInLookbackPeriod": str,
        "OnDemandHoursInLookbackPeriod": str,
        "TotalRunningHoursInLookbackPeriod": str,
        "MonthlyCost": str,
        "CurrencyCode": str,
    },
    total=False,
)

DateIntervalTypeDef = TypedDict(
    "DateIntervalTypeDef",
    {
        "Start": str,
        "End": str,
    },
)

DeleteAnomalyMonitorRequestRequestTypeDef = TypedDict(
    "DeleteAnomalyMonitorRequestRequestTypeDef",
    {
        "MonitorArn": str,
    },
)

DeleteAnomalySubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteAnomalySubscriptionRequestRequestTypeDef",
    {
        "SubscriptionArn": str,
    },
)

DeleteCostCategoryDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteCostCategoryDefinitionRequestRequestTypeDef",
    {
        "CostCategoryArn": str,
    },
)

DeleteCostCategoryDefinitionResponseTypeDef = TypedDict(
    "DeleteCostCategoryDefinitionResponseTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveEnd": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeCostCategoryDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeCostCategoryDefinitionRequestRequestTypeDef",
    {
        "CostCategoryArn": str,
    },
)
_OptionalDescribeCostCategoryDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeCostCategoryDefinitionRequestRequestTypeDef",
    {
        "EffectiveOn": str,
    },
    total=False,
)

class DescribeCostCategoryDefinitionRequestRequestTypeDef(
    _RequiredDescribeCostCategoryDefinitionRequestRequestTypeDef,
    _OptionalDescribeCostCategoryDefinitionRequestRequestTypeDef,
):
    pass

DescribeCostCategoryDefinitionResponseTypeDef = TypedDict(
    "DescribeCostCategoryDefinitionResponseTypeDef",
    {
        "CostCategory": "CostCategoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DimensionValuesTypeDef = TypedDict(
    "DimensionValuesTypeDef",
    {
        "Key": DimensionType,
        "Values": List[str],
        "MatchOptions": List[MatchOptionType],
    },
    total=False,
)

DimensionValuesWithAttributesTypeDef = TypedDict(
    "DimensionValuesWithAttributesTypeDef",
    {
        "Value": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)

DiskResourceUtilizationTypeDef = TypedDict(
    "DiskResourceUtilizationTypeDef",
    {
        "DiskReadOpsPerSecond": str,
        "DiskWriteOpsPerSecond": str,
        "DiskReadBytesPerSecond": str,
        "DiskWriteBytesPerSecond": str,
    },
    total=False,
)

EBSResourceUtilizationTypeDef = TypedDict(
    "EBSResourceUtilizationTypeDef",
    {
        "EbsReadOpsPerSecond": str,
        "EbsWriteOpsPerSecond": str,
        "EbsReadBytesPerSecond": str,
        "EbsWriteBytesPerSecond": str,
    },
    total=False,
)

EC2InstanceDetailsTypeDef = TypedDict(
    "EC2InstanceDetailsTypeDef",
    {
        "Family": str,
        "InstanceType": str,
        "Region": str,
        "AvailabilityZone": str,
        "Platform": str,
        "Tenancy": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)

EC2ResourceDetailsTypeDef = TypedDict(
    "EC2ResourceDetailsTypeDef",
    {
        "HourlyOnDemandRate": str,
        "InstanceType": str,
        "Platform": str,
        "Region": str,
        "Sku": str,
        "Memory": str,
        "NetworkPerformance": str,
        "Storage": str,
        "Vcpu": str,
    },
    total=False,
)

EC2ResourceUtilizationTypeDef = TypedDict(
    "EC2ResourceUtilizationTypeDef",
    {
        "MaxCpuUtilizationPercentage": str,
        "MaxMemoryUtilizationPercentage": str,
        "MaxStorageUtilizationPercentage": str,
        "EBSResourceUtilization": "EBSResourceUtilizationTypeDef",
        "DiskResourceUtilization": "DiskResourceUtilizationTypeDef",
        "NetworkResourceUtilization": "NetworkResourceUtilizationTypeDef",
    },
    total=False,
)

EC2SpecificationTypeDef = TypedDict(
    "EC2SpecificationTypeDef",
    {
        "OfferingClass": OfferingClassType,
    },
    total=False,
)

ESInstanceDetailsTypeDef = TypedDict(
    "ESInstanceDetailsTypeDef",
    {
        "InstanceClass": str,
        "InstanceSize": str,
        "Region": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)

ElastiCacheInstanceDetailsTypeDef = TypedDict(
    "ElastiCacheInstanceDetailsTypeDef",
    {
        "Family": str,
        "NodeType": str,
        "Region": str,
        "ProductDescription": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)

ExpressionTypeDef = TypedDict(
    "ExpressionTypeDef",
    {
        "Or": List[Dict[str, Any]],
        "And": List[Dict[str, Any]],
        "Not": Dict[str, Any],
        "Dimensions": "DimensionValuesTypeDef",
        "Tags": "TagValuesTypeDef",
        "CostCategories": "CostCategoryValuesTypeDef",
    },
    total=False,
)

ForecastResultTypeDef = TypedDict(
    "ForecastResultTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "MeanValue": str,
        "PredictionIntervalLowerBound": str,
        "PredictionIntervalUpperBound": str,
    },
    total=False,
)

_RequiredGetAnomaliesRequestRequestTypeDef = TypedDict(
    "_RequiredGetAnomaliesRequestRequestTypeDef",
    {
        "DateInterval": "AnomalyDateIntervalTypeDef",
    },
)
_OptionalGetAnomaliesRequestRequestTypeDef = TypedDict(
    "_OptionalGetAnomaliesRequestRequestTypeDef",
    {
        "MonitorArn": str,
        "Feedback": AnomalyFeedbackTypeType,
        "TotalImpact": "TotalImpactFilterTypeDef",
        "NextPageToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetAnomaliesRequestRequestTypeDef(
    _RequiredGetAnomaliesRequestRequestTypeDef, _OptionalGetAnomaliesRequestRequestTypeDef
):
    pass

GetAnomaliesResponseTypeDef = TypedDict(
    "GetAnomaliesResponseTypeDef",
    {
        "Anomalies": List["AnomalyTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAnomalyMonitorsRequestRequestTypeDef = TypedDict(
    "GetAnomalyMonitorsRequestRequestTypeDef",
    {
        "MonitorArnList": List[str],
        "NextPageToken": str,
        "MaxResults": int,
    },
    total=False,
)

GetAnomalyMonitorsResponseTypeDef = TypedDict(
    "GetAnomalyMonitorsResponseTypeDef",
    {
        "AnomalyMonitors": List["AnomalyMonitorTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAnomalySubscriptionsRequestRequestTypeDef = TypedDict(
    "GetAnomalySubscriptionsRequestRequestTypeDef",
    {
        "SubscriptionArnList": List[str],
        "MonitorArn": str,
        "NextPageToken": str,
        "MaxResults": int,
    },
    total=False,
)

GetAnomalySubscriptionsResponseTypeDef = TypedDict(
    "GetAnomalySubscriptionsResponseTypeDef",
    {
        "AnomalySubscriptions": List["AnomalySubscriptionTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCostAndUsageRequestRequestTypeDef = TypedDict(
    "_RequiredGetCostAndUsageRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Granularity": GranularityType,
        "Metrics": List[str],
    },
)
_OptionalGetCostAndUsageRequestRequestTypeDef = TypedDict(
    "_OptionalGetCostAndUsageRequestRequestTypeDef",
    {
        "Filter": "ExpressionTypeDef",
        "GroupBy": List["GroupDefinitionTypeDef"],
        "NextPageToken": str,
    },
    total=False,
)

class GetCostAndUsageRequestRequestTypeDef(
    _RequiredGetCostAndUsageRequestRequestTypeDef, _OptionalGetCostAndUsageRequestRequestTypeDef
):
    pass

GetCostAndUsageResponseTypeDef = TypedDict(
    "GetCostAndUsageResponseTypeDef",
    {
        "NextPageToken": str,
        "GroupDefinitions": List["GroupDefinitionTypeDef"],
        "ResultsByTime": List["ResultByTimeTypeDef"],
        "DimensionValueAttributes": List["DimensionValuesWithAttributesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCostAndUsageWithResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredGetCostAndUsageWithResourcesRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Granularity": GranularityType,
        "Filter": "ExpressionTypeDef",
    },
)
_OptionalGetCostAndUsageWithResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalGetCostAndUsageWithResourcesRequestRequestTypeDef",
    {
        "Metrics": List[str],
        "GroupBy": List["GroupDefinitionTypeDef"],
        "NextPageToken": str,
    },
    total=False,
)

class GetCostAndUsageWithResourcesRequestRequestTypeDef(
    _RequiredGetCostAndUsageWithResourcesRequestRequestTypeDef,
    _OptionalGetCostAndUsageWithResourcesRequestRequestTypeDef,
):
    pass

GetCostAndUsageWithResourcesResponseTypeDef = TypedDict(
    "GetCostAndUsageWithResourcesResponseTypeDef",
    {
        "NextPageToken": str,
        "GroupDefinitions": List["GroupDefinitionTypeDef"],
        "ResultsByTime": List["ResultByTimeTypeDef"],
        "DimensionValueAttributes": List["DimensionValuesWithAttributesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCostCategoriesRequestRequestTypeDef = TypedDict(
    "_RequiredGetCostCategoriesRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
    },
)
_OptionalGetCostCategoriesRequestRequestTypeDef = TypedDict(
    "_OptionalGetCostCategoriesRequestRequestTypeDef",
    {
        "SearchString": str,
        "CostCategoryName": str,
        "Filter": "ExpressionTypeDef",
        "SortBy": List["SortDefinitionTypeDef"],
        "MaxResults": int,
        "NextPageToken": str,
    },
    total=False,
)

class GetCostCategoriesRequestRequestTypeDef(
    _RequiredGetCostCategoriesRequestRequestTypeDef, _OptionalGetCostCategoriesRequestRequestTypeDef
):
    pass

GetCostCategoriesResponseTypeDef = TypedDict(
    "GetCostCategoriesResponseTypeDef",
    {
        "NextPageToken": str,
        "CostCategoryNames": List[str],
        "CostCategoryValues": List[str],
        "ReturnSize": int,
        "TotalSize": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCostForecastRequestRequestTypeDef = TypedDict(
    "_RequiredGetCostForecastRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Metric": MetricType,
        "Granularity": GranularityType,
    },
)
_OptionalGetCostForecastRequestRequestTypeDef = TypedDict(
    "_OptionalGetCostForecastRequestRequestTypeDef",
    {
        "Filter": "ExpressionTypeDef",
        "PredictionIntervalLevel": int,
    },
    total=False,
)

class GetCostForecastRequestRequestTypeDef(
    _RequiredGetCostForecastRequestRequestTypeDef, _OptionalGetCostForecastRequestRequestTypeDef
):
    pass

GetCostForecastResponseTypeDef = TypedDict(
    "GetCostForecastResponseTypeDef",
    {
        "Total": "MetricValueTypeDef",
        "ForecastResultsByTime": List["ForecastResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDimensionValuesRequestRequestTypeDef = TypedDict(
    "_RequiredGetDimensionValuesRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Dimension": DimensionType,
    },
)
_OptionalGetDimensionValuesRequestRequestTypeDef = TypedDict(
    "_OptionalGetDimensionValuesRequestRequestTypeDef",
    {
        "SearchString": str,
        "Context": ContextType,
        "Filter": "ExpressionTypeDef",
        "SortBy": List["SortDefinitionTypeDef"],
        "MaxResults": int,
        "NextPageToken": str,
    },
    total=False,
)

class GetDimensionValuesRequestRequestTypeDef(
    _RequiredGetDimensionValuesRequestRequestTypeDef,
    _OptionalGetDimensionValuesRequestRequestTypeDef,
):
    pass

GetDimensionValuesResponseTypeDef = TypedDict(
    "GetDimensionValuesResponseTypeDef",
    {
        "DimensionValues": List["DimensionValuesWithAttributesTypeDef"],
        "ReturnSize": int,
        "TotalSize": int,
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetReservationCoverageRequestRequestTypeDef = TypedDict(
    "_RequiredGetReservationCoverageRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
    },
)
_OptionalGetReservationCoverageRequestRequestTypeDef = TypedDict(
    "_OptionalGetReservationCoverageRequestRequestTypeDef",
    {
        "GroupBy": List["GroupDefinitionTypeDef"],
        "Granularity": GranularityType,
        "Filter": "ExpressionTypeDef",
        "Metrics": List[str],
        "NextPageToken": str,
        "SortBy": "SortDefinitionTypeDef",
        "MaxResults": int,
    },
    total=False,
)

class GetReservationCoverageRequestRequestTypeDef(
    _RequiredGetReservationCoverageRequestRequestTypeDef,
    _OptionalGetReservationCoverageRequestRequestTypeDef,
):
    pass

GetReservationCoverageResponseTypeDef = TypedDict(
    "GetReservationCoverageResponseTypeDef",
    {
        "CoveragesByTime": List["CoverageByTimeTypeDef"],
        "Total": "CoverageTypeDef",
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetReservationPurchaseRecommendationRequestRequestTypeDef = TypedDict(
    "_RequiredGetReservationPurchaseRecommendationRequestRequestTypeDef",
    {
        "Service": str,
    },
)
_OptionalGetReservationPurchaseRecommendationRequestRequestTypeDef = TypedDict(
    "_OptionalGetReservationPurchaseRecommendationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Filter": "ExpressionTypeDef",
        "AccountScope": AccountScopeType,
        "LookbackPeriodInDays": LookbackPeriodInDaysType,
        "TermInYears": TermInYearsType,
        "PaymentOption": PaymentOptionType,
        "ServiceSpecification": "ServiceSpecificationTypeDef",
        "PageSize": int,
        "NextPageToken": str,
    },
    total=False,
)

class GetReservationPurchaseRecommendationRequestRequestTypeDef(
    _RequiredGetReservationPurchaseRecommendationRequestRequestTypeDef,
    _OptionalGetReservationPurchaseRecommendationRequestRequestTypeDef,
):
    pass

GetReservationPurchaseRecommendationResponseTypeDef = TypedDict(
    "GetReservationPurchaseRecommendationResponseTypeDef",
    {
        "Metadata": "ReservationPurchaseRecommendationMetadataTypeDef",
        "Recommendations": List["ReservationPurchaseRecommendationTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetReservationUtilizationRequestRequestTypeDef = TypedDict(
    "_RequiredGetReservationUtilizationRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
    },
)
_OptionalGetReservationUtilizationRequestRequestTypeDef = TypedDict(
    "_OptionalGetReservationUtilizationRequestRequestTypeDef",
    {
        "GroupBy": List["GroupDefinitionTypeDef"],
        "Granularity": GranularityType,
        "Filter": "ExpressionTypeDef",
        "SortBy": "SortDefinitionTypeDef",
        "NextPageToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetReservationUtilizationRequestRequestTypeDef(
    _RequiredGetReservationUtilizationRequestRequestTypeDef,
    _OptionalGetReservationUtilizationRequestRequestTypeDef,
):
    pass

GetReservationUtilizationResponseTypeDef = TypedDict(
    "GetReservationUtilizationResponseTypeDef",
    {
        "UtilizationsByTime": List["UtilizationByTimeTypeDef"],
        "Total": "ReservationAggregatesTypeDef",
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRightsizingRecommendationRequestRequestTypeDef = TypedDict(
    "_RequiredGetRightsizingRecommendationRequestRequestTypeDef",
    {
        "Service": str,
    },
)
_OptionalGetRightsizingRecommendationRequestRequestTypeDef = TypedDict(
    "_OptionalGetRightsizingRecommendationRequestRequestTypeDef",
    {
        "Filter": "ExpressionTypeDef",
        "Configuration": "RightsizingRecommendationConfigurationTypeDef",
        "PageSize": int,
        "NextPageToken": str,
    },
    total=False,
)

class GetRightsizingRecommendationRequestRequestTypeDef(
    _RequiredGetRightsizingRecommendationRequestRequestTypeDef,
    _OptionalGetRightsizingRecommendationRequestRequestTypeDef,
):
    pass

GetRightsizingRecommendationResponseTypeDef = TypedDict(
    "GetRightsizingRecommendationResponseTypeDef",
    {
        "Metadata": "RightsizingRecommendationMetadataTypeDef",
        "Summary": "RightsizingRecommendationSummaryTypeDef",
        "RightsizingRecommendations": List["RightsizingRecommendationTypeDef"],
        "NextPageToken": str,
        "Configuration": "RightsizingRecommendationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSavingsPlansCoverageRequestRequestTypeDef = TypedDict(
    "_RequiredGetSavingsPlansCoverageRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
    },
)
_OptionalGetSavingsPlansCoverageRequestRequestTypeDef = TypedDict(
    "_OptionalGetSavingsPlansCoverageRequestRequestTypeDef",
    {
        "GroupBy": List["GroupDefinitionTypeDef"],
        "Granularity": GranularityType,
        "Filter": "ExpressionTypeDef",
        "Metrics": List[str],
        "NextToken": str,
        "MaxResults": int,
        "SortBy": "SortDefinitionTypeDef",
    },
    total=False,
)

class GetSavingsPlansCoverageRequestRequestTypeDef(
    _RequiredGetSavingsPlansCoverageRequestRequestTypeDef,
    _OptionalGetSavingsPlansCoverageRequestRequestTypeDef,
):
    pass

GetSavingsPlansCoverageResponseTypeDef = TypedDict(
    "GetSavingsPlansCoverageResponseTypeDef",
    {
        "SavingsPlansCoverages": List["SavingsPlansCoverageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSavingsPlansPurchaseRecommendationRequestRequestTypeDef = TypedDict(
    "_RequiredGetSavingsPlansPurchaseRecommendationRequestRequestTypeDef",
    {
        "SavingsPlansType": SupportedSavingsPlansTypeType,
        "TermInYears": TermInYearsType,
        "PaymentOption": PaymentOptionType,
        "LookbackPeriodInDays": LookbackPeriodInDaysType,
    },
)
_OptionalGetSavingsPlansPurchaseRecommendationRequestRequestTypeDef = TypedDict(
    "_OptionalGetSavingsPlansPurchaseRecommendationRequestRequestTypeDef",
    {
        "AccountScope": AccountScopeType,
        "NextPageToken": str,
        "PageSize": int,
        "Filter": "ExpressionTypeDef",
    },
    total=False,
)

class GetSavingsPlansPurchaseRecommendationRequestRequestTypeDef(
    _RequiredGetSavingsPlansPurchaseRecommendationRequestRequestTypeDef,
    _OptionalGetSavingsPlansPurchaseRecommendationRequestRequestTypeDef,
):
    pass

GetSavingsPlansPurchaseRecommendationResponseTypeDef = TypedDict(
    "GetSavingsPlansPurchaseRecommendationResponseTypeDef",
    {
        "Metadata": "SavingsPlansPurchaseRecommendationMetadataTypeDef",
        "SavingsPlansPurchaseRecommendation": "SavingsPlansPurchaseRecommendationTypeDef",
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSavingsPlansUtilizationDetailsRequestRequestTypeDef = TypedDict(
    "_RequiredGetSavingsPlansUtilizationDetailsRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
    },
)
_OptionalGetSavingsPlansUtilizationDetailsRequestRequestTypeDef = TypedDict(
    "_OptionalGetSavingsPlansUtilizationDetailsRequestRequestTypeDef",
    {
        "Filter": "ExpressionTypeDef",
        "DataType": List[SavingsPlansDataTypeType],
        "NextToken": str,
        "MaxResults": int,
        "SortBy": "SortDefinitionTypeDef",
    },
    total=False,
)

class GetSavingsPlansUtilizationDetailsRequestRequestTypeDef(
    _RequiredGetSavingsPlansUtilizationDetailsRequestRequestTypeDef,
    _OptionalGetSavingsPlansUtilizationDetailsRequestRequestTypeDef,
):
    pass

GetSavingsPlansUtilizationDetailsResponseTypeDef = TypedDict(
    "GetSavingsPlansUtilizationDetailsResponseTypeDef",
    {
        "SavingsPlansUtilizationDetails": List["SavingsPlansUtilizationDetailTypeDef"],
        "Total": "SavingsPlansUtilizationAggregatesTypeDef",
        "TimePeriod": "DateIntervalTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSavingsPlansUtilizationRequestRequestTypeDef = TypedDict(
    "_RequiredGetSavingsPlansUtilizationRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
    },
)
_OptionalGetSavingsPlansUtilizationRequestRequestTypeDef = TypedDict(
    "_OptionalGetSavingsPlansUtilizationRequestRequestTypeDef",
    {
        "Granularity": GranularityType,
        "Filter": "ExpressionTypeDef",
        "SortBy": "SortDefinitionTypeDef",
    },
    total=False,
)

class GetSavingsPlansUtilizationRequestRequestTypeDef(
    _RequiredGetSavingsPlansUtilizationRequestRequestTypeDef,
    _OptionalGetSavingsPlansUtilizationRequestRequestTypeDef,
):
    pass

GetSavingsPlansUtilizationResponseTypeDef = TypedDict(
    "GetSavingsPlansUtilizationResponseTypeDef",
    {
        "SavingsPlansUtilizationsByTime": List["SavingsPlansUtilizationByTimeTypeDef"],
        "Total": "SavingsPlansUtilizationAggregatesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTagsRequestRequestTypeDef = TypedDict(
    "_RequiredGetTagsRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
    },
)
_OptionalGetTagsRequestRequestTypeDef = TypedDict(
    "_OptionalGetTagsRequestRequestTypeDef",
    {
        "SearchString": str,
        "TagKey": str,
        "Filter": "ExpressionTypeDef",
        "SortBy": List["SortDefinitionTypeDef"],
        "MaxResults": int,
        "NextPageToken": str,
    },
    total=False,
)

class GetTagsRequestRequestTypeDef(
    _RequiredGetTagsRequestRequestTypeDef, _OptionalGetTagsRequestRequestTypeDef
):
    pass

GetTagsResponseTypeDef = TypedDict(
    "GetTagsResponseTypeDef",
    {
        "NextPageToken": str,
        "Tags": List[str],
        "ReturnSize": int,
        "TotalSize": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetUsageForecastRequestRequestTypeDef = TypedDict(
    "_RequiredGetUsageForecastRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Metric": MetricType,
        "Granularity": GranularityType,
    },
)
_OptionalGetUsageForecastRequestRequestTypeDef = TypedDict(
    "_OptionalGetUsageForecastRequestRequestTypeDef",
    {
        "Filter": "ExpressionTypeDef",
        "PredictionIntervalLevel": int,
    },
    total=False,
)

class GetUsageForecastRequestRequestTypeDef(
    _RequiredGetUsageForecastRequestRequestTypeDef, _OptionalGetUsageForecastRequestRequestTypeDef
):
    pass

GetUsageForecastResponseTypeDef = TypedDict(
    "GetUsageForecastResponseTypeDef",
    {
        "Total": "MetricValueTypeDef",
        "ForecastResultsByTime": List["ForecastResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupDefinitionTypeDef = TypedDict(
    "GroupDefinitionTypeDef",
    {
        "Type": GroupDefinitionTypeType,
        "Key": str,
    },
    total=False,
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "Keys": List[str],
        "Metrics": Dict[str, "MetricValueTypeDef"],
    },
    total=False,
)

_RequiredImpactTypeDef = TypedDict(
    "_RequiredImpactTypeDef",
    {
        "MaxImpact": float,
    },
)
_OptionalImpactTypeDef = TypedDict(
    "_OptionalImpactTypeDef",
    {
        "TotalImpact": float,
    },
    total=False,
)

class ImpactTypeDef(_RequiredImpactTypeDef, _OptionalImpactTypeDef):
    pass

InstanceDetailsTypeDef = TypedDict(
    "InstanceDetailsTypeDef",
    {
        "EC2InstanceDetails": "EC2InstanceDetailsTypeDef",
        "RDSInstanceDetails": "RDSInstanceDetailsTypeDef",
        "RedshiftInstanceDetails": "RedshiftInstanceDetailsTypeDef",
        "ElastiCacheInstanceDetails": "ElastiCacheInstanceDetailsTypeDef",
        "ESInstanceDetails": "ESInstanceDetailsTypeDef",
    },
    total=False,
)

ListCostCategoryDefinitionsRequestRequestTypeDef = TypedDict(
    "ListCostCategoryDefinitionsRequestRequestTypeDef",
    {
        "EffectiveOn": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListCostCategoryDefinitionsResponseTypeDef = TypedDict(
    "ListCostCategoryDefinitionsResponseTypeDef",
    {
        "CostCategoryReferences": List["CostCategoryReferenceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricValueTypeDef = TypedDict(
    "MetricValueTypeDef",
    {
        "Amount": str,
        "Unit": str,
    },
    total=False,
)

ModifyRecommendationDetailTypeDef = TypedDict(
    "ModifyRecommendationDetailTypeDef",
    {
        "TargetInstances": List["TargetInstanceTypeDef"],
    },
    total=False,
)

NetworkResourceUtilizationTypeDef = TypedDict(
    "NetworkResourceUtilizationTypeDef",
    {
        "NetworkInBytesPerSecond": str,
        "NetworkOutBytesPerSecond": str,
        "NetworkPacketsInPerSecond": str,
        "NetworkPacketsOutPerSecond": str,
    },
    total=False,
)

ProvideAnomalyFeedbackRequestRequestTypeDef = TypedDict(
    "ProvideAnomalyFeedbackRequestRequestTypeDef",
    {
        "AnomalyId": str,
        "Feedback": AnomalyFeedbackTypeType,
    },
)

ProvideAnomalyFeedbackResponseTypeDef = TypedDict(
    "ProvideAnomalyFeedbackResponseTypeDef",
    {
        "AnomalyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RDSInstanceDetailsTypeDef = TypedDict(
    "RDSInstanceDetailsTypeDef",
    {
        "Family": str,
        "InstanceType": str,
        "Region": str,
        "DatabaseEngine": str,
        "DatabaseEdition": str,
        "DeploymentOption": str,
        "LicenseModel": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)

RedshiftInstanceDetailsTypeDef = TypedDict(
    "RedshiftInstanceDetailsTypeDef",
    {
        "Family": str,
        "NodeType": str,
        "Region": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)

ReservationAggregatesTypeDef = TypedDict(
    "ReservationAggregatesTypeDef",
    {
        "UtilizationPercentage": str,
        "UtilizationPercentageInUnits": str,
        "PurchasedHours": str,
        "PurchasedUnits": str,
        "TotalActualHours": str,
        "TotalActualUnits": str,
        "UnusedHours": str,
        "UnusedUnits": str,
        "OnDemandCostOfRIHoursUsed": str,
        "NetRISavings": str,
        "TotalPotentialRISavings": str,
        "AmortizedUpfrontFee": str,
        "AmortizedRecurringFee": str,
        "TotalAmortizedFee": str,
        "RICostForUnusedHours": str,
        "RealizedSavings": str,
        "UnrealizedSavings": str,
    },
    total=False,
)

ReservationCoverageGroupTypeDef = TypedDict(
    "ReservationCoverageGroupTypeDef",
    {
        "Attributes": Dict[str, str],
        "Coverage": "CoverageTypeDef",
    },
    total=False,
)

ReservationPurchaseRecommendationDetailTypeDef = TypedDict(
    "ReservationPurchaseRecommendationDetailTypeDef",
    {
        "AccountId": str,
        "InstanceDetails": "InstanceDetailsTypeDef",
        "RecommendedNumberOfInstancesToPurchase": str,
        "RecommendedNormalizedUnitsToPurchase": str,
        "MinimumNumberOfInstancesUsedPerHour": str,
        "MinimumNormalizedUnitsUsedPerHour": str,
        "MaximumNumberOfInstancesUsedPerHour": str,
        "MaximumNormalizedUnitsUsedPerHour": str,
        "AverageNumberOfInstancesUsedPerHour": str,
        "AverageNormalizedUnitsUsedPerHour": str,
        "AverageUtilization": str,
        "EstimatedBreakEvenInMonths": str,
        "CurrencyCode": str,
        "EstimatedMonthlySavingsAmount": str,
        "EstimatedMonthlySavingsPercentage": str,
        "EstimatedMonthlyOnDemandCost": str,
        "EstimatedReservationCostForLookbackPeriod": str,
        "UpfrontCost": str,
        "RecurringStandardMonthlyCost": str,
    },
    total=False,
)

ReservationPurchaseRecommendationMetadataTypeDef = TypedDict(
    "ReservationPurchaseRecommendationMetadataTypeDef",
    {
        "RecommendationId": str,
        "GenerationTimestamp": str,
    },
    total=False,
)

ReservationPurchaseRecommendationSummaryTypeDef = TypedDict(
    "ReservationPurchaseRecommendationSummaryTypeDef",
    {
        "TotalEstimatedMonthlySavingsAmount": str,
        "TotalEstimatedMonthlySavingsPercentage": str,
        "CurrencyCode": str,
    },
    total=False,
)

ReservationPurchaseRecommendationTypeDef = TypedDict(
    "ReservationPurchaseRecommendationTypeDef",
    {
        "AccountScope": AccountScopeType,
        "LookbackPeriodInDays": LookbackPeriodInDaysType,
        "TermInYears": TermInYearsType,
        "PaymentOption": PaymentOptionType,
        "ServiceSpecification": "ServiceSpecificationTypeDef",
        "RecommendationDetails": List["ReservationPurchaseRecommendationDetailTypeDef"],
        "RecommendationSummary": "ReservationPurchaseRecommendationSummaryTypeDef",
    },
    total=False,
)

ReservationUtilizationGroupTypeDef = TypedDict(
    "ReservationUtilizationGroupTypeDef",
    {
        "Key": str,
        "Value": str,
        "Attributes": Dict[str, str],
        "Utilization": "ReservationAggregatesTypeDef",
    },
    total=False,
)

ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "EC2ResourceDetails": "EC2ResourceDetailsTypeDef",
    },
    total=False,
)

ResourceUtilizationTypeDef = TypedDict(
    "ResourceUtilizationTypeDef",
    {
        "EC2ResourceUtilization": "EC2ResourceUtilizationTypeDef",
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

ResultByTimeTypeDef = TypedDict(
    "ResultByTimeTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Total": Dict[str, "MetricValueTypeDef"],
        "Groups": List["GroupTypeDef"],
        "Estimated": bool,
    },
    total=False,
)

RightsizingRecommendationConfigurationTypeDef = TypedDict(
    "RightsizingRecommendationConfigurationTypeDef",
    {
        "RecommendationTarget": RecommendationTargetType,
        "BenefitsConsidered": bool,
    },
)

RightsizingRecommendationMetadataTypeDef = TypedDict(
    "RightsizingRecommendationMetadataTypeDef",
    {
        "RecommendationId": str,
        "GenerationTimestamp": str,
        "LookbackPeriodInDays": LookbackPeriodInDaysType,
        "AdditionalMetadata": str,
    },
    total=False,
)

RightsizingRecommendationSummaryTypeDef = TypedDict(
    "RightsizingRecommendationSummaryTypeDef",
    {
        "TotalRecommendationCount": str,
        "EstimatedTotalMonthlySavingsAmount": str,
        "SavingsCurrencyCode": str,
        "SavingsPercentage": str,
    },
    total=False,
)

RightsizingRecommendationTypeDef = TypedDict(
    "RightsizingRecommendationTypeDef",
    {
        "AccountId": str,
        "CurrentInstance": "CurrentInstanceTypeDef",
        "RightsizingType": RightsizingTypeType,
        "ModifyRecommendationDetail": "ModifyRecommendationDetailTypeDef",
        "TerminateRecommendationDetail": "TerminateRecommendationDetailTypeDef",
        "FindingReasonCodes": List[FindingReasonCodeType],
    },
    total=False,
)

RootCauseTypeDef = TypedDict(
    "RootCauseTypeDef",
    {
        "Service": str,
        "Region": str,
        "LinkedAccount": str,
        "UsageType": str,
    },
    total=False,
)

SavingsPlansAmortizedCommitmentTypeDef = TypedDict(
    "SavingsPlansAmortizedCommitmentTypeDef",
    {
        "AmortizedRecurringCommitment": str,
        "AmortizedUpfrontCommitment": str,
        "TotalAmortizedCommitment": str,
    },
    total=False,
)

SavingsPlansCoverageDataTypeDef = TypedDict(
    "SavingsPlansCoverageDataTypeDef",
    {
        "SpendCoveredBySavingsPlans": str,
        "OnDemandCost": str,
        "TotalCost": str,
        "CoveragePercentage": str,
    },
    total=False,
)

SavingsPlansCoverageTypeDef = TypedDict(
    "SavingsPlansCoverageTypeDef",
    {
        "Attributes": Dict[str, str],
        "Coverage": "SavingsPlansCoverageDataTypeDef",
        "TimePeriod": "DateIntervalTypeDef",
    },
    total=False,
)

SavingsPlansDetailsTypeDef = TypedDict(
    "SavingsPlansDetailsTypeDef",
    {
        "Region": str,
        "InstanceFamily": str,
        "OfferingId": str,
    },
    total=False,
)

SavingsPlansPurchaseRecommendationDetailTypeDef = TypedDict(
    "SavingsPlansPurchaseRecommendationDetailTypeDef",
    {
        "SavingsPlansDetails": "SavingsPlansDetailsTypeDef",
        "AccountId": str,
        "UpfrontCost": str,
        "EstimatedROI": str,
        "CurrencyCode": str,
        "EstimatedSPCost": str,
        "EstimatedOnDemandCost": str,
        "EstimatedOnDemandCostWithCurrentCommitment": str,
        "EstimatedSavingsAmount": str,
        "EstimatedSavingsPercentage": str,
        "HourlyCommitmentToPurchase": str,
        "EstimatedAverageUtilization": str,
        "EstimatedMonthlySavingsAmount": str,
        "CurrentMinimumHourlyOnDemandSpend": str,
        "CurrentMaximumHourlyOnDemandSpend": str,
        "CurrentAverageHourlyOnDemandSpend": str,
    },
    total=False,
)

SavingsPlansPurchaseRecommendationMetadataTypeDef = TypedDict(
    "SavingsPlansPurchaseRecommendationMetadataTypeDef",
    {
        "RecommendationId": str,
        "GenerationTimestamp": str,
        "AdditionalMetadata": str,
    },
    total=False,
)

SavingsPlansPurchaseRecommendationSummaryTypeDef = TypedDict(
    "SavingsPlansPurchaseRecommendationSummaryTypeDef",
    {
        "EstimatedROI": str,
        "CurrencyCode": str,
        "EstimatedTotalCost": str,
        "CurrentOnDemandSpend": str,
        "EstimatedSavingsAmount": str,
        "TotalRecommendationCount": str,
        "DailyCommitmentToPurchase": str,
        "HourlyCommitmentToPurchase": str,
        "EstimatedSavingsPercentage": str,
        "EstimatedMonthlySavingsAmount": str,
        "EstimatedOnDemandCostWithCurrentCommitment": str,
    },
    total=False,
)

SavingsPlansPurchaseRecommendationTypeDef = TypedDict(
    "SavingsPlansPurchaseRecommendationTypeDef",
    {
        "AccountScope": AccountScopeType,
        "SavingsPlansType": SupportedSavingsPlansTypeType,
        "TermInYears": TermInYearsType,
        "PaymentOption": PaymentOptionType,
        "LookbackPeriodInDays": LookbackPeriodInDaysType,
        "SavingsPlansPurchaseRecommendationDetails": List[
            "SavingsPlansPurchaseRecommendationDetailTypeDef"
        ],
        "SavingsPlansPurchaseRecommendationSummary": "SavingsPlansPurchaseRecommendationSummaryTypeDef",
    },
    total=False,
)

SavingsPlansSavingsTypeDef = TypedDict(
    "SavingsPlansSavingsTypeDef",
    {
        "NetSavings": str,
        "OnDemandCostEquivalent": str,
    },
    total=False,
)

_RequiredSavingsPlansUtilizationAggregatesTypeDef = TypedDict(
    "_RequiredSavingsPlansUtilizationAggregatesTypeDef",
    {
        "Utilization": "SavingsPlansUtilizationTypeDef",
    },
)
_OptionalSavingsPlansUtilizationAggregatesTypeDef = TypedDict(
    "_OptionalSavingsPlansUtilizationAggregatesTypeDef",
    {
        "Savings": "SavingsPlansSavingsTypeDef",
        "AmortizedCommitment": "SavingsPlansAmortizedCommitmentTypeDef",
    },
    total=False,
)

class SavingsPlansUtilizationAggregatesTypeDef(
    _RequiredSavingsPlansUtilizationAggregatesTypeDef,
    _OptionalSavingsPlansUtilizationAggregatesTypeDef,
):
    pass

_RequiredSavingsPlansUtilizationByTimeTypeDef = TypedDict(
    "_RequiredSavingsPlansUtilizationByTimeTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Utilization": "SavingsPlansUtilizationTypeDef",
    },
)
_OptionalSavingsPlansUtilizationByTimeTypeDef = TypedDict(
    "_OptionalSavingsPlansUtilizationByTimeTypeDef",
    {
        "Savings": "SavingsPlansSavingsTypeDef",
        "AmortizedCommitment": "SavingsPlansAmortizedCommitmentTypeDef",
    },
    total=False,
)

class SavingsPlansUtilizationByTimeTypeDef(
    _RequiredSavingsPlansUtilizationByTimeTypeDef, _OptionalSavingsPlansUtilizationByTimeTypeDef
):
    pass

SavingsPlansUtilizationDetailTypeDef = TypedDict(
    "SavingsPlansUtilizationDetailTypeDef",
    {
        "SavingsPlanArn": str,
        "Attributes": Dict[str, str],
        "Utilization": "SavingsPlansUtilizationTypeDef",
        "Savings": "SavingsPlansSavingsTypeDef",
        "AmortizedCommitment": "SavingsPlansAmortizedCommitmentTypeDef",
    },
    total=False,
)

SavingsPlansUtilizationTypeDef = TypedDict(
    "SavingsPlansUtilizationTypeDef",
    {
        "TotalCommitment": str,
        "UsedCommitment": str,
        "UnusedCommitment": str,
        "UtilizationPercentage": str,
    },
    total=False,
)

ServiceSpecificationTypeDef = TypedDict(
    "ServiceSpecificationTypeDef",
    {
        "EC2Specification": "EC2SpecificationTypeDef",
    },
    total=False,
)

_RequiredSortDefinitionTypeDef = TypedDict(
    "_RequiredSortDefinitionTypeDef",
    {
        "Key": str,
    },
)
_OptionalSortDefinitionTypeDef = TypedDict(
    "_OptionalSortDefinitionTypeDef",
    {
        "SortOrder": SortOrderType,
    },
    total=False,
)

class SortDefinitionTypeDef(_RequiredSortDefinitionTypeDef, _OptionalSortDefinitionTypeDef):
    pass

SubscriberTypeDef = TypedDict(
    "SubscriberTypeDef",
    {
        "Address": str,
        "Type": SubscriberTypeType,
        "Status": SubscriberStatusType,
    },
    total=False,
)

TagValuesTypeDef = TypedDict(
    "TagValuesTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MatchOptions": List[MatchOptionType],
    },
    total=False,
)

TargetInstanceTypeDef = TypedDict(
    "TargetInstanceTypeDef",
    {
        "EstimatedMonthlyCost": str,
        "EstimatedMonthlySavings": str,
        "CurrencyCode": str,
        "DefaultTargetInstance": bool,
        "ResourceDetails": "ResourceDetailsTypeDef",
        "ExpectedResourceUtilization": "ResourceUtilizationTypeDef",
        "PlatformDifferences": List[PlatformDifferenceType],
    },
    total=False,
)

TerminateRecommendationDetailTypeDef = TypedDict(
    "TerminateRecommendationDetailTypeDef",
    {
        "EstimatedMonthlySavings": str,
        "CurrencyCode": str,
    },
    total=False,
)

_RequiredTotalImpactFilterTypeDef = TypedDict(
    "_RequiredTotalImpactFilterTypeDef",
    {
        "NumericOperator": NumericOperatorType,
        "StartValue": float,
    },
)
_OptionalTotalImpactFilterTypeDef = TypedDict(
    "_OptionalTotalImpactFilterTypeDef",
    {
        "EndValue": float,
    },
    total=False,
)

class TotalImpactFilterTypeDef(
    _RequiredTotalImpactFilterTypeDef, _OptionalTotalImpactFilterTypeDef
):
    pass

_RequiredUpdateAnomalyMonitorRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAnomalyMonitorRequestRequestTypeDef",
    {
        "MonitorArn": str,
    },
)
_OptionalUpdateAnomalyMonitorRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAnomalyMonitorRequestRequestTypeDef",
    {
        "MonitorName": str,
    },
    total=False,
)

class UpdateAnomalyMonitorRequestRequestTypeDef(
    _RequiredUpdateAnomalyMonitorRequestRequestTypeDef,
    _OptionalUpdateAnomalyMonitorRequestRequestTypeDef,
):
    pass

UpdateAnomalyMonitorResponseTypeDef = TypedDict(
    "UpdateAnomalyMonitorResponseTypeDef",
    {
        "MonitorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAnomalySubscriptionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAnomalySubscriptionRequestRequestTypeDef",
    {
        "SubscriptionArn": str,
    },
)
_OptionalUpdateAnomalySubscriptionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAnomalySubscriptionRequestRequestTypeDef",
    {
        "Threshold": float,
        "Frequency": AnomalySubscriptionFrequencyType,
        "MonitorArnList": List[str],
        "Subscribers": List["SubscriberTypeDef"],
        "SubscriptionName": str,
    },
    total=False,
)

class UpdateAnomalySubscriptionRequestRequestTypeDef(
    _RequiredUpdateAnomalySubscriptionRequestRequestTypeDef,
    _OptionalUpdateAnomalySubscriptionRequestRequestTypeDef,
):
    pass

UpdateAnomalySubscriptionResponseTypeDef = TypedDict(
    "UpdateAnomalySubscriptionResponseTypeDef",
    {
        "SubscriptionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateCostCategoryDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCostCategoryDefinitionRequestRequestTypeDef",
    {
        "CostCategoryArn": str,
        "RuleVersion": Literal["CostCategoryExpression.v1"],
        "Rules": List["CostCategoryRuleTypeDef"],
    },
)
_OptionalUpdateCostCategoryDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCostCategoryDefinitionRequestRequestTypeDef",
    {
        "DefaultValue": str,
    },
    total=False,
)

class UpdateCostCategoryDefinitionRequestRequestTypeDef(
    _RequiredUpdateCostCategoryDefinitionRequestRequestTypeDef,
    _OptionalUpdateCostCategoryDefinitionRequestRequestTypeDef,
):
    pass

UpdateCostCategoryDefinitionResponseTypeDef = TypedDict(
    "UpdateCostCategoryDefinitionResponseTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveStart": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UtilizationByTimeTypeDef = TypedDict(
    "UtilizationByTimeTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Groups": List["ReservationUtilizationGroupTypeDef"],
        "Total": "ReservationAggregatesTypeDef",
    },
    total=False,
)
