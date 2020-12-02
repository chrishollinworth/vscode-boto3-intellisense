"""
Main interface for devops-guru service type definitions.

Usage::

    ```python
    from mypy_boto3_devops_guru.type_defs import AnomalySourceDetailsTypeDef

    data: AnomalySourceDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AnomalySourceDetailsTypeDef",
    "AnomalyTimeRangeTypeDef",
    "CloudFormationCollectionFilterTypeDef",
    "CloudFormationCollectionTypeDef",
    "CloudFormationHealthTypeDef",
    "CloudWatchMetricsDetailTypeDef",
    "CloudWatchMetricsDimensionTypeDef",
    "EndTimeRangeTypeDef",
    "EventResourceTypeDef",
    "EventTimeRangeTypeDef",
    "EventTypeDef",
    "InsightHealthTypeDef",
    "InsightTimeRangeTypeDef",
    "ListInsightsAnyStatusFilterTypeDef",
    "ListInsightsClosedStatusFilterTypeDef",
    "ListInsightsOngoingStatusFilterTypeDef",
    "NotificationChannelConfigTypeDef",
    "NotificationChannelTypeDef",
    "OpsCenterIntegrationConfigTypeDef",
    "OpsCenterIntegrationTypeDef",
    "PredictionTimeRangeTypeDef",
    "ProactiveAnomalySummaryTypeDef",
    "ProactiveAnomalyTypeDef",
    "ProactiveInsightSummaryTypeDef",
    "ProactiveInsightTypeDef",
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
    "ResourceCollectionFilterTypeDef",
    "ResourceCollectionTypeDef",
    "ServiceIntegrationConfigTypeDef",
    "SnsChannelConfigTypeDef",
    "StartTimeRangeTypeDef",
    "UpdateCloudFormationCollectionFilterTypeDef",
    "AddNotificationChannelResponseTypeDef",
    "DescribeAccountHealthResponseTypeDef",
    "DescribeAccountOverviewResponseTypeDef",
    "DescribeAnomalyResponseTypeDef",
    "DescribeInsightResponseTypeDef",
    "DescribeResourceCollectionHealthResponseTypeDef",
    "DescribeServiceIntegrationResponseTypeDef",
    "GetResourceCollectionResponseTypeDef",
    "InsightFeedbackTypeDef",
    "ListAnomaliesForInsightResponseTypeDef",
    "ListEventsFiltersTypeDef",
    "ListEventsResponseTypeDef",
    "ListInsightsResponseTypeDef",
    "ListInsightsStatusFilterTypeDef",
    "ListNotificationChannelsResponseTypeDef",
    "ListRecommendationsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "SearchInsightsFiltersTypeDef",
    "SearchInsightsResponseTypeDef",
    "UpdateResourceCollectionFilterTypeDef",
    "UpdateServiceIntegrationConfigTypeDef",
)

AnomalySourceDetailsTypeDef = TypedDict(
    "AnomalySourceDetailsTypeDef",
    {"CloudWatchMetrics": List["CloudWatchMetricsDetailTypeDef"]},
    total=False,
)

_RequiredAnomalyTimeRangeTypeDef = TypedDict(
    "_RequiredAnomalyTimeRangeTypeDef", {"StartTime": datetime}
)
_OptionalAnomalyTimeRangeTypeDef = TypedDict(
    "_OptionalAnomalyTimeRangeTypeDef", {"EndTime": datetime}, total=False
)


class AnomalyTimeRangeTypeDef(_RequiredAnomalyTimeRangeTypeDef, _OptionalAnomalyTimeRangeTypeDef):
    pass


CloudFormationCollectionFilterTypeDef = TypedDict(
    "CloudFormationCollectionFilterTypeDef", {"StackNames": List[str]}, total=False
)

CloudFormationCollectionTypeDef = TypedDict(
    "CloudFormationCollectionTypeDef", {"StackNames": List[str]}, total=False
)

CloudFormationHealthTypeDef = TypedDict(
    "CloudFormationHealthTypeDef",
    {"Insight": "InsightHealthTypeDef", "StackName": str},
    total=False,
)

CloudWatchMetricsDetailTypeDef = TypedDict(
    "CloudWatchMetricsDetailTypeDef",
    {
        "Dimensions": List["CloudWatchMetricsDimensionTypeDef"],
        "MetricName": str,
        "Namespace": str,
        "Period": int,
        "Stat": Literal["Sum", "Average", "SampleCount", "Minimum", "Maximum", "p99", "p90", "p50"],
        "Unit": str,
    },
    total=False,
)

CloudWatchMetricsDimensionTypeDef = TypedDict(
    "CloudWatchMetricsDimensionTypeDef", {"Name": str, "Value": str}, total=False
)

EndTimeRangeTypeDef = TypedDict(
    "EndTimeRangeTypeDef", {"FromTime": datetime, "ToTime": datetime}, total=False
)

EventResourceTypeDef = TypedDict(
    "EventResourceTypeDef", {"Arn": str, "Name": str, "Type": str}, total=False
)

EventTimeRangeTypeDef = TypedDict(
    "EventTimeRangeTypeDef", {"FromTime": datetime, "ToTime": datetime}
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "DataSource": Literal["AWS_CLOUD_TRAIL", "AWS_CODE_DEPLOY"],
        "EventClass": Literal[
            "INFRASTRUCTURE", "DEPLOYMENT", "SECURITY_CHANGE", "CONFIG_CHANGE", "SCHEMA_CHANGE"
        ],
        "EventSource": str,
        "Id": str,
        "Name": str,
        "ResourceCollection": "ResourceCollectionTypeDef",
        "Resources": List["EventResourceTypeDef"],
        "Time": datetime,
    },
    total=False,
)

InsightHealthTypeDef = TypedDict(
    "InsightHealthTypeDef",
    {
        "MeanTimeToRecoverInMilliseconds": int,
        "OpenProactiveInsights": int,
        "OpenReactiveInsights": int,
    },
    total=False,
)

_RequiredInsightTimeRangeTypeDef = TypedDict(
    "_RequiredInsightTimeRangeTypeDef", {"StartTime": datetime}
)
_OptionalInsightTimeRangeTypeDef = TypedDict(
    "_OptionalInsightTimeRangeTypeDef", {"EndTime": datetime}, total=False
)


class InsightTimeRangeTypeDef(_RequiredInsightTimeRangeTypeDef, _OptionalInsightTimeRangeTypeDef):
    pass


ListInsightsAnyStatusFilterTypeDef = TypedDict(
    "ListInsightsAnyStatusFilterTypeDef",
    {"StartTimeRange": "StartTimeRangeTypeDef", "Type": Literal["REACTIVE", "PROACTIVE"]},
)

ListInsightsClosedStatusFilterTypeDef = TypedDict(
    "ListInsightsClosedStatusFilterTypeDef",
    {"EndTimeRange": "EndTimeRangeTypeDef", "Type": Literal["REACTIVE", "PROACTIVE"]},
)

ListInsightsOngoingStatusFilterTypeDef = TypedDict(
    "ListInsightsOngoingStatusFilterTypeDef", {"Type": Literal["REACTIVE", "PROACTIVE"]}
)

NotificationChannelConfigTypeDef = TypedDict(
    "NotificationChannelConfigTypeDef", {"Sns": "SnsChannelConfigTypeDef"}
)

NotificationChannelTypeDef = TypedDict(
    "NotificationChannelTypeDef",
    {"Config": "NotificationChannelConfigTypeDef", "Id": str},
    total=False,
)

OpsCenterIntegrationConfigTypeDef = TypedDict(
    "OpsCenterIntegrationConfigTypeDef",
    {"OptInStatus": Literal["ENABLED", "DISABLED"]},
    total=False,
)

OpsCenterIntegrationTypeDef = TypedDict(
    "OpsCenterIntegrationTypeDef", {"OptInStatus": Literal["ENABLED", "DISABLED"]}, total=False
)

_RequiredPredictionTimeRangeTypeDef = TypedDict(
    "_RequiredPredictionTimeRangeTypeDef", {"StartTime": datetime}
)
_OptionalPredictionTimeRangeTypeDef = TypedDict(
    "_OptionalPredictionTimeRangeTypeDef", {"EndTime": datetime}, total=False
)


class PredictionTimeRangeTypeDef(
    _RequiredPredictionTimeRangeTypeDef, _OptionalPredictionTimeRangeTypeDef
):
    pass


ProactiveAnomalySummaryTypeDef = TypedDict(
    "ProactiveAnomalySummaryTypeDef",
    {
        "AnomalyTimeRange": "AnomalyTimeRangeTypeDef",
        "AssociatedInsightId": str,
        "Id": str,
        "Limit": float,
        "PredictionTimeRange": "PredictionTimeRangeTypeDef",
        "ResourceCollection": "ResourceCollectionTypeDef",
        "Severity": Literal["LOW", "MEDIUM", "HIGH"],
        "SourceDetails": "AnomalySourceDetailsTypeDef",
        "Status": Literal["ONGOING", "CLOSED"],
        "UpdateTime": datetime,
    },
    total=False,
)

ProactiveAnomalyTypeDef = TypedDict(
    "ProactiveAnomalyTypeDef",
    {
        "AnomalyTimeRange": "AnomalyTimeRangeTypeDef",
        "AssociatedInsightId": str,
        "Id": str,
        "Limit": float,
        "PredictionTimeRange": "PredictionTimeRangeTypeDef",
        "ResourceCollection": "ResourceCollectionTypeDef",
        "Severity": Literal["LOW", "MEDIUM", "HIGH"],
        "SourceDetails": "AnomalySourceDetailsTypeDef",
        "Status": Literal["ONGOING", "CLOSED"],
        "UpdateTime": datetime,
    },
    total=False,
)

ProactiveInsightSummaryTypeDef = TypedDict(
    "ProactiveInsightSummaryTypeDef",
    {
        "Id": str,
        "InsightTimeRange": "InsightTimeRangeTypeDef",
        "Name": str,
        "PredictionTimeRange": "PredictionTimeRangeTypeDef",
        "ResourceCollection": "ResourceCollectionTypeDef",
        "Severity": Literal["LOW", "MEDIUM", "HIGH"],
        "Status": Literal["ONGOING", "CLOSED"],
    },
    total=False,
)

ProactiveInsightTypeDef = TypedDict(
    "ProactiveInsightTypeDef",
    {
        "Id": str,
        "InsightTimeRange": "InsightTimeRangeTypeDef",
        "Name": str,
        "PredictionTimeRange": "PredictionTimeRangeTypeDef",
        "ResourceCollection": "ResourceCollectionTypeDef",
        "Severity": Literal["LOW", "MEDIUM", "HIGH"],
        "SsmOpsItemId": str,
        "Status": Literal["ONGOING", "CLOSED"],
    },
    total=False,
)

ReactiveAnomalySummaryTypeDef = TypedDict(
    "ReactiveAnomalySummaryTypeDef",
    {
        "AnomalyTimeRange": "AnomalyTimeRangeTypeDef",
        "AssociatedInsightId": str,
        "Id": str,
        "ResourceCollection": "ResourceCollectionTypeDef",
        "Severity": Literal["LOW", "MEDIUM", "HIGH"],
        "SourceDetails": "AnomalySourceDetailsTypeDef",
        "Status": Literal["ONGOING", "CLOSED"],
    },
    total=False,
)

ReactiveAnomalyTypeDef = TypedDict(
    "ReactiveAnomalyTypeDef",
    {
        "AnomalyTimeRange": "AnomalyTimeRangeTypeDef",
        "AssociatedInsightId": str,
        "Id": str,
        "ResourceCollection": "ResourceCollectionTypeDef",
        "Severity": Literal["LOW", "MEDIUM", "HIGH"],
        "SourceDetails": "AnomalySourceDetailsTypeDef",
        "Status": Literal["ONGOING", "CLOSED"],
    },
    total=False,
)

ReactiveInsightSummaryTypeDef = TypedDict(
    "ReactiveInsightSummaryTypeDef",
    {
        "Id": str,
        "InsightTimeRange": "InsightTimeRangeTypeDef",
        "Name": str,
        "ResourceCollection": "ResourceCollectionTypeDef",
        "Severity": Literal["LOW", "MEDIUM", "HIGH"],
        "Status": Literal["ONGOING", "CLOSED"],
    },
    total=False,
)

ReactiveInsightTypeDef = TypedDict(
    "ReactiveInsightTypeDef",
    {
        "Id": str,
        "InsightTimeRange": "InsightTimeRangeTypeDef",
        "Name": str,
        "ResourceCollection": "ResourceCollectionTypeDef",
        "Severity": Literal["LOW", "MEDIUM", "HIGH"],
        "SsmOpsItemId": str,
        "Status": Literal["ONGOING", "CLOSED"],
    },
    total=False,
)

RecommendationRelatedAnomalyResourceTypeDef = TypedDict(
    "RecommendationRelatedAnomalyResourceTypeDef", {"Name": str, "Type": str}, total=False
)

RecommendationRelatedAnomalySourceDetailTypeDef = TypedDict(
    "RecommendationRelatedAnomalySourceDetailTypeDef",
    {"CloudWatchMetrics": List["RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef"]},
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
    {"MetricName": str, "Namespace": str},
    total=False,
)

RecommendationRelatedEventResourceTypeDef = TypedDict(
    "RecommendationRelatedEventResourceTypeDef", {"Name": str, "Type": str}, total=False
)

RecommendationRelatedEventTypeDef = TypedDict(
    "RecommendationRelatedEventTypeDef",
    {"Name": str, "Resources": List["RecommendationRelatedEventResourceTypeDef"]},
    total=False,
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "Description": str,
        "Link": str,
        "Name": str,
        "Reason": str,
        "RelatedAnomalies": List["RecommendationRelatedAnomalyTypeDef"],
        "RelatedEvents": List["RecommendationRelatedEventTypeDef"],
    },
    total=False,
)

ResourceCollectionFilterTypeDef = TypedDict(
    "ResourceCollectionFilterTypeDef",
    {"CloudFormation": "CloudFormationCollectionFilterTypeDef"},
    total=False,
)

ResourceCollectionTypeDef = TypedDict(
    "ResourceCollectionTypeDef", {"CloudFormation": "CloudFormationCollectionTypeDef"}, total=False
)

ServiceIntegrationConfigTypeDef = TypedDict(
    "ServiceIntegrationConfigTypeDef", {"OpsCenter": "OpsCenterIntegrationTypeDef"}, total=False
)

SnsChannelConfigTypeDef = TypedDict("SnsChannelConfigTypeDef", {"TopicArn": str}, total=False)

StartTimeRangeTypeDef = TypedDict(
    "StartTimeRangeTypeDef", {"FromTime": datetime, "ToTime": datetime}, total=False
)

UpdateCloudFormationCollectionFilterTypeDef = TypedDict(
    "UpdateCloudFormationCollectionFilterTypeDef", {"StackNames": List[str]}, total=False
)

AddNotificationChannelResponseTypeDef = TypedDict(
    "AddNotificationChannelResponseTypeDef", {"Id": str}, total=False
)

DescribeAccountHealthResponseTypeDef = TypedDict(
    "DescribeAccountHealthResponseTypeDef",
    {"MetricsAnalyzed": int, "OpenProactiveInsights": int, "OpenReactiveInsights": int},
    total=False,
)

DescribeAccountOverviewResponseTypeDef = TypedDict(
    "DescribeAccountOverviewResponseTypeDef",
    {"MeanTimeToRecoverInMilliseconds": int, "ProactiveInsights": int, "ReactiveInsights": int},
    total=False,
)

DescribeAnomalyResponseTypeDef = TypedDict(
    "DescribeAnomalyResponseTypeDef",
    {"ProactiveAnomaly": "ProactiveAnomalyTypeDef", "ReactiveAnomaly": "ReactiveAnomalyTypeDef"},
    total=False,
)

DescribeInsightResponseTypeDef = TypedDict(
    "DescribeInsightResponseTypeDef",
    {"ProactiveInsight": "ProactiveInsightTypeDef", "ReactiveInsight": "ReactiveInsightTypeDef"},
    total=False,
)

DescribeResourceCollectionHealthResponseTypeDef = TypedDict(
    "DescribeResourceCollectionHealthResponseTypeDef",
    {"CloudFormation": List["CloudFormationHealthTypeDef"], "NextToken": str},
    total=False,
)

DescribeServiceIntegrationResponseTypeDef = TypedDict(
    "DescribeServiceIntegrationResponseTypeDef",
    {"ServiceIntegration": "ServiceIntegrationConfigTypeDef"},
    total=False,
)

GetResourceCollectionResponseTypeDef = TypedDict(
    "GetResourceCollectionResponseTypeDef",
    {"NextToken": str, "ResourceCollection": "ResourceCollectionFilterTypeDef"},
    total=False,
)

InsightFeedbackTypeDef = TypedDict(
    "InsightFeedbackTypeDef",
    {
        "Feedback": Literal[
            "VALID_COLLECTION",
            "RECOMMENDATION_USEFUL",
            "ALERT_TOO_SENSITIVE",
            "DATA_NOISY_ANOMALY",
            "DATA_INCORRECT",
        ],
        "Id": str,
    },
    total=False,
)

ListAnomaliesForInsightResponseTypeDef = TypedDict(
    "ListAnomaliesForInsightResponseTypeDef",
    {
        "NextToken": str,
        "ProactiveAnomalies": List["ProactiveAnomalySummaryTypeDef"],
        "ReactiveAnomalies": List["ReactiveAnomalySummaryTypeDef"],
    },
    total=False,
)

ListEventsFiltersTypeDef = TypedDict(
    "ListEventsFiltersTypeDef",
    {
        "DataSource": Literal["AWS_CLOUD_TRAIL", "AWS_CODE_DEPLOY"],
        "EventClass": Literal[
            "INFRASTRUCTURE", "DEPLOYMENT", "SECURITY_CHANGE", "CONFIG_CHANGE", "SCHEMA_CHANGE"
        ],
        "EventSource": str,
        "EventTimeRange": "EventTimeRangeTypeDef",
        "InsightId": str,
        "ResourceCollection": "ResourceCollectionTypeDef",
    },
    total=False,
)

ListEventsResponseTypeDef = TypedDict(
    "ListEventsResponseTypeDef", {"Events": List["EventTypeDef"], "NextToken": str}, total=False
)

ListInsightsResponseTypeDef = TypedDict(
    "ListInsightsResponseTypeDef",
    {
        "NextToken": str,
        "ProactiveInsights": List["ProactiveInsightSummaryTypeDef"],
        "ReactiveInsights": List["ReactiveInsightSummaryTypeDef"],
    },
    total=False,
)

ListInsightsStatusFilterTypeDef = TypedDict(
    "ListInsightsStatusFilterTypeDef",
    {
        "Any": "ListInsightsAnyStatusFilterTypeDef",
        "Closed": "ListInsightsClosedStatusFilterTypeDef",
        "Ongoing": "ListInsightsOngoingStatusFilterTypeDef",
    },
    total=False,
)

ListNotificationChannelsResponseTypeDef = TypedDict(
    "ListNotificationChannelsResponseTypeDef",
    {"Channels": List["NotificationChannelTypeDef"], "NextToken": str},
    total=False,
)

ListRecommendationsResponseTypeDef = TypedDict(
    "ListRecommendationsResponseTypeDef",
    {"NextToken": str, "Recommendations": List["RecommendationTypeDef"]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

SearchInsightsFiltersTypeDef = TypedDict(
    "SearchInsightsFiltersTypeDef",
    {
        "ResourceCollection": "ResourceCollectionTypeDef",
        "Severities": List[Literal["LOW", "MEDIUM", "HIGH"]],
        "Statuses": List[Literal["ONGOING", "CLOSED"]],
    },
    total=False,
)

SearchInsightsResponseTypeDef = TypedDict(
    "SearchInsightsResponseTypeDef",
    {
        "NextToken": str,
        "ProactiveInsights": List["ProactiveInsightSummaryTypeDef"],
        "ReactiveInsights": List["ReactiveInsightSummaryTypeDef"],
    },
    total=False,
)

UpdateResourceCollectionFilterTypeDef = TypedDict(
    "UpdateResourceCollectionFilterTypeDef",
    {"CloudFormation": "UpdateCloudFormationCollectionFilterTypeDef"},
    total=False,
)

UpdateServiceIntegrationConfigTypeDef = TypedDict(
    "UpdateServiceIntegrationConfigTypeDef",
    {"OpsCenter": "OpsCenterIntegrationConfigTypeDef"},
    total=False,
)
