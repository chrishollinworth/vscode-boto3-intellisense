"""
Type annotations for logs service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/literals.html)

Usage::

    ```python
    from mypy_boto3_logs.literals import AnomalyDetectorStatusType

    data: AnomalyDetectorStatusType = "ANALYZING"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AnomalyDetectorStatusType",
    "DataProtectionStatusType",
    "DeliveryDestinationTypeType",
    "DescribeDeliveriesPaginatorName",
    "DescribeDeliveryDestinationsPaginatorName",
    "DescribeDeliverySourcesPaginatorName",
    "DescribeDestinationsPaginatorName",
    "DescribeExportTasksPaginatorName",
    "DescribeLogGroupsPaginatorName",
    "DescribeLogStreamsPaginatorName",
    "DescribeMetricFiltersPaginatorName",
    "DescribeQueriesPaginatorName",
    "DescribeResourcePoliciesPaginatorName",
    "DescribeSubscriptionFiltersPaginatorName",
    "DistributionType",
    "EvaluationFrequencyType",
    "ExportTaskStatusCodeType",
    "FilterLogEventsPaginatorName",
    "InheritedPropertyType",
    "ListAnomaliesPaginatorName",
    "ListLogAnomalyDetectorsPaginatorName",
    "LogGroupClassType",
    "OrderByType",
    "OutputFormatType",
    "PolicyTypeType",
    "QueryStatusType",
    "ScopeType",
    "StandardUnitType",
    "StateType",
    "SuppressionStateType",
    "SuppressionTypeType",
    "SuppressionUnitType",
)

AnomalyDetectorStatusType = Literal[
    "ANALYZING", "DELETED", "FAILED", "INITIALIZING", "PAUSED", "TRAINING"
]
DataProtectionStatusType = Literal["ACTIVATED", "ARCHIVED", "DELETED", "DISABLED"]
DeliveryDestinationTypeType = Literal["CWL", "FH", "S3"]
DescribeDeliveriesPaginatorName = Literal["describe_deliveries"]
DescribeDeliveryDestinationsPaginatorName = Literal["describe_delivery_destinations"]
DescribeDeliverySourcesPaginatorName = Literal["describe_delivery_sources"]
DescribeDestinationsPaginatorName = Literal["describe_destinations"]
DescribeExportTasksPaginatorName = Literal["describe_export_tasks"]
DescribeLogGroupsPaginatorName = Literal["describe_log_groups"]
DescribeLogStreamsPaginatorName = Literal["describe_log_streams"]
DescribeMetricFiltersPaginatorName = Literal["describe_metric_filters"]
DescribeQueriesPaginatorName = Literal["describe_queries"]
DescribeResourcePoliciesPaginatorName = Literal["describe_resource_policies"]
DescribeSubscriptionFiltersPaginatorName = Literal["describe_subscription_filters"]
DistributionType = Literal["ByLogStream", "Random"]
EvaluationFrequencyType = Literal[
    "FIFTEEN_MIN", "FIVE_MIN", "ONE_HOUR", "ONE_MIN", "TEN_MIN", "THIRTY_MIN"
]
ExportTaskStatusCodeType = Literal[
    "CANCELLED", "COMPLETED", "FAILED", "PENDING", "PENDING_CANCEL", "RUNNING"
]
FilterLogEventsPaginatorName = Literal["filter_log_events"]
InheritedPropertyType = Literal["ACCOUNT_DATA_PROTECTION"]
ListAnomaliesPaginatorName = Literal["list_anomalies"]
ListLogAnomalyDetectorsPaginatorName = Literal["list_log_anomaly_detectors"]
LogGroupClassType = Literal["INFREQUENT_ACCESS", "STANDARD"]
OrderByType = Literal["LastEventTime", "LogStreamName"]
OutputFormatType = Literal["json", "parquet", "plain", "raw", "w3c"]
PolicyTypeType = Literal["DATA_PROTECTION_POLICY"]
QueryStatusType = Literal[
    "Cancelled", "Complete", "Failed", "Running", "Scheduled", "Timeout", "Unknown"
]
ScopeType = Literal["ALL"]
StandardUnitType = Literal[
    "Bits",
    "Bits/Second",
    "Bytes",
    "Bytes/Second",
    "Count",
    "Count/Second",
    "Gigabits",
    "Gigabits/Second",
    "Gigabytes",
    "Gigabytes/Second",
    "Kilobits",
    "Kilobits/Second",
    "Kilobytes",
    "Kilobytes/Second",
    "Megabits",
    "Megabits/Second",
    "Megabytes",
    "Megabytes/Second",
    "Microseconds",
    "Milliseconds",
    "None",
    "Percent",
    "Seconds",
    "Terabits",
    "Terabits/Second",
    "Terabytes",
    "Terabytes/Second",
]
StateType = Literal["Active", "Baseline", "Suppressed"]
SuppressionStateType = Literal["SUPPRESSED", "UNSUPPRESSED"]
SuppressionTypeType = Literal["INFINITE", "LIMITED"]
SuppressionUnitType = Literal["HOURS", "MINUTES", "SECONDS"]
