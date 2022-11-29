"""
Type annotations for cloudwatch service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/literals.html)

Usage::

    ```python
    from mypy_boto3_cloudwatch.literals import ActionsSuppressedByType

    data: ActionsSuppressedByType = "Alarm"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionsSuppressedByType",
    "AlarmExistsWaiterName",
    "AlarmTypeType",
    "AnomalyDetectorStateValueType",
    "AnomalyDetectorTypeType",
    "ComparisonOperatorType",
    "CompositeAlarmExistsWaiterName",
    "DescribeAlarmHistoryPaginatorName",
    "DescribeAlarmsPaginatorName",
    "DescribeAnomalyDetectorsPaginatorName",
    "GetMetricDataPaginatorName",
    "HistoryItemTypeType",
    "ListDashboardsPaginatorName",
    "ListMetricsPaginatorName",
    "MetricStreamOutputFormatType",
    "RecentlyActiveType",
    "ScanByType",
    "StandardUnitType",
    "StateValueType",
    "StatisticType",
    "StatusCodeType",
)

ActionsSuppressedByType = Literal["Alarm", "ExtensionPeriod", "WaitPeriod"]
AlarmExistsWaiterName = Literal["alarm_exists"]
AlarmTypeType = Literal["CompositeAlarm", "MetricAlarm"]
AnomalyDetectorStateValueType = Literal["PENDING_TRAINING", "TRAINED", "TRAINED_INSUFFICIENT_DATA"]
AnomalyDetectorTypeType = Literal["METRIC_MATH", "SINGLE_METRIC"]
ComparisonOperatorType = Literal[
    "GreaterThanOrEqualToThreshold",
    "GreaterThanThreshold",
    "GreaterThanUpperThreshold",
    "LessThanLowerOrGreaterThanUpperThreshold",
    "LessThanLowerThreshold",
    "LessThanOrEqualToThreshold",
    "LessThanThreshold",
]
CompositeAlarmExistsWaiterName = Literal["composite_alarm_exists"]
DescribeAlarmHistoryPaginatorName = Literal["describe_alarm_history"]
DescribeAlarmsPaginatorName = Literal["describe_alarms"]
DescribeAnomalyDetectorsPaginatorName = Literal["describe_anomaly_detectors"]
GetMetricDataPaginatorName = Literal["get_metric_data"]
HistoryItemTypeType = Literal["Action", "ConfigurationUpdate", "StateUpdate"]
ListDashboardsPaginatorName = Literal["list_dashboards"]
ListMetricsPaginatorName = Literal["list_metrics"]
MetricStreamOutputFormatType = Literal["json", "opentelemetry0.7"]
RecentlyActiveType = Literal["PT3H"]
ScanByType = Literal["TimestampAscending", "TimestampDescending"]
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
StateValueType = Literal["ALARM", "INSUFFICIENT_DATA", "OK"]
StatisticType = Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
StatusCodeType = Literal["Complete", "Forbidden", "InternalError", "PartialData"]
