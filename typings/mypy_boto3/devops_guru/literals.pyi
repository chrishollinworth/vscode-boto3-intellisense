"""
Type annotations for devops-guru service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/literals.html)

Usage::

    ```python
    from mypy_boto3_devops_guru.literals import AnomalySeverityType

    data: AnomalySeverityType = "HIGH"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AnomalySeverityType",
    "AnomalyStatusType",
    "AnomalyTypeType",
    "CloudWatchMetricDataStatusCodeType",
    "CloudWatchMetricsStatType",
    "CostEstimationServiceResourceStateType",
    "CostEstimationStatusType",
    "DescribeOrganizationResourceCollectionHealthPaginatorName",
    "DescribeResourceCollectionHealthPaginatorName",
    "EventClassType",
    "EventDataSourceType",
    "EventSourceOptInStatusType",
    "GetCostEstimationPaginatorName",
    "GetResourceCollectionPaginatorName",
    "InsightFeedbackOptionType",
    "InsightSeverityType",
    "InsightStatusType",
    "InsightTypeType",
    "ListAnomaliesForInsightPaginatorName",
    "ListAnomalousLogGroupsPaginatorName",
    "ListEventsPaginatorName",
    "ListInsightsPaginatorName",
    "ListMonitoredResourcesPaginatorName",
    "ListNotificationChannelsPaginatorName",
    "ListOrganizationInsightsPaginatorName",
    "ListRecommendationsPaginatorName",
    "LocaleType",
    "LogAnomalyTypeType",
    "OptInStatusType",
    "OrganizationResourceCollectionTypeType",
    "ResourceCollectionTypeType",
    "ResourcePermissionType",
    "ResourceTypeFilterType",
    "SearchInsightsPaginatorName",
    "SearchOrganizationInsightsPaginatorName",
    "ServiceNameType",
    "UpdateResourceCollectionActionType",
)

AnomalySeverityType = Literal["HIGH", "LOW", "MEDIUM"]
AnomalyStatusType = Literal["CLOSED", "ONGOING"]
AnomalyTypeType = Literal["CAUSAL", "CONTEXTUAL"]
CloudWatchMetricDataStatusCodeType = Literal["Complete", "InternalError", "PartialData"]
CloudWatchMetricsStatType = Literal[
    "Average", "Maximum", "Minimum", "SampleCount", "Sum", "p50", "p90", "p99"
]
CostEstimationServiceResourceStateType = Literal["ACTIVE", "INACTIVE"]
CostEstimationStatusType = Literal["COMPLETED", "ONGOING"]
DescribeOrganizationResourceCollectionHealthPaginatorName = Literal[
    "describe_organization_resource_collection_health"
]
DescribeResourceCollectionHealthPaginatorName = Literal["describe_resource_collection_health"]
EventClassType = Literal[
    "CONFIG_CHANGE", "DEPLOYMENT", "INFRASTRUCTURE", "SCHEMA_CHANGE", "SECURITY_CHANGE"
]
EventDataSourceType = Literal["AWS_CLOUD_TRAIL", "AWS_CODE_DEPLOY"]
EventSourceOptInStatusType = Literal["DISABLED", "ENABLED"]
GetCostEstimationPaginatorName = Literal["get_cost_estimation"]
GetResourceCollectionPaginatorName = Literal["get_resource_collection"]
InsightFeedbackOptionType = Literal[
    "ALERT_TOO_SENSITIVE",
    "DATA_INCORRECT",
    "DATA_NOISY_ANOMALY",
    "RECOMMENDATION_USEFUL",
    "VALID_COLLECTION",
]
InsightSeverityType = Literal["HIGH", "LOW", "MEDIUM"]
InsightStatusType = Literal["CLOSED", "ONGOING"]
InsightTypeType = Literal["PROACTIVE", "REACTIVE"]
ListAnomaliesForInsightPaginatorName = Literal["list_anomalies_for_insight"]
ListAnomalousLogGroupsPaginatorName = Literal["list_anomalous_log_groups"]
ListEventsPaginatorName = Literal["list_events"]
ListInsightsPaginatorName = Literal["list_insights"]
ListMonitoredResourcesPaginatorName = Literal["list_monitored_resources"]
ListNotificationChannelsPaginatorName = Literal["list_notification_channels"]
ListOrganizationInsightsPaginatorName = Literal["list_organization_insights"]
ListRecommendationsPaginatorName = Literal["list_recommendations"]
LocaleType = Literal[
    "DE_DE",
    "EN_GB",
    "EN_US",
    "ES_ES",
    "FR_FR",
    "IT_IT",
    "JA_JP",
    "KO_KR",
    "PT_BR",
    "ZH_CN",
    "ZH_TW",
]
LogAnomalyTypeType = Literal[
    "BLOCK_FORMAT",
    "FORMAT",
    "HTTP_CODE",
    "KEYWORD",
    "KEYWORD_TOKEN",
    "NEW_FIELD_NAME",
    "NUMERICAL_NAN",
    "NUMERICAL_POINT",
]
OptInStatusType = Literal["DISABLED", "ENABLED"]
OrganizationResourceCollectionTypeType = Literal[
    "AWS_ACCOUNT", "AWS_CLOUD_FORMATION", "AWS_SERVICE", "AWS_TAGS"
]
ResourceCollectionTypeType = Literal["AWS_CLOUD_FORMATION", "AWS_SERVICE", "AWS_TAGS"]
ResourcePermissionType = Literal["FULL_PERMISSION", "MISSING_PERMISSION"]
ResourceTypeFilterType = Literal["LOG_GROUPS"]
SearchInsightsPaginatorName = Literal["search_insights"]
SearchOrganizationInsightsPaginatorName = Literal["search_organization_insights"]
ServiceNameType = Literal[
    "API_GATEWAY",
    "APPLICATION_ELB",
    "AUTO_SCALING_GROUP",
    "CLOUD_FRONT",
    "DYNAMO_DB",
    "EC2",
    "ECS",
    "EKS",
    "ELASTIC_BEANSTALK",
    "ELASTI_CACHE",
    "ELB",
    "ES",
    "KINESIS",
    "LAMBDA",
    "NAT_GATEWAY",
    "NETWORK_ELB",
    "RDS",
    "REDSHIFT",
    "ROUTE_53",
    "S3",
    "SAGE_MAKER",
    "SNS",
    "SQS",
    "STEP_FUNCTIONS",
    "SWF",
]
UpdateResourceCollectionActionType = Literal["ADD", "REMOVE"]
