"""
Type annotations for devops-guru service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/type_defs.html)

Usage::

    ```python
    from mypy_boto3_devops_guru.type_defs import AccountHealthTypeDef

    data: AccountHealthTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AnomalySeverityType,
    AnomalyStatusType,
    AnomalyTypeType,
    CloudWatchMetricDataStatusCodeType,
    CloudWatchMetricsStatType,
    CostEstimationServiceResourceStateType,
    CostEstimationStatusType,
    EventClassType,
    EventDataSourceType,
    EventSourceOptInStatusType,
    InsightFeedbackOptionType,
    InsightSeverityType,
    InsightStatusType,
    InsightTypeType,
    LocaleType,
    LogAnomalyTypeType,
    NotificationMessageTypeType,
    OptInStatusType,
    OrganizationResourceCollectionTypeType,
    ResourceCollectionTypeType,
    ResourcePermissionType,
    ResourceTypeFilterType,
    ServiceNameType,
    UpdateResourceCollectionActionType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountHealthTypeDef",
    "AccountInsightHealthTypeDef",
    "AddNotificationChannelRequestRequestTypeDef",
    "AddNotificationChannelResponseTypeDef",
    "AmazonCodeGuruProfilerIntegrationTypeDef",
    "AnomalousLogGroupTypeDef",
    "AnomalyReportedTimeRangeTypeDef",
    "AnomalyResourceTypeDef",
    "AnomalySourceDetailsTypeDef",
    "AnomalySourceMetadataTypeDef",
    "AnomalyTimeRangeTypeDef",
    "CloudFormationCollectionFilterTypeDef",
    "CloudFormationCollectionTypeDef",
    "CloudFormationCostEstimationResourceCollectionFilterTypeDef",
    "CloudFormationHealthTypeDef",
    "CloudWatchMetricsDataSummaryTypeDef",
    "CloudWatchMetricsDetailTypeDef",
    "CloudWatchMetricsDimensionTypeDef",
    "CostEstimationResourceCollectionFilterTypeDef",
    "CostEstimationTimeRangeTypeDef",
    "DeleteInsightRequestRequestTypeDef",
    "DescribeAccountHealthResponseTypeDef",
    "DescribeAccountOverviewRequestRequestTypeDef",
    "DescribeAccountOverviewResponseTypeDef",
    "DescribeAnomalyRequestRequestTypeDef",
    "DescribeAnomalyResponseTypeDef",
    "DescribeEventSourcesConfigResponseTypeDef",
    "DescribeFeedbackRequestRequestTypeDef",
    "DescribeFeedbackResponseTypeDef",
    "DescribeInsightRequestRequestTypeDef",
    "DescribeInsightResponseTypeDef",
    "DescribeOrganizationHealthRequestRequestTypeDef",
    "DescribeOrganizationHealthResponseTypeDef",
    "DescribeOrganizationOverviewRequestRequestTypeDef",
    "DescribeOrganizationOverviewResponseTypeDef",
    "DescribeOrganizationResourceCollectionHealthRequestRequestTypeDef",
    "DescribeOrganizationResourceCollectionHealthResponseTypeDef",
    "DescribeResourceCollectionHealthRequestRequestTypeDef",
    "DescribeResourceCollectionHealthResponseTypeDef",
    "DescribeServiceIntegrationResponseTypeDef",
    "EndTimeRangeTypeDef",
    "EventResourceTypeDef",
    "EventSourcesConfigTypeDef",
    "EventTimeRangeTypeDef",
    "EventTypeDef",
    "GetCostEstimationRequestRequestTypeDef",
    "GetCostEstimationResponseTypeDef",
    "GetResourceCollectionRequestRequestTypeDef",
    "GetResourceCollectionResponseTypeDef",
    "InsightFeedbackTypeDef",
    "InsightHealthTypeDef",
    "InsightTimeRangeTypeDef",
    "ListAnomaliesForInsightFiltersTypeDef",
    "ListAnomaliesForInsightRequestRequestTypeDef",
    "ListAnomaliesForInsightResponseTypeDef",
    "ListAnomalousLogGroupsRequestRequestTypeDef",
    "ListAnomalousLogGroupsResponseTypeDef",
    "ListEventsFiltersTypeDef",
    "ListEventsRequestRequestTypeDef",
    "ListEventsResponseTypeDef",
    "ListInsightsAnyStatusFilterTypeDef",
    "ListInsightsClosedStatusFilterTypeDef",
    "ListInsightsOngoingStatusFilterTypeDef",
    "ListInsightsRequestRequestTypeDef",
    "ListInsightsResponseTypeDef",
    "ListInsightsStatusFilterTypeDef",
    "ListMonitoredResourcesFiltersTypeDef",
    "ListMonitoredResourcesRequestRequestTypeDef",
    "ListMonitoredResourcesResponseTypeDef",
    "ListNotificationChannelsRequestRequestTypeDef",
    "ListNotificationChannelsResponseTypeDef",
    "ListOrganizationInsightsRequestRequestTypeDef",
    "ListOrganizationInsightsResponseTypeDef",
    "ListRecommendationsRequestRequestTypeDef",
    "ListRecommendationsResponseTypeDef",
    "LogAnomalyClassTypeDef",
    "LogAnomalyShowcaseTypeDef",
    "LogsAnomalyDetectionIntegrationConfigTypeDef",
    "LogsAnomalyDetectionIntegrationTypeDef",
    "MonitoredResourceIdentifierTypeDef",
    "NotificationChannelConfigTypeDef",
    "NotificationChannelTypeDef",
    "NotificationFilterConfigTypeDef",
    "OpsCenterIntegrationConfigTypeDef",
    "OpsCenterIntegrationTypeDef",
    "PaginatorConfigTypeDef",
    "PerformanceInsightsMetricDimensionGroupTypeDef",
    "PerformanceInsightsMetricQueryTypeDef",
    "PerformanceInsightsMetricsDetailTypeDef",
    "PerformanceInsightsReferenceComparisonValuesTypeDef",
    "PerformanceInsightsReferenceDataTypeDef",
    "PerformanceInsightsReferenceMetricTypeDef",
    "PerformanceInsightsReferenceScalarTypeDef",
    "PerformanceInsightsStatTypeDef",
    "PredictionTimeRangeTypeDef",
    "ProactiveAnomalySummaryTypeDef",
    "ProactiveAnomalyTypeDef",
    "ProactiveInsightSummaryTypeDef",
    "ProactiveInsightTypeDef",
    "ProactiveOrganizationInsightSummaryTypeDef",
    "PutFeedbackRequestRequestTypeDef",
    "ReactiveAnomalySummaryTypeDef",
    "ReactiveAnomalyTypeDef",
    "ReactiveInsightSummaryTypeDef",
    "ReactiveInsightTypeDef",
    "ReactiveOrganizationInsightSummaryTypeDef",
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
    "SearchOrganizationInsightsFiltersTypeDef",
    "SearchOrganizationInsightsRequestRequestTypeDef",
    "SearchOrganizationInsightsResponseTypeDef",
    "ServiceCollectionTypeDef",
    "ServiceHealthTypeDef",
    "ServiceInsightHealthTypeDef",
    "ServiceIntegrationConfigTypeDef",
    "ServiceResourceCostTypeDef",
    "SnsChannelConfigTypeDef",
    "StartCostEstimationRequestRequestTypeDef",
    "StartTimeRangeTypeDef",
    "TagCollectionFilterTypeDef",
    "TagCollectionTypeDef",
    "TagCostEstimationResourceCollectionFilterTypeDef",
    "TagHealthTypeDef",
    "TimestampMetricValuePairTypeDef",
    "UpdateCloudFormationCollectionFilterTypeDef",
    "UpdateEventSourcesConfigRequestRequestTypeDef",
    "UpdateResourceCollectionFilterTypeDef",
    "UpdateResourceCollectionRequestRequestTypeDef",
    "UpdateServiceIntegrationConfigTypeDef",
    "UpdateServiceIntegrationRequestRequestTypeDef",
    "UpdateTagCollectionFilterTypeDef",
)

AccountHealthTypeDef = TypedDict(
    "AccountHealthTypeDef",
    {
        "AccountId": str,
        "Insight": "AccountInsightHealthTypeDef",
    },
    total=False,
)

AccountInsightHealthTypeDef = TypedDict(
    "AccountInsightHealthTypeDef",
    {
        "OpenProactiveInsights": int,
        "OpenReactiveInsights": int,
    },
    total=False,
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

AmazonCodeGuruProfilerIntegrationTypeDef = TypedDict(
    "AmazonCodeGuruProfilerIntegrationTypeDef",
    {
        "Status": EventSourceOptInStatusType,
    },
    total=False,
)

AnomalousLogGroupTypeDef = TypedDict(
    "AnomalousLogGroupTypeDef",
    {
        "LogGroupName": str,
        "ImpactStartTime": datetime,
        "ImpactEndTime": datetime,
        "NumberOfLogLinesScanned": int,
        "LogAnomalyShowcases": List["LogAnomalyShowcaseTypeDef"],
    },
    total=False,
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

AnomalyResourceTypeDef = TypedDict(
    "AnomalyResourceTypeDef",
    {
        "Name": str,
        "Type": str,
    },
    total=False,
)

AnomalySourceDetailsTypeDef = TypedDict(
    "AnomalySourceDetailsTypeDef",
    {
        "CloudWatchMetrics": List["CloudWatchMetricsDetailTypeDef"],
        "PerformanceInsightsMetrics": List["PerformanceInsightsMetricsDetailTypeDef"],
    },
    total=False,
)

AnomalySourceMetadataTypeDef = TypedDict(
    "AnomalySourceMetadataTypeDef",
    {
        "Source": str,
        "SourceResourceName": str,
        "SourceResourceType": str,
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
        "AnalyzedResourceCount": int,
    },
    total=False,
)

CloudWatchMetricsDataSummaryTypeDef = TypedDict(
    "CloudWatchMetricsDataSummaryTypeDef",
    {
        "TimestampMetricValuePairList": List["TimestampMetricValuePairTypeDef"],
        "StatusCode": CloudWatchMetricDataStatusCodeType,
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
        "MetricDataSummary": "CloudWatchMetricsDataSummaryTypeDef",
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
        "Tags": List["TagCostEstimationResourceCollectionFilterTypeDef"],
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

DeleteInsightRequestRequestTypeDef = TypedDict(
    "DeleteInsightRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeAccountHealthResponseTypeDef = TypedDict(
    "DescribeAccountHealthResponseTypeDef",
    {
        "OpenReactiveInsights": int,
        "OpenProactiveInsights": int,
        "MetricsAnalyzed": int,
        "ResourceHours": int,
        "AnalyzedResourceCount": int,
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

_RequiredDescribeAnomalyRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAnomalyRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDescribeAnomalyRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAnomalyRequestRequestTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)

class DescribeAnomalyRequestRequestTypeDef(
    _RequiredDescribeAnomalyRequestRequestTypeDef, _OptionalDescribeAnomalyRequestRequestTypeDef
):
    pass

DescribeAnomalyResponseTypeDef = TypedDict(
    "DescribeAnomalyResponseTypeDef",
    {
        "ProactiveAnomaly": "ProactiveAnomalyTypeDef",
        "ReactiveAnomaly": "ReactiveAnomalyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventSourcesConfigResponseTypeDef = TypedDict(
    "DescribeEventSourcesConfigResponseTypeDef",
    {
        "EventSources": "EventSourcesConfigTypeDef",
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

_RequiredDescribeInsightRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeInsightRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDescribeInsightRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeInsightRequestRequestTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)

class DescribeInsightRequestRequestTypeDef(
    _RequiredDescribeInsightRequestRequestTypeDef, _OptionalDescribeInsightRequestRequestTypeDef
):
    pass

DescribeInsightResponseTypeDef = TypedDict(
    "DescribeInsightResponseTypeDef",
    {
        "ProactiveInsight": "ProactiveInsightTypeDef",
        "ReactiveInsight": "ReactiveInsightTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationHealthRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationHealthRequestRequestTypeDef",
    {
        "AccountIds": List[str],
        "OrganizationalUnitIds": List[str],
    },
    total=False,
)

DescribeOrganizationHealthResponseTypeDef = TypedDict(
    "DescribeOrganizationHealthResponseTypeDef",
    {
        "OpenReactiveInsights": int,
        "OpenProactiveInsights": int,
        "MetricsAnalyzed": int,
        "ResourceHours": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeOrganizationOverviewRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeOrganizationOverviewRequestRequestTypeDef",
    {
        "FromTime": Union[datetime, str],
    },
)
_OptionalDescribeOrganizationOverviewRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeOrganizationOverviewRequestRequestTypeDef",
    {
        "ToTime": Union[datetime, str],
        "AccountIds": List[str],
        "OrganizationalUnitIds": List[str],
    },
    total=False,
)

class DescribeOrganizationOverviewRequestRequestTypeDef(
    _RequiredDescribeOrganizationOverviewRequestRequestTypeDef,
    _OptionalDescribeOrganizationOverviewRequestRequestTypeDef,
):
    pass

DescribeOrganizationOverviewResponseTypeDef = TypedDict(
    "DescribeOrganizationOverviewResponseTypeDef",
    {
        "ReactiveInsights": int,
        "ProactiveInsights": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeOrganizationResourceCollectionHealthRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeOrganizationResourceCollectionHealthRequestRequestTypeDef",
    {
        "OrganizationResourceCollectionType": OrganizationResourceCollectionTypeType,
    },
)
_OptionalDescribeOrganizationResourceCollectionHealthRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeOrganizationResourceCollectionHealthRequestRequestTypeDef",
    {
        "AccountIds": List[str],
        "OrganizationalUnitIds": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeOrganizationResourceCollectionHealthRequestRequestTypeDef(
    _RequiredDescribeOrganizationResourceCollectionHealthRequestRequestTypeDef,
    _OptionalDescribeOrganizationResourceCollectionHealthRequestRequestTypeDef,
):
    pass

DescribeOrganizationResourceCollectionHealthResponseTypeDef = TypedDict(
    "DescribeOrganizationResourceCollectionHealthResponseTypeDef",
    {
        "CloudFormation": List["CloudFormationHealthTypeDef"],
        "Service": List["ServiceHealthTypeDef"],
        "Account": List["AccountHealthTypeDef"],
        "NextToken": str,
        "Tags": List["TagHealthTypeDef"],
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
        "Tags": List["TagHealthTypeDef"],
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

EventSourcesConfigTypeDef = TypedDict(
    "EventSourcesConfigTypeDef",
    {
        "AmazonCodeGuruProfiler": "AmazonCodeGuruProfilerIntegrationTypeDef",
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

ListAnomaliesForInsightFiltersTypeDef = TypedDict(
    "ListAnomaliesForInsightFiltersTypeDef",
    {
        "ServiceCollection": "ServiceCollectionTypeDef",
    },
    total=False,
)

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
        "AccountId": str,
        "Filters": "ListAnomaliesForInsightFiltersTypeDef",
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

_RequiredListAnomalousLogGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListAnomalousLogGroupsRequestRequestTypeDef",
    {
        "InsightId": str,
    },
)
_OptionalListAnomalousLogGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListAnomalousLogGroupsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAnomalousLogGroupsRequestRequestTypeDef(
    _RequiredListAnomalousLogGroupsRequestRequestTypeDef,
    _OptionalListAnomalousLogGroupsRequestRequestTypeDef,
):
    pass

ListAnomalousLogGroupsResponseTypeDef = TypedDict(
    "ListAnomalousLogGroupsResponseTypeDef",
    {
        "InsightId": str,
        "AnomalousLogGroups": List["AnomalousLogGroupTypeDef"],
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
        "AccountId": str,
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

ListMonitoredResourcesFiltersTypeDef = TypedDict(
    "ListMonitoredResourcesFiltersTypeDef",
    {
        "ResourcePermission": ResourcePermissionType,
        "ResourceTypeFilters": List[ResourceTypeFilterType],
    },
)

ListMonitoredResourcesRequestRequestTypeDef = TypedDict(
    "ListMonitoredResourcesRequestRequestTypeDef",
    {
        "Filters": "ListMonitoredResourcesFiltersTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListMonitoredResourcesResponseTypeDef = TypedDict(
    "ListMonitoredResourcesResponseTypeDef",
    {
        "MonitoredResourceIdentifiers": List["MonitoredResourceIdentifierTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredListOrganizationInsightsRequestRequestTypeDef = TypedDict(
    "_RequiredListOrganizationInsightsRequestRequestTypeDef",
    {
        "StatusFilter": "ListInsightsStatusFilterTypeDef",
    },
)
_OptionalListOrganizationInsightsRequestRequestTypeDef = TypedDict(
    "_OptionalListOrganizationInsightsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "AccountIds": List[str],
        "OrganizationalUnitIds": List[str],
        "NextToken": str,
    },
    total=False,
)

class ListOrganizationInsightsRequestRequestTypeDef(
    _RequiredListOrganizationInsightsRequestRequestTypeDef,
    _OptionalListOrganizationInsightsRequestRequestTypeDef,
):
    pass

ListOrganizationInsightsResponseTypeDef = TypedDict(
    "ListOrganizationInsightsResponseTypeDef",
    {
        "ProactiveInsights": List["ProactiveOrganizationInsightSummaryTypeDef"],
        "ReactiveInsights": List["ReactiveOrganizationInsightSummaryTypeDef"],
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
        "AccountId": str,
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

LogAnomalyClassTypeDef = TypedDict(
    "LogAnomalyClassTypeDef",
    {
        "LogStreamName": str,
        "LogAnomalyType": LogAnomalyTypeType,
        "LogAnomalyToken": str,
        "LogEventId": str,
        "Explanation": str,
        "NumberOfLogLinesOccurrences": int,
        "LogEventTimestamp": datetime,
    },
    total=False,
)

LogAnomalyShowcaseTypeDef = TypedDict(
    "LogAnomalyShowcaseTypeDef",
    {
        "LogAnomalyClasses": List["LogAnomalyClassTypeDef"],
    },
    total=False,
)

LogsAnomalyDetectionIntegrationConfigTypeDef = TypedDict(
    "LogsAnomalyDetectionIntegrationConfigTypeDef",
    {
        "OptInStatus": OptInStatusType,
    },
    total=False,
)

LogsAnomalyDetectionIntegrationTypeDef = TypedDict(
    "LogsAnomalyDetectionIntegrationTypeDef",
    {
        "OptInStatus": OptInStatusType,
    },
    total=False,
)

MonitoredResourceIdentifierTypeDef = TypedDict(
    "MonitoredResourceIdentifierTypeDef",
    {
        "MonitoredResourceName": str,
        "Type": str,
        "ResourcePermission": ResourcePermissionType,
        "LastUpdated": datetime,
        "ResourceCollection": "ResourceCollectionTypeDef",
    },
    total=False,
)

_RequiredNotificationChannelConfigTypeDef = TypedDict(
    "_RequiredNotificationChannelConfigTypeDef",
    {
        "Sns": "SnsChannelConfigTypeDef",
    },
)
_OptionalNotificationChannelConfigTypeDef = TypedDict(
    "_OptionalNotificationChannelConfigTypeDef",
    {
        "Filters": "NotificationFilterConfigTypeDef",
    },
    total=False,
)

class NotificationChannelConfigTypeDef(
    _RequiredNotificationChannelConfigTypeDef, _OptionalNotificationChannelConfigTypeDef
):
    pass

NotificationChannelTypeDef = TypedDict(
    "NotificationChannelTypeDef",
    {
        "Id": str,
        "Config": "NotificationChannelConfigTypeDef",
    },
    total=False,
)

NotificationFilterConfigTypeDef = TypedDict(
    "NotificationFilterConfigTypeDef",
    {
        "Severities": List[InsightSeverityType],
        "MessageTypes": List[NotificationMessageTypeType],
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

PerformanceInsightsMetricDimensionGroupTypeDef = TypedDict(
    "PerformanceInsightsMetricDimensionGroupTypeDef",
    {
        "Group": str,
        "Dimensions": List[str],
        "Limit": int,
    },
    total=False,
)

PerformanceInsightsMetricQueryTypeDef = TypedDict(
    "PerformanceInsightsMetricQueryTypeDef",
    {
        "Metric": str,
        "GroupBy": "PerformanceInsightsMetricDimensionGroupTypeDef",
        "Filter": Dict[str, str],
    },
    total=False,
)

PerformanceInsightsMetricsDetailTypeDef = TypedDict(
    "PerformanceInsightsMetricsDetailTypeDef",
    {
        "MetricDisplayName": str,
        "Unit": str,
        "MetricQuery": "PerformanceInsightsMetricQueryTypeDef",
        "ReferenceData": List["PerformanceInsightsReferenceDataTypeDef"],
        "StatsAtAnomaly": List["PerformanceInsightsStatTypeDef"],
        "StatsAtBaseline": List["PerformanceInsightsStatTypeDef"],
    },
    total=False,
)

PerformanceInsightsReferenceComparisonValuesTypeDef = TypedDict(
    "PerformanceInsightsReferenceComparisonValuesTypeDef",
    {
        "ReferenceScalar": "PerformanceInsightsReferenceScalarTypeDef",
        "ReferenceMetric": "PerformanceInsightsReferenceMetricTypeDef",
    },
    total=False,
)

PerformanceInsightsReferenceDataTypeDef = TypedDict(
    "PerformanceInsightsReferenceDataTypeDef",
    {
        "Name": str,
        "ComparisonValues": "PerformanceInsightsReferenceComparisonValuesTypeDef",
    },
    total=False,
)

PerformanceInsightsReferenceMetricTypeDef = TypedDict(
    "PerformanceInsightsReferenceMetricTypeDef",
    {
        "MetricQuery": "PerformanceInsightsMetricQueryTypeDef",
    },
    total=False,
)

PerformanceInsightsReferenceScalarTypeDef = TypedDict(
    "PerformanceInsightsReferenceScalarTypeDef",
    {
        "Value": float,
    },
    total=False,
)

PerformanceInsightsStatTypeDef = TypedDict(
    "PerformanceInsightsStatTypeDef",
    {
        "Type": str,
        "Value": float,
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
        "SourceMetadata": "AnomalySourceMetadataTypeDef",
        "AnomalyResources": List["AnomalyResourceTypeDef"],
        "Description": str,
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
        "SourceMetadata": "AnomalySourceMetadataTypeDef",
        "AnomalyResources": List["AnomalyResourceTypeDef"],
        "Description": str,
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
        "AssociatedResourceArns": List[str],
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
        "Description": str,
    },
    total=False,
)

ProactiveOrganizationInsightSummaryTypeDef = TypedDict(
    "ProactiveOrganizationInsightSummaryTypeDef",
    {
        "Id": str,
        "AccountId": str,
        "OrganizationalUnitId": str,
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
        "Type": AnomalyTypeType,
        "Name": str,
        "Description": str,
        "CausalAnomalyId": str,
        "AnomalyResources": List["AnomalyResourceTypeDef"],
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
        "Type": AnomalyTypeType,
        "Name": str,
        "Description": str,
        "CausalAnomalyId": str,
        "AnomalyResources": List["AnomalyResourceTypeDef"],
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
        "AssociatedResourceArns": List[str],
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
        "Description": str,
    },
    total=False,
)

ReactiveOrganizationInsightSummaryTypeDef = TypedDict(
    "ReactiveOrganizationInsightSummaryTypeDef",
    {
        "Id": str,
        "AccountId": str,
        "OrganizationalUnitId": str,
        "Name": str,
        "Severity": InsightSeverityType,
        "Status": InsightStatusType,
        "InsightTimeRange": "InsightTimeRangeTypeDef",
        "ResourceCollection": "ResourceCollectionTypeDef",
        "ServiceCollection": "ServiceCollectionTypeDef",
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
        "AnomalyId": str,
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
        "Category": str,
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
        "Tags": List["TagCollectionFilterTypeDef"],
    },
    total=False,
)

ResourceCollectionTypeDef = TypedDict(
    "ResourceCollectionTypeDef",
    {
        "CloudFormation": "CloudFormationCollectionTypeDef",
        "Tags": List["TagCollectionTypeDef"],
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

SearchOrganizationInsightsFiltersTypeDef = TypedDict(
    "SearchOrganizationInsightsFiltersTypeDef",
    {
        "Severities": List[InsightSeverityType],
        "Statuses": List[InsightStatusType],
        "ResourceCollection": "ResourceCollectionTypeDef",
        "ServiceCollection": "ServiceCollectionTypeDef",
    },
    total=False,
)

_RequiredSearchOrganizationInsightsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchOrganizationInsightsRequestRequestTypeDef",
    {
        "AccountIds": List[str],
        "StartTimeRange": "StartTimeRangeTypeDef",
        "Type": InsightTypeType,
    },
)
_OptionalSearchOrganizationInsightsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchOrganizationInsightsRequestRequestTypeDef",
    {
        "Filters": "SearchOrganizationInsightsFiltersTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class SearchOrganizationInsightsRequestRequestTypeDef(
    _RequiredSearchOrganizationInsightsRequestRequestTypeDef,
    _OptionalSearchOrganizationInsightsRequestRequestTypeDef,
):
    pass

SearchOrganizationInsightsResponseTypeDef = TypedDict(
    "SearchOrganizationInsightsResponseTypeDef",
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
        "AnalyzedResourceCount": int,
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
        "LogsAnomalyDetection": "LogsAnomalyDetectionIntegrationTypeDef",
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

TagCollectionFilterTypeDef = TypedDict(
    "TagCollectionFilterTypeDef",
    {
        "AppBoundaryKey": str,
        "TagValues": List[str],
    },
)

TagCollectionTypeDef = TypedDict(
    "TagCollectionTypeDef",
    {
        "AppBoundaryKey": str,
        "TagValues": List[str],
    },
)

TagCostEstimationResourceCollectionFilterTypeDef = TypedDict(
    "TagCostEstimationResourceCollectionFilterTypeDef",
    {
        "AppBoundaryKey": str,
        "TagValues": List[str],
    },
)

TagHealthTypeDef = TypedDict(
    "TagHealthTypeDef",
    {
        "AppBoundaryKey": str,
        "TagValue": str,
        "Insight": "InsightHealthTypeDef",
        "AnalyzedResourceCount": int,
    },
    total=False,
)

TimestampMetricValuePairTypeDef = TypedDict(
    "TimestampMetricValuePairTypeDef",
    {
        "Timestamp": datetime,
        "MetricValue": float,
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

UpdateEventSourcesConfigRequestRequestTypeDef = TypedDict(
    "UpdateEventSourcesConfigRequestRequestTypeDef",
    {
        "EventSources": "EventSourcesConfigTypeDef",
    },
    total=False,
)

UpdateResourceCollectionFilterTypeDef = TypedDict(
    "UpdateResourceCollectionFilterTypeDef",
    {
        "CloudFormation": "UpdateCloudFormationCollectionFilterTypeDef",
        "Tags": List["UpdateTagCollectionFilterTypeDef"],
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
        "LogsAnomalyDetection": "LogsAnomalyDetectionIntegrationConfigTypeDef",
    },
    total=False,
)

UpdateServiceIntegrationRequestRequestTypeDef = TypedDict(
    "UpdateServiceIntegrationRequestRequestTypeDef",
    {
        "ServiceIntegration": "UpdateServiceIntegrationConfigTypeDef",
    },
)

UpdateTagCollectionFilterTypeDef = TypedDict(
    "UpdateTagCollectionFilterTypeDef",
    {
        "AppBoundaryKey": str,
        "TagValues": List[str],
    },
)
