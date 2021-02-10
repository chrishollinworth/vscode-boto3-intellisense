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
    {"StackName": str, "Insight": "InsightHealthTypeDef"},
    total=False,
)

CloudWatchMetricsDetailTypeDef = TypedDict(
    "CloudWatchMetricsDetailTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List["CloudWatchMetricsDimensionTypeDef"],
        "Stat": Literal["Sum", "Average", "SampleCount", "Minimum", "Maximum", "p99", "p90", "p50"],
        "Unit": str,
        "Period": int,
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
    "EventResourceTypeDef", {"Type": str, "Name": str, "Arn": str}, total=False
)

EventTimeRangeTypeDef = TypedDict(
    "EventTimeRangeTypeDef", {"FromTime": datetime, "ToTime": datetime}
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "ResourceCollection": "ResourceCollectionTypeDef",
        "Id": str,
        "Time": datetime,
        "EventSource": str,
        "Name": str,
        "DataSource": Literal["AWS_CLOUD_TRAIL", "AWS_CODE_DEPLOY"],
        "EventClass": Literal[
            "INFRASTRUCTURE", "DEPLOYMENT", "SECURITY_CHANGE", "CONFIG_CHANGE", "SCHEMA_CHANGE"
        ],
        "Resources": List["EventResourceTypeDef"],
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
    "_RequiredInsightTimeRangeTypeDef", {"StartTime": datetime}
)
_OptionalInsightTimeRangeTypeDef = TypedDict(
    "_OptionalInsightTimeRangeTypeDef", {"EndTime": datetime}, total=False
)


class InsightTimeRangeTypeDef(_RequiredInsightTimeRangeTypeDef, _OptionalInsightTimeRangeTypeDef):
    pass


ListInsightsAnyStatusFilterTypeDef = TypedDict(
    "ListInsightsAnyStatusFilterTypeDef",
    {"Type": Literal["REACTIVE", "PROACTIVE"], "StartTimeRange": "StartTimeRangeTypeDef"},
)

ListInsightsClosedStatusFilterTypeDef = TypedDict(
    "ListInsightsClosedStatusFilterTypeDef",
    {"Type": Literal["REACTIVE", "PROACTIVE"], "EndTimeRange": "EndTimeRangeTypeDef"},
)

ListInsightsOngoingStatusFilterTypeDef = TypedDict(
    "ListInsightsOngoingStatusFilterTypeDef", {"Type": Literal["REACTIVE", "PROACTIVE"]}
)

NotificationChannelConfigTypeDef = TypedDict(
    "NotificationChannelConfigTypeDef", {"Sns": "SnsChannelConfigTypeDef"}
)

NotificationChannelTypeDef = TypedDict(
    "NotificationChannelTypeDef",
    {"Id": str, "Config": "NotificationChannelConfigTypeDef"},
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
        "Id": str,
        "Severity": Literal["LOW", "MEDIUM", "HIGH"],
        "Status": Literal["ONGOING", "CLOSED"],
        "UpdateTime": datetime,
        "AnomalyTimeRange": "AnomalyTimeRangeTypeDef",
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
        "Severity": Literal["LOW", "MEDIUM", "HIGH"],
        "Status": Literal["ONGOING", "CLOSED"],
        "UpdateTime": datetime,
        "AnomalyTimeRange": "AnomalyTimeRangeTypeDef",
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
        "Severity": Literal["LOW", "MEDIUM", "HIGH"],
        "Status": Literal["ONGOING", "CLOSED"],
        "InsightTimeRange": "InsightTimeRangeTypeDef",
        "PredictionTimeRange": "PredictionTimeRangeTypeDef",
        "ResourceCollection": "ResourceCollectionTypeDef",
    },
    total=False,
)

ProactiveInsightTypeDef = TypedDict(
    "ProactiveInsightTypeDef",
    {
        "Id": str,
        "Name": str,
        "Severity": Literal["LOW", "MEDIUM", "HIGH"],
        "Status": Literal["ONGOING", "CLOSED"],
        "InsightTimeRange": "InsightTimeRangeTypeDef",
        "PredictionTimeRange": "PredictionTimeRangeTypeDef",
        "ResourceCollection": "ResourceCollectionTypeDef",
        "SsmOpsItemId": str,
    },
    total=False,
)

ReactiveAnomalySummaryTypeDef = TypedDict(
    "ReactiveAnomalySummaryTypeDef",
    {
        "Id": str,
        "Severity": Literal["LOW", "MEDIUM", "HIGH"],
        "Status": Literal["ONGOING", "CLOSED"],
        "AnomalyTimeRange": "AnomalyTimeRangeTypeDef",
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
        "Severity": Literal["LOW", "MEDIUM", "HIGH"],
        "Status": Literal["ONGOING", "CLOSED"],
        "AnomalyTimeRange": "AnomalyTimeRangeTypeDef",
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
        "Severity": Literal["LOW", "MEDIUM", "HIGH"],
        "Status": Literal["ONGOING", "CLOSED"],
        "InsightTimeRange": "InsightTimeRangeTypeDef",
        "ResourceCollection": "ResourceCollectionTypeDef",
    },
    total=False,
)

