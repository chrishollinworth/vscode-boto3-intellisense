"""
Type annotations for devops-guru service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/type_defs.html)

Usage::

    ```python
    from mypy_boto3_devops_guru.type_defs import AddNotificationChannelRequestRequestTypeDef

    data: AddNotificationChannelRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AnomalySeverityType,
    AnomalyStatusType,
    CloudWatchMetricsStatType,
    CostEstimationServiceResourceStateType,
    CostEstimationStatusType,
    EventClassType,
    EventDataSourceType,
    InsightFeedbackOptionType,
    InsightSeverityType,
    InsightStatusType,
    InsightTypeType,
    LocaleType,
    OptInStatusType,
    ResourceCollectionTypeType,
    ServiceNameType,
    UpdateResourceCollectionActionType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddNotificationChannelRequestRequestTypeDef",
    "AddNotificationChannelResponseTypeDef",
    "AnomalyReportedTimeRangeTypeDef",
    "AnomalySourceDetailsTypeDef",
    "AnomalyTimeRangeTypeDef",
    "CloudFormationCollectionFilterTypeDef",
    "CloudFormationCollectionTypeDef",
    "CloudFormationCostEstimationResourceCollectionFilterTypeDef",
    "CloudFormationHealthTypeDef",
    "CloudWatchMetricsDetailTypeDef",
    "CloudWatchMetricsDimensionTypeDef",
    "CostEstimationResourceCollectionFilterTypeDef",
    "CostEstimationTimeRangeTypeDef",
    "DescribeAccountHealthResponseTypeDef",
    "DescribeAccountOverviewRequestRequestTypeDef",
    "DescribeAccountOverviewResponseTypeDef",
    "DescribeAnomalyRequestRequestTypeDef",
    "DescribeAnomalyResponseTypeDef",
    "DescribeFeedbackRequestRequestTypeDef",
    "DescribeFeedbackResponseTypeDef",
    "DescribeInsightRequestRequestTypeDef",
    "DescribeInsightResponseTypeDef",
    "DescribeResourceCollectionHealthRequestRequestTypeDef",
    "DescribeResourceCollectionHealthResponseTypeDef",
    "DescribeServiceIntegrationResponseTypeDef",
    "EndTimeRangeTypeDef",
    "EventResourceTypeDef",
    "EventTimeRangeTypeDef",
    "EventTypeDef",
    "GetCostEstimationRequestRequestTypeDef",
    "GetCostEstimationResponseTypeDef",
    "GetResourceCollectionRequestRequestTypeDef",
    "GetResourceCollectionResponseTypeDef",
    "InsightFeedbackTypeDef",
    "InsightHealthTypeDef",
    "InsightTimeRangeTypeDef",
    "ListAnomaliesForInsightRequestRequestTypeDef",
    "ListAnomaliesForInsightResponseTypeDef",
    "ListEventsFiltersTypeDef",
    "ListEventsRequestRequestTypeDef",
    "ListEventsResponseTypeDef",
    "ListInsightsAnyStatusFilterTypeDef",
    "ListInsightsClosedStatusFilterTypeDef",
    "ListInsightsOngoingStatusFilterTypeDef",
    "ListInsightsRequestRequestTypeDef",
    "ListInsightsResponseTypeDef",
    "ListInsightsStatusFilterTypeDef",
    "ListNotificationChannelsRequestRequestTypeDef",
    "ListNotificationChannelsResponseTypeDef",
    "ListRecommendationsRequestRequestTypeDef",
    "ListRecommendationsResponseTypeDef",
    "NotificationChannelConfigTypeDef",
    "NotificationChannelTypeDef",
    "OpsCenterIntegrationConfigTypeDef",
    "OpsCenterIntegrationTypeDef",
    "PaginatorConfigTypeDef",
    "PredictionTimeRangeTypeDef",
    "ProactiveAnomalySummaryTypeDef",
    "ProactiveAnomalyTypeDef",
    "ProactiveInsightSummaryTypeDef",
    "ProactiveInsightTypeDef",
    "PutFeedbackRequestRequestTypeDef",
    "ReactiveAnomalySummaryTypeDef",
    "ReactiveAnomalyTypeDef",
    "ReactiveInsightSummaryTypeDef",
    "ReactiveInsightTypeDef",
    "RecommendationRelatedAnomalyResourceTypeDef",
    "RecommendationRelatedAnomalySourceDetailTypeDef",
    "RecommendationRelatedAnomalyTypeDef",
    "RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef",
    "RecommendationRelatedEventResourceTypeDef",
    "RecommendationRelatedEventTypeDef",
    "RecommendationTypeDef",
    "RemoveNotificationChannelRequestRequestTypeDef",
    "ResourceCollectionFilterTypeDef",
    "ResourceCollectionTypeDef",
    "ResponseMetadataTypeDef",
    "SearchInsightsFiltersTypeDef",
    "SearchInsightsRequestRequestTypeDef",
    "SearchInsightsResponseTypeDef",
    "ServiceCollectionTypeDef",
    "ServiceHealthTypeDef",
    "ServiceInsightHealthTypeDef",
    "ServiceIntegrationConfigTypeDef",
    "ServiceResourceCostTypeDef",
    "SnsChannelConfigTypeDef",
    "StartCostEstimationRequestRequestTypeDef",
    "StartTimeRangeTypeDef",
    "UpdateCloudFormationCollectionFilterTypeDef",
    "UpdateResourceCollectionFilterTypeDef",
    "UpdateResourceCollectionRequestRequestTypeDef",
    "UpdateServiceIntegrationConfigTypeDef",
    "UpdateServiceIntegrationRequestRequestTypeDef",
)

AddNotificationChannelRequestRequestTypeDef = TypedDict(
    "AddNotificationChannelRequestRequestTypeDef",
    {
        "Config": "NotificationChannelConfigTypeDef",
    },
)

AddNotificationChannelResponseTypeDef = TypedDict(
    "AddNotificationChannelResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAnomalyReportedTimeRangeTypeDef = TypedDict(
    "_RequiredAnomalyReportedTimeRangeTypeDef",
    {
        "OpenTime": datetime,
    },
)
_OptionalAnomalyReportedTimeRangeTypeDef = TypedDict(
    "_OptionalAnomalyReportedTimeRangeTypeDef",
    {
        "CloseTime": datetime,
    },
    total=False,
)

class AnomalyReportedTimeRangeTypeDef(
    _RequiredAnomalyReportedTimeRangeTypeDef, _OptionalAnomalyReportedTimeRangeTypeDef
):
    pass

AnomalySourceDetailsTypeDef = TypedDict(
    "AnomalySourceDetailsTypeDef",
    {
        "CloudWatchMetrics": List["CloudWatchMetricsDetailTypeDef"],
    },
    total=False,
)

_RequiredAnomalyTimeRangeTypeDef = TypedDict(
    "_RequiredAnomalyTimeRangeTypeDef",
    {
        "StartTime": datetime,
    },
)
_OptionalAnomalyTimeRangeTypeDef = TypedDict(
    "_OptionalAnomalyTimeRangeTypeDef",
    {
        "EndTime": datetime,
    },
    total=False,
)

class AnomalyTimeRangeTypeDef(_RequiredAnomalyTimeRangeTypeDef, _OptionalAnomalyTimeRangeTypeDef):
    pass

CloudFormationCollectionFilterTypeDef = TypedDict(
    "CloudFormationCollectionFilterTypeDef",
    {
        "StackNames": List[str],
    },
    total=False,
)

CloudFormationCollectionTypeDef = TypedDict(
    "CloudFormationCollectionTypeDef",
    {
        "StackNames": List[str],
    },
    total=False,
)

CloudFormationCostEstimationResourceCollectionFilterTypeDef = TypedDict(
    "CloudFormationCostEstimationResourceCollectionFilterTypeDef",
    {
        "StackNames": List[str],
    },
    total=False,
)

CloudFormationHealthTypeDef = TypedDict(
    "CloudFormationHealthTypeDef",
    {
        "StackName": str,
        "Insight": "InsightHealthTypeDef",
    },
    total=False,
)

CloudWatchMetricsDetailTypeDef = TypedDict(
    "CloudWatchMetricsDetailTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List["CloudWatchMetricsDimensionTypeDef"],
        "Stat": CloudWatchMetricsStatType,
        "Unit": str,
        "Period": int,
    },
    total=False,
)

CloudWatchMetricsDimensionTypeDef = TypedDict(
    "CloudWatchMetricsDimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

CostEstimationResourceCollectionFilterTypeDef = TypedDict(
    "CostEstimationResourceCollectionFilterTypeDef",
    {
        "CloudFormation": "CloudFormationCostEstimationResourceCollectionFilterTypeDef",
    },
    total=False,
)

CostEstimationTimeRangeTypeDef = TypedDict(
    "CostEstimationTimeRangeTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

DescribeAccountHealthResponseTypeDef = TypedDict(
    "DescribeAccountHealthResponseTypeDef",
    {
        "OpenReactiveInsights": int,
        "OpenProactiveInsights": int,
        "MetricsAnalyzed": int,
        "ResourceHours": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAccountOverviewRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAccountOverviewRequestRequestTypeDef",
    {
        "FromTime": Union[datetime, str],
    },
)
_OptionalDescribeAccountOverviewRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAccountOverviewRequestRequestTypeDef",
    {
        "ToTime": Union[datetime, str],
    },
    total=False,
)

class DescribeAccountOverviewRequestRequestTypeDef(
    _RequiredDescribeAccountOverviewRequestRequestTypeDef,
    _OptionalDescribeAccountOverviewRequestRequestTypeDef,
):
    pass

DescribeAccountOverviewResponseTypeDef = TypedDict(
    "DescribeAccountOverviewResponseTypeDef",
    {
        "ReactiveInsights": int,
        "ProactiveInsights": int,
        "MeanTimeToRecoverInMilliseconds": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAnomalyRequestRequestTypeDef = TypedDict(
    "DescribeAnomalyRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeAnomalyResponseTypeDef = TypedDict(
    "DescribeAnomalyResponseTypeDef",
    {
        "ProactiveAnomaly": "ProactiveAnomalyTypeDef",
        "ReactiveAnomaly": "ReactiveAnomalyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFeedbackRequestRequestTypeDef = TypedDict(
    "DescribeFeedbackRequestRequestTypeDef",
    {
        "InsightId": str,
    },
    total=False,
)

DescribeFeedbackResponseTypeDef = TypedDict(
    "DescribeFeedbackResponseTypeDef",
    {
        "InsightFeedback": "InsightFeedbackTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInsightRequestRequestTypeDef = TypedDict(
    "DescribeInsightRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeInsightResponseTypeDef = TypedDict(
    "DescribeInsightResponseTypeDef",
    {
        "ProactiveInsight": "ProactiveInsightTypeDef",
        "ReactiveInsight": "ReactiveInsightTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeResourceCollectionHealthRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeResourceCollectionHealthRequestRequestTypeDef",
    {
        "ResourceCollectionType": ResourceCollectionTypeType,
    },
)
_OptionalDescribeResourceCollectionHealthRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeResourceCollectionHealthRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class DescribeResourceCollectionHealthRequestRequestTypeDef(
    _RequiredDescribeResourceCollectionHealthRequestRequestTypeDef,
    _OptionalDescribeResourceCollectionHealthRequestRequestTypeDef,
):
    pass

DescribeResourceCollectionHealthResponseTypeDef = TypedDict(
    "DescribeResourceCollectionHealthResponseTypeDef",
    {
        "CloudFormation": List["CloudFormationHealthTypeDef"],
        "Service": List["ServiceHealthTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServiceIntegrationResponseTypeDef = TypedDict(
    "DescribeServiceIntegrationResponseTypeDef",
    {
        "ServiceIntegration": "ServiceIntegrationConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndTimeRangeTypeDef = TypedDict(
    "EndTimeRangeTypeDef",
    {
        "FromTime": Union[datetime, str],
        "ToTime": Union[datetime, str],
    },
    total=False,
)

EventResourceTypeDef = TypedDict(
    "EventResourceTypeDef",
    {
        "Type": str,
        "Name": str,
        "Arn": str,
    },
    total=False,
)

EventTimeRangeTypeDef = TypedDict(
    "EventTimeRangeTypeDef",
    {
        "FromTime": Union[datetime, str],
        "ToTime": Union[datetime, str],
    },
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "ResourceCollection": "ResourceCollectionTypeDef",
        "Id": str,
        "Time": datetime,
        "EventSource": str,
        "Name": str,
        "DataSource": EventDataSourceType,
        "EventClass": EventClassType,
        "Resources": List["EventResourceTypeDef"],
    },
    total=False,
)

GetCostEstimationRequestRequestTypeDef = TypedDict(
    "GetCostEstimationRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

GetCostEstimationResponseTypeDef = TypedDict(
    "GetCostEstimationResponseTypeDef",
    {
        "ResourceCollection": "CostEstimationResourceCollectionFilterTypeDef",
        "Status": CostEstimationStatusType,
        "Costs": List["ServiceResourceCostTypeDef"],
        "TimeRange": "CostEstimationTimeRangeTypeDef",
        "TotalCost": float,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetResourceCollectionRequestRequestTypeDef = TypedDict(
    "_RequiredGetResourceCollectionRequestRequestTypeDef",
    {
        "ResourceCollectionType": ResourceCollectionTypeType,
    },
)
_OptionalGetResourceCollectionRequestRequestTypeDef = TypedDict(
    "_OptionalGetResourceCollectionRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class GetResourceCollectionRequestRequestTypeDef(
    _RequiredGetResourceCollectionRequestRequestTypeDef,
    _OptionalGetResourceCollectionRequestRequestTypeDef,
):
    pass

GetResourceCollectionResponseTypeDef = TypedDict(
    "GetResourceCollectionResponseTypeDef",
    {
        "ResourceCollection": "ResourceCollectionFilterTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InsightFeedbackTypeDef = TypedDict(
    "InsightFeedbackTypeDef",
    {
        "Id": str,
        "Feedback": InsightFeedbackOptionType,
    },
    total=False,
)

InsightHealthTypeDef = TypedDict(
    "InsightHealthTypeDef",
    {
        "OpenProactiveInsights": int,
        "OpenReactiveInsights": int,
        "MeanTimeToRecoverInMilliseconds": int,
    },
    total=False,
)

_RequiredInsightTimeRangeTypeDef = TypedDict(
    "_RequiredInsightTimeRangeTypeDef",
    {
        "StartTime": datetime,
    },
)
_OptionalInsightTimeRangeTypeDef = TypedDict(
    "_OptionalInsightTimeRangeTypeDef",
    {
        "EndTime": datetime,
    },
    total=False,
)

class InsightTimeRangeTypeDef(_RequiredInsightTimeRangeTypeDef, _OptionalInsightTimeRangeTypeDef):
    pass

_RequiredListAnomaliesForInsightRequestRequestTypeDef = TypedDict(
    "_RequiredListAnomaliesForInsightRequestRequestTypeDef",
    {
        "InsightId": str,
    },
)
_OptionalListAnomaliesForInsightRequestRequestTypeDef = TypedDict(
    "_OptionalListAnomaliesForInsightRequestRequestTypeDef",
    {
        "StartTimeRange": "StartTimeRangeTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAnomaliesForInsightRequestRequestTypeDef(
    _RequiredListAnomaliesForInsightRequestRequestTypeDef,
    _OptionalListAnomaliesForInsightRequestRequestTypeDef,
):
    pass

ListAnomaliesForInsightResponseTypeDef = TypedDict(
    "ListAnomaliesForInsightResponseTypeDef",
    {
        "ProactiveAnomalies": List["ProactiveAnomalySummaryTypeDef"],
        "ReactiveAnomalies": List["ReactiveAnomalySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventsFiltersTypeDef = TypedDict(
    "ListEventsFiltersTypeDef",
    {
        "InsightId": str,
        "EventTimeRange": "EventTimeRangeTypeDef",
        "EventClass": EventClassType,
        "EventSource": str,
        "DataSource": EventDataSourceType,
        "ResourceCollection": "ResourceCollectionTypeDef",
    },
    total=False,
)

_RequiredListEventsRequestRequestTypeDef = TypedDict(
    "_RequiredListEventsRequestRequestTypeDef",
    {
        "Filters": "ListEventsFiltersTypeDef",
    },
)
_OptionalListEventsRequestRequestTypeDef = TypedDict(
    "_OptionalListEventsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListEventsRequestRequestTypeDef(
    _RequiredListEventsRequestRequestTypeDef, _OptionalListEventsRequestRequestTypeDef
):
    pass

ListEventsResponseTypeDef = TypedDict(
    "ListEventsResponseTypeDef",
    {
        "Events": List["EventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInsightsAnyStatusFilterTypeDef = TypedDict(
    "ListInsightsAnyStatusFilterTypeDef",
    {
        "Type": InsightTypeType,
        "StartTimeRange": "StartTimeRangeTypeDef",
    },
)

ListInsightsClosedStatusFilterTypeDef = TypedDict(
    "ListInsightsClosedStatusFilterTypeDef",
    {
        "Type": InsightTypeType,
        "EndTimeRange": "EndTimeRangeTypeDef",
    },
)

ListInsightsOngoingStatusFilterTypeDef = TypedDict(
    "ListInsightsOngoingStatusFilterTypeDef",
    {
        "Type": InsightTypeType,
    },
)

_RequiredListInsightsRequestRequestTypeDef = TypedDict(
    "_RequiredListInsightsRequestRequestTypeDef",
    {
        "StatusFilter": "ListInsightsStatusFilterTypeDef",
    },
)
_OptionalListInsightsRequestRequestTypeDef = TypedDict(
    "_OptionalListInsightsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListInsightsRequestRequestTypeDef(
    _RequiredListInsightsRequestRequestTypeDef, _OptionalListInsightsRequestRequestTypeDef
):
    pass

ListInsightsResponseTypeDef = TypedDict(
    "ListInsightsResponseTypeDef",
    {
        "ProactiveInsights": List["ProactiveInsightSummaryTypeDef"],
        "ReactiveInsights": List["ReactiveInsightSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInsightsStatusFilterTypeDef = TypedDict(
    "ListInsightsStatusFilterTypeDef",
    {
        "Ongoing": "ListInsightsOngoingStatusFilterTypeDef",
        "Closed": "ListInsightsClosedStatusFilterTypeDef",
        "Any": "ListInsightsAnyStatusFilterTypeDef",
    },
    total=False,
)

ListNotificationChannelsRequestRequestTypeDef = TypedDict(
    "ListNotificationChannelsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListNotificationChannelsResponseTypeDef = TypedDict(
    "ListNotificationChannelsResponseTypeDef",
    {
        "Channels": List["NotificationChannelTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRecommendationsRequestRequestTypeDef = TypedDict(
    "_RequiredListRecommendationsRequestRequestTypeDef",
    {
        "InsightId": str,
    },
)
_OptionalListRecommendationsRequestRequestTypeDef = TypedDict(
    "_OptionalListRecommendationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "Locale": LocaleType,
    },
    total=False,
)

class ListRecommendationsRequestRequestTypeDef(
    _RequiredListRecommendationsRequestRequestTypeDef,
    _OptionalListRecommendationsRequestRequestTypeDef,
):
    pass

ListRecommendationsResponseTypeDef = TypedDict(
    "ListRecommendationsResponseTypeDef",
    {
        "Recommendations": List["RecommendationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationChannelConfigTypeDef = TypedDict(
    "NotificationChannelConfigTypeDef",
    {
        "Sns": "SnsChannelConfigTypeDef",
    },
)

NotificationChannelTypeDef = TypedDict(
    "NotificationChannelTypeDef",
    {
        "Id": str,
        "Config": "NotificationChannelConfigTypeDef",
    },
    total=False,
)

OpsCenterIntegrationConfigTypeDef = TypedDict(
    "OpsCenterIntegrationConfigTypeDef",
    {
        "OptInStatus": OptInStatusType,
    },
    total=False,
)

OpsCenterIntegrationTypeDef = TypedDict(
    "OpsCenterIntegrationTypeDef",
    {
        "OptInStatus": OptInStatusType,
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

_RequiredPredictionTimeRangeTypeDef = TypedDict(
    "_RequiredPredictionTimeRangeTypeDef",
    {
        "StartTime": datetime,
    },
)
_OptionalPredictionTimeRangeTypeDef = TypedDict(
    "_OptionalPredictionTimeRangeTypeDef",
    {
        "EndTime": datetime,
    },
    total=False,
)

class PredictionTimeRangeTypeDef(
    _RequiredPredictionTimeRangeTypeDef, _OptionalPredictionTimeRangeTypeDef
):
    pass

ProactiveAnomalySummaryTypeDef = TypedDict(
    "ProactiveAnomalySummaryTypeDef",
    {
        "Id": str,
        "Severity": AnomalySeverityType,
        "Status": AnomalyStatusType,
        "UpdateTime": datetime,
        "AnomalyTimeRange": "AnomalyTimeRangeTypeDef",
        "AnomalyReportedTimeRange": "AnomalyReportedTimeRangeTypeDef",
        "PredictionTimeRange": "PredictionTimeRangeTypeDef",
        "SourceDetails": "AnomalySourceDetailsTypeDef",
        "AssociatedInsightId": str,
        "ResourceCollection": "ResourceCollectionTypeDef",
        "Limit": float,
    },
    total=False,
)

ProactiveAnomalyTypeDef = TypedDict(
    "ProactiveAnomalyTypeDef",
    {
        "Id": str,
        "Severity": AnomalySeverityType,
        "Status": AnomalyStatusType,
        "UpdateTime": datetime,
        "AnomalyTimeRange": "AnomalyTimeRangeTypeDef",
        "AnomalyReportedTimeRange": "AnomalyReportedTimeRangeTypeDef",
        "PredictionTimeRange": "PredictionTimeRangeTypeDef",
        "SourceDetails": "AnomalySourceDetailsTypeDef",
        "AssociatedInsightId": str,
        "ResourceCollection": "ResourceCollectionTypeDef",
        "Limit": float,
    },
    total=False,
)

ProactiveInsightSummaryTypeDef = TypedDict(
    "ProactiveInsightSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Severity": InsightSeverityType,
        "Status": InsightStatusType,
        "InsightTimeRange": "InsightTimeRangeTypeDef",
        "PredictionTimeRange": "PredictionTimeRangeTypeDef",
        "ResourceCollection": "ResourceCollectionTypeDef",
        "ServiceCollection": "ServiceCollectionTypeDef",
    },
    total=False,
)

ProactiveInsightTypeDef = TypedDict(
    "ProactiveInsightTypeDef",
    {
        "Id": str,
        "Name": str,
        "Severity": InsightSeverityType,
        "Status": InsightStatusType,
        "InsightTimeRange": "InsightTimeRangeTypeDef",
        "PredictionTimeRange": "PredictionTimeRangeTypeDef",
        "ResourceCollection": "ResourceCollectionTypeDef",
        "SsmOpsItemId": str,
    },
    total=False,
)

PutFeedbackRequestRequestTypeDef = TypedDict(
    "PutFeedbackRequestRequestTypeDef",
    {
        "InsightFeedback": "InsightFeedbackTypeDef",
    },
    total=False,
)

ReactiveAnomalySummaryTypeDef = TypedDict(
    "ReactiveAnomalySummaryTypeDef",
    {
        "Id": str,
        "Severity": AnomalySeverityType,
        "Status": AnomalyStatusType,
        "AnomalyTimeRange": "AnomalyTimeRangeTypeDef",
        "AnomalyReportedTimeRange": "AnomalyReportedTimeRangeTypeDef",
        "SourceDetails": "AnomalySourceDetailsTypeDef",
        "AssociatedInsightId": str,
        "ResourceCollection": "ResourceCollectionTypeDef",
    },
    total=False,
)

ReactiveAnomalyTypeDef = TypedDict(
    "ReactiveAnomalyTypeDef",
    {
        "Id": str,
        "Severity": AnomalySeverityType,
        "Status": AnomalyStatusType,
        "AnomalyTimeRange": "AnomalyTimeRangeTypeDef",
        "AnomalyReportedTimeRange": "AnomalyReportedTimeRangeTypeDef",
        "SourceDetails": "AnomalySourceDetailsTypeDef",
        "AssociatedInsightId": str,
        "ResourceCollection": "ResourceCollectionTypeDef",
    },
    total=False,
)

ReactiveInsightSummaryTypeDef = TypedDict(
    "ReactiveInsightSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Severity": InsightSeverityType,
        "Status": InsightStatusType,
        "InsightTimeRange": "InsightTimeRangeTypeDef",
        "ResourceCollection": "ResourceCollectionTypeDef",
        "ServiceCollection": "ServiceCollectionTypeDef",
    },
    total=False,
)

ReactiveInsightTypeDef = TypedDict(
    "ReactiveInsightTypeDef",
    {
        "Id": str,
        "Name": str,
        "Severity": InsightSeverityType,
        "Status": InsightStatusType,
        "InsightTimeRange": "InsightTimeRangeTypeDef",
        "ResourceCollection": "ResourceCollectionTypeDef",
        "SsmOpsItemId": str,
    },
    total=False,
)

RecommendationRelatedAnomalyResourceTypeDef = TypedDict(
    "RecommendationRelatedAnomalyResourceTypeDef",
    {
        "Name": str,
        "Type": str,
    },
    total=False,
)

RecommendationRelatedAnomalySourceDetailTypeDef = TypedDict(
    "RecommendationRelatedAnomalySourceDetailTypeDef",
    {
        "CloudWatchMetrics": List["RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef"],
    },
    total=False,
)

RecommendationRelatedAnomalyTypeDef = TypedDict(
    "RecommendationRelatedAnomalyTypeDef",
    {
        "Resources": List["RecommendationRelatedAnomalyResourceTypeDef"],
        "SourceDetails": List["RecommendationRelatedAnomalySourceDetailTypeDef"],
    },
    total=False,
)

RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef = TypedDict(
    "RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
    },
    total=False,
)

RecommendationRelatedEventResourceTypeDef = TypedDict(
    "RecommendationRelatedEventResourceTypeDef",
    {
        "Name": str,
        "Type": str,
    },
    total=False,
)

RecommendationRelatedEventTypeDef = TypedDict(
    "RecommendationRelatedEventTypeDef",
    {
        "Name": str,
        "Resources": List["RecommendationRelatedEventResourceTypeDef"],
    },
    total=False,
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "Description": str,
        "Link": str,
        "Name": str,
        "Reason": str,
        "RelatedEvents": List["RecommendationRelatedEventTypeDef"],
        "RelatedAnomalies": List["RecommendationRelatedAnomalyTypeDef"],
    },
    total=False,
)

RemoveNotificationChannelRequestRequestTypeDef = TypedDict(
    "RemoveNotificationChannelRequestRequestTypeDef",
    {
        "Id": str,
    },
)

ResourceCollectionFilterTypeDef = TypedDict(
    "ResourceCollectionFilterTypeDef",
    {
        "CloudFormation": "CloudFormationCollectionFilterTypeDef",
    },
    total=False,
)

ResourceCollectionTypeDef = TypedDict(
    "ResourceCollectionTypeDef",
    {
        "CloudFormation": "CloudFormationCollectionTypeDef",
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

SearchInsightsFiltersTypeDef = TypedDict(
    "SearchInsightsFiltersTypeDef",
    {
        "Severities": List[InsightSeverityType],
        "Statuses": List[InsightStatusType],
        "ResourceCollection": "ResourceCollectionTypeDef",
        "ServiceCollection": "ServiceCollectionTypeDef",
    },
    total=False,
)

_RequiredSearchInsightsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchInsightsRequestRequestTypeDef",
    {
        "StartTimeRange": "StartTimeRangeTypeDef",
        "Type": InsightTypeType,
    },
)
_OptionalSearchInsightsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchInsightsRequestRequestTypeDef",
    {
        "Filters": "SearchInsightsFiltersTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class SearchInsightsRequestRequestTypeDef(
    _RequiredSearchInsightsRequestRequestTypeDef, _OptionalSearchInsightsRequestRequestTypeDef
):
    pass

SearchInsightsResponseTypeDef = TypedDict(
    "SearchInsightsResponseTypeDef",
    {
        "ProactiveInsights": List["ProactiveInsightSummaryTypeDef"],
        "ReactiveInsights": List["ReactiveInsightSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceCollectionTypeDef = TypedDict(
    "ServiceCollectionTypeDef",
    {
        "ServiceNames": List[ServiceNameType],
    },
    total=False,
)

ServiceHealthTypeDef = TypedDict(
    "ServiceHealthTypeDef",
    {
        "ServiceName": ServiceNameType,
        "Insight": "ServiceInsightHealthTypeDef",
    },
    total=False,
)

ServiceInsightHealthTypeDef = TypedDict(
    "ServiceInsightHealthTypeDef",
    {
        "OpenProactiveInsights": int,
        "OpenReactiveInsights": int,
    },
    total=False,
)

ServiceIntegrationConfigTypeDef = TypedDict(
    "ServiceIntegrationConfigTypeDef",
    {
        "OpsCenter": "OpsCenterIntegrationTypeDef",
    },
    total=False,
)

ServiceResourceCostTypeDef = TypedDict(
    "ServiceResourceCostTypeDef",
    {
        "Type": str,
        "State": CostEstimationServiceResourceStateType,
        "Count": int,
        "UnitCost": float,
        "Cost": float,
    },
    total=False,
)

SnsChannelConfigTypeDef = TypedDict(
    "SnsChannelConfigTypeDef",
    {
        "TopicArn": str,
    },
    total=False,
)

_RequiredStartCostEstimationRequestRequestTypeDef = TypedDict(
    "_RequiredStartCostEstimationRequestRequestTypeDef",
    {
        "ResourceCollection": "CostEstimationResourceCollectionFilterTypeDef",
    },
)
_OptionalStartCostEstimationRequestRequestTypeDef = TypedDict(
    "_OptionalStartCostEstimationRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class StartCostEstimationRequestRequestTypeDef(
    _RequiredStartCostEstimationRequestRequestTypeDef,
    _OptionalStartCostEstimationRequestRequestTypeDef,
):
    pass

StartTimeRangeTypeDef = TypedDict(
    "StartTimeRangeTypeDef",
    {
        "FromTime": Union[datetime, str],
        "ToTime": Union[datetime, str],
    },
    total=False,
)

UpdateCloudFormationCollectionFilterTypeDef = TypedDict(
    "UpdateCloudFormationCollectionFilterTypeDef",
    {
        "StackNames": List[str],
    },
    total=False,
)

UpdateResourceCollectionFilterTypeDef = TypedDict(
    "UpdateResourceCollectionFilterTypeDef",
    {
        "CloudFormation": "UpdateCloudFormationCollectionFilterTypeDef",
    },
    total=False,
)

UpdateResourceCollectionRequestRequestTypeDef = TypedDict(
    "UpdateResourceCollectionRequestRequestTypeDef",
    {
        "Action": UpdateResourceCollectionActionType,
        "ResourceCollection": "UpdateResourceCollectionFilterTypeDef",
    },
)

UpdateServiceIntegrationConfigTypeDef = TypedDict(
    "UpdateServiceIntegrationConfigTypeDef",
    {
        "OpsCenter": "OpsCenterIntegrationConfigTypeDef",
    },
    total=False,
)

UpdateServiceIntegrationRequestRequestTypeDef = TypedDict(
    "UpdateServiceIntegrationRequestRequestTypeDef",
    {
        "ServiceIntegration": "UpdateServiceIntegrationConfigTypeDef",
    },
)