ReactiveInsightTypeDef = TypedDict(
    "ReactiveInsightTypeDef",
    {
        "Id": str,
        "Name": str,
        "Severity": Literal["LOW", "MEDIUM", "HIGH"],
        "Status": Literal["ONGOING", "CLOSED"],
        "InsightTimeRange": "InsightTimeRangeTypeDef",
        "ResourceCollection": "ResourceCollectionTypeDef",
        "SsmOpsItemId": str,
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
        "RelatedEvents": List["RecommendationRelatedEventTypeDef"],
        "RelatedAnomalies": List["RecommendationRelatedAnomalyTypeDef"],
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
    "AddNotificationChannelResponseTypeDef", {"Id": str}
)

DescribeAccountHealthResponseTypeDef = TypedDict(
    "DescribeAccountHealthResponseTypeDef",
    {
        "OpenReactiveInsights": int,
        "OpenProactiveInsights": int,
        "MetricsAnalyzed": int,
        "ResourceHours": int,
    },
)

DescribeAccountOverviewResponseTypeDef = TypedDict(
    "DescribeAccountOverviewResponseTypeDef",
    {"ReactiveInsights": int, "ProactiveInsights": int, "MeanTimeToRecoverInMilliseconds": int},
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

_RequiredDescribeResourceCollectionHealthResponseTypeDef = TypedDict(
    "_RequiredDescribeResourceCollectionHealthResponseTypeDef",
    {"CloudFormation": List["CloudFormationHealthTypeDef"]},
)
_OptionalDescribeResourceCollectionHealthResponseTypeDef = TypedDict(
    "_OptionalDescribeResourceCollectionHealthResponseTypeDef", {"NextToken": str}, total=False
)


class DescribeResourceCollectionHealthResponseTypeDef(
    _RequiredDescribeResourceCollectionHealthResponseTypeDef,
    _OptionalDescribeResourceCollectionHealthResponseTypeDef,
):
    pass


DescribeServiceIntegrationResponseTypeDef = TypedDict(
    "DescribeServiceIntegrationResponseTypeDef",
    {"ServiceIntegration": "ServiceIntegrationConfigTypeDef"},
    total=False,
)

GetResourceCollectionResponseTypeDef = TypedDict(
    "GetResourceCollectionResponseTypeDef",
    {"ResourceCollection": "ResourceCollectionFilterTypeDef", "NextToken": str},
    total=False,
)

InsightFeedbackTypeDef = TypedDict(
    "InsightFeedbackTypeDef",
    {
        "Id": str,
        "Feedback": Literal[
            "VALID_COLLECTION",
            "RECOMMENDATION_USEFUL",
            "ALERT_TOO_SENSITIVE",
            "DATA_NOISY_ANOMALY",
            "DATA_INCORRECT",
        ],
    },
    total=False,
)

ListAnomaliesForInsightResponseTypeDef = TypedDict(
    "ListAnomaliesForInsightResponseTypeDef",
    {
        "ProactiveAnomalies": List["ProactiveAnomalySummaryTypeDef"],
        "ReactiveAnomalies": List["ReactiveAnomalySummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListEventsFiltersTypeDef = TypedDict(
    "ListEventsFiltersTypeDef",
    {
        "InsightId": str,
        "EventTimeRange": "EventTimeRangeTypeDef",
        "EventClass": Literal[
            "INFRASTRUCTURE", "DEPLOYMENT", "SECURITY_CHANGE", "CONFIG_CHANGE", "SCHEMA_CHANGE"
        ],
        "EventSource": str,
        "DataSource": Literal["AWS_CLOUD_TRAIL", "AWS_CODE_DEPLOY"],
        "ResourceCollection": "ResourceCollectionTypeDef",
    },
    total=False,
)

_RequiredListEventsResponseTypeDef = TypedDict(
    "_RequiredListEventsResponseTypeDef", {"Events": List["EventTypeDef"]}
)
_OptionalListEventsResponseTypeDef = TypedDict(
    "_OptionalListEventsResponseTypeDef", {"NextToken": str}, total=False
)


class ListEventsResponseTypeDef(
    _RequiredListEventsResponseTypeDef, _OptionalListEventsResponseTypeDef
):
    pass


ListInsightsResponseTypeDef = TypedDict(
    "ListInsightsResponseTypeDef",
    {
        "ProactiveInsights": List["ProactiveInsightSummaryTypeDef"],
        "ReactiveInsights": List["ReactiveInsightSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
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

ListNotificationChannelsResponseTypeDef = TypedDict(
    "ListNotificationChannelsResponseTypeDef",
    {"Channels": List["NotificationChannelTypeDef"], "NextToken": str},
    total=False,
)

ListRecommendationsResponseTypeDef = TypedDict(
    "ListRecommendationsResponseTypeDef",
    {"Recommendations": List["RecommendationTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

SearchInsightsFiltersTypeDef = TypedDict(
    "SearchInsightsFiltersTypeDef",
    {
        "Severities": List[Literal["LOW", "MEDIUM", "HIGH"]],
        "Statuses": List[Literal["ONGOING", "CLOSED"]],
        "ResourceCollection": "ResourceCollectionTypeDef",
    },
    total=False,
)

SearchInsightsResponseTypeDef = TypedDict(
    "SearchInsightsResponseTypeDef",
    {
        "ProactiveInsights": List["ProactiveInsightSummaryTypeDef"],
        "ReactiveInsights": List["ReactiveInsightSummaryTypeDef"],
        "NextToken": str,
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
